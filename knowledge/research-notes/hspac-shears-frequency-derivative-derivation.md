---
type: research-note
title: "HSPAC 剪刀模型中能量与频率的代数关系：4Î 导数偏差的严格解析与根因定位"
aliases: [HSPAC derivative derivation, 4I-hat frequency discrepancy, Rajbanshi 2018 frequency formula audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
evidence_sources: [rajbanshi-2018-extremely-asymmetric-shears-143sm]
created_from: Day27 continued theoretical investigation of modified SPAC and shears-plus-core dynamics
promotion_target: ""
tags: [HSPAC, SPAC, shears-mechanism, 143Sm, mathematical-derivation, analytical-reconstruction]
---

# HSPAC 剪刀模型中能量与频率的代数关系：$4\hat{I}$ 导数偏差的严格解析与根因定位

## Research Trigger

在对 $^{143}\text{Sm}$ 极不对称剪刀带（DB III）原始文献 [[rajbanshi-2018-extremely-asymmetric-shears-143sm]]（PRC 98, 061304(R)）及其方法基础 S. Rajbanshi 2017（arXiv:1712.00353v1）的深度审读中，发现原印无量纲转动频率 $\hat{\omega}$ 公式与能量表达式 $\hat{E}(\hat{I}, \theta_1)$ 的正则偏导数之间存在表观为 $4\hat{I}$ 的代数不一致（RA18-8）。

为了将该模型推进为可复现数值拟合代码，必须严格判定该偏差究竟源于：（1）不同的频率定义或背景扣除；（2）角动量依赖核芯惯量 $\mathcal{J}(I)$ 的外层导数项；（3）代数推导中的印刷符号错误。

## Grounded Evidence

1. **文献能量表达式：** S. Rajbanshi 2017（arXiv:1712.00353v1）Eq. (2) 及 Rajbanshi 2018（PRC 98, 061304(R)）PDF p. 4 给出的无量纲能量为：
   \[
   \hat{E}(\hat{I}, \theta_1) = \hat{I}^2 + \frac{1+a^2}{4} - \frac{1}{2}\left[ \sqrt{4\hat{I}^2 - \sin^2\theta_1}(a + \cos\theta_1) + \sin^2\theta_1 \right] + \frac{a}{2}\cos\theta_1 + \frac{\chi}{4}\cos^2\theta_1 - \frac{\chi}{12}.
   \]
   其中 $\hat{I} = I/(2j_1)$，$a = j_2/j_1$，$\chi = 3v_2\mathcal{J}/j_1^2$。
2. **极小化驻点条件：** 能量对剪刀角 $\theta_1$ 的驻点条件 $\frac{\partial \hat{E}}{\partial \theta_1} = 0$ 在 $\sin\theta_1 \neq 0$ 时化简为 Rajbanshi 2017 Eq. (4)：
   \[
   \sqrt{4\hat{I}^2 - \sin^2\theta_1} + \frac{\cos\theta_1(a + \cos\theta_1)}{\sqrt{4\hat{I}^2 - \sin^2\theta_1}} - (2+\chi)\cos\theta_1 - a = 0.
   \]
3. **文献原印频率表达式：** Rajbanshi 2017 Eq. (5) 及 Rajbanshi 2018 PDF p. 5 印刷的无量纲转动频率为：
   \[
   \hat{\omega}_{\text{printed}} = 2\hat{I}\left( 1 - \chi + \frac{\sqrt{4\hat{I}^2 - \sin^2\theta_1} - a}{\cos\theta_1} \right).
   \]

## Provisional Reasoning

记 $S \equiv \sqrt{4\hat{I}^2 - \sin^2\theta_1}$。

### 1. 能量对自旋的正则偏导数
在固定剪刀角 $\theta_1$ 下，对无量纲能量 $\hat{E}$ 求偏导数：
\[
\frac{\partial S}{\partial \hat{I}} = \frac{8\hat{I}}{2\sqrt{4\hat{I}^2 - \sin^2\theta_1}} = \frac{4\hat{I}}{S}.
\]
代入 $\hat{E}(\hat{I}, \theta_1)$：
\[
\frac{\partial \hat{E}}{\partial \hat{I}} = 2\hat{I} - \frac{1}{2} \left[ \frac{\partial S}{\partial \hat{I}}(a + \cos\theta_1) \right] = 2\hat{I} - \frac{1}{2}\left( \frac{4\hat{I}}{S} \right)(a + \cos\theta_1) = 2\hat{I}\left( 1 - \frac{a + \cos\theta_1}{S} \right). \tag{A}
\]

根据包络定理（Envelope Theorem），在能面平衡轨迹上（$\frac{\partial \hat{E}}{\partial \theta_1} = 0$），全导数等于偏导数：
\[
\frac{d \hat{E}}{d \hat{I}} = \frac{\partial \hat{E}}{\partial \hat{I}} + \frac{\partial \hat{E}}{\partial \theta_1}\frac{d \theta_1}{d \hat{I}} = \frac{\partial \hat{E}}{\partial \hat{I}}.
\]

### 2. 驻点条件的在壳代换（On-shell Substitution）
由驻点条件 Eq. (4)：
\[
S + \frac{\cos\theta_1(a + \cos\theta_1)}{S} - a = (2+\chi)\cos\theta_1.
\]
两边同除以 $\cos\theta_1$（当 $\cos\theta_1 \neq 0$）：
\[
\frac{S - a}{\cos\theta_1} + \frac{a + \cos\theta_1}{S} = 2 + \chi.
\]
由此严格解出比值项：
\[
\frac{a + \cos\theta_1}{S} = (2 + \chi) - \frac{S - a}{\cos\theta_1}. \tag{B}
\]

### 3. 在壳严格导数
将式 (B) 代入正则导数式 (A)：
\[
\frac{d \hat{E}}{d \hat{I}} = 2\hat{I}\left( 1 - \left[ (2 + \chi) - \frac{S - a}{\cos\theta_1} \right] \right) = 2\hat{I}\left( 1 - 2 - \chi + \frac{S - a}{\cos\theta_1} \right) = 2\hat{I}\left( -1 - \chi + \frac{S - a}{\cos\theta_1} \right). \tag{C}
\]

## Root Cause of the Printed Formula Discrepancy

对比严格在壳导数式 (C) 与文献原印式 Eq. (5)：
\[
\hat{\omega}_{\text{printed}} = 2\hat{I}\left( \mathbf{+1} - \chi + \frac{S - a}{\cos\theta_1} \right),
\]
\[
\left(\frac{d \hat{E}}{d \hat{I}}\right)_{\text{exact}} = 2\hat{I}\left( \mathbf{-1} - \chi + \frac{S - a}{\cos\theta_1} \right).
\]

二者之差严格为常数：
\[
\hat{\omega}_{\text{printed}} - \left(\frac{d \hat{E}}{d \hat{I}}\right)_{\text{exact}} = 2\hat{I}\big( (+1) - (-1) \big) = 4\hat{I}.
\]

**根因判定：**
该偏差确认为**文献在化简括号内常数项时出现的印刷符号笔误**：在从 $1 - (2+\chi)$ 化简时，作者将 $1 - 2 = -1$ 误写为了 $+1$。不存在任何深奥的未知多体物理修正或非自洽惯量导数。

## Numerical Verification across 143Sm High-Spin States

通过独立数值验证脚本 `system/scripts/day27_hspac_derivative_derivation.py`，在 $^{143}\text{Sm}$ DB III 的 4 个实测高自旋态（$I = 51/2^-, 53/2^-, 55/2^-, 57/2^-$）以及对称剪刀控制用例下进行高精度数值校验：

| 状态 / 算例 | 总自旋 $I$ | $\hat{I}$ | $a$ | $\chi$ | 平衡剪刀角 $\theta_1$ | 正则解析导数 | 有限差分导数 | 原印 $\hat{\omega}$ | 差量 $\hat{\omega} - d\hat{E}/d\hat{I}$ | 理论值 $4\hat{I}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| 51/2− 态 | 25.5 | 2.8333 | 4.0 | 1.0 | $40.909^\circ$ | 0.878842 | 0.878842 | 12.212176 | 11.333333 | 11.333333 |
| 53/2− 态 | 26.5 | 2.9444 | 4.0 | 1.0 | $30.733^\circ$ | 1.010929 | 1.010929 | 12.788707 | 11.777778 | 11.777778 |
| 55/2− 态 | 27.5 | 3.0556 | 4.0 | 1.2 | $29.390^\circ$ | 1.224029 | 1.224029 | 13.446251 | 12.222222 | 12.222222 |
| 57/2− 态 | 28.5 | 3.1667 | 4.0 | 1.4 | $28.180^\circ$ | 1.438236 | 1.438236 | 14.104902 | 12.666667 | 12.666667 |
| 对称控制态 | 8.5 | 0.8500 | 1.0 | 0.5 | $75.709^\circ$ | 0.182462 | 0.182462 | 3.582462 | 3.400000 | 3.400000 |

所有状态下：
1. 正则解析偏导数与平衡轨迹上的两点中心有限差分导数在 $10^{-8}$ 精度内完全重合，确证包络定理成立；
2. 原印公式与真实能量导数差量在 $10^{-10}$ 精度内严格等于 $4\hat{I}$。

## Assumptions

1. 单个准粒子叶片沿核芯转轴，另一叶片在主平面内转动，遵循 HSPAC 平面几何；
2. 假定核芯惯量 $\mathcal{J}$ 在求偏导时作为状态参数固定，或自旋依赖由 $\chi(I)$ 离散点表征。

## Competing Explanations

1. **假设一（符号笔误）：** 推导中 $1 - (2+\chi) = -1 - \chi$ 被印刷误写为 $1 - \chi$。本笔记的代数推导与 $4\hat{I}$ 完全匹配强有力支持该解释。
2. **假设二（不同频率标度）：** 假定 $\hat{\omega}$ 定义包含了某种人为平移。但由于 $4\hat{I}$ 是随自旋线性变化的量而非固定常数，平移会导致转动惯量 $\mathcal{J}^{(2)}$ 的斜率发生物理畸变，故排除单纯常数平移假说。

## Transfer Conditions

在任何使用 HSPAC / modified SPAC 模型进行能量—频率联合拟合的数值程序中，必须采用正确导数式 (C)；若使用原印公式 (5)，算出的无量纲频率将被系统性虚假抬高 $4\hat{I}$。

## Failure Conditions

当剪刀叶片出现非共面三维手征转动（$J_l \neq 0$）或质子-质子空穴吸引项 $V_{\pi\pi}$ 占主导时，单角度驻点方程需扩展为二阶张量方程，本一维导数关系不再适用。

## Falsification or Reverse Tests

运行可复现验证脚本：
```bash
python3 system/scripts/day27_hspac_derivative_derivation.py --output-dir outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/hspac-derivation
```
检查输出 `hspac_derivative_resolution.json` 中所有状态的 `proof_status` 是否全绿通过。

## Open Questions

在 Rajbanshi 2018 原论文的实际 Fortran/C 计算代码中，作者使用的是正确的导数式 (C) 还是印刷错误的公式 (5)？这可以通过对比其实际计算曲线在自旋 $57/2^-$ 处的斜率做进一步判定。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 Codex 基于原始预印本与期刊论文开展的 self-audit，保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-10-29：基于 Rajbanshi 2017/2018 原始公式完成代数与数值闭环推导，成功定位 $4\hat{I}$ 偏差起源，彻底闭合 RA18-8 待核项。

## Agent Self-Audit Triage

- **P0: none identified.** 数学推导完全闭合，数值验证全绿。
- **P1:** 需进一步核验该符号纠正对实际 $^{143}\text{Sm}$ 实验频率拟合曲线的定量影响程度。
- **P2/P3:** 保持标准 schema 规范与 source 交叉索引。
