# Software Architecture Skills

Opinionated architecture guidance plus CLI tools. Each skill states a goal, this repo's default position, boundaries, and a definition of done. Skills tell you what this repo prefers, not what the concepts mean.

## Skills

| Skill | Use when |
|---|---|
| `skills/evaluating-microservices-readiness` | User wants microservices. Challenge first; default is a modular monolith. |
| `skills/designing-modular-monoliths` | Structuring a new app or carving modules from a tangled one. |
| `skills/modeling-with-ddd` | Subdomains, bounded contexts, ACLs, aggregates, and invariants. |
| `skills/structuring-clean-architecture` | Ports-and-adapters dependency boundaries for complex domain modules. |
| `skills/structuring-monorepos` | Multi-package workspaces, affected CI, caching, and package boundaries. |
| `skills/balancing-architectural-tradeoffs` | Choosing between styles or quality attributes. |
| `skills/choosing-api-style` | REST vs GraphQL vs gRPC vs WebSockets. |
| `skills/protecting-and-sizing-apis` | Capacity sizing (QPS/storage), rate limiting, distributed IDs. |
| `skills/choosing-database-type` | Picking a database or splitting storage. |
| `skills/choosing-message-broker` | Adding async messaging; RabbitMQ vs Kafka. |
| `skills/designing-cqrs-and-event-sourcing` | Separating read/write models, event streams, projections, and sagas. |
| `skills/designing-idempotent-mutations` | Idempotency keys, optimistic locks, payments/ledgers, Saga vs 2PC. |
| `skills/modeling-threats-and-privacy` | STRIDE threat modeling, trust boundaries, PII minimization, and retention. |
| `skills/selecting-design-patterns` | Which GoF pattern, or whether one is justified at all. |
| `skills/verifying-solid-compliance` | Reviewing code for SOLID violations. |
| `skills/refactoring-god-classes` | Splitting an oversized class safely. |
| `skills/modernizing-legacy-systems` | Incremental Strangler Fig migrations, characterization tests, and tech debt. |
| `skills/writing-adrs` | Any hard-to-reverse decision; "why is it built this way?" |
| `skills/documenting-with-c4` | Diagramming boundaries, deployables, components. |
| `skills/deploying-with-containers` | Dockerfile, Kubernetes manifests, CI pipeline, rollout. |
| `skills/ai-factory-builder` | Turning recurring digital team workflows into specific, shared, scrutinized AI factories (7-trait scorer, shadow-run plan, evals). |
| `skills/agent-harness` | Self-improving agent harness router: 3-pillar memory, loop guardrails, LLMOps eval loop, headless Claude CLI delegation, MCP sales agent (6 sub-skills, `tools/memory_store.py`, `tools/tracer_eval.py`). |
| `skills/mcp-connector-setup` | Connecting Gmail/Drive/Calendar/Zapier/PayPal/QuickBooks to Claude via native connectors or custom remote MCP servers; Claude Projects setup guide. |
| `skills/claude-code-github-launcher` | Cloning, Dockerizing and iterating GitHub repos from the terminal with Claude Code (`scripts/github_claude_launcher.sh`, `scripts/claude_api_runner.py`). |

## Tools (`tools/`)

```bash
python tools/arch_tools.py adr-new "Title"            # scaffold ADR in docs/adrs
python tools/arch_tools.py adr-list
python tools/arch_tools.py adr-supersede <id> "Title"
python tools/arch_tools.py init-c4 --level context|container|component --name X
python tools/arch_tools.py check-god-classes <dir> [--threshold 500]
python tools/arch_tools.py check-module-boundaries <src-dir>
python tools/devops_tools.py init-docker [--stack node|python|go|java]
python tools/devops_tools.py init-k8s <service> [--replicas 3]
python tools/devops_tools.py init-pipeline [--provider github|gitlab]
```

Checks exit 1 on findings. Scaffolds refuse to overwrite without `--force`.

## Two modes

**New project (no code yet):** ask stage, team size, and the one non-negotiable quality attribute. Then decide in order: style → module structure → storage → API/messaging → C4 context diagram → deployment scaffolds. One ADR per decision.

**Existing project:** read before proposing. Run `check-god-classes` and `check-module-boundaries`, read `docs/adrs` if present, then ground every finding in a file and line. Refactors do not change behavior in the same PR. Migrations are incremental.

If unclear which mode applies, look at the workspace; do not ask.

## Working rules

- Record every architectural decision with `adr-new` as it is made, not at the end.
- For a theoretical question, answer directly. No interview, no scan.
- Do not spawn parallel subagents for an audit unless the user asks for a full-codebase review.
- Scope stays with the user: these skills set defaults, the user can override them. Say when they do, and record it in the ADR.
