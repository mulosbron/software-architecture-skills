---
name: selecting-design-patterns
description: Use when deciding which design pattern to apply to solve a specific architectural or coding problem
---

# Selecting Design Patterns

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Design patterns provide tested, proven solutions to recurring software design problems. Choosing the right pattern is critical for maintainability and flexibility. This skill helps map common problems to the appropriate GoF pattern.

## Core Pattern

### 1. Object Creation Problems (Creational)
- **Single global instance**: `Singleton`
- **Delegate creation to subclasses**: `Factory Method`
- **Families of related objects**: `Abstract Factory`
- **Step-by-step complex creation**: `Builder`
- **Clone expensive objects**: `Prototype`

### 2. Structure Problems (Structural)
- **Incompatible interfaces**: `Adapter`
- **Separate abstraction from implementation**: `Bridge`
- **Tree structures**: `Composite`
- **Dynamic responsibilities**: `Decorator`
- **Simplified interface to subsystem**: `Facade`
- **Access control/Lazy loading**: `Proxy`
- **Memory optimization for many objects**: `Flyweight`

### 3. Behavior Problems (Behavioral)
- **Request pipeline**: `Chain of Responsibility`
- **Undo/Queuing (Object request)**: `Command`
- **Language grammar**: `Interpreter`
- **Centralized communication**: `Mediator`
- **Save/Restore state**: `Memento`
- **Publish/Subscribe**: `Observer`
- **State Machine**: `State`
- **Interchangeable algorithms**: `Strategy`
- **Algorithm skeleton**: `Template Method`
- **Operations on object structures**: `Visitor`

## Anti-Pattern to Avoid
Do not apply design patterns indiscriminately (Patternitis). Use them only when a clear problem exists that the pattern solves.



