#!/usr/bin/env python3
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".go", ".json", ".md", ".mjs", ".py", ".swift", ".ts", ".yaml"}
TEXT_PATHS = [
    path
    for path in sorted(ROOT.rglob("*"))
    if path.is_file()
    and path.name != "AGENTS.md"
    and ".git" not in path.parts
    and "__pycache__" not in path.parts
    and ".build" not in path.parts
    and path.suffix in TEXT_SUFFIXES
]
EXTERNAL_LINK_RE = re.compile(r"http" + r"s?://|www" + r"\.")

def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    failures = 0
    skill = (ROOT / "SKILL.md").read_text()
    refs = re.findall(r"`(references/[^`]+)`", skill)
    for ref in refs:
        if not (ROOT / ref).exists():
            failures += fail(f"missing reference {ref}")

    for path in TEXT_PATHS:
        text = path.read_text()
        rel = path.relative_to(ROOT)
        if EXTERNAL_LINK_RE.search(text):
            failures += fail(f"external link in {rel}")

    if failures:
        return 1
    print("OK: skill references, locality, and naming validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
