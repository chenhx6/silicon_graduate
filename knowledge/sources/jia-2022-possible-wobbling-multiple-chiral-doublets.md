---
type: source
title: "Possible wobbling motion in multiple chiral doublets"
aliases: [Jia et al. 2022, wobbling in MchiD]
created: 2026-07-15
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: theory-article
reading_depth: deep-read
title_original: "Possible wobbling motion in multiple chiral doublets"
authors: [H. Jia, S. Y. Wang, B. Qi, C. Liu, L. Zhu]
journal: Physics Letters B
year: 2022
volume: 833
pages: 137303
doi: 10.1016/j.physletb.2022.137303
arxiv:
language: en
canonical_source: doi:10.1016/j.physletb.2022.137303
zotero_item_key:
citation_key: jia_2022_Possiblewobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2022_Jia et al_Possible wobbling motion in multiple chiral doublets.pdf"
raw_sha256: 02579162123510335140D160CABE4883F8C42273CF02EF1E55100242D3449614
nuclei: [a130-odd-odd-model]
reactions: []
experiments: []
models: [particle-rotor-model]
observables: [mixing-ratio, interband-e2-strengths, bm1-be2-ratio, angular-momentum-components]
methods: [azimuthal-angular-momentum-plot]
tags: [multiple-chiral-doublets, chirality, wobbling, particle-rotor, mixing-ratio, odd-odd]
---

# Jia et al. (2022): Possible wobbling motion in multiple chiral doublets

## Bibliographic Record

H. Jia, S. Y. Wang, B. Qi, C. Liu and L. Zhu, *Physics Letters B* **833**, 137303 (2022), DOI `10.1016/j.physletb.2022.137303`. The BibTeX key is uniquely matched as `jia_2022_Possiblewobbling`.

## Scientific Question and Motivation

The paper asks whether an excited pair of multiple chiral doublet (MchiD) bands can carry a wobbling motion of the triaxial core. It uses an ideal odd-odd particle-rotor model with pi h11/2 coupled to a nu h11/2 hole to calculate mixing ratios, E2 fractions, angular-momentum geometry and azimuthal plots. The result is a theoretical proposal, not a new spectroscopy observation.

## Scope and Reading Depth

Full six-page article read. Covered: PRM formalism, mixing-ratio and E2-fraction equations, calculated four-band level scheme and transition tables, angular-momentum components/orientations, azimuthal plots and the comparison with `130Ba` two-quasiparticle wobbling. Not covered: experimental verification of the proposed MchiD linking transitions or a non-ideal configuration survey.

## Summary

An ideal odd-odd PRM calculation predicts nearly pure-M1 intrapair links and more E2-rich interpair links in two MchiD pairs. The paper presents this as a possible future wobbling signature, not as an observation in a named nucleus.

## Method and Design Logic

The PRM treats a triaxial rotor with gamma = 90 degrees and a pi h11/2 times nu h11/2-hole configuration. Reduced E2 and M1 transition probabilities give delta and the E2 fraction delta-squared/(1+delta-squared). Expectations of squared proton, neutron and core components are converted to polar/azimuthal angles, and the total-angular-momentum distribution is plotted on the body-fixed sphere.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JIA22-1 | In the ideal PRM calculation, bands 1-2 form the lowest chiral doublet and bands 3-4 form an excited MchiD pair for the pi h11/2 times nu h11/2-hole configuration; this is a model level scheme, not an observed band assignment. | model-calculation | direct | PDF pp. 1-2, Fig. 1 and surrounding text | true |
| JIA22-2 | The mixing ratio delta for a Delta-I = 1 M1/E2 transition is defined from E2 and M1 matrix elements, and the calculated E2 fraction is delta-squared/(1+delta-squared). | method/formalism | direct | PDF p. 2, Eqs. (1)-(4) | true |
| JIA22-3 | The calculated intrapair Delta-I = 1 transitions in the lowest and excited chiral doublets have nearly zero E2 fraction and are therefore nearly pure M1 in this ideal model. | model-calculation / experimental-criterion | direct | PDF pp. 2-4, Table 2 and Fig. 2(a)-(b) | true |
| JIA22-4 | The calculated transitions linking the excited doublet to the lowest doublet have an E2 fraction of about 20 percent, mainly for specified even-to-odd and odd-to-even spin sequences, and are interpreted as relatively collective M1/E2 links. | model-calculation / author-interpretation | direct | PDF pp. 2-4, Table 1-2 and Fig. 2(c) | true |
| JIA22-5 | The model predicts that the interpair B(M1)out/B(E2)in and B(E2)out/B(E2)in ratios are of comparable scale to the `130Ba` two-quasiparticle wobbling example, although the E2 ratio is somewhat underestimated. | model-calculation / comparison | direct | PDF p. 4, ratios after Fig. 3 | true |
| JIA22-6 | In the component analysis, the proton, neutron and core angular momenta mainly align with the short, long and intermediate axes, respectively, for both doublet pairs; the excited pair has smaller intermediate-axis and larger short/long core components. | model-calculation | direct | PDF pp. 3-4, Fig. 3 | true |
| JIA22-7 | The calculated core orientation changes its polar angle by roughly 15 degrees between the lowest and excited doublets while retaining an azimuth near 45 degrees; the authors associate this with a one-dimensional wobbling motion of the core. | model-calculation / author-interpretation | direct | PDF pp. 3-4, Fig. 4 and text | true |
| JIA22-8 | At I = 17 hbar, azimuthal plots show maxima near theta about 40/140 degrees for the lowest pair and 60/120 degrees for the excited pair; the authors interpret both as static chirality, with the excited pair additionally carrying core wobbling. | model-calculation / author-interpretation | direct | PDF pp. 4-5, Fig. 5 and summary | true |
| JIA22-9 | The paper proposes that nearly pure intrapair M1 links and relatively E2-rich interpair links could provide a future mixing-ratio criterion for distinguishing chiral-doublet structure and possible wobbling in MchiD. | author-interpretation / future-proposal | direct | PDF pp. 3-6, discussion and Conclusions | true |
| JIA22-10 | The result is conditional on an ideal gamma = 90 degrees configuration, selected effective g factors, fixed MoI and PRM dynamics; it motivates future measurements of mixing ratios rather than establishing wobbling in any named nucleus. | limitation / future-proposal | direct | PDF pp. 1-2 and 5-6 | true |

## Analytical Reconstruction

The proposed evidence chain is: ideal PRM configuration -> calculated M1/E2 matrix elements -> E2-fraction pattern -> core/proton/neutron geometry -> azimuthal topology. The authors use the contrast between nearly pure-M1 intrapair links and E2-admixed interpair links as a possible wobbling fingerprint. Because every step is model-generated, the chain supports an experimental design question rather than a paper-evidence claim about an already observed MchiD nucleus.

## Competing Interpretations and Limitations

- The gamma = 90-degree configuration, fixed MoI and effective g factors are idealized model inputs.
- E2-fraction patterns require experimental mixing-ratio measurements and branch checks before use as a criterion.
- The `130Ba` comparison is not an independent validation of the odd-odd proposal.

## Assumptions, Limits and Reverse Tests

- The gamma = 90-degree ideal triaxial shape, fixed moments of inertia and effective g factors are not generic properties of all odd-odd MchiD systems.
- A reverse test should vary gamma, configuration, pairing and core inertia and check whether the E2-fraction separation survives.
- The comparison to `130Ba` is a scale comparison between calculations/available data, not an independent validation of the proposed odd-odd criterion.
- Mixing ratios from future experiments must be checked for sign, two-solution ambiguities and complete linking-transition coverage before use in the evidence gate.

## Related Knowledge and Project Relation

- Concepts: [[wobbling-motion]], [[nuclear-chirality]], [[multiple-chiral-doublet-bands]], [[triaxial-deformation]], [[chiral-doublet-bands]]
- Models: [[particle-rotor-model]], [[triaxial-particle-rotor-model]]
- Methods/observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[bm1-be2-ratio]], [[spin-coherent-state-map]]
- Projects/synthesis: [[nuclear-chirality-and-multiple-chiral-doublet-bands]], [[low-spin-wobbling-controversies]]

This theory source connects MchiD and wobbling questions, but it does not provide a new experimental source or settle whether any real MchiD bands wobble.

## Extracted Pages

- Model region: A approximately 130 odd-odd PRM (no specific experimental nucleus is claimed)
- Concepts: [[nuclear-chirality]], [[multiple-chiral-doublet-bands]], [[wobbling-motion]], [[chiral-doublet-bands]]
- Models/observables: [[particle-rotor-model]], [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[bm1-be2-ratio]]
- Project: [[nuclear-chirality-and-multiple-chiral-doublet-bands]]

## Human Review Triage

P0:

1. **JIA22-2/JIA22-4, PDF pp. 2-4, Eqs. (1)-(4), Tables 1-2 and Fig. 2.** Verify delta convention, E2-fraction equation, transition directions and the approximately 20 percent interpair E2 statement.
2. **JIA22-6/JIA22-8, PDF pp. 3-5, Figs. 3-5.** Check axis labels, angles and whether static-chirality/wobbling language is explicitly model interpretation.
3. **JIA22-9/JIA22-10, PDF pp. 4-6.** Verify that the proposed criterion is presented as future experimental work and is not promoted to an observed MchiD fact.

P1:

- JIA22-1/JIA22-5: check the model band labels and `130Ba` comparison scope.
- JIA22-3: verify the “nearly pure M1” wording against the plotted E2 fractions.

## Review Status

Page and all JIA22 claims remain unreviewed with `needs_review: true`. Human review is deferred until use: perform targeted claim review when this content is used for paper writing, a key project decision, synthesis finalization or a paper-level evidence pool.

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页：刊头、摘要、§1 引言、§2 理论框架及式(1)–(6)、§3 结果开头。
- 物理第3–4页：§3 能级方案、跃迁、与 ¹³⁰Ba 的比较和角动量分析。图1与表1–2在第3页，图2–3在第4页。第4页起为 §4 总结。
- 物理第5–6页：第5页图4–5、总结续、利益声明、致谢与文献[1]–[48]。第6页为文献[49]–[75]。
- 本次获取的具体覆盖：通读物理第1–6页的抽取文本，覆盖正文、式号、两表、五幅图的图注及参考文献清单。建议接受 Wiki 同版六页的文本覆盖，按下列定位修订条目后保留图面和公式字形的待核状态。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 在 A≈130 的理想奇奇核量子粒子转子模型中，作者采用 πh₁₁/₂ 粒子与 νh₁₁/₂ 空穴构型。按计算的带内 B(E2; I→I−2) 重排个别自旋点后，带1、2组成最低手征双带，带3、4组成激发手征双带。 | 模型设定与计算 | source-reported | 物理第2页 §2–3，第3页图1及图注。图中能级和箭头待核第3页。 | true |
| A17-2 | 作者由 E2/M1 矩阵元求 δ，再用 δ²/(1+δ²) 求 E2 分数。计算中两对双带各自内部的 ΔI=1 跃迁近于纯 M1，激发对连至最低对的 3→1、4→2 支路通常有较大 E2 混合，正文概述为约20%。表2的 3→1 支路在 I=19、21ℏ 时分别列 δ=−7.54、−2.04，约20%不能逐支路套用。 | 模型计算 | source-reported | 物理第2页式(1)–(4)及 E2 分数定义，第3页表1–2与图2讨论起段，第4页图2(a)–(c)及续文。曲线与异常自旋点待核第4页图2及第3页表2。 | true |
| A17-3 | 计算的价质子、价中子和核芯角动量主要沿短、长、中间轴。激发对的核芯中间轴分量较小，短轴和长轴分量较大。核芯方位角近45°，手征自旋区内激发对的极角约大15°。I=17ℏ 时正文给最低对和激发对的平均核芯极角约21°和33°，总角动量概率峰的极角分别约为40°/140°和60°/120°。 | 模型计算 | source-reported | 物理第2页式(5)–(6)，第4页图3与正文，第5页图4(a)–(b)、图5。核芯角与总角动量峰位待核第4–5页。 | true |
| A17-4 | 作者把两对双峰概率分布解释为静态手征，并把激发对的核芯取向变化解释为绕中间轴的可能摆动。作者提出未来可测量 δ，以检验双带对内近纯 M1、两对之间 E2 混合较大的判据。 | 作者解释与实验建议 | source-reported | 物理第4页 §3 末段及 §4，第5页图4–5和总结续。 | true |

计算固定 β=0.22、γ=90°、J₀=30ℏ²/MeV，质子和中子相对核芯的有效 g 因子差分别取 +0.7、−0.7。物理第2页称参数及数值细节沿用文献[49]，部分 B(M1) 和 B(E2) 数据指向该文献。第4页借文献[25–26]的 ¹³⁰Ba 双准粒子摆动数据作量级比较，并指出 E2 强度比略低估。只读到本篇对这些文献的引述及书目。

- 更正 JIA22-1、JIA22-3–4、JIA22-6–8 的图表页码。图1及表1–2在物理第3页，图2–3在第4页，图4–5在第5页。JIA22-9–10 的总结定位改为第4–5页，第6页只列参考文献。
- JIA22-4 将约20%注明为正文对常见跨对支路的概述，保留表2的 3→1 异常点。JIA22-7 区分自旋区总体约15°和 I=17ℏ 时21°至33°。
