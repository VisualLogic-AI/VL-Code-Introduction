"""Synthesize narration per segment, then enforce a target speaking rate.

Usage: tts.py <lang zh|en> [only_ids_csv]
Primary route: OpenAI gpt-4o-mini-tts (credential loaded locally from Secret Root).
Fallback: macOS `say`. Leading/trailing silence trimmed; ffmpeg atempo (pitch-preserving)
applied when the voice is slower than the target rate.
zh target: 1.45x the measured v1 rate (build/audio-v1-zh). en target: 175 words/min.
Writes build/audio-<lang>/<id>.wav + manifest.json (sanitized).
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
import secret_env  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FF, FP = "/opt/homebrew/bin/ffmpeg", "/opt/homebrew/bin/ffprobe"
SPEEDUP = float(os.environ.get("ZH_SPEEDUP", "1.45"))
EN_WPM = float(os.environ.get("EN_WPM", "175"))


def dur(p):
    return float(subprocess.check_output([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip())


def units(text, lang):
    if lang == "en":
        return len(re.findall(r"[A-Za-z0-9'-]+", text))
    return len(re.findall(r"[一-鿿]", text)) + len(re.findall(r"[A-Za-z0-9-]+", text))


def zh_v1_rate():
    m = json.load(open(os.path.join(ROOT, "build", "audio-v1-zh", "manifest.json")))
    segs = {s["id"]: s["text"] for s in json.load(open(os.path.join(ROOT, "script", "segments.json"), encoding="utf-8"))["segments"]}
    u = sum(units(segs[s["id"]], "zh") for s in m["segments"])
    t = sum(s["seconds"] for s in m["segments"])
    return u / t


def openai_tts(text, instructions, out_mp3, voice):
    from openai import OpenAI
    with OpenAI().audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts", voice=voice, input=text, instructions=instructions, response_format="mp3",
    ) as resp:
        resp.stream_to_file(out_mp3)


def main():
    lang = sys.argv[1]
    only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 and sys.argv[2] else None
    data = json.load(open(os.path.join(ROOT, "script", f"segments_{lang}.json"), encoding="utf-8"))
    outdir = os.path.join(ROOT, "build", f"audio-{lang}")
    os.makedirs(outdir, exist_ok=True)
    voice = os.environ.get("TTS_VOICE", "coral")
    have_key = "OPENAI_API_KEY" in secret_env.load(["OPENAI_API_KEY"]) or bool(os.environ.get("OPENAI_API_KEY"))
    target = zh_v1_rate() * SPEEDUP if lang == "zh" else EN_WPM / 60.0
    unit = "chars/s" if lang == "zh" else "words/s"
    man = {"lang": lang, "route": "openai" if have_key else "say", "model": "gpt-4o-mini-tts", "voice": voice,
           "target_rate": round(target, 3), "unit": unit, "segments": []}
    if lang == "zh":
        man["v1_rate"] = round(zh_v1_rate(), 3)
    for seg in data["segments"]:
        if only and seg["id"] not in only:
            continue
        sid, text = seg["id"], seg["text"]
        raw = os.path.join(outdir, sid + ".raw")
        used = "openai"
        try:
            if not have_key:
                raise RuntimeError("no key")
            openai_tts(text, data.get("voice_instructions", ""), raw + ".mp3", voice)
            raw += ".mp3"
        except Exception as exc:
            print(f"{sid}: openai failed ({type(exc).__name__} {getattr(exc, 'status_code', '')}); using say")
            used = "say"
            raw += ".aiff"
            subprocess.check_call(["say", "-v", "Tingting" if lang == "zh" else "Samantha", "-r", "230", "-o", raw, text])
        trimmed = os.path.join(outdir, sid + ".trim.wav")
        trim = ("silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,"
                "areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse")
        subprocess.check_call([FF, "-y", "-v", "error", "-i", raw, "-af", trim, "-ar", "48000", "-ac", "2", trimmed])
        d0 = dur(trimmed)
        n = units(text, lang)
        factor = min(max(1.0, d0 / (n / target)), 1.9)
        wav = os.path.join(outdir, sid + ".wav")
        subprocess.check_call([FF, "-y", "-v", "error", "-i", trimmed, "-af", f"atempo={factor:.4f}", "-ar", "48000", "-ac", "2", wav])
        os.remove(raw)
        os.remove(trimmed)
        d1 = dur(wav)
        man["segments"].append({"id": sid, "route": used, "units": n, "raw_seconds": round(d0, 3), "atempo": round(factor, 4),
                                "seconds": round(d1, 3), "rate": round(n / d1, 3)})
        print(f"{sid}: {used} raw {d0:.2f}s x{factor:.3f} -> {d1:.2f}s  {n/d1:.2f} {unit}")
    mf = os.path.join(outdir, "manifest.json")
    if only and os.path.exists(mf):
        old = json.load(open(mf))
        ids = {s["id"] for s in man["segments"]}
        man["segments"] = [s for s in old["segments"] if s["id"] not in ids] + man["segments"]
    order = [s["id"] for s in data["segments"]]
    man["segments"].sort(key=lambda s: order.index(s["id"]))
    json.dump(man, open(mf, "w"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
