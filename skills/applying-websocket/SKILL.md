---
name: applying-websocket
description: Use when you need real-time, full-duplex communication between client and server (e.g., chat, live trading).
---

# Applying WebSocket

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
WebSocket upgrades a standard HTTP connection into a persistent, stateful, bidirectional TCP connection.

## Core Pattern
1. Start with an HTTP GET request with an `Upgrade: websocket` header.
2. Keep the connection open for continuous data pushing from the server without the client polling.
3. When scaling horizontally across multiple servers, use a **Backplane** (like Redis Pub/Sub) to broadcast events to all servers so they can notify their connected clients.

## Anti-Pattern to Avoid
Don't use standard WebSockets without a backplane in a distributed environment, or users on Server A will never receive events triggered on Server B.



