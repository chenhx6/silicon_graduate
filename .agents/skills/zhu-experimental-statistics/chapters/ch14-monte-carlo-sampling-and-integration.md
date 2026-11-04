# 第 14 章：蒙特卡罗方法、随机抽样与自适应数值积分

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 581–645 / 扫描 PDF pp. 597–661

---

## 1. 核心理论推导与数学基础

### 1.1 蒙特卡罗方法原理与大数定律
蒙特卡罗（Monte Carlo, MC）方法是以概率统计理论为基础，通过计算机生成伪随机数序列模拟微观物理过程或求解高维数学积分的数值计算方法。
- **积分估计量**：考虑多维积分 $I = \int_\Omega f(\vec{x}) d\vec{x}$。设在区域 $\Omega$（体积为 $V$）内均匀独立抽取 $N$ 个随机点 $\vec{x}_1, \vec{x}_2, \dots, \vec{x}_N$：
  $$\hat{I}_N = \frac{V}{N} \sum_{i=1}^N f(\vec{x}_i);$$
- **方差与中心极限定理**：
  $$E[\hat{I}_N] = I, \quad \sigma^2(\hat{I}_N) = \frac{V^2}{N} \sigma_f^2 = \frac{V^2}{N} \left[ \frac{1}{V}\int_\Omega f^2(\vec{x}) d\vec{x} - \left(\frac{I}{V}\right)^2 \right];$$
- **维数无关收敛律**：估计误差按 $\sigma \propto N^{-1/2}$ 渐近收敛。与传统网格数值积分（如梯形法则误差为 $O(N^{-2/d})$，辛普森法则为 $O(N^{-4/d})$）相比，**当积分维数 $d \ge 4$ 时，蒙特卡罗方法的收敛效率全面压倒网格积分**。

### 1.2 连续型随机变量抽样方法
1. **逆变换抽样法 (Inverse Transform Method)**：
   - 若目标变量的一维概率分布函数 $F(x) = \int_{-\infty}^x f(t) dt$ 严格单调且解析可求逆；
   - 生成均匀随机数 $u \sim U(0, 1)$，令 $x = F^{-1}(u)$，则 $x$ 严格服从密度 $f(x)$。
   - 实例：指数分布 $f(t) = \lambda e^{-\lambda t} \implies t = -\frac{1}{\lambda} \ln(1 - u) = -\frac{1}{\lambda} \ln(u')$。
2. **Box-Muller 高斯变换**：
   - 从两个独立均匀随机数 $u_1, u_2 \sim U(0, 1)$ 生成两个独立标准正态随机数：
     $$z_1 = \sqrt{-2\ln u_1} \cos(2\pi u_2), \quad z_2 = \sqrt{-2\ln u_1} \sin(2\pi u_2).$$
3. **冯·诺依曼舍选抽样法 (Acceptance-Rejection Method)**：
   - 对任意复杂或不可解析求逆的概率密度 $f(x)$，构造已知易抽样的包络密度 $g(x)$，满足存在常数 $M \ge 1$ 使得 $f(x) \le M \cdot g(x)$ 对所有 $x$ 成立；
   - 步骤：
     1. 从 $g(x)$ 抽取候选样点 $x$；
     2. 独立抽取均匀随机数 $u \sim U(0, 1)$；
     3. **判定准则**：若 $u \le \frac{f(x)}{M g(x)}$，**接受**该点作为样本；否则**舍弃**该点，重回步骤 1。
   - 抽样效率严格为 $\eta = \frac{1}{M}$。

---

## 2. 方差缩减技术 (Variance Reduction)

为了在有限抽样次数 $N$ 下显著压低积分统计方差：
### 2.1 重要性抽样法 (Importance Sampling)
通过变换被积变量概率测度，将积分散布集中于被积函数幅值最大的核心贡献区：
$$I = \int \frac{f(\vec{x})}{g(\vec{x})} g(\vec{x}) d\vec{x} = E_g\left[ \frac{f(\vec{X})}{g(\vec{X})} \right].$$
若选取的参考分布 $g(\vec{x}) \approx |f(\vec{x})| / I$，则比值 $f(\vec{x}) / g(\vec{x}) \approx \text{const}$，方差理论上趋于零！

### 2.2 分层抽样法 (Stratified Sampling)
将总积分空间划分为 $k$ 个互不重叠的子区域 $\Omega = \bigcup_{j=1}^k \Omega_j$，在各子区域独立分配样点数 $N_j$ 进行积分。消除跨区域之间的宏观方差。

---

## 3. 核物理实验实战案例：HPGe 阵列有限立体角几何衰减因子 $Q_k$ 计算

在在束角分布 $W(\theta) = 1 + a_2 Q_2 P_2(\cos\theta) + a_4 Q_4 P_4(\cos\theta)$ 中，探测器晶体具有有限尺寸，导致角分布被平滑衰减。
- **几何积分模型**：圆柱形 HPGe 晶体正面半径 $R$，厚度 $L$，探测器距靶距离 $D$，准直吸收系数为 $\mu(E_\gamma)$。
- **蒙特卡罗模拟流程**：
  1. 从核反应点各向同性发射 $\gamma$ 射线方向向量 $(\theta, \phi)$；
  2. 追踪光子是否击中晶体表面并计算穿透晶体路径长度 $s(\theta, \phi)$；
  3. 赋以探测效率权重 $w = 1 - e^{-\mu s}$；
  4. 统计求和计算 Legendre 多项式加权均值：
     $$Q_k = \frac{\int P_k(\cos\alpha) \epsilon(\alpha) \sin\alpha d\alpha}{\int \epsilon(\alpha) \sin\alpha d\alpha} \approx \frac{\sum_{i=1}^N P_k(\cos\alpha_i) w_i}{\sum_{i=1}^N w_i}.$$
利用重要性抽样（仅在探测器立体角锥体内发射），在秒级时间内将 $Q_2, Q_4$ 的统计相对误差压缩至 $0.05\%$ 以内，为后续多极混合比 $\delta$ 的精密提取消除系统几何偏离。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-monte-carlo-integration-and-adaptive-sampling.md`
- **代码实现**：`system/scripts/analysis/monte_carlo_integrator.py`
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
