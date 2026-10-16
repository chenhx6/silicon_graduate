---
type: method
title: DCO 比值分析
aliases: [DCO ratio, RDCO, directional correlation from oriented states]
created: 2026-07-01
updated: 2026-10-17
status: active
review_status: unreviewed
method_type: gamma-ray-angular-correlation
tags: [multipolarity, gamma-spectroscopy]
---

# DCO 比值分析（Directional Correlation from Oriented States）

## Purpose

利用不同探测角度的符合强度比约束 γ 跃迁多极性和 mixing ratio。

## Inputs and Assumptions

探测器角度组、门跃迁多极性、alignment 和效率校正。

## Procedure

在已知 stretched E2 等门上构造非对称矩阵，比较实验 R_DCO 与给定几何下的理论值。

### 原件复核后的强度比与标签

[[kramer-flecken-1989-use-dco-ratios]] KF89-9（printed334）更正旧Wiki实验分式的倒置转写。其gamma1是门、gamma2是待测线，定义`W(theta1,theta2,phi)=I_gamma2@theta2(Gate_gamma1@theta1)`，所以

\[
R_{\rm DCO}=\frac{W(\theta_2,\theta_1,\phi)}{W(\theta_1,\theta_2,\phi)}
=\frac{I^{\gamma_2}_{\theta_1}(\mathrm{Gate}^{\gamma_1}_{\theta_2})}
{I^{\gamma_2}_{\theta_2}(\mathrm{Gate}^{\gamma_1}_{\theta_1})}.
\]

旧方法页曾把后一个I分式写成倒数，现以原件方向替换；原论文的两个公式一致。角度下标是detector标签，gamma1/gamma2不自动等于物理发射先后。交换角组或待测/门可在**相同corrected pair cells、selection和normalization**下取倒数；真实换门改变条件密度/cuts时，须重新核joint response。

这里I取共同曝光/一致normalization的net peak yield，不能额外各除一次本角组gate counts后仍当同一个joint-intensity比。原件printed335另要求相对效率修正。在point、可分离单gamma效率且live exposure匹配的模型内，从raw比恢复joint理论比的因子为`epsilon_gamma2(theta2) epsilon_gamma1(theta1) / [epsilon_gamma2(theta1) epsilon_gamma1(theta2)]`；对composite groups或finite joint response，不能强塞一个通用scalar因子。[[smith-2019-griffin-angular-correlation-analysis]] SG19-3/6保留finite-response边界，[[angular-distribution]]中ADO还另有gate/self-exclusion的f。

[[dco-pdco-ambiguity-worksheet]]的R*分子/分母、source原图近似例和本任务精确同R根另行明确，不能仅因都叫R_DCO就共用.5/1经验值。

## What It Can Establish

区分主要 dipole/quadrupole 特征，并与 ANGCOR 等计算联合约束 δ。

## What It Cannot Establish Alone

有限角度和弱跃迁时不能唯一给出 δ 符号或排除全部解。

Kramer-Flecken 1989 还明确指出：把 `sigma/I` 当作近似常数只是经验简化，原件printed334的低自旋边界为`I≤6`（旧摘要写I<6）。其half-width用语未在本文给指数定义，不能仅靠同字母当作HWHM或其它source的std。低自旋DCO解释须自己校准取向；D96的sigma/I0=.3模型不是实际低spin核的测量。

Kramer-Flecken 1989 还明确指出：当允许 dipole-quadrupole mixing 时，同一个 DCO ratio 可对应多个自旋或 `delta` 解；一般 `Delta I = ±1` 不能单靠 DCO 唯一区分。

## Conventions and Systematics

R_DCO 的“dipole≈0.5 / quadrupole≈1”等经验值只对特定门和几何有效。

同L也不能忽略spin path。KF89-11的Table1中，两个pureL2在10→8→7给.66、10→8→8给.57；stretched10→8→6才给1。generic dipole/quadrupole delta还可能是M2/E1（如KF的182-keV例），不能一律计算E2份额。

几何选择会直接改变判别力。Kramer-Flecken 1989 对 OSIRIS 的分析显示，把 detector angles 选在接近 `0°/180°` 与 `90°` 的组合，可放大不同 cascades 的 DCO 差异；相对效率修正也应尽量用能量相近、已知多极性的参考 cascade 标定。

不要把 DCO 与 [[two-point-angular-correlation-ratio]] 混写：后者可设计为对 gating transition 多极性不敏感，但其经验标定仍依赖具体阵列。

## Reference-Guide Boundary

[[summary-2013-bases-spin-parity-assignments]] records DCO-ratio practice as part of a spin/parity-assignment guide for high-spin work. Its quoted typical orientation parameter is `σ/I = 0.3`. For the sigma-over-I project this is useful background evidence that practical assignment workflows often assume a typical orientation scale, but it is not enough to justify one universal default across different reactions and fitting contexts.

## Examples

[[chakraborty-2023-131xe-wobbling-origin]] 使用 40°、90°、125° INGA 数据约束 671、882、1055 keV 等跃迁。

[[domscheit-1999-triaxial-superdeformation-163lu]] 用 Euroball forward/backward 对 near-90° Clover 构造 DCO 矩阵，并在 Table 1 报告 SD1 衰变跃迁的 `R_DCO`。该表没有为每一行单列多极性栏，数值必须结合门条件、能级差和正文指认使用。

[[matta-2015-transverse-wobbling-135pr]] 称 702.7 keV `135Pr` signature-partner link 的 DCO ratio 支持 pure dipole，但 PRL 未列出具体比值；该赋值需在人工审阅时保留信息缺口。

[[lv-2021-tilted-precession-135nd]] 以 157.6° tapered 对 75.5°、104.5° clover 非对称矩阵提取 `R_DCO`。其阵列标定在 stretched-quadrupole gate 下给出 quadrupole/dipole 约 1/0.46，在 stretched-dipole gate 下给出 dipole/quadrupole 约 1/2.1；这些经验值只适用于该 geometry 与 gate convention。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[domscheit-1999-triaxial-superdeformation-163lu]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[lv-2021-tilted-precession-135nd]]
- [[kramer-flecken-1989-use-dco-ratios]]
- [[summary-2013-bases-spin-parity-assignments]]

## Evolution Log

- 2026-07-01：由 `131Xe` 实验建立。
- 2026-07-03：加入早期 Euroball 几何实例及“不跨阵列套用经验阈值”的限制。
- 2026-07-03：加入 Matta 2015 的“正文给出结论但未列具体 DCO 数值”案例。
- 2026-07-04：加入 Lv 2021 JUROGAM II `135Nd` 双 gate convention 与经验值。
- 2026-07-12：加入 Kramer-Flecken 1989 的定义、几何依赖、效率修正和多解边界。
