"""Real operation capture of the Matrix desktop window (VisualLogic.app).

Clicks each sidebar page through Accessibility (AXPress), captures only that
window with `screencapture -l`, and blurs sensitive text (local paths, other
emails, key-like strings) using Accessibility text positions.
Restores the page that was open before the capture.
Outputs: build/desktop/<n>-<page>.png (clean) + capture.json (sanitized).
"""
import json
import os
import re
import subprocess
import sys
import time

import ApplicationServices as A
import Quartz
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "desktop")
PAGES = ["Overview", "Account", "Device & Gateway", "AI Resources", "Core Modules"]
OWNER_EMAIL = "kk@visuallogic.ai"
SENSITIVE = [
    re.compile(r"(^|\s)(/Users/|/private/|/tmp/|~/|[A-Z]:\\)"),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"(sk-|ghp_|xox[bp]-|AKIA)[A-Za-z0-9_-]{6,}"),
    re.compile(r"\b[0-9a-f]{32,}\b"),
]


def ax(e, attr):
    err, v = A.AXUIElementCopyAttributeValue(e, attr, None)
    return v if err == 0 else None


def pos_size(e):
    p, s = ax(e, "AXPosition"), ax(e, "AXSize")
    if p is None or s is None:
        return None
    ok1, pt = A.AXValueGetValue(p, A.kAXValueCGPointType, None)
    ok2, sz = A.AXValueGetValue(s, A.kAXValueCGSizeType, None)
    return (pt.x, pt.y, sz.width, sz.height)


def walk(e, out, depth=0):
    if depth > 25:
        return
    out.append(e)
    for k in ax(e, "AXChildren") or []:
        walk(k, out, depth + 1)


def label(e):
    for attr in ("AXTitle", "AXDescription", "AXValue"):
        v = ax(e, attr)
        if isinstance(v, str) and v.strip():
            return v
    return None


def is_sensitive(text):
    for rx in SENSITIVE:
        for m in rx.finditer(text):
            if m.group(0).strip().lower() == OWNER_EMAIL:
                continue
            return True
    return False


def find_pid():
    out = subprocess.check_output(["pgrep", "-f", "/Applications/VisualLogic.app/Contents/MacOS/visuallogic-core"])
    return int(out.split()[0])


def window_id(pid):
    for w in Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionAll, 0):
        if w.get("kCGWindowOwnerPID") == pid and w.get("kCGWindowLayer") == 0 and w.get("kCGWindowName") == "Matrix":
            return w["kCGWindowNumber"], dict(w["kCGWindowBounds"])
    raise SystemExit("Matrix window not found")


def main():
    os.makedirs(OUT, exist_ok=True)
    pid = find_pid()
    app = A.AXUIElementCreateApplication(pid)
    win = (ax(app, "AXWindows") or [None])[0]
    if win is None:
        raise SystemExit("no AX window")
    wid, b = window_id(pid)
    wx, wy = b["X"], b["Y"]
    elems = []
    walk(win, elems)
    buttons = {label(e): e for e in elems if ax(e, "AXRole") == "AXButton" and label(e) in PAGES}
    missing = [p for p in PAGES if p not in buttons]
    if missing:
        raise SystemExit(f"sidebar buttons missing: {missing}")
    # remember current page: the page heading text equal to a page name, outside the sidebar
    side_x = max(pos_size(buttons[p])[0] + pos_size(buttons[p])[2] for p in PAGES)
    current = None
    for e in elems:
        if ax(e, "AXRole") == "AXStaticText" and label(e) in PAGES:
            ps = pos_size(e)
            if ps and ps[0] > side_x:
                current = label(e)
                break
    report = {"window_bounds": b, "restored_page": current, "pages": []}
    for i, page in enumerate(PAGES, 1):
        fresh = []
        walk(win, fresh)
        btns = {label(e): e for e in fresh if ax(e, "AXRole") == "AXButton" and label(e) in PAGES}
        btn = btns.get(page) or buttons[page]
        bp = pos_size(btn) or pos_size(buttons[page])
        buttons.update(btns)
        A.AXUIElementPerformAction(btn, "AXPress")
        time.sleep(1.8)
        raw = os.path.join(OUT, f"raw-{i:02d}.png")
        subprocess.check_call(["screencapture", "-x", "-o", f"-l{wid}", raw])
        img = Image.open(raw).convert("RGB")
        scale = img.width / b["Width"]
        cur = []
        walk(win, cur)
        boxes = []
        for e in cur:
            t = label(e)
            if not t or not is_sensitive(t):
                continue
            ps = pos_size(e)
            if not ps or ps[2] <= 0 or ps[3] <= 0:
                continue
            x0, y0 = (ps[0] - wx) * scale, (ps[1] - wy) * scale
            x1, y1 = x0 + ps[2] * scale, y0 + ps[3] * scale
            x0, y0 = max(0, int(x0) - 6), max(0, int(y0) - 4)
            x1, y1 = min(img.width, int(x1) + 6), min(img.height, int(y1) + 4)
            if x1 > x0 and y1 > y0:
                boxes.append((x0, y0, x1, y1))
        for bx in boxes:
            region = img.crop(bx).filter(ImageFilter.GaussianBlur(14))
            img.paste(region, bx[:2])
        name = page.lower().replace(" & ", "-").replace(" ", "-")
        clean = os.path.join(OUT, f"{i:02d}-{name}.png")
        img.save(clean)
        os.remove(raw)
        click = [((bp[0] - wx) + bp[2] / 2) * scale, ((bp[1] - wy) + bp[3] / 2) * scale]
        report["pages"].append({"page": page, "file": os.path.relpath(clean, ROOT), "size": [img.width, img.height],
                                "click_px": [round(click[0]), round(click[1])], "blurred_boxes": len(boxes)})
        print(f"{page}: {img.width}x{img.height} blurred={len(boxes)}")
    if current:
        fresh = []
        walk(win, fresh)
        for e in fresh:
            if ax(e, "AXRole") == "AXButton" and label(e) == current:
                A.AXUIElementPerformAction(e, "AXPress")
                break
    json.dump(report, open(os.path.join(OUT, "capture.json"), "w"), indent=2)
    print("restored:", current)


if __name__ == "__main__":
    main()
