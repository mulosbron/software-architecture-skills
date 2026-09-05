---
name: applying-strategy-pattern
description: Use when you have multiple algorithms for a specific task and want to switch between them at runtime.
---

# Applying Strategy Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

## Core Pattern
1. Define a Strategy interface for the algorithm.
2. Create Concrete Strategies.
3. The Context uses a Strategy via the interface.
4. The Client selects and passes the appropriate Strategy to the Context.

## Anti-Pattern to Avoid
Don't hardcode algorithms inside the Context. Extract them so they can vary independently.



