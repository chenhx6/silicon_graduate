---
type: source
title: "Samanta et al. 2019 - Single particle configurations in 61Ni"
aliases: [Samanta 2019 61Ni configurations]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Single particle configurations in 61Ni"
authors: [S. Samanta, S. Das, R. Bhattacharjee, S. Chatterjee, R. Raut, S. S. Ghugre, A. K. Sinha, U. Garg, Neelam, N. Kumar, P. Jones, Md. S. R. Laskar, F. S. Babra, S. Biswas, S. Saha, P. Singh, R. Palit]
journal: "Physical Review C"
year: 2019
volume: 99
article: 014315
pages: "1-10"
doi: "10.1103/PhysRevC.99.014315"
citation_key: Samanta_2019
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.99.014315"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2019_Samanta et al_Single particle configurations in 61Ni.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2019_Samanta et al_Single particle configurations in 61Ni.pdf"
raw_sha256: "5b0575aeb4d75f13cf239cbe3293875b3c0f62507921568c0dc72749e663c9a5"
nuclei: [61Ni, 59Co]
reactions: [59Co(7Li,alpha n)61Ni]
experiments: [tifr-clover-61ni]
models: [large-basis-shell-model, fp-g-model-space]
observables: [level-scheme, RADO, RDCO, linear-polarization, gamma-branching]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [61Ni, shell-model, single-particle, g9/2, level-scheme, A≈60]
---

# Single particle configurations in 61Ni

## Bibliographic Record

- S. Samanta *et al.*, *Physical Review C* **99**, 014315 (2019), DOI `10.1103/PhysRevC.99.014315`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2019_Samanta et al_Single particle configurations in 61Ni.pdf`。

## Scope and Reading Depth

- PDF pp.1–10 fully read: TIFR `59Co(7Li,αn)` experiment, 11-clover geometry, RADO/RDCO/polarization calibration, Figs.1–10, level scheme, 17 new transitions, six re-placements, shell-model comparison and conclusions.
- Not covered: raw cubes, MARCOS/RADWARE files and complete shell-model code/input.

## Key Evidence and Reasoning Chain

- `61Ni` is extended to `Ex≈7 MeV` and spin `≈10ℏ`; 17 transitions are new and six placements are modified relative to prior work.
- RADO references are `1.24±0.02` for pure quadrupole and `0.81±0.01` for pure dipole; polarization asymmetry is corrected with energy-dependent `Q(Eγ)`, and RDCO reference values are given for the geometry.
- Large-basis `fpg` shell-model calculations include `g9/2`, enabling positive-parity/high-excitation configuration interpretation beyond earlier MSDI/ASDI work.
- Differences from Wadsworth/Meyer lineages are retained; the modern clover data improve placement and multipolarity but do not make historical discrepancies disappear without source-by-source mapping.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SA19-1 | TIFR clover spectroscopy identifies 17 new transitions and modifies six placements, extending `61Ni` to about 7 MeV and `10ℏ`. | experimental-result | direct | PDF pp.1–5, Fig.4 | true |
| SA19-2 | RADO/RDCO and linear polarization assign transition multipolarities/electromagnetic character using geometry-specific reference values. | experimental-method-result | direct | PDF pp.2–4, Figs.1–3 | true |
| SA19-3 | Large-basis `fpg` shell-model calculations including `g9/2` reproduce/interpret single-particle configurations at high excitation. | model-result | mixed | PDF pp.5–9, Figs.5–10 | true |

## Summary

Samanta *et al.* modernize the `61Ni` level scheme with high-efficiency clover coincidences and a large-basis shell-model comparison, providing a direct follow-up to Wadsworth/Meyer-era spectroscopy while preserving placement and model boundaries.

## Competing Interpretations and Limitations

Weak transitions, unresolved doublets, energy-dependent polarization sensitivity and shell-model interaction/truncation choices affect placements and configurations. Historical source differences must be reconciled line-by-line; a modern level scheme is not automatically a correction of every prior result.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SA19-AR-1 | Evidence chain | Coincidence cube/branching → RADO/RDCO/polarization → level placement → shell-model configuration. | PDF pp.2–9 | self-checking |
| SA19-AR-2 | Transfer condition | RADO/RDCO and Q values are array-specific; shell-model configurations require the stated `fpg` space/interactions. | PDF pp.2–3, 5–9 | provisional |
| SA19-AR-3 | Lineage | Compare directly with Wadsworth 1977/Meyer 1978 and later sources; do not count as same experiment. | Introduction/Discussion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` and updates the `61Ni` level/method lineage; creates an L3 reconciliation question with Wadsworth/Meyer.
- Persistence: link to [[wadsworth-1977-61ni-levels]], [[meyer-1978-multiparticle-configurations-61ni-67zn]], [[angular-distribution]], [[linear-polarization-asymmetry]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SA19-P0-1`: preserve source lineage and array-specific calibration when reconciling altered placements.

## Extracted Pages

- Nuclei: `61Ni` (source-level).
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[two-point-angular-correlation-ratio]]。
- Sources: [[wadsworth-1977-61ni-levels]], [[meyer-1978-multiparticle-configurations-61ni-67zn]]。
