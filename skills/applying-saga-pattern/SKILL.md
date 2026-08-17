---
name: applying-saga-pattern
description: Use when a business transaction spans multiple microservices and you need to maintain data consistency without distributed locks.
---

# Applying Saga Pattern

## Overview
Manages distributed transactions by breaking them down into a sequence of local transactions. If one step fails, it triggers compensating transactions to undo the previous steps.

## Core Pattern
1. Identify the steps of the distributed transaction.
2. Define a **Compensating Action** (undo) for every step.
3. Choose Choreography (event-driven, decentralized) for simple flows, or Orchestration (central controller) for complex flows.

## Anti-Pattern to Avoid
Avoid using 2-Phase Commit (2PC) or traditional ACID transactions across microservices, as they lock databases and kill performance.
