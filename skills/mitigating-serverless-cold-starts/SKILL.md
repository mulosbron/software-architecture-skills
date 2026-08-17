---
name: mitigating-serverless-cold-starts
description: Use when user experience is impacted by the initial delay of booting up a serverless function.
---

# Mitigating Serverless Cold Starts

## Overview
Cold starts occur when a FaaS platform provisions a new container to handle an event after a period of inactivity.

## Core Pattern
1. Choose faster runtimes (e.g., Go, Node.js, Python) over heavy JVM/Java runtimes if cold starts are critical.
2. Reduce deployment package size and minimize 3rd-party library imports.
3. Use Provider features like AWS 'Provisioned Concurrency' to keep a pool of warm instances ready.

## Anti-Pattern to Avoid
Don't ignore cold starts in user-facing synchronous APIs. A 3-second cold start on a login endpoint is terrible UX.
