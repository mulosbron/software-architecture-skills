---
name: applying-dip
description: Use when connecting high-level business logic to low-level infrastructure, or when implementing dependency injection
---

# Applying Dependency Inversion Principle (DIP)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
"High-level modules should not depend on low-level modules. Both should depend on abstractions." This eliminates tight coupling and makes the system testable.

## Core Pattern: Dependency Injection
1. Define abstractions (interfaces) for low-level operations (e.g., `ILogger`).
2. Low-level modules implement the abstraction (`FileLogger : ILogger`).
3. High-level modules request the abstraction via their constructor (Constructor Injection).
4. An IoC/DI Container wires them together at runtime.

## Anti-Pattern to Avoid
High-level classes instantiating low-level classes directly using the `new` keyword (e.g., `var emailService = new SmtpEmailService()`).



