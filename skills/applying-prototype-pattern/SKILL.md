---
name: applying-prototype-pattern
description: Use when creating an object is expensive (DB calls, complex logic), and you want to clone an existing instance instead.
---

# Applying Prototype Pattern

## Overview
Lets you copy existing objects without making your code dependent on their classes. Reduces the cost of creating new objects.

## Core Pattern
1. Declare a `Prototype` interface with a `clone()` method.
2. A concrete class implements the `clone()` method, copying its own fields to the new object.

## Anti-Pattern to Avoid
Beware of shallow vs. deep copy issues. Don't use Prototype if the object is simple to instantiate with `new`.
