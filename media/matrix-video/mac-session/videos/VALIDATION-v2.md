# Validation v2 — faster Chinese narration, new DAG + VLC IDE scenes, English version

| Item | 中文 v2 | English |
|---|---|---|
| File | out/Matrix-产品介绍-中文-v2.mp4 | out/Matrix-Product-Intro-EN.mp4 |
| sha256 | 517e2a4a0aa43a1e42e6bb2af0c54b169e011b5051b5bf196e0de595dcb1f008 | 0eb0091804b779faf37c9fc04081041955e72ab2c023bf92d0594f84fdf44a7f |
| Duration / size | 287.94 s / 69.2 MB | 289.15 s / 70.4 MB |
| Scenes | 17 (v1: 13) | 17 |
| Video / audio | H.264 1920x1080 30fps; AAC 48 kHz | same |
| Loudness | -15.8 LUFS, LRA 4.1 | -16.0 LUFS, LRA 4.3 |
| Speaking rate | 4.629 chars/s vs v1 3.194 → 1.45x | 2.916 words/s = 175 wpm |
| Rate method | gpt-4o-mini-tts (fast-pace prompt) + silence trim + ffmpeg atempo 1.23–1.60 (pitch-preserving) | same, atempo 1.09–1.53 |
| Subtitles | burned-in + mov_text (chi) + SRT, 91 cues, last ends 04:47.327 | burned-in + mov_text (eng) + SRT, 105 cues, last ends 04:48.576 |
| Decode test | 0 errors | 0 errors |
| Pauses > 1.5 s | 0 | 0 |
| Visual QA | all 58 shots + 17 scene frames PASS | all 58 shots + 17 scene frames PASS |

New scenes: s08b DAG orchestration (Matrix PRD-review screenshots: workflow choices, static catalog, dynamic DAG, workflow call),
s08c DAG execution (6-frame illustrated walkthrough: plan → parallel → test → dynamic fix node → human gate → deliver, then 5 real Flow run screenshots executing → finished → node detail → artifacts),
s11b VLC IDE views (editor, Visual, Logic, Flow, ER, DB), s11c VLC IDE AI assistant / compile / preview / publish / library.
Sources: CodeHub docs/ui-audit/2026-10 (build, flow), VL-Matrix-Cloud docs/reviews/2026-09-22-prd-1.2.0/screenshots.
Redaction additions in v2: hex hashes, path fragments (CodeHub/Documents/Users), 9+ digit IDs (account chip). v1 archived in out/archive/v1.
