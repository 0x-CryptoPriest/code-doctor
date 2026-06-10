# Overview

Use this skill to judge whether a change is merge-ready.

## Default order
1. Read the diff and the smallest relevant surrounding context.
2. Check repo-local policy first: AGENTS, project docs, CODEOWNERS, CI, lint, typecheck, tests, security config, branch rules, quality gates.
3. Load only the specific reference file for the change type.
4. Pick the least invasive operating mode that satisfies the request.
5. Prefer concrete evidence over general advice.

## Review policy
- Prefer repo policy over generic thresholds.
- If repo policy is missing, use the fallback guidance in the domain references.
- Keep comments actionable and tied to code.
- Separate findings from questions.
- Report issues introduced by the diff or made reachable by the diff. Put unrelated existing debt in residual risk.
- On incremental reviews, re-check new commits and unresolved blockers; do not repeat resolved comments.
- In `review-only` mode, do not patch even if the fix is obvious.
- In repair modes, edit only findings that pass the Fix Gate in `SKILL.md`.

## Severity
- P0: data loss, security breach, auth bypass, production outage, irreversible migration failure.
- P1: clear functional regression, public contract break, core workflow failure, quality gate failure.
- P2: proven edge-case bug, maintainability/testability risk with a credible near-term trigger.
- P3: low-risk cleanup, naming, style, or documentation issue; omit unless requested or bundled with a fix.

## Finding quality
- High signal only.
- Avoid cosmetic noise unless it blocks readability or maintenance.
- If evidence is weak, label it as risk or question instead of a hard finding.
- Each finding needs a trigger: input, state, call order, config, or user action that makes the issue real.
- Each fix should be the smallest repo-aligned change, or state why the correct fix is broader.
- Findings without evidence, impact, fix, and validation are not ready to repair.
