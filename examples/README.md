# Examples And Gallery

This gallery shows the main scenarios supported by `tech-route-maker`. Each demo includes a source brief, `tech-route.json`, and editable outputs.

| Demo | Audience | Layout | Style | Preview |
|---|---|---|---|---|
| [Academic paper method framework](academic-paper-demo/) | Academic paper or defense | AI pipeline | Premium scientific | [SVG](academic-paper-demo/outputs/tech-route.svg) |
| [Thesis proposal route](thesis-proposal-demo/) | Thesis, proposal, research plan | Vertical research route | Academic blue | [SVG](thesis-proposal-demo/outputs/tech-route.svg) |
| [Software architecture route](software-architecture-demo/) | Engineering handoff | Engineering architecture | Schematic precision | [SVG](software-architecture-demo/outputs/tech-route.svg) |
| [Campaign strategy route](campaign-route-demo/) | Advertising and campaign planning | Campaign funnel | Advertising clean campaign | [SVG](campaign-route-demo/outputs/tech-route.svg) |

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
