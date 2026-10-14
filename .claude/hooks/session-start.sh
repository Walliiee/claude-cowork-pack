#!/usr/bin/env bash
# Runs at the start of every Claude Code session. Keep it fast and quiet.
# Customise the checks for your project.

echo "Claude session: $(basename "$PWD")"

# List the project's npm scripts so both you and Claude know what can run.
if [ -f package.json ]; then
  scripts=$(node -e "try{console.log(Object.keys(require('./package.json').scripts||{}).join(', '))}catch(e){console.log('')}" 2>/dev/null)
  [ -n "$scripts" ] && echo "  scripts: $scripts"
fi

echo "  reminder: run the tests and the linter before anything ships."
