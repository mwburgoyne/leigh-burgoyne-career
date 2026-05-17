#!/usr/bin/env python3
"""
Render a paper-summary HTML from its YAML data file.

Default output is the public/sanitised form (no PDF download buttons). Pass
--full to include the PDF-link anchor recorded in the YAML (used when
rendering into the local-only dad_chatbot_full/ directory beside the PDFs).

Usage:
    python build_summary.py paper_data/<id>.yaml [--out paper_summaries/]
    python build_summary.py --all
    python build_summary.py --all --full --out ../dad_chatbot_full/paper_summaries
"""
from pathlib import Path
import argparse
import sys
import yaml
from jinja2 import Environment, FileSystemLoader

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = PROJECT_ROOT / "tools" / "templates"
DATA_DIR = PROJECT_ROOT / "paper_data"
OUT_DIR = PROJECT_ROOT / "paper_summaries"


def authors_html(authors, burgoyne_index=None):
    """Render authors as a single comma-separated string with <mark> around Burgoyne."""
    if not authors:
        return ""
    if burgoyne_index is None:
        burgoyne_index = next(
            (i for i, a in enumerate(authors) if "Burgoyne" in a), None
        )
    rendered = []
    for i, a in enumerate(authors):
        if i == burgoyne_index:
            rendered.append(f"<mark>{a}</mark>")
        else:
            rendered.append(a)
    return ", ".join(rendered)


def render(data_path: Path, is_sanitised: bool = True) -> str:
    with data_path.open() as f:
        data = yaml.safe_load(f)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        keep_trailing_newline=True,
    )
    template = env.get_template("summary.html.j2")

    ctx = dict(data)
    ctx["authors_html"] = authors_html(data.get("authors"), data.get("burgoyne_index"))
    if data.get("authors"):
        ctx.setdefault("page_title", f"{data['authors'][0].split()[-1]} et al. - {data['title']}")
    else:
        ctx.setdefault("page_title", data.get("title", data.get("id", "")))
    ctx["is_sanitised"] = is_sanitised
    return template.render(**ctx)


def output_path_for(data_path: Path) -> Path:
    return OUT_DIR / f"{data_path.stem}.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("yaml", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default=str(OUT_DIR))
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("--full", action="store_true",
                     help="Include the PDF-link anchor (for the local "
                          "dad_chatbot_full/ render alongside the PDFs).")
    # Kept for backward compatibility - default is already sanitised
    grp.add_argument("--sanitised", action="store_true",
                     help="(default) Strip PDF download link.")
    args = ap.parse_args()

    if args.all:
        files = sorted(DATA_DIR.glob("*.yaml"))
        if not files:
            print(f"No YAML files in {DATA_DIR}", file=sys.stderr)
            sys.exit(1)
    elif args.yaml:
        files = [Path(args.yaml)]
    else:
        ap.print_help()
        sys.exit(1)

    is_sanitised = not args.full  # default is sanitised
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        html = render(f, is_sanitised=is_sanitised)
        out = out_dir / f"{f.stem}.html"
        out.write_text(html)
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
