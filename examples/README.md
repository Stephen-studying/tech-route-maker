# Examples And Gallery

This gallery shows the main scenarios supported by `tech-route-maker`. Each demo includes a source brief, `tech-route.json`, and editable outputs. SVG, PPTX, Draw.io, Excalidraw, HTML, Markdown, and JSON are generated from the same route model.

The optional `assets/github-visual-preview.png` image on the repository homepage is a generated visual preview only. It is not used as the editable diagram source.

| Demo | Audience | Layout | Style | Preview |
|---|---|---|---|---|
| [Academic paper method framework](academic-paper-demo/) | Academic paper or defense | Academic method framework | Premium scientific | [SVG](academic-paper-demo/outputs/tech-route.svg) |
| [Thesis proposal route](thesis-proposal-demo/) | Thesis, proposal, research plan | Proposal matrix route | Proposal pastel route | [SVG](thesis-proposal-demo/outputs/tech-route.svg) |
| [Software architecture route](software-architecture-demo/) | Engineering handoff | Software system route | Schematic precision | [SVG](software-architecture-demo/outputs/tech-route.svg) |
| [Campaign strategy route](campaign-route-demo/) | Advertising and campaign planning | Campaign strategy map | Advertising clean campaign | [SVG](campaign-route-demo/outputs/tech-route.svg) |

## Render All Demo Outputs

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
python scripts/render_all.py examples/thesis-proposal-demo/outputs/tech-route.json examples/thesis-proposal-demo/outputs --formats pptx,svg,drawio,html,markdown,json
python scripts/render_all.py examples/software-architecture-demo/outputs/tech-route.json examples/software-architecture-demo/outputs --formats pptx,svg,drawio,html,markdown,json
python scripts/render_all.py examples/campaign-route-demo/outputs/tech-route.json examples/campaign-route-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

## What To Compare

- PPTX: editable slide shapes.
- SVG: vector preview and design-tool editing.
- Draw.io: long-term technical maintenance.
- HTML: interactive reading and evidence inspection.
- JSON: source of truth for rerendering.
