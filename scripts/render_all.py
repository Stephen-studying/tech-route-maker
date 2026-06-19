import argparse
import shutil
import subprocess
import sys
from pathlib import Path


SCRIPT_BY_FORMAT = {
    "mermaid": ("render_mermaid.py", "tech-route.mmd"),
    "svg": ("render_svg.py", "tech-route.svg"),
    "drawio": ("render_drawio.py", "tech-route.drawio"),
    "excalidraw": ("render_excalidraw.py", "tech-route.excalidraw"),
    "html": ("render_html.py", "tech-route.html"),
    "markdown": ("render_markdown.py", "TECH_ROUTE.md"),
    "pptx": ("render_pptx.py", "tech-route.pptx"),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("route_json")
    parser.add_argument("output_dir")
    parser.add_argument("--formats", required=True, help="Comma-separated formats or all")
    args = parser.parse_args()
    selected = [x.strip().lower() for x in args.formats.split(",") if x.strip()]
    if "all" in selected:
        selected = list(SCRIPT_BY_FORMAT) + ["json"]
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    script_dir = Path(__file__).resolve().parent
    for fmt in selected:
        if fmt == "json":
            target = out_dir / "tech-route.json"
            if Path(args.route_json).resolve() != target.resolve():
                shutil.copyfile(args.route_json, target)
                print(f"Wrote {target}")
            else:
                print(f"Kept {target}")
            continue
        if fmt not in SCRIPT_BY_FORMAT:
            raise SystemExit(f"Unknown format: {fmt}")
        script, filename = SCRIPT_BY_FORMAT[fmt]
        subprocess.check_call([sys.executable, str(script_dir / script), args.route_json, str(out_dir / filename)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
