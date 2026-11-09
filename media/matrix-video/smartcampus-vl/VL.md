# SmartCampus — VL Project

## Project Description
SmartCampus — Application project based on the bound VL syntax Resource Center mirror.

## VL Syntax Essentials
- File Types: .vx (App), .sc (Section), .cp (Component), .vs (Service), .vdb (Database), .vth (Theme)
- Indentation: consecutive hyphens (-), NOT spaces

## File Naming Conventions
- Theme file is always `Theme/Theme.vth` and uses the latest snapshot from Resource Center slug theme-default (SystemDoc key ThemeDefault mirror) unless the user explicitly asks for theme customization
- Database file is always `Database/SmartCampus.vdb`
- Service files: `Services/<DomainId>.vs`
- Component files: `ExtComponents/<ComponentId>.cp`
- Section files: `Sections/<SectionId>.sc`
- App files: `Apps/<AppId>.vx`

## Canonical Development Guide (SystemDoc key DevGuide / reserved path 11)
- Treat SystemDoc key `DevGuide` (reserved path 11) as the authoritative VL project workflow guide
- Use the currently selected workspace; new projects default to the current user's Documents/VLProjects directory. Projects should include at least `Config/`, `Apps/`, `Sections/`, and `.vl-code/project.json`
- Store the remote project `gid` only through VLC's managed `.vl-code/project.json` fields (`groupId` + `gidBinding`); do not hand-edit it. Legacy `Config/ProjectConfig` is migrated away when seen
- Do not use ZIP upload. Sync source files through Workspace APIs such as `writeFiles`; for full deploys, use `listFile` + `deleteFiles` before rewriting everything
- After every write, run `lintPjt` until `summary.errors === 0`, then call `parsevl`
- Minimal parser call: `{"action":"parsePjt","targetGid":<gid>,"download":true}`; do not pass `file` or `projectName` unless explicitly required
- `targetGid` and Workspace `gid` must be integers
- Use the installed local Lint, Compile and Preview by default; local development needs no cloud account, GID or AI connection. Use cloud compilation only when explicitly selected
- App preview roots come from `previewUrl`; concrete pages append `/route/{path}`
- Cloud Workspace / parser requests use the configured authentication; local Lint, Compile and Preview do not require cloud credentials. Never hardcode or commit tokens


## Generation Workflow Rules
- After metadata/spec files are ready, .vs/.cp/.sc/.vx generation should be parallel and file-level decoupled
- Every metadata object must include its final `filePath`; downstream agents must not infer names ad hoc
- Do not create extra theme variants or use `main.vdb` / `Theme-Default.vth`

## Project Custom Instructions
[Add project-specific AI instructions here]
