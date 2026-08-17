---
name: evaluating-microservices-readiness
description: Use when a user wants to start a new project with Microservices, or migrate an existing monolith to Microservices.
---

# Evaluating Microservices Readiness

## Overview
Microservices solve organizational scaling and extreme traffic problems, but introduce massive complexity (network latency, distributed transactions, tracing).

## Core Pattern

### REQUIRED AGENT BEHAVIOR (CRITICAL)

Before helping a user start a Microservices project from scratch, you MUST question them:
1. "Do you really need Microservices? Are you expecting massive scale or do you have multiple independent development teams?"
2. Suggest starting with a Modular Monolith if they are just starting out (as per best practices).
3. Explain that a 'Distributed Monolith' (tightly coupled microservices) is the worst possible anti-pattern.

If migrating, use the **Strangler Fig** pattern instead of a big-bang rewrite.

## Anti-Pattern to Avoid
Avoid starting with Microservices for MVP projects. Never build a Distributed Monolith.
