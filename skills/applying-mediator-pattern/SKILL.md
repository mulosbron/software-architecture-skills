---
name: applying-mediator-pattern
description: Use when a set of objects communicate in complex, chaotic ways, and you want to centralize communication.
---

# Applying Mediator Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Reduces chaotic dependencies between objects. Restricts direct communications and forces them to collaborate only via a mediator object.

## Core Pattern
1. Declare a Mediator interface.
2. Colleague classes hold a reference to the Mediator and notify it of state changes.
3. Concrete Mediator receives notifications and coordinates other colleagues.

## Anti-Pattern to Avoid
Don't let colleagues communicate directly (Spaghetti code). Beware of the Mediator becoming a God Class.



