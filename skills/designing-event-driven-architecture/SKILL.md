---
name: designing-event-driven-architecture
description: Use when transitioning a system from synchronous REST/RPC calls to asynchronous event-driven communication.
---

# Designing Event-Driven Architecture

## Overview
Event-Driven Architecture (EDA) makes systems more reactive, scalable, and resilient by having services react to 'events' rather than explicitly asking other services to do work.

## Core Pattern
1. Identify synchronous bottlenecks in your system.
2. Convert commands (Do this) into events (This happened).
3. Use a Message Broker to decouple the sender from the receiver, ensuring failures don't cascade.

## Anti-Pattern to Avoid
Don't use EDA for every single communication. If a user interface needs an immediate synchronous response (e.g., login validation), a REST call might be better.
