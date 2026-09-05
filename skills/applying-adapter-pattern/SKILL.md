---
name: applying-adapter-pattern
description: Use when integrating legacy code or 3rd-party libraries with incompatible interfaces into your system.
---

# Applying Adapter Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Allows objects with incompatible interfaces to collaborate by providing a wrapper that translates requests.

## Core Pattern
1. Identify Target interface and Adaptee class.
2. Create an Adapter class that implements the Target interface and wraps the Adaptee via composition.
3. The Adapter translates the Target method calls into Adaptee method calls.

## Anti-Pattern to Avoid
Do not rewrite the entire legacy system. Use Adapter to bridge the gap. Avoid using inheritance (Class Adapter); prefer composition (Object Adapter).



