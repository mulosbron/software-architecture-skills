"""Architecture CLI: ADRs, C4 scaffolds, God Class and module-boundary checks."""
import argparse
import os
import re
import sys
from datetime import date

ADR_DIR = os.path.join("docs", "adrs")
C4_DIR = os.path.join("docs", "c4")
CODE_EXT = (".java", ".py", ".cs", ".ts", ".tsx", ".js", ".jsx", ".go", ".kt", ".rb", ".php", ".rs")
SKIP_DIRS = {"node_modules", ".git", "vendor", "dist", "build", "target", "__pycache__", ".venv", "venv", "bin", "obj"}

# ---------------------------------------------------------------- ADR

def _adr_files():
    if not os.path.isdir(ADR_DIR):
        return []
    return sorted(f for f in os.listdir(ADR_DIR) if re.match(r"^\d{4}-.*\.md$", f))


def _next_adr_id():
    ids = [int(f[:4]) for f in _adr_files()]
    return (max(ids) + 1) if ids else 1


def _adr_path(adr_id):
    for f in _adr_files():
        if int(f[:4]) == adr_id:
            return os.path.join(ADR_DIR, f)
    return None


def _slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def adr_new(args):
    os.makedirs(ADR_DIR, exist_ok=True)
    adr_id = _next_adr_id()
    path = os.path.join(ADR_DIR, f"{adr_id:04d}-{_slug(args.title)}.md")
    body = f"""# {adr_id}. {args.title}

Date: {date.today().isoformat()}

## Status
Proposed

## Context
What constraint forces this decision? (team size, SLA, budget, deadline)

## Decision
What are we doing?

## Consequences
Positive:
-

Negative (required, at least one):
-
"""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    print(f"[OK] {path}")
    return path


def adr_list(args):
    files = _adr_files()
    if not files:
        print(f"[INFO] No ADRs in {ADR_DIR}")
        return
    for f in files:
        status = "?"
        with open(os.path.join(ADR_DIR, f), encoding="utf-8") as fh:
            text = fh.read()
        m = re.search(r"^## Status\s*\n\s*(.+)$", text, re.M)
        if m:
            status = m.group(1).strip()
        print(f"{f[:4]}  {status:<22} {f[5:-3]}")


def adr_supersede(args):
    old = _adr_path(args.id)
    if not old:
        sys.exit(f"[ERR] ADR {args.id:04d} not found in {ADR_DIR}")
    new_path = adr_new(args)
    new_id = int(os.path.basename(new_path)[:4])
    with open(old, encoding="utf-8") as fh:
        text = fh.read()
    text = re.sub(r"(^## Status\s*\n\s*)(.+)$", rf"\g<1>Superseded by {new_id:04d}", text, count=1, flags=re.M)
    with open(old, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(new_path, encoding="utf-8") as fh:
        text = fh.read()
    text = text.replace("## Context\n", f"## Context\nSupersedes {args.id:04d}.\n\n", 1)
    with open(new_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"[OK] {os.path.basename(old)} marked Superseded by {new_id:04d}")

# ---------------------------------------------------------------- C4

C4_TEMPLATES = {
    "context": """@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml
title System Context: {name}

Person(user, "User", "Who uses the system")
System(sys, "{name}", "What it does in one line")
System_Ext(ext, "External System", "e.g. payment provider")

Rel(user, sys, "Uses", "HTTPS")
Rel(sys, ext, "Calls", "HTTPS/JSON")
@enduml
""",
    "container": """@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
title Containers: {name}

Person(user, "User")
System_Boundary(sys, "{name}") {{
  Container(web, "Web App", "TECH", "Serves the UI")
  Container(api, "API", "TECH", "Business logic")
  ContainerDb(db, "Database", "TECH", "Stores state")
}}

Rel(user, web, "Uses", "HTTPS")
Rel(web, api, "Calls", "JSON/HTTPS")
Rel(api, db, "Reads/writes", "TCP")
@enduml
""",
    "component": """@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml
title Components: {name} API

Container_Boundary(api, "{name} API") {{
  Component(ctrl, "Controller", "TECH", "HTTP entry")
  Component(svc, "Service", "TECH", "Business rules")
  Component(repo, "Repository", "TECH", "Data access")
}}
ContainerDb(db, "Database", "TECH")

Rel(ctrl, svc, "Calls")
Rel(svc, repo, "Calls")
Rel(repo, db, "SQL")
@enduml
""",
}


def init_c4(args):
    os.makedirs(C4_DIR, exist_ok=True)
    path = os.path.join(C4_DIR, f"{args.level}.puml")
    if os.path.exists(path) and not args.force:
        sys.exit(f"[ERR] {path} exists. Use --force to overwrite.")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(C4_TEMPLATES[args.level].format(name=args.name))
    print(f"[OK] {path}  (replace TECH labels and the placeholder descriptions)")

# ---------------------------------------------------------------- God classes

CLASS_RE = re.compile(r"^\s*(?:export\s+|public\s+|internal\s+|abstract\s+|final\s+|sealed\s+|partial\s+|data\s+|open\s+)*(?:class|struct|object|interface|impl)\s+([A-Za-z_][A-Za-z0-9_]*)")


def _walk(directory):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if f.endswith(CODE_EXT):
                yield os.path.join(root, f)


def _class_sizes(path):
    """Approximate class length as the span from one class declaration to the next (or EOF)."""
    with open(path, encoding="utf-8", errors="ignore") as fh:
        lines = fh.readlines()
    starts = [(i, m.group(1)) for i, line in enumerate(lines) if (m := CLASS_RE.match(line))]
    if not starts:
        return [("<file>", len(lines))]
    out = []
    for n, (i, name) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        out.append((name, end - i))
    return out


def check_god_classes(args):
    hits = []
    for path in _walk(args.dir):
        for name, size in _class_sizes(path):
            if size > args.threshold:
                hits.append((size, path, name))
    if not hits:
        print(f"[OK] No class/file over {args.threshold} lines in {args.dir}")
        return
    for size, path, name in sorted(hits, reverse=True):
        print(f"{size:6d}  {path}  {name}")
    print(f"[WARN] {len(hits)} candidate(s) over {args.threshold} lines")
    sys.exit(1)

# ---------------------------------------------------------------- Module boundaries

IMPORT_RE = re.compile(r"""^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w.]+)|import\s+.*?from\s+['"]([^'"]+)['"]|require\(['"]([^'"]+)['"]\)|using\s+([\w.]+);)""")
PUBLIC_MARKERS = ("api", "public", "contracts", "__init__", "index")


def check_module_boundaries(args):
    src = os.path.abspath(args.dir)
    modules = sorted(d for d in os.listdir(src) if os.path.isdir(os.path.join(src, d)) and d not in SKIP_DIRS and not d.startswith("."))
    if not modules:
        sys.exit(f"[ERR] No module directories under {src}")
    violations = []
    for path in _walk(src):
        rel = os.path.relpath(path, src).replace("\\", "/")
        own = rel.split("/")[0]
        with open(path, encoding="utf-8", errors="ignore") as fh:
            for ln, line in enumerate(fh, 1):
                m = IMPORT_RE.match(line)
                if not m:
                    continue
                target = next(g for g in m.groups() if g)
                parts = [p for p in re.split(r"[./]", target) if p and p not in ("..",)]
                if not parts:
                    continue
                # find the first segment that names a sibling module
                other = next((p for p in parts if p in modules), None)
                if not other or other == own or other == args.shared:
                    continue
                after = parts[parts.index(other) + 1:]
                if not after or after[0].lower() in PUBLIC_MARKERS:
                    continue
                violations.append((rel, ln, own, other, target))
    if not violations:
        print(f"[OK] {len(modules)} modules, no boundary violations ({', '.join(modules)})")
        return
    for rel, ln, own, other, target in violations:
        print(f"{rel}:{ln}  {own} -> {other} internals  ({target})")
    print(f"[WARN] {len(violations)} violation(s). Modules may only import a sibling's public entry: {', '.join(PUBLIC_MARKERS)}")
    sys.exit(1)

# ---------------------------------------------------------------- main

def main():
    p = argparse.ArgumentParser(description="Software architecture CLI")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("adr-new", help="Create an ADR in docs/adrs")
    s.add_argument("title")
    s.set_defaults(func=adr_new)

    s = sub.add_parser("adr-list", help="List ADRs with status")
    s.set_defaults(func=adr_list)

    s = sub.add_parser("adr-supersede", help="Create a new ADR that supersedes an existing one")
    s.add_argument("id", type=int, help="ID of the ADR being superseded, e.g. 3")
    s.add_argument("title")
    s.set_defaults(func=adr_supersede)

    s = sub.add_parser("init-c4", help="Scaffold a C4 PlantUML diagram in docs/c4")
    s.add_argument("--level", choices=list(C4_TEMPLATES), default="context")
    s.add_argument("--name", default="System")
    s.add_argument("--force", action="store_true")
    s.set_defaults(func=init_c4)

    s = sub.add_parser("check-god-classes", help="List classes/files over a line threshold (exit 1 if any)")
    s.add_argument("dir")
    s.add_argument("--threshold", type=int, default=500)
    s.set_defaults(func=check_god_classes)

    s = sub.add_parser("check-module-boundaries", help="Flag imports that reach into a sibling module's internals (exit 1 if any)")
    s.add_argument("dir", help="Directory whose immediate subdirectories are modules")
    s.add_argument("--shared", default="shared", help="Module name exempt from the rule (default: shared)")
    s.set_defaults(func=check_module_boundaries)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
