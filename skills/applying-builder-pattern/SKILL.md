---
name: applying-builder-pattern
description: Use when constructing complex objects step by step, or when you want to create different representations of some product.
---

# Applying Builder Pattern

## Overview
Separates the construction of a complex object from its representation so that the same construction process can create different representations.

## Core Pattern
1. Define a `Builder` interface or static inner class.
2. Add step-by-step building methods returning `this` (Fluent Interface).
3. Provide a `build()` method to return the final product.
4. (Optional) Use a Director to encapsulate standard configurations.

## Anti-Pattern to Avoid
Avoid 'Telescoping Constructors' (constructors with a huge list of parameters). Don't use Builder for simple objects with few parameters.
