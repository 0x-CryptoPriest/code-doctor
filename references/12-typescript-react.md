# TypeScript and React Playbook

Use this file for TypeScript, JavaScript, React, Next.js, Node, and frontend changes.

## Read first
- `package.json`, `tsconfig`, ESLint, formatter config, test runner, framework config, route conventions.
- Existing state, data fetching, form, and component patterns.

## Blockers
- `any`, unsafe casts, non-null assertions, or ignored errors that hide real uncertainty.
- Client trust for authorization, pricing, permissions, rate limits, or ownership.
- Effects that can loop, double-submit, race, leak subscriptions, or update unmounted state.
- Unsanitized HTML, URL, redirect, template, SQL, command, or filesystem input.
- User-visible UI with no loading, empty, error, disabled, or long-content state.

## Review checks
- Prefer narrow types at module edges and runtime validation for external data.
- Keep server-only secrets and privileged logic out of client bundles.
- Keep React state minimal; derive values instead of duplicating source of truth.
- `useEffect` should synchronize with external systems, not patch avoidable render logic.
- Memoization is a tool for measured churn, not a default style.
- Verify accessibility basics: labels, focus, keyboard, contrast, semantic buttons/links.

## Repair moves
- Replace unsafe casts with parsed or narrowed data.
- Move repeated data-shaping, permission, or validation logic to a shared module.
- Add tests that exercise user behavior and contract edges, not implementation details.
