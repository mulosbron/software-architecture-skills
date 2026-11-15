---
name: designing-cqrs-and-event-sourcing
description: Use when separating read/write models (CQRS), designing append-only event streams, building projections, or orchestrating distributed sagas.
---

# Designing CQRS and Event Sourcing

## Goal
Keep state modeling as simple as possible while isolating read/write scaling, temporal auditability, and multi-step compensating workflows where justified.

## Repo defaults
- **Single relational model is the default.** Challenge CQRS and Event Sourcing first; adopt only with measured read/write divergence or strict audit/temporal replay requirements.
- **Immutable versioned events.** Append-only streams with schema versioning, correlation IDs, and snapshots; build read projections asynchronously via `choosing-message-broker`.
- **Orchestration for complex sagas.** Prefer explicit state-machine orchestration over ad-hoc choreography for >3 steps, pairing compensating actions with `designing-idempotent-mutations`.

## Boundaries
- Never mutate or delete production events; emit compensating events and schema upcasters.
- Never rebuild projections directly against production read tables without staging and verification.
- Record CQRS/ES adoption and broker/projection choices via `python tools/arch_tools.py adr-new`.

## Done when
- Command/query separation and event-sourcing justification are recorded in an ADR.
- Event schemas, snapshotting, idempotent handlers, and projection rebuild steps are defined.
- Saga state transitions and per-step compensations handle partial failures and retries.
