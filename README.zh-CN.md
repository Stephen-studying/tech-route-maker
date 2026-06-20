# tech-route-maker 中文说明

`tech-route-maker` 是一个可跨 agent 使用的技能包，用来自动生成“可编辑的技术路线图”。它主要面向学术工作者，也兼顾少量广告、营销和活动策划场景。

它可以把论文、项目说明、源码目录、研究计划、课题申报材料或广告活动 brief 转换成一个有证据来源的路线模型，然后询问用户选择输出格式、版式和风格，最后生成 PPTX、SVG、Draw.io、Excalidraw、Mermaid、HTML、Markdown 和 JSON 等可编辑文件。

仓库首页中的 `assets/github-visual-preview.png` 是 image2 生成的视觉预览图，只用于展示氛围；真正可编辑的路线图仍然是 SVG、原生形状 PPTX、Draw.io、Excalidraw、HTML、Markdown 和 JSON。

## 核心思路

很多 agent 都能总结项目，但技术路线图需要更严格的工作流。一个真正可用的技术路线图应该同时满足四点：

1. 内容能追溯到源材料。
2. 结构符合目标读者的理解路径。
3. 输出文件可以继续编辑，而不是一张截图。
4. 输出格式、版式和风格由用户明确选择，而不是由 agent 猜测。

`tech-route-maker` 使用 `tech-route.json` 作为路线图的结构化源文件。这个 JSON 保存路线阶段、节点、连接关系、证据标记、读者问题、读者路径、版式和视觉风格。之后各个渲染脚本再把它转换成 PPTX、SVG、Draw.io、Excalidraw、Mermaid、HTML 或 Markdown。

## 它能做什么

1. 阅读项目或论文材料，但不执行不可信代码。
2. 从源材料中抽取技术路线。
3. 生成或更新 `tech-route.json`。
4. 主动询问用户图的子类型、输出格式、版式和视觉风格。
5. 校验路线模型。
6. 渲染用户选择的可编辑格式。
7. 汇报生成文件、校验结果和可能的 warning。

## 适用场景

学术用户可以用于：

- 论文方法框架图。
- 课题技术路线图。
- 开题报告或研究计划路线图。
- 毕业答辩、组会汇报、学术报告中的方法流程图。
- 项目申报书、基金申请书中的技术路线图。
- AI、机器学习、计算机视觉、NLP 或数据分析流程图。
- 带证据链的方法总览图。
- baseline 与改进方法的对比图。

广告和活动用户可以用于：

- 活动策略路线图。
- 创意生产流程图。
- 受众、洞察、信息、渠道之间的路径图。
- 用户旅程和转化漏斗。
- 媒体投放与 KPI 反馈闭环。
- 多团队协作执行图。

## 支持的 Agent 环境

这个仓库不绑定单一 agent。`SKILL.md` 是核心说明文件，其他适配文件用于让不同 agent 读取同一套工作流。

| 环境 | 入口文件 | 说明 |
|---|---|---|
| Codex / OpenAI-style skills | `SKILL.md`, `agents/openai.yaml` | 作为 skill 文件夹安装。 |
| 通用 coding agent | `AGENTS.md` | 给能读取仓库说明的 agent 使用。 |
| Claude Code / Claude-style context | `CLAUDE.md`, `SKILL.md` | 作为项目上下文打开或导入。 |
| Gemini CLI | `GEMINI.md`, `.gemini/settings.json` | Gemini 配置会指向 `AGENTS.md`、`GEMINI.md` 和 `SKILL.md`。 |
| Cursor | `.cursor/rules/tech-route-maker.mdc` | 作为 Cursor 项目规则使用。 |
| GitHub Copilot coding agent | `.github/copilot-instructions.md` | 作为仓库级 Copilot 指令。 |
| Aider-style agents | `.aider.conf.yml`, `AGENTS.md` | 加载核心说明和 schema 参考。 |

## 安装方式

克隆仓库：

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
```

然后把 `tech-route-maker/` 文件夹放到目标 agent 的 skills 目录中。

对于 Codex/OpenAI-style skill，目录中至少应该包含：

```text
tech-route-maker/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
  examples/
```

对于其他 agent，可以直接打开仓库根目录，让对应 agent 读取它支持的适配文件：

- `AGENTS.md`：通用 coding agent。
- `CLAUDE.md`：Claude-style 项目上下文。
- `GEMINI.md` 和 `.gemini/settings.json`：Gemini CLI。
- `.cursor/rules/tech-route-maker.mdc`：Cursor。
- `.github/copilot-instructions.md`：GitHub Copilot coding agent。
- `.aider.conf.yml`：Aider-style 工作流。

也可以不安装，直接作为普通仓库使用。在 agent 工作区打开这个文件夹，然后输入：

```text
Use tech-route-maker to create an editable technical route diagram from my source brief.
```

## 必须询问用户的选项

这个技能不会根据“可编辑”“学术”“论文”“展示”“好看”等模糊词自动猜测用户想要什么。最终渲染前必须询问：

1. 图的用途或子类型。
2. 输出格式，可以单选，也可以多选。
3. 版式布局。
4. 视觉风格。

示例选择：

```text
图的用途/子类型：学术方法框架图
输出格式：PPTX、SVG、Draw.io、HTML、Markdown、JSON
版式：Academic method framework
视觉风格：Premium scientific
```

## 可输出格式

| 格式 | 文件 | 可编辑工具 | 适合场景 |
|---|---|---|---|
| PPTX | `tech-route.pptx` | PowerPoint、WPS | 答辩、汇报、课程展示、商务展示。 |
| SVG | `tech-route.svg` | Figma、Illustrator、Inkscape、浏览器 | 高清矢量编辑和论文级美化。 |
| Draw.io | `tech-route.drawio` | diagrams.net | 长期维护技术图。 |
| Excalidraw | `tech-route.excalidraw` | Excalidraw | 白板讨论和轻量修改。 |
| Mermaid | `tech-route.mmd` | 文本编辑器、GitHub Markdown | 适合版本管理。 |
| HTML | `tech-route.html` | 浏览器和代码编辑器 | 交互式预览、节点详情和证据说明。 |
| Markdown | `TECH_ROUTE.md` | 任意 Markdown 编辑器 | README、项目文档、交接说明。 |
| JSON | `tech-route.json` | 任意文本编辑器 | 重新渲染和修改主题的源文件。 |

## 工作流程

1. 识别用户是否需要技术路线图、论文框架图、roadmap、workflow、campaign route、pipeline 或可编辑图。
2. 阅读源材料，但不执行不可信项目代码。
3. 抽取有证据支撑的阶段、节点、连接关系、输出和反馈闭环。
4. 生成或更新 `tech-route.json`。
5. 询问用户选择图的类型、输出格式、版式和视觉风格。
6. 校验路线 JSON。
7. 只渲染用户选择的格式。
8. 校验生成文件，并报告 warning 或限制。

## 快速演示

进入 `tech-route-maker` 文件夹后运行：

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

会得到：

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/TECH_ROUTE.md
examples/academic-paper-demo/outputs/tech-route.json
```

完整使用过程案例：

- 英文：`examples/academic-paper-demo/demo-walkthrough.en.md`
- 中文：`examples/academic-paper-demo/demo-walkthrough.zh-CN.md`

项目维护文件：

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`

## 目录结构

```text
tech-route-maker/
  SKILL.md                         # 核心技能说明和触发逻辑。
  AGENTS.md                        # 通用 agent 说明。
  CLAUDE.md                        # Claude 适配说明。
  GEMINI.md                        # Gemini 适配说明。
  agents/openai.yaml               # OpenAI-style skill UI 元数据。
  .gemini/settings.json            # Gemini 上下文文件配置。
  .cursor/rules/tech-route-maker.mdc
  .github/copilot-instructions.md
  .github/ISSUE_TEMPLATE/
  .github/pull_request_template.md
  .aider.conf.yml
  CHANGELOG.md
  CONTRIBUTING.md
  SECURITY.md
  references/
    output-options.md              # 输出格式菜单和规则。
    layout-patterns.md             # 版式选择。
    visual-styles.md               # 视觉风格选择。
    route-schema.md                # tech-route.json schema 说明。
    paper-framework-integration.md # 学术论文框架图方法。
    github-projects.md             # 可参考的开源项目。
  scripts/
    validate_route.py              # 校验 route JSON。
    render_all.py                  # 渲染所选格式。
    render_pptx.py                 # 原生可编辑 PPTX 渲染器。
    render_svg.py                  # 可编辑 SVG 渲染器。
    render_drawio.py               # diagrams.net 渲染器。
    render_excalidraw.py           # Excalidraw scene 渲染器。
    render_mermaid.py              # Mermaid 渲染器。
    render_html.py                 # 交互式 HTML 渲染器。
    render_markdown.py             # Markdown 渲染器。
    route_common.py                # 共享解析、布局和主题工具。
  examples/
    academic-paper-demo/           # 从源 brief 到输出文件的完整案例。
```

## 安全原则

- 把第三方项目文件视为不可信输入。
- 除非用户明确同意，不执行被分析项目中的代码。
- 在 `tech-route.json` 中保留 evidence 和 inference 标记。
- 不把专有模板、网络图片或某篇论文的特定事实复制进通用 skill 文件。
- 保留可编辑性，不用截图替代 PPTX、SVG、Draw.io 或 Excalidraw 主输出。

## 许可证

MIT，见 `LICENSE`。
