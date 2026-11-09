"""Assemble narration + shots into the final MP4 with Chinese subtitles.

Usage: build_video.py [scene_ids_csv] [output_name]
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FF, FP = "/opt/homebrew/bin/ffmpeg", "/opt/homebrew/bin/ffprobe"
B = os.path.join(ROOT, "build")
FPS, XF, LEAD, TAIL = 30, 0.45, 0.3, 0.4
LANG = "zh"


def run(args):
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def dur(p):
    return float(subprocess.check_output([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip())


def chunks(text, maxlen=None):
    if LANG == "en":
        maxlen = maxlen or 58
        parts = [p for p in re.split(r"(?<=[.,;:!?])\s+", text) if p.strip()]
        out, cur = [], ""
        for p in parts:
            for w in p.split():
                if cur and len(cur) + 1 + len(w) > maxlen:
                    out.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if len(cur) > maxlen * 0.55:
                out.append(cur)
                cur = ""
        if cur:
            out.append(cur)
        return [c.rstrip(",;:") for c in out]
    maxlen = maxlen or 24
    parts = [p for p in re.split(r"(?<=[。！？；，、：])", text) if p.strip()]
    out, cur = [], ""
    for p in parts:
        if cur and len(cur) + len(p) > maxlen:
            out.append(cur)
            cur = p
        else:
            cur += p
    if cur:
        out.append(cur)
    return [c.rstrip("，、；：") for c in out]


def ts(t):
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def scene_clip(sid, shots, adur, out, subs=()):
    total = LEAD + adur + TAIL
    n = len(shots)
    per = (total + XF * (n - 1)) / n
    frames = int(round(per * FPS))
    args = [FF, "-y"]
    for s in shots:
        args += ["-loop", "1", "-framerate", str(FPS), "-t", f"{per:.3f}", "-i", os.path.join(B, f"shots-{LANG}", s)]
    args += ["-i", os.path.join(B, f"audio-{LANG}", f"{sid}.wav")]
    for png, _, _ in subs:
        args += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", png]
    fl = []
    for i in range(n):
        zin = i % 2 == 0
        z = f"'1+0.045*on/{frames}'" if zin else f"'1.045-0.045*on/{frames}'"
        fl.append(f"[{i}:v]scale=3840:2160,zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps={FPS},"
                  f"trim=duration={per:.3f},setpts=PTS-STARTPTS,format=yuv420p[v{i}]")
    last = "v0"
    for i in range(1, n):
        off = per * i - XF * i
        fl.append(f"[{last}][v{i}]xfade=transition=fade:duration={XF}:offset={off:.3f}[x{i}]")
        last = f"x{i}"
    if sid == "s01":
        fl.append(f"[{last}]fade=t=in:st=0:d=0.8[vf]")
        last = "vf"
    if sid == "s13":
        fl.append(f"[{last}]fade=t=out:st={total-1.0:.3f}:d=1.0[vo]")
        last = "vo"
    for j, (_, a, b) in enumerate(subs):
        fl.append(f"[{last}][{n+1+j}:v]overlay=0:H-h-28:enable='between(t,{a:.3f},{b:.3f})'[sb{j}]")
        last = f"sb{j}"
    fl.append(f"[{n}:a]adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,atrim=0:{total:.3f}[a]")
    args += ["-filter_complex", ";".join(fl), "-map", f"[{last}]", "-map", "[a]", "-t", f"{total:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", out]
    run(args)
    return total


def render_subs(items):
    from playwright.sync_api import sync_playwright
    d = os.path.join(B, f"subs-{LANG}")
    os.makedirs(d, exist_ok=True)
    css = ("*{margin:0;padding:0}html,body{background:transparent;width:1920px;height:140px}"
           "body{display:flex;align-items:center;justify-content:center;font-family:" + ("'PingFang SC',sans-serif" if LANG == "zh" else "'Helvetica Neue',sans-serif") + "}"
           "span{font-size:46px;font-weight:600;color:#fff;background:rgba(6,8,18,.72);padding:12px 34px;border-radius:12px;"
           "letter-spacing:1px;text-shadow:0 2px 6px rgba(0,0,0,.8)}")
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 1920, "height": 140})
        for key, text in items:
            pg.set_content(f"<html><head><meta charset='utf-8'><style>{css}</style></head><body><span>{text}</span></body></html>")
            pg.screenshot(path=os.path.join(d, key + ".png"), omit_background=True)
        br.close()
    return d


def main():
    global LANG
    LANG = sys.argv[1]
    name = sys.argv[2]
    only = sys.argv[3].split(",") if len(sys.argv) > 3 and sys.argv[3] else None
    segs = json.load(open(os.path.join(ROOT, "script", f"segments_{LANG}.json"), encoding="utf-8"))["segments"]
    plan = json.load(open(os.path.join(B, f"plan-{LANG}.json")))
    cdir = os.path.join(B, f"clips-{LANG}")
    os.makedirs(cdir, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "out"), exist_ok=True)
    t, srt, idx, lst, timeline = 0.0, [], 1, [], []
    for seg in segs:
        sid = seg["id"]
        if only and sid not in only:
            continue
        wav = os.path.join(B, f"audio-{LANG}", f"{sid}.wav")
        adur = dur(wav)
        clip = os.path.join(cdir, f"{sid}.mp4")
        cs = chunks(seg["text"])
        weights = [max(len(c), 4) for c in cs]
        rel, local = LEAD, []
        for k, (c, w) in enumerate(zip(cs, weights)):
            d = adur * w / sum(weights)
            srt.append(f"{idx}\n{ts(t + rel)} --> {ts(t + rel + d - 0.04)}\n{c}\n")
            local.append((f"{sid}-{k:02d}", c, rel, rel + d - 0.04))
            idx += 1
            rel += d
        sd = render_subs([(key, c) for key, c, _, _ in local])
        total = scene_clip(sid, plan[sid], adur, clip, [(os.path.join(sd, key + ".png"), a, b) for key, _, a, b in local])
        timeline.append({"id": sid, "start": round(t, 3), "end": round(t + total, 3), "narration_s": round(adur, 3), "shots": plan[sid]})
        lst.append(f"file '{clip}'")
        t += total
        print(f"{sid}: {total:.2f}s")
    open(os.path.join(cdir, "list.txt"), "w").write("\n".join(lst) + "\n")
    srt_path = os.path.join(ROOT, "out", f"{name}.srt")
    open(srt_path, "w", encoding="utf-8").write("\n".join(srt))
    joined = os.path.join(B, f"joined-{LANG}.mp4")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(cdir, "list.txt"), "-c", "copy", joined])
    final = os.path.join(ROOT, "out", f"{name}.mp4")
    run([FF, "-y", "-i", joined, "-i", srt_path, "-map", "0:v", "-map", "0:a", "-map", "1:s",
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-c:s", "mov_text", "-metadata:s:s:0", "language=" + ("chi" if LANG == "zh" else "eng"), "-movflags", "+faststart", final])
    json.dump({"duration_s": round(t, 3), "scenes": timeline}, open(os.path.join(ROOT, "out", f"timeline-{LANG}.json"), "w"),
              ensure_ascii=False, indent=2)
    print("total", round(t, 2), final)


if __name__ == "__main__":
    main()
