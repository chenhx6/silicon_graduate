# 第 3 章：误差理论与多维协方差误差传播定律

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 65–110 / 扫描 PDF pp. 81–126

---

## 1. 核心理论推导与数学基础

### 1.1 随机变量的方差、协方差与相关系数
设 $n$ 维连续型随机向量 $\vec{X} = (X_1, X_2, \dots, X_n)^T$ 的联合概率密度函数为 $f(\vec{x})$，其均值向量为 $\vec{\mu} = E[\vec{X}]$。
- **方差 (Variance)**：
  $$\sigma_i^2 = V(X_i) = E[(X_i - \mu_i)^2] = \int (x_i - \mu_i)^2 f(\vec{x}) d\vec{x};$$
- **协方差 (Covariance)**：
  $$\text{cov}(X_i, X_j) = V_{ij} = E[(X_i - \mu_i)(X_j - \mu_j)];$$
- **相关系数 (Correlation Coefficient)**：
  $$\rho_{ij} = \frac{\text{cov}(X_i, X_j)}{\sigma_i \sigma_j}, \quad -1 \le \rho_{ij} \le +1;$$
- **协方差矩阵 (Covariance Matrix $V_X$)**：
  $$V_X = \begin{pmatrix} \sigma_1^2 & \rho_{12}\sigma_1\sigma_2 & \dots & \rho_{1n}\sigma_1\sigma_n \\ \rho_{21}\sigma_2\sigma_1 & \sigma_2^2 & \dots & \rho_{2n}\sigma_2\sigma_n \\ \vdots & \vdots & \ddots & \vdots \\ \rho_{n1}\sigma_n\sigma_1 & \rho_{n2}\sigma_n\sigma_2 & \dots & \sigma_n^2 \end{pmatrix}.$$
  $V_X$ 为实对称半正定矩阵，对其特征值分解满足所有特征值 $\lambda_k \ge 0$。

### 1.2 多维非线性误差传播定律（一阶泰勒展开）
设从输入测量向量 $\vec{X}$ 通过可微非线性函数映射到 $m$ 维导出物理向量 $\vec{Y} = \vec{f}(\vec{X}) = (f_1(\vec{X}), \dots, f_m(\vec{X}))^T$。
在输入量均值 $\vec{\mu}_X$ 附近作一阶泰勒展开：
$$Y_k \approx f_k(\vec{\mu}_X) + \sum_{i=1}^n \left. \frac{\partial f_k}{\partial X_i} \right|_{\vec{X} = \vec{\mu}_X} (X_i - \mu_{Xi}).$$
定义 $m \times n$ 阶**雅可比变换矩阵 (Jacobian Matrix $J$)**：
$$J_{ki} = \left. \frac{\partial f_k}{\partial X_i} \right|_{\vec{X} = \vec{\mu}_X}.$$
导出向量 $\vec{Y}$ 的协方差矩阵严格表示为矩阵二次型乘积：
$$V_Y = E[(\vec{Y} - \vec{\mu}_Y)(\vec{Y} - \vec{\mu}_Y)^T] = J \cdot V_X \cdot J^T.$$
展开为标量求和形式：
$$V_{Y, kl} = \sum_{i=1}^n \sum_{j=1}^n \frac{\partial f_k}{\partial X_i} \frac{\partial f_l}{\partial X_j} V_{X, ij}.$$

### 1.3 相关性对导出量方差的决定性作用
特别地，对于单个标量输出 $Y = f(X_1, X_2)$：
$$\sigma_Y^2 = \left( \frac{\partial f}{\partial X_1} \right)^2 \sigma_1^2 + \left( \frac{\partial f}{\partial X_2} \right)^2 \sigma_2^2 + 2 \left( \frac{\partial f}{\partial X_1} \right) \left( \frac{\partial f}{\partial X_2} \right) \rho_{12} \sigma_1 \sigma_2.$$
- **相减差值 $Y = X_1 - X_2$**：
  $$\sigma_Y^2 = \sigma_1^2 + \sigma_2^2 - 2 \rho_{12} \sigma_1 \sigma_2.$$
  若两测量量存在强正相关（如同一能谱的两个相邻重叠峰受共模本底或公共探测效率漂移调制，$\rho_{12} \to +1$），则其能级间隔或强度差值的误差被**大幅度消除**；若误将 $\rho_{12}$ 设为 0，将严重高估物理量的不确定度！
- **乘积或商值比率 $Y = X_1 / X_2$**：
  $$\left( \frac{\sigma_Y}{Y} \right)^2 = \left( \frac{\sigma_1}{X_1} \right)^2 + \left( \frac{\sigma_2}{X_2} \right)^2 - 2 \rho_{12} \left( \frac{\sigma_1}{X_1} \right) \left( \frac{\sigma_2}{X_2} \right).$$

---

## 2. 实验物理计算范式与算法实现

### 2.1 高阶非线性修正与二阶截断准则
当函数具有极强曲率且测量误差 $\sigma_i$ 较大时，一阶近似导致期望值发生偏移：
$$E[Y] \approx f(\vec{\mu}_X) + \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \left. \frac{\partial^2 f}{\partial X_i \partial X_j} \right|_{\vec{\mu}_X} V_{X, ij}.$$
**适用条件**：当二阶修正项 $\frac{1}{2} \text{Tr}(H V_X) \ll |f(\vec{\mu}_X)|$ 时，一阶矩阵法则完全精准成立。

### 2.2 核结构实验经典案例：能级寿命反演跃迁几率 $B(E2)$
由实测退激 $\gamma$ 能量 $E_\gamma$、能级寿命 $\tau$、总内转换系数 $\alpha_T$ 与跃迁分支比 $B_\gamma$ 计算约化跃迁几率：
$$B(E2) = C \cdot \frac{B_\gamma}{\tau \cdot E_\gamma^5 \cdot (1 + \alpha_T)}, \quad C = \frac{1}{1.225 \times 10^9 \text{ s}^{-1} \text{MeV}^{-5} e^2 \text{b}^2}.$$
输入参量向量 $\vec{X} = (B_\gamma, \tau, E_\gamma, \alpha_T)$，求对数对导数：
$$\frac{\sigma_{B(E2)}}{B(E2)} = \sqrt{\left(\frac{\sigma_{B_\gamma}}{B_\gamma}\right)^2 + \left(\frac{\sigma_\tau}{\tau}\right)^2 + 25\left(\frac{\sigma_{E_\gamma}}{E_\gamma}\right)^2 + \left(\frac{\sigma_{\alpha_T}}{1+\alpha_T}\right)^2 - 2 \rho_{B_\gamma, \tau} \frac{\sigma_{B_\gamma}}{B_\gamma}\frac{\sigma_\tau}{\tau}}.$$
可见能量相对误差被放大 **5 倍**，在能级寿命反演中必须保证高精度能量刻度与严密的协方差追踪。

---

## 3. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-advanced-statistics-and-parameter-estimation-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`error-prop` 子命令)
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
