---
name: balancing-architectural-tradeoffs
description: Use when choosing an architectural style, resolving conflicting non-functional requirements, or transitioning a project across growth phases
---

# Balancing Architectural Tradeoffs

## Overview
Architecture is about making trade-offs between conflicting Business Goals and Architectural Drivers (Quality Attributes). A perfect architecture does not exist; only the most "fit-for-purpose" one does.

## Core Pattern: Phase-Based Design

### Startup Phase (Minimum Viable Product)
- **Primary Business Goal**: Time-to-Market, validation of idea.
- **Primary Architectural Driver**: Speed of development, simplicity, low cost.
- **Architectural Choice**: **Monolithic Architecture**.
- **Trade-off**: Sacrificing long-term scalability and strict modularity for rapid delivery.

### Growth Phase
- **Primary Business Goal**: Handle millions of users, ensure 99.99% uptime.
- **Primary Architectural Driver**: Scalability, Reliability, Team Autonomy.
- **Architectural Choice**: **Microservices Architecture**.
- **Trade-off**: Sacrificing simplicity and operational ease. Absorbing the high complexity of distributed systems (Event-driven communication, Kubernetes) to achieve scale.

## Conway's Law
Always consider the organizational structure. "Organizations design systems that mirror their own communication structure."
- Small, single team -> Monolith.
- Multiple autonomous squads -> Microservices.
Do not force an architecture that conflicts with the team structure.

## Red Flags - STOP and Re-evaluate
- Trying to build a highly scalable microservices architecture for an unproven MVP with 3 developers (Over-engineering).
- Keeping a massive monolith when 10 different teams are stepping on each other's toes (Under-engineering).
