import sys

from route_common import flatten_nodes, load_route, normalize_route


def validate(route):
    errors = []
    warnings = []
    if not route.get("title"):
        errors.append("Missing route title.")
    if not route.get("stages"):
        errors.append("Missing stages.")

    node_ids = set()
    stage_ids = set()
    for stage in route.get("stages", []):
        if stage["id"] in stage_ids:
            errors.append(f"Duplicate stage id: {stage['id']}")
        stage_ids.add(stage["id"])
        if not stage.get("nodes"):
            warnings.append(f"Stage has no nodes: {stage['id']}")
        if len(stage.get("nodes", [])) > 6:
            warnings.append(f"Stage has more than 6 nodes: {stage['id']}")
        for node in stage.get("nodes", []):
            if node["id"] in node_ids:
                errors.append(f"Duplicate node id: {node['id']}")
            node_ids.add(node["id"])
            if len(node.get("label", "")) > 42:
                warnings.append(f"Long visible label: {node['id']}")
            if not node.get("evidence"):
                warnings.append(f"Node has no evidence: {node['id']}")
    for edge in route.get("edges", []):
        if not edge.get("valid", True):
            errors.append(f"Edge endpoint missing: {edge.get('from')} -> {edge.get('to')}")

    metadata = route.get("metadata") or {}
    selected = metadata.get("selected_output_formats")
    if not selected:
        warnings.append("No selected_output_formats recorded in metadata. Confirm the user chose formats before rendering.")

    if len(flatten_nodes(route)) > 36:
        warnings.append("Diagram has more than 36 nodes; consider a summary view plus drill-down diagrams.")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_route.py <tech-route.json>")
        return 2
    raw = load_route(sys.argv[1])
    route = normalize_route(raw)
    errors, warnings = validate(route)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Validation failed with {len(errors)} error(s) and {len(warnings)} warning(s).")
        return 1
    print(f"Validation passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
