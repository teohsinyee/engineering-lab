# How To Get `PR_APP_ID` And `PR_APP_PRIVATE_KEY`

This guide shows how to create or open a GitHub App and get the two values needed by the workflow:

- `PR_APP_ID`
- `PR_APP_PRIVATE_KEY`

This write-up is meant for general use, not just this repo.

## What These Two Values Are

### `PR_APP_ID`

This is the numeric GitHub App ID.

The workflow uses it together with the private key to mint an installation token for `PR Opener Bot`.

### `PR_APP_PRIVATE_KEY`

This is the full PEM private key generated for the GitHub App.

You store the entire contents of the downloaded private key file as a GitHub Actions secret.

That means you should include:

- `-----BEGIN RSA PRIVATE KEY-----`
- the full key body
- `-----END RSA PRIVATE KEY-----`

## Before You Start

Decide these things first:

- Will the app live under your personal GitHub account or an organization?
- Will the app be reused across multiple repos?
- Who is allowed to generate, rotate, and revoke private keys?

For a reusable solo developer bot, a personal-account-owned app is often the simplest starting point.

## Part 1: Create Or Open The GitHub App

1. In GitHub, open your profile menu.
2. Go to `Settings`.
3. Open `Developer settings`.
4. Open `GitHub Apps`.
5. Do one of the following:
   - If the app does not exist yet, click `New GitHub App`
   - If the app already exists, click `Edit`

Recommended name:

- `PR Opener Bot`

Recommended purpose:

- `Open pull requests for AI-assisted repo work so the human maintainer can stay in the review and approval path`

## Recommended Create App Form Values

Use the smallest practical setup for this workflow.

### Basic Information

- `GitHub App name`: use your chosen unique app name, for example `AI PR Opener Bot`
- Description: `Open pull requests for AI-assisted repo work so the human maintainer can stay in the review and approval path`
- `Homepage URL`: use a repository URL that explains or hosts the workflow, such as `https://github.com/teohsinyee/engineering-lab`

Why this is enough:

- the app needs a homepage because GitHub requires one
- the homepage does not control PR creation behavior
- using the repo URL is a simple and acceptable starting point

### Identifying And Authorizing Users

For this workflow:

- do not add a `Callback URL`
- do not enable `Request user authorization (OAuth) during installation`
- `Expire user authorization tokens` is not needed for this setup

Why:

- this workflow does not use GitHub OAuth sign-in
- it does not redirect users back to your app
- it uses GitHub App installation authentication, not user authorization tokens

### Webhooks

For the first version:

- disable webhook handling
- do not provide a `Webhook URL`
- do not provide a `Webhook secret`

Why:

- the workflow is triggered manually through `workflow_dispatch`
- the app does not need inbound webhook events to open pull requests
- leaving webhooks out keeps the setup smaller and easier to reason about

### Repository Permissions

Start with:

- `Contents`: `Read and write`
- `Pull requests`: `Read and write`
- `Metadata`: read-only is provided by GitHub automatically

Set everything else to `No access` unless implementation proves it is needed later.

Why:

- `Contents` access is needed for repository-level operations tied to the installation
- `Pull requests` access is needed to create the PR and request reviewers
- smaller permission scope is safer and easier to audit

### Organization Permissions

If GitHub shows organization permissions and you are not using org-level features:

- leave them as `No access`

Why:

- this workflow only needs repo-scoped PR automation
- unnecessary org permissions make review harder and increase blast radius

### Installation Scope

When GitHub asks where the app can be installed:

- prefer the smallest scope that still matches your intended usage
- if you want to reuse the app across multiple repos later, that is fine, but still install it selectively where practical

Why:

- the app can be reusable without being installed everywhere
- smaller installation scope reduces accidental access

## Part 2: Get `PR_APP_ID`

1. Open the GitHub App settings page.
2. Look for the app metadata near the top of the page.
3. Copy the numeric `App ID`.
4. Save that value for later.

Use this value as:

- repository secret: `PR_APP_ID`

## Part 3: Generate `PR_APP_PRIVATE_KEY`

1. Stay on the GitHub App settings page.
2. Scroll to the `Private keys` section.
3. Click `Generate a private key`.
4. GitHub will download a `.pem` file to your computer.
5. Open the file in a text editor.
6. Copy the entire file contents exactly as-is.

Use the full PEM contents as:

- repository secret: `PR_APP_PRIVATE_KEY`

Important:

- GitHub only stores the public part of the key
- if you lose the downloaded private key, you cannot recover it from GitHub
- if you only have one key and want to rotate safely later, generate a new key before deleting the old one

## Part 4: Store The Values In GitHub Actions

In the target repository:

1. Open `Settings`
2. Open `Secrets and variables`
3. Open `Actions`
4. Add these secrets:

- `PR_APP_ID`
- `PR_APP_PRIVATE_KEY`

For `PR_APP_PRIVATE_KEY`, paste the entire PEM file content with original line breaks preserved.

## Part 5: Install The App On The Target Repo

The workflow will not work unless the app is installed on the account or repo it needs to access.

After creating the app:

1. Open the app settings
2. Go to the install section for the app
3. Install it on the correct personal account or organization
4. Grant access to the intended repository or repositories

For a smaller blast radius, prefer repo-only access when that matches your use case.

## Common Mistakes

### Secret Contains Only Part Of The Key

Wrong:

- only copying the middle lines
- removing the `BEGIN` or `END` lines

Right:

- copy the full PEM file content exactly

### App Exists But Is Not Installed

Creating the GitHub App is not enough.

You must also install it on the target account or repo.

### Wrong Secret Type

For this workflow:

- `PR_APP_ID` is stored as a secret in this repo's current implementation
- `PR_APP_PRIVATE_KEY` is stored as a secret

If you later move `PR_APP_ID` to an Actions variable, update the workflow and docs together.

### Key Was Lost After Download

GitHub does not let you re-download the original private key later.

If the key is lost:

1. Generate a new private key
2. Update `PR_APP_PRIVATE_KEY`
3. Delete the old key if it is no longer needed

## Security Guidance

- Never commit the PEM file into the repo
- Never paste the key into docs, issues, or PR comments
- Prefer as few private keys as practical
- Rotate keys when ownership or exposure risk changes
- Remove old keys after a safe rotation

## Official References

- [Registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/creating-github-apps/creating-a-github-app)
- [Managing private keys for GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps)
- [Making authenticated API requests with a GitHub App in a GitHub Actions workflow](https://docs.github.com/en/apps/creating-github-apps/guides/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow)
- [Authenticating as a GitHub App installation](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation)
