"""Build the guide PDF from GUIDE.md. Usage: python3 build/tools/build_pdf.py"""
import markdown, pathlib, subprocess
root = pathlib.Path(__file__).resolve().parents[2]
build = root / 'build'
md = (root/'GUIDE.md').read_text()
body = markdown.markdown(md, extensions=['tables','fenced_code'])
i = body.rfind('<h2>Sources'); body = body[:i] + '<div class="sources">' + body[i:] + '</div>'
css = """
.sources { break-inside: avoid; }
@page { size: A4; margin: 18mm 18mm 20mm 18mm; background: #F7E7D0;
  @bottom-right { content: counter(page); } }
body { font-family: Inter, -apple-system, sans-serif; color: #5A4353; font-size: 10.5pt; line-height: 1.6; background:#F7E7D0; }
h1 { font-family: Fraunces, Georgia, serif; color:#451D3E; font-size: 30pt; font-weight:700; letter-spacing:-0.02em; margin:0 0 6pt; border-bottom: 6px solid #F89404; padding-bottom:8pt;}
h2 { font-family: Fraunces, Georgia, serif; color:#451D3E; font-size: 16pt; font-weight:700; margin: 20pt 0 6pt; break-after: avoid;}
strong { color:#451D3E; }
a { color:#6F3C70; }
code { font-family: 'DM Mono', ui-monospace, monospace; color:#451D3E; background:#F0DCBE; padding:0 3px; border-radius:3px; font-size:9.5pt;}
table { border-collapse: collapse; width:100%; font-size:9.3pt; margin:8pt 0; break-inside: avoid;}
th { background:#451D3E; color:#F7E7D0; text-align:left; padding:5pt 6pt; font-weight:600;}
td { border-bottom:1px solid #E4CCA9; padding:5pt 6pt; vertical-align:top;}
tr:nth-child(even) td { background:#F0DCBE; }
li { margin: 2pt 0; }
h2:last-of-type ~ ol { font-size: 9pt; color:#66525F; }
.footer { margin-top:24pt; padding:8pt 12pt; background:#F89404; color:#451D3E; border-radius:12px; font-weight:600;}
"""
(build/'out').mkdir(exist_ok=True)
html = f"<html><head><meta charset='utf-8'><title>Claude Cowork Pack | Krohn AI</title><style>{css}</style></head><body>{body}<div class='footer'>Krohn AI · mikekrohn.ai · Company AI setups for small, owner-led businesses.</div></body></html>"
out = build/'out'/'guide.html'
out.write_text(html)
pdf = root/'claude-cowork-pack.pdf'
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--no-pdf-header-footer',f'--print-to-pdf={pdf}',out.as_uri()],check=True,stderr=subprocess.DEVNULL)
shots = build/'screenshots'
for f in shots.glob('page-*.png'): f.unlink()
subprocess.run(['pdftoppm','-png','-r','70',str(pdf),str(shots/'pg')],check=True,stderr=subprocess.DEVNULL)
for f in shots.glob('pg-*.png'):
    f.rename(shots/f"page-{int(f.stem.split('-')[1])}.png")
print(pdf)
