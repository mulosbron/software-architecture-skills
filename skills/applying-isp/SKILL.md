---
name: applying-isp
description: Use when designing interfaces, extracting interfaces from classes, or decoupling clients from unused methods
---

# Applying Interface Segregation Principle (ISP)

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
"Clients should not be forced to depend on methods they do not use." Large, monolithic interfaces create unnecessary coupling.

## Core Pattern
- Split "fat" interfaces into smaller, role-specific interfaces.
- For example, instead of a massive `IProductRepository`, create `IGenericRepository`, `IPhysicalProductRepository`, and `IDigitalProductRepository`.
- A class can implement multiple small interfaces if needed.

## Anti-Pattern to Avoid
A class implementing an interface but leaving half of the methods empty or throwing exceptions because those methods are irrelevant to the class.



