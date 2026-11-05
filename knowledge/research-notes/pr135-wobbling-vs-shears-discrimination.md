---
type: research-note
title: "135Pr 横向摆动与磁转动（剪刀机制）的条件判据与实验辨析"
aliases: [pr135-wobbling-vs-shears-discrimination, 135Pr transverse wobbling magnetic rotation discrimination]
created: 2026-10-28
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, garg-2019-135pr-polarization-erratum, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
created_from: Day26 deep doctoral investigation
promotion_target: magnetic-rotation
tags: [135Pr, transverse-wobbling, magnetic-rotation, shears, discrimination, erratum]
---

# 135Pr 横向摆动与磁转动（剪刀机制）的条件判据与实验辨析

## Research Trigger

在奇 $A$ 核 $^{135}\text{Pr}$ 的负宇称能带结构归属中，历史上存在深刻的物理争议：Matta 等人（PRL 114, 082501 (2015)）曾将该带解释为三轴原子核的**横向摆动运动（Transverse Wobbling, TW）**；而 Garg 等人（PRC 92, 054325 (2015)）则指出其电磁性质更符合**磁转动（Magnetic Rotation, MR / Shears）**。随后，Garg 等人于 2019 年发表偏振测量勘误（PRC 100, 069901(E)），修正了跨带跃迁的偏振不对称度。本笔记系统梳理横向摆动与磁转动的理论判据，以微观算符、多极纯度与能谱微商为基准，对 $^{135}\text{Pr}$ 的物理模式开展多极纯度、能谱微商与实验适用条件辨析。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| PR135-DIS-01 | $813.3\text{ keV}$ 跨带跃迁的偏振不对称度经 2019 勘误修正为 $P = +0.04(3)$（旧值为 $-0.20(8)$），$R_{\text{DCO}} = 0.22(2)$ | 直接实验数据 | Garg 2019 PRC 100, 069901(E) p.1 | 勘误修正了能量响应因子 $a(E_\gamma)$，确定其为弱偏振正值 |
| PR135-DIS-02 | 基于康普顿探测灵敏度 $Q \approx 0.22$ 与高斯取向假设（$\sigma/I \approx 0.3$），偏振不对称度 $\Delta=+0.04(3)$ 在一阶近似下对应小混合比 $\delta(E2/M1) \sim 0.1-0.2$ 与大 $M1$ 分额 | 导出模型相关量 | 本工作工件 `pr135-mixing-ratio-polarization-bounds-059` | 混合比提取严格依赖核取向参数 $\sigma/I$ 与退取向系数，非孤立无模型直接测量；详细边界见 [[pr135-mr-crossing-racah-polarization-source-boundary]] |
| PR135-DIS-03 | 候选摆动能量 $E_{\text{wob}} = E(I, n_w=1) - \frac{1}{2}[E(I+1) + E(I-1)]$ 从 $27/2^-$ 的 $-43.5\text{ keV}$ 急剧上升至 $35/2^-$ 的 $+424.5\text{ keV}$ | 实验能级差推导 | 本工作工件 `pr135-wobbling-vs-magnetic-rotation-063` | 与横向摆动预言的 $E_{\text{wob}}$ 随自旋单调下降截然相反，反映了 3qp 向 5qp 的能带交叉 |
| PR135-DIS-04 | 实验未测得横向摆动标志性的跨带增强 $B(E2)_{\text{out}} / B(E2)_{\text{in}} \sim 0.5 - 2.0$，仅测得巨大的 $B(M1)/B(E2) \sim 15 - 95(\mu_N/e\text{b})^2$ | 电磁比值实验对账 | Garg 2015 PDF p.7 Table I; Matta 2015 | 跨带 $E2$ 线极其微弱，受检出限与背景制约 |

## Provisional Reasoning

### 1. 横向摆动与磁转动的核心判据对照

| 物理可观测量 | 横向摆动理论预言（TW） | 磁转动理论预言（MR / Shears） | $^{135}\text{Pr}$ 实测结果与裁决 |
|---|---|---|---|
| **跨带跃迁主导多极性** | 强烈集体电四极 $E2$（伸展或混合） | 磁偶极 $M1$ 主导（带间微弱 $E2$ crossover） | 在声明的取向与响应假设下，条件反演偏向 M1-rich 分支；不能把该分支直接当作无模型纯度测量 |
| **电四极跃迁比 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$** | 显著增强：$0.5 \sim 2.0$（1-声子退激特征） | 极度压低：$\ll 0.1$（单粒子级别交叉跃迁） | 公开材料未提供完整 partner-resolved absolute $B(E2)$；缺失/弱分支会降低简单 TW 解释的支持度，但不能单独排除所有摆动机制 |
| **能量差演化趋势 $E_{\text{wob}}(I)$** | 随自旋增加单调减小（声子软化） | 受剪刀闭合与能带交叉主导 | **随自旋从 $-43.5\text{ keV}$ 激增至 $+424.5\text{ keV}$**，在固定三轴转子图像下不利于简单 TW 解释 |
| **核形变几何环境** | 显著稳定的三轴形变（$\gamma \approx 20^\circ-30^\circ$） | 近球形或弱四极形变（$\beta_2 \le 0.15$） | 微观计算 $\beta_2 \approx 0.12-0.15$，弱形变支持剪刀相干 |

### 2. 偏振勘误对摆动运动解释的条件性约束

在 Matta 2015 的早期工作中，作者依据当时的偏振不对称度（旧值 $-0.20(8)$）和其它观测提出横向摆动解释。
然而，2019 年 Garg 等人查明康普顿散射仪的能量效率校准因子 $a(E_\gamma)$ 存在偏差，修正后的真值为 $P = +0.04(3)$。
依据独立验证工件 `pr135-mixing-ratio-polarization-bounds-059.py/json`：
- 修正后的偏振将多极混合比限定在 $\delta(E2/M1) \in [0.10, 0.19]$；
- 辐射场中的 $M1$ 强度占比超过 $96.5\%$，而摆动模式所必需的集体 $E2$ 辐射强度被限制在 $< 3.5\%$ 的极低背景水平；
- 这会在该取向、响应和误差合同下显著削弱“大 $E2$ 连接”这一支持链，但不能替代统一 response/covariance 重分析，也不能单独排除所有横向摆动解释。

### 3. 能级演化本质：准粒子顺对齐能带交叉

依据工件 `pr135-wobbling-vs-magnetic-rotation-063.py/json` 对能级差的计算：
所谓“摆动能级差”从自旋 $27/2^-$ 的 $-43.5\text{ keV}$ 变到 $35/2^-$ 的 $+424.5\text{ keV}$（变化近 $500\text{ keV}$）。这一非线性跳跃与转动频率 $\hbar\omega \approx 0.37\text{ MeV}$ 处的 **Coriolis 3qp $\to$ 5qp 能带交叉**相容，但这里仍是模型解释：
- 对齐质子对导致有效质子叶片由 $5.5\hbar$ 跃迁至 $11.5\hbar$；
- 剪刀角由濒临完全闭合突发性重新打开至 $\sim 88^\circ$；
- 剪刀角重开为 $B(M1)/B(E2)$ 在 $35/2^-$ 附近反弹和能谱间距扩张提供了一个模型解释；这些相对量不是绝对 $B(M1)$ 或 $B(E2)$ 测量。

## Open Questions

1. 高自旋能带交叉后更高的能级（$I > 39/2^-$）是否存在残余的三轴扰动或手征几何分岔？
2. 能否通过 Doppler Shift Attenuation Method (DSAM) 直接测定该能带的绝对能级寿命，提取出绝对 $B(M1)$ 强度以实现对剪刀开角完全闭合与重新张开的绝对微观定标？

## Assumptions

分析假定核芯处于弱四极形变环境（$\beta_2 \approx 0.12 - 0.15$），探测器康普顿偏振灵敏度取典型高纯锗 Clover 阵列参数 $Q \approx 0.22$；自旋宇称与能级差严格基于 Garg 2015 与 2019 勘误报告。

## Competing Explanations

横向摆动（TW）、纵向摆动（LW）、手征转动与磁转动（MR）都是需要比较的候选假说；偏振勘误和相对强度系统学提高了 MR/剪刀解释的权重，但仍保留响应、绝对寿命和组态混合边界。

## Transfer Conditions

本判据体系可迁移到 $A\approx 130$ 质量区其它奇 $A$ 候选，但每个核素都必须重新建立 transition identity、偏振响应、取向/feeding、绝对寿命和 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ 合同。

## Failure Conditions

若未来的寿命和绝对电磁强度显示带间 $E2$ 存在集体增强，或共同响应分析偏向电多极分支，则当前 MR 优先级判断需要重新审视。

## Falsification or Reverse Tests

利用独立验证程序 `pr135-wobbling-vs-magnetic-rotation-063.py` 与 `pr135-mixing-ratio-polarization-bounds-059.py` 进行偏振混合比与能谱微商多角度计算，数值工件保存于相应 JSON 文件。

## Knowledge Impact and Learning Decision

`supports` 在声明的取向/响应合同下 MR/剪刀重对齐解释的相对优先级；`revises` 把旧偏振值当作大 $E2$ 排他证据的做法；`limits` 任何由偏振或相对强度推导的混合比与模式排序。本笔记由 Codex self-audit 驱动，保持 `unreviewed`。

## Sources

- [[garg-2015-135pr-magnetic-rotation]]
- [[garg-2019-135pr-polarization-erratum]]
- [[pr135-shears-dynamics-bandcrossing-rebound]]
- [[mr-amr-observable-matrix-boundary]]

## Review Status

自主研学产物，未进行人工审核。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，系统化建立摆动对决磁转动的排他性实验判据。
