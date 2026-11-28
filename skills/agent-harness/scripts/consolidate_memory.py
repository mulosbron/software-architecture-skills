#!/usr/bin/env python3
"""
Episodic -> Semantic Memory Consolidation Gate.
Checks unconsolidated rows in <root>/state.db. Only when the count meets or
exceeds --threshold (e.g., 20 episodes) does it distill durable facts into
<root>/memories/memory.md and mark those episodes as consolidated.
"""

import argparse
import datetime
import json
import sqlite3
from pathlib import Path
from typing import List, Tuple


def distill_facts_heuristic(episodes: List[Tuple[int, str, str, str]]) -> List[str]:
    """
    Offline deterministic distiller (replace or augment with a cheaper auxiliary
    LLM call such as Gemini Flash / Haiku in production).
    Extracts preference/decision/fact statements from raw episode text.
    """
    cue_words = ("favorite", "prefer", "always", "never", "my company", "quirk", "error", "pytest", "use ")
    facts: List[str] = []
    seen = set()
    for _id, _ts, role, content in episodes:
        lower = content.lower()
        if any(cue in lower for cue in cue_words):
            snippet = " ".join(content.strip().split())[:220]
            if snippet not in seen:
                seen.add(snippet)
                facts.append(f"[{role}] {snippet}")
    return facts


def run_consolidation(root: Path, threshold: int = 20, force: bool = False) -> dict:
    db_path = root / "state.db"
    mem_path = root / "memories" / "memory.md"
    if not db_path.exists():
        return {"status": "skipped", "reason": f"Database not found: {db_path}"}

    with sqlite3.connect(db_path) as conn:
        rows = conn.execute(
            "SELECT id, timestamp, role, content FROM episodes WHERE consolidated = 0 ORDER BY id ASC"
        ).fetchall()

        if not force and len(rows) < threshold:
            return {
                "status": "gate_closed",
                "unconsolidated_count": len(rows),
                "threshold": threshold,
                "message": "Threshold not reached; skipping consolidation to save tokens.",
            }

        facts = distill_facts_heuristic(rows)
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        mem_path.parent.mkdir(parents=True, exist_ok=True)
        with mem_path.open("a", encoding="utf-8") as f:
            if facts:
                f.write(f"\n### Consolidated Batch ({ts}, {len(rows)} episodes)\n")
                for fact in facts:
                    f.write(f"- [consolidated] {fact}\n")

        ids = [(r[0],) for r in rows]
        conn.executemany("UPDATE episodes SET consolidated = 1 WHERE id = ?", ids)

    return {
        "status": "consolidated",
        "episodes_processed": len(rows),
        "facts_distilled": len(facts),
        "memory_file": str(mem_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Episodic -> Semantic Consolidation Gate")
    parser.add_argument("--root", default=".hermes")
    parser.add_argument("--threshold", type=int, default=20, help="Min unconsolidated episodes before running")
    parser.add_argument("--force", action="store_true", help="Bypass threshold gate")
    args = parser.parse_args()
    result = run_consolidation(Path(args.root), threshold=args.threshold, force=args.force)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
