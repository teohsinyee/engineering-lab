# PRD: GitHub App PR Automation

## Problem

We want AI-assisted local development to stay fast, but we do not want pull requests to be opened under the human approver identity by default.

This is especially painful for a solo developer workflow. When AI helps write code, the same human still needs a workable review and merge path. If the PR is opened under the same personal account that is supposed to review it, that person cannot meaningfully separate PR opening from PR approval.

## Goal

Create a governed pull request creation path where:

- Codex can work locally and create commits with author `Codex <codex@openai.com>`
- A human explicitly decides when a pull request should be opened
- The pull request is created through the GitHub App identity `PR Opener Bot`
- Human review remains required before merge

## Why This Matters

- It separates AI-authored development from human approval
- It separates PR opening from PR approval for solo developers
- It improves auditability compared with using a personal account end to end
- It gives us a narrower permission model than a shared bot user
- It creates a repeatable workflow that can scale beyond one repo or one session
- It creates one reusable bot identity for both personal and work repos

## Users

- Primary operator: the human maintainer who triggers pull request creation
- Secondary operator: Codex working locally on implementation changes
- Reviewer: `teohsinyee`
- GitHub App identity: `PR Opener Bot`

## Success Criteria

- Codex-authored commits can still be pushed normally
- A human can trigger pull request creation manually
- The PR is opened through the GitHub App path, not the reviewer personal identity
- Review is automatically requested from `teohsinyee`
- The workflow is documented clearly enough to repeat later without relying on memory
- The same GitHub App pattern can be reused across multiple repos

## Non-Goals

- Replacing human review
- Auto-merging AI-generated changes
- Letting the GitHub App approve pull requests
- Expanding the GitHub App into a broad repo admin identity

## Deliverables

- A GitHub App configuration checklist
- A GitHub Actions workflow for manual PR creation
- Repo documentation for the operator flow
- Validation notes capturing any GitHub permission or API surprises

## Documentation Targets

To keep planning and execution cleanly separated:

- change intent lives under `docs/changes/`
- operator runbooks live under `docs/github-app-pr/`
