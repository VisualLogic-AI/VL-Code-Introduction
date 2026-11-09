# Mac-side production materials (Matrix product videos)

Produced on the founder's Mac through the Matrix Hand (session "本地 Hand 调用 OpenAI Brain 的 TTS 和视频生成"). Public marketing material; no credentials.

| Folder | Content |
| --- | --- |
| `videos/` | `Matrix-产品介绍-中文-v2.mp4` (Chinese, 4:48, narration at 1.45×) and `Matrix-Product-Intro-EN.mp4` (English, 4:49), each with `.srt` subtitles and `timeline-*.json`; `VALIDATION-v2.md` frame-by-frame QA report; `probe-s01-s04.*` the render probe; `archive-v1/` the first Chinese cut with its validation report |
| `script/` | Narration segments (`segments.json`, `segments_zh.json`, `segments_en.json`) |
| `scripts/` | The production pipeline: `tts.py` (OpenAI TTS with macOS `say` fallback), `capture_desktop.py` (real desktop-app capture with blur), `render_shots.py` (Playwright 1080p frames + subtitles), `build_video.py` (ffmpeg assembly, loudnorm), `qa_frames.py` (vision QA), `sanitize_web.py`, `secret_env.py` (reads provider keys inside the local process only) |
| `screenshots-web/` | Real product screenshots used in the videos (Matrix web, VLC editor tabs, DAG runs) |
| `probe/` | Readiness checks and QA transcripts (`READINESS.md`, `QA-*.txt`, probe frames) |
| `recorders/` | Playwright recorders used for the Huzhou project, the hosted apps, the IDE tour and the generation attempts |
| `release-review/` | Review stills, manifest, checksums and release notes of the v1 to v4 public release |
| `ENGINEERING-zh.md` | How the Chinese video was made (Chinese) |
| `PRODUCTION-BRIEF.md` | The production brief the Mac session worked from |

Intermediate build files (clips, per-segment audio), logs and the private `huzhou-factory` checkout are intentionally not published.
