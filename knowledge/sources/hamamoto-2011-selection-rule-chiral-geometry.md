---
type: source
title: "Hamamoto 2011 - Selection rule for electromagnetic transitions in chiral geometry"
aliases: [Hamamoto 2011 chiral transition selection rule]
created: 2026-10-10
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Selection Rule for Electromagnetic Transitions in Nuclear Chiral Geometry"
authors: [Ikuko Hamamoto]
journal: "International Journal of Modern Physics E"
year: 2011
volume: 20
issue: 2
pages: "373-379"
doi: "10.1142/S0218301311017740"
arxiv: "1102.0163v1"
canonical_source: "https://doi.org/10.1142/S0218301311017740"
full_text_url: "https://arxiv.org/pdf/1102.0163v1"
downloaded_pdf_sha256: "dafe5f8f25081661413c5c8e2dc0b1d44a48c12ec4f5169bd1b06b0facd1c205"
nuclei: [128Cs, 126Cs, 134Pr, 132La]
models: [particle-rotor-model, triaxial-rotor]
observables: [B(E2), B(M1), transition-selection-rules, chiral-doublet]
methods: [discrete-symmetry, electromagnetic-transition-matrix-elements]
tags: [chirality, selection-rules, B(E2), B(M1), model-limit, 128Cs]
citation_key: "Hamamoto_2011"
raw_file: "raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/hamamoto-2011-selection-rule.pdf"
raw_sha256: "dafe5f8f25081661413c5c8e2dc0b1d44a48c12ec4f5169bd1b06b0facd1c205"
---

# Selection rule for electromagnetic transitions in nuclear chiral geometry

## Bibliographic Record

- Ikuko Hamamoto, “Selection Rule for Electromagnetic Transitions in Nuclear Chiral Geometry,” *International Journal of Modern Physics E* **20**(2), 373–379 (2011), DOI 10.1142/S0218301311017740.
- Crossref verifies the title, author, journal, volume, issue, pages, and February 2011 publication record. The arXiv record identifies version 1 as 1102.0163, posted 2011-02-01.
- Locators below use the arXiv manuscript pagination, distinct from the Crossref journal pages 373–379. The arXiv PDF was downloaded to the run-local temporary directory and SHA-256 checked as dafe5f8f25081661413c5c8e2dc0b1d44a48c12ec4f5169bd1b06b0facd1c205. 早期临时下载记录保留；本轮核实frontmatter所列raw原件实际存在，12个physical页，哈希一致。正文1–7、TableI页8、captions页9、Figs1–3页10–12；不把7页正文误写为整个PDF页数。

## Scope and Reading Depth

The full article was read from the introduction through the particle-rotor construction, symmetry and transition-matrix-element derivation, numerical level scheme, experimental comparison, limitations, Table I, and Figures 1–3. The central result is a selection rule for one special odd-odd configuration. This is a model-derived rule and a comparison to previously reported transition data, not a new experiment.

## Model and Selection-Rule Derivation

The limiting model couples a triaxial core at gamma = 90 degrees to a proton particle and neutron hole in the same single-j shell. In the Lund convention the gamma value corresponds to -30 degrees, with the intermediate axis as quantization axis. The numerical example takes both valence angular momenta from h11/2 and uses a specified core moment of inertia and deformation.

The Hamiltonian is invariant under an operation A formed by a pi/2 or 3pi/2 rotation about the intermediate axis together with exchange of the valence proton and neutron. Its eigenstates therefore carry A = +1 or -1 even when chiral geometry is absent. Table I gives the allowed combinations of the rotor projection R3 and the proton-neutron exchange quantum number C for each A eigenvalue.

For collective-core E2 transitions, the model requires delta-C = 0 and delta-R3 nonzero; the gamma = 90 degree core makes delta-R3 = 0 E2 matrix elements vanish. The resulting selection rule is delta-A nonzero for a nonzero B(E2). For M1, the chosen particle-rotor operator and gyromagnetic factors make the matrix element approximately antisymmetric under proton-neutron exchange. In this construction, B(M1) for delta-A nonzero is predicted to be much stronger than for delta-A = 0.

When a chiral pair is formed, the left- and right-handed configurations combine into states with opposite A quantum numbers. In Figure 2(a), this gives allowed E2 transitions with delta-I = 1 and 2 and stronger M1 transitions with delta-I = 1; weaker delta-I = 1 M1 transitions are also allowed in the schematic. Figure 2(b) shows a particle-rotor calculation with approximate degeneracy of the two lowest bands over 13 < I < 24. Figure 3 illustrates why the authors expect chiral geometry only at moderate spin in this example: the angular-momentum vectors are coplanar at low spin and align toward the intermediate axis at high spin.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HM11-1 | The special model uses gamma = 90 degrees, equivalent to gamma = -30 degrees in the Lund convention when the intermediate axis is the quantization axis. | model-assumption | model | arXiv PDF p. 3, footnote 2 | true |
| HM11-2 | The particle-rotor model includes a core rotational Hamiltonian with the stated triaxial moment-of-inertia dependence. | model-definition | model | Eq. (2) | true |
| HM11-3 | The proton-particle potential in the same-j-shell limit is proportional to the difference of its squared angular-momentum components along axes 1 and 2. | model-definition | model | Eq. (3) | true |
| HM11-4 | The neutron-hole potential has the opposite axis ordering to the proton-particle potential in this limit. | model-definition | model | Eq. (4) | true |
| HM11-5 | The Hamiltonian is invariant under a combined intermediate-axis rotation and proton-neutron exchange, defining A = +/-1 eigenvalues independently of whether chirality is realized. | symmetry-argument | model | arXiv PDF p. 4, paragraph beginning “The total particle-rotor Hamiltonian” | true |
| HM11-6 | Table I lists the allowed R3 and C combinations for each A eigenvalue. | model-structure | model | Table I | true |
| HM11-7 | With only the collective-core E2 operator, nonzero B(E2) requires delta-A nonzero in this model. | model-result | model | Eq. (5) | true |
| HM11-8 | With the specified particle-rotor M1 operator and gyromagnetic factors, B(M1) for delta-A nonzero is predicted to exceed the delta-A = 0 strength. | model-result | model | Eq. (7) | true |
| HM11-9 | In the chiral construction, the two nearly degenerate partner states have opposite A eigenvalues. | model-result | model | Eq. (9) | true |
| HM11-10 | Figure 2(a) depicts the allowed E2 and stronger M1 transition classes and also shows weaker allowed delta-I = 1 M1 transitions. | selection-rule-summary | model | Figure 2(a) | true |
| HM11-11 | The numerical particle-rotor example has approximate partner-band degeneracy over 13 < I < 24. | model-result | model | Figure 2(b) | true |
| HM11-12 | The calculated angular-momentum vectors favor coplanar low-spin and high-spin aligned limits, leaving moderate spin as the candidate chiral region. | model-result | model | Figure 3 | true |
| HM11-13 | The author reports that measured electromagnetic properties of 128Cs and 126Cs are consistent with the proposed rules. | author-comparison | interpretation | arXiv PDF p. 7 | true |
| HM11-14 | The author summarizes the 134Pr in-band B(E2) values as differing by at least a factor of two. | author-summary | interpretation | arXiv PDF p. 6 | true |
| HM11-15 | The author reports that measured 134Pr M1 transitions violate the proposed rule. | author-summary | interpretation | arXiv PDF p. 6 | true |
| HM11-16 | The author cautions that deviations from the special model assumptions can modify the selection rule. | applicability-limit | interpretation | arXiv PDF p. 7 | true |
| HM11-17 | The 128Cs comparison cites Grodner et al. 2006, so the article adds no independent 128Cs transition-strength dataset. | source-lineage | direct | Reference [8] | true |
| HM11-18 | The numerical illustration uses A=130, Z=55, beta=0.3, and a core moment-of-inertia parameter of 8.55 hbar-squared/MeV. | model-input | model | arXiv PDF p. 5 | true |

## Evidence Classification and Limits

The symmetry operator and transition inequalities are model results. The statements about 128Cs, 126Cs, and 134Pr are the author’s comparisons to previously reported measurements; they are not measurements in this paper. The 128Cs comparison points to Grodner et al. 2006, represented in [[grodner-2006-128cs-chiral-doublet-lifetimes]]. This article does not report event-level spectra, a new lifetime, a new absolute B value, or a covariance matrix.

The rule is conditional on the special same-j proton-particle/neutron-hole configuration, gamma = 90 degrees, the selected collective E2 contribution, and the M1 operator and gyromagnetic assumptions. The paper explicitly says realistic deviations can modify the rule. Near-degenerate bands alone do not establish that its symmetry assignment applies. The authors also note that equal spin-parity had not been experimentally proved for many of the candidate pairs discussed.

For 134Pr, the factor-of-two B(E2) difference and M1-rule violation are retained here as the author’s summary of cited work, not as an independent remeasurement or a new numerical extraction. The source is useful as a conditional model discriminator and as a warning against treating near-degeneracy or any single B(M1)/B(E2) trend as sufficient evidence of chiral geometry.

## Wiki Relations

- The 128Cs experimental comparison is linked to [[grodner-2006-128cs-chiral-doublet-lifetimes]]; the 2003 level-scheme and DCO context is [[koike-2003-128cs-chiral-doublet-bands]]. These are experimental records, not extra calculations in this article.
- The model context is [[particle-rotor-model]] and [[triaxial-particle-rotor-model]]. The cross-source interpretation is tracked in [[chirality-wobbling-competition-evidence]].

## Knowledge Impact and Learning Decision

Decision: **limits**. The model provides a symmetry-based set of transition tests for a clearly specified odd-odd limit, and the author finds the reported 128Cs properties consistent with it. The 134Pr comparison is a counterexample within the same article. This makes electromagnetic transition patterns more useful as conditional, configuration-aware diagnostics, but it does not promote the 128Cs assignment to direct geometric evidence or add an independent experiment.

## Summary

This paper derives A-quantum-number E2/M1 selection rules in a restricted particle-rotor model and compares them with previously published 128Cs and 134Pr electromagnetic evidence.

## Key Results

- HM11-1–8 specify the model assumptions, A operator, and conditional E2/M1 selection rules.
- HM11-9–12 give model-state/geometry examples; HM11-13–15 summarize the authors’ comparison with 128Cs and 134Pr.
- HM11-17 records the data/reference lineage for the 128Cs comparison.

## Competing Interpretations and Limitations

The rules depend on the selected gamma=90° and same-j particle-hole model. Koike 2004 states the rule can hold without chiral geometry; the paper’s cited-data comparisons are not new measurements or direct A labels.

## Extracted Pages

- [[koike-2004-chiral-bands-selection-rules]]
- [[koike-2003-128cs-chiral-doublet-bands]]
- [[petrache-2006-near-degenerate-chiral-misinterpretation]]
- [[chirality-wobbling-competition-evidence]]

## Day19量化审计：A量子数电磁选择定则、交错反相与128Cs/134Pr实验判据

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiral_selection_rule_a_audit.py` 的 79 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-selection-rule-a-result-038.json`，旧草稿曾声称核准了 $\mathcal{A}$ 量子数（$\pi/2$ 转动 + 质子中子交换）的代数选择定则与实验判据边界；其过强结论已由下列superseded行及Day24逐项更正：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HM11-D19-1 | superseded by HM11-D24-001–006：保留special-model A对称和同A collective E2禁戒；撤回旧“ΔA改变是非零E2充要条件”、固定g系数平方等于actual B(M1)比/普适1000压制、固定period4足证实测交错、134Pr实测γ16–20及唯一破缺机制、该规则为所有实际手征核一般必要条件的认证。旧行完整保存在本run hamamoto-oldclaim-withdrawal-062.json；原脚本79项通过只覆盖其指定算术/硬编码，不补实验或波函数。 | superseded-source-and-quantifier-audit | direct-original-recheck-and-withdrawal | PDF4 Eq5–7; PDF7 limitations; PDF9 Fig2caption | true |


## Day24 checkpoint062：选择规则的逻辑、输入和奇A迁移

本轮先作Wiki-primed recall，root连续读同SHA原件physical1–12全部科学主线/TableI/captions，视觉核3–7方法/结论及10–12全部三图。没有新测量、谱数字化、实际本征态/波函数复现；未运行会覆盖历史输出的Day19 producer。旧HM11-1至18 review/needs_review保持，新行只作source self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HM11-D24-001 | Eq5是B(E2)非零蕴涵ΔA非零：同A严格零，异A只是对称允许。角动量三角规则、其它量子数、相干抵消仍可令异A矩阵元零；不能说充要条件。该结论限同single-j p-particle/n-hole、γ90、core-only E2。 | source-logical-implication-and-domain | direct-original-plus-logical-inference | physicalPDF4 Eq5 | true |
| HM11-D24-002 | A=±1在是否有chiral geometry时都可定义。Fig2带内ΔI2 enhanced/allowed是组织band的前提，由此A(I+2)=−A(I)；period4图例不是任意band排序/混合下的普适实验定理。 | symmetry-and-band-assignment-boundary | direct-original | physicalPDF4 A paragraph; physicalPDF5 Eq9; physicalPDF11 Fig2 | true |
| HM11-D24-003 | 正文Eq6示例gR=.5给p/n系数±.5与2.848/−2.792；实际Fig2caption另用gR=55/130=.423、gs=.6free。Eq7是近似强弱关系，未给实核所有态B比下界；两组gR不能混当同一个数值job。 | operator-input-and-strength-boundary | direct-original | physicalPDF4 Eqs6–7; physicalPDF9 Fig2caption | true |
| HM11-D24-004 | 将原印刷rounding的Eq6系数投影到h11/2 j=l+1/2并只改gR，exchange antisym/sym系数平方比由78000.51(.5)变80.03(55/130)；这是任务算符系数算术，不是作者actual Fig2或两实际B比，更不排除态矩阵元干涉/零值。 | task-source-coefficient-crosscheck | conditional-operator-algebra-not-rate | physicalPDF4 Eq6; physicalPDF9 Fig2caption | true |
| HM11-D24-005 | 134Pr B(E2)差异和M1规则不符是作者对Refs5/6的实验总结；本文未给实测γ16–20或唯一几何破缺机制。128Cs/126Cs支持来自Refs8/9，其中126Cs当时workshop/to-be-published；不是本篇新增独立dataset。 | experimental-attribution-and-unsupported-claim-withdrawal | direct-original | physicalPDF6–7 §III; physicalPDF7 Refs5–9 | true |
| HM11-D24-006 | 作者明确说实核偏离模型会修改规则，并将odd-A Nd中以aligned S-band angular momentum替代jp的选择规则列为should be worked out。不能把本odd-odd A标记直接移给MU07 odd-A三qp或133Ce单qp，也不据不满足此特殊规则普适否决手征。 | explicit-oddA-readiness-boundary | direct-original | physicalPDF7 final paragraph | true |

### 同一个M1算符也需核数值job

固定single-j h11/2且忽略跨j耦合时，P l P=(10/11)j、P s P=(1/11)j。令c_p,c_n为含−gR后的有效系数，算符相应部分为a(jp+jn)+b(jp−jn)，a=(cp+cn)/2、b=(cp−cn)/2。原页4rounded输入给gR=.5时a=.00254545、b=.71090909；仅按caption换gR55/130给a=.07946853而b不变。b²/a²分别78000.51和80.03。

它们衡量系数接近exchange-odd的程度，不是两跃迁B的比率。真实allowed/weak振幅另含不同态RME、coherent组分、能级binding与实际有效g，任何一项可有抵消。故原“>1000”旧算术即使成立也不认证全态或实核强弱下界；这里也不把80.03变成新的硬门。source的Eq7近似趋势与原Fig2数值支持仍保留。

### 主线与反证的影响

特殊A symmetry、实验近简并、L/R高I且无隧穿的理想等强、实际几何是四项不同命题。本文自身的共面/高I alignment图保有限spin窗口；p7为oddA规则留白，不能以别核一条选择模式给135Nd补完整EM核或排除所有替代解释。本次decision为revises旧强认证、supports有条件模型诊断、limits未经验证的迁移；不改变MU07的实验正支持。
