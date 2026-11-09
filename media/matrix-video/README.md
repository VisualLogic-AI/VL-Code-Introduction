# Matrix product video assets

Public home for every video, recording, slide and pipeline file produced for the Matrix / HiCode product videos. Everything here is marketing material and may be shared freely. Earlier finished videos (v1 to v4) are published as release assets: https://github.com/VisualLogic-AI/VL-Code-Introduction/releases/tag/matrix-product-videos-20261108 . The current v5 file and all raw material live in this folder.

## Final videos

| File | Language | Length | Notes |
| --- | --- | --- | --- |
| `Matrix-Intro-EN-v5.mp4` | English (1.3x narration) | 6:38 | Current deliverable: slides + matrix.hicode.com production + VLC Flow DAGs with a live tool-DAG run + Map/Code/Preview/Object Tree/Logic/ER/Theme + hosted Huzhou VL apps |
| v4 / v3 (Chinese), v2 / v1 (English) | — | — | In the release linked above |

## Recordings (raw, with `marks.json` timecodes used by the composer)

- `flow/` VLC Flow canvas on the English Smart Campus project: Meta Sharded, Parallel Codegen, EnterpriseGrand cascade graphs and a real run of the read-only `metadata-check` DAG (`flow.webm` is referenced from the v5 composer; stills `g-*.png`, `04b-run-dialog.png`, `05-run-end.png`).
- `vlc-tour/` VLC IDE tour of the English Smart Campus project: Map, Code, Preview, Object Tree, Logic (METHOD Refresh / METHOD init), ER, Theme, Flow (`tour.webm` + stills).
- `apps/` Hosted Huzhou University VL applications recorded from the Mac: faculty development dashboard (`pre.dev.h5app.com/play/Wyqvuc5U`) and teacher recuperation service admin side (demo login printed on its own login page; de-identified demo data). `apps.webm` + stills.
- `huzhou/` Huzhou faculty development dashboard private project opened in VL 4.3.0 on the Mac (frame only; service-backed data does not load in local preview).
- `smartcampus-vl/` The English "Smart Campus" VL project used in the IDE shots: the bundled `huzhou-dashboard` example with 179 Chinese strings translated (`translate.py` reproduces it from a fresh copy). Code identical to the example apart from string literals and comments.
- `tools/record-tour-en.cjs` Playwright tour recorder as run on the Mac/cloud.

## v5 sources and pipeline

- `v5-sources/script.json` narration (English) with per-line clip acts; `timeline.json` (line start/end after TTS); `subs.srt`; `slides/` PNG slides; `audio/` edge-tts lines (`en-US-AndrewNeural`, rate +30%).
- `pipeline/` `tts_par.py` + `build_audio.py` (TTS, envelope, timeline, subtitles), `slides.cjs` (slide renderer), `rec_flow_cloud.cjs` / `rec_tour_cloud.cjs` (Playwright recorders with marks), `compose5.py` (marks-based clip plans, speed badges, ffmpeg concat, ASS subtitles → `Matrix-Intro-EN-v5.mp4`).
- `web-page.html` The claude.ai artifact page that plays the video in ≤20 MB parts.

## Provenance and honesty notes

- Production shots use the founder's own account on matrix.hicode.com with real devices and Brains; the Brain-Hand Task in v5 reports 3 of 5 steps done and 2 not done (no command execution permission on that lease at recording time) — kept as recorded.
- The VL generation DAG did **not** run end to end through Matrix during recording (worker B030 file-lane gate refuses API-Brain text replies on Workspace-bound Tasks; VLC's evidence rules do not accept Claude personal CLI seats; one seat's OAuth had expired). The v5 narration says so and shows the tool-only `metadata-check` DAG running instead. Details are tracked in the private engineering repository (Fresh/Lines, 2026-11-09 entry).
- No credentials, session tokens or private raw data are in this branch.
