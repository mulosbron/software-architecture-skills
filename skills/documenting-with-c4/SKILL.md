---
name: documenting-with-c4
description: Use when asked to diagram system boundaries, deployable units, or component structure.
---

# Documenting with C4

**Goal:** One diagram at the right level for the audience that asked. Not all four.

## How this repo does it
```bash
python tools/arch_tools.py init-c4 --level context   # or container, component
```
Output is PlantUML using the C4-PlantUML stdlib, saved under `docs/c4/`. Edit the scaffold; keep the include line.

## Pick the level
- Business or product stakeholder → Context.
- Deployment, ops, tech leads → Container.
- Developers of one container → Component.
- Code level: skip unless explicitly asked.

## Boundaries
- "Container" means a deployable unit or data store, not Docker.
- One level per diagram. No classes in a Context diagram.

## Done when
The .puml renders, and every box at Container level and below carries a technology label.
