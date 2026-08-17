---
name: designing-rest-api
description: Use when designing public-facing, resource-oriented APIs over HTTP.
---

# Designing RESTful APIs

## Overview
REST (Representational State Transfer) is a stateless, resource-oriented architectural style. It leverages standard HTTP methods and status codes.

## Core Pattern
1. Use **Nouns, not Verbs** for URIs (e.g., `POST /books`, not `POST /createBook`).
2. Keep requests **Stateless**; auth tokens should be in headers, not server sessions.
3. Use standard HTTP methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove).
4. Return proper HTTP Status Codes (200, 201, 204, 400, 401, 403, 404, 500).

## Anti-Pattern to Avoid
Don't use `GET` to change state. Don't return `200 OK` when an error occurs just because the JSON body says `{"error": true}`.
