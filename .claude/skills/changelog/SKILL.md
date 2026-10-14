---
name: changelog
description: Summarise the changes since a baseline (a tag or ref) into a changelog entry grouped as Added, Changed and Fixed. Use when preparing a release or a progress update.
---

# Changelog

Baseline: the ref passed as `$ARGUMENTS` if one was given. Otherwise the most recent git tag, or the last 20 commits if there are no tags.

1. Read the commits and the diff since the baseline.
2. Group the changes under **Added**, **Changed** and **Fixed**. Leave out empty groups.
3. Write each item as one line a user would understand: what changed and what it means for them. Do not copy commit subjects. Skip formatting and lockfile changes.
4. Output Markdown, ready to paste under a new version heading.
