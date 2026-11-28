#!/usr/bin/env bash
# Clone any GitHub repository, inspect stack (Docker/Node/Python), and launch Claude Code.
# Usage: bash scripts/github_claude_launcher.sh https://github.com/owner/repo [target_dir]

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <github_repo_url> [target_dir]"
  exit 1
fi

REPO_URL="$1"
REPO_NAME="$(basename "$REPO_URL" .git)"
TARGET_DIR="${2:-$REPO_NAME}"

echo "==> Cloning $REPO_URL into $TARGET_DIR..."
if [ -d "$TARGET_DIR" ]; then
  echo "Directory '$TARGET_DIR' already exists. Entering directory..."
else
  git clone "$REPO_URL" "$TARGET_DIR"
fi

cd "$TARGET_DIR"

echo "==> Detected project files:"
[ -f "docker-compose.yml" ] || [ -f "compose.yml" ] && echo "  - Docker Compose detected"
[ -f "package.json" ] && echo "  - Node.js (package.json) detected"
[ -f "requirements.txt" ] || [ -f "pyproject.toml" ] && echo "  - Python project detected"

if command -v claude >/dev/null 2>&1; then
  echo "==> Launching Claude Code inside $(pwd)..."
  claude "Read the README and project files in this repo, explain the setup prerequisites, and walk me step-by-step through installing dependencies and running it locally (ask before running system-level commands)."
else
  echo "Claude Code CLI ('claude') not found in PATH."
  echo "Install it via: npm install -g @anthropic-ai/claude-code"
  echo "Then run 'claude' inside: $(pwd)"
fi
