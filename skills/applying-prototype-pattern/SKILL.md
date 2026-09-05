---
name: applying-prototype-pattern
description: Use when creating an object is expensive (DB calls, complex logic), and you want to clone an existing instance instead.
---

# Applying Prototype Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Lets you copy existing objects without making your code dependent on their classes. Reduces the cost of creating new objects.

## Core Pattern
1. Declare a `Prototype` interface with a `clone()` method.
2. A concrete class implements the `clone()` method, copying its own fields to the new object.

## Anti-Pattern to Avoid
Beware of shallow vs. deep copy issues. Don't use Prototype if the object is simple to instantiate with `new`.



