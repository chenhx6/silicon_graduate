---
type: source
title: "Irving 1979 131Xe spectroscopy source scope and access boundary"
aliases: [Irving 1979 131Xe, 1979IR01, 131Xe gamma angular distribution polarization]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: journal-article-abstract
reading_depth: metadata-only
title_original: "The properties of low-lying levels of 129Xe and 131Xe"
authors: ["A. D. Irving", "P. D. Forsyth", "I. Hall", "D. G. E. Martin"]
year: 1979
pages: "J. Phys. G 5, 1595"
language: en
canonical_source: "https://doi.org/10.1088/0305-4616/5/11/015"
source_url: "https://doi.org/10.1088/0305-4616/5/11/015"
citation_key: irving_1979_131xe_spectroscopy
raw_file: "raw/papers/gpt/learning-daily/20261101-day29-irving-1979/crossref.json"
raw_sha256: "7c3bfb5417828b809ae6ea027efd12f75120ef0320db2e13d751db584f879158"
raw_storage_status: verified-public-metadata
nuclei: [129xe, 131xe]
reactions: [126te-alpha-n-gamma, 128te-alpha-n-gamma]
experiments: [in-beam-gamma-spectroscopy]
observables: [gamma-energy, gamma-intensity, angular-distribution, linear-polarization, mixing-ratio]
methods: [gamma-ray-spectroscopy]
tags: [131xe, source-access-boundary, angular-distribution, polarization, metadata-only]
---

# Irving 1979 `131Xe` spectroscopy source scope

## Bibliographic Record

The DOI and Crossref records identify the paper as A. D. Irving, P. D. Forsyth,
I. Hall and D. G. E. Martin, *The properties of low-lying levels of 129Xe and
131Xe*, J. Phys. G 5, 1595–1612 (1979), DOI `10.1088/0305-4616/5/11/015`.
The DOI route was reachable on 2026-11-01, but no lawful full-text PDF or
line-level table was recovered.

## Scope and Reading Depth

The public abstract was read as metadata/abstract evidence. It describes
`126,128Te(α,nγ)` measurements at 16 MeV and reports gamma energies and
intensities, angular distributions and linear polarizations, together with
level, spin, parity, mixing-ratio, `B(E2)`, `B(M1)` and branching information
for the Xe products. The abstract does not expose the `794.6-keV` row,
its conversion coefficient, or the original angular-distribution table.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| IR79-1 | The DOI record identifies the 1979 `129,131Xe` spectroscopy paper and its bibliographic identity. | source-identity | metadata | DOI landing page, title and citation block | true |
| IR79-2 | The public abstract describes `126,128Te(α,nγ)` at 16 MeV and lists gamma energies/intensities, angular distributions and linear polarizations among the reported observables. | experiment-scope | targeted-abstract | DOI landing page, abstract paragraph 1 | true |
| IR79-3 | The abstract claims Xe level, spin/parity, mixing-ratio, `B(E2)`, `B(M1)` and branching information, but does not provide the `794.6-keV` line-level AD/ICC table needed for the present parity audit. | access-and-evidence-boundary | targeted-abstract | DOI landing page, abstract paragraph 2 | true |

## Extracted Pages

- Crossref JSON: `raw/papers/gpt/learning-daily/20261101-day29-irving-1979/crossref.json`;
  title, authors, journal, volume and page range fields.
- DOI landing page: the retrieved HTML is a challenge shell rather than article
  full text; it is retained as an access record and is not used as a scientific
  data source.
- Public DOI abstract: title/scope and abstract paragraphs were read through the
  DOI record; no line-level `794.6-keV` table was exposed.

## Summary

This source closes the identity and broad observable scope of the 1979 experiment.
It does not close the `794.6-keV` line-level evidence contract. The 1979 paper
therefore remains a source-recovery target rather than a primary numerical input
for the Day29 `131Xe` design.

## Competing Interpretations and Limitations

The abstract-level scope is compatible with the possibility that the original
paper contains the needed parity-sensitive measurement, but that cannot be
inferred from the abstract alone. The 1979 experiment, the 1983 Xe band-structure
paper and later ENSDF transcription remain separate evidence layers until their
line-level source relation is recovered.

## Knowledge Impact and Learning Decision

`supports`: the historical `131Xe` source route is correctly identified and is
methodologically relevant to the planned angular-distribution/polarization audit.

`limits`: no line-level `794.6-keV` AD, polarization, conversion coefficient,
response matrix or covariance is promoted to observed data.

## Human Review

This page is a Codex self-audit and remains `unreviewed`; it does not set
`human-reviewed`.
