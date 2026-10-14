---
name: draft-pr
description: Turn a finished, verified change into one clean commit and a draft pull request. Use when the work is done and tested and you want it reviewed.
---

# Draft PR

1. Run the project's tests and linter. Stop if they fail: fix them or report the failure.
2. Read the diff (`git diff`). If it holds two unrelated changes, say so and propose a split.
3. If you are on the default branch, create a topic branch first.
4. Write the commit message: a one-line summary in imperative mood, 72 characters or fewer, then a short body that explains why.
5. Open a **draft** PR. The body covers what changed, why, and how to verify it.
6. Report the PR link. Do not mark it ready for review unless asked.

## Rules

- Never force-push or rewrite shared history without explicit approval.
- Keep the PR to one change. Small diffs get reviewed faster.
