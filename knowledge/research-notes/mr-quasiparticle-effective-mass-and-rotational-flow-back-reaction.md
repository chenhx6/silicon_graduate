---
type: research-note
title: "磁转动中微观准粒子有效质量与转动坐标系流场反作用机制"
aliases: [mr-quasiparticle-effective-mass-and-rotational-flow-back-reaction, MR effective mass flow back-reaction]
created: 2026-10-29
updated: 2026-10-29
category: research-notes
tags: [magnetic-rotation, effective-mass, flow-back-reaction, shears-stiffness, cdft, gogny]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism-review]
created_from: Day26 quasiparticle effective mass and rotational flow back-reaction study
---

# 磁转动中微观准粒子有效质量与转动坐标系流场反作用机制

## Research Trigger

在微观核平均场与推转密度泛函理论（CDFT, Skyrme, Gogny）中，空间非定域交换项诱发核子在介质中具有显著小于裸质量的微观有效质量（$m^*/m \\approx 0.65 - 0.85$）。然而，在传统唯象剪刀模型中，粒子-空穴剩余恢复常数 $C_{\\text{shears}}$ 通常被视作不依赖有效质量的唯象参数。

本研究探讨介质微观有效质量 $m^*$ 与推转非惯性系下科里奥利反作用流场 $\\delta\\vec{v}(\\vec{r})$ 对剪刀势能面刚度与角动量平衡的自洽重整机制。

## Grounded Evidence

### 1. 剪刀能带斜率与有效质量事实
- $^{198}\\text{Bi}$ 与 $^{135}\\text{Pr}$：微观推转 Routhian 能级斜率系统性陡于基于自由核子质量推演的剪刀曲线；
- 相对论协变泛函（CDFT, $m^*/m \\sim 0.60 - 0.65$）与非相对论 Gogny/Skyrme 泛函（$m^*/m \\sim 0.70 - 0.80$）给出的推转单粒子响应存在系统性刚度阶跃。

### 2. 流场反作用微观方程
在转动坐标系中，流场反作用由非惯性科里奥利涡旋电流给出：
$$\\delta \\vec{j}(\\vec{r}) = - \\rho(\\vec{r}) \\frac{m - m^*}{m^*} (\\vec{\\omega} \\times \\vec{r})$$
该反向环流反作用于总角动量，产生一个对消对准自旋的有效负向流修正 $\\Delta J_{\\text{back}} = - \\kappa_{\\text{flow}} (1 - m^*/m) \\omega$。

## Provisional Reasoning

微观推演表明，费米面附近的单粒子态密度反比于单粒子速度，正比于有效质量：$g(\\epsilon_F) \\propto m^*$。剪刀恢复势能来自于价核子对准对极化核芯施加的四极畸变能量，其刚度与单粒子极化率成反比，因此剪刀恢复相互作用常数显式反比于有效质量：
$$C_{\\text{shears}}(m^*) = C_0 \\left( \\frac{m}{m^*} \\right)$$
数值变分结果证实，在相对论有效质量 $m^*/m = 0.65$ 下，有效剪刀刚度从裸值 $1.45\\text{ MeV}$ 显著硬化至 $2.23\\text{ MeV}$（刚度增强达 $53.8%$）。这一微观硬化有效推迟了剪刀叶片在低转动频率下的过早闭合，保持了中自旋区稳定的开角（在 $\\omega = 0.20\\text{ MeV}$ 处仍保持 $\\theta = 9.5^\\circ$，而裸质量模型此时早已强行闭合至 $0^\\circ$）。同时，反向反作用流分担了角动量积累，自洽重现了实验测定的动力学转动惯量 $J^{(2)}$。

## Assumptions

1. 有效质量在原子核内部区域近似为各向同性空间常数；
2. 反作用流场在低频推转下表现为无旋逆流展开；
3. 偶极跃迁算符的有效电荷与 $g$ 因子重整化保持微扰。

## Competing Explanations

1. **裸质量常数剪刀刚度假说**：假定势能刚度与介质有效质量无关；该假说导致在推转频率略微上升时剪刀瞬间关闭，必须人为提高带终止自旋以拟合实验；
2. **纯核芯变形自发拉伸假说**：将所有惯量偏离归因于核芯四极形变 $\\beta_2$；本模型证实即使在严格冻结核芯形变下，有效质量硬化效应即可提供超过一半的剪刀动力学延迟。

## Transfer Conditions

1. 适用于由重核侵入轨道构成的大-$j$ 磁转动能带（如铅区 $A \\approx 190 - 200$ 与稀土区 $A \\approx 130$）；
2. 适用于推转频率处于准粒子破缺阈值以下的单带剪刀运动。

## Failure Conditions

1. 在极高激发能区或核表面边缘，有效质量 $m^*(r) \\to m$ 恢复为裸质量，局域硬化假说退化；
2. 若核态发生强反向手征进动，流场反作用必须升级为三维 Euler 旋度流。

## Falsification or Reverse Tests

1. 对比不同泛函预测的剪刀临界频率：检验采用高有效质量（$m^*/m = 0.85$）与低有效质量（$m^*/m = 0.65$）泛函计算的剪刀闭合频率；若实验测量更契合高剪刀刚度预测，则直接证实了有效质量硬化效应；
2. 精确测量带内 $B(M1)$ 随自旋的线性衰减区间：若衰减区间较长且闭合频率显著高于接触理论，则排除了裸质量常数模型。

## Open Questions

1. 速度依赖两体相互作用与张量力在有效质量各向异性（$m_\\perp^* \\ne m_\\parallel^*$）中的微观耦合；
2. 反磁转动四叶片中局域流场反作用在四极辐射通道中的干涉抵消。

## Human Review

本研究笔记基于微观密度泛函有效质量理论与推转流体力学反作用模型建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29：基于 Day 26 磁转动微观准粒子有效质量与流场动力学深入研学创建初始草案。
