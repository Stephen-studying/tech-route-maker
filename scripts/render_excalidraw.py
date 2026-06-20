import json
import sys

from route_common import build_layout, center, get_style, load_route, save_text


def element_id(prefix, value):
    return f"{prefix}_{str(value).replace('-', '_')}"


def make_excalidraw(route):
    layout = build_layout(route)
    route = layout["route"]
    style = get_style(route)
    nodes = layout["nodes"]
    elements = []
    elements.append({
        "id": "title",
        "type": "text",
        "x": layout["width"] / 2 - 220,
        "y": 22,
        "width": 440,
        "height": 32,
        "angle": 0,
        "strokeColor": style["text"],
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "text": route["title"],
        "fontSize": 24,
        "fontFamily": 1,
        "textAlign": "center",
        "verticalAlign": "middle",
        "containerId": None,
        "originalText": route["title"],
        "lineHeight": 1.25,
    })
    for stage in layout["stages"]:
        elements.append({
            "id": element_id("stage", stage["id"]),
            "type": "rectangle",
            "x": stage["x"],
            "y": stage["y"],
            "width": stage["w"],
            "height": stage["h"],
            "angle": 0,
            "strokeColor": style["stage_stroke"],
            "backgroundColor": style["stage_fill"],
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
        })
        if stage.get("label_box"):
            label = stage["label_box"]
            elements.append({
                "id": element_id("stage_label", stage["id"]),
                "type": "rectangle",
                "x": label["x"],
                "y": label["y"],
                "width": label["w"],
                "height": label["h"],
                "angle": 0,
                "strokeColor": style["header_fill"],
                "backgroundColor": style["header_fill"],
                "fillStyle": "solid",
                "strokeWidth": 1,
                "strokeStyle": "solid",
                "roughness": 0,
                "opacity": 100,
            })
        elements.append({
            "id": element_id("stage_text", stage["id"]),
            "type": "text",
            "x": (stage.get("label_box") or stage)["x"] + 12,
            "y": (stage.get("label_box") or stage)["y"] + 10,
            "width": (stage.get("label_box") or stage)["w"] - 24,
            "height": min(42, (stage.get("label_box") or stage)["h"] - 12),
            "angle": 0,
            "strokeColor": style["header_text"] if stage.get("label_box") else style["text"],
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "text": stage["title"],
            "fontSize": 15,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": None,
            "originalText": stage["title"],
            "lineHeight": 1.25,
        })
    for edge in route["edges"]:
        if not edge.get("valid", True) or edge["from"] not in nodes or edge["to"] not in nodes:
            continue
        x1, y1 = center(nodes[edge["from"]])
        x2, y2 = center(nodes[edge["to"]])
        elements.append({
            "id": element_id("edge", edge["id"]),
            "type": "arrow",
            "x": x1,
            "y": y1,
            "width": x2 - x1,
            "height": y2 - y1,
            "angle": 0,
            "strokeColor": style["line"],
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "points": [[0, 0], [x2 - x1, y2 - y1]],
            "lastCommittedPoint": [x2 - x1, y2 - y1],
            "startBinding": None,
            "endBinding": None,
            "startArrowhead": None,
            "endArrowhead": "arrow",
        })
    for stage in route["stages"]:
        for node in stage["nodes"]:
            box = nodes[node["id"]]
            elements.append({
                "id": element_id("node", node["id"]),
                "type": "rectangle",
                "x": box["x"],
                "y": box["y"],
                "width": box["w"],
                "height": box["h"],
                "angle": 0,
                "strokeColor": style["node_stroke"],
                "backgroundColor": style["node_fill"],
                "fillStyle": "solid",
                "strokeWidth": 1,
                "strokeStyle": "solid",
                "roughness": 0,
                "opacity": 100,
            })
            elements.append({
                "id": element_id("node_text", node["id"]),
                "type": "text",
                "x": box["x"] + 8,
                "y": box["y"] + 15,
                "width": box["w"] - 16,
                "height": box["h"] - 16,
                "angle": 0,
                "strokeColor": style["text"],
                "backgroundColor": "transparent",
                "fillStyle": "solid",
                "strokeWidth": 1,
                "strokeStyle": "solid",
                "roughness": 0,
                "opacity": 100,
                "text": node["label"],
                "fontSize": 14,
                "fontFamily": 1,
                "textAlign": "center",
                "verticalAlign": "middle",
                "containerId": None,
                "originalText": node["label"],
                "lineHeight": 1.25,
            })
    scene = {"type": "excalidraw", "version": 2, "source": "tech-route-maker", "elements": elements, "appState": {"viewBackgroundColor": style["background"]}, "files": {}}
    return json.dumps(scene, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) != 3:
        print("Usage: python render_excalidraw.py <tech-route.json> <output.excalidraw>")
        return 2
    save_text(sys.argv[2], make_excalidraw(load_route(sys.argv[1])))
    print(f"Wrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
