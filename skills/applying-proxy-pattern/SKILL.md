---
name: applying-proxy-pattern
description: Use when you need to control access to an object (security, lazy loading, caching) without modifying its code.
---

# Applying Proxy Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Provides a surrogate or placeholder for another object to control access to it.

## Core Pattern
1. Create a Subject interface.
2. The RealSubject implements business logic.
3. The Proxy implements the Subject interface, holding a reference to the RealSubject. The Proxy performs its check/cache/loading before delegating to the RealSubject.

## Anti-Pattern to Avoid
Don't put heavy initialization in constructors. Use Virtual Proxy to delay creation. Don't mix Proxy and Decorator intents.



