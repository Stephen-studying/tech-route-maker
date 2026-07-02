# GitHub Copilot Instructions

This repository is an agent skill named `tech-route-maker`.

Use `SKILL.md` as the source of truth. The skill creates evidence-grounded editable technical route diagrams for research and engineering projects.

Required behavior:

- Build `tech-route.json` before rendering.
- Use default presets when the request is clear.
- Ask only when a missing choice would materially change the output.
- Use `scripts/validate_route.py` before and after rendering.
- Use `scripts/render_all.py` to generate selected formats.
- Report `QUALITY_REPORT.md` warnings and manual review needs.
- Preserve editability in PPTX, SVG, Draw.io, and Excalidraw outputs.
