---
name: applying-observability
description: Use when designing a system to ensure issues can be detected, diagnosed, and resolved quickly in production.
---

# Applying Observability

## Overview
Observability is the ability to understand a system's internal state based on its external outputs. It answers the "why" and "where" when things go wrong, moving beyond basic monitoring.

## Core Pattern (The Three Pillars)
1. **Metrics (What is happening?)**: Aggregate numerical data over time (e.g., RPS, CPU %, Error Rates). Useful for dashboards and alerts (e.g., Grafana, Prometheus).
2. **Distributed Traces (Where is it happening?)**: Tracks a single request as it flows across multiple microservices using a unique `Trace ID`. Essential for finding performance bottlenecks (e.g., Zipkin, Jaeger).
3. **Structured Logs (Why is it happening?)**: Detailed, JSON-formatted event records that provide the exact context of an error or action (e.g., ELK Stack).

## Anti-Pattern to Avoid
Don't rely solely on unstructured, plain-text log files in a microservices environment. Without a central `Trace ID`, it's impossible to follow a request's path across 10 different services.
