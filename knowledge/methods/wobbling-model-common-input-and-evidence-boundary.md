---
type: method
title: "冻结对齐摆动模型的共同输入与证据边界"
aliases: [wobbling common-input audit, frozen-alignment HFA contract]
method_type: "model-consistency-and-evidence-boundary"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Cross-check of A_m/A_s/A_l and J_m/J_s/J_l frozen-alignment harmonic implementations"
confidence: "high for algebraic cross-checks; low for experimental mode inference"
tags: [wobbling, transverse-wobbling, longitudinal-wobbling, TiP, common-input, model-boundary]
sources: [book-petrache-chirality-and-wobbling, book-bohr-mottelson-nuclear-structure-vol2]
---

# 冻结对齐摆动模型的共同输入与证据边界

## Purpose

统一仓库中以转动常数 \(A_k\) 和以转动惯量 \(\mathcal J_k\) 表示的冻结对齐
谐摆动实现，避免裸的 `A1/A2/A3` 在不同代码中隐含不同轴标签。

## Inputs and Assumptions

- 公共轴约定为 \(m,s,l\)，满足
  \[
  \mathcal J_m>\mathcal J_s>\mathcal J_l,
  \qquad
  A_m<A_s<A_l,
  \qquad
  A_k=\frac{\hbar^2}{2\mathcal J_k}.
  \]
- TW 的冻结准粒子沿短轴，使用
  \[
  \bar A_s=A_s(1-j/I),
  \qquad
  \hbar\omega_{\mathrm{TW}}
  =2I\sqrt{(A_m-\bar A_s)(A_l-\bar A_s)}.
  \]
- LW 的对应参考式以 \(\bar A_m=A_m(1-j/I)\) 替代对齐轴的转动常数；
 具体粒子-转子模型仍需明确其组态和核芯角动量定义。
- 这里的 \(I\) 是冻结对齐谐近似中的经典高自旋输入；它不等于完整有限自旋
  QTR/TPSM/TAC 计算的自动替代。

对于 Bohr–Mottelson 水动力学惯量，代码允许 Lund 区间
\(0^\circ\le\gamma\le60^\circ\)，但返回值始终按命名轴排序为
\((A_m,A_s,A_l)\)。在 \(\gamma>30^\circ\) 时，原始 \(k=(1,2,3)\) 数字轴中的
短轴/长轴标签需要交换；代码通过 `axis_permutation_applied` 和
`raw_k_axis_mapping` 留下这一转换。端点只报告 \(J_m=J_s\) 或 \(J_s=J_l\)
的轴对称关系，不从 \(\kappa\) 数值单独推断 prolate/oblate 形状名称。

## What It Can Establish

共同输入对账可以：

- 检查 \(A\)-表示和 \(J\)-表示是否给出相同的 HFA 频率；
- 定位 \(I=I_c\) 的 \(\omega_w=0\) 软化点；
- 区分 `stable_harmonic`、`critical_softening` 和
  `HFA_unstable_requires_full_model` 三种计算状态；
- 报告频率斜率、局部非单调性和 \(B(E2)\) 代理量作为模型描述符。

当前代码接口：

```text
system/scripts/analysis/davydov_wobbling_rotor_calculator.py
  frauendorf_wobbling_frequency(...)

system/scripts/analysis/triaxial_wobbling_tip_chiral_analyzer.py
  calculate_transverse_wobbling_spectrum(...)

system/scripts/analysis/odd_a_transverse_longitudinal_wobbling_stability_solver.py
  OddAWobblingStabilitySolver
```

同一组 \(A_m,A_s,A_l,I,j\) 的交叉回归已加入
`system/tests/test_wobbling_common_input.py`。旧的电磁筛选函数现在返回
条件性模型状态，不再返回实验确认标签。

## What It Cannot Establish Alone

- \(I>I_c\) 只说明冻结对齐 HFA 失稳，不能自动命名为 TiP、flip mode、
  粒子重取向或构型混合；
- 频率下降、上升或先升后降不能单独确认 TW/LW；
- \(B(E2)\) 代理、混合比阈值和单个近简并能级不能确认实验模式；
- 手征性还需要相同宇称、共同组态、带间/带内电磁矩阵元、寿命和竞争模型；
- \(\gamma\) 变化会重新排序主轴，固定 \(m,s,l\) 标签的 hydrodynamic 输入不能
  在未做轴交换时直接外推到整个 \(0^\circ<\gamma<60^\circ\) 区间；应使用
  `hydrodynamic_inertia_contract(...)` 保留转换元数据。

## Counter-evidence and Competing Interpretations

同一能量趋势可由 TiP、\(\gamma\)-软核、旋称伙伴、两准粒子构型混合或完整
粒子-转子解产生。实际分析应把频率、\(B(E2)\)、\(B(M1)\)、\(\delta\)、偏振、
寿命和 feeding 放入共同响应合同，并保存误差和上限。

## Verification

2026-11-03：

- 统一前后 \(I=10.5,\ j=6.5,\ (A_m,A_s,A_l)=(12,25,45)\) keV 的 TW
  频率交叉对账通过；
- \(I=13.5\) 的同一输入被识别为 HFA 失稳，且 `mode_confirmed` 保持 `None`；
- Lawrie 方法页的 wobbling 能量式修正为加和形式；
- 水动力学惯量的 \(\gamma>30^\circ\) 短轴/长轴置换加入显式合同，并覆盖
  \(\gamma=0^\circ,30^\circ,40^\circ,60^\circ\)；
- 全分析回归脚本通过，新增共同输入测试通过。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[petrache-ch2-frauendorf-topological-wobbling-contract]]
- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[lawrie-tip-wobbling-discrimination]]
