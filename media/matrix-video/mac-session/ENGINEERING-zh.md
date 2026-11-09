# Matrix 产品介绍视频（中文）— 录制与生成工程

## 产物
- `out/Matrix-产品介绍-中文.mp4` — 1920×1080 / 30fps / H.264 + AAC，中文字幕已烧录，另含可开关的 mov_text 中文字幕轨
- `out/Matrix-产品介绍-中文.srt` — 外挂中文字幕
- `out/timeline.json` — 每段时间轴（场景、旁白时长、所用画面）
- `probe/` — 录制前的就绪检查与 probe 证据（已脱敏）

## 实际方法
| 环节 | 方法 |
|---|---|
| 旁白稿 | Claude 依据本机 `VL-Matrix-Cloud/docs/MATRIX-PRODUCT-PRD.zh.md`（§1、§4、§5）与 ui-audit 文档编写：`script/segments.json` |
| 中文配音 | OpenAI `gpt-4o-mini-tts`，voice `coral`；凭据仅在本机 Python 进程内从 Secret Root 读取（`scripts/secret_env.py`），不打印、不落盘；出口为美国（OpenAI 支持地区）。失败时自动回退 macOS `say`（Tingting） |
| 桌面端操作画面 | 实机录制：通过 macOS 辅助功能依次点击 Matrix 桌面端（VisualLogic.app）侧栏五个页面，用 `screencapture -l` 只截该窗口；本机路径、非本人邮箱等按辅助功能文字坐标自动模糊；结束后恢复原页面（`scripts/capture_desktop.py`） |
| Web 端操作画面 | CodeHub `docs/ui-audit/2026-10/screenshots`（matrix-work / matrix-ops）中的真实产品截图 |
| 版式与字幕 | Playwright（Chromium）渲染 1920×1080 画面与字幕 PNG（PingFang SC），`scripts/render_shots.py` |
| 合成 | Homebrew ffmpeg 9.0.2：缓慢推拉、交叉淡化、按旁白时长对齐、字幕叠加、loudnorm（-16 LUFS），`scripts/build_video.py` |
| 画面质检 | OpenAI `gpt-4.1` 视觉检查抽帧（渲染与敏感信息），`scripts/qa_frames.py` |

未使用 Sora 等生成式视频：操作演示必须是真实界面。未使用 Kimi/DeepSeek：本任务无需其文本能力，且二者不提供 TTS/视频接口。

## 重新生成
```bash
.venv/bin/python scripts/tts.py                 # 配音
.venv/bin/python scripts/capture_desktop.py     # 桌面端实机画面
.venv/bin/python scripts/render_shots.py        # 画面
.venv/bin/python scripts/build_video.py         # 合成
```
