---
type: method
title: "朗道经典力学刚体转动、非对称陀螺与罗斯函数（Routhian）方法合同"
aliases: [Landau-mechanics-contract, Asymmetric-top-contract, Routhian-formalism-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: classical-mechanics-contract
tags: [classical-mechanics, landau-lifshitz, rigid-body, asymmetric-top, routhian, euler-equations, separatrix, phase-space]
topics: [rigid-body, asymmetric-top, routhian, euler-equations, phase-space]
sources: [book-ju-landau-mechanics, book-greiner-nuclear-models, book-bohr-mottelson-nuclear-structure-vol2]
---

# 朗道经典力学刚体转动、非对称陀螺与罗斯函数（Routhian）方法合同

## Purpose

本方法合同严格绑定鞠国兴《朗道〈力学〉解读》（高等教育出版社 2019）第 6 章 §36–37 与第 7 章 §41–42（印刷 pp. 255–267, 294–305 / 物理 PDF pp. 270–282, 309–320），
系统形式化非轴对称刚体转动（非对称陀螺）的欧拉动力学方程、能量与角动量守恒椭球交截、中轴不稳定分离线（Separatrix）、Jacobi 椭圆函数解析解，
以及分析力学中的罗斯函数（Routhian）混合变换与转动参照系哈密顿量  = H - \vec{\omega} \cdot \vec{I}$，
为原子核三轴刚性转子模型、横向摆动运动（Wobbling）经典稳定性判定以及推转壳模型（CSM）与 3D TAC 提供第一性原理的经典力学规范。

## Inputs and Assumptions

1. **刚体自由度与欧拉角参数化**：定点转动刚体由三个独立欧拉角 $ 完全描述，内禀主轴坐标系下角速度分量由欧拉运动学方程确定；
2. **主惯量张量三轴分立性**：假设三个主转动惯量互不相等且有序排列： < I_2 < I_3$；
3. **力矩自由定点转动（Euler-Poinsot 运动）**：刚体不受外力矩作用（$\vec{M} = 0$），转动动能 E = \sum I_k \Omega_k^2$ 与总角动量模平方 ^2 = \sum I_k^2 \Omega_k^2$ 为严格严格运动守恒积分；
4. **循环坐标正则变换条件**：对于包含循环坐标的力学系统，通过部分动量 Legendre 变换构造 Routhian。

## What It Can Establish

1. **主轴转动稳定性定理与欧拉方程解析判定（式 36.1–36.3）**：
   333499I_1 \dot{\Omega}_1 = (I_2 - I_3) \Omega_2 \Omega_3333499
   333499I_2 \dot{\Omega}_2 = (I_3 - I_1) \Omega_3 \Omega_1333499
   333499I_3 \dot{\Omega}_3 = (I_1 - I_2) \Omega_1 \Omega_2333499
   - 证明：微扰围绕 1 轴或 3 轴转动时，偏离方程呈现简谐振动形式（特征根为纯虚数 $\pm i\omega$），转动动力学稳定；
   - 证明：微扰围绕 2 轴（中间轴）转动时，特征根为纯实数 $\pm\lambda$，微扰随时间指数级发散，转动动力学不稳定；
   - 形式化解释了核物理中三轴核转动优先沿最大惯量轴（中间主轴）旋转且诱发横向摆动微振动的经典动力学本质；
2. **非对称陀螺相空间相轨迹与临界分离线（Separatrix）**：
   - 在角动量空间 $ 中，运动轨迹为能量椭球 ^2/I_1 + M_2^2/I_2 + M_3^2/I_3 = 2E$ 与球面 ^2 + M_2^2 + M_3^2 = M^2$ 的立体交线；
   - 当能量等于临界值 E = M^2 / I_2$ 时，交线退化为穿过 $ 与 $ 鞍点的双渐近双曲分离线，将相空间严格划分为绕最小惯量轴与最大惯量轴旋转的两个对易相空间；
3. **罗斯函数（Routhian）与推转模型微观基础（式 041.3–041.5）**：
   333499R = \sum_i p_i \dot{q}_i - L \implies R = H - \sum_k \omega_k I_k333499
   - 证明在以角速度 $\vec{\omega}$ 旋转的内禀参考系中，科氏力与离心力可通过引入有效哈密顿量（Routhian $）完全吸收，微观导出推转壳模型（Cranked Shell Model）基础。

## What It Cannot Establish Alone

1. **无法描述微观费米子自旋单粒子对齐**：经典陀螺仅考虑连续刚体质量分布，不能自动再现由微观奇核子波函数角动量 $\vec{j}$ 诱发的时间反演破缺与反冲力矩；
2. **宏观刚体惯量不能代替超流体配对惯量**：经典刚体转动惯量比实验测量的核转动惯量高估 2–3 倍，在核结构应用中必须引入 BCS 配对淬灭修正；
3. **分离线处的经典混沌与量子隧穿效应**：在分离线鞍点附近，经典运动周期发散（ \to \infty$），量子力学中表现为左手进动与右手进动之间的微观量子穿隧（即手征双阱隧穿），经典力学无法给出量子隧穿简并能隙 $\Delta E$。

## Sources

- [[book-ju-landau-mechanics]]：第六章 §36–37 (印刷 pp. 255–267) & 第七章 §41–42 (印刷 pp. 294–305).
- L. D. Landau & E. M. Lifshitz, *Mechanics* (Volume 1 of Course of Theoretical Physics), Butterworth-Heinemann (1976).
- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]：Davydov-Filippov 三轴转子动力学.
- [[cranked-triaxial-shape-coexistence-pes]]：推转三轴形变共存势能面.
