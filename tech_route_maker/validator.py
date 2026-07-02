import json
from pathlib import Path

from .quality import _assumption_node_ids, build_quality_report, iter_nodes
from .schema import ROUTE_VERSION, VALID_CONFIDENCE, VALID_PRESETS, selected_output_formats


def load_route(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(route):
    errors = []
    warnings = []

    if not route.get("title"):
        errors.append("Missing route title.")
    if not route.get("stages"):
        errors.append("Missing stages.")

    route_version = route.get("route_version")
    if not route_version:
        errors.append("Missing route_version.")
    elif route_version != ROUTE_VERSION:
        warnings.append(f"Route version is {route_version}; current schema version is {ROUTE_VERSION}.")

    selected_preset = route.get("selected_preset")
    if not selected_preset:
        errors.append("Missing selected_preset.")
    elif selected_preset not in VALID_PRESETS:
        errors.append(f"Invalid selected_preset: {selected_preset}")

    stages = route.get("stages") or []
    if len(stages) < 4:
        warnings.append("Route has fewer than 4 stages; consider adding validation or output stages.")
    if len(stages) > 7:
        warnings.append("Route has more than 7 stages; consider grouping stages.")

    stage_ids = set()
    node_ids = set()
    assumption_node_ids = _assumption_node_ids(route)

    for stage in stages:
        stage_id = stage.get("id")
        if not stage_id:
            errors.append("Stage missing id.")
            continue
        if stage_id in stage_ids:
            errors.append(f"Duplicate stage id: {stage_id}")
        stage_ids.add(stage_id)

        stage_nodes = stage.get("nodes") or []
        if not stage_nodes:
            warnings.append(f"Stage has no nodes: {stage_id}")
        if len(stage_nodes) < 2:
            warnings.append(f"Stage has fewer than 2 nodes: {stage_id}")
        if len(stage_nodes) > 6:
            warnings.append(f"Stage has more than 6 nodes: {stage_id}")

        for node in stage_nodes:
            node_id = node.get("id")
            if not node_id:
                errors.append(f"Node in stage {stage_id} missing id.")
                continue
            if node_id in node_ids:
                errors.append(f"Duplicate node id: {node_id}")
            node_ids.add(node_id)

            if not node.get("label"):
                errors.append(f"Node missing label: {node_id}")
            if len(str(node.get("label") or "")) > 42:
                warnings.append(f"Long visible label: {node_id}")

            confidence = node.get("confidence")
            if confidence not in VALID_CONFIDENCE:
                errors.append(f"Invalid or missing node confidence for {node_id}: {confidence}")

            evidence = node.get("evidence")
            has_evidence = isinstance(evidence, list) and len(evidence) > 0
            is_inferred = node.get("is_inferred") is True
            if not has_evidence and not is_inferred:
                errors.append(f"Node has no evidence and is not marked inferred: {node_id}")
            if is_inferred and node_id not in assumption_node_ids:
                warnings.append(f"Inferred node is not linked from assumptions: {node_id}")

    edge_ids = set()
    for index, edge in enumerate(route.get("edges") or [], start=1):
        edge_id = edge.get("id") or f"edge_{index}"
        if edge_id in edge_ids:
            errors.append(f"Duplicate edge id: {edge_id}")
        edge_ids.add(edge_id)
        source = edge.get("from") or edge.get("source")
        target = edge.get("to") or edge.get("target")
        if source not in node_ids or target not in node_ids:
            errors.append(f"Edge endpoint missing: {source} -> {target}")
        confidence = edge.get("confidence", "medium")
        if confidence not in VALID_CONFIDENCE:
            errors.append(f"Invalid edge confidence for {edge_id}: {confidence}")

    metadata = route.get("metadata") or {}
    if not isinstance(metadata.get("source_files", []), list):
        errors.append("metadata.source_files must be a list.")
    if not isinstance(metadata.get("source_hashes", []), list):
        errors.append("metadata.source_hashes must be a list.")
    if not selected_output_formats(route):
        warnings.append("No selected_output_formats recorded in metadata.")

    if not isinstance(route.get("assumptions", []), list):
        errors.append("assumptions must be a list.")
    if not isinstance(route.get("unresolved_questions", []), list):
        errors.append("unresolved_questions must be a list.")

    quality_report = build_quality_report(route)
    for warning in quality_report.get("warnings") or []:
        if warning not in warnings:
            warnings.append(warning)

    return errors, warnings, quality_report


def format_validation_result(route, errors, warnings, quality_report):
    status = "Validation failed" if errors else "Validation OK"
    lines = [
        status,
        f"Route version: {route.get('route_version', '')}",
        f"Preset: {route.get('selected_preset', '')}",
        f"Stages: {quality_report.get('stage_count', 0)}",
        f"Nodes: {quality_report.get('node_count', 0)}",
        f"Edges: {quality_report.get('edge_count', 0)}",
        f"Evidence coverage: {quality_report.get('evidence_coverage', 0) * 100:.1f}%",
    ]
    if errors:
        lines.append("Errors:")
        lines.extend([f"- {error}" for error in errors])
    lines.append("Warnings:")
    if warnings:
        lines.extend([f"- {warning}" for warning in warnings])
    else:
        lines.append("- none")
    return "\n".join(lines)


def validate_file(path):
    route = load_route(Path(path))
    errors, warnings, report = validate(route)
    return route, errors, warnings, report
