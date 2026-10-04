# Three-Column Template Library Demo

This example applies `cn-three-column-research-framework` to a source-verified campus energy project.

The template separates:

- left: research logic;
- center: editable research-content rows;
- right: research methods.

All visible content nodes are grounded in `source/project-brief.md`. The main canvas intentionally contains no semantic edge labels or node-to-node auto-routing.

Editable outputs:

- `outputs/tech-route.pptx`
- `outputs/tech-route.svg`
- `outputs/tech-route.drawio`
- `outputs/tech-route.drawio-code.xml`
- `outputs/tech-route.html`
- `outputs/tech-route.json`

Regenerate:

```bash
python scripts/build_template_demo.py
python scripts/render_all.py examples/template-library-demo/outputs/tech-route.json examples/template-library-demo/outputs --formats pptx,svg,drawio,drawio-code,html,json
```
