---
name: evaluating-microservices-readiness
description: Use when the user wants to start a project with microservices or split a monolith. Push back first; default to a modular monolith.
---

# Evaluating Microservices Readiness

**Stance:** This repo's position is that microservices solve organizational scaling, not code problems. Do not help build them until the user has passed the gate below.

## Gate (ask before designing anything)
1. How many independent teams will own services? Fewer than 3 → modular monolith.
2. Is there a measured load or availability problem today? No numbers → modular monolith.
3. Is a platform already in place (CI, container runtime, tracing, on-call)? No → modular monolith.

If the user still insists, proceed, state that you recommended against it, and record it:
`python tools/arch_tools.py adr-new "Adopt microservices"`.

## Boundaries
- Migration from an existing monolith is incremental (strangler fig), never a rewrite.
- A distributed monolith (services that must deploy together or share a database) is a hard fail. Flag it.

## Done when
The user has written answers to the three gate questions and an ADR for the outcome.
