# Structural Template Catalog

Use this catalog when the user asks to apply a reusable style or template. A template controls semantic roles and geometry. A visual style controls color and typography only.

## Selection rule

1. If the user names a template, apply it directly.
2. If the user provides a reference image, select the template with the same structural grammar.
3. If the request is field-specific but structurally ambiguous, show the six template names below and ask for one concise choice.
4. Do not choose a template from color alone.
5. Keep source-specific wording editable and evidence-grounded.

## Templates

### `cn-three-column-research-framework`

- Chinese name: 三栏科研框架图
- Best for: thesis proposals, grant applications, research plans, material/chemical/biomedical mechanisms, and academic project applications.
- Structure: left research logic, central research content, right research method.
- Required stage fields: `logic_label`, `content_label`, `method_label`.
- Required density: 4–6 stages and 2–3 central content rows per stage.
- Main-canvas connectors: one thick vertical logic spine plus short inward block arrows. Never render semantic edge labels.
- Default outputs: PPTX, SVG, Draw.io, HTML, JSON.

### `cn-horizontal-defense-mainline`

- Chinese name: 横向答辩主线图
- Best for: 16:9 defense slides and project presentations.
- Structure: 4–6 horizontal main stages, 2–3 support tasks under each stage, one final output bar.
- Default outputs: PPTX, SVG, Draw.io, HTML, JSON.

### `cn-a4-stacked-research`

- Chinese name: A4 竖向分阶段图
- Best for: Word, thesis, proposal body pages, and portrait figures.
- Structure: centered stage headers, 2–3 task cards per stage, straight top-to-bottom arrows.
- Default outputs: PPTX, SVG, Draw.io, HTML, JSON.

### `cn-method-matrix-board`

- Chinese name: 研究方法矩阵图
- Best for: paper method overviews and research-content matrices.
- Structure: objective/data/method/validation/output regions with compact editable rows.
- Default outputs: PPTX, SVG, Draw.io, HTML, JSON.

### `cn-monochrome-review-route`

- Chinese name: 黑白评审线框图
- Best for: print-heavy formal submissions and reviewer-facing appendices.
- Structure: restrained monochrome sections and explicit flow direction.
- Default outputs: PPTX, SVG, Draw.io, HTML, JSON.

### `cn-engineering-layer-map`

- Chinese name: 工程系统分层图
- Best for: energy, control, platform, hardware, and software engineering projects.
- Structure: system boundary, inputs or flows, service/module layers, validation, and outputs.
- Default outputs: PPTX, SVG, Draw.io, HTML, JSON.

## Commands

```bash
trm templates
trm templates --json
trm init --template cn-three-column-research-framework --output tech-route.json
trm render tech-route.json outputs --formats pptx,svg,drawio,html,json --allow-draft
```

The generated files are editable first drafts. The user must review factual accuracy, terminology, density, color, and final publication layout.
