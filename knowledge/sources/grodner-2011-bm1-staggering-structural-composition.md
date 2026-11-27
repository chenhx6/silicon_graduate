---
type: source
title: "Grodner 2011 - B(M1) staggering and structural composition of chiral bands"
aliases: [Grodner 2011 B(M1) staggering]
created: 2026-10-10
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Staggering of the B(M1) value as a fingerprint of specific chiral bands structure"
authors: [E. Grodner]
journal: "International Journal of Modern Physics E"
year: 2011
volume: 20
issue: 2
pages: "380-386"
doi: "10.1142/S0218301311017752"
arxiv: "1101.5907v1"
canonical_source: "https://doi.org/10.1142/S0218301311017752"
full_text_url: "https://arxiv.org/pdf/1101.5907v1"
downloaded_pdf_sha256: "716faa155028c0a6f6e34faca638c9ca76ec98ee7c69642a3d8186eb98190d67"
nuclei: [128Cs, 135Nd, 106Rh, 105Rh, 104Rh, 103Rh, 102Rh]
models: [symmetry-restoration, core-quasiparticle-coupling]
observables: [B(M1), B(E2), inband-strength, interband-strength, chiral-doublet]
methods: [R_yT-symmetry, phase-convention, transition-matrix-element-analysis]
tags: [chirality, M1-staggering, configuration-dependence, triaxiality, 128Cs]
citation_key: "Grodner_2011_BM1"
raw_file: "raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/grodner-2011-bm1-staggering.pdf"
raw_sha256: "716faa155028c0a6f6e34faca638c9ca76ec98ee7c69642a3d8186eb98190d67"
---

# B(M1) staggering and structural composition of chiral bands

## Bibliographic Record

- E. Grodner, “Staggering of the B(M1) value as a fingerprint of specific chiral bands structure,” *Int. J. Mod. Phys. E* **20**(2), 380–386 (2011), DOI 10.1142/S0218301311017752.
- Crossref verifies the DOI, author, journal, volume, issue, and pages. The arXiv record identifies version 1 as 1101.5907, posted 2011-01-31. The full seven-page text was read from the arXiv PDF; SHA-256 716faa155028c0a6f6e34faca638c9ca76ec98ee7c69642a3d8186eb98190d67.
- The article has no experimental table or new data figure. Its main line is a symmetry/transition-matrix-element argument and a model-dependent comparison to previously published data.

## Theory Argument and Evidence Type

The paper uses the combined time-reversal/π-rotation operator R_yT to define the chiral-symmetry basis and introduces a phase convention for matrix elements. In the strong-symmetry-breaking limit it expresses the inband transition amplitude through the real part and the interband amplitude through the imaginary part of a left-handed matrix element. The author argues that B(M1) staggering is not caused by chirality alone: it depends on the odd-particle configuration and the triaxial core structure, especially the single-j πh11/2⊗νh11/2−1 case.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GRODNER11-1 | The combined R_yT operator commutes with the nuclear Hamiltonian and relates partner eigenstates. | symmetry-argument | model | Eq. (1) | true |
| GRODNER11-2 | The electromagnetic transition operator M(σλ) is taken to commute with R_yT. | symmetry-argument | model | Eq. (19) | true |
| GRODNER11-3 | In the strong chiral limit, the derived inband transition amplitude reduces to a real-part combination of left-handed matrix elements. | model-result | model | Eq. (26) | true |
| GRODNER11-4 | In the strong chiral limit, the derived interband transition amplitude reduces to an imaginary-part combination of left-handed matrix elements. | model-result | model | Eq. (27) | true |
| GRODNER11-5 | The author states that corresponding B(M1) and B(E2) probabilities in partner bands should become equal in the strong-limit construction. | model-result | model | printed p. 6 | true |
| GRODNER11-6 | B(M1) staggering depends on structural composition, including the odd-nucleon configuration and triaxial core, rather than on chiral symmetry alone. | interpretation-boundary | model | printed p. 6 | true |
| GRODNER11-7 | The paper cites weak or absent B(M1) staggering in 104Rh and 135Nd as cases where partner-band structure differs from the specific Cs configuration. | interpretation | mixed | printed p. 6 | true |
| GRODNER11-8 | The cited core-quasiparticle model predicts that the staggering weakens rapidly when the triaxial deformation moves away from γ≈30°. | model-result | model | printed p. 6 | true |
| GRODNER11-9 | The conclusion describes B(M1) staggering as an additional property arising from the structural composition of a nucleus. | author-conclusion | interpretation | printed p. 7 | true |
| GRODNER11-10 | The 128Cs experimental input is cited to Grodner et al. 2006, so this article adds no independent 128Cs transition-strength dataset. | source-lineage | direct | Reference [1] | true |
| GRODNER11-11 | The 135Nd comparison is cited to Mukhopadhyay et al. 2007, so that comparison reuses the existing DSAM dataset. | source-lineage | direct | Reference [12] | true |

## Comparison Boundary

For 128Cs, this is a theoretical interpretation of the same published transition-strength evidence already represented by the Grodner 2006 DSAM source. For 135Nd, it cites the same 2007 lifetime/strength study used in the DAY10 continuity analysis. The paper does not add a new experiment, independent lifetime, or direct geometric measurement.

The author distinguishes two claims: partner-band strength equality in the strong chiral limit, and spin-dependent B(M1) staggering that requires additional structural conditions. The first does not make staggering a universal necessary indicator; the second does not make observed staggering sufficient proof of a particular geometry. Its descriptions of 135Nd and Rh are author/model interpretations, not new reanalyses of their raw spectra or covariance.

## Scope and Reading Depth

The seven-page arXiv article and Eqs. (1)–(27) were read; its model conditions, phase convention, and references to reused 128Cs/135Nd data were checked. It contains no new experimental table.

## Summary

The paper derives how in-band and interband B(M1) staggering depends on configuration and triaxial-core structure in the model. It limits staggering as a unique experimental fingerprint of chiral geometry.

## Key Results

- GRODNER11-1/2/3/4 define the R_yT-symmetry construction and matrix-element phase relations.
- GRODNER11-5/6/7/8/9 show configuration- and deformation-dependent staggering examples.
- GRODNER11-10/11 identify the reused 128Cs and 135Nd experimental datasets.

## Competing Interpretations and Limitations

This is a theoretical interpretation, not an additional experiment. Its examples reuse GR06 and MU07 inputs; changes in configuration or core deformation can weaken or remove the staggering without uniquely diagnosing geometry.

## Extracted Pages

- [[grodner-2006-128cs-chiral-doublet-lifetimes]]
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]
- [[chirality-wobbling-competition-evidence]]

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start": 1, "end": 2, "sections": "题名、摘要、第1节引言、第2节哈密顿量本征态与相位约定"}
- {"start": 3, "end": 4, "sections": "第3节对称破缺态、第4节对称恢复、第5节电磁矩阵元开头"}
- {"start": 5, "end": 7, "sections": "第5节矩阵元推导、强破缺极限及结构实例，第6节总结和全部参考文献"}
- 本次获取的具体覆盖：逐页读完物理第1–7页的提取文本，包括六节正文、式(1)–(27)的上下文和参考文献[1]–[13]。正文未见图、表或图注。公式的版面和精确字符尚待核对。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 按文中的对称性假设，反幺正算符 R_yT 将哈密顿量本征态映射到同一能量本征空间。对按文中方式选相的态，与 R_yT 对易的电磁算符给出实矩阵元。 | 模型推导 | source-reported | 物理第2页式(1)–(9)，第4页式(19)。第2页原式的括号和复共轭范围待查。 | true |
| A17-2 | 在作者取左右手态无隧穿、无重叠且 M1/E2 跨手性矩阵元为零的强破缺极限，带内振幅取左手态矩阵元的实部，带间振幅取其虚部并带相位约定下的符号。对应的两带跃迁概率在该极限下相等。 | 模型结果 | source-reported | 物理第5页式(24)–(27)及其前提，第6页首段。式(25)、(27)的符号和下标待查第5页。 | true |
| A17-3 | 作者转述既有寿命研究，称 ¹⁰⁴Rh 与 ¹³⁵Nd 的 B(M1) 交错很弱或未见，并称 ¹³⁵Nd 两条带的对应跃迁概率近似相等。 | 既有实验的转述 | source-reported | 物理第6页比较段，第7页参考文献[12]、[13]。 | true |
| A17-4 | 作者将随自旋变化的 B(M1) 交错归因于额外的组态和芯结构条件，讨论了同一 h₁₁/₂ 壳的质子粒子－中子空穴组态，并援引 CQPC 计算说明三轴形变 γ 偏离约30°时交错迅速减弱。 | 作者解释与所引模型 | source-reported | 物理第6页第5节末段，第7页第6节及参考文献[3]、[8]。 | true |

Cs 实验依据沿用 Grodner 等的参考文献[1]，Wiki 将其链接到 ¹²⁸Cs 寿命研究。¹³⁵Nd 和 ¹⁰⁴Rh 的比较分别来自[12] Mukhopadhyay 等与[13] Suzuki 等。选择规则和形变趋势分别借助[8]与[3]，原文献的数据和计算未纳入本次阅读。

- 将 GRODNER11-1 中“联系伙伴本征态”改为“映射至同能量本征空间”。式(1)–(4)本身未建立两个线性独立的伙伴态。
- 在 GRODNER11-3 至 GRODNER11-5 补明无隧穿、无重叠及跨手性 M1/E2 矩阵元取零的条件，把第6–7页定位标为 arXiv 物理页。
- 物理第4页式(17)–(18)的根号与归一化因子在提取中分行。引用精确公式前，连同第2页和第5页所列歧义核对原排版。
