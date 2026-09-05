---
name: applying-visitor-pattern
description: Use when you need to perform an operation on elements of an object structure without changing the classes on which it operates.
---

# Applying Visitor Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Separates algorithms from the objects on which they operate. Uses double dispatch.

## Core Pattern
1. Define a Visitor interface with `visit(Element)` methods.
2. Elements implement an `accept(Visitor)` method that calls `visitor.visit(this)`.
3. Concrete Visitors implement operations for each Element type.

## Anti-Pattern to Avoid
Don't pollute Element classes with distinct logic (e.g., ExportToPdf, ExportToXml). Keep Elements clean and move logic to Visitors.



