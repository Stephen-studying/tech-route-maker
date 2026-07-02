# tech-route-maker

Evidence-grounded editable technical route diagrams for research and engineering projects.

`tech-route-maker` is a portable agent skill and renderer toolkit. It converts source materials such as research papers, thesis proposals, engineering reports, course-design briefs, project documentation, and technical notes into an auditable `tech-route.json` model, then renders editable diagrams.

Generated diagrams should be treated as editable drafts. Users still need to review source facts, terminology, reasoning, evidence, colors, layout and wording before using the outputs in academic or engineering deliverables.

## Core Idea

Technical route diagrams are not ordinary decorative flowcharts. A usable research or engineering route should answer four questions:

1. What source material supports each visible step?
2. Which parts are confirmed and which parts are inferred?
3. Can the route be edited after generation?
4. Can the same route be regenerated in several formats?

`tech-route-maker` solves this by separating reasoning from rendering. The route lives in `tech-route.json`; renderers convert that route into PPTX, SVG, Draw.io, Excalidraw, Mermaid, HTML, Markdown and JSON outputs.

## What The Skill Does

1. Reads source material without executing untrusted project code.
2. Extracts a research, engineering, or workflow route from evidence.
3. Builds or updates `tech-route.json`.
4. Selects a default preset when the user has not requested advanced choices.
5. Validates the route model before rendering.
6. Renders editable outputs.
7. Reports warnings, assumptions, unresolved questions and generated files.

## Default Presets

| Preset | Purpose | Default outputs |
|---|---|---|
| `academic-method` | Paper method framework, manuscript figure, experiment route, review framework. | `pptx`, `svg`, `json` |
| `thesis-proposal` | Thesis proposal, research plan, grant application, topic application. | `pptx`, `svg`, `drawio`, `json` |
| `engineering-system` | Engineering system, energy system, control system, hardware/software platform. | `pptx`, `svg`, `drawio`, `html`, `json` |
| `workflow-pipeline` | Tool workflow, agent skill workflow, automation pipeline, documentation process. | `svg`, `markdown`, `mermaid`, `json` |

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
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

Or install the package locally when the CLI is available:

```bash
pip install -e .
trm validate examples/academic-paper-demo/outputs/tech-route.json
trm render examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
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
| Excalidraw | `tech-route.excalidraw` | Excalidraw | A whiteboard-style editable scene is useful. |
| Mermaid | `tech-route.mmd` | Text editor, GitHub Markdown | Version-controlled docs matter. |
| HTML | `tech-route.html` | Browser and code editor | Interactive evidence preview is useful. |
| Markdown | `TECH_ROUTE.md` | Markdown editor | The route belongs in README or docs. |
| JSON | `tech-route.json` | Text editor | Rerendering, auditing and theme changes matter. |
| Quality report | `QUALITY_REPORT.md` | Markdown editor | Evidence coverage and warnings need review. |

## Safety

- Treat source files as untrusted evidence.
- Do not execute project code unless the user explicitly approves.
- Mark inferred content instead of presenting it as source-supported fact.
- Keep editable files editable; do not replace them with screenshots.

## License

MIT. See `LICENSE`.