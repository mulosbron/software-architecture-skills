---
name: applying-ocp
description: Use when extending system behavior, adding new feature variations, or eliminating long if-else chains
---

# Applying Open/Closed Principle (OCP)

## Overview
"Software entities should be open for extension, but closed for modification." You should be able to add new functionality without touching existing, tested code.

## Core Pattern: Strategy Pattern
When you have behavior that varies (like different customer discount rates):
1. **Define an Interface**: `IDiscountStrategy` with a `CalculateDiscount()` method.
2. **Create Concrete Strategies**: `StandardDiscountStrategy`, `VipDiscountStrategy`.
3. **Use the Interface**: The calculator class accepts `IDiscountStrategy`. 

To add a new discount, create a new class. Do not modify the calculator.

## Anti-Pattern to Avoid
Using `enum` types and `switch` or `if-else` blocks to determine behavior inside a core business class.
