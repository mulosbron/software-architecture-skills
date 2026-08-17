---
name: applying-template-method-pattern
description: Use when you want to define the skeleton of an algorithm but let subclasses override specific steps.
---

# Applying Template Method Pattern

## Overview
Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

## Core Pattern
1. Abstract Class contains a `final` template method defining the algorithm steps.
2. Some steps are implemented in the abstract class, others are declared `abstract`.
3. Subclasses implement the abstract steps.

## Anti-Pattern to Avoid
Don't allow subclasses to change the overall structure of the algorithm. Override only the specific hooks/steps.
