from collections import Counter

from .schema import ROUTE_VERSION, selected_output_formats


def iter_nodes(route):
    for stage in route.get("stages") or []:
        for node in stage.get("nodes") or []:
            yield stage, node


def _has_evidence(node):
    evidence = node.get("evidence")
    return isinstance(evidence, list) and len(evidence) > 0


def _assumption_node_ids(route):
    linked = set()
    for assumption in route.get("assumptions") or []:
        for node_id in assumption.get("node_ids") or []:
            linked.add(node_id)
    return linked


def build_quality_report(route):
    stages = route.get("stages") or []
    nodes = list(iter_nodes(route))
    edges = route.get("edges") or []
    node_count = len(nodes)
    evidence_nodes = [node for _, node in nodes if _has_evidence(node)]
    inferred_nodes = [node for _, node in nodes if node.get("is_inferred") is True]
    missing_evidence_nodes = [
        node.get("id", "")
        for _, node in nodes
        if not _has_evidence(node) and node.get("is_inferred") is not True
    ]
    long_label_nodes = [
        node.get("id", "")
        for _, node in nodes
        if len(str(node.get("label") or "")) > 42
    ]
    stages_with_too_many_nodes = [
        stage.get("id", "")
        for stage in stages
        if len(stage.get("nodes") or []) > 6
    ]
    stages_with_too_few_nodes = [
        stage.get("id", "")
        for stage in stages
        if len(stage.get("nodes") or []) < 2
    ]
    confidence_counts = Counter(str(node.get("confidence") or "missing") for _, node in nodes)

    warnings = []
    if len(stages) < 4:
        warnings.append("Route has fewer than 4 stages; a technical route may be underspecified.")
    if len(stages) > 7:
        warnings.append("Route has more than 7 stages; consider grouping stages for readability.")
    for stage_id in stages_with_too_many_nodes:
        warnings.append(f"Stage has more than 6 nodes: {stage_id}")
    for stage_id in stages_with_too_few_nodes:
        warnings.append(f"Stage has fewer than 2 nodes: {stage_id}")
    for node_id in long_label_nodes:
        warnings.append(f"Long visible label: {node_id}")
    for node_id in missing_evidence_nodes:
        warnings.append(f"Node has no evidence and is not marked inferred: {node_id}")

    evidence_coverage = (len(evidence_nodes) + len(inferred_nodes)) / node_count if node_count else 0.0

    return {
        "route_version": route.get("route_version") or ROUTE_VERSION,
        "selected_preset": route.get("selected_preset") or "custom",
        "selected_output_formats": selected_output_formats(route),
        "stage_count": len(stages),
        "node_count": node_count,
        "edge_count": len(edges),
        "evidence_node_count": len(evidence_nodes),
        "evidence_coverage": round(evidence_coverage, 4),
        "inferred_node_count": len(inferred_nodes),
        "unresolved_question_count": len(route.get("unresolved_questions") or []),
        "long_label_nodes": long_label_nodes,
        "stages_with_too_many_nodes": stages_with_too_many_nodes,
        "stages_with_too_few_nodes": stages_with_too_few_nodes,
        "missing_evidence_nodes": missing_evidence_nodes,
        "confidence_summary": dict(confidence_counts),
        "warnings": warnings,
        "suggested_manual_review": [
            "Check terminology against the source material.",
            "Check whether inferred nodes should be removed or supported with evidence.",
            "Check edge labels and route logic.",
            "Check output layout, color hierarchy, spacing and text wrapping.",
        ],
    }


def render_quality_report_markdown(report):
    coverage = report.get("evidence_coverage", 0.0) * 100
    lines = [
        "# Quality Report",
        "",
        "## Summary",
        "",
        f"- Route version: {report.get('route_version', '')}",
        f"- Selected preset: {report.get('selected_preset', '')}",
        f"- Output formats: {', '.join(report.get('selected_output_formats') or []) or 'not recorded'}",
        f"- Stage count: {report.get('stage_count', 0)}",
        f"- Node count: {report.get('node_count', 0)}",
        f"- Edge count: {report.get('edge_count', 0)}",
        f"- Evidence coverage: {coverage:.1f}%",
        f"- Inferred node count: {report.get('inferred_node_count', 0)}",
        f"- Unresolved questions: {report.get('unresolved_question_count', 0)}",
        "",
        "## Structural Checks",
        "",
        f"- [{'x' if 4 <= report.get('stage_count', 0) <= 7 else ' '}] Main route has 4-7 stages.",
        f"- [{'x' if not report.get('stages_with_too_many_nodes') else ' '}] Each stage has 2-6 visible nodes.",
        f"- [{'x' if not report.get('long_label_nodes') else ' '}] Node labels are concise.",
        "- [x] Edges connect existing nodes after validation.",
        "",
        "## Evidence Checks",
        "",
        f"- Nodes with evidence: {report.get('evidence_node_count', 0)}",
        f"- Nodes marked as inferred: {report.get('inferred_node_count', 0)}",
        f"- Nodes missing evidence: {len(report.get('missing_evidence_nodes') or [])}",
        "",
        "## Layout Checks",
        "",
        f"- Long labels: {', '.join(report.get('long_label_nodes') or []) or 'none'}",
        f"- Dense stages: {', '.join(report.get('stages_with_too_many_nodes') or []) or 'none'}",
        "",
        "## Warnings",
        "",
    ]
    warnings = report.get("warnings") or []
    if warnings:
        lines.extend([f"- {warning}" for warning in warnings])
    else:
        lines.append("- none")
    lines.extend(["", "## Suggested Manual Review", ""])
    lines.extend([f"- {item}" for item in report.get("suggested_manual_review") or []])
    lines.append("")
    return "\n".join(lines)
