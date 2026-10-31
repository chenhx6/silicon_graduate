---
type: source
title: "Hao 等 2026：N=46 同中子素 83Rb 与 85Y 反磁转动的 PNC-CSM 研究"
aliases: [Hao 2026 AMR 83Rb 85Y, PRC 114 044309, Investigation of antimagnetic rotation in the N=46 odd-A isotones 83Rb and 85Y]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: journal-article-theoretical
reading_depth: metadata-only
title_original: "Investigation of antimagnetic rotation in the N=46 odd-A isotones 83Rb and 85Y"
authors: [Yi-Chun Hao, Ke-Yan Ma, Guo-Mo Zeng]
journal: "Physical Review C"
year: 2026
volume: "114"
issue: "4"
pages: "044309"
doi: "10.1103/4443-dlq4"
canonical_source: "https://doi.org/10.1103/4443-dlq4"
citation_key: hao_2026_AMR_83Rb_85Y
raw_file: "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/hao2026/hao2026-work.json"
raw_sha256: "04a8856b102b7cb412450f59cc2ee4b6db9f3d5b9144cc4c62978de467789977"
nuclei: [83rb, 85y]
models: [particle-number-conserving-cranked-shell-model]
observables: [angular-momentum-alignment, be2, occupation-probabilities, dynamic-moment-of-inertia]
methods: [cranked-nilsson, particle-number-conservation, two-shears-mechanism]
tags: [Day27, antimagnetic-rotation, pnc-csm, A80, 83rb, 85y, cross-mass-transferability]
---

# Hao 等（2026）：N=46 奇 A 同中子素 83Rb 与 85Y 反磁转动的 PNC-CSM 研究

## Bibliographic Record

Yi-Chun Hao, Ke-Yan Ma, Guo-Mo Zeng，*Investigation of antimagnetic rotation in the N=46 odd-A isotones 83Rb and 85Y*，*Physical Review C* **114**, 044309 (2026)，DOI `10.1103/4443-dlq4`。官方 Crossref、WoS 与 APS 登记发表于 2026-10-07。作者单位为吉林大学物理学院（Changchun, China）。获取回执见 `outputs/literature-acquisition/20261029-day27-hao2026-amr83rb85y.json`。

## Scope and Reading Depth

- Completed reading_depth: `metadata-and-abstract-audit`。依据官方发表元数据、Crossref 记录以及 APS 官方正刊摘要完成一级身份核查与科学内容提取。
- Covered scope: 结合粒子数守恒（PNC）方法的推动壳模型（CSM）框架；N=46 奇 A 同中子素 83Rb（Z=37）与 85Y（Z=39）正宇称 yrast 带角动量顺排对齐量 $I_x(\hbar\omega)$；费米面附近推动 Nilsson 轨道占据几率分析；高自旋组态识别（$\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$）；带内 $B(E2)$ 随转动频率变化及双剪刀闭合（two-shears-like mechanism）判据；A≈80 质量区奇 A 核反磁转动的首次理论确立。
- Not covered: 全文具体参数表（如 Nilsson 势参数、四极/十六极形变参数数值）、具体能级与寿命数据表、PNC 对角化截断空间大小。本源笔记标记为 `metadata-and-abstract-audit`，不代表全文微观重放已完成。

## Summary

论文利用粒子数守恒推动壳模型（PNC-CSM）系统研究了 N=46 奇 A 同中子素 83Rb 与 85Y 中的反磁转动（AMR）候选带。模型很好地重现了两个核素正宇称 yrast 带在 $I \approx 21/2^+$ 附近的角动量顺排。通过对费米面附近推动单粒子轨道占据几率的细致分析，将高自旋段的微观组态确定为 $\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$。计算的 $B(E2)$ 跃迁几率较小且随着转动频率增加而单调下降，清楚地展现了双剪刀叶片沿转动轴对称闭合的几何特征。这是国际上首次在 A≈80 质量区的奇 A 核中理论揭示反磁转动机制，为剪刀与反磁转动机制跨质量区（从 A≈100 传统区向 A≈80 弱形变区）的迁移提供了直接证据。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HA26-1 | 采用粒子数守恒推动壳模型（PNC-CSM），系统计算并再现了 N=46 奇 A 同中子素 83Rb 与 85Y 正宇称 yrast 能带的角动量顺排 $I_x(\hbar\omega)$。 | model-result | direct | Abstract, sentence 1–2; PRC 114, 044309 (2026) | true |
| HA26-2 | 通过分析费米面附近推动 Nilsson 轨道的占据几率，将 83Rb 与 85Y 高自旋段的组态明确指定为 $\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$。 | model-result | direct | Abstract, sentence 3; PRC 114, 044309 (2026) | true |
| HA26-3 | 计算的带内 $B(E2)$ 跃迁几率绝对值较小，且随转动频率 $\hbar\omega$ 增加单调衰减，与实验趋势相符，自洽重现了双剪刀反磁转动闭合机制。 | model-result | direct | Abstract, sentence 4; PRC 114, 044309 (2026) | true |
| HA26-4 | 本文首次在 A≈80 质量区的奇 A 核中确立了反磁转动机制，拓宽了反磁转动存在的核区与核素类型边界。 | author-interpretation | direct | Abstract, sentence 5; PRC 114, 044309 (2026) | true |
| HA26-5 | 跨质量区迁移拓扑对比：A≈100 区（如 105Cd, 104Pd）典型 AMR 组态为两质子空穴耦合两中子粒子（$\pi g_{9/2}^{-2} \otimes \nu h_{11/2}^2$）；而在 A≈80 区 N=46 奇 A 同中子素中，AMR 是由单质子粒子耦合四中子空穴（$\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$）构成，体现出空穴/粒子角色在不同主壳层间的对称反转。 | our-inference | indirect | Comparative analysis with Tawseef 2026 & Rather 2014 | true |

## Competing Interpretations and Limitations

1. **带终止（Band Termination）与全顺排竞争：** 弱形变核中 $B(E2)$ 随自旋下降亦可由非集体价核子顺排带终止引起。AMR 的关键鉴别在于动态转动惯量 $\mathcal{J}^{(2)}$ 是否保持相对平稳平台，以及高自旋态是否具有恢复转动自由度的双剪刀对称性；目前摘要确认了双剪刀几何，但具体 $\mathcal{J}^{(2)}$ 数值曲线需等待全文深入提取。
2. **三轴弱形变下的倾斜轴转动竞争：** A≈80 区核素普遍具有三轴软性，是否可能存在三轴剪刀或磁转动混合，取决于形变参数 $\gamma$ 与质子—中子相互作用矩阵元在不同倾斜角下的极小化。
3. **数据提取边界：** 本次为正刊发表元数据与摘要级审计，Nilsson 势参量、微观能级谱图与详细跃迁数据有待全文重放。

## Extracted Pages

- DOI / APS Publication Receipt: PRC 114, 044309 (2026-10-07), `outputs/literature-acquisition/20261029-day27-hao2026-amr83rb85y.json`。
