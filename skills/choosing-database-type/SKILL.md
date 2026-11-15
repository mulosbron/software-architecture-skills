---
name: choosing-database-type
description: Use when picking a database for a service or deciding whether to split storage.
---

# Choosing Database Type

**Default in this repo:** PostgreSQL. Deviate only with a measured reason.

## Reasons that justify deviating
- Hot-path lookups measured beyond what Postgres handles → Redis in front; Postgres stays the source of truth.
- Append-only, high-volume time series → a time-series store.
- Traversal-heavy queries (3+ hops) that are slow in SQL → graph database.
- Schema that genuinely varies per record and is never joined → document store.

## Boundaries
- One service, one database. No shared tables across services.
- Money, orders, auth: relational and ACID, no exceptions.
- Read-after-write critical paths (balances, bookings, payments): read from primary or consensus store; replicas serve failover or stale-tolerant reads.
- If write/storage math forces sharding: shard by an even-distribution key using consistent hashing with virtual nodes, isolate hot ("celebrity") keys, and avoid cross-shard joins.
- Each extra engine adds backups, ops, and failure modes. Say so in the ADR.

## Done when
Engine chosen, owning service named, ADR written.
