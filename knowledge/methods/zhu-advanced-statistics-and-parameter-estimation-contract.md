---
type: method
title: "朱永生实验统计学：参数估计、剖面误差、假设检验与蒙特卡罗方法合同"
aliases: [Zhu Experimental Statistics Contract, 朱永生实验统计学合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: experimental-statistics-contract
tags: [experimental-statistics, maximum-likelihood, minos-errors, levenberg-marquardt, hypothesis-testing, neyman-pearson, monte-carlo, rejection-sampling]
topics: [statistics, parameter-estimation, profile-likelihood, hypothesis-testing]
sources: [book-zhu-probability-statistics-in-physics, book-behnke-data-analysis-hep, book-bonamente-statistics-scientific-data]
---

# 朱永生实验统计学：参数估计、剖面误差、假设检验与蒙特卡罗方法合同

## Purpose

本方法合同严格绑定中国科学院高能物理研究所朱永生研究员编著《实验物理中的概率和统计（第二版）》（科学出版社 2006 年）第 4、8、9、11、12、13、14 章，
系统形式化极大似然估计的一致性与 Cramér-Rao 最小方差下限（CRLB）、非线性最小二乘拟合 Levenberg-Marquardt 自适应阻尼迭代算法、MINOS 剖面似然（Profile Likelihood）非对称误差确定、Neyman-Pearson 最优假设检验与信号发现显著性 $Z\\sigma$ 裁决，以及蒙特卡罗舍选抽样（Acceptance-Rejection）算法，
为在束核谱学微弱能峰拟合、多极混合比 $\\delta$ 双根仲裁与新激发模式置信度报告提供权威统计推断规范。

## Inputs and Assumptions

1. **似然函数正则条件**：对数似然函数 $\\ln L(\\vec{\\theta})$ 关于待估参数三阶可微，导数运算与积分运算可对换顺序；
2. **多维误差一阶截断**：误差传递公式基于测量量在真值附近的 Taylor 展开一阶线性截断 $\\mathbf{V}_y = J \\mathbf{V}_x J^T$；
3. **加权残差独立同分布或协方差已知**：拟合各道计数误差满足方差模型（高计数下 Poisson 逼近正态，低计数下直接使用 Poisson 似然）；
4. **复合假设 Wilks 渐近条件**：零假设 $H_0$ 位于备择假设 $H_1$ 参数空间的内部（无边界效应），样本量趋于大样本极限。

## What It Can Establish

1. **极大似然估计量有效性与 Cramér-Rao 最小方差下限（CRLB）**：
   $$V(\\hat{\\vec{\\theta}}) \\ge I(\\vec{\\theta})^{-1},\\quad I_{jk}(\\vec{\\theta}) = -E\\left[ \\frac{\\partial^2 \\ln L}{\\partial \\theta_j \\partial \\theta_k} \\right]$$
   - 证明在大样本极限下极大似然估计是渐近有效估计量，其逆 Fisher 信息矩阵给出理论最小方差协方差下限；
2. **Levenberg-Marquardt 自适应阻尼非线性多峰解叠算法**：
   $$(J^T W J + \\lambda \\, \\text{diag}(J^T W J)) \\Delta\\vec{\\theta} = J^T W \\vec{r}$$
   - 在高阻尼最速下降法（大 $\\lambda$）与快速 Gauss-Newton 二阶收敛（小 $\\lambda$）之间平滑自适应切换，彻底根除紧密重叠能谱双峰拟合在初值偏差下的病态振荡；
3. **MINOS 剖面似然非对称非正态误差**：
   $$\\chi_p^2(\\theta_j) \\equiv \\min_{\\vec{\\theta}_{\\ne j}} \\chi^2(\\theta_j, \\vec{\\theta}_{\\ne j}),\\quad \\chi_p^2(\\theta_j \\pm \\sigma_{\\pm}) = \\chi_{\\min}^2 + 1.0$$
   - 证明当参数处于物理边界附近（如四极矩 $B(E2) \\ge 0$）或模型高度非线性时，MIGRAD 对称二次抛物线误差失效，MINOS 给出真实非对称置信区间 $(\\theta_j)_{-\\sigma_-}^{+\\sigma_+}$；
4. **Neyman-Pearson 最优假设检验与信号显著性 $Z\\sigma$ 规范**：
   $$\\lambda(\\vec{x}) = \\frac{L(\\vec{x}|H_0)}{L(\\vec{x}|H_1)},\\quad q_0 = -2 \\ln \\lambda(\\vec{x}),\\quad Z = \\Phi^{-1}(1 - p_0) \\approx \\sqrt{q_0}$$
   - 证明似然比检验在给定假阳性率 $\\alpha$ 下保证第二类错误率 $\\beta$（漏报率）极小；
   - 确立物理学严格判定阈值：$Z \\ge 3.0\\sigma$（$p_0 \\le 1.35 \\times 10^{-3}$）为“物理证据（Evidence）”，$Z \\ge 5.0\\sigma$（$p_0 \\le 2.87 \\times 10^{-7}$）为“确证发现（Discovery）”；
5. **蒙特卡罗舍选抽样（Acceptance-Rejection Sampling）**：
   - 对任意复杂角关联理论密度 $W(\\theta) \\le M$，按 $u \\le W(\\theta)/M$ 接受样本，抽样效率严格为 $1/M$；为探测器阵列几何效率模拟提供无偏抽样算法。

## What It Cannot Establish Alone

1. **边界受限参数下的标准 Wilks 卡方分布**：当待测物理参数位于物理边界（如信号强度 $S=0$）时，标准 Wilks 定理失效，需采用 Cowan 2011 单侧检验统计量 $q_0$ 分布修正；
2. **多极混合比 $\\delta$ 双根的单物理裁决**：单个方向角分布二次方程 $(1+a\\delta+b\\delta^2)/(1+c\\delta^2)$ 产生的两个实数解在统计上完全简并，必须结合线偏振度 $P$ 或寿命测量予以物理排他；
3. **未建模仪器系统误差的消除**：统计误差仅反映有限计数泊松涨落，无法替代由于探测器效率刻度漂移、靶倾角不准或死时间漏计造成的系统偏差。

## Sources

- [[book-zhu-probability-statistics-in-physics]]
- [[book-behnke-data-analysis-hep]]
- [[book-bonamente-statistics-scientific-data]]
- [[experimental-statistics-and-dual-root-determination]]
