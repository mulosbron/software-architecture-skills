#!/usr/bin/env python3
"""
Scaffolds a complete local Hermes-style Agent Harness workspace:
  <root>/
    soul.md
    memories/memory.md
    skills/
    logs/trajectories.jsonl
    state.db
"""

import argparse
import shutil
import sqlite3
from pathlib import Path


def init_harness(root: Path, skillset_root: Path = None) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "memories").mkdir(exist_ok=True)
    (root / "skills").mkdir(exist_ok=True)
    (root / "logs").mkdir(exist_ok=True)

    soul_path = root / "soul.md"
    if not soul_path.exists():
        tpl = skillset_root / "templates" / "soul.md" if skillset_root else None
        if tpl and tpl.exists():
            shutil.copy2(tpl, soul_path)
        else:
            soul_path.write_text("# Soul\nYou are a helpful local AI agent.\n", encoding="utf-8")

    mem_path = root / "memories" / "memory.md"
    if not mem_path.exists():
        tpl = skillset_root / "templates" / "memory.md" if skillset_root else None
        if tpl and tpl.exists():
            shutil.copy2(tpl, mem_path)
        else:
            mem_path.write_text("# Semantic Memory\n\n", encoding="utf-8")

    # Copy bundled skills if available
    if skillset_root and (skillset_root / "skills").exists():
        for skill_md in (skillset_root / "skills").rglob("SKILL.md"):
            rel = skill_md.relative_to(skillset_root / "skills")
            dest = root / "skills" / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                shutil.copy2(skill_md, dest)

    # Initialize SQLite episodic memory
    db_path = root / "state.db"
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS episodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                metadata_json TEXT DEFAULT '{}',
                consolidated INTEGER DEFAULT 0
            )
            """
        )

    log_path = root / "logs" / "trajectories.jsonl"
    if not log_path.exists():
        log_path.touch()

    print(f"[OK] Harness workspace initialized at: {root.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize local Agent Harness workspace")
    parser.add_argument("--root", default=".hermes", help="Target harness directory")
    args = parser.parse_args()
    skillset_root = Path(__file__).resolve().parent.parent
    init_harness(Path(args.root), skillset_root=skillset_root)


if __name__ == "__main__":
    main()
