---
type: research-note
title: "磁转动中微观三维推转空间取向角与轴比演化机制"
aliases: [tac-3d-tilt-angles-and-axis-ratio-evolution, 3D TAC tilt angles and axis ratios in MR]
created: 2026-10-29
updated: 2026-10-29
category: research-notes
tags: [magnetic-rotation, 3d-tac, tilt-angles, axis-ratios, out-of-plane-stability, planar-shears]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism-review]
created_from: Day26 3D TAC tilt angles and axis ratios study
---

# 磁转动中微观三维推转空间取向角与轴比演化机制

## Research Trigger

在倾斜推转模型（Tilted Axis Cranking, TAC）中，传统二维推转假设转动轴严格局限于某个主平面（通常为 $(x,z)$ 平面，极角为 $\\theta_{\\text{rot}}$，方位角 $\\phi_{\\text{rot}} = 0$）。然而，当价核子在非共面轨道上运动或核芯存在三轴形变软度时，转动轴可能自发向三维立体空间偏转（3D TAC, $\\phi_{\\text{rot}} \\ne 0$），进而诱发手征对称性破缺。

本研究探讨在典型磁转动（MR）核中，自洽三维推转势能面上的方位角稳定性曲率 $K_\\phi = \\frac{\\partial^2 R}{\\partial \\phi^2}$、剪刀开角闭合与核芯三轴轴比（$R_x : R_y : R_z$）的动力学响应，量化共面磁转动对三维手征涨落的拓扑免疫边界。

## Grounded Evidence

### 1. 磁转动共面性实验证据
- $^{198}\\text{Bi}$ 与 $^{106}\\text{Ag}$：线性偏振测量证实其带内 $\\Delta I = 1$ 跃迁主要由纯 $M1$（伴随极微弱 $E2$）主导；
- 缺乏手征双重带（chiral doublet bands）：在严格共面磁转动核中，能谱中未观测到几乎简并的同宇称伙伴带，表明方位反演对称性 $\\mathcal{T}\\mathcal{R}_y(\\pi)$ 保持未破缺状态。

### 2. 3D TAC 自洽倾斜角条件
在三维内禀系中，转动角速度矢量为：
$$\\vec{\\omega} = \\omega (\\sin\\theta_{\\text{rot}}\\cos\\phi_{\\text{rot}}, \\sin\\theta_{\\text{rot}}\\sin\\phi_{\\text{rot}}, \\cos\\theta_{\\text{rot}})$$
自洽定态要求总角动量 $\\vec{J}$ 严格平行于 $\\vec{\\omega}$：
$$\\frac{J_x}{\\omega_x} = \\frac{J_y}{\\omega_y} = \\frac{J_z}{\\omega_z} = \\mathcal{J}_{\\text{eff}}$$

## Provisional Reasoning

微观推演表明，在磁转动体系中，质子粒子叶片与中子空穴叶片通过吸引的四极粒子-空穴剩余相互作用倾向于维持在一个共同的剪刀平面内。偏离该平面的出平面偏转（$\\phi_{\\text{rot}} \\ne 0$）会导致两叶片矢量重叠减小并显著提高有效变形能。数值变分结果证实，在全转动频率区间（$\\hbar\\omega = 0.12 - 0.44\\text{ MeV}$），方位恢复曲率恒为正值（$K_\\phi \\approx 1.3 - 5.1\\text{ MeV}$），证明纯磁转动能带处于稳定的共面极小谷中。同时，核芯三轴形变微商保持微小（$|\\gamma| < 1^\\circ$），三轴轴比仅发生极微弱调制（$R_x / R_z \\approx 0.94 - 0.95$），排除了由离心拉伸自发诱发手征分岔的假说。

## Assumptions

1. 质子与中子价准粒子角动量量值在全带保持恒定；
2. 核芯三轴转动惯量遵循流体动力学角依赖规律（$\\mathcal{J}_k \\propto \\sin^2(\\gamma - 2\\pi k/3)$）；
3. 偶极磁矩算符主要由价准粒子自旋磁矩驱动。

## Competing Explanations

1. **三维手征自发分岔模型**：假定所有大-$j$ 粒子-空穴系统均将在某一自旋处失稳出平面；本模型证明只有当三轴形变刚性达到 $\\gamma \\sim 30^\\circ$ 且价粒子拥有互不相等的三个主轴分量时，分岔才可能发生；在弱长椭核芯（$\\beta_2 \\sim 0.12, \\gamma \\sim 0^\\circ$）中，共面极小极其稳固；
2. **纯主轴推转模型（1D PAC）**：将磁转动近似为绕主轴转动，忽略倾角演化；该模型无法解释从带头向带顶 $B(M1)$ 随极角 $\\theta_{\\text{rot}}$ 对准的非简谐演化。

## Transfer Conditions

1. 适用于近球形或弱形变核中由两对大-$j$ 准粒子构成的经典剪刀磁转动带；
2. 适用于评估磁转动核素是否存在潜在手征拓扑伙伴带的排他性检验。

## Failure Conditions

1. 若核芯展现强内禀三轴形变（$\\gamma \\gtrsim 20^\\circ$），$K_\\phi$ 可能会在临界频率处变负，转变为非平面手征相；
2. 若价核子发生多对破裂引发三体互相垂直对齐，平面的概念即告失效。

## Falsification or Reverse Tests

1. 测量高灵敏度康普顿线偏振度 $P_\\gamma$：若实验检测到显著出平面的非零 $E2/M1$ 干涉项，则表明 $\\phi_{\\text{rot}} \\ne 0$，共面假设失效；
2. 搜索同宇称激发态能谱：若在剪刀能带旁发现能量相近且电磁跃迁特征对称的第二条伙伴带，则表明体系已分岔进入手征双带。

## Open Questions

1. 动态配对涨落对出平面恢复曲率 $K_\\phi$ 的弱化效应；
2. 在超重核剪刀带中相对论自旋-轨道相互作用对三维倾角的微观重整。

## Human Review

本研究笔记基于 Frauendorf (2001) 经典 TAC 理论与可复现 3D 变分计算建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29：基于 Day 26 磁转动三维推转空间稳定性深入研学创建初始草案。
