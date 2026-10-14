# Claude Cowork Pack

A starter kit for working with Claude as a co-worker: templates for Claude (chat and Cowork) and a ready-made `.claude/` folder for Claude Code. Updated October 2026.

From Krohn AI, mikekrohn.ai. Free to use and adapt.

## 1. What changed in 2026

On 16 September 2026 Anthropic announced that Claude Cowork and chat are merging into one Claude [1]. The rollout starts with Pro and Max plans on web, desktop and mobile. Team and Free plans follow later, and Enterprise admins get at least 30 days' notice before anything changes for their organisation [1][2].

What this means in practice, per Anthropic's Help Center [2]:

- There is no mode to pick. You ask in one conversation, and Claude decides whether a quick answer or a longer task fits.
- If your message box still shows separate "Chat" and "Cowork" options, your account does not have the new experience yet.
- Once your account moves over, you cannot switch back to separate options.
- Existing Cowork tasks, projects, connectors, skills, artifacts and files carry over. The model picker and the "Code" tab stay where they were.
- Cowork's global instructions move into Settings > General > Instructions for Claude.
- The web search toggle is gone. Claude searches when it helps. Research is under `/deep-research` or the "+" button.

New with the merge and in beta on paid plans: Claude Docs, Claude Slides, and Claude Design inside the conversation [1]. Enterprise admins decide when to turn them on.

## 2. Chat vs Cowork: what's the difference

| | Chat (before the merge) | Cowork (before the merge) | One Claude (after the merge) |
|---|---|---|---|
| Built for | Questions, drafting, thinking out loud | Handing over a whole task that takes many steps | Both, in the same conversation |
| How you start | Type a message | Pick Cowork in the mode picker, often choose a folder | Type a message; no mode |
| Output | Answers and artifacts in the chat | Finished files saved to a folder or project | Answers or finished files, depending on the ask |
| Runs while you are away | No | Yes, longer tasks and scheduled tasks | Yes, in the cloud; local file tasks need Claude Desktop open |
| Local files and computer | No | Yes, a folder you grant, in Claude Desktop | Same, in Claude Desktop |

Sources: [1][2][3].

Anthropic's reason for merging, from the announcement: people used both products, found it frustrating to decide where a task belonged, and work started in one did not carry into the other [1].

**When to use which.** If you have the merged experience, you do not choose. Write the request and Claude scales the work to it. What you still choose:

- **Desktop or web/phone.** Use Claude Desktop when the task needs files on your computer, the built-in browser, or computer use. A task started on web or phone can reach your connected apps but not your local folders [2][3].
- **Manual or Auto.** Manual is the default: Claude asks before each action. Auto lets Claude keep working, with automated safety checks before actions [2]. Start on Manual. Use Auto only for tasks and tools you trust.
- **Claude Code.** For software work inside a repository, use Claude Code. The `.claude/` folder in this pack is for that.

If you do not have the merge yet: use Chat for quick questions and drafts, and Cowork for anything that should end as a file, takes several steps, or should run on a schedule [2].

## 3. What Claude can do on a longer task

All of these are from Anthropic's Help Center as of October 2026 [2]. Check your plan; some are in beta.

- Work through a task on its own: search the web, read your files, run code, combine the results. Several tasks can run at once.
- Keep running in the cloud after you close your laptop. Tasks that use local files or apps need Claude Desktop open.
- Return finished files: documents, spreadsheets with working formulas, and presentations that open in PowerPoint.
- Use connected apps such as Google Drive, Gmail, Microsoft 365 and Slack while it works. Connect them under Customize > Connectors.
- In Claude Desktop: read and write a folder you grant, browse the web with the built-in browser or Claude in Chrome, and (beta, Pro and Max) use apps on your screen.
- Run scheduled tasks, for example an inbox summary every Monday at 8 [2][4].
- Show progress on Claude Mobile, where you can answer questions and redirect the task.
- Follow skills (saved instructions for a task) and plugins (bundles of skills and connectors).

By default Claude asks before permanently deleting files [2].

Current limitations listed by Anthropic [2]: "Add from GitHub" is not supported, conversations cannot be branched from an earlier point, incognito chats open in the previous experience, search does not cover older Cowork tasks, and Dispatch is not available to new users.

## 4. Set it up in 20 minutes

1. **Instructions for Claude.** Paste `cowork/instructions-for-claude.md` into Settings > General, then edit it to fit you.
2. **Connectors.** Connect the two or three apps your work lives in. Check each connector's description: some can only read and search.
3. **A working folder** (Claude Desktop). Make one folder per piece of recurring work with `inputs/`, `output/` and `scratch/`, and paste `cowork/folder-instructions.md` into its folder instructions.
4. **First task.** Use `cowork/task-brief.md`. Name the outcome, the format and the inputs, as the Help Center recommends [2].
5. **One scheduled task.** Pick a weekly report you write by hand and set it up with `cowork/scheduled-task.md`. Keep it on Manual for the first runs.

## 5. Skills: one file, two places

The eight skills in `.claude/skills/` follow the Agent Skills format: a folder with a `SKILL.md` that has a `name` and a `description` [5].

- **Claude Code** loads them from `.claude/skills/` in your project. Type `/draft-pr`, `/changelog` and so on, or let Claude pick one when the description matches.
- **Claude (chat and Cowork)** does not read skills from your disk. Upload a skill to your claude.ai account to use it there. Uploads accept only the spec fields `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`, so this pack's skills use only `name` and `description` [5].

Custom commands are now part of skills in Claude Code. The old `.claude/commands/changelog.md` from the first version of this pack is now `.claude/skills/changelog/SKILL.md`. Old command files keep working [5].

| Skill | Use it when |
|---|---|
| `weekly-report` | The Monday report from the sales sheet in Drive |
| `morning-digest` | A weekday summary of your team's Slack channels |
| `compare-tools` | Picking a tool or supplier, with sources |
| `draft-pr` | A tested change is ready for review |
| `explain-codebase` | You start on a repo you do not know |
| `research-note` | You need a sourced answer, not a guess |
| `verify-change` | Before you call a change done |
| `changelog` | You prepare a release or a progress update |

## 6. Claude Code quick start

1. Install Claude Code: see code.claude.com/docs.
2. Copy the pack into your project root: `cp -r CLAUDE.md .claude .mcp.json.example /path/to/project/`
3. Make the hook executable: `chmod +x .claude/hooks/session-start.sh`
4. Fill in `CLAUDE.md`. This pays back fastest.
5. Rename `.mcp.json.example` to `.mcp.json` only if you use MCP servers, and keep keys out of git.
6. Run `claude` in the project. The hook prints a short status, and the skills appear under `/`.

`.claude/settings.json` allows read-only git commands and the npm test, lint and build scripts, and denies `git push --force`, `git reset --hard` and `rm -rf`. Tighten the list to the commands you trust.

## 7. Safety habits

- Start every new kind of task on Manual.
- Give Claude the smallest folder that does the job. Keep originals in an `inputs/` folder Claude does not edit.
- For work with real consequences, such as sending messages or changing important files, stay close and review each step, as Anthropic advises [2].
- Longer tasks use more of your plan's usage than quick questions. Check Settings > Usage [2].

## 8. Files in this pack

| File | Where it goes |
|---|---|
| `cowork/instructions-for-claude.md` | Settings > General > Instructions for Claude |
| `cowork/folder-instructions.md` | Folder instructions in Claude Desktop (Customize panel) |
| `cowork/task-brief.md` | Your first message for a new task |
| `cowork/scheduled-task.md` | Scheduled > New task > Set up manually |
| `CLAUDE.md`, `.claude/`, `.mcp.json.example` | The root of a code project, for Claude Code |
| `.claude/skills/*` | Three office skills and five developer skills. Claude Code loads them as-is; upload a folder to claude.ai to use it in Claude |

Get the latest version at github.com/Walliiee/claude-cowork-pack. Licence: MIT.

## Sources

Checked on 14 October 2026. Anthropic's pages often carry no publish date; where they do not, that is stated.

1. Anthropic, "Claude Cowork and chat are now one Claude", claude.com/blog/cowork-is-now-claude. Published 16 September 2026 (date from the @claudeai announcement post; the page itself shows no date).
2. Claude Help Center, "Claude Cowork and chat are one Claude", support.claude.com/en/articles/16761823. Page marked "Updated over a month ago" on 14 October 2026.
3. Claude Help Center and Claude Academy material on Cowork setup and folder access (support.claude.com, academy.claude.com/courses/introduction-to-claude-cowork). No date shown.
4. Claude Help Center, "Schedule recurring tasks in Claude Cowork", support.claude.com/en/articles/13854387. No date shown.
5. Claude Code docs, "Extend Claude with skills", code.claude.com/docs/en/skills. No date shown.
