"""DevOps scaffolds: Dockerfile (stack-detected), Kubernetes manifests with probes/limits, CI pipeline."""
import argparse
import os
import sys

DOCKERFILES = {
    "node": """# syntax=docker/dockerfile:1
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE {port}
CMD ["node", "dist/index.js"]
""",
    "python": """# syntax=docker/dockerfile:1
FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=build /install /usr/local
COPY . .
RUN useradd -m app && chown -R app /app
USER app
EXPOSE {port}
CMD ["python", "-m", "app"]
""",
    "go": """# syntax=docker/dockerfile:1
FROM golang:1.22 AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /out/app ./...

FROM gcr.io/distroless/static-debian12
COPY --from=build /out/app /app
EXPOSE {port}
ENTRYPOINT ["/app"]
""",
    "java": """# syntax=docker/dockerfile:1
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -q dependency:go-offline
COPY src ./src
RUN mvn -q clean package -DskipTests

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
USER 1000
EXPOSE {port}
ENTRYPOINT ["java", "-jar", "app.jar"]
""",
}

K8S = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
  labels:
    app: {name}
spec:
  replicas: {replicas}
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0
      maxSurge: 1
  selector:
    matchLabels:
      app: {name}
  template:
    metadata:
      labels:
        app: {name}
    spec:
      containers:
        - name: {name}
          image: REGISTRY/{name}:GIT_SHA   # never :latest outside local dev
          ports:
            - containerPort: {port}
          readinessProbe:
            httpGet:
              path: /health/ready
              port: {port}
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /health/live
              port: {port}
            initialDelaySeconds: 15
            periodSeconds: 20
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
          envFrom:
            - secretRef:
                name: {name}-secrets   # created from the platform secret store, not committed
---
apiVersion: v1
kind: Service
metadata:
  name: {name}
spec:
  selector:
    app: {name}
  ports:
    - port: 80
      targetPort: {port}
  type: ClusterIP
"""

PIPELINES = {
    "github": """name: ci
on:
  push:
    branches: [main]
  pull_request:

env:
  IMAGE: ghcr.io/${{{{ github.repository }}}}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "TODO: install deps and run tests"

  build-push:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{{{ github.actor }}}}
          password: ${{{{ secrets.GITHUB_TOKEN }}}}
      - uses: docker/build-push-action@v6
        with:
          push: true
          tags: ${{{{ env.IMAGE }}}}:${{{{ github.sha }}}}

  deploy:
    needs: build-push
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: |
          sed -i "s|REGISTRY/.*:GIT_SHA|${{{{ env.IMAGE }}}}:${{{{ github.sha }}}}|" k8s/*.yaml
          echo "TODO: kubectl apply -f k8s/ (configure cluster credentials first)"
          echo "Rollback: kubectl rollout undo deployment/<name>"
""",
    "gitlab": """stages: [test, build, deploy]

variables:
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - echo "TODO: install deps and run tests"

build:
  stage: build
  image: docker:24
  services: [docker:24-dind]
  only: [main]
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE .
    - docker push $IMAGE

deploy:
  stage: deploy
  only: [main]
  environment: production
  script:
    - sed -i "s|REGISTRY/.*:GIT_SHA|$IMAGE|" k8s/*.yaml
    - echo "TODO: kubectl apply -f k8s/ (configure cluster credentials first)"
    - echo "Rollback: kubectl rollout undo deployment/<name>"
""",
}

PIPELINE_PATHS = {"github": os.path.join(".github", "workflows", "ci.yml"), "gitlab": ".gitlab-ci.yml"}


def detect_stack():
    if os.path.exists("package.json"):
        return "node"
    if os.path.exists("go.mod"):
        return "go"
    if os.path.exists("pom.xml"):
        return "java"
    if any(os.path.exists(f) for f in ("requirements.txt", "pyproject.toml")):
        return "python"
    return None


def _write(path, content, force):
    if os.path.exists(path) and not force:
        sys.exit(f"[ERR] {path} exists. Use --force to overwrite.")
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"[OK] {path}")


def init_docker(args):
    stack = args.stack or detect_stack()
    if not stack:
        sys.exit("[ERR] Could not detect stack. Pass --stack node|python|go|java")
    _write("Dockerfile", DOCKERFILES[stack].format(port=args.port), args.force)
    print(f"     stack={stack}. Check the build command and entrypoint match your project.")


def init_k8s(args):
    _write(os.path.join("k8s", f"{args.name}.yaml"), K8S.format(name=args.name, replicas=args.replicas, port=args.port), args.force)
    print("     Replace REGISTRY, implement /health/ready and /health/live, tune resource limits.")


def init_pipeline(args):
    _write(PIPELINE_PATHS[args.provider], PIPELINES[args.provider], args.force)
    print("     Fill the TODO test step and cluster credentials.")


def main():
    p = argparse.ArgumentParser(description="DevOps scaffolding")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("init-docker", help="Multi-stage Dockerfile for the detected stack")
    s.add_argument("--stack", choices=list(DOCKERFILES))
    s.add_argument("--port", type=int, default=8080)
    s.add_argument("--force", action="store_true")
    s.set_defaults(func=init_docker)

    s = sub.add_parser("init-k8s", help="Deployment + Service with probes and limits")
    s.add_argument("name")
    s.add_argument("--replicas", type=int, default=3)
    s.add_argument("--port", type=int, default=8080)
    s.add_argument("--force", action="store_true")
    s.set_defaults(func=init_k8s)

    s = sub.add_parser("init-pipeline", help="CI pipeline: test -> build -> push -> deploy")
    s.add_argument("--provider", choices=list(PIPELINES), default="github")
    s.add_argument("--force", action="store_true")
    s.set_defaults(func=init_pipeline)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
