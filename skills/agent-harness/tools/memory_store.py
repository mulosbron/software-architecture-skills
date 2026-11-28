#!/usr/bin/env python3
"""
Local 3-Pillar Memory Store (Hermes-style architecture):
  1. Procedural Memory: <root>/skills/<category>/<name>/SKILL.md
  2. Semantic Memory:   <root>/memories/memory.md (plain-text top-k keyword retrieval)
  3. Episodic Memory:   <root>/state.db (SQLite time-series event & chat log)
"""

import argparse
import datetime
import json
import re
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Tuple


class LocalMemoryStore:
    def __init__(self, root: Path):
        self.root = Path(root)
        self.memories_dir = self.root / "memories"
        self.memory_file = self.memories_dir / "memory.md"
        self.skills_dir = self.root / "skills"
        self.db_path = self.root / "state.db"
        self._ensure_initialized()

    def _ensure_initialized(self) -> None:
        self.memories_dir.mkdir(parents=True, exist_ok=True)
        self.skills_dir.mkdir(parents=True, exist_ok=True)
        if not self.memory_file.exists():
            self.memory_file.write_text("# Semantic Memory\n\n", encoding="utf-8")
        with sqlite3.connect(self.db_path) as conn:
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
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_episodes_session ON episodes(session_id)"
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_episodes_consolidated ON episodes(consolidated)"
            )

    # --- Semantic Memory (memory.md) ---
    def remember(self, category: str, fact: str) -> Dict[str, Any]:
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        entry = f"- [{category}] ({ts}) {fact.strip()}\n"
        with self.memory_file.open("a", encoding="utf-8") as f:
            f.write(entry)
        return {"status": "saved", "file": str(self.memory_file), "entry": entry.strip()}

    @staticmethod
    def _tokenize(text: str) -> set:
        return set(re.findall(r"[a-zA-Z0-9_çğıöşüÇĞİÖŞÜ]+", text.lower()))

    def search_semantic(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        q_tokens = self._tokenize(query)
        if not q_tokens or not self.memory_file.exists():
            return []
        scored: List[Tuple[int, str]] = []
        for line in self.memory_file.read_text(encoding="utf-8").splitlines():
            clean = line.strip()
            if not clean.startswith("- "):
                continue
            overlap = len(q_tokens & self._tokenize(clean))
            if overlap > 0:
                scored.append((overlap, clean))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [{"score": s, "fact": text} for s, text in scored[:top_k]]

    # --- Episodic Memory (state.db) ---
    def log_episode(
        self, session_id: str, role: str, content: str, metadata: Dict[str, Any] = None
    ) -> int:
        ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
        meta_str = json.dumps(metadata or {}, ensure_ascii=False)
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                """
                INSERT INTO episodes (timestamp, session_id, role, content, metadata_json, consolidated)
                VALUES (?, ?, ?, ?, ?, 0)
                """,
                (ts, session_id, role, content, meta_str),
            )
            return int(cur.lastrowid)

    def search_episodic(
        self, query: str = "", session_id: str = None, limit: int = 10
    ) -> List[Dict[str, Any]]:
        sql = "SELECT id, timestamp, session_id, role, content FROM episodes WHERE 1=1"
        params: List[Any] = []
        if session_id:
            sql += " AND session_id = ?"
            params.append(session_id)
        sql += " ORDER BY id DESC LIMIT 200"
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(sql, params).fetchall()

        results = []
        q_tokens = self._tokenize(query) if query else set()
        for row_id, ts, sess, role, content in rows:
            score = len(q_tokens & self._tokenize(content)) if q_tokens else 1
            if not q_tokens or score > 0:
                results.append(
                    {
                        "id": row_id,
                        "timestamp": ts,
                        "session_id": sess,
                        "role": role,
                        "content": content,
                        "score": score,
                    }
                )
        results.sort(key=lambda r: (r["score"], r["id"]), reverse=True)
        return results[:limit]

    def recall(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        return {
            "query": query,
            "semantic_facts": self.search_semantic(query, top_k=top_k),
            "episodic_matches": self.search_episodic(query, limit=top_k),
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Local 3-Pillar Agent Memory CLI")
    parser.add_argument("--root", default=".hermes", help="Harness root directory")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_rem = sub.add_parser("remember", help="Save a durable fact to semantic memory")
    p_rem.add_argument("--category", default="general")
    p_rem.add_argument("--fact", required=True)

    p_log = sub.add_parser("log-episode", help="Log an event/message to episodic state.db")
    p_log.add_argument("--session", required=True)
    p_log.add_argument("--role", default="user")
    p_log.add_argument("--content", required=True)

    p_rec = sub.add_parser("recall", help="Recall from semantic + episodic memory")
    p_rec.add_argument("--query", required=True)
    p_rec.add_argument("--top-k", type=int, default=5)

    args = parser.parse_args()
    store = LocalMemoryStore(Path(args.root))

    if args.cmd == "remember":
        print(json.dumps(store.remember(args.category, args.fact), indent=2, ensure_ascii=False))
    elif args.cmd == "log-episode":
        ep_id = store.log_episode(args.session, args.role, args.content)
        print(json.dumps({"status": "logged", "episode_id": ep_id}, indent=2))
    elif args.cmd == "recall":
        print(json.dumps(store.recall(args.query, top_k=args.top_k), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
