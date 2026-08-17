---
name: applying-circuit-breaker-pattern
description: Use when a microservice calls another service and you need to prevent cascading failures if the target service goes down.
---

# Applying Circuit Breaker Pattern

## Overview
Prevents a network or service failure from cascading to other services. It stops sending requests to a failing service and returns a fallback response immediately.

## Core Pattern
1. Wrap the inter-service call in a Circuit Breaker.
2. **Closed State**: Normal operation.
3. **Open State**: If failure threshold is reached, block calls and return fallback instantly.
4. **Half-Open State**: After a timeout, allow one test request to see if the service recovered.

## Anti-Pattern to Avoid
Don't rely solely on HTTP timeouts. A slow service will exhaust thread pools; a Circuit Breaker fails fast.
