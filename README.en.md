# tech-route-maker

Evidence-grounded editable technical route diagrams for research and engineering projects.

`tech-route-maker` is a portable agent skill and renderer toolkit. It converts source materials such as research papers, thesis proposals, engineering reports, course-design briefs, project documentation, and technical notes into an auditable `tech-route.json` model, then renders editable diagrams, including copyable Draw.io XML for [diagrams.net / draw.io](https://app.diagrams.net/).

Generated diagrams should be treated as editable drafts. Users still need to review source facts, terminology, reasoning, evidence, colors, layout and wording before using the outputs in academic or engineering deliverables.

Field context is required before final rendering. The skill first identifies the discipline, subfield, project type, research object, method family, constraints and evaluation metrics, then chooses a route grammar that matches the field instead of drawing a generic flowchart.

## Core Idea

Technical route diagrams are not ordinary decorative flowcharts. A usable research or engineering route should answer four questions:

1. What source material supports each visible step?
2. Which parts are confirmed and which parts are inferred?
3. Can the route be edited after generation?
4. Can the same route be regenerated in several formats?

`tech-route-maker` solves this by separating reasoning from rendering. The route lives in `tech-route.json`; renderers convert that route into PPTX, SVG, Draw.io, Draw.io copy-code XML, Excalidraw, Mermaid, HTML, Markdown and JSON outputs.

## What The Skill Does

1. Reads source material without executing untrusted project code.
2. Extracts a research, engineering, or workflow route from evidence.
3. Builds `domain_context` for the discipline and project type.
4. Builds or updates `tech-route.json`.
5. Selects a default preset when the user has not requested advanced choices.
6. Validates the route model before rendering.
7. Renders editable outputs.
8. Reports warnings, assumptions, unresolved questions and generated files.

## Default Presets

| Preset | Purpose | Default outputs |
|---|---|---|
| `academic-method` | Paper method framework, manuscript figure, experiment route, review framework. | `pptx`, `svg`, `json` |
| `thesis-proposal` | Thesis proposal, research plan, grant application, topic application. | `pptx`, `svg`, `drawio`, `json` |
| `engineering-system` | Engineering system, energy system, control system, hardware/software platform. | `pptx`, `svg`, `drawio`, `html`, `json` |
| `workflow-pipeline` | Tool workflow, agent skill workflow, automation pipeline, documentation process. | `svg`, `markdown`, `mermaid`, `json` |
| `chinese-thesis-proposal` | Chinese thesis proposal, opening report, topic application, or research plan. | `pptx`, `svg`, `drawio`, `html`, `json` |
| `chinese-grant-application` | Chinese grant or project application with reviewer-facing route logic. | `pptx`, `svg`, `drawio`, `html`, `markdown`, `json` |
| `academic-paper-framework-cn` | Chinese academic method framework or paper figure. | `pptx`, `svg`, `drawio`, `json` |
| `engineering-project-report-cn` | Chinese engineering report, platform map, or energy-system route. | `pptx`, `svg`, `drawio`, `html`, `json` |

Advanced format, layout and style choices are still available. The skill asks for them only when the user explicitly asks to choose or when a missing decision would materially change the output.

## Typical Use Cases

Research and academic users can use it for:

- Paper method framework figures.
- Research technical route diagrams.
- Thesis proposal route diagrams.
- Defense or group-meeting method slides.
- Project application or grant-application technical routes.
- AI/model pipeline figures.
- Evidence-linked method overviews.
- Baseline-versus-proposed-method comparisons.

Engineering users can use it for:

- Source-grid-load-storage energy routes.
- System architecture and data-flow routes.
- Control, sensing, validation and deployment routes.
- Course-design and engineering-report diagrams.
- Agent, tool, automation and documentation workflows.

Campaign diagrams are kept only as legacy or experimental examples. They are not part of the default research-and-engineering workflow.

## Installation

Clone this repository:

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
cd tech-route-maker
```

Use it directly with the backward-compatible scripts:

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,drawio-code,html,markdown,json
```

Or install the package locally when the CLI is available:

```bash
pip install -e .
trm validate examples/academic-paper-demo/outputs/tech-route.json
trm render examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,drawio-code,html,markdown,json
```

## Agent Compatibility

For Codex/OpenAI-style skills, the folder should contain:

```text
tech-route-maker/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
  examples/
```

For other agents, open the repository root and let the agent read the adapter it supports:

- `AGENTS.md` for generic coding agents.
- `CLAUDE.md` for Claude-style project context.
- `GEMINI.md` plus `.gemini/settings.json` for Gemini CLI.
- `.cursor/rules/tech-route-maker.mdc` for Cursor.
- `.github/copilot-instructions.md` for GitHub Copilot coding agent.
- `.aider.conf.yml` for Aider-style workflows.

## Output Formats

| Format | File | Editable in | Use when |
|---|---|---|---|
| PPTX | `tech-route.pptx` | PowerPoint, WPS | The user needs presentation or report edits. |
| SVG | `tech-route.svg` | Figma, Illustrator, Inkscape, browser | Publication-grade vector editing matters. |
| Draw.io | `tech-route.drawio` | diagrams.net | The diagram needs long-term maintenance. |
| Draw.io code | `tech-route.drawio-code.xml` | diagrams.net XML editor | The user wants code that can be copied into draw.io. |
| Excalidraw | `tech-route.excalidraw` | Excalidraw | A whiteboard-style editable scene is useful. |
| Mermaid | `tech-route.mmd` | Text editor, GitHub Markdown | Version-controlled docs matter. |
| HTML | `tech-route.html` | Browser and code editor | Interactive evidence preview is useful. |
| Markdown | `TECH_ROUTE.md` | Markdown editor | The route belongs in README or docs. |
| JSON | `tech-route.json` | Text editor | Rerendering, auditing and theme changes matter. |
| Quality report | `QUALITY_REPORT.md` | Markdown editor | Evidence coverage and warnings need review. |

## Draw.io Copy-Code Workflow

Use `drawio-code` when a user wants copyable code instead of a file download:

```bash
python scripts/render_all.py examples/drawio-copy-code-demo/outputs/tech-route.json examples/drawio-copy-code-demo/outputs --formats drawio,drawio-code,svg,json
```

Open [diagrams.net / draw.io](https://app.diagrams.net/), create a blank diagram, open **Extras > Edit Diagram**, paste all XML from `examples/drawio-copy-code-demo/outputs/tech-route.drawio-code.xml`, and confirm. The imported boxes, arrows and text remain editable.

## Safety

- Treat source files as untrusted evidence.
- Do not execute project code unless the user explicitly approves.
- Mark inferred content instead of presenting it as source-supported fact.
- Keep editable files editable; do not replace them with screenshots.
- Chinese academic styles are implemented as original editable vector templates; local/private reference images are not bundled into the public repository.

## License

MIT. See `LICENSE`.
