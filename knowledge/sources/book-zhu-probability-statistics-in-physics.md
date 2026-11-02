---
type: source
title: "朱永生 2006 - 实验物理中的概率和统计（第二版）"
aliases: [朱永生实验物理统计, Zhu 2006 Probability and Statistics, 实验物理中的概率和统计]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "实验物理中的概率和统计（第二版）"
authors: [朱永生]
publisher: "科学出版社"
year: 2006
pages: "671"
isbn: "7-03-016986-7"
canonical_source: "朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006)"
raw_storage_status: archived-local
archive_required: true
library_file: "raw/books/实验物理中的概率和统计_朱永生著.pdf"
raw_file: "raw/books/实验物理中的概率和统计_朱永生著.pdf"
raw_sha256: "e97062665497c597609d58c23dfa977824c43e73d3ae8cb4ca3c0855e381894b"
nuclei: []
reactions: []
experiments: []
models: [maximum-likelihood, least-squares, profile-likelihood, feldman-cousins, hypothesis-testing]
tags: [books, experimental-statistics, error-propagation, parameter-estimation, dual-root-degeneracy, hypothesis-testing]
---

# 朱永生 2006 - 实验物理中的概率和统计（第二版）

## Bibliographic Record

- **书名**：实验物理中的概率和统计（第二版）（现代物理基础丛书 10）
- **著者**：朱永生（中国科学院高能物理研究所）
- **出版信息**：科学出版社（北京东黄城根北街 16 号），2006 年 4 月第 2 版，2006 年 4 月第 2 次印刷（1992 年 2 月第 1 版）。
- **书号与定版**：ISBN 7-03-016986-7（978-7-03-016986-0），中国版本图书馆 CIP 数据核字 (2006) 第 016593 号。
- **全书规模**：671 物理 PDF 页；正文印刷页 1–655（PDF 页码与正文印刷页码偏移量为 $\Delta = +16$）。
- **本地原件**：`raw/books/实验物理中的概率和统计_朱永生著.pdf`
- **原件 SHA-256**：`e97062665497c597609d58c23dfa977824c43e73d3ae8cb4ca3c0855e381894b`

## Scope and Reading Depth

本来源登记状态定为 `skimmed`，明确界定本轮针对极大似然法、小信号区间估计与假设检验的重点查验范围：
- **已核查章节**：
  - 封面、版权页、第二版前言与目录（PDF pp. 1–16）；
  - 第 8 章 极大似然法（印刷 pp. 242–292 / PDF pp. 258–308）：极大似然原理、渐近性质、剖面似然（Profile Likelihood）与非正态似然函数误差；
  - 第 9 章 最小二乘法（印刷 pp. 293–352 / PDF pp. 309–368）：线性与非线性最小二乘、直方图数据拟合、协方差矩阵反演；
  - 第 11 章 小信号测量的区间估计（印刷 pp. 370–383 / PDF pp. 386–399）：经典 Neyman 边界缺陷、似然比顺序求和（Feldman-Cousins 统一方法）；
  - 第 12 章 假设检验（印刷 pp. 384–465 / PDF pp. 400–481）：复合假设似然比检验、实验 $p$ 值、信号统计显著性 $Z$ 与 Wilks 定理。
- **未核查内容**：第 1–7 章概率论初步与常见分布细节、第 10 章矩法细节、第 13 章极小化算法（MINUIT 算法）与第 14 章蒙特卡罗方法全文。

## Summary

本书是中国科学院高能物理研究所朱永生研究员著述的实验物理统计学权威巨著。全书以严谨的数理逻辑紧密结合物理实验数据分析实务，系统阐述了误差传播、参数估计（极大似然、最小二乘）、小信号物理边界下的置信区间构造（Feldman-Cousins 方法）以及信号发现的统计显著性检验。在实验核结构与核谱学中，本书为微弱跃迁峰面积拟合、角分布多极混合比 $\delta$ 双根退化仲裁、以及谱线发现的 $5\sigma$ 准则提供了标准数理统计方法。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZHU-1 | 极大似然估计（MLE）渐近性：大样本下似然函数趋于高斯抛物线，参数协方差矩阵由 Fisher 信息阵的逆矩阵给出；非正态或小统计量下由剖面似然（Profile Likelihood）轮廓切线 $\Delta \ln\mathcal{L} = -0.5 \Delta\chi^2$ 确定非对称置信区间。 | model-result | direct | 第 8 章 §8.2–8.4, 印刷 pp. 245–262 / PDF pp. 261–278 | false |
| ZHU-2 | 数据加权直方图拟合的下偏缺陷：当直方图道计数 $n_i$ 较小（$n_i \le 10$）时，以 $1/n_i$ 作为权重的 Neyman 最小二乘卡方拟合会受到向下涨落数据点的过度加权拉扯，导致拟合面积出现系统性负偏差。 | model-result | direct | 第 9 章 §9.5, 印刷 pp. 325–331 / PDF pp. 341–347 | false |
| ZHU-3 | 小信号物理边界与 Feldman-Cousins 统一区间：当待测物理量受物理边界约束（$\mu \ge 0$）且伴随本底 $b$ 时，经典 Neyman 方法在 $n < b$ 时会出现无物理意义的负值或空集；基于似然比 $R(n) = P(n\|\mu+b)/P(n\|\mu_{\text{best}}+b)$ 顺序求和构造的 Feldman-Cousins 统一方法可自然平滑过渡并严格保证覆盖率。 | model-result | direct | 第 11 章 §11.1–11.2, 印刷 pp. 370–381 / PDF pp. 386–397 | false |
| ZHU-4 | 复合假设似然比检验与 Wilks 定理：定义统计检验量 $\Delta\chi^2 = -2\ln[\mathcal{L}(H_0)/\mathcal{L}(\hat{H})]$；当零假设成立且满足大样本正则条件时，$\Delta\chi^2$ 渐近服从自由度为 $\nu$ 的 $\chi^2$ 分布，单自由度下统计显著度近似为 $Z \approx \sqrt{\Delta\chi^2}$。 | model-result | direct | 第 12 章 §12.2 与 §12.5, 印刷 pp. 394–398, 429–434 / PDF pp. 410–414, 445–450 | false |
| ZHU-5 | Feldman-Cousins 似然比顺序求和统一置信区间：待测物理量受物理边界约束（$\mu \ge 0$）且伴随本底 $b$ 时，定义似然比 $R(n) = P(n|\mu+b)/P(n|\mu_{\text{best}}+b)$（其中 $\mu_{\text{best}} = \max(0, n-b)$）；按 $R$ 降序累加直至覆盖概率 $\ge \text{CL}$，严格消除空集与涵盖不足，在小计数下自动给出物理上限，大计数下自动平滑过渡为双侧区间。 | model-result | direct | 第 11 章 §11.2, 印刷 pp. 377–381 / PDF pp. 393–397, 式 (11.2.1)–(11.2.4) | false |
| ZHU-6 | DCO 与角分布多极混合比 $\delta(E2/M1)$ 剖面似然 $\chi^2(\theta_\delta)$、双实数根简并与联合物理判据：由有理二次方程 $R_{\text{DCO}}(\delta) = R_{\text{exp}}$ 产生的双实数根在统计上表现为 $\chi^2(\delta)$ 剖面的双极小，通过紧致化参数 $\theta_\delta = \arctan(\delta)$ 消除无穷大发散；联合线偏振度 $P(\delta)$、内转换系数 $\alpha_K(\delta)$ 与 Weisskopf 单粒子跃迁上限构建联合卡方 $\chi^2_{\text{joint}}$，利用对数似然比检验 $\Delta\chi^2 \ge 9.0$ 判定伪根在 $\ge 3\sigma$ 置信度被排除。 | model-result | direct | 第 6 章 §6.3, 第 8 章 §8.4, 第 12 章 §12.5; 印刷 pp. 182–190, 275–282, 440–448 / PDF pp. 198–206, 291–298, 456–464 | false |
| ZHU-7 | 加权最小二乘多项式拟合与强负协方差误差传播：在探测器效率刻度与能谱函数拟合中，多项式相邻阶次参数间具有极高负相关性（$\rho_{ij} \sim -0.80 \dots -0.99$）；必须通过全协方差矩阵 $\mathbf{V}_a = (\mathbf{X}^T \mathbf{W} \mathbf{X})^{-1}$ 计算任意能量点的雅可比方差 $\sigma^2(E) = \mathbf{j}^T \mathbf{V}_a \mathbf{j}$，若忽略非对角协方差项而采用简单的对角方差和将造成高达 $200\% \sim 600\%$ 的虚假误差高估。 | method/formalism | direct | 第 3 章 §3.4, 第 9 章 §9.1–9.3; 印刷 pp. 78–92, 295–315 / PDF pp. 94–108, 311–331 | false |

## Competing Interpretations and Limitations

- **小样本下的有限性与边界反常**：虽然极大似然法在大样本极限下具备一致性与最小方差优良性质，但在极其稀疏的小样本下（如每道平均计数接近 0），似然估计仍可能存在有限样本偏差；当待测参数位于物理边界（$\mu=0$）时，标准 Wilks 定理的高斯假设失效，必须采用 Cowan 等 2011 发展的单侧检验统计量 $q_0$ 分布修正。
- **角分布双根判定与先验依赖**：由单个角分布系数 $a_2$ 反解关于多极混合比 $\delta$ 的二次方程必然产生两个数学实数根，此时两解在卡方空间上完全简并，仅凭统计拟合优度本身无法决定物理真解，必须引入独立的物理先验（如 Clover 康普顿线偏振度 $P$ 或内转换系数 $\alpha_K$）联合破除简并。

## Extracted Pages

- 印刷 pp. 370–381（PDF pp. 386–397）：小信号测量的经典边界困境、似然比顺序求和（Feldman-Cousins 统一方法）及正态/泊松置信带构造。
- 印刷 pp. 242–262（PDF pp. 258–278）：极大似然法原理、Fisher 信息矩阵与剖面似然。
- 印刷 pp. 325–331（PDF pp. 341–347）：最小二乘法应用于直方图数据及数据加权偏差。
- 印刷 pp. 370–381（PDF pp. 386–397）：小信号测量的经典边界困境与 Feldman-Cousins 似然比排序构造。
- 印刷 pp. 429–434（PDF pp. 445–450）：实验 $p$ 值、统计显著性 $Z\sigma$ 与 Wilks 渐近卡方检验。
