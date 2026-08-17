---
name: applying-grpc
description: Use when you need high-performance, low-latency communication between internal microservices.
---

# Applying gRPC

## Overview
gRPC is a high-performance RPC framework by Google. It uses HTTP/2 for transport and Protocol Buffers (Protobuf) for binary serialization.

## Core Pattern
1. Define your service contract in a `.proto` file.
2. Generate client (stub) and server code automatically in your target language.
3. Use gRPC for 'East-West' traffic (microservice to microservice) to maximize throughput and minimize latency.
4. Leverage HTTP/2 features like Multiplexing and Streaming (Unary, Server/Client/Bidirectional stream).

## Anti-Pattern to Avoid
Don't use gRPC as the primary public-facing API for web browsers, as browsers have limited support for raw HTTP/2 framing without proxies (gRPC-Web).
