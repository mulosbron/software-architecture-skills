---
name: applying-apache-kafka
description: Use when you need to implement Apache Kafka for high-throughput event streaming and data retention.
---

# Applying Apache Kafka

## Overview
Kafka is a distributed commit log that stores events sequentially on disk. It relies on consumers to track their own state.

## Core Pattern
1. Producers append events to a **Topic**.
2. Topics are split into **Partitions** for parallel processing.
3. Consumers in a Consumer Group read from partitions and manage their own **Offsets**.
4. Use Kafka when you need to retain data for days/weeks and allow new services to replay past events.

## Anti-Pattern to Avoid
Don't treat Kafka like a traditional message queue where the broker deletes the message immediately after it's read.
