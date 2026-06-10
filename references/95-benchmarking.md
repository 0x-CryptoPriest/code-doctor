# Benchmarking Protocol

Use this file only when evaluating the skill itself.

## Rules
- Do not give the repair agent `oracle.json`, expected defects, scoring logic, or this file.
- Give the agent only the selected fixture's `repo` directory: code, intent file, and public tests.
- Save the agent review as `review.md` if measuring findings.
- Score only after the agent has finished reviewing or repairing.

## Local run
1. Pick a fixture under `benchmarks/fixtures`.
2. Copy that fixture's `repo` directory to a temp directory.
3. Ask an agent to review and repair the temp copy using this skill.
4. Run:

```bash
python3 scripts/score_benchmark.py /tmp/repaired-repo \
  --fixture benchmarks/fixtures/python-ledger \
  --review /tmp/review.md
```

Available fixtures:
- `python-ledger`: Python security, intent, data ownership, money, and over-edit traps.
- `ts-react-dashboard`: TypeScript React-style tenant, XSS, state mutation, key, and redirect traps.
- `go-checkout`: Go pricing, coupon ownership, expiry, and invalid input traps.
- `swift-ledger`: Swift owner scoping, soft delete, negative amount, and audit privacy traps.

## Metrics
- `bug_found`: fraction of expected findings mentioned in the review.
- `bug_fixed`: hidden oracle behavior passes after repair.
- `regression_free`: public behavior still passes after repair.
- `over_edit`: disallowed files, forbidden patterns, or excessive changed lines.

Use the score as a signal, not as the only judgment. Read the diff when the score is surprising.
