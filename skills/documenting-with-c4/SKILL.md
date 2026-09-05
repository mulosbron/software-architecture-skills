---
name: documenting-with-c4
description: Use when documenting system architecture, explaining system components to stakeholders, or visualizing boundaries between systems
---

# Documenting with C4 Model

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
The C4 model is a hierarchical approach to software architecture documentation. It uses a zoom-in/zoom-out metaphor to explain the system at different levels of detail for different audiences.

## The 4 Levels

### 1. Context (Level 1)
- **Audience**: All stakeholders (Business, PMs, non-technical).
- **Focus**: The big picture. Shows the main system as a single box surrounded by users (actors) and external systems (APIs, email services).
- **Goal**: Define system boundaries and scope.

### 2. Container (Level 2)
- **Audience**: Architects, Technical Leads, Developers.
- **Focus**: The separately deployable units (e.g., Web App, Mobile App, API Backend, Database).
- **Goal**: Show high-level technology choices and how containers communicate (e.g., HTTPS/JSON).

### 3. Component (Level 3)
- **Audience**: Developers.
- **Focus**: The internal building blocks of a single Container (e.g., Controllers, Services, Repositories).
- **Goal**: Show structural organization, business logic distribution, and database abstraction.

### 4. Code (Level 4)
- **Audience**: Developers.
- **Focus**: UML class diagrams showing properties, methods, and relationships.
- **Goal**: Deep dive into complex components (only when strictly necessary).

## Common Mistakes
- **Mixing levels**: Do not put classes in a Context diagram. Keep the abstraction strict.
- **Confusing Container with Docker**: In C4, a "Container" is a deployable application or data store, not specifically a Docker container.



