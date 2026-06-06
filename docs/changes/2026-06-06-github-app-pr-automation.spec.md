# Spec: GitHub App PR Automation

## Scope

This spec defines the first implementation of GitHub App based pull request creation for this repo.

## Workflow

1. Codex works locally and creates commits with author `Codex <codex@openai.com>`.
2. A human pushes the branch normally.
3. A human manually triggers a GitHub Actions workflow with `workflow_dispatch`.
4. The workflow validates the requested branch and base branch inputs.
5. The workflow generates a `PR Opener Bot` GitHub App installation token.
6. The workflow creates a pull request from the requested branch to the requested base.
7. The workflow requests review from `teohsinyee`.
8. `teohsinyee` reviews and decides whether to merge.

## Identity Goal

This flow exists to separate PR opening from PR approval in AI-assisted solo developer workflows.

The PR should be opened by `PR Opener Bot`, while the human maintainer keeps the reviewer or approver role under their personal account.

## Required Inputs

The first version should support:

- `branch`
- `base`
- `title`
- `body`
- `draft`

Possible later additions:

- `labels`
- `milestone`
- `assignees`

## Required GitHub App Permissions

Start with:

- `Contents: Read and write`
- `Pull requests: Read and write`
- `Metadata: Read`

Only add more scopes after confirming a concrete API requirement.

## Required Repository Secrets

- `PR_APP_ID`
- `PR_APP_PRIVATE_KEY`

Optional if implementation requires it:

- `PR_APP_INSTALLATION_ID`

## Required Workflow Behavior

The workflow must:

- accept manual dispatch inputs
- validate that the source branch exists on the remote
- fail clearly when configuration is missing or invalid
- create the PR using the `PR Opener Bot` installation token
- support draft PR creation
- request review from `teohsinyee`

The workflow should, when practical:

- detect duplicate open PRs for the same branch
- return a clear operator-facing error message when the PR already exists

## Phases

### Phase 1: Identity and Permissions

- Create the GitHub App
- Install it on the target repo
- Confirm the App can authenticate inside GitHub Actions
- Confirm repo metadata access works

Exit criteria:

- A workflow can obtain a valid GitHub App installation token

### Phase 2: Minimal PR Creation

- Create the manual `workflow_dispatch` workflow
- Accept `branch`, `base`, and `title`
- Create a draft PR through the App identity

Exit criteria:

- A manual run opens a PR as the GitHub App, not the reviewer personal identity

### Phase 3: Review Routing

- Add `body` and `draft`
- Request review from `teohsinyee`
- Improve failure messages for common operator mistakes

Exit criteria:

- The workflow opens the PR and requests human review automatically

### Phase 4: Governance Hardening

- Add branch existence checks
- Add duplicate PR protection when practical
- Document the operator workflow in the repo

Exit criteria:

- The flow is safe enough for repeated use

## Validation Order

1. Verify App installation and permissions
2. Verify token creation in Actions
3. Verify draft PR creation from a test branch
4. Verify review request to `teohsinyee`
5. Verify `teohsinyee` can still approve the PR

## Supporting Documentation

The following operator-facing docs should exist and stay aligned with the workflow implementation:

- `docs/github-app-pr/setup-checklist.md`
- `docs/github-app-pr/operator-guide.md`
