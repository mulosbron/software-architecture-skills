---
name: refactoring-big-ball-of-mud
description: Use when you encounter a massive 'God Class' controller or service that handles routing, business logic, and database access all in one place.
---

# Refactoring Big Ball of Mud

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Extracts responsibilities from a tangled, tightly-coupled monolithic class into distinct, testable layers (N-Tier) using Separation of Concerns.

## Core Pattern
1. Identify the Presentation, Business, and Data Access responsibilities in the tangled code.
2. Create a Data Access interface (Repository) and move DB logic there.
3. Create a Business Logic interface (Service) and move business rules there, injecting the Repository.
4. Clean the Presentation layer (Controller) to only handle HTTP routing and inject the Service.

## Anti-Pattern to Avoid
Do not leave database dependencies (`new DbContext()`) inside the Controller. Do not skip Dependency Injection (DI).



