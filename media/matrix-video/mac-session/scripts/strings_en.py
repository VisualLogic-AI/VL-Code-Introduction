"""English on-screen strings for render_shots.py (VLANG=en)."""

SCENE_TITLES = {
    "s01": "", "s02": "Why Matrix", "s03": "Core concepts: Brain · Hand · Workspace",
    "s04": "Step 1 · Matrix desktop app", "s05": "Step 2 · Sign in and Pool", "s06": "Step 3 · Device and Workspace",
    "s07": "Step 4 · Create a task in the Assistant", "s08": "Step 5 · Run canvas and teamwork",
    "s09": "Step 6 · Terminal, files and delivery", "s10": "Step 7 · Stop, waiting and failures",
    "s11": "Step 8 · Organizations and access", "s12": "Remote development: Brain in the cloud, Hand on the device", "s13": "",
}

DESKTOP_CAPTIONS = [
    "Overview: account, device and gateway status", "Account: sign-in and session",
    "Device & Gateway: bind the device, manage Workspaces", "AI Resources: resources found on this Mac",
    "Core Modules: VL Code, Factory, VL-Base",
]
DESKTOP_URL = "Matrix desktop · live capture"

WEB = {
    "s05": [("03-sign-in", "Sign in to Matrix in the browser"), ("02-pool-populated", "Pool: authorized resources, prices and remaining quota"), ("05-pool-resource-details", "Resource details and usage")],
    "s06": [("13-task-home-workspace-gallery", "Task: device bar on top, Workspace tree on the left"), ("14-add-workspace-dialog", "Add Workspace: pick a project folder on the device"), ("16-task-line-created", "Create a task line")],
    "s07": [("18-new-task-draft-advanced", "Assistant task draft: goal, collaboration and workflow"), ("21-task-models-panel", "Choose model resources, then Send and start")],
    "s08": [("42-task-running", "Run canvas: real execution status"), ("46-task-team", "Team task: the leader assigns, workers execute"), ("58-running-execution-context", "Execution context: model, device and Workspace")],
    "s09": [("26-task-terminal", "Open a terminal in the same task"), ("27-task-files", "Browse files the task produced"), ("44-task-delivered", "Delivered: traceable, verifiable results")],
    "s10": [("23-stop-inline-confirm", "Stop a task: confirm exactly what stops"), ("57-task-waiting-for-you", "Waiting for you: clear, visible states"), ("43-task-failed", "Failure reason, with continue / retry paths")],
    "s11": [("30-settings-org-created", "Settings → Organizations: create an organization"), ("32-org-invite-created", "Invite members"), ("33-org-manage-pool-access-invites", "Grant the company pool and access")],
}
S12_CAPTION = "Settings → Devices: manage bound devices"


def slides(chrome):
    return {
        ("s01", 1): chrome("s01") + '<div class="center"><h1>Matrix</h1><div class="sub">People, AI resources and authorized devices,<br>working together on verifiable software tasks</div><div class="tag">PRODUCT OVERVIEW · WALKTHROUGH</div></div>',
        ("s02", 1): chrome("s02") + '<div class="center"><div class="cols">'
        '<div class="list bad"><h3>Before: scattered</h3><ul><li>Many <b>CLIs</b>, <b>APIs</b> and accounts</li><li>Many <b>devices</b> and project folders</li><li>What works? How much quota is left?</li><li>What is running? Is the result real?</li></ul></div>'
        '<div class="arrow">→</div>'
        '<div class="list good"><h3>Matrix: unified, verifiable</h3><ul><li><b>Pool</b>: authorized resources and quota</li><li><b>Task</b>: work, execution and outputs</li><li><b>Assistant</b>: context-aware collaboration</li><li>Every run traced to model, device and Workspace</li></ul></div>'
        '</div></div>',
        ("s03", 1): chrome("s03") + '<div class="center"><div class="cards">'
        '<div class="card"><div class="k">BRAIN</div><h3>Thinks and plans</h3><p>Can run in the cloud.<br>Understands the goal,<br>breaks down the work.</p></div><div class="arrow">⇄</div>'
        '<div class="card"><div class="k">HAND</div><h3>Your device</h3><p>Your own computer<br>or server. Performs real<br>file and tool operations.</p></div><div class="arrow">→</div>'
        '<div class="card"><div class="k">WORKSPACE</div><h3>Authorized project</h3><p>A project folder you<br>explicitly authorize.<br>AI works only inside it.</p></div>'
        '</div><div class="note">Permission to use a model ≠ permission to access device files</div></div>',
        ("s12", 1): chrome("s12") + '<div class="center"><div class="cards">'
        '<div class="card"><div class="k">BROWSER</div><h3>Pick a device</h3><p>Open Matrix anywhere,<br>choose another authorized<br>device and Workspace.</p></div><div class="arrow">→</div>'
        '<div class="card"><div class="k">BRAIN · CLOUD</div><h3>Plans and decides</h3><p>Understands the goal and<br>issues file and command<br>actions via a restricted channel.</p></div><div class="arrow">→</div>'
        '<div class="card"><div class="k">HAND · PROJECT DEVICE</div><h3>Real execution</h3><p>Reads and writes files,<br>runs commands in the<br>Workspace; results return.</p></div>'
        '</div></div>',
        ("s13", 1): chrome("s13") + '<div class="center"><h1 style="font-size:96px">Three steps</h1><div class="steps">'
        '<div class="step"><div class="n">1</div><div class="t">Sign in</div><div class="d">Sign in on the web; bind this device in the desktop app</div></div>'
        '<div class="step"><div class="n">2</div><div class="t">Add a Workspace</div><div class="d">Pick a project folder on the device</div></div>'
        '<div class="step"><div class="n">3</div><div class="t">Describe the goal</div><div class="d">Send and start in the Assistant</div></div>'
        '</div><div class="sub" style="margin-top:60px">Matrix · every execution, on the record</div></div>',
    }


SCENE_TITLES.update({"s08b": "DAG orchestration · static workflows and dynamic planning", "s08c": "DAG execution, step by step",
                     "s11b": "VLC IDE · visual development workbench", "s11c": "VLC IDE · AI assistant, compile, preview, publish"})
WEB.update({
    "s08b": [("m-06-06-workflow-three-choices", "Workflow: none / static / dynamic planning"), ("m-07-07-static-workflow-catalog", "Static workflow catalog"), ("m-09-10-dynamic-dag", "Dynamic DAG: new steps, reasons and scope visible"), ("m-35-04c-workflow-call-selected", "A step calls a sub-workflow or AI team")],
    "s11b": [("b-09-editor-wide-1680-header", "VLC IDE editor: project, file tree, many views"), ("b-17-tab-visual", "Visual: edit the UI visually"), ("b-18-tab-logic", "Logic: visual business logic"), ("b-14-tab-flow", "Flow view"), ("b-71-votemini-tab-er", "ER: data model diagram"), ("b-72-votemini-tab-db", "DB: database tables")],
    "s11c": [("b-after-assistant-1680", "Built-in AI assistant"), ("b-78-assistant-goal-build-chip", "New app, workflow, component, service"), ("b-12-compile-running", "Check and compile in one click"), ("b-16-tab-preview", "Preview the result"), ("b-after-publish-bound-confirm", "Publish to the cloud"), ("b-60-mode-flows", "Library: flows, docs, skills, tools")],
})
FLOW_REAL = [("f-20-run-executing", "Real workflow canvas: running"), ("f-22-run-after-14s", "Nodes complete; a human-approval node waits"), ("f-24-node-detail-after-run", "Open a node: inputs, outputs, run details"), ("f-26-run-finished", "Run finished: done 11/11"), ("f-28-artifacts-after-run", "All run artifacts listed")]
DAG = {
    "label": "Execution walkthrough (illustration)",
    "nodes": {"goal": "Goal", "plan": "Leader plan", "fe": "Frontend", "be": "Backend", "test": "Test", "fix": "Fix (added)", "review": "Human approval", "deliver": "Deliver"},
    "steps": ["① The leader turns the goal into a plan", "② Dependencies ready: frontend and backend run in parallel", "③ Tests run",
              "④ Tests find a problem → a Fix step is added dynamically", "⑤ Human approval: waiting for you", "⑥ Delivered: verifiable result, resources returned, usage settled"],
    "legend": {"pending": "Pending", "running": "Running", "done": "Done", "wait": "Waiting for you", "new": "Added dynamically"},
    "reason": "Reason: 2 tests failed · Scope: backend",
    "hud": ["done 1/7", "done 1/7 · parallel 2", "done 3/7", "done 4/8 · graph changed +1", "done 7/8", "done 8/8 · delivered"],
}
