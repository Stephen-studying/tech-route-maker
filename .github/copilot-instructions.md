# GitHub Copilot Instructions

This repository is an agent skill named `tech-route-maker`.

Use `SKILL.md` as the source of truth. The skill creates editable technical route diagrams for academic workers and advertising/campaign teams.

Required behavior:

- Build `tech-route.json` before rendering.
- Ask the user to choose figure purpose/subtype, output formats, layout, and visual style.
- Do not infer those options from ambiguous user wording.
- Use `scripts/validate_route.py` before and after rendering.
- Use `scripts/render_all.py` to generate selected formats.
- Preserve editability in PPTX, SVG, Draw.io, and Excalidraw outputs.
