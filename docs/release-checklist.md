# Release Checklist

Use this checklist before creating a GitHub release.

## Validation

- [ ] `python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json`
- [ ] `python scripts/validate_route.py examples/thesis-proposal-demo/outputs/tech-route.json`
- [ ] `python scripts/validate_route.py examples/engineering-energy-system-demo/outputs/tech-route.json`
- [ ] `python scripts/validate_route.py examples/agent-workflow-demo/outputs/tech-route.json`
- [ ] Python source compile check for `scripts/*.py` and `tech_route_maker/*.py`.
- [ ] `pip install -e .`
- [ ] `trm --help`
- [ ] `trm doctor`
- [ ] `trm validate examples/academic-paper-demo/outputs/tech-route.json`
- [ ] `trm render examples/academic-paper-demo/outputs/tech-route.json /tmp/academic --formats pptx,svg,drawio,html,markdown,json`
- [ ] Legacy scripts still render representative outputs.
- [ ] Generated PPTX/SVG/Draw.io/JSON parse check.
- [ ] `QUALITY_REPORT.md` exists in each core demo output directory.

## Documentation

- [ ] `README.md` states the research and engineering positioning in the first screen.
- [ ] `README.md` does not present advertising as a core scenario.
- [ ] `README.en.md` and `README.zh-CN.md` match the same information structure.
- [ ] `docs/quickstart.md`, `docs/schema.md`, `docs/output-formats.md` and `docs/faq.md` are current.
- [ ] `examples/README.md` lists the four core demos.
- [ ] `docs/release-notes-v0.2.0.md` is ready for GitHub Releases.

## GitHub Surface

- [ ] Repository description: `Evidence-grounded editable technical route diagrams for research and engineering projects.`
- [ ] Topics: `agent-skill`, `technical-route`, `diagram-generator`, `research-diagram`, `engineering-diagram`, `pptx`, `svg`, `drawio`, `mermaid`, `academic-writing`, `ai-agents`, `workflow`.
- [ ] Social preview uses `assets/social-preview.svg` or a PNG export.
- [ ] Create tag `v0.2.0`.
- [ ] Publish release title: `v0.2.0 - Research and Engineering Focus`.
- [ ] Publish release notes from `docs/release-notes-v0.2.0.md`.