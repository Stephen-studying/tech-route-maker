# Examples And Gallery

This gallery shows the core research and engineering scenarios supported by `tech-route-maker`. Each demo includes a source brief, `tech-route.json`, editable outputs, and a quality report. SVG, PPTX, Draw.io, HTML, Markdown and JSON are generated from the same route model.

The optional `assets/github-visual-preview.png` image on the repository homepage is a generated visual preview only. It is not used as the editable diagram source.

| Demo | Audience | Layout | Style | Preview |
|---|---|---|---|---|
| [Academic paper method route](academic-paper-demo/) | Academic paper or defense | Academic method framework | Academic blue | [SVG](academic-paper-demo/outputs/tech-route.svg) |
| [Thesis proposal technical route](thesis-proposal-demo/) | Thesis, proposal, research plan | Proposal matrix route | Presentation clean | [SVG](thesis-proposal-demo/outputs/tech-route.svg) |
| [Engineering energy system route](engineering-energy-system-demo/) | Engineering report or course design | Engineering architecture route | Dark technical | [SVG](engineering-energy-system-demo/outputs/tech-route.svg) |
| [Agent workflow route](agent-workflow-demo/) | Skill/tool documentation | Horizontal stages | Minimal gray | [SVG](agent-workflow-demo/outputs/tech-route.svg) |

## Legacy / Experimental

`legacy-campaign-route-demo/` is retained for users who explicitly need campaign or advertising route diagrams. It is not part of the default gallery.

## Render All Demo Outputs

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
python scripts/render_all.py examples/thesis-proposal-demo/outputs/tech-route.json examples/thesis-proposal-demo/outputs --formats pptx,svg,drawio,html,markdown,json
python scripts/render_all.py examples/engineering-energy-system-demo/outputs/tech-route.json examples/engineering-energy-system-demo/outputs --formats pptx,svg,drawio,html,markdown,json
python scripts/render_all.py examples/agent-workflow-demo/outputs/tech-route.json examples/agent-workflow-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

## What To Compare

- PPTX: editable slide shapes.
- SVG: vector preview and design-tool editing.
- Draw.io: long-term technical maintenance.
- HTML: interactive reading and evidence inspection.
- JSON: source of truth for rerendering.
- `QUALITY_REPORT.md`: warnings and manual review checklist.