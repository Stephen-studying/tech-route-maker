# Demo Walkthrough: Academic Method Framework

This walkthrough shows how a user can start with a short academic project brief and get editable technical route diagrams.

Detailed versions:

- English: `examples/academic-paper-demo/demo-walkthrough.en.md`
- Chinese: `examples/academic-paper-demo/demo-walkthrough.zh-CN.md`

## 1. User request

```text
Use $tech-route-maker to create a technical route diagram for examples/academic-paper-demo/source/project-brief.md.
```

## 2. Skill asks required choices

The skill must not guess these choices. In this demo, the user selects:

```text
Figure purpose/subtype:
1. Academic method framework

Output formats:
PPTX, SVG, Draw.io, HTML, Markdown, JSON

Layout:
4. AI or algorithm pipeline

Visual style:
14. Premium scientific
```

## 3. Route model

The structured source of truth is:

```text
examples/academic-paper-demo/outputs/tech-route.json
```

The route answers this reader question:

```text
该方法如何从多模态图像输入走向可验证的缺陷检测结果？
```

Reader path:

```text
研究目标 -> 数据构建 -> 预处理 -> 核心方法 -> 训练推理 -> 验证输出
```

## 4. Render commands

From the `tech-route-maker` folder:

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

## 5. Generated editable outputs

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/TECH_ROUTE.md
examples/academic-paper-demo/outputs/tech-route.json
```

## 6. What users can edit next

- Change `style` in `tech-route.json` to `schematic-precision`, `editorial-clarity`, or `monochrome-paper`.
- Change `layout` to `vertical-research-route` or `closed-loop-optimization`.
- Add/remove nodes under `stages`.
- Change output formats and rerun `render_all.py`.
