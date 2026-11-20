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
reading_depth: read
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
PDF 4 和 142 列仪器文章 *Nucl. Instrum. Methods A* **953**, 163136 (2020)，
DOI `10.1016/j.nima.2019.163136`。前言将
$^{145}$Sm 论文记为提交稿。Crossref 的出版元数据把同一作者的高自旋
异能态论文登记为 *Phys. Rev. C* **102**, 044319，2020 年 10 月 16 日发表，
DOI `10.1103/PhysRevC.102.044319`。这里的数值来自学位论文，期刊版的数值和
版本差异待核。

## Scope and Reading Depth

原件 PDF 1–147 已由 Codex 核读和对账。第 1–9 章及 Gammasphere 附录按正文
证据记录，封面附页和书目按书证处理。未收到可验收的 Gemini 回执。
本文所引正文的印刷页为 PDF 页减 13。书目定位不授予所引原文的阅读覆盖。

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
| GER-12 | 1105 keV 态的 12.1(18) ns 是以 945 与 1331 keV 两条馈入线之和作门、和 1105 keV 退激作时间差，由 prompt 高斯与指数卷积拟得的半衰期。12.9(12) ns 是与文献 13.5(15) ns 的加权采用值。 | measurement-and-adopted-average | direct-original-pages | PDF 96–98, Figs. 7.6–7.7 |
| GER-13 | 396 keV 峰在 458、313 keV 门中可见，在从上方馈入原 6756 keV 态的 1047 keV 门中较弱。570/571 keV 两个门的 396、540 keV 峰强不同，作者据此把两条级联并列，并用 714 keV 及能量和约束新增 6931 keV 态。 | level-placement-evidence | direct-original-pages | PDF 97–103, Figs. 7.8–7.13 |
| GER-14 | 对 3921→3483 keV 的 438 keV 支路，作者据 1105 keV 门内较弱的 K 电子峰改指为 E1，从而提出 3921 keV 态为 $27/2^-$。Fig. 7.14 图内两个 M1 对照峰标 364、481 keV，图注把后者写成 438 keV。 | multipolarity-reassignment-and-caption-conflict | direct-original-pages | PDF 104–106 Fig. 7.14, Table 7.4 |
| GER-15 | 截断的 KShell 计算以 $^{132}$Sn 惰性核芯运行，文中组态另以 $^{146}$Gd 亚壳闭合作参考。3921 keV $27/2^-$ 态的匹配能量为 3961 keV，最大组态占 36.9%。作者将 8815 keV 异能态解释为变形的芯中子激发，这一自由度在该球形计算空间外。 | model-and-truncation-boundary | direct-original-pages | PDF 113–115 Table 8.2, 120–123 Figs. 8.7–8.8 |

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
- $^{145}$Sm 的已置位支路在 5029 keV 以上约缺少 40% 的总通量
  （PDF 120–121，Fig. 8.7）。作者把未置位谱线列为可能贡献。
  30 keV 线的 $\alpha_{\rm tot}<3.2$ 是强度平衡约束。Table 7.2 的
  61(3) 光子相对强度使用 E1 的理论 $\alpha_{\rm tot}=1.27(10)$ 回推，
  只能视为与 E1 假设相联系的采用值（PDF 90、107）。
- 第 8 章的跨核比较保留参照核数据。变形芯激发的解释借用了 $^{147}$Gd
  的四极矩和 $g$ 因子以及强 E2 跨越支路的上限。对 $^{143}$Nd 4076 keV
  态反转宇称的建议仍属系统学推断（PDF 122–125）。
- PDF 16 将 $\cos(3\gamma)$、$\sin(3\gamma)$ 写入形状分量，却同时以
  0°/60° 标长椭/扁椭并以 30° 图示三轴。若按印式，30° 的两个分量为
  $(-\beta_2,0)$，是轴对称的，和 PDF 17 Fig. 2.1 不一致。
  该印式不能用于重建本章图形。
- 第 9 章的探测器位置、焦斑测量与快定时升级，及其它同中子素的候选态，
  按作者的研究设想记录（PDF 128–133）。

## Extracted Pages

- PDF 1–13：学位身份、前言、摘要、目录及图表目录。
- PDF 14–27：研究动机、结构导论与形状示意。
- PDF 28–84：辐射与内转换、Solenogam、实验处理、Pt 衰变证据。
- PDF 85–137：Sm-145 衰变、壳模型讨论、结论及前瞻、Gammasphere 附录。
- PDF 138–147：书目。半衰期历史值来源 [Fer93] 在 PDF 141，
  铂混合比/转换数据的 [Xu92a]、[Xu92b] 在 PDF 147。
- 其余页面及所引原始文献保留为待核范围。
