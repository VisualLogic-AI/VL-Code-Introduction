"""Visual QA of frames via an OpenAI vision model (credential loaded locally).

Usage: qa_frames.py <png> [<png> ...]  -> prints a sanitized per-image report.
"""
import base64
import io
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import secret_env  # noqa: E402
from PIL import Image  # noqa: E402

PROMPT = (
    "You are a visual QA reviewer for a product demo video. For EACH image (in the order given, named in the text before it), "
    "output one line: <name> | rendering: OK/PROBLEM (<short reason>) | sensitive: NONE or <type and location>.\n"
    "Rendering checks: text legible (including Chinese), nothing cut off, no tofu/missing glyph boxes, subtitles at the bottom readable, "
    "a yellow highlight ring (if present) sits on a left sidebar button, no overlapping or broken layout.\n"
    "Sensitive checks: API keys, tokens, passwords, full local filesystem paths (/Users/...), email addresses other than kk@visuallogic.ai, "
    "phone numbers, IPs other than 127.0.0.1, private personal data. Blurred regions count as handled. Never quote a secret value.\n"
    "End with: VERDICT: PASS or VERDICT: FAIL (<names>)."
)


def enc(path, width=1600):
    im = Image.open(path).convert("RGB")
    if im.width > width:
        im = im.resize((width, int(im.height * width / im.width)))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=85)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def main():
    secret_env.load(["OPENAI_API_KEY"])
    from openai import OpenAI
    client = OpenAI()
    content = [{"type": "text", "text": PROMPT}]
    for p in sys.argv[1:]:
        content.append({"type": "text", "text": "Image name: " + os.path.basename(p)})
        content.append({"type": "image_url", "image_url": {"url": enc(p), "detail": "high"}})
    model = os.environ.get("QA_MODEL", "gpt-4.1")
    try:
        r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": content}], temperature=0)
    except Exception as exc:
        print(f"qa call failed: {type(exc).__name__} {getattr(exc, 'status_code', '')}")
        sys.exit(2)
    print(f"[model {model}]")
    print(r.choices[0].message.content)


if __name__ == "__main__":
    main()
