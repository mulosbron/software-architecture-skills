---
name: designing-idempotent-mutations
description: Use when designing payment, booking, inventory, or cross-service mutating workflows that require idempotency, concurrency control, or failure recovery.
---

# Designing Idempotent Mutations

**Goal:** Every mutating workflow executes at-most-once per client intent and recovers deterministically on partial failure.

## Defaults this repo takes
- **Idempotency:** Require an `Idempotency-Key` (client UUID) enforced by a unique DB constraint; return the stored outcome on retry instead of re-executing.
- **Concurrency:** Optimistic locking (`version` column + DB `CHECK` invariants) first. Reserve `SELECT ... FOR UPDATE` only for short transactions on hot contended rows.
- **Money & cards:** Represent money as integer minor units or fixed decimal strings—never IEEE float/double. Keep an append-only double-entry ledger, use hosted PSP tokenization (no raw card storage), and schedule nightly external settlement reconciliation.
- **Cross-service writes:** Compensating Saga / Try-Confirm-Cancel over distributed 2PC; publish retries with exponential backoff + dead-letter queue.

## Boundaries
- Never rely on UI button-disabling alone for duplicate prevention.
- Never silently drop failed downstream ledger/wallet updates; track state transitions (`NOT_STARTED -> EXECUTING -> SUCCESS/FAILED`) and reconcile.

## Done when
Idempotency key & unique constraint exist, concurrency mechanism and money types are fixed, failure/DLQ + reconciliation path is specified, ADR written.
