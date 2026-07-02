# Quick Start

This page gives the shortest path from clone to editable route outputs.

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
Validation OK
```

Older versions may print:

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
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/QUALITY_REPORT.md
```

## 4. Use The CLI

After local installation:

```bash
pip install -e .
trm doctor
trm validate examples/academic-paper-demo/outputs/tech-route.json
trm render examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

## 5. Use With An Agent

Ask your agent:

```text
Use tech-route-maker to create an editable technical route diagram from my source brief.
```

The agent should choose a default preset when the request is clear. It should ask only when a missing choice would materially change the result.

## Manual Review Reminder

The generated route is an editable draft. Before using it in a paper, thesis defense, grant proposal, course design or engineering report, review:

- Facts and terminology.
- Evidence and inferred nodes.
- Route logic and edge labels.
- Colors, layout and spacing.
- Long labels and overloaded stages.