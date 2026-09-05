---
name: applying-template-method-pattern
description: Use when you want to define the skeleton of an algorithm but let subclasses override specific steps.
---

# Applying Template Method Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

## Core Pattern
1. Abstract Class contains a `final` template method defining the algorithm steps.
2. Some steps are implemented in the abstract class, others are declared `abstract`.
3. Subclasses implement the abstract steps.

## Anti-Pattern to Avoid
Don't allow subclasses to change the overall structure of the algorithm. Override only the specific hooks/steps.



