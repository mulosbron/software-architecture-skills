import os
import sys
import argparse
from datetime import datetime

def init_c4(args):
    template = """@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

title System Context diagram for [System Name]

Person(user, "User", "A user of the system.")
System(system, "Software System", "Allows users to do things.")

Rel(user, system, "Uses")
@enduml
"""
    filename = "c4_context.puml"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"[SUCCESS] Created C4 Context diagram boilerplate at {filename}")

def check_god_classes(args):
    directory = args.dir
    threshold = args.threshold
    
    print(f"[INFO] Scanning {directory} for potential God Classes (>{threshold} lines)...")
    found = False
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".java", ".py", ".cs", ".ts", ".js", ".go", ".cpp", ".php")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        if len(lines) > threshold:
                            print(f"[WARNING] Potential God Class: {path} ({len(lines)} lines)")
                            found = True
                except Exception as e:
                    pass
    
    if not found:
        print("[SUCCESS] No God Classes found! Your codebase looks well-segregated.")

def adr_new(args):
    title = args.title
    safe_title = title.lower().replace(" ", "-")
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    os.makedirs("docs/adrs", exist_ok=True)
    
    # Simple auto-increment ID
    adr_files = [f for f in os.listdir("docs/adrs") if f.endswith(".md")]
    adr_id = len(adr_files) + 1
    
    filename = f"docs/adrs/{adr_id:04d}-{safe_title}.md"
    
    template = f"""# {adr_id}. {title}

Date: {date_str}

## Status
Proposed

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Consequences
What becomes easier or more difficult to do because of this change?
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"[SUCCESS] Created new ADR at {filename}")

def main():
    parser = argparse.ArgumentParser(description="Software Architecture CLI Tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # C4 Command
    c4_parser = subparsers.add_parser("init-c4", help="Initialize a C4 Context PlantUML diagram")
    c4_parser.set_defaults(func=init_c4)

    # God Class Check Command
    god_parser = subparsers.add_parser("check-god-classes", help="Scan directory for massive files")
    god_parser.add_argument("dir", type=str, help="Directory to scan")
    god_parser.add_argument("--threshold", type=int, default=500, help="Line limit threshold (default: 500)")
    god_parser.set_defaults(func=check_god_classes)

    # ADR Command
    adr_parser = subparsers.add_parser("adr-new", help="Create a new Architecture Decision Record")
    adr_parser.add_argument("title", type=str, help="Title of the ADR")
    adr_parser.set_defaults(func=adr_new)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
