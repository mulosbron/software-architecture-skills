---
name: applying-bulkhead-pattern
description: Use when you need to isolate resources (like thread pools) so a failure in one part of the system doesn't take down the rest.
---

# Applying Bulkhead Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Partitions application resources into isolated pools so that if one pool is exhausted (e.g., due to a slow dependency), the others remain unaffected.

## Core Pattern
1. Identify critical vs non-critical dependencies.
2. Assign separate thread pools or connection limits to different external calls.
3. If Service A gets slow, only its dedicated thread pool fills up, leaving threads available for Service B.

## Anti-Pattern to Avoid
Don't use a single global thread pool for all outgoing network calls in a microservice.



