# Context System Ontology

An AI factory cannot perform reliably without a clean context system feeding it. This document defines the leanest durable context structure to establish before or alongside your first factory.

## Six Jobs of a Context System

1. Store the organization's core knowledge and operational state.
2. Keep everything organized with clear, predictable homes.
3. Govern data with granular permissions and version history.
4. Surface information in whatever view each team needs.
5. Provide strong human collaboration (comments, notifications, desktop + mobile).
6. Integrate cleanly with any AI agent.

## Core Databases

Do not start with an over-engineered ontology. Start with a small core set and wire clean relations between them:

| Database | Typical Properties | Relations |
|---|---|---|
| **Projects** | Name, status, DRI (Directly Responsible Individual), date range | Tasks, Documents, Meetings, Customers |
| **Tasks** | Name, status (`todo` / `in_progress` / `done`), assignee, project | Projects, People |
| **Documents** | Title, type, owner, version | Projects, People |
| **People** | Role, manager (derives org chart), team | Teams, Projects |
| **Teams** | Name, members | People, Projects |
| **Customers** | Name, status, primary contact | Projects, Meetings |

Derived views (like org charts or project rollups) emerge automatically from these relations without custom glue code.

## Fractal Structure

Even ad-hoc databases outside the core benefit from light structure. A versioned handbook can live in a draft tracker with version numbers and timestamps so agents can diff versions on demand. Making structure effortless should be the default behavior of the context system.

## Syncs

Two ways to centralize operational knowledge:

- **Managed syncs.** Native platform connectors (e.g., Salesforce, Slack, calendars).
- **Worker syncs.** Lightweight scheduled scripts or agent workers pulling from systems without native connectors.

You can keep using external tools, but granting every agent direct access to dozens of scattered APIs multiplies failure modes and governance overhead. Sync data into a single managed access layer — a **context warehouse**.

## Permissions

- Assign permissions to **groups**, not individuals, so role changes and onboarding update access automatically.
- Do not duplicate an entire database just to hide one sensitive field — use **column-level permissions** when available.
- Use **row-level permissions** so individuals only see their own records where required (e.g., performance reviews).

## Validation

A context system should block low-quality records at entry: required fields, schema/format checks, automated checks verifying product specs answer core questions, routing stray pages into canonical databases, and propagating new decisions across linked docs.

## Context Rot

The #1 enemy of any AI factory is **bad context**: stale, incomplete, misfiled, or outdated records. With agents, cleanup becomes continuous. Every factory blueprint should include a context-rot check: which sources are scanned, how often, how staleness is flagged, and who resolves it.
