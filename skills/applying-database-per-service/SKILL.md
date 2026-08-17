---
name: applying-database-per-service
description: Use when designing the data layer of a microservices architecture to ensure loose coupling.
---

# Applying Database-per-Service

## Overview
To keep microservices independent, each service must own its data. No other service is allowed to connect directly to that database.

## Core Pattern
1. Assign a private, dedicated database (or schema) to each microservice.
2. If Service A needs Service B's data, Service A must call Service B's API.
3. Changes to Service B's database schema now only affect Service B, preventing cascading failures across teams.

## Anti-Pattern to Avoid
Don't allow multiple microservices to connect to the exact same database tables. This creates a 'Shared Database' anti-pattern and tight coupling.
