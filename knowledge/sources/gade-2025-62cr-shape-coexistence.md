---
type: source
title: "Gade et al. 2025 - In-beam spectroscopy reveals competing nuclear shapes in 62Cr"
aliases: [Gade 2025 62Cr shape coexistence]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-model
reading_depth: deep-read
title_original: "In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr"
authors: [Alexandra Gade, Brenden Longfellow, Robert V. F. Janssens, Duc D. Dao, Frédéric Nowacki, Jeffrey A. Tostevin, et al.]
journal: "Nature Physics"
year: 2025
volume: 21
pages: "37-42"
doi: "10.1038/s41567-024-02680-0"
citation_key: Gade_2024
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1038/s41567-024-02680-0"
library_file: "raw/papers/gpt/high-spin-20260920/形变/2025_Gade et al_In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/2025_Gade et al_In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr.pdf"
raw_sha256: "80ada48de9df6bddc15b9de79ad6e6d77fc4a6822264d8d7ebdf23762c12203e"
nuclei: [62Cr, 64Fe]
reactions: [64Fe-two-proton-knockout-9Be]
experiments: [FRIB-GRETINA-S800]
models: [large-scale-shell-model-LNPS, discrete-nonorthogonal-shell-model]
observables: [0plus-shape-coexistence, gamma-spectrum, momentum-distribution, B(E2), shell-occupancy]
methods: [in-beam-gamma-spectroscopy, knockout-momentum-distribution]
tags: [62Cr, shape-coexistence, N40-island-inversion, FRIB, GRETINA]
---

# In-beam spectroscopy reveals competing nuclear shapes in 62Cr

## Bibliographic Record

- A. Gade *et al.*, *Nature Physics* **21**, 37–42 (2025), DOI `10.1038/s41567-024-02680-0`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/2025_Gade et al_In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr.pdf`。

## Scope and Reading Depth

- PDF pp.37–42 fully read: FRIB `64Fe` two-proton knockout, S800 particle ID, GRETINA Doppler spectroscopy, γγ/multiplicity, momentum distributions, level scheme, LNPS shell-model and DNO-SM shape interpretation.
- Figure/table audit: Figs.1–4, Extended Data descriptions and shape/configuration discussion.
- Not covered: raw GRETINA event files, full LNPS/DNO-SM code and supplementary source data.

## Key Results

- An excited `0+` state in `62Cr` at about 1.38 MeV is established through a 1,016-keV decay to `2+_1`; competing 933/1,509-keV cascades assign `2+_2`, while momentum distributions constrain spins.
- `62Cr` exhibits competing shapes near the N=40 island of inversion; large-scale LNPS and DNO-SM calculations reproduce level ordering and interpret shape coexistence/axial asymmetry.
- The experiment combines particle ID, Doppler-corrected GRETINA spectra, multiplicity and two-proton knockout momentum widths; no single observable alone establishes shape coexistence.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA25-1 | A low-lying excited `0+` state in `62Cr` is established by γγ/multiplicity and decay to `2+_1`. | experimental-result | direct | PDF pp.37–40, Figs.1–2 | true |
| GA25-2 | Momentum distributions and γ cascades assign `2+_1`, `4+_1`, `6+_1`, `0+_2`, `2+_2`, `2+_3` structures. | experimental-assignment | mixed | PDF pp.38–41, Fig.3–4 | true |
| GA25-3 | LNPS shell model and DNO-SM reproduce data and interpret competing shapes/axial asymmetry. | model-result | mixed | PDF pp.39–42 | true |

## Summary

Gade *et al.* provide direct FRIB evidence for a low-lying `0+` shape-coexisting state in `62Cr`, combining γ spectroscopy, reaction kinematics and shell-model/DNO-SM interpretation near the N=40 island of inversion.

## Competing Interpretations and Limitations

Shape assignments depend on shell-model interaction, DNO-SM basis, momentum-distribution reaction assumptions and incomplete weak branches; shape coexistence requires the combined evidence chain rather than a single γ line.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GA25-AR-1 | Evidence chain | particle ID/knockout → γγ/multiplicity → level scheme/momentum J → LSSM/DNO-SM shape interpretation. | PDF Figs.1–4 | self-checking |
| GA25-AR-2 | Transfer condition | 0+ coexistence interpretation requires matched reaction/model and weak-branch sensitivity; no universal N=40 rule. | PDF pp.39–42 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[triaxial-shape-coexistence]] and [[heyde-wood-2011-shape-coexistence-review]] with a modern direct experiment outside A≈130.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `GA25-P0-1`: separate direct `0+`/γ/momentum evidence from model-derived shape labels and DNO-SM axial asymmetry.

## Extracted Pages

- Concepts: [[triaxial-shape-coexistence]], [[gamma-soft-deformation]]。
- Methods: in-beam gamma spectroscopy (source-level).
