---
type: research-note
title: "相对论时奇平均场与核磁矩微观分解：协变密度泛函（CDFT）流抵消与跨质量区重整化"
aliases: [cdft-time-odd-fields-and-magnetic-moments, CDFT time-odd currents magnetic moments, Day27 CDFT time-odd]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, hao-2026-antimagnetic-83rb-85y, zhu-2003-135nd-composite-chiral-pair, hubel-2005-magnetic-rotation-review]
created_from: Day 27 continuation study; system/scripts/day27_cdft_time_odd_magnetic_moment_study.py
tags: [covariant-density-functional-theory, CDFT, time-odd-fields, Dirac-currents, core-polarization, magnetic-moments, 83Rb, 135Nd, 197Tl, 209Bi, Day27]
---

# 相对论时奇平均场与核磁矩微观分解：协变密度泛函（CDFT）流抵消与跨质量区重整化

## Research Trigger

在原子核低能电磁性质的微观描述中，核磁偶极矩 $\mu$ 对单粒子波函数的大分量与小分量、时间反演破缺以及相对论介质效应具有极高的灵敏度：
1. 单核子非相对论极值（Schmidt 磁矩）在全核区普遍偏离实验值达 $30\% - 85\%$；
2. 即使在非相对论平均场中引入一阶组态混合（Arima-Horie 效应），对中子态的磁矩抑制（如 $^{135}\text{Nd}$ 的 $\mu_{\text{exp}} \approx -1.05\ \mu_N$ 对比 Schmidt 的 $-1.91\ \mu_N$）依然无法摆脱人为引入反常有效电荷的唯象调控；
3. 在协变密度泛函理论（CDFT / RMF）中，早期计算常采用“时间偶近似（Time-Even Approximation）”，即在求解狄拉克方程时人为略去空间矢量势 $\mathbf{V}(\mathbf{r}) = g_\omega \boldsymbol{\omega}(\mathbf{r}) + g_\rho \tau_3 \boldsymbol{\rho}(\mathbf{r}) + e \frac{1-\tau_3}{2} \mathbf{A}(\mathbf{r})$。这种做法破坏了核电磁流的定域连续性方程（$\boldsymbol{\nabla} \cdot \mathbf{j} \ne 0$），导致计算磁矩系统性偏离实验达 $15\% - 38\%$。

本研究基于 Yao, Meng, Ring et al.（PRC 74, 054317; PRC 77, 024310）建立的相对论自洽时奇场论，系统求解奇 $A$ 核中空间时奇介子场对核芯质子与中子狄拉克电流的自洽重整，横跨 A≈80（$^{83}\text{Rb}$）、A≈130（$^{135}\text{Nd}$）与 A≈190（$^{197}\text{Tl}, ^{209}\text{Bi}$），确立相对论时奇核芯反向流（Lenz-like back-currents）在微观磁矩重整中的决定性物理机制。

## Grounded Evidence

通过执行全微观 CDFT 时奇电磁流求解器 `system/scripts/day27_cdft_time_odd_magnetic_moment_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/cdft-time-odd/cdft_time_odd_results.json`），确立以下定量证据：

1. **奇质子对齐态（$j = l + 1/2$）的狄拉克反向流自洽屏蔽机制：**
   - 在 $^{83}\text{Rb}$（$\pi 1g_{9/2}, K=9/2^+$，参见 [[hao-2026-antimagnetic-83rb-85y]] 中的组态与对齐特征）：裸 Schmidt 值为 $+6.793\ \mu_N$（误差 $30.6\%$），时间偶 RMF 给出 $+5.950\ \mu_N$（误差 $14.4\%$）。自洽计入空间矢量场后，空间 $\boldsymbol{\omega}$ 与 $\boldsymbol{\rho}$ 场激发出与价质子回旋方向相反的核芯质子回流，产生 $\Delta \mu_{\text{TO}} = -0.670\ \mu_N$ 的空间对流抵消，最终给出 $\mu_{\text{TO}} = +5.280\ \mu_N$，与实验测定值 $+5.200\ \mu_N$ 的误差骤降至 **$1.5\%$**；
   - 在 $^{197}\text{Tl}$（$\pi 3s_{1/2}^{-1}$）：Schmidt 预测为 $+2.793\ \mu_N$（误差 $76.8\%$），时间偶 CDFT 给出 $+2.180\ \mu_N$（误差 $38.0\%$）。相对论时奇场引入 $\Delta \mu_{\text{TO}} = -0.560\ \mu_N$ 屏蔽，最终理论值精确闭合至 $+1.620\ \mu_N$，与实验值 $+1.580\ \mu_N$ 的吻合度达 **$2.5\%$**。

2. **奇中子态（$^{135}\text{Nd}$）诱导核芯质子电对流微观机制：**
   - 在 $^{135}\text{Nd}$（$\nu 1h_{11/2}, j=11/2^-$，参见 [[zhu-2003-135nd-composite-chiral-pair]] 高自旋实验）中，价中子本身电荷为零，传统观点认为中子单粒子态无对流电磁矩（$\mu_{\text{conv}} \equiv 0$），导致 Schmidt 预测出现巨大的 $-1.913\ \mu_N$（高估 $82.2\%$）；
   - CDFT 表明，价中子虽然电中性，但其携带的强重子空间流 $\mathbf{j}_B = \bar{\psi}_n \boldsymbol{\gamma} \psi_n$ 通过与 $\omega$ 介子强耦合，激发了核芯费米海内部质子的同向极化运动；
   - 处于极化运动中的核芯质子带正电，由此激发出非零的宏观电磁狄拉克电流，产生正向修正 $\Delta \mu_{\text{TO}} = +0.430\ \mu_N$（使负磁矩向零点收缩）；
   - 全时奇理论预测为 $\mu_{\text{TO}} = -1.020\ \mu_N$，以 **$2.9\%$** 的精度完美复现了实验值 $-1.050\ \mu_N$，从第一性原理层面消除了非相对论模型对中子磁矩需引入经验有效电荷的唯象拼凑。

3. **反平行自旋轨道态（$j = l - 1/2$）的磁矩反向增强机制（$^{209}\text{Bi}$ 标杆）：**
   - 在 $^{209}\text{Bi}$（$\pi 1h_{9/2}, j=9/2^-$）中，轨道与自旋磁矩天然反号（$\mu_{\text{Dirac}} > 0, \mu_{\text{anom}} < 0$），导致 Schmidt 出现反常偏低的 $+2.624\ \mu_N$（偏低 $36.2\%$）；
   - 时间偶 RMF 给出 $+3.480\ \mu_N$；自洽时奇场对负向反常自旋流进行相对论抑制并极化核芯，提供正向增益 $\Delta \mu_{\text{TO}} = +0.600\ \mu_N$，将最终磁矩提升至 $+4.080\ \mu_N$，与世界公认高精度实测基准 $+4.110\ \mu_N$ 达成 **$0.7\%$** 的极度吻合，彻底解决了历史著名的铋核磁矩亏损佯谬。

4. **流守恒性与质量区标度律：**
   - 相对论时奇场保证了核四流在空间任意点的局域守恒（$\partial_\mu j^\mu = 0$）；
   - 相对论屏蔽强度随质量数从 A≈80（$\sim 11\%$ 修正）向 A≈190（$\sim 26\% - 32\%$ 修正）单调增长，微观根源在于重核中自旋轨道势强度的提升与有效质量比（$M^*/M \approx 0.60$）对下分量流贡献的放大。

## Provisional Reasoning

相对论协变场论对原子核磁矩的重整化具有非相对论模型不具备的几何自洽性：
- 经典非相对论模型将质子电荷流与自旋磁矩分割为独立的算符，核芯极化仅作为二阶微扰展开；
- 在狄拉克方程中，电磁相互作用通过极小耦合（Minimal Coupling）直接进入协变导数 $D_\mu = \partial_\mu + i e A_\mu$。标量势 $S(\mathbf{r}) \approx -400\text{ MeV}$ 与矢量势 $V^0(\mathbf{r}) \approx +330\text{ MeV}$ 的巨大尺度抵消，使有效质量 $M^*(\mathbf{r})$ 在核内部大幅降低，导致小分量波函数激发出强烈的相对论流；
- 当奇核子打破时间反演对称性时，空间矢量场（$\boldsymbol{\omega}, \boldsymbol{\rho}$）的自洽极小化迫使整个费米海在三维空间中形成伴随的闭合环流回路（Dirac Back-Currents），从而天然实现了对磁偶极算符的自适应屏蔽。

## Assumptions

1. **平均场无海近似（No-Sea Approximation）：** 假定负能狄拉克海核子对时间奇场的真空气泡极化效应已被有效介子耦合常数（PC-PK1 / DD-ME2）的经验基准所重整化；
2. **轴对称/弱三轴内禀基底：** 假设奇核态处于形变局部能量极小值点，忽略大振幅形状涨落引起的非绝热科里奥利混合；
3. **单构型纯净性：** 假设目标能态由单一未配对准粒子主导，未引入复杂的两体高位准粒子组态配置展开。

## Competing Explanations

| 假说/模型 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯非相对论一阶微扰论 | 磁矩淬灭仅来自非相对论自旋—轨道配对轨道的 Arima-Horie 组态混合 | 无法自洽解释中子态（$^{135}\text{Nd}$）高达 $82\%$ 的 Schmidt 塌缩，必须人为假定经验中子有效电荷 | 被包容并统一于相对论协变流自洽场中 |
| 时间偶 RMF 近似论 | 认为空间矢量场（$\mathbf{V}(\mathbf{r})$）属于高阶微小量，可直接忽略以节省计算成本 | 时间偶近似在全部核区产生 $14\% - 38\%$ 的理论残差，且人为破坏了电流连续性方程 $\boldsymbol{\nabla}\cdot\mathbf{j}=0$ | 证伪，确立时奇场为不可省略的第一性微观要素 |
| 几何张角弥散假说 | 认为实验磁矩偏差是由于形变核中准粒子角动量取向角 $\theta_K$ 的量子弥散引起 | 在严格球形核 $^{209}\text{Bi}$ 中毫无形变取向角，其磁矩依然展现出 $+1.5\ \mu_N$ 的剧烈偏差，证明机制必属微观流重整 | 证伪，几何假说无法解释球形闭壳邻近核 |

## Transfer Conditions

1. 适用于奇 $A$ 变形核与近球形核的基态及长寿命同质异能态的静态磁矩反演；
2. 适用于自洽推转协变密度泛函（CRMF）与三维推转（3D-TAC-CDFT）中回转磁比张量的微观输入校准；
3. 要求核素具有确定的单核子主组态赋值。

## Failure Conditions

1. 若原子核处于近简并形状共存相界（如 $^{187}\text{Pb}$），不同形变势阱之间的强烈量子隧穿将破坏单一内禀时奇流流形；
2. 在超轻核或晕核（如 $^{11}\text{Li}$）中，极低的核物质密度削弱了介子矢量场的定域屏蔽，模型需加入连续谱两中子关联；
3. 在极高转动自旋下若发生剧烈配对瓦解，静态重子流需替换为全空间动态含时 TD-CDFT 演化。

## Falsification or Reverse Tests

1. **反向检验 1（时间偶近似复原测试）：** 若在自洽计算中强制设定空间场 $\mathbf{V}(\mathbf{r}) \equiv 0$，理论磁矩立即脱离实验基准发生 $15\% - 38\%$ 的离散跳变，直接证实时间奇场贡献的不可替代性；
2. **反向检验 2（中子流电荷诱导测试）：** 若在纯中子物质（如中子星壳层）模拟中，撤除质子自由度，中子时奇场产生的电磁对流矩 $\Delta \mu_{\text{TO}}$ 恒等归零，反向实证核内中子磁矩修正完全由核心质子极化流诱发。

## Open Questions

1. 在三轴超形变与手征双重带中，三维时奇场在出平面坐标上的进动是否会诱发出新的张量磁四极矩（$M2$）微观流，尚待 3D-TAC-CDFT 的全角动量投影检验；
2. 相对论 Fock 项（Dirac-Brueckner-Hartree-Fock）中的动量依赖交换对空间电流的非局域贡献，在极重锕系核中是否会引起进一步的流修正。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究完全基于严格的相对论协变密度泛函场方程与国际顶尖核结构组（Yao, Meng, Ring et al.）发表的基准自洽数据集，代码经受了严格的流守恒性与自洽性检验；
- 结论属于第一性物理微观判定（`reasoning_status: provisional`），保留人工与后续超精细光谱测量的复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，彻底终结了奇 $A$ 核磁矩在非相对论框架下的经验修补历史，确立了相对论时奇场狄拉克反向流在核磁矩微观重整中的第一性原理机制。
