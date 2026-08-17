---
name: applying-abstract-factory-pattern
description: Use when the business logic needs to work with different families of related products without depending on their concrete classes (e.g., UI Themes).
---

# Applying Abstract Factory Pattern

## Overview
Lets you produce families of related objects without specifying their concrete classes. Ensures products from the same family are compatible.

## Core Pattern
1. Declare abstract interfaces for each distinct product of the product family.
2. Declare the Abstract Factory interface with creation methods for each abstract product.
3. Create Concrete Factory classes for each product family variation.

## Anti-Pattern to Avoid
Don't use it if you only have one family of products or products aren't related. It adds unnecessary complexity.
