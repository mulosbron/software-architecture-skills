---
name: modernizing-legacy-systems
description: Use when migrating legacy codebases or outdated frameworks incrementally, auditing technical debt, or reducing rewrite risk.
---

# Modernizing Legacy Systems

## Goal
Replace or clean up brittle legacy systems safely in thin vertical slices without halting delivery or breaking existing behavior.

## Repo defaults
- **Strangler Fig, never big-bang rewrites.** Route new behavior and extracted slices through compatibility shims behind feature flags while keeping rollback trivial.
- **Characterization tests before touching seams.** Run `python tools/arch_tools.py check-god-classes <dir>` and `check-module-boundaries <src-dir>` first, then lock existing behavior with tests before refactoring.
- **Prioritize debt by blast radius.** Rank technical debt hotspots using change frequency x complexity x business impact rather than cosmetic cleanup.

## Boundaries
- Never mix behavioral changes and structural refactors in the same PR.
- Never retire a legacy path without backward-compatibility shims, deprecation timelines, and rollback steps.
- Track major cutover/decommission decisions via `python tools/arch_tools.py adr-new`.

## Done when
- Debt hotspots are ranked with exact file/line evidence and measurable exit criteria.
- Characterization tests cover the target slice before any code movement.
- Rollout uses incremental routing/feature flags with verified rollback.
