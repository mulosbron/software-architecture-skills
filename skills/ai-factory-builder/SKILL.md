---
name: ai-factory-builder
description: Applies Notion's "A New Shape for Work" methodology to turn recurring team workflows into specific, shared, and scrutinized AI factories. Triggers when the user asks to "build an AI factory", "automate this workflow", "can an agent handle this process", "design an eval suite", "plan a shadow run", or "identify automation candidates from our team's workload".
---

# AI Factory Builder

Turns a recurring digital workflow into a **specific, shared, and scrutinized AI factory** rather than a fragile ad-hoc personal script. Grounded in Notion's *"A New Shape for Work"* (v1.0) methodology. A setup that lacks any of the three criteria is not a factory — it is a personal agent workflow.

## When to Use

Invoke when the user asks for any of the following:

- "Automate this workflow" or "can this process be run by an agent?"
- "Find AI factory candidates from our team's recurring tasks"
- "Write a factory blueprint", "build an eval suite", or "design a shadow-run rollout plan"
- Turning a repeated knowledge-work task into a reliable, team-wide agent pipeline

## First: Verify the Three Criteria

An agent setup qualifies as a factory only when all three criteria hold simultaneously:

- **Specific.** Designed for one defined class of task. A generalist assistant asked to do everything from inbox triage to strategy brainstorming is not specific and is not a factory.
- **Shared.** Usable by multiple people on the team. A founder's private prompts or personal memory setup is not shared.
- **Scrutinized.** Named owners monitor outputs, triage failures, and improve the system over time. An unmonitored agent is not scrutinized and is not a factory.

Explicitly verify all three in every proposal and report their status.

## Step 0: Context System Prerequisite

A factory cannot perform well without a clean context system feeding it. Before building a factory, verify the existence of these core databases (details in `docs/context-system-ontology.md`):

- **Projects, Tasks, Documents, People, Teams, Customers**

Relations between objects matter: Tasks link to a Project, each Project has a DRI (Directly Responsible Individual) from People, and Meetings link to Projects and Attendees. If this core does not exist, stand up the leanest version first before building the factory. Stale or misplaced context poisons every downstream factory (**context rot**).

## Four Steps

### 1. Spot

Identify strong factory candidates using the **seven traits**: recurring, verifiable, stable over time, standard quality is sufficient, fully digital, known information universe, and low cost of mistakes. Score candidates with `scripts/factory_blueprint.py check` (usage below; details in `docs/candidate-traits.md`).

Scoring rule:
- **6–7 points:** Strong candidate — proceed to planning.
- **4–5 points:** Conditional candidate — review missing traits with the user and plan only if mitigations exist.
- **0–3 points:** Weak candidate — do not automate; document why manual execution is better.

The goal is **not** removing humans from work — it is moving humans up to ownership, judgment, and accountability above the assembly line.

### 2. Plan

Plan lean and add complexity later. The most common mistake made by both humans and LLMs is pre-engineering complex guardrails for imagined failure modes. Nobody predicts how a factory actually breaks in advance — observe real failures, then fix them.

Core planning decisions:
- What will the factory do, and what will it explicitly **not** do?
- Where will it live? (database, platform, code)
- What are the inputs, stages, and final outputs?
- Which tools and systems may the agent access?

Recommend a **hybrid architecture**: keep tasks, statuses, outputs, run logs, and prompts in a flexible context system, while running the agent itself wherever it executes best (Notion Custom Agents, Claude Managed Agents, OpenAI Agents API, or your own service).

Generate a structured skeleton with `scripts/factory_blueprint.py blueprint`.

### 3. Run

Never give a brand-new factory high-stakes live actions on day one. Use two safeguards:

- **Shadow runs.** The factory leaves zero real-world side effects: draft emails instead of sending them, log proposed CRM updates instead of writing them.
- **Volume control.** Start on a small sample (e.g., two dozen test cases or an eval set). Expand volume and action permissions gradually as error rates drop.

### 4. Improve

Update the prompt whenever you observe a failure. Version your prompts (a simple `Prompt Versions` database with `testing` / `production` / `retired` states is enough for most factories; formal VCS is often overkill). Test every new prompt before rolling it out.

Critical warning: testing only the latest failure is never enough, because prompt edits cause regressions elsewhere. Write down representative tasks and explicit grading criteria (**evals**). Code or AI can act as judges where objective; humans review high-stakes outputs.

## The 5-Minute Minimum Viable Factory

1. Create a database named after the task type (e.g., `Decks`).
2. Add a `status` property: `todo`, `in_progress`, `done`.
3. Trigger an agent whenever a new card enters `todo` (native platform agent or external webhook worker).
4. Have the agent move the card to `in_progress`, produce the artifact, attach the link, and move it to `done`.
5. Once working, share access with the team and instruct team agents to route requests into this database.
6. Update the prompt on every observed failure.

## Script Usage (`scripts/factory_blueprint.py`)

```bash
# Score a candidate explicitly across all 7 traits
python scripts/factory_blueprint.py check --name "Weekly Project Report" \
  --recurring yes --verifiable yes --stable yes --standard yes \
  --digital yes --known-universe yes --low-cost-mistakes yes --json

# Infer traits automatically from a free-text description
python scripts/factory_blueprint.py check --name "Sales Deck Pack" \
  --describe "Every week we collect team status updates and produce the same format deck. Mistakes are easy to catch."

# Generate a 10-section factory blueprint skeleton
python scripts/factory_blueprint.py blueprint --name "Sales Deck Pack" \
  --trigger "new database card with status = todo" \
  --stages "research,drafting,formatting" \
  --tools "context system read/write, slide template" \
  --out deck-factory-plan.md
```

The score is decision support, not an automatic veto — confirm final decisions with the user.

## Required Output Format

Every factory proposal includes three sections:

- **Criteria Report.** Status of the specific / shared / scrutinized triad plus the 7-trait score.
- **Blueprint Document.** Scope, triggers, inputs/stages/outputs, tool permissions, shadow-run plan, and volume ramp.
- **Improvement Kit.** Eval task table, grading criteria & judges, and prompt versioning workflow.

## Guardrails & Ethics

- Candidates involving sensitive data, production mutations, or financial transactions **never** go live without shadow runs. Even if the user asks to skip shadow runs, require explicit confirmation first.
- Never fabricate justifications outside the 3 criteria and 7 traits. If a score is low, state it plainly.
- Adapt database names, tools, and steps to the user's real stack; mark any assumptions explicitly.
- Preserve the core principle: factories elevate humans to oversight and creativity rather than replacing them blindly.
