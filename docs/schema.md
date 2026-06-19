# Route Schema

`tech-route.json` is the source of truth for rendering.

## Minimal Structure

```json
{
  "title": "Project Technical Route",
  "subtitle": "Editable route diagram",
  "layout": "horizontal-stages",
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

---

# 路线 Schema

`tech-route.json` 是渲染源文件。修改标题、阶段、节点、连接、风格或输出格式后，可以重新运行 `render_all.py` 生成新的可编辑文件。
