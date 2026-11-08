---
type: source
title: "Jouni Suhonen 2007 - From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory"
aliases: [Suhonen2007, Suhonen微观核理论, 从核子到原子核]
created: 2026-11-01
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory"
authors: [Jouni Suhonen]
publisher: "Springer-Verlag Berlin Heidelberg"
year: 2007
citation_key: "suhonen_2007_nucleons-nucleus-concepts"
pages: "654"
isbn: "9783540488590"
canonical_source: "J. Suhonen, From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory, Springer (2007)"
library_file: "raw/books/From nucleons to nucleus concepts of microscopic .pdf"
raw_file: "raw/books/From nucleons to nucleus concepts of microscopic .pdf"
raw_sha256: "4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c"
raw_storage_status: archived-local
archive_required: true
nuclei: []
reactions: []
experiments: []
models: [spherical-shell-model, bcs-quasiparticle, qrpa, sdi, tensor-algebra]
tags: [angular-momentum-coupling, tensor-operators, wigner-eckart-theorem, electromagnetic-transition-operators]
---

# Jouni Suhonen 2007 - From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory

## 专著概况与定位

芬兰于韦斯屈莱大学（Jyväskylä）Jouni Suhonen 教授所著的微观核结构教材，是国际上把**角动量 Racah 代数、球张量算符、Wigner-Eckart 定理与电磁跃迁几率计算**推导得最详尽、最适合作为手算与编程基准的实战宝典。

## 核心章节精要与物理内容

### Chapters 1–4: Angular Momentum & Tensor Operators（张量代数机器）
- **不可约球张量算符**：$[T_k, J_\pm]$ 的对易子关系。
- **Wigner-Eckart 定理的严格相位约定**：
  $$\langle j_f m_f | T_{\lambda \mu} | j_i m_i \rangle = (-1)^{2\lambda} \frac{C_{j_i m_i \lambda \mu}^{j_f m_f}}{\sqrt{2 j_f + 1}} \langle j_f || T_\lambda || j_i \rangle$$
  给出了单粒子与多体初末态约化矩阵元与 Clebsch-Gordan 系数分离的标准相位。

### Chapters 6–7: Electromagnetic Transitions（电磁跃迁微观理论）
- **跃迁几率与约化矩阵元**：
  $$T_{fi}(\sigma\lambda) = \frac{8\pi(\lambda+1)}{\lambda[(2\lambda+1)!!]^2} \frac{k^{2\lambda+1}}{\hbar} B(\sigma\lambda; I_i \to I_f)$$
  $$B(\sigma\lambda; I_i \to I_f) = \frac{1}{2I_i + 1} |\langle I_f || \mathcal{M}(\sigma\lambda) || I_i \rangle|^2$$
- **单粒子电多极与磁多极算符显式表达**：包含轨道磁矩 $g_l$ 与自旋磁矩 $g_s$ 的淬灭（Quenching）效应。

### Chapters 12–19: Quasiparticles, BCS & QRPA（准粒子平均场与组态混合）
- **Bogoliubov-Valatin 变换**：费米子算符向准粒子算符 $a_j^\dagger = u_j c_j^\dagger - v_j \tilde{c}_j$ 映射。
- **表面 $\delta$ 相互作用（Surface Delta Interaction, SDI）**：在紧凑模型空间下精确求解二体剩余相互作用矩阵元。


## Bibliographic Record

本书完整原著收录于 `book-suhonen-from-nucleons-to-nucleus.md` 对应原始路径，哈希与元数据已于前置卡固化。


## Scope and Reading Depth

覆盖全书核心章节与关键推导，结合在束谱学需求进行深度研学。

2026-11-08配对写作的有界核查：T10实际回读印刷399–404、408–411，
对应PDF412–417、421–424；总控核模型代数并重放有限pair占据空间控制。
本地页序在此不连续，印刷408–411也在PDF396–399重复出现，
PDF402–403为印刷414–415，PDF404回到印刷391。定位不能套固定偏移，
这次局部回读不追加全书通读声明。
§13.5.2/Eqs.(13.103)–(13.124)中的跨壳矩阵元与自能，
不能和只写成对散射的pair-only Hamiltonian混用。
原书 \(G_c=2\epsilon/(4\Omega-1)\) 保留其条件；
本任务不同H的推导及相位/粒子数边界见
[[a130-rewrite-bcs-convention-and-model-hamiltonian-boundaries-20261108]]。


## Summary

提供系统性核结构与实验数据分析理论框架。


## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SRC-1 | 本专著提供了自洽的核理论与实验分析基准。 | model-result | direct | Ch. 1 | false |


## Competing Interpretations and Limitations

唯象模型与微观第一性原理计算在适用范围与截断上存在边界差异。


## Extracted Pages

核心章节已提取并形式化为 Wiki 概念与方法合同。

## 2026-11-07 定向原件核读：E3 轨道选择规则

本次实际回读 printed pp.29–30、121–124、127–128，对应 PDF44–45、
136–139、142–143；不以这次局部核查补证全书阅读完成率。原 PDF 不改写，
SHA-256 沿用本页登记并在角向计算 provenance 中再次核对。

### Covered scope

Wigner–Eckart 定义、三角条件、电多极宇称、单粒子径向/角向分离，
以及 Table6.5 的 E3 例子。采用文中 Condon–Shortley 的 `ls` 耦合约定。

### Not covered

本次未恢复真实核的径向波函数、占据、有效电荷或多体跃迁密度，
没有由角向因子计算实际 B(E3)、八极势能面或静态形变。

| ID | 原件内容与本次用途 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH07-C01 | 秩 L 张量只有在初末态 j 与 L 满足三角关系时才能非零；E3 要求两态异宇称。 | experimental-criterion | direct | printed29–30 Eqs2.27–2.29；printed121 Eq6.18 | false |
| SH07-C02 | 单粒子电多极约化矩阵元分成宇称因子、3j 角向因子和径向积分；允许性不能给出径向重叠或多体相干强度。 | model-result | direct | printed122–124 Eqs6.22–6.23、6.32 | false |
| SH07-C03 | Table6.5 中 d5/2 与 p1/2、d3/2 与 f5/2 的 E3 元非零，给出 Δl=1、Δj非3 的明确反例；Δl=Δj=3 不是严格必要选择规则。 | model-result | direct | printed128 Table6.5；表值含振子径向积分，不是本任务纯角向因子 | false |

P0: none identified in this scoped unit。P1：公式相位受 `ls/sl` 与 CS/BR 约定影响，
本轮独立比较约化元的模方，并以 CG/Gaunt 展开和 6j 重耦合核对；
不能将只检验模方写成所有有符号相位已经认证。相关长期笔记为
[[octupole-orbital-eligibility-and-collectivity-boundary-20261107]]。

## 2026-11-08 弱算符与设计换算的定向回读

- T07及总控核印刷541–543/PDF552–554的Eqs.(17.63)–(17.74)，
  用于指定单体算符的Ikeda差和；不把总物理流或有限Q窗沿用为同一和。
- 设计阶段总控再核PDF44–45/印刷29–30及PDF133–136/印刷118–121，
  分别为Wigner–Eckart、率/寿命、算符单位和数值换算。
  本书不同部分的物理/印刷页偏移不同，不能用一个全书常数。
- Eq.(6.13)列基本常数，Eq.(6.14)才给实用率形式。
  以所印圆整数重建E2系数约1.2250×10⁹，对应MeV、e²fm⁴与s⁻¹，
  不是在该系数后再乘ħ或ln2。IC在本章明确不展开，不能冒引它为分支/ICC公式来源。
- 具体合同与单位边界见[[doctoral-thesis-high-risk-section-contracts-20261108]] F04。
  未重做完整电磁场量子化、原实验或其它未读章节。
