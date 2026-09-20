---
type: source
title: "Coupling of pairing and triaxial shape vibrations in collective states of gamma-soft nuclei"
aliases: []
created: 2026-07-05
updated: 2026-07-05
status: ai-draft
review_status: human-reviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Coupling of pairing and triaxial shape vibrations in collective states of γ-soft nuclei"
authors: [K. Nomura, D. Vretenar, Z. P. Li, J. Xiang]
journal: Physical Review C
year: 2021
volume: 103
pages: 054322
doi: 10.1103/PhysRevC.103.054322
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.103.054322
zotero_item_key:
citation_key: nomura_2021_Couplingpairing
zotero_uri:
library_file:
raw_file: "raw/papers/2021_Nomura et al_Coupling of pairing and triaxial shape vibrations in collective states of γ -soft nuclei.pdf"
raw_sha256: CF500A8CDCF4E192AE79DB7AC22A29EB2272034FE797D2E0EC350516810102C4
alternate_version_file: "raw/papers/gpt/high-spin-20260920/形变/2021_Nomura et al_Coupling of pairing and triaxial shape vibrations in collective states of γ.pdf"
alternate_version_sha256: "883850ece784ecf7fcf126859f1a37c59772b42a5fb5aeae575e0aeef6600087"
alternate_version_identity: "arXiv:2105.11997v1; same title/authors and seven-page preprint"
nuclei: [128xe, 130xe]
reactions: []
experiments: []
models: [interacting-boson-model, covariant-density-functional-theory, gamma-unstable-model, davydov-triaxial-rotor-model]
observables: []
methods: []
tags: [gamma-softness, triaxiality, pairing-vibration, interacting-boson-model, xe]
---

# Nomura 等（2021）：γ-soft 核中的配对与三轴形状振动耦合

## Bibliographic Record

Physical Review C 103, 054322 (2021)，DOI `10.1103/PhysRevC.103.054322`。PDF 正文与参考文献共 6 页。

## Scope and Reading Depth

全文精读，并视觉核对 Fig.1 的三维势能面投影、Fig.2 的激发 `0+` 态、Fig.3 的 γ 带与 γ-softness 比值、Fig.4 的低能谱和 B(E2) 比较，以及 Eqs.(1)-(5) 的玻色子数非守恒模型空间与映射。

## Summary

论文把 RMF+BCS 自洽平均场的 `(α,β,γ)` 势能面映射到允许玻色子数变化的 IBM 哈密顿量，以同时描述单极配对振动和三轴四极形状自由度。对 `128Xe`、`130Xe` 的示例计算表明，动力学配对主要降低激发 `0+` 态和其上能带，而显式三轴自由度对 γ 带能量与 γ-softness 诊断量更关键。论文以两个几何模型作参照：Davydov-Filippov（D-F）极限是在 `γ=30°` 有固定极小的刚性三轴转子；Wilets-Jean（W-J）极限是势能与 γ 无关的 γ-unstable 转子，并等价于 IBM 的 O(6) 动力学对称性。Fig.3 中 `E(2+_γ)/E(2+_g)` 与一个 B(E2) 比值分别更靠近 W-J 与 D-F 参考值，说明单一指标不能把真实核归入纯粹 γ-unstable 或 rigid-triaxial 极限。

## Experimental or Theoretical Setup

- RMF+BCS 使用 PC-PK1 泛函和可分离配对相互作用；
- 约束量为 `Q20`、`Q22` 与单极配对算符，分别定义 `β`、`γ` 和配对形变 `α`；
- 不区分质子和中子的配对振动自由度；
- IBM Hilbert 空间为 `(sd)^(n0-1) ⊕ (sd)^n0 ⊕ (sd)^(n0+1)`；
- 玻色子数非守恒项以 `s†+s` 在相邻子空间间耦合；
- 三体 `d` 玻色子项用于产生三轴极小并描述 γ 带；
- IBM 参数由 SCMF 势能面映射确定，转动项强度另按经验 yrast 转动惯量调整。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NOM21-1 | PC-PK1 RMF+BCS 势能面显示 `128Xe`、`130Xe` 均沿 γ 较软；`128Xe` 在 `β≈0.2, γ≈18°` 有浅三轴极小，`130Xe` 的全局极小约为 `β≈0.15, γ≈0°`。 | model-result | direct | PDF p.2, Fig.1 and first full paragraph | false |
| NOM21-2 | 两核在配对形变 α 方向也具有浅极小和较软势面；作者据此预期 γ 与配对涨落都会影响谱学性质。 | model-result | direct | PDF p.2, Fig.1 and discussion | false |
| NOM21-3 | 模型用 `n0-1, n0, n0+1` 三个玻色子数子空间及玻色子数非守恒项显式表示配对振动；三体 `d` 玻色子项用于获得三轴极小和 γ 带结构。 | model-result | direct | PDF pp.2-3, Eqs.(1)-(5) | false |
| NOM21-4 | 纳入 γ 与配对自由度总体降低 `0+_2,0+_3,0+_4` 的计算能量并改善与实验的比较；由于组态混合，不能逐态唯一拆分两种自由度的贡献。 | model-result | direct | PDF pp.3-4, Fig.2 | false |
| NOM21-5 | 模型空间不含约 3 MeV 以上可能重要的二、四准粒子态；作者认为这些组态会改变量化结果，但不会改变动力学配对降低激发 `0+` 态的定性趋势。 | model-result | direct | PDF p.3, final paragraph | false |
| NOM21-6 | 显式三轴自由度改善 γ 带成员能量，而与配对振动耦合反而提高计算 γ 带能量；作者把与实验的偏差归因于玻色子数子空间间组态混合导致的能级排斥。 | model-result | direct | PDF p.4, top-left paragraph and Fig.3(a,b) | false |
| NOM21-7 | Fig.3 以两种低能偶偶核几何极限作参照：固定 `γ=30°` 的刚性三轴 Davydov-Filippov（D-F）转子给出 `E2γ=E(2+_γ)/E(2+_g)=2.00`、`R3γ=B(E2;3+_γ→2+_γ)/B(E2;2+_g→0+_g)=1.78`；势能与 γ 无关的 Wilets-Jean（W-J）γ-unstable 转子（等价于 IBM O(6) 极限）给出 `E2γ=2.50`、`R3γ=1.19`。对 `128,130Xe`，完整 `(α,β,γ)` 计算的 `E2γ` 点位于 W-J 线附近并高于 2.50，而 `R3γ` 点位于两条参考线之间并向 D-F 的 1.78 靠近。两指标没有把核一致地归到同一纯极限。 | model-result | direct | PDF pp.1,4, geometric-limit definitions; Fig.3(c-f) and caption | false |
| NOM21-8 | `128Xe` 的 `0+_2` 波函数在 `[n0-1]` 与 `[n0+1]` 子空间中合计超过 90%，被作者解释为配对振动态；`130Xe` 的 `0+_2`、`0+_3` 也具有配对振动结构。 | model-result | direct | PDF p.5, paragraphs below Fig.4 | false |
| NOM21-9 | 完整模型总体再现两核低能谱和多数已有 E2 强度，但两核 γ 带均算得偏高，`128Xe` 的部分激发 `0+` 能量和弱 E2 跃迁存在明显偏差，非 yrast 实验 B(E2) 还受大误差限制。 | model-result | direct | PDF pp.4-5, Fig.4 and discussion | false |

## Nuclear Structure Information

本文只对偶偶 `128Xe`、`130Xe` 做示例计算。形状与配对软度均来自模型势能面；实验数据用于低能谱和 B(E2) 比较，不是新的测量。

## Authors' Interpretation

作者认为 γ-soft 或三轴核的低能 `0+` 激发态不能只用形状振动描述，动力学配对是必要自由度；同时，真实非轴核通常位于 γ-unstable 与 rigid-triaxial 两个几何极限之间。

## Model Results

- `(α,β,γ)` RMF+BCS 势能面被映射到玻色子数非守恒 IBM；
- 四种截断比较分别保留轴向 β、三轴 `(β,γ)`、配对加轴向 `(α,β)` 与完整 `(α,β,γ)`；
- 主要计算量包括激发 `0+` 态、γ 带能量、两个 γ-softness 比值和 B(E2)；
- 低能 yrast 带对动力学配对不敏感，激发 `0+` 结构更敏感。

## Competing Interpretations and Limitations

- 模型不区分质子、 中子配对坐标；
- IBM 映射空间只含 `s,d` 玻色子，较高激发的多准粒子组态缺失；
- 转动项强度用经验转动惯量调整，且约比 Inglis-Belyaev 值大 40%；
- 三体哈密顿量原则上要求 E2 算符包含相应高阶项，本文的比较受此近似限制；
- 两个 γ-softness 指标指向不同几何极限，不能挑选单一比值给核贴“刚性”或“完全 γ-unstable”标签。
- D-F/W-J 数值是本文用于 `128,130Xe` 低能偶偶 γ 带的几何模型参考线；不能不经奇粒子耦合、能带定义和模型前提核对，就直接移植为 `131Ce/133Ce` 奇 A 激发模式的分类阈值。

## Extracted Pages

- Concepts: [[gamma-soft-deformation]], [[gamma-rigid-deformation]]

## Alternate-version self-audit (2026-09-20)

- The supplied arXiv v1 was reread end-to-end; its equations, four model-space comparisons, Figs.1–4 and limitations agree with the canonical PRC source. No material claim change was found.
- HS-071 is an exact SHA-256 duplicate row of HS-070; neither adds an independent experiment or source.
- Models: [[interacting-boson-model]], [[covariant-density-functional-theory]], [[gamma-unstable-model]], [[davydov-triaxial-rotor-model]]
- Nuclei: `128Xe`, `130Xe`
- Project: [[a130-high-spin-collective-modes-evidence-map]]

## Personal Notes

本文最可复用的边界是：γ-softness 与 pairing softness 可以同时存在，且不同谱学量可能分别偏向不同几何极限；对形状背景层应保留多观测量和模型空间依赖。
