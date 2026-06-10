# Source Map

This skill is self-contained. Use this file only when you need the reasoning behind a rule.

## Localized principles
- Product quality models justify checking functional correctness, reliability, security, maintainability, usability, compatibility, and performance.
- Software review standards justify evidence-first findings, severity, explicit impact, and clear disposition.
- Secure coding taxonomies justify strict treatment of auth, injection, secrets, unsafe deserialization, SSRF, logging, and dependency risk.
- Modular design literature justifies small interfaces, high leverage, locality, deletion tests, and testing through public interfaces.
- Legacy-code testing practice justifies finding seams only where behavior must vary or be isolated for verification.
- Enterprise architecture patterns justify ports/adapters for owned remote dependencies and narrow adapters for true external services.
- Language style guides justify repo-native formatting, naming, typing, error handling, and idioms over generic preference.
- Automated review practice justifies diff-scoped findings, incremental review, repository policy first, and concise quality-gate reporting.

## Rule mapping
- Intent-first review: product quality, software review standards, acceptance traceability.
- Findings with trigger, evidence, impact, fix: software review standards and automated review practice.
- Blocker severity for correctness, security, public contracts, migration, and quality gates: product quality and review disposition practice.
- Security hotspots require reachability confirmation: secure coding taxonomies and defensive review practice.
- Repair loop with validation after every patch: software life-cycle quality control and regression-testing practice.
- Coverage ledger and convergence pass: software review disposition practice, regression-testing practice, and change-impact analysis.
- Architecture deepening: modular design literature, legacy-code testing practice, and enterprise architecture patterns.
- Language playbooks: language style guides plus secure coding and maintainability principles.
