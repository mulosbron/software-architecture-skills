---
name: choosing-message-broker
description: Use when adding asynchronous messaging or choosing between RabbitMQ and Kafka.
---

# Choosing a Message Broker

**Default in this repo:** No broker until a synchronous call is shown to be the bottleneck. Then RabbitMQ for work queues, Kafka only for replayable event streams.

## Decide with one question
Do consumers need to re-read history (replay, audit, late joiners)? Yes → Kafka. No → RabbitMQ.

## Boundaries
- Every message has a schema file committed next to its producer.
- Every consumer is idempotent. Document the dedupe key.
- Dead-letter handling is designed before go-live, not after the first incident.

## Done when
Broker chosen, first topic or queue named with its schema, retention and DLQ policy stated, ADR written.
