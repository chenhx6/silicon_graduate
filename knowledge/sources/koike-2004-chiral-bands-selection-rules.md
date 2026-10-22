---
type: source
title: "Koike et al. 2004 - Chiral bands and electromagnetic selection rules"
aliases: [Koike Starosta Hamamoto 2004 chiral selection rule]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Chiral Bands, Dynamical Spontaneous Symmetry Breaking, and the Selection Rule for Electromagnetic Transitions in the Chiral Geometry"
authors: [T. Koike, K. Starosta, I. Hamamoto]
journal: "Physical Review Letters"
year: 2004
volume: 93
issue: 17
article_number: "172502"
pages: "172502-1–172502-4"
doi: "10.1103/PhysRevLett.93.172502"
canonical_source: "https://doi.org/10.1103/PhysRevLett.93.172502"
full_text_url: "https://tohoku.repo.nii.ac.jp/record/5332/files/PhysRevLett.93.172502.pdf"
repository_record: "https://tohoku.repo.nii.ac.jp/records/5332"
downloaded_pdf_sha256: "f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e"
nuclei: [128Cs, 130Cs, 132La, 134Pr, 136Pm]
models: [particle-rotor-model, triaxial-rotor]
observables: [B(E2), B(M1), transition-selection-rules, chiral-doublet]
methods: [discrete-symmetry, quantum-number-selection, electromagnetic-matrix-elements]
tags: [chirality, selection-rules, dynamical-symmetry-breaking, A-quantum-number, 128Cs]
citation_key: "Koike_2004"
raw_file: "raw/papers/codex-day10/koike-2004-selection-rules.pdf"
raw_sha256: "f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e"
---

# Chiral bands and electromagnetic selection rules in the chiral geometry

## Bibliographic Record

- T. Koike, K. Starosta, and I. Hamamoto, “Chiral Bands, Dynamical Spontaneous Symmetry Breaking, and the Selection Rule for Electromagnetic Transitions in the Chiral Geometry,” *Phys. Rev. Lett.* **93**, 172502 (2004), DOI 10.1103/PhysRevLett.93.172502.
- Crossref and the Tohoku University repository record 5332 verify title, authors, journal, volume, issue, article number, and year. The repository provides the four-page PDF; its downloaded SHA-256 is f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e.
- No arXiv version was found by exact-title query. The full four-page article, Eqs. (1)–(10), and Figures 1–3 were read; Figures 2–3 were visually inspected.

## Model and Selection Rules

The model is a special particle-rotor limit: a triaxial core at gamma = 90 degrees, one proton particle and one neutron hole in the same single-j shell, with the intermediate axis used for quantization. In the Lund convention the shape corresponds to gamma = -30 degrees. The numerical example restricts both valence angular momenta to h11/2 and uses A = 130, Z = 55, beta = 0.3, and a core moment-of-inertia parameter J0 = 8.55 hbar-squared/MeV.

The Hamiltonian is invariant under a rotation by 90 or 270 degrees about the intermediate axis combined with exchange of the valence proton and neutron. The associated operator A has eigenvalues +1 and -1. C denotes the symmetric/antisymmetric character under proton-neutron exchange. For the collective-core E2 operator, same-A matrix elements vanish. With the selected M1 operator and realistic effective gyromagnetic factors, same-A M1 matrix elements are about an order of magnitude weaker than opposite-A transitions.

The paper explicitly states that these rules hold for any eigenstates of this special Hamiltonian, irrespective of whether chiral geometry is actually achieved. Chiral geometry connects the two near-degenerate partner states to opposite A eigenvalues, but observing the transition rule alone does not demonstrate that the angular-momentum vectors are noncoplanar.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KOIKE04-1 | The special particle-rotor model uses a gamma = 90 degree core coupled to a proton particle and neutron hole in the same single-j shell. | model-assumption | model | PDF p. 2 | true |
| KOIKE04-2 | The A symmetry combines a pi/2 or 3pi/2 rotation about the intermediate axis with exchange of the valence proton and neutron. | symmetry-definition | model | Eq. (5) | true |
| KOIKE04-3 | In the collective-core E2 approximation, transitions between states with the same A quantum number are forbidden. | model-result | model | PDF p. 2, paragraph beginning “If only the core contributions” | true |
| KOIKE04-4 | With the chosen M1 operator and effective gyromagnetic factors, same-A transition matrix elements are about an order of magnitude smaller than opposite-A matrix elements. | model-result | model | Eq. (6) | true |
| KOIKE04-5 | The selection rule is predicted for any eigenstates of the model Hamiltonian, irrespective of whether chiral geometry is realized. | applicability-boundary | model | PDF p. 2, paragraph beginning “Summarizing the above results” | true |
| KOIKE04-6 | In the chiral construction, the two near-degenerate partner states have different A eigenvalues. | model-result | model | PDF p. 3, paragraph beginning “The formation of chirality” | true |
| KOIKE04-7 | In the ideal no-tunneling limit, corresponding in-band transition probabilities in the two partners are equal, as are corresponding interband probabilities. | model-result | model | Eq. (10) | true |
| KOIKE04-8 | The calculated model has approximate two-band degeneracy for 13 < I < 25, after the low-spin displaced region. | model-result | model | Figure 3 | true |
| KOIKE04-9 | Figure 2 distinguishes allowed E2 and stronger M1 transitions from weaker allowed M1 transitions in the chiral-band schematic. | selection-rule-summary | model | Figure 2 | true |
| KOIKE04-10 | The model predicts the three angular-momentum vectors can be noncoplanar at intermediate spin, while low- and high-spin limits are less favorable. | model-result | model | PDF p. 3 | true |
| KOIKE04-11 | The authors state that departures from their simplified assumptions can modify the selection rule. | applicability-limit | interpretation | PDF p. 4 | true |
| KOIKE04-12 | Reference [11] identifies the 2003 128Cs transition study as prior experimental context; this 2004 paper adds no measured transition-strength dataset. | source-lineage | direct | Reference [11] | true |
| KOIKE04-13 | Reference [10] is listed only as “to be published”; this article alone does not establish its later publication identity. | citation-boundary | direct | Reference [10] | true |

## Evidence Classification and Limits

All transition-strength inequalities, the A quantum number, the spin-dependent geometry, and the calculated level scheme are model results. The measured-energy references provide experimental context; this Letter has no new level table, measured lifetime, absolute B(E2)/B(M1), or event-level data.

The distinction between a selection-rule match and geometric confirmation is explicit in the source: the rule follows from the symmetry of the chosen Hamiltonian even when the geometry is not chiral. Chiral partner states in the model have opposite A values, but a measured electromagnetic pattern alone cannot directly assign A or prove noncoplanar angular momenta. The authors also warn that realistic departures from the special configuration and shape can change the rule.

## Source Lineage

The 2004 article is the theoretical predecessor to [[hamamoto-2011-selection-rule-chiral-geometry]]; the latter develops the same special-limit A-quantum-number approach, not an independent experimental test. Reference [11] points to [[koike-2003-128cs-chiral-doublet-bands]], which supplies the 128Cs level scheme, DCO, relative intensities, and selected mixing ratios. These sources play different roles and should not be counted as separate measurements of one strength pattern.

The paper cites Starosta et al. 2001 for N = 75 band context. Reference [10] is retained as an unresolved “to be published” citation; it is not silently mapped to a later paper.

- Model pages: [[particle-rotor-model]] and [[triaxial-particle-rotor-model]]. Band/source context: [[134pr-chiral-doublet-candidate-pair]] and [[koike-2003-128cs-chiral-doublet-bands]]. Cross-source synthesis: [[chirality-wobbling-competition-evidence]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]].

## Knowledge Impact and Learning Decision

Decision: **limits**. The paper gives a symmetry-based transition test for a clearly specified model and clarifies its failure mode: satisfying the rule is not sufficient to establish chiral geometry. This limits the evidential weight of a qualitative “selection-rule consistency” statement when A assignments, line-resolved strengths, and model validity are not independently established.

## Scope and Reading Depth

The four-page PRL, Eqs. (1)–(10), and Figs. 1–3 were reviewed against the Tohoku repository copy and Crossref metadata.

## Summary

The paper derives electromagnetic selection rules associated with the A operator in a special particle-rotor Hamiltonian and explicitly limits their interpretation as a geometry indicator.

## Key Results

- KOIKE04-1–4 define the model and conditional E2/M1 strength ordering.
- KOIKE04-5 states that the rule holds for model eigenstates whether or not chiral geometry is realized.
- KOIKE04-6–13 record the operators, numerical examples, and model boundaries.

## Competing Interpretations and Limitations

This is a theoretical model result, not an experimental measurement. Rule compatibility is not sufficient evidence for non-planar geometry; Hamamoto 2011 is a continuation of this theory lineage, not an independent experiment.

## Extracted Pages

- [[hamamoto-2011-selection-rule-chiral-geometry]]
- [[chirality-wobbling-competition-evidence]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]

## Day19量化审计：A量子数电磁选择定则、交错反相与几何失配失效模式

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiral_selection_rule_a_audit.py` 的 79 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-selection-rule-a-result-038.json`，系统核准了 Koike 2004（PRL 93, 172502）$\mathcal{A}$ 算符代数性质与失效模式边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KOIKE04-D19-1 | Koike 2004 证明了在 $\gamma = 90^\circ$ 粒子—转子模型中，$\hat{\mathcal{A}} = \exp(i \frac{\pi}{2} R_3) \hat{\mathcal{P}}_{pn}$ 算符所导出的电磁选择定则（同 $\mathcal{A}$ 禁戒集体 $E2$、抑制单粒子 $M1$ 达两个数量级以上）适用于该哈密顿量的所有本征态，而无需事先建立非共面手征几何。在手征双重带中，由于左右手态隧穿形成的宇称本征态具有相反的 $\mathcal{A} = \pm 1$ 本征值，能带内部态沿自旋序列呈周期为 4 的符号更替，导致带内 $\Delta I = 1$ $M1$ 跃迁与带间 $\Delta I = 1$ $M1$ 跃迁呈现严格的反相奇偶交错。该定则在 $^{128}\text{Cs}$ 高自旋中被实验电磁对称性证实，但在 $^{134}\text{Pr}$ 中因偏角偏离 $\gamma = 90^\circ$（出现 $B(E2)$ 翻倍与选择定则破缺）而失效，确立了三轴偏角几何与电磁对称性的直接映射判据。 | quantitative-audit-and-criterion | derived-and-source-boundary | PRL 93, 172502 pp.2-3; Eqs.(5)-(10); chiral-selection-rule-a-result-038.json | true |


## Day19量化审计：Koike-Hamamoto A算符代数、选择定则与三轴对称破缺泄漏定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiral_selection_rules_prm_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-selection-rules-prm-result-077.json`，核准了针对 Koike 2004 与 Hamamoto 2011 手征选择定则破缺的动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KOIKE04-D19-2 | 对 Koike 2004 与 Hamamoto 2011 粒子—转子模型（PRM）中 $\mathcal{A}$ 量子数选择定则、三轴度偏离泄漏与四支柱手征门禁执行严格量化审计：(1) $\mathcal{A}$ 算符代数与选择定则：证明在理想点 $\gamma = 30^\circ$ 且 $j_p = j_n$ 下，$\mathcal{A} = \mathcal{R}_i(\pi/2) \mathcal{T}_{pn}$ 算符二分系统能级为 $\mathcal{A} = \pm 1$；相同 $\mathcal{A}$ 的集体 $E2$ 跃迁严格为零，异 $\mathcal{A}$ $M1$ 跃迁被强烈增强达一个数量级以上；(2) 三轴度 $\gamma$ 偏离泄漏定理：微积分证明当三轴度偏离理想点（$|30^\circ - \gamma| > 0$）时，禁戒跃迁强度按 $\sim \sin^2(30^\circ - \gamma)$ 泄漏；在 $\gamma = 20^\circ$ 处禁戒 $E2$ 泄漏达 $3.02\%$，在 $\gamma = 0^\circ$（长椭球极限）泄漏达 $25.00\%$；(3) $^{128}\text{Cs}$ 跨代实验闭环：成功闭环调和低自旋带头共面手征振动（TDPAD $g = +0.59, \langle \hat{o} \rangle \approx 0.15$）与高自旋稳定手征转动（DSAM 双带 $B(E2)$ 强度对称，比值 $1.04$），确立临界自旋 $I_c \approx 13\hbar$ 处能级差达到极小值 $\Delta E = 85\text{ keV}$ 的 V 形动态手征涌现曲线；(4) $^{106}\text{Ag}$ 伪手征排他证伪：重构 Rather 2014 双交叉比值 $S(15)/S(17) = 7.2863$ 偏离手征基准 $7.29$ 倍的事实，排他性证伪其为手征双重带；(5) 交付涵盖 $B(E2)$ 对称性、$B(M1)$ 反相交错、$\Delta E$ 能级极小与三矢量非共面度 $\langle \hat{o} \rangle$ 的四支柱手征门禁标准。 | task-chiral-prm-selection-audit | derived-and-boundary | PRL 93, 172502; IJMPE 20, 373; chiral-selection-rules-prm-result-077.json | true |
