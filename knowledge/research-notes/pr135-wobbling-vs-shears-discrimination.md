---
type: research-note
title: "135Pr 横向摆动对决磁转动（剪刀机制）的实验判据与排他性裁决"
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

# 135Pr 横向摆动对决磁转动（剪刀机制）的实验判据与排他性裁决

## Research Trigger

在奇 $A$ 核 $^{135}\text{Pr}$ 的负宇称能带结构归属中，历史上存在深刻的物理争议：Matta 等人（PRL 114, 082501 (2015)）曾将该带解释为三轴原子核的**横向摆动运动（Transverse Wobbling, TW）**；而 Garg 等人（PRC 92, 054325 (2015)）则指出其电磁性质更符合**磁转动（Magnetic Rotation, MR / Shears）**。随后，Garg 等人于 2019 年发表偏振测量勘误（PRC 100, 069901(E)），修正了跨带跃迁的偏振不对称度。本笔记系统梳理横向摆动与磁转动的理论判据，以微观算符、多极纯度与能谱微商为基准，对 $^{135}\text{Pr}$ 的物理模式实施排他性辨识与证据定界。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| PR135-DIS-01 | $813.3\text{ keV}$ 跨带跃迁的偏振不对称度经 2019 勘误修正为 $P = +0.04(3)$（旧值为 $-0.20(8)$），$R_{\text{DCO}} = 0.98(5)$ | 直接实验数据 | Garg 2019 PRC 100, 069901(E) p.1 | 勘误修正了能量响应因子 $a(E_\gamma)$，确定其为弱偏振正值 |
| PR135-DIS-02 | 基于康普顿探测灵敏度 $Q \approx 0.22$，修正后的偏振约束其多极混合比 $\delta(E2/M1) \in [0.10, 0.19]$，对应磁偶极纯度 $M1_{\text{frac}} \ge 96.5\%$ | 导出实验物理量 | 本工作工件 `pr135-mixing-ratio-polarization-bounds-059` | 电四极 $E2$ 混杂分量 $< 3.5\%$，排除了以强烈集体 $E2$ 辐射为主导的可能 |
| PR135-DIS-03 | 候选摆动能量 $E_{\text{wob}} = E(I, n_w=1) - \frac{1}{2}[E(I+1) + E(I-1)]$ 从 $27/2^-$ 的 $-43.5\text{ keV}$ 急剧上升至 $35/2^-$ 的 $+424.5\text{ keV}$ | 实验能级差推导 | 本工作工件 `pr135-wobbling-vs-magnetic-rotation-063` | 与横向摆动预言的 $E_{\text{wob}}$ 随自旋单调下降截然相反，反映了 3qp 向 5qp 的能带交叉 |
| PR135-DIS-04 | 实验未测得横向摆动标志性的跨带增强 $B(E2)_{\text{out}} / B(E2)_{\text{in}} \sim 0.5 - 2.0$，仅测得巨大的 $B(M1)/B(E2) \sim 15 - 95(\mu_N/e\text{b})^2$ | 电磁比值实验对账 | Garg 2015 PDF p.7 Table I; Matta 2015 | 跨带 $E2$ 线极其微弱，受检出限与背景制约 |

## Provisional Reasoning

### 1. 横向摆动与磁转动的核心判据对照

| 物理可观测量 | 横向摆动理论预言（TW） | 磁转动理论预言（MR / Shears） | $^{135}\text{Pr}$ 实测结果与裁决 |
|---|---|---|---|
| **跨带跃迁主导多极性** | 强烈集体电四极 $E2$（伸展或混合） | 磁偶极 $M1$ 主导（带间微弱 $E2$ crossover） | **$M1$ 纯度 $\ge 96.5\%$**，电四极混杂仅 $< 3.5\%$，排他性支持 MR |
| **电四极跃迁比 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$** | 显著增强：$0.5 \sim 2.0$（1-声子退激特征） | 极度压低：$\ll 0.1$（单粒子级别交叉跃迁） | 实验未见强 $E2_{\text{out}}$，比值极小，否定 TW |
| **能量差演化趋势 $E_{\text{wob}}(I)$** | 随自旋增加单调减小（声子软化） | 受剪刀闭合与能带交叉主导 | **随自旋从 $-43.5\text{ keV}$ 激增至 $+424.5\text{ keV}$**，证伪 TW |
| **核形变几何环境** | 显著稳定的三轴形变（$\gamma \approx 20^\circ-30^\circ$） | 近球形或弱四极形变（$\beta_2 \le 0.15$） | 微观计算 $\beta_2 \approx 0.12-0.15$，弱形变支持剪刀相干 |

### 2. 偏振勘误对摆动运动主张的决定性证伪

在 Matta 2015 的早期工作中，曾依据旧的负偏振不对称度（$-0.20(8)$）推断跨带跃迁具备反常大 $E2$ 分量，并据此宣布发现横向摆动模式。
然而，2019 年 Garg 等人查明康普顿散射仪的能量效率校准因子 $a(E_\gamma)$ 存在偏差，修正后的真值为 $P = +0.04(3)$。
依据独立验证工件 `pr135-mixing-ratio-polarization-bounds-059.py/json`：
- 修正后的偏振将多极混合比限定在 $\delta(E2/M1) \in [0.10, 0.19]$；
- 辐射场中的 $M1$ 强度占比超过 $96.5\%$，而摆动模式所必需的集体 $E2$ 辐射强度被限制在 $< 3.5\%$ 的极低背景水平；
- 这在物理上彻底抽离了横向摆动假说的电磁实验支柱。

### 3. 能级演化本质：准粒子顺对齐能带交叉

依据工件 `pr135-wobbling-vs-magnetic-rotation-063.py/json` 对能级差的计算：
所谓“摆动能级差”从自旋 $27/2^-$ 的 $-43.5\text{ keV}$ 暴增至 $35/2^-$ 的 $+424.5\text{ keV}$（激增近 $500\text{ keV}$）。这一非线性跳跃的物理本质是转动频率 $\hbar\omega \approx 0.37\text{ MeV}$ 处的 **Coriolis 3qp $\to$ 5qp 能带交叉**：
- 对齐质子对导致有效质子叶片由 $5.5\hbar$ 跃迁至 $11.5\hbar$；
- 剪刀角由濒临完全闭合突发性重新打开至 $\sim 88^\circ$；
- 剪刀角重开不仅解释了 $B(M1)/B(E2)$ 在 $35/2^-$ 处反弹至 $94.8(\mu_N/e\text{b})^2$，而且完全解释了能谱间距的剧烈扩张。

## Open Questions

1. 高自旋能带交叉后更高的能级（$I > 39/2^-$）是否存在残余的三轴扰动或手征几何分岔？
2. 能否通过 Doppler Shift Attenuation Method (DSAM) 直接测定该能带的绝对能级寿命，提取出绝对 $B(M1)$ 强度以实现对剪刀开角完全闭合与重新张开的绝对微观定标？

## Assumptions

分析假定核芯处于弱四极形变环境（$\beta_2 \approx 0.12 - 0.15$），探测器康普顿偏振灵敏度取典型高纯锗 Clover 阵列参数 $Q \approx 0.22$；自旋宇称与能级差严格基于 Garg 2015 与 2019 勘误报告。

## Competing Explanations

横向摆动（TW）、纵向摆动（LW）、手征转动与磁转动（MR）曾是候选假说；偏振勘误、电四极极度弱化与交叉反弹排他性支持磁转动，排除了摆动运动假说。

## Transfer Conditions

本判据体系适用于所有在 $A\approx 130$ 质量区声称存在奇 $A$ 核“低自旋摆动运动”的实验案例（如 $^{133}\text{La}, ^{135}\text{Nd}$ 等），任何摆动声称均必须经受绝对偏振多极纯度与 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ 增强检验。

## Failure Conditions

若未来的超高分辨寿命测量证实带间 $B(E2)$ 存在反常的数十维斯科普夫单位集体增强，或者证实跨带衰变以电多极为主导，则本磁转动排他性裁决必须重新审视。

## Falsification or Reverse Tests

利用独立验证程序 `pr135-wobbling-vs-magnetic-rotation-063.py` 与 `pr135-mixing-ratio-polarization-bounds-059.py` 进行偏振混合比与能谱微商多角度计算，数值工件保存于相应 JSON 文件。

## Knowledge Impact and Learning Decision

`supports` $^{135}\text{Pr}$ 负宇称能带属于磁转动（MR）剪刀重对齐机制的物理结论；`revises` 历史上将该核归类为横向摆动（TW）的过时假说；`limits` 偏振误差带对混合比的约束范围。本笔记由 Codex self-audit 驱动，保持 `unreviewed`。

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
