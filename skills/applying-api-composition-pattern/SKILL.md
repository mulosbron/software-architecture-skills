---
name: applying-api-composition-pattern
description: Use when a client needs data from multiple microservices and you want to reduce network calls from the client.
---

# Applying API Composition Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Implements a query by invoking multiple internal microservices and aggregating the results into a single response for the client.

## Core Pattern
1. Create an Aggregator service (or use the API Gateway).
2. The Aggregator makes parallel calls to the required microservices.
3. It combines the JSON responses and returns a unified payload to the client.

## Anti-Pattern to Avoid
Don't force the frontend/mobile app to make 10 different HTTP calls to render a single page.



