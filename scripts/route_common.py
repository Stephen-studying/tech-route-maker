import copy
import json
import math
import re
from pathlib import Path


STYLES = {
    "academic-blue": {
        "background": "#FFFFFF",
        "text": "#1F2937",
        "muted": "#64748B",
        "line": "#2563EB",
        "stage_fill": "#EFF6FF",
        "stage_stroke": "#93C5FD",
        "header_fill": "#1D4ED8",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#60A5FA",
        "palette": ["#DBEAFE", "#E0F2FE", "#EEF2FF", "#ECFDF5", "#FFF7ED", "#FDF2F8"],
    },
    "blue-green-research": {
        "background": "#FFFFFF",
        "text": "#12333A",
        "muted": "#527078",
        "line": "#0F766E",
        "stage_fill": "#ECFEFF",
        "stage_stroke": "#5EEAD4",
        "header_fill": "#0E7490",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#14B8A6",
        "palette": ["#CFFAFE", "#CCFBF1", "#DCFCE7", "#E0F2FE", "#F0FDFA", "#F7FEE7"],
    },
    "monochrome-paper": {
        "background": "#FFFFFF",
        "text": "#111111",
        "muted": "#555555",
        "line": "#111111",
        "stage_fill": "#F5F5F5",
        "stage_stroke": "#777777",
        "header_fill": "#222222",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#333333",
        "palette": ["#F8F8F8", "#EEEEEE", "#E5E5E5", "#DDDDDD", "#D4D4D4", "#CCCCCC"],
    },
    "defense-color": {
        "background": "#FFFFFF",
        "text": "#172033",
        "muted": "#4B5563",
        "line": "#7C3AED",
        "stage_fill": "#F8FAFC",
        "stage_stroke": "#CBD5E1",
        "header_fill": "#4338CA",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#8B5CF6",
        "palette": ["#DBEAFE", "#EDE9FE", "#DCFCE7", "#FEF3C7", "#FFE4E6", "#CCFBF1"],
    },
    "minimal-gray": {
        "background": "#FFFFFF",
        "text": "#242424",
        "muted": "#6B7280",
        "line": "#475569",
        "stage_fill": "#F8FAFC",
        "stage_stroke": "#CBD5E1",
        "header_fill": "#334155",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#94A3B8",
        "palette": ["#F8FAFC", "#F1F5F9", "#E2E8F0", "#F8FAFC", "#F1F5F9", "#E2E8F0"],
    },
    "nature-editorial": {
        "background": "#FFFFFF",
        "text": "#17201D",
        "muted": "#5B6670",
        "line": "#2F5D62",
        "stage_fill": "#F7FAF8",
        "stage_stroke": "#A7C4BC",
        "header_fill": "#2F5D62",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#7AA6A1",
        "palette": ["#E8F3F1", "#EEF2E6", "#F7EEE3", "#EAF0F6", "#F2EAF3", "#F6F4EA"],
    },
    "accessible-high-contrast": {
        "background": "#FFFFFF",
        "text": "#000000",
        "muted": "#333333",
        "line": "#000000",
        "stage_fill": "#FFFFFF",
        "stage_stroke": "#000000",
        "header_fill": "#000000",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#000000",
        "palette": ["#FFFFFF", "#F2F2F2", "#E6E6E6", "#FFFFFF", "#F2F2F2", "#E6E6E6"],
    },
    "dark-technical": {
        "background": "#0B1020",
        "text": "#E5E7EB",
        "muted": "#AAB2C0",
        "line": "#38BDF8",
        "stage_fill": "#111827",
        "stage_stroke": "#334155",
        "header_fill": "#0F766E",
        "header_text": "#FFFFFF",
        "node_fill": "#111827",
        "node_stroke": "#38BDF8",
        "palette": ["#172554", "#164E63", "#064E3B", "#3B0764", "#451A03", "#4C0519"],
    },
    "soft-pastel": {
        "background": "#FFFFFF",
        "text": "#334155",
        "muted": "#64748B",
        "line": "#64748B",
        "stage_fill": "#FFFBF7",
        "stage_stroke": "#E5E7EB",
        "header_fill": "#A78BFA",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#C4B5FD",
        "palette": ["#FDE2E4", "#E2F0CB", "#CDE7F0", "#F7D9C4", "#D8E2DC", "#E8DAEF"],
    },
    "schematic-precision": {
        "background": "#FFFFFF",
        "text": "#111827",
        "muted": "#4B5563",
        "line": "#1F2937",
        "stage_fill": "#F9FAFB",
        "stage_stroke": "#9CA3AF",
        "header_fill": "#374151",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#111827",
        "palette": ["#F9FAFB", "#F3F4F6", "#EEF2FF", "#ECFEFF", "#F0FDF4", "#FFFBEB"],
    },
    "editorial-clarity": {
        "background": "#FFFFFF",
        "text": "#18212F",
        "muted": "#687386",
        "line": "#2563EB",
        "stage_fill": "#FFFFFF",
        "stage_stroke": "#E2E8F0",
        "header_fill": "#1E40AF",
        "header_text": "#FFFFFF",
        "node_fill": "#F8FAFC",
        "node_stroke": "#CBD5E1",
        "palette": ["#EFF6FF", "#F8FAFC", "#ECFDF5", "#F8FAFC", "#FFF7ED", "#F8FAFC"],
    },
    "mechanism-snapshot": {
        "background": "#FFFFFF",
        "text": "#1E293B",
        "muted": "#64748B",
        "line": "#C2410C",
        "stage_fill": "#FFF7ED",
        "stage_stroke": "#FDBA74",
        "header_fill": "#C2410C",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#FB923C",
        "palette": ["#FFEDD5", "#FEF3C7", "#ECFCCB", "#E0F2FE", "#FDE68A", "#FED7AA"],
    },
    "evidence-infographic": {
        "background": "#FFFFFF",
        "text": "#172033",
        "muted": "#475569",
        "line": "#7C3AED",
        "stage_fill": "#FAF5FF",
        "stage_stroke": "#C4B5FD",
        "header_fill": "#6D28D9",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#A78BFA",
        "palette": ["#EDE9FE", "#DBEAFE", "#DCFCE7", "#FEF3C7", "#FCE7F3", "#CCFBF1"],
    },
    "premium-scientific": {
        "background": "#FFFFFF",
        "text": "#17201D",
        "muted": "#59636A",
        "line": "#315C61",
        "stage_fill": "#F8FAF9",
        "stage_stroke": "#B8C7C1",
        "header_fill": "#315C61",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#8BAAA5",
        "palette": ["#E8F3F1", "#F2EFE6", "#EAF0F6", "#F6F1E8", "#EDF4EA", "#F3EEF4"],
    },
    "advertising-clean-campaign": {
        "background": "#FFFFFF",
        "text": "#111827",
        "muted": "#5B6472",
        "line": "#E11D48",
        "stage_fill": "#FFF7F7",
        "stage_stroke": "#FDA4AF",
        "header_fill": "#E11D48",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#FB7185",
        "palette": ["#FFE4E6", "#FEF3C7", "#DBEAFE", "#DCFCE7", "#FCE7F3", "#E0F2FE"],
    },
    "proposal-pastel-route": {
        "background": "#FFFFFF",
        "text": "#162033",
        "muted": "#5B6472",
        "line": "#2C6A93",
        "stage_fill": "#F8FBFC",
        "stage_stroke": "#6FAEC3",
        "header_fill": "#7BCFD0",
        "header_text": "#122033",
        "node_fill": "#FFFFFF",
        "node_stroke": "#9FB6C4",
        "palette": ["#D9F2F2", "#F7E0E8", "#FFF1C7", "#DDECF9", "#E6F4D7", "#F6E7D7"],
        "accent": "#F36E78",
        "accent_2": "#F7C744",
        "accent_3": "#67C7A5",
        "stage_dash": "6 6",
    },
    "grant-linework": {
        "background": "#FFFFFF",
        "text": "#111111",
        "muted": "#555555",
        "line": "#111111",
        "stage_fill": "#FFFFFF",
        "stage_stroke": "#222222",
        "header_fill": "#FFFFFF",
        "header_text": "#111111",
        "node_fill": "#FFFFFF",
        "node_stroke": "#222222",
        "palette": ["#FFFFFF", "#F7F7F7", "#FFFFFF", "#F7F7F7", "#FFFFFF", "#F7F7F7"],
        "accent": "#111111",
        "accent_2": "#666666",
        "accent_3": "#999999",
        "stage_dash": "7 5",
    },
    "wide-collaboration-map": {
        "background": "#FFFFFF",
        "text": "#111827",
        "muted": "#526070",
        "line": "#2D5CA8",
        "stage_fill": "#F8FBFF",
        "stage_stroke": "#AFC4E8",
        "header_fill": "#2D5CA8",
        "header_text": "#FFFFFF",
        "node_fill": "#FFFFFF",
        "node_stroke": "#8BADE3",
        "palette": ["#DCE9FF", "#DFF2E3", "#E9EEFF", "#FFF1D6", "#E4F6F5", "#FCE3E8"],
        "accent": "#2D5CA8",
        "accent_2": "#5E9F3B",
        "accent_3": "#D94E4E",
        "stage_dash": "8 6",
    },
}

STYLE_DEFAULTS = {
    "accent": "#2563EB",
    "accent_2": "#0F766E",
    "accent_3": "#F59E0B",
    "stage_dash": "",
    "canvas_stroke": "#D8E1EA",
    "soft_shadow": "#E7ECF2",
}


def load_route(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_text(path, text):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def slug(value, fallback):
    value = str(value or "")
    value = re.sub(r"[^A-Za-z0-9_]+", "_", value.strip()).strip("_").lower()
    return value or fallback


def wrap_text(value, width=18, max_lines=3):
    text = str(value or "").strip()
    if not text:
        return [""]
    parts = []
    current = ""
    for token in re.split(r"(\s+)", text):
        if not token:
            continue
        if token.isspace():
            if current and len(current) < width:
                current += " "
            continue
        if len(token) > width:
            if current:
                parts.append(current.rstrip())
                current = ""
            for i in range(0, len(token), width):
                parts.append(token[i : i + width])
            continue
        if len(current) + len(token) > width and current:
            parts.append(current.rstrip())
            current = token
        else:
            current += token
    if current:
        parts.append(current.rstrip())
    if len(parts) > max_lines:
        parts = parts[: max_lines - 1] + [parts[max_lines - 1][: max(1, width - 1)] + "..."]
    return parts or [text]


def normalize_route(route):
    data = copy.deepcopy(route)
    data["title"] = str(data.get("title") or "Project Technical Route")
    data["subtitle"] = str(data.get("subtitle") or "")
    data["layout"] = data.get("layout") or "horizontal-stages"
    data["style"] = data.get("style") or data.get("theme") or "academic-blue"
    data["metadata"] = data.get("metadata") or {}
    stages = []
    node_ids = set()
    for si, stage in enumerate(data.get("stages") or []):
        sid = slug(stage.get("id") or stage.get("title") or stage.get("name"), f"stage_{si + 1}")
        title = str(stage.get("title") or stage.get("name") or f"Stage {si + 1}")
        nodes = []
        for ni, node in enumerate(stage.get("nodes") or []):
            if isinstance(node, str):
                node = {"label": node}
            nid = slug(node.get("id") or node.get("label"), f"{sid}_node_{ni + 1}")
            base = nid
            offset = 2
            while nid in node_ids:
                nid = f"{base}_{offset}"
                offset += 1
            node_ids.add(nid)
            nodes.append(
                {
                    "id": nid,
                    "label": str(node.get("label") or node.get("title") or f"Node {ni + 1}"),
                    "detail": str(node.get("detail") or node.get("summary") or ""),
                    "tag": str(node.get("tag") or stage.get("tag") or "step"),
                    "evidence": node.get("evidence") if isinstance(node.get("evidence"), list) else [],
                }
            )
        stages.append(
            {
                "id": sid,
                "title": title,
                "summary": str(stage.get("summary") or ""),
                "nodes": nodes,
            }
        )
    data["stages"] = stages
    valid_ids = {node["id"] for stage in stages for node in stage["nodes"]}
    edges = []
    for ei, edge in enumerate(data.get("edges") or []):
        if not isinstance(edge, dict):
            continue
        source = slug(edge.get("from") or edge.get("source"), f"missing_from_{ei}")
        target = slug(edge.get("to") or edge.get("target"), f"missing_to_{ei}")
        edges.append(
            {
                "id": slug(edge.get("id"), f"edge_{ei + 1}"),
                "from": source,
                "to": target,
                "label": str(edge.get("label") or edge.get("title") or "next"),
                "kind": str(edge.get("kind") or "flow"),
                "valid": source in valid_ids and target in valid_ids,
            }
        )
    if not edges:
        last = None
        count = 1
        for stage in stages:
            for node in stage["nodes"]:
                if last:
                    edges.append({"id": f"edge_{count}", "from": last, "to": node["id"], "label": "next", "kind": "flow", "valid": True})
                    count += 1
                last = node["id"]
    data["edges"] = edges
    return data


def get_style(route):
    name = route.get("style") or "academic-blue"
    style = copy.deepcopy(STYLES.get(name, STYLES["academic-blue"]))
    for key, value in STYLE_DEFAULTS.items():
        style.setdefault(key, value)
    style["name"] = name
    return style


def flatten_nodes(route):
    return [node for stage in route["stages"] for node in stage["nodes"]]


def build_layout(route):
    route = normalize_route(route)
    layout_name = route.get("layout", "horizontal-stages")
    stages = route["stages"]
    margin = 64
    title_h = 102
    node_h = 62
    header_h = 42
    gap = 38
    node_gap = 16
    nodes = {}
    stage_boxes = []

    matrix_layouts = {"academic-method-framework", "proposal-matrix-route"}
    system_layouts = {"software-system-route"}
    campaign_layouts = {"campaign-strategy-map"}

    if layout_name in matrix_layouts:
        width = 1280
        content_x = 228
        content_w = 980
        label_x = 62
        label_w = 128
        y = title_h + 44
        row_gap = 24
        node_h = 60
        node_gap = 16
        for si, stage in enumerate(stages):
            count = max(1, len(stage["nodes"]))
            cols = 1 if count == 1 else min(3, count)
            rows = int(math.ceil(count / cols))
            node_w = (content_w - 72 - (cols - 1) * node_gap) / cols
            row_h = max(112, 32 + rows * node_h + max(0, rows - 1) * node_gap + 34)
            label_box = {
                "x": label_x,
                "y": y + row_h / 2 - 28,
                "w": label_w,
                "h": 56,
            }
            stage_boxes.append(
                {
                    "id": stage["id"],
                    "title": stage["title"],
                    "x": content_x,
                    "y": y,
                    "w": content_w,
                    "h": row_h,
                    "index": si,
                    "layout": "matrix",
                    "label_box": label_box,
                }
            )
            for ni, node in enumerate(stage["nodes"]):
                row = ni // cols
                col = ni % cols
                if count == 1:
                    node_w_single = min(760, content_w - 110)
                    nx = content_x + (content_w - node_w_single) / 2
                    nw = node_w_single
                else:
                    nx = content_x + 36 + col * (node_w + node_gap)
                    nw = node_w
                ny = y + 32 + row * (node_h + node_gap)
                nodes[node["id"]] = {"x": nx, "y": ny, "w": nw, "h": node_h, "stage": stage["id"]}
            y += row_h + row_gap
        height = y + 40
        return {
            "width": int(width),
            "height": int(height),
            "layout_name": layout_name,
            "orientation": "matrix",
            "stages": stage_boxes,
            "nodes": nodes,
            "route": route,
        }

    if layout_name in system_layouts:
        width = 1320
        content_x = 238
        content_w = 1008
        label_x = 58
        label_w = 146
        y = title_h + 48
        row_gap = 18
        node_h = 58
        node_gap = 18
        for si, stage in enumerate(stages):
            count = max(1, len(stage["nodes"]))
            cols = min(4, count)
            rows = int(math.ceil(count / cols))
            node_w = (content_w - 70 - (cols - 1) * node_gap) / cols
            row_h = max(104, 28 + rows * node_h + max(0, rows - 1) * node_gap + 28)
            label_box = {
                "x": label_x,
                "y": y,
                "w": label_w,
                "h": row_h,
            }
            stage_boxes.append(
                {
                    "id": stage["id"],
                    "title": stage["title"],
                    "x": content_x,
                    "y": y,
                    "w": content_w,
                    "h": row_h,
                    "index": si,
                    "layout": "system",
                    "label_box": label_box,
                }
            )
            for ni, node in enumerate(stage["nodes"]):
                row = ni // cols
                col = ni % cols
                nx = content_x + 35 + col * (node_w + node_gap)
                ny = y + 28 + row * (node_h + node_gap)
                nodes[node["id"]] = {"x": nx, "y": ny, "w": node_w, "h": node_h, "stage": stage["id"]}
            y += row_h + row_gap
        height = y + 44
        return {
            "width": int(width),
            "height": int(height),
            "layout_name": layout_name,
            "orientation": "system",
            "stages": stage_boxes,
            "nodes": nodes,
            "route": route,
        }

    if layout_name in campaign_layouts:
        width = 1360
        height = 690
        margin = 60
        top = title_h + 74
        gap = 22
        stage_w = (width - margin * 2 - max(0, len(stages) - 1) * gap) / max(1, len(stages))
        stage_h = 390
        for si, stage in enumerate(stages):
            x = margin + si * (stage_w + gap)
            stage_boxes.append(
                {
                    "id": stage["id"],
                    "title": stage["title"],
                    "x": x,
                    "y": top,
                    "w": stage_w,
                    "h": stage_h,
                    "index": si,
                    "layout": "campaign",
                }
            )
            node_w = stage_w - 34
            for ni, node in enumerate(stage["nodes"]):
                nx = x + 17
                ny = top + 68 + ni * (node_h + node_gap)
                nodes[node["id"]] = {"x": nx, "y": ny, "w": node_w, "h": node_h, "stage": stage["id"]}
        return {
            "width": int(width),
            "height": int(height),
            "layout_name": layout_name,
            "orientation": "campaign",
            "stages": stage_boxes,
            "nodes": nodes,
            "route": route,
        }

    vertical = layout_name in {"vertical-research-route", "closed-loop-optimization", "evidence-centered", "proposal-phase-axis"}
    if vertical:
        width = 1120
        axis_x = 102
        stage_x = 202
        stage_w = 842
        y = title_h + 36
        for si, stage in enumerate(stages):
            count = max(1, len(stage["nodes"]))
            cols = 1 if count == 1 else min(3, count)
            rows = int(math.ceil(max(1, len(stage["nodes"])) / cols))
            node_w = (stage_w - 70 - (cols - 1) * node_gap) / cols
            sh = header_h + rows * node_h + max(0, rows - 1) * node_gap + 42
            stage_boxes.append(
                {
                    "id": stage["id"],
                    "title": stage["title"],
                    "x": stage_x,
                    "y": y,
                    "w": stage_w,
                    "h": sh,
                    "index": si,
                    "axis_x": axis_x,
                    "layout": "vertical",
                }
            )
            for ni, node in enumerate(stage["nodes"]):
                row = ni // cols
                col = ni % cols
                nx = stage_x + 35 + col * (node_w + node_gap)
                ny = y + header_h + 18 + row * (node_h + node_gap)
                nodes[node["id"]] = {"x": nx, "y": ny, "w": node_w, "h": node_h, "stage": stage["id"]}
            y += sh + gap
        height = y + 48
    else:
        max_nodes = max([len(s["nodes"]) for s in stages] + [1])
        if layout_name in {"campaign-funnel", "creative-production-pipeline"}:
            width = 1320
            height = 620
            gap = 28
        elif layout_name in {"engineering-architecture", "layered-architecture", "timeline-swimlane", "wide-collaboration-map"}:
            width = 1340
            height = 580
            gap = 30
        else:
            width = max(1180, min(1520, margin * 2 + len(stages) * 214 + max(0, len(stages) - 1) * gap))
            height = 610
        stage_w = (width - margin * 2 - max(0, len(stages) - 1) * gap) / max(1, len(stages))
        stage_w = max(150, stage_w)
        stage_h = min(390, height - title_h - margin - 56)
        for si, stage in enumerate(stages):
            x = margin + si * (stage_w + gap)
            y = title_h + margin
            stage_boxes.append(
                {
                    "id": stage["id"],
                    "title": stage["title"],
                    "x": x,
                    "y": y,
                    "w": stage_w,
                    "h": stage_h,
                    "index": si,
                    "layout": "horizontal",
                }
            )
            node_w = max(116, stage_w - 42)
            for ni, node in enumerate(stage["nodes"]):
                nx = x + (stage_w - node_w) / 2
                ny = y + header_h + 18 + ni * (node_h + node_gap)
                nodes[node["id"]] = {"x": nx, "y": ny, "w": node_w, "h": node_h, "stage": stage["id"]}
    return {
        "width": int(width),
        "height": int(height),
        "layout_name": layout_name,
        "orientation": "vertical" if vertical else "horizontal",
        "stages": stage_boxes,
        "nodes": nodes,
        "route": route,
    }


def center(box):
    return (box["x"] + box["w"] / 2, box["y"] + box["h"] / 2)


def html_escape(value):
    return (
        str(value or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def ensure_parent(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
