---
name: applying-observer-pattern
description: Use when changes to the state of one object require changing other objects, and the set of objects is unknown or dynamic (Pub-Sub).
---

# Applying Observer Pattern

## Overview
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.

## Core Pattern
1. Subject maintains a list of Observers and methods to add/remove them.
2. Subject calls `notify()` when state changes.
3. Concrete Observers implement `update()` to react to the Subject.

## Anti-Pattern to Avoid
Avoid tight coupling between the event source and listeners. Watch out for memory leaks if Observers aren't unregistered (Lapsed Listener Problem).
