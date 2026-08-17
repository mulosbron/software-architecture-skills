---
name: applying-command-pattern
description: Use when you need to parameterize objects with operations, delay execution, queue requests, or support Undo operations.
---

# Applying Command Pattern

## Overview
Turns a request into a stand-alone object containing all information about the request.

## Core Pattern
1. Declare a Command interface with `execute()` (and `undo()`).
2. Concrete Commands wrap a Receiver and parameters.
3. The Invoker triggers the command without knowing the Receiver.
4. Client wires Invoker, Command, and Receiver.

## Anti-Pattern to Avoid
Don't couple the UI (Invoker) directly to business logic (Receiver). Command is the mediator.
