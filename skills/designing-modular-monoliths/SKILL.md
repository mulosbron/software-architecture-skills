---
name: designing-modular-monoliths
description: Use when structuring a new monolithic application to prevent it from becoming a tangled mess, or when preparing for a future microservices migration.
---

# Designing Modular Monoliths

## Overview
A Modular Monolith logically separates the codebase into distinct functional modules (business capabilities) with high internal cohesion and loose coupling, while still deploying as a single unit.

## Core Pattern
1. Identify distinct business domains (e.g., Catalog, Orders, Users).
2. Create separate logical modules for each domain.
3. Enforce strict boundaries between modules using interfaces; modules must not directly access each other's databases.
4. Deploy everything together as a single executable or package.

## Anti-Pattern to Avoid
Avoid the 'Distributed Monolith' (modules running on separate servers but tightly coupled). Avoid the 'Big Ball of Mud' (no module boundaries).
