---
type: method
method_type: experimental-analysis-contract
title: "实验物理统计分析、误差传播与多解/双根退化判决指南"
aliases: [双根退化判决, 实验统计分析指南, 角分布混合比拟合, 极大似然与协方差反演]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
tags: [experimental-statistics, maximum-likelihood, profile-likelihood, dual-root-degeneracy, angular-distribution]
---

# 实验物理统计分析、误差传播与多解/双根退化判决指南

## Purpose

### 统计分析在实验核谱学中的核心地位

低能核物理实验获得的数据本质上是微观核反应与核衰变过程的随机计数。根据朱永生《实验物理中的概率和统计》，物理结论的真实性完全取决于数理统计处理的严谨性。

特别是在处理高自旋核能带结构时，一个最臭名昭著且导致多项国际争议（如 $^{135}\text{Pr}$ 横向摆动带争议、$^{187}\text{Au}$ 纵向摆动争议）的统计陷阱，就是**在束 $\gamma$ 射线角分布混合比 $\delta(E2/M1)$ 的数学双根退化问题（Dual-Root Degeneracy）**。

---

## Inputs and Assumptions

### 角分布与双根退化的数学物理机理

### (1) 方向角分布方程与拟合
在熔合蒸发反应中，定向核发射的 $\gamma$ 射线在与束流轴夹角 $\theta$ 处的角分布强度表达为 Legendre 多项式展开：
$$W(\theta) = A_0 [1 + a_2 P_2(\cos\theta) + a_4 P_4(\cos\theta)]$$
其中 $P_2(x) = \frac{1}{2}(3x^2 - 1)$，$P_4(x) = \frac{1}{8}(35x^4 - 30x^2 + 3)$。
由实验测量的各探测器角度计数 $Y_i \pm \sigma_i$，通过带协方差权重的最小二乘法（或 Poisson 极大似然法），拟合出系数向量 $\vec{a} = (A_0, a_2, a_4)^T$ 及其协方差矩阵 $\mathbf{V}_{a}$。

### (2) 多极混合比 $\delta$ 的数学双根结构
根据 Hamilton 1975 与 Rose-Brink/Krane-Steffen 理论，$a_2$ 是多极混合比 $\delta$ 的二次有理分式：
$$a_2(\delta) = \frac{B_2(I_i)}{B_0(I_i)} \frac{F_2(L L I_f I_i) + 2\delta F_2(L L' I_f I_i) + \delta^2 F_2(L' L' I_f I_i)}{1 + \delta^2}$$
对偶极-四极混合跃迁（$L=1, L'=2$），设有效取向归一化系数为 $\alpha_2 = B_2/B_0$。将其化简为关于 $\delta$ 的标准一元二次方程：
$$(a_2 - \alpha_2 F_2(2 2 I_f I_i)) \cdot \delta^2 - (2 \alpha_2 F_2(1 2 I_f I_i)) \cdot \delta + (a_2 - \alpha_2 F_2(1 1 I_f I_i)) = 0$$
**判决法则**：
只要判别式 $\Delta \ge 0$，该方程**严格存在两个实数根** $\delta_1$ 与 $\delta_2$：
- **根 1（大 $|\delta|$ 根）**：对应四极跃迁 $E2$ 成分占优（通常 $|\delta| \sim 1.5 \text{--} 3.0$）；
- **根 2（小 $|\delta|$ 根）**：对应偶极跃迁 $M1$ 成分占优（通常 $|\delta| \sim 0.1 \text{--} 0.5$）。

由于两个根产生完全相同的 $a_2$ 理论期望值，**仅凭未极化的方向角分布测量，在数学和统计上无论统计量多大，都存在不可解的双根简并（$\Delta\chi^2 \equiv 0$）**！

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### 打破双根退化的正交实验裁判法

### (1) 康普顿线偏振度（Linear Polarization）正交裁判
线偏振灵敏度对于多极混合比的响应方程为：
$$P(\theta) = \frac{ \pm 2 \delta \cdot \dots + \delta^2 \cdot \dots }{ 1 + a_2 P_2(\cos\theta) + a_4 P_4(\cos\theta) }$$
其关键物理特性在于：**线偏振表达式中一次交叉项的符号直接取决于跃迁是磁性还是电性**。
利用联合似然卡方检验：
$$\chi^2_{\text{joint}}(\delta) = \chi^2_{\text{AD}}(\delta) + \left( \frac{P_{\text{exp}} - P_{\text{theo}}(\delta)}{\sigma_P} \right)^2$$
扫描剖面似然曲线 $\Delta\chi^2(\delta) = \chi^2_{\text{joint}}(\delta) - \chi^2_{\min}$：
- 若在其中一个根处 $\Delta\chi^2 > 9.0$（对应 $> 3\sigma$ 排除），则该根被显著否定；
- 若预先声明的检验合同、适用的渐近分布和覆盖率检查均成立，且
  $\Delta\chi^2 > 25.0$ 可作为强烈不支持该假设的参考；它不自动等同于
  模型无关的“彻底证伪”，尤其在双根、边界或响应协方差未闭合时。

### (2) 反模式警示：切忌“先入为主”挑选根
- **严重科研误区**：某些文献因为预设了原子核具有“摆动模式（Wobbling）”，便主观认定跨带连接线必须是 $E2$ 占优的大 $\delta$ 根，而对小 $\delta$ 的 $M1$ 占优伙伴带解置之不理。
- **Wiki 黄金准则**：在缺乏独立的线偏振或内转换系数实验证据之前，**必须在能级图和数据表中同时保留两个根，并显式标注其双根退化状态**！

---

## 4. 复杂物理导出量的完全协方差误差传播

设导出物理量 $Y = f(X_1, X_2, \dots, X_m)$（例如从寿命 $\tau$、混合比 $\delta$ 和能量比计算 $B(E2)_{\text{out}} / B(E2)_{\text{in}}$）。
若输入变量间存在非零协方差矩阵 $\mathbf{V}_X$，则 $Y$ 的不确定度严格由协方差误差传播公式给出：
$$\sigma_Y^2 = \sum_{i=1}^m \sum_{j=1}^m \frac{\partial f}{\partial X_i} \frac{\partial f}{\partial X_j} (\mathbf{V}_X)_{ij}$$
当函数具有高度非线性（如含 $\delta^2$ 或反三角函数）时，一阶偏导数近似失效，必须采用 **Monte Carlo 协方差重采样（Bootstrap / Gaussian Toy Sampling）** 构建真实后验分布区间。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
