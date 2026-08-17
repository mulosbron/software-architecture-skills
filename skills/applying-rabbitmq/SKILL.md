---
name: applying-rabbitmq
description: Use when you need to implement RabbitMQ for complex message routing and task queues.
---

# Applying RabbitMQ

## Overview
RabbitMQ is an AMQP-based broker that uses Exchanges and Queues to intelligently route messages.

## Core Pattern
1. Producers send messages to an **Exchange**.
2. Choose Exchange Type: **Direct** (exact match), **Topic** (wildcard match), or **Fanout** (broadcast to all).
3. Consumers pull messages from bound **Queues**.
4. Use ACKs to ensure messages aren't lost if a consumer crashes.

## Anti-Pattern to Avoid
Don't have producers send messages directly to a queue. Always route through an Exchange for future flexibility.
