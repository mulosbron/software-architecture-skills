#!/usr/bin/env python3
"""
LLMOps Evaluation & Diagnosis Report Generator.
Reads JSONL trajectory logs, evaluates each agent run against latency/token/tool
SLAs, and outputs an actionable summary with SHIP vs DIAGNOSE_AND_FIX gates.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from tracer_eval import diagnose_trace  # noqa: E402


def generate_report(log_path: Path, latency_sla_ms: float, token_budget: int) -> dict:
    if not log_path.exists():
        return {"status": "empty", "message": f"No log file found at {log_path}"}

    traces = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            traces.append(json.loads(line))

    if not traces:
        return {"status": "empty", "total_runs": 0}

    diagnostics = [diagnose_trace(t, latency_sla_ms=latency_sla_ms, token_budget=token_budget) for t in traces]
    healthy_count = sum(1 for d in diagnostics if d["healthy"])
    avg_latency = round(sum(t.get("total_latency_ms", 0.0) for t in traces) / len(traces), 2)
    avg_tokens = round(
        sum(t.get("prompt_tokens", 0) + t.get("completion_tokens", 0) for t in traces) / len(traces), 1
    )

    return {
        "total_runs": len(traces),
        "healthy_runs": healthy_count,
        "health_rate_pct": round((healthy_count / len(traces)) * 100, 1),
        "avg_latency_ms": avg_latency,
        "avg_total_tokens": avg_tokens,
        "skill_candidates": [d["run_id"] for d in diagnostics if d["offer_skill_creation"]],
        "failing_runs": [d for d in diagnostics if not d["healthy"]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze LLMOps trajectory logs")
    parser.add_argument("--logs", default=".hermes/logs/trajectories.jsonl")
    parser.add_argument("--latency-sla-ms", type=float, default=5000.0)
    parser.add_argument("--token-budget", type=int, default=8000)
    args = parser.parse_args()
    report = generate_report(Path(args.logs), args.latency_sla_ms, args.token_budget)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
