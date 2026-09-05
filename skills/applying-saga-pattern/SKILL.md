---
name: applying-saga-pattern
description: Use when a business transaction spans multiple microservices and you need to maintain data consistency without distributed locks.
---

# Applying Saga Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Manages distributed transactions by breaking them down into a sequence of local transactions. If one step fails, it triggers compensating transactions to undo the previous steps.

## Core Pattern
1. Identify the steps of the distributed transaction.
2. Define a **Compensating Action** (undo) for every step.
3. Choose Choreography (event-driven, decentralized) for simple flows, or Orchestration (central controller) for complex flows.

## Anti-Pattern to Avoid
Avoid using 2-Phase Commit (2PC) or traditional ACID transactions across microservices, as they lock databases and kill performance.



