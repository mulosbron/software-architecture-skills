---
name: applying-rbac-authorization
description: Use when determining if an authenticated user has permission to perform a specific action.
---

# Applying RBAC Authorization

## Overview
Role-Based Access Control (RBAC) separates the identity of the user (who they are) from their permissions (what they can do) by grouping permissions into Roles.

## Core Pattern
1. **Authentication First**: Always verify the user's identity before checking authorization.
2. **Assign Roles**: Users are assigned roles (e.g., `Admin`, `Customer`, `Editor`).
3. **Check Permissions**: Instead of hardcoding user IDs, check if the user's role has permission to access the endpoint (e.g., `POST /books` requires `Admin` role).
4. **Middleware Enforcement**: Implement these checks at the API Gateway or via middleware/filters before the request reaches the business logic.

## Anti-Pattern to Avoid
Don't confuse Authentication (AuthN - Who are you?) with Authorization (AuthZ - What can you do?). Logging in successfully does not mean the user is allowed to delete records.
