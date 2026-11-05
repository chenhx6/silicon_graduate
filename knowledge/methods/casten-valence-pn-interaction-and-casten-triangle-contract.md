---
type: method
title: "Casten 价核子质中相互作用、NpNn 标度律与对称性三角形方法合同"
aliases: [Casten NpNn and Triangle Contract, 卡斯滕NpNn与对称性三角形合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: collective-model-contract
tags: [casten-scheme, npnn-systematics, p-factor, casten-triangle, ibm-limits, triaxiality, gamma-softness, two-state-mixing]
topics: [collective-motion, valence-interactions, ibm, triaxiality, two-state-mixing]
sources: [book-casten-nuclear-structure-simple-perspective, book-greiner-nuclear-models, book-heyde-nuclear-physics-concepts]
---

# Casten 价核子质中相互作用、NpNn 标度律与对称性三角形方法合同

## Purpose

本方法合同严格绑定 R. F. Casten 经典专著 *Nuclear Structure from a Simple Perspective*（Oxford University Press 1990）第 1、6、7、8、10 章，
系统形式化两态混合本征能量排斥下限与跨带 $E2$ 跃迁相消定理、价核子质子-中子相互作用（Valence $p$-$n$）驱动形变相变机制、$N_p N_n$ 体系学与无量纲 $P$ 因子相变标度律、相互作用玻色子模型（IBM）Casten 对称性三角形，以及 $\\gamma$ 刚性与 $\\gamma$ 软度的能级交错指数 $S(J)$ 判据，
为从微观壳组态直观推演低能集体运动相变与三轴性提供权威方法基石。

## Inputs and Assumptions

1. **直观两体残余作用竞争模型**：低能核结构由同类核子单极/对力（超流配对，倾向维持球形 $J=0$ 耦合）与异类价核子长程四极质中相互作用（倾向打破球形对称、建立四极形变）之间的动态竞争所主导；
2. **价核子数定义准则**：价核子数 $N_p, N_n$ 从最近的经典闭壳层（2, 8, 20, 28, 50, 82, 126）起算；当核子数超过壳层半满时，以价空穴数计算；
3. **两态弱扰动正交展开**：未扰动态具有清晰内禀形变矩（$Q_1, Q_2$），残余相互作用矩阵元为常数 $V = \\langle 1  \vert V  \vert 2 \ \rangle$；
4. **IBM-1 玻色子映射空间**：偶偶核价核子对映射为角动量 $L=0$ 的 $s$ 玻色子与 $L=2$ 的 $d$ 玻色子，总玻色子数守恒 $N_B = (N_p + N_n)/2$。

## What It Can Establish

1. **两态混合能级排斥下限与跨带 $E2$ 跃迁相消定理**：
   $$\\Delta E_{\\text{obs}} = \\sqrt{\\Delta E_u^2 + 4V^2} \\ge 2|V|$$
   $$\\langle \\psi_+  \vert \\hat{Q}  \vert \\psi_- \ \rangle = \\alpha\\beta (Q_2 - Q_1) = \\alpha\\beta \\Delta Q$$
   - 证明测得的能级间距绝不可能小于两倍耦合矩阵元 $2|V|$；
   - 证明当混合两组态形变相近（$\\Delta Q \\approx 0$）时，即便处于最大强混合状态（$\\alpha \\approx \\beta \\a1/\\sqrt{2}$），跨带跃迁仍发生代数相消 $B(E2) \\to 0$；微弱的跨带跃迁绝不能作为否定组态混合的依据；
2. **$N_p N_n$ 标度律与 $P$ 因子相变判据**：
   $$P \\equiv \\frac{N_p N_n}{N_p + N_n}$$
   - 不同同位素链和同中子素链的分立集体可观测量（$E(2_1^+), R_{4/2}, B(E2)$）在 $N_p N_n$ 坐标系下汇聚为单一光滑普适曲线；
   - 确立相变临界阈值 $P_c \\approx 4.0 - 5.0$：$P < 4$ 维持球形或弱谐振动，$P \\approx 4-5$ 发生四极形变量子相变，$P > 5$ 进入良好变形刚性转子区；
3. **Casten 动力学对称性三角形**：
   - 形式化 IBM-1 三大群极限：$U(5)$ 球形振动（$R_{4/2}=2.00$）、$SU(3)$ 轴对称长椭转子（$R_{4/2}=3.333$）与 $O(6)$ $\\gamma$ 软核（$R_{4/2}=2.50$）；
   - 将中重核集体运动结构全部映射于三角形内部路径；
4. **$\\gamma$ 刚性与 $\\gamma$ 软度的能级交错指数 $S(J)$ 判据**：
   $$S(J) \\equiv \\frac{[E(J) - E(J-1)] - [E(J-1) - E(J-2)]}{E(2_1^+)}$$
   - Davydov-Filippov 刚性三轴核（$\\gamma \\a30^\\circ$）在奇数自旋 $J$ 呈现负交错（$S(J) < 0$），能级按 $2^+, (3^+, 4^+), (5^+, 6^+)$ 成对聚集；
   - Wilets-Jean / $O(6)$ $\\gamma$ 软核在奇数自旋 $J$ 呈现正交错（$S(J) > 0$），能级按 $(2^+, 3^+), (4^+, 5^+), (6^+, 7^+)$ 成对聚集；这是理想极限下的比较指纹，不是跨核素排他性判据。

## What It Cannot Establish Alone

1. **三维非轴对称推转与高自旋退对演化**：$N_p N_n$ 与 IBM 三角形基于低自旋现象学，无法替代高自旋 Coriolis 退对（CAP）、回弯现象与 3D TAC 出平面手征分岔；
2. **微观壳层演化与同位旋依赖张量力**：单核子能级随中子数变化的微观移动（如质子-中子单极相互作用驱动的幻数漂移）超出宏观价核子数标度；
3. **单态混合比 $\\delta(E2/M1)$ 数值确定**：两态混合仅给出四极矩阵元，不包含单粒子自旋流与轨道流磁偶极 $M1$ 跃迁细节。

## Sources

- [[book-casten-nuclear-structure-simple-perspective]]
- [[book-greiner-nuclear-models]]
- [[book-heyde-nuclear-physics-concepts]]
- [[greiner-asymmetric-rotor-and-rvm-contract]]
