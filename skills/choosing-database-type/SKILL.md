---
name: choosing-database-type
description: Use when deciding between SQL and different types of NoSQL databases for a project.
---

# Choosing Database Type (SQL vs NoSQL)

## Overview
Different data requirements dictate different database types based on the CAP Theorem and ACID/BASE guarantees.

## Core Pattern
1. **SQL (PostgreSQL, MySQL)**: Use for strong ACID transactions and relational data (e.g., billing, orders).
2. **NoSQL Document (MongoDB)**: Use for flexible schemas and storing complex JSON objects (e.g., product catalogs).
3. **NoSQL Key-Value (Redis, DynamoDB)**: Use for ultra-fast, simple lookups (e.g., sessions, caching).
4. **NoSQL Graph (Neo4j)**: Use for highly connected data and complex relationships (e.g., recommendation engines).

## Anti-Pattern to Avoid
Don't use a relational database for massive time-series event logging, and don't use a NoSQL Document store for critical banking transactions requiring strict ACID compliance.
