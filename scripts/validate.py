#!/usr/bin/env python3
"""Fail if a bot profile drifts from the loops quality bar."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOTS = ROOT / "bots"
GROUPS = ROOT / "groups"
REQUIRED = 20
GROUP_SIZE = 6
BANNED = (
    "you are a helpful",
    "general helper",
    "as an ai",
    "i hope this helps",
)
HARD_STOP = re.compile(r"\b(never|do not|don't|without approval)\b", re.I)
PIPELINE = re.compile(r"(→|->|gather|rank|draft|return)", re.I)
NAME = re.compile(r"^[a-z][a-z0-9-]{0,23}$")
FRONT = re.compile(
    r"^---\nname:\s*(.+)\njob:\s*(.+)\ncategory:\s*(.+)\nplugins:\s*\[(.*?)\]\n---\n",
    re.S,
)
GROUP_FRONT = re.compile(
    r"^---\nname:\s*(.+)\ntitle:\s*(.+)\nbots:\s*\[(.*?)\]\n---\n",
    re.S,
)


def fail(msg: str) -> None:
    print(f"FAIL {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    files = sorted(BOTS.glob("*.md"))
    if len(files) != REQUIRED:
        fail(f"want {REQUIRED} bots/*.md, got {len(files)}")
    names: set[str] = set()
    jobs: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        m = FRONT.match(text)
        if not m:
            fail(f"{path.name}: front matter must be name, job, category, plugins")
        name, job, category, _plugins = (x.strip() for x in m.groups())
        if path.stem != name:
            fail(f"{path.name}: filename stem must equal name {name!r}")
        if not NAME.match(name):
            fail(f"{path.name}: name must be short lowercase")
        if name in names:
            fail(f"duplicate name {name}")
        names.add(name)
        if job in jobs:
            fail(f"duplicate job {job!r}")
        jobs.add(job)
        if category not in {"eng", "ops", "growth", "personal", "markets"}:
            fail(f"{path.name}: bad category {category}")
        body = text[m.end() :].lstrip("\n")
        if not body.startswith(f"# {name}"):
            fail(f"{path.name}: h1 must be # {name}")
        parts = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        if len(parts) < 2:
            fail(f"{path.name}: need heading plus description")
        desc = parts[1]
        if not (80 <= len(desc) <= 520):
            fail(f"{path.name}: description length {len(desc)} not in 80-520")
        if not HARD_STOP.search(desc):
            fail(f"{path.name}: description needs a hard stop")
        if not PIPELINE.search(desc):
            fail(f"{path.name}: description needs a pipeline or return")
        low = text.lower()
        for bad in BANNED:
            if bad in low:
                fail(f"{path.name}: banned phrase {bad!r}")
        if "first task" not in low:
            fail(f"{path.name}: missing First task")
    print(f"ok {len(files)} bots")
    validate_groups(names)


def validate_groups(bot_names: set[str]) -> None:
    files = sorted(GROUPS.glob("*.md"))
    if not files:
        fail("want at least one groups/*.md")
    seen: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        m = GROUP_FRONT.match(text)
        if not m:
            fail(f"{path.name}: front matter must be name, title, bots")
        name, title, raw_bots = (x.strip() for x in m.groups())
        if path.stem != name:
            fail(f"{path.name}: filename stem must equal name {name!r}")
        if not NAME.match(name):
            fail(f"{path.name}: name must be short lowercase")
        if name in seen:
            fail(f"duplicate group {name}")
        seen.add(name)
        if not title:
            fail(f"{path.name}: empty title")
        roster = [b.strip() for b in raw_bots.split(",") if b.strip()]
        if len(roster) != GROUP_SIZE:
            fail(f"{path.name}: want {GROUP_SIZE} bots, got {len(roster)}")
        if len(set(roster)) != GROUP_SIZE:
            fail(f"{path.name}: duplicate bot on the roster")
        for bot in roster:
            if bot not in bot_names:
                fail(f"{path.name}: unknown bot {bot}")
            if f"@{bot}" not in text.lower():
                fail(f"{path.name}: kickoff must @{bot}")
        low = text.lower()
        if "## kickoff" not in low:
            fail(f"{path.name}: missing Kickoff")
        if "## hard stop" not in low:
            fail(f"{path.name}: missing Hard stop")
        if not HARD_STOP.search(text):
            fail(f"{path.name}: needs a hard stop")
    print(f"ok {len(files)} groups")


if __name__ == "__main__":
    main()
