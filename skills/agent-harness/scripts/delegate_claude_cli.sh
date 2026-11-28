#!/usr/bin/env bash
# Headless Claude CLI Sub-Agent Delegation Script
# Usage: ./scripts/delegate_claude_cli.sh "Build a Python script that fetches top 5 Hacker News stories to Markdown"

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 "<task prompt for headless Claude CLI>"" >&2
  exit 1
fi

TASK_PROMPT="$1"
LOG_DIR="${HARNESS_LOG_DIR:-.hermes/logs}"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y%m%d_%H%M%S)"
OUT_LOG="$LOG_DIR/subagent_claude_${STAMP}.log"

if ! command -v claude >/dev/null 2>&1; then
  echo "[ERROR] 'claude' CLI not found in PATH. Install Claude Code CLI first." >&2
  exit 127
fi

echo "[INFO] Delegating task to headless Claude CLI..."
echo "[INFO] Output log: $OUT_LOG"

claude -p "$TASK_PROMPT" --output-format text | tee "$OUT_LOG"
echo "[OK] Sub-agent finished. Verify generated files before marking loop complete."
