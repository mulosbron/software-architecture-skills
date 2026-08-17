---
name: applying-event-sourcing-pattern
description: Use when you need a complete audit trail of how data reached its current state, rather than just storing the current state.
---

# Applying Event Sourcing Pattern

## Overview
Stores the state of a system as a sequence of immutable events. The current state is derived by replaying these events.

## Core Pattern
1. Instead of UPDATE/DELETE, append an Event (e.g., `OrderCreated`, `ItemAdded`) to an Event Store.
2. Replay events to rebuild the current state in memory.
3. Usually paired with CQRS to project the events into a queryable read database.

## Anti-Pattern to Avoid
Don't mutate past events. Events are immutable historical facts. Don't use Event Sourcing if simple CRUD is sufficient.
