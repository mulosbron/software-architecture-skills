#!/usr/bin/env python3
"""
Demo script from the Hermes + Headless Claude CLI walkthrough:
Fetches the top N Hacker News stories via the official Firebase API and writes
a clean Markdown summary.
"""

import argparse
import datetime
import json
import urllib.request
from pathlib import Path

HN_TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{item_id}.json"


def fetch_json(url: str, timeout: int = 10):
    req = urllib.request.Request(url, headers={"User-Agent": "agent-harness-skillset/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_top_stories(limit: int = 5) -> list:
    story_ids = fetch_json(HN_TOP_URL)[:limit]
    stories = []
    for sid in story_ids:
        item = fetch_json(HN_ITEM_URL.format(item_id=sid))
        if item:
            stories.append(
                {
                    "title": item.get("title", "Untitled"),
                    "url": item.get("url") or f"https://news.ycombinator.com/item?id={sid}",
                    "score": item.get("score", 0),
                    "by": item.get("by", "unknown"),
                    "comments": item.get("descendants", 0),
                }
            )
    return stories


def render_markdown(stories: list) -> str:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"# Top {len(stories)} Hacker News Stories ({now})", ""]
    for i, s in enumerate(stories, 1):
        lines.append(
            f"{i}. **[{s['title']}]({s['url']})** — {s['score']} points by `{s['by']}` ({s['comments']} comments)"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch top Hacker News stories to Markdown")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--out", default="hackernews_top5.md")
    args = parser.parse_args()

    stories = fetch_top_stories(limit=args.limit)
    md = render_markdown(stories)
    Path(args.out).write_text(md, encoding="utf-8")
    print(md)
    print(f"[OK] Saved to {args.out}")


if __name__ == "__main__":
    main()
