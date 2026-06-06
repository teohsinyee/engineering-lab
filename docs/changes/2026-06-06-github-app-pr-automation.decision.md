# Decision: GitHub App PR Automation

## Decision Summary

We will manage this work as a structured change record under `docs/changes` instead of keeping the plan only as a standalone root-level note.

We will implement PR creation through a manually triggered GitHub Actions workflow that authenticates as a GitHub App installation.

The GitHub App will be named `PR Opener Bot` so it can be reused across personal and work repos instead of sounding repo-specific.

## Final Choices

- Keep local development in Codex
- Keep human intent explicit with `workflow_dispatch`
- Use the GitHub App `PR Opener Bot` and its installation token to create pull requests
- Request review from `teohsinyee` automatically
- Start with minimum practical GitHub App permissions and widen only when implementation proves it is necessary

## Why This Approach

- `workflow_dispatch` is a clean governance checkpoint
- A GitHub App gives clearer identity separation than using a personal token
- A reusable bot identity solves the solo developer problem where the same personal account should not be both PR opener and approver
- Installation-scoped auth is easier to reason about than a shared user account
- Splitting planning into PRD, decision, spec, and logs makes future updates easier to extend without rewriting the original thinking

## Tradeoffs

### Benefits

- Better audit trail
- Narrower access surface
- Clearer operator flow
- Easier future maintenance

### Costs

- More setup than using a PAT
- GitHub App permissions can be finicky in practice
- Review requests or labels may require permission adjustments during implementation

## Constraints

- Human approval must stay required before merge
- The GitHub App should not become a generic write path
- Misconfiguration should fail clearly
- The workflow should stay usable by a human operator without custom local tooling

## Open Questions To Resolve During Implementation

- Whether review requests need any extra permission beyond pull request write access
- Whether duplicate PR prevention should be a hard block or a warning
- Whether labels, assignees, or milestone support belong in the first implementation or later
