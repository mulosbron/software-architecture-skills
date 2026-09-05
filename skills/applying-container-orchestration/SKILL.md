---
name: applying-container-orchestration
description: Use when deploying and managing hundreds or thousands of containerized microservices in production.
---

# Applying Container Orchestration (Kubernetes)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
While Docker packages a single application into a portable container, a Container Orchestrator (like Kubernetes) manages clusters of these containers, ensuring high availability, scaling, and networking.

## Core Pattern
1. **Desired State**: Declare the desired state (e.g., "I need 3 replicas of the Author Service running").
2. **Control Loop**: The orchestrator constantly monitors the actual state. If a server crashes and a container dies, it automatically spins up a replacement on a healthy node (Self-healing).
3. **Service Discovery**: Containers are assigned dynamic IPs. The orchestrator provides an internal DNS/Load Balancer so services can reliably find each other.

## Anti-Pattern to Avoid
Don't run raw Docker containers manually via `docker run` on production servers. You will lose automatic failover, scaling, and rolling updates.



