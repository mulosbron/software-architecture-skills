---
name: applying-singleton-pattern
description: Use when you need to ensure a class has only one instance, while providing a global access point to this instance (e.g., Configuration Managers, DB Connections).
---

# Applying Singleton Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
"A class should have only one instance and provide a global point of access to it." This is useful for managing shared resources.

## Core Pattern
1. Make the default constructor private.
2. Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field.
3. All following calls to this method return the cached object.

## Anti-Pattern to Avoid
Avoid using Singleton just to provide a global variable. Be cautious of Thread Safety issues in multi-threaded environments. Prefer Dependency Injection (DI) frameworks to manage singleton lifecycles.



