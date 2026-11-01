---
type: source
title: "朱永生 2006 - 实验物理中的概率和统计（第二版）"
aliases: [朱永生实验物理统计, Zhu 2006 Probability and Statistics, 实验物理中的概率和统计]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "实验物理中的概率和统计（第二版）"
authors: [朱永生]
publisher: "科学出版社"
year: 2006
pages: "671"
isbn: "9787030172600"
canonical_source: "朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006)"
library_file: "raw/books/实验物理中的概率和统计_朱永生著.pdf"
raw_file: "raw/books/实验物理中的概率和统计_朱永生著.pdf"
raw_sha256: "e97062665497c597609d58c23dfa977824c43e73d3ae8cb4ca3c0855e381894b"
nuclei: []
reactions: []
experiments: []
models: [maximum-likelihood, least-squares, profile-likelihood, chi-squared-minimization]
topics: [experimental-statistics, error-propagation, parameter-estimation, dual-root-degeneracy, hypothesis-testing]
---

# 朱永生 2006 - 实验物理中的概率和统计（第二版）

## 专著概况与定位

本书由中国科学院高能物理研究所朱永生研究员所著，是国内实验物理学界（尤其是核物理与粒子物理）最具深度、最为权威的数理统计与误差处理巨著（671 页）。本书以极其严谨的数学推导结合物理实操案例，彻底奠定了参数估计（极大似然法与最小二乘法）、协方差矩阵反演、非对称误差、置信区间构造以及似然比假设检验的理论基石。

## 核心章节精要与物理内容

### 第 8 章：极大似然法（pp. 228–275）
- **极大似然原理（Maximum Likelihood Principle）**：对相互独立测量集 $\{x_i\}$，联合概率密度 $\mathcal{L}(\theta) = \prod_{i=1}^N f(x_i; \theta)$。极大化对数似然函数 $\ln\mathcal{L}$。
- **似然函数的渐近性质与误差估计**：大样本极限下 $\ln\mathcal{L}(\theta)$ 趋于高斯抛物线，参数协方差矩阵由 Fisher 信息阵的逆给出：
  $$V_{ij}^{-1} = - \left. \frac{\partial^2 \ln\mathcal{L}}{\partial \theta_i \partial \theta_j} \right|_{\hat{\theta}}$$
- **非对称误差与剖面似然（Profile Likelihood）**：当似然函数偏离对称高斯时，置信度为 $1\sigma$（$68.27\%$）的非对称误差区间由水平切线决定：
  $$\ln\mathcal{L}(\theta) = \ln\mathcal{L}_{\max} - \frac{1}{2}\Delta\chi^2 \quad (\Delta\chi^2 = 1.0\text{ for } 1\text{ DOF})$$

### 第 9 章：最小二乘法与多项式拟合（pp. 276–340）
- **非相关与相关测量值的加权拟合**：给出具有完全协方差矩阵时的广义 $\chi^2$ 矩阵公式：
  $$\chi^2 = (\vec{y} - \vec{f}(\vec{\theta}))^T \mathbf{V}^{-1} (\vec{y} - \vec{f}(\vec{\theta}))$$
- **角分布 Legendre 多项式展开拟合**：推导勒让德多项式基函数正交性下的系数 $a_2, a_4$ 协方差估计与奇异性处理。

### 第 10 章：假设检验与多解退化判定（pp. 341–410）
- **似然比检验（Likelihood Ratio Test）**：检验两套相互竞争的物理假设（如 $H_0$: 摆动解 vs $H_1$: 旋称伙伴解），定义检验统计量：
  $$\lambda = -2 \ln \frac{\mathcal{L}(H_0)}{\mathcal{L}(H_1)} = \chi^2(H_0) - \chi^2(H_1) = \Delta\chi^2$$
  依据 Wilks 定理，自由度差为 $\nu$ 时 $\Delta\chi^2$ 渐近服从 $\chi^2(\nu)$ 分布，从而计算排除显著性（如 $3\sigma, 5\sigma$）。

## 对本 Wiki 研究的核心指导价值

1. **角分布混合比双根退化判决**：提供严谨的剖面似然扫描算法，杜绝在局部极小值处盲目截断参数范围。
2. **非线性参数误差传递**：为从衰变寿命 $\tau$、混合比 $\delta$ 和能量比计算减缩跃迁几率 $B(E2)/B(M1)$ 及其比值提供完全协方差反演算法。
