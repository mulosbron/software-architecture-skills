---
name: applying-api-gateway-pattern
description: Use when you need a single entry point for clients to access multiple microservices.
---

# Applying API Gateway Pattern

## Overview
Provides a single entry point for all clients, abstracting the internal microservice architecture. It handles routing, authentication, rate limiting, and response aggregation.

## Core Pattern
1. Place the Gateway between external clients and internal services.
2. Centralize cross-cutting concerns (AuthN/AuthZ, SSL termination).
3. Use it to route requests (`/api/users` -> User Service) or aggregate responses (API Composition).

## Anti-Pattern to Avoid
Don't put heavy business logic inside the API Gateway. It should act as a router and security checkpoint, not a God Service.
