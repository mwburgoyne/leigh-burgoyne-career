#!/usr/bin/env python3
"""
Scan section bodies for author+year mentions that could be cross-linked to
other papers in the corpus, and produce a review report.

Matches "Surname (YYYY)" and "Surname1 & Surname2 (YYYY)" patterns. A match
is reported only when:
  - the cited (Surname, YYYY) maps to exactly one paper in the corpus AND
  - the cited surname matches the FIRST author of that paper (so co-author
    references don't get linked to the wrong paper)

The report is markdown, grouped by source paper, and is written to
`intra_link_suggestions.md`. Apply manually by editing the YAML body_html.

Usage:
  python3 tools/find_intra_links.py
"""
from __future__ import annotations
import yaml
import re
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "paper_data"
OUT = PROJECT_ROOT / "intra_link_suggestions.md"


def first_author_surname(d: dict) -> str | None:
    for a in d.get("authors") or []:
        if a:
            return a.strip().split()[-1].strip("*.,").lower()
    return None


def main() -> None:
    papers = []
    by_first_year: dict[tuple[str, int], list[str]] = defaultdict(list)
    for f in sorted(DATA_DIR.glob("*.yaml")):
        d = yaml.safe_load(open(f))
        papers.append(d)
        m = re.match(r"(\d{4})_", d.get("id", ""))
        if not m:
            continue
        year = int(m.group(1))
        first = first_author_surname(d)
        if not first:
            continue
        by_first_year[(first, year)].append(d["id"])

    # Match a full author-list-plus-year citation: one or more capitalised
    # surnames joined by ", " / " & " / " &amp; " / " and ", followed by "(YYYY)".
    # We then peel off the FIRST surname for the lookup.
    surname = r"[A-Z][a-zA-Z'-]{2,}"
    sep = r"(?:,\s+|\s+&\s+|\s+&amp;\s+|\s+and\s+)"
    pat = re.compile(rf"\b({surname}(?:{sep}{surname})*)\s*\((\d{{4}})[a-z]?\)")
    first_surname_re = re.compile(rf"^({surname})")
    # Look-behind: if the chars immediately before the match end with a
    # co-author separator, the regex's start surname is a co-author and the
    # link target would be wrong.
    co_author_prefix = re.compile(r"(?:,|&|&amp;|\band\b)\s*$")

    suggestions: dict[str, list[str]] = defaultdict(list)
    for d in papers:
        pid = d.get("id")
        for section in d.get("sections") or []:
            heading = section.get("heading") or ""
            body = section.get("body_html") or ""
            for m in pat.finditer(body):
                preceding = body[max(0, m.start() - 40): m.start()]
                if co_author_prefix.search(preceding):
                    continue
                fm = first_surname_re.match(m.group(1))
                if not fm:
                    continue
                cited = fm.group(1).lower()
                year = int(m.group(2))
                key = (cited, year)
                if key not in by_first_year:
                    continue
                candidates = [c for c in by_first_year[key] if c != pid]
                if len(candidates) != 1:
                    continue
                target = candidates[0]
                # Skip if already linked
                start = max(0, m.start() - 80)
                end = min(len(body), m.end() + 20)
                context = body[start:end]
                if f"{target}.html" in context:
                    continue
                suggestions[pid].append(
                    f"  - section '{heading}': **{m.group(0)}** -> `{target}.html`"
                )

    with OUT.open("w") as out:
        out.write("# Intra-corpus link suggestions\n\n")
        out.write("Candidate cross-links between papers in the corpus. ")
        out.write("Each entry shows a passage in `paper_data/<source>.yaml` where ")
        out.write("a citation could be wrapped in `<a href=\"<target>.html\">...</a>`.\n\n")
        out.write("Only matches where the cited surname is the **first author** of ")
        out.write("the target paper are listed (so co-author references aren't ")
        out.write("misrouted).\n\n")
        total = sum(len(v) for v in suggestions.values())
        out.write(f"**{total} candidate links across {len(suggestions)} papers.**\n\n")
        for pid in sorted(suggestions):
            out.write(f"## {pid}\n\n")
            for line in suggestions[pid]:
                out.write(line + "\n")
            out.write("\n")
    print(f"wrote {OUT}")
    print(f"{total} candidate links across {len(suggestions)} papers")


if __name__ == "__main__":
    main()
