---
type: source
title: "Construction and use of a three Ge(Li) Compton polarimeter"
aliases: ["Butler 1973 three GeLi polarimeter", "Three-Ge(Li) Compton polarimeter"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "CONSTRUCTION AND USE OF A THREE Ge(Li) COMPTON POLARIMETER"
authors: ["P. A. Butler", "P. E. Carr", "L. L. Gadeken", "A. N. James", "P. J. Nolan", "J. F. Sharpey-Schafer", "P. J. Twin", "D. A. Viggars"]
journal: "Nuclear Instruments and Methods"
year: 1973
volume: 108
pages: "497-502"
doi: "10.1016/0029-554X(73)90530-2"
citation_key: Butler_1973
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Butler, P. A. et al. Construction and use of a three Ge(Li) Compton polarimeter. Nucl. Instrum. Methods 108, 497-502 (1973)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1973_Butler et al_Construction and use of a three Ge(Li) Compton polarimeter.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1973_Butler et al_Construction and use of a three Ge(Li) Compton polarimeter.pdf"
raw_sha256: "1d19589bd41fb0b28230a3cb76cf8c240fc5f7899b1bd50a1c288bcfb8a3e7c2"
nuclei: ["33S", "56Fe", "24Mg", "28Si", "12C", "26Al"]
reactions: ["30Si(α,n)33S"]
observables: ["linear-polarization", "polarization-asymmetry", "polarimeter-sensitivity", "peak-to-background", "figure-of-merit"]
methods: ["compton-polarimetry", "linear-polarization-asymmetry", "angular-distribution"]
tags: [three-GeLi, Compton-polarimeter, detector-calibration, 33S, spin-parity-assignment]
---

# Construction and use of a three Ge(Li) Compton polarimeter

## Bibliographic Record

- 作者：P. A. Butler 等。
- 期刊：*Nuclear Instruments and Methods* 108, 497-502 (1973)。DOI：`10.1016/0029-554X(73)90530-2`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1973_Butler et al_Construction and use of a three Ge(Li) Compton polarimeter.pdf`；SHA-256：`1d19589bd41fb0b28230a3cb76cf8c240fc5f7899b1bd50a1c288bcfb8a3e7c2`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.497-502 全文；three-Ge(Li) apparatus、P/A/Q definitions、Compton/gamma gates、calibration Table 1、Q(E) interpolation、`33S` 4868-keV spin ambiguity application、Figs.1-6 和总结均已阅读。
- Not covered: 原始 event tapes、electronics response simulation 和引用论文全文。
- Coverage caveats: 1973 detector response is geometry/energy/threshold-specific；`33S` assignment is conditional on population and multipolarity assumptions explicitly described by the authors。

## Paper Question and Scientific Motivation

- 论文构建三 Ge(Li) Compton polarimeter，测定 `0.4-4.4 MeV` γ 线性偏振，并示范其如何解决 `33S` 4868-keV level 的 `7/2−` vs `11/2−` spin ambiguity（摘要；PDF pp.497,501）。

## Method and Design Logic

- 50 cm³ coaxial Ge(Li) 作为 scatterer，35/61 cm³ 两个 coaxial Ge(Li) 作为 `Q=0°/90°` absorbers；scatterer axis 与 beam 垂直，lead shielding 减少 direct radiation（PDF pp.497-498）。
- 定义 `P`、experimental asymmetry `A=(N⊥−N∥)/(N⊥+N∥)`，并用 relative efficiency `a(E)` 修正两个 absorber；`P=A/[Q(1−αA)]` 的实际形式把 finite geometry sensitivity `Q(E)` 纳入（PDF p.497）。
- Compton kinematic `cos θ` gates 与 511-keV pair-production veto 减少背景；calibration 用已知 E2/E1 transitions 的 angular distributions 和 polarization（PDF pp.498-500，Table 1）。

## Key Evidence and Reasoning Chain

1. `cos θ` gates 把 `56Fe` 847-keV peak-to-background 从约 3 提升至 5，并在 `33S` 841-keV complex spectrum 把 improvement factor 从 4 提升至 7；pair-production veto 进一步改善高能数据（PDF pp.498-499）。
2. Table 1 calibration 给出 Q 约 `0.44` at 847 keV、`0.274` at 1368 keV、`0.235` at 1779 keV、`0.09` at 4430 keV 等，显示 sensitivity 随能量下降（PDF p.500）。
3. 拟合得到 `Q(E)≈0.84 Q′(E)`，其中 Q′ 是点散射/点探测器 Klein-Nishina estimate；finite detector size 造成约 16% 整体 sensitivity reduction（PDF p.501，式 (5)）。
4. 对 `30Si(α,n)33S` 4868-keV level，angular distribution 给出 `a2≈0.41`、`a4≈−0.27`，单独只能支持 `7/2` 或 `11/2`；偏振测得 `P(90°)=0.56±0.15`，与 χ² 和 pure-E2 constraint 联合后选择 `11/2−`（PDF pp.501-502，Fig.6）。

## Summary

三 Ge(Li) polarimeter 以独立 scatterer/absorber geometry 兼顾 energy resolution、Compton sensitivity 和 background rejection。作者通过已知偏振线标定 Q(E)，再用 `33S` 4868-keV level 演示 polarization 与 angular distribution 联合解决 spin ambiguity。该来源为现代 clover/segmented polarimeter 提供历史 detector-response baseline，尤其展示 kinematic gate、pair veto 和 calibration dependence。

## Experimental or Theoretical Setup

- Detector: 50 cm³ scatterer + 35/61 cm³ absorbers, absorber directions 0° and 90° relative to polarization plane。
- Calibration transitions: `56Fe`, `24Mg`, `28Si`, `12C`, `26Al`, `33S` known E2/E1 cases。
- Application: `30Si(α,n)33S`, `Eα=9.8 MeV`, 4868-keV level。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B73-1 | 三 Ge(Li) polarimeter 的 P/A/Q formalism 与 relative absorber efficiency correction 已建立。 | method-definition | direct | PDF pp.497-500，式 (1)-(3) | false |
| B73-2 | Kinematic `cosθ` gates 和 511-keV veto 显著改善 peak-to-background，尤其在复杂高能谱中。 | detector-result | direct | PDF pp.498-499，Figs.2-3 | false |
| B73-3 | Q(E) 从约 `0.44` at 847 keV 降到约 `0.09` at 4430 keV，且 `Q≈0.84Q′`。 | calibration-result | direct | PDF pp.500-501，Table 1，Fig.5 | false |
| B73-4 | `33S` 4868-keV level 的 polarization `P=0.56±0.15` 与 angular distribution 联合支持 `11/2−` assignment。 | experimental-criterion | direct | PDF pp.501-502，Fig.6 | true |

## Nuclear Structure Information

- 该来源主要是方法；`33S` 仅作为 spin-assignment demonstration，不能单独替代原始 spectroscopy source。
- 4868-keV state 的最终 assignment 依赖 population/substate and pure-E2 assumptions；本页保留 conditional language。

## Authors' Interpretation

- 三晶体 polarimeter 的高 resolution 和 Compton background control 使其适合复杂 high-spin spectra；polarization 能补足 angular-distribution spin ambiguity。

## Model Results

- 不适用；Q(E) interpolation 是 detector response calibration，不是 nuclear structure model。

## Competing Interpretations and Limitations

- `33S` assignment 对 population of first two magnetic substates and E2 assumption 敏感；不同 reaction alignment 可能改变 inference。
- Q(E) depends on detector volumes, scatter angle, absorber geometry, threshold and efficiency; no universal Q.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-B73-1 | Core reconstruction | 本文把 detector calibration、background gating 和 polarization/spin inference 连接起来，强调 response-first 分析。 | PDF pp.497-502 | self-checking |
| AR-B73-2 | Assumptions and dependencies | 依赖 known-P calibration, relative efficiency `a(E)`, reaction alignment, angular-distribution coefficients and multipolarity constraint. | PDF pp.499-502 | self-checking |
| AR-B73-3 | Transfer conditions | P/A/Q/gate logic transfers; Q values and 33S inference do not transfer without matched calibration. | PDF pp.497-502 | provisional |
| AR-B73-4 | Failure conditions | Background, pair production, finite detector response or unresolved substate population can change P and spin assignment. | PDF pp.498-502 | active-L3 |
| AR-B73-5 | Reverse/falsification test | Repeat 33S-like combined χ² with alternate substate populations, no-polarization branch and independent Q calibration lines. | PDF pp.501-502 | candidate-L3 |
| AR-B73-6 | Research-question decision | Historical calibration source for P/A/Q and combined spin assignment; no L4. | PDF pp.497-502 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki already has Compton P/A/Q and detector-response boundaries; this source adds three-crystal geometry, cosθ gating, pair veto and a concrete joint spin-assignment case.
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: It supports response-first linear-polarization analysis and shows why angular distribution alone can leave spin ambiguity.
- Persistence decision: update [[compton-polarimetry]] and [[linear-polarization-asymmetry]] source lists。
- Review state: `unreviewed`; method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[compton-polarimetry]] | Historical three-Ge(Li) scatterer/absorber calibration and background controls. |
| methodological-bridge | [[spin-parity-assignment]] | Joint angular-distribution/polarization χ² resolves a conditional spin ambiguity. |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | Adds early detector-response lineage to modern clover/tracking sources. |

## Human Review Triage

### P0

- B73-P0-1：`33S` `11/2−` assignment is conditional on reaction population and pure-E2 assumptions; do not state as unconditional without the source boundary。

### P1

- B73-P1-1：Q(E) and background-improvement ratios are detector-specific calibration values。

### P2/P3

- DOI and pages are aligned from PDF PII; no nucleus page created。

## Extracted Pages

- Nuclei: no standalone `33S` page。
- Bands: no band page。
- Concepts: Compton response, polarization calibration, spin ambiguity。
- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[spin-parity-assignment]]。

## Non-source Notes and Follow-up

- Next: compare B73 with Simpson HS-008 and Garcia-Raffi HS-009 in the detector-method project; continue HS-013.
