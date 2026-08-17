---
name: applying-lsp
description: Use when designing class hierarchies, using inheritance, or when subclasses cause unexpected runtime errors
---

# Applying Liskov Substitution Principle (LSP)

## Overview
"Subtypes must be substitutable for their base types." If a function expects a base class, passing a subclass should not break the program's correctness.

## Core Pattern
- Favor composition or small interfaces over deep inheritance trees.
- If a subclass cannot logically implement a base class method, they should not be in the same inheritance hierarchy.

## Anti-Pattern to Avoid
- A subclass throwing `NotImplementedException` for a base class method (e.g., `EmailOnlyNotification` throwing an error for `SendSms()`).
- Using `if (object is SubClass)` inside code that operates on the Base Class.
