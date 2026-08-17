---
name: applying-api-composition-pattern
description: Use when a client needs data from multiple microservices and you want to reduce network calls from the client.
---

# Applying API Composition Pattern

## Overview
Implements a query by invoking multiple internal microservices and aggregating the results into a single response for the client.

## Core Pattern
1. Create an Aggregator service (or use the API Gateway).
2. The Aggregator makes parallel calls to the required microservices.
3. It combines the JSON responses and returns a unified payload to the client.

## Anti-Pattern to Avoid
Don't force the frontend/mobile app to make 10 different HTTP calls to render a single page.
