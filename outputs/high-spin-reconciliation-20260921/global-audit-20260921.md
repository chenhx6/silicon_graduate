---
type: research-audit
title: "Whole knowledge directory audit"
created: 2026-09-21
updated: 2026-09-21
status: complete-with-registered-residuals
review_status: unreviewed
---

# Whole knowledge directory audit

## Scope and measured baseline

The audit scanned every Markdown page under `knowledge/`, not only the high-spin source graph:

| Page type | Count |
|---|---:|
| source | 243 |
| nucleus | 59 |
| band | 61 |
| experiment | 37 |
| concept | 48 |
| method | 21 |
| model | 15 |
| observable | 20 |
| project | 10 |
| synthesis | 11 |
| total knowledge pages | 528 |

The high-spin ledger remains separately auditable at 127 rows / 118 valid / 9 excluded / 110 unique hashes.

## Checks completed

- YAML/frontmatter parse audit across all pages.
- Required field audit by page type.
- Wikilink target audit and orphan-page inventory.
- Source claim-table, locator and claim-kind audit.
- Raw source mapping and SHA-256 audit for the high-spin ledger.
- Global lint and protected-BibTeX preflight.
- QMD collection refresh and embedding status check.

The two structural frontmatter errors in `131ba-band-2.md` and `133ce-band-2.md` were fixed by quoting aliases containing square brackets. The malformed unquoted journal field in `meng-2010-open-problems-nuclear-chirality.md` was fixed. The duplicate identity warning for the two “Summary of Bases” sources was resolved by making the 1970 title version-specific.

Final lint result: `errors=0`, `warnings=269`, `info=1106`.

## Registered residuals

### Citation keys: 150 warnings

Many historical and newly created source pages lack a verified Zotero citation key. The audit records this as a metadata gap rather than inventing keys. A future metadata pass can fill a key only after title/author/year/DOI matching against the protected bibliography or a verified external record.

### Orphan pages: 59 warnings

These are source pages with no inbound link outside `knowledge/index.md`. They fall into three groups:

1. source-only historical or method records intentionally retained for provenance;
2. recently ingested sources whose domain/project owner has not yet acquired an explicit relation;
3. older pages that need a future graph-owner decision.

The list is retained in the lint output and is not silently solved by adding meaningless links. The high-spin pages with clear scientific relations were connected during the reconciliation; the remaining source-only pages are a documented follow-up queue.

### Reaction and element warnings: 45 warnings

Complex reaction strings (`xn`, spontaneous fission, mixed products) and several element symbols are outside the current lint parser/configuration. They are parser/configuration warnings, not source identity failures. The original reaction text remains authoritative in each source page.

### Raw working-tree warning

The local reading record and external PDF/manifest remain outside the public Git commit by design. Their hashes and paths are recorded in the ledger or external manifest; raw evidence is not moved or overwritten.

## Scientific status

All high-spin source-level reading rows have terminal states. Four cross-source synthesis pages and four L3 units are self-audited. No L4 run was claimed. Global pages retain their actual `review_status` and claim `needs_review` values; self-audit did not become human review.

## Decision

The whole `knowledge/` directory has been mechanically and graph-audited, with all structural errors fixed and residual warnings registered with reasons. Scientific completeness is bounded by the source-level review queues, missing citation metadata, orphan ownership decisions and unavailable L4 inputs listed above.
