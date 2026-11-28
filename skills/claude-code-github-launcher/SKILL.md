---
name: claude-code-github-launcher
description: Terminal playbook for non-coders using Claude Code (standalone or inside Google Antigravity IDE terminal) to clone/launch GitHub repos, auto-configure Docker, and iteratively upgrade local apps in plain English.
---

# Claude Code + Antigravity IDE Workflow Skill

## Purpose
Enable non-technical builders to run complex GitHub repositories locally and upgrade IDE projects in plain English using Claude Code in the terminal.

## Workflow 1 — Zero-Friction GitHub Repo Setup
1. Copy the GitHub repository URL and its README installation section.
2. Open your terminal and start Claude Code (`claude`).
3. Paste the repo URL/README and prompt:
   > "Clone this GitHub repository into a clean local folder, check prerequisites (Docker, Node, Python), set up dependencies, and launch the app locally. Ask me before running any destructive or system-wide commands."
4. Approve each safe step (`Yes`) as Claude Code opens Docker, installs packages, and starts the local server.

## Workflow 2 — Hybrid Antigravity IDE + Claude Code (Credit-Saver Power Pattern)
1. Open or scaffold your project inside **Google Antigravity IDE** (free local IDE).
2. Open **Terminal -> New Terminal** inside Antigravity.
3. Launch `claude` directly inside that project directory.
4. Give plain-English upgrade prompts to Claude Code so it directly reads and edits your `HTML`, `CSS`, and `JS` files without consuming Antigravity Gemini credits:
   > "Read the current project files, keep all existing functionality working, and upgrade the UI to be colorful, animated, and gamified with XP, levels, and smooth transitions."
5. Preview live in the browser and iterate until polished.
