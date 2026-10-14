---
name: explain-codebase
description: Map an unfamiliar codebase (structure, entry points, conventions, risky areas) before changing anything. Use at the start of work on a repo you do not know yet.
---

# Explain codebase

1. Read the orientation files first: README, CLAUDE.md, package or manifest files, and any docs/ folder.
2. Find the entry points and trace one real path end to end: a request, a command, or a build.
3. Read a few representative files to find the conventions in use: naming, structure, test layout. Do not guess.
4. Write a short map: what the project is, the stack, where the important pieces live, how to run and test it, and which files everything depends on.
5. Flag risky areas (central, fragile, or untested code) so the first change avoids them.
6. End with where you would start on the task at hand.

Read a few files in depth rather than skimming all of them.
