---
name: applying-canary-deployment
description: Use when you want to minimize the "blast radius" of a potential bug by slowly rolling out a new feature to a small subset of users.
---

# Applying Canary Deployment

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Named after the "canary in a coal mine", this strategy routes a small percentage of real user traffic to a new version to test its stability before a full rollout.

## Core Pattern
1. **Initial Deployment**: Deploy the new version (v1.1) alongside the existing version (v1.0).
2. **Traffic Split**: Route a tiny fraction of traffic (e.g., 5%) to v1.1.
3. **Monitor**: Closely observe metrics, error logs, and tracing for v1.1.
4. **Gradual Rollout**: If v1.1 is healthy, gradually increase its traffic share (10%, 50%, 100%). If it errors, route traffic back to v1.0 instantly.

## Anti-Pattern to Avoid
Don't attempt a Canary deployment without a mature, automated observability stack. If you can't automatically detect that the 5% of users are experiencing errors, the strategy fails.



