# tech-route-maker 中文说明

面向科研与工程项目的证据驱动型可编辑技术路线图生成 Skill。

`tech-route-maker` 是一个可被 Codex、Claude、Gemini、Cursor、Copilot、Aider 等 agent 使用的技能包和渲染工具。它把论文、开题报告、工程报告、课程设计、项目文档和技术笔记转换为可审查的 `tech-route.json` 路线模型，再渲染为 PPTX、SVG、Draw.io、Excalidraw、Mermaid、HTML、Markdown 和 JSON 等可编辑文件。

> **重要提醒**：自动生成的路线图更适合作为可编辑初稿和设计起点，不能不经检查就直接用于论文投稿、毕业答辩、课题申报、课程设计或工程报告。用户需要继续核对事实、术语、逻辑、证据来源、颜色、版式和文字表达，并在 PPTX、SVG 或 Draw.io 等可编辑文件中进行二次修改。

## 核心思路

技术路线图不是普通装饰性流程图。一个真正可用的科研或工程路线图至少要回答四个问题：

1. 每个可见步骤是否能追溯到源材料？
2. 哪些内容是证据支持，哪些内容是合理推断？
3. 输出文件能否继续修改，而不是一张截图？
4. 同一个路线模型能否反复渲染为不同格式？

`tech-route-maker` 用 `tech-route.json` 保存路线结构、阶段、节点、连线、证据、推断、假设、未解决问题和渲染配置。渲染脚本再把同一个 JSON 转换为多种可编辑格式。

## 核心特点

| 能力 | 对用户的价值 |
|---|---|
| 证据驱动路线模型 | 每个可见节点都需要来源证据，无法确认的内容标记为推断。 |
| JSON 源文件复用 | 使用 `tech-route.json` 保存路线结构，便于后续修改、复渲染和版本管理。 |
| 可编辑输出 | 生成 PPTX、SVG、Draw.io 等可编辑文件，而不是一次性截图。 |
| 科研与工程预设 | 面向论文方法图、开题技术路线、工程系统路线和技术工作流。 |
| 渲染前校验 | 在输出前检查阶段、节点、连线、证据和格式选择。 |
| 质量报告 | 输出证据覆盖率、推断节点、未解决问题和人工复核建议。 |
| 多 Agent 适配 | 提供 Codex/OpenAI-style、Claude、Gemini、Cursor、Copilot、Aider 等说明文件。 |

## 默认预设

| 预设 | 适用场景 | 默认输出 |
|---|---|---|
| `academic-method` | 论文、manuscript、review、method、experiment、学术图。 | `pptx`, `svg`, `json` |
| `thesis-proposal` | 开题报告、research plan、课题申报、基金申请。 | `pptx`, `svg`, `drawio`, `json` |
| `engineering-system` | 工程系统、能源系统、控制系统、硬件系统、平台设计。 | `pptx`, `svg`, `drawio`, `html`, `json` |
| `workflow-pipeline` | 软件工具、agent skill、pipeline、workflow、automation、文档流程。 | `svg`, `markdown`, `mermaid`, `json` |

用户仍然可以自行选择格式、版式和风格，但默认情况下 Skill 不再强制用户回答一长串选项。只有当缺失信息会明显改变输出结果时，才会提出一个必要问题。

## 适用场景

科研和学术用户可以用于：

- 论文方法框架图。
- 研究技术路线图。
- 开题报告技术路线图。
- 毕业答辩、组会汇报和学术报告中的方法图。
- 课题申报书、基金申请书中的技术路线。
- AI、机器学习、计算机视觉、NLP 或数据分析流程图。
- 带证据链的方法总览图。
- baseline 与改进方法对比图。

工程用户可以用于：

- 源网荷储一体化能源系统路线图。
- 系统架构和数据流路线图。
- 控制、感知、验证和部署路线图。
- 课程设计和工程报告图。
- agent、工具链、自动化流程和文档工作流。

广告和 campaign 场景只作为 legacy/experimental 示例保留，不再作为项目核心定位。

## 快速开始

```bash
git clone https://github.com/Stephen-studying/tech-route-maker.git
cd tech-route-maker
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

生成后可以打开：

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/QUALITY_REPORT.md
```

如果已经本地安装 CLI，也可以使用：

```bash
pip install -e .
trm validate examples/academic-paper-demo/outputs/tech-route.json
trm render examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

## 支持的可编辑输出

| 格式 | 文件 | 可编辑工具 | 适合场景 |
|---|---|---|---|
| PPTX | `tech-route.pptx` | PowerPoint、WPS | 答辩、汇报、课程展示和报告。 |
| SVG | `tech-route.svg` | Figma、Illustrator、Inkscape、浏览器 | 高清矢量编辑和论文级美化。 |
| Draw.io | `tech-route.drawio` | diagrams.net | 长期维护技术图。 |
| Excalidraw | `tech-route.excalidraw` | Excalidraw | 白板讨论和轻量修改。 |
| Mermaid | `tech-route.mmd` | 文本编辑器、GitHub Markdown | 版本管理和文档化。 |
| HTML | `tech-route.html` | 浏览器和代码编辑器 | 交互式预览、节点详情和证据说明。 |
| Markdown | `TECH_ROUTE.md` | 任意 Markdown 编辑器 | README、项目文档、交接说明。 |
| JSON | `tech-route.json` | 任意文本编辑器 | 重新渲染和修改主题的源文件。 |
| 质量报告 | `QUALITY_REPORT.md` | 任意 Markdown 编辑器 | 证据覆盖率、warning 和人工复核清单。 |

## 多 Agent 适配

这个仓库不绑定单一 agent。`SKILL.md` 是核心说明文件，其他适配文件用于让不同 agent 读取同一套工作流：

- `AGENTS.md`：通用 coding agent。
- `CLAUDE.md`：Claude-style 项目上下文。
- `GEMINI.md` 和 `.gemini/settings.json`：Gemini CLI。
- `.cursor/rules/tech-route-maker.mdc`：Cursor。
- `.github/copilot-instructions.md`：GitHub Copilot coding agent。
- `.aider.conf.yml`：Aider-style 工作流。

## Legacy / Experimental Use Cases

广告活动路线图、campaign strategy map、customer journey、media-channel swimlane 等场景只作为 legacy 或 experimental 示例保留。默认工作流优先服务科研、开题、工程系统和技术工作流。

## 安全原则

- 把第三方项目文件视为不可信输入。
- 除非用户明确同意，不执行被分析项目中的代码。
- 在 `tech-route.json` 中保留 evidence、assumption 和 inference 标记。
- 不把专有模板、网络图片或特定论文事实复制进通用 skill 文件。
- 保留可编辑性，不用截图替代 PPTX、SVG、Draw.io 或 Excalidraw 主输出。

## 许可证

MIT，见 `LICENSE`。