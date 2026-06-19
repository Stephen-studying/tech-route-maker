# Quick Start

This page gives the shortest path from clone to editable outputs.

## 1. Clone

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
cd tech-route-maker
```

## 2. Validate A Demo Route

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
```

Expected result:

```text
Validation passed with 0 warning(s).
```

## 3. Render Editable Outputs

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

Open:

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.html
```

## 4. Use With An Agent

Ask your agent:

```text
Use tech-route-maker to create an editable technical route diagram from my source brief.
```

The agent must ask for:

1. Figure purpose/subtype.
2. Output format(s).
3. Layout.
4. Visual style.

---

# 快速开始

最短流程：

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
cd tech-route-maker
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

然后打开 `examples/academic-paper-demo/outputs/` 中的 PPTX、SVG 或 HTML 文件。
