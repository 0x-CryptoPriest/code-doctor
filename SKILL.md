---
name: code-doctor
description: Evidence-backed code review, repair, and controlled restructure skill for diffs, pull requests, bugs, tests, security, acceptance gaps, and intent alignment. Use when Codex needs to review code changes, fix real defects, verify engineering quality, or propose/perform bounded architecture improvements before merge.
---

# Code Doctor

## Operating mode
Pick one mode before acting, based on the user request. State the mode in the final output.

- `review-only`: default for "review", "audit", or "check"; report findings and do not edit.
- `repair`: use when the user asks to fix, address, repair, or make the change pass.
- `restructure`: use only when structure is a proven blocker or the user asks to remove duplication/simplify.
- `architecture`: use only when the user asks for architecture improvement; default to proposal unless the user authorizes implementation.
- `security`: use when the task concerns secrets, auth, permissions, injection, crypto, compliance, or exposure.

If the requested mode is unclear, choose the least invasive mode that can satisfy the request.
Do not ask the user to pick a mode unless the next action would be risky, destructive, or impossible to infer safely.

## Workflow
1. Build a project intent map from the repo's high-level anchors: README, ADRs, task docs, tests, public API, and config.
2. Inspect the diff, touched files, and nearby code.
3. Load only the reference that matches the change: language, framework, security, API, repair, or architecture.
4. Check intent first, then correctness, maintainability, tests, security, and acceptance.
5. Before any edit, pass the Fix Gate: clear evidence, real impact, smallest safe change, and a relevant validation path.
6. If the code is wrong, weak, off-intent, or structurally poor within the active mode, patch with the smallest change that fixes the real problem.
7. Restructure only inside the reviewed scope: shorten functions, remove duplication, merge repeated logic, and replace unsafe implementations without losing capability.
8. Deepen architecture only when caller knowledge or scattered behavior is the proven risk; hide behavior behind a smaller public interface and preserve tests through that interface.
9. Run a convergence pass: record reviewed scope, adjacent risk surfaces, explicit exclusions, and what a second pass would likely inspect.
10. Re-run the relevant checks, rebuild intent, and review the result again.
11. Prefer repo-local tooling and thresholds over generic defaults.
12. Report findings before summary.

## Fix Gate
Do not patch until all four answers are concrete:

- Evidence: what file, line, diff, test, runtime path, or config proves the issue?
- Impact: what user-visible, runtime, security, data, maintainability, or acceptance risk follows?
- Smallest fix: what is the narrowest repo-aligned change that removes the risk?
- Validation: what test, build, typecheck, lint, command, screenshot, or manual check can confirm it?

If any answer is weak, report it as a question, residual risk, or second-pass item instead of editing.

## Scope control
- Never touch unrelated dirty worktree changes.
- Do not widen blast radius to make code look cleaner.
- Do not convert subjective style preferences into findings.
- Do not rewrite broad architecture during a narrow bug fix unless the current structure blocks the correct fix.
- Do not remove behavior, public API, compatibility, migration paths, logs, or tests unless the intent explicitly allows it.
- Delete redundant code only when no reachable behavior, test fixture, migration, or public contract depends on it.
- Put unrelated existing debt in residual risk, not in the main findings.

## Severity
- `P0`: data loss, security breach, auth bypass, production outage, irreversible migration failure.
- `P1`: clear functional regression, public contract break, core workflow failure, quality gate failure.
- `P2`: proven edge-case bug, maintainability/testability risk with a credible near-term trigger.
- `P3`: low-risk cleanup, naming, style, or documentation issue; omit unless requested or bundled with a fix.

Use `Intent Miss` as a separate hard blocker when the implementation solves the wrong problem.

## Output
- Start with `Intent` using four lines: `Goal`, `Non-goals`, `Constraints`, `Success criteria`.
- Include `Mode: <review-only|repair|restructure|architecture|security>`.
- For non-trivial work, include `Coverage` using three lines: `Reviewed`, `Not reviewed`, `Second-pass check`.
- Findings first, ordered by severity.
- Each finding: `severity`, `file:line`, `evidence`, `impact`, `fix`.
- `Intent Miss` is a separate hard blocker.
- If an issue does not pass the Fix Gate, label it as `Question`, `Residual risk`, or `Deferred`.
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
