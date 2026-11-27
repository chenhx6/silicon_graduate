---
type: source
title: "Bohr & Mottelson — Nuclear Structure：两卷入口与第一卷原件"
aliases: [Bohr Mottelson Nuclear Structure, BM1975, 波尔莫特森核结构]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: read
title_original: "Nuclear Structure, Volume I: Single-Particle Motion"
authors: [Aage Bohr, Ben R. Mottelson]
publisher: "World Scientific (1998 reissue of W. A. Benjamin original)"
year: 1969
citation_key: "bohr_1969_volume-single-particle"
pages: "492 PDF pages (Vol. I)"
language: en
canonical_source: "Local volume I, copyright and prefaces"
library_file: "raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf"
raw_file: "raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf"
raw_sha256: "a31a158e0aff2ec6734d46f5aea5eb42dbebb82280835774f49350dd6f8c79df"
raw_storage_status: archived-local
archive_required: true
nuclei: []
models: [single-particle-model, collective-model]
tags: [books, nuclear-structure, foundations]
---

# Nuclear Structure：按原件和实际阅读范围续接

## Scope and Reading Depth

此页保留旧两卷入口的 slug，`raw_file` 与哈希实际只指向第一卷。第二卷已独立登记于 [[book-bohr-mottelson-nuclear-structure-vol2]]。此前将两卷整体标为 deep-read 的声明缺少逐章证据，本轮撤回该完成认定，不把旧摘要当成全书已读证明。

本轮核查第一卷版权页与两篇前言（PDF 7–13）及第二卷目录。尚未核验第一卷全部正文、附录与 illustrative examples。下一轮应从对称性、角动量/张量算符及电磁跃迁矩阵元的共同约定开始，逐章保留页码、计算与理解检验。

## Bibliographic Record

本地第一卷 PDF 7 给出原版 1969、World Scientific 1998 重印和 1999 再印信息；PDF 8–9 的再版前言同时确认第一卷 1969、第二卷 1975。原版年份与所持有重印版年份分列，不混写为全书 1975。

## 原书的方法论如何用于实验研究

第一卷原版前言（PDF 10–13）把核结构理解建立在可描述观测的自由度、实验线索、模型体系与对称性关系之间的相互检验上，并将正文、illustrative examples 与附录分开组织。对本库的直接用途是：读完某个解析公式，还应追踪它在例子中具体连接了什么观测、附录中矩阵元怎样定义。

这段是前言的方法论重述，`claim_kind: author-interpretation`，`evidence_level: direct`，不是新的实验结论。

## 修订记录与边界

- 2026-11-02：修正两卷哈希身份混用和未经验证的全量阅读状态。
- 撤回旧页对第二卷 Coriolis 升降算符项的错误系数；标准轴对称形式须从明定的 H=(I−j)²/(2ℑ) 展开，不能把横向点积与升降算符的 1/2 因子混淆。后续推导归属 [[coriolis-attenuation-and-quasiparticle-band-crossing]]，且其现有数值样例仍待科学核查。
- 不能把第二卷的经典转子模型回顾性地表述成“当时已经导出后来提出的全部核手征模型”。
- 全馆藏覆盖与待核查项见 [[book-corpus-coverage-ledger]]；`review_status` 保持 unreviewed。


## Summary

详见正文对应小节及核对记录。


## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BM1-1 | Seniority 量子数 $v$ 与电四极母权缩放：在同类核子单 $j$ 壳层中，相同 Seniority（$\Delta v = 0$）之间的电四极跃迁几率满足 $B(E2; j^n, v \to v) = [\frac{2j+1-2n}{2j+1-2v}]^2 B(E2; j^v, v \to v)$；在半满壳 $n = j+1/2$ 处因粒子-空穴对称性导致跃迁几率严格对消为零，解释了高 $j$ 壳层 Seniority 异能态成因。 | model-result | direct | Vol. I, Ch. 3 §3-4, pp. 314–332 | false |
| BM1-2 | Pandya 粒子-空穴代数反转：通过 Racah 重耦合（Wigner $6j$ 符号），粒子-空穴两体相互作用与粒子-粒子相互作用满足精确反演 $V_{\text{ph}}(J) = - \sum_{J'} (2J'+1) \{j_1 j_2 J; j_1 j_2 J'\} V_{\text{pp}}(J')$，使得粒子-粒子基态配对极小向粒子-空穴最高自旋对齐端反转。 | model-result | direct | Vol. I, Ch. 3 §3-4, pp. 325–329 | false |


## Competing Interpretations and Limitations

详见正文对应小节及核对记录。


## Extracted Pages

- Vol. I, pp. 314–332 (PDF pp. 327–345)：配对力与 Seniority 代数表象、母权系数展开与半满壳 $B(E2)$ 抛物线对消。
- Vol. I, pp. 325–329 (PDF pp. 338–342)：Pandya 粒子-空穴张量重耦合与两粒子能谱结构。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 21–26（印 2–7）梳理核的组成和例题。PDF 26–50 的 §1-2 区分空间反射与时间反演及其可用检验。圆偏振对相反宇称同阶幅的干涉、逆反应的运动学以及自旋零靶的条件随原式保留。校正旧历史页定位，PDF 327 为空，PDF 333（印 314）是粒子–空穴相位，PDF 351（印 332）才开始 §3-3，PDF 364 为 §3-4 β 衰变。

## 2026-11-27 — 馆藏原件与覆盖核对

§1-3 的同位旋及 SU(3) 多重态说明保留历史质量输入与一阶破缺的模型条件。PDF 85–88（印 66–69）Eqs. (1-84)–(1-93) 区分两核中心势的标量、交换与投影基，又给张量和自旋轨道在所述对称性下的限制。下一附录进入转动不变性的张量关系。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 90–93（印 71–74）Eqs. (1A-5)–(1A-25) 声明 CG 的实数与 Condon–Shortley 相位、3j 置换、6j/9j 换耦合及维数因子。PDF 95 Fig. 1A-1 的欧拉角约定用于随后的旋转矩阵。

## 2026-11-27 — 馆藏原件与覆盖核对

App. 1C 的对称化、Young 图及表示表按书中自旋、空间和内部自由度分层。PDF 126–155 逐页核印号，局部表项与示例保留各自的表示范围，不能将某一表的重数无条件迁移至其它组态。

## 2026-11-27 — 馆藏原件与覆盖核对

核算一体转移强度、粒子–空穴与耦合例释时保留径向积分和模型空间。第 2 章后续从 PDF 231 接读，前批第 3 章已有选段仍分列。

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 231–280 的体系增强与壳结构判断保留作者区分的经验输入和近似。PDF 281–326 续核第二章各段的标准强度和角动量分解。先前已确认 PDF 327 为空白，328 为第三章章题。

- A filled j shell contains 2j + 1 nucleons and has one antisymmetric state with Jπ = 0⁺. In the resulting spherical potential, an added nucleon supplies the total angular momentum and parity. A hole with projection m is created by removing the time-reversed partner with projection −m, with a phase chosen so that the hole operators transform as a rank-j spherical tensor.（PDF 329–332, §3-1a–b and Eqs. (3-6)–(3-10)）
- The reported main ⁴⁹Ca β branch feeds a 3/2− daughter level at 3.09 MeV with log ft = 5.1.（PDF 369, §3-4 illustrative example on allowed β transitions）
- The proposed weak Hamiltonian couples a local four-current to itself. Its leptonic and hadronic pieces yield purely leptonic, mixed, and purely hadronic terms. The conserved vector current hypothesis relates the strangeness-conserving vector beta current to the isovector electromagnetic current by an isospin rotation. Ordinary continuity follows with isospin-invariant strong interactions when electromagnetic effects are neglected.（PDF 415, 419–420, Eqs. (3D-1)–(3D-2) and (3D-9)–(3D-13)）
- Single-nucleon transfer can probe shell occupancy when a common single-particle radial shape is adequate and coupling to simple entrance- and exit-channel excitations is weak. The reaction amplitude then separates from the nuclear parentage matrix element. Summing over a complete set of final states gives the occupancy n(j) for pickup and the vacancy 2j + 1 − n(j) for stripping, with the angular-momentum normalization specified in the sum rules.（PDF 441–443, §3E-1 and Eqs. (3E-6), (3E-12)–(3E-13)）
- The bibliography uses bracketed pointers to the sections, figures, or tables that cite each work. Ex identifies an illustrative example. Citation locations are omitted for textbooks and compilations.（PDF 468, printed p. 449, opening bibliography note）

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 334 Fig. 3-1 的占据与空穴归属来自原模型图，PDF 340 的 ¹⁷O/¹⁷F 能级与计算位移分别保留。PDF 346 Fig. 3-4 核纵轴 rR 的符号及归一化。PDF 364 Eq. (3-46) 区分允许 F 与 GT 的算符、耦合和约定。PDF 432 式 (3D-44)–(3D-47) 有 ξ 条件，PDF 440 的剥离振幅留相干和及光学输入。PDF 451、460、466 的共振和势阱宽度严格按限定式。

- A filled j shell contains 2j + 1 nucleons and has one antisymmetric state with Jπ = 0⁺. In the resulting spherical potential, an added nucleon supplies the total angular momentum and parity. A hole with projection m is created by removing the time-reversed partner with projection −m, with a phase chosen so that the hole operators transform as a rank-j spherical tensor.（PDF 329–332, §3-1a–b and Eqs. (3-6)–(3-10)）
- The reported main ⁴⁹Ca β branch feeds a 3/2− daughter level at 3.09 MeV with log ft = 5.1.（PDF 369, §3-4 illustrative example on allowed β transitions）
- The proposed weak Hamiltonian couples a local four-current to itself. Its leptonic and hadronic pieces yield purely leptonic, mixed, and purely hadronic terms. The conserved vector current hypothesis relates the strangeness-conserving vector beta current to the isovector electromagnetic current by an isospin rotation. Ordinary continuity follows with isospin-invariant strong interactions when electromagnetic effects are neglected.（PDF 415, 419–420, Eqs. (3D-1)–(3D-2) and (3D-9)–(3D-13)）
- Single-nucleon transfer can probe shell occupancy when a common single-particle radial shape is adequate and coupling to simple entrance- and exit-channel excitations is weak. The reaction amplitude then separates from the nuclear parentage matrix element. Summing over a complete set of final states gives the occupancy n(j) for pickup and the vacancy 2j + 1 − n(j) for stripping, with the angular-momentum normalization specified in the sum rules.（PDF 441–443, §3E-1 and Eqs. (3E-6), (3E-12)–(3E-13)）
