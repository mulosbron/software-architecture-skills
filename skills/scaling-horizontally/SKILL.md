---
name: scaling-horizontally
description: Use when designing a system to handle increased load without being limited by single-server hardware capacity.
---

# Scaling Horizontally

## Overview
Horizontal Scaling involves adding more server instances to distribute the load, rather than upgrading a single server's hardware (Vertical Scaling). This is essential for high availability and cloud-native applications.

## Core Pattern
1. **Stateless Applications**: Ensure your web or API servers don't store session state locally. Store state in a distributed cache like Redis.
2. **Load Balancing**: Place a Load Balancer (e.g., Nginx, HAProxy, AWS ALB) in front of your server instances to distribute incoming traffic evenly.
3. **Auto-Scaling**: Configure infrastructure to automatically spin up new instances when CPU/Memory usage spikes, and scale down when traffic drops.

## Anti-Pattern to Avoid
Don't rely purely on Vertical Scaling (buying a bigger server) for web applications, as it creates a Single Point of Failure (SPOF) and has a hard hardware limit.
