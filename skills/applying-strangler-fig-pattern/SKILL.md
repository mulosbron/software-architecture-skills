---
name: applying-strangler-fig-pattern
description: Use when migrating a legacy Monolith to Microservices incrementally without a risky 'Big Bang' rewrite.
---

# Applying Strangler Fig Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Gradually replaces a legacy system by wrapping it with a proxy and intercepting requests, routing them either to the new microservice or the old monolith.

## Core Pattern
1. Put an API Gateway or Proxy in front of the Monolith.
2. Extract one domain into a new Microservice.
3. Update the Gateway to route requests for that domain to the new service, while the rest goes to the Monolith.
4. Repeat until the Monolith is entirely replaced.

## Anti-Pattern to Avoid
Never attempt a 'Big Bang' rewrite of a massive monolith. Always migrate incrementally.



