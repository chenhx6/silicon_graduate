# 第 8 章：极大似然法与 Cramér-Rao 最小方差下限 (CRLB)

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 245–310 / 扫描 PDF pp. 261–326

---

## 1. 核心理论推导与数学基础

### 1.1 似然函数与极大似然原理
设独立同分布样本观测值为 $\vec{x} = (x_1, x_2, \dots, x_N)$，其单粒子概率密度函数为 $f(x; \vec{\theta})$，其中 $\vec{\theta} = (\theta_1, \dots, \theta_m)^T$ 为未知参数。
- **似然函数 (Likelihood Function)**：
  $$L(\vec{\theta}) = \prod_{i=1}^N f(x_i; \vec{\theta});$$
- **对数似然函数 (Log-Likelihood Function)**：
  $$\ln L(\vec{\theta}) = \sum_{i=1}^N \ln f(x_i; \vec{\theta});$$
- **极大似然估计量 (MLE, Maximum Likelihood Estimator)**：
  $$\hat{\vec{\theta}} = \arg\max_{\vec{\theta}} L(\vec{\theta}) = \arg\min_{\vec{\theta}} [-\ln L(\vec{\theta})].$$
在参数空间内部且函数可微时，估计量满足**似然方程组 (Likelihood Equations)**：
$$\left. \frac{\partial \ln L(\vec{\theta})}{\partial \theta_j} \right|_{\vec{\theta} = \hat{\vec{\theta}}} = 0, \quad j = 1, 2, \dots, m.$$

### 1.2 得分函数与 Fisher 信息矩阵
- **得分函数 (Score Function $S$)**：
  $$S(\vec{\theta}) = \nabla_{\vec{\theta}} \ln L(\vec{\theta}), \quad E[S(\vec{\theta})] = 0;$$
- **Fisher 信息矩阵 (Fisher Information Matrix $I(\vec{\theta})$)**：
  $$I_{jk}(\vec{\theta}) = \text{cov}(S_j, S_k) = E\left[ \frac{\partial \ln L}{\partial \theta_j} \frac{\partial \ln L}{\partial \theta_k} \right] = -E\left[ \frac{\partial^2 \ln L}{\partial \theta_j \partial \theta_k} \right].$$
对于 $N$ 个独立样本，总信息矩阵随样本量线性增长：$I_N(\vec{\theta}) = N \cdot I_1(\vec{\theta})$。

### 1.3 Cramér-Rao 不等式（最小方差理论极限）
设 $\hat{\vec{\theta}}$ 为参数向量 $\vec{\theta}$ 的任意无偏估计量（$E[\hat{\vec{\theta}}] = \vec{\theta}$），在满足正则条件（微分与积分次序可交换）下，其协方差矩阵 $V(\hat{\vec{\theta}})$ 满足**Cramér-Rao 不等式 (CRLB)**：
$$V(\hat{\vec{\theta}}) \ge I(\vec{\theta})^{-1}.$$
即矩阵 $V(\hat{\vec{\theta}}) - I(\vec{\theta})^{-1}$ 为半正定矩阵。
- **单参数形式**：
  $$\sigma^2(\hat{\theta}) \ge \frac{1}{I(\theta)} = \frac{1}{-E\left[ \frac{\partial^2 \ln L}{\partial \theta^2} \right]};$$
- **有效估计量 (Efficient Estimator)**：若无偏估计量的方差严格等于 CRLB 下限，称该估计量为充分有效的；极大似然估计在大样本渐近极限（$N \to \infty$）下严格达到 CRLB，且服从渐近正态分布：
  $$\hat{\vec{\theta}} \xrightarrow{d} \mathcal{N}\left(\vec{\theta}_0, I_N(\vec{\theta}_0)^{-1}\right).$$

### 1.4 极大似然估计的优良性质
1. **参数变换不变性 (Invariance)**：若待估参数变换为 $\phi = g(\theta)$，则 $\phi$ 的极大似然估计量直接为 $\hat{\phi} = g(\hat{\theta})$；
2. **相合性 (Consistency)**：在温和正则条件下，$\lim_{N \to \infty} P(|\hat{\vec{\theta}} - \vec{\theta}_0| < \varepsilon) = 1$；
3. **充分性 (Sufficiency)**：若存在充分统计量 $T(\vec{x})$，极大似然估计必通过 $T(\vec{x})$ 构成。

---

## 2. 轮廓似然法 (Profile Likelihood) 与干扰参数消解

当模型包含物理关注参数 $\vec{\psi}$（如四极形变 $\beta_2$ 或多极混合比 $\delta$）与干扰参数 $\vec{\lambda}$（如探测器绝对效率、本底斜率、束流强度），定义**轮廓似然 (Profile Likelihood)**：
$$L_{\text{prof}}(\vec{\psi}) = \sup_{\vec{\lambda}} L(\vec{\psi}, \vec{\lambda}) = L(\vec{\psi}, \hat{\hat{\vec{\lambda}}}(\vec{\psi})),$$
其中 $\hat{\hat{\vec{\lambda}}}(\vec{\psi})$ 为在固定参数 $\vec{\psi}$ 条件下的干扰参数条件极大似然解。
轮廓似然将高维优化问题严格投影为低维物理参数空间扫描，保持渐近卡方性质不变。

---

## 3. 核物理经典案例：指数衰变寿命未分道极大似然解

测量放射性核素衰变时间间隔序列 $t_1, t_2, \dots, t_N$，衰变常数为 $\lambda$（寿命 $\tau = 1/\lambda$），时间窗口为 $[0, T]$。
单粒子概率密度函数：
$$f(t; \lambda) = \frac{\lambda e^{-\lambda t}}{1 - e^{-\lambda T}}.$$
对数似然函数：
$$\ln L(\lambda) = N \ln \lambda - \lambda \sum_{i=1}^N t_i - N \ln(1 - e^{-\lambda T}).$$
求导置零导出解析似然方程：
$$\frac{1}{\hat{\lambda}} - \frac{T e^{-\hat{\lambda} T}}{1 - e^{-\hat{\lambda} T}} = \bar{t} = \frac{1}{N}\sum_{i=1}^N t_i.$$
当测量窗口 $T \gg \tau$ 时，截断效应消失，$\hat{\lambda} = 1/\bar{t}$，其方差达到 CRLB 下限：$\sigma^2(\hat{\lambda}) = \frac{\hat{\lambda}^2}{N}$。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-advanced-statistics-and-parameter-estimation-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`profile-lh` 子命令)
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
