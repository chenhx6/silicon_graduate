---
type: source
title: "ENSDF adopted levels and transfer assignments for 133Sn"
aliases: [133Sn NuDat levels, 133Sn adopted transfer assignments]
created: 2026-09-29
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
citation_key: Khazov2011SN133
title_original: "Adopted Levels, Gammas for 133Sn"
authors: [Yu. Khazov, A. Rodionov, F. G. Kondev]
journal: Nuclear Data Sheets
year: 2011
volume: 112
pages: 855
language: en
canonical_source: "https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=133SN&unc=nds"
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/nudat-133Sn-levels.html"
raw_sha256: 5c631c0f019a3698e01ef549544738c39f3047e08baf04dbf7eaafcec117a4bb
retrieval_date: 2026-09-29
ensdf_cutoff: 2010-10-31
nuclei: [133sn]
reactions: ["132Sn(d,p)133Sn"]
experiments: [132sn-transfer]
models: [dwba]
observables: [excitation-energy, spin-parity, transfer-angular-momentum, spectroscopic-factor, neutron-separation-energy]
methods: [transfer-angular-distribution, evaluated-level-data]
tags: [sn133, n82, neutron-addition, single-particle-orbitals, ensdf]
---

# ENSDF adopted levels for `133Sn`

## Bibliographic Record

The NNDC NuDat 3 page identifies the adopted-level evaluator team (Yu. Khazov, A. Rodionov and F. G. Kondev), *Nuclear Data Sheets* **112**, 855 (2011), with literature cutoff 31-Oct-2010. Its reference `2010Jo03` resolves to Jones et al., “The magic nature of 132Sn explored through the single-particle states of 133Sn,” DOI `10.1038/nature09048`.

## Scope and Reading Depth

The adopted `133Sn` level table, XREFs, transfer-angular-momentum remarks and neutron-separation summary were read from the saved NuDat HTML page. The evaluation is a database view of the cited experiments and is not an additional experiment.

## Summary

The table assigns the `133Sn` ground state and several low-lying levels using beta decay, fission and `132Sn(d,p)` data. Transfer populates an `N=83` particle spectrum; this is the particle side of the `N=82` gap. A matching `N=81` neutron-hole spectrum is still needed to map the full single-particle spacing.

## Key Results

| ID | Adopted record | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENSDF133SN-1 | The `133Sn` ground state is `0.0 keV`, `7/2−`; its spin/parity is supported by `132Sn(d,p)` proton angular distributions and the evaluation gives `L(d,p)=3` in `2010Jo03`. | experimental-fact | contextual | NuDat 3 `133SN` adopted-level table, ground-state row | true |
| ENSDF133SN-2 | The ground state is tagged as a possible `νf7/2` particle configuration, not a measured occupation probability. | author-interpretation | contextual | NuDat 3 `133SN` ground-state comment | true |
| ENSDF133SN-3 | The `853.7(3)-keV` level is `3/2−` with `L(d,p)=1` in `2010Jo03`, supporting a `p3/2` assignment. | experimental-fact | contextual | NuDat 3 `133SN` 853.7-keV row | true |
| ENSDF133SN-4 | The `1363(31)-keV` level is tentatively `(1/2−)` and is tagged as a possible `νp1/2` configuration from `2010Jo03`. | author-interpretation | contextual | NuDat 3 `133SN` 1363-keV row | true |
| ENSDF133SN-5 | The `1560.9(5)-keV` `(9/2−)` level is tagged as a possible `νh9/2` configuration, but its XREFs are beta-decay/fission (A/B/C), not the `132Sn(d,p)` transfer XREF (D). | evidence-boundary | contextual | NuDat 3 `133SN` 1560.9-keV row and XREF column | true |
| ENSDF133SN-6 | The `2004.6(10)-keV` `(5/2−)` level is tagged as a possible `νf5/2` configuration and has a `132Sn(d,p)` XREF. | author-interpretation | contextual | NuDat 3 `133SN` 2004.6-keV row | true |
| ENSDF133SN-7 | The adopted one-neutron separation energy is `S_n=2402(4) keV`. | experimental-fact | contextual | NuDat 3 `133SN` ground-state summary, `S(n)` field | true |
| ENSDF133SN-8 | The evaluation states that `Jπ` assignments are supported by proton angular distributions in `132Sn(d,p)`, except where level comments note otherwise. | experimental-criterion | contextual | NuDat 3 `133SN` level-table comment | true |

## Competing Interpretations and Limitations

`Jπ`, `L(d,p)` and configuration confidence differ by level; a database configuration tag marked “possible” is not an independently measured spectroscopic factor. In particular the `1560.9-keV` `h9/2` candidate has no transfer XREF in the adopted table. The table cites the same `2010Jo03` dataset as the Nature article and Supplementary Information.

## Extracted Pages

- NuDat 3 adopted levels and gammas for `133Sn`: level rows, XREFs, transfer comments, `S_n` summary and reference list.

## Related Knowledge

- [[jones-2010-133sn-single-particle-transfer]]
- [[ame2020-sn132-mass-curvature]]
- [[iaea-livechart-132sn-134te-levels]]
- [[a130-shell-gap-orbital-observable]]
