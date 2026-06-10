# TS React Dashboard Fixture Intent

The dashboard prepares user rows for a React admin screen.

Required behavior:
- Viewers can see only active users in their own organization.
- Admins can see active users in their own organization, not other organizations.
- User display text must be safe to render and must not preserve raw HTML/event handlers.
- Row keys must be stable across filtering and sorting.
- Rendering must not mutate the caller's `users` array.
- Profile links may carry only local `next` paths.

Non-goals:
- No real network request, router, CSS, or browser runtime.
- No package install; the fixture runs with Node's built-in TypeScript support.
