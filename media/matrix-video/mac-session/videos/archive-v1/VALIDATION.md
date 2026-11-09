# Final validation — Matrix 产品介绍视频（中文）

| Item | Result |
|---|---|
| File | out/Matrix-产品介绍-中文.mp4 (64,243,853 bytes, sha256 ef913d82705740aae550f0f6a783fc70dec23c89da1f7eaa2c3ab5de039fe94c) |
| Duration | 304.27 s (13 scenes, out/timeline.json) |
| Video | H.264, 1920x1080, 30 fps, yuv420p, faststart |
| Audio | AAC 48 kHz stereo; integrated loudness -16.1 LUFS, LRA 4.4 LU |
| Subtitles | Burned-in Chinese captions + embedded mov_text track (chi) + out/Matrix-产品介绍-中文.srt (69 cues, last cue ends 05:03.502 < 05:04.27) |
| Timing | Each scene = 0.35 s lead + narration + 0.65 s tail; captions split by punctuation and timed proportionally within each narration segment |
| Decode test | Full decode of video+audio: 0 errors |
| Silence | Only 3 pauses of ~2.0–2.4 s, all at scene boundaries (natural transitions) |
| Visual QA | All 31 rendered shots: rendering OK, sensitive NONE (probe/QA-shots-1.txt, probe/QA-shots-2.txt) |
| Redaction | Desktop capture: Accessibility-text-based blur (7 boxes on Device & Gateway). Web screenshots: on-device macOS Vision OCR blur of paths, UUIDs, non-owner emails, URLs/invite links, IPs (originals in assets/web/orig, not used in output) |
| Fixes during QA | Round 1: local path in Add Workspace dialog (s06-2); round 2: IP in invite link (s11-2) — both blurred and re-verified |
