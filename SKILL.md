---
name: tech-route-maker
description: Create editable technical route diagrams for academic workers and, secondarily, advertising or campaign teams. Use when the user asks to draw, generate, visualize, or export a technical route diagram, research route, paper method framework, publication figure, project roadmap, method flowchart, architecture roadmap, workflow, pipeline, system process diagram, campaign route, or editable diagram output. Supports implicit invocation when the user asks for diagrams and explicit invocation with $tech-route-maker.
---

# Tech Route Maker

## Purpose

Use this skill to understand a project, paper, method, research plan, or advertising/campaign brief, extract its technical route, ask the user to choose output options, and render editable diagram files.

Primary users are academic workers preparing paper framework figures, method overview diagrams, proposal route maps, thesis defenses, and research reports. Secondary users are advertising workers who need editable strategy, campaign, customer-journey, or production-route diagrams.

The skill must not guess final output format, layout, or style from words such as "editable", "paper", "presentation", "GitHub", "interactive", or similar context. Always ask the user to choose.

## Portability

This skill is intentionally agent-agnostic. `SKILL.md` is the source of truth for Codex/OpenAI-style skill loaders and any agent that understands skill folders. Other adapters in the repository point back here:

- `AGENTS.md` for generic coding agents.
- `CLAUDE.md` for Claude-style project context.
- `GEMINI.md` and `.gemini/settings.json` for Gemini CLI.
- `.cursor/rules/tech-route-maker.mdc` for Cursor.
- `.github/copilot-instructions.md` for GitHub Copilot coding agent.
- `.aider.conf.yml` for Aider-style workflows.

## Workflow

1. Confirm the source scope: current repository, a specific directory, a document set, or pasted project notes.
2. Inspect project evidence before diagramming:
   - README, docs, notebooks, papers, reports, or brief files.
   - PDF, LaTeX, manuscript text, method sections, supplements, proposal documents, grant/task briefs.
   - Advertising briefs, audience research, campaign plan, channel/media plan, creative pipeline, deliverable list.
   - Directory structure and manifest/config files.
   - Entrypoints, API routes, model/training/inference scripts, data-processing scripts, deployment files.
   - Tests, examples, and outputs when they clarify validation or deliverables.
3. Build a source-grounded foundation before diagramming:
   - Problem, gap, objective, assumptions, audience, and intended reader effect.
   - Ordered method/process steps and non-droppable core substeps.
   - Inputs, outputs, artifacts, variables, metrics, claims, evidence, and risk items.
   - For papers: figure slot, reader question, caption burden, terminology/acronym integrity.
   - For advertising: campaign objective, audience segment, insight, creative strategy, media flow, conversion/evaluation signals.
4. Extract a route model with this minimum logic:
   `problem or objective -> inputs/data -> methods/modules -> implementation/training/inference -> validation/evaluation -> outputs/applications`.
5. Create a `tech-route.json` draft internally before rendering any user-facing format.
6. Ask the user to choose all mandatory options:
   - Figure purpose/subtype.
   - Output formats, single or multiple.
   - Layout pattern.
   - Visual style.
7. Render only the formats selected by the user. Do not infer or auto-select formats except for the internal JSON source.
8. Run validation and report generated files, warnings, and unresolved assumptions.

## Mandatory User Choice Prompt

Ask in the user's language. Provide choices, allow single or multiple selections, and stop if the user has not selected the required options.

Use this shape:

```text
Please choose one figure purpose/subtype:
1. Academic method framework
2. Paper architecture overview
3. Pipeline or process figure
4. Agent or tool workflow
5. System/data-flow figure
6. Mechanism intuition schematic
7. Case walkthrough / example strip
8. Evidence-linked framework
9. Failure-aware or limitation framework
10. Thesis/proposal technical route
11. Advertising strategy route
12. Campaign production workflow
13. Customer journey / conversion funnel
14. Media-channel swimlane

Please choose output format(s), single or multiple:
1. PPTX - editable in PowerPoint or WPS
2. SVG - editable in Figma, Illustrator, or Inkscape
3. Draw.io - editable in diagrams.net
4. Excalidraw - editable whiteboard-style diagram
5. Mermaid - text-editable Markdown diagram
6. HTML - interactive preview with node details
7. Markdown - project documentation page
8. JSON - structured source file for re-rendering
9. All formats

Please choose one layout:
1. Horizontal stages
2. Vertical research route
3. Three-column goals/content/results
4. AI or algorithm pipeline
5. Engineering architecture route
6. Timeline or swimlane roadmap
7. Layered architecture
8. Closed-loop optimization route
9. Evidence-centered route
10. Hub-and-spoke core method
11. Baseline-vs-ours split
12. Case walkthrough strip
13. Campaign funnel
14. Creative-production pipeline
15. Proposal phase axis
16. Wide collaboration map

Please choose one visual style:
1. Academic blue
2. Blue-green research
3. Monochrome paper
4. Defense presentation color
5. Minimal gray
6. Nature-style editorial
7. High-contrast accessible
8. Dark technical
9. Soft pastel
10. Schematic precision
11. Editorial clarity
12. Mechanism snapshot
13. Evidence infographic
14. Premium scientific
15. Advertising clean campaign
16. Proposal pastel route
17. Grant linework
18. Wide collaboration map
```

If the user chooses "all formats", render PPTX, SVG, Draw.io, Excalidraw, Mermaid, HTML, Markdown, and JSON.

## Route Model

Use `references/route-schema.md` for the JSON schema. Keep every visible node traceable. Each node should include at least one evidence item or an explicit `inference` evidence item.

Use `references/paper-framework-integration.md` for paper-grounded and publication-figure rules, especially when the input is a manuscript, thesis, proposal, academic project, or method description.

Use concise node labels:
- Prefer 3 to 9 words.
- Keep each stage to 2 to 6 nodes when possible.
- Use edge labels for semantic transitions such as `feeds`, `trains`, `validates`, `optimizes`, `deploys`, `supports`, or the user's language equivalent.
- Keep variables, temporary artifacts, scores, metrics, parameters, and pass-through states on edges, ports, tags, or legends unless the source proves they are actual modules.
- Separate the semantic graph used for audit from the visual graph that will be rendered.
- Compress repeated actors, samples, panels, rows, arrows, or equivalent flows unless each visible repetition adds source-grounded meaning.

## Output Formats

Read `references/output-options.md` before presenting output choices or explaining tradeoffs.

Editable constraints:
- PPTX: use native shapes, text boxes, and connector lines; do not paste a screenshot as the main diagram.
- SVG: use editable text, rectangles, paths, and lines; do not rasterize the diagram.
- Draw.io: use editable `mxCell` nodes and edges.
- Excalidraw: use editable scene elements.
- Mermaid: keep the `.mmd` source as text.
- HTML: keep interaction data in structured JSON or embedded object data.
- Markdown: include Mermaid source and evidence tables.

## Layout And Style

Read `references/layout-patterns.md` before asking for layout choices or building `tech-route.json`.

Read `references/visual-styles.md` before asking for visual style choices or setting a theme.

For proposal and research-report diagrams, prefer the polished academic template language documented in `references/visual-styles.md`: white canvas, title pill or title band, low-saturation stage regions, dashed logical boundaries, left phase axis for long vertical routes, and white editable node cards. For project-report or advertising diagrams, prefer wide collaboration maps or campaign routes only when the user explicitly chooses them.

For academic figures, choose a reader-first diagram: the 3 to 7 step first-glance path should be clear without reading long captions. For advertising diagrams, keep audience, insight, creative route, channel route, and measurement route visibly separated.

Never copy online template images into outputs. Convert public visual patterns into original editable shapes.

## Open Source References

Read `references/github-projects.md` when deciding what to reuse or cite. Use permissively licensed projects as dependencies or design references when helpful, but do not copy code from projects without a clear compatible license.

## Scripts

All scripts accept a route JSON file and write an output file. They use Python standard library only unless clearly stated.

Common commands:

```bash
python scripts/validate_route.py outputs/tech-route.json
python scripts/render_mermaid.py outputs/tech-route.json outputs/tech-route.mmd
python scripts/render_svg.py outputs/tech-route.json outputs/tech-route.svg
python scripts/render_drawio.py outputs/tech-route.json outputs/tech-route.drawio
python scripts/render_excalidraw.py outputs/tech-route.json outputs/tech-route.excalidraw
python scripts/render_html.py outputs/tech-route.json outputs/tech-route.html
python scripts/render_markdown.py outputs/tech-route.json outputs/TECH_ROUTE.md
python scripts/render_pptx.py outputs/tech-route.json outputs/tech-route.pptx
```

Use `scripts/render_all.py` after the user has selected formats:

```bash
python scripts/render_all.py outputs/tech-route.json outputs --formats pptx,svg,drawio
```

## Onboarding Demo

For a low-friction first run, use the academic demo:

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

Read `examples/academic-paper-demo/demo-walkthrough.md` to see the simulated user request, required option choices, route JSON, render commands, and generated editable files.

## Validation

Run `scripts/validate_route.py` before and after rendering. Treat errors as blockers and warnings as items to report.

Validation checks:
- Required route title and stages.
- Unique stage and node IDs.
- Edge endpoints exist.
- Every node has evidence or explicit inference.
- Nodes are not overloaded with long labels.
- User-facing output formats were selected explicitly.

## Iteration

When the user asks to change colors, layout, labels, node count, or output formats, update `tech-route.json` first and then re-render the selected files. Do not re-scan the whole project unless the user asks for content changes or the current route source is insufficient.
