#!/usr/bin/env python3
"""
Refresh the local full version at /home/mark/projects/dad_chatbot_full/ from
this (canonical, public) project.

The full version is what gets distributed to family. It is identical to the
public dad_chatbot project except:
  - paper_summaries/*.html include "View Original PDF" buttons
  - paper_summaries/burgoyne_papers.jsonl retains the pdf_path field
  - it contains burgoyne_papers/ and reference_papers/ PDFs (never synced -
    those are added/maintained manually inside dad_chatbot_full/)

Usage:
  python3 tools/sync_full.py            # mirror everything except the PDFs
  python3 tools/sync_full.py --dry-run  # show what would be copied
"""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FULL_ROOT = Path("/home/mark/projects/dad_chatbot_full")


def copy_if_changed(src: Path, dst: Path, *, dry_run: bool) -> bool:
    if not src.exists():
        return False
    if dst.exists() and src.read_bytes() == dst.read_bytes():
        return False
    if dry_run:
        print(f"  would copy {src} -> {dst}")
        return True
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  copied {src.name}")
    return True


def patch_full_jsonl(*, dry_run: bool) -> None:
    """Mirror the canonical JSONL into the full version, preserving pdf_path
    on entries that already had one."""
    src = PROJECT_ROOT / "paper_summaries" / "burgoyne_papers.jsonl"
    dst = FULL_ROOT / "paper_summaries" / "burgoyne_papers.jsonl"
    if not src.exists():
        print("  ! canonical JSONL missing, skipping")
        return
    src_lines = [l for l in src.read_text().splitlines() if l.strip()]
    dst_lines = [l for l in dst.read_text().splitlines() if l.strip()] if dst.exists() else []
    pdf_paths = {}
    for line in dst_lines:
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = d.get("id") or d.get("title")
        if key and d.get("pdf_path"):
            pdf_paths[key] = d["pdf_path"]
    out = []
    for line in src_lines:
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = d.get("id") or d.get("title")
        if key and key in pdf_paths:
            d["pdf_path"] = pdf_paths[key]
        out.append(json.dumps(d, ensure_ascii=False))
    if dry_run:
        print(f"  would write JSONL ({len(out)} lines, {sum(1 for o in out if 'pdf_path' in o)} with pdf_path)")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(out) + "\n")
    print(f"  wrote JSONL ({len(out)} lines)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not FULL_ROOT.exists():
        print(f"ERROR: full root {FULL_ROOT} does not exist", file=sys.stderr)
        sys.exit(1)

    print("== Rendering paper summaries with PDF links ==")
    cmd = [
        "python3", str(PROJECT_ROOT / "tools" / "build_summary.py"),
        "--all", "--full",
        "--out", str(FULL_ROOT / "paper_summaries"),
    ]
    if args.dry_run:
        print(f"  would run: {' '.join(cmd)}")
    else:
        subprocess.run(cmd, check=True)

    print("\n== Mirroring index.html, CSS, images ==")
    for rel in ["index.html", "assets/style.css",
                "dad.png", "flinders_logo.png", "flinders_logo_white.png"]:
        copy_if_changed(PROJECT_ROOT / rel, FULL_ROOT / rel, dry_run=args.dry_run)

    print("\n== Patching JSONL (preserving pdf_path entries) ==")
    patch_full_jsonl(dry_run=args.dry_run)

    print("\nDone. PDFs in burgoyne_papers/ and reference_papers/ are not touched.")


if __name__ == "__main__":
    main()
