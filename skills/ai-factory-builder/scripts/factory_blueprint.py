#!/usr/bin/env python3
"""
factory_blueprint.py — AI factory candidate scorer and blueprint generator.

Methodology: Notion's "A New Shape for Work" (ai-factory-builder skill).

Usage:
    # Score traits explicitly
    python factory_blueprint.py check --name "Weekly Report" --recurring yes --verifiable yes \
        --stable yes --standard yes --digital yes --known-universe yes --low-cost-mistakes yes --json

    # Infer traits from free text
    python factory_blueprint.py check --name "Sales Deck Pack" \
        --describe "Every week we build the same format deck from our CRM; mistakes are easy to catch."

    # Generate a 10-section factory blueprint skeleton
    python factory_blueprint.py blueprint --name "Sales Deck Pack" --trigger "new card in todo" \
        --stages "research,drafting,formatting" --tools "context system, slide template" --out plan.md

Boolean values accepted: yes/y/true/1 (and no/n/false/0).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Set

YES = {"yes", "y", "true", "1", "evet", "var"}
NO = {"no", "n", "false", "0", "hayir", "hayır", "yok"}

TRAITS = [
    ("recurring", "Recurring workflow"),
    ("verifiable", "Verifiable output quality"),
    ("stable", "Stable over time (consistent process and requirements)"),
    ("standard", "Standard/reliable quality is sufficient (no one-off genius required)"),
    ("digital", "Fully digital knowledge work"),
    ("known-universe", "Bounded, known information universe"),
    ("low-cost-mistakes", "Low cost of mistakes (inexpensive or easy to catch)"),
]

HINTS = {
    "recurring": r"every (week|day|month|quarter)|weekly|daily|monthly|quarterly|recurr|repeat|regularly",
    "verifiable": r"verif|check|qa|quality|catch (error|mistake)|eval|criteria|checklist|rubric",
    "stable": r"same format|consistent|standard|template|fixed|stable|unchanging",
    "standard": r"standard|good enough|reliable|routine|average|solid|consistent quality",
    "digital": r"e-?mail|report|doc(ument)?|deck|slide|data|table|ticket|pr|pull request|digital|spreadsheet",
    "known-universe": r"database|crm|warehouse|archive|repo(sitory)?|wiki|notion|knowledge base|sources",
    "low-cost-mistakes": r"easy (to )?(catch|detect|spot)|low (risk|cost)|reversible|draft|shadow|review",
}


def _norm(v: str | None) -> bool | None:
    if v is None:
        return None
    s = v.strip().lower()
    if s in YES:
        return True
    if s in NO:
        return False
    return None


def infer_from_text(text: str) -> Dict[str, bool]:
    return {key: bool(re.search(rx, text, re.IGNORECASE)) for key, rx in HINTS.items()}


def evaluate(name: str, flags: Dict[str, bool], inferred_keys: Set[str]) -> dict:
    score_val = sum(1 for k, _ in TRAITS if flags.get(k))
    missing = [label for key, label in TRAITS if not flags.get(key)]
    if score_val >= 6:
        tier = "strong"
        verdict = "STRONG CANDIDATE — proceed to factory blueprint."
    elif score_val >= 4:
        tier = "conditional"
        verdict = "CONDITIONAL CANDIDATE — review missing traits with the user and plan only if mitigations exist."
    else:
        tier = "weak"
        verdict = "WEAK CANDIDATE — do not automate; document why manual execution is better."
    return {
        "ok": True,
        "name": name,
        "score": score_val,
        "max_score": len(TRAITS),
        "tier": tier,
        "verdict": verdict,
        "traits": {
            key: {"passed": bool(flags.get(key)), "label": label, "inferred": key in inferred_keys}
            for key, label in TRAITS
        },
        "missing": missing,
        "triad_reminder": ["specific", "shared", "scrutinized"],
    }


def format_report(res: dict) -> str:
    lines = [
        "=" * 60,
        f"Factory Candidate Score: {res['name']}",
        "=" * 60,
        f"Score: {res['score']}/{res['max_score']}",
        f"Verdict: {res['verdict']}",
        "",
        "Trait breakdown:",
    ]
    for key, label in TRAITS:
        info = res["traits"][key]
        mark = "yes" if info["passed"] else "no"
        src = " (inferred from text)" if info["inferred"] else ""
        lines.append(f"  [{mark:>3}] {label}{src}")
    if res["missing"]:
        lines.append("")
        lines.append("Missing traits:")
        for label in res["missing"]:
            lines.append(f"  - {label}")
    lines.append("")
    lines.append("Reminder: also verify the three factory criteria — specific, shared, scrutinized.")
    lines.append("=" * 60)
    return "\n".join(lines)


def cmd_check(args: argparse.Namespace) -> int:
    flags: Dict[str, bool | None] = {}
    inferred_keys: Set[str] = set()
    for key, _ in TRAITS:
        flags[key] = _norm(getattr(args, key.replace("-", "_"), None))
    if args.describe:
        inferred = infer_from_text(args.describe)
        for key, value in inferred.items():
            if flags[key] is None:
                flags[key] = value
                inferred_keys.add(key)
    final_flags: Dict[str, bool] = {}
    for key, _ in TRAITS:
        if flags[key] is None:
            final_flags[key] = False
            inferred_keys.add(key)
        else:
            final_flags[key] = bool(flags[key])
    res = evaluate(args.name, final_flags, inferred_keys)
    print(json.dumps(res, indent=2) if args.json else format_report(res))
    return 0


BLUEPRINT = """# AI Factory Blueprint: {name}

## 1. Triad Criteria Check

- **Specific:** [which exact task class this factory handles, and what is out of scope]
- **Shared:** [who on the team uses it and how access is provisioned]
- **Scrutinized:** [named owner(s), review cadence, and error-triage loop]

## 2. Task Definition

[Describe in 3 sentences how the task is performed today and what artifact the factory produces.]

## 3. Triggers

- **Scheduled:** [e.g. every Monday at 09:00]
- **Event-driven:** {trigger}

## 4. Inputs, Stages & Outputs

- **Inputs:** [databases, files, external synced sources]
- **Stages:** {stages}
- **Outputs:** [where final artifacts are written and which card/status updates]

## 5. Tools & Permissions

- **Required access:** {tools}
- **Explicitly forbidden:** [sensitive data, production mutations, financial actions]

## 6. Shadow-Run Rollout Plan

1. First 5 runs operate strictly in draft/shadow mode: zero external side effects, log proposed actions only.
2. Human review: [reviewer and acceptance criteria]
3. Promotion rule: [consecutive passing shadow runs required before ramping live volume]

## 7. Volume Control Plan

- **Initial volume:** [e.g. 5 cards/day or 5% of incoming volume]
- **Ramp / rollback rule:** [error-rate threshold for increasing or pausing volume]

## 8. Eval Suite

| Task | Grading Criteria | Judge (code / AI / human) |
|---|---|---|
| [test task 1] | [required properties] | [code / AI / human] |
| [negative / out-of-scope test] | [factory rejects or escalates cleanly] | [code] |

## 9. Prompt Versioning

- **Storage:** [Prompt Versions database or repository]
- **States:** `testing`, `production`, `retired`
- **Rollback rule:** [condition that reverts to previous production prompt]

## 10. Context System Integration

- **Core databases used:** [Projects, Tasks, Documents, People, Teams, Customers]
- **Factory database:** [{name} task cards + run history]
- **Context-rot hygiene:** [scan cadence, staleness flags, and owner]
"""


def cmd_blueprint(args: argparse.Namespace) -> int:
    stages = ", ".join(s.strip() for s in args.stages.split(",") if s.strip()) if args.stages else "single unified stage"
    tools = args.tools or "[required agent tools]"
    body = BLUEPRINT.format(
        name=args.name,
        trigger=args.trigger or "[unspecified trigger]",
        stages=stages,
        tools=tools,
    )
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body, encoding="utf-8")
        if args.json:
            print(json.dumps({"ok": True, "name": args.name, "out": str(out_path)}, indent=2))
        else:
            print(f"Blueprint written to: {out_path}")
    else:
        if args.json:
            print(json.dumps({"ok": True, "name": args.name, "blueprint": body}, indent=2))
        else:
            print(body)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="AI factory candidate scorer and blueprint generator")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ck = sub.add_parser("check", help="Score a candidate workflow across the 7 factory traits")
    ck.add_argument("--name", required=True, help="Candidate workflow name")
    ck.add_argument("--describe", help="Free-text description used to infer omitted traits")
    for key, _ in TRAITS:
        ck.add_argument(f"--{key}", help="yes/no (default: inferred or no)")
    ck.add_argument("--json", action="store_true", help="Output machine-readable JSON")

    bp = sub.add_parser("blueprint", help="Generate a 10-section AI factory blueprint skeleton")
    bp.add_argument("--name", required=True, help="Factory name")
    bp.add_argument("--trigger", help="Event-driven trigger description")
    bp.add_argument("--stages", help="Comma-separated pipeline stages")
    bp.add_argument("--tools", help="Tools and systems the agent can access")
    bp.add_argument("--out", help="Output markdown path (prints to stdout if omitted)")
    bp.add_argument("--json", action="store_true", help="Output machine-readable JSON")

    args = ap.parse_args()
    if args.cmd == "check":
        return cmd_check(args)
    if args.cmd == "blueprint":
        return cmd_blueprint(args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
