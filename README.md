# Claude Cowork Pack

Templates and a ready `.claude/` setup for working with Claude as a co-worker, updated for the October 2026 merge of Claude chat and Cowork.

**Guide (PDF):** [claude-cowork-pack.pdf](./claude-cowork-pack.pdf) · LinkedIn carousel: [claude-cowork-pack-linkedin.pdf](./claude-cowork-pack-linkedin.pdf) · source text in [GUIDE.md](./GUIDE.md)

## What's inside

| Path | What it is |
|---|---|
| `GUIDE.md`, `claude-cowork-pack.pdf`, `claude-cowork-pack-linkedin.pdf` | The guide: what changed with the merge, Chat vs Cowork, setup, safety habits, with sources |
| `cowork/instructions-for-claude.md` | Template for Settings > General > Instructions for Claude |
| `cowork/folder-instructions.md` | Template for per-folder instructions in Claude Desktop |
| `cowork/task-brief.md` | A brief for handing Claude a whole task |
| `cowork/scheduled-task.md` | Fields for a recurring task |
| `CLAUDE.md` | Project orientation template for Claude Code |
| `.claude/settings.json` | Default permissions (safe commands allowed, destructive ones denied) and a SessionStart hook |
| `.claude/hooks/session-start.sh` | Prints a short status when a Claude Code session starts |
| `.claude/skills/` | Five skills: `draft-pr`, `explain-codebase`, `research-note`, `verify-change`, `changelog` |
| `.mcp.json.example` | Template for MCP servers in Claude Code |

## How to use it

**Claude (chat and Cowork):** paste `cowork/instructions-for-claude.md` into Settings > General, connect your main apps, and brief your first task with `cowork/task-brief.md`. To use a skill there, upload its folder to your claude.ai account.

**Claude Code:**

```bash
cp -r CLAUDE.md .claude .mcp.json.example /path/to/your/project/
chmod +x /path/to/your/project/.claude/hooks/session-start.sh
```

Fill in `CLAUDE.md`, then run `claude` in the project. The skills appear under `/`.

Everything here is a starting point. Cut what you do not use.

## Status

Feature claims are checked against Anthropic's own pages on 14 October 2026 and listed in the guide's Sources section. The merge is rolling out in stages, so your account may still show separate Chat and Cowork options.

## License

MIT. See [LICENSE](./LICENSE). Copy, adapt and reuse the templates freely; keep the copyright notice.

---

Made by [Krohn AI](https://mikekrohn.ai), Copenhagen. Company AI setups for small, owner-led businesses.
