# Repair Loop

Use this file when the task is not only to review but also to repair.

## Loop
1. Identify the highest-signal defect or design flaw.
2. Make the smallest change that fixes the actual problem.
3. Keep the fix aligned with local patterns and existing APIs.
4. Re-run the narrowest relevant checks: tests, lint, typecheck, or screenshot verification.
5. Review the new state again.
6. Run the convergence pass in `references/65-convergence.md`.
7. Repeat until there are no remaining high-signal issues in the reviewed scope.

## Stop conditions
- Remaining issues are cosmetic or subjective.
- Further change would be speculative without more context.
- The next fix would be too broad for the current task.
- Validation is blocked by missing repo setup or missing tool access.
- A broader second pass would require a new scope, service action, credentials, or production operation.

## Guardrails
- Do not pile on unrelated refactors.
- Do not widen the blast radius just to make the code look cleaner.
- Preserve behavior unless the change is explicitly a behavior fix.
- Keep each pass small enough to verify.
- After each repair, re-check the diff for new public behavior, brittle tests, weakened validation, or intent drift.
- Do not claim the whole project is clean unless the whole project was actually reviewed.
