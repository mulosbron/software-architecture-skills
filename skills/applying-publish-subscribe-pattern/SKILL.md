---
name: applying-publish-subscribe-pattern
description: Use when you need to decouple event producers from event consumers in a distributed system.
---

# Applying Publish/Subscribe Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
The Pub/Sub pattern (an architectural version of the Observer pattern) allows services to communicate asynchronously without knowing about each other.

## Core Pattern
1. The Publisher sends a message (event) to a Channel/Topic on the Message Broker.
2. The Broker distributes a copy of the message to all subscribed Consumers.
3. The Publisher does not know who the subscribers are, and subscribers don't know who the publisher is.

## Anti-Pattern to Avoid
Don't hardcode IP addresses of subscribers into the publisher. The publisher should only know the Message Broker.



