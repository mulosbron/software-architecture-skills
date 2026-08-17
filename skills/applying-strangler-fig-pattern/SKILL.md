---
name: applying-strangler-fig-pattern
description: Use when migrating a legacy Monolith to Microservices incrementally without a risky 'Big Bang' rewrite.
---

# Applying Strangler Fig Pattern

## Overview
Gradually replaces a legacy system by wrapping it with a proxy and intercepting requests, routing them either to the new microservice or the old monolith.

## Core Pattern
1. Put an API Gateway or Proxy in front of the Monolith.
2. Extract one domain into a new Microservice.
3. Update the Gateway to route requests for that domain to the new service, while the rest goes to the Monolith.
4. Repeat until the Monolith is entirely replaced.

## Anti-Pattern to Avoid
Never attempt a 'Big Bang' rewrite of a massive monolith. Always migrate incrementally.
