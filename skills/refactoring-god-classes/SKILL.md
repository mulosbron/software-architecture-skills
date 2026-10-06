---
name: refactoring-god-classes
description: Use when a single class or file owns too many concerns and must be split safely.
---

# Refactoring God Classes

**Goal:** The class becomes a thin coordinator; each extracted concern is a separately testable unit. Behavior does not change.

## Order of operations
1. Find them: `python tools/arch_tools.py check-god-classes <dir> --threshold 400`.
2. Characterization tests first. No tests, no refactor.
3. Extract one responsibility at a time, running tests after each.
4. Replace a growing if/switch with Strategy only where the variant list is actually growing.
5. Inject the extracted units via constructor. Remove `new` from the coordinator.

## Boundaries
- No feature changes in the same PR.
- Stop and ask if an extraction forces a public API change.

## Done when
The original file is under the threshold, tests pass unchanged, and each new unit has at least one direct test.
