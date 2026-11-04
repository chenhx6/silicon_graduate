---
name: zhu-experimental-statistics
description: "朱永生《实验物理中的概率和统计》（第二版）：实验物理数据统计推断、多维非线性误差传播协方差、极大似然估计与CRLB下界、Levenberg-Marquardt非线性拟合、MINOS剖面似然非对称误差、Wilks定理似然比假设检验与Feldman-Cousins物理边界区间估计。"
---

<!-- argument-hint: [topic, method, algorithm, or chapter number] -->

# 实验物理中的概率和统计（第二版，朱永生）

**著者**：朱永生（中国科学院高能物理研究所） | **出版社**：科学出版社 (2006) | **页数**：671 页
**本地原件**：`raw/books/实验物理中的概率和统计_朱永生著.pdf` (SHA-256 `e97062665497c597609d58c23dfa977824c43e73d3ae8cb4ca3c0855e381894b`)

本技能将中国科学院高能物理研究所朱永生研究员的经典巨著《实验物理中的概率和统计（第二版）》转化为智能体技能，为在束核谱学数据处理、多维非线性参数拟合、协方差误差传播、角分布双根似然比裁决及实验物理测量置信区间估计提供坚实的数学与统计学支撑。

## How to Use This Skill

- **误差传播与协方差**：询问 `多维误差传播`、`非对角协方差反演`、`雅可比变换矩阵`、`相关系数影响`；
- **参数拟合与极小化**：询问 `极大似然法`、`CRLB最小方差下限`、`Levenberg-Marquardt算法`、`MIGRAD抛物线误差`、`MINOS轮廓似然非对称误差`；
- **假设检验与双根裁决**：询问 `似然比假设检验`、`Wilks定理`、`双根退化判决`、`发现显著性Z与p值换算`；
- **小信号与物理边界**：询问 `Feldman-Cousins统一方法`、`弱信号置信区间`、`覆益率Coverage保证`；
- **蒙特卡罗方法**：询问 `舍选抽样法`、`逆变换抽样`、`重要性抽样`、`多重数值积分`；
- **按章节调用**：调用 `ch03`（误差理论）、`ch08`（极大似然）、`ch09`（最小二乘与LM）、`ch11`（小信号与FC）、`ch12`（假设检验与Wilks）、`ch13`（极小化与MINUIT）或 `ch14`（蒙特卡罗）。

---

## Core Frameworks and Mental Models

1. **多维非线性误差传播协方差定律（第 3 章）**：
   - 设 $n$ 个关联测量量 $\vec{X} = (X_1, \dots, X_n)$ 的协方差矩阵为 $V_X$，经过非线性映射生成 $m$ 个物理量 $\vec{Y} = \vec{f}(\vec{X})$；
   - **一阶泰勒展开矩阵形式**：
     $$V_Y = J \cdot V_X \cdot J^T,$$
     其中雅可比矩阵元素为 $J_{ij} = \left.\frac{\partial f_i}{\partial X_j}\right|_{\vec{X} = \bar{\vec{X}}}$；
   - **相关性的决定性作用**：若 $X_1$ 与 $X_2$ 正相关（$\text{cov}(X_1, X_2) > 0$），差值 $Y = X_1 - X_2$ 的方差被大幅压缩：$\sigma_Y^2 = \sigma_1^2 + \sigma_2^2 - 2 \text{cov}(X_1, X_2)$；若盲目忽略非对角协方差，将导致误差评估产生重大系统偏离！

2. **极大似然估计与 Cramér-Rao 最小方差下界（CRLB，第 8 章）**：
   - **似然函数与对数似然**：$L(\vec{\theta}) = \prod_{i=1}^N f(x_i; \vec{\theta})$，对数似然 $\ln L(\vec{\theta}) = \sum_{i=1}^N \ln f(x_i; \vec{\theta})$；
   - **Fisher 信息矩阵**：
     $$I_{jk}(\vec{\theta}) = - E\left[ \frac{\partial^2 \ln L}{\partial \theta_j \partial \theta_k} \right];$$
   - **Cramér-Rao 不等式**：任何无偏估计量 $\hat{\vec{\theta}}$ 的协方差矩阵必然大于等于信息矩阵的逆：
     $$V(\hat{\vec{\theta}}) \ge I(\vec{\theta})^{-1}.$$
     极大似然估计在大样本渐近下严格达到 CRLB 下界（具备充分性、相合性与渐近有效性）。

3. **非线性最小二乘与 Levenberg-Marquardt 自适应阻尼算法（第 9 章）**：
   - 拟合目标函数：$\chi^2(\vec{\theta}) = \sum_{i=1}^N \frac{(y_i - f(x_i; \vec{\theta}))^2}{\sigma_i^2}$；
   - 传统高斯-牛顿法在大残差或非线性极强区域易发散，最陡下降法在狭长谷底收敛极其缓慢；
   - **Levenberg-Marquardt（LM）自适应阻尼步长**：
     $$\left[ J^T W J + \lambda \cdot \text{diag}(J^T W J) \right] \Delta\vec{\theta} = J^T W (\vec{y} - \vec{f}),$$
     其中 $\lambda$ 为阻尼因子。当迭代使 $\chi^2$ 减小时，减小 $\lambda$ 加快逼近高斯-牛顿二次收敛；当 $\chi^2$ 增大时，增大 $\lambda$ 退化为稳定保底的最陡下降步，完美解决多重能峰解卷积的非线性拟合稳定性。

4. **MINUIT 风格的极小化与非对称误差剖面（第 13 章）**：
   - **MIGRAD 抛物线误差**：在极小点 $\vec{\theta}^*$ 附近作二次泰勒展开，误差矩阵取自 Hessian 逆矩阵：$V = 2 \cdot H^{-1} = 2 \left[ \frac{\partial^2 \chi^2}{\partial \theta_j \partial \theta_k} \right]^{-1}$，仅在正态对称线性近似下有效；
   - **MINOS 轮廓似然非对称误差（Profile Likelihood）**：当参数非线性显著（如物理边界附近或比值分布）时，参数 $\theta_j$ 的下限 $\theta_j^-$ 与上限 $\theta_j^+$ 由**轮廓极小化约束条件**严格定义：
     $$\min_{\theta_{k \neq j}} \chi^2(\theta_j^\pm, \theta_{k \neq j}) = \chi^2_{\min} + \Delta\chi^2_{\text{cut}},$$
     对应 68.27% 置信度时 $\Delta\chi^2_{\text{cut}} = 1.0$；对应 95.45% 时为 $4.0$；对应 99.73%（$3\sigma$）时为 $9.0$。

5. **假设检验、Wilks 定理与发现显著性（第 12 章）**：
   - **复合假设似然比检验统计量**：
     $$\lambda = \frac{\sup_{\vec{\theta} \in \Theta_0} L(\vec{\theta})}{\sup_{\vec{\theta} \in \Theta} L(\vec{\theta})}, \quad -2 \ln \lambda = -2 [\ln L(H_0) - \ln L(H_1)] = \Delta\chi^2;$$
   - **Wilks 定理**：当零假设 $H_0$ 成立且样本容量足够大时，检验统计量 $-2\ln\lambda$ 渐近服从自由度为 $k$（两模型自由参数个数之差）的 $\chi^2(k)$ 分布；
   - **实验 $p$ 值与高斯等效显著性 $Z$**：
     $$p = \int_{\Delta\chi^2_{\text{obs}}}^\infty f(x; k) dx, \quad Z = \Phi^{-1}(1 - p) \approx \sqrt{\Delta\chi^2} \quad (k=1).$$
     排除零假设的标准门槛为：$Z \ge 3.0\sigma$ 视为“存在观测证据（Evidence）”；$Z \ge 5.0\sigma$（$p \le 2.87 \times 10^{-7}$）视为“确证发现（Discovery）”。

6. **小信号测量的 Feldman-Cousins 统一置信区间（第 11 章）**：
   - 经典 Neyman 构造在低计数小信号或物理边界（如信号非负 $S \ge 0$）附近会出现空集（$0$ 计数时得出负置信上限）或覆益率不足问题；
   - **Feldman-Cousins 似然比排序原理**：按似然比比值 $R(n; \mu) = \frac{P(n; \mu)}{P(n; \hat{\mu}_{\text{phys}})}$ 从大到小将观测值 $n$ 依序加入接受域，其中 $\hat{\mu}_{\text{phys}} = \max(0, n - b)$；
   - 自然顺畅地在未测到信号时的“给出上限（Upper limit）”与测到显著信号时的“给出双侧区间（Two-sided interval）”之间无缝切换，彻底消除触发条件翻转偏差（Flip-flopping）。

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核物理应用 |
|---|---|---|
| [ch03](chapters/ch03-error-propagation-and-covariance.md) | 误差理论与多维协方差传播 | 矩阵展开公式 $V_Y = J V_X J^T$、相关系数影响、寿命与形变误差传播 |
| [ch08](chapters/ch08-maximum-likelihood-and-crlb.md) | 极大似然法与 CRLB 方差下限 | 似然方程、Fisher 信息矩阵、剖面似然、大样本渐近有效性 |
| [ch09](chapters/ch09-least-squares-and-lm-algorithm.md) | 最小二乘与自适应 LM 阻尼极小化 | 线性与非线性最小二乘、Levenberg-Marquardt 阻尼迭代、直方图拟合 |
| [ch11](chapters/ch11-small-signals-and-feldman-cousins.md) | 小信号测量与 Feldman-Cousins 统一区间 | 物理边界约束（$S \ge 0$）、Neyman 缺陷消除、似然比排序构造、覆益率保证 |
| [ch12](chapters/ch12-hypothesis-testing-and-wilks-theorem.md) | 假设检验与 Wilks 定理显著性 | 似然比检验、Wilks 定理 $\Delta\chi^2 \sim \chi^2(k)$、$p$ 值与 $3\sigma/5\sigma$ 发现门槛 |
| [ch13](chapters/ch13-minimization-methods-and-minuit.md) | 极小化方法与 MINUIT 非对称误差 | 黄金分割、共轭梯度、MIGRAD 抛物线误差、MINOS 轮廓似然非对称误差 |
| [ch14](chapters/ch14-monte-carlo-sampling-and-integration.md) | 蒙特卡罗抽样与自适应积分 | 伪随机数、舍选抽样、逆 CDF 抽样、重要性抽样、多维相空间积分 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 实验统计推断、误差分析与假设检验专业术语定义。
- [patterns.md](patterns.md) — 5 大数据分析与似然极小化高阶实操范式。
- [cheatsheet.md](cheatsheet.md) — 统计置信度与 $\Delta\chi^2$ 阈值表、正态显著性 $Z$ 与 $p$ 值速查表。

---

## Scope & Limits

本技能提供实验物理统计推断、误差传播、非线性拟合与假设检验的严格数学基础。对于低能核实验仪器与探测方法，配合 `nuclear-experimental-methods`；对于三轴形变手征几何与摆动多极性双根仲裁，配合 `chirality-and-wobbling-atomic-nuclei`；对于高阶角分布公式推演，配合 `bohr-mottelson-nuclear-structure`。
