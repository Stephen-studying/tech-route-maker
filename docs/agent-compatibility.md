# Agent Compatibility

`tech-route-maker` is agent-agnostic. `SKILL.md` is the source of truth; adapter files tell different agents how to find and use that workflow.

| Agent environment | File |
|---|---|
| Codex / OpenAI-style skills | `SKILL.md`, `agents/openai.yaml` |
| Generic coding agents | `AGENTS.md` |
| Claude-style context | `CLAUDE.md` |
| Gemini CLI | `GEMINI.md`, `.gemini/settings.json` |
| Cursor | `.cursor/rules/tech-route-maker.mdc` |
| GitHub Copilot coding agent | `.github/copilot-instructions.md` |
| Aider-style agents | `.aider.conf.yml` |

## Required Agent Behavior

Every compatible agent should:

1. Read `SKILL.md`.
2. Inspect source evidence without executing untrusted code.
3. Build or update `tech-route.json`.
4. Ask the user to choose figure subtype, formats, layout, and style.
5. Validate the route.
6. Render only selected outputs.

---

# Agent 兼容性

核心原则：不同 agent 可以有不同入口文件，但都应回到同一个 `SKILL.md` 和同一个 `tech-route.json` 工作流。
