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
raw_file: "raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/koike-2004-selection-rules.pdf"
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
| KOIKE04-D19-1 | superseded at Day23checkpoint049：撤回旧四支柱/实验排他或跨核闭环认证、未由本源支持的精确泄漏式/百分数及把A当parity的表述。以KOIKE04-1至13和KOIKE04-D23-001至004的源条件为准；旧全文保pre-correction049。 | withdrawn-task-certification | rejected-and-replaced | checkpoint049 originalPRL pp2–4 | true |


## Day19量化审计：Koike-Hamamoto A算符代数、选择定则与三轴对称破缺泄漏定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiral_selection_rules_prm_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-selection-rules-prm-result-077.json`，核准了针对 Koike 2004 与 Hamamoto 2011 手征选择定则破缺的动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KOIKE04-D19-2 | superseded at Day23checkpoint049：撤回旧四支柱/实验排他或跨核闭环认证、未由本源支持的精确泄漏式/百分数及把A当parity的表述。以KOIKE04-1至13和KOIKE04-D23-001至004的源条件为准；旧全文保pre-correction049。 | withdrawn-task-certification | rejected-and-replaced | checkpoint049 originalPRL pp2–4 | true |

## Day23定向原件回核：轴、EM截断和带标签

本次完整回读4页正文/Eqs1–10/Figs1–3，fresh视觉核pp2–4；新下载Tohoku副本与既有raw同SHA f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e。既有KOIKE04-1至13已覆盖主线，不以重复阅读冒充新独立证据。此次补下列实际缺口并定向撤回两条旧任务过认证；不改原raw/Bib/既有flags，不新增human-reviewed。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KOIKE04-D23-001 | 本源γ90°以3轴为m量子化轴、1l/2s/3m，明确等价Lundγ−30°。Eq1的Hrot=ħ²[R3²+4(R1²+R2²)]/(8J0)，惯量为(Jl,Js,Jm)=(J0,J0,4J0)，数值例J0=8.55ħ²/MeV而非任务ZH07variant的Jm=30/Js=Jl=7.5。二者结构可在明确轴变换后比较，不能裸抄γ/J0或称数值输入已相同。 | source-coordinate-and-inertia-definition | direct-original-visual-and-bounded-model-comparison | printed172502-2 Eqs1–4/axis paragraph; printed172502-3 numericalinputs | true |
| KOIKE04-D23-002 | A由绕core R3的π/2或3π/2与价p/n交换C组合；这里C是unitary标签交换，不是本Wiki常写的antiunitary手征Cχ。same-A coreE2为0，same-A M1在near-isovector采用g条件下较弱，不是普遍严格M1零；源明确选择规则对该H任意本征态成立，无论是否达手征几何。A分扇区并不强迫能量简并。 | source-operation-identity-and-selection-domain | direct-original-plus-operator-boundary | printed172502-2 Eq5/6 and lastparagraph | true |
| KOIKE04-D23-003 | 作者说明全basis H对角化后，lowest/highest single-particle levels的粒子/空穴成分近bandhead约98%，到I15降约70%；随后EM计算改用限制这两个levels的simplifiedmodel。Fig3在近简并区按B(E2;I→I−2)组织两带，低spin按能量；因此in/out的bandlabel不是全程energyordinal定义，未公开的EM简化也不能被任务fullj矩阵静默代替或相反。 | source-EM-truncation-and-band-mapping | direct-original | printed172502-3 Fig3organizationparagraph; printed172502-4 first/secondcolumns and Fig3caption | true |
| KOIKE04-D23-004 | Eq10两组partner对应率相等使用Eq7/8左右手线性组合及Eq9 cross-handed EM≈0的理想极限；不是近简并独自推出。数值例另用gR=55/130、gs,eff=.6gs,free和core-only E2，说明实际偏离简化条件可改规则。源所说staticquadrupole moment0是本模型same-A lab静态量，不是intrinsicQ0=0或detector Q(E)=0。旧精确sin²泄漏百分数、128Cs实验closedloop/106Ag排他四支柱均非本PRL的新测量或证明。 | source-factorization-and-overreach-correction | direct-original-and-scope-audit | printed172502-2 coreE2paragraph; printed172502-3 Eqs7–10; printed172502-4 EM/limitations | true |

[[qi-2009-135nd-particle-rotor-chirality]] ZH07-D24P-014–017的任务S与这里A有相同“core quarterrotation+交换”结构；须先将轴明确对齐，任务H参数及fullEM实现仍不等原数值例。[[signature-partner-bands]]、[[nuclear-chirality]]和[[signature-tip-shears-discrimination-contract]]保这个比较与真实experiment分别处理，新增needs_review:true，仅Day24无学分预习，不改原Day21/22credit。
