#!/usr/bin/env python3
"""
Local LLMOps Trajectory Tracer & Deterministic Evaluator.
Fills the LLMOps/Eval gap in local harnesses (like Hermes Agent) by recording
each agent run as a structured JSONL trace tree and evaluating Health & Quality.
"""

import datetime
import json
import time
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class ToolEvent:
    tool_name: str
    duration_ms: float
    success: bool
    error: Optional[str] = None


@dataclass
class AgentRunTrace:
    run_id: str
    timestamp: str
    user_prompt: str
    model: str
    retrievals: List[str] = field(default_factory=list)
    tool_events: List[ToolEvent] = field(default_factory=list)
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_latency_ms: float = 0.0
    succeeded: bool = True
    judge_score: Optional[float] = None  # 1.0 - 5.0 optional LLM-as-a-Judge score


class TrajectoryTracer:
    def __init__(self, log_path: Path):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self._start_ts: float = 0.0
        self.current: Optional[AgentRunTrace] = None

    def start_run(self, user_prompt: str, model: str = "gemini-3.1") -> str:
        run_id = f"run_{uuid.uuid4().hex[:10]}"
        self._start_ts = time.perf_counter()
        self.current = AgentRunTrace(
            run_id=run_id,
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            user_prompt=user_prompt,
            model=model,
        )
        return run_id

    def log_retrieval(self, source: str) -> None:
        if self.current:
            self.current.retrievals.append(source)

    def log_tool(self, tool_name: str, duration_ms: float, success: bool = True, error: str = None) -> None:
        if self.current:
            self.current.tool_events.append(ToolEvent(tool_name, round(duration_ms, 2), success, error))

    def end_run(
        self,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
        succeeded: bool = True,
        judge_score: Optional[float] = None,
    ) -> AgentRunTrace:
        if not self.current:
            raise RuntimeError("No active run to end.")
        elapsed_ms = (time.perf_counter() - self._start_ts) * 1000.0
        self.current.prompt_tokens = prompt_tokens
        self.current.completion_tokens = completion_tokens
        self.current.total_latency_ms = round(elapsed_ms, 2)
        self.current.succeeded = succeeded
        self.current.judge_score = judge_score

        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(self.current), ensure_ascii=False) + "\n")
        finished = self.current
        self.current = None
        return finished


def diagnose_trace(trace: Dict[str, Any], latency_sla_ms: float = 5000.0, token_budget: int = 8000) -> Dict[str, Any]:
    issues: List[str] = []
    latency = trace.get("total_latency_ms", 0.0)
    total_tokens = trace.get("prompt_tokens", 0) + trace.get("completion_tokens", 0)
    tool_events = trace.get("tool_events", [])
    retrievals = trace.get("retrievals", [])

    if latency > latency_sla_ms:
        slow_tools = [t["tool_name"] for t in tool_events if t.get("duration_ms", 0) > latency_sla_ms * 0.5]
        if slow_tools:
            issues.append(f"High latency ({latency}ms) caused by slow tool(s): {', '.join(slow_tools)}")
        else:
            issues.append(f"High latency ({latency}ms) — inspect Working Memory size or model latency")

    if total_tokens > token_budget:
        issues.append(f"Token budget exceeded ({total_tokens} > {token_budget}) — consider tighter Top-K retrieval or consolidation")

    failed_tools = [t["tool_name"] for t in tool_events if not t.get("success", True)]
    if failed_tools:
        issues.append(f"Tool execution failures detected: {', '.join(failed_tools)}")

    if len(trace.get("user_prompt", "").split()) <= 5 and len(retrievals) >= 3:
        issues.append("Potential unnecessary retrieval on a very short/simple prompt")

    healthy = trace.get("succeeded", False) and len(issues) == 0
    return {
        "run_id": trace.get("run_id"),
        "healthy": healthy,
        "gate_decision": "SHIP" if healthy else "DIAGNOSE_AND_FIX",
        "issues": issues,
        "offer_skill_creation": trace.get("succeeded", False) and len(tool_events) >= 5,
    }


if __name__ == "__main__":
    # Quick self-test when executed directly
    demo_log = Path("/tmp/demo_trajectories.jsonl")
    if demo_log.exists():
        demo_log.unlink()
    tracer = TrajectoryTracer(demo_log)
    tracer.start_run("Check OS version and last 10 shell history lines")
    tracer.log_retrieval("memory.md")
    tracer.log_tool("terminal_exec", duration_ms=120.5, success=True)
    tr = tracer.end_run(prompt_tokens=650, completion_tokens=180, succeeded=True, judge_score=4.8)
    print(json.dumps(diagnose_trace(asdict(tr)), indent=2))
