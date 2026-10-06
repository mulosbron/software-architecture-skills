---
name: selecting-design-patterns
description: Use when deciding which GoF pattern fits a problem, or when reviewing whether an existing pattern is justified.
---

# Selecting Design Patterns

**Goal:** Name the one pattern that fits, why, and what it costs. The default answer is often "no pattern, a function will do."

## Problem → pattern
| Problem | Pattern |
|---|---|
| Growing if/switch on a variant | Strategy |
| Add behavior without touching the class | Decorator |
| Incompatible third-party interface | Adapter |
| Undo, queueing, audit of operations | Command |
| Many listeners for a state change | Observer |
| Behavior changes with lifecycle state | State |
| Construction with many optional steps | Builder |
| Hide a messy subsystem behind one entry | Facade |
| Tree of parts and wholes treated alike | Composite |
| Lazy load, access control, caching of one object | Proxy |
| Family of related objects swapped together | Abstract Factory |

Singleton: use the DI container's singleton scope. Do not hand-roll one.

## Boundaries
- One pattern per problem. If you need three, the problem is misdiagnosed.
- Match the codebase's existing conventions before introducing a new one.

## Done when
The recommendation names the pattern, the trigger it solves, and the indirection the user accepts in return.
