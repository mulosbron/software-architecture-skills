---
name: self-improving-memory-ops
description: Manage a 3-pillar AI agent memory architecture (Procedural, Semantic, Episodic) with token-efficient retrieval, hybrid SQL+keyword/RAG search, and gated consolidation using auxiliary models.
---

> **Nested sub-skill of [`agent-harness`](../SKILL.md).** Paths such as `tools/`, `scripts/`, `presets/`, `configs/`, `prompts/`, `templates/` or `tests/` that do not exist inside this folder resolve from the parent skill root (`../`).
# Self-Improving 3-Pillar Memory Operations

Use this skill to design, query, and maintain long-term memory without exploding token costs or degrading response latency.

## The Three Memory Pillars

| Pillar | What It Stores | Storage Format | Retrieval Method |
| :--- | :--- | :--- | :--- |
| **Procedural Memory** | How the agent should act; repeatable workflows & style rules | Plain Markdown files (`skills/<cat>/<name>/SKILL.md`) | Intent/skill name match loaded on demand |
| **Semantic Memory** | Durable facts, user profile, company info, learned quirks | Plain text (`memories/memory.md`) or Vector Store | Top-K keyword matching (local) or RAG similarity search |
| **Episodic Memory** | Dated events, full chat history, transaction/complaint logs | SQLite (`state.db`) or Vector + Relational DB | Hybrid: SQL time/entity filters + semantic/keyword search |

## Retrieval Decision Rules
1. **Skip Retrieval on General Knowledge**: Do not query memory databases for static world facts (e.g., *"When was OpenAI founded?"*) — the LLM already knows this and skipping retrieval cuts latency.
2. **Use SQL for Time/Entity Bounds**: For queries like *"Last 10 conversations with customer X"*, run a deterministic SQL query on `state.db`.
3. **Use Hybrid SQL + Semantic/Keyword Search**: For queries like *"Last 20 unresolved product quality complaints"*, filter by timeframe/status in SQL and rank text relevance via top-k keyword or RAG search.

## Consolidation Gate (Episodic → Semantic)
Never summarize every single message into Semantic Memory (that duplicates storage and wastes tokens). Instead:
1. **Set a Gate Threshold**: Trigger consolidation only after `N` new episodes (e.g., 20 personal conversations or 2,000 high-volume e-commerce chats).
2. **Use a Cheaper Auxiliary Model**: Route the batch of raw episodes to a fast, low-cost summarizer model to **distill durable facts** (pivots, preferences, recurring customer issues).
3. **Deduplicate & Append**: Merge distilled facts into `memories/memory.md` and mark processed episodes as consolidated in `state.db`.

## Self-Learning Skill Trigger
- **Explicit Save**: Immediately write a `SKILL.md` when the user asks to remember a workflow or formatting rule.
- **Proactive Save**: Whenever an agent run succeeds after a complex iterative loop (**≥ 5 tool calls**), propose saving the verified sequence as a new procedural skill.
