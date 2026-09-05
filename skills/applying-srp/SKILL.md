---
name: applying-srp
description: Use when designing a new class or reviewing an existing class to ensure it only has one reason to change
---

# Applying Single Responsibility Principle (SRP)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
"A class should have one, and only one, reason to change." SRP is about high cohesion and low coupling. A class should serve a single actor or responsibility area.

## Core Pattern
Divide responsibilities across layers:
1. **Data Access (Repository)**: Handles only database queries (e.g., `DbContext`).
2. **Business Logic (Service)**: Handles business rules (e.g., checking stock).
3. **Presentation/API (Controller)**: Handles formatting (JSON) and HTTP routing.

## Anti-Pattern to Avoid
Do not mix data access, business logic, and presentation in a single class (e.g., a `BookService` that fetches from DB, checks stock, and serializes to JSON).



