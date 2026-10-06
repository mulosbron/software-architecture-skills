# Software Architecture Skills for AI Agents

Twelve opinionated architecture skills and a small CLI, built for coding agents that read `AGENTS.md`.

## Why only twelve

The first version had 76 skills. Most were textbook summaries of things a current model already knows (what a Decorator is, what the three pillars of observability are). Those files added tokens, not judgment. They were removed.

What remains passes one test: *could the model not know this on its own?* Each skill now carries the things a model cannot infer:

- **a default position** this repo takes (Postgres unless measured otherwise; monolith unless there are 3+ teams),
- **boundaries** it must not cross (no shared tables across services; no refactor without characterization tests),
- **a definition of done**, and
- **the repo's own tools** that produce the artifact.

## Skills

| Skill | Use when |
|---|---|
| `evaluating-microservices-readiness` | User wants microservices. Pushes back first. |
| `designing-modular-monoliths` | Structuring a new app or carving modules out. |
| `balancing-architectural-tradeoffs` | Choosing between styles or quality attributes. |
| `choosing-api-style` | REST vs GraphQL vs gRPC vs WebSockets. |
| `choosing-database-type` | Picking or splitting storage. |
| `choosing-message-broker` | Adding async; RabbitMQ vs Kafka. |
| `selecting-design-patterns` | Which GoF pattern, if any. |
| `verifying-solid-compliance` | Reviewing code for SOLID violations. |
| `refactoring-god-classes` | Splitting an oversized class safely. |
| `writing-adrs` | Recording decisions; answering "why is it built this way?" |
| `documenting-with-c4` | Context, container, component diagrams. |
| `deploying-with-containers` | Dockerfile, Kubernetes, CI pipeline, rollout. |

## Tools

```bash
python tools/arch_tools.py adr-new "Use PostgreSQL for orders"
python tools/arch_tools.py adr-list
python tools/arch_tools.py adr-supersede 3 "Move orders to CockroachDB"
python tools/arch_tools.py init-c4 --level container --name Shop
python tools/arch_tools.py check-god-classes src --threshold 400
python tools/arch_tools.py check-module-boundaries src
python tools/devops_tools.py init-docker            # detects node / python / go / java
python tools/devops_tools.py init-k8s order-service
python tools/devops_tools.py init-pipeline --provider github
```

Checks exit 1 when they find something, so they work in CI. Scaffolds never overwrite without `--force`. Python 3.8+, no dependencies.

## How to use it

The skills behave differently depending on whether there is code yet. Tell the agent which case you are in; it changes the first thing it does.

### Starting a new project

The agent interviews before it designs. Expect three questions (stage, team size, the one non-negotiable) and then decisions in this order, each ending in an ADR:

```
1. Style        -> balancing-architectural-tradeoffs, evaluating-microservices-readiness
2. Structure    -> designing-modular-monoliths
3. Storage      -> choosing-database-type
4. Interface    -> choosing-api-style, choosing-message-broker (only if async is justified)
5. Diagram      -> documenting-with-c4  (init-c4 --level context)
6. Shipping     -> deploying-with-containers (init-docker, init-k8s, init-pipeline)
```

Example prompt:

> New project: B2B invoicing SaaS, 2 developers, must ship a demo in 6 weeks. Set up the architecture.

What you get: a module layout, `docs/adrs/0001..000N`, a context diagram, a Dockerfile and manifests. What you will not get: microservices, unless you overrule the agent and it records that in the ADR.

### Working on an existing project

The agent reads before it proposes. It runs the checks first and grounds every suggestion in a file and line:

```
Review       -> check-god-classes, check-module-boundaries, verifying-solid-compliance
Change       -> writing-adrs (why), then the relevant choosing-* or designing-* skill
Refactor     -> refactoring-god-classes (tests first, one extraction at a time)
Migrate      -> evaluating-microservices-readiness (incremental only, never a rewrite)
Document     -> documenting-with-c4 at the level the audience needs, adr-list for history
```

Example prompts:

> Audit `src/` for architectural problems and rank them.

> We want to move notifications out of the monolith into its own service. Evaluate and, if it makes sense, plan it.

> Why does this project use RabbitMQ? (the agent reads `docs/adrs` before answering)

What you get: findings with locations, a plan that does not change behavior in the same PR, and an ADR for any decision that is hard to reverse.

### Overriding a default

Every skill states the repo's default. Say so when you want something else, and the agent will proceed and write the ADR with your reason:

> I know the default is Postgres. Use MongoDB; the schema is per-tenant and never joined.

## Install

Clone into your agent's skills directory (for example `~/.agents/`) or copy `AGENTS.md`, `skills/`, and `tools/` into a project. Agents that read `AGENTS.md` pick the skills up automatically.

## Adding a skill

Keep the format: a one-line `description` starting with "Use when", a goal, the repo's default, boundaries, done criteria. Under 30 lines. If a section only explains a concept, delete it.
