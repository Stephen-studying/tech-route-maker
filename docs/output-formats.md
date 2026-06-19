# Output Formats

| Format | File | Editable in | Use when |
|---|---|---|---|
| PPTX | `tech-route.pptx` | PowerPoint, WPS | The user needs slides, defense material, or business presentation edits. |
| SVG | `tech-route.svg` | Figma, Illustrator, Inkscape, browser | The user needs high-resolution vector editing. |
| Draw.io | `tech-route.drawio` | diagrams.net | The diagram must be maintained as a technical diagram. |
| Excalidraw | `tech-route.excalidraw` | Excalidraw | The team wants a whiteboard-style editable scene. |
| Mermaid | `tech-route.mmd` | Text editor, GitHub Markdown | Version control and simple docs matter more than precise layout. |
| HTML | `tech-route.html` | Browser and code editor | The user wants an interactive preview with details. |
| Markdown | `TECH_ROUTE.md` | Markdown editor | The route belongs in README or docs. |
| JSON | `tech-route.json` | Text editor | The user wants to rerender or change themes later. |

## Selection Rule

Do not infer output from vague words such as "editable", "paper", or "presentation". Ask the user to choose one or more formats.

## Recommended Bundles

- Academic paper figure: `svg,json,markdown`
- Thesis defense: `pptx,svg,html,json`
- Engineering handoff: `drawio,html,markdown,json`
- Campaign planning: `pptx,drawio,html,json`
- Full archive: `pptx,svg,drawio,excalidraw,mermaid,html,markdown,json`

---

# 输出格式

用户可以单选，也可以多选。默认建议保留 `json`，因为它是重新渲染和修改主题的源文件。
