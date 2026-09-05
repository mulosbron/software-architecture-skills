---
name: applying-state-pattern
description: Use when an object's behavior depends on its state, and it must change its behavior at runtime (State Machine).
---

# Applying State Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Core Pattern
1. Context holds a reference to a State interface.
2. Concrete States implement state-specific behaviors.
3. Context delegates method calls to the current State object. State transitions replace the Context's State reference.

## Anti-Pattern to Avoid
Don't use massive `switch-case` statements in the Context. Encapsulate each state in a class.



