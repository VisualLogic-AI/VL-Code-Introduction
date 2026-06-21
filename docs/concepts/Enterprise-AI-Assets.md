# Enterprise AI Assets / 企业 AI 资产

> **Own the intelligence. Don't rent it by the token. / 把智能变成资产，而不是按 token 租来用。**
>
> Public deck: [`../../decks/VL-Enterprise-AI-Assets-EN.pdf`](../../decks/VL-Enterprise-AI-Assets-EN.pdf) and [`../../decks/VL-Enterprise-AI-Assets-EN.pptx`](../../decks/VL-Enterprise-AI-Assets-EN.pptx).
> Bilingual, paired EN-then-中文. This public version removes internal build paths and keeps the commercial source boundary explicit.

---

## The thesis in one paragraph / 一段话讲清

**EN** — Most "AI adoption" today produces nothing durable: the value lives in throwaway chats, one engineer's private prompts, and a single model's API, and it evaporates the moment the model version changes or the person leaves. An **enterprise AI asset** is the opposite — a durable, owned capability that (1) is **decoupled from any specific model**, (2) **accumulates the company's own knowledge, methods, AI capabilities, and production experience**, (3) **stays inside the enterprise**, and (4) is **a complete solution — or a sharp solution to one specific problem**. The natural carrier is a **Flow**: bundle the knowledge + docs (including skills) + code + components that solve a problem into one Workflow / DAG. Made concrete, that asset is a **`.vflow`** — a self-describing, tamper-evident bundle — which you **maintain visually and run as a local-first Agent App.**

**中文** — 今天大多数「AI 落地」都没沉淀下任何资产：价值散落在用完即弃的对话、某个工程师私藏的 prompt、以及某一个模型的 API 里，模型一升级、人一离职就蒸发。**企业 AI 资产**正相反 —— 它是一份可拥有、可累积的能力，满足四条：① **与任何具体模型解耦**、② **沉淀企业自己的知识、方法、AI 能力与生产经验**、③ **留在企业内部**、④ **是一套完整方案 —— 或针对某个专门问题的方案**。最自然的载体是 **Flow**：把解决一个问题所需的知识 + 文档（含 skills）+ 代码 + 组件，编排进一张 Workflow / DAG。让它落地，这个资产就是一个 **`.vflow`** —— 一个自描述、防篡改的 bundle —— 你**以本地优先的 Agent App 可视化地维护并运行它**。

---

## 1 · The gap: a game needs a prompt, an app needs a harness / 缺口：做游戏靠 prompt，做企业应用靠 harness

**EN** — AI coding can make a game from one sentence. A game can live inside the prompt — rules, assets, state, and feedback are self-contained. A real enterprise solution cannot: it must connect backend resources, data contracts, approvals, and human decisions across many steps. It is not that AI cannot write the code; harnessing a real project is a long, grounded process, not one giant super-node. That long, grounded process is exactly where today's AI value evaporates — it lives in throwaway chats and nothing accumulates. *One AI node creates output. A DAG harness creates progress.*

**中文** — AI Coding 一句话就能做个游戏。游戏可以活在 prompt 里 —— 规则、素材、状态、反馈都相对自洽。真实企业方案不行：它必须把后台资源、数据契约、审批和人的决策，在漫长步骤里连起来。不是写不出代码，而是要整合并深入真实资源 —— 不是一个超级节点一次搞定。正是在这条漫长且落地的过程里，今天的 AI 价值在蒸发 —— 它散落在用完即弃的对话里，什么都没积累。*一个 AI 节点产出结果，一张 DAG harness 产出进展。*

## 2 · The definition: four conditions / 定义：四条

| | EN | 中文 |
|---|---|---|
| **1. Model-decoupled / 与模型解耦** | Pluggable providers, right-model-per-node — the model is a swappable input, not the asset. The value lives in the representation, which outlives any model version. | 模型 provider 可插拔、能力用在刀刃上 —— 模型是可替换的输入，不是资产本身。价值活在表示层，比任何一代模型都长寿。 |
| **2. Accumulates your own / 沉淀你自己的** | Banks the enterprise's own knowledge, methods, AI capabilities, and production experience — generate once, store it, reuse it. | 沉淀企业自己的知识、方法、AI 能力与生产经验 —— 造一次、存下来、反复用。 |
| **3. Kept inside / 留在企业内部** | Local-first: the asset never has to leave. Cloud deploy is an option, not a cage; export the source = 0 lock-in. | 本地优先：资产不必外流。云端部署是可选项，不是牢笼；可导出源码 = 0 绑定。 |
| **4. A solution, carried by Flow / 是方案，由 Flow 承载** | A complete solution — or a sharp one to a specific problem — orchestrated into one Workflow / DAG: a tamper-evident `.vflow`. | 一套完整方案 —— 或针对某个专门问题的方案 —— 编排成一张 Workflow / DAG：一个防篡改的 `.vflow`。 |

These four conditions become the four pillars below. / 这四条，就是下文的四根支柱。

## 3 · Pillar 1 — the model is an input, not the asset / 支柱一 —— 模型是输入，不是资产

**EN** — Anthropic, OpenAI, DeepSeek, Kimi, GLM, Gemini are all swappable; use expensive models for the hard nodes and cheap ones for the routine. The model plugs in — swapping it never destroys the asset. **Representation efficiency > model size.** The asset lives in the VL representation (the IR: human intent compiled to executable code), not in whichever model generated it. Whoever controls the representation controls the ceiling.

**中文** — Anthropic、OpenAI、DeepSeek、Kimi、GLM、Gemini 都可替换；难节点用贵模型，常规节点用便宜模型。模型只是插进来 —— 换掉它，绝不会毁掉资产。**表示效率 > 模型大小。** 资产活在 VL 表示里（IR：人类意图编译成可执行代码），而非生成它的那个模型。谁掌握表示层，谁就掌握上限。

## 4 · Pillar 2 — keep it in-house, compound it / 支柱二 —— 留在企业内，让它复利

**EN** — VL Agent is local-first, **not SaaS**: assets stay on your machines, and you can export the source any time — the enterprise owns the intelligence, not a vendor. The **Component Factory** banks expensive token-compute (generate once, reuse forever — *don't buy more GPUs, store the compute*). The **Resource Center** runs a review-gated lifecycle (`local → cloud-private → submitted → platform-shared`); nothing reaches the shared inventory without review.

**中文** — VL Agent 本地优先，**不是 SaaS**：资产留在你自己的机器上，随时可导出源码 —— 智能归企业，而不是供应商。**组件工厂**把昂贵的 token 算力存起来（造一次，永久复用 —— *别再买显卡，把算力存下来*）。**资源中心**走审核分级生命周期（`本地 → 云端私有 → 提交 → 平台共享`）；任何资源都要先过审才能进共享库。

## 5 · Pillar 3 — a solution isn't a prompt, it's a Flow / 支柱三 —— 解决方案不是 prompt，是一条 Flow

**EN** — A real enterprise solution must connect resources, steps, validation, and human decisions across a long line — and AI is brilliant at a point but can't hold a line. A DAG is the bridge from point intelligence to process intelligence: **creativity in the nodes, determinism in the edges.** So the natural carrier of a complete or problem-specific solution is a Flow — the one bundle that holds the whole line, not a clever sentence that holds none of it. *A game needs a prompt. A solution needs a Flow.*

**中文** — 真实的企业方案要在一条很长的线上连起资源、步骤、验证和人的决策 —— 而 AI 擅长一个「点」，守不住一条「线」。DAG 正是从点状智能走向过程智能的桥：**创造力在节点内部，确定性在连边之间。** 所以一个完整、或针对具体问题的方案，天然的载体就是 Flow —— 一个装得下整条线的 bundle，而不是一句什么都装不下的漂亮话。*做游戏靠 prompt，做解决方案靠 Flow。*

## 6 · Pillar 3 — the asset IS a `.vflow` / 支柱三 —— 资产即 `.vflow`

**EN** — Not a black box. A `.vflow` is a portable ZIP that carries the complete Workflow JSON (a steps DAG, Spec 4.1), its subflows, an auto-generated resource manifest, and its prompts and docs — in plain folders. It **declares its own portability** (`self-contained` / `needs-runtime` / `needs-secrets`), so you know before you open it whether it will just run. It is **tamper-evident**: every file is sha256-checksummed against the manifest; a mismatched or missing file is rejected on import. (Checksums, not signatures — never "signed" or "encrypted".)

**中文** — 不是黑箱。`.vflow` 是一个可移植的 ZIP，装下完整 Workflow JSON（步骤 DAG，Spec 4.1）、子流程、自动生成的资源清单，以及它的 prompt 与文档 —— 全在明文目录里。它**自声明可移植性**（`self-contained` / `needs-runtime` / `needs-secrets`），打开前你就知道能不能直接跑。它**防篡改**：每个文件按 sha256 与 manifest 校验，不匹配或缺失即在导入时拒绝。（是校验和，不是数字签名 —— 绝不说「签名」或「加密」。）

## 7 · Pillar 4 — maintain it visually / 支柱四 —— 可视化维护

**EN** — Everything is a picture you can inspect, and any run you can pause, resume, and audit. Architecture → **Map** (the whole asset as one architecture graph). Process → **DAG** (each run a verifiable steps DAG: breakpoints, pause, resume, rerun-from-step). Data → **ER**. Code ↔ graph is 1:1 bidirectional — edit either side. *Everything graphical; the IDE is a projection of the language.*

**中文** — 一切皆图，可查看；任意一次运行都可暂停、恢复、审计。架构 → **Map**（整个资产呈现为一张架构图）。过程 → **DAG**（每次运行是一张可校验的步骤 DAG：断点、暂停、恢复、从某步重跑）。数据 → **ER**。代码 ↔ 图 1:1 双向 —— 改哪一边都行。*一切皆图；IDE 就是语言的投影。*

## 8 · Pillar 4 — run it as an Agent App / 支柱四 —— 当作 Agent App 运行

**EN** — **Install:** an entry workflow plus a top-level `app` block makes the *same* `.vflow` an installable, portable Agent App — install, start, pause, resume. (An Agent App is a `.vflow` *with* an `app` block — not a separate `.vapp` file.) **Run:** the flow's own human-in-the-loop steps become the app's interaction cards automatically (Manifest → Workflow Engine executes → Control Plane persists → VL renders). **Audit:** a SQLite control plane records every run, task, artifact, and review — so any run is replayable and auditable.

**中文** — **安装：** 一条入口工作流加一个顶层 `app` 块，让*同一个* `.vflow` 变成可安装、可移植的 Agent App —— 安装、启动、暂停、恢复。（Agent App 就是一个*带* `app` 块的 `.vflow` —— 不是另一个 `.vapp` 文件。）**运行：** 流程自身的人审步骤自动变成应用的交互卡片（Manifest → 工作流引擎执行 → 控制面持久化 → VL 渲染）。**审计：** 一个 SQLite 控制面记录每一次运行、任务、产物与审核 —— 任何一次运行都可重放、可审计。

## 9 · Two shapes, one compounding library / 两种形态，一座越积越厚的资产库

**EN** — An AI asset is a **complete solution** — an end-to-end Agent App as one `.vflow` (like the in-box Approval Flow Runtime: requester/approver cards, SLA reminders, durable background execution) — **or a problem-specific solution**: one sharp capability as a `.vflow`. Both land in the same review-gated library; generate once, reuse forever; the enterprise's intelligence compounds.

**中文** — 一个 AI 资产，要么是**完整方案** —— 一整套端到端 Agent App 就是一个 `.vflow`（如开箱即有的 Approval Flow Runtime：申请/审批卡片、SLA 提醒、持久后台执行）—— 要么是**具体问题的解**：一项利落的能力，也是一个 `.vflow`。两者都进入同一座审核分级的资产库；造一次，永久复用；企业的智能越积越厚。

## 10 · Governance & audit: not a file, a governed asset / 治理与审计：不是文件，是受治理的资产

**EN** — Trustworthy by construction. The **control-plane ledger** (SQLite) records every run, task, artifact, and review — the ledger is what turns a clever one-off into an *institutional* asset. The **review-gated lifecycle** governs who can use what at every gate. The **tamper-evident bundle** sha256-checks every file against its manifest, byte-for-byte across both products. (Integrity is checksums — tamper-evident, not signed or encrypted.)

**中文** — 生而可信。**控制面账本**（SQLite）记录每一次运行、任务、产物与审核 —— 账本，正是把「一次性聪明脚本」变成*机构级*资产的关键。**审核分级生命周期**在每一道关口治理谁能用什么。**防篡改 bundle** 按 sha256 校验每个文件与 manifest，两个产品间逐字节一致。（完整性靠校验和 —— 防篡改，而非签名或加密。）

## 11 · The whole thesis / 完整命题

**EN** — Four pillars, one carrier: **model-decoupled** (pluggable providers, right model per node) · **precipitated in-house** (knowledge, methods, AI capability, production experience) · **carried by Flow** (a `.vflow` bundles the whole solution) · **maintained and run as a local-first Agent App.** The model is a swappable input; the asset is what outlives it — and stays inside the enterprise.

**中文** — 四根支柱，一个载体：**与模型解耦**（provider 可插拔，难节点用贵模型）· **在企业内部沉淀**（知识、方法、AI 能力、生产经验）· **以 Flow 为载体**（一个 `.vflow` 装下整套解决方案）· **作为本地优先的 Agent App 维护与运行**。模型只是可替换的输入；资产是比模型活得更久的那部分 —— 而且留在企业内部。

---

## Map to real, shipped concepts / 对应到真实、已发布的概念

| Thesis term / 命题用语 | VisualLogic concept / 真实概念 |
|---|---|
| The asset / 资产本体 | `.vflow` — portable, tamper-evident bundle (Workflow JSON @ Spec 4.1 + subflows + manifest + prompts + docs) |
| Decoupled from the model / 与模型解耦 | Pluggable model providers · right-model-per-node · VL as IR |
| Carried by Flow / 由 Flow 承载 | VL Workflow Engine / DAG (creativity in nodes, determinism in edges) |
| Accumulate & bank / 沉淀与存算力 | Component Factory (store the token-compute, reuse) |
| Kept in-house / 留在企业内 | Local-first (offline Lint/Compile/codegen; export the source = 0 lock-in) |
| Maintain visually / 可视化维护 | Everything graphical — Map / DAG / ER, code ↔ graph 1:1 |
| Run as an Agent App / 以 Agent App 运行 | `.vflow` + `app` block = installable Agent App (install/pause/resume/audit) |
| Governed & auditable / 治理与可审计 | Resource Center (review-gated lifecycle) · SQLite control-plane ledger |

## Guardrails honoured / 守住的红线

- `.vflow` integrity = **sha256 checksums = tamper-evident**, never "signed"/"encrypted".
- An Agent App = a `.vflow` **with an `app` block**; `.vapp` is **not** a live separate file type.
- VL Agent is **local-first, not SaaS** — this is *why* assets stay inside the enterprise.
- "Maintain visually" = the shipped graphical projection + Agent-App lifecycle + Resource-Center review; **not** the design-frozen contract-authoring IDE (no drag-to-wire authoring claim).
- "150+" workflows (never "113"); ÷10/×10/10× are positioning, not audited benchmarks; no finished-marketplace/resource-API claim.
- Public GitHub materials contain documentation, decks, video, screenshots, tutorials, and installers only. Product source code, VL parser implementation, and internal workflow source stay private.
