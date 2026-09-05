---
name: applying-polyglot-persistence
description: Use when designing a system where a single database type is insufficient for all functional requirements.
---

# Applying Polyglot Persistence

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

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



