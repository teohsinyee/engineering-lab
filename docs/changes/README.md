# Change Index

This folder records why a change exists, not only what changed.

It is here so future implementation work does not have to rediscover the same intent, tradeoffs, and operating rules from scratch.

Use:

- `*.prd.md` for the goal, context, and why the change matters
- `*.decision.md` for tradeoffs, constraints, and final choices
- `*.spec.md` for the implementation and operating rules
- `*.logs.md` for failures, lessons, and validation notes worth keeping

## Naming Convention

Use date-prefixed filenames so changes sort naturally:

```text
YYYY-MM-DD-change-name.prd.md
YYYY-MM-DD-change-name.decision.md
YYYY-MM-DD-change-name.spec.md
YYYY-MM-DD-change-name.logs.md
```

## Current Changes

- `2026-06-06-github-app-pr-automation`
  - PRD: [2026-06-06-github-app-pr-automation.prd.md](./2026-06-06-github-app-pr-automation.prd.md)
  - Decision: [2026-06-06-github-app-pr-automation.decision.md](./2026-06-06-github-app-pr-automation.decision.md)
  - Spec: [2026-06-06-github-app-pr-automation.spec.md](./2026-06-06-github-app-pr-automation.spec.md)
  - Logs: [2026-06-06-github-app-pr-automation.logs.md](./2026-06-06-github-app-pr-automation.logs.md)
  - Supporting docs: [operator guide](../github-app-pr/operator-guide.md), [setup checklist](../github-app-pr/setup-checklist.md)
