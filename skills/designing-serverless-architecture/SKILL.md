---
name: designing-serverless-architecture
description: Use when deciding if a Serverless architecture is appropriate for a project or component.
---

# Designing Serverless Architecture

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Serverless removes server management, scales automatically to zero, and charges only per millisecond of execution. It is ideal for event-driven, unpredictable, or highly variable workloads.

## Core Pattern
1. Use Serverless for Web APIs, background data processing, IoT event handling, and scheduled cron jobs.
2. Combine FaaS (Custom Logic) with BaaS (Managed Auth, Storage, DB) for maximum speed.
3. Keep functions small, focused, and stateless.

## Anti-Pattern to Avoid
Don't use Serverless for consistently high-CPU/long-running background jobs, or extremely low-latency requirements (due to cold starts). Don't try to migrate a massive Monolith directly into a single Lambda function.



