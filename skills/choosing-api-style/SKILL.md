---
name: choosing-api-style
description: Use when deciding between REST, GraphQL, gRPC, or WebSockets for a new interface.
---

# Choosing API Style

**Defaults in this repo:** REST for anything public. gRPC for service-to-service. GraphQL only when a client team owns the schema and over-fetching is measured, not assumed. WebSockets only for server push, never as a general transport.

## Ask
- Who consumes it: browser, mobile, another service, third parties?
- Is caching on GET a meaningful win?
- Does any flow need server push?

## Boundaries
- Do not mix styles on one surface without an ADR.
- REST ships with an OpenAPI spec committed; gRPC ships with its .proto committed.

## Done when
Style chosen, consumer named, contract file location decided, ADR written.
