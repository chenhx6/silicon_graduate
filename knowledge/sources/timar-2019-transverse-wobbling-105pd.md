---
type: source
title: "Timár et al. 2019 - Experimental Evidence for Transverse Wobbling in 105Pd"
aliases: [Timar 2019 105Pd transverse wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Experimental Evidence for Transverse Wobbling in 105Pd"
authors: [J. Timár, Q. B. Chen, B. Kruzsicz, D. Sohler, I. Kuti, S. Q. Zhang, J. Meng, P. Joshi, R. Wadsworth, K. Starosta, A. Algora, P. Bednarczyk, D. Curien, Zs. Dombrádi, G. Duchêne, A. Gizon, J. Gizon, D. G. Jenkins, T. Koike, A. Krasznahorkay, J. Molnár, B. M. Nyakó, E. S. Paul, G. Rainovski, J. N. Scheurer, A. J. Simons, C. Vaman, L. Zolnai]
journal: Physical Review Letters
year: 2019
volume: 122
pages: 062501
doi: 10.1103/PhysRevLett.122.062501
canonical_source: https://doi.org/10.1103/PhysRevLett.122.062501
citation_key: timar_2019_ExperimentalEvidence
raw_file: "raw/papers/2019_Timár et al_Experimental Evidence for Transverse Wobbling in Pd 105.pdf"
raw_sha256: 3948CF32712A400AA8DF0AEE489EBEBD89DF7480508BDDC60156A359ED322909
nuclei: [105pd]
reactions: ["96Zr(13C,4n)105Pd"]
experiments: []
models: [covariant-density-functional-theory, particle-rotor-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [dco-ratio, linear-polarization-asymmetry, gamma-gamma-coincidence]
tags: [experiment-ingest, transverse-wobbling, one-neutron, low-spin]
---

# Experimental Evidence for Transverse Wobbling in `105Pd`

## Bibliographic Record

PRL 122, 062501 (2019), DOI `10.1103/PhysRevLett.122.062501`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, level scheme, DCO/polarization, `δ`, wobbling energy, CDFT+PRM comparison and limitations.
- Not covered: unpublished follow-up cited by the paper.
- Coverage caveats: band C is less well reproduced/constrained than the primary A/B pair; PRM uses effective `g`-factor quenching.

## Paper Question and Scientific Motivation

- Author-explicit motivation: establish a one-neutron, A≈100 transverse-wobbling case using electromagnetic link character and the predicted spin dependence of wobbling energy (PDF pp.1-2).

## Method and Design Logic

- Combine DCO and polarization to select δ branches for A-B links; compute E_wob; obtain triaxial input from CDFT and compare bands/transition ratios with PRM through the upbend region (PDF pp.2-5, Figs.1-3, Table I).

## Key Evidence and Reasoning Chain

- Polarization-selected large δ → E2-dominated A-B links; decreasing E_wob through I=29/2 → transverse signature; CDFT+PRM reproduction → author geometry assignment, with a configuration-change boundary above the upbend.

## Summary

The paper reports experimental evidence for transverse wobbling in bands A/B of `105Pd`, with large mixing ratios selected by combined DCO and polarization and a decreasing `E_wob` up to `I=29/2`.

## Experimental or Theoretical Setup

`96Zr(13C,4n)105Pd` at Vivitron/IReS; EUROBALL IV with 15 Cluster and 24 Clover detectors plus DIAMANT charged-particle veto.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TI19-1 | Bands B/C were established as negative-parity E2 rotational bands linked to the known `νh11/2` band A. | experimental-fact | direct | PDF pp.2-3, Fig.1 | true |
| TI19-2 | For 991, 1034 and 994 keV A-B links, DCO+polarization select `δ=1.8(5),2.3(3),2.7(6)`, about 80% E2. | experimental-criterion | direct | PDF pp.2-3, Fig.2 | true |
| TI19-3 | Earlier smaller angular-distribution solutions for two links are disfavoured specifically by the polarization data. | experimental-criterion | direct | PDF p.3 | true |
| TI19-4 | Experimental `E_wob` decreases with spin to `I=29/2`, used as the transverse-wobbling signature. | experimental-fact | direct | PDF pp.3-4, Fig.3(c) | true |
| TI19-5 | CDFT gives triaxial input and PRM reproduces A/B energies and transition ratios; band C energies are overestimated by about 500 keV. | model-result | direct | PDF pp.4-5, Fig.3, Table I | true |
| TI19-6 | PRM uses a `0.36` quenching of `g_eff` to address known M1 overestimation and reproduce `δ`. | model-result | direct | PDF p.5 | true |
| TI19-7 | Authors conclude first one-neutron transverse-wobbling evidence and first A≈100 wobbling observation. | author-interpretation | indirect | PDF p.5, Summary | true |

## Nuclear Structure Information

Bands A/B are the primary νh11/2 zero-/one-phonon candidates; band C is less well reproduced. The interpretation is explicitly bounded to I≤29/2 before the reported configuration change.

## Authors' Interpretation

The authors call the case first one-neutron transverse wobbling. Earlier small-δ angular-distribution solutions are rejected using the new polarization observable.

## Model Results

CDFT supplies triaxial deformation and PRM reproduces A/B behavior using effective inertia and g-factor quenching; band C remains overpredicted by about 500 keV.

## Competing Interpretations and Limitations

The A/B assignment is stronger than energy-only cases because branch selection uses polarization. Nevertheless, configuration changes above the upbend, effective inertia parametrization and M1 quenching restrict model transfer; the paper itself bounds the main interpretation to `I≤29/2`.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| TI19-AR-1 | Core reconstruction | The direct chain is polarization-selected E2 dominance plus decreasing E_wob through I=29/2; the angular-momentum geometry remains model-derived. | Key Results and Competing Interpretations above | unreviewed |
| TI19-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| TI19-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| TI19-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| TI19-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| TI19-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: The direct chain is polarization-selected E2 dominance plus decreasing E_wob through I=29/2; the angular-momentum geometry remains model-derived.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[transverse-wobbling]] | One-neutron A≈100 case with polarization-selected large `δ`. |
| competing-interpretation | [[nomura-2022-questioning-wobbling-ibfm]] | Provides the original experimental dataset challenged by the later IBFM comparison. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `TI19-2`/`TI19-3`, Fig.2 — Evidence: polarization selects large δ values that conflict with earlier smaller angular-distribution solutions. Agent inference: the branch selection is decisive. User check: polarization sign, conventions and fit compatibility. Risk: wrong branch removes E2 dominance.

### P1

- `TI19-4`/`TI19-5`, Fig.3 and Table I — Evidence: decreasing E_wob and PRM agreement apply through `I≤29/2`; a configuration change follows. Agent inference: the wobbling family cannot be extended unchanged above the boundary. User check: exact spin cutoff and band-C/model mismatch. Risk: overextending the conclusion mixes configurations.

### P2/P3

- P1: g-factor quenching and CDFT deformation inputs. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[105pd]]
- Concepts: [[transverse-wobbling]]
- Methods: [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

User review should compare TI19 mixing ratios with the conflicting values summarized in Nomura 2022.

## Day18修订：DCO双解、偏振companion与有效g定标

原TI19-1–7及原human-reviewed页状态/各原flags完全保持；仅新Day18追加段纠错，新增行仍needs_review true。旧result/contract-021有条件替δ算术，但checks_passed=True不是原实验拟合验证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TI19-D18-1 | 撤回旧把DCO小解称唯一physical根、无理由“人工强配”与完整M1算符削弱7.72倍的结论；仅保留固定其余输入时的替δ敏感性，由D18-2–6限定。 | task-correction | superseded-interpretation | 本段D18-2–6；旧result-021 | true |
| TI19-D18-2 | TableI三线991/1034/994的RE2为.66(.18)/.60(.09)/.34(.07)，采用δ1.8(.5)/2.3(.3)/2.7(.6)。它们是作者实验提取；δ与派生B同data，不能各计独立实验。 | reported-result-and-dependence | direct | PDF5 TableI | true |
| TI19-D18-3 | 作者确实报告991/1034的DCO也容.59(.20)/.40(.06)，但立即以同实验linear polarization反对小解、支持大解；Rickey AD .46(.10)/.62(.18)为另引用结果，本文未提供本次已取得的全部原producer/Σ。994的.35不是原文明确数值，只能自设条件input。 | companion-and-branch-boundary | direct | PDF3右栏/Fig2；Ref29；[[nomura-2022-questioning-wobbling-ibfm]] NOM22-D18-6 | true |
| TI19-D18-4 | 固定强度比、能量及in-band E2假设时，以fE2=δ²/(1+δ²)替991/1034的小δ可使RE2变为.223021/.098403，同时RM1变为.509517/.482595。此为条件中心敏感性，不是新观测、branch概率或对原偏振选择的反驳。 | task-conditional-rate-decomposition | derived-and-boundary | PDF3所印两小解；PDF5 TableI；新mixed-boundary result-047 | true |
| TI19-D18-5 | 原文定义g_eff=g_nu(h11/2)-g_R，δ∝Q0/g_eff、RM1∝(g_eff/Q0)²；以q=.36缩放g_eff以定标21/2→19/2 δ，并明说原PRM缺scissors-mode mixing作为理由。该点是定标，其他量仍需逐项评价，不能称无物理理由或将所有一致性归于强配。 | model-definition-and-calibration | direct | PDF4末段；PDF5首段/TableI footnote a；原Ref44 | true |
| TI19-D18-6 | 固定波函数/Q0和原比例式适用时，q=.36使有效M1幅度乘.36、强度乘.1296（逆比7.716），δ乘2.778。q(g_nu-g_R)不同于q g_nu-g_R；未得完整producer，不把它当所有M1算符或其它核/多qp模型的普适缩放。 | conditional-model-scaling | derived-and-boundary | TI19-D18-5；新mixed-boundary result-047 | true |

独立worker完整六页文字主线，PDF3/5视觉；主代理定向原读PDF3–5并核关键图/表。原raw SHA256 `3948cf32712a400aa8df0aee489ebebd89df7480508bddc60156a359ed322909`保持；无原response/Cov，未求新τ/B/δ实验CI。作者的wobbling解释与IBFM替代模型均保留证据和适用边界。
