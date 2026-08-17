---
name: choosing-message-broker
description: Use when deciding between RabbitMQ and Apache Kafka for an Event-Driven Architecture.
---

# Choosing a Message Broker (RabbitMQ vs Kafka)

## Overview
Different message brokers solve different problems. RabbitMQ focuses on flexible message routing, while Kafka focuses on high-throughput, persistent event streaming.

## Core Pattern
1. Use **RabbitMQ** (Smart Broker) if you need complex routing (direct, topic, fanout exchanges), task queues, and instant message deletion after processing.
2. Use **Apache Kafka** (Smart Consumer) if you need event sourcing, log aggregation, real-time analytics, high throughput, and the ability to replay historical events (messages are stored on disk).

## Anti-Pattern to Avoid
Don't use Kafka just for simple task queues or traditional microservice async RPC. Don't use RabbitMQ for massive real-time data lakes.
