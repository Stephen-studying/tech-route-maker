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
5. Records source files and SHA-256 hashes before accepting evidence.
6. Separates verified evidence coverage from inferred coverage.
7. Applies a strict final-quality gate before rendering.
8. Renders editable outputs and reports required manual revision.

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

The skill offers a recommended preset, then confirms final formats, target medium, layout and style in one concise grouped choice. It does not silently guess delivery preferences.

## Typical Use Cases

Research and academic users can use it for:

- Paper method framework figures.
- Research technical route diagrams.
- Thesis proposal route diagrams.
- Defense or group-meeting method slides.
- Project application or grant-application technical routes.
- AI/model pipeline figures.
- Evidence-linked method overviews.

Engineering users can use it for:

- Source-grid-load-storage energy routes.
- System architecture and data-flow routes.
- Control, sensing, validation and deployment routes.
- Course-design and engineering-report diagrams.
- Agent, tool, automation and documentation workflows.

Campaign diagrams are kept only as legacy or experimental examples. They are not part of the default research-and-engineering workflow.

## Installation

Install the root skill directly with GitHub CLI 2.96 or newer:

```bash
gh skill install Stephen-studying/tech-route-maker SKILL.md --agent codex --scope user
gh skill install Stephen-studying/tech-route-maker SKILL.md --agent claude-code --scope user
gh skill install Stephen-studying/tech-route-maker SKILL.md --agent cursor --scope user
gh skill install Stephen-studying/tech-route-maker SKILL.md --agent gemini-cli --scope user
gh skill install Stephen-studying/tech-route-maker SKILL.md --agent github-copilot --scope user
```

Clone this repository:

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
cd tech-route-maker
```

Install the CLI and validate a complete demo:

```bash
python -m pip install -e .
trm doctor
trm validate examples/academic-paper-demo/outputs/tech-route.json --strict
trm render examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,drawio-code,excalidraw,mermaid,html,markdown,json
```

For a new project, run `trm ingest <sources> --output-dir evidence-pack`, then `trm init`. Final rendering is blocked until domain context, source hashes, node evidence, inferred content and unresolved questions pass. Use `--allow-draft` only for an explicitly unfinished draft.

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

The preferred installer is `gh skill install ... SKILL.md --agent <agent> --scope user`. For unsupported hosts, use `python scripts/install_agent_skill.py --target <skill-parent-directory> --agent <name>`; the fallback installer requires an explicit destination and does not guess agent-specific private paths.

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
