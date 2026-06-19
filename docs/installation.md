# Installation

`tech-route-maker` can be used as a skill folder, a repository context, or a normal local rendering toolkit.

## Codex / OpenAI-Style Skill

Place the repository folder under the agent's skills directory:

```text
skills/
  tech-route-maker/
    SKILL.md
    agents/openai.yaml
    scripts/
    references/
    examples/
```

Then ask:

```text
Use $tech-route-maker to create an editable technical route diagram from my source.
```

## Generic Agent Context

Open the repository root in the agent. The agent should read:

- `AGENTS.md`
- `SKILL.md`
- relevant files under `references/`

## Claude, Gemini, Cursor, Copilot, Aider

Use the adapter files already included in the repository:

- `CLAUDE.md`
- `GEMINI.md`
- `.gemini/settings.json`
- `.cursor/rules/tech-route-maker.mdc`
- `.github/copilot-instructions.md`
- `.aider.conf.yml`

## Local Rendering Toolkit

No package installation is required for the included renderers. They use Python standard-library functionality.

```bash
python scripts/validate_route.py <route-json>
python scripts/render_all.py <route-json> <output-dir> --formats pptx,svg,drawio,html,markdown,json
```

---

# 安装说明

这个仓库可以作为 skill 文件夹、agent 项目上下文，也可以作为普通本地渲染工具包使用。核心入口是 `SKILL.md`，不同 agent 的适配文件已经放在仓库中。
