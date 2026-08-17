---
name: choosing-monolithic-architecture
description: Use when starting a new project, building an MVP, or deciding if microservices are premature.
---

# Choosing Monolithic Architecture

## Overview
Monoliths are not an anti-pattern. They are the most efficient starting point for most projects due to their simplicity in development, deployment, and testing.

## Core Pattern
Choose a Monolithic Architecture when:
- The project is an MVP (Minimum Viable Product) aiming for rapid time-to-market.
- The domain and business boundaries are not yet clearly understood.
- The team size is small.
- Network latency between components needs to be avoided (in-memory calls are faster).

## Anti-Pattern to Avoid
Don't use a monolith if different parts of the system require wildly different scaling (e.g., heavy video processing vs simple text serving). Avoid 'Technology Stack Lock-in' if you foresee needing multiple languages.
