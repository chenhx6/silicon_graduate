# 第 9 章：最小二乘法与 Levenberg-Marquardt 自适应非线性拟合

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 311–370 / 扫描 PDF pp. 327–386

---

## 1. 核心理论推导与数学基础

### 1.1 最小二乘原理与目标函数
设对自变量 $x_i$ 测得响应量 $y_i$（$i=1, 2, \dots, N$），其误差矩阵为 $V_y$（独立测量时对角元为 $\sigma_i^2$），理论拟合模型为 $f(x; \vec{\theta})$，待估参数 $\vec{\theta} = (\theta_1, \dots, \theta_m)^T$。
- **广义加权卡方目标函数 ($\chi^2$)**：
  $$\chi^2(\vec{\theta}) = (\vec{y} - \vec{f}(\vec{\theta}))^T V_y^{-1} (\vec{y} - \vec{f}(\vec{\theta}));$$
  独立测量时化为标量加权形式：
  $$\chi^2(\vec{\theta}) = \sum_{i=1}^N \frac{(y_i - f(x_i; \vec{\theta}))^2}{\sigma_i^2}.$$

### 1.2 线性最小二乘与高斯-马尔可夫定理
若模型为参数的线性组合：$f(x_i; \vec{\theta}) = \sum_{j=1}^m X_{ij} \theta_j$，即矩阵形式 $\vec{f} = X \vec{\theta}$。
- **正规方程组 (Normal Equations)**：
  $$(X^T V_y^{-1} X) \hat{\vec{\theta}} = X^T V_y^{-1} \vec{y};$$
- **解析最优解与参数协方差**：
  $$\hat{\vec{\theta}} = (X^T V_y^{-1} X)^{-1} X^T V_y^{-1} \vec{y}, \quad V_{\hat{\vec{\theta}}} = (X^T V_y^{-1} X)^{-1};$$
- **Gauss-Markov 定理**：在所有线性无偏估计量中，最小二乘估计量具有严格最小方差（最佳线性无偏估计量，BLUE），且无需假设残差必须严格服从高斯分布。

---

## 2. 非线性最小二乘与 Levenberg-Marquardt 阻尼算法

### 2.1 高斯-牛顿迭代的病态性
对非线性模型在当前迭代点 $\vec{\theta}^{(k)}$ 作一阶泰勒展开，残差向量为 $\vec{r} = \vec{y} - \vec{f}(\vec{\theta}^{(k)})$，雅可比矩阵 $J_{ij} = \frac{\partial f_i}{\partial \theta_j}$，权重矩阵 $W = V_y^{-1}$。
- 高斯-牛顿法步长：
  $$(J^T W J) \Delta\vec{\theta} = J^T W \vec{r}.$$
**致命缺陷**：当参数初值偏离真值较远或多重峰高度关联时，矩阵 $J^T W J$ 近似奇异（条件数过大），导致步长 $\Delta\vec{\theta}$ 剧烈振荡甚至发散。

### 2.2 Levenberg-Marquardt (LM) 自适应阻尼步长
为了在高斯-牛顿法（二次超快收敛但局部脆弱）与最陡下降法（全局稳定保底但谷底极其缓慢）之间平滑权衡，引入自适应正定对角阻尼项 $\lambda \cdot D$：
$$\left[ J^T W J + \lambda \cdot \text{diag}(J^T W J) \right] \Delta\vec{\theta} = J^T W \vec{r}.$$
- **自适应动态调优律**：
  1. 计算测试步更新后的新卡方 $\chi_{\text{trial}}^2 = \chi^2(\vec{\theta} + \Delta\vec{\theta})$；
  2. **若 $\chi_{\text{trial}}^2 < \chi_{\text{current}}^2$**：表明局部二次近似有效，**接受**该步迭代更新 $\vec{\theta} \gets \vec{\theta} + \Delta\vec{\theta}$，并将阻尼因子调小 $\lambda \gets \lambda / \nu_{\text{down}}$（如除以 10），加速逼近高斯-牛顿收敛；
  3. **若 $\chi_{\text{trial}}^2 \ge \chi_{\text{current}}^2$**：表明曲率扭曲严重，**拒绝**该步更新，保持参数不变，将阻尼因子调大 $\lambda \gets \lambda \times \nu_{\text{up}}$（如乘以 10），步长方向转向负梯度最陡下降方向并缩短步长，确保数值单调下降。

---

## 3. 分道能谱拟合：Neyman 卡方、Pearson 卡方与 Baker-Cousins 似然比较

对于道计数 $n_i$ 与模型期望计数 $\mu_i(\vec{\theta})$：
1. **Neyman $\chi_N^2 = \sum \frac{(n_i - \mu_i)^2}{n_i}$**：在低计数道中发生除以零错误（需人工将 $n_i=0$ 剔除或加 1），更致命的是给小计数道赋予过大权重，导致拟合总积分峰面积发生 **$-10\% \sim -20\%$ 的系统低估**；
2. **Pearson $\chi_P^2 = \sum \frac{(n_i - \mu_i)^2}{\mu_i}$**：消除了 $n_i=0$ 除零奇异性，但方差包含理论期望，求导较为复杂；
3. **Baker-Cousins 泊松似然偏差 (Poisson Deviance)**：
   $$\chi_{\text{BC}}^2 = 2 \sum_{i=1}^N \left[ \mu_i - n_i + n_i \ln\left( \frac{n_i}{\mu_i} \right) \right].$$
   严格由极大似然比推导，完全克服所有小样本计数系统偏向，是大阵列核谱学低计数峰拟合的标准黄金准则。

---

## 4. 核谱学实战：重叠高斯多峰与线性本底解卷积

在 HPGe $\gamma$ 能谱中拟合双重叠峰：
$$f(x; \vec{\theta}) = a_0 + a_1 x + \frac{A_1}{\sqrt{2\pi}\sigma_1} \exp\left(-\frac{(x - \mu_1)^2}{2\sigma_1^2}\right) + \frac{A_2}{\sqrt{2\pi}\sigma_2} \exp\left(-\frac{(x - \mu_2)^2}{2\sigma_2^2}\right).$$
参数空间维度 $m = 8$。利用 LM 算法结合 Baker-Cousins 目标函数，即使两峰中心距小于 $1.5 \times \text{FWHM}$ 且伴随非对称拖尾，仍可稳定无偏提取净峰面积 $A_1, A_2$ 及其完整相关系数 $\rho_{A_1, A_2}$。

---

## 5. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-advanced-statistics-and-parameter-estimation-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`fit-multiplet` 子命令)
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
