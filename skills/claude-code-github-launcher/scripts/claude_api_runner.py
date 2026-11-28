#!/usr/bin/env python3
"""
Lightweight CLI Runner for any SKILL.md using the Anthropic Messages API.
Requires: export ANTHROPIC_API_KEY="sk-ant-..."
Zero third-party dependencies (uses Python stdlib urllib).
"""

import argparse
import json
import os
import urllib.request
from pathlib import Path


def run_skill(skill_path: Path, user_prompt: str, model: str, extended_thinking: bool, max_tokens: int):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("Error: Set ANTHROPIC_API_KEY environment variable first.")

    skill_text = skill_path.read_text(encoding="utf-8")
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "system": skill_text,
        "messages": [{"role": "user", "content": user_prompt}],
    }
    if extended_thinking:
        payload["thinking"] = {"type": "enabled", "budget_tokens": max(1024, max_tokens // 2)}

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    text_blocks = [b["text"] for b in data.get("content", []) if b.get("type") == "text"]
    return "\n\n".join(text_blocks)


def main():
    p = argparse.ArgumentParser(description="Execute any SKILL.md via Anthropic API.")
    p.add_argument("--skill", required=True, type=Path, help="Path to SKILL.md")
    p.add_argument("--prompt", default="", help="Inline user prompt")
    p.add_argument("--input-file", type=Path, default=None, help="Optional input text file to append")
    p.add_argument("--model", default="claude-opus-4-5", help="Claude model ID (default: claude-opus-4-5)")
    p.add_argument("--thinking", action="store_true", help="Enable Extended Thinking mode")
    p.add_argument("--max-tokens", type=int, default=4096, help="Max output tokens")
    p.add_argument("-o", "--output", type=Path, default=None, help="Optional output file")
    args = p.parse_args()

    prompt = args.prompt
    if args.input_file:
        prompt = (prompt + "\n\n" if prompt else "") + args.input_file.read_text(encoding="utf-8")
    if not prompt.strip():
        raise SystemExit("Provide --prompt or --input-file.")

    result = run_skill(args.skill, prompt, args.model, args.thinking, args.max_tokens)
    if args.output:
        args.output.write_text(result, encoding="utf-8")
        print(f"Saved output -> {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
