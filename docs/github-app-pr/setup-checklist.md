# GitHub App PR Setup Checklist

This checklist is for the first-time setup of `PR Opener Bot`, a reusable GitHub App for opening pull requests across repos.

## Outcome

After finishing this checklist:

- the repo can use `PR Opener Bot` for PR creation
- GitHub Actions can mint an installation token for that App
- a human can manually trigger PR creation
- review is still routed to `teohsinyee`

## Why This Exists

This setup solves a solo developer workflow problem:

- AI can help write the code
- the human still needs a clean review and merge path
- if the same personal account opens the PR, that same person cannot cleanly act as the approver

`PR Opener Bot` creates a separate PR opener identity so the human account can stay in the reviewer or approver role.

## 1. Confirm The Repo Target

- [ ] Confirm the target repository name
- [ ] Confirm the default branch name
- [ ] Confirm `teohsinyee` is the intended reviewer account
- [ ] Confirm the human operator will trigger PR creation manually from Actions

## 2. Create The GitHub App

Create a new GitHub App and keep the scope intentionally narrow.

- [ ] Set the app name to `PR Opener Bot`
- [ ] Set the owner to the correct GitHub account or organization
- [ ] Set a homepage URL that points to this repository or a repo doc
- [ ] Disable any webhook setup unless implementation later requires it

Suggested app purpose:

`Open pull requests for AI-assisted repo work so the human maintainer can stay in the review and approval path`

## 3. Configure GitHub App Permissions

Start with the minimum practical permissions:

- [ ] `Contents: Read and write`
- [ ] `Pull requests: Read and write`
- [ ] `Metadata: Read`

Do not add more permissions unless implementation proves they are required.

If review request APIs fail during implementation:

- [ ] Record the exact failing API call
- [ ] Confirm whether the failure is permission-related or request-shape-related
- [ ] Add only the smallest extra permission needed
- [ ] Record the reason in `docs/changes/2026-06-06-github-app-pr-automation.logs.md`

## 4. Generate Credentials

- [ ] Copy the GitHub App ID
- [ ] Generate a private key
- [ ] Store the private key in a secure temporary local location
- [ ] Confirm who is allowed to manage or rotate this key

## 5. Install The App On The Repo

- [ ] Install the App on this repository only, if possible
- [ ] Confirm the installation includes the correct repo
- [ ] Confirm the installation owner is correct
- [ ] Capture the installation ID if the workflow implementation chooses to use it explicitly

## 6. Add GitHub Actions Secrets

In repository secrets, add:

- [ ] `PR_APP_ID`
- [ ] `PR_APP_PRIVATE_KEY`

Optional only if implementation needs it:

- [ ] `PR_APP_INSTALLATION_ID`

Secret handling checks:

- [ ] The private key is pasted with original line breaks preserved
- [ ] No extra quote wrapping is added unless the workflow expects it
- [ ] Secret names match the workflow exactly

## 7. Add Or Update The Workflow

The workflow should:

- [ ] use `workflow_dispatch`
- [ ] accept `branch`, `base`, `title`, `body`, and `draft`
- [ ] generate a GitHub App installation token
- [ ] validate branch existence before PR creation
- [ ] create the PR through the App identity
- [ ] request review from `teohsinyee`
- [ ] fail clearly on duplicate PRs or bad inputs

Recommended operator-facing messages:

- [ ] missing secret error is explicit
- [ ] branch-not-found error is explicit
- [ ] duplicate-PR error is explicit
- [ ] review-request failure is explicit

## 8. Run Validation In Order

- [ ] Validate App authentication in GitHub Actions
- [ ] Validate token creation
- [ ] Validate draft PR creation from a test branch
- [ ] Validate reviewer request to `teohsinyee`
- [ ] Validate that `teohsinyee` can still approve and merge normally

## 9. Record Evidence

- [ ] Save final workflow behavior notes in the change logs file
- [ ] Record any permission surprises
- [ ] Record any API endpoint quirks
- [ ] Update the operator guide if the real workflow differs from the planned flow

## 10. Ready For Routine Use

This setup is ready for routine use only when all of the following are true:

- [ ] PR creation runs under the GitHub App identity
- [ ] The workflow is manually triggered by a human
- [ ] Human review remains required
- [ ] Failure cases are understandable without reading workflow source code
- [ ] The repo docs are clear enough for reuse later
