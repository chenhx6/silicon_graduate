# 第 13 章：数值极小化方法与 MINUIT 非对称误差分析

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 521–580 / 扫描 PDF pp. 537–596

---

## 1. 核心理论推导与数学基础

### 1.1 目标函数极小化的一般数学表述
设连续实值目标函数为 $F(\vec{\theta})$（通常为负对数似然 $-2\ln L$ 或加权最小二乘 $\chi^2$），待估参数 $\vec{\theta} = (\theta_1, \dots, \theta_m)^T \in \mathbb{R}^m$。
- **极小点充要条件**：
  1. **一阶必要条件**：梯度向量为零，$\vec{g}(\vec{\theta}^*) = \nabla F(\vec{\theta}^*) = \vec{0}$；
  2. **二阶充分条件**：海森矩阵 (Hessian Matrix $H$) 严格正定，即对任意非零向量 $\vec{v}$，$\vec{v}^T H \vec{v} > 0$。

### 1.2 常用数值极小化算法比较
1. **一维搜索算法**：
   - **黄金分割法 (Golden Section Search)**：不需要导数信息，每次迭代按比例 $\tau = \frac{\sqrt{5}-1}{2} \a0.618$ 压缩搜索区间，线性收敛；
   - **Brent 抛物线插值法**：利用三点二次插值与黄金分割自适应切换，超线性收敛。
2. **最陡下降法 (Steepest Descent)**：
   - 迭代方向为负梯度方向：$\vec{d}^{(k)} = -\vec{g}^{(k)}$；在狭长谷底（奇异度高）时发生剧烈的“之”字形振荡，收敛速度极慢。
3. **共轭梯度法 (Conjugate Gradient, CG)**：
   - 构造关于 Hessian 矩阵正交的共轭方向：$\vec{d}^{(k)} = -\vec{g}^{(k)} + \beta_k \vec{d}^{(k-1)}$（Fletcher-Reeves 或 Polak-Ribière 公式）；仅需存储梯度向量，适合超多参数（$m > 100$）优化。
4. **变度量拟牛顿法 (Quasi-Newton, DFP / BFGS)**：
   - 不直接计算耗时的二阶偏导数矩阵，而是利用各步迭代的梯度差分序列自适应逼近逆海森矩阵 $G \approx H^{-1}$；具有二次终止性与超线性收敛速度。
5. **单纯形法 (Nelder-Mead Simplex)**：
   - 在 $m$ 维空间构造由 $m+1$ 个顶点构成的多面体，通过反射、扩展、收缩与压缩操作逐步包围极小点；无需导数，对抗目标函数不平滑或存在跳变极其稳健。

---

## 2. MINUIT 程序包架构与误差分析方法

MINUIT 是 CERN 与高能/核物理实验通用的权威极小化程序库，朱永生在第 13 章详述了其三大核心命令机制：

### 2.1 MIGRAD 与抛物线误差 (Parabolic Errors)
- **算法机制**：基于 Fletcher 变度量法（BFGS），动态更新协方差矩阵估计 $V$。
- **收敛判据 (EDM, Estimated Distance to Minimum)**：
  $$\text{EDM} = \frac{1}{2} \vec{g}^T V \vec{g} < 10^{-3} \times \text{UP} \times \text{TOLERANCE},$$
  其中 $\text{UP}$ 为误差定义常数（卡方下取 $1.0$，负对数似然下取 $0.5$）。
- **抛物线误差**：假设目标函数在极小点附近是纯二次抛物线，误差由逆 Hessian 给出：
  $$\sigma_j = \sqrt{2 \cdot (H^{-1})_{jj}}.$$

### 2.2 HESSE 局部曲率检验
在极小点处通过有限差分数值严密计算完整二阶偏导数矩阵：
$$H_{ij} = \frac{F(\vec{\theta}^* + \vec{\delta}_i + \vec{\delta}_j) - F(\vec{\theta}^* + \vec{\delta}_i) - F(\vec{\theta}^* + \vec{\delta}_j) + F(\vec{\theta}^*)}{h_i h_j}.$$
求逆后输出高精度的完整协方差矩阵 $V = 2 H^{-1}$ 与参数相关系数矩阵 $C$。

### 2.3 MINOS 轮廓似然非对称误差分析 (Profile Errors)
当物理模型具有强非线性、变量受物理边界约束或参数之间呈现高度弯曲的“香蕉形”关联时，抛物线对称近似彻底失效。
- **MINOS 轮廓极小化算法**：
  对关注参数 $\theta_j$，定义沿超平面的剖面函数：
  $$F_{\text{prof}}(\theta_j) = \min_{\vec{\theta}_{k \neq j}} F(\theta_j, \vec{\theta}_{k \neq j});$$
  分别向正负方向单维追踪，求解代数方程：
  $$F_{\text{prof}}(\theta_j^+) = F_{\min} + \text{UP}, \quad F_{\text{prof}}(\theta_j^-) = F_{\min} + \text{UP}.$$
- **非对称误差输出**：
  $$\sigma_j^+ = \theta_j^+ - \theta_j^*, \quad \sigma_j^- = \theta_j^* - \theta_j^-.$$
  MINOS 精确给出了多维曲面上正确的非对称置信边界，彻底杜绝人为经验近似。

---

## 3. 核结构实战案例：三轴位能面 (PES) 极小值搜寻与曲率惯量

在微观-宏观 Strutinsky 势能面计算中，形变能曲面 $E(\beta, \gamma)$ 具有两参数非线性几何结构：
1. **极小化初态定位**：使用 Nelder-Mead Simplex 在 $(\beta, \gamma) \in [0, 0.6] \times [0^\circ, 60^\circ]$ 网格粗搜寻局部极小核芯；
2. **精确收敛与惯量张量**：在粗极小点处启动 MIGRAD 快速收敛至绝对基态 $(\beta^*, \gamma^*)$；
3. **HESSE 刚度分析**：计算 Hessian 矩阵 $H_{\beta\beta}, H_{\gamma\gamma}, H_{\beta\gamma}$，判断原子核属于 $\gamma$-rigid 刚性三轴还是 $\gamma$-soft 软三轴；
4. **MINOS 形变不确定度**：在 $E_{\text{PES}} = E_{\min} + 0.5\text{ MeV}$ 轮廓线上扫描获取非对称形变涨落宽度 $\Delta\beta_{-\sigma_-}^{+\sigma_+}$ 与 $\Delta\gamma_{-\sigma_-}^{+\sigma_+}$。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-minimization-and-profile-error-contract.md`
- **代码实现**：`system/scripts/analysis/experimental_statistics_minimizer.py`
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
