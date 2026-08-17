---
name: applying-infrastructure-as-code
description: Use when managing or provisioning cloud infrastructure and you need to avoid manual configurations (configuration drift).
---

# Applying Infrastructure as Code (IaC)

## Overview
IaC is the practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.

## Core Pattern
1. **Declarative Definitions**: Define what the infrastructure should look like (e.g., using Terraform, CloudFormation) rather than writing imperative scripts on how to create it.
2. **Version Control**: Store these definition files in a Git repository. Every infrastructure change must go through a Pull Request and code review.
3. **Automation**: Use an automation server to apply the changes to the cloud provider automatically.

## Anti-Pattern to Avoid
Don't use the cloud provider's web console (UI) to manually create or modify servers and databases. This leads to configuration drift and makes disaster recovery nearly impossible.
