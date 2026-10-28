---
type: source
title: "Nomura et al. 2018：富中子奇质量钡同位素八极相关性与 sdf-IBFM 谱学"
aliases: [Nomura 2018 odd Ba octupole, sdf-IBFM 143-147Ba]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Signatures of octupole correlations in neutron-rich odd-mass barium isotopes"
authors: [K. Nomura, T. Nikšić, D. Vretenar]
journal: Physical Review C
year: 2018
volume: 97
pages: "024317"
doi: "10.1103/PhysRevC.97.024317"
citation_key: Nomura2018OddBaOctupole
citation_key_origin: agent-local-key-with-Crossref-metadata
citation_key_verified: 2026-10-28
canonical_source: "Nomura, Nikšić, and Vretenar, Phys. Rev. C 97, 024317 (2018); actual reading: arXiv1711.09587v2"
raw_file: "raw/papers/gpt/day26-20261028/nomura-2018-odd-ba-octupole-arxiv1711.09587v2.pdf"
raw_sha256: 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be
nuclei: [143Ba, 145Ba, 147Ba, 142Ba, 144Ba, 146Ba]
models: [RHB-DD-PC1, SCMF, sdf-IBM, sdf-IBFM]
observables: [E2, E3, excitation-energy, occupation-probability]
tags: [octupole, odd-mass, barium, sdf-IBFM, blocking-effect]
---

# 富中子奇质量钡同位素八极相关性与 sdf-IBFM 谱学

## Bibliographic Record

Crossref DOI 10.1103/PhysRevC.97.024317 与 INSPIRE 元数据完全一致。作者为 Kosuke Nomura、Tamara Nikšić 与 Dario Vretenar。实际读取文件为原作者在 arXiv 发布的完整预印本 `1711.09587v2 [nucl-th]`（共 11 页，包含完整的理论推导、参数表与谱学比较）；文件签名 `%PDF-1.5`，SHA-256 哈希值与本地归档一致。

## Scope and Reading Depth

对全文 11 页进行精读与系统学复算，覆盖：
1. 相对论 Hartree-Bogoliubov（RHB，DD-PC1 泛函与可分离配对力）在 $(\beta_2, \beta_3)$ 约束下的偶偶核核芯微观势能面；
2. 波色子相干态映射法确定偶偶核核芯 $sdf$-IBM 哈密顿量参数；
3. 广义 Seniority 方案下奇核子单粒子能量、占据数与波色子—费米子动力学、交换和单极耦合系数的解析映射；
4. $^{143,145,147}\text{Ba}$ 激发谱、奇偶宇称能带、$f$-波色子数 $\langle \hat{n}_f \rangle$ 与单粒子轨道成分分解；
5. $B(E2)$ 与 $B(E3)$ 绝对跃迁几率预报及奇中子阻塞机制物理图像。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| NO18-D26-001 | 偶偶核核芯 $sdf$-IBM 参数（$d$、$f$ 玻色子单能与四极/八极相互作用）完全由微观约束 RHB 势能面映射确定，保留了 $^{144,146}\text{Ba}$ 的 $\beta_3$ 软势能特征。 | model-method | direct-original-preprint | model-calculation | PDF2–3 Sec.II, Table I | true |
| NO18-D26-002 | 奇中子价空间涵盖中子 $N=82–126$ 主壳（$3p_{1/2}, 3p_{3/2}, 2f_{5/2}, 2f_{7/2}, 1h_{9/2}, 1i_{13/2}$），其单能与球形占据几率 $v_j^2$ 均由零形变约束 SCMF 严格微观确定。 | calculation-input | direct-original-preprint | model-calculation | PDF3 Sec.II, Table II | true |
| NO18-D26-003 | 玻色子—费米子耦合项由广义 Seniority 方案解析构造，耦合常数正比于占据因子 $(u_i u_j - v_i v_j)$ 或 $(u_i v_j + v_i u_j)$，将多参数微观约束至渐变唯象空间。 | model-formulation | direct-original-preprint | model-calculation | PDF3–4 Eqs(7)–(12) | true |
| NO18-D26-004 | 在 $^{143,145,147}\text{Ba}$ 中，奇中子主要占据 $\nu 1h_{9/2}$ 与 $\nu 2f_{7/2}$，基态与低激发带的八极玻色子数 $\langle \hat{n}_f \rangle \approx 0.000$（如 $^{145}\text{Ba}$ 基态 $5/2_1^-$ 中 $1h_{9/2} \otimes sd$ 占比达 $92\%$），未展现低能八极凝聚。 | model-result | direct-original-preprint | model-calculation | PDF6–8 Tables V, VII, IX | true |
| NO18-D26-005 | 八极集体激发在奇核中被推迟至较高激发能（$E_x > 0.7 - 1.2\text{ MeV}$），表现为带头态包含显著 $f$-玻色子成分（如 $^{145}\text{Ba}$ 的 $11/2_1^+$ 与 $15/2_4^-$），并向基带发射大 $B(E3)$ 跃迁。 | observable-prediction | direct-original-preprint | model-calculation | PDF7 Sec.IV.B, Table VI | true |
| NO18-D26-006 | 奇中子阻塞效应抑制了 $\nu(2f_{7/2} \leftrightarrow 1i_{13/2})$ 虚拟粒子—空穴相干散射，导致奇质量钡无法形成类似锕系奇核（如 $^{225}\text{Ra}$）的低激发近简并交替宇称双重态。 | physical-mechanism | direct-original-preprint | author-synthesis | PDF8–10 Sec.V | true |

## Summary

Nomura 等人基于相对论密度泛函与 $sdf$-IBFM 模型，系统分析了富中子奇质量钡同位素（$^{143,145,147}\text{Ba}$）的低能能级结构与跃迁速率。研究确立了由于奇中子占据 $\nu 1h_{9/2}$ 等单粒子轨道引发的泡利阻塞效应，使得偶偶核中显著的八极集体性在奇质量核的基态附近完全被抑制，真正的八极声子态被推移至 $0.7 - 1.2\text{ MeV}$ 以上的高能区。

## Competing Interpretations and Limitations

早期唯象几何转子模型曾假定如果偶偶核具备八极形变，邻近奇核必然在基态附近展现出反射不对称的宇称双重带。实验上 $^{145}\text{Ba}$ 基态附近缺失宇称双重态曾被部分观点怀疑为偶偶核八极增强的证伪反例。Nomura 2018 的微观分析澄清了这一争议：偶偶核的 $\beta_3$ 软性与奇核的基态八极淬灭在微观上完全兼容，奇核子的单粒子阻塞足以解耦基态与八极自由度。

## Model Dependence

模型依赖于 DD-PC1 密度泛函的单粒子能级排序、经验确定的配对相互作用强度、以及 $sdf$-IBM 相干态映射在软势能面上的半经典近似。此外，对于高自旋态未包含推转含时效应或多准粒子破对耦合。

## Knowledge Impact and Learning Decision

`supports` 奇质量原子核中八极关联被奇核子占据选择性阻塞的微观物理机制；`limits` 将偶偶核的大 $B(E3)$ 唯象外推为奇质量同位素基态必有宇称双重态的简单推论；为跨质量区核结构系统学提供关键的奇偶差分判据。

## Extracted Pages

- [[octupole-correlation]]、[[octupole-deformation]]、[[octupole-mr-amr-evidence-gradient]]、[[cross-mass-region-collective-mode-transfer-boundaries]]。

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[bernard-2016-144ba-sccm-octupole]]
- [[gaffney-2013-pear-shaped-rn-ra]]

## Review Status

Codex source self-audit；所有新 claim 保持 needs_review: true。
