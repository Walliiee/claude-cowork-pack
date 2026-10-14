# Claude Cowork Pack

Five everyday office tasks you can hand to Claude, with the templates and skills to set them up. Updated for the October 2026 merge of Claude chat and Cowork.

**Guide (PDF):** [claude-cowork-pack.pdf](./claude-cowork-pack.pdf) · **LinkedIn carousel:** [claude-cowork-pack-linkedin.pdf](./claude-cowork-pack-linkedin.pdf) · source text in [GUIDE.md](./GUIDE.md)

## 5 use cases for everyday work

| Use case | You give Claude | You get back | Start with |
|---|---|---|---|
| Weekly report | The sales sheet in Google Drive | A report and a five-slide deck, every Monday | `weekly-report` skill + a scheduled task |
| Morning digest | Your team's Slack channels | One short summary, weekdays at 8 AM | `morning-digest` skill + a scheduled task |
| Compare tools | Your requirements | A spreadsheet with source links and a one-page summary | `compare-tools` skill |
| Clean up a folder | One folder on your computer (Claude Desktop) | Files sorted by type and date | `cowork/task-brief.md` |
| Notes to a deck | Meeting or interview notes | A doc and a 10-slide deck | `cowork/task-brief.md` |

Claude Docs and Claude Slides are in beta on paid plans. Scheduled tasks that only use connected apps run in the cloud; tasks that use local files need Claude Desktop open. Sources are listed in the guide.

## What's in the repo

| Path | What it is |
|---|---|
| `claude-cowork-pack.pdf`, `GUIDE.md` | The guide: what changed with the merge, Chat vs Cowork, setup, safety, sources |
| `claude-cowork-pack-linkedin.pdf` | The 10-slide carousel version |
| `cowork/instructions-for-claude.md` | Template for Settings > General > Instructions for Claude |
| `cowork/folder-instructions.md` | Template for per-folder instructions in Claude Desktop |
| `cowork/task-brief.md` | A brief for handing Claude a whole task |
| `cowork/scheduled-task.md` | Fields for a recurring task |
| `.claude/skills/weekly-report/` | Office skill: sales sheet to report and deck |
| `.claude/skills/morning-digest/` | Office skill: Slack summary |
| `.claude/skills/compare-tools/` | Office skill: sourced comparison |
| `build/` | Build scripts, carousel outline, visuals and page screenshots |
| `LICENSE` | MIT |

## How to use it

1. Paste `cowork/instructions-for-claude.md` into Settings > General and edit it.
2. Connect the apps your work lives in (Drive, Slack, Gmail, Microsoft 365) under Customize > Connectors.
3. To use an office skill in Claude, upload its folder from `.claude/skills/` to your claude.ai account.
4. Brief your first task with `cowork/task-brief.md`. Start on Manual, where Claude asks before each action.

## For developers (Claude Code)

These files are for Claude Code inside a code repository.

| Path | What it is |
|---|---|
| `CLAUDE.md` | Project orientation template |
| `.claude/settings.json` | Default permissions (safe commands allowed, destructive ones denied) and a SessionStart hook |
| `.claude/hooks/session-start.sh` | Prints a short status when a session starts |
| `.claude/skills/draft-pr/` | Turn a verified change into a draft PR |
| `.claude/skills/explain-codebase/` | Map an unfamiliar repo before changing it |
| `.claude/skills/research-note/` | A dated note with a source for every claim |
| `.claude/skills/verify-change/` | Check a change by running it |
| `.claude/skills/changelog/` | Changelog entry since a tag or ref |
| `.mcp.json.example` | Template for MCP servers |

```bash
cp -r CLAUDE.md .claude .mcp.json.example /path/to/your/project/
chmod +x /path/to/your/project/.claude/hooks/session-start.sh
```

Fill in `CLAUDE.md`, then run `claude` in the project. The skills appear under `/`. Delete the office skills there if you do not need them.

## Rebuild the PDFs

Needs Python 3 with `markdown`, Google Chrome and poppler-utils.

```bash
python3 build/tools/build_pdf.py        # claude-cowork-pack.pdf + build/screenshots/page-N.png
python3 build/tools/build_linkedin.py   # claude-cowork-pack-linkedin.pdf + build/screenshots/linkedin-page-N.png
```

## Status

Feature claims were checked against Anthropic's own pages on 14 October 2026. The merge is rolling out in stages, so your account may still show separate Chat and Cowork options.

## License

MIT. See [LICENSE](./LICENSE).

---

Made by [Krohn AI](https://mikekrohn.ai), Copenhagen. Company AI setups for small, owner-led businesses.
