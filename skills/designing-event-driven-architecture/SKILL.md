---
name: designing-event-driven-architecture
description: Use when transitioning a system from synchronous REST/RPC calls to asynchronous event-driven communication.
---

# Designing Event-Driven Architecture

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Event-Driven Architecture (EDA) makes systems more reactive, scalable, and resilient by having services react to 'events' rather than explicitly asking other services to do work.

## Core Pattern
1. Identify synchronous bottlenecks in your system.
2. Convert commands (Do this) into events (This happened).
3. Use a Message Broker to decouple the sender from the receiver, ensuring failures don't cascade.

## Anti-Pattern to Avoid
Don't use EDA for every single communication. If a user interface needs an immediate synchronous response (e.g., login validation), a REST call might be better.



