---
name: protecting-and-sizing-apis
description: Use when estimating capacity (QPS/storage), choosing distributed ID schemes, or adding rate limiting before scaling out services or databases.
---

# Protecting and Sizing APIs

**Goal:** Ground caching, sharding, ID generation, and rate limiting in measured or calculated numbers before adding distributed infrastructure.

## Defaults this repo takes
- **Capacity math first:** Compute DAU, average QPS, 2x–3x peak QPS, and 5-year storage before introducing Redis caches, read replicas, or horizontal sharding.
- **Rate limiting:** Enforce at the server middleware or API Gateway (never client-only). Default to Token Bucket for burst tolerance, backed by atomic Redis Lua/sorted-set ops across instances, returning `429` with `Retry-After`.
- **Distributed IDs:** Use UUIDv7 or a 64-bit time-sortable Snowflake layout (timestamp + node + sequence with NTP clock-skew handling) rather than exposing sequential DB auto-increments or introducing a centralized ticket-server SPOF.

## Boundaries
- Keep web/API tiers stateless (move session/rate-limit state to Redis/DB) before scaling horizontally.
- Do not add Redis or shard databases purely by intuition; cite the estimated QPS, latency budget, or storage threshold in the ADR.

## Done when
QPS/peak/storage assumptions, throttling algorithm + placement, and ID strategy are documented and recorded via `arch_tools.py adr-new`.
