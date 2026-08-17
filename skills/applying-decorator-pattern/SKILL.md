---
name: applying-decorator-pattern
description: Use when you need to attach additional responsibilities to an object dynamically without subclassing.
---

# Applying Decorator Pattern

## Overview
Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

## Core Pattern
1. Create a Component interface.
2. Create a Base Decorator implementing Component, wrapping a Component reference.
3. Create Concrete Decorators extending the Base Decorator, adding behavior before/after calling the wrapped object.

## Anti-Pattern to Avoid
Don't create a subclass for every feature combination. Use Decorators to stack features dynamically.
