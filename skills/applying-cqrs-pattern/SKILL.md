---
name: applying-cqrs-pattern
description: Use when read and write operations have vastly different performance, scaling, or data model requirements.
---

# Applying CQRS Pattern

## Overview
Command Query Responsibility Segregation (CQRS) separates the data models and APIs for reading data (Queries) from writing data (Commands).

## Core Pattern
1. Split the system into a Write Side (Commands that mutate state) and a Read Side (Queries that return state).
2. Often backed by separate databases (e.g., Write to PostgreSQL, Read from ElasticSearch).
3. Sync databases asynchronously via events (Eventual Consistency).

## Anti-Pattern to Avoid
Don't use CQRS for simple CRUD applications. The eventual consistency and dual-model overhead is only justified in complex domains.
