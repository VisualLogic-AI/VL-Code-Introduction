"""Blur sensitive text in web screenshots using on-device macOS Vision OCR.

Originals are kept in assets/web/orig/; sanitized copies replace assets/web/*.png.
Prints only counts per file.
"""
import glob
import os
import re
import shutil

import Vision
from Foundation import NSURL
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "assets", "web")
ORIG = os.path.join(WEB, "orig")
OWNER = "kk@visuallogic.ai"
RX = [
    re.compile(r"(/Users/|/home/|/private/|/tmp/|/var/|~/|[A-Z]:\\|\\Users\\)"),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"(sk-|ghp_|xox[bp]-|AKIA)[A-Za-z0-9_-]{6,}"),
    re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"),
    re.compile(r"/\s*[\w.\-]+\s*/"),
    re.compile(r"https?\s*:|invite\s*=|join\.html|\d+\s*\.\s*\d+\s*\.\s*\d+\s*\.\s*\d+", re.I),
    re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{6,}"),
    re.compile(r"\b(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{7,}\b"),
    re.compile(r"\d{9,}"),
    re.compile(r"CodeHub|Documents|Users|VLProjects|[\w.-]+/[\w.-]+/", re.I),
]


def sensitive(t):
    for rx in RX:
        for m in rx.finditer(t):
            g = m.group(0)
            if g.lower() == OWNER or g.startswith("127.0.0.1"):
                continue
            return True
    return False


def ocr(path):
    url = NSURL.fileURLWithPath_(path)
    req = Vision.VNRecognizeTextRequest.alloc().init()
    req.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
    req.setUsesLanguageCorrection_(False)
    handler = Vision.VNImageRequestHandler.alloc().initWithURL_options_(url, None)
    handler.performRequests_error_([req], None)
    out = []
    for obs in req.results() or []:
        cand = obs.topCandidates_(1)
        if cand and len(cand):
            bb = obs.boundingBox()
            out.append((str(cand[0].string()), bb.origin.x, bb.origin.y, bb.size.width, bb.size.height))
    return out


def main():
    os.makedirs(ORIG, exist_ok=True)
    for p in sorted(glob.glob(os.path.join(WEB, "*.png"))):
        name = os.path.basename(p)
        src = os.path.join(ORIG, name)
        if not os.path.exists(src):
            shutil.copy2(p, src)
        img = Image.open(src).convert("RGB")
        W, H = img.size
        n = 0
        for text, x, y, w, h in ocr(src):
            if not sensitive(text):
                continue
            x0, x1 = int(x * W) - 8, int((x + w) * W) + 8
            y0, y1 = int((1 - y - h) * H) - 5, int((1 - y) * H) + 5
            box = (max(0, x0), max(0, y0), min(W, x1), min(H, y1))
            img.paste(img.crop(box).filter(ImageFilter.GaussianBlur(12)), box[:2])
            n += 1
        img.save(p)
        print(f"{name}: blurred {n}")


if __name__ == "__main__":
    main()
