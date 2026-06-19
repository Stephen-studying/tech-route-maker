# 完整案例：学术方法框架图

这个案例展示用户从“提供一个简短学术项目 brief”到“获得可编辑技术路线图”的完整过程。流程包括：用户提出需求、agent 阅读源材料、agent 询问必要选项、生成结构化路线模型、校验路线、渲染多个可编辑输出。

## 1. 场景

用户想为一个“多模态光伏组件缺陷检测”学术项目生成一张可编辑技术路线图。

源文件是：

```text
examples/academic-paper-demo/source/project-brief.md
```

这个 brief 是合成的入门示例，不是真实论文。

## 2. 用户输入

用户可以这样说：

```text
Use tech-route-maker to create a technical route diagram for examples/academic-paper-demo/source/project-brief.md.
```

如果 agent 支持直接调用 skill，也可以这样说：

```text
Use $tech-route-maker to create an editable technical route diagram from examples/academic-paper-demo/source/project-brief.md.
```

## 3. Agent 理解源材料

agent 阅读 brief 后，抽取出下面的证据：

| 证据区域 | 抽取内容 |
|---|---|
| 项目目标 | 为多模态光伏组件缺陷检测项目创建方法总览图。 |
| 输入数据 | RGB 组件图像和红外热图像。 |
| 数据准备 | 质量筛选、配准、标注、增强、训练/验证/测试集划分。 |
| 核心方法 | baseline 检测器、多模态特征融合、注意力增强特征提取、损失函数和指标驱动优化。 |
| 训练与推理 | 监督训练、验证监控、未见图像推理、置信度筛选。 |
| 评估验证 | baseline 对比、模块消融、precision、recall、mAP 和定性缺陷图。 |
| 输出结果 | 缺陷类别、位置、置信度和可用于报告的可视化结果。 |

## 4. 必须询问用户的选项

skill 不能直接猜测最终输出选项，必须询问：

```text
1. 图的用途或子类型
2. 输出格式，可以单选或多选
3. 版式布局
4. 视觉风格
```

本案例中，用户选择：

```text
图的用途/子类型：
学术方法框架图

输出格式：
PPTX、SVG、Draw.io、HTML、Markdown、JSON

版式：
AI 或算法 pipeline

视觉风格：
Premium scientific
```

## 5. 生成路线模型

结构化源文件是：

```text
examples/academic-paper-demo/outputs/tech-route.json
```

读者问题：

```text
该方法如何从多模态图像输入走向可验证的缺陷检测结果？
```

读者阅读路径：

```text
研究目标 -> 数据构建 -> 预处理 -> 核心方法 -> 训练推理 -> 验证输出
```

路线模型中的每个阶段、节点和连接关系都可以继续修改。用户后续可以编辑 `tech-route.json`，再重新渲染出新的 PPTX、SVG 或 Draw.io 文件。

## 6. 校验

在 `tech-route-maker` 文件夹中运行：

```bash
python scripts/validate_route.py examples/academic-paper-demo/outputs/tech-route.json
```

预期结果：

```text
Validation passed with 0 warning(s).
```

## 7. 渲染

渲染用户选择的格式：

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio,html,markdown,json
```

生成的可编辑输出：

```text
examples/academic-paper-demo/outputs/tech-route.pptx
examples/academic-paper-demo/outputs/tech-route.svg
examples/academic-paper-demo/outputs/tech-route.drawio
examples/academic-paper-demo/outputs/tech-route.html
examples/academic-paper-demo/outputs/TECH_ROUTE.md
examples/academic-paper-demo/outputs/tech-route.json
```

## 8. 用户如何继续修改

用户可以直接修改这些输出：

- 用 PowerPoint 或 WPS 打开 `tech-route.pptx`，修改文字、颜色、形状、连接线和布局。
- 用 Figma、Illustrator、Inkscape 或浏览器 SVG 编辑器打开 `tech-route.svg`。
- 用 diagrams.net 打开 `tech-route.drawio`。
- 用浏览器打开 `tech-route.html`，查看交互式预览和节点说明。
- 修改 `TECH_ROUTE.md`，作为项目文档或 README 内容。
- 修改 `tech-route.json`，调整路线、风格、版式、节点，再重新渲染。

修改风格后重新渲染的例子：

```bash
python scripts/render_all.py examples/academic-paper-demo/outputs/tech-route.json examples/academic-paper-demo/outputs --formats pptx,svg,drawio
```

## 9. 交付前检查清单

交付给用户前，agent 应确认：

- `tech-route.json` 校验通过。
- 用户选择的输出文件都已生成。
- PPTX、SVG、Draw.io 和 JSON 可以正常解析。
- 主要标签仍然是可编辑文字，而不是截图。
- 图中没有声称源材料中不存在的证据。
- 输出格式、版式和视觉风格符合用户明确选择。
