---
name: writing-adrs
description: Use when deciding on a major architectural change, technology selection, or when asked to document the rationale behind a design decision
---

# Writing Architecture Decision Records (ADRs)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
An Architecture Decision Record (ADR) is a short text file that captures an important architectural decision made along with its context and consequences. If a decision is not documented, it effectively doesn't exist, leading to "architectural drift".

## When to Use
- You are making a choice between Monolithic and Microservices
- You are selecting a database or message broker
- You need to explain *why* a system is designed the way it is

## Core Pattern
Every ADR must follow this simple structure:

1. **Title**: Short summary of the decision (e.g., "001: Using RabbitMQ for Inter-service Communication").
2. **Status**: Current state ("Proposed", "Accepted", "Rejected", "Superseded").
3. **Context**: What is the problem? What business goals or constraints drive this?
4. **Decision**: What is the final choice?
5. **Consequences**: The trade-offs. What becomes easier (Positive)? What becomes harder (Negative)?

## Common Mistakes
- **Documenting only the "What"**: Always document the "Why" and the "Context".
- **Ignoring negative consequences**: Every decision has a trade-off. If you don't list negatives (e.g., "increased operational complexity"), the ADR is incomplete.



