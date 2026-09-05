---
name: applying-n-tier-architecture
description: Use when structuring an application into logical layers to separate user interface, business rules, and database access.
---

# Applying N-Tier (Layered) Architecture

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
N-Tier architecture separates the application into horizontal layers, isolating concerns to improve testability and maintainability. The most common is the 3-Tier architecture.

## Core Pattern
1. **Presentation Layer**: Handles HTTP requests, UI, and input validation.
2. **Business Logic Layer (BLL)**: Contains core business rules. Independent of UI and specific DB technologies.
3. **Data Access Layer (DAL)**: Handles CRUD operations and database communication.

**Rule**: Dependencies must flow downwards. Presentation -> BLL -> DAL.

## Anti-Pattern to Avoid
Never allow the Data Access Layer to call the Business Logic Layer. Never put database SQL queries or business rules inside the Presentation (Controller) Layer.



