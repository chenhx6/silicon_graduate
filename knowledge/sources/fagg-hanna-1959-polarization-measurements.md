---
type: source
title: "Fagg and Hanna 1959 - Polarization measurements on nuclear gamma rays"
aliases: [Fagg Hanna 1959 polarization]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Polarization Measurements on Nuclear Gamma Rays"
authors: [Lawrence W. Fagg, Stanley S. Hanna]
journal: "Reviews of Modern Physics"
year: 1959
citation_key: fagg_1959_Polarization
volume: 31
pages: "711-756"
doi: "10.1103/RevModPhys.31.711"
canonical_source: "Fagg & Hanna, Rev. Mod. Phys. 31, 711-756 (1959)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf"
raw_sha256: "bb3571150d4c552dc5acdbd148546acc7eea4f07dce907eaf0d82377191cb2ee"
nuclei: [generic]
reactions: [radioactive-source, nuclear-reaction, Coulomb-excitation]
experiments: [Compton-polarimetry, photodisintegration, photoelectric-polarimetry]
models: [angular-correlation, polarization-distribution]
observables: [linear-polarization, circular-polarization, parity, multipolarity]
methods: [Compton-effect, photoelectric-effect, deuteron-photodisintegration]
tags: [polarization, Compton, angular-correlation, review, parity]
---

# Polarization measurements on nuclear γ rays

## Bibliographic Record

- L. W. Fagg & S. S. Hanna, *Rev. Mod. Phys.* **31**, 711–756 (1959), DOI `10.1103/RevModPhys.31.711`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf`。

## Scope and Reading Depth

- PDF pp.711–756 (48 pages) fully read: linear/circular polarization theory, alignment versus polarization, Compton/photoelectric/deuteron processes, experimental detector methods, direction–polarization/circular correlations and tabulated historical experiments.
- Not covered: primary data behind every historical entry and later segmented-detector developments.

## Key Results

- The review separates nuclear alignment (`w(m)=w(−m)`) from polarization (`w(m)≠w(−m)`), explaining which direction/polarization/circular correlations each preparation can support (PDF pp.711–718, Table I).
- Linear polarization distributions are written as angular-correlation expansions with Legendre/associated Legendre functions; mixed multipoles enter through amplitude ratios and orientation coefficients. Polarization can resolve electric/magnetic parity ambiguity left by direction-only measurements (PDF pp.712–718, Eqs.I-1–I-14).
- Compton scattering is the primary plane-polarization analyzer; photoelectric effect, deuteron photodisintegration, pair production and nuclear photoeffect are reviewed as complementary analyzers (PDF pp.719–726).
- The experimental survey covers annihilation radiation, direction–polarization correlations, radioactive sources, nuclear reactions/Coulomb excitation, aligned nuclei, circular polarization and tabulated parity/multipolarity results (PDF pp.726–756).
- For a simple mixed transition, polarization can determine the sign of the angular-correlation term and often constrain the mixing branch, but pure dipole/pure quadrupole special cases require additional information (PDF pp.713–718, Eqs.I-8–I-11).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FH59-1 | Alignment supports linear but not circular polarization; polarization requires a directed substate population. | formalism-result | review | PDF pp.711–718, Table I | false |
| FH59-2 | Compton/photoelectric and related processes provide parity-sensitive polarization analyzers complementary to angular distributions. | method-synthesis | review | PDF pp.719–756 | true |
| FH59-3 | Polarization can resolve multipole/parity or mixing ambiguities only with orientation, convention and detector response controlled. | limitation | review | PDF pp.712–718, 726–756 | false |

## Summary

Fagg and Hanna's review is the historical bridge between nuclear orientation theory and modern Compton polarimetry. It clarifies the alignment/polarization distinction and records the detector and correlation logic underlying later CLOVER, SeGA and PDCO measurements.

## Competing Interpretations and Limitations

- Historical polarization signs depend on scattering-plane definitions, detector corrections and phase conventions; tabulated experiments are not automatically interchangeable.
- Direction–polarization correlations require known or modeled alignment and multipolarity; polarization alone does not identify a unique state sequence.
- The review's detector technology and numerical sensitivities are historical baselines, not current array calibrations.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| FH59-AR-1 | Orientation chain | Population mechanism → alignment/polarization tensor → angular distribution/correlation → linear/circular polarization. | PDF Table I, Eqs.I-1–I-14 | self-checking |
| FH59-AR-2 | Detector chain | Compton/photoelectric/deuteron analyzer → asymmetry/polarization sign → parity/multipolarity constraint. | PDF Secs.II–III | self-checking |
| FH59-AR-3 | Transfer condition | Map historical plane/sign conventions and detector response before comparing with modern `P/A/Q` values. | PDF pp.726–756 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]], [[angular-distribution]] and polarization history.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `FH59-P0-1`: Preserve historical convention and detector-response boundaries; do not import tabulated polarization signs without source-level mapping.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]]。
