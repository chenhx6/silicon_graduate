---
type: source
title: "Lönnroth 1983 Xe quasiparticle states and conversion-electron scope"
aliases: [Lönnroth 1983 Xe, 1983Lo08, Xe conversion-electron spectroscopy]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: journal-article-abstract
reading_depth: metadata-only
title_original: "One- and Three-Quasiparticle States in 127,129,131,133Xe and Their Coexistence With Band Structures"
authors: ["T. Lönnroth", "J. Kumpulainen", "C. Tuokko"]
year: 1983
pages: "Physica Scripta 27, 228–240"
language: en
canonical_source: "https://doi.org/10.1088/0031-8949/27/4/002"
source_url: "https://doi.org/10.1088/0031-8949/27/4/002"
citation_key: lonnroth_1983_xe_quasiparticle_states
raw_file: "raw/papers/gpt/learning-daily/20261101-day29-lonnroth-1983/crossref.json"
raw_sha256: "0b3e378f1563b9b06c92a6b008701bca9092e0a37262ff91a742d3a96293efae"
raw_storage_status: verified-public-metadata
nuclei: [127xe, 129xe, 131xe, 133xe]
experiments: [conversion-electron-spectroscopy, in-beam-gamma-spectroscopy]
observables: [conversion-electron, spin, parity, level-energy, band-structure]
methods: [conversion-electron-spectroscopy, quasiparticle-interpretation]
tags: [131xe, source-access-boundary, conversion-electron, metadata-only]
---

# Lönnroth 1983 Xe quasiparticle-state scope

## Bibliographic Record

Crossref identifies T. Lönnroth, J. Kumpulainen and C. Tuokko,
*One- and Three-Quasiparticle States in 127,129,131,133Xe and Their Coexistence
With Band Structures*, Physica Scripta 27, 228–240 (1983), DOI
`10.1088/0031-8949/27/4/002`.

## Scope and Reading Depth

The public DOI abstract was read as metadata/abstract evidence. It describes
conversion-electron spectroscopy of Xe isotopes, including `131Xe`, and reports
the extraction of level energies and definite spin/parity assignments. It also
describes one- and three-quasiparticle configurations and their coexistence with
band structures. No full-text PDF, table, `794.6-keV` line record, conversion
coefficient uncertainty or joint response/covariance package was recovered.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LO83-1 | The DOI/Crossref record identifies the 1983 Xe quasiparticle and band-structure paper. | source-identity | metadata | DOI landing page and Crossref JSON bibliographic fields | true |
| LO83-2 | The public abstract describes conversion-electron spectroscopy for Xe isotopes including `131Xe`, with level energies and definite spin/parity assignments. | experiment-scope | targeted-abstract | DOI landing page, abstract paragraph 1 | true |
| LO83-3 | The abstract connects one- and three-quasiparticle states with band structures, but does not expose the `794.6-keV` line-level conversion or angular-distribution table. | access-and-evidence-boundary | targeted-abstract | DOI landing page, abstract paragraph 2 | true |

## Extracted Pages

- Crossref JSON: `raw/papers/gpt/learning-daily/20261101-day29-lonnroth-1983/crossref.json`;
  title, authors, journal, volume, issue and page range fields.
- Public DOI abstract: title, conversion-electron method scope and isotope coverage
  were read; line-level tables were not exposed.

## Summary

This source strengthens the historical method lineage behind the evaluated
`131Xe` spin/parity and conversion-electron records. It does not close the
present `794.6-keV` source-to-line mapping or provide the response inputs needed
for an event-level parity reanalysis.

## Competing Interpretations and Limitations

The abstract supports a conversion-electron and spin/parity method scope, but it
does not show whether the historical `794.6-keV` record came from the same
measurement, an earlier experiment, or an evaluated transcription. The
conversion-electron method therefore informs the design of a future response
closure without supplying a line-level measurement or independent acquisition
weight.

## Knowledge Impact and Learning Decision

`supports`: conversion-electron spectroscopy is a historically relevant
companion observable for the `131Xe` parity audit.

`limits`: no line-level conversion coefficient, uncertainty, angular-distribution
coefficient, response matrix or covariance is promoted to observed data.

## Human Review

This page is a Codex self-audit and remains `unreviewed`; it does not set
`human-reviewed`.
