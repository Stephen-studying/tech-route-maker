import sys

from route_common import build_layout, center, get_style, html_escape, load_route, save_text, wrap_text


def make_svg(route):
    layout = build_layout(route)
    route = layout["route"]
    style = get_style(route)
    width = layout["width"]
    height = layout["height"]
    nodes = layout["nodes"]
    palette = style["palette"]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{style["line"]}"/></marker>',
        "</defs>",
        f'<rect width="100%" height="100%" fill="{style["background"]}"/>',
        f'<text x="{width/2:.1f}" y="36" text-anchor="middle" font-size="24" font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="{style["text"]}">{html_escape(route["title"])}</text>',
    ]
    if route.get("subtitle"):
        out.append(f'<text x="{width/2:.1f}" y="60" text-anchor="middle" font-size="13" font-family="Arial, Helvetica, sans-serif" fill="{style["muted"]}">{html_escape(route["subtitle"])}</text>')

    for stage in layout["stages"]:
        fill = palette[stage["index"] % len(palette)]
        out.append(f'<rect x="{stage["x"]:.1f}" y="{stage["y"]:.1f}" width="{stage["w"]:.1f}" height="{stage["h"]:.1f}" rx="12" fill="{style["stage_fill"]}" stroke="{style["stage_stroke"]}" stroke-width="1.5"/>')
        out.append(f'<rect x="{stage["x"]:.1f}" y="{stage["y"]:.1f}" width="{stage["w"]:.1f}" height="38" rx="12" fill="{style["header_fill"]}"/>')
        out.append(f'<text x="{stage["x"] + stage["w"]/2:.1f}" y="{stage["y"] + 24:.1f}" text-anchor="middle" font-size="14" font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="{style["header_text"]}">{html_escape(stage["title"])}</text>')

    for edge in route["edges"]:
        if not edge.get("valid", True) or edge["from"] not in nodes or edge["to"] not in nodes:
            continue
        x1, y1 = center(nodes[edge["from"]])
        x2, y2 = center(nodes[edge["to"]])
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{style["line"]}" stroke-width="2" marker-end="url(#arrow)" opacity="0.78"/>')
        if edge.get("label"):
            out.append(f'<text x="{(x1+x2)/2:.1f}" y="{(y1+y2)/2 - 6:.1f}" text-anchor="middle" font-size="10" font-family="Arial, Helvetica, sans-serif" fill="{style["muted"]}">{html_escape(edge["label"])}</text>')

    stage_lookup = {stage["id"]: stage["index"] for stage in layout["stages"]}
    for stage in route["stages"]:
        for node in stage["nodes"]:
            box = nodes[node["id"]]
            fill = style["node_fill"]
            stroke = style["node_stroke"]
            out.append(f'<g class="node" data-node="{html_escape(node["id"])}" style="cursor:pointer">')
            out.append(f'<rect x="{box["x"]:.1f}" y="{box["y"]:.1f}" width="{box["w"]:.1f}" height="{box["h"]:.1f}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
            lines = wrap_text(node["label"], 18, 3)
            start_y = box["y"] + box["h"] / 2 - (len(lines) - 1) * 7 + 5
            for li, line in enumerate(lines):
                out.append(f'<text x="{box["x"] + box["w"]/2:.1f}" y="{start_y + li*15:.1f}" text-anchor="middle" font-size="12" font-family="Arial, Helvetica, sans-serif" fill="{style["text"]}">{html_escape(line)}</text>')
            out.append("</g>")
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
