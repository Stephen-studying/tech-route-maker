# Changelog

## 0.2.0 - 2026-07-02

Research and engineering focus release.

Added:

- Default presets for academic methods, thesis proposals, engineering systems and workflow pipelines.
- `route_version: 0.2.0` schema with structured assumptions, unresolved questions, confidence fields and inference flags.
- `QUALITY_REPORT.md` generation for evidence coverage, inferred nodes, warning checks and manual review guidance.
- Python package entry point with `trm validate`, `trm render`, `trm init` and `trm doctor`.
- Engineering energy system demo for source-grid-load-storage planning.
- Agent workflow demo for converting technical materials into editable route diagrams.
- `docs/schema-migration-v0.2.md` migration guide.

Changed:

- README positioning narrowed from broad cross-domain route diagrams to evidence-grounded research and engineering route diagrams.
- Skill interaction policy now uses default presets instead of forcing long option selection.
- Advertising/campaign examples moved to legacy or experimental status.
- GitHub Actions now validates the four core research and engineering examples.

Validation:

- Python source compile check for `scripts/*.py` and `tech_route_maker/*.py`.
- Example route JSON validation.
- Demo rendering for PPTX, SVG, Draw.io, Excalidraw, Mermaid, HTML, Markdown, JSON and `QUALITY_REPORT.md`.
- CLI validation through `trm --help`, `trm doctor`, `trm validate` and `trm render`.

## 0.1.1 - 2026-06-19

Repository-surface upgrade.

Added:

- Visual GitHub README hero with banner, badges, preview image, gallery, and 30-second start.
- `assets/` visual assets for banner, demo preview, and social preview.
- `docs/` documentation hub with quick start, installation, output formats, agent compatibility, schema, FAQ, and release checklist.
- `examples/README.md` gallery.
- Thesis proposal, software architecture, and campaign route demos with generated editable outputs.
- GitHub Actions validation workflow for route JSON, renderers, and representative outputs.

## 0.1.0 - 2026-06-19

Initial public release of `tech-route-maker`.

Added:

- Portable `SKILL.md` workflow for editable technical route diagrams.
- Cross-agent adapters for Codex/OpenAI-style skills, AGENTS.md readers, Claude-style contexts, Gemini CLI, Cursor, GitHub Copilot coding agent, and Aider-style workflows.
- Structured `tech-route.json` schema guidance.
- Renderers for PPTX, SVG, Draw.io, Excalidraw, Mermaid, HTML, Markdown, and JSON.
- Academic paper-framework guidance and open-source reference notes.
- Complete academic demo with source brief, route JSON, editable outputs, and English/Chinese walkthroughs.
- English and Chinese README files.