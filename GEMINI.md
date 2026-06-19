# Gemini Adapter

Use `SKILL.md` as the primary instruction file for `tech-route-maker`.

This project is a portable skill for generating editable technical route diagrams for academic and advertising/campaign workflows.

Mandatory flow:

1. Read `SKILL.md`.
2. Use `references/route-schema.md` for `tech-route.json`.
3. Ask the user to explicitly choose:
   - figure purpose/subtype;
   - output format(s);
   - layout;
   - visual style.
4. Render selected formats with:

```bash
python scripts/render_all.py <route-json> <output-dir> --formats <formats>
```

5. Validate with:

```bash
python scripts/validate_route.py <route-json>
```

Do not guess output format, layout, or style from user wording.
