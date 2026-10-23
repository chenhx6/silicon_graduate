---
type: source
title: "Chakraborty et al. 2020 - Multiphonon longitudinal wobbling in 127Xe"
aliases: [Chakraborty 2020 127Xe longitudinal wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Multiphonon longitudinal wobbling in 127Xe"
authors: [S. Chakraborty, H. P. Sharma, S. S. Tiwary, C. Majumder, A. K. Gupta, P. Banerjee, S. Ganguly, S. Rai, Pragati, Mayank, S. Kumar, A. Kumar, R. Palit, S. S. Bhattacharjee, R. P. Singh, S. Muralithar]
journal: Physics Letters B
year: 2020
volume: 811
pages: 135854
doi: 10.1016/j.physletb.2020.135854
canonical_source: https://doi.org/10.1016/j.physletb.2020.135854
citation_key: chakraborty_2020_Multiphononlongitudinal
raw_file: "raw/papers/2020_Chakraborty et al_Multiphonon longitudinal wobbling in 127Xe.pdf"
raw_sha256: B04503FCE61B249AB1193F395B4276364945D02CED5EAC347A5DD2E45DF6EA1A
nuclei: [127xe]
reactions: ["122Sn(9Be,4n)127Xe"]
experiments: []
models: []
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, longitudinal-wobbling, multiphonon, odd-neutron, a130]
---

# Multiphonon longitudinal wobbling in `127Xe`

## Bibliographic Record

Physics Letters B 811, 135854 (2020), DOI `10.1016/j.physletb.2020.135854`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, four-band level scheme, DCO/polarization, `δ` branches, relative strengths, energy systematics and phonon assignments.
- Not covered: forthcoming full level scheme and independent recalculation.
- Coverage caveats: key links have contamination/low-statistics limitations; some polarization values are inherited from earlier work.

## Paper Question and Scientific Motivation

- Author-explicit motivation: search for first- and second-phonon longitudinal wobbling in an odd-neutron A≈130 nucleus (PDF pp.1-2).

## Method and Design Logic

- Extend four negative-parity bands; use DCO/polarization and δ branches for adjacent links; compare E_wob and relative transition ratios; infer n_w=0/1/2 and signature-partner roles from the decay topology (PDF pp.2-5, Figs.1-6, Table 1).

## Key Evidence and Reasoning Chain

- Selected E2-dominated links → one-phonon candidate; increasing E_wob → longitudinal label; band-4 placement/decay analogy → second-phonon claim, despite atypical topology and contaminated key evidence.

## Summary

The paper reports “conclusive evidence” for first- and second-phonon longitudinal wobbling and the first odd-neutron LW case. The Wiki preserves substantial claim-specific uncertainties, especially for the 651-keV link and the `n_ω=2` decay pattern.

## Experimental or Theoretical Setup

`122Sn(9Be,4n)127Xe` at 48 MeV with the IUAC 15UD Pelletron and 14-clover INGA; approximately `9×10^8` twofold-or-higher coincidence events.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH20-1 | Four negative-parity bands were organized into proposed `n_ω=0,1,2` and signature-partner structures. | experimental-fact | direct | PDF pp.2-5, Figs.1-2 and 6 | true |
| CH20-2 | DCO/polarization analysis of the 483-keV link gives large and small `δ` branches; polarization supports the large-E2 solution. | experimental-criterion | direct | PDF pp.3-4, Fig.3, Table 1 | true |
| CH20-3 | The 651-keV link is affected by a contaminant 652-keV transition; its polarization conflicts with a previously reported extreme large-`δ` solution and supports a smaller value. | experimental-criterion | direct | PDF pp.3-4 | true |
| CH20-4 | Band-1/Band-3 links are predominantly E2 and reported E2 fractions increase with spin. | experimental-fact | direct | PDF pp.4-5, Fig.4, Table 1 | true |
| CH20-5 | Increasing `E_wob` is used to classify the proposed sequence as longitudinal. | author-interpretation | indirect | PDF pp.4-5, Fig.5 | true |
| CH20-6 | Band 4 is assigned as second-phonon wobbling although its decay pattern is noted to differ from earlier two-phonon cases and resemble a quasi-γ-band pattern in `126Xe`. | author-interpretation | indirect | PDF p.5 | true |
| CH20-7 | Authors conclude first odd-neutron LW and first second-phonon LW observation. | author-interpretation | indirect | PDF p.5, conclusion | true |

## Nuclear Structure Information

Bands 1/3/4 are proposed as n_w=0/1/2 and band 2 as signature partner. The 651-keV link and band-4 decay pattern are the critical weak points in that hierarchy.

## Authors' Interpretation

The authors call the result conclusive evidence for odd-neutron and multiphonon longitudinal wobbling; this page retains the transition-specific caveats.

## Model Results

No independent microscopic model section is presented in the source; classification mainly uses measured transition observables, energy trends and structural analogy. Later IBFM work is external competing evidence.

## Competing Interpretations and Limitations

The paper itself notes nonstandard `n_ω=2` decay topology. Contamination, inherited polarization and branch ambiguity require transition-by-transition review. Later IBFM work provides an alternative description.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| CH20-AR-1 | Core reconstruction | One-phonon evidence is stronger than the second-phonon claim, whose atypical topology and contaminated link require separate review. | Key Results and Competing Interpretations above | unreviewed |
| CH20-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| CH20-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| CH20-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| CH20-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| CH20-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: One-phonon evidence is stronger than the second-phonon claim, whose atypical topology and contaminated link require separate review.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[longitudinal-wobbling]] | Reported odd-neutron and multiphonon LW case. |
| competing-interpretation | [[nomura-2022-questioning-wobbling-ibfm]] | Original experiment later challenged by IBFM. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `CH20-3`, 651-keV link, PDF pp.3-4 — Evidence: 652-keV contamination and polarization conflict with an earlier extreme δ solution. Agent inference: this transition is not a stable quantitative anchor. User check: subtraction/contamination handling and adopted branch. Risk: contaminated evidence propagates into strengths and band assignment.

### P1

- `CH20-6`, band 4, PDF p.5 — Evidence: the proposed n_w=2 decay topology differs from earlier cases and resembles a quasi-γ pattern. Agent inference: structural analogy does not close the second-phonon claim. User check: all band-4 branches and the alternative interpretation. Risk: an atypical side band may be mislabeled multiphonon wobbling.

### P2/P3

- P1: compare the later IBFM alternative on common observables. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[127xe]]
- Concepts: [[longitudinal-wobbling]]
- Methods: [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

P0: band-4 `n_ω=2` assignment and 651-keV contamination/branch handling.

## Day18 checkpoint052修订：多声子候选、替根敏感性与衰变拓扑

原CH20-claims/review保持；旧CH20-D18-1降为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH20-D18-1 | **superseded**：旧关于“小解下全线崩塌为单粒子/拓扑证明非wobbling”等断言降格，由D18-2/3分层记录。 | task-correction | superseded-interpretation | 本段D18-2/3；旧chakraborty20-127xe-wobbling-result-023 | true |
| CH20-D18-2 | Table 1报告五条跨带连接线大混合比（delta = -2.1至-3.1）及B(E2_out)/B(E2_in) = 0.92-2.35，受到DCO与偏振不对称度asym支持，作者据此提出多声子纵向wobbling候选；小根（|delta| ~ 0.3）是未被作者采纳的替代分支，非本文测量解。 | source-result-and-selection | direct-and-boundary | PDF p.3 Table 1；Fig. 3 | true |
| CH20-D18-3 | 在固定其余输入下，若代入小根敏感性分析，E2份额下降8.2-10.0倍；Band 4向yrast带的衰变以Delta I = 0为主，作者指出这类似于126Xe中准gamma振动与基态带的耦合，提示可能存在wobbling与gamma振动的混合。这属于结构模式讨论，不构成对两声子态存在的排他否决。 | interpretation-and-decay-topology | direct-and-derived | PDF pp.3-4；新au-xe-wobbling-boundary-result-052 | true |

## Day20量化审计：483 keV小根塌缩与两声子准伽马振动拓扑反证

> checkpoint032：008–026新增科学认证已撤回，逐claim待核；旧passed不恢复认证，source原始claims/review保持。

依据独立审计程序 `system/scripts/day20_chiral_wobbling_geometry_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/chiral-wobbling-geometry-result-022.json`，核准了 $^{127}\text{Xe}$ 483 keV 连接跃迁小根塌缩与 Band 4 衰变拓扑反证：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CH20-D20-1 | checkpoint042纠正483keV13/2→11/2，原DCO小δ−.29(+.03/−.04)，旧−.31是另选输入。作者P支持大模、原首行无E2out/in值；纯份额中心敏感性非分支概率/结构判决。Band4复杂退激提示作者wobbling–γ耦合可能，作者仍保留nω2，旧排他纯γ/非wobbling本质认证撤回。见R42-1/R42-2。 | task-multiphonon-and-decay-topology-audit | derived-and-boundary | PDF pp.3-5 Figs.3-6; Table 1; chiral-wobbling-geometry-result-022.json | true |

## Day20 checkpoint042：逐线分支、模型轴与校准依赖

本轮先冻结primed回忆，定向原读Table/图/分析与解释范围；未重新测δ或取得完整likelihood/producer。原review/flags保留，新增仅Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH20-D20-R42-1 | 483keV为13/2−→11/2−，DCO大δ−2.1(.2)或小−.29(+.03/−.04)，作者P=.23(.13)支持大模；旧−.31为另选输入。原Table1首行未报E2out/in，纯份额中心大/小比10.5079只为条件敏感性，不认证可采小分支或CI。 | literal-line-and-published-root | original-selected-and-conditional | PDF2 Fig1; PDF3 Table1/Fig3 and text | true |
| CH20-D20-R42-2 | Band4向1和3均有ΔI0/1/2退激；ΔI0较强且类似126Xequasiγ是作者提出wobbling–γ耦合的可能依据，原文仍保nω2并要求进一步理论。旧排他纯γ/证伪两声子认证不由该拓扑成立。 | author-competing-coupling | original-selected-and-conditional | PDF4 Fig6 and discussion/conclusion | true |
