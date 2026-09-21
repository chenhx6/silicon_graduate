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
| source | 244 |
| nucleus | 59 |
| band | 61 |
| experiment | 37 |
| concept | 48 |
| method | 21 |
| model | 15 |
| observable | 20 |
| project | 11 |
| synthesis | 11 |
| total knowledge pages | 529 |

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

Initial lint result: `errors=0`, `warnings=269`, `info=1106`. After the residual pass, the measured result is `errors=0`, `warnings=79`, `info=1106`.

## Registered residuals

### Citation keys: 76 warnings remain

The baseline contained 150 missing/empty keys. Nineteen were uniquely matched to the read-only local BibTeX exports; a further 55 were verified through DOI/title/author/year matching against Crossref records and are marked `citation_key_origin: crossref-content-negotiation`. The protected bibliography was not changed. Seventy-six remain intentionally empty because no unique local/external record is available or the arXiv version identity is unresolved. Full mapping is in `citation-key-audit.md` and `citation-key-crossref-registry.json`.

### Orphan pages: resolved by explicit provenance registry

The baseline contained 59 source pages with no inbound link outside `knowledge/index.md`. They are now intentionally linked from `[[source-provenance-coverage-map]]`, which records graph ownership without promoting claims:

1. source-only historical or method records intentionally retained for provenance;
2. recently ingested sources whose domain/project owner has not yet acquired an explicit relation;
3. older pages that need a future graph-owner decision.

The list is retained in the lint output and is not silently solved by adding meaningless links. The high-spin pages with clear scientific relations were connected during the reconciliation; the remaining source-only pages are a documented follow-up queue.

### Reaction and element warnings: 3 warnings remain

The element map and exact `p3n/2pn/1p3n` parser were expanded and regression-tested. The remaining strings (`11B(96Zr,xn)103,104Rh`, `110Pd(28Si,xnyp)`, `110Pd(28Si,xnyalpha)`) are genuinely multi-channel/underdetermined, so they remain warnings rather than being falsely balanced. The original reaction text remains authoritative.

### Raw working-tree warning

The local reading record and external PDF/manifest remain outside the public Git commit by design. Their hashes and paths are recorded in the ledger or external manifest; raw evidence is not moved or overwritten.

## Scientific status

All high-spin source-level reading rows have terminal states. Four cross-source synthesis pages and four L3 units are self-audited. No L4 run was claimed. Global pages retain their actual `review_status` and claim `needs_review` values; self-audit did not become human review.

## Decision

The whole `knowledge/` directory has been mechanically and graph-audited, with all structural errors fixed and residual warnings registered with reasons. Scientific completeness is bounded by the remaining source-level review queues, 76 unresolved citation identities, three underdetermined reaction strings and unavailable L4 inputs. The `137Ba` public-data check is recorded in `outputs/l4/137ba-double-gamma-readiness-20260921/report.md`; it remains safe-suspended, not a fabricated run.

QMD post-pass state: 532 Markdown documents indexed, 2,172 current vectors, zero pending vectors and zero retained orphan chunks after cache compaction. QMD is a retrieval cache and does not alter evidence status.
