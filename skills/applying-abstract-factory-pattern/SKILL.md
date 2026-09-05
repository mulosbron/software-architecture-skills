---
name: applying-abstract-factory-pattern
description: Use when the business logic needs to work with different families of related products without depending on their concrete classes (e.g., UI Themes).
---

# Applying Abstract Factory Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Lets you produce families of related objects without specifying their concrete classes. Ensures products from the same family are compatible.

## Core Pattern
1. Declare abstract interfaces for each distinct product of the product family.
2. Declare the Abstract Factory interface with creation methods for each abstract product.
3. Create Concrete Factory classes for each product family variation.

## Anti-Pattern to Avoid
Don't use it if you only have one family of products or products aren't related. It adds unnecessary complexity.



