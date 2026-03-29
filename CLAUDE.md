# Dad Chatbot Project — Claude Memory

## Project Overview
Mark Burgoyne is creating a "This is your life" tribute to his father, **Professor Leigh A. Burgoyne AM** (Emeritus, Flinders University of South Australia). The project involves ingesting all of Burgoyne's publications, creating HTML summaries, maintaining a JSONL dataset for future RAG use, and building an interactive career arc narrative page.

## Current State (as of 2026-03-29)

### Completed
- **93 entries processed** (79 original papers + 1 placeholder replaced + 7 from to_check batch + 4 new: Crick BBC transcript, Murray 1979 acknowledgment, 1990 forensic book chapter, Kornberg 1974 citing paper + 1 new: 1978 Cell Nucleus review chapter + 1 new: 1985 Cytobios back-to-back zig-zag model) — all HTML summaries in `paper_summaries/`, all JSONL entries in `paper_summaries/burgoyne_papers.jsonl`, all career arc notes in `career_arc_notes.md`
- **index.html** (formerly `career_arc.html`) — Interactive career arc tribute page, deployed via GitHub Pages. Self-contained HTML/CSS/JS with:
  - **Introduction section** — warm, accessible overview of Leigh's life and career for both specialists and family members; explicitly frames the page as scientific record and family tribute
  - Co-author filtering (searchable dropdown with name normalization)
  - Theme/topic filtering (13 clickable theme buttons)
  - SVG timeline visualization (dots sized by citations, color-coded by phase, tooltips include paper titles)
  - Career arc organized by 4 phases (expandable sections) — each phase has an italic plain-language lead paragraph ("teaser") **always visible outside the collapsible area**, with a "Read more" link and clickable header to expand the technical detail
  - **Browse & Filter Publications** — single collapsible section (collapsed by default) combining the filter controls and the full publication list; italic hint line visible when collapsed; timeline dot clicks auto-expand this section before scrolling
  - Collaborator network section — descriptions humanised with relationship context, not just technical topics
  - Section order: Hero → Introduction → Stats → Timeline → Career Arc → Honours & Awards → Browse & Filter Publications → Collaborators → Footer
  - **Dual-audience design**: page serves both domain specialists (e.g. Leigh himself) and non-specialist family (Mark, his sisters). Technical jargon is explained in context; key discoveries have plain-English analogies (e.g. "thread wound around beads" for nucleosomes, "biological postcode" for soil DNA)
- **SESSION_STATUS.md** — Master tracking document with full task list, file inventory, collaborator registry, and workflow documentation

### Holistic Review Complete
- All 79 paper summaries reviewed with benefit of full career context
- Bottom "Back to Career Arc" link added to all HTML files
- Posthumous/finality language fixed in 8 files (removed "capstone," "final publication," "last known," "concluded with")
- 2 factual errors corrected (author order in 1970 paper, wrong attribution in 1971 paper)
- ~25 missing forward/backward connections added across 19 files

### Biographical Integration Complete (2026-03-18)
- Birth date, degree progression, Fulbright Scholar, four study leaves, and self-described expertise quote added to index.html
- Honours & Awards section added (6 entries: Citation Classic, Australian Technology Award, SA Great, Flinders Outstanding Contribution, two NIFS awards, Member of the Order of Australia AM 2024)
- Pyknosis paper elevated with "Leigh's proudest paper" note
- Citation Classic (1982) noted in Phase 2 influence-box
- Study-leave hosts (J. Tata, D. Bootsma, D. Finnegan) added to collaborator registry

### Nobel Prize Language (2026-03-19)
- index.html introduction and Phase 2 sections rewritten to explicitly name Roger Kornberg as the 2006 Nobel Prize in Chemistry recipient
- Chain of influence clearly described: Hewish & Burgoyne 1973 experiment → Kornberg 1974 nucleosome model → Kornberg 2006 Nobel Prize
- Language carefully avoids any implication that Burgoyne received a Nobel Prize (Leigh was uncomfortable with previous wording)
- Kornberg 1974 paper processed as a "citing paper" with full HTML summary including the exact quotes where Kornberg credits "Hewish and Burgoyne" as "the first such observation"

### 1978 Cell Nucleus Review Chapter (2026-03-24)
- Burgoyne & Hewish, "The Regular Substructure of Mammalian Nuclei and Nuclear Ca-Mg Endonuclease," Chapter 2 in *The Cell Nucleus*, Volume 4: Chromatin, Part A (ed. Harris Busch), pp. 47-74, Academic Press, published 28 January 1978. ISBN 0-12-147604-9.
- Authoritative invited review synthesising the entire Burgoyne-Hewish chromatin substructure programme (1970-1977). Last co-authored publication with Hewish.
- Prescient speculation that Ca-Mg endonuclease's natural function is "programmed nuclear destruction during necrosis" — foreshadowing apoptotic DNA laddering and the 1999 pyknosis paper by two decades.
- Not indexed in citation databases (book chapter). Confirmed publication details via Elsevier product page.

### 1985 Cytobios Back-to-Back Zig-Zag Model (2026-03-28)
- Burgoyne (sole author), "A back-to-back zig-zag model for higher order chromatin structure," Cytobios 43, 141-147, 1985. Accepted 6 June 1985.
- Sole-author theoretical paper formally proposing the fold-back model for chromatin higher-order structure as an alternative to the solenoid (Finch & Klug 1979) and coiled ribbon (Woodcock et al. 1984) models.
- Zig-zag nucleofilament folds back on itself in hairpin loops; interdigitation naturally produces the dinucleosomal repeat. Predicts base-sequence control of higher-order folding. Proposes primitive mechanism for meiotic synaptic alignment.
- Published in small Cambridge journal; ~5 citations. Leigh notes to Mark: "the rest of the world" missed this paper, contributing to incorrect solenoid/coil depictions persisting in textbooks and on Wikipedia for decades. The fold-back model is substantially closer to what modern cryo-EM has confirmed.
- PDF renamed to `burgoyne_1985_cytobios_backtoback_zigzag.pdf` in `burgoyne_papers/`. HTML summary includes Leigh's personal note to Mark. Phase 3 narrative in index.html updated to specifically mention this paper and its neglect.
- career_arc_notes.md entry: 23a. index.html papers array and JSONL already had entries from a previous session; HTML summary file updated with correct PDF link and Leigh's note.
- Wording correction (2026-03-28): In the Context & Background section, changed "Burgoyne had shown that the nucleosome filament adopts a zig-zag conformation" to "Burgoyne had accepted that the…" — Leigh's correction; he accepted the zig-zag conformation rather than being the one who demonstrated it.

### Document Types Tracked
The project tracks four types of documents in the publication list and JSONL:
1. **Burgoyne publications** — papers, patents, book chapters where Burgoyne is an author/inventor
2. **Recognition documents** — external sources crediting Burgoyne's work (e.g. Crick BBC transcript)
3. **Acknowledgment papers** — papers by others that acknowledge Burgoyne for discussions (e.g. Murray & Fitzgerald 1979)
4. **Citing papers** — key papers that cite Burgoyne's work (e.g. Kornberg 1974 nucleosome model)

### Pending
- **~30 additional publications** the user plans to add (list provided in conversation — includes PhD thesis, book chapters, conference abstracts, and papers from 1967-2019). When PDFs arrive, process them the same way (HTML + JSONL + career_arc_notes.md + update index.html papers array)
- **Bob Symons obituary** — mentioned by Leigh
- Future RAG chatbot integration using the JSONL data

### Visual Design (established)
- **Flinders University colour scheme** applied throughout:
  - Primary: Midnight Blue `#002F60` (headings, text, buttons, stats, controls)
  - Accent: Gold `#FFD300` (section header underlines, active button text, footer top border, timeline dot hover stroke, hero bottom border)
  - Hero: deep navy gradient (`#001a3a` → `#003b73`)
  - Footer: Midnight Blue background with gold top border
- **Hero layout**: Flinders white logo (left) | title & subtitle (centre) | `dad.png` portrait in circle with gold border (right). Stacks vertically on mobile. Subtitle: "From Chromosomes to Crime Scenes — Six Decades of Discovery"
- **Phase colours preserved** (distinct from Flinders chrome): Purple `#6b46c1` (Phase 1), Red `#c53030` (Phase 2), Blue `#2b6cb0` (Phase 3), Green `#276749` (Phase 4)
- **Assets**: `flinders_logo_white.png` and `flinders_logo.png` (black version) downloaded to project root; `dad.png` (portrait cutout) in root

### Layout Preferences & Interactivity (established)
- **Career Arc teaser design (2026-03-29):** Each phase's italic lead paragraph sits in a `.phase-teaser` div **outside** the collapsible `.phase-content`, always visible without clicking. A `.phase-read-more` link ("Read more"/"Read less" with rotating arrow) sits between the teaser and the collapsible content. Both the phase header and the read-more link toggle the same content via `togglePhase()` using `.closest('.phase-section')`.
- **Browse & Filter Publications (2026-03-29):** The former separate "Filter & Explore" and "Publication List" sections are combined into a single collapsible section headed "Browse & Filter Publications", collapsed by default. A one-line italic hint ("Click to browse all N publications with co-author and theme filters.") is visible when collapsed and hidden when expanded. Uses `toggleRefSection()` and `ensureRefSectionOpen()` JS functions. CSS class `.ref-section-content` uses `max-height: none` when open (no fixed max-height limit).
- Timeline tooltips include paper titles (bulleted) alongside year, count, and citation totals
- Timeline dots are clickable — clicking a dot auto-expands the Browse & Filter section (if collapsed) then smooth-scrolls to the first matching publication entry for that year, with a brief yellow highlight flash (50ms delay to allow section expansion)
- Timeline dots show hover effect (full opacity + gold stroke) to signal interactivity
- Publication entries have `data-year` attributes for year-based targeting
- Timeline container has no scrollbar — SVG scales to fit container width (`overflow-x: hidden`, no `min-width` on SVG wrap)

## Dual-Version Setup (established 2026-03-29)

Two versions of the project are maintained:

| Version | Path | Purpose |
|---------|------|---------|
| **Sanitised (GitHub)** | `/home/mark/projects/dad_chatbot/` | Public-facing, no PDFs, no PDF download links. Pushed to GitHub Pages. |
| **Full (local only)** | `/home/mark/projects/dad_chatbot_full/` | Contains all source PDFs (`burgoyne_papers/`, `reference_papers/`), HTML summaries with "View Original PDF" buttons and poster links, JSONL with `pdf_path` fields. For family distribution. Never pushed to GitHub. |

**IMPORTANT workflow rule:** When making edits to content (HTML summaries, index.html, JSONL, career_arc_notes.md, etc.), **duplicate the changes to both versions**. The sanitised version omits PDFs and PDF links; everything else should stay in sync. When processing new papers, create the full version first (in `dad_chatbot_full`), then copy the HTML summary to `dad_chatbot` with PDF links stripped.

### What was removed from the sanitised version
- `burgoyne_papers/` directory (102 PDFs + 11 posters)
- `reference_papers/` directory (1 PDF)
- All `<a class="pdf-link">View Original PDF</a>` buttons from 91 HTML summaries
- All "Related Conference Poster(s)/Abstract(s)" sections (7 across 7 files)
- `.pdf-link` and `.pdf-link:hover` CSS rules from all HTML summaries
- `pdf_path` field from 87 JSONL entries

## Deployment
- **GitHub Pages repository**: `https://github.com/mwburgoyne/leigh-burgoyne-career`
- **Git remote**: `origin` is configured to `https://github.com/mwburgoyne/leigh-burgoyne-career.git`
- **Main file**: `index.html` (renamed from `career_arc.html` on 2026-03-29 for GitHub Pages compatibility)
- **Branch**: `master`
- All paper summary "Back to Career Arc" links point to `../index.html`
- When asked to push, use `git push origin master`

## Key Files
- `SESSION_STATUS.md` — Master tracking document (read this first when resuming)
- `career_arc_notes.md` — Working career arc notes organized by career phases + collaborator registry
- `index.html` — The main interactive tribute page (renamed from `career_arc.html` for GitHub Pages deployment)
- `paper_summaries/burgoyne_papers.jsonl` — 93-entry JSONL dataset for RAG
- `paper_summaries/*.html` — 93 individual summary HTML files (includes recognition, acknowledgment, and citing paper entries)
- `burgoyne_papers/` — Source PDFs (Burgoyne publications and related recognition/acknowledgment documents)
- `reference_papers/` — Non-Burgoyne papers relevant to the career arc (e.g. Kornberg 1974 nucleosome model)
- `Leigh_Burgoyne_Publications_DOI_List.docx` — Master publication list
- `dad.png` — Portrait photo of Prof Burgoyne (transparent background cutout)
- `flinders_logo_white.png` — White Flinders University logo (for dark backgrounds)
- `flinders_logo.png` — Black/navy Flinders University logo (for light backgrounds)

## Processing Workflow (Per Paper)
1. Read PDF via Read tool
2. Quick citation lookup via OpenAlex API
3. Create HTML summary in `paper_summaries/` with consistent CSS styling (blue meta boxes, green influence boxes, orange connections boxes, red PDF buttons, `<mark>` around Burgoyne's name)
4. Append JSONL entry to `burgoyne_papers.jsonl`
5. Update `career_arc_notes.md` with numbered entry in appropriate phase
6. Update collaborator registry if new collaborators appear
7. Update `SESSION_STATUS.md`

Process papers **two at a time in parallel** using Task agents. Hard auto-compact after every 4 papers.

**Non-Burgoyne papers** (recognition, acknowledgment, citing papers): same workflow but PDFs go to `reference_papers/` (if not directly related to Burgoyne) or `burgoyne_papers/` (if recognition/acknowledgment documents). JSONL `type` field distinguishes: `"recognition"`, `"acknowledgment"`, `"citing_paper"`.

**IMPORTANT**: Use Claude (Opus) model, not Sonnet, for writing paper summaries and career arc updates. Sonnet can be used for file identification and data extraction only.

## Writing Style
Based on Mark's writing style guide (source: `/home/mark/projects/Assurance_POC/0-Info/Writing_Style_Guide.md`). This project allows a slightly warmer, more marketing-friendly tone than the assurance reports, but the core anti-AI-tell rules apply strictly. The page should read like it was written by a person, not generated.

### Hard rules
- **No em-dashes** (`&mdash;`, `—`). Use commas, parentheses, semicolons, colons, or start a new sentence. En-dashes (`&ndash;`) in date/number ranges are fine.
- **Banned words/phrases** (immediate AI tells, never use): "comprehensive" (unless naming a specific study), "robust", "holistic", "seamlessly", "cutting-edge", "genuinely", "straightforward", "notably", "importantly", "interestingly", "it's worth noting", "it should be noted", "this is particularly relevant", "let's dive in", "let's unpack", "here's where it gets interesting"
- **No passive hedging**: "it was noted that...", "it might be worth considering"
- **Australian/British English**: favour, honour, colour, recognise, defence, programme (except in proper nouns)
- **Active voice** for statements of fact
- **No padding**: every sentence earns its place
- **No section preambles** that preview what follows ("In this section we will discuss...")
- **Dates**: day-month format (22 September 1939, not September 22, 1939)

### Tone
- Experienced person explaining to a peer or family member. Direct, specific, clear
- Authority comes from the content, not from the language
- Contractions are fine (personal tribute, not a formal report)
- Short paragraphs, mixed sentence lengths
- Not: plausible-sounding AI text, padding, hedging, or sales pitch

### Allowed exceptions
- Em-dashes in `<title>` tags (browser tab separator)
- Em-dashes in DOI placeholder fields (`<p><strong>DOI:</strong> &mdash;</p>`)
- Em-dashes in quote attribution lines (`<div class="attribution">&mdash; Francis Crick...`)
- Em-dashes in structural labels (study leave headings, award names, pyknosis heading, stats bar labels, footer dedication)
- Em-dashes in Leigh's direct quotes (quoted speech)
- The word "robust" in paper titles that actually use the word (e.g. "Robust and reliable DNA typing of soils")

## User Preferences
- Fully autonomous, hands-free operation - do NOT prompt for permission or ask questions during paper processing
- Don't spider references - use existing knowledge to assess significance
- Work in parallel pairs via Task agents
- Focus on content, influence, and career arc - not detailed methods unless central
- No emojis unless requested
- **Dual audience**: page must serve both domain specialists (Leigh) and non-specialist family members (Mark, his sisters). Explain jargon in context; provide plain-language lead paragraphs for each career phase
- Section heading is "Career Arc" (not "Career Narrative")
- Footer: warm/personal tone — "For Dad — whose curiosity never stops." (present tense)
- Stats bar labels should be accessible to non-scientists (e.g. explain what citations are)
- **IMPORTANT: Leigh is alive and still researching.** All language must use present tense for his ongoing career. Say "most recent paper" not "final paper". Use "1993–present" not "1993–2025". Footer year is 2026.
- **Nobel Prize language**: Don't over-disclaim. The chain of influence (Hewish & Burgoyne 1973 → Kornberg 1974 nucleosome model → Kornberg 2006 Nobel Prize in Chemistry) should be stated factually — name Kornberg as the recipient, describe the citation chain, and let the facts speak for themselves. No "To be clear, Leigh did not receive a Nobel Prize" disclaimers — the context makes this obvious and the defensive phrasing was unwanted.

## Biographical Details
- **Born:** 22 September 1939, Adelaide, South Australia
- **Degrees:** BSc Agricultural Science (1962), Honours in Agricultural Biochemistry (1963), PhD in Biochemistry (May 1968) — all University of Adelaide
- **Fulbright Scholar** — postdoctoral fellowship at Yale University (1968–1969)
- **Study leaves:** MRC Mill Hill, London, J. Tata (1973–74, 9 months); MRC LMB, Cambridge (1977–78, 8 months); Erasmus University Rotterdam, D. Bootsma (1981–82, 6 months); Edinburgh University, D. Finnegan (1991, 5 months)
- **Awards:** Citation Classic (1982), Australian Technology Award finalist (May 1999), SA Great Award for Science (Dec 1999), Outstanding Contribution to Flinders University (2006), Two NIFS awards (2012), **Member of the Order of Australia (AM)** (2024 Australia Day Honours, for significant service to science)

## Career Phase Structure
- **Phase 1: Yeast Enzymology (1966-1969)** — BSc/Honours/PhD Adelaide, Fulbright postdoc Yale
- **Phase 2: DNA Synthesis & Replication (1970-1974)** — Flinders, Ca2+ endonuclease, **1973 landmark chromatin paper (~1172 citations, Citation Classic 1982)**; study leave Mill Hill (1973–74)
- **Phase 3: Chromatin Structure (1975-1992)** — Superstructure, satellite DNA, AT studies; study leaves Cambridge (1977–78), Rotterdam (1981–82), Edinburgh (1991)
- **Phase 4: DNA Forensics, FTA & Applied Biology (1993-present)** — FTA invention, ~19 patents, soil metagenomics, **pyknosis (1999) is Leigh's proudest paper**, 2025 macrofungi paper at age ~84, still active

## Key Fact
The 1973 Hewish & Burgoyne paper discovering chromatin substructure (~1,172 citations) is the career peak. Roger Kornberg explicitly cited it as "the first such observation" in his 1974 nucleosome model paper (Science 184, 868–871; ~2,606 citations). Kornberg received the 2006 Nobel Prize in Chemistry for his subsequent work on eukaryotic transcription, built upon the chromatin structural understanding established in that 1974 paper. Francis Crick described the Hewish & Burgoyne result as a "breakthrough" on BBC Radio Three in March 1974. The 1973 paper was designated a Citation Classic in 1982 — one of only 10 Australian biomedical papers with that distinction. The 2025 macrofungi paper self-cites this discovery, bringing the career full circle. Leigh identifies the 1999 pyknosis paper as his proudest publication. Leigh is still actively researching.

## Anecdotes (from Leigh via Mark)
- **Crick and the stuck paper (1974):** The Burgoyne, Hewish & Mobbs 1974 2D PAGE paper had been languishing with the *Biochemical Journal* editors. Francis Crick telephoned Leigh to ask when it would be published — he wanted to cite it in his own chromatin paper (likely the "Kornberg, Klug, F. H. C. Crick, in preparation" listed as ref 38 in Kornberg's 1974 nucleosome model paper). When Leigh told him it was stuck, Crick apparently contacted the journal himself — the paper was accepted the next day. Recorded in the 1974 2D PAGE summary, Kornberg summary, and career_arc_notes.md.
- **The paper the world missed (1985):** Leigh sent Mark his 1985 Cytobios sole-author paper proposing the back-to-back zig-zag fold-back model for chromatin higher-order structure with the note: "I think that the AI missed this published paper. So did the rest of the world and that is why Wikipedia still, or did until recently, showed chromatin as a coil, leaving a falsity in the body of knowledge about chromatin." He added that he wasn't sure it was ever cited except by himself. The model proposed — non-helical fold-back zig-zag — is closer to what modern cryo-EM has confirmed than the solenoid models that dominated for decades.
