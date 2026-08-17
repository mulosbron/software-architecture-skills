---
name: applying-polyglot-persistence
description: Use when designing a system where a single database type is insufficient for all functional requirements.
---

# Applying Polyglot Persistence

## Overview
Polyglot Persistence means using different database technologies for different parts of an application, picking the best tool for each specific job.

## Core Pattern
1. Break the application into autonomous services.
2. Let the Auth/Billing service use a Relational DB (SQL).
3. Let the Catalog service use a Document DB (MongoDB).
4. Let the Search service use a search engine (Elasticsearch).
5. Let the Caching layer use a Key-Value store (Redis).

## Anti-Pattern to Avoid
Don't force every service to use PostgreSQL just because it's the company standard, if a specific service handles graph-like recommendation queries.
