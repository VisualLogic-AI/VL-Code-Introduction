# Install And Use VLCode

This guide is for the public desktop build. VLCode is a local-first IDE for generating, editing, validating, and deploying VL enterprise applications.

## 1. Download

| Platform | Build | Link |
|---|---:|---|
| macOS Apple Silicon | `v1.230.1` | [VLCode-Lite-1.230.1-arm64.dmg](https://github.com/VisualLogic-AI/vlcode-releases/releases/download/v1.230.1/VLCode-Lite-1.230.1-arm64.dmg) |
| macOS Apple Silicon ZIP | `v1.230.1` | [VLCode-Lite-1.230.1-arm64.zip](https://github.com/VisualLogic-AI/vlcode-releases/releases/download/v1.230.1/VLCode-Lite-1.230.1-arm64.zip) |
| Windows x64 | `v1.230.0` | [VLCode-Lite-1.230.0-x64.exe](https://github.com/VisualLogic-AI/vlcode-releases/releases/download/v1.230.0/VLCode-Lite-1.230.0-x64.exe) |

All release assets are published from [VisualLogic-AI/vlcode-releases](https://github.com/VisualLogic-AI/vlcode-releases/releases).

## 2. Install

### macOS

1. Download the DMG.
2. Open it and drag **VLCode Lite** into **Applications**.
3. Launch **VLCode Lite** from Applications.
4. If macOS asks for confirmation because the app was downloaded from the internet, choose **Open**.

### Windows

1. Download the EXE installer.
2. Run the installer.
3. Keep the default installation path unless your organization has a standard tools directory.
4. Launch **VLCode Lite** from the Start menu or desktop shortcut.

The Windows `v1.230.0` installer is Authenticode-signed by `VisualLogicAI, LLC`.

## 3. First Run

1. Open or create a local workspace, usually under `~/Documents/VLProjects/<ProjectName>`.
2. Open **Settings** and confirm your model provider configuration.
3. Use the AI Assistant panel as the main command surface.
4. Ask for a small app first, such as a team task board or approval tracker.
5. Let the workflow write VL files, then inspect the generated project in the file tree.

## 4. Daily Workflow

Use this loop for normal project work:

1. **Describe the goal** in AI Chat.
2. **Run a workflow** such as code generation, add-page, add-service, feature adjust, or repair.
3. **Review the Detail Log** for node progress, tool calls, file writes, validation, and errors.
4. **Inspect generated VL** in Code, Visual, Map, Flow, Data, and Preview modes.
5. **Validate in order**: Lint first, then Compile, then Preview.
6. **Export or deploy** only after validation is clean.

## 5. Key Screens

| Screen | What It Is For |
|---|---|
| AI Chat | Goals, workflow control, final summaries, human decisions |
| Detail Log | Full verbose run trace: nodes, tools, file writes, validation |
| Code | VL source files: apps, sections, services, data, themes |
| Visual | Visual inspection and component structure |
| Map | Application architecture and page relationships |
| Flow | DAG workflow execution and debugging |
| Preview | Run the generated app and verify user-facing behavior |

## 6. What To Build First

Try one of these starter prompts:

```text
Build a TeamPM task board. Tasks have title, assignee, due date, and status.
Show Todo, In Progress, and Done columns. Add a form to create a task.
```

```text
Build an approval tracker for purchase requests. Include requester, amount,
department, approval status, approver comments, and a dashboard by status.
```

Keep the first run scoped. After it works, ask VLCode to add pages, services, fields, and validation rules incrementally.

## 7. Validation Discipline

- Use **Lint** for fast syntax checks.
- Use **Compile** after lint is clean.
- Use **Preview** to test user workflows.
- Keep screenshots or logs for important errors.
- Prefer minimal repair requests: describe the specific failing page, action, or validation error.

## 8. More Tutorials

- [VLCode Tutorial PDF](tutorials/VLCode-Tutorial-EN.pdf)
- [VL Agent Tutorial PDF](tutorials/VL-Agent-Tutorial-EN.pdf)
- [DAG Harness video](../media/VisualLogic-DAG-Harness-Video.mp4)

## 9. Source Code Policy

VLCode and the VL parser are commercial/private code. Public GitHub repositories contain product materials, installers, tutorials, videos, screenshots, and concept documents only.
