import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
pages = [
("cover", """<div class='kicker'>Krohn AI · October 2026</div>
<h1>Claude Cowork Pack</h1>
<p class='promise'>Set up Claude to finish whole tasks for you, now that chat and Cowork are one app.</p>
<div class='brand'>Krohn AI<br><span>mikekrohn.ai</span></div>"""),
("", """<h2>What changed</h2>
<p>On 16 September 2026 Anthropic announced that Claude Cowork and chat are merging into one Claude.</p>
<ul><li>No mode to pick. Claude decides if a quick answer or a longer task fits.</li>
<li>Pro and Max first. Team and Free later. Enterprise gets 30 days' notice.</li>
<li>Once your account moves over, you can't switch back.</li>
<li>Cowork tasks, projects, connectors, skills and files carry over.</li></ul>"""),
("", """<h2>Chat vs Cowork</h2>
<table><tr><th></th><th>Chat</th><th>Cowork</th></tr>
<tr><td>For</td><td>Questions, drafts</td><td>Whole tasks, many steps</td></tr>
<tr><td>Output</td><td>Answers in the chat</td><td>Finished files</td></tr>
<tr><td>Runs while you're away</td><td>No</td><td>Yes</td></tr>
<tr><td>Local files</td><td>No</td><td>Yes, in Claude Desktop</td></tr></table>
<p>After the merge: both, in one conversation.</p>"""),
("", """<h2>When to use what</h2>
<ul><li><b>Desktop</b> when the task needs files on your computer or the browser. Web and phone reach your connected apps only.</li>
<li><b>Manual</b> (default): Claude asks before each action. Use <b>Auto</b> only for tasks you trust.</li>
<li><b>Claude Code</b> for software work in a repository.</li></ul>"""),
("", """<h2>What Claude can do on a longer task</h2>
<ul><li>Search the web, read your files, run code</li>
<li>Keep running in the cloud after you close the laptop</li>
<li>Return Word, Excel and PowerPoint files</li>
<li>Use Drive, Gmail, Microsoft 365, Slack</li>
<li>Run on a schedule, e.g. every Monday at 8</li></ul>"""),
("", """<h2>Set it up in 20 minutes</h2>
<ol><li>Write your Instructions for Claude (Settings &gt; General)</li>
<li>Connect the 2 or 3 apps your work lives in</li>
<li>One folder per recurring job: inputs, output, scratch</li>
<li>Brief the first task: outcome, format, inputs</li>
<li>Schedule one weekly report, on Manual</li></ol>"""),
("", """<h2>A brief that works</h2>
<div class='code'>Outcome: a comparison of five project tools<br>
Format: a spreadsheet + half-page summary<br>
Inputs: web research, ./inputs/process.md<br>
Limits: no trial sign-ups<br>
Done when: every row has a source link</div>
<p>The pack has templates for this, for instructions, folders and scheduled tasks.</p>"""),
("", """<h2>Safety habits</h2>
<ul><li>Start every new kind of task on Manual</li>
<li>Give Claude the smallest folder that does the job</li>
<li>Keep originals where Claude doesn't edit</li>
<li>Review each step when it sends messages or changes important files</li></ul>
<p class='src'>Sources: claude.com/blog/cowork-is-now-claude (16 Sep 2026); support.claude.com/en/articles/16761823. Checked 14 Oct 2026.</p>"""),
("cover", """<h2 class='light'>Get the full pack</h2>
<p class='promise'>Templates, five skills and a ready Claude Code setup. Free, MIT licence.</p>
<p class='url'>github.com/Walliiee/claude-cowork-pack</p>
<div class='brand'>Krohn AI<br><span>mikekrohn.ai</span></div>"""),
]
css = """
@page { size: 1080px 1350px; margin: 0; }
body { margin:0; font-family: Inter, sans-serif; }
.p { width:1080px; height:1350px; box-sizing:border-box; padding:110px 100px; background:#F7E7D0; color:#5A4353; font-size:38px; line-height:1.45; page-break-after:always; position:relative; overflow:hidden; }
.p.cover { background:#451D3E; color:#F7E7D0; }
.p:not(.cover)::before { content:''; position:absolute; top:0; left:0; right:0; height:22px; background:#F89404; }
.num { position:absolute; bottom:60px; right:100px; font-size:26px; color:#66525F; }
.foot { position:absolute; bottom:60px; left:100px; font-size:26px; color:#66525F; }
h1 { font-family:Fraunces, serif; font-size:120px; line-height:1.02; color:#F7E7D0; margin:40px 0; letter-spacing:-0.02em; }
h2 { font-family:Fraunces, serif; font-size:72px; line-height:1.1; color:#451D3E; margin:0 0 50px; letter-spacing:-0.01em; }
h2.light { color:#F7E7D0; }
.kicker { color:#F89404; font-size:32px; font-weight:600; margin-top:120px; }
.promise { font-size:48px; line-height:1.35; }
.brand { position:absolute; bottom:110px; left:100px; font-family:Fraunces, serif; font-size:52px; font-weight:700; color:#F89404; }
.brand span { font-family:Inter, sans-serif; font-size:34px; color:#F7E7D0; font-weight:400; }
.url { font-family:'DM Mono', monospace; font-size:33px; white-space:nowrap; background:#F89404; color:#451D3E; padding:24px 30px; border-radius:24px; display:inline-block; margin-top:30px; }
li { margin:0 0 28px; } b { color:#451D3E; }
table { border-collapse:collapse; width:100%; font-size:34px; margin-bottom:40px; }
th { background:#451D3E; color:#F7E7D0; text-align:left; padding:18px; }
td { padding:18px; border-bottom:2px solid #E4CCA9; vertical-align:top; }
tr:nth-child(odd) td { background:#F0DCBE; }
.code { font-family:'DM Mono', monospace; font-size:32px; background:#F0DCBE; color:#451D3E; padding:36px; border-radius:24px; margin-bottom:40px; line-height:1.6; }
.src { font-size:26px; color:#66525F; margin-top:60px; }
"""
html = "".join(f"<div class='p {c}'>{b}" + ("" if c else f"<div class='foot'>Krohn AI · mikekrohn.ai</div><div class='num'>{i+1}/{len(pages)}</div>") + "</div>" for i,(c,b) in enumerate(pages))
(root/'build').mkdir(exist_ok=True)
(root/'build'/'linkedin.html').write_text(f"<html><head><meta charset='utf-8'><title>Claude Cowork Pack | Krohn AI</title><style>{css}</style></head><body>{html}</body></html>")
