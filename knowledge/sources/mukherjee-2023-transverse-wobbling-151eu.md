---
type: source
title: "Mukherjee et al. 2023 - Evidence of transverse wobbling motion in 151Eu"
aliases: [Mukherjee 2023 151Eu transverse wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence of transverse wobbling motion in 151Eu"
authors: [A. Mukherjee, S. Bhattacharya, T. Trivedi, S. Tiwari, R. P. Singh, S. Muralithar, Yashraj, K. Katre, R. Kumar, R. Palit, S. Chakraborty, S. Jehangir, Nazira Nazir, S. P. Rouoof, G. H. Bhat, J. A. Sheikh, N. Rather, R. Raut, S. S. Ghugre, S. Ali, S. Rajbanshi, S. Nag, S. S. Tiwary, A. Sharma, S. Kumar, S. Yadav, A. K. Jain]
journal: Physical Review C
year: 2023
volume: 107
pages: 054310
doi: 10.1103/PhysRevC.107.054310
canonical_source: https://doi.org/10.1103/PhysRevC.107.054310
citation_key: mukherjee_2023_Evidencetransverse
raw_file: "raw/papers/2023_Mukherjee et al_Evidence of transverse wobbling motion in Eu 151.pdf"
raw_sha256: 3A1C99A806353E5DAF0D8B29FB9325ECAE47624BC46C5F98A3B502451091F8B0
nuclei: [151eu]
reactions: ["148Nd(7Li,4n)151Eu"]
experiments: []
models: [triaxial-projected-shell-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, transverse-wobbling, candidate, a150]
---

# Evidence of transverse wobbling motion in `151Eu`

## Bibliographic Record

PRC 107, 054310 (2023), DOI `10.1103/PhysRevC.107.054310`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, revised level scheme, DCO/polarization calibration, `δ` extraction, wobbling energy and TPSM comparison.
- Not covered: independent reproduction of TPSM and earlier lifetime measurements.
- Coverage caveats: large-`δ` solutions have broad asymmetric uncertainties; transition ratios are intensity/mixing-ratio derived rather than lifetime-based absolute strengths.

## Paper Question and Scientific Motivation

- Author-explicit motivation: resolve the roles of three negative-parity bands in `151Eu` and test for an A≈150 transverse-wobbling candidate distinct from a signature partner (PDF pp.1-3).

## Method and Design Logic

- Revise the level scheme; calibrate DCO/polarization and σ/j; extract δ for A-C and A-B links; compare E_wob and transition ratios with TPSM (PDF pp.3-10, Figs.1,5-14, Tables I-III).

## Key Evidence and Reasoning Chain

- E2-dominated A-C links versus M1-dominated A-B link → internal wobbling/signature comparator; decreasing E_wob and TPSM reproduction → transverse candidate, with broad δ/model geometry limits.

## Summary

The paper distinguishes a proposed `n_ω=1` band C from a predominantly M1 signature-partner band B. Its summary calls `151Eu` the first A≈150 transverse-wobbling “candidate,” matching the title's evidence-level wording.

## Experimental or Theoretical Setup

`148Nd(7Li,4n)151Eu` at 30 MeV with IUAC 15UD Pelletron and 16 INGA clovers plus two LEPS detectors; `5.2×10^8` γ-γ events. The target had 750 μg `148Nd` backed by 12 mg/cm² `197Au`.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU23-1 | Three new links were placed between negative-parity bands and earlier spin/parity ambiguities were revised using DCO/polarization. | experimental-fact | direct | PDF pp.3-5, Fig.1, Tables I-II | true |
| MU23-2 | Alignment calibration gives average `σ/j≈0.35`; stretched quadrupole/dipole `R_DCO` benchmarks are about 1/0.6. | experimental-criterion | direct | PDF p.4 | true |
| MU23-3 | A-C links 415.0 and 537.9 keV have large negative `δ` solutions selected by polarization and are E2 dominated. | experimental-criterion | direct | PDF pp.5-6, Figs.5-8 | true |
| MU23-4 | A-B 554.5-keV link has `δ_av≈-0.09` and is M1 dominated, supporting band B as unfavoured signature partner. | experimental-criterion | direct | PDF pp.5-6, Figs.9-10 | true |
| MU23-5 | `E_wob` for band C decreases with spin; authors use this to suggest transverse wobbling. | author-interpretation | indirect | PDF pp.6-7, Fig.11 | true |
| MU23-6 | TPSM reproduces energies and calculated transition ratios, supporting A/C wobbling and A/B signature-partner interpretations. | model-result | direct | PDF pp.8-10, Figs.13-14 | true |
| MU23-7 | Authors conclude `151Eu` is the first A≈150 transverse-wobbling candidate. | author-interpretation | indirect | PDF p.10, Summary | true |

## Nuclear Structure Information

Bands A/C form the proposed zero-/one-phonon pair; band B is the unfavored signature partner. The comparator is stronger than treating either side band alone.

## Authors' Interpretation

The authors consistently use evidence/candidate wording and acknowledge TiP and broader interpretation debates.

## Model Results

TPSM reproduces energies and ratios but does not provide the same semiclassical particle/core geometry decomposition; configuration mixing and deformation inputs remain model dependencies.

## Competing Interpretations and Limitations

The article acknowledges TiP and ongoing debates. TPSM cannot separate core and particle angular momenta as in semiclassical geometry, so transverse classification uses energy trend and transition pattern rather than a directly extracted precession cone.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MU23-AR-1 | Core reconstruction | E2-dominant A-C and M1-dominant A-B links provide an internal comparator, while broad δ uncertainty and TPSM geometry limit conclusion strength. | Key Results and Competing Interpretations above | unreviewed |
| MU23-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| MU23-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| MU23-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| MU23-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| MU23-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: E2-dominant A-C and M1-dominant A-B links provide an internal comparator, while broad δ uncertainty and TPSM geometry limit conclusion strength.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[wobbling-vs-signature-partner]] | Same nucleus contains E2-dominant candidate-wobbling and M1-dominant signature-partner links. |
| supports | [[transverse-wobbling]] | A≈150 evidence/candidate case with TPSM support. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- P0: none identified.

### P1

- `MU23-3`/`MU23-4`, Figs.5-10 — Evidence: broad asymmetric δ ranges distinguish E2-dominant A-C from M1-dominant A-B. Agent inference: the internal comparator is valuable but uncertainty-sensitive. User check: branch choice, errors and Table III ratios. Risk: overprecise wording hides fit breadth.
- `MU23-6`, Figs.13-14 — Review TPSM geometry/configuration limits and the TiP comparison before promoting the candidate beyond the source's evidence-level wording.

### P2/P3

- P2: calibration and target-detail transcription. P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[151eu]]
- Concepts: [[transverse-wobbling]], [[signature-partner-bands]]
- Methods: [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

Keep final wording at “candidate/evidence,” consistent with the paper summary.

## Day18 checkpoint054修订：横向摆动混合比解选择与偏振不对称度边界

原MU23-claims保持；旧MU23-D18-1降格为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU23-D18-1 | **superseded**：旧关于“制造了高达600倍虚假放大”的过强断言降格，由MU23-D18-8/9分层记录作者对415.0/537.9 keV大解（E2主导）的选择依据、偏振不对称度显著性（1.09sigma/1.60sigma）与反事实小根敏感性。 | task-correction | superseded-interpretation | 本段D18-8/9；旧mukherjee23-151eu-wobbling-result-024 | true |
| MU23-D18-8 | 本文Table III报告415.0 keV与537.9 keV带间跃迁混合比大解分别为delta = -3.3(+1.5/-3.3)与-6.3(+4.1/-8.8)，对应E2份额91.6%与97.5%，支持Band C为一声子横向wobbling带；线偏振不对称度测量值分别为Delta = +0.038(35)（Z = 1.09sigma）与+0.024(15)（Z = 1.60sigma），具有正偏振倾向但统计显著性有限。 | source-result-and-method | direct | PDF pp.5-6 Table III, Figs. 5-8；Sec. III | true |
| MU23-D18-9 | RDCO允许的第二组小根解（-0.12与-0.04）对应E2份额仅1.42%与0.16%，构成对混合比选择的敏感性测试；作者依据正不对称度倾向及与TPSM模型关于E_wobb随自旋下降趋势的符合，选定大解并判定为A≈150区首个横向摆动候选核。 | author-interpretation-boundary | direct-and-boundary | PDF pp.6-10 Figs. 11, 14；Sec. IV | true |
