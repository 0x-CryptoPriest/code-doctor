# Overview

Use this skill to judge whether a change is merge-ready.

## Default order
1. Read the diff and the smallest relevant surrounding context.
2. Check repo-local policy first: AGENTS, project docs, CODEOWNERS, CI, lint, typecheck, tests, security config, branch rules, quality gates.
3. Load only the specific reference file for the change type.
4. Prefer concrete evidence over general advice.

## Review policy
- Prefer repo policy over generic thresholds.
- If repo policy is missing, use the fallback guidance in the domain references.
- Keep comments actionable and tied to code.
- Separate findings from questions.
- Report issues introduced by the diff or made reachable by the diff. Put unrelated existing debt in residual risk.
- On incremental reviews, re-check new commits and unresolved blockers; do not repeat resolved comments.

## Severity
- Blocker: correctness, security, data loss, public contract, migration, or quality-gate failure that should stop merge.
- High: clear runtime, regression, or operability risk with a credible trigger.
- Medium: proven maintainability, testability, or architecture risk that will slow safe change.
- Low: omit by default unless the user asks for exhaustive review.

## Finding quality
- High signal only.
- Avoid cosmetic noise unless it blocks readability or maintenance.
- If evidence is weak, label it as risk or question instead of a hard finding.
- Each finding needs a trigger: input, state, call order, config, or user action that makes the issue real.
- Each fix should be the smallest repo-aligned change, or state why the correct fix is broader.
