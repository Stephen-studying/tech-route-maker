# Claude Adapter

Use this repository as a Claude-compatible project context or skill folder.

Read `SKILL.md` first. It is the source of truth for when to use `tech-route-maker`, how to select default presets, when to ask necessary questions, and how to render editable outputs.

When a user asks for a technical route diagram, paper framework figure, engineering route, project roadmap, method flowchart, workflow, pipeline, or editable diagram:

1. Inspect source evidence.
2. Build `tech-route.json`.
3. Choose the closest default preset unless the user asks for advanced options.
4. Run `scripts/validate_route.py`.
5. Render selected formats with `scripts/render_all.py`.
6. Report `QUALITY_REPORT.md` warnings and manual review needs.

Ask only when a missing choice would materially change the output. Do not render screenshots as the main editable output.
