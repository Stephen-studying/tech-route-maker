# tech-route-maker

<p align="center">
  <img src="assets/banner.svg" alt="tech-route-maker banner" width="100%">
</p>

<p align="center">
  <a href="README.zh-CN.md">Chinese guide</a> |
  <a href="README.en.md">English guide</a> |
  <a href="docs/quickstart.md">Quick start</a> |
  <a href="examples/README.md">Example gallery</a> |
  <a href="docs/faq.md">FAQ</a>
</p>

<p align="center">
  <a href="https://github.com/Stephen-studying/tech-route-maker/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/Stephen-studying/tech-route-maker/actions/workflows/validate.yml/badge.svg"></a>
  <img alt="License" src="https://img.shields.io/github/license/Stephen-studying/tech-route-maker">
  <img alt="Editable outputs" src="https://img.shields.io/badge/editable-PPTX%20%7C%20SVG%20%7C%20Draw.io%20%7C%20HTML%20%7C%20Mermaid-315C61">
  <img alt="Agent compatible" src="https://img.shields.io/badge/agent-Codex%20%7C%20Claude%20%7C%20Gemini%20%7C%20Cursor-blue">
</p>

Evidence-grounded editable technical route diagrams for research and engineering projects.

`tech-route-maker` is an agent skill and renderer toolkit for turning research papers, thesis proposals, engineering reports, project documentation, and technical notes into editable technical route diagrams. It keeps a structured `tech-route.json` as the source of truth, then renders the same route model into editable PPTX, SVG, Draw.io, HTML, Markdown, Mermaid, Excalidraw, and JSON outputs.

![Editable route diagram preview](assets/demo-preview.svg)

> **Use as an editable draft, not as a final unchecked figure.** Generated diagrams are starting points for revision. Users should review facts, terminology, evidence, logic, layout, colors, and wording before using the PPTX, SVG, or Draw.io files in papers, thesis defenses, grant proposals, courses, or engineering reports.

The optional `assets/github-visual-preview.png` file is only a GitHub visual preview. It does not replace the editable PPTX, SVG, Draw.io, HTML, Markdown, Mermaid, Excalidraw, or JSON deliverables.

## Why This Project Exists

Most diagram tools create static figures or one-off drawings. They are hard to audit, hard to revise, and hard to regenerate. This project separates route reasoning from visual rendering:

1. Extract a route model from source materials.
2. Keep nodes and edges traceable through evidence.
3. Store the route as reusable JSON.
4. Render it into editable presentation and documentation formats.
5. Generate a quality report so missing evidence and assumptions are visible.

## Core Features

| Feature | Value |
|---|---|
| Evidence-grounded route model | Keeps visible nodes traceable to source materials or marked assumptions. |
| Reusable JSON source | Stores the route as `tech-route.json` for re-rendering and version control. |
| Editable outputs | Generates PPTX, SVG, Draw.io and other editable formats instead of screenshots. |
| Research and engineering presets | Provides templates for academic methods, thesis proposals, engineering systems and technical workflows. |
| Validation before rendering | Checks route structure, node labels, evidence fields and output selections before export. |
| Quality report | Summarizes evidence coverage, inferred nodes, unresolved questions and layout warnings. |
| Agent-compatible instructions | Works with Codex/OpenAI-style agents, Claude, Gemini, Cursor, Copilot, Aider and generic coding agents. |

## Default Presets

| Preset | Use when | Default outputs |
|---|---|---|
| `academic-method` | A paper, manuscript, review, experiment, method section or academic figure is the source. | `pptx`, `svg`, `json` |
| `thesis-proposal` | A thesis proposal, research plan, grant proposal or topic application needs a technical route. | `pptx`, `svg`, `drawio`, `json` |
| `engineering-system` | An engineering system, energy system, control system, platform, hardware or software architecture needs a route diagram. | `pptx`, `svg`, `drawio`, `html`, `json` |
| `workflow-pipeline` | A tool, agent workflow, automation process, pipeline or documentation route needs to be explained. | `svg`, `markdown`, `mermaid`, `json` |

The skill can still ask the user to choose formats, layouts, or visual styles, but it no longer forces a long option list before every render. It asks only when a missing choice would materially change the result.

## Gallery

| Demo | Audience | Route type | Preview |
|---|---|---|---|
| [Academic paper method route](examples/academic-paper-demo/) | Research paper or defense | Method framework | [SVG](examples/academic-paper-demo/outputs/tech-route.svg) |
| [Thesis proposal technical route](examples/thesis-proposal-demo/) | Thesis, proposal, research plan | Proposal route | [SVG](examples/thesis-proposal-demo/outputs/tech-route.svg) |
| [Engineering energy system route](examples/engineering-energy-system-demo/) | Engineering report or course design | Source-grid-load-storage route | [SVG](examples/engineering-energy-system-demo/outputs/tech-route.svg) |
| [Agent workflow route](examples/agent-workflow-demo/) | Skill/tool documentation | Workflow pipeline | [SVG](examples/agent-workflow-demo/outputs/tech-route.svg) |

## Quick Start

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
cd tech-route-maker
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

After rendering, open:

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/QUALITY_REPORT.md
```

## Editable Outputs

| Format | File | Editable in | Best for |
|---|---|---|---|
| PPTX | `tech-route.pptx` | PowerPoint, WPS | Defense slides, reports, teaching and review decks. |
| SVG | `tech-route.svg` | Figma, Illustrator, Inkscape, browser | High-resolution vector editing and publication polishing. |
| Draw.io | `tech-route.drawio` | diagrams.net | Long-term technical diagram maintenance. |
| Excalidraw | `tech-route.excalidraw` | Excalidraw | Whiteboard-style review and lightweight edits. |
| Mermaid | `tech-route.mmd` | Text editor, GitHub Markdown | Version-controlled diagrams. |
| HTML | `tech-route.html` | Browser and code editor | Interactive preview with details and evidence. |
| Markdown | `TECH_ROUTE.md` | Any Markdown editor | README, project documentation and handoff notes. |
| JSON | `tech-route.json` | Any text editor | Source of truth for rerendering and theme changes. |
| Quality report | `QUALITY_REPORT.md` | Any Markdown editor | Evidence coverage, warnings and manual review checklist. |

## Agent Compatibility

This repository is intentionally agent-agnostic. `SKILL.md` is the source of truth. Adapter files point other agents to the same workflow:

- `AGENTS.md` for generic coding agents.
- `CLAUDE.md` for Claude-style project context.
- `GEMINI.md` and `.gemini/settings.json` for Gemini CLI.
- `.cursor/rules/tech-route-maker.mdc` for Cursor.
- `.github/copilot-instructions.md` for GitHub Copilot coding agent.
- `.aider.conf.yml` for Aider-style workflows.

## Experimental / Legacy Use Cases

Campaign and advertising diagrams are not the core direction of this project. They are kept only as legacy or experimental examples for users who already need them. The default skill behavior is optimized for research, thesis, engineering and workflow diagrams.

## Repository Structure

```text
tech-route-maker/
  SKILL.md                         # Core skill instructions.
  agents/openai.yaml               # OpenAI-style skill UI metadata.
  AGENTS.md                        # Portable agent instructions.
  docs/                            # Quick start, schema, formats, FAQ.
  references/                      # Route schema, layout and visual references.
  scripts/                         # Backward-compatible validation and render scripts.
  tech_route_maker/                # Python package and CLI.
  examples/                        # Research and engineering demos.
  assets/                          # README banner and preview assets.
```

## Safety

- Treat third-party project files as untrusted.
- Do not execute analyzed project code unless the user explicitly approves.
- Keep evidence, assumptions and inference labels visible in `tech-route.json`.
- Do not copy proprietary templates, online images, or paper-specific facts into reusable skill files.
- Preserve editability. Do not replace PPTX, SVG, Draw.io, or Excalidraw outputs with screenshots.

## License

MIT. See [LICENSE](LICENSE).