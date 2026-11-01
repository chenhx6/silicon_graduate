---
type: synthesis
title: Book corpus coverage ledger and verifiable study queue
aliases: [book-corpus-coverage, book-library-study-ledger]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
scope: raw-books-recursive-inventory-and-reading-evidence
confidence: high-for-file-measurements-only
sources: [book-petrache-chirality-and-wobbling, book-bohr-mottelson-nuclear-structure, book-bohr-mottelson-nuclear-structure-vol2, book-heyde-nuclear-physics-concepts, book-iaea-reaction-data-handbook, book-bertulani-nuclear-reactions, book-bonamente-statistics-scientific-data, book-wu-nuclear-experiment-methods, book-zhu-probability-statistics-in-physics, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, frauendorf-2024-wobbling-review, sheikh-jehangir-bhat-2024-tpsm-wobbling]
tags: [book-corpus, reading-coverage, evidence-boundary, study-queue, ocr]
---

# Book corpus coverage ledger

## Question and Scope

What is actually present in `raw/books/`, what prior reading can be traced to it,
and what remains to be studied? This ledger covers **all 33 PDFs recursively,
12,076 physical pages and 2,754 bookmark entries**, including the seven PDFs in
the ScienceDirect subdirectory. There are 33 distinct SHA-256 identities. The
denominator includes books, a report, review articles, atomic-data papers and an
editorial page; it is not a count of 33 nuclear-structure textbooks.

This is a completed inventory and an open study queue. **No chapter was awarded
reading credit by this audit.** Extraction, a `reading_depth: deep-read` label,
a bibliography entry, bookmark, synthesis page, or successful analysis program
does not establish completed study. In particular, the historical claim of
“92 production modules” supplies no evidence of book knowledge. The handoff's
“全量专著吸收完成” statement (`system/handoff.md:267`) exceeds the reading evidence
verified here. The historical files and review states are preserved.

## Evidence and measurement contract

The reproducible metadata receipt is
`outputs/learning-milestones/20261102-book-corpus-inventory.json`; the producer is
`system/scripts/book_corpus_inventory.py`. The receipt preserves each PDF's
repository path, size, SHA-256, actual page count, every bookmark and every page's
native-text character count, nonwhitespace count, replacement-character count,
image coverage and parser-warning count. Its producer section pins the script,
Python, PyMuPDF and MuPDF versions and text flags. It contains no extracted body
text, rendered pages or OCR transcript. The original PDFs are opened read-only;
each hash is compared before and after inspection.

All ranges below are inclusive, **one-based physical PDF pages**, not printed
folios. `PDF 1-40` means every physical page from 1 through 40. Embedded PDF
labels are recorded separately and are not assumed reliable. The primary
`native_text_chars` metric is the Unicode length of the untrimmed result of
`page.get_text("text", flags=TEXTFLAGS_TEXT, sort=False)`; whitespace is included.
The separate nonwhitespace metric controls triage. “Native” means an existing
PDF text layer, which may itself be historical OCR, not proof of born-digital
or correct text.

| Measured state | Pages | Meaning |
|---|---:|---|
| Zero nonwhitespace native characters | 4,043 | Includes blank pages, scans and pages needing visual triage |
| Nonzero but fewer than 100 nonwhitespace characters | 81 | Includes title pages, running folios and sparse figures |
| OCR or visual transcription route | 4,022 | Fewer than 100 nonwhitespace characters and image-rectangle union covering at least 50% of the page |
| Zero-text visual triage without that raster coverage | 46 | No automatic assumption that these pages are blank |
| Sparse-text visual triage without that raster coverage | 56 | Inspect the rendered page before selecting an access method |
| Text layer over raster union covering at least 80% | 1,625 | Quality-check existing OCR, including symbols and reading order |
| Other pages with available native text | 6,327 | Availability only; no scientific reading credit |
| Pages with parser warnings | 104 | May overlap the access classes; inspect equations and figures before reuse |

The five access-route rows total 12,076; zero/sparse/warning rows are overlapping
diagnostics, not additional pages. Seven PDFs have zero native text on every
page: B10, B26, B27, B28, B29, B31 and B33. B20 has text on only PDF 532, 559
and 727; those three islands do not make the surrounding scanned chapters
searchable. B24, B25 and B30 mostly have text layers over scans.

The OCR route is an exact reproducible **access-routing set**, not a claim
that every flagged page contains prose. It deliberately includes scan covers
and possible blank scans. For each routed page either produce checked OCR or
visual transcription, or document a visual blank/decorative-page exemption.
Do not silently subtract blanks on the basis of zero text. B29 contains tiled
scans, so the script uses the union of clipped image rectangles rather than
only the largest image; overlapping rectangles are not double counted.

**Formula/figure/table boundary: every page of every file remains uncertified
for these objects.** The receipt's `raster_image_pdf_ranges` identifies image
placement, not whether an image is a plot, formula, table, cover or scan.
Vector diagrams and equations may occur outside those ranges. A large text
count cannot verify subscripts, Greek letters, signs, matrix elements, axes,
units, captions or table row alignment. OCR must preserve that boundary until
the relevant rendered object is checked with its locator. No OCR was executed
and no page was marked “read” in this inventory.

## Evidence Matrix

The refreshed source search finds 22 source pages with an exact corpus path
or matching raw hash. Twenty-one PDFs have an exact `raw_file` source card; B18
matches an existing source by SHA-256 through its duplicate in `raw/papers/`.
All 22 matched hash claims agree with the measured bytes. At the initial
snapshot, B25 had only a conceptual mention in the combined Bohr-Mottelson
card. During this task, the parent task created a separate Vol. II source;
the refreshed inventory matches it. Eleven PDFs still have no path/hash-matched
source page. An identity gap is not proof that nobody ever read the file.

The JSON lists source-card headings and all literal source/raw-path reference
candidates in `knowledge/`, with file hashes and line numbers. Its search
deliberately does not infer that a title mention proves reading, resolve every
possible spelling alias, or equate a preprint with a published chapter. The
manual version crosswalk below supplements that conservative machine map.

| Record verified in this audit | Actual evidence and scope | Credit boundary |
|---|---|---|
| [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] (B18) | Source `Scope and Reading Depth` records a staged review of printed 463-514; F01-1 through F01-15 have locators and an existing user-review record. Both local PDF copies have SHA-256 `d43c7290cf5899ebc9b94324af5e95eb40e488bacf1c70c89e0b3bd61d916172` and 52 pages. | Preserve the historical record. This audit did not reread all 52 pages or re-certify all reviewed claims. A source-level review record is not the completion of a new book curriculum. |
| Same source, dated Day17 section and F01-D17-1 | The existing reading-scope receipt explicitly records PDF 6-11 / printed 468-473, Eqs. 8-49, Table I and Figs. 5-8; its hash agrees. The cited exercise contract/result files exist. Selected source anchors were checked again in the actual corpus PDF. | Verified bounded prior reading record; task derivations remain conditional and are not experiments. No credit for the unrecorded remainder follows. |
| Same source, Day23/Day24 preview and Day26 sections | Explicit existing scopes PDF 12-14 / printed 474-476 and PDF 26-28 / printed 488-490, with atomic claim IDs, source versus task distinctions and limitations. Actual text anchors at these pages were checked; PDF 14 and 27 were also rendered for visual audit. | Targeted record, not a fresh full review. Day24 preview explicitly carries no course credit. |
| [[frauendorf-2024-wobbling-review]] related to B02 chapter 2 | A separate 26-page arXiv v1 exists at `raw/papers/2024_Frauendorf_Wobbling motion in triaxial nuclei.pdf`; measured SHA-256 `c2b08136af03b4544de7fbfe5ea3d6677d1704e8c6e13772cb2f934da554a6ea` agrees. Source scope names selected sections, Fig. 46 and conclusions; later entries specify PDF 14, 20-22 and 24-26. | Useful existing reading of that preprint. B02's author/title bookmark identifies a related 38-page published chapter at PDF 43-80. Preprint-to-book equation, figure and section alignment remains open; no published-chapter completion is assigned. |
| [[sheikh-jehangir-bhat-2024-tpsm-wobbling]] related to B02 chapter 12 | The source explicitly identifies chapter 12 / DOI suffix `-12`, and a local 25-page arXiv v1 with measured SHA-256 `a7fa3cc75113a1ff2881cbc7edd9d3285a228b429c34b6f0b9b22da4c2b90d22`. Its scope records methods, Table 1, normal-deformed cases, Figs. 11-14 and explicit exclusions. | Verified bounded preprint reading record. B02's PDF 256-274 is a differently paginated published chapter. Lu/Ta coverage and full version alignment cannot be inferred from the normal-deformed subset. |
| Parent's corrected [[book-petrache-chirality-and-wobbling]] | Current source is `skimmed`, explicitly records PDF 43-47, 56-57, 118-123, 244-246, selected image checks, and chapter-12 PDF 258-259. Its chapter map names all 17 chapters and distinguishes navigation from selected reading. | Preserve this bounded new reading record; this inventory did not perform the parent's derivations or certify whole chapters. |
| Parent's [[book-bohr-mottelson-nuclear-structure]] and new [[book-bohr-mottelson-nuclear-structure-vol2]] | Vol. I source is now `skimmed` with copyright/prefaces PDF 7-13; separate Vol. II has the measured hash `46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a`, `skimmed` and selected section 4-5e, PDF 212-214 / printed 190-192. | Identity separation repairs the initial file-mapping gap. The source explicitly leaves later E2 formulas, examples, appendices and the rest of Vol. II unread. No whole-volume credit follows. |
| Initial twenty `book-*` cards | The initial snapshot had matching paths/hashes and `deep-read` labels but chapter synopses without adequate full-study accounting. Parent corrections to Petrache and Bohr-Mottelson were observed and are recorded separately here. | These historical labels are not reading proof. Current source wording is read at its own stated scope; a source rewrite by either agent is not itself a new receipt for all chapters. |

The Day17 scope/result records are
`outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/frauendorf2001-e2-reading-scope.json`
and `frauendorf2001-e2-exercise-result.json` in the same directory. They provide
provenance for the knowledge source, not a second scientific authority.
No independent experiment is created by a book repeating the same paper or
by a preprint and chapter sharing a model calculation.

## Locator gaps actually checked

These are structural crosschecks of the **initial historical card snapshot**
against the local book, not endorsements of the scientific claims in those
summaries or assertions that corrected current cards still contain the old
text. Line numbers in this table refer to that initial snapshot. Parent edits
are independent concurrent work; this task does not overwrite or supersede
their sources. Embedded bookmarks establish navigation only; chapter study
remains open.

| Book / existing source locator | Local original locator checked | Finding |
|---|---|---|
| B01 [[book-heyde-nuclear-physics-concepts]], heading at line 38: chapters 8-9, pp. 235-340 as collective/deformation | PDF bookmarks: ch. 8 at 285, ch. 9 at 294, ch. 13 at 430 and ch. 14 at 486 | Collective modes and deformation map to chapters 13-14, not 8-9. The old span is not a valid chapter-completion record. |
| B03 [[book-behnke-data-analysis-hep]], line 36: chapters 3-4 as profile likelihood/systematics | Render-independent native TOC PDF 7-11 | Ch. 3 is hypothesis testing, ch. 4 interval estimation; systematics has its own ch. 8, printed 263 onward. Re-map individual methods rather than retain a blanket heading. |
| B04 [[book-suhonen-from-nucleons-to-nucleus]], line 42: chapters 6-7 as electromagnetic transitions | Native TOC PDF 10-11 | Ch. 6 is electromagnetic moments/transitions; ch. 7 is beta decay. Chapters 1-4 also include mean field and occupation-number representation, beyond angular-momentum algebra alone. |
| B05 [[book-iaea-reaction-data-handbook]], line 35: ch. 5 level densities | Bookmarks PDF 60 and 98 | Ch. 5 is optical-model parameters; level densities is ch. 6, PDF 98-129. The claimed pp. 67-104 mixes navigation regions. |
| B06 [[book-bertulani-nuclear-reactions]], line 36: ch. 6 compound nucleus | Bookmarks PDF 120, 172, 214 | Compound nucleus is ch. 4 (PDF 120-171); ch. 5 is fusion/fission, ch. 6 direct reactions. |
| B10 [[book-greiner-nuclear-models]], line 38: chapters 5-6 as asymmetric rotor | Rendered TOC PDF 14-16 | Ch. 5 concerns electromagnetic moments/transitions; ch. 6 collective models contains the asymmetric-rotor material. There is no native text layer to substantiate an extracted full read. |
| B19 [[book-bonamente-statistics-scientific-data]], line 36: ch. 8 nonlinear fitting/bootstrap | Bookmarks PDF 151, 228 | Ch. 8 concerns average values; Gaussian linear/nonlinear regression is ch. 11. The chapter-8 attribution is not a verified locator. |
| B22 [[book-jain-nuclear-isomers]], line 42: ch. 5 pp. 71-98 | Bookmarks ch. 5 PDF 90, ch. 6 PDF 111; native TOC | Chapter identity is correct, but the stated page span must be re-mapped to physical/printed numbering before reading credit. |
| B24/B25 historical combined card, lines 18-19 and 37-46 | Initial identity fields name only Vol. I; Vol. II native TOC PDF 9-12 lists chapters 4-6. | The initial second-volume identity gap is now repaired by the parent's separate source. Neither initial synopsis nor repaired identity demonstrates two complete volumes read. |
| B26 [[book-wu-nuclear-experiment-methods]], line 36: ch. 3 semiconductor detectors, pp. 67-112 | Rendered TOC PDF 2-3 | Ch. 3 is gas detectors (printed 69 onward); semiconductor detectors are ch. 5 (printed 135 onward). The PDF starts with eight TOC pages; source folios and physical pages must be distinguished. |
| B27 [[book-lu-nuclear-physics-chinese]], lines 36 and 47 | Rendered TOC PDF 8-9 | Gamma transitions start printed 165 and nuclear-structure models printed 190, not 147 and 177 as claimed. Ch. 9 starts printed 227; one correct anchor does not validate the other ranges. |
| B29 [[book-zhu-probability-statistics-in-physics]], line 47: ch. 10 hypothesis testing pp. 341-410 | Rendered TOC PDF 13-14 | Ch. 9 is small-sample statistics; ch. 10 concerns chi-square and goodness of fit, ch. 11 parameter-estimation fundamentals, ch. 12 parameter estimation. The claimed aggregate attribution needs a section-by-section remap. |
| B32 [[book-nakhostin-signal-processing-detectors]], lines 35, 40, 44 | Native TOC PDF 3-10 | Ch. 1 at PDF 11, ch. 4 at PDF 169 and ch. 10 at PDF 375 are usable navigation anchors. Their match establishes the TOC mapping, not complete chapter reading. |

For other cards, the verified minimum is identity plus the existence of the
recorded headings, not a comprehensive audit of all numbers or assertions.
Source-card `pages` fields are bibliographic claims; for journal papers they
can be printed page intervals. They must not replace measured PDF lengths.
B20's bookmarks are a personal, unsorted set of chapter/formula targets,
not a complete table of contents. B27's 434 bookmarks are largely page-number
labels, not 434 chapters.

The actual B02 copyright page (PDF 5) was checked directly: **first edition
2025, CRC Press**, ebook ISBN `9781032691633`, hardback `9781032691282`,
paperback `9781032691602`, DOI `10.1201/9781032691633`. The historical 2024
year, Springer attribution and ISBN `9781032483863` are not supported by this
edition. The parent source now records the actual local imprint. The 2024
Frauendorf and Sheikh preprints remain separate versions with their own hashes.

## Reusable study-completion criteria

For each queue unit, persist the following in a knowledge source or a linked
knowledge reading record. Do not upgrade to `human-reviewed` through self-audit.

1. Bind the exact raw file/hash and edition/volume/version. Give the physical
   page range and checked printed-folio crosswalk, chapter/section title,
   reading mode and explicit exclusions. Inventory IDs are sorted-path
   snapshot IDs; use raw path plus hash for durable identity if files are added.
2. Read the full assigned interval with surrounding definitions. Resolve OCR,
   encoding and parser-warning pages; inspect every scientific equation,
   table, figure, axis and caption used in the notes against the rendered
   source. Classify front matter, blank pages, references and appendices
   explicitly rather than silently dropping them.
3. Record the question, assumptions, conventions, units, core argument and
   exact source locators. Separate the source's reported measurements,
   interpretation, model calculation and the learner's reconstruction.
   Keep sign/phase, axis and normalization contracts explicit.
4. Demonstrate understanding with closed-book recall and a checked derivation
   or worked problem appropriate to the unit. Reproduce a selected source
   example when data permit; label invented inputs and model controls. Keep
   failed attempts and corrections. List unattempted exercises without
   claiming the whole exercise set was completed.
5. Test at least one relevant limit, rival interpretation or counterexample.
   For contested modes preserve competing explanations and source lineage;
   agreement with a chosen calculation is not independent experimental proof.
   For atomic or administrative documents use an appropriate identity/schema
   or exclusion rationale rather than inventing nuclear-collectivity content.
6. Write the reusable result and unresolved questions into `knowledge/`, with
   locators and a resumable next action. A chapter becomes complete only when
   all its page units and scientific objects satisfy the declared criteria
   and remaining exclusions are visible. Whole-book completion requires all
   chapters and appendices reconciled; an inventory, code suite or topic
   synthesis cannot substitute for that accounting.

Allowed unit states are `queued`, `access-triage`, `reading-partial`,
`source-checked`, and `study-complete`. Keep `record-verified` separate: it
means a prior record and its bounded identity/locator were checked, not that
all study criteria have now passed. An editorial page may close as
`administrative-classified`; it never earns scientific chapter credit.

## Synthesis

The useful next step is a complete page-accounted reading program anchored by
the checked subset records, starting with S1 sources and their access gaps.
The following queue preserves the entire library denominator.

### Bibliographic notes on unmapped and composite entries

These entries currently have no source page bound to their exact path or hash:

- **B07**: Leonid Shifrin, *Mathematica® Programming: An Advanced Introduction*,
  Part I: The Core Language, Version 1.01 (2008), 408 physical pages. An advanced
  text on the symbolic, functional and rule-based architecture of the language;
  queue as symbolic foundations, distinct from cookbook recipes.
- **B08**: Sal Mangano, *Mathematica Cookbook*, O’Reilly Media (2010), ISBN
  `9780596520991`, 827 physical pages. Problem-solution reference across 19
  chapters and appendix.
- **B11, B15, B16, B17**: Four separate research articles from *Atomic Data and
  Nuclear Data Tables* 125 (2019): B11 on Bi IV oscillator strengths and core
  polarization; B15 on radiative rates in Ne-like Hf LXIII, Ta LXIV, Re LXVI;
  B16 on Ne-like Cu XX, Zn XXI, Ga XXII; B17 on W33+ level energies. They share
  a volume with B13 and B14 but are separate files and discrete topics; do not
  collapse them or confound atomic calculations with nuclear collectivity.
- **B12**: *Atomic Data and Nuclear Data Tables* 125 (2019) editorial board page,
  1 physical page. Preserved in the denominator as an administrative file; no
  scientific credit is assigned.
- **B21**: Angela Gargano, Giovanni De Gregorio, Silvia M. Lenzi (eds.), *The
  Nuclear Shell Model 70 Years after Its Advent: Achievements and Prospects*,
  MDPI reprint book (2023), ISBN `9783036577883` / `9783036577890`, 334 physical
  pages. Eleven reprinted research and review papers (including Talmi, Stuchbery
  & Wood, Otsuka, Brown, Horoi, Martínez-Pinedo & Langanke); build a separate
  per-paper crosswalk before assigning reading credit.
- **B28**: 同济大学数学系《高等数学》（第七版下册），高等教育出版社（2014），
  ISBN `9787040396621`，367 页。经典工科微积分与空间解析几何教材，含第八至
  十二章及习题解答。
- **B30**: 鞠国兴《朗道〈力学〉解读》，高等教育出版社（2019），ISBN
  `9787040524451`，400 页。配合同济高数和朗道原著，重点解析守恒律、微振动、
  刚体转动欧拉角与哈密顿正则方程。
- **B31**: 汪晓莲、李澄、邵明、陈宏芳《粒子探测技术》，中国科学技术大学出版社
  （2009），ISBN `9787312022715`，444 页。已有概念页多处引用该书与吴治华实验方法
  的比较，但全书 11 章（气体、闪烁体、半导体、位置灵敏探测器及读出电子学）尚未建立
  逐章完成台账；本次完成全书页码与无文本层扫描状态登记。

Every physical page appears in exactly one 40-page interval per PDF below
(the last interval is shorter). Unit IDs are `Q-Bnn-001`, `Q-Bnn-002`, etc.,
in the displayed order. These are access/study work packets, not claims about
chapter boundaries. Split or merge them along verified sections while
preserving a complete page partition. All packets currently remain `queued`;
bounded historical records guide rereading without certifying the packet.

Priorities are study scheduling, unrelated to governance P0/P1: **S1** nuclear
structure, spectroscopy, reactions and statistics; **S2** wider nuclear
physics, mathematical foundations and detector breadth; **S3** Mathematica
programming; **S4** peripheral atomic papers and administrative classification.
S3/S4 remain in the denominator and queue. Do not omit them to improve a
completion percentage. B21 is a collection of papers: build an article-level
crosswalk before assigning chapter credit, and do not count reprints as
independent experiments.

For each file below, `OCR` names the exact automatic OCR/transcription route.
`zero` and `sparse` identify native-text triage ranges separately. Formula,
figure and table verification remains open over **PDF 1-N for every entry**,
including pages absent from the OCR list. The JSON retains complete raster
and warning ranges and the page-by-page numerical measurements.

## B01: Heyde: Basic Ideas and Concepts in Nuclear Physics

- Priority: **S1**. Physical pages: **647**. Bookmarks: **22**.
- Raw: `raw/books/Basic Ideas and Concepts in Nuclear Physics An Introductory Approach (Kris L.G. Heyde) (Z-Library).pdf`
- SHA-256: `0490c8036be9cd8702cd8aec9c858ebb0e898e6c7b2b1056ce36e205f9f3c18a`
- Source identity: [[book-heyde-nuclear-physics-concepts]]
- Record/gap: Historical chapter 8-9 synopsis has a locator mismatch; no complete-chapter receipt verified. Establish full 17-chapter map and study collective chapters 13-14 in context.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: 3, 25, 80-81, 112-113, 121, 221-223, 226-227, 330.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-647**.
- Complete page queue, `Q-B01-001` through `Q-B01-017`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-560, 561-600, 601-640, 641-647**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 25: Chapter 1 Nuclear global properties
- PDF 90: Chapter 2 General nuclear radioactive decay properties and transmutations
- PDF 121: Chapter 3 General methods
- PDF 128: Chapter 4 Alpha-decay
- PDF 152: Chapter 5 Beta-decay
- PDF 228: Chapter 6 Gamma decay
- PDF 259: Chapter 7 The liquid drop model approach
- PDF 285: Chapter 8 The simplest independent particle model
- PDF 294: Chapter 9 The nuclear shell model
- PDF 338: Chapter 10 The nuclear mean-field
- PDF 362: Chapter 11 The nuclear shell model
- PDF 417: Chapter 12 Nuclear physics of very light nuclei
- PDF 430: Chapter 13 Collective modes of motion
- PDF 486: Chapter 14 Deformation in nuclei
- PDF 520: Chapter 15 Nuclear physics at the extremes of stability
- PDF 573: Chapter 16 Deep inside the nucleus
- PDF 603: Chapter 17 Outlook
- PDF 609: Appendix A Units and conversion between various unit systems
- PDF 618: Appendix B Spherical tensor properties
- PDF 626: Appendix C Second quantization-an introduction

## B02: Petrache (ed.): Chirality and Wobbling in Atomic Nuclei, CRC 2025

- Priority: **S1**. Physical pages: **339**. Bookmarks: **197**.
- Raw: `raw/books/Chirality and Wobbling in Atomic Nuclei.pdf`
- SHA-256: `787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2`
- Source identity: [[book-petrache-chirality-and-wobbling]]
- Record/gap: Parent now records selected published-page checks with skimmed status; related preprint records exist for chapters 2 and 12. All 17 full published chapters remain open. Check PDF 5 for edition identity.
- OCR/transcription access route (PDF): **1, 3, 7, 13, 15, 17**.
- Zero native text (PDF): 1. Sparse nonzero text: 3-4, 7, 13, 15, 17.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-339**.
- Complete page queue, `Q-B02-001` through `Q-B02-009`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-339**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 20: Chapter 1: History and future perspectives on chirality and wobbling in atomic nuclei, C. M. Petrache
- PDF 43: Chapter 2: Wobbling motion in triaxial nuclei, S. Frauendorf
- PDF 81: Chapter 3: The 25th anniversary for nuclear chirality, J. Meng, Y. P. Wang
- PDF 94: Chapter 4: Algebraic description of wobbling motion in nuclei, K. Tanabe and K. Sugawara-Tanabe
- PDF 110: Chapter 5: Recent experimental results on chirality and wobbling motion in triaxially deformed nuclei, S. Guo and B. F. Lv
- PDF 127: Chapter 6: Tilted precession and wobbling in triaxial nuclei, E. A. Lawrie
- PDF 156: Chapter 7: Experimental search for non-chiral to chiral configuration transition in 126,128Cs isotopes, E. Grodner
- PDF 167: Chapter 8: Semiclassical feature of wobbling and chiral properties in atomic nuclei, A. A. Raduta, C. M. Raduta, R. Poenaru
- PDF 204: Chapter 9: Nuclear chiral dynamics within time-dependent covariant density functional theory, P. W. Zhao
- PDF 222: Chapter 10: Study of wobbling motion within CDFT+PRM approach, Q. B. Chen, H. M. Dai, Y. Z. Ji
- PDF 239: Chapter 11: Recent developments and novel applications of the interacting boson-fermion model, K. Nomura
- PDF 256: Chapter 12: Microscopic investigation of wobbling motion in atomic nuclei using the triaxial projected shell model approach, J. A. Sheikh, S. Jehangir, G. H. Bhat
- PDF 275: Chapter 13: Spin dynamics of triaxial nuclei with quasiparticle alignments, R. Budaca
- PDF 292: Chapter 14: Recent progress on nuclear chiral and wobbling motions based on the triaxial projected shell model, Y. K. Wang
- PDF 302: Chapter 15: Studies of nuclear Chirality in A≈80 mass region, B. Qi
- PDF 311: Chapter 16: Recent progress in nuclear chirality of cesium isotopes, J. Li, D. Chen
- PDF 323: Chapter 17: Collective model for multiple chiral doublets bands and wobbling bands, Y. Zhang, H. D. Jiang, B. Qi
- PDF 338: Index

## B03: Behnke et al.: Data Analysis in High Energy Physics

- Priority: **S1**. Physical pages: **430**. Bookmarks: **0**.
- Raw: `raw/books/Data Analysis in High Energy Physics, A Practical Guide to Statistical Methods (Olaf Behnke, Kevin Kroninger, Gregory Schott etc.) (Z-Library).pdf`
- SHA-256: `18cf194b5cd4e86d8413244cf913fe5699de211a68e4a5d1164709e92fcbe84c`
- Source identity: [[book-behnke-data-analysis-hep]]
- Record/gap: Historical chapter heading conflates hypothesis tests, interval construction and systematics; no full-chapter completion verified. Read the TOC PDF 5-12 and retain parser-warning boundaries.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: 179.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): 4-5, 12, 19, 26, 46-47, 93, 95, 124, 130, 169, 171, 179, 202, 207, 242, 279, 283, 311, 313, 344, 349, 362, 371, 373, 394, 397, 423, 425.
- Formula/figure/table certification: **open over PDF 1-430**.
- Complete page queue, `Q-B03-001` through `Q-B03-011`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-430**.

## B04: Suhonen: From Nucleons to Nucleus

- Priority: **S1**. Physical pages: **654**. Bookmarks: **0**.
- Raw: `raw/books/From nucleons to nucleus concepts of microscopic .pdf`
- SHA-256: `4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c`
- Source identity: [[book-suhonen-from-nucleons-to-nucleus]]
- Record/gap: Native TOC PDF 8-16 identifies 19 chapters. Chapter 6 is electromagnetic multipoles and 7 beta decay; current historical summary is not a full-study receipt.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: 2, 4.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): 22, 44, 56, 58, 79, 89, 103, 105, 137-138, 149, 173-174, 183, 224, 233, 252, 260, 264, 273, 302-303, 305, 321, 324, 342, 399-400, 424-425, 432-433, 466-467, 484, 500, 504-505, 535, 537, 539, 572, 580, 582, 608, 610, 620, 637.
- Formula/figure/table certification: **open over PDF 1-654**.
- Complete page queue, `Q-B04-001` through `Q-B04-017`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-560, 561-600, 601-640, 641-654**.

## B05: IAEA: Handbook for Calculations of Nuclear Reaction Data

- Priority: **S1**. Physical pages: **172**. Bookmarks: **78**.
- Raw: `raw/books/Handbook for calculations of nuclear reaction data.pdf`
- SHA-256: `7db49b1250cfe8690cbc5986fec2392518faa24844c6370a6ccf47bce45a61d4`
- Source identity: [[book-iaea-reaction-data-handbook]]
- Record/gap: Historical level-density chapter number is wrong. Queue all eight numbered chapters, errata and parameter tables; preserve evaluated-input versus experiment distinctions.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): 7, 13, 17, 49, 77, 97, 129, 171. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-172**.
- Complete page queue, `Q-B05-001` through `Q-B05-005`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-172**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 14: 1 INTRODUCTION
- PDF 18: 2 ATOMIC MASSES
- PDF 24: 3 DISCRETE LEVELS
- PDF 50: 4 AVERAGE NEUTRON RESONANCEPARAMETERS
- PDF 60: 5 OPTICAL MODEL PARAMETERS
- PDF 98: 6 NUCLEAR LEVEL DENSITIES
- PDF 130: 7 GAMMA-RAY STRENGTH FUNCTIONS
- PDF 152: 8 NUCLEAR FISSION

## B06: Bertulani and Danielewicz: Introduction to Nuclear Reactions

- Priority: **S1**. Physical pages: **421**. Bookmarks: **17**.
- Raw: `raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf`
- SHA-256: `ad1391abd781e2277433283b6635679cfc45efc9d9d5472d4aabcd172509cb71`
- Source identity: [[book-bertulani-nuclear-reactions]]
- Record/gap: Historical compound-nucleus chapter number is wrong. Queue all nine chapters; reaction and structure inferences require explicit channel and approximation contracts.
- OCR/transcription access route (PDF): **1**.
- Zero native text (PDF): 1, 3, 7, 9, 11, 79, 119, 265, 383. Sparse nonzero text: 2, 4, 6.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-421**.
- Complete page queue, `Q-B06-001` through `Q-B06-011`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-421**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 12: 1. Classical and quantum scattering
- PDF 42: 2. The partial-wave expansion method
- PDF 80: 3. Formal scattering theory
- PDF 120: 4. Compound nucleus reactions
- PDF 172: 5. Fusion and fission
- PDF 214: 6. Direct reactions
- PDF 266: 7. Nuclear reactions in the cosmos
- PDF 334: 8. High-energy collisions
- PDF 384: 9. Relativistic collisions
- PDF 419: Index

## B07: MathProgrammingIntro: Mathematica programming introduction

- Priority: **S3**. Physical pages: **408**. Bookmarks: **0**.
- Raw: `raw/books/MathProgrammingIntro.pdf`
- SHA-256: `43c24ec835b7ad38ee7a4c4a4263f1afc6d6b2812ed764a734980525db8db107`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: No path/hash-bound source or verifiable reading record found. Title-page identity and full chapter boundaries must be registered before study; symbolic programming remains in the full queue.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: 1, 3.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): 26, 35.
- Formula/figure/table certification: **open over PDF 1-408**.
- Complete page queue, `Q-B07-001` through `Q-B07-011`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-408**.

## B08: Mathematica Cookbook

- Priority: **S3**. Physical pages: **827**. Bookmarks: **1168**.
- Raw: `raw/books/Mathematica Cookbook.pdf`
- SHA-256: `e0db550c74888adf211725140f3c8549cdfc85aff79f279b1eeb1eb00de2a37d`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: No path/hash-bound source or verifiable reading record found. The 1,168 bookmarks include recipes and subtopics, not 1,168 completed chapters; cover all sections and appendices at lower priority.
- OCR/transcription access route (PDF): **1-2**.
- Zero native text (PDF): 1-2, 16, 110, 170, 262, 300, 354, 398, 574, 618, 666, 744, 802. Sparse nonzero text: 3, 5, 7-8, 10, 13-14, 555, 673.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-827**.
- Complete page queue, `Q-B08-001` through `Q-B08-021`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-560, 561-600, 601-640, 641-680, 681-720, 721-760, 761-800, 801-827**.

## B09: Motivations for Early High-Profile FRIB Experiments

- Priority: **S2**. Physical pages: **230**. Bookmarks: **77**.
- Raw: `raw/books/Motivations for Early High-Profle FRIB Experiments.pdf`
- SHA-256: `d1b6bba7bd97cbc2c256fc32c39be399cb11f1b5579e111f6bf43acf93457282`
- Source identity: [[book-frib-motivations-experiments]]
- Record/gap: Existing source is a historical report synopsis, not verified whole-report study. Queue every scientific case, method section and references without treating a proposal as an observation.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: 3.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-230**.
- Complete page queue, `Q-B09-001` through `Q-B09-006`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-230**.

## B10: Greiner and Maruhn: Nuclear Models

- Priority: **S1**. Physical pages: **399**. Bookmarks: **0**.
- Raw: `raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf`
- SHA-256: `db5e43efaa80877822540bf0caae9be93d54d5499c5df89faae69769e6f77091`
- Source identity: [[book-greiner-nuclear-models]]
- Record/gap: Entire file has no native text. Rendered TOC PDF 14-16 contradicts the old combined chapter title. Recover chapter/section map and checked OCR/transcription before full study.
- OCR/transcription access route (PDF): **1-399**.
- Zero native text (PDF): 1-399. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-399**.
- Complete page queue, `Q-B10-001` through `Q-B10-010`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-399**.

## B11: ADNDT: Core-polarization effects / oscillator strengths

- Priority: **S4**. Physical pages: **10**. Bookmarks: **15**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Core-polarization-effects--Oscillator-strengths--trans_2019_Atomic-Data-and-.pdf`
- SHA-256: `7f7ef3786c8b618414e2bdd84ea009a5192906fb8f26e6ac927668e70ff45644`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: Peripheral atomic-data article, not a nuclear-structure monograph; no path/hash-bound source or reading receipt found. Classify target ions, calculated observables and reusable data conventions, and cover all ten pages.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-10**.
- Complete page queue, `Q-B11-001` through `Q-B11-001`, all `queued`: **1-10**.

## B12: ADNDT: Editorial Board

- Priority: **S4**. Physical pages: **1**. Bookmarks: **0**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Editorial-Board_2019_Atomic-Data-and-Nuclear-Data-Tables.pdf`
- SHA-256: `d7c2a050d2f452893f5456050b92252b24df140b39c2b4a25d8403ae9381602b`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: Administrative one-page PDF. Classify explicitly in the corpus; no chapter or scientific reading credit. It remains in the inventory denominator.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-1**.
- Complete page queue, `Q-B12-001` through `Q-B12-001`, all `queued`: **1**.

## B13: Xiong and Wang: Nuclear Chiral Doublet Bands Data Tables

- Priority: **S1**. Physical pages: **33**. Bookmarks: **16**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Nuclear-chiral-doublet-bands-data-tabl_2019_Atomic-Data-and-Nuclear-Data-Tab.pdf`
- SHA-256: `39d0808ec9b2583e16ec2417264a12bb4a1fb3c7d30558f787ae28e04caaaf4e`
- Source identity: [[book-xiong-wang-2019-chiral-tables]]
- Record/gap: Existing compilation source has no verified table-by-table completion record. Queue the introduction, explanation of tables, every table and references; trace candidates back to original experiments.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-33**.
- Complete page queue, `Q-B13-001` through `Q-B13-001`, all `queued`: **1-33**.

## B14: Moller et al.: Nuclear Properties for Astrophysical and Radioactive-Ion-Beam Applications

- Priority: **S1**. Physical pages: **192**. Bookmarks: **31**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Nuclear-properties-for-astrophysical-and-radioact_2019_Atomic-Data-and-Nucle.pdf`
- SHA-256: `b751c8054d52975be92b0e4857351226c38059f1e3e4766a1b15c084132f6dbb`
- Source identity: [[book-moller-2019-frdm-nuclear-properties]]
- Record/gap: Existing source lists specific shape values without a demonstrated row/column audit here. Queue model description and every data-table segment; verify column identities and treat predictions as model results.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-192**.
- Complete page queue, `Q-B14-001` through `Q-B14-005`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-192**.

## B15: ADNDT: Radiative rates, E1/E2/M1/M2 (filename with transitions-_)

- Priority: **S4**. Physical pages: **26**. Bookmarks: **15**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Radiative-rates-for-E1--E2--M1--and-M2-transitions-_2019_Atomic-Data-and-Nuc.pdf`
- SHA-256: `cd6034ab922983c13ad56bcae9d35e07be145fc91b25baba5b07908c7d816433`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: Distinct hash and 26 pages: do not merge with B16 on filename similarity. No path/hash-bound source/reading record found; queue atomic transition tables and their uncertainty/selection rules.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-26**.
- Complete page queue, `Q-B15-001` through `Q-B15-001`, all `queued`: **1-26**.

## B16: ADNDT: Radiative rates, E1/E2/M1/M2 (filename with transitions_)

- Priority: **S4**. Physical pages: **35**. Bookmarks: **16**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Radiative-rates-for-E1--E2--M1--and-M2-transitions_2019_Atomic-Data-and-Nucl.pdf`
- SHA-256: `eef7c5968bad8d16b37cfae2db8c76a96c0e6ae6e53f1522f928d10ee94ee97e`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: Distinct hash and 35 pages: do not merge with B15. No path/hash-bound source/reading record found; establish the actual ion/configuration identity and table coverage.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-35**.
- Complete page queue, `Q-B16-001` through `Q-B16-001`, all `queued`: **1-35**.

## B17: ADNDT: Theoretical level energies and transition data for 4p configurations

- Priority: **S4**. Physical pages: **26**. Bookmarks: **10**.
- Raw: `raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Theoretical-level-energies-and-transition-data-for-4p_2019_Atomic-Data-and-N.pdf`
- SHA-256: `344ae821c61c505ef5b5b53e779e293ef4aaa73c459839e466f17bab17c1f66c`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: Peripheral atomic-data article. No path/hash-bound source/reading record found; inspect every page, classify transferable numerical/table conventions and record limits of relevance.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-26**.
- Complete page queue, `Q-B17-001` through `Q-B17-001`, all `queued`: **1-26**.

## B18: Frauendorf: Spontaneous Symmetry Breaking in Rotating Nuclei

- Priority: **S1**. Physical pages: **52**. Bookmarks: **0**.
- Raw: `raw/books/Spontaneous symmetry breaking in rotating nuclei_Frauendorf.pdf`
- SHA-256: `d43c7290cf5899ebc9b94324af5e95eb40e488bacf1c70c89e0b3bd61d916172`
- Source identity: [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- Record/gap: Byte-identical to the source-bound raw/papers copy. Verified bounded prior records include PDF 6-11, 12-14 and 26-28. Preserve the historical staged full-review record without claiming a fresh 52-page reread or book-course completion.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-52**.
- Complete page queue, `Q-B18-001` through `Q-B18-002`, all `queued`: **1-40, 41-52**.

## B19: Bonamente: Statistics and Analysis of Scientific Data, third edition

- Priority: **S1**. Physical pages: **491**. Bookmarks: **242**.
- Raw: `raw/books/Statistics and Analysis of Scientific Data (Graduate Texts in Physics), 3rd Edition (Massimiliano Bonamente) (Z-Library).pdf`
- SHA-256: `e5197dffd54d527b9d6925b92eeae34e0859e0062063861f2e54abf333d2b2ca`
- Source identity: [[book-bonamente-statistics-scientific-data]]
- Record/gap: Historical nonlinear/bootstrap chapter-8 attribution fails the TOC check. Queue all 22 chapters, examples, problems, references and index with explicit statistics assumptions.
- OCR/transcription access route (PDF): **1**.
- Zero native text (PDF): none. Sparse nonzero text: 1, 4, 6, 23, 163, 357.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-491**.
- Complete page queue, `Q-B19-001` through `Q-B19-013`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-491**.

## B20: Hamilton (ed.): The Electromagnetic Interaction in Nuclear Spectroscopy

- Priority: **S1**. Physical pages: **956**. Bookmarks: **29**.
- Raw: `raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf`
- SHA-256: `93b32a8debb66ad036229d860ad56f0434dc49b56edd32f1628af1d71a21ae00`
- Source identity: [[book-hamilton-electromagnetic-interaction]]
- Record/gap: 953 pages have no native text; only PDF 532, 559, 727 have native text. Existing personal bookmarks are incomplete and unsorted. Recover the full TOC and chapter authors, and verify phase/normalization conventions directly.
- OCR/transcription access route (PDF): **1-531, 533-558, 560-726, 728-956**.
- Zero native text (PDF): 1-531, 533-558, 560-726, 728-956. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-956**.
- Complete page queue, `Q-B20-001` through `Q-B20-024`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-560, 561-600, 601-640, 641-680, 681-720, 721-760, 761-800, 801-840, 841-880, 881-920, 921-956**.

## B21: The Nuclear Shell Model 70 Years after Its Advent: Achievements and Prospects

- Priority: **S2**. Physical pages: **334**. Bookmarks: **0**.
- Raw: `raw/books/The Nuclear Shell Model 70 Years after Its Advent Achievements and Prospects_Gargano, Gregorio, Lenzi.pdf`
- SHA-256: `1b2418417419c343d2a35684a7d3dc7136ad0bc340d609eecbd028830b55eec1`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: A multi-article reprint collection; no whole-volume path/hash-bound source or reading receipt found. Native contents PDF 5-6 provides article starts; create an article/DOI/version crosswalk before awarding any per-article completion.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): 3, 9, 11, 97, 149, 171, 185, 203, 221, 233, 253, 271, 301, 317, 331, 333. Sparse nonzero text: 2, 334.
- Text-on-scan quality review (PDF): 1.
- Parser-warning pages (PDF): 30, 227, 320.
- Formula/figure/table certification: **open over PDF 1-334**.
- Complete page queue, `Q-B21-001` through `Q-B21-009`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-334**.

## B22: Jain et al.: Nuclear Isomers, A Primer

- Priority: **S1**. Physical pages: **151**. Bookmarks: **109**.
- Raw: `raw/books/nuclear isomer - A Prime.pdf`
- SHA-256: `20f88b84240637e10a6086eca6b9f6e80a28813ad1ecf14a795144a4d5c2ac34`
- Source identity: [[book-jain-nuclear-isomers]]
- Record/gap: Existing K-isomer synopsis has an unverified page span. Queue all eight chapters plus appendix; separate mechanism categories from evidence for any particular nuclide.
- OCR/transcription access route (PDF): **1**.
- Zero native text (PDF): none. Sparse nonzero text: 1-3, 5.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): 16, 51, 63, 91, 121, 139.
- Formula/figure/table certification: **open over PDF 1-151**.
- Complete page queue, `Q-B22-001` through `Q-B22-004`, all `queued`: **1-40, 41-80, 81-120, 121-151**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 13: 1 An Overview of Nuclear Isomers
- PDF 29: 2 Spin Isomers
- PDF 46: 3 Seniority Isomers
- PDF 62: 4 Generalized Seniority Isomers
- PDF 90: 5 K-Isomers in Deformed Nuclei
- PDF 111: 6 Shape and Fission Isomers
- PDF 126: 7 Unusual Isomers
- PDF 139: 8 Experimental Methods, Applications, Future Prospects
- PDF 150: Appendix  Summary

## B23: Raduta: Nuclear Structure with Coherent States

- Priority: **S1**. Physical pages: **524**. Bookmarks: **157**.
- Raw: `raw/books/nuclear structure with coherent states_Raduta.pdf`
- SHA-256: `98b057e53e323b0f4781060ad5ae4a8c045ac36b32c0650033953360d951aca3`
- Source identity: [[book-raduta-coherent-states]]
- Record/gap: Existing chapters 4/6 summary is not a complete-chapter receipt. Queue all fifteen chapters, appendices and bibliography; verify projection, semiclassical limits and source-defined notation.
- OCR/transcription access route (PDF): **2**.
- Zero native text (PDF): none. Sparse nonzero text: 2-4.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): 18, 52, 100, 137, 186, 243, 262, 285, 299, 342, 353, 368, 413, 475, 477.
- Formula/figure/table certification: **open over PDF 1-524**.
- Complete page queue, `Q-B23-001` through `Q-B23-014`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-524**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 13: 1 Introduction
- PDF 17: 2 Classical Versus Quantal Features  in a Projected Coherent State
- PDF 50: 3 Compact Formulas for Ground Band Energies
- PDF 82: 4 Description of the Triaxial Rotor
- PDF 137: 5 Semiclassical Description of Many Body Systems
- PDF 186: 6 The Coherent State Model
- PDF 243: 7 Pear Shaped Nuclei
- PDF 262: 8 Coupling of One, Two and Three Quasiparticles to a CSM Core
- PDF 284: 9 The Generalized Coherent State Model
- PDF 298: 10 Two Applications of GCSM
- PDF 342: 11 Boson States Basis
- PDF 353: 12 Unified Single Particle Basis
- PDF 368: 13 Boson Hamiltonians
- PDF 412: 14 Comparison of CSM with Some Other Models
- PDF 472: 15 Conclusions

## B24: Bohr and Mottelson: Nuclear Structure I

- Priority: **S1**. Physical pages: **492**. Bookmarks: **0**.
- Raw: `raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf`
- SHA-256: `a31a158e0aff2ec6734d46f5aea5eb42dbebb82280835774f49350dd6f8c79df`
- Source identity: [[book-bohr-mottelson-nuclear-structure]]
- Record/gap: Parent corrected source to skimmed with copyright/prefaces PDF 7-13. Existing text layer is largely OCR over scans. Queue all body chapters 1-3, illustrative examples and appendices; preface reading does not certify them.
- OCR/transcription access route (PDF): **1, 3-4, 13, 19-20, 156, 212, 215, 253, 327-328, 397, 467, 491**.
- Zero native text (PDF): 1, 3, 13, 19, 327, 397, 467, 491-492. Sparse nonzero text: 4, 20, 156, 212, 215, 253, 328.
- Text-on-scan quality review (PDF): 5-12, 14-18, 21-22, 24-66, 68-155, 157-211, 214, 217-225, 227-252, 254-287, 289-326, 329-396, 398-466, 468-490.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-492**.
- Complete page queue, `Q-B24-001` through `Q-B24-013`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-492**.

## B25: Bohr and Mottelson: Nuclear Structure II

- Priority: **S1**. Physical pages: **772**. Bookmarks: **0**.
- Raw: `raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf`
- SHA-256: `46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a`
- Source identity: [[book-bohr-mottelson-nuclear-structure-vol2]]
- Record/gap: New parent source separately binds the measured Vol. II hash and records PDF 212-214 / printed 190-192 only, plus front matter. Queue chapters 4-6, illustrative examples, appendices and cumulative bibliography/index; selected harmonic-limit reading is not whole-volume completion.
- OCR/transcription access route (PDF): **1, 3, 18, 22-23, 219, 233, 347, 488-490, 556, 771-772**.
- Zero native text (PDF): 1-3, 18, 22, 771-772. Sparse nonzero text: 23, 219, 233, 347, 488-490, 556.
- Text-on-scan quality review (PDF): 4-17, 19-21, 24-218, 220-232, 234-346, 348-487, 491-555, 557-770.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-772**.
- Complete page queue, `Q-B25-001` through `Q-B25-020`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-560, 561-600, 601-640, 641-680, 681-720, 721-760, 761-772**.

## B26: Wu Zhihua: Nuclear Physics Experimental Methods, third edition

- Priority: **S1**. Physical pages: **483**. Bookmarks: **0**.
- Raw: `raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf`
- SHA-256: `e23f010ff8d3b4737405235c4aba920533f44e89409ebb7e2cb076b7ab4ee591`
- Source identity: [[book-wu-nuclear-experiment-methods]]
- Record/gap: All 483 pages are scans. Actual PDF starts with TOC, not a title page. Rendered TOC shows gas detectors in ch. 3 and semiconductor detectors in ch. 5; historical source chapter mapping needs correction before study credit.
- OCR/transcription access route (PDF): **1-483**.
- Zero native text (PDF): 1-483. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-483**.
- Complete page queue, `Q-B26-001` through `Q-B26-013`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-483**.

## B27: Lu Xiting et al.: Nuclear Physics, revised edition

- Priority: **S1**. Physical pages: **439**. Bookmarks: **434**.
- Raw: `raw/books/原子核物理（修订版） (卢希庭江栋兴叶沿林) (Z-Library).pdf`
- SHA-256: `a47c26b77283b871529633dc87b6b7def412f715ed66889e373ab69100147d02`
- Source identity: [[book-lu-nuclear-physics-chinese]]
- Record/gap: All 439 pages are scans. Most bookmarks are physical-page/folio labels, not sections. Rendered TOC PDF 7-10 must supply semantic chapters; historical gamma/model page spans are wrong.
- OCR/transcription access route (PDF): **1-439**.
- Zero native text (PDF): 1-439. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-439**.
- Complete page queue, `Q-B27-001` through `Q-B27-011`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-439**.

## B28: Tongji Advanced Mathematics, seventh edition, lower volume

- Priority: **S2**. Physical pages: **367**. Bookmarks: **47**.
- Raw: `raw/books/同济大学高等数学第七版下册.pdf`
- SHA-256: `4fe09776fec91bd3d780b163758025e6fbc2ce62ec15b53ee41ccdb3a8c48bf2`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: All 367 pages are scans; no source/reading receipt found. Retain all chapters 8-12, problem solutions and end matter: vectors/geometry, multivariable calculus, multiple integrals, line/surface integrals, infinite series.
- OCR/transcription access route (PDF): **1-367**.
- Zero native text (PDF): 1-367. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-367**.
- Complete page queue, `Q-B28-001` through `Q-B28-010`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-367**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 8: 第八章 向量代数与空间解析几何
- PDF 61: 第九章 多元函数微分法及其应用
- PDF 142: 第十章 重积分
- PDF 192: 第十一章 曲线积分与曲面积分
- PDF 258: 第十二章 无穷级数

## B29: Zhu Yongsheng: Probability and Statistics in Experimental Physics

- Priority: **S1**. Physical pages: **671**. Bookmarks: **0**.
- Raw: `raw/books/实验物理中的概率和统计_朱永生著.pdf`
- SHA-256: `e97062665497c597609d58c23dfa977824c43e73d3ae8cb4ca3c0855e381894b`
- Source identity: [[book-zhu-probability-statistics-in-physics]]
- Record/gap: All 671 pages are image-only, including tiled scans. Rendered TOC PDF 10-16 is navigable but is not itself body reading. Re-map the historical chapter claims and queue all fourteen chapters and end matter.
- OCR/transcription access route (PDF): **1-671**.
- Zero native text (PDF): 1-671. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-671**.
- Complete page queue, `Q-B29-001` through `Q-B29-017`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-480, 481-520, 521-560, 561-600, 601-640, 641-671**.

## B30: Ju Guoxing: Commentary on Landau Mechanics

- Priority: **S2**. Physical pages: **400**. Bookmarks: **66**.
- Raw: `raw/books/朗道《力学》解读 (鞠国兴) (Z-Library).pdf`
- SHA-256: `4886cb7585f26f41828e75e43d542d787d9202d3e0af41ce645c88bbff4a0d30`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: No source/reading receipt found. Text layer largely sits over scans; queue all seven chapters, especially rigid-body and canonical mechanics, plus front/end matter. Do not substitute general mechanics familiarity for this edition.
- OCR/transcription access route (PDF): **1, 67**.
- Zero native text (PDF): none. Sparse nonzero text: 1, 67.
- Text-on-scan quality review (PDF): 2-66, 68-400.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-400**.
- Complete page queue, `Q-B30-001` through `Q-B30-010`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 17: 第一章 运动方程
- PDF 40: 第二章 守恒定律
- PDF 69: 第三章 运动方程的积分
- PDF 120: 第四章 质点碰撞
- PDF 152: 第五章 微振动
- PDF 237: 第六章 刚体的运动
- PDF 303: 第七章 正则方程

## B31: Wang Xiaolian et al.: Particle Detection Technology

- Priority: **S2**. Physical pages: **444**. Bookmarks: **0**.
- Raw: `raw/books/粒子探测技术 (汪晓莲  李澄  绍明  陈宏芳) (Z-Library).pdf`
- SHA-256: `250b51039f35e6a22e1311d645637d741b0f859af9d328f62c450ae9422c3cb4`
- Source identity: No exact raw-path/hash-matched source page found.
- Record/gap: All 444 pages are scans; no path/hash-bound source found. Existing Wu/Wang comparison and detector concept pages mention the book without a verifiable per-chapter receipt. Rebuild source/edition/TOC and check the alleged comparisons from the actual pages.
- OCR/transcription access route (PDF): **1-444**.
- Zero native text (PDF): 1-444. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-444**.
- Complete page queue, `Q-B31-001` through `Q-B31-012`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-440, 441-444**.

## B32: Nakhostin, translated by Wu Hongyi: Signal Processing for Radiation Detectors

- Priority: **S1**. Physical pages: **427**. Bookmarks: **0**.
- Raw: `raw/books/翻译版-SignalProcessingforRadiationDetectors.pdf`
- SHA-256: `85e38c7aeb0121faed84cb0b2d8bb03e3e9c80e65dab84c8aad3893bc1399f99`
- Source identity: [[book-nakhostin-signal-processing-detectors]]
- Record/gap: TOC PDF 3-10 gives matching selected chapter starts but no complete-chapter receipt was verified. Queue all ten chapters and references; confirm translated terminology and every discrete-filter equation against the rendered original.
- OCR/transcription access route (PDF): **none**.
- Zero native text (PDF): none. Sparse nonzero text: 1-2, 10, 70, 122, 226, 254, 298, 326, 424-426.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-427**.
- Complete page queue, `Q-B32-001` through `Q-B32-011`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-240, 241-280, 281-320, 321-360, 361-400, 401-427**.

## B33: Lin Chengjian: Heavy-Ion Nuclear Reactions

- Priority: **S1**. Physical pages: **223**. Bookmarks: **8**.
- Raw: `raw/books/重离子核反应 (林承键) (Z-Library).pdf`
- SHA-256: `792bfe7f7807623b7e1439b32eddb7320ab3ec6bf6be7e3894b436c1c9f65b2e`
- Source identity: [[book-lin-heavy-ion-reactions]]
- Record/gap: All 223 pages are scans. Bookmarks provide seven chapters; old ch. 6 page span extends into ch. 7 by the bookmark navigation. Queue all chapters, equations, figures, references and end matter.
- OCR/transcription access route (PDF): **1-223**.
- Zero native text (PDF): 1-223. Sparse nonzero text: none.
- Text-on-scan quality review (PDF): none.
- Parser-warning pages (PDF): none.
- Formula/figure/table certification: **open over PDF 1-223**.
- Complete page queue, `Q-B33-001` through `Q-B33-006`, all `queued`: **1-40, 41-80, 81-120, 121-160, 161-200, 201-223**.

Chapter/navigation targets (metadata only; no study credit):

- PDF 11: 第 1 章：概述
- PDF 28: 第 2 章：重离子相互作用势
- PDF 47: 第 3 章：弹性散射
- PDF 73: 第 4 章：准弹性散射
- PDF 104: 第 5 章：深部非弹性散射和多核子转移反应
- PDF 144: 第 6 章：熔合反应
- PDF 187: 第 7 章：裂变反应

## Counter-evidence

The blanket “full library absorbed” claim is contradicted by image-only books,
incorrect chapter locators, missing source identities and the absence of
page-accounted study receipts in the initial cards. Conversely, lack of a
whole-book receipt does not erase the explicit, hash-bound targeted records
listed in the Evidence Matrix. The parent's corrected `skimmed` records are
useful positive evidence of bounded work; this audit does not inflate or
replace their stated scopes.

## Model Dependence

The OCR route depends on a declared character threshold and geometric raster
coverage. It is an access heuristic, not a model of comprehension or a verdict
on the physics. Scientific claims and model comparisons in a later study need
their own source-level assumptions and negative controls. Neither the routing
threshold nor the 40-page packet size determines a valid physical conclusion.

## Limitations and Missing Evidence

- No full chapter was studied or newly certified by this inventory. Most
  whole-book completion evidence is missing; source-card chapter summaries
  require direct rechecking.
- An exact path/hash search cannot find every title alias or partially
  overlapping reprint. The two checked preprint-to-chapter relations are
  version crosswalk leads, not proofs of identical contents.
- Every formula, table and figure remains outside inventory certification.
  Parser-warning ranges especially require rendered inspection before reuse;
  warning-free text can still contain errors.
- Covers, blanks and decorative pages in the OCR route need explicit visual
  classification. No unattended OCR pass was run, no copyrighted body text
  is included in either durable deliverable, and no raw file was changed.
- Concurrent parent changes to source cards are expected inputs. The initial
  historical locator checks and the refreshed current identity map refer to
  different snapshots; neither agent's edits alone certify completed study.
  The final receipt pins each current matched source page by hash.

## Sources

Scientific reading evidence is grounded in the source pages linked per book
and in the Evidence Matrix, with their actual raw artifacts and bounded
locators. The copyright/TOC checks above also cite the relevant original
physical PDF pages directly. File measurements and access-routing results
come from the local artifacts themselves; the JSON is a reproducible audit
receipt, not a substitute scientific source.

Reproduce the metadata from the repository root:

```bash
python3 system/scripts/book_corpus_inventory.py --root . --jobs 4 \
  --output outputs/learning-milestones/20261102-book-corpus-inventory.json
```

`--jobs 1` gives a sequential reference run. Worker processes only inspect
PDFs; they are not agents. Output ordering is fixed and has no execution
timestamp or filesystem mtime. An unchanged rerun prints `"changed": false`.
Source-card and knowledge-reference inventories are also inputs: expected
parent edits change those sections, while unchanged raw files reproduce
identical `books` records. For byte equality of the entire receipt, freeze
the script, PDFs, versions, source cards and matched knowledge references.

The reusable work queue is complete at **318 packets / 33 PDFs / 12,076
physical pages**. This is a coverage denominator and a plan for study, not
318 completed readings.
