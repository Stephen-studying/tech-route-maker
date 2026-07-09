# Gemini Adapter

Use `SKILL.md` as the primary instruction file for `tech-route-maker`.

This project is a portable skill for generating evidence-grounded editable technical route diagrams for research and engineering workflows.

Mandatory flow:

1. Read `SKILL.md`.
2. Use `references/route-schema.md` for `tech-route.json`.
3. Establish `domain_context` before final rendering: discipline, subfield, project type, research object, method family, data/materials, constraints and evaluation metrics.
4. Read `references/domain-profiles.md` when the discipline is unclear or unfamiliar.
5. Choose the closest default preset when the request is clear.
6. Ask only when a missing choice would materially change the output; missing domain context is such a case.
7. Render selected formats with:

```bash
python scripts/render_all.py <route-json> <output-dir> --formats <formats>
```

8. Validate with:

```bash
python scripts/validate_route.py <route-json>
```

Do not force a long option list by default. Keep PPTX, SVG, Draw.io and Excalidraw outputs editable.

When the user asks for copyable Draw.io or diagrams.net code, include `drawio-code` and explain that `tech-route.drawio-code.xml` can be pasted into [diagrams.net / draw.io](https://app.diagrams.net/) with **Extras > Edit Diagram**.
