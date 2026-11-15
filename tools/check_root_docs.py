#!/usr/bin/env python3
"""Validate live root Markdown links, referenced handoff files, and obsolete guidance.

This intentionally excludes MERGE_ARCHIVE history, files generated in CI /tmp,
and off-site URLs. No artwork or authored scripts are modified.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
REQUIRED_HANDOFF = (
    "README.md", "AGENTS.md", "WORK_CHECKPOINT.md", "SERIES_CANON.md",
    "AUDIT_AND_COMPLETION_REPORT.md", "CODEX_IMAGE_TASKS.md",
    "ENGLISH_LEARNING_QA.md", "tools/audit_series.py",
    "tools/check_series.py", "tools/production_handoff.py",
    ".github/workflows/validate.yml",
)

def root_link_issues(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED_HANDOFF:
        if not (root / relative).is_file():
            errors.append(f"missing project handoff {relative}")
    for doc in sorted(root.glob("*.md")):
        body = doc.read_text(encoding="utf-8")
        for m in MARKDOWN_LINK.finditer(body):
            raw = m.group(1).strip().split(maxsplit=1)[0].strip("<>")
            u = urlsplit(raw)
            if u.scheme or u.netloc or not u.path:
                continue
            path = (doc.parent / unquote(u.path)).resolve()
            if not path.exists():
                errors.append(f"{doc.name}: broken root link: {raw}")
    agents = root / "AGENTS.md"
    if agents.is_file():
        content = agents.read_text(encoding="utf-8")
        if "current selected storyboards are exactly" in content and "BOARD_12.png" in content:
            errors.append("AGENTS.md: obsolete Episode 01 12-board instruction")
        if "BOARD_20.png" not in content:
            errors.append("AGENTS.md: active Episode 01 20-board mapping absent")
    checkpoint = root / "WORK_CHECKPOINT.md"
    if checkpoint.is_file():
        body = checkpoint.read_text(encoding="utf-8").lower()
        if "has not been merged into main" in body:
            errors.append("WORK_CHECKPOINT.md: wrongly calls merged PR unmerged")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    failures = root_link_issues(ROOT)
    if failures:
        for fail in failures:
            print("FAIL:", fail)
        return 1
    print("PASS: live root documents and handoff links are consistent; merge history untouched")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
