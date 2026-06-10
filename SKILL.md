---
name: code-doctor
description: Concise evidence-backed code review, repair, and restructure skill for diffs, pull requests, refactors, bugs, tests, security, acceptance gaps, and intent alignment. Use when Codex needs to review code changes, repair bugs, restructure code, or re-verify engineering quality before merge.
---

# Code Doctor

## Workflow
1. Build a project intent map from the repo's high-level anchors: README, ADRs, task docs, tests, public API, and config.
2. Inspect the diff, touched files, and nearby code.
3. Load only the reference that matches the change: language, framework, security, API, repair, or architecture.
4. Check intent first, then correctness, maintainability, tests, security, and acceptance.
5. If the code is wrong, weak, off-intent, or structurally poor, patch or restructure it with the smallest change that fixes the real problem.
6. When structure is poor, perform a restructure pass: shorten functions, remove duplication, merge repeated logic, and replace unsafe or hard-to-maintain implementations without losing capability.
7. When architecture is shallow, deepen the module: reduce caller knowledge, concentrate behavior, and test through the public interface.
8. Run a convergence pass: record reviewed scope, adjacent risk surfaces, explicit exclusions, and what a second pass would likely inspect.
9. Re-run the relevant checks, rebuild intent, and review the result again.
10. Prefer repo-local tooling and thresholds over generic defaults.
11. Report findings before summary.

## Output
- Start with `Intent` using four lines: `Goal`, `Non-goals`, `Constraints`, `Success criteria`.
- For non-trivial work, include `Coverage` using three lines: `Reviewed`, `Not reviewed`, `Second-pass check`.
- Findings first, ordered by severity.
- Each finding: `severity`, `file:line`, `evidence`, `impact`, `fix`.
- `Intent Miss` is a separate hard blocker.
- If you restructured code, summarize the module/function consolidation and the behavior preserved.
- If you deepened architecture, summarize the interface reduced, behavior hidden, and tests moved or preserved.
- If nothing is wrong, say that clearly and note residual risk or test gaps.
- If you repaired code, summarize the change, the validation run, and any remaining risk.

## Reference map
- Overview and review contract: `references/00-overview.md`
- Static analysis and style: `references/10-static-analysis.md`
- Tests and quality gates: `references/20-testing-quality-gates.md`
- PR review heuristics: `references/30-peer-review.md`
- Security and compliance: `references/40-security-compliance.md`
- Acceptance and UI checks: `references/50-acceptance-and-ui.md`
- Repair loop: `references/60-repair-loop.md`
- Convergence and coverage: `references/65-convergence.md`
- Intent evaluation: `references/70-intent-evaluation.md`
- Restructure pass: `references/80-restructure.md`
- Architecture deepening: `references/85-architecture-deepening.md`
- Python playbook: `references/11-python.md`
- TypeScript and React playbook: `references/12-typescript-react.md`
- Go playbook: `references/13-go.md`
- Swift playbook: `references/14-swift.md`
- Backend API playbook: `references/41-api-backend.md`
- Security audit playbook: `references/42-security-audit.md`
- Benchmarking protocol: `references/95-benchmarking.md`
- Source map: `references/90-sources.md`

## Evaluation assets
- Benchmark scorer: `scripts/score_benchmark.py`
- Skill validator: `scripts/validate_skill.py`
- Local fixtures: `benchmarks/fixtures`
- Gold review example: `examples/review-output.md`
- Gold repair example: `examples/repair-loop-output.md`
