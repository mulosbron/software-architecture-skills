---
name: applying-bridge-pattern
description: Use when you need to divide a large class or a set of closely related classes into two separate hierarchies (Abstraction and Implementation).
---

# Applying Bridge Pattern

## Overview
Decouples an abstraction from its implementation so that the two can vary independently, avoiding a Cartesian product of subclasses (class explosion).

## Core Pattern
1. Define an Abstraction class holding a reference to an Implementation interface.
2. Define the Implementation interface.
3. Concrete Implementations provide platform-specific code.
4. Refined Abstractions provide high-level control logic.

## Anti-Pattern to Avoid
Don't use subclassing for every combination of dimensions (e.g., `RedCircle`, `BlueCircle`). Use Bridge to separate Shape and Color.
