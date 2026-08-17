---
name: choosing-api-style
description: Use when deciding between REST, GraphQL, gRPC, and WebSockets for a new service.
---

# Choosing an API Architecture Style

## Overview
Different API styles solve different problems. Choosing the right one is critical for system performance and developer experience.

## Core Pattern
1. **REST**: Default choice for public APIs, excellent for standard CRUD, caching, and simple integrations.
2. **GraphQL**: Best for complex UIs, mobile apps, and aggregating data from multiple sources to prevent over/under-fetching.
3. **gRPC**: Best for internal microservice-to-microservice communication where raw performance and strict typing matter.
4. **WebSocket**: Best for real-time dashboards, games, or chat apps.

## Anti-Pattern to Avoid
Don't blindly choose the newest tech (like GraphQL) if your API simply serves static data that would benefit massively from standard HTTP GET caching.
