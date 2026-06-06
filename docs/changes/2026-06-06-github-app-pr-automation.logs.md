# Logs: GitHub App PR Automation

## Purpose

Use this file to capture implementation-time evidence that is worth preserving, especially:

- permission errors
- token generation failures
- review request edge cases
- duplicate PR behavior
- final validation results

## Current Status

Planning structure created on `2026-06-06`.

Workflow implementation added at `.github/workflows/create-pr-via-app.yml`.

No live GitHub Actions run has been executed yet in this repo.

## Recorded Notes

### 2026-06-06

- Context: First implementation pass for `PR Opener Bot` workflow
- Action: Added a manual `workflow_dispatch` workflow that validates inputs, creates a GitHub App installation token, blocks duplicate open PRs, creates the PR, and requests review from `teohsinyee`
- Result: Workflow file created locally; live validation still pending because repo secrets and GitHub App installation were not exercised in this session
- Follow-up: Run the workflow in GitHub after configuring `PR_APP_ID` and `PR_APP_PRIVATE_KEY`, then record any permission or review-request surprises

### 2026-06-06

- Context: Needed a public-facing guide for getting `PR_APP_ID` and `PR_APP_PRIVATE_KEY`
- Action: Added `docs/github-app-pr/app-credentials-guide.md` with step-by-step guidance for creating or opening a GitHub App, copying the App ID, generating a PEM private key, storing both as Actions secrets, and avoiding common mistakes
- Result: The setup docs now include a dedicated credential guide that can be reused across repos and by non-expert operators
- Follow-up: Keep the guide aligned if the workflow later moves `PR_APP_ID` from a secret to an Actions variable

### 2026-06-06

- Context: The chat included important Create App form guidance that should not stay only in conversation history
- Action: Expanded `docs/github-app-pr/app-credentials-guide.md` with recommended values and rationale for the Create GitHub App form, including homepage URL, callback URL, OAuth settings, webhook settings, repository permissions, organization permissions, and installation scope
- Result: The docs now capture the practical field-by-field setup guidance needed during GitHub App creation
- Follow-up: If the final chosen app name or permission set changes during live setup, update the guide to match the real production configuration

### 2026-06-06

- Context: Wanted a local workflow lint check before asking for a live GitHub Actions run
- Action: Installed `actionlint` version `1.7.12` via `winget`, then ran it against `.github/workflows/create-pr-via-app.yml`
- Result: Lint passed with no workflow errors; on Windows, the new PATH entry was not available in the current shell immediately, so the installed binary was invoked via its absolute path under `AppData\\Local\\Microsoft\\WinGet\\Packages`
- Follow-up: After opening a fresh shell, confirm whether the `actionlint` alias is available directly without the absolute path workaround

## Suggested Log Format

### YYYY-MM-DD

- Context:
- Action:
- Result:
- Follow-up:
