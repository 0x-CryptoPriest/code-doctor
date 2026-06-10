# Security and Compliance

Use this file for defensive review only.

## Checks
- Authn and authz are explicit and least-privilege.
- Inputs are parameterized and escaped where needed.
- Secrets are not hardcoded or logged.
- Deserialization, file access, redirects, and SSRF paths are constrained.
- Crypto and password handling use modern, approved defaults.
- Dependencies and licenses match repo policy.

## What to flag
- SQL, shell, template, or path injection risk.
- Overbroad permissions or missing authorization checks.
- Secret leakage in code, tests, configs, or logs.
- Security-sensitive code that lacks review or tests.
- Third-party package risk that the repo policy would reject.

## Review moves
- Treat security hotspots as review items, not proof of exploitation.
- Treat scanner or tool output as evidence to verify, not as the conclusion.
- Confirm source, sink, sanitizer, authorization boundary, and reachability before calling a hotspot exploitable.
- Prefer the safest existing project pattern.
- If the code touches tokens, passwords, or keys, be strict.
- Fix leaks and authorization gaps at the decision point; do not rely on filtering after broad data access.
