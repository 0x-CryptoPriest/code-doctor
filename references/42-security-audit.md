# Security Audit Playbook

Use this file when code touches auth, data ownership, input handling, secrets, files, network calls, crypto, dependencies, or logs.

## Blockers
- Authorization missing, client-enforced, or checked after data access.
- SQL, command, template, LDAP, path, SSRF, open redirect, or deserialization injection.
- Secrets, tokens, credentials, session IDs, or PII stored, logged, returned, or committed.
- Weak password, token, random, crypto, or signature handling.
- Dependency, license, or generated-code change that bypasses repo policy.
- Security-sensitive behavior without regression tests or review evidence.

## Review checks
- Treat every external value as untrusted: request data, headers, URLs, files, env, queues, webhooks.
- Check both read and write authorization, including bulk, export, include-deleted, admin, and retry paths.
- Constrain filesystem paths to an allowed base and reject traversal after resolving the path.
- Constrain outbound network targets before fetching; deny private metadata and loopback targets unless explicitly allowed.
- Prefer allowlists over blocklists for redirects, file types, domains, and privileged actions.
- Ensure error messages and logs do not reveal secrets or authorization facts.

## Repair moves
- Add an exploit-shaped regression test when safe to do locally.
- Fix at the decision point, not by filtering results after a leak-prone query.
- Centralize repeated authorization or input validation so the same bug cannot return at another caller.
