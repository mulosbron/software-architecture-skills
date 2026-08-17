---
name: applying-proxy-pattern
description: Use when you need to control access to an object (security, lazy loading, caching) without modifying its code.
---

# Applying Proxy Pattern

## Overview
Provides a surrogate or placeholder for another object to control access to it.

## Core Pattern
1. Create a Subject interface.
2. The RealSubject implements business logic.
3. The Proxy implements the Subject interface, holding a reference to the RealSubject. The Proxy performs its check/cache/loading before delegating to the RealSubject.

## Anti-Pattern to Avoid
Don't put heavy initialization in constructors. Use Virtual Proxy to delay creation. Don't mix Proxy and Decorator intents.
