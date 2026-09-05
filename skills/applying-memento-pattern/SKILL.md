---
name: applying-memento-pattern
description: Use when you need to save and restore an object's state (Undo/Rollback) without violating its encapsulation.
---

# Applying Memento Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Captures and externalizes an object's internal state so that the object can be restored to this state later.

## Core Pattern
1. Originator creates a Memento containing a snapshot of its state.
2. Memento restricts access to its data from everyone except the Originator.
3. Caretaker stores the Memento but never modifies it.

## Anti-Pattern to Avoid
Don't expose the Originator's internal fields publicly just to save state. Use Memento to preserve encapsulation.



