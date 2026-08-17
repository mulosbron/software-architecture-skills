---
name: selecting-uml-diagrams
description: Use when visualizing system behavior, object structure, workflows, or deciding which modeling technique to apply
---

# Selecting UML Diagrams

## Overview
UML diagrams provide a standardized way to visualize both the structural and behavioral aspects of a system. Using the right diagram prevents communication gaps.

## Quick Reference

| Need to show... | Use Diagram | Category | Key Elements |
|---|---|---|---|
| User interactions with features | **Use Case** | Behavioral | Actors, Use Cases, Include, Extend |
| System structure & relationships | **Class** | Structural | Attributes, Methods, Association, Composition |
| Snapshot of objects in runtime | **Object** | Structural | Instances, specific values |
| Time-ordered message flow | **Sequence** | Behavioral | Lifelines, synchronous/asynchronous messages |
| Step-by-step business workflows | **Activity** | Behavioral | Initial node, Decisions, Forks/Joins, Final node |

## Class Diagram Relationships
When creating Class Diagrams, be precise with relationships:
1. **Association**: Direct connection (e.g., Customer -> Order).
2. **Dependency**: Temporary use (e.g., PaymentProcessor uses Order temporarily).
3. **Inheritance**: "Is-a" relationship (e.g., Manager is a User).
4. **Composition**: Strict "Has-a". If parent dies, child dies (e.g., Car has Engine).
5. **Aggregation**: Loose "Has-a". Child can exist independently (e.g., Team has Players).

## Use Case Diagram Relationships
- **Include**: Mandatory sub-step (e.g., "Place Order" *includes* "Process Payment").
- **Extend**: Optional behavior under specific conditions (e.g., "Process Payment" is *extended by* "Apply Coupon").
