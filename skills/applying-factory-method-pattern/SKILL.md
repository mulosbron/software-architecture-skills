---
name: applying-factory-method-pattern
description: Use when a class can't anticipate the class of objects it must create, delegating instantiation to subclasses.
---

# Applying Factory Method Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

## Core Pattern
1. Declare a common product interface.
2. Create a Creator class with an abstract or default `createProduct()` factory method.
3. Subclasses override the factory method to return specific concrete products.

## Anti-Pattern to Avoid
Avoid creating a massive factory class with huge `if/else` or `switch` statements. Do not use Factory when simple instantiation (`new`) suffices.



