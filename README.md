# Code Doctor

Code Doctor is a review, repair, and restructure skill for serious codebases.

It is built to find real bugs, fix them, re-check the result, and keep going until the reviewed scope has no high-signal issues left.

## Install

Codex:

```bash
npx --yes skills add https://github.com/0x-CryptoPriest/code-doctor -g --skill code-doctor --agent codex -y --copy
```

Claude:

```bash
npx --yes skills add https://github.com/0x-CryptoPriest/code-doctor -g --skill code-doctor --agent claude-code -y --copy
```

Private repo access requires GitHub auth on the machine.

## Why It Is Strong

- Intent-first review: it builds a project intent map before judging code.
- Intent Miss is a hard blocker: passing tests are not enough if the code solves the wrong problem.
- Repair loop: it fixes the highest-signal issue, validates, reviews again, and repeats.
- Restructure pass: it shortens functions, removes duplication, improves safety, and preserves behavior.
- Architecture deepening: it reduces caller knowledge, improves locality, and tests through public interfaces.
- Convergence pass: it records reviewed scope and asks what a second review would inspect.
- Language playbooks: Python, TypeScript/React, Go, Swift, backend API, and security audit rules are split into concise references.
- Local benchmarks: Python, TS/React, Go, and Swift fixtures measure bug finding, bug fixing, regressions, and over-editing.
- Gold examples: expected review and repair outputs are bundled so agents produce stable, useful reports.
- Self-contained: the skill has no runtime dependency on external review services.

## Local Installer

After cloning the repo:

```bash
./install.sh --all --force
```

Use `--codex` or `--claude` to install only one target.
