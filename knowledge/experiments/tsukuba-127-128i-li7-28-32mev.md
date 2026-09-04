---
type: experiment
title: "University of Tsukuba 124Sn(7Li,xn)127,128I in-beam gamma spectroscopy experiment"
aliases: ["124Sn 7Li 4n 127I 32 MeV", "124Sn 7Li 3n 128I 28 MeV", "Ding 2012 127,128I Experiment", "日本筑波大学串列加速器 127,128I 实验"]
created: 2026-09-02
updated: 2026-09-02
status: active
review_status: unreviewed
experiment_id: tsukuba-127-128i-li7-28-32mev
facility: University of Tsukuba tandem accelerator
beam: 7Li
target: 124Sn
beam_energy: "28 MeV (128I, 3n); 32 MeV (127I, 4n)"
reaction: 124Sn(7Li,4n)127I
additional_reactions: [124Sn(7Li,3n)128I]
evaporation_channel: "3n at 28 MeV; 4n at 32 MeV"
residual_nuclei: [127i, 128i]
detector_array: 9 BGO Compton-suppressed HPGe detectors + 1 planar HPGe detector
data_status: published
sources: [ding-2012-phd-thesis-127-128i-high-spin]
tags: [fusion-evaporation, in-beam-gamma-spectroscopy, gamma-gamma-coincidence, ado-ratio, a130]
---

# University of Tsukuba $^{124}\text{Sn}({}^7\text{Li}, x\text{n})^{127, 128}\text{I}$ 在束 $\gamma$ 谱学实验

## Identity

丁兵 2012 年博士学位论文中的在束 $\gamma$ 谱学实验。实验在日本筑波大学串列加速器上进行，通过重离子熔合蒸发反应研究过渡区奇 $A$ 核 $^{127}\text{I}$ 和双奇核 $^{128}\text{I}$ 的高自旋态能级结构。

## Beam, Target and Reaction

- **加速器与束流**：日本筑波大学串列加速器提供的 $^7\text{Li}$ 离子束；28 MeV 用于布居 $^{128}\text{I}$ 的 3n 道，32 MeV 用于布居 $^{127}\text{I}$ 的 4n 道。
- **靶材料**：富集 $^{124}\text{Sn}$ 同位素靶。
- **反应道**：
  - $^{124}\text{Sn}({}^7\text{Li}, 4\text{n})^{127}\text{I}$（32 MeV）
  - $^{124}\text{Sn}({}^7\text{Li}, 3\text{n})^{128}\text{I}$（28 MeV）

## Detector Configuration

- 阵列由 9 套带有 BGO 反康普顿屏蔽的同轴 HPGe 探测器和 1 套小平面 HPGe 探测器（灵敏区薄，专门用于测量低能 $\gamma$ 和 X 射线）组成。
- 5 套 HPGe 探测器位于相对束流约 $37^\circ$ 或 $143^\circ$，其余探测器位于约 $90^\circ$，用于提取 ADO 系数并进行符合测量。
- 使用 $^{152}\text{Eu}$ 和 $^{133}\text{Ba}$ 标准源进行能量与相对效率刻度；$^{60}\text{Co}$ 的 1332 keV 线用于检查探测器能量分辨率。

## Multipolarity Analysis

- 论文第四章介绍 DCO 与 ADO 两种符合分析方法；本论文对 $^{127}\text{I}$ 和 $^{128}\text{I}$ 的实际多极性指认采用 ADO 系数。
- 实验中纯四极跃迁的 ADO 系数约为 $1.29$，纯偶极跃迁约为 $0.64$，混合跃迁位于两者之间；表 5.1 和表 6.1 的实验列标记为 $R_{\text{ADO}}$。

## Known Limitations

- 实验未测量跃迁寿命（未开展 DSAM 或 RDDS 线形分析），也未配备康普顿散射线偏振计；
- 宇称与组态的确定结合了 ADO 多极性、带间/带内强度比、内转换系数、系统学演化规律以及理论 PES/NPA 计算。

## Sources

- [[ding-2012-phd-thesis-127-128i-high-spin]]：D12-1 至 D12-11，第 3-6 章；实验装置与 ADO 方法见 PDF p.57（印刷页 49）。
