---
name: applying-circuit-breaker-pattern
description: Use when a microservice calls another service and you need to prevent cascading failures if the target service goes down.
---

# Applying Circuit Breaker Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Prevents a network or service failure from cascading to other services. It stops sending requests to a failing service and returns a fallback response immediately.

## Core Pattern
1. Wrap the inter-service call in a Circuit Breaker.
2. **Closed State**: Normal operation.
3. **Open State**: If failure threshold is reached, block calls and return fallback instantly.
4. **Half-Open State**: After a timeout, allow one test request to see if the service recovered.

## Anti-Pattern to Avoid
Don't rely solely on HTTP timeouts. A slow service will exhaust thread pools; a Circuit Breaker fails fast.



