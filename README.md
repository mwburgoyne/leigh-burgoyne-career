# The Career Arc of Professor Leigh A. Burgoyne AM

A "This is your life" tribute page for **Professor Leigh A. Burgoyne AM** — Emeritus, Flinders University of South Australia.

**Live site:** [https://mwburgoyne.github.io/leigh-burgoyne-career/](https://mwburgoyne.github.io/leigh-burgoyne-career/)

The page covers six decades of Leigh's career, from yeast enzymology in 1960s Adelaide through the 1973 chromatin substructure landmark (cited by Roger Kornberg in his Nobel-winning nucleosome work), the FTA paper invention, and on to the 2025 macrofungi DNA extraction protocol he co-authored at age 84.

## What's here

- `index.html` — the interactive tribute page (hero, timeline, four career-phase narratives, browse-and-filter publications, collaborator network, honours)
- `paper_summaries/` — 91 individual HTML pages, one per paper, rendered from YAML
- `paper_summaries/burgoyne_papers.jsonl` — the same data as a JSONL feed for future RAG use
- `paper_data/` — the YAML source of truth (one file per paper)
- `tools/` — build pipeline (`build_summary.py`, `extract_summaries.py`, `update_citations.py`, `sync_full.py`)
- `assets/style.css` — shared stylesheet for both the index page and per-paper summaries

## Rebuilding the site

```bash
python3 tools/build_summary.py --all              # regenerate every paper_summaries/*.html
python3 tools/update_citations.py --refresh       # refresh live citation counts
```
