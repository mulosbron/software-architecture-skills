---
name: subagent-claude-cli-delegation
description: Delegate isolated coding, bug-fixing, or parallel research tasks to background sub-agents or headless Claude Code CLI sessions and verify their outputs.
---

> **Nested sub-skill of [`agent-harness`](../SKILL.md).** Paths such as `tools/`, `scripts/`, `presets/`, `configs/`, `prompts/`, `templates/` or `tests/` that do not exist inside this folder resolve from the parent skill root (`../`).
# Sub-Agent & Headless Claude CLI Delegation

Use this skill when a user request benefits from parallel research or delegating heavy software engineering tasks to a specialized coding CLI.

## When to Delegate
1. **Parallel Research**: Spawn 2+ independent sub-agents concurrently when comparing frameworks, architectures, or data sources (e.g., researching `lm-eval-harness` and `VLM architectures` simultaneously).
2. **Headless Coding**: Delegate code generation, refactoring, or GitHub bug fixes to a headless coding CLI (`claude -p "..."`) so the main harness stays focused on orchestration and verification.

## Standard Headless Delegation Workflow
1. **Scope the Task Clearly**: Provide exact input/output paths, runtime constraints, and verification requirements (e.g., *"Write `fetch_hackernews.py` to fetch the top 5 Hacker News stories into Markdown and verify it runs without errors"*).
2. **Invoke Headless CLI**:
   ```bash
   ./scripts/delegate_claude_cli.sh "<clear, self-contained coding prompt>"
   ```
3. **Verify Execution**: Never trust generated code without running it. Execute the resulting script via the terminal tool and inspect stdout/stderr and exit code.
4. **Return Verified Results**: Summarize the verified output to the user and log any reusable pattern to Procedural Memory if the task required 5+ iterative steps.
