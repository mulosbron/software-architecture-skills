---
name: structuring-monorepos
description: Use when structuring a multi-package monorepo, configuring build caching or affected-CI pipelines, or enforcing cross-package dependencies.
---

# Structuring Monorepos

## Goal
Enable fast, predictable multi-package builds and safe code sharing with explicit package boundaries.

## Repo defaults
- **Keep packages cohesive and acyclic.** Separate deployable `apps/` from shared `packages/` (`libs/`); extract shared code only when >=2 consumers need identical semantics.
- **Affected-only CI + remote cache.** Configure workspace dependency graphs, local/remote build caching, and affected-target detection (Nx, Turborepo, Bazel, or native workspaces).
- **Enforce ownership and lint constraints.** Pair package boundary tags with `CODEOWNERS` and `python tools/arch_tools.py check-module-boundaries <src-dir>`.

## Boundaries
- No circular dependencies between workspace packages or deep relative imports across package roots.
- Do not introduce Bazel or heavy meta-tooling when native workspaces plus Turborepo/Nx suffice.
- Record workspace layout and versioning policy via `python tools/arch_tools.py adr-new`.

## Done when
- Workspace layout, package public entrypoints, and dependency constraints are enforced in CI.
- Affected build/test commands and caching configuration work cleanly.
- An ADR documents package ownership and release/versioning rules.
