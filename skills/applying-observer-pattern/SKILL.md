---
name: applying-observer-pattern
description: Use when changes to the state of one object require changing other objects, and the set of objects is unknown or dynamic (Pub-Sub).
---

# Applying Observer Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.

## Core Pattern
1. Subject maintains a list of Observers and methods to add/remove them.
2. Subject calls `notify()` when state changes.
3. Concrete Observers implement `update()` to react to the Subject.

## Anti-Pattern to Avoid
Avoid tight coupling between the event source and listeners. Watch out for memory leaks if Observers aren't unregistered (Lapsed Listener Problem).



