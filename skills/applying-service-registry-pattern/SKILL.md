---
name: applying-service-registry-pattern
description: Use when microservices need to dynamically discover the IP addresses and ports of other services.
---

# Applying Service Registry Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
In cloud environments, service IPs change dynamically. A Service Registry acts as a central phonebook where services register themselves and look up others.

## Core Pattern
1. Deploy a Service Registry (e.g., Eureka, Consul).
2. Services register their network location upon startup.
3. Client services query the registry to find the target service before making an HTTP/gRPC call.

## Anti-Pattern to Avoid
Don't hardcode IP addresses in configuration files in a microservices environment.



