"""Build the source-verified three-column structural-template demo."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tech_route_maker.schema import ROUTE_VERSION  # noqa: E402
from tech_route_maker.sources import sha256_file  # noqa: E402
from tech_route_maker.validator import validate  # noqa: E402


SOURCE_PATH = "examples/template-library-demo/source/project-brief.md"


STAGES = [
    {
        "id": "system_model",
        "title": "系统建模",
        "content_label": "系统建模",
        "logic_label": "提出问题",
        "method_label": "文献调研与\n理论分析法",
        "nodes": ["校园负荷与光伏资源", "源网荷储系统边界", "协同优化目标定义"],
    },
    {
        "id": "state_forecast",
        "title": "状态预测",
        "content_label": "状态预测",
        "logic_label": "分析问题\n（状态感知）",
        "method_label": "数据驱动\n预测方法",
        "nodes": ["光伏出力短期预测", "校园负荷短期预测", "储能 SOC 状态估计"],
    },
    {
        "id": "optimization",
        "title": "优化决策",
        "content_label": "优化决策",
        "logic_label": "分析问题\n（优化决策）",
        "method_label": "多目标优化与\n约束求解",
        "nodes": ["经济、低碳与可靠性目标", "源储荷协同调度", "并网功率与设备约束"],
    },
    {
        "id": "simulation",
        "title": "仿真验证",
        "content_label": "仿真验证",
        "logic_label": "分析问题\n（运行验证）",
        "method_label": "场景仿真与\n对比实验",
        "nodes": ["典型日运行仿真", "极端天气压力测试", "基线策略对比验证"],
    },
    {
        "id": "evaluation",
        "title": "评价应用",
        "content_label": "评价应用",
        "logic_label": "解决问题\n（评价输出）",
        "method_label": "综合评价法",
        "nodes": ["经济性与减排评价", "供能可靠性评价", "运行策略与实施建议"],
    },
]


def make_node(stage_id, index, label):
    return {
        "id": f"{stage_id}_{index}",
        "label": label,
        "detail": f"项目简要说明中的“{label}”任务。",
        "tag": "source-grounded",
        "node_type": "content",
        "confidence": "high",
        "is_inferred": False,
        "evidence": [
            {
                "kind": "source",
                "source_id": "source_1",
                "path": SOURCE_PATH,
                "locator": label,
                "quote_or_note": f"项目简要说明明确列出“{label}”。",
            }
        ],
    }


def build_route():
    source = ROOT / SOURCE_PATH
    digest = sha256_file(source)
    stages = []
    for order, item in enumerate(STAGES, start=1):
        stages.append(
            {
                "id": item["id"],
                "title": item["title"],
                "content_label": item["content_label"],
                "logic_label": item["logic_label"],
                "method_label": item["method_label"],
                "order": order,
                "nodes": [
                    make_node(item["id"], index, label)
                    for index, label in enumerate(item["nodes"], start=1)
                ],
            }
        )
    route = {
        "route_version": ROUTE_VERSION,
        "title": "校园源网荷储协同优化技术路线",
        "subtitle": "",
        "selected_preset": "chinese-thesis-proposal",
        "template_id": "cn-three-column-research-framework",
        "layout": "cn-three-column-research-framework",
        "style": "cn-classic-research-framework",
        "domain_context": {
            "discipline": "能源动力与电气工程",
            "subfield": "校园综合能源系统优化运行",
            "project_type": "项目申请技术路线图",
            "research_object": "校园光伏、储能、负荷与电网协同系统",
            "method_family": "预测、优化调度与场景仿真",
            "application_area": "校园综合能源管理",
            "data_or_materials": ["校园负荷数据", "光伏资源数据", "储能状态数据"],
            "technical_objects": ["短期预测模型", "多目标优化模型", "协同调度策略"],
            "domain_constraints": ["并网功率约束", "储能 SOC 约束", "设备运行边界"],
            "evaluation_metrics": ["运行成本", "碳排放", "供能可靠性"],
            "expected_outputs": ["协同调度策略", "仿真评价结果", "实施建议"],
            "terminology": {"SOC": "储能荷电状态"},
            "domain_profile": {"family": "energy-system"},
            "source": SOURCE_PATH,
            "confidence": "high",
        },
        "metadata": {
            "created_by": "tech-route-maker",
            "template_id": "cn-three-column-research-framework",
            "template_name": "三栏科研框架图",
            "template_headers": {
                "logic": "研究框架",
                "content": "研究内容",
                "method": "研究方法",
            },
            "selected_output_formats": ["pptx", "svg", "drawio", "html", "json"],
            "source_type": "proposal",
            "source_files": [
                {
                    "id": "source_1",
                    "path": SOURCE_PATH,
                    "kind": "document",
                    "description": "Source-verified campus energy project brief",
                    "sha256": digest,
                }
            ],
            "source_hashes": [
                {
                    "source_id": "source_1",
                    "path": SOURCE_PATH,
                    "algorithm": "sha256",
                    "value": digest,
                }
            ],
            "language": "zh-CN",
            "audience": "research",
        },
        "stages": stages,
        "edges": [],
        "assumptions": [],
        "unresolved_questions": [],
        "quality_report": {},
        "citations": [],
        "renderer_overrides": {
            "show_edge_labels": False,
            "show_node_edges": False,
        },
    }
    output = ROOT / "examples" / "template-library-demo" / "outputs" / "tech-route.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    errors, warnings, report = validate(route, route_path=output)
    if errors:
        raise SystemExit("Template demo validation errors: " + "; ".join(errors))
    route["quality_report"] = report
    output.write_text(json.dumps(route, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")


if __name__ == "__main__":
    build_route()
