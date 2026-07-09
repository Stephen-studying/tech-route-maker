# Claude Adapter

Use this repository as a Claude-compatible project context or skill folder.

Read `SKILL.md` first. It is the source of truth for when to use `tech-route-maker`, how to select default presets, when to ask necessary questions, and how to render editable outputs.

When a user asks for a technical route diagram, paper framework figure, engineering route, project roadmap, method flowchart, workflow, pipeline, or editable diagram:

1. Inspect source evidence.
2. Establish `domain_context`: discipline, subfield, project type, research object, method family, data/materials, constraints and evaluation metrics.
3. Read `references/domain-profiles.md` when the discipline is unclear or unfamiliar.
4. Build `tech-route.json`.
5. Choose the closest default preset unless the user asks for advanced options.
6. Run `scripts/validate_route.py`.
7. Render selected formats with `scripts/render_all.py`.
8. Report `QUALITY_REPORT.md` warnings and manual review needs.

If the user asks for copyable Draw.io or diagrams.net code, render `drawio-code` and tell them to paste `tech-route.drawio-code.xml` into [diagrams.net / draw.io](https://app.diagrams.net/) through **Extras > Edit Diagram**.

Ask only when a missing choice would materially change the output. Missing domain context is a reason to ask before final rendering. Do not render screenshots as the main editable output.
