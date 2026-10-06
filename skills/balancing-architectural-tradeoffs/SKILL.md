---
name: balancing-architectural-tradeoffs
description: Use when choosing between architectural styles or weighing quality attributes (speed-to-market vs scale, consistency vs availability).
---

# Balancing Architectural Tradeoffs

**Goal:** A recommendation tied to the user's stage, team shape, and the one quality attribute they will not compromise.

## Ask these, nothing else
1. Stage: unproven idea, growing, or established?
2. Team: how many people, how many teams?
3. The one non-negotiable: latency, uptime, consistency, cost, or ship date?

## Defaults this repo takes
- Unproven idea or single team → monolith (`designing-modular-monoliths`).
- Multiple autonomous teams with a platform → services are on the table (`evaluating-microservices-readiness`).
- Conway's law wins. Do not propose a structure the org cannot staff.

## Done when
The answer names what is sacrificed, and the decision is recorded with `arch_tools.py adr-new`.
