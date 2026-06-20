# Route Schema

`tech-route.json` is the source of truth for rendering. Edit the JSON first, then rerender PPTX, SVG, Draw.io, Excalidraw, Mermaid, HTML, Markdown, or JSON outputs from the same model.

## Minimal Structure

```json
{
  "title": "Project Technical Route",
  "subtitle": "Editable route diagram",
  "layout": "academic-method-framework",
  "style": "academic-blue",
  "metadata": {
    "selected_output_formats": ["pptx", "svg", "json"]
  },
  "stages": [
    {
      "id": "objective",
      "title": "Objective",
      "nodes": [
        {
          "id": "objective_goal",
          "label": "Define project goal",
          "detail": "Clarify the problem and expected result.",
          "tag": "objective",
          "evidence": [
            {"kind": "document", "path": "source.md", "note": "Project goal"}
          ]
        }
      ]
    }
  ],
  "edges": [
    {"from": "objective_goal", "to": "next_node", "label": "guides"}
  ]
}
```

## Practical Rules

- Keep the main route to 4 to 7 stages.
- Keep each stage to 2 to 6 nodes.
- Keep visible labels short.
- Put long explanations in `detail`, Markdown, or HTML.
- Use `evidence` for every node.
- Use `metadata.selected_output_formats` to record the user's explicit choices.

## Layout Values

- `academic-method-framework`: default academic template for papers, defenses, and research reports.
- `proposal-matrix-route`: thesis proposal, grant route, and research-plan route.
- `software-system-route`: software architecture, system engineering, and platform workflow.
- `campaign-strategy-map`: advertising strategy, campaign workflow, channel route, and optimization map.
- `proposal-phase-axis`: legacy long vertical route with a left phase axis; do not use it as the default Gallery/README example.

---

# 路线 Schema

`tech-route.json` 是渲染源文件。修改标题、阶段、节点、连接、风格或输出格式后，可以重新运行 `render_all.py` 生成新的可编辑文件。

## 实用规则

- 主路线建议保留 4 到 7 个阶段。
- 每个阶段建议 2 到 6 个节点。
- 可见标签要短，长解释放在 `detail`、Markdown 或 HTML 面板中。
- 每个节点都应有 `evidence`，或者明确标记为推断。
- `metadata.selected_output_formats` 用来记录用户明确选择的输出格式。
