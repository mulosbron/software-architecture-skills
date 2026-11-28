# Agent Harness & Self-Improving AI Skillset

A production-ready collection of **Skills**, **Tools**, **Scripts** and **Templates** extracted from the **Hermes Agent Harness**, **Loop Engineering**, the **3-Tier Memory Architecture (Procedural / Semantic / Episodic)**, **LLMOps & Eval (Trace → Evaluate → Diagnose → Gate → Ship)** and the **Sales Representative Agent over MCP / REST API** architectures.

---

## Folder Layout

```text
agent-harness-skillset/
├── README.md                              # This documentation
├── templates/                             # Ready-made configuration templates
│   ├── soul.md                            # System prompt and persona definition
│   ├── memory.md                          # Semantic memory (persistent facts & profile)
│   └── claude_desktop_config.json         # MCP server configuration template
├── skills/                                # Procedural memory (SKILL.md files)
│   ├── agent-harness-architect/SKILL.md   # Harness + working memory + 3-tier memory
│   ├── loop-engineering-guardrails/SKILL.md # End-loop guardrails, permission hooks, approval gates
│   ├── self-improving-memory-ops/SKILL.md # 3-tier memory & Consolidation Gate
│   ├── llmops-eval-diagnosis/SKILL.md     # Tracing, evaluation, diagnosis and iteration loop
│   ├── subagent-claude-cli-delegation/SKILL.md # Headless Claude CLI & parallel sub-agent delegation
│   ├── video-prep/SKILL.md                # Example skill: video script formatting
│   └── sales-agent-mcp-deployment/SKILL.md # Sales agent setup over MCP/API & lead extraction
├── tools/                                 # Tool schemas and Python modules
│   ├── tool_schemas.json                  # LLM tool-calling JSON schemas (OpenAI/Anthropic/Gemini compatible)
│   ├── memory_store.py                    # Local 3-tier memory engine (SQLite state.db + memory.md + skills/)
│   ├── skill_manager.py                   # Skill CRUD + automatic skill-suggestion detector after 5+ tool calls
│   └── tracer_eval.py                     # Local LLMOps trajectory tracer (JSONL) + health/quality evaluator
└── scripts/                               # Runnable automation scripts
    ├── init_harness.py                    # Bootstraps a local `.hermes` workspace from scratch
    ├── consolidate_memory.py              # Distills episodic records (state.db) into semantic memory (memory.md)
    ├── run_eval_report.py                 # Analyzes trajectory logs and produces a health/diagnosis report
    ├── delegate_claude_cli.sh             # Sub-agent task delegation via headless Claude CLI
    ├── permission_notify_hook.sh          # Loop hook that sends a desktop notification while waiting for permission
    ├── cron_scheduler.py                  # Local scheduled-task (cron) runner and output logger
    ├── fetch_hackernews.py                # Example script that pulls the top 5 Hacker News stories into Markdown
    └── create_sales_agent_api.sh          # Template for creating a Sales Agent via REST API (curl)
```

> In this repository the `video-prep` example skill lives in `writing-skills/skills/video-script-prep`.

---

## Quick Start

### 1. Initialize the Local Harness Workspace
```bash
python3 scripts/init_harness.py --root ./.hermes
```
This creates `soul.md`, `memories/memory.md`, `skills/`, `state.db` (SQLite episodic memory) and a `logs/` folder under `.hermes/`.

### 2. Use the Memory and Skill Tools
```bash
# Add a persistent fact to semantic memory
python3 tools/memory_store.py --root ./.hermes remember --category preferences --fact "Favorite testing framework is pytest"

# Add an episodic (chat/event) record
python3 tools/memory_store.py --root ./.hermes log-episode --session s1 --role user --content "What can you do?"

# Recall context from memory by keyword (Top-K plain text + SQLite hybrid)
python3 tools/memory_store.py --root ./.hermes recall --query "pytest testing" --top-k 5

# Create a new procedural skill
python3 tools/skill_manager.py --root ./.hermes create --name video-prep --category media --description "Format video scripts in spoken English with inline jargon definitions"
```

### 3. Episodic → Semantic Memory Consolidation (Consolidation Gate)
```bash
python3 scripts/consolidate_memory.py --root ./.hermes --threshold 20
```
When the given threshold (`--threshold`) is exceeded, new episodic events are summarized and distilled into persistent facts inside `memories/memory.md`.

### 4. LLMOps Tracing and Evaluation Report
```bash
python3 scripts/run_eval_report.py --logs ./.hermes/logs/trajectories.jsonl
```
Reports latency (`latency_ms`), token usage, tool-call count, success rate and bottleneck diagnoses (oversized working memory, slow tools, unnecessary RAG calls) for every agent run (`agent_run`).

### 5. Permission Notification Hook & Headless Delegation
```bash
chmod +x scripts/permission_notify_hook.sh scripts/delegate_claude_cli.sh
./scripts/permission_notify_hook.sh "Agent is waiting for permission: file write approval"
./scripts/delegate_claude_cli.sh "Build a Python script that fetches top 5 Hacker News stories to Markdown"
```
