#!/usr/bin/env python3
"""Render the day's front page (page.html) and screenshot it to entry.png.

Pipeline: news.json -> page.html -> headless Chromium -> entry.png.
The grader never runs this file; main.py ships the finished image.
Run locally with:  python3 render.py
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHROME = "/home/hatch/.cache/puppeteer/chrome-headless-shell/linux-157.0.8103.78/chrome-headless-shell-linux64/chrome-headless-shell"
W = H = 1024

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1024px; height:1024px; overflow:hidden; background:#f6f1e5;
  font-family:'Liberation Sans',sans-serif; color:#141310; }
.page { padding:18px 34px 10px 34px; height:1024px; display:flex; flex-direction:column; }
.rule-top { border-top:5px solid #141310; border-bottom:1.5px solid #141310; height:9px; }
.masthead { text-align:center; padding-top:7px; }
.masthead h1 { font-family:'Liberation Serif',serif; font-size:50px; letter-spacing:6px; font-weight:700; }
.tagline { font-size:17px; letter-spacing:3.5px; text-transform:uppercase; color:#5a5344; margin-top:2px; }
.dateband { margin-top:9px; background:#a4161a; color:#fff; display:flex;
  justify-content:space-between; align-items:center; padding:9px 18px; }
.dateband .date { font-size:27px; font-weight:700; letter-spacing:2px; }
.dateband .side { font-size:16px; letter-spacing:2px; text-transform:uppercase; }
.lead { border-bottom:3px solid #141310; padding:12px 2px 11px 2px; }
.chip { display:inline-block; background:#141310; color:#f6f1e5; font-size:15px; font-weight:700;
  letter-spacing:2px; padding:4px 10px; text-transform:uppercase; }
.chip.red { background:#a4161a; }
.lead h2 { font-family:'Liberation Serif',serif; font-size:36px; line-height:1.1; margin-top:7px; }
.lead p { font-size:19.5px; line-height:1.32; margin-top:6px; color:#26241d; }
.lead .place { color:#a4161a; font-weight:700; }
.grid { display:grid; grid-template-columns:1fr 1fr; column-gap:26px; flex:1; }
.card { border-bottom:1.5px solid #b9b09a; padding:8px 0 7px 0; }
.card h3 { font-family:'Liberation Serif',serif; font-size:23.5px; line-height:1.12; margin-top:6px; }
.card p { font-size:17px; line-height:1.28; margin-top:4px; color:#2b2921; }
.briefs { background:#141310; color:#f6f1e5; margin-top:11px; padding:11px 18px 9px 18px; }
.briefs h4 { font-size:16px; letter-spacing:3px; color:#e8b64c; margin-bottom:8px; }
.briefs .bgrid { display:grid; grid-template-columns:1fr 1fr; column-gap:26px; row-gap:5px; }
.brief { font-size:14.5px; line-height:1.24; }
.brief b { color:#e8b64c; letter-spacing:1px; font-size:14.5px; }
.src { margin-top:8px; font-size:12.5px; color:#a49a83; letter-spacing:0.5px; }
.footer { margin-top:8px; border-top:1.5px solid #141310; padding-top:7px;
  font-size:14.5px; color:#5a5344; display:flex; justify-content:space-between; }
"""


def build_html(news: dict) -> str:
    lead = news["lead"]
    cards = "".join(
        f'<div class="card"><span class="chip">{c["tag"]}</span>'
        f'<h3>{c["headline"]}</h3><p>{c["body"]}</p></div>'
        for c in news["cards"]
    )
    briefs = "".join(
        f'<div class="brief"><b>{b["tag"]} —</b> {b["text"]}</div>' for b in news["briefs"]
    )
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">
  <div class="rule-top"></div>
  <div class="masthead"><h1>{news['masthead']}</h1>
    <div class="tagline">{news['tagline']}</div></div>
  <div class="dateband"><div class="date">{news['date_line']}</div>
    <div class="side">One day · One picture</div></div>
  <div class="lead"><span class="chip red">{lead['tag']}</span>
    <h2>{lead['headline']}</h2>
    <p><span class="place">{lead['place']} —</span> {lead['body']}</p></div>
  <div class="grid">{cards}</div>
  <div class="briefs"><h4>ALSO TODAY</h4><div class="bgrid">{briefs}</div><div class="src">{news['footer']} · 25 · 11 · 2026</div></div>
  
</div></body></html>"""


def main() -> None:
    news = json.loads((HERE / "news.json").read_text(encoding="utf-8"))
    html_path = HERE / "page.html"
    html_path.write_text(build_html(news), encoding="utf-8")
    out = HERE / "entry.png"
    subprocess.run(
        [
            CHROME, "--headless", "--disable-gpu", "--no-sandbox",
            f"--window-size={W},{H}", "--hide-scrollbars",
            f"--screenshot={out}", html_path.as_uri(),
        ],
        check=True,
    )
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    sys.exit(main())
