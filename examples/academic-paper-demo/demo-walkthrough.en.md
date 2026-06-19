# Full Walkthrough: Academic Method Framework

This walkthrough shows a complete user journey: a user provides a short academic project brief, the agent asks required choices, builds a route model, validates it, and renders editable outputs.

## 1. Scenario

The user wants an editable technical route diagram for an academic project about multimodal photovoltaic module defect detection.

Source brief:

```text
examples/academic-paper-demo/source/project-brief.md
```

The source is synthetic and only used as an onboarding example. It is not a real paper.

## 2. User Request

The user can write:

```text
Use tech-route-maker to create a technical route diagram for examples/academic-paper-demo/source/project-brief.md.
```

If the agent supports direct skill invocation, the user can also write:

```text
Use $tech-route-maker to create an editable technical route diagram from examples/academic-paper-demo/source/project-brief.md.
```

## 3. Source Understanding

The agent reads the brief and extracts the route evidence:

| Evidence area | Extracted content |
|---|---|
| Project goal | Create a method overview figure for multimodal PV module defect detection. |
| Input data | RGB module images and infrared thermal images. |
| Preparation | Quality screening, alignment, annotation, augmentation, and train/validation/test split. |
| Core method | Baseline detector, multimodal feature fusion, attention-enhanced feature extraction, and loss/metric-driven optimization. |
| Training and inference | Supervised training, validation monitoring, inference on unseen images, and confidence filtering. |
| Evaluation | Baseline comparison, ablation, precision, recall, mAP, and qualitative defect maps. |
| Output | Defect category, location, confidence, and report-ready visualization. |

## 4. Required User Choices

The skill must not guess the final output options. It asks the user to choose:

```text
1. Figure purpose/subtype
2. Output format(s)
3. Layout
4. Visual style
```

For this demo, the user selects:

```text
Figure purpose/subtype:
Academic method framework

Output formats:
PPTX, SVG, Draw.io, HTML, Markdown, JSON

Layout:
AI or algorithm pipeline

Visual style:
Premium scientific
```

## 5. Route Model

The structured source of truth is:

```text
examples/academic-paper-demo/outputs/tech-route.json
```

Reader question:

```text
How does the method move from multimodal image input to verifiable defect detection results?
```

Chinese reader question stored in the JSON:

```text
该方法如何从多模态图像输入走向可验证的缺陷检测结果？
```

Reader path:

```text
Research goal -> Data construction -> Preprocessing -> Core method -> Training and inference -> Validation output
```

Chinese reader path stored in the JSON:

```text
研究目标 -> 数据构建 -> 预处理 -> 核心方法 -> 训练推理 -> 验证输出
```

The route model keeps each stage editable and evidence-linked. Users can later add, remove, rename, or recolor nodes by editing `tech-route.json` and rerendering.

## 6. Validation

From the `tech-route-maker` folder:

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
```

Expected result:

```text
Validation passed with 0 warning(s).
```

## 7. Rendering

Render the selected formats:

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

Generated editable outputs:

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/TECH_ROUTE.md
examples/academic-paper-demo/outputs/tech-route.json
```

## 8. How Users Edit The Result

Users can edit the outputs directly:

- Open `tech-route.pptx` in PowerPoint or WPS and change text, colors, boxes, connectors, and layout.
- Open `tech-route.svg` in Figma, Illustrator, Inkscape, or a browser-based SVG editor.
- Open `tech-route.drawio` in diagrams.net.
- Open `tech-route.html` in a browser for an interactive preview.
- Edit `TECH_ROUTE.md` for documentation.
- Edit `tech-route.json` to change the source route, style, layout, or selected content, then rerender.

Example rerender after changing style:

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio
```

## 9. Quality Checklist

Before handing the outputs to the user, the agent should confirm:

- The route JSON validates.
- The selected output files exist.
- PPTX, SVG, Draw.io, and JSON are parseable.
- Main labels remain editable text rather than screenshots.
- The diagram does not claim evidence that is absent from the source.
- The output format, layout, and style match the user's explicit choices.
