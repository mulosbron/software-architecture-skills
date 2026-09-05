---
name: choosing-message-broker
description: Use when deciding between RabbitMQ and Apache Kafka for an Event-Driven Architecture.
---

# Choosing a Message Broker (RabbitMQ vs Kafka)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Different message brokers solve different problems. RabbitMQ focuses on flexible message routing, while Kafka focuses on high-throughput, persistent event streaming.

## Core Pattern
1. Use **RabbitMQ** (Smart Broker) if you need complex routing (direct, topic, fanout exchanges), task queues, and instant message deletion after processing.
2. Use **Apache Kafka** (Smart Consumer) if you need event sourcing, log aggregation, real-time analytics, high throughput, and the ability to replay historical events (messages are stored on disk).

## Anti-Pattern to Avoid
Don't use Kafka just for simple task queues or traditional microservice async RPC. Don't use RabbitMQ for massive real-time data lakes.



