---
type: source
title: "Rojeeta Devi et al. 2021 - Observation of multiphonon transverse wobbling in 133Ba"
aliases: [Rojeeta Devi 2021 133Ba wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Observation of multiphonon transverse wobbling in 133Ba"
authors: [K. Rojeeta Devi, Suresh Kumar, Naveen Kumar, Neelam, F. S. Babra, Md. S. R. Laskar, S. Biswas, S. Saha, P. Singh, S. Samanta, S. Das, S. Chakraborty, R. P. Singh, S. Muralithar, A. Kumar]
journal: Physics Letters B
year: 2021
volume: 823
pages: 136756
doi: 10.1016/j.physletb.2021.136756
canonical_source: https://doi.org/10.1016/j.physletb.2021.136756
citation_key: rojeetadevi_2021_Observationmultiphonon
raw_file: "raw/papers/2021_Rojeeta Devi et al_Observation of multiphonon transverse wobbling in 133Ba.pdf"
raw_sha256: FB6EA8474676875752CA83399E8F27AA792AA07643C5FA962FE44CAB1AE0697B
nuclei: [133ba]
reactions: ["124Sn(13C,4n)133Ba"]
experiments: []
models: [triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, transverse-wobbling, multiphonon, hole-like-quasiparticle, a130]
---

# Multiphonon transverse wobbling in `133Ba`

## Bibliographic Record

Physics Letters B 823, 136756 (2021), DOI `10.1016/j.physletb.2021.136756`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, bands 1-4, new links, DCO/polarization, mixing ratios, transition ratios and QTR/FA comparison.
- Not covered: detailed setup paper cited as Ref.39 and independent QTR reproduction.
- Coverage caveats: low-energy 146.3/219.2-keV links could not be characterized; some in-band E2 assignments are assumed from band structure.

## Paper Question and Scientific Motivation

- Author-explicit motivation: identify multiphonon transverse wobbling associated with a hole-like quasiparticle in `133Ba` (PDF pp.1-2).

## Method and Design Logic

- Extend bands and links, use DCO/polarization contour fits where statistics permit, calculate E_wob and relative ratios, and compare a frozen-alignment QTR description with the proposed n_w ladder (PDF pp.2-6, Figs.1-4, Tables 1-2).

## Key Evidence and Reasoning Chain

- Electric/E2-dominated measured links → adjacent-band wobbling evidence; decreasing E_wob → transverse classification; QTR agreement → hole-like n_w=0/1/2 interpretation; unmeasured low-energy links leave the ladder incomplete.

## Summary

The paper reports `n_ω=0,1,2` transverse wobbling and calls it the first hole-like quasiparticle TW case. The adjacent-band links with sufficient statistics are predominantly electric/E2, but the full decay network is not uniformly measured.

## Experimental or Theoretical Setup

`124Sn(13C,4n)133Ba` at 48 MeV using the TIFR 14-UD Pelletron; 11 Compton-suppressed INGA clovers at 157°, 140°, 115° and 90°.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RD21-1 | New γ transitions extend the negative-parity band system and support bands 1/2/3 as proposed `n_ω=0/1/2`; band 4 is assigned signature partner. | experimental-fact | direct | PDF pp.2-4, Fig.1 | true |
| RD21-2 | `R_DCO` and polarization establish electric character for key 613.2, 626.8 and 812.0-keV adjacent-band links; contour fits provide `δ` and E2 fractions. | experimental-criterion | direct | PDF pp.2-4, Figs.3-4, Tables 1-2 | true |
| RD21-3 | 146.3 and 219.2-keV links could not be measured by DCO/polarization because of low energy/intensity. | experimental-fact | direct | PDF pp.2,4 | true |
| RD21-4 | `E_wob` decreases with spin and is used to classify transverse wobbling. | experimental-fact | direct | PDF pp.3-5 | true |
| RD21-5 | QTR frozen-alignment calculations reproduce the reported wobbling energy and transition ratios with a hole-like `νh11/2` geometry. | model-result | direct | PDF pp.4-6 | true |
| RD21-6 | Authors conclude first multiphonon TW associated with a hole-like quasiparticle. | author-interpretation | indirect | Abstract and conclusion | true |

## Nuclear Structure Information

Bands 1/2/3 are proposed as n_w=0/1/2 and band 4 as signature partner. The 146.3- and 219.2-keV links lack measured multipolarities.

## Authors' Interpretation

The authors report first hole-like multiphonon transverse wobbling; the source does not claim uniform electromagnetic characterization of every ladder link.

## Model Results

Frozen-alignment QTR reproduces selected energies/ratios using chosen MoI values. Its alignment and rigidity assumptions define the interpretation boundary.

## Competing Interpretations and Limitations

The band hierarchy combines measured and assumed multipolarities. Missing low-energy link characterization weakens a fully closed phonon ladder; frozen alignment and selected MoI values remain model assumptions.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| RD21-AR-1 | Core reconstruction | Several adjacent links are measured, but uncharacterized low-energy links prevent a uniformly closed multiphonon ladder. | Key Results and Competing Interpretations above | unreviewed |
| RD21-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| RD21-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| RD21-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| RD21-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| RD21-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Several adjacent links are measured, but uncharacterized low-energy links prevent a uniformly closed multiphonon ladder.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[transverse-wobbling]] | Reported hole-like multiphonon candidate with measured electric links. |
| limits | [[interband-e2-strengths]] | Some low-energy adjacent-band links remain uncharacterized. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- P0: none identified.

### P1

- `RD21-2`/`RD21-3`, Tables 1-2 — Evidence: several links are electric/E2, but 146.3 and 219.2 keV lack multipolarity measurements. Agent inference: the phonon ladder is not electromagnetically complete. User check: which ladder steps are measured versus assumed and whether the n_w=2 assignment survives. Risk: uniform certainty would overstate incomplete coverage.

### P2/P3

- P2: in-band E2 assumptions and selected MoI values. P3: navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[133ba]]
- Concepts: [[transverse-wobbling]]
- Methods: [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

Review Table 2 and the unmeasured 146/219-keV links separately.


## Day18定量审计：跨带B(E2)out/B(E2)in的五次方能量比放大代数解构

在Day18正式学习中对本文Table 1与2中133Ba带间跃迁数据进行代数解构与物理审计，raw SHA256 `FB6EA8474676875752CA83399E8F27AA792AA07643C5FA962FE44CAB1AE0697B`已核。原RD21-1–6各claim及`human-reviewed`状态完全保留；新RD21-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RD21-D18-1 | 本文Table 2报告的三条跨带跃迁带间与带内强度比 $B(E2)_	ext{out}/B(E2)_	ext{in}$ 高达 $2.94(18)$、$2.36(20)$ 和 $3.40(22)$（远超Lu同位素中 $\sim 0.2	ext{--}0.3$ 的范围）。代数解构证实该异常大比值主要由相空间动力学因子 $(E_	ext{in}/E_	ext{out})^5$ 主导：743.4 keV放大1.54倍，812.0 keV放大2.29倍，457.6 keV（带内641.9 keV）放大高达5.43倍！这证明 $B(E2)_	ext{out}/B(E2)_	ext{in} > 1$ 是由于低激发能跨带线被五次方相空间因子强烈放大所致，绝不自动等同于四极跃迁算符本征矩阵元超越内禀跃迁。 | task-rate-decomposition-audit | derived-and-boundary | PDF p.4 Tables 1–2；新devi21-133ba-wobbling-result-019 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/devi21-133ba-wobbling-contract-019.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/devi21-133ba-wobbling-result-019.json)4项检查全过。
