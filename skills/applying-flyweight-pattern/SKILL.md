---
name: applying-flyweight-pattern
description: Use when your program needs to support a huge number of similar objects, and RAM is a constraint.
---

# Applying Flyweight Pattern

## Overview
Minimizes memory usage by sharing as much data as possible with other similar objects.

## Core Pattern
1. Divide object state into Intrinsic (shared) and Extrinsic (context-specific).
2. Create a Flyweight class holding Intrinsic state.
3. Create a Flyweight Factory to manage a pool of Flyweights.
4. The Client passes Extrinsic state to the Flyweight's methods.

## Anti-Pattern to Avoid
Don't store Extrinsic state in the Flyweight. Don't create Flyweights manually without a factory pool.
