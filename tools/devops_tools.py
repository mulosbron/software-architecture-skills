import argparse
import os

def scaffold_docker(args):
    content = """# Multi-stage Dockerfile
FROM maven:3.8-openjdk-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package -DskipTests

FROM openjdk:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
"""
    with open("Dockerfile", "w", encoding="utf-8") as f:
        f.write(content)
    print("[SUCCESS] Scaffoled Dockerfile")

def scaffold_k8s(args):
    content = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {args.name}-deployment
spec:
  replicas: {args.replicas}
  selector:
    matchLabels:
      app: {args.name}
  template:
    metadata:
      labels:
        app: {args.name}
    spec:
      containers:
      - name: {args.name}
        image: {args.name}:latest
        ports:
        - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: {args.name}-service
spec:
  selector:
    app: {args.name}
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
"""
    os.makedirs("k8s", exist_ok=True)
    with open(f"k8s/{args.name}.yaml", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] Scaffoled Kubernetes manifests at k8s/{args.name}.yaml")

def main():
    parser = argparse.ArgumentParser(description="DevOps & CI/CD Scaffolding Tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    docker_parser = subparsers.add_parser("init-docker", help="Initialize a multi-stage Java/Maven Dockerfile")
    docker_parser.set_defaults(func=scaffold_docker)

    k8s_parser = subparsers.add_parser("init-k8s", help="Initialize Kubernetes Deployment & Service manifests")
    k8s_parser.add_argument("name", type=str, help="Name of the service (e.g. order-service)")
    k8s_parser.add_argument("--replicas", type=int, default=3, help="Number of replicas (default: 3)")
    k8s_parser.set_defaults(func=scaffold_k8s)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
