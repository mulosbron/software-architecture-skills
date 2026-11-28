---
name: agent-harness-architect
description: Design and implement a complete AI Agent Harness controlling an LLM ("the horse") with Working Memory, 3-Pillar Persistent Memory, Tool Loop Engineering, Gateway interfaces, and LLMOps/Eval observability.
---

> **Nested sub-skill of [`agent-harness`](../SKILL.md).** Paths such as `tools/`, `scripts/`, `presets/`, `configs/`, `prompts/`, `templates/` or `tests/` that do not exist inside this folder resolve from the parent skill root (`../`).
# Agent Harness Architect

Use this skill when designing, auditing, or implementing an autonomous AI agent system (local-first like Hermes Agent or cloud-hosted via LangGraph/PydanticAI).

## Core Principle
An LLM is a probabilistic next-token engine ("a powerful horse") that knows general world knowledge but does not know the user, the business, or how to act reliably. The **Harness** is the deterministic control layer around the LLM that bounds randomness and turns ephemeral runs into a self-improving system.

## Architecture Blueprint

### 1. Gateway Layer (Entry Points)
Expose the same agent harness through one or more gateways:
- **Desktop / CLI UI**: Local interactive sessions.
- **Messaging Gateways**: WhatsApp, Slack, Telegram, or Web Chat routing messages into the same local/VPS harness.
- **Scheduled Triggers**: Cron jobs for unattended recurring tasks (always persist output to logs or push via gateway so results are not lost in terminal UI).

### 2. Working Memory (Context RAM)
Assemble a focused context window for every ephemeral agent run:
1. **System Prompt (`soul.md`)**: Identity, persona, and operating guardrails.
2. **User Prompt + Current Chat History**: Immediate turn context.
3. **Retrieved Procedural Memory (`skills/*/SKILL.md`)**: Only skills relevant to the task.
4. **Retrieved Semantic Memory (`memories/memory.md`)**: Top-K durable facts & user profile.
5. **Retrieved Episodic Memory (`state.db`)**: Relevant dated events or past session snippets.

### 3. Tool Loop Engineering
Equip the agent with bounded tools:
- Terminal / Shell execution
- Browser / Web fetch
- Sub-agent delegation (`delegate_task`)
- Cron scheduler
- Skill & Memory management tools
- External MCP servers (CRM, Payments, Knowledge Base)

Always pair tool execution with **End-Loop Guardrails** (see `loop-engineering-guardrails`).

### 4. Persistence & Self-Improvement
- Store every completed run into **Episodic Memory** (`state.db`).
- Run a **Consolidation Gate** (every N sessions/events) with a cheaper auxiliary summarizer model to distill durable facts into **Semantic Memory** (`memory.md`).
- Trigger **Procedural Skill creation** after difficult multi-step tasks (5+ tool calls) or repeated workflows.

### 5. Observability & LLMOps
Export structured run trajectories (`.hermes/logs/trajectories.jsonl`) capturing prompts, retrievals, tool calls, latencies, and token counts so an Eval/Diagnosis loop can continuously tune prompts, model configs, and retrieval knobs.
