---
type: method
title: "朱永生第十三章：极小化、约束优化与非对称 profile 误差"
aliases: [Zhu minimization, MINUIT-style profile error, 极小化方法, 非对称误差轮廓]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: "bounded-minimization-and-profile-error"
scope: "Rendered and OCR-assisted verification of Zhu Chapter 13, printed pages 466-524"
confidence: "high for the listed equations and algorithm boundaries"
tags: [zhu-statistics, minimization, golden-section, gauss-newton, profile-likelihood, minuit, asymmetric-uncertainty]
sources: [book-zhu-probability-statistics-in-physics]
---

# 朱永生第十三章：极小化、约束优化与非对称 profile 误差

## Purpose

第十三章把参数估计中的“求最优参数”拆成目标函数、局部/全域极小、约束处理和
误差估计四个层次。对在束谱学最有用的迁移是：

```text
先构造可审计的目标函数
-> 用有界方法找局部候选
-> 检查边界、初值和多极小
-> 沿参数 profile 扫描目标函数阈值
-> 报告非对称误差与未覆盖的边界
```

## Inputs and Assumptions

- 目标函数在被搜索区间内可计算，并对非有限值显式报错；
- 黄金分割法需要一个近似单峰的一维区间；它不证明全域最小；
- profile 阈值需要先指定目标函数变化量 \(\Delta f\)，不能把任意阈值自动称为置信区间；
- 多维拟合的 Hessian、协方差、参数边界和 nuisance 参数必须由调用方提供；
- 约束罚函数改变了优化目标，罚因子、内点/外点选择和收敛条件必须记录。

## What It Can Establish

### 一维黄金分割搜索

对于包含一个有用局部极小的区间 \([a,b]\)，黄金分割法重复保留较低目标函数值的一侧，
区间长度按
\[
\rho=\frac{\sqrt{5}-1}{2}\a0.618
\]
收缩。第十三章指出，在单峰假设成立时，它只需复用一个内部函数值，计算量稳定，
但仍然只给出该区间内的局部结果。

### 最小二乘与似然的专用近似

对
\[
Q^2(x)=\sum_i g_i(x)^2
\]
线性化残差并构造 Jacobian \(G\) 后，高斯–牛顿近似使用
\[
H_{\mathrm{GN}}\simeq 2G^{\mathsf T}G.
\]
对负对数似然 \(F(x)=-\sum_i\ln f_i(x)\)，在局部线性化下也可用 score 的
Gram 矩阵近似 Hessian。这个近似依赖局部曲率和可辨识性；远离极小点、强非线性或
近奇异参数化时应使用阻尼、profile 或完整 Hessian 检查。

### MINUIT 风格 profile 阈值误差

第 13.8 节描述了沿某一个参数方向寻找
\[
F(x)=F(x^\ast)+\Delta F
\]
的上下交点。当局部二次近似不可靠时，上、下两侧交点不同，误差自然是非对称的；
若某一侧在物理边界前始终未达到阈值，应报告开放边界而不是制造有限误差。

## Discriminating Observables

代码 `system/scripts/analysis/experimental_statistics_minimizer.py` 提供：

- `golden_section_minimize`：有界一维黄金分割、函数调用次数、最终区间和收敛标志；
- `profile_threshold_interval`：上下 profile 交点、非对称误差、交叉状态和开放边界；
- `boundary` 字段：明确输出是优化/目标函数轮廓，不是自动的 coverage 结果。

对于 \(\delta(E2/M1)\)、峰面积、寿命或响应参数，建议把每一个候选根单独作为
profile 输入，在相同的响应、背景和协方差合同下比较，而不是由优化器返回的第一个
局部极小自动选择物理解。

该方法已接入固定模板泊松伽马峰计算器
`system/scripts/analysis/poisson_likelihood_peak_fitting_bias_calculator.py`：
峰面积的 \(\Delta C\) 上下端点现在由 `profile_threshold_interval` 求解，并在结果中
标记 `profile_method: "zhu-ch13-profile-threshold"`。这里的峰位、宽度和本底仍是
固定输入，故它是朱书方法的可复现接入示例，不是包含响应协方差的完整多参数拟合。

## Supporting Evidence

- 朱永生 physical PDF pp. 482–484 / printed pp. 466–468：目标函数、梯度、Hessian、
  局部极小和迭代停止条件；
- physical PDF pp. 485–497 / printed pp. 469–481：黄金分割、斐波那契、抛物线插值、
  进退法及一维区间构造；
- physical PDF pp. 498–507 / printed pp. 482–491：最速下降、牛顿、共轭方向/梯度和
  变尺度法；
- physical PDF pp. 508–511 / printed pp. 492–495：坐标轮换、Hooke–Jeeves、Rosenbrock
  转轴和单纯形直接法；
- physical PDF pp. 507–511 / printed pp. 491–495：高斯–牛顿与似然极小化；
- physical PDF pp. 512–520 / printed pp. 496–504：局部/全域极小和约束罚函数；
- physical PDF pp. 521–524 / printed pp. 505–508：参数误差、目标函数轮廓和 MINUIT 风格
  的上下误差搜索。

## What It Cannot Establish Alone

优化器收敛、Hessian 正定或 profile 交点存在，都不能单独证明模型正确、参数唯一或
置信区间覆盖率达标。多峰目标函数需要多起点、全域搜索或物理约束对账；边界上的
参数还会破坏常规 Wilks/高斯近似。profile 误差也不能替代对背景、效率、响应、
侧馈和停止本领协方差的联合传播。

## Counter-evidence and Competing Interpretations

- 同一谱线的两个 \(\delta\) 根可以拥有相同的角分布目标函数值，优化器不会自动识别
  哪一个代表 E2 主导或 M1 主导；
- 罚函数的极小点可能停在略微越界的位置，尤其当罚因子有限时；
- 局部二次曲率给出的对称误差可能掩盖真正的非对称 profile；
- 随机多起点得到相同局部极小只能增加稳定性证据，不能把结果升级为实验事实。

## Model Dependence

```text
实验计数/峰形
-> 物理与响应模型
-> 目标函数或似然
-> 优化路径与边界
-> profile/Hessian/Monte Carlo 不确定度
```

每一层都应保留版本、初值、范围、停止条件和共享协方差；代码输出只表示数值方法
的结果，不替代对原始谱线和实验响应的审核。

## Limitations and Missing Evidence

本页已核查第十三章主线和第 13.8 节，但没有实现完整 MINUIT 参数空间、约束
多维 profile、MINOS 的全部内部策略或实验专用 likelihood。当前实现是一维、可复现
的数值基线；把它接到多极混合比和 HPGe 峰拟合前，仍需加入 nuisance 参数扫描、
Poisson likelihood、响应协方差和真实输入数据。

## Sources

- [[book-zhu-probability-statistics-in-physics]]
- [[experimental-uncertainty-propagation-and-double-root-triage]]
- [[dco-mixing-ratio-double-root-arbitration-and-profile-likelihood]]
