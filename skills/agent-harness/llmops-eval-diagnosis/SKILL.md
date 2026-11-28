---
name: llmops-eval-diagnosis
description: Run a structured LLMOps feedback loop (Trace -> Evaluate -> Diagnose -> Gate -> Ship or Fix) to measure agent quality, latency, token efficiency, and tool reliability.
---

> **Nested sub-skill of [`agent-harness`](../SKILL.md).** Paths such as `tools/`, `scripts/`, `presets/`, `configs/`, `prompts/`, `templates/` or `tests/` that do not exist inside this folder resolve from the parent skill root (`../`).
# LLMOps, Tracing & Evaluation Pipeline

Use this skill to move an agent harness from "works in a demo" to a continuously monitored, self-improving production system.

## The 5-Stage LLMOps Loop

### Stage 1: Trace (Trajectory Export)
Instrument every `agent_run` (from user input to final reply, regardless of how many internal tool calls occur) as a tree of events in JSONL or an observability platform (Langfuse, LangSmith):
- User prompt & session ID
- Memory retrievals performed (which pillar, how many tokens injected)
- Tool calls (tool name, arguments, duration in ms, success/error status)
- Total latency (`latency_ms`) and token usage (`prompt_tokens`, `completion_tokens`)

### Stage 2: Evaluate ("Was It Good?" & "Was It Healthy?")
Score every trace across two dimensions:
- **Deterministic Health Checks**:
  - Latency within SLA (e.g., `< 5000ms` for interactive chat; flag `20s+` spikes).
  - Token usage within budget.
  - Expected tool actually triggered (e.g., meeting scheduler or refund API called when requested).
  - Zero unhandled exceptions or guardrail violations.
- **Quality Checks (LLM-as-a-Judge)**:
  - Score task completion, factual grounding, and persona/style adherence on a 1–5 rubric.

### Stage 3: Diagnose Root Causes
When a metric fails, inspect the trace tree before changing code:
- **High Latency**: Is a single tool call hanging, or is Working Memory bloated?
- **High Token Cost**: Is the agent running full RAG/memory retrieval on simple factual questions that need zero retrieval?
- **Missing Tool Trigger**: Did the system prompt (`soul.md`) or tool schema description fail to clarify when to call the tool?

### Stage 4: Gate Decision
- **Pass / Minor Tuning Needed** → Ship updated system prompt (`soul.md`), model config (e.g., auxiliary model for summarization), or retrieval `top_k` parameters directly back into the harness.
- **Deeply Broken** → Route the trace to a coding agent to fix the underlying bug, then **re-run → re-trace → re-evaluate** before shipping.
