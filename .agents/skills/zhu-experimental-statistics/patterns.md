# Reasoning Patterns: 朱永生实验统计与高阶数据分析范式

提炼自朱永生《实验物理中的概率和统计（第二版）》的 5 大统计推断、误差分析与假设检验高阶分析范式。

---

## Pattern 1: 多维非线性误差传播与完整协方差反演范式

- **核心法则**：核物理测量量大多是多道实测数据（如峰面积、能量、寿命、分次探测效率）的非线性代数复合函数。若忽略非对角协方差项（误设 $\text{cov}(X_i, X_j) = 0$），将导致物理结果误差被严重低估或高估。
- **标准计算程序**：
  1. **构建输入量协方差矩阵 $V_X$**：对 $n$ 个直接测量量 $\vec{X} = (X_1, \dots, X_n)$，对角元填入方差 $\sigma_i^2$，非对角元填入公共刻度、本底共扣除或分次比引入的协方差 $V_{ij} = \rho_{ij} \sigma_i \sigma_j$；
  2. **推导雅可比偏导数矩阵 $J$**：对 $m$ 个导出物理量 $\vec{Y} = \vec{f}(\vec{X})$，严格求一阶偏导数 $J_{ki} = \left.\frac{\partial f_k}{\partial X_i}\right|_{\vec{X}_0}$；
  3. **计算输出误差矩阵 $V_Y$**：
     $$V_Y = J \cdot V_X \cdot J^T;$$
  4. **核结构典型实例（能级寿命 $\tau$ 与跃迁四极矩 $Q_t$ 误差）**：
     $$Q_t = \sqrt{\frac{16\pi}{5} \frac{B(E2; I \to I-2)}{\langle I K 2 0 | I-2 K\rangle^2}}, \quad B(E2) = \frac{0.08156 \cdot B_\gamma}{\tau \cdot E_\gamma^5 (1 + \alpha_T)},$$
     其中分支比 $B_\gamma$ 与能级寿命 $\tau$、峰能量 $E_\gamma$ 强相关。利用 $V_Y = J V_X J^T$ 可精确分离 $E_\gamma^{-5}$ 高次幂放大效应与分支比协方差。

---

## Pattern 2: 角分布与 DCO/极化双根剖面似然仲裁范式

- **核心法则**：在束 $\gamma$ 谱学测量中，方向角分布与角符合比值（DCO / ADO）对多极混合比 $\delta(E2/M1)$ 是非线性的二次分式函数，天然存在**两个数学等价的解根**（$\delta_1 \approx 0$ 弱 $E2$ 与 $\delta_2 \sim 3 - 8$ 强 $E2$）。单靠角分布数据无法破除该简并。
- **标准仲裁程序**：
  1. **构建角分布剖面似然曲线 $\chi_{\text{ang}}^2(\delta)$**：
     $$\chi_{\text{ang}}^2(\delta) = \min_{\alpha, A_0} \sum_{i=1}^{N_\theta} \frac{\left( W(\theta_i; \delta, \alpha, A_0) - Y_i \right)^2}{\sigma_i^2},$$
     其中 $\alpha = \sigma/J$ 为自旋取向衰减宽度，$A_0$ 为总强度归一化。该曲线必出现两个极小深谷 $\delta_1, \delta_2$，且 $\Delta\chi^2 \approx 0$；
  2. **引入独立正交物理观测量（康普顿线偏振度 $P$ 或转化系数 $\alpha_K$）**：偏振度对多极混合比具有正负号相反或正交的干涉响应；
  3. **联合剖面似然统计检验**：
     $$\chi_{\text{joint}}^2(\delta) = \chi_{\text{ang}}^2(\delta) + \frac{\left( P_{\text{theo}}(\delta) - P_{\text{exp}} \right)^2}{\sigma_P^2};$$
  4. **依据 Wilks 定理裁决**：
     $$\Delta\chi^2 = \chi_{\text{joint}}^2(\delta_2) - \chi_{\text{joint}}^2(\delta_1).$$
     - 若 $\Delta\chi^2 \ge 9.0$（$3.0\sigma$），排除次极小根；
     - 若 $\Delta\chi^2 \ge 25.0$（$5.0\sigma$），确证唯一起主导的物理真根，彻底粉碎伪物理模式（如 $^{135}\text{Pr}$ 中 $11.1\sigma$ 证伪摆动运动）。

---

## Pattern 3: 低计数泊松极大似然与无偏能峰解卷积范式

- **核心法则**：常规加权最小二乘法（Neyman $\chi^2 = \sum \frac{(y_i - f_i)^2}{y_i}$ 或 Pearson $\chi^2 = \sum \frac{(y_i - f_i)^2}{f_i}$）在低道计数（$y_i < 10$）或本底边缘道中存在严重系统偏向（Neyman 导致峰面积低估 $10\% - 20\%$）。小计数能谱拟合必须使用**泊松极大似然法（Baker-Cousins 似然偏差统计量）**。
- **标准拟合程序**：
  1. **构建 Baker-Cousins 泊松似然偏差目标函数 $\chi_P^2$**：
     $$\chi_P^2(\vec{\theta}) = -2 \ln \lambda_P(\vec{\theta}) = 2 \sum_{i=1}^M \left[ \mu_i(\vec{\theta}) - y_i + y_i \ln\left( \frac{y_i}{\mu_i(\vec{\theta})} \right) \right],$$
     规定当 $y_i = 0$ 时，末项极限为 $0$；
  2. **解析梯度与 Fisher 信息矩阵推导**：
     $$\frac{\partial \chi_P^2}{\partial \theta_j} = 2 \sum_{i=1}^M \left( 1 - \frac{y_i}{\mu_i} \right) \frac{\partial \mu_i}{\partial \theta_j}, \quad I_{jk} = \sum_{i=1}^M \frac{1}{\mu_i} \frac{\partial \mu_i}{\partial \theta_j} \frac{\partial \mu_i}{\partial \theta_k};$$
  3. **利用自适应阻尼算法极小化**：采用修改的 Levenberg-Marquardt 阻尼方程求解参数步长 $\Delta\vec{\theta}$；
  4. **检验渐近性**：当总计数极大时，$\chi_P^2$ 渐近趋近于标准高斯最小二乘 $\chi^2$；但在弱跃迁（如微弱退激支）中保证参数期望严格无偏。

---

## Pattern 4: Feldman-Cousins 物理边界与小信号区间构造范式

- **核心法则**：在核结构实验中探测稀有衰变、弱禁戒跃迁或微弱分支比时，测量量具有严密的非负物理边界（信号计数 $S \ge 0$）。经典 Neyman 构造在低观测计数甚至下浮动涨落时会给出空集或无物理意义的负置信区间；若实验者根据观测结果主观切换“给出上限”或“给出测量值”，将引发严重的翻转偏差（Flip-flopping）。
- **FC 统一构造算法**：
  1. **定义物理受限最大似然值 $\hat{\mu}_{\text{phys}}$**：对于泊松信号加已知本底 $n \sim \text{Poisson}(\mu + b)$，
     $$\hat{\mu}_{\text{phys}} = \max(0, n - b);$$
  2. **计算似然比排序度量 $R(n; \mu)$**：
     $$R(n; \mu) = \frac{P(n \mid \mu + b)}{P(n \mid \hat{\mu}_{\text{phys}} + b)};$$
  3. **依排序原则构造置信带**：对每个给定的理论真实参数 $\mu \ge 0$，将观测值 $n$ 按照 $R(n; \mu)$ 从大到小排列，依次将 $n$ 收入置信域 $[n_1(\mu), n_2(\mu)]$，直至累积概率首次达到标称置信度：
     $$\sum_{n = n_1}^{n_2} P(n \mid \mu + b) \ge 1 - \alpha;$$
  4. **带间反演**：实验测得具体计数 $n_{\text{obs}}$ 时，作水平切线截取所有使 $n_{\text{obs}} \in [n_1(\mu), n_2(\mu)]$ 成立的参数范围，严格获得区间 $[\mu_{\text{low}}, \mu_{\text{high}}]$。该区间在所有 $\mu \ge 0$ 上严格满足 Coverage $\ge 1 - \alpha$。

---

## Pattern 5: MINOS 轮廓极小化与非对称误差提取范式

- **核心法则**：高斯近似下的对称抛物线误差（$\theta \pm \Delta\theta$）仅在目标函数关于参数二次纯抛物线展开成立时可靠。当模型存在强非线性、关联长尾或物理边界时，必须采用 MINOS 轮廓极小化获取真实的非对称置信区间 $[\theta^- , \theta^+]$。
- **标准提取程序**：
  1. **寻找全局最小点**：利用极小化器找到最优解 $\vec{\theta}^* = (\theta_1^*, \dots, \theta_m^*)$，记录最低卡方 $\chi_{\min}^2$；
  2. **设定误差切割阈值**：对于 1 个物理参数，设定 $\Delta\chi^2_{\text{cut}} = 1.00$（$68.27\%$ CL）或 $3.84$（$95.0\%$ CL）或 $9.00$（$99.73\%$ CL）；
  3. **边缘消解其他参数（Profiling）**：定义一维剖面目标函数：
     $$\chi_{\text{prof}}^2(\theta_j) = \min_{\theta_{k \neq j}} \chi^2(\theta_j, \vec{\theta}_{k \neq j});$$
  4. **单根搜寻交点**：利用 Brent 根寻找法或高阶多项式外推，分别在 $\theta_j < \theta_j^*$ 与 $\theta_j > \theta_j^*$ 方向寻找方程解：
     $$\chi_{\text{prof}}^2(\theta_j^\pm) - \chi_{\min}^2 = \Delta\chi^2_{\text{cut}};$$
  5. **输出非对称置信区间**：报告格式为 $\hat{\theta}_j{}^{+\Delta\theta_j^+}_{-\Delta\theta_j^-}$，其中 $\Delta\theta_j^+ = \theta_j^+ - \theta_j^*$，$\Delta\theta_j^- = \theta_j^* - \theta_j^-$。
