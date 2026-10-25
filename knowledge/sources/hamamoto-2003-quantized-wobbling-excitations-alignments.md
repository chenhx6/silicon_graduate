---
type: source
title: "Quantized wobbling excitations with alignments"
aliases: [Hamamoto and Hagemann 2003, quantized wobbling with alignment]
created: 2026-07-15
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
source_type: theory-article
reading_depth: deep-read
title_original: "Quantized Wobbling Excitations with Alignments"
authors: [Ikuko Hamamoto, Gudrun B. Hagemann]
journal: Physical Review C
year: 2003
volume: 67
pages: 014319
doi: 10.1103/PhysRevC.67.014319
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.67.014319
zotero_item_key:
citation_key: hamamoto_2003_Quantizedwobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2003_Hamamoto_Hagemann_Quantized wobbling excitations with alignments.pdf"
raw_sha256: 47E9858D2CD772B8383179A14FC8DF196F93E08F557E8FDB856A98EF5E1170B9
nuclei: [163lu]
reactions: []
experiments: []
models: [particle-rotor-model, bohr-mottelson-wobbling-model]
observables: [wobbling-energy, interband-e2-strengths, moments-of-inertia, triaxiality]
methods: []
tags: [wobbling, quantized-wobbling, alignment, 163lu, two-phonon, triaxiality]
---

# Hamamoto and Hagemann (2003): Quantized wobbling with alignment

## Bibliographic Record

Ikuko Hamamoto and Gudrun B. Hagemann, *Physical Review C* **67**, 014319 (2003), DOI `10.1103/PhysRevC.67.014319`. The BibTeX key is uniquely matched as `hamamoto_2003_Quantizedwobbling`.

## Scientific Question and Motivation

The paper asks how intrinsic high-(j) alignment changes the quantized wobbling spectrum and its electromagnetic fingerprints. It uses the TSD bands of `163Lu` as the motivating case, where TSD2 had been interpreted as one-phonon wobbling and TSD3 as a possible two-phonon band.

## Scope and Reading Depth

Day22实际重读并核验原件共5页（014319-1–5）；旧记录“eight-page”错误，以下locator已按实际页码更正。Covered: introduction, aligned particle-rotor Hamiltonian, limiting formulas (Eqs. 1-14), numerical spectra and B(E2) ratios (Figs. 1-4), parameter dependence and anharmonicity discussion, and conclusions. Not covered: independent remeasurement of the `163Lu` transitions or later microscopic calculations; cited experimental inputs are retained as background to this theory source.

## Summary

The paper derives an alignment-dependent quantized wobbling spectrum and tests B(E2) scaling and anharmonicity against previously reported `163Lu` bands. It is a theory/background source rather than a new experimental measurement.

## Method and Design Logic

The authors start from the Bohr-Mottelson wobbling Hamiltonian and add a highly aligned quasiparticle to the particle-rotor coupling. Alignment makes the condition that the total angular momentum lie close to the largest-moment-of-inertia axis easier to satisfy at lower spin. They derive a wobbling-energy expression containing both the inertial-frequency term and an alignment-dependent term, then diagonalize a simplified particle-rotor Hamiltonian for `i13/2` proton configurations and compare calculated energies and B(E2) ratios with reported `163Lu` TSD data.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H03-1 | In the aligned particle-rotor Hamiltonian, a large component of the intrinsic particle angular momentum along the principal rotation axis lowers the rotational cost of maintaining (I_1\approx I) and allows a wobbling-like regime to occur at lower angular momentum than in the no-alignment textbook limit. | model-result / author-interpretation | direct | 014319-2, Eqs. (6)-(11) and surrounding text | true |
| H03-2 | The derived wobbling excitation energy contains an inertial-frequency contribution and an alignment-dependent contribution; with constant (A_k), the phonon spacing can be written as a positive intercept plus a term proportional to (I), and larger alignment changes the spacing quantitatively. | model-result | direct | 014319-2, Eqs. (9)-(13) | true |
| H03-3 | For the limiting (A_1<A_2=A_3) case, the B(E2) ratio between an interband ΔI=1 transition and an in-band ΔI=2 transition depends steeply on the triaxiality parameter γ, especially for γ above roughly +20 degrees, and is relatively insensitive to the absolute moments of inertia. | model-result / experimental-criterion | direct | 014319-3, Eq. (14) and text below it | true |
| H03-4 | The `163Lu` interpretation assigns TSD1 to the yrast band, TSD2 to the one-phonon wobbling band and TSD3 to a candidate two-phonon band; this is an author/model interpretation based on similar alignments and moments of inertia together with interband B(E2) evidence, not a new observation by this theory paper. | author-interpretation / review-background | direct | PDF pp. 1, 3-4, introduction and Fig. 1 discussion | true |
| H03-5 | 作者尝试以 A1>A2 得到随 I 减小的 u1−f1 间隔，但不能同时复现间隔绝对量并保持 f2 的近似二声子结构，因而放弃该参数路线。所示 A1≲A2、固定 Ak 的计算改为拟合平均带间隔，并未复现实测 TSD2−TSD1 随 I 下降。f2 为模型中的二声子对应候选，不能把此计算写成成功复现全部能量趋势。 | model-result | direct | 014319-3, Sec. III and Fig. 1; 014319-5, Sec. IV | true |
| H03-6 | Calculated B(E2) ratios for TSD2 to TSD1 and TSD3 to TSD2 are compared with the reported `163Lu` ratios; the paper uses their magnitude and γ dependence as a practical wobbling diagnostic rather than treating a single ratio as a model-independent proof. | model-result / experimental-criterion | direct | 014319-4, Figs. 2-3 and captions | true |
| H03-7 | The observed TSD3-to-TSD2 B(E2) value is described as large and close to the scale expected from a two-phonon boson factor, but the calculated two-phonon transition strengths need not be exactly (2\) times the one-phonon strengths; anharmonicity and configuration mixing are explicitly retained as limitations. | review-background / model-result / limitation | direct | 014319-1, introduction; 014319-4, Fig. 3 and anharmonicity discussion | true |
| H03-8 | The model predicts that the energy distance between the two-phonon and one-phonon bands can be smaller than the one-phonon-to-yrast distance, but it does not reproduce the full observed spin dependence; small changes of moments of inertia with spin can strongly alter the wobbling energy. | model-result / limitation | direct | 014319-5, Eq. (15) and Sec. IV; 014319-3, Fig. 1 | true |
| H03-9 | The authors infer that the triaxiality of the strongly deformed `163Lu` bands is near +20 degrees and may increase slightly with spin, using the B(E2)-ratio comparison; this is a model-conditioned inference, not a direct shape measurement. | author-interpretation | direct | 014319-4, Figs. 2-4; 014319-5, Sec. IV | true |
| H03-10 | The simple calculation assumes (A_k) independent of spin even though pairing, deformation and other rotational effects should change them; this prevents a quantitatively complete account of the observed anharmonicity and energy evolution. | limitation / author-interpretation | direct | 014319-3, Sec. III; 014319-5, Sec. IV | true |

## Analytical Reconstruction

The paper turns alignment into a quantitative bridge between high-(j) structure and low-spin wobbling: alignment shifts the energy cost for rotation about the favored axis, while γ controls the interband E2 ratio. The evidence chain for `163Lu` therefore has three layers: reported band energies/transition strengths (reviewed background), particle-rotor calculations, and the authors' assignment of TSD1/TSD2/TSD3. The model does not by itself establish that the bands are harmonic phonons, because the same calculation shows anharmonic energy and transition-strength behavior.

## Competing Interpretations and Limitations

- The TSD1/TSD2/TSD3 phonon labels are inherited author/model assignments from the cited spectroscopy literature.
- Fixed rotational parameters and simplified pairing/deformation treatment limit quantitative use of the calculated energies and transition strengths.
- A full particle-rotor or microscopic calculation is a required reverse test for phonon-number scaling.

## Assumptions, Limits and Reverse Tests

- (A_k), pairing and deformation are simplified and effectively fixed over the calculated spin interval; a spin-dependent calculation is a required reverse test.
- B(E2) ratios depend on γ and transition selection; they should be combined with level identity, moments of inertia, alignments and, where available, lifetimes.
- The `163Lu` experimental comparisons are cited inputs, not independently remeasured here; do not use this source as an original experimental source.
- A reverse test is to compare the same energies and B(E2) ratios with a full particle-rotor/TiP calculation and with a cranking/signature-partner alternative, while checking whether phonon-number scaling survives.

## Related Knowledge and Project Relation

- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[triaxial-deformation]], [[signature-partner-bands]], [[angular-momentum-alignment]]
- Models: [[particle-rotor-model]], [[triaxial-rotor-model]], [[tilted-axis-cranking]]
- Observables: [[wobbling-energy]], [[interband-e2-strengths]], [[moments-of-inertia]], [[bm1-be2-ratio]]
- Projects/synthesis: [[low-spin-wobbling-controversies]], [[wobbling-vs-signature-partner]]

This is a theory/background source that sharpens the alignment-dependent phonon-energy and B(E2)-ratio criteria used in later wobbling claims. It does not replace the original `163Lu` spectroscopy papers and does not directly test `135Pr`, `187Au` or `131Xe`.

## Extracted Pages

- Nucleus: `163Lu` (cited experimental context)
- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[triaxial-deformation]], [[angular-momentum-alignment]]
- Models/observables: [[particle-rotor-model]], [[wobbling-energy]], [[interband-e2-strengths]]
- Project: [[low-spin-wobbling-controversies]]

## Human Review Triage

P0:

1. **H03-1/H03-2, 014319-2, Eqs. (6)-(13).** Verify the alignment term and the stated dependence of wobbling energy on (A_k), (I) and (j_1). This controls how later discussions of increasing/decreasing wobbling energy should be phrased.
2. **H03-3/H03-6, 014319-3, Eq. (14); 014319-4, Figs. 2-3.** Check the γ dependence and the precise numerator/denominator of each B(E2) ratio; a swapped ratio would reverse the inferred triaxiality trend.
3. **H03-4/H03-7/H03-8, 014319-1; 014319-3, Fig. 1; 014319-4, Fig. 3; 014319-5, Eq. (15).** Verify the TSD1/TSD2/TSD3 interpretation, the two-phonon comparison, and the limits from anharmonicity and energy-spacing evolution.

P1:

- H03-5/H03-9: verify which conclusions are parameter-fitted model results and which are author inference about `163Lu` triaxiality.
- H03-10: verify the constant-(A_k) and spin-dependent pairing/deformation caveat.

## Review Status

Page and all H03 claims remain unreviewed with `needs_review: true`. Human review is deferred until use: perform targeted claim review when this content is used for paper writing, a key project decision, synthesis finalization or a paper-level evidence pool.

## Day22 原件复核：轴编号、谱趋势与声子边界

本次是Codex self-audit；逐页实际读取014319-1–5，视觉核第2–5页的公式和四图；文件SHA-256与frontmatter一致。旧H03-5“复现下降趋势”与旧5–8页locator已更正，旧表述只作错误历史，不继承为证据。该论文没有新增独立实验。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H03-D22-001 | 原件为5页、编号014319-1–5；图1在第3页，图2–4在第4页，Eq. (15)及结论在第5页。 | source-identity-and-locator-correction | direct-original | 014319-1–5, page footers | true |
| H03-D22-002 | 对已展示的固定Ak模型，作者明确承认不能同时复现实测TSD2−TSD1下降和TSD3−TSD2明显压缩；A1>A2路线因绝对间隔与f2结构不能兼顾而放弃。 | model-limitation | direct-original | 014319-3, Sec. III; 014319-5, Sec. IV | true |
| H03-D22-003 | Eq. (14)比较同母态的带间ΔI=1 E2与带内ΔI=2 E2，极限A1<A2=A3下其γ依赖为比例于tan²(γ+30°)，不是一条连接线本身的E2/M1混合比，也不提供普适绝对比例系数。 | formalism-and-ratio-identity | direct-original | 014319-3, Eq. (14) | true |
| H03-D22-004 | 无alignment、A1<A2=A3的精确谱Eq. (5)给出相邻两声子间距之差−2(A2−A1)<0；有限I的非谐压缩不自动排除wobbling，但本文不能定量复现163Lu全部压缩与自旋演化。 | model-result-and-domain | direct-original | 014319-2, Eq. (5); 014319-5, Eq. (15) and Sec. IV | true |
| H03-D22-005 | 本文Bohr–Mottelson起始轴序为𝒥1>𝒥2>𝒥3、A1<A2<A3，alignment沿1轴；跨文献移植时应先映射“最大惯量轴/短中长轴”，不得把轴号1原样当Frauendorf2014的轴号1。 | notation-and-model-domain | direct-original | 014319-2, Eqs. (1)-(11) | true |

### Knowledge Impact and Learning Decision

Revises：撤回H03-5旧的能量趋势成功复现描述；支持alignment、E2比与声子非谐性的理论讨论，限制其作为163Lu完整能谱拟合或新独立实验的用途。下一步与[[frauendorf-2014-transverse-wobbling]]的HFA/完整QTR逐假设比较，再用原始163Lu实验与135Pr争议检查同一观测向量。


## Day22 checkpoint091 直接原件纠错

本次定向文本复核Fig.4讨论及结论；本地5页PDF。未新增实验、未重算非谐波函数。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H03-D22-R091-1 | 作者用有限自旋非谐性解释非零的f2→f1 ΔI=2 E2，并在Fig.4与TSD3→TSD1数据比较。Δn≈2在严格谐极限被抑制，不能把任意非零跨两声子退激当成对所有wobbling模型的排他否证。 | model-domain-and-transition-limit | direct-original | 014319-4, Fig.4 and paragraph beginning “For reference”; 014319-5, Sec.IV | true |

## Day22 checkpoint121：既有核心来源主线回读

2026-10-25T14:11:06.327994+08:00回读现有同SHA原件：014319-1–5 all mainline and references；本次重新视觉核014319-3 Eq14/parameter route；014319-4 Figs2–4/Delta-n≈2 paragraph。问题、方法、拟合输入、结果、局限和结论与当前原子条目核对，未发现需要新增科学结论的差额。原实现/完整Cov及外部引用缺口保持；没有新增实验、下载或human review。阅读记录见source-mainline-recheck-121.json。
