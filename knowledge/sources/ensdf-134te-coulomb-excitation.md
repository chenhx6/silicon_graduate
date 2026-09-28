---
type: source
title: "ENSDF 134Te Coulomb-excitation subfile"
aliases: [ENSDF 134Te CoulEx, 134Te Coulomb excitation evaluation sheet]
created: 2026-09-28
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "134Te Coulomb excitation"
authors: [A. A. Sonzogni]
journal: Nuclear Data Sheets
year: 2004
volume: 103
pages: 1
language: en
canonical_source: "https://www.nndc.bnl.gov/ensnds/134/Te/coulex.pdf"
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/ensdf-134Te-coulex.pdf"
raw_sha256: 37f02b8998302844bd7e1d7816c405e1779e335b5f4a1ef5743ffd01c8e505ea
data_url: "https://www.nndc.bnl.gov/ensnds/134/Te/coulex.pdf"
data_sha256: 37f02b8998302844bd7e1d7816c405e1779e335b5f4a1ef5743ffd01c8e505ea
data_bytes: 21210
related_doi: 10.1016/S0370-2693(02)03066-6
nuclei: [134te]
reactions: [134te-12c-coulomb-excitation]
experiments: [coulomb-excitation]
models: []
observables: [b-e2, level-energy, lifetime]
methods: [evaluated-data-compilation]
tags: [ensdf, te134, n82, coulomb-excitation, b-e2]
---

# ENSDF `134Te` Coulomb-excitation subfile

## Bibliographic Record

The one-page NNDC/ENSDF Coulomb-excitation subfile was retrieved and visually checked on 2026-09-28. The payload is 21,210 bytes with SHA-256 `37f02b8998302844bd7e1d7816c405e1779e335b5f4a1ef5743ffd01c8e505ea`. It identifies A. A. Sonzogni as evaluator, *Nuclear Data Sheets* **103**, 1 (2004), literature cutoff 31-Jul-2004.

The cited primary record `2003Ba01` is bibliographically identified by Crossref and the NNDC reference route as C. J. Barton et al., “B(E2) values from low-energy Coulomb excitation at an ISOL facility: the N=80,82 Te isotopes,” *Physics Letters B* **551**(3–4), 269–276 (2003), DOI `10.1016/S0370-2693(02)03066-6`. The publisher article endpoint returned HTTP 403 in this run; the primary full text was not read.

## Scope and Reading Depth

This one-page evaluation subfile was read and visually checked in full. It covers the adopted `134Te` Coulomb-excitation record, not the full primary 2003 paper.

## Summary

The adopted `134Te` `2+` level is at `1279.11(10) keV`; the sheet attributes `B(E2)↑=0.13 4` and its derived lifetime to `2003Ba01`.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENSDF134TE-1 | The adopted `134Te` `2+` level at `1279.11(10) keV` is associated with `B(E2)↑=0.13 4` from Coulomb-excitation reference `2003Ba01`; the sheet also lists `T₁/₂=0.64(20) ps` as derived from that strength. | derived-observable | contextual | PDF p.1, `134Te Levels`, 1279.11-keV row | true |
| ENSDF134TE-2 | The `2003Ba01` reaction is `134Te(12C,12C′)` at 350 MeV. | experimental-method | contextual | PDF p.1, header paragraph under `Coulomb excitation` | true |
| ENSDF134TE-3 | The adopted level row attributes the state to `N=82` systematics and the B(E2) value to Coulomb excitation; the evaluation sheet is not the primary report. | evidence-boundary | direct | PDF p.1, 1279.11-keV level comments | true |

## Competing Interpretations and Limitations

NuDat 3 displays the same adopted level as `B(E2)(W.u.)=6.3 20` and the adopted-level comment `B(E2)=0.13 4`. These are two views of the same ENSDF evaluation, not independent measurements. The primary DOI metadata confirms identity, but the full paper could not be read from the publisher endpoint; retain the evaluated value and its locator without calling it independently verified against the article text.

## Extracted Pages

- PDF p.1: evaluator metadata, `134Te(12C,12C′)` reaction, adopted `2+` level, `B(E2)`, lifetime and reference identifier.

## Related Knowledge

- [[iaea-livechart-132sn-134te-levels]]
- [[a130-shell-gap-orbital-observable]]
