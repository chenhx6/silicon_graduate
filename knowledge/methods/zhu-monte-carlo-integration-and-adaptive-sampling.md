---
type: method
title: "朱永生第十四章：蒙特卡罗积分、重要抽样与自适应分层抽样"
aliases: [Zhu Monte Carlo, 蒙特卡罗积分, 重要抽样, 自适应蒙特卡罗]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: "monte-carlo-numerical-integration"
scope: "Rendered and OCR-assisted verification of Zhu Chapter 14, printed pages 525-572, with targeted equation checks in pages 554-569"
confidence: "high for the listed equations and numerical-method boundaries"
tags: [monte-carlo, importance-sampling, stratified-sampling, uncertainty, zhu-statistics]
sources: [book-zhu-probability-statistics-in-physics]
---

# 朱永生第十四章：蒙特卡罗积分、重要抽样与自适应分层抽样

## Purpose

把朱永生第十四章中可直接迁移到 Python 科研计算的蒙特卡罗方法整理成三层：

```text
均匀抽样 -> 重要抽样 -> 分层/自适应抽样
```

这些方法适合高维积分、响应函数、复杂几何接受度和非解析传播过程；输出必须
同时报告抽样误差、随机种子和生成模型。

第十四章还先给出伪随机数发生器的周期性、均匀性、独立性和连贯性检验，再介绍
任意分布的直接抽样、反函数、舍选、复合、近似和条件密度方法。因此，随机数质量
和抽样算法本身也是积分误差合同的一部分，不能只记录最终积分值。

## Inputs and Assumptions

- 被积函数在选定区域内可计算，且积分有限；
- 均匀抽样时积分区域体积 \(V_s\) 已知；
- 重要抽样时 proposal density \(f(x)\) 已归一化，并覆盖被积函数的支撑；
- 估计的标准误只描述有限抽样误差，不包含模型、响应和系统误差；
- 自适应分层的 pilot 样本不能与生产样本的统计独立性混淆，必须保存分层和分配记录。

## What It Can Establish

### 均匀蒙特卡罗

若 \(\xi_i\) 在体积 \(V_s\) 内均匀分布，
\[
I=\int_{V_s}g(x)\,dx
\approx V_s\frac1n\sum_{i=1}^n g(\xi_i).
\]
用样本方差估计积分方差：
\[
\widehat{\mathrm{Var}}(I)
=\frac{V_s^2}{n}
\left[
\frac1n\sum_i g(\xi_i)^2-
\left(\frac1n\sum_i g(\xi_i)\right)^2
\right].
\]

### 重要抽样

若从密度 \(f(x)\) 抽样，
\[
I=\int\frac{g(x)}{f(x)}f(x)\,dx
\approx \frac1n\sum_i\frac{g(\xi_i)}{f(\xi_i)}.
\]
抽样密度应在被积函数变化大的区域提高权重；否则虽然估计仍可能无偏，
方差会显著增大。

### 自适应分层

将区域分为 \(V_i\)，每层使用 \(L_i\) 个样本，先以 pilot 样本估计层内方差，
再按层体积和波动大小重新分配样本。当前 Python 实现使用
\[
L_i\propto V_i\,s_i
\]
的有限预算分配，并返回每层边界、样本数、pilot 标准差和总方差估计。

### 粒子输运

第十四章还把蒙特卡罗用于粒子传播：当相互作用概率已知时逐事件跟踪粒子，
从初态抽样得到中间态、末态、能量和方向分布。这个框架可以迁移到核反应、
探测器响应和衰减级联，但每一个物理过程的截面、边界条件和响应模型都必须单独
给出。

### 抽样质量和响应矩阵

第 14.2 节把参数、频率、累积频率、相关系数、列联表、多维频率矩和游程检验作为
伪随机数的不同诊断；第 14.3 节说明反函数法、舍选效率
\[
\eta=\frac{\int f(x)\,dx}{(b-a)M}
\]
以及条件密度分解如何将多维抽样化为一维抽样。对 HPGe/Geant4 响应模拟，这些
诊断应和几何、截面、阈值及探测器效率分开记录。

## Discriminating Observables

代码 `system/scripts/analysis/monte_carlo_integrator.py` 输出：

- 积分估计 `estimate`；
- 样本方差和标准误 `sample_variance`、`standard_error`；
- 随机种子、维度、区域边界和抽样模式；
- 自适应分层中的层边界、pilot 波动和最终样本分配；
- 重要抽样时的 proposal 密度和权重边界。

解析回归基准包括：

- \(\int_0^1 x^2dx=1/3\)；
- \(\int_0^1 e^x dx=e-1\)；
- \(q(x)=2x\) 重要抽样下的等价积分。

## Supporting Evidence

- 朱永生 physical PDF pp. 541–553 / printed pp. 525–537：伪随机数、均匀性/
  独立性/连贯性检验和任意分布抽样；
- physical PDF pp. 554–559 / printed pp. 538–543：均匀投点、期望值法、重要抽样和
  抽样方差；
- physical PDF pp. 560–565 / printed pp. 544–549：半解析方法、表 14.3 和近似抽样；
- physical PDF pp. 566–569 / printed pp. 550–553：自适应蒙特卡罗的分层分配、迭代
  更新与粒子传播入口。

## What It Cannot Establish Alone

蒙特卡罗标准误不是实验系统误差，也不是模型不确定度；一次固定 seed 的输出
不能证明覆盖率。重要抽样的 proposal 选择不当会制造高权重长尾，自适应分层的
pilot 样本不足会低估层间方差。真实核谱学中还要加入效率、死时间、背景、
停止本领、侧馈和校准协方差。

## Counter-evidence

- 高维积分的抽样误差可能很小，但若被积函数或响应模型错误，结果仍然系统偏差；
- 分层抽样降低的是抽样方差，不会自动消除边界截断、数值离散或物理模型误差；
- 重要抽样的“高概率区域”需要依据物理响应而非事后挑选，以免产生选择偏差；
- 粒子输运的逐事件模拟不能替代真实探测器的波形、阈值和堆积响应标定。

## Model Dependence

在核实验应用中，蒙特卡罗应与 likelihood、协方差传播和响应矩阵分开记录：

```text
物理生成模型 -> 输运/响应模型 -> 抽样估计 -> 统计误差
                         \-> 系统/模型变化与协方差
```

当前接口只实现数值积分层，不把输出称为实验数据或完整不确定度。

## Limitations and Missing Evidence

本轮已建立第十四章 PDF pp. 541–588 / printed pp. 525–572 的 OCR 导航，并对
第 14.1、14.2、14.4 和 14.5 的关键页面做渲染核对；复杂图表和所有抽样表格仍不
等同于逐字人工审校。第十三章极小化已另建
[[zhu-minimization-and-profile-error-contract]]，全书其它章节仍未完成逐页阅读。
后续需要把该接口与实际 HPGe 几何、DSAM stopping、gamma cascade 和
reaction-channel Monte Carlo 连接。

## Sources

- [[book-zhu-probability-statistics-in-physics]]
- [[advanced-statistical-inference-feldman-cousins-and-mcmc]]
- [[experimental-uncertainty-propagation-and-double-root-triage]]
