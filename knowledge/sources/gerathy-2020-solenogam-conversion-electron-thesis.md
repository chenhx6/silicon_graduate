---
type: source
title: "Gerathy 2020 - Investigating nuclear structure through gamma-ray and electron spectroscopy with Solenogam"
title_original: "Investigating nuclear structure through γ-ray and electron spectroscopy with Solenogam"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: skimmed
authors: ["Matthew Stephen Michael Gerathy"]
year: 2020
institution: Australian National University
doi: 10.25911/5edf65740b697
canonical_source: "Australian National University doctoral thesis, 2020"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W3083623021.pdf
raw_sha256: dad32f09fa6ca67164661d755bf70f9218d176342c33cca998070f112567decf
raw_storage_status: archived-local
archive_required: true
nuclei: ["184Pt", "190Pt", "145Sm"]
tags: [conversion-electrons, E0, angular-correlation, nuclear-isomers, thesis]
---

# Gerathy 2020：Solenogam 的内转换测量及同核异能态

## Bibliographic Record

Matthew Stephen Michael Gerathy，Australian National University 博士论文，2020。
PDF 4 列仪器文章 *Nucl. Instrum. Methods A* **953**, 163136 (2020)，并将
$^{145}$Sm 论文记为提交稿。Crossref 的出版元数据把同一作者的高自旋
异能态论文登记为 *Phys. Rev. C* **102**, 044319，2020 年 10 月 16 日发表，
DOI `10.1103/PhysRevC.102.044319`。这里的数值来自学位论文，期刊版的数值和
版本差异待核。

## Scope and Reading Depth

原件 147 页。Codex 已覆盖 71 页，包括连续核读第 3–6 章，以及
定向核查 $^{145}$Sm 异能态及 Gammasphere 附录。模型主读和其余 76 页待补。
本文所引正文的印刷页为 PDF 页减 13。

## Summary

Solenogam 用 γ 与内转换电子的单谱和符合谱确定分壳转换系数。
铂的例子揭示混合比反演受弱电子线和角关联统计限制。钐的例子显示
相邻 γ 峰的核素身份和放置会改变异能态的自旋宇称解释。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| GER-1 | $q_K^2=I_K(E0)/I_K(E2)$。作者说明，充分精确的不同分壳转换系数可联合约束 $\delta^2$ 与 $q_K^2$。γ–γ 角关联也可约束 γ 多极混合，再用转换系数估计 $q_K^2$。 | analysis-method | direct-original-pages | PDF 32, 34–35, Eq. (3.16) |
| GER-2 | $^{184}$Pt 681 keV 跃迁的 K 电子峰可分，L、M 峰处于本底水平。作者给 $\alpha_L\le4.3\times10^{-2}$，与 K 系数合用仍留下很宽的混合参数范围。Table 6.2 的 $\delta$ 栏来自文献 [Xu92a]，部分 $\alpha_K$ 为本工作和既往数据的加权结果。 | measurement-and-source-dependency | direct-original-pages | PDF 80–82 Table 6.2, Figs. 6.9–6.10 |
| GER-3 | $^{184}$Pt 486–163 keV 级联将 163 keV 跃迁视为纯 E2，角关联曲线在原文约定下给出 $\delta=1.49$ 的最低点。作者称一倍标准差范围延伸到 $\delta\ge0.54$，图中 $\delta=5$ 仍在此范围内。Table 6.2 同线的 $+0.49(7)$ 来自文献，保留两个数值各自的来源。 | weakly-constrained-fit | direct-original-pages | PDF 80–81, 83 Table 6.2, Figs. 6.11–6.12 |
| GER-4 | $^{145}$Sm 合计时间谱的指数拟合给高自旋异能态 $t_{1/2}=3.52(16)$ μs。30/31 keV 双峰分别用符合谱回链 $^{145}$Sm 和校准源相关本底。作者由能量与强度平衡提出 8815→8785 keV 的 30 keV E1 分支，给 8815 keV 态 $49/2^+$ 候选；直接测得的是合计衰变时间。 | measurement-and-proposed-placement | direct-original-pages | PDF 93, 107–109 Figs. 7.15–7.16, 127 |
| GER-5 | PDF 107 的强度平衡段将 8785 keV 态写作 $47/2^+$，转换表、随后讨论和结论写 $47/2^-$。上下文的 30 keV E1 及 8815 keV 正宇称提议支持将此处标为疑似排印问题。 | internal-assignment-conflict | direct-original-pages | PDF 92 Table 7.2, 107, 109, 127 |
| GER-6 | 用 $^{152}$Eu 点源分别标定 HPGe 光峰效率与 Si(Li) 电子效率。单谱以效率修正后的峰面积比求转换系数。符合谱按探测器对组合效率，两 γ 的求和排除同一探测器，γ–电子则用两阵列的有效探测器组合。 | efficiency-and-coincidence-model | direct-original-pages | PDF 39–41 Fig. 4.4, 65–68 Eqs. (5.3)–(5.4) |
| GER-7 | 点源 Geant4 模拟在给定二阶角关联下得到单个 HPGe 与 Si(Li) 的 $Q_2$ 分别为 0.96 和 0.87。对两个读出分别取乘积，得到 γ–γ 的 0.9216 与 γ–电子的 0.8352，对应 Fig. 4.12 的 0.92、0.84。扩展源对 γ–电子衰减更明显。 | simulated-geometry-and-arithmetic-check | direct-original-pages | PDF 48–53 Eqs. (4.10)–(4.11), Figs. 4.12–4.13 |
| GER-8 | Eq. (3.27) 左侧为第 $i$ 壳的 $\alpha_i$，右侧纯 M1、E2 项均印 $\alpha_K$。按 Eq. (3.4) 和分壳定义，推广到 $i\ne K$ 时，M1、E2 基线都要换成 $i$ 壳值，E0 项仍用 $\Omega_i/\Omega_K$ 转移 K 壳归一。 | printed-index-inconsistency | direct-original-pages-and-definition-check | PDF 29–30, 32, 34–35 |
| GER-9 | Pt 衰变数据由 Au 母核的 β 衰变布居，停束后以模拟电子学的符合触发记录。$^{145}$Sm 使用数字单事例，在离线预排序后做反康普顿和符合选择。角关联按探测器对开角分别构造 γ–γ 矩阵。 | experimental-and-analysis-workflow | direct-original-pages | PDF 55–56 Table 5.1, 59–60, 62, 64–68, 70–75 |
| GER-10 | Argonne 的 Gammasphere 数据来自另一组实验。附录对 570/571 keV 双峰给出不同门谱及 396、540 keV 线的强度变化，支持分开处理两个近邻跃迁。474 keV 峰同时见于 929 与 685 keV 门。 | independent-coincidence-cross-check | direct-original-pages | PDF 134–137, Figs. A.1–A.5 |
| GER-11 | Table 6.2 的 681 keV 行给中心值 $\alpha_K=0.30$、$\alpha_K(M1)=0.0289$、$\alpha_K(E2)=0.0095$、$\lvert\delta\rvert=1.2$。代入 K 壳式复得 $q_K^2\simeq50.4$，与表的中心值 50 相符。该计算沿用文献混合比，仅复核中心值，表中区间未重算。 | arithmetic-check-of-derived-result | reproduced-from-printed-operands | PDF 34 Eq. (3.27), 80 Table 6.2 |

## Competing Interpretations and Limitations

- $^{184}$Pt 的 E0 强度依赖转换系数、文献混合比和相邻核的 $B(E2)$ 估计。
  两态形状混合与原文采用的带结构类比一起评估。此次核查的可观测量为强度、
  电子转换和角关联，缺少可与 $\delta$ 配对的实测 γ 线偏振输入。
- $^{145}$Sm 的 30 keV 能量放置依赖较弱的符合谱和强度口径，在原文保留
  候选层级。附录的第二套 γ–γ 数据约束级联放置，30 keV 指认和 3.52(16) μs
  半衰期仍按正文的 Solenogam 证据引用。
- Chapter 4 用只含二阶项的模拟展示 $Q_2$ 取法。PDF 68 另外报告实用的 HPGe
  $Q_4=0.75$，上述二阶计算无法单独检验它。Table 4.2 在 41° 和 90° 两组
  同时印有 G1、G4 组合。复用逐对角矩阵时需回查实际探测器编号和分组。
- Table 5.1 的 $^{184}$Au 母核反应印 $^{156}$Tb($^{30}$Si,5n)，Fig. 5.2 的
  PACE2 图则标 $^{159}$Tb。质量数闭合为 $159+30-5=184$，因此把表中 156
  登记为疑似排印差异，不用模拟激发函数替代原始机时记录。
- 该实验在分离后测长寿命态及其衰变。PDF 31 将初级布居近似视为随机取向，
  角关联由第一个辐射的条件探测定义。这一几何衰减和状态选择并不直接给出
  在束 P–γ 角分布拟合的 $\sigma/I$。

## Extracted Pages

- PDF 1、4、6：学位身份、出版关系、实验摘要。
- PDF 28–84：辐射与内转换、Solenogam、实验处理、Pt 衰变证据。
- PDF 92–93、107–109、126–127、134–137：Sm-145 指定原页与 Gammasphere 附录。
- 其余页面及所引原始文献保留为待核范围。
