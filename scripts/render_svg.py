import sys

from route_common import build_layout, get_style, html_escape, load_route, save_text, wrap_text


FONT = "Arial, Helvetica, sans-serif"


def svg_text(x, y, text, size, fill, anchor="middle", weight="400", extra=""):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
        f'font-size="{size}" font-family="{FONT}" font-weight="{weight}" fill="{fill}" {extra}>'
        f"{html_escape(text)}</text>"
    )


def rect(x, y, w, h, rx, fill, stroke="none", stroke_width=1.5, dash="", extra=""):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{dash_attr} {extra}/>'
    )


def stage_palette(style, index):
    palette = style.get("palette") or [style["stage_fill"]]
    return palette[index % len(palette)]


def node_port(box, side):
    if side == "left":
        return box["x"], box["y"] + box["h"] / 2
    if side == "right":
        return box["x"] + box["w"], box["y"] + box["h"] / 2
    if side == "top":
        return box["x"] + box["w"] / 2, box["y"]
    return box["x"] + box["w"] / 2, box["y"] + box["h"]


def draw_wrapped_text(out, text, x, y, width_chars, max_lines, size, fill, weight="400"):
    lines = wrap_text(text, width_chars, max_lines)
    start_y = y - (len(lines) - 1) * (size * 0.58)
    for i, line in enumerate(lines):
        out.append(svg_text(x, start_y + i * (size + 3), line, size, fill, weight=weight))


def draw_title(out, route, layout, style):
    width = layout["width"]
    title_y = 42
    if layout["orientation"] == "vertical":
        pill_w = min(760, max(440, len(route["title"]) * 18))
        out.append(rect((width - pill_w) / 2, 18, pill_w, 58, 28, "#FFFFFF", stage_palette(style, 1), 2.2, "", 'filter="url(#softShadow)"'))
        out.append(svg_text(width / 2, title_y + 10, route["title"], 25, style["text"], weight="700"))
    else:
        out.append(rect(64, 22, width - 128, 58, 18, stage_palette(style, 0), "none"))
        out.append(svg_text(width / 2, 58, route["title"], 24, style["text"], weight="700"))
    if route.get("subtitle"):
        out.append(svg_text(width / 2, 92, route["subtitle"], 12, style["muted"]))
    reader_path = route.get("reader_path") or []
    if reader_path:
        visible = reader_path[:7]
        chip_gap = 10
        chip_w = min(128, max(82, (width - 160 - chip_gap * (len(visible) - 1)) / max(1, len(visible))))
        total_w = len(visible) * chip_w + max(0, len(visible) - 1) * chip_gap
        x = (width - total_w) / 2
        y = 108
        for i, item in enumerate(visible):
            out.append(rect(x + i * (chip_w + chip_gap), y, chip_w, 26, 13, "#FFFFFF", stage_palette(style, i + 1), 1.0))
            draw_wrapped_text(out, item, x + i * (chip_w + chip_gap) + chip_w / 2, y + 17, 15, 1, 10, style["muted"], "600")


def draw_vertical_axis(out, layout, style):
    stages = layout["stages"]
    if not stages:
        return
    axis_x = stages[0].get("axis_x", 100)
    y1 = stages[0]["y"] + 12
    y2 = stages[-1]["y"] + stages[-1]["h"] - 12
    out.append(f'<line x1="{axis_x:.1f}" y1="{y1:.1f}" x2="{axis_x:.1f}" y2="{y2:.1f}" stroke="{style["accent"]}" stroke-width="3" opacity="0.82"/>')
    for stage in stages:
        cy = stage["y"] + stage["h"] / 2
        color = stage_palette(style, stage["index"])
        out.append(f'<circle cx="{axis_x:.1f}" cy="{cy:.1f}" r="7" fill="{style["accent"]}"/>')
        out.append(rect(axis_x - 56, cy - 34, 72, 68, 12, color, "none"))
        draw_wrapped_text(out, stage["title"], axis_x - 20, cy + 4, 4, 3, 15, style["text"], "700")


def draw_stage_regions(out, layout, style):
    for stage in layout["stages"]:
        fill = stage_palette(style, stage["index"])
        dash = style.get("stage_dash", "")
        if layout["orientation"] == "vertical":
            out.append(rect(stage["x"], stage["y"], stage["w"], stage["h"], 22, fill, style["stage_stroke"], 1.6, dash, 'opacity="0.92"'))
            title_w = min(310, max(170, len(stage["title"]) * 16))
            out.append(rect(stage["x"] + 28, stage["y"] - 17, title_w, 34, 10, style["header_fill"], style["header_fill"], 1.0, "", 'filter="url(#softShadow)"'))
            out.append(svg_text(stage["x"] + 28 + title_w / 2, stage["y"] + 5, stage["title"], 14, style["header_text"], weight="700"))
        else:
            out.append(rect(stage["x"], stage["y"], stage["w"], stage["h"], 14, style["stage_fill"], style["stage_stroke"], 1.3, dash))
            out.append(rect(stage["x"], stage["y"], stage["w"], 42, 12, style["header_fill"], style["header_fill"], 1.0))
            draw_wrapped_text(out, stage["title"], stage["x"] + stage["w"] / 2, stage["y"] + 27, 14, 2, 13, style["header_text"], "700")


def draw_edges(out, route, layout, style):
    nodes = layout["nodes"]
    vertical = layout["orientation"] == "vertical"
    for edge in route["edges"]:
        if not edge.get("valid", True) or edge["from"] not in nodes or edge["to"] not in nodes:
            continue
        a = nodes[edge["from"]]
        b = nodes[edge["to"]]
        if vertical:
            x1, y1 = node_port(a, "bottom")
            x2, y2 = node_port(b, "top")
            mid_y = (y1 + y2) / 2
            path = f"M {x1:.1f} {y1:.1f} C {x1:.1f} {mid_y:.1f}, {x2:.1f} {mid_y:.1f}, {x2:.1f} {y2:.1f}"
        else:
            if b["x"] >= a["x"]:
                x1, y1 = node_port(a, "right")
                x2, y2 = node_port(b, "left")
                mid_x = (x1 + x2) / 2
                path = f"M {x1:.1f} {y1:.1f} C {mid_x:.1f} {y1:.1f}, {mid_x:.1f} {y2:.1f}, {x2:.1f} {y2:.1f}"
            else:
                x1, y1 = node_port(a, "top")
                x2, y2 = node_port(b, "top")
                arc_y = min(y1, y2) - 62
                path = f"M {x1:.1f} {y1:.1f} C {x1:.1f} {arc_y:.1f}, {x2:.1f} {arc_y:.1f}, {x2:.1f} {y2:.1f}"
        dash = ' stroke-dasharray="6 5"' if edge.get("kind") == "feedback" or nodes[edge["to"]]["x"] < nodes[edge["from"]]["x"] else ""
        out.append(f'<path d="{path}" fill="none" stroke="{style["line"]}" stroke-width="2.1" marker-end="url(#arrow)" opacity="0.72"{dash}/>')
        if edge.get("label"):
            label_x = (a["x"] + a["w"] / 2 + b["x"] + b["w"] / 2) / 2
            label_y = (a["y"] + a["h"] / 2 + b["y"] + b["h"] / 2) / 2 - 7
            out.append(rect(label_x - 31, label_y - 13, 62, 19, 9, "#FFFFFF", style["soft_shadow"], 0.8))
            draw_wrapped_text(out, edge["label"], label_x, label_y + 1, 12, 1, 9, style["muted"], "600")


def draw_nodes(out, route, layout, style):
    nodes = layout["nodes"]
    for stage in route["stages"]:
        for node in stage["nodes"]:
            box = nodes[node["id"]]
            out.append(f'<g class="node" data-node="{html_escape(node["id"])}" style="cursor:pointer">')
            out.append(rect(box["x"], box["y"], box["w"], box["h"], 10, style["node_fill"], style["node_stroke"], 1.45, "", 'filter="url(#softShadow)"'))
            tag = str(node.get("tag") or "")
            if tag:
                out.append(f'<circle cx="{box["x"] + 14:.1f}" cy="{box["y"] + 14:.1f}" r="4.2" fill="{style["accent_2"]}" opacity="0.86"/>')
            width_chars = max(10, int(box["w"] / 8.5))
            draw_wrapped_text(out, node["label"], box["x"] + box["w"] / 2, box["y"] + box["h"] / 2 + 4, width_chars, 3, 12, style["text"], "600")
            out.append("</g>")


def make_svg(route):
    layout = build_layout(route)
    route = layout["route"]
    style = get_style(route)
    width = layout["width"]
    height = layout["height"]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{style["line"]}"/></marker>',
        '<filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#CBD5E1" flood-opacity="0.32"/></filter>',
        "</defs>",
        f'<rect width="100%" height="100%" fill="{style["background"]}"/>',
        rect(10, 10, width - 20, height - 20, 18, "none", style.get("canvas_stroke", "#D8E1EA"), 1.0),
    ]
    draw_title(out, route, layout, style)
    if layout["orientation"] == "vertical":
        draw_vertical_axis(out, layout, style)
    draw_stage_regions(out, layout, style)
    draw_edges(out, route, layout, style)
    draw_nodes(out, route, layout, style)
    out.append("</svg>")
    return "\n".join(out)


def main():
    if len(sys.argv) != 3:
        print("Usage: python render_svg.py <tech-route.json> <output.svg>")
        return 2
    save_text(sys.argv[2], make_svg(load_route(sys.argv[1])))
    print(f"Wrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
