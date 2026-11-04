---
type: method
title: "Hamilton 第15章：Compton 偏振仪的 P-A-Q 响应合同"
aliases: [Compton polarimeter response, P-A-Q contract, Hamilton linear polarization]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: "compton-polarimeter-response"
scope: "Rendered verification of Hamilton Ch. 15, PDF pp. 716-721"
confidence: "high for the listed equations and response boundaries"
tags: [hamilton, compton-polarimetry, linear-polarization, detector-response, sensitivity, efficiency]
sources: [book-hamilton-electromagnetic-interaction]
---

# Hamilton 第15章：Compton 偏振仪的 P-A-Q 响应合同

## Purpose

把实验中容易混淆的四个量分开：

```text
核结构模型 -> physical polarization P
探测器计数 -> asymmetry A
响应校准 -> sensitivity Q
几何/效率/本底 -> response and covariance
```

Hamilton Ch. 15 的关键关系是
\[
P_{\mathrm{exp}}(\theta)
 =\frac{1}{Q(E_\gamma,\mathrm{geometry})}
 \frac{N_\perp-a_{\mathrm{geom}}N_\parallel}
      {N_\perp+a_{\mathrm{geom}}N_\parallel},
\]
其中 \(Q\) 是探测器偏振灵敏度，\(a_{\mathrm{geom}}\) 是无偏振几何/相对效率校准
因子。这个式子把计数层、响应层和核跃迁层明确分开。

## Inputs and Assumptions

- \(N_\perp,N_\parallel\) 是相同门条件、相同能量窗和相同时间选择下的散射计数；
- \(a_{\mathrm{geom}}\) 来自无偏振参考源或等价的响应测量，不能默认恒为 1；
- \(Q\) 来自强偏振参考线或经过验证的 detector-response simulation；
- 物理偏振的相位、正负极性和 Compton 平面约定已经记录；
- 取向张量、混合比、\(\Delta I\)、背景/随机扣除和有限立体角修正不能被 \(Q\)
  吸收后静默消失；
- 误差传播必须包括计数、\(a_{\mathrm{geom}}\)、\(Q\) 和共享校准的协方差。

## What It Can Establish

Hamilton 直接核对的实验合同包括：

- 线偏振的计数定义与 \(P(\theta)\)；
- 多探测器结构：散射体、吸收体以及 \(\Omega=0^\circ,90^\circ\) 的方向选择；
- 分辨率、偏振灵敏度和全能峰效率之间的折衷；
- 两个吸收体可以提高效率并降低部分系统误差，但相对效率仍需无偏振源测量；
- \(Q\) 需要强偏振参考线标定；
- 能量门和散射角门可以降低 Compton 本底，但会损失峰计数；
- \(P(90^\circ)\) 的理论值必须与角分布系数和取向条件共同解释。

当前代码 `system/scripts/analysis/clover_compton_addback_polarization_calculator.py`
返回：

- `corrected_asymmetry_A`；
- `polarization_sensitivity_Q`；
- `linear_polarization_P`；
- `geometric_factor_a_geom` 及其不确定度传播；
- `response_contract` 和 `evidence_level: conditional-candidate-only`。

## What It Cannot Establish Alone

一个正或负的 \(P\)、\(A\) 或 \(A/Q\) 不能单独确认 \(E\)/\(M\) 多极性、宇称或
wobbling/chirality。响应参数若来自经验占位式，输出只能作为方法演示。不同阵列、
能量、散射角门、阈值和 add-back 逻辑之间不能直接移植 \(Q\)。

Hamilton PDF p. 718 明确强调灵敏度与效率存在折衷；PDF p. 719 说明不同敏感体积、
相对效率和阈值会使 \(Q\) 的直接计算困难，因此必须把校准数据作为第一类输入。

## Counter-evidence and Competing Interpretations

- 多极混合会改变偏振的大小和方向；相同符号可能对应不同 \(\delta\)、取向或
  \(\Delta I\) 候选；
- 几何不对称、阈值和本底会改变 \(A\)，而 \(Q\) 只修正已定义的响应，不自动修正
  随机符合和未建模背景；
- 只使用一个吸收体可能降低效率和系统控制能力；多吸收体提高统计量但增加相对
  效率和响应一致性要求；
- 理论 \(P(\theta)\) 与实验 \(P_{\mathrm{exp}}\) 的比较需要统一角度、相位和固体角
  约定，不能直接把表中历史数值当现代 Clover 响应。

## Model Dependence

```text
alignment + multipole model
        -> P_theory(theta, delta)
counts + geometry + background
        -> A_exp
unpolarized calibration + polarized reference
        -> a_geom, Q, covariance
joint likelihood
        -> branch comparison, not automatic mode confirmation
```

## Limitations and Missing Evidence

本页核对的是 Hamilton 第 15 章的历史 Compton polarimeter 方法页，不是现代
EXOGAM、Gammasphere、AGATA 或 GRETINA 的完整响应模型。当前 Clover 代码的
\(Q(E_\gamma)\) 仍是经验占位参数化；后续应接入实际无偏振/强偏振标定谱、响应矩阵、
阈值、散射角接受度、随机本底和完整协方差。

## Sources

- [[book-hamilton-electromagnetic-interaction]]
- [[clover-compton-polarimetry-and-addback]]
- [[gamma-ray-linear-polarization]]
- [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]
