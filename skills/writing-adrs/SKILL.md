---
name: writing-adrs
description: Use when an architectural decision is made, or when someone asks why the system is designed a certain way.
---

# Writing ADRs

**Goal:** Every hard-to-reverse decision gets a record in `docs/adrs/` before the code lands.

## How this repo does it
```bash
python tools/arch_tools.py adr-new "Use PostgreSQL for orders"
python tools/arch_tools.py adr-list
python tools/arch_tools.py adr-supersede 3 "Move orders to CockroachDB"
```
The scaffold creates Status, Context, Decision, Consequences. Fill them; do not add sections.

## Rules
- Context states the forcing constraint (team size, SLA, budget), not background.
- Consequences must list at least one negative. An ADR with only upsides is incomplete.
- Never edit an Accepted ADR. Supersede it.

## Done when
The file exists, status is Proposed or Accepted, and the implementing PR links to it.
