---
type: source
title: "Biswas et al. 2019 - Longitudinal wobbling in 133La"
aliases: [Biswas 2019 133La longitudinal wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Longitudinal wobbling in 133La"
authors: [S. Biswas, R. Palit, S. Frauendorf, U. Garg, W. Li, G. H. Bhat, J. A. Sheikh, J. Sethi, S. Saha, Purnima Singh, D. Choudhury, J. T. Matta, A. D. Ayangeakaa, W. A. Dar, V. Singh, S. Sihotra]
journal: European Physical Journal A
year: 2019
volume: 55
pages: 159
doi: 10.1140/epja/i2019-12856-5
canonical_source: https://doi.org/10.1140/epja/i2019-12856-5
citation_key: biswas_2019_Longitudinalwobbling
raw_file: "raw/papers/2019_Biswas et al_Longitudinal wobbling in 133La.pdf"
raw_sha256: 579ECFF6DAA4CD8505C25966D15B998037930770E45382CCBA90BAE809707E03
nuclei: [133la]
reactions: ["126Te(11B,4n)133La"]
experiments: []
models: [triaxial-particle-rotor-model, tilted-axis-cranking]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [angular-distribution, dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, longitudinal-wobbling, low-spin, a130]
---

# Longitudinal wobbling in `133La`

## Bibliographic Record

EPJ A 55, 159 (2019), DOI `10.1140/epja/i2019-12856-5`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full seven-page article, INGA setup, DCO/polarization/angular distributions, mixing ratios, strength ratios, wobbling energy and QTR/HFA/TAC comparisons.
- Not covered: independent reproduction of QTR/TAC calculations.
- Coverage caveats: `σ/I=0.3` is assumed in the DCO calculation; longitudinal interpretation depends on effective moment-of-inertia evolution and an inferred aligned proton pair.

## Paper Question and Scientific Motivation

- Author-explicit motivation: identify the character of the low-spin yrast/yrare pair in `133La` and test the predicted longitudinal-wobbling regime (PDF pp.1-2).

## Method and Design Logic

- Use angular distributions, DCO and polarization to determine link mixing; calculate E_wob and relative strengths; compare QTR/HFA/TAC descriptions and infer the moment-of-inertia change from proton-pair alignment (PDF pp.2-6, Figs.1-8, Table 1).

## Key Evidence and Reasoning Chain

- E2-dominated links → wobbling-like interband character; increasing E_wob → longitudinal classification; QTR/HFA agreement plus inferred pair alignment → author microscopic mechanism. Each step adds model/analysis assumptions.

## Summary

The paper reports “first observation” of longitudinal wobbling in `133La`, using E2-dominated links plus increasing `E_wob`. The proposed microscopic cause—early gradual alignment of a positive-parity proton pair—is a QTR-supported author interpretation.

## Experimental or Theoretical Setup

`126Te(11B,4n)133La` at 52 MeV with the TIFR 14-UD Pelletron and 21-clover INGA; about `3×10^8` twofold-or-higher events.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI19-1 | Yrast and yrare negative-parity sequences are identified as `n_ω=0/1` candidates and linked by 758, 874 and 982 keV transitions. | experimental-fact | direct | PDF pp.2-3, Fig.1 | true |
| BI19-2 | Angular distributions and combined DCO-polarization fits give strong E2 admixtures for the three links; `σ/I=0.3` is assumed in DCO calculations. | experimental-criterion | direct | PDF pp.3-4, Figs.2-5, Table 1 | true |
| BI19-3 | E2 fraction increases with spin and `E_wob` increases with spin. | experimental-fact | direct | PDF pp.3-4, Figs.5-6 | true |
| BI19-4 | Authors use the increasing `E_wob` plus E2-dominated links to identify longitudinal wobbling. | author-interpretation | indirect | PDF pp.4,6, Summary | true |
| BI19-5 | QTR/HFA reproduce energies and transition ratios reasonably, while QTR overestimates some `B(M1)_out/B(E2)_in`. | model-result | direct | PDF pp.4-6, Table 1, Figs.6-8 | true |
| BI19-6 | Longitudinal behavior is attributed to early gradual alignment of a positive-parity `(dg)` proton pair, making the short-axis MoI exceed the medium-axis MoI. | author-interpretation | indirect | PDF pp.5-6 | true |
| BI19-7 | Authors explicitly state this interpretation differs from earlier treatments. | author-interpretation | direct | PDF p.6 | true |

## Nuclear Structure Information

The negative-parity yrast/yrare pair is linked by 758, 874 and 982-keV transitions. Configuration and pair-alignment assignments organize the sequence but are not direct independent observables.

## Authors' Interpretation

The authors report first longitudinal wobbling and attribute it to gradual alignment of a positive-parity proton pair that changes the effective MoI ordering.

## Model Results

QTR/HFA/TAC reproduce selected energies and ratios with assumed σ/I and effective parameters; some M1 strengths are overestimated, defining a model limit.

## Competing Interpretations and Limitations

The band configuration and additional pair alignment are model interpretations. Increasing `E_wob` classifies the calculated/assumed geometry but is not independent proof of a harmonic wobbling phonon; later IBFM/TiP alternatives remain relevant.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BI19-AR-1 | Core reconstruction | Links, fitted δ values and increasing E_wob support the reported pattern; longitudinal geometry and pair alignment remain model-mediated. | Key Results and Competing Interpretations above | unreviewed |
| BI19-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| BI19-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| BI19-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| BI19-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| BI19-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Links, fitted δ values and increasing E_wob support the reported pattern; longitudinal geometry and pair alignment remain model-mediated.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[longitudinal-wobbling]] | Original reported low-spin LW experiment. |
| competing-interpretation | [[nomura-2022-questioning-wobbling-ibfm]] | Original dataset for later IBFM challenge. |
| methodological-bridge | [[sigma-over-i-assumptions-and-mixing-ratio-extraction]] | DCO calculation uses assumed `σ/I=0.3`. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `BI19-2`, Figs.4-5 and Table 1 — Evidence: combined fits use assumed `σ/I=0.3` and branch-sensitive δ values. Agent inference: the inferred E2 fractions require an alignment-systematics audit. User check: Fig.4/5 contours, branch selection and Table 1 propagation. Risk: incorrect δ changes the longitudinal evidence chain.

### P1

- `BI19-5`/`BI19-6` — Evidence: QTR/HFA and pair alignment explain increasing E_wob. Agent inference: geometry and MoI inversion are model-mediated, not directly measured. User check: pair-alignment/configuration dependence and model normalization. Risk: model mechanism could be mistaken for experimental fact.

### P2/P3

- P1: transition-ratio/M1 overprediction. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[133la]]
- Concepts: [[longitudinal-wobbling]]
- Methods: [[angular-distribution]], [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

P0: inspect Fig.4/5 branch selection and Table 1 before using transition ratios.

## Day18 checkpoint050修订：小根仅为条件敏感性

原BI19-claims/review保留；旧BI19-D18-1关于小根的句子改分层。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI19-D18-2 | Table1大根δ=-2.05,-2.60,-3.07与BE2out/in=1.127,.716,.545是原文派生结果；旧脚本的-.35/-.40/-.38替代根未在本文Table1中作为实验解列出，必须标为条件输入。固定强度、能量和in-band E2分母时，替根可算出6.32–7.40倍的中心敏感性；不构成重新拟合或分支概率。 | conditional-root-sensitivity | direct-and-boundary | PDF5 Table1；旧result020输入 | true |
| BI19-D18-3 | 原作者以DCO/偏振/角分布的大根与wobbling模型解释三线；小根敏感性说明识别依赖，但不单独证明“完全退化为单粒子M1”，还需同源polarization likelihood、模型响应和必要寿命/绝对强度。 | author-model-boundary | direct-and-boundary | PDF3–6；Table1 methods | true |
