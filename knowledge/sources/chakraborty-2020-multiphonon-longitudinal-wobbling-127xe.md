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

## Day18定量审计：多声子纵向wobbling混合比双解敏感性与两声子衰变拓扑异常

在Day18正式学习中对本文Table 1与正文p.4中127Xe的跃迁几率比值及两声子带衰变拓扑进行定量审计，raw SHA256 `B04503FCE61B249AB1193F395B4276364945D02CED5EAC347A5DD2E45DF6EA1A`已核。原CH20-1–7各claim及`human-reviewed`状态完全保留；新CH20-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH20-D18-1 | 本文Table 1报告的五条跨带连接线（639, 735, 800, 884, 638 keV）的B(E2_out)/B(E2_in)高达0.92–2.35，被作为核内首个“多声子纵向wobbling”模式的证据。定量审计揭示双重物理脆弱性：(1) 在DCO小解分支（|delta| ~ 0.30–0.35）下，所有五条跃迁的B(E2_out)/B(E2_in)遭遇8.19至10.04倍的断崖式暴跌（暴跌至0.100–0.234），而B(M1_out)/B(E2_in)反向暴增5.36至9.57倍（跃升至0.380–0.739 mu_N^2/e^2b^2），使所谓集体E2增强与M1抑制完全退化为单粒子M1跃迁；(2) 声称的二声子带（Band 4）向yrast带（Band 1）的退激反常地以Delta I = 0跃迁为主导，且其强度高于Delta I = 2跃迁，直接违背谐振子wobbling声子两声子退激的选择定则，其拓扑模式与126Xe中准gamma振动带耦合完全相符（后由Nomura 2022 IBFM证实）。 | task-rate-decomposition-audit | derived-and-boundary | PDF pp.3-5 Table 1；新chakraborty20-127xe-wobbling-result-023 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/chakraborty20-127xe-wobbling-contract-023.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/chakraborty20-127xe-wobbling-result-023.json)4项检查全过。
