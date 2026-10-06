---
name: deploying-with-containers
description: Use when containerizing a service, writing Kubernetes manifests, or setting up a pipeline with zero-downtime rollout.
---

# Deploying with Containers

**Goal:** Every service ships the same way: multi-stage Dockerfile, Kubernetes Deployment + Service with probes and limits, rolled out progressively.

## How this repo does it
```bash
python tools/devops_tools.py init-docker                       # detects stack: node, python, go, java
python tools/devops_tools.py init-k8s order-service --replicas 3
python tools/devops_tools.py init-pipeline --provider github   # or gitlab
```
The scaffolds are starting points. Fill the placeholders they print.

## Rules
- Images are tagged by git SHA. `latest` is for local dev only.
- Every Deployment has readiness and liveness probes and CPU/memory limits. The scaffold includes them; do not remove them.
- RollingUpdate by default. Blue/green or canary only when the user has a traffic router (ingress controller or mesh) that supports it. Ask before assuming.
- Secrets come from the platform's secret store, never from the image or the repo.

## Done when
Dockerfile builds, manifests apply cleanly, pipeline runs test → build → push → deploy, and rollback is one command the user can name.
