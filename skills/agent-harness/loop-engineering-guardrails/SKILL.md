---
name: loop-engineering-guardrails
description: Implement reliable agent execution loops with explicit termination conditions, end-loop guardrails, human-in-the-loop confirmation gates, and permission notification hooks.
---

> **Nested sub-skill of [`agent-harness`](../SKILL.md).** Paths such as `tools/`, `scripts/`, `presets/`, `configs/`, `prompts/`, `templates/` or `tests/` that do not exist inside this folder resolve from the parent skill root (`../`).
# Loop Engineering & End-Loop Guardrails

Use this skill whenever an agent can invoke tools repeatedly in an autonomous loop (e.g., querying a CRM, issuing refunds, browsing, running terminal commands, or coding).

## Why Loops Fail Without Guardrails
Without explicit stopping criteria, a tool-calling agent will either:
1. Loop indefinitely burning tokens and hitting rate limits.
2. Execute irreversible side effects (e.g., issuing Stripe/Alipay refunds or deleting files) without user approval.
3. Stall silently waiting for a permission prompt while the user is away from the screen.

## Guardrail Checklist

### 1. Define Explicit Stopping Conditions
- **Success Exit**: Verification step passes (e.g., script executes with exit code 0 and expected output).
- **Max Iteration Budget**: Enforce a hard cap (e.g., `max_steps = 10` or `max_tool_calls = 15`).
- **Empty/Stalled Progress Guard**: If a search/browser call returns empty or the same error repeats twice, stop, log the quirk to `memory.md`, and either pivot strategy or ask the user for corrected input (e.g., updated URL).

### 2. Split Read-Only vs. Actionable Endpoints
During planning, classify the user's goal before executing side effects:
- **Report-Only Mode**: Fetch data (e.g., identify 8 customers who did not receive a refund) and return the structured list.
- **Action Mode**: Confirm with the user before triggering mutations (e.g., *"Should I schedule follow-up meetings and trigger Stripe refunds for these 8 customers, or just list them for your review?"*).

### 3. Permission Notification Hooks
When running long coding or terminal loops (such as Claude Code or Hermes CLI):
- Attach a hook (`scripts/permission_notify_hook.sh`) that sends a desktop/OS notification whenever the loop pauses awaiting user permission or finishes a long run.
- This prevents 25+ minutes of idle waiting on a hidden permission dialog.

### 4. Error-to-Memory Feedback
When a tool fails due to an environmental quirk (wrong URL, auth expiry, CLI flag mismatch), record the root cause in `memories/memory.md` so future loops avoid repeating the mistake.
