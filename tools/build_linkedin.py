"""Build the LinkedIn carousel (1080x1350, 4:5) from linkedin-outline.md content.
Images: visuals/cover.png, uc3.png ... uc7.png are used when present; otherwise a marked placeholder is drawn.
Usage: python3 tools/build_linkedin.py   (writes build/linkedin.html and claude-cowork-pack-linkedin.pdf)
"""
import pathlib, subprocess, html as H
root = pathlib.Path(__file__).resolve().parent.parent
vis = root / 'visuals'

def slot(name, size, cls):
    f = vis / name
    if f.exists():
        return f"<div class='slot {cls}'><img src='{f.as_uri()}'></div>"
    return f"<div class='slot {cls} ph'><div>IMAGE SLOT<br><b>visuals/{name}</b><br>supply {size}<br>shown {"900x500 card" if cls=="hero" else ("900x400 crop" if cls=="panel" else "220x220")}</div></div>"

def foot(n):
    return f"<div class='foot'>Krohn AI · mikekrohn.ai</div><div class='num'>{n}/10</div>"

def usecase(n, title, img, size, inp, does, get, prompt, beta=False):
    tag = "<span class='beta'>beta</span>" if beta else ""
    return f"""<div class='p uc'>{slot(img, size, 'panel')}
<h2>{H.escape(title)}{tag}</h2>
<div class='flow'>
<div class='box'><div class='lbl'>Input</div>{H.escape(inp)}</div><div class='arr'>›</div>
<div class='box'><div class='lbl'>Claude</div>{H.escape(does)}</div><div class='arr'>›</div>
<div class='box hl'><div class='lbl'>You get</div>{H.escape(get)}</div></div>
<div class='prompt'>“{H.escape(prompt)}”</div>{foot(n)}</div>"""

pages = []
pages.append(f"""<div class='p cover'>{slot('cover.png', '1080x1350 hero', 'hero')}<div class='shade'></div>
<h1>Hand Claude the task. Get the file back.</h1>
<div class='brand'>Krohn AI<br><span>mikekrohn.ai</span></div></div>""")
pages.append(f"""<div class='p'><h2>Chat vs Cowork in one line</h2>
<div class='band b1'><span class='ic'>💬</span>Chat: you ask, it answers.</div>
<div class='band b2'><span class='ic'>📁</span>Cowork: you hand over a task, you get files back.</div>
<div class='band b3'><span class='ic'>💬+📁</span>Now: one Claude does both.</div>{foot(2)}</div>""")
pages.append(usecase(3, "The weekly report you stop writing", "uc3.png", "4:5 panel", "Sales sheet in Drive", "Flags what slipped, drafts slides", "Report and deck, every Monday", "Summarise last week's pipeline. Five slides.", beta=True))
pages.append(usecase(4, "Your morning digest, before you sit down", "uc4.png", "4:5 panel", "Team Slack channels", "Reads new messages each weekday", "One short summary", "Weekdays at 8 AM: summarise new Slack messages."))
pages.append(usecase(5, "Compare tools, with sources attached", "uc5.png", "4:5 panel", "Your requirements", "Searches the web, compares options", "Spreadsheet plus one-page summary", "Compare five project tools. Source links."))
pages.append(usecase(6, "Clean up the shared folder", "uc6.png", "4:5 panel", "One folder on your computer", "Sorts files by type and date", "A tidy folder", "Sort this folder by type and date."))
pages.append(usecase(7, "From notes to a deck you can present", "uc7.png", "1080x1350 hero", "Interview notes", "Pulls themes and quotes", "A doc and a 10-slide deck", "Top themes, one quote each, 10 slides.", beta=True))
items = [("👤","Write your instructions for Claude"),("🔌","Connect two or three apps"),("📁","Make one working folder"),("💬","Brief one real task"),("📅","Schedule one weekly report")]
pages.append("<div class='p'><h2>Set it up in 20 minutes</h2>" + "".join(f"<div class='chk'><span class='dot'>{i}</span>{t}</div>" for i,t in items) + foot(8) + "</div>")
safe = ["Start on Manual: Claude asks first.","Give it the smallest folder.","Keep originals out of reach.","Review anything that sends or deletes."]
pages.append("<div class='p'><h2>Four safety habits</h2>" + "".join(f"<div class='safe'><span class='tick'>✓</span>{t}</div>" for t in safe) + foot(9) + "</div>")
pages.append(f"""<div class='p cover'><h2 class='light'>Get the free pack: templates, five skills, setup guide.</h2>
<div class='url'>github.com/Walliiee/claude-cowork-pack</div>
{slot('logo.png','square, optional','logo') if (vis/'logo.png').exists() else ''}
<div class='brand'>Krohn AI<br><span>mikekrohn.ai</span></div></div>""")

css = """
@page { size: 1080px 1350px; margin: 0; }
body { margin:0; font-family: Inter, sans-serif; }
.p { width:1080px; height:1350px; box-sizing:border-box; padding:100px 90px; background:#F7E7D0; color:#5A4353; font-size:40px; line-height:1.35; page-break-after:always; position:relative; overflow:hidden; }
.p:not(.cover)::before { content:''; position:absolute; top:0; left:0; right:0; height:22px; background:#F89404; z-index:2; }
.p.cover { background:#451D3E; color:#F7E7D0; }
h1 { position:relative; z-index:2; font-family:Fraunces, serif; font-size:112px; line-height:1.02; color:#F7E7D0; margin:80px 0 0; letter-spacing:-0.02em; }
h2 { font-family:Fraunces, serif; font-size:68px; line-height:1.08; color:#451D3E; margin:0 0 40px; letter-spacing:-0.01em; }
h2.light { color:#F7E7D0; font-size:76px; margin-top:120px; }
.slot.ph { border:6px dashed #F89404; background:repeating-linear-gradient(45deg,#F0DCBE,#F0DCBE 20px,#E4CCA9 20px,#E4CCA9 40px); display:flex; align-items:center; justify-content:center; text-align:center; color:#451D3E; font-size:30px; font-family:'DM Mono',monospace; box-sizing:border-box; }
.slot.ph div { background:#F7E7D0; padding:14px 22px; border-radius:12px; }
.slot img { width:100%; height:100%; object-fit:cover; object-position:center; display:block; }
.slot.hero { position:absolute; left:90px; right:90px; bottom:250px; height:500px; border-radius:30px; overflow:hidden; }
.shade { position:absolute; left:0; right:0; bottom:300px; height:600px; display:none; }
.cover .slot.ph div { position:relative; z-index:3; }
.brand { position:absolute; bottom:90px; left:90px; font-family:Fraunces, serif; font-size:54px; font-weight:700; color:#F89404; z-index:3; }
.brand span { font-family:Inter, sans-serif; font-size:34px; color:#F7E7D0; font-weight:400; }
.slot.panel { height:400px; border-radius:30px; overflow:hidden; margin:10px 0 44px; }
.beta { font-family:Inter, sans-serif; font-size:24px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; background:#F89404; color:#451D3E; border-radius:999px; padding:6px 16px; margin-left:18px; vertical-align:middle; }
.flow { display:flex; align-items:stretch; gap:10px; margin-bottom:40px; }
.box { flex:1; background:#F0DCBE; border-radius:24px; padding:24px 22px; font-size:32px; line-height:1.25; color:#451D3E; }
.box.hl { background:#451D3E; color:#F7E7D0; }
.lbl { font-size:22px; font-weight:700; text-transform:uppercase; letter-spacing:0.08em; color:#6F3C70; margin-bottom:10px; }
.hl .lbl { color:#F89404; }
.arr { align-self:center; font-size:56px; color:#F89404; font-weight:700; }
.prompt { font-family:'DM Mono',monospace; font-size:32px; color:#451D3E; border-left:8px solid #F89404; padding:8px 0 8px 26px; }
.band { display:flex; align-items:center; gap:30px; border-radius:30px; padding:46px 40px; margin-bottom:30px; font-size:46px; line-height:1.2; color:#451D3E; font-weight:500; }
.b1 { background:#FFF6EA; } .b2 { background:#F0DCBE; } .b3 { background:#F89404; font-weight:700; }
.ic { font-size:56px; min-width:150px; text-align:center; }
.chk, .safe { display:flex; align-items:center; gap:34px; font-size:44px; color:#451D3E; margin-bottom:46px; }
.dot { width:96px; height:96px; border-radius:50%; background:#F89404; display:flex; align-items:center; justify-content:center; font-size:46px; flex-shrink:0; }
.tick { width:70px; height:70px; border-radius:50%; background:#451D3E; color:#F89404; display:flex; align-items:center; justify-content:center; font-size:40px; flex-shrink:0; }
.safe { font-size:50px; margin-bottom:60px; }
.url { font-family:'DM Mono', monospace; font-size:36px; white-space:nowrap; background:#F89404; color:#451D3E; padding:26px 32px; border-radius:24px; display:inline-block; margin-top:20px; }
.slot.logo { position:absolute; right:90px; bottom:90px; width:220px; height:220px; border-radius:24px; overflow:hidden; font-size:22px; }
.foot { position:absolute; bottom:56px; left:90px; font-size:26px; color:#66525F; }
.num { position:absolute; bottom:56px; right:90px; font-size:26px; color:#66525F; }
"""
(root/'build').mkdir(exist_ok=True)
out = root/'build'/'linkedin.html'
out.write_text(f"<html><head><meta charset='utf-8'><title>Claude Cowork: 5 simple use cases for everyday work</title><style>{css}</style></head><body>{''.join(pages)}</body></html>")
pdf = root/'claude-cowork-pack-linkedin.pdf'
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--allow-file-access-from-files',f'--print-to-pdf={pdf}',out.as_uri()],check=True,stderr=subprocess.DEVNULL)
shots = root/'screenshots'
for f in shots.glob('linkedin-page-*.png'): f.unlink()
subprocess.run(['pdftoppm','-png','-r','40',str(pdf),str(shots/'li')],check=True,stderr=subprocess.DEVNULL)
for f in shots.glob('li-*.png'):
    f.rename(shots/f"linkedin-page-{int(f.stem.split('-')[1])}.png")
print(pdf)
