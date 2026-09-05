---
name: applying-chain-of-responsibility-pattern
description: Use when a request can be handled by multiple objects, and the handler isn't known a priori (e.g., Middleware, Event bubbling).
---

# Applying Chain of Responsibility Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Passes requests along a chain of handlers. Upon receiving a request, each handler decides either to process it or to pass it to the next handler.

## Core Pattern
1. Declare a Handler interface/abstract class with a `setNext()` method and a `handle()` method.
2. Concrete Handlers implement processing logic or delegate to `next`.
3. Client builds the chain and sends the request to the first handler.

## Anti-Pattern to Avoid
Don't hardcode handler sequences in business logic. Avoid chains where a request drops off the end silently by mistake.



