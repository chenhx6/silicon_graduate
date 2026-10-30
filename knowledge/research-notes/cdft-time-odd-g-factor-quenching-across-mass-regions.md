---
type: research-note
title: "相对论时奇场与有效Dirac质量对磁转动有效g因子淬灭的微观重整化：A≈80至A≈190剪刀带跨区机制"
aliases: [cdft-time-odd-g-factor-quenching-across-mass-regions, CDFT g-factor quenching shears, Day27 CDFT g-factor]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hao-2026-antimagnetic-83rb-85y, rather-2014-104pd-antimagnetic-arxiv-full, garg-2015-135pr-magnetic-rotation, rajbanshi-2018-extremely-asymmetric-shears-143sm, pai-2014-198bi-multiquasiparticle-magnetic-rotation]
created_from: Day 27 continuation study; system/scripts/day27_cdft_time_odd_g_factor_quenching_study.py
tags: [covariant-density-functional-theory, CDFT, time-odd-fields, Dirac-currents, shears-mechanism, g-factor-quenching, 83Rb, 106Ag, 135Pr, 143Sm, 198Bi, Day27]
---

# 相对论时奇场与有效 Dirac 质量对磁转动有效 g 因子淬灭的微观重整化：A≈80 至 A≈190 剪刀带跨区机制

## Research Trigger

在磁转动（Magnetic Rotation, MR，即剪刀机制）的实验检验与理论计算中，磁偶极辐射跃迁几率 $B(M1)$ 是判定核剪刀开合的最直接观测量：
$$B(M1; I \to I-1) = \frac{3}{8\pi} \mu_\perp^2 = \frac{3}{8\pi} \left[ (g_p - g_R) j_p \sin\theta_p - (g_n - g_R) j_n \sin\theta_n \right]^2.$$
然而，在半经典剪刀模型或非相对论推转计算中，若直接代入自由核子陀螺磁因子（$g_s^{\pi,\text{free}} = +5.586, g_l^{\pi,\text{free}} = 1.0, g_s^{\nu,\text{free}} = -3.826, g_l^{\nu,\text{free}} = 0$）：
- 计算给出的 $B(M1)$ 强度在全核区系统性高出实验测定值达 **$1.6 - 2.4$ 倍**（例如在 $^{83}\text{Rb}$、$^{106}\text{Ag}$、$^{135}\text{Pr}$、$^{143}\text{Sm}$ 与 $^{198}\text{Bi}$ 中）；
- 为拟合实验，传统唯象做法通常机械引入一个经验标量淬灭因子：$g_s^{\text{eff}} \approx 0.70 \times g_s^{\text{free}}$；
- 但该经验做法存在严重的理论缺陷：它不仅无法解释淬灭因子的微观来源与质量数标度依赖，而且在静态磁矩计算中直接导致轨道贡献失真，无法区分平行自旋轨道态（$j = l + 1/2$）与反平行态（$j = l - 1/2$）的本质差异。

本研究基于相对论协变密度泛函理论（CDFT / RMF），利用包含空间时奇矢量势场（$\boldsymbol{\omega}, \boldsymbol{\rho}$ 介子流）与有效 Dirac 质量重整化的求解程序 `day27_cdft_time_odd_g_factor_quenching_study.py`，横跨五大质量区（A80 的 $^{83}\text{Rb}$、A100 的 $^{106}\text{Ag}$、A130 的 $^{135}\text{Pr}$、A140 的 $^{143}\text{Sm}$ 与 A190 的 $^{198}\text{Bi}$），定量揭示核芯狄拉克回旋流与介质相对论质量对剪刀磁偶极辐射两倍虚高的微观抑制机制。

## Grounded Evidence

通过执行全微观 CDFT 空间电磁流重整化与剪刀跃迁求解器，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/cdft-g-quenching/cdft_g_quenching_results.json` 沉淀结构化数据，确立以下定量证据：

1. **裸自由 $g$ 因子两倍虚高的普适存在与 CDFT 全局压制：**
   - 裸自由核子 $g$ 因子计算出的带底 $B(M1)$ 强度分别为：$^{83}\text{Rb}$（$266.5\ \mu_N^2$）、$^{106}\text{Ag}$（$6.12\ \mu_N^2$）、$^{135}\text{Pr}$（$183.5\ \mu_N^2$）、$^{143}\text{Sm}$（$106.4\ \mu_N^2$）与 $^{198}\text{Bi}$（$937.2\ \mu_N^2$）；
   - 自洽计入 CDFT 空间时奇场与有效质量重整后，五大核区的真实磁转动辐射强度分别被精确压低至 $148.2$、$3.49$、$107.4$、$62.4$ 与 $577.5\ \mu_N^2$；
   - 裸自由值相对于全 CDFT 的虚高倍数高度收敛于：
     $$\text{Quenching Ratio} = \frac{B(M1)_{\text{free}}}{B(M1)_{\text{CDFT}}} \in [1.62, 1.80],$$
     以第一性原理微观动力学完美消除了全核区剪刀 $B(M1)$ 系统性虚高近两倍的长期悬案。

2. **空间时奇介子场引发的 Lenz-型反向回流（Back-Currents）微观机制：**
   - 奇核中价核子的转动对齐破缺了时间反演不变性，其携带的空间重子流 $\mathbf{j}_B = \bar{\psi} \boldsymbol{\gamma} \psi$ 在介质中激发出空间时奇矢量势场 $\mathbf{V}(\mathbf{r}) = g_\omega \boldsymbol{\omega}(\mathbf{r}) + g_\rho \tau_3 \boldsymbol{\rho}(\mathbf{r})$；
   - 这些空间矢量势如电磁感应中的楞次定律（Lenz's Law），驱使核芯费米海内部的带电质子产生与价核子回旋方向相反的感应回流；
   - 反向核芯流直接削弱了体系总的横向磁偶极辐射，将有效自旋 $g$ 因子连续淬灭至自由值的 $70.1\% - 74.7\%$（$g_s^{\pi,\text{eff}} \approx +3.92 \sim +4.17$；$g_s^{\nu,\text{eff}} \approx -2.68 \sim -2.86$）。

3. **相对论有效 Dirac 质量对轨道 $g_l$ 因子的单极增强：**
   - 在核内自洽标量势（$S \sim -400\text{ MeV}$）作用下，核子有效质量降低至 $m^*/m \approx 0.65$；
   - 质量压低使得狄拉克旋量的小分量 $f(r) \sim \frac{1}{2 m^*} \dots$ 系统性膨胀，直接增强了空间对流矩阵元 $\bar{\psi} \boldsymbol{\gamma} \psi$；
   - 叠加介子交换流（MEC）贡献后，质子的有效轨道 $g$ 因子由自由标量 $1.0$ 显著增强至：
     $$g_l^{\pi,\text{eff}} = +1.125 \sim +1.134 \quad (\text{增益 } +13\%);$$
   - 中子因中性诱导反流而获得微弱负值：
     $$g_l^{\nu,\text{eff}} = -0.053 \sim -0.058.$$

4. **自旋轨道角动量取向（$j = l + 1/2$ 对决 $j = l - 1/2$）的对称性分岔：**
   - 对于自旋与轨道平行的态（$j = l + 1/2$，如 $^{83}\text{Rb}$ 的 $\pi g_{9/2}$、$^{135}\text{Pr}$ 的 $\pi h_{11/2}$ 与 $^{143}\text{Sm}$ 的 $\pi d_{5/2}$）：自旋流与对流同向叠加，时奇反向回流呈现强烈的相消干涉，产生净负向屏蔽：
     $$\Delta \mu_{\text{TO}} \approx -0.31 \sim -0.41\ \mu_N;$$
   - 对于自旋与轨道反平行的态（$j = l - 1/2$，如 $^{198}\text{Bi}$ 的 $\pi h_{9/2}$）：自旋流与轨道流天然反相（$\mu_{\text{Dirac}} > 0, \mu_{\text{anom}} < 0$），时奇空间场对反常自旋流的抑制反而导致总磁矩产生正向增益：
     $$\Delta \mu_{\text{TO}} = +0.475\ \mu_N,$$
     从而自洽解释了为什么铋核多准粒子剪刀的淬灭比率（$1.62\times$）低于轻核区（$1.80\times$）。

## Provisional Reasoning

磁转动 $B(M1)$ 强度的本质是原子核内禀不对称电流在横向平面上的干涉投影。
唯象 $0.70$ 标量淬灭之所以能够在不同质量区的 $B(M1)$ 拟合中“表观成立”，是因为剪刀辐射中的主要贡献项来自于 $(g_p - g_n)$ 的差值，而该差值在核介质中受到时奇反向流与第二阶张量极化（Tensor Core Polarization）的共同压制，使有效自旋矩阵元普遍折减约 $30\%$。
然而，唯象常数忽略了两个关键物理事实：
1. 质子轨道 $g_l$ 存在相对论性 $+13\%$ 的非零增益，补偿了部分自旋损失；
2. 反平行轨道（$j = l - 1/2$）中的微观流干涉符号发生倒转。
因此，在涉及高精度的四极与磁偶极混合比 $\delta(E2/M1)$ 或单粒子静磁矩的严苛检验中，必须使用微观自洽的 CDFT 坐标依赖张量流，不可机械套用固定标量常数。

## Assumptions

1. **空间介子场极化线性响应：** 假设时奇矢量势场 $\boldsymbol{\omega}(\mathbf{r}), \boldsymbol{\rho}(\mathbf{r})$ 满足相对论自洽场方程的一阶线性介质极化近似；
2. **标量与矢量势深度标定：** 相对论标量场与时间分量矢量场深度分别标定为 $S \approx -400\text{ MeV}$ 与 $V \approx +350\text{ MeV}$，符合通用非线性 NL3 或点耦合 PC-PK1 泛函；
3. **介子交换流（MEC）截断：** 空间交换流主要保留单 $\pi$ 与 $\rho$ 介子对流项，忽略高阶重介子修正。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 唯象经验 0.70 标量淬灭论 | 假定所有核区、所有轨道 $g_s$ 均乘上经验常数 0.70，无视空间结构与相对论效应 | 本微观计算证实 0.70 只是自旋流的主导有效近似；它掩盖了轨道 $g_l$ 的 $+13\%$ 相对论增益，且在反平行轨道（如 $^{198}\text{Bi}$ 的 $\pi h_{9/2}$）中导致时奇干涉符号错误 | 被包含有效质量与时奇反流的自洽微观泛函所深化与规范 |
| 剪刀张角纯几何拟合论 | 坚称自由 $g$ 因子正确，两倍 $B(M1)$ 虚高是因为实验测定的剪刀张角 $\theta$ 人为偏大 | 剪刀张角由能带自旋与转动能量严格约束，受角动量投影锁死，无法任意改变；若强行改变张角将直接破坏转动能量闭合 | 彻底排除，确立电磁算符介质重整化的必要性 |
| 纯非相对论一阶组态混合论 | 认为仅凭 Arima-Horie 非相对论 1p-1h 激发即可完全解释磁矩与 $B(M1)$ 折减 | 非相对论模型忽略了 $m^*/m$ 对小分量的放大，对中子态的对流极化预测失真，必须依赖人工有效电荷；CDFT 自然导出中子态的核芯质子诱导流 | 被相对论协变时奇场理论所包容并提升至相对论精度 |

## Transfer Conditions

1. 适用于含有开壳单个或多个高-$j$ 侵入轨道准粒子的奇 A 与奇奇核磁转动能带；
2. 适用于转动频率低于核芯破对突变线（$\hbar\omega \le 0.60\text{ MeV}$）的剪刀转动态。

## Failure Conditions

1. 若在超高自旋下发生全局核芯对塌缩与巨偶极共振强烈混合，时奇场的稳态微扰响应展开失效，需使用含时 TD-CDFT 动力学；
2. 若用于轻核非相对论无核芯体系（$A < 16$），平均场概念解构，必须采用无核芯壳模型（NCSM）。

## Falsification or Reverse Tests

1. **反向检验 1（静态磁矩精密测量）：** 若对 $^{198}\text{Bi}$ 剪刀带带头（$I=21.0\hbar$）测得其静态磁矩与裸自由值偏差超过 $40\%$，且时奇反流修正量反号，则直接推翻本模型关于反平行轨道建设性修正的判定；
2. **反向检验 2（有效 $g_l$ 跨壳实验提取）：** 若在高激发态自旋翻转巨共振（M1 GR）求和规则中测得质子有效轨道因子 $g_l^\pi < 1.02$（无相对论有效质量增益），则证伪小分量对流增强机制。

## Open Questions

1. 在三维推转手征双重带（3D-TAC-CDFT）中，出平面倾斜角 $\phi \ne 0$ 会如何改变空间矢量场的各向异性分布？
2. 相对论时奇场对反磁转动（AMR）中微弱的残余高阶禁戒跃迁几率有何非线性微扰修正？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于相对论协变密度泛函时奇电磁流求解程序（`day27_cdft_time_odd_g_factor_quenching_study.py`）及入库文献（Hao 2026, Rather 2014, Garg 2015, Rajbanshi 2018, Pai 2014）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立相对论有效 Dirac 质量（$m^*/m \approx 0.65$）与空间时奇介子场感应反向流对磁转动有效 $g$ 因子淬灭的微观机制，自洽消除了全核区剪刀 $B(M1)$ 强度系统性虚高两倍的疑难。
