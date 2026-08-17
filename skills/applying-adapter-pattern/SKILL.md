---
name: applying-adapter-pattern
description: Use when integrating legacy code or 3rd-party libraries with incompatible interfaces into your system.
---

# Applying Adapter Pattern

## Overview
Allows objects with incompatible interfaces to collaborate by providing a wrapper that translates requests.

## Core Pattern
1. Identify Target interface and Adaptee class.
2. Create an Adapter class that implements the Target interface and wraps the Adaptee via composition.
3. The Adapter translates the Target method calls into Adaptee method calls.

## Anti-Pattern to Avoid
Do not rewrite the entire legacy system. Use Adapter to bridge the gap. Avoid using inheritance (Class Adapter); prefer composition (Object Adapter).
