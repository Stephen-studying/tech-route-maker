"""Reusable structural templates for editable technical-route diagrams."""

from copy import deepcopy


TEMPLATE_LIBRARY = {
    "cn-three-column-research-framework": {
        "name_zh": "三栏科研框架图",
        "name_en": "Three-column research framework",
        "description_zh": "左侧研究逻辑、中部研究内容、右侧研究方法，适合开题、基金、论文和项目申请。",
        "layout": "cn-three-column-research-framework",
        "style": "cn-classic-research-framework",
        "outputs": ["pptx", "svg", "drawio", "html", "json"],
        "stage_range": [4, 6],
        "nodes_per_stage": [2, 3],
        "aspect": "near-square portrait",
        "source_family": "clean-room reconstruction from common Chinese academic route grammar",
    },
    "cn-horizontal-defense-mainline": {
        "name_zh": "横向答辩主线图",
        "name_en": "Horizontal defense mainline",
        "description_zh": "五阶段横向主线与支撑任务，适合 16:9 答辩 PPT。",
        "layout": "cn-ppt-mainline-route",
        "style": "research-ppt-blue",
        "outputs": ["pptx", "svg", "drawio", "html", "json"],
        "stage_range": [4, 6],
        "nodes_per_stage": [2, 3],
        "aspect": "16:9 landscape",
        "source_family": "academic presentation mainline",
    },
    "cn-a4-stacked-research": {
        "name_zh": "A4 竖向分阶段图",
        "name_en": "A4 stacked research route",
        "description_zh": "居中阶段标题与纵向流程，适合论文、Word 和项目书正文。",
        "layout": "cn-a4-stage-route",
        "style": "cn-polished-pastel-academic",
        "outputs": ["pptx", "svg", "drawio", "html", "json"],
        "stage_range": [4, 7],
        "nodes_per_stage": [2, 3],
        "aspect": "A4 portrait",
        "source_family": "stacked academic report route",
    },
    "cn-method-matrix-board": {
        "name_zh": "研究方法矩阵图",
        "name_en": "Research method matrix",
        "description_zh": "按研究目标、数据、方法、验证和输出分区，适合论文方法总览。",
        "layout": "cn-research-method-matrix",
        "style": "cn-blue-green-proposal",
        "outputs": ["pptx", "svg", "drawio", "html", "json"],
        "stage_range": [4, 7],
        "nodes_per_stage": [2, 4],
        "aspect": "portrait matrix",
        "source_family": "academic method matrix",
    },
    "cn-monochrome-review-route": {
        "name_zh": "黑白评审线框图",
        "name_en": "Monochrome reviewer route",
        "description_zh": "黑白线框、低装饰、高打印兼容，适合正式申报书和审稿附件。",
        "layout": "cn-monochrome-linework-route",
        "style": "cn-reviewer-linework",
        "outputs": ["pptx", "svg", "drawio", "html", "json"],
        "stage_range": [4, 7],
        "nodes_per_stage": [2, 3],
        "aspect": "portrait",
        "source_family": "formal monochrome linework",
    },
    "cn-engineering-layer-map": {
        "name_zh": "工程系统分层图",
        "name_en": "Engineering layer map",
        "description_zh": "系统边界、数据或能量流、服务层、验证层分明，适合工程项目。",
        "layout": "cn-wide-project-map",
        "style": "cn-blue-green-proposal",
        "outputs": ["pptx", "svg", "drawio", "html", "json"],
        "stage_range": [4, 7],
        "nodes_per_stage": [2, 4],
        "aspect": "wide landscape",
        "source_family": "engineering layered system route",
    },
}


THREE_COLUMN_STAGE_DEFAULTS = [
    {
        "logic_label": "提出问题",
        "content_label": "项目立项",
        "method_label": "文献调研与理论分析法",
        "nodes": ["研究背景与现实需求", "关键科学或工程问题", "总体目标与研究假设"],
    },
    {
        "logic_label": "分析问题\n（对象构建）",
        "content_label": "对象构建",
        "method_label": "实验研究与数据获取法",
        "nodes": ["研究对象或样本获取", "实验材料与数据准备"],
    },
    {
        "logic_label": "分析问题\n（性能表征）",
        "content_label": "性能表征",
        "method_label": "仪器表征与指标测试法",
        "nodes": ["关键结构与特征表征", "核心性能与指标测试", "对照实验与差异分析"],
    },
    {
        "logic_label": "分析问题\n（机理探究）",
        "content_label": "机理验证",
        "method_label": "机理分析与对比验证法",
        "nodes": ["关键机制或作用路径分析", "模型、实验或消融验证", "结果解释与稳健性检验"],
    },
    {
        "logic_label": "解决问题\n（优化评价）",
        "content_label": "优化应用",
        "method_label": "综合评价法",
        "nodes": ["关键参数与方案优化", "综合效果与适用性评价", "成果输出与应用建议"],
    },
]


GENERIC_TEMPLATE_STAGE_DEFAULTS = {
    "cn-horizontal-defense-mainline": [
        ("基础分析", ["研究对象与边界", "关键数据与条件"]),
        ("方案设计", ["核心技术方案", "关键参数配置"]),
        ("系统建模", ["模型或系统构建", "约束与接口定义"]),
        ("仿真验证", ["场景实验与对照", "指标测试与分析"]),
        ("评价应用", ["综合评价与优化", "成果输出与建议"]),
    ],
    "cn-a4-stacked-research": [
        ("01 基础分析", ["研究背景与问题", "对象、数据或材料"]),
        ("02 方案设计", ["总体研究方案", "关键方法与技术"]),
        ("03 实施过程", ["实验、建模或开发", "过程控制与记录"]),
        ("04 验证分析", ["对照与指标测试", "结果与稳健性分析"]),
        ("05 成果输出", ["结论与方案优化", "应用建议与交付物"]),
    ],
    "cn-method-matrix-board": [
        ("研究目标", ["核心问题界定", "预期目标与假设"]),
        ("数据材料", ["样本、数据或材料", "预处理与质量控制"]),
        ("核心方法", ["关键方法与模型", "实验或实现流程"]),
        ("验证评价", ["对照、消融或验证", "评价指标与统计分析"]),
        ("成果输出", ["主要结果与结论", "应用、论文或工程交付"]),
    ],
    "cn-monochrome-review-route": [
        ("问题与依据", ["研究问题与现实依据", "文献与理论基础"]),
        ("研究设计", ["研究对象与变量", "总体技术方案"]),
        ("实施与分析", ["实验、调查或建模", "数据处理与结果分析"]),
        ("验证与复核", ["对照与稳健性检验", "风险与质量控制"]),
        ("结论与应用", ["结论、局限与改进", "成果输出与应用建议"]),
    ],
    "cn-engineering-layer-map": [
        ("系统边界", ["工程对象与输入", "运行条件与约束"]),
        ("数据与感知", ["数据采集与治理", "状态识别与预测"]),
        ("模型与服务", ["核心模型或服务", "接口与模块协同"]),
        ("控制与执行", ["决策、控制与调度", "执行反馈与异常处理"]),
        ("验证与交付", ["场景验证与指标评价", "系统方案与工程交付"]),
    ],
}


def get_template(template_id):
    if template_id not in TEMPLATE_LIBRARY:
        supported = ", ".join(sorted(TEMPLATE_LIBRARY))
        raise ValueError(f"Unknown template '{template_id}'. Supported templates: {supported}")
    return deepcopy(TEMPLATE_LIBRARY[template_id])


def template_stage_skeleton(template_id, source_path="source.md"):
    if template_id == "cn-three-column-research-framework":
        source = [
            (default["content_label"], default["nodes"], default)
            for default in THREE_COLUMN_STAGE_DEFAULTS
        ]
    else:
        defaults = GENERIC_TEMPLATE_STAGE_DEFAULTS.get(template_id)
        if not defaults:
            return None
        source = [(title, nodes, None) for title, nodes in defaults]

    stages = []
    for stage_index, (title, labels, special) in enumerate(source, start=1):
        nodes = []
        for node_index, label in enumerate(labels, start=1):
            node_id = f"stage_{stage_index}_content_{node_index}"
            nodes.append(
                {
                    "id": node_id,
                    "label": label,
                    "detail": "Replace this placeholder with source-grounded project content.",
                    "tag": "template-placeholder",
                    "node_type": "content",
                    "confidence": "low",
                    "is_inferred": True,
                    "evidence": [],
                }
            )
        stage = {
            "id": f"stage_{stage_index}",
            "title": title,
            "order": stage_index,
            "nodes": nodes,
        }
        if special:
            stage.update(
                {
                    "content_label": special["content_label"],
                    "logic_label": special["logic_label"],
                    "method_label": special["method_label"],
                }
            )
        stages.append(stage)
    return stages


def apply_template(route, template_id):
    """Apply a structural template without discarding route content."""
    data = deepcopy(route)
    template = get_template(template_id)
    data["template_id"] = template_id
    data["layout"] = template["layout"]
    data["style"] = template["style"]
    metadata = data.setdefault("metadata", {})
    metadata["template_id"] = template_id
    metadata["template_name"] = template["name_zh"]
    metadata["selected_output_formats"] = list(template["outputs"])
    metadata.setdefault(
        "template_headers",
        {"logic": "研究框架", "content": "研究内容", "method": "研究方法"},
    )
    overrides = data.setdefault("renderer_overrides", {})
    overrides["show_edge_labels"] = False
    overrides["show_node_edges"] = False

    if template_id == "cn-three-column-research-framework":
        defaults = THREE_COLUMN_STAGE_DEFAULTS
        for index, stage in enumerate(data.get("stages") or []):
            fallback = defaults[min(index, len(defaults) - 1)]
            stage.setdefault("content_label", stage.get("title") or fallback["content_label"])
            stage.setdefault("logic_label", fallback["logic_label"])
            stage.setdefault("method_label", fallback["method_label"])
    return data


def template_summary_rows():
    rows = []
    for template_id, item in TEMPLATE_LIBRARY.items():
        rows.append(
            {
                "id": template_id,
                "name_zh": item["name_zh"],
                "name_en": item["name_en"],
                "layout": item["layout"],
                "style": item["style"],
                "outputs": list(item["outputs"]),
                "description_zh": item["description_zh"],
            }
        )
    return rows
