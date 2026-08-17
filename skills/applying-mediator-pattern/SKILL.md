---
name: applying-mediator-pattern
description: Use when a set of objects communicate in complex, chaotic ways, and you want to centralize communication.
---

# Applying Mediator Pattern

## Overview
Reduces chaotic dependencies between objects. Restricts direct communications and forces them to collaborate only via a mediator object.

## Core Pattern
1. Declare a Mediator interface.
2. Colleague classes hold a reference to the Mediator and notify it of state changes.
3. Concrete Mediator receives notifications and coordinates other colleagues.

## Anti-Pattern to Avoid
Don't let colleagues communicate directly (Spaghetti code). Beware of the Mediator becoming a God Class.
