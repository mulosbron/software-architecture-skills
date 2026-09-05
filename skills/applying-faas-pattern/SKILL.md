---
name: applying-faas-pattern
description: Use when building Function-as-a-Service (FaaS) components like AWS Lambda or Google Cloud Functions.
---

# Applying Function-as-a-Service (FaaS)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
FaaS allows you to run custom business logic in response to events (HTTP requests, file uploads, database changes) without provisioning servers.

## Core Pattern
1. Make functions **Stateless**: Do not rely on local memory or disk across invocations. Store state in a BaaS database (e.g., DynamoDB).
2. Make functions **Event-Driven**: Bind the function to a specific trigger.
3. Keep dependencies minimal to reduce cold start times.

## Anti-Pattern to Avoid
Don't build 'God Functions' that route internally to dozens of different business processes. Map one endpoint/event to one focused function.



