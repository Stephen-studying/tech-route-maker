import sys

from route_common import build_layout, get_style, html_escape, load_route, save_text


def make_drawio(route):
    layout = build_layout(route)
    route = layout["route"]
    style = get_style(route)
    nodes = layout["nodes"]
    parts = [
        '<mxfile host="app.diagrams.net" modified="2026-06-19T00:00:00.000Z" agent="tech-route-maker" version="24.7.8">',
        '<diagram id="tech-route" name="Tech Route">',
        '<mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" math="0" shadow="0">',
        "<root>",
        '<mxCell id="0"/>',
        '<mxCell id="1" parent="0"/>',
    ]
    parts.append(f'<mxCell id="title" value="{html_escape(route["title"])}" style="text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;fontColor={style["text"]};" vertex="1" parent="1"><mxGeometry x="40" y="20" width="{layout["width"] - 80}" height="40" as="geometry"/></mxCell>')
    for stage in layout["stages"]:
        sid = f'stage_{stage["id"]}'
        stage_value = "" if stage.get("label_box") else html_escape(stage["title"])
        parts.append(f'<mxCell id="{sid}" value="{stage_value}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={style["stage_fill"]};strokeColor={style["stage_stroke"]};fontColor={style["text"]};fontStyle=1;verticalAlign=top;spacingTop=8;" vertex="1" parent="1"><mxGeometry x="{stage["x"]:.0f}" y="{stage["y"]:.0f}" width="{stage["w"]:.0f}" height="{stage["h"]:.0f}" as="geometry"/></mxCell>')
        if stage.get("label_box"):
            label = stage["label_box"]
            parts.append(f'<mxCell id="{sid}_label" value="{html_escape(stage["title"])}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={style["header_fill"]};strokeColor={style["header_fill"]};fontColor={style["header_text"]};fontStyle=1;" vertex="1" parent="1"><mxGeometry x="{label["x"]:.0f}" y="{label["y"]:.0f}" width="{label["w"]:.0f}" height="{label["h"]:.0f}" as="geometry"/></mxCell>')
    for stage in route["stages"]:
        for node in stage["nodes"]:
            box = nodes[node["id"]]
            detail = html_escape(node.get("detail", ""))
            value = html_escape(node["label"])
            parts.append(f'<mxCell id="{node["id"]}" value="{value}" tooltip="{detail}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={style["node_fill"]};strokeColor={style["node_stroke"]};fontColor={style["text"]};arcSize=12;" vertex="1" parent="1"><mxGeometry x="{box["x"]:.0f}" y="{box["y"]:.0f}" width="{box["w"]:.0f}" height="{box["h"]:.0f}" as="geometry"/></mxCell>')
    for edge in route["edges"]:
        if not edge.get("valid", True):
            continue
        parts.append(f'<mxCell id="{edge["id"]}" value="{html_escape(edge.get("label", ""))}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor={style["line"]};fontColor={style["muted"]};" edge="1" parent="1" source="{edge["from"]}" target="{edge["to"]}"><mxGeometry relative="1" as="geometry"/></mxCell>')
    parts.extend(["</root>", "</mxGraphModel>", "</diagram>", "</mxfile>"])
    return "\n".join(parts)


def main():
    if len(sys.argv) != 3:
        print("Usage: python render_drawio.py <tech-route.json> <output.drawio>")
        return 2
    save_text(sys.argv[2], make_drawio(load_route(sys.argv[1])))
    print(f"Wrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
