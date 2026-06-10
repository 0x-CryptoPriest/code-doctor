#!/usr/bin/env python3
import argparse
import difflib
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path


IGNORED_PARTS = {
    "__pycache__",
    ".build",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".git",
    "node_modules",
}
IGNORED_SUFFIXES = {".db", ".o", ".out", ".pyc", ".pyo", ".sqlite"}
SCORER_ONLY_FILES = {"oracle.json", "INTENT.md"}


def load_json(path):
    return json.loads(Path(path).read_text())


def text_files(root):
    root = Path(root)
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in IGNORED_PARTS for part in rel.parts):
            continue
        if path.suffix in IGNORED_SUFFIXES:
            continue
        yield rel


def read_text(path):
    try:
        return Path(path).read_text()
    except UnicodeDecodeError:
        return ""


def run_command(command, cwd, oracle_dir=None, timeout=60):
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = str(cwd) + os.pathsep + env.get("PYTHONPATH", "")
    env["CANDIDATE_DIR"] = str(cwd)
    command = command.format(
        python=shlex.quote(sys.executable),
        candidate=shlex.quote(str(cwd)),
        oracle=shlex.quote(str(oracle_dir)) if oracle_dir else "",
    )
    result = subprocess.run(
        command,
        cwd=cwd,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
        timeout=timeout,
    )
    return {
        "command": command,
        "passed": result.returncode == 0,
        "returncode": result.returncode,
        "output_tail": result.stdout[-4000:],
    }


def score_review(review_path, targets):
    if not review_path:
        return {"score": 0.0, "matched": [], "missing": [target["id"] for target in targets]}
    text = Path(review_path).read_text().lower()
    matched = []
    missing = []
    for target in targets:
        if all(token.lower() in text for token in target["must_mention"]):
            matched.append(target["id"])
        else:
            missing.append(target["id"])
    score = len(matched) / max(1, len(targets))
    return {"score": score, "matched": matched, "missing": missing}


def diff_stats(fixture, candidate, allowed_files):
    fixture = Path(fixture)
    candidate = Path(candidate)
    allowed = {Path(item) for item in allowed_files}
    rels = set(text_files(fixture)) | set(text_files(candidate))
    changed_files = []
    disallowed_files = []
    changed_lines = 0
    for rel in sorted(rels):
        before = read_text(fixture / rel).splitlines()
        after = read_text(candidate / rel).splitlines()
        if before == after:
            continue
        changed_files.append(str(rel))
        if rel not in allowed and rel.name != "oracle.json" and rel.name != "INTENT.md":
            disallowed_files.append(str(rel))
        for line in difflib.unified_diff(before, after, lineterm=""):
            if line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
                changed_lines += 1
    return {
        "changed_files": changed_files,
        "disallowed_files": disallowed_files,
        "changed_lines": changed_lines,
    }


def forbidden_hits(candidate, patterns):
    hits = []
    for rel in text_files(candidate):
        if rel.name in SCORER_ONLY_FILES:
            continue
        text = read_text(Path(candidate) / rel)
        for pattern in patterns:
            if pattern in text:
                hits.append({"file": str(rel), "pattern": pattern})
    return hits


def main():
    parser = argparse.ArgumentParser(description="Score a repaired code-doctor benchmark fixture.")
    parser.add_argument("candidate", help="Path to the repaired fixture directory.")
    parser.add_argument(
        "--fixture",
        default=str(Path(__file__).resolve().parents[1] / "benchmarks" / "fixtures" / "python-ledger"),
        help="Path to the fixture root containing repo/, oracle/, and oracle.json.",
    )
    parser.add_argument("--review", help="Optional review.md produced by the agent.")
    parser.add_argument("--json", action="store_true", help="Emit compact JSON only.")
    args = parser.parse_args()

    fixture = Path(args.fixture).resolve()
    candidate = Path(args.candidate).resolve()
    fixture_repo = fixture / "repo"
    oracle_dir = fixture / "oracle"
    oracle = load_json(fixture / "oracle.json")
    timeout = oracle.get("timeout_seconds", 60)

    review = score_review(args.review, oracle["review_targets"])
    public = run_command(oracle["commands"]["public"], candidate, timeout=timeout)
    hidden = run_command(
        oracle["commands"]["oracle"],
        candidate,
        oracle_dir=oracle_dir,
        timeout=timeout,
    )
    diff = diff_stats(fixture_repo, candidate, oracle["repair"]["allowed_files"])
    forbidden = forbidden_hits(candidate, oracle["repair"]["forbidden_patterns"])
    over_edit = bool(
        diff["disallowed_files"]
        or diff["changed_lines"] > oracle["repair"]["max_changed_lines"]
        or forbidden
    )

    weights = oracle["weights"]
    score = (
        review["score"] * weights["bug_found"]
        + (1.0 if hidden["passed"] else 0.0) * weights["bug_fixed"]
        + (1.0 if public["passed"] else 0.0) * weights["regression_free"]
        - (weights["over_edit_penalty"] if over_edit else 0.0)
    )
    score = max(0.0, min(1.0, score))

    result = {
        "case_id": oracle["id"],
        "score": round(score, 4),
        "bug_found": round(review["score"], 4),
        "bug_fixed": hidden["passed"],
        "regression_free": public["passed"],
        "over_edit": over_edit,
        "details": {
            "matched_findings": review["matched"],
            "missing_findings": review["missing"],
            "public_test": public,
            "oracle_test": hidden,
            "diff": diff,
            "forbidden_hits": forbidden,
        },
    }

    output = json.dumps(result, indent=None if args.json else 2, sort_keys=True)
    print(output)
    return 0 if score >= 0.8 and public["passed"] and hidden["passed"] and not over_edit else 1


if __name__ == "__main__":
    sys.exit(main())
