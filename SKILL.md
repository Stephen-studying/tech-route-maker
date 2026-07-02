---
name: tech-route-maker
description: Create evidence-grounded editable technical route diagrams for research and engineering projects. Use when the user asks to draw, generate, visualize, render, export, or revise a technical route diagram, research route, paper method framework, publication figure, thesis proposal route, engineering system route, software or agent workflow, pipeline, architecture roadmap, process diagram, or editable PPTX/SVG/Draw.io/Mermaid/HTML diagram. Supports implicit invocation when the user asks for route diagrams and explicit invocation with $tech-route-maker.
---

# Tech Route Maker

## Purpose

Use this skill to turn source materials into evidence-grounded editable technical route diagrams for research and engineering projects.

Primary users are researchers, students, academic writers, engineering teams and agent/tool builders preparing paper framework figures, method overview diagrams, thesis proposal routes, defense visuals, course-design diagrams, engineering system routes and workflow pipelines.

Campaign or advertising routes are legacy/experimental use cases. Do not make them the default direction unless the user explicitly asks for them.

## Portability

This skill is intentionally agent-agnostic. `SKILL.md` is the source of truth for Codex/OpenAI-style skill loaders and any agent that understands skill folders. Other adapters in the repository point back here:

- `AGENTS.md` for generic coding agents.
- `CLAUDE.md` for Claude-style project context.
- `GEMINI.md` and `.gemini/settings.json` for Gemini CLI.
- `.cursor/rules/tech-route-maker.mdc` for Cursor.
- `.github/copilot-instructions.md` for GitHub Copilot coding agent.
- `.aider.conf.yml` for Aider-style workflows.

## Default Interaction Policy

Do not interrupt the user with a long option list by default.

If the user provides enough context, choose the closest preset automatically and proceed. Ask a clarification question only when a missing choice would materially change the output.

Default behavior:

- If the user asks for an editable presentation figure, generate `pptx`, `svg` and `json`.
- If the user asks for a paper or research figure, generate `svg`, `pptx` and `json`.
- If the user asks for a maintainable system diagram, generate `drawio`, `svg` and `json`.
- If the user asks for documentation output, generate `markdown`, `mermaid` and `json`.
- If the user asks for long-term maintenance, add `drawio`.
- If the user asks for all formats, render `pptx`, `svg`, `drawio`, `excalidraw`, `mermaid`, `html`, `markdown` and `json`.

Always record the selected preset and output formats in `selected_preset` and `metadata.selected_output_formats`.

## Default Presets

Use these presets unless the user explicitly chooses a different layout, format bundle or visual style.

```yaml
academic-method:
  purpose: Academic method framework
  trigger_hints: [paper, manuscript, review, method, experiment, publication figure, academic figure]
  outputs: [pptx, svg, json]
  layout: academic-method-framework
  style: academic-blue

thesis-proposal:
  purpose: Thesis/proposal technical route
  trigger_hints: [proposal, research plan, thesis, grant, topic application, 开题, 课题申报]
  outputs: [pptx, svg, drawio, json]
  layout: proposal-matrix-route
  style: presentation-clean

engineering-system:
  purpose: Engineering system route
  trigger_hints: [engineering system, energy system, control system, hardware system, platform design, architecture]
  outputs: [pptx, svg, drawio, html, json]
  layout: engineering-architecture-route
  style: dark-technical

workflow-pipeline:
  purpose: Workflow or tool pipeline
  trigger_hints: [software tool, agent skill, pipeline, workflow, automation, documentation]
  outputs: [svg, markdown, mermaid, json]
  layout: horizontal-stages
  style: minimal-gray
```

## Ask Only When Necessary

Ask one concise clarification question when:

- No source material or topic is available.
- The user requests a final figure but gives no target audience or use case and several presets fit equally well.
- The user asks for a specific output environment but the format is ambiguous.
- A requested format conflicts with editability or with available renderer support.
- The source evidence is too weak to decide whether a node is source-supported or inferred.

Do not ask repeated setup questions when reasonable defaults are available. Start from a draft route, expose assumptions, and let the user revise.

## Advanced Options

Show advanced choices only when the user asks to choose formats, style, layout, presets, or says advanced mode.

Advanced output formats:

1. `pptx` - editable in PowerPoint or WPS.
2. `svg` - editable in Figma, Illustrator or Inkscape.
3. `drawio` - editable in diagrams.net.
4. `excalidraw` - editable whiteboard-style scene.
5. `mermaid` - text-editable Markdown diagram.
6. `html` - interactive preview with node details.
7. `markdown` - project documentation page.
8. `json` - structured source file for re-rendering.

Advanced layout families:

1. `academic-method-framework`
2. `proposal-matrix-route`
3. `engineering-architecture-route`
4. `horizontal-stages`
5. `vertical-research-route`
6. `layered-architecture`
7. `closed-loop-optimization-route`
8. `evidence-centered-route`
9. `baseline-vs-ours-split`
10. `case-walkthrough-strip`

Advanced visual styles:

1. `academic-blue`
2. `blue-green-research`
3. `monochrome-paper`
4. `presentation-clean`
5. `minimal-gray`
6. `nature-style-editorial`
7. `high-contrast-accessible`
8. `dark-technical`
9. `schematic-precision`
10. `premium-scientific`

## Workflow

1. Confirm the source scope: current repository, a specific directory, a document set, or pasted project notes.
2. Inspect project evidence before diagramming:
   - README, docs, notebooks, papers, reports, briefs or notes.
   - PDF, LaTeX, manuscript text, method sections, supplements, proposal documents or task briefs.
   - Directory structure, manifests and config files.
   - Entrypoints, API routes, model/training/inference scripts, data-processing scripts and deployment files when they clarify the system.
   - Tests, examples and outputs when they clarify validation or deliverables.
3. Build a source-grounded foundation:
   - Problem, gap, objective, assumptions, audience and intended reader effect.
   - Ordered method/process steps and non-droppable core substeps.
   - Inputs, outputs, artifacts, variables, metrics, claims, evidence and risk items.
   - For papers: figure slot, reader question, caption burden and terminology/acronym integrity.
   - For engineering: system boundary, modules, data/energy/material flow, validation and deliverables.
4. Select the closest preset and output bundle using the default policy.
5. Extract a route model with this minimum logic:
   `problem or objective -> inputs/data -> methods/modules -> implementation/training/inference -> validation/evaluation -> outputs/applications`.
6. Create or update `tech-route.json` before rendering any user-facing format.
7. Validate route structure, evidence coverage, inferred content, warnings and unresolved assumptions.
8. Render selected editable formats.
9. Report generated files, warnings, quality report findings and recommended manual review steps.

## Route Model

Use `references/route-schema.md` for the JSON schema. Keep every visible node traceable. Each visible node should include at least one evidence item or be marked with `is_inferred: true` and linked to an assumption.

Use `references/paper-framework-integration.md` for paper-grounded and publication-figure rules, especially when the input is a manuscript, thesis, proposal, academic project, or method description.

Use concise node labels:

- Prefer 3 to 9 words.
- Keep each stage to 2 to 6 nodes when possible.
- Use edge labels for semantic transitions such as `feeds`, `trains`, `validates`, `optimizes`, `deploys`, `supports`, or the user's language equivalent.
- Keep variables, temporary artifacts, scores, metrics, parameters and pass-through states on edges, tags or legends unless the source proves they are actual modules.
- Separate the semantic graph used for audit from the visual graph that will be rendered.
- Compress repeated actors, samples, panels, rows, arrows or equivalent flows unless each visible repetition adds source-grounded meaning.

## Output Formats

Read `references/output-options.md` before explaining format tradeoffs.

Editable constraints:

- PPTX: use native shapes, text boxes and connector lines; do not paste a screenshot as the main diagram.
- SVG: use editable text, rectangles, paths and lines; do not rasterize the diagram.
- Draw.io: use editable `mxCell` nodes and edges.
- Excalidraw: use editable scene elements.
- Mermaid: keep the `.mmd` source as text.
- HTML: keep interaction data in structured JSON or embedded object data.
- Markdown: include Mermaid source and evidence tables when useful.
- JSON: keep the route source complete enough to re-render.
- Quality report: include evidence coverage, inferred node count, unresolved questions and manual review suggestions.

## Layout And Style

Read `references/layout-patterns.md` before building `tech-route.json` for an unfamiliar layout.

Read `references/visual-styles.md` before setting a theme.

For proposal and research-report diagrams, prefer polished academic template language: white canvas, clear title, matrix or framework sections, low-saturation logical regions, dashed boundaries where they clarify grouping, and white editable node cards.

Use a left phase axis only when the user explicitly asks for a long vertical route. Do not use the vertical phase-axis layout as the default academic format.

For engineering diagrams, separate system boundary, data or energy flow, service/module layers, validation and outputs. Do not force engineering routes into a thesis-proposal layout.

Never copy online template images into outputs. Convert public visual patterns into original editable shapes.

## Legacy / Experimental Use Cases

Campaign strategy routes, creative-production pipelines, customer-journey diagrams and media-channel swimlanes are legacy or experimental. Use them only when the user explicitly asks for campaign, advertising, marketing, conversion funnel, media planning or commercial launch diagrams.

Do not show campaign options in the default preset list. Do not use campaign examples in the main README gallery.

## Open Source References

Read `references/github-projects.md` when deciding what to reuse or cite. Use permissively licensed projects as dependencies or design references when helpful, but do not copy code from projects without a clear compatible license.

## Scripts

All scripts accept a route JSON file and write output files. They use Python standard library only unless clearly stated.

Common legacy commands:

```bash
python scripts/validate_route.py outputs/tech-route.json
python scripts/render_mermaid.py outputs/tech-route.json outputs/tech-route.mmd
python scripts/render_svg.py outputs/tech-route.json outputs/tech-route.svg
python scripts/render_drawio.py outputs/tech-route.json outputs/tech-route.drawio
python scripts/render_excalidraw.py outputs/tech-route.json outputs/tech-route.excalidraw
python scripts/render_html.py outputs/tech-route.json outputs/tech-route.html
python scripts/render_markdown.py outputs/tech-route.json outputs/TECH_ROUTE.md
python scripts/render_pptx.py outputs/tech-route.json outputs/tech-route.pptx
python scripts/render_all.py outputs/tech-route.json outputs --formats pptx,svg,drawio
```

CLI commands, when installed:

```bash
trm validate outputs/tech-route.json
trm render outputs/tech-route.json outputs --formats pptx,svg,drawio,html,markdown,json
trm init --preset academic-method --output tech-route.json
trm doctor
```

## Onboarding Demo

For a low-friction first run, use the academic demo:

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

Read `examples/academic-paper-demo/demo-walkthrough.md` to see the simulated user request, route JSON, render commands and generated editable files.

## Validation

Run validation before and after rendering. Treat errors as blockers and warnings as items to report.

Validation checks:

- Required route title and stages.
- `route_version` and `selected_preset`.
- Unique stage and node IDs.
- Edge endpoints exist.
- Every visible node has evidence or explicit inference.
- Confidence values use `high`, `medium` or `low`.
- Node labels are not overloaded.
- Quality report warnings are visible to the user.

## Iteration

When the user asks to change colors, layout, labels, node count or output formats, update `tech-route.json` first and then re-render the selected files. Do not re-scan the whole project unless the user asks for content changes or the current route source is insufficient.