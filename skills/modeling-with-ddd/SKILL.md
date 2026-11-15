---
name: modeling-with-ddd
description: Use when a domain has complex rules, colliding team terminology, or unclear service or module boundaries needing Domain-Driven Design.
---

# Modeling with DDD

## Goal
Apply strategic and tactical DDD only where business complexity justifies it, aligning module boundaries with subdomains and domain invariants.

## Repo defaults
- **Viability check first.** Adopt full DDD only when >=2 apply: fast-changing rules, colliding team terms, unstable contracts, or strict audit invariants; otherwise use `designing-modular-monoliths`.
- **Strategic before tactical.** Classify core/supporting/generic subdomains, map bounded contexts, and define an Anti-Corruption Layer (ACL) at upstream boundaries before writing aggregates.
- **Aggregate = transaction boundary.** Enforce invariants inside aggregate methods with immutable value objects; repositories load and save aggregate roots only.

## Boundaries
- No cross-aggregate synchronous writes in a single transaction; use domain events.
- Never leak ORM models into domain entities or push domain rules into controllers.
- Record every bounded-context split or ACL decision via `python tools/arch_tools.py adr-new`.

## Done when
- Subdomain classification, context map (upstream/downstream + ACL), and glossary exist.
- Aggregates, value objects, domain events, and repository boundaries are explicit.
- Boundary choices have corresponding ADRs in `docs/adrs/`.
