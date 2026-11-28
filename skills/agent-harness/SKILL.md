---
name: agent-harness
description: Router for building self-improving AI agent harnesses (Hermes-style): harness + working memory architecture, 3-pillar persistent memory (procedural skills / semantic memory.md / episodic SQLite), loop engineering with end-loop guardrails and permission hooks, LLMOps trace -> evaluate -> diagnose -> gate -> ship loop, headless Claude CLI sub-agent delegation, and MCP/REST sales-agent deployment. Use when designing or debugging an agent runtime, its memory, its tool loop, or its eval pipeline.
---

# Agent Harness & Self-Improving Agent Skillset

The LLM is the horse; the harness (tools, memory, loop control, gateways, observability) decides whether it does useful work. Load only the sub-skill that matches the task:

| Task | Sub-skill |
|---|---|
| Design the whole runtime (soul.md, working memory, tool loop, gateways, eval hooks) | [`agent-harness-architect`](agent-harness-architect/SKILL.md) |
| Termination conditions, max-iteration guards, human approval gates, permission notifications | [`loop-engineering-guardrails`](loop-engineering-guardrails/SKILL.md) |
| Procedural / semantic / episodic memory, hybrid recall, gated consolidation | [`self-improving-memory-ops`](self-improving-memory-ops/SKILL.md) |
| Trace -> Evaluate -> Diagnose -> Gate -> Ship/Fix quality loop | [`llmops-eval-diagnosis`](llmops-eval-diagnosis/SKILL.md) |
| Parallel / background work via headless `claude -p` sessions | [`subagent-claude-cli-delegation`](subagent-claude-cli-delegation/SKILL.md) |
| 24/7 sales agent over MCP or REST, lead extraction | [`sales-agent-mcp-deployment`](sales-agent-mcp-deployment/SKILL.md) |

## Quick start (local `.hermes` workspace)

```powershell
python scripts/init_harness.py --root ./.hermes
python tools/memory_store.py --root ./.hermes remember --category preferences --fact "Favorite test framework is pytest"
python tools/memory_store.py --root ./.hermes recall --query "pytest" --top-k 5
python scripts/consolidate_memory.py --help
python scripts/run_eval_report.py --help
```

Resources: `templates/` (`soul.md`, `memory.md`, `claude_desktop_config.json`), `tools/` (`memory_store.py`, `skill_manager.py`, `tracer_eval.py`, `tool_schemas.json`), `scripts/` (init, consolidation, eval report, cron, Claude CLI delegation, permission hook, sales-agent API). The `video-prep` example skill from the original bundle lives in `writing-skills/skills/video-script-prep`.

## Rules

- Every loop needs an explicit stop condition and an iteration/token budget; destructive tools go behind a human confirmation gate.
- Never write secrets into `memory.md` or `soul.md`; keep API keys in environment variables.
- Promote an episodic pattern into a procedural skill only after it repeats (the `skill_manager.py` 5+ tool-call detector) and passes an eval gate.
- Related packs: `software-architecture-skills/skills/ai-factory-builder`, `mcp-connector-setup`, `claude-code-github-launcher`.

---

## Integrated Skillset (sub-skills, scripts & tools)


| Sub-skill | Use it for |
|---|---|
| [`agent-harness-architect`](agent-harness-architect/SKILL.md) | Design and implement a complete AI Agent Harness controlling an LLM ("the horse") with Working Memory, 3-Pillar Persistent Memory, Tool Loop Engineering, Gateway interfaces, and LLMOps/Eval observability. |
| [`llmops-eval-diagnosis`](llmops-eval-diagnosis/SKILL.md) | Run a structured LLMOps feedback loop (Trace -> Evaluate -> Diagnose -> Gate -> Ship or Fix) to measure agent quality, latency, token efficiency, and tool reliability. |
| [`loop-engineering-guardrails`](loop-engineering-guardrails/SKILL.md) | Implement reliable agent execution loops with explicit termination conditions, end-loop guardrails, human-in-the-loop confirmation gates, and permission notification hooks. |
| [`sales-agent-mcp-deployment`](sales-agent-mcp-deployment/SKILL.md) | Deploy a 24/7 Sales Representative AI Agent for a business or SaaS product via MCP server (Claude Desktop/Code) or REST API, enrich its knowledge base, verify domain ownership, and extract structured leads. |
| [`self-improving-memory-ops`](self-improving-memory-ops/SKILL.md) | Manage a 3-pillar AI agent memory architecture (Procedural, Semantic, Episodic) with token-efficient retrieval, hybrid SQL+keyword/RAG search, and gated consolidation using auxiliary models. |
| [`subagent-claude-cli-delegation`](subagent-claude-cli-delegation/SKILL.md) | Delegate isolated coding, bug-fixing, or parallel research tasks to background sub-agents or headless Claude Code CLI sessions and verify their outputs. |

**Bundled resources:** `scripts/` · `templates/` · `tools/`

Original skillset overview: [`SKILLSET-README.md`](SKILLSET-README.md). Read the matching sub-skill before running its tools; tool CLIs are relative to this skill folder.
