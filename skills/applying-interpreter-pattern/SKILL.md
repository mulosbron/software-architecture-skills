---
name: applying-interpreter-pattern
description: Use when you need to parse and evaluate sentences in a simple language, grammar, or rules engine.
---

# Applying Interpreter Pattern

## Agent Execution Flow (IMPORTANT)
1. **Information Gathering:** Ask clarifying questions to determine context and constraints before proposing a solution.
2. **Context Scanning:** Scan the workspace (`list_dir`, `view_file`) to understand current architecture and code.
3. **Analyze & Propose:** Once context is fully understood, formulate your architecture strategy or design pattern recommendation.

## Overview
Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences.

## Core Pattern
1. Define Abstract Expression interface with `interpret()`.
2. Create Terminal Expressions (leaves).
3. Create Non-terminal Expressions (rules) that compose other expressions.
4. Client builds an Abstract Syntax Tree (AST) and evaluates it.

## Anti-Pattern to Avoid
Don't use it for complex languages (use a real parser/compiler). It creates too many classes for heavy grammars.



