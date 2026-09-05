---
name: designing-modular-monoliths
description: Use when structuring a new monolithic application to prevent it from becoming a tangled mess, or when preparing for a future microservices migration.
---

# Designing Modular Monoliths

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
A Modular Monolith logically separates the codebase into distinct functional modules (business capabilities) with high internal cohesion and loose coupling, while still deploying as a single unit.

## Core Pattern
1. Identify distinct business domains (e.g., Catalog, Orders, Users).
2. Create separate logical modules for each domain.
3. Enforce strict boundaries between modules using interfaces; modules must not directly access each other's databases.
4. Deploy everything together as a single executable or package.

## Anti-Pattern to Avoid
Avoid the 'Distributed Monolith' (modules running on separate servers but tightly coupled). Avoid the 'Big Ball of Mud' (no module boundaries).



