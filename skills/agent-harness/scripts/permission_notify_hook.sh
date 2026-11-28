#!/usr/bin/env bash
# Loop Engineering Permission Hook
# Sends an OS desktop notification whenever the agent pauses for user permission
# or completes a long-running loop (prevents silent waiting).

set -euo pipefail

TITLE="${1:-Agent Harness Attention}"
MESSAGE="${2:-Agent loop is waiting for your permission or input.}"

if [[ "$OSTYPE" == "darwin"* ]] && command -v osascript >/dev/null 2>&1; then
  osascript -e "display notification "${MESSAGE}" with title "${TITLE}" sound name "Glass""
elif command -v notify-send >/dev/null 2>&1; then
  notify-send "$TITLE" "$MESSAGE"
else
  # Fallback to terminal bell + stdout
  printf '\a[%s] %s\n' "$TITLE" "$MESSAGE"
fi
