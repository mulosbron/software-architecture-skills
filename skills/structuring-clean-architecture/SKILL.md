---
name: structuring-clean-architecture
description: Use when separating domain logic from frameworks, ORMs, and transport layers using Clean or Hexagonal (ports-and-adapters) architecture.
---

# Structuring Clean Architecture

## Goal
Keep core business rules independent of web frameworks, databases, and external SDKs without over-abstracting simple CRUD paths.

## Repo defaults
- **Hexagonal inside complex modules only.** Pair Clean/Hexagonal ports-and-adapters with `designing-modular-monoliths` for modules with non-trivial business rules; keep pure CRUD modules flat.
- **Inward dependency rule.** Domain and application layers define port interfaces; infrastructure and transport adapters depend inward on ports, never the reverse.
- **Verify boundaries continuously.** Run `python tools/arch_tools.py check-module-boundaries <src-dir>` on changes.

## Boundaries
- Domain layer must have zero imports from HTTP frameworks, ORMs, queues, or cloud SDKs.
- Do not add pass-through service/repository interfaces around trivial single-table CRUD.
- Use infrastructure durable execution or transactional outbox for crash-safe workflows.

## Done when
- Layer direction and port/adapter ownership are explicit per module.
- Core domain tests run in-memory without starting a database or HTTP server.
- `check-module-boundaries` passes with no inward dependency violations.
