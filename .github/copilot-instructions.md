# GitHub Copilot Instructions

This repository is an agent skill named `tech-route-maker`.

Use `SKILL.md` as the source of truth. The skill creates evidence-grounded editable technical route diagrams for research and engineering projects.

Required behavior:

- Build `tech-route.json` before rendering.
- Establish `domain_context` before final rendering: discipline, subfield, project type, research object, method family, data/materials, constraints and evaluation metrics.
- Read `references/domain-profiles.md` when the discipline is unclear or unfamiliar.
- Use default presets when the request is clear.
- Ask only when a missing choice would materially change the output; missing domain context is such a case.
- Use `scripts/validate_route.py` before and after rendering.
- Use `scripts/render_all.py` to generate selected formats.
- Report `QUALITY_REPORT.md` warnings and manual review needs.
- Preserve editability in PPTX, SVG, Draw.io, and Excalidraw outputs.
- If the user asks for copyable Draw.io or diagrams.net code, generate `drawio-code` and mention [diagrams.net / draw.io](https://app.diagrams.net/) with **Extras > Edit Diagram**.
