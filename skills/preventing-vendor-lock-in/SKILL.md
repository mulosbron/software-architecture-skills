---
name: preventing-vendor-lock-in
description: Use when designing serverless applications to minimize the risk of being permanently tied to one cloud provider.
---

# Preventing Vendor Lock-in in Serverless

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Serverless inherently ties you to a provider's ecosystem (e.g., AWS API Gateway + Lambda + DynamoDB). You must design your code to minimize the blast radius of this lock-in.

## Core Pattern
1. Use **Hexagonal Architecture (Ports & Adapters)**: Keep your core business logic completely unaware of AWS/Google SDKs.
2. Write adapter classes for Lambda handlers that simply parse the event and pass pure objects to your business logic.
3. Isolate database access behind Repository interfaces so you can swap DynamoDB for MongoDB later if needed.

## Anti-Pattern to Avoid
Don't sprinkle `boto3` or AWS SDK calls directly inside your core business logic calculations.



