---
name: applying-graphql
description: Use when frontend clients need flexible, complex data querying without over-fetching or under-fetching.
---

# Applying GraphQL

## Overview
GraphQL is a query language for APIs that allows clients to request exactly the data they need from a single endpoint.

## Core Pattern
1. Expose a single endpoint (usually `/graphql`).
2. Define a strong, typed Schema using Schema Definition Language (SDL).
3. Clients send **Queries** for reading, **Mutations** for writing, and **Subscriptions** for real-time updates.
4. Ideal for mobile apps or complex SPAs where bandwidth and precise data are critical.

## Anti-Pattern to Avoid
Don't use GraphQL for simple CRUD applications where REST caching (via CDNs) would be much more effective. GraphQL makes HTTP-level caching difficult.
