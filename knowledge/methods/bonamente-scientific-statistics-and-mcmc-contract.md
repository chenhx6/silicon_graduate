---
type: method
title: "Massimiliano Bonamente 科学实验数据统计、Cash 泊松似然与 MCMC 方法合同"
aliases: [Bonamente-statistics-contract, Cash-statistic-contract, Poisson-MLE-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: statistics-method-contract
tags: [bonamente, experimental-statistics, cash-statistic, poisson-likelihood, gehrels-approximation, bootstrap-resampling, mcmc, wilks-theorem]
topics: [experimental-statistics, cash-statistic, poisson-likelihood, bootstrap, mcmc]
sources: [book-bonamente-statistics-scientific-data, book-zhu-probability-statistics-in-physics, book-behnke-data-analysis-hep]
---

# Massimiliano Bonamente 科学实验数据统计、Cash 泊松似然与 MCMC 方法合同

## Purpose

本方法合同严格绑定 Massimiliano Bonamente《Statistics and Analysis of Scientific Data》（Springer 2022 第三版）第 5、7、15、16、20、22 章（物理 PDF pp. 101–147, 289–324, 358–417），
系统形式化科学测量中误差完全协方差传播、低计数泊松数据的 Cash 似然统计量（$C$-Statistic）、Gehrels 泊松置信区间解析逼近、多维参数剖面似然（$\Delta\chi^2 / \Delta C$）、非参数 Bootstrap 重采样以及 Metropolis-Hastings MCMC 马尔可夫链蒙特卡罗推断，
为在束微弱 $\gamma$ 峰拟合、非线性多极混合比误差反演与多参数后验采样提供权威数理统计规范。

## Inputs and Assumptions

1. **计数统计分布原假设**：全能峰与连续本底离散光子计数严格服从独立 Poisson 过程；在大计数极限下渐近逼近多元正态分布；
2. **多变量函数误差一阶泰勒展开假设**：导出物理量 $Y = f(\vec{X})$ 在测量均值邻域满足光滑可微，协方差矩阵为 $\mathbf{V}_X$；
3. **参数空间先验约束**：物理参数位于明确的物理定义域内（例如分支比 $b_\gamma \in [0, 1]$，能级寿命 $\tau > 0$）；
4. **MCMC 平稳马尔可夫链假设**：提议分布满足遍历性与细致平衡条件（Detailed Balance），多链采样满足 Gelman-Rubin 诊断。

## What It Can Establish

1. **Cash 泊松似然统计量与最小二乘拟合偏倚纠正（式 15.6, 16.25）**：
   $$C = 2 \sum_{i=1}^N \left[ e_i - d_i \ln e_i \right] + \text{const}$$
   - 证明在低计数泊松谱学分析中，直接采用高斯最小二乘法（$\chi^2 = \sum (d_i - e_i)^2 / d_i$ 或 $/e_i$）会导致测定光子强度的**系统性负偏差（向小值低估高达 $10\% - 30\%$）**；
   - 确立 Cash 似然统计量为低计数泊松谱拟合的严格无偏最大似然标准；
2. **Gehrels 泊松非对称置信区间解析逼近定理（式 7.22）**：
   对于观测计数 $d$，其 $1\sigma$ 单侧上限与下限由经典解析公式给出：
   $$\lambda_{\text{upper}} \approx d + 1 + \sqrt{d + 0.75}, \quad \lambda_{\text{lower}} \approx d \left[ 1 - \frac{1}{9d} - \frac{1}{3\sqrt{d}} \right]^3$$
   即使在零计数（$d=0$）极端极限下，仍给出严格上界 $\lambda_{\text{upper}}(0) = 1.841$（精确值为 $1.833$），彻底消除高斯误差在零计数处给出负强度的荒谬伪影；
3. **基于 Wilks 定理的参数剖面置信区间（$\Delta C$ 准则）**：
   $$\Delta C(\mu) = C(\mu, \hat{\hat{\vec{\theta}}}) - C_{\min} \le \chi^2_1(\alpha)$$
   给出了自动吸收本底斜率、探测效率涨落等所有连续干扰参数后的真实单参数非对称误差区间；
4. **非参数 Bootstrap 蒙特卡罗误差反演（式 20.18）**：
   通过生成 $N = 10^5$ 组多元高斯伪实验样本，直接提取经验分位数：
   $$\hat{Y} = Y_{50\%}, \quad +\sigma = Y_{84.13\%} - Y_{50\%}, \quad -\sigma = Y_{50\%} - Y_{15.87\%}$$
   彻底攻克多极混合比 $\delta$ 跨越零点（导数发散）或极值发散时的非线性奇异误差传播问题；
5. **Metropolis-Hastings MCMC 后验抽样与 Gelman-Rubin 收敛诊断（式 22.18）**：
   多链方差比 $\hat{R} = \sqrt{V / W} < 1.10$ 确立马尔可夫链充分遍历混合，输出复杂多准粒子多能带拟合参数的完全后验联合分布。

## What It Cannot Establish Alone

1. **统计无偏性不能纠正错误的物理仪器响应模型**：若拟合采用的高斯加单指数尾部峰形函数自身与真实探测器脉冲成形响应存在偏差，Cash 似然依然会输出带有模型偏差的参数中心；
2. **渐近 Wilks 定理在超极小样本下的有限偏离**：当全能峰计数过少（$N_{\text{counts}} < 5$）且本底估计不准时，$\Delta C$ 分布可能偏离标准 $\chi^2_1$，需结合 Toy Monte Carlo 伪实验进行精确覆盖率校准（Coverage Test）；
3. **MCMC 虚假收敛伪影**：在存在多个孤立深极小的多峰后验空间中，单一起始点的马尔可夫链容易被困在局部伪极小中，必须采用多链不同初始值并行抽样。

## Sources

- [[book-bonamente-statistics-scientific-data]]：Chapters 5, 7, 12, 15, 16, 20, 22.
- [[book-zhu-probability-statistics-in-physics]]：朱永生 2006, 第 6、7、13 章.
- [[book-behnke-data-analysis-hep]]：Chapters 6–8 似然与假设检验.
- [[poisson-maximum-likelihood-and-gamma-peak-fitting-bias]]：泊松极大似然与拟合偏差机理.
- [[experimental-statistics-and-dual-root-determination]]：双根退化与高级统计推断法典.
