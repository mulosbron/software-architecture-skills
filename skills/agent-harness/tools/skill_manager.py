#!/usr/bin/env python3
"""
Procedural Memory (Skill) Manager + Self-Learning Trigger Detector.
Manages SKILL.md files under <root>/skills/<category>/<name>/SKILL.md and
detects when a complex iterative task (>= 5 tool calls) should be distilled
into a reusable skill.
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


class SkillManager:
    SELF_LEARN_TOOL_THRESHOLD = 5

    def __init__(self, root: Path):
        self.skills_dir = Path(root) / "skills"
        self.skills_dir.mkdir(parents=True, exist_ok=True)

    def create_skill(
        self, name: str, category: str, description: str, instructions: str = ""
    ) -> Dict[str, Any]:
        slug = name.strip().lower().replace(" ", "-")
        cat = category.strip().lower().replace(" ", "-")
        skill_path = self.skills_dir / cat / slug / "SKILL.md"
        skill_path.parent.mkdir(parents=True, exist_ok=True)

        body = instructions.strip() or (
            f"# {name}\n\n"
            "## Steps\n"
            "1. Review inputs and constraints.\n"
            "2. Execute verified workflow.\n"
            "3. Validate output before replying.\n"
        )
        content = f"---\nname: {slug}\ndescription: {description.strip()}\n---\n\n{body}\n"
        skill_path.write_text(content, encoding="utf-8")
        return {"status": "created", "skill": slug, "path": str(skill_path)}

    def list_skills(self) -> List[Dict[str, str]]:
        items: List[Dict[str, str]] = []
        for md in sorted(self.skills_dir.rglob("SKILL.md")):
            rel = md.relative_to(self.skills_dir)
            parts = rel.parts
            category = parts[0] if len(parts) >= 3 else "general"
            name = parts[-2] if len(parts) >= 2 else md.stem
            items.append({"name": name, "category": category, "path": str(md)})
        return items

    def should_proactively_save_skill(self, tool_call_count: int, succeeded: bool) -> Dict[str, Any]:
        trigger = succeeded and tool_call_count >= self.SELF_LEARN_TOOL_THRESHOLD
        return {
            "should_offer_skill": trigger,
            "tool_call_count": tool_call_count,
            "threshold": self.SELF_LEARN_TOOL_THRESHOLD,
            "reason": (
                "Complex iterative task succeeded with >= 5 tool calls; offer to save as reusable SKILL.md."
                if trigger
                else "Below complexity threshold or unsuccessful run."
            ),
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Procedural Skill Manager CLI")
    parser.add_argument("--root", default=".hermes")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_create = sub.add_parser("create", help="Create a new SKILL.md")
    p_create.add_argument("--name", required=True)
    p_create.add_argument("--category", default="general")
    p_create.add_argument("--description", required=True)
    p_create.add_argument("--instructions", default="")

    sub.add_parser("list", help="List all installed skills")

    p_check = sub.add_parser("check-trigger", help="Check if run qualifies for proactive skill creation")
    p_check.add_argument("--tool-calls", type=int, required=True)
    p_check.add_argument("--succeeded", action="store_true")

    args = parser.parse_args()
    mgr = SkillManager(Path(args.root))

    if args.cmd == "create":
        res = mgr.create_skill(args.name, args.category, args.description, args.instructions)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.cmd == "list":
        print(json.dumps(mgr.list_skills(), indent=2, ensure_ascii=False))
    elif args.cmd == "check-trigger":
        res = mgr.should_proactively_save_skill(args.tool_calls, args.succeeded)
        print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
