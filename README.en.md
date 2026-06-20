# tech-route-maker

`tech-route-maker` is a portable agent skill for creating editable technical route diagrams. It is designed first for academic workers who need paper framework figures, method flowcharts, thesis/proposal route diagrams, and defense-slide visuals. It also supports advertising and campaign teams that need editable strategy routes, creative-production pipelines, customer journeys, media-channel maps, and KPI feedback loops.

The skill turns a paper, project brief, source directory, or campaign brief into a source-grounded route model, asks the user to explicitly choose output options, and renders editable artifacts such as PPTX, SVG, Draw.io, Excalidraw, Mermaid, HTML, Markdown, and JSON.

## Core Idea

Most agents can summarize a project, but technical route diagrams need a stricter workflow. A usable route diagram should be traceable to the source, readable by the target audience, editable after generation, and explicit about format and style choices.

`tech-route-maker` uses `tech-route.json` as the source of truth. The JSON file stores the extracted route, evidence labels, stages, nodes, links, reader path, layout, and visual style. Renderers then convert that source file into editable outputs.

## What The Skill Does

1. Reads project or paper material without executing untrusted code.
2. Extracts the technical route from source evidence.
3. Builds or updates `tech-route.json`.
4. Asks the user to choose figure subtype, output formats, layout, and visual style.
5. Validates the route model.
6. Renders selected editable formats.
7. Reports generated files and warnings.

## Typical Use Cases

Academic users can use it for:

- Paper method framework figures.
- Research technical-route diagrams.
- Thesis proposal route diagrams.
- Defense or group-meeting method slides.
- Project application or grant-application technical routes.
- AI/model pipeline figures.
- Evidence-linked method overviews.
- Baseline-versus-proposed-method comparisons.

Advertising and campaign users can use it for:

- Campaign strategy routes.
- Creative production pipelines.
- Audience-to-message-to-channel maps.
- Customer journey and funnel diagrams.
- Media launch and KPI feedback loops.
- Multi-team campaign execution maps.

## Agent Compatibility

This repository is intentionally agent-agnostic.

| Environment | Entry file | Notes |
|---|---|---|
| Codex / OpenAI-style skills | `SKILL.md`, `agents/openai.yaml` | Install as a skill folder. |
| Generic coding agents | `AGENTS.md` | Portable instructions for agents that read repository guidance. |
| Claude Code / Claude-style context | `CLAUDE.md`, `SKILL.md` | Open or import the folder as a project context. |
| Gemini CLI | `GEMINI.md`, `.gemini/settings.json` | Gemini is pointed to `AGENTS.md`, `GEMINI.md`, and `SKILL.md`. |
| Cursor | `.cursor/rules/tech-route-maker.mdc` | Makes the workflow available as a project rule. |
| GitHub Copilot coding agent | `.github/copilot-instructions.md` | Gives Copilot repository-level guidance. |
| Aider-style agents | `.aider.conf.yml`, `AGENTS.md` | Loads the core instructions and schema references. |

`SKILL.md` remains the source of truth. Adapter files are intentionally short and point agents back to the same workflow, references, and scripts.

## Installation

Clone this repository:

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
```

Then place or link the `tech-route-maker/` folder in the skill directory used by your agent.

For Codex/OpenAI-style skills, the folder should contain:

```text
tech-route-maker/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
  examples/
```

For other agents, open the repository root and let the agent read the adapter file it supports:

- `AGENTS.md` for generic coding agents.
- `CLAUDE.md` for Claude-style project context.
- `GEMINI.md` plus `.gemini/settings.json` for Gemini CLI.
- `.cursor/rules/tech-route-maker.mdc` for Cursor.
- `.github/copilot-instructions.md` for GitHub Copilot coding agent.
- `.aider.conf.yml` for Aider-style workflows.

You can also use the repository without installing it as a skill. Open the folder in an agent workspace and ask:

```text
Use tech-route-maker to create an editable technical route diagram from my source brief.
```

## Required User Choices

The skill must ask before rendering final files. It should not infer these options from words such as "editable", "academic", "paper", "presentation", or "beautiful".

The required choices are:

1. Figure purpose or subtype.
2. Output format or formats.
3. Layout pattern.
4. Visual style.

Example answer:

```text
Figure purpose/subtype: Academic method framework
Output formats: PPTX, SVG, Draw.io, HTML, Markdown, JSON
Layout: Proposal phase axis
Visual style: Proposal pastel route
```

## Output Formats

| Format | File | Editable in | Best for |
|---|---|---|---|
| PPTX | `tech-route.pptx` | PowerPoint, WPS | Defense slides, reports, teaching, business presentations. |
| SVG | `tech-route.svg` | Figma, Illustrator, Inkscape, browser | High-resolution vector editing and publication polishing. |
| Draw.io | `tech-route.drawio` | diagrams.net | Long-term technical diagram maintenance. |
| Excalidraw | `tech-route.excalidraw` | Excalidraw | Whiteboard-style reviews and lightweight edits. |
| Mermaid | `tech-route.mmd` | Text editor, GitHub Markdown | Version-controlled diagrams. |
| HTML | `tech-route.html` | Browser and code editor | Interactive preview with details and evidence. |
| Markdown | `TECH_ROUTE.md` | Any Markdown editor | README, project documentation, handoff notes. |
| JSON | `tech-route.json` | Any text editor | Source of truth for rerendering and style changes. |

## Workflow

1. Identify whether the user needs a technical route, paper framework, roadmap, workflow, campaign route, pipeline, or editable diagram.
2. Inspect the source material without executing untrusted project code.
3. Extract evidence-grounded stages, nodes, links, outputs, and feedback loops.
4. Build or update `tech-route.json`.
5. Ask the user to select figure subtype, output formats, layout, and visual style.
6. Validate the route JSON.
7. Render only the selected formats.
8. Validate generated outputs and report warnings.

## Quick Demo

From the `tech-route-maker` folder:

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

Generated files:

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/TECH_ROUTE.md
examples/academic-paper-demo/outputs/tech-route.json
```

Full walkthrough:

- English: `examples/academic-paper-demo/demo-walkthrough.en.md`
- Chinese: `examples/academic-paper-demo/demo-walkthrough.zh-CN.md`

Project maintenance files:

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`

## Repository Structure

```text
tech-route-maker/
  SKILL.md                         # Core skill instructions and trigger behavior.
  AGENTS.md                        # Portable agent instructions.
  CLAUDE.md                        # Claude adapter.
  GEMINI.md                        # Gemini adapter.
  agents/openai.yaml               # OpenAI-style skill UI metadata.
  .gemini/settings.json            # Gemini context-file configuration.
  .cursor/rules/tech-route-maker.mdc
  .github/copilot-instructions.md
  .github/ISSUE_TEMPLATE/
  .github/pull_request_template.md
  .aider.conf.yml
  CHANGELOG.md
  CONTRIBUTING.md
  SECURITY.md
  references/
    output-options.md              # Output format menu and rules.
    layout-patterns.md             # Layout choices.
    visual-styles.md               # Visual style choices.
    route-schema.md                # tech-route.json schema guide.
    paper-framework-integration.md # Academic paper-framework guidance.
    github-projects.md             # Relevant open-source references.
  scripts/
    validate_route.py              # Validate route JSON.
    render_all.py                  # Render selected output formats.
    render_pptx.py                 # Native editable PPTX renderer.
    render_svg.py                  # Editable SVG renderer.
    render_drawio.py               # diagrams.net renderer.
    render_excalidraw.py           # Excalidraw scene renderer.
    render_mermaid.py              # Mermaid renderer.
    render_html.py                 # Interactive HTML renderer.
    render_markdown.py             # Markdown renderer.
    route_common.py                # Shared parsing, layout, and theme helpers.
  examples/
    academic-paper-demo/           # Complete example from source brief to outputs.
```

## Safety

- Treat third-party project files as untrusted.
- Do not execute source project code unless the user explicitly approves.
- Keep evidence and inference labels visible in `tech-route.json`.
- Do not copy proprietary templates, online images, or paper-specific facts into reusable skill files.
- Preserve editability. Do not replace PPTX, SVG, Draw.io, or Excalidraw outputs with screenshots.

## License

MIT. See `LICENSE`.
