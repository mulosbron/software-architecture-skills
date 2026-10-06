---
name: verifying-solid-compliance
description: Use when asked to review code for SOLID violations or architectural smells.
---

# Verifying SOLID Compliance

**Goal:** A short list of concrete violations with file:line, ranked by blast radius. Not a lecture on SOLID.

## Signals to scan for
- **SRP:** class names ending in Manager/Processor/Handler/System; one class touching DB, business rules, and I/O.
- **OCP:** `if/switch` on a type or enum that grows with each feature (payment type, notification channel).
- **LSP:** subclasses throwing NotImplemented/NotSupported; overrides that silently no-op.
- **ISP:** implementations with empty methods; interfaces with 10+ members.
- **DIP:** `new ConcreteService()` inside business logic; static calls into infrastructure.

Start with `python tools/arch_tools.py check-god-classes <dir>` to find the biggest files and read those first.

## Boundaries
- Report, do not refactor, unless asked. Refactoring is `refactoring-god-classes`.
- Skip generated code, tests, and vendored directories.

## Done when
Each finding has a location, the principle, and a one-line fix. At most 10 findings; say if there are more.
