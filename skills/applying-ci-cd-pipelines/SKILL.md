---
name: applying-ci-cd-pipelines
description: Use when designing the workflow to automatically test, build, and release application code.
---

# Applying CI/CD Pipelines

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Continuous Integration (CI) and Continuous Delivery/Deployment (CD) bridge the gap between development and operations by automating the building, testing, and deployment of applications.

## Core Pattern
1. **Continuous Integration**: Developers merge changes frequently to the main branch. Every merge triggers an automated build and test suite.
2. **Continuous Delivery**: Automatically package the code into a releasable artifact (e.g., Docker Image) and deploy it to a staging environment for final manual approval.
3. **Continuous Deployment**: If tests pass, automatically deploy the artifact straight to production without manual intervention.

## Anti-Pattern to Avoid
Don't wait for weeks to integrate code branches ("Integration Hell"). Code should be merged to the main branch at least daily, backed by strong automated tests.



