---
name: applying-jwt-authentication
description: Use when implementing stateless authentication for RESTful APIs.
---

# Applying JWT Authentication

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
JSON Web Tokens (JWT) provide a stateless way to authenticate users in distributed systems and RESTful APIs, eliminating the need for server-side session storage.

## Core Pattern
1. **Login**: Client sends credentials to the Auth Server.
2. **Token Generation**: If valid, the server signs a JWT containing the user ID and roles, and sends it to the client.
3. **Storage**: The client securely stores the token.
4. **Usage**: The client includes the token in the `Authorization: Bearer <token>` HTTP header for every subsequent request.
5. **Verification**: The Resource Server validates the token's cryptographic signature locally without needing to query the database.

## Anti-Pattern to Avoid
Don't store sensitive information (like passwords or credit card numbers) in the JWT payload, as it is only Base64 encoded, not encrypted.



