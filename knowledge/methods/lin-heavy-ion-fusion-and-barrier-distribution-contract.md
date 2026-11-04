---
type: method
title: "林承键重离子反应：熔合势垒分布、耦合道效应与截面动力学方法合同"
aliases: [Lin Heavy Ion Reaction Contract, 林承键重离子反应合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: reaction-dynamics-contract
tags: [heavy-ion-reactions, fusion-cross-section, barrier-distribution, wong-formula, coupled-channels, rainbow-scattering, wilczynski-plot]
topics: [heavy-ion-reactions, fusion-barrier, reaction-kinematics]
sources: [book-lin-heavy-ion-reactions, book-bertulani-nuclear-reactions, book-wu-nuclear-experiment-methods]
---

# 林承键重离子反应：熔合势垒分布、耦合道效应与截面动力学方法合同

## Purpose

本方法合同严格绑定中国原子能科学研究院林承键研究员专著《重离子核反应》（科学出版社 2017 年）第 2、3、4、5、6、7 章，
系统形式化重离子半经典弹性散射菲涅耳衍射 1/4 截面点（Quarter-Point）相互作用半径反演、Wong 单抛物线势垒穿透公式与渐近线、Rowley 熔合势垒分布二阶导数反演定理 $D_{\\text{fus}}(E) = d^2(E\\sigma_{\\text{fus}})/dE^2$、深部非弹性散射（DIC）Wilczynski 动力学关联，以及复合核去激中子蒸发残留核自旋窗口优化，
为在束高自旋实验靶核反应设计、手征带与摆动带布居效率最大化提供权威反应学标准。

## Inputs and Assumptions

1. **半经典强吸收碰撞假设**：Sommerfeld 参数 $\\eta = Z_1 Z_2 \\alpha_{\\text{em}} / (v/c) \\gg 1$，库仑势主导远距运动，近距发生强表面吸收；
2. **抛物线反转势垒近似**：相互作用总势（库仑势+核相互作用势+离心势）在势垒极大值处局部展开为反转简谐抛物线；
3. **耦合道自由度投影**：弹核与靶核内禀表面低频振动（$2^+, 3^-$ 声子）及基态四极/八极形变与相对轨道运动发生非绝热强耦合；
4. **统计完全熔合与中子级联冷却**：越过复合核鞍点后形成完全平衡系统，退激过程由中子蒸发道（$xn$）主导。

## What It Can Establish

1. **菲涅耳衍射与 1/4 截面点相互作用半径反演**：
   $$\\left. \\frac{\\sigma_{\\text{el}}(\\theta)}{\\sigma_R(\\theta)} \\right|_{\\theta = \\theta_{1/4}} = 0.25 \\implies R_{\\text{int}} = \\frac{\\eta}{k}\\left[ 1 + \\csc\\left(\\frac{\\theta_{1/4}}{2}\\right) \\right]$$
   - 证明测定重离子弹性散射比值下降至 0.25 的角度 $\\theta_{1/4}$ 可直接反演核强吸收半径；
2. **Wong 熔合截面公式及其渐近行为**：
   $$\\sigma_{\\text{fus}}(E_{\\text{c.m.}}) = \\frac{\\hbar\\omega_B R_B^2}{2 E_{\\text{c.m.}}} \\ln\\left[ 1 + \\exp\\left( \\frac{2\\pi (E_{\\text{c.m.}} - V_B)}{\\hbar\\omega_B} \\right) \\right]$$
   - 在高能区渐近还原为经典公式 $\\sigma_{\\text{fus}} \\approx \\pi R_B^2 (1 - V_B/E_{\\text{c.m.}})$；在深垒区呈现指数穿透；
3. **Rowley 熔合势垒分布二阶导数反演定理**：
   $$D_{\\text{fus}}(E) \\equiv \\frac{d^2 (E_{\\text{c.m.}} \\sigma_{\\text{fus}})}{d E_{\\text{c.m.}}^2}$$
   - 单势垒下给出半高宽 $\\text{FWHM} \\a0.56\\hbar\\omega_B$ 的对称钟形峰；
   - 在耦合道效应下分裂为多重分立峰结构，直接在实验上反演基态四极形变 $\\beta_2$ 与振动声子耦合强度；
4. **深部非弹性散射（DIC）大自旋转移与 Wilczynski 图谱**：
   - 粘滞极限下将 $28\\% \\sim 35\\%$ 的轨道角动量转移为碎片内禀自旋（自旋高达 $40 - 50\\hbar$）；
   - 在 $(\\theta_{\\text{c.m.}}, \\text{TKEL})$ 平面呈现向负角偏转的特征鸟嘴形脊线；
5. **在束高自旋 $A\\sim 130$ 手征与摆动带实验自旋窗口优化**：
   - 复合核初态角动量延伸至 $\\ell_{\\text{crit}} \\sim 60 - 70\\hbar$；
   - 每个中子蒸发带走 $\\sim 10.5\\text{ MeV}$ 能量而仅带走 $\\sim 1\\hbar$ 角动量，在 Yrast 线上方集中形成 $I = 15 \\sim 35\\hbar$ 的入口态自旋窗口。

## What It Cannot Establish Alone

1. **深垒极低能区势垒反常阻碍（Fusion Hindrance）**：当能量远低于势垒时，绝热单体势能面颈部收缩导致截面下落速度快于 Wong 公式预期；
2. **非完全熔合（Incomplete Fusion）与破裂反应**：对于弱束缚弹核（如 $^6\\text{Li}, ^9\\text{Be}$），弹核在越过势垒前发生破裂导致的通量损失；
3. **出射残留核特征 $\\gamma$ 跃迁角关联比值**：宏观重离子势模型仅给出各通道总截面，不包含各能级磁亚态高斯展宽 $\\sigma/I$ 的精确量化。

## Sources

- [[book-lin-heavy-ion-reactions]]
- [[book-bertulani-nuclear-reactions]]
- [[book-wu-nuclear-experiment-methods]]
- [[heavy-ion-fusion-experiment-design-guide]]
