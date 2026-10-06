---
name: designing-modular-monoliths
description: Use when structuring a new application or carving modules out of a tangled codebase.
---

# Designing Modular Monoliths

**Goal:** One deployable, with module boundaries strict enough that any module could later be extracted without a rewrite.

## Rules this repo enforces
- One top-level directory per business capability (orders, catalog, billing), not per technical layer.
- A module exposes one public entry point (a package, `api/`, or `__init__`). Everything else is internal.
- Modules never read each other's tables. Cross-module data goes through the public entry point or an in-process event.
- Shared code lives in a small `shared/` kernel with no business logic.

Check it: `python tools/arch_tools.py check-module-boundaries <src-dir>` lists imports that reach into another module's internals.

## Boundaries
- Do not put a network between modules. That is a distributed monolith.
- A God Class inside a module is handled by `refactoring-god-classes`.

## Done when
Module list exists, each has a named public entry point, and the boundary check passes.
