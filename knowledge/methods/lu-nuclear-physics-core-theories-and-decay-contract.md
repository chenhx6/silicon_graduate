---
type: method
title: "卢希庭核物理基础理论、衰变动力学与截面共振方法合同"
aliases: [Lu Nuclear Physics Theory Contract, 卢希庭基础理论方法合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: core-nuclear-physics-contract
tags: [nuclear-physics, bethe-weizsacker, beta-decay, gamma-transitions, internal-conversion, breit-wigner, bateman-equations]
topics: [decay-kinetics, beta-decay, internal-conversion, neutron-physics]
sources: [book-lu-nuclear-physics-chinese, book-bohr-mottelson-nuclear-structure, book-wu-nuclear-experiment-methods]
---

# 卢希庭核物理基础理论、衰变动力学与截面共振方法合同

## Purpose

本方法合同严格绑定卢希庭、江栋兴、叶沿林编著《原子核物理（修订版）》（原子能出版社 2000 年），
系统形式化原子核宏观液滴与结合能公式（SEMF）、多级衰变链 Bateman 方程与放射性平衡、$\\beta$ 衰变 Fermi 统计理论与 Kurie 图谱线型拟合、电磁跃迁内转换系数（ICC）多极性判据，以及慢中子 Breit-Wigner 单能级共振截面，
为在束实验设计、活化测量、衰变纲图构建与中子反应道分析提供标准物理依据。

## Inputs and Assumptions

1. **宏观球形液滴假设**：原子核视为均一不可压缩带电荷液滴，短程核力饱和导致体积正比于质量数 $A$，饱和密度对应核半径 $R = R_0 A^{1/3}$；
2. **无关联独立衰变微分律**：每一个不稳定核在单位时间内的衰变几率恒定为 $\\lambda$（衰变常数），与原子核所处化学环境、温度、压力及物理寿命历程严格无关；
3. **弱相互作用 Fermi 理论点接触近似**：$\\beta$ 衰变有效相互作用哈密顿量为轻子流与强子流的四费米子点接触耦合，长波极限下出射轻子平面波可在原点展开；
4. **内转换两步虚跃迁模型**：内转换电子发射是核电磁跃迁算符通过库仑场与原子束缚态电子相互作用的单步二级量子过程，不是光子发射后再吸收；
5. **共振复能级单道独立假设**：入射慢中子能量接近孤立复合态能级 $E_0$，相邻能级间距远大于共振总宽度（$D \\gg \\Gamma$），忽略多能级干涉效应。

## What It Can Establish

1. **Bethe-Weizsäcker 半经验结合能公式（SEMF）与稳定线方程**：
   $$B(A, Z) = a_v A - a_s A^{2/3} - a_c \\frac{Z(Z-1)}{A^{1/3}} - a_{\\text{sym}} \\frac{(A-2Z)^2}{A} + \\delta(A)$$
   - 给出结合能经典拟合参数：$a_v \\a15.75\\text{ MeV}, a_s \\a17.8\\text{ MeV}, a_c \\a0.711\\text{ MeV}, a_{\\text{sym}} \\approx 23.7\\text{ MeV}$；
   - 导出奇 $A$ 核 $\\beta$ 稳定线谷底电荷方程：$Z_{\\text{stable}} = \\frac{A}{2 + (a_c / 2 a_{\\text{sym}})A^{2/3}}$；
2. **串联级联衰变 Bateman 方程与两级放射性平衡判据**：
   $$N_n(t) = N_1(0) \\sum_{i=1}^n c_i e^{-\\lambda_i t},\\quad c_i = \\frac{\\prod_{j=1}^{n-1}\\lambda_j}{\\prod_{j=1, j\\ne i}^n (\\lambda_j - \\lambda_i)}$$
   - 证明久期平衡（$\\lambda_1 \\ll \\lambda_2$ 时 $\\lim A_2(t) = A_1(t)$）；
   - 证明暂时平衡（$\\lambda_1 < \\lambda_2$ 时 $\\lim A_2(t)/A_1(t) = \\lambda_2/(\\lambda_2-\\lambda_1) > 1$）；
3. **$\\beta$ 衰变 Fermi 统计理论与 Kurie 图谱线型**：
   $$K(E_e) \\equiv \\left[ \\frac{N(p_e)}{p_e^2 F(Z, E_e)} \\right]^{1/2} = C |M_{fi}| (E_0 - E_e)$$
   - 允许跃迁 Kurie 图呈严格负斜率直线，截距无偏测定衰变端点能量 $E_0 = Q_\\beta$；
   - 确立 Fermi 跃迁（$\\Delta I = 0, \\Delta \\pi = \\text{no}$，$\\tau_\\pm$ 算符）与 Gamow-Teller 跃迁（$\\Delta I = 0, \\pm 1$ 但 $0 \\to 0$ 禁，$\\sigma\\tau_\\pm$ 算符）选择定则；
4. **电磁内转换系数（ICC）与多极性指纹**：
   $$\\alpha \\equiv \\frac{\\lambda_e}{\\lambda_\\gamma} = \\alpha_K + \\alpha_{L_I} + \\alpha_{L_{II}} + \\alpha_{L_{III}} + \\dots$$
   - 确立总跃迁强度平衡方程 $I_{\\text{tot}} = I_\\gamma (1 + \\alpha)$，消除低能跃迁因忽略电子发射造成的能级布居失衡；
   - 确立同阶多极性下 $\\alpha(M\\lambda) > \\alpha(E\\lambda)$，以及 $K/L$ 与亚壳层比值对跃迁多极性的敏感判据；
5. **Breit-Wigner 单能级共振公式与 $1/v$ 吸收定律**：
   $$\\sigma_{nr}(E) = \\pi \\lambdabar^2 g_J \\frac{\\Gamma_n \\Gamma_r}{(E - E_0)^2 + (\\Gamma/2)^2}$$
   - 推导出热能区慢中子辐射捕获截面严格遵循 $\\sigma_{n\\gamma}(E) \\propto 1/\\sqrt{E} \\propto 1/v$ 定律。

## What It Cannot Establish Alone

1. **微观幻数突变与壳演化**：SEMF 仅含宏观平均项，无法预言滴线区由张量力诱发的非经典幻数消失与新反转岛；
2. **非简谐三轴能级与摆动激发**：书中集体模型局限于轴对称四极转子，三轴刚度 $\\gamma$ 与手征双重带必须由专用三轴微观模型（PRM、TAC、TPSM）求解；
3. **多能级干涉中子截面**：当共振能级密集且宽度重叠时，Breit-Wigner 单能级公式失效，必须采用 Reich-Moore 准则的 $R$ 矩阵理论处理通道相位干涉。

## Sources

- [[book-lu-nuclear-physics-chinese]]
- [[nuclear-physics-standard-terminology-chinese-english]]
- [[internal-conversion-coefficients-and-bricc-formalism]]
- [[compound-nucleus-statistical-decay-and-level-density]]
