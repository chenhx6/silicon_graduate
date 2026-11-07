---
type: experiment
title: "先进伽马跟踪阵列（AGATA）"
aliases: [AGATA, Advanced Gamma Tracking Array, 4pi 锗跟踪阵列]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
experiment_id: europe-agata-collaboration
facility: European Collaboration (LNL Legnaro, GANIL, GSI/FAIR)
accelerators: [piave-alnico-lnl, spiral2-ganil, gsi-sis18]
detector_arrays: [agata-segmented-hpge-tracking-array]
data_status: operational-international-flagship
sources: []
tags: [agata, gamma-tracking, segmented-hpge, pulse-shape-analysis, relativistic-doppler]
---

# 先进伽马跟踪阵列（Advanced GAmma Tracking Array, AGATA）

## Concept and Tracking Principle

AGATA 是欧洲大型核物理合作组研发的新一代 $4\pi$ 空间立体角全吸收**先进伽马跟踪谱仪（Gamma Tracking Array）**。与依赖物理 BGO 屏蔽准直的传统 Compton 抑制阵列不同，AGATA 彻底取消了死角庞大的物理屏蔽体，完全由高度分段（Segmented）的密排大体积六角形高纯锗晶体构成一个封闭球壳（最终目标由 180 个 36 段灵敏体积的 HPGe 晶体组成）：

1. **脉冲形状分析（Pulse Shape Analysis, PSA）**：通过数字化超快采样记录 36 个微段及中心电极的感应电荷波形，利用微观 Shockley-Ramo 电场矩阵反演，将每一个 $\gamma$ 光子在晶体内部多次康普顿散射的相互作用三维坐标定位至毫米量级（$\Delta x \approx 2\text{--}4\text{ mm}$）；
2. **伽马径迹重构算法（Tracking Algorithms）**：根据 Compton 散射能量-角度相干公式与光电效应截面，在计算机算法层面对杂乱无章的离散击中点进行因果时间顺序重构，彻底重建初始入射 $\gamma$ 光子的能量与入射矢量，将峰总比（P/T）提升至 $60\%$ 以上，全能峰探测效率达到 $35\%\sim 40\%$。

## Breakthroughs for In-Beam Nuclear Physics

- **彻底解决相对论多普勒展宽**：当放射性核束反应产物的反冲速度高达 $\beta = v/c \sim 0.1 \sim 0.5$ 时，传统大角度探测器的开角展宽会彻底摧毁能量分辨率；AGATA 毫米级的三维位置灵敏度将有效张角缩小到 $1^\circ$ 以下，使快速反冲核发射的 $\gamma$ 峰分辨率恢复至同轴 HPGe 的本征极限（$\sim 2\text{ keV}$）；
- **超强线偏振与低截面灵敏度**：每个分段晶体内部的第一次与第二次散射点自然构成理想的康普顿散射仪（Compton Polarimeter），偏振测量灵敏度较传统阵列提升一个数量级。
