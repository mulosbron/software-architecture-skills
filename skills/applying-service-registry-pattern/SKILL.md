---
name: applying-service-registry-pattern
description: Use when microservices need to dynamically discover the IP addresses and ports of other services.
---

# Applying Service Registry Pattern

## Overview
In cloud environments, service IPs change dynamically. A Service Registry acts as a central phonebook where services register themselves and look up others.

## Core Pattern
1. Deploy a Service Registry (e.g., Eureka, Consul).
2. Services register their network location upon startup.
3. Client services query the registry to find the target service before making an HTTP/gRPC call.

## Anti-Pattern to Avoid
Don't hardcode IP addresses in configuration files in a microservices environment.
