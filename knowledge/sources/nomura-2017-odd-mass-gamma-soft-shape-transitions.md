---
type: source
title: "Shape-phase transitions in odd-mass gamma-soft nuclei with mass A approximately 130"
aliases: []
created: 2026-07-05
updated: 2026-11-06
status: ai-draft
review_status: human-reviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Shape-phase transitions in odd-mass γ-soft nuclei with mass A ≈ 130"
authors: [K. Nomura, T. Nikšić, D. Vretenar]
journal: Physical Review C
year: 2017
volume: 96
pages: 014304
doi: 10.1103/PhysRevC.96.014304
arxiv: 1704.07101
language: en
canonical_source: doi:10.1103/PhysRevC.96.014304
zotero_item_key:
citation_key: nomura_2017_Shapephasetransitions
zotero_uri:
library_file:
raw_file: "raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf"
raw_sha256: 481E6A9E0F6B01E9C5DB5E2B06D9B350DBA0638393C7DA7F532C3040E9EFAEA9
archive_required: true
nuclei: [129ba, 131ba, 133ba, 135ba, 137ba, 127xe, 129xe, 131xe, 133xe, 135xe, 129la, 131la, 133la, 135la, 137la, 127cs, 129cs, 131cs, 133cs, 135cs]
reactions: []
experiments: []
models: [interacting-boson-model, covariant-density-functional-theory]
observables: []
methods: []
tags: [a130, gamma-softness, shape-phase-transition, odd-mass, ibfm, rhb]
---

# Nomura 等（2017）：A≈130 奇质量 γ-soft 核的形状相变

## Bibliographic Record

Physical Review C 96, 014304 (2017)，DOI `10.1103/PhysRevC.96.014304`。PDF 为 arXiv v2 版，共 13 页；正文至 p.12，p.13 为参考文献。

**2026-11-06来源重放补核：** [[ba135-ba137-source-energy-replay-boundary]]
从本原件Fig.5(c)和其原始矢量图先冻结135/137Ba各六条负宇称系列，
再与本任务固定kernel比较。排序一致，去掉共同11/2零点后最大差
分别1.896与3.128keV；这不是所有点1keV内的精确重放。原图没有19/2
或更高同自旋态，作者运行卡／波函数／电磁图重放仍未恢复。本条是本任务
核查结果，不改写原文理论数值或赋予作者新的异能态预测。

## Scope and Reading Depth

全文精读。重点核对粒子-芯耦合哈密顿量、RHB 到 IBM 的映射、Fig. 1-3 的偶偶芯势能面与谱学演化、Figs. 5-8 的奇 A 能级系统学、Figs. 13-15 与 Eqs. (12)-(15) 的四极形状不变量，以及结论中的模型限制。

## Summary

论文以相互作用玻色子-费米子模型（interacting boson-fermion model, IBFM）描述 `129-137Ba`、`127-135Xe`、`129-137La` 和 `127-135Cs`。偶偶芯的 `(β,γ)` 势能面、奇核子球形单粒子能和占据概率由 DD-PC1 相对论 Hartree-Bogoliubov（RHB）计算给出；玻色子-费米子耦合强度和部分电磁算符参数仍需按核素拟合。计算把 N≈76-78 附近的谱学变化和由 E2 矩阵元构造的有效 `γ_eff` 变化解释为近球形到 γ-soft 形状的二阶量子相变信号。

## Experimental or Theoretical Setup

- 偶偶芯使用不区分质子、 中子玻色子的 IBM；`s`、`d` 玻色子对应 `J=0,2` 价核子对；
- 奇核使用 IBFM，正宇称空间为 `3s1/2, 2d3/2, 2d5/2, 1g7/2`，负宇称空间为 `1h11/2`；
- RHB 使用 DD-PC1 能量密度泛函与有限程可分离配对力；
- IBM 参数由 RHB `(β,γ)` 势能面映射确定；单粒子能和占据概率由同一 RHB 框架给出；
- 玻色子-费米子耦合的 9 个参数以及 4 个 E2 算符参数仍通过选定低能数据调整；
- 本文没有报告新的实验数据，而是与既有能级、电磁跃迁和矩数据比较。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NOM17-1 | RHB 势能面给出 `130,132Ba` 在 `γ≈10°-20°` 附近的浅三轴极小且沿 γ 较软；`134Ba` 在小 β 区域呈平底并沿 γ 近乎平坦，`136Ba` 则在 `β≈0.1` 附近近球形。 | model-result | direct | PDF pp.5-6, Fig.1 | false |
| NOM17-2 | 对应 Xe 芯的势能面与 Ba 系统相似，但计算中 Xe 一般更 γ-soft；`132Xe` 被预测具有类似 `134Ba` 的 E(5)-like 平底势。 | model-result | direct | PDF pp.5-6, Fig.2 and text after Fig.2 | false |
| NOM17-3 | IBM 计算和经验系统学都在 N=72-78 给出相近的 `4+_1`、`2+_2` 能级；作者把这一结构作为有效势 γ-softness 的谱学特征。 | author-interpretation | direct | PDF p.6, Fig.3 and paragraph below | false |
| NOM17-4 | 奇 A Ba 计算中最低正宇称态的自旋在 N=79 由 `1/2+` 变为 `3/2+`，最低负宇称态在 N=77 由 `9/2-` 变为 `11/2-`；作者将其联系到偶偶 Ba 芯在 N=78 附近的相变。 | model-result | direct | PDF p.7, Fig.5 and discussion | false |
| NOM17-5 | 奇 A Xe 的最低正、负宇称态自旋变化分别出现在 N=77 与 N=75；奇 Z La、Cs 的正宇称低能级在 N=76-78 过渡区发生交叉，而负宇称序列较接近稳定的弱耦合 `ΔJ=2` 结构。 | model-result | direct | PDF pp.7-8, Figs.6-8 | false |
| NOM17-6 | 对 `135Ba`，完整 IBFM 比单一 `2d3/2` 轨道的 E(5/4) 极限更能反映经验能级和分支的复杂性；计算的 `1/2+_1`、`1/2+_2` 波函数分别以 `3s1/2`、`2d3/2` 成分为主。 | model-result | direct | PDF pp.8-9, Fig.9 and paragraph below | false |
| NOM17-7 | Fig.13 只对偶偶 `128-136Ba`、`126-134Xe` 的基态 `0+_1` 计算四极形状不变量：`β_eff` 随中子数平缓下降，`γ_eff` 分别在 N=78、N=76 出现峰值；作者将峰值与近球形到 γ-soft 的相变联系。该结论不自动适用于其他自旋态或奇 A 核。 | model-result | direct | PDF p.11, Eqs.(12)-(15), Fig.13 and paragraph below | false |
| NOM17-8 | 奇 A 计算没有普遍重复偶偶 `0+_1` 的同形峰值：Fig.14 对奇 N Ba/Xe 的 `1/2+_1, 3/2+_1, 5/2+_1, 11/2-_1` 给出态依赖变化，许多态在 N=79 明显改变，奇 A Ba 的 `3/2+_1,5/2+_1` 还在 N=75 变化；Fig.15 对奇 Z La/Cs 的 `3/2+_1,5/2+_1,7/2+_1,11/2-_1` 给出更明显信号，La 在 N=76 或 78、Cs 在 N=76 变化。 | model-result | direct | PDF pp.11-12, Figs.14-15 and surrounding text | false |
| NOM17-9 | 作者综合势能面、能级演化与 `γ_eff`，把 N=76-78 的变化解释为偶偶与奇质量系统中近球形到 γ-soft 的形状相变。 | author-interpretation | direct | PDF p.12, Concluding Remarks | false |
| NOM17-10 | 当前实现的主要限制是玻色子-费米子耦合必须逐核拟合；因此方法依赖已有低能数据，尚不是完全由 EDF 与配对相互作用决定的预测框架。 | model-result | direct | PDF p.12, final two paragraphs | false |

## Nuclear Structure Information

研究对象覆盖 A≈130 的四条奇 A 同位素链，并以偶偶 Ba、Xe 作为芯。论文的“相变位置”是模型和多种谱学量共同给出的区间，不是直接实验测得的单一临界中子数。

## Authors' Interpretation

作者认为奇核子的加入没有消除近球形到 γ-soft 的二阶形状相变，但会使不同宇称、不同自旋态的信号错开。基态自旋变化与 `γ_eff` 的非平滑变化可作为奇 A 系统中的候选量子序参量。

## Model Results

- DD-PC1 RHB 势能面确定偶偶芯的形状演化；
- IBM/IBFM 比较能级、E2/M1 跃迁以及谱学四极矩和磁矩；
- 四极形状不变量由有限组低能 E2 矩阵元构造，并映射为 `β_eff`、`γ_eff`；
- 经验谱的总体趋势得到较好再现，但部分非 yrast 能级、电磁量和组态混合存在明显偏差。

## Competing Interpretations and Limitations

- `γ_eff` 是由模型 E2 矩阵元导出的有效量，不是直接测得的静态 γ；
- Fig.13 的峰值只对应偶偶核 `0+_1`；奇 A Figs.14-15 中不同自旋态的 `γ_eff` 可在不同中子数增加或降低，不能套用统一峰值模板；
- 有限核中的二阶相变被平滑，中子数又是离散控制参数，因此“临界点”只能在核素区间内讨论；
- IBFM 粒子-芯耦合和部分电磁算符参数按数据拟合，限制了独立预测力；
- 模型空间未显式区分质子、 中子玻色子，也不包含所讨论价空间之外的复杂组态；
- 本文对既有实验数据的再现属于模型一致性证据，不应改写成相变已被单一观测直接证明。

## Extracted Pages

- Concepts: [[gamma-soft-deformation]]
- Models: [[interacting-boson-model]], [[covariant-density-functional-theory]]
- Nuclei: `129-137Ba`, `127-135Xe`, `129-137La`, `127-135Cs`
- Project: [[a130-high-spin-collective-modes-evidence-map]]

## Personal Notes

本文对后续 A≈130 奇核分析的关键价值是：γ-softness 的诊断必须同时保留偶偶芯势能面、奇粒子耦合和态依赖的 E2 不变量，不能把一个拟合 `γ_eff` 当成直接形状测量。

## 2026-11-06 原式、输入与重放补核

本次为 Agent 直接原件复核；不新增人工审核事件。所持 PDF 为
arXiv:1704.07101v2，页边版本日期为2017-07-08；标题块2021-11-21是编译日期，
不能作为新文章年份。v2 原始 TeX 的 `\date{\today}` 和版本身份已归档于
`raw/papers/gpt/query/20261105-nomura2017-input-audit/manifest.json`；
v1/v2比较位于 `raw/papers/gpt/query/20261106-nomura-invariant-version-audit/manifest.json`。

- Eqs.(12)–(15)，PDF p.11，明确只取 \(J'=J+2\) 中最低五态；三次和取绝对值。
  在一般非零J，这与完整电荷张量 \(q_2,q_3\) 的全通道闭合表达式不同。
  受限的完整多重态投影仍保持旋转不变，不能把它说成非标量。
- Eqs.(7)–(8)、PDF pp.4–5给 \(e_BQ_{\chi'=0.35}\) 和费米子E2项；
  相应芯 \(B(E2;2_1\to0_1)\) 定eB，137Ba \(11/2^-_1\) 矩定
  \(e_n=0.125\,eb\)。文中没有逐核eB、完整RME表或invariant生产程序；
  第III D节的通用Q并未另给与实际E2算符的生产者对应表。
- 负宇称129Ba的来源支持重建采用128Ba芯、NB=8；已查能量图子集约1keV一致。
  该结果不认证原作者完整代码，也不认证电磁图件。
- 同一重建使用打印电磁算符和原式求和，128Ba芯得
  \(\gamma_{\rm eff}=29.496^\circ\)，原Fig.13(b)向量图读值得8.975°。
  J=0处已经存在差别，因此不能以非零自旋的通道缺失解释该重放差别。
  v1/v2相关式、参数和图几何一致；实际算符对应仍未确定。

本任务的独立模型研究见 [[odd-ba-quadrupole-closure-and-spin-channel-redistribution]]。
它没有声称纠正原作者图件或恢复原作者运行输入。源版本、公式定位和重放差别的
逐项回执位于 `outputs/l4/20261105-ba129-controlled-pairing/` 的
`ibfm-input-review/`、`spin-invariant-algebra/` 与 `spin-invariant-source-replay/`。
