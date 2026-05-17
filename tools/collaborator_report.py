#!/usr/bin/env python3
"""
Generate a collaborator-frequency report from the YAML corpus.

Lists every co-author surname (excluding Burgoyne) with the count of papers
they appear in and the list of paper IDs. Useful for spotting collaborators
who deserve a card in the index.html collaborator network section.

Writes to `collaborator_report.md` in the project root.

Usage:
  python3 tools/collaborator_report.py
"""
from __future__ import annotations
import yaml
import re
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "paper_data"
OUT = PROJECT_ROOT / "collaborator_report.md"


def main() -> None:
    by_surname: dict[str, list[tuple[str, int, list[str]]]] = defaultdict(list)
    for f in sorted(DATA_DIR.glob("*.yaml")):
        d = yaml.safe_load(open(f))
        pid = d.get("id", f.stem)
        m = re.match(r"(\d{4})_", pid)
        year = int(m.group(1)) if m else 0
        authors = d.get("authors") or []
        for a in authors:
            if not a:
                continue
            surname = a.strip().split()[-1].strip("*.,")
            if surname.lower() == "burgoyne" or len(surname) < 3:
                continue
            by_surname[surname].append((pid, year, authors))

    # Sort by paper count desc, then alphabetical
    rows = sorted(by_surname.items(), key=lambda kv: (-len(kv[1]), kv[0].lower()))

    with OUT.open("w") as out:
        out.write("# Collaborator frequency report\n\n")
        out.write(f"Generated from {len(list(DATA_DIR.glob('*.yaml')))} YAML files. ")
        out.write("Collaborators sorted by paper count (excluding Burgoyne).\n\n")
        out.write("| Surname | Papers | Year span | IDs |\n")
        out.write("|---|---|---|---|\n")
        for surname, papers in rows:
            n = len(papers)
            years = [y for _, y, _ in papers if y]
            span = f"{min(years)}-{max(years)}" if years else ""
            ids = ", ".join(sorted({p for p, _, _ in papers}))
            out.write(f"| {surname} | {n} | {span} | {ids} |\n")
    print(f"wrote {OUT}")
    print(f"collaborators in 2+ papers: {sum(1 for _, ps in rows if len(ps) >= 2)}")


if __name__ == "__main__":
    main()
