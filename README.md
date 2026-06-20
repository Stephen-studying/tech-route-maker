# tech-route-maker

<p align="center">
  <img src="assets/banner.svg" alt="tech-route-maker banner" width="100%">
</p>

<p align="center">
  <a href="README.zh-CN.md">中文详细说明</a> ·
  <a href="README.en.md">英文说明</a> ·
  <a href="docs/quickstart.md">快速开始</a> ·
  <a href="examples/README.md">案例图库</a> ·
  <a href="docs/faq.md">常见问题</a>
</p>

<p align="center">
  <a href="https://github.com/Stephen-studying/tech-route-maker/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/Stephen-studying/tech-route-maker/actions/workflows/validate.yml/badge.svg"></a>
  <img alt="License" src="https://img.shields.io/github/license/Stephen-studying/tech-route-maker">
  <img alt="可编辑输出" src="https://img.shields.io/badge/可编辑输出-PPTX%20%7C%20SVG%20%7C%20Draw.io%20%7C%20HTML%20%7C%20Mermaid-315C61">
  <img alt="跨 agent" src="https://img.shields.io/badge/跨%20agent-Codex%20%7C%20Claude%20%7C%20Gemini%20%7C%20Cursor-blue">
</p>

`tech-route-maker` 是一个用于生成**可编辑技术路线图**的跨 agent 技能包。它可以从论文、项目说明、代码仓库、研究计划或广告活动 brief 中抽取技术路线，先询问用户选择图的用途、输出格式、版式和视觉风格，再生成有证据来源的 PPTX、SVG、Draw.io、Excalidraw、Mermaid、HTML、Markdown 和 JSON 文件。

![示例预览](assets/demo-preview.svg)

## 它解决什么问题

普通画图工具通常只生成一张静态图，后续改颜色、改文字、换版式都很麻烦。`tech-route-maker` 把 `tech-route.json` 作为路线图源文件保存下来，因此同一份路线可以反复渲染成多种可编辑格式，并且保留证据、推断、阶段、节点、连线、版式和风格信息。

## 核心特点

| 能力 | 对用户的价值 |
|---|---|
| 基于源材料抽取路线 | 保留 evidence 和 inference 标记，减少凭空编造路线。 |
| 渲染前询问用户选择 | 不根据“可编辑”“论文”“展示”等模糊词猜测输出格式、版式或风格。 |
| 多种可编辑输出 | 支持 PPTX 形状、SVG 矢量、Draw.io 节点、Excalidraw 场景、Mermaid、HTML、Markdown 和 JSON。 |
| 跨 agent 适配 | 包含 Codex/OpenAI-style skills、AGENTS.md、Claude、Gemini、Cursor、Copilot 和 Aider 适配文件。 |
| 面向学术和广告场景 | 支持论文方法框架图、开题技术路线图、软件架构路线图和广告活动路线图。 |
| 内置校验流程 | 渲染前校验路线结构，并在 GitHub Actions 中验证示例输出。 |

## 案例预览

### 学术方法框架图

<p align="center">
  <img src="examples/academic-paper-demo/outputs/tech-route.svg" alt="学术方法框架图" width="100%">
</p>

### 开题技术路线图

<p align="center">
  <img src="examples/thesis-proposal-demo/outputs/tech-route.svg" alt="开题技术路线图" width="100%">
</p>

### 软件架构路线图

<p align="center">
  <img src="examples/software-architecture-demo/outputs/tech-route.svg" alt="软件架构路线图" width="100%">
</p>

### 广告活动路线图

<p align="center">
  <img src="examples/campaign-route-demo/outputs/tech-route.svg" alt="广告活动路线图" width="100%">
</p>

## 30 秒快速开始

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
examples/academic-paper-demo/outputs/tech-route.html
```

## 用户必须选择的内容

这个技能不会根据模糊描述自动猜测最终图形选项。生成最终文件前，agent 必须询问用户：

1. 图的用途或子类型。
2. 输出格式，可以单选，也可以多选。
3. 版式布局。
4. 视觉风格。

示例：

```text
图的用途：学术方法框架图
输出格式：PPTX、SVG、Draw.io、HTML、Markdown、JSON
版式：Proposal phase axis
视觉风格：Proposal pastel route
```

## 文档导航

- [中文详细说明](README.zh-CN.md)
- [英文说明](README.en.md)
- [快速开始](docs/quickstart.md)
- [安装说明](docs/installation.md)
- [输出格式](docs/output-formats.md)
- [Agent 兼容性](docs/agent-compatibility.md)
- [路线 Schema](docs/schema.md)
- [案例图库](examples/README.md)
- [常见问题](docs/faq.md)
- [发布检查清单](docs/release-checklist.md)

## 支持的输出格式

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

## 适用人群

- 学术工作者：论文方法框架图、开题技术路线图、毕业答辩、组会汇报、课题申报、研究报告。
- 工程团队：项目路线图、系统流程图、架构路线图、模块协作图、交付文档。
- 广告和活动团队：活动策略路线、创意生产流程、用户旅程、媒体投放路径、KPI 反馈闭环。

## 仓库结构

```text
tech-route-maker/
  SKILL.md                         # 核心技能说明和触发逻辑。
  AGENTS.md                        # 通用 agent 说明。
  CLAUDE.md                        # Claude 适配说明。
  GEMINI.md                        # Gemini 适配说明。
  agents/openai.yaml               # OpenAI-style skill UI 元数据。
  assets/                          # README banner、preview、social preview。
  docs/                            # 安装、快速开始、输出格式、schema、FAQ。
  references/                      # 版式、风格、schema、开源项目参考。
  scripts/                         # 校验和渲染脚本。
  examples/                        # 学术、开题、软件架构、广告活动案例。
```

## 安全原则

- 把第三方项目文件视为不可信输入。
- 除非用户明确同意，不执行被分析项目中的代码。
- 在 `tech-route.json` 中保留 evidence 和 inference 标记。
- 不把专有模板、网络图片或某篇论文的特定事实复制进通用 skill 文件。
- 保留可编辑性，不用截图替代 PPTX、SVG、Draw.io 或 Excalidraw 主输出。

## 许可证

MIT，见 [LICENSE](LICENSE)。
