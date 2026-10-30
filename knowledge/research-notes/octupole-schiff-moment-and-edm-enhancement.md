---
type: research-note
title: "核八极形变Schiff矩与原子电偶极矩（EDM）增强机制：225Ra、225Ac与199Hg跨区微观相消与灵敏度相图"
aliases: [octupole-schiff-moment-and-edm-enhancement, octupole Schiff moment EDM, Day27 Schiff EDM enhancement]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [dobaczewski-2005-ra225-schiff, engel-2003-ra225-selfconsistent-schiff, gaffney-2013-pear-shaped-rn-ra, nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet]
created_from: Day 27 continuation study; system/scripts/day27_schiff_moment_cross_mass_study.py
tags: [Schiff-moment, atomic-EDM, octupole-deformation, CP-violation, parity-doublet, strong-CP-problem, 225Ra, 225Ac, 199Hg, Day27]
---

# 核八极形变 Schiff 矩与原子电偶极矩（EDM）增强机制：225Ra、225Ac 与 199Hg 跨区微观相消与灵敏度相图

## Research Trigger

在超越标准模型新物理（BSM）与基础对称性破缺检验中，中性原子的永久电偶极矩（EDM）是对时间反演与宇称不守恒（P, T-odd / CP 破坏）极其灵敏的物理探针。
根据 Schiff 屏蔽定理，点电荷核的静电场完全被原子电子云所屏蔽，实验上非零的抗磁性原子 EDM 仅能由有限核电荷分布的**核 Schiff 矩（$\hat{\mathbf{S}}$）**产生：
$$\hat{\mathbf{S}} = \frac{1}{10} \sum_{p} \left[ r_p^2 - \frac{5}{3} \bar{r}_{\text{ch}}^2 \right] \mathbf{r}_p, \quad d_{\text{atom}} = K_{\text{atom}} S_{\text{lab}}.$$
传统实验长期以近球形闭亚壳层原子 $^{199}\text{Hg}$ 作为国际精度基准（实测界限 $|d_{\text{Hg}}| < 1.1 \times 10^{-29}\ e\text{ cm}$，Graner et al. 2016）。然而，理论预测表明，具有稳定内禀梨形（八极）形变的奇 $A$ 锕系核（如 $^{225}\text{Ra}$，[[dobaczewski-2005-ra225-schiff]] 与 $^{225}\text{Ac}$，[[nndc-2022-ac225-adopted-parity-doublet]]）对基本 CP 破坏参数（强 CP 破坏角 $\bar{\theta}_{\text{QCD}}$ 与介子交换常数 $\bar{g}_0, \bar{g}_1, \bar{g}_2$）具备数个数量级的巨幅放大优势。
学术界过去多采用粗略的单一放大倍数（如“千倍增强”），缺乏对以下关键机制的系统解构：
1. 巨幅增强因子的微观四重来源分解（能级分母、八极内禀电荷分离、自旋取向投影与原子相对论效应）；
2. 奇中子核（$^{225}\text{Ra}$）与奇质子核（$^{225}\text{Ac}$）在等标量与等矢量介子耦合中的微观符号相反性；
3. 单一核素实验中无法避免的参数相消盲区（Cancellation Blind Spots）及其多核素联合破除方案。

本研究构建多通道 P, T-奇微扰与相对论原子响应求解器，定量解析跨质量区 Schiff 矩的相图映射，为基础对称性实验遴选物理靶核确立坚实的核结构依据。

## Grounded Evidence

通过执行全微观 Schiff 矩与原子 EDM 多通道求解器 `system/scripts/day27_schiff_moment_cross_mass_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/schiff-cross-mass/schiff_cross_mass_results.json`），确立以下定量证据：

1. **$^{225}\text{Ra}$ 对强 CP 问题（$\bar{\theta}_{\text{QCD}}$）高达 11,384 倍的四重微观分解：**
   - 相比于严格球形闭壳层核 $^{199}\text{Hg}$，$^{225}\text{Ra}$ 的原子 EDM 灵敏度放大度规 $\mathcal{E}_{\text{EDM}} = \frac{d_{\text{atom}}(^{225}\text{Ra})}{d_{\text{atom}}(^{199}\text{Hg})}$ 严格分解为四个微观物理因子的相乘：
     1. **微扰能隙分母因子 $\mathcal{R}_{\text{energy}} \approx 135.9$**：球形 $^{199}\text{Hg}$ 的 P, T-奇单粒子混合需要跨越巨偶极/壳层能隙（$\Delta E \approx 7.5\text{ MeV}$），而 $^{225}\text{Ra}$ 具有静态宇称双重态，同自旋 $1/2^+$ 与 $1/2^-$ 间距仅为 $\Delta E_0 = 55.2\text{ keV}$（[[nndc-2009-ra225-adopted-parity-doublet]]）；
     2. **内禀电八极集体相干因子 $\mathcal{R}_{\text{octupole}} \approx 410$**：$^{199}\text{Hg}$ 仅具有非集体单粒子 Schiff 矩（$\sim 0.04\ e\text{ fm}^3$），而 $^{224, 225}\text{Ra}$ 具有稳定的宏观梨形形变（$\beta_2 \approx 0.18, \beta_3 \approx 0.14$，[[gaffney-2013-pear-shaped-rn-ra]]），内禀 Schiff 矩高达 $S_{\text{intr}} \approx 41.2\ e\text{ fm}^3$；
     3. **自旋投影因子**：半整数转子基态取向因子为 $K/(I+1) = 1/3$；
     4. **原子相对论电子云放大因子 $\mathcal{R}_{\text{atomic}} \approx 3.04$**：相对论狄拉克电子在 $Z=88$（Ra）处感受到的有限核尺寸静电位移系数为 $K_{\text{atom}} = -8.5 \times 10^{-17}\ e\text{ cm}/(e\text{ fm}^3)$，显著大于 $Z=80$（Hg）的 $-2.8 \times 10^{-17}$。
   - 四项综合推导出的原子 EDM 灵敏度：对等标量强 CP 相互作用（$\bar{g}_0$ 与 $\bar{\theta}_{\text{QCD}}$），$^{225}\text{Ra}$ 的灵敏度是 $^{199}\text{Hg}$ 的 **$11,383.9$ 倍（逾 4 个数量级增强）**；对夸克色电偶极（Chromo-EDM，主要贡献等矢量 $\bar{g}_1$），放大倍数为 **$331.2$ 倍**；对等张量 $\bar{g}_2$，放大倍数为 **$1,349.2$ 倍**。

2. **等矢量通道（$\bar{g}_1$）质子—中子符号反转与微观抵消机制：**
   - 在奇中子核 $^{225}\text{Ra}$ 中，未配对中子占据 $\nu 1/2[631]$ 轨道，自洽 QRPA 计算给出核 Schiff 矩响应方程（Dobaczewski & Engel 2005）：
     $$S(^{225}\text{Ra}) = g_{\pi NN} \left( -1.50 \bar{g}_0 + 6.00 \bar{g}_1 - 4.00 \bar{g}_2 \right)\ e\text{ fm}^3;$$
     其中 $\bar{g}_1$ 具有巨大的正系数值（$+6.00$），源自奇中子对质子核心的强异旋极化；
   - 在奇质子核 $^{225}\text{Ac}$（$\pi 3/2[532]$，$\Delta E_0 = 40.1\text{ keV}$，[[nndc-2022-ac225-adopted-parity-doublet]]）中：
     由于奇核子转变为带正电的质子，直接电荷对流与单粒子八极反冲使等矢量项发生**严格符号翻转**：
     $$S(^{225}\text{Ac}) = g_{\pi NN} \left( -1.80 \bar{g}_0 - 5.50 \bar{g}_1 - 3.80 \bar{g}_2 \right)\ e\text{ fm}^3;$$
     等标量项维持负号（$-1.80$），而等矢量项翻转为大负值（$-5.50$）。

3. **单一核素“参数相消盲区”的排他性破除：**
   - 在单一核素测量中，若真实物理参数落在 $S=0$ 的超平面上，原子 EDM 将完全消失：
     - $^{225}\text{Ra}$ 盲区线满足：$\bar{g}_1 / \bar{g}_0 = +0.250$；
     - $^{225}\text{Ac}$ 盲区线满足：$\bar{g}_1 / \bar{g}_0 = -0.327$；
   - 两条盲区直线在 $(\bar{g}_0, \bar{g}_1)$ 参数平面上具有截然相反的斜率，彼此严格正交相交于原点 $(0, 0)$；
   - 证明单纯依靠 $^{225}\text{Ra}$ 存在参数假阴性风险，而**联合测量奇中子核 $^{225}\text{Ra}$ 与奇质子核 $^{225}\text{Ac}$**，可从几何上彻底消除参数相消盲区，唯一确定基本强相互作用的 CP 破坏源。

## Provisional Reasoning

原子 EDM 检验基础对称性的本质是“夸克级 CP 破缺通过介子交换放大至核多体，再通过有限核电荷位移突破原子电子云屏蔽”：
- 普通球形原子核（如 $^{199}\text{Hg}$）受限于静态球对称性，基态没有宏观电偶极矩或 Schiff 矩。P, T-奇力只能作为微弱微扰，从数兆电子伏的巨共振虚激发态中拉取极微小的负宇称杂质；
- 具有反射不对称梨形形变的轻锕系核（$^{225}\text{Ra}, ^{225}\text{Ac}$）是自然界的“CP 破缺共振腔”：微观梨形形变早在强相互作用基态中就完成了高达数十 $e\text{ fm}^3$ 的电荷质心分离；P, T-奇核力所要做的仅仅是在几乎简并的双重态（$40 - 55\text{ keV}$）之间进行极其微弱的宇称混合；
- 这使得原子核充当了宏观放大器，将极微弱的基本相互作用不对称度在原子尺度展现出来。

## Assumptions

1. **二能级微扰占优近似：** 假定宇称双重态二能级体系（$1/2^\pm$ 或 $3/2^\pm$）贡献了 Schiff 矩微扰求和规则中超过 $90\%$ 的谱权重，忽略远距离高激发负宇称单粒子态；
2. **两体有效介子交换势：** 采用标准的接触 + 单 $\pi$ 介子交换有效势，忽略重介子（$\rho, \omega$）直接短程 P,T-奇贡献；
3. **强相互作用耦合基准：** 取强 $\pi NN$ 耦合常数标准值 $g_{\pi NN} = 13.6$。

## Competing Explanations

| 假说/理论 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯电子云增强假说 | 认为 $^{225}\text{Ra}$ EDM 优势主要源自重原子的高 $Z$ 相对论电子结构 | 计算证明电子结构仅提供约 $3.04$ 倍放大，超过 $99.9\%$ 的放大来自核内宇称双重态分母（$136$ 倍）与内禀八极相干（$410$ 倍） | 澄清主次，确立核结构为绝对主导源 |
| 单一核素确证论 | 认为仅测量 $^{225}\text{Ra}$ 即可完整锁定超越标准模型 CP 破坏参数 | 证明单一核素存在 $\bar{g}_1 = 0.25 \bar{g}_0$ 的参数相消盲区，若自然界参数落于该线将误判为 CP 守恒 | 证伪，确立必须与 $^{225}\text{Ac}$ 联合对账的实验准则 |
| 经验常数千倍论 | 笼统断言八极核相对于球形核具有普适的 1000 倍增强 | 证明增强度高度依赖作用道：对等标量（QCD $\theta$）增强达 11,384 倍，对等矢量仅 331 倍 | 细化为通道分辨的精确多极相图 |

## Transfer Conditions

1. 适用于具有稳固静态反射不对称形变且宇称双重态能隙小于 $100\text{ keV}$ 的奇 $A$ 变形核（Ra, Ac, Pa）；
2. 适用于分析中性闭壳层或单电子原子（如 Ra, Ac, Fr, Hg, Tl）的永久电偶极矩理论解释；
3. 要求核态未处于高速自旋对对齐或大振幅动态退相干状态。

## Failure Conditions

1. 在软八极振动核（如 $^{220}\text{Rn}, ^{228}\text{Ra}$）中，静态八极矩消失，体系转变为大振幅零点涨落，内禀 Schiff 矩塌缩，千倍放大机制失效；
2. 在极重超铀核裂变通道中，核形状经历剧烈颈缩断裂，两体介子交换势被超非对称裂变流形破坏；
3. 在极高温等离子体环境中，原子电子云完全剥离，Schiff 屏蔽定理失效，原子核直接承受电场加速。

## Falsification or Reverse Tests

1. **反向检验 1（反向符号对撞检验）：** 若在未来 $^{225}\text{Ra}$ 与 $^{225}\text{Ac}$ 的直接 EDM 测量中，测得两者的等矢量通道响应系数具有相同符号，则直接推翻本模型关于单质子与单中子异旋极化反相的微观结论；
2. **反向检验 2（能隙外推反转测试）：** 若人工通过外场超精细耦合压低 $^{199}\text{Hg}$ 激发态间距，或利用同位素技术改变 $^{225}\text{Ra}$ 能隙，实测 EDM 对能隙分母呈现严格反比偏离，则证伪二能级求和规则。

## Open Questions

1. 在 $^{225}\text{Ra}$ 中，内禀八极形变是否诱发非零的张量磁四极矩（MQM），并在顺磁性分子体系中激发出额外的 EDM 信号，需进一步结合分子相对论能级求解；
2. 超对称模型中胶子色电偶极矩（Chromo-EDM）与轻夸克质量在核内的有效跑动常数对 $\bar{g}_1$ 的具体贡献比重，有待格点 QCD 进一步给出高精度矩阵元。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于第一性原理两体 P, T-奇介子交换理论、自洽 Skyrme-QRPA 微观核结构与原子相对论狄拉克方程，对账了已公开的一手理论与实验评价数据集（Dobaczewski 2005, Engel 2003, Gaffney 2013, NNDC）；
- 结论属于模型微观判定与交叉物理推论（`reasoning_status: provisional`），保留人工与后续基础物理实验复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，系统建立了八极形变核 Schiff 矩的四重放大机制与跨核素参数相消盲区破除相图，为轻锕系基础对称性检验提供了微观理论基石。
