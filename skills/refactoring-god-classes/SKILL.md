---
name: refactoring-god-classes
description: Use when breaking down a massive, tightly-coupled class (God Class) into smaller, manageable, SOLID-compliant components
---

# Refactoring God Classes

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
A "God Class" is an anti-pattern where a single class controls too many processes (SRP violation), depends on concrete implementations (DIP violation), and uses hardcoded branching (OCP violation). Refactoring it requires a systematic approach.

## Refactoring Steps

### Step 1: Isolate Responsibilities (SRP)
- Identify distinct domains (e.g., Database, Payment, Notification, Logging).
- Extract each domain into its own interface (e.g., `IOrderRepository`, `IPaymentProcessor`).

### Step 2: Implement Strategy Pattern (OCP)
- Remove hardcoded `if-else` blocks for varying behaviors (e.g., Discount calculation, Payment methods).
- Create a common interface (`IPaymentStrategy`) and implement concrete strategy classes.

### Step 3: Segregate Interfaces (ISP)
- Ensure the newly created interfaces are small and focused.
- Do not group unrelated methods (e.g., `SaveOrder` and `SendEmail`) into the same interface.

### Step 4: Invert Dependencies (DIP)
- Remove all `new` keywords for services inside the God Class.
- Inject the isolated interfaces via the constructor (Dependency Injection).
- The former God Class becomes a lightweight orchestrator/coordinator.



