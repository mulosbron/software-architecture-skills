---
name: applying-facade-pattern
description: Use when you need to provide a simple, unified interface to a complex subsystem of classes, APIs, or frameworks.
---

# Applying Facade Pattern

## Overview
Provides a simplified interface to a library, a framework, or any other complex set of classes.

## Core Pattern
1. Identify a complex subsystem with many dependencies.
2. Create a Facade class providing simplified methods for common use cases.
3. The Facade delegates client requests to appropriate subsystem objects.

## Anti-Pattern to Avoid
Don't force the client to use the subsystem classes directly. The Facade shouldn't become a 'God Class' containing business logic.
