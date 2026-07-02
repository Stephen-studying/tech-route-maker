# Gemini Adapter

Use `SKILL.md` as the primary instruction file for `tech-route-maker`.

This project is a portable skill for generating evidence-grounded editable technical route diagrams for research and engineering workflows.

Mandatory flow:

1. Read `SKILL.md`.
2. Use `references/route-schema.md` for `tech-route.json`.
3. Choose the closest default preset when the request is clear.
4. Ask only when a missing choice would materially change the output.
5. Render selected formats with:

```bash
python scripts/render_all.py <route-json> <output-dir> --formats <formats>
```

6. Validate with:

```bash
python scripts/validate_route.py <route-json>
```

Do not force a long option list by default. Keep PPTX, SVG, Draw.io and Excalidraw outputs editable.
