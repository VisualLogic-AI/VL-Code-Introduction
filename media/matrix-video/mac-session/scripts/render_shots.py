"""Render every shot of the storyboard to 1920x1080 PNGs with Playwright.

Usage: render_shots.py <lang zh|en> [only_scene_ids_csv]
Shots: designed slides, the DAG execution walkthrough (6 frames), real desktop captures
(with click marker) and real product screenshots framed with an operation caption.
Output: build/shots-<lang>/*.png and build/plan-<lang>.json.
"""
import base64
import importlib
import json
import os
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
LANG = sys.argv[1] if len(sys.argv) > 1 else "zh"
S = importlib.import_module(f"strings_{LANG}")
OUT = os.path.join(ROOT, "build", f"shots-{LANG}")
FONT = "'PingFang SC','Hiragino Sans GB','Helvetica Neue',sans-serif" if LANG == "zh" else "'Helvetica Neue','SF Pro Display','PingFang SC',sans-serif"

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;overflow:hidden;background:radial-gradient(1200px 700px at 78% -10%,#2a2f6b 0%,rgba(10,13,26,0) 60%),radial-gradient(900px 600px at -10% 110%,#173a4a 0%,rgba(10,13,26,0) 55%),#0a0d1a;
font-family:FONT;color:#e8ebff}
.brand{position:absolute;left:64px;top:44px;display:flex;align-items:center;gap:14px;font-size:26px;font-weight:600;letter-spacing:.5px}
.logo{width:44px;height:44px;border-radius:10px;background:#141a33;border:1px solid #3a4280;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:700;color:#9aa3ff}
.stitle{position:absolute;right:64px;top:50px;font-size:26px;color:#aab1e6;font-weight:500}
.frame{position:absolute;left:50%;top:118px;transform:translateX(-50%);border-radius:14px;overflow:hidden;background:#0f1324;border:1px solid #2c3366;box-shadow:0 30px 80px rgba(0,0,0,.55)}
.bar{height:36px;background:#151a33;display:flex;align-items:center;padding:0 16px;gap:8px;border-bottom:1px solid #262c58}
.dot{width:12px;height:12px;border-radius:50%}
.bar .u{margin-left:18px;font-size:15px;color:#7f87c2}
.frame img{display:block}
.cap{position:absolute;left:64px;bottom:150px;background:rgba(124,131,255,.16);border:1px solid rgba(154,163,255,.55);color:#f2f3ff;font-size:30px;font-weight:600;padding:14px 26px;border-radius:12px;backdrop-filter:blur(6px)}
.click{position:absolute;width:64px;height:64px;margin:-32px 0 0 -32px;border-radius:50%;border:4px solid #ffd166;box-shadow:0 0 0 10px rgba(255,209,102,.22),0 0 30px rgba(255,209,102,.6)}
.cursor{position:absolute;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-bottom:30px solid #fff;transform:rotate(-30deg);filter:drop-shadow(0 2px 4px rgba(0,0,0,.7))}
.center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
h1{font-size:120px;font-weight:700;letter-spacing:2px;background:linear-gradient(90deg,#c9ceff,#7c83ff 60%,#5ad1ff);-webkit-background-clip:text;color:transparent}
.sub{margin-top:28px;font-size:40px;color:#c7cbef;max-width:1500px;line-height:1.5}
.tag{margin-top:40px;font-size:26px;color:#8a91c9;letter-spacing:6px}
.cards{display:flex;gap:40px;margin-top:20px}
.card{width:480px;min-height:330px;background:rgba(20,26,51,.85);border:1px solid #2f3770;border-radius:18px;padding:36px;text-align:left}
.card h3{font-size:38px;margin-bottom:12px;color:#fff}
.card .k{font-size:22px;color:#7c83ff;letter-spacing:3px;margin-bottom:18px}
.card p{font-size:27px;line-height:1.6;color:#c7cbef}
.arrow{font-size:60px;color:#7c83ff;align-self:center}
.note{margin-top:46px;font-size:30px;color:#ffd166;background:rgba(255,209,102,.08);border:1px solid rgba(255,209,102,.4);padding:14px 30px;border-radius:12px}
.cols{display:flex;gap:70px;align-items:stretch;margin-top:10px}
.list{width:640px;background:rgba(20,26,51,.85);border:1px solid #2f3770;border-radius:18px;padding:40px;text-align:left}
.list h3{font-size:36px;margin-bottom:26px}
.list li{font-size:29px;line-height:1.9;color:#c7cbef;list-style:none}
.list li b{color:#fff}
.bad h3{color:#ff8a8a}.good h3{color:#7ef0b0}
.steps{display:flex;gap:36px;margin-top:50px}
.step{width:440px;background:rgba(20,26,51,.85);border:1px solid #2f3770;border-radius:18px;padding:34px;text-align:left}
.step .n{font-size:64px;font-weight:700;color:#7c83ff}
.step .t{font-size:36px;font-weight:600;margin-top:8px}
.step .d{font-size:24px;color:#aab1e6;margin-top:12px;line-height:1.5}
.dag{position:absolute;left:80px;top:150px;width:1760px;height:720px;background:rgba(14,18,38,.9);border:1px solid #2c3366;border-radius:18px;
 background-image:radial-gradient(rgba(124,131,255,.18) 1.2px,transparent 1.2px);background-size:28px 28px}
.node{position:absolute;width:220px;height:92px;margin:-46px 0 0 -110px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;
 font-size:27px;font-weight:600;border:2px solid #39407a;background:#151a36;color:#8d93c4}
.node small{font-size:17px;font-weight:500;margin-top:4px;opacity:.9}
.node.running{border-color:#5ab0ff;background:#10294a;color:#e6f2ff;box-shadow:0 0 0 6px rgba(90,176,255,.18),0 0 34px rgba(90,176,255,.55)}
.node.done{border-color:#3ed598;background:#0f2e25;color:#d9fff0}
.node.wait{border-color:#ffd166;background:#3a2f10;color:#fff3cf;box-shadow:0 0 0 6px rgba(255,209,102,.18),0 0 34px rgba(255,209,102,.5)}
.node.new{border-style:dashed}
.node.hidden{display:none}
.badge{position:absolute;top:-14px;right:-14px;width:34px;height:34px;border-radius:50%;font-size:20px;display:flex;align-items:center;justify-content:center;color:#0a0d1a;font-weight:800}
.done .badge{background:#3ed598}.running .badge{background:#5ab0ff}.wait .badge{background:#ffd166}
.reason{position:absolute;font-size:20px;color:#d8b4ff;background:rgba(160,110,255,.14);border:1px dashed #b48cff;padding:6px 14px;border-radius:8px;white-space:nowrap}
.dstep{position:absolute;left:80px;top:890px;font-size:38px;font-weight:700;color:#fff}
.hud{position:absolute;right:110px;top:176px;font-size:22px;color:#c7cbef;background:#151a36;border:1px solid #2f3770;padding:8px 18px;border-radius:999px}
.dlabel{position:absolute;left:110px;top:176px;font-size:20px;color:#8a91c9;letter-spacing:2px}
.legend{position:absolute;right:80px;top:900px;display:flex;gap:22px;font-size:21px;color:#aab1e6}
.legend span{display:flex;align-items:center;gap:8px}.legend i{width:18px;height:18px;border-radius:5px;display:inline-block;border:2px solid}
""".replace("FONT", FONT)


def img_uri(path):
    with open(path, "rb") as fh:
        return "data:image/png;base64," + base64.b64encode(fh.read()).decode()


def chrome(sid):
    t = S.SCENE_TITLES.get(sid, "")
    return '<div class="brand"><div class="logo">VL</div>Matrix</div>' + (f'<div class="stitle">{t}</div>' if t else "")


def framed(sid, png, caption, url, click=None, max_w=1640, max_h=820):
    w, h = Image.open(png).size
    s = min(max_w / w, (max_h - 36) / h)
    dw, dh = int(w * s), int(h * s)
    extra = ""
    if click:
        cx, cy = click[0] * s, click[1] * s + 36
        extra = (f'<div class="click" style="left:{cx:.0f}px;top:{cy:.0f}px"></div>'
                 f'<div class="cursor" style="left:{cx+6:.0f}px;top:{cy+4:.0f}px"></div>')
    return (chrome(sid) +
            f'<div class="frame" style="width:{dw}px;height:{dh+36}px"><div class="bar">'
            '<span class="dot" style="background:#ff5f57"></span><span class="dot" style="background:#febc2e"></span>'
            f'<span class="dot" style="background:#28c840"></span><span class="u">{url}</span></div>'
            f'<img src="{img_uri(png)}" style="width:{dw}px;height:{dh}px"></div>'
            f'<div style="position:absolute;left:{(1920-dw)//2}px;top:118px;width:{dw}px;height:{dh+36}px">{extra}</div>'
            f'<div class="cap">{caption}</div>')


# DAG walkthrough: node positions inside the .dag box (px), edges, and per-frame states
POS = {"goal": (150, 360), "plan": (420, 360), "fe": (720, 200), "be": (720, 520), "test": (1010, 360),
       "fix": (1010, 610), "review": (1300, 360), "deliver": (1590, 360)}
EDGES = [("goal", "plan"), ("plan", "fe"), ("plan", "be"), ("fe", "test"), ("be", "test"), ("test", "review"), ("review", "deliver")]
FIX_EDGES = [("test", "fix"), ("fix", "review")]
FRAMES = [
    {"goal": "done", "plan": "running"},
    {"goal": "done", "plan": "done", "fe": "running", "be": "running"},
    {"goal": "done", "plan": "done", "fe": "done", "be": "done", "test": "running"},
    {"goal": "done", "plan": "done", "fe": "done", "be": "done", "test": "done", "fix": "running"},
    {"goal": "done", "plan": "done", "fe": "done", "be": "done", "test": "done", "fix": "done", "review": "wait"},
    {k: "done" for k in POS},
]
COL = {"pending": "#39407a", "running": "#5ab0ff", "done": "#3ed598", "wait": "#ffd166", "new": "#b48cff"}


def dag_frame(i):
    st = FRAMES[i]
    show_fix = i >= 3
    svg = ['<svg width="1760" height="720" style="position:absolute;left:0;top:0"><defs>']
    for k, c in COL.items():
        svg.append(f'<marker id="a{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    svg.append("</defs>")
    for a, b in EDGES + (FIX_EDGES if show_fix else []):
        (x1, y1), (x2, y2) = POS[a], POS[b]
        x1 += 110
        x2 -= 112
        sa, sb = st.get(a, "pending"), st.get(b, "pending")
        key = "done" if sa == "done" and sb != "pending" else ("running" if sa == "done" else "pending")
        if (a, b) in FIX_EDGES:
            key = "new" if key == "pending" else key
            if a == "test":
                x1, y1, x2, y2 = POS[a][0], POS[a][1] + 46, POS[b][0], POS[b][1] - 48
            else:
                x1, y1 = POS[a][0] + 110, POS[a][1]
        dash = ' stroke-dasharray="10 8"' if (a, b) in FIX_EDGES else ""
        mx = (x1 + x2) / 2
        path = f"M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}" if y1 != y2 and (a, b) not in FIX_EDGES[:1] else f"M{x1},{y1} L{x2},{y2}"
        svg.append(f'<path d="{path}" stroke="{COL[key]}" stroke-width="4" fill="none"{dash} marker-end="url(#a{key})"/>')
    svg.append("</svg>")
    nodes = []
    for k, (x, y) in POS.items():
        if k == "fix" and not show_fix:
            continue
        s = st.get(k, "pending")
        cls = f"node {s}" + (" new" if k == "fix" else "")
        badge = {"done": "✓", "running": "▶", "wait": "!"}.get(s, "")
        sub = S.DAG["legend"][s] if s != "pending" else S.DAG["legend"]["pending"]
        nodes.append(f'<div class="{cls}" style="left:{x}px;top:{y}px">{S.DAG["nodes"][k]}<small>{sub}</small>'
                     + (f'<span class="badge">{badge}</span>' if badge else "") + "</div>")
    reason = ""
    if show_fix:
        fx, fy = POS["fix"]
        reason = f'<div class="reason" style="left:{fx+130}px;top:{fy-20}px">{S.DAG["reason"]}</div>'
    legend = "".join(f'<span><i style="border-color:{COL[k]};background:{COL[k]}33"></i>{S.DAG["legend"][k]}</span>'
                     for k in ["pending", "running", "done", "wait", "new"])
    return (chrome("s08c") + f'<div class="dag">{"".join(svg)}{"".join(nodes)}{reason}</div>'
            f'<div class="dlabel">{S.DAG["label"]}</div><div class="hud">{S.DAG["hud"][i]}</div>'
            f'<div class="dstep">{S.DAG["steps"][i]}</div><div class="legend">{legend}</div>')


def main():
    os.makedirs(OUT, exist_ok=True)
    pages = dict(S.slides(chrome))
    cap = json.load(open(os.path.join(ROOT, "build", "desktop", "capture.json")))
    for i, p in enumerate(cap["pages"], 1):
        pages[("s04", i)] = framed("s04", os.path.join(ROOT, p["file"]), S.DESKTOP_CAPTIONS[i - 1], S.DESKTOP_URL, click=p["click_px"])
    for sid, shots in S.WEB.items():
        for i, (name, caption) in enumerate(shots, 1):
            url = "VLC IDE · Build" if name.startswith("b-") else "matrix.hicode.com"
            pages[(sid, i)] = framed(sid, os.path.join(ROOT, "assets", "web", name + ".png"), caption, url)
    for i in range(len(FRAMES)):
        pages[("s08c", i + 1)] = dag_frame(i)
    for j, (name, caption) in enumerate(S.FLOW_REAL, len(FRAMES) + 1):
        pages[("s08c", j)] = framed("s08c", os.path.join(ROOT, "assets", "web", name + ".png"), caption, "Flow · Workflow canvas")
    pages[("s12", 2)] = framed("s12", os.path.join(ROOT, "assets", "web", "25-settings-devices.png"), S.S12_CAPTION, "matrix.hicode.com")
    only = sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] else None
    plan = {}
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        for (sid, i), body in sorted(pages.items(), key=lambda kv: (kv[0][0], kv[0][1])):
            plan.setdefault(sid, []).append(f"{sid}-{i:02d}.png")
            if only and sid not in only:
                continue
            pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
            pg.wait_for_timeout(120)
            pg.screenshot(path=os.path.join(OUT, f"{sid}-{i:02d}.png"))
        br.close()
    json.dump(plan, open(os.path.join(ROOT, "build", f"plan-{LANG}.json"), "w"), indent=2)
    print({k: len(v) for k, v in plan.items()})


if __name__ == "__main__":
    main()
