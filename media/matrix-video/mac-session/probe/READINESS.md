# Readiness and probe evidence (sanitized)

Date: 2026-11-08 (UTC). Hand dev_3551181d05b9, workspace ws_a1a65170c19e (this folder), owner-mode route.

| Check | Result |
|---|---|
| Live Hand command execution | OK (`echo ok` / pwd = this folder) |
| ffmpeg / ffprobe | /opt/homebrew/bin, 9.0.2 (no libass: subtitles rendered as PNG overlays instead) |
| Python env | .venv (Homebrew python3.14): openai, playwright+chromium, pillow, pyobjc Quartz/ApplicationServices |
| Screen recording permission | CGPreflightScreenCaptureAccess = True; window-only capture via `screencapture -l` (full-screen permission probe image deleted after check) |
| Accessibility permission | AXIsProcessTrusted = True (sidebar navigation of Matrix desktop window) |
| Narration route | OpenAI gpt-4o-mini-tts; credential name OPENAI_API_KEY present in local Secret Root, loaded only inside the calling process; value never printed/logged |
| Egress / region | US (ipinfo country), OpenAI-supported region |
| Demo pages | Matrix desktop window (VisualLogic.app 1.3.185, title "Matrix"); real web screenshots from CodeHub ui-audit 2026-10 |
| Secret-free frames | Automatic blur of local paths / non-owner emails / key-like strings by AX text boxes (Device & Gateway: 7 boxes); vision QA of 11 probe frames: PASS |
| Probe render | out/probe-s01-s04.mp4 — 42.87 s, 1920x1080 h264 30fps, AAC 48 kHz, mov_text subtitles |

No macOS permission prompt was required.
