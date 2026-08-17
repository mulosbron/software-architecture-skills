---
name: applying-composite-pattern
description: Use when you need to represent part-whole hierarchies and want clients to treat individual objects and compositions uniformly.
---

# Applying Composite Pattern

## Overview
Composes objects into tree structures. Clients can treat individual objects (Leaves) and groups (Composites) identically.

## Core Pattern
1. Create a Component interface defining common operations.
2. Create Leaf classes representing end objects.
3. Create Composite classes that contain a list of Components and delegate operations to their children.

## Anti-Pattern to Avoid
Don't use it if your domain isn't a tree structure. Avoid casting to Composite/Leaf in client code.
