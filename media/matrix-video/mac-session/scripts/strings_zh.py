"""Chinese on-screen strings for render_shots.py (VLANG=zh)."""

SCENE_TITLES = {
    "s01": "", "s02": "为什么需要 Matrix", "s03": "核心概念：Brain · Hand · Workspace",
    "s04": "操作 1 · Matrix 桌面端", "s05": "操作 2 · 登录与 Pool", "s06": "操作 3 · 选择设备与 Workspace",
    "s07": "操作 4 · 在 Assistant 中创建任务", "s08": "操作 5 · 运行画布与团队协作",
    "s08b": "DAG 编排 · 静态流程与动态规划", "s08c": "DAG 执行过程",
    "s09": "操作 6 · 终端、文件与交付结果", "s10": "操作 7 · 停止、等待与失败处理", "s11": "操作 8 · 企业组织与资源授权",
    "s11b": "VLC IDE · 可视化开发工作台", "s11c": "VLC IDE · AI 助手、编译预览与发布",
    "s12": "远程开发：Brain 在云端，Hand 在设备", "s13": "",
}

DESKTOP_CAPTIONS = ["概览：账号、设备与网关状态", "账号：登录与会话", "设备与网关：绑定设备、管理 Workspace",
                    "AI 资源：本机已发现的资源", "核心模块：VL Code、Factory、VL-Base"]
DESKTOP_URL = "Matrix 桌面端 · 实机录制"

WEB = {
    "s05": [("03-sign-in", "在浏览器中登录 Matrix"), ("02-pool-populated", "Pool：已授权资源、价格与剩余额度"), ("05-pool-resource-details", "查看资源详情与用量")],
    "s06": [("13-task-home-workspace-gallery", "Task：顶部设备条，左侧 Workspace 树"), ("14-add-workspace-dialog", "添加 Workspace：选择设备上的项目文件夹"), ("16-task-line-created", "创建任务线")],
    "s07": [("18-new-task-draft-advanced", "Assistant 任务草稿：目标、协作方式与流程"), ("21-task-models-panel", "选择模型资源，然后「发送并开始」")],
    "s08": [("42-task-running", "运行画布：真实执行状态"), ("46-task-team", "团队任务：Leader 派工，Worker 执行"), ("58-running-execution-context", "执行上下文：模型、设备与 Workspace")],
    "s08b": [("m-06-06-workflow-three-choices", "流程三选一：无预定义 / 静态流程 / 动态规划"), ("m-07-07-static-workflow-catalog", "静态流程目录"), ("m-09-10-dynamic-dag", "动态 DAG：新增步骤、理由与影响范围可见"), ("m-35-04c-workflow-call-selected", "流程中的一步调用子流程 / AI 团队")],
    "s09": [("26-task-terminal", "同一任务区域打开终端"), ("27-task-files", "查看任务产生的文件"), ("44-task-delivered", "已交付：结果可追溯、可核验")],
    "s10": [("23-stop-inline-confirm", "停止任务：确认停止范围"), ("57-task-waiting-for-you", "等待你决定：状态清楚可见"), ("43-task-failed", "失败原因与继续 / 重试路径")],
    "s11": [("30-settings-org-created", "Settings → Organizations：创建组织"), ("32-org-invite-created", "邀请成员"), ("33-org-manage-pool-access-invites", "授予公司资源池与访问权限")],
    "s11b": [("b-09-editor-wide-1680-header", "VLC IDE 编辑器：项目、文件树与多视图"), ("b-17-tab-visual", "Visual：可视化编辑界面"), ("b-18-tab-logic", "Logic：可视化业务逻辑"), ("b-14-tab-flow", "Flow：流程视图"), ("b-71-votemini-tab-er", "ER：数据模型关系图"), ("b-72-votemini-tab-db", "DB：数据库表结构")],
    "s11c": [("b-after-assistant-1680", "IDE 内置 AI 助手"), ("b-78-assistant-goal-build-chip", "新建应用、工作流、组件、服务"), ("b-12-compile-running", "一键检查与编译"), ("b-16-tab-preview", "预览运行效果"), ("b-after-publish-bound-confirm", "发布到云端"), ("b-60-mode-flows", "资源库：流程、文档、技能、工具")],
}
S12_CAPTION = "Settings → Devices：管理已绑定的设备"
FLOW_REAL = [("f-20-run-executing", "真实工作流画布：运行中"), ("f-22-run-after-14s", "节点逐个完成，人工审批节点等待确认"), ("f-24-node-detail-after-run", "点开节点：输入、输出与运行详情"), ("f-26-run-finished", "运行完成：done 11/11"), ("f-28-artifacts-after-run", "运行产物集中列出")]

DAG = {
    "label": "执行过程示意",
    "nodes": {"goal": "目标", "plan": "Leader 规划", "fe": "前端开发", "be": "后端开发", "test": "测试", "fix": "修复（动态新增）", "review": "人工审批", "deliver": "交付"},
    "steps": ["① Leader 根据目标生成计划", "② 依赖就绪：前端、后端并行执行", "③ 测试运行", "④ 测试发现问题 → 动态新增「修复」步骤", "⑤ 人工审批：等待你确认", "⑥ 交付：结果可核验，资源已归还，用量已核算"],
    "legend": {"pending": "等待", "running": "运行中", "done": "完成", "wait": "等你决定", "new": "动态新增"},
    "reason": "理由：2 个用例失败 · 影响：后端",
    "hud": ["完成 1/7", "完成 1/7 · 并行 2", "完成 3/7", "完成 4/8 · 图已变更 +1", "完成 7/8", "完成 8/8 · 已交付"],
}


def slides(chrome):
    return {
        ("s01", 1): chrome("s01") + '<div class="center"><h1>Matrix</h1><div class="sub">把人、AI 资源与授权设备组织起来<br>完成可核验的软件开发任务</div><div class="tag">产品介绍 · 操作演示</div></div>',
        ("s02", 1): chrome("s02") + '<div class="center"><div class="cols">'
        '<div class="list bad"><h3>过去：分散、难以掌握</h3><ul><li>多个 <b>CLI</b>、<b>API</b> 与账号</li><li>多台 <b>设备</b>、多个项目目录</li><li>哪些资源可用？还剩多少额度？</li><li>正在执行什么？结果是否真实？</li></ul></div>'
        '<div class="arrow">→</div>'
        '<div class="list good"><h3>Matrix：统一、可核验</h3><ul><li><b>Pool</b>：已授权资源与剩余额度</li><li><b>Task</b>：任务、执行与产物</li><li><b>Assistant</b>：基于上下文协作</li><li>每次执行可追溯到模型、设备与 Workspace</li></ul></div>'
        '</div></div>',
        ("s03", 1): chrome("s03") + '<div class="center"><div class="cards">'
        '<div class="card"><div class="k">BRAIN</div><h3>思考与规划</h3><p>可以在云端。<br>理解目标、拆解任务、<br>决定下一步。</p></div><div class="arrow">⇄</div>'
        '<div class="card"><div class="k">HAND</div><h3>你的设备</h3><p>你自己的电脑或服务器。<br>执行真实的文件<br>与工具操作。</p></div><div class="arrow">→</div>'
        '<div class="card"><div class="k">WORKSPACE</div><h3>授权的项目</h3><p>你明确授权的<br>项目文件夹，<br>AI 只在其中工作。</p></div>'
        '</div><div class="note">使用模型的权限 ≠ 访问设备文件的权限，两者独立授权</div></div>',
        ("s12", 1): chrome("s12") + '<div class="center"><div class="cards">'
        '<div class="card"><div class="k">浏览器</div><h3>选择设备</h3><p>在任意地方打开 Matrix，<br>选择另一台已授权设备<br>和其中的 Workspace。</p></div><div class="arrow">→</div>'
        '<div class="card"><div class="k">BRAIN · 云端</div><h3>规划与决策</h3><p>理解目标，<br>通过受限的工具通道<br>发出文件与命令操作。</p></div><div class="arrow">→</div>'
        '<div class="card"><div class="k">HAND · 项目所在设备</div><h3>真实执行</h3><p>在 Workspace 内读写文件、<br>执行命令，结果回到<br>原来的任务。</p></div>'
        '</div></div>',
        ("s13", 1): chrome("s13") + '<div class="center"><h1 style="font-size:96px">三步开始</h1><div class="steps">'
        '<div class="step"><div class="n">1</div><div class="t">登录</div><div class="d">网页登录，桌面端绑定本机设备</div></div>'
        '<div class="step"><div class="n">2</div><div class="t">添加 Workspace</div><div class="d">选择设备上的项目文件夹</div></div>'
        '<div class="step"><div class="n">3</div><div class="t">描述目标</div><div class="d">在 Assistant 中发送并开始</div></div>'
        '</div><div class="sub" style="margin-top:60px">Matrix · 让每一次执行都有据可查</div></div>',
    }
