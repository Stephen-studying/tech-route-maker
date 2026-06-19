# Release Checklist

Use this checklist before creating a GitHub release.

## Validation

- [ ] `python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json`
- [ ] `python scripts/validate_route.py examples/thesis-proposal-demo/outputs/tech-route.json`
- [ ] `python scripts/validate_route.py examples/software-architecture-demo/outputs/tech-route.json`
- [ ] `python scripts/validate_route.py examples/campaign-route-demo/outputs/tech-route.json`
- [ ] Python source compile check.
- [ ] Generated PPTX/SVG/Draw.io/JSON parse check.

## Documentation

- [ ] `README.md` shows gallery and quick start.
- [ ] `README.en.md` and `README.zh-CN.md` point to examples.
- [ ] `docs/` pages are current.
- [ ] `examples/README.md` lists all demos.

## GitHub Surface

- [ ] Add repository description.
- [ ] Add topics: `agent-skill`, `diagram-generator`, `pptx`, `svg`, `drawio`, `mermaid`, `academic-writing`, `roadmap`, `workflow`, `ai-agents`.
- [ ] Add social preview image from `assets/social-preview.svg` or a PNG export.
- [ ] Create tag `v0.1.0`.
- [ ] Publish release notes from `CHANGELOG.md`.
