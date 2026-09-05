---
name: verifying-solid-compliance
description: Use when asked to review existing code, check if a project complies with SOLID principles, or identify architectural smells
---

# Verifying SOLID Compliance

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Before refactoring or adding new features, it is critical to verify if the existing codebase adheres to SOLID principles. This skill provides a checklist to identify violations without rewriting the project from scratch.

## Verification Checklist

### 1. Check SRP (Single Responsibility)
- **Look for**: Classes with "Manager", "Processor", or "System" in their names.
- **Red Flags**: A single class handling database access, business logic, and presentation/logging simultaneously.
- **Question**: Does this class have more than one reason to change?

### 2. Check OCP (Open/Closed)
- **Look for**: Long `if-else` or `switch` statements checking object types or enums (e.g., `PaymentMethod == "CreditCard"`).
- **Red Flags**: Modifying existing, tested classes to add a new variation of a feature.
- **Question**: Can I add a new feature (like a new payment type) just by adding a new class?

### 3. Check LSP (Liskov Substitution)
- **Look for**: Subclasses throwing `NotImplementedException` or `NotSupportedException`.
- **Red Flags**: Methods in a subclass that leave the base class's contract unfulfilled.
- **Question**: If I replace the base class with this subclass, will the program crash?

### 4. Check ISP (Interface Segregation)
- **Look for**: "Fat" interfaces with many methods.
- **Red Flags**: Classes implementing interfaces where many methods are left empty or throw exceptions.
- **Question**: Is the client forced to depend on methods it doesn't use?

### 5. Check DIP (Dependency Inversion)
- **Look for**: The `new` keyword used inside business logic to instantiate low-level services (e.g., `new SmtpEmailService()`).
- **Red Flags**: High-level modules depending directly on low-level concrete classes.
- **Question**: Are dependencies injected via constructor using abstractions (interfaces)?



