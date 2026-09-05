---
name: applying-blue-green-deployment
description: Use when you need to deploy a new version of an application with zero downtime and instant rollback capabilities.
---

# Applying Blue/Green Deployment

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Blue/Green deployment reduces risk by running two identical production environments. Only one serves live production traffic at any time.

## Core Pattern
1. **Two Environments**: Keep the current live version running in the "Blue" environment.
2. **Deploy to Idle**: Deploy the new version to the idle "Green" environment.
3. **Test**: Run acceptance tests against the isolated Green environment.
4. **Switch Traffic**: Update the load balancer/router to point 100% of live traffic to the Green environment.
5. **Instant Rollback**: If a critical bug is found, switch the router back to the Blue environment instantly.

## Anti-Pattern to Avoid
Don't use this if your database schemas change destructively between versions without backward compatibility. Both Blue and Green must be able to safely talk to the database at the same time.



