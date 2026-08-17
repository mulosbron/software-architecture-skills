---
name: applying-isp
description: Use when designing interfaces, extracting interfaces from classes, or decoupling clients from unused methods
---

# Applying Interface Segregation Principle (ISP)

## Overview
"Clients should not be forced to depend on methods they do not use." Large, monolithic interfaces create unnecessary coupling.

## Core Pattern
- Split "fat" interfaces into smaller, role-specific interfaces.
- For example, instead of a massive `IProductRepository`, create `IGenericRepository`, `IPhysicalProductRepository`, and `IDigitalProductRepository`.
- A class can implement multiple small interfaces if needed.

## Anti-Pattern to Avoid
A class implementing an interface but leaving half of the methods empty or throwing exceptions because those methods are irrelevant to the class.
