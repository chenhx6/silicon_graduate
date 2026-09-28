---
type: source
title: "ENSDF adopted levels for 131Sn"
aliases: [131Sn NuDat levels, N=81 neutron-hole evaluation]
created: 2026-09-29
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
citation_key: Khazov2006SN131
title_original: "Adopted Levels, Gammas for 131Sn"
authors: [Yu. Khazov, I. Mitropolsky, A. Rodionov]
journal: Nuclear Data Sheets
year: 2006
volume: 107
pages: 2715
language: en
canonical_source: "https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=131SN&unc=nds"
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/nudat-131Sn-levels.html"
raw_sha256: 2e753486769f32704159ed1206c1b8e0e6e7063da02267b15b132401ea770637
retrieval_date: 2026-09-29
ensdf_cutoff: 2006-07-17
nuclei: [131sn, 132sn]
reactions: []
experiments: [131in-beta-decay, 248cm-spontaneous-fission]
models: [ensdf-evaluation]
observables: [excitation-energy, spin-parity, neutron-separation-energy]
methods: [evaluated-level-data, beta-decay-spectroscopy]
tags: [sn131, n81, neutron-hole, ensdf, shell-structure]
---

# ENSDF adopted levels for 131Sn

## Bibliographic Record

The NNDC NuDat 3 entry identifies the evaluator team Yu. Khazov, I. Mitropolsky and A. Rodionov, Nuclear Data Sheets 107, 2715 (2006), with evaluation cutoff 17-Jul-2006. The entry lists S(n)=5211(7) keV. Its XREF labels include beta decay of 131In, beta-delayed neutron decay of 132In and 248Cm spontaneous fission.

## Scope and Reading Depth

Read the adopted-level table, low-lying rows, XREF legend and level comments from the saved NuDat HTML snapshot. This is an evaluated database page, not a new experiment and not a direct reading of Orlandi et al. 2018. Its cutoff predates that paper.

## Summary

The 131Sn evaluation supplies a contextual N=81 spectrum below the 132Sn N=82 closure. It identifies a 3/2+ ground state, a low-lying 11/2− isomer whose absolute excitation energy is unresolved in the table, and positive-parity excited levels. The ground-state spin assignment is attributed to nearby odd-A Sn systematics and hyperfine/moment measurements; these rows do not provide neutron-removal spectroscopic factors.

## Key Results

| ID | Adopted record | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENSDF131SN-1 | The adopted neutron separation energy is S(n)=5211(7) keV. | evaluated-observable | contextual | NuDat 3 131SN page header, S(n) field | true |
| ENSDF131SN-2 | The 131Sn ground state is at 0.0 keV with adopted Jπ=(3/2+); its XREFs are 131In beta decays, and the evaluation cites neighboring odd-A Sn systematics plus hyperfine/moment data for the assignment. | evaluated-level | contextual | NuDat 3 131SN adopted-level table, 0.0-keV row and Jπ comment | true |
| ENSDF131SN-3 | A level at 0.0+X is assigned (11/2−); X means its absolute excitation relative to the ground state is unresolved in this entry. | evaluated-level | contextual | NuDat 3 131SN adopted-level table, 0.0+X row | true |
| ENSDF131SN-4 | The 331.73(10)-keV level is assigned (1/2+) and has the 131In beta-decay XREF B. | evaluated-level | contextual | NuDat 3 131SN adopted-level table, 331.73-keV row | true |
| ENSDF131SN-5 | The 1654.53(8)-keV level is assigned (5/2+) and has 131In beta-decay XREFs A and B. | evaluated-level | contextual | NuDat 3 131SN adopted-level table, 1654.53-keV row | true |

## Competing Interpretations and Limitations

The evaluation describes these spin assignments as consistent with systematics and moment measurements; it does not give a complete neutron-hole strength distribution in the rows cited here. In particular, the 11/2− isomer's absolute energy is unresolved. The 2006 cutoff excludes the 2018 Orlandi neutron-hole transfer paper, whose metadata identifies it as a relevant primary-source route; that paper's results are not inferred from this evaluation.

## Extracted Pages

- NuDat 3 131SN adopted-level table, low-lying levels, S(n), XREF legend and ground-state comments.

## Related Knowledge

- [[jones-2010-133sn-single-particle-transfer]]
- [[ensdf-133sn-transfer-levels]]
- [[orlandi-2018-131sn-neutron-hole-transfer]]
- [[ame2020-sn132-mass-curvature]]
- [[a130-shell-gap-orbital-observable]]
