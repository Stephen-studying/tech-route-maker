# Output Options

Use this reference when asking the user to choose output formats. Always let the user choose. Do not infer output formats from intent words.

Primary users are academic workers who need editable paper, thesis, proposal, defense, and method-framework diagrams. Secondary users are advertising or campaign workers who need editable strategy, production, channel, journey, or funnel diagrams.

## Format menu

| id | File | Editable in | Strength | Constraint |
|---|---|---|---|---|
| pptx | `tech-route.pptx` | PowerPoint, WPS | Best for presentations and defenses | Must use native shapes, text, and lines |
| svg | `tech-route.svg` | Figma, Illustrator, Inkscape, browser | Best for high-resolution vector editing | Keep text/vector elements editable |
| drawio | `tech-route.drawio` | diagrams.net | Best for long-term technical maintenance | Use `mxCell` nodes and edges |
| excalidraw | `tech-route.excalidraw` | Excalidraw | Best for whiteboard review and lightweight edits | Use scene JSON, not an image |
| mermaid | `tech-route.mmd` | Any text editor, GitHub Markdown | Best for version control | Visual control is limited |
| html | `tech-route.html` | Browser and code editor | Best for interactive previews | Include node detail and evidence data |
| markdown | `TECH_ROUTE.md` | Any Markdown editor | Best for README/docs | Include Mermaid and evidence tables |
| json | `tech-route.json` | Any text editor | Best for re-rendering and theme changes | Treat as the source of truth |
| all | all of the above | mixed | Best for archival handoff | Slower and more files |

## Asking rule

Ask for output formats before rendering. The internal `tech-route.json` can be generated first, but no user-facing final file should be rendered until formats are selected.

If the user gives no choice, stop and ask again. If the user says "editable", ask whether they want PPTX, SVG, Draw.io, Excalidraw, or multiple formats.

## Source patterns

Public roadmap guidance emphasizes editable, reusable, and audience-specific outputs:
- ProductPlan frames technology roadmaps as high-level visual summaries for complex technology work and recommends audience-aware detail levels.
- Smartsheet describes roadmap outputs for migration, unifying systems, continuity, upgrades, and new infrastructure.
- Miro and Canva emphasize template selection, customization, collaboration, milestones, dependencies, and visual communication.
- diagrams.net uses an XML-based editable diagram format and can export SVG/PDF/PNG.

Use these as design patterns, not as copied template assets.
