---
type: metadata-audit
title: "Citation-key residual audit"
created: 2026-09-21
updated: 2026-09-21
status: completed-with-explicit-residuals
review_status: unreviewed
---

# Citation-key residual audit

## What was required

`citation_key` is a navigation/citation metadata field, not a scientific claim. It should be filled only when the identity is unique; a missing key must not be repaired by guessing a Zotero identifier.

## Measured changes

| Stage | Missing/empty source keys |
|---|---:|
| Whole-library audit baseline | 150 |
| Unique matches in the read-only local BibTeX exports | 131 after the first pass (19 restored) |
| Crossref DOI content-negotiation pass | 76 |

The Crossref pass added 55 keys whose DOI resolved to a unique record and whose title/author/year identity was checked. These keys are marked in source frontmatter with `citation_key_origin: crossref-content-negotiation` and are listed in [`citation-key-crossref-registry.json`](citation-key-crossref-registry.json). The protected `raw/zotero/wiki-inbox.bib` was not edited.

## Remaining 76

- 73 sources have no persistent identifier or no unique local/external bibliographic record (many are theses, historical scans or method notes).
- 2 sources have a real arXiv identifier but no matching local bibliography entry; their source/version identity still needs a version-specific record.
- 1 source (`jahangir-2026-tpsm-gamma-bands-nb-tc`) has an arXiv DOI whose Crossref endpoint did not return a record; it remains unmapped rather than being confused with a later publication.

The remaining paths are exactly the `CITATION_KEY_MISSING` entries emitted by the current lint report. They are not a scientific completeness queue. A later metadata pass may resolve them when the user supplies a bibliography export or a stable external record; until then, the empty field is the honest state.

## Verification rule

No page-level `review_status`, claim `needs_review`, raw file, protected BibTeX, or historical ledger event was changed by this metadata pass. External keys are explicitly distinguishable from Zotero keys, and their DOI/title provenance is reproducible from the registry.
