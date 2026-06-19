# Claude Adapter

Use this repository as a Claude-compatible project context or skill folder.

Read `SKILL.md` first. It is the source of truth for when to use `tech-route-maker`, how to ask required user choices, and how to render editable outputs.

When a user asks for a technical route diagram, paper framework figure, project roadmap, method flowchart, campaign route, workflow, pipeline, or editable diagram:

1. Inspect source evidence.
2. Build `tech-route.json`.
3. Ask the user to choose figure subtype, output format(s), layout, and visual style.
4. Run `scripts/validate_route.py`.
5. Render selected formats with `scripts/render_all.py`.

Do not infer output options. Do not render screenshots as the main editable output.
