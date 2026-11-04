# Glossary: 朱永生《实验物理中的概率和统计》核心术语与统计推断规范

本术语表汇编朱永生《实验物理中的概率和统计（第二版）》（科学出版社，2006）中的核心专业术语、中英文对照及严密数学定义，为核物理实验数据分析、参数拟合与误差评估提供统一统计语言。

---

## 1. 误差与协方差 (Error, Covariance and Propagation)

- **Statistical Error (统计误差 / 偶然误差)**: 由测量过程中的有限抽样涨落引起、随测量次数 $N$ 增加而按 $1/\sqrt{N}$ 缩小的随机偏差。
- **Systematic Error (系统误差)**: 由探测器标定不准、本底模型偏差、吸收修正截断等确定的非统计因素引起的恒定偏离或单向漂移。
- **Covariance Matrix (协方差矩阵 $V$ / 误差矩阵)**: 描述多维随机变量联合涨落的实对称半正定方阵，对角元为方差 $V_{ii} = \sigma_i^2$，非对角元为协方差 $V_{ij} = \text{cov}(X_i, X_j) = E[(X_i - \mu_i)(X_j - \mu_j)]$。
- **Correlation Coefficient (相关系数 $\rho_{ij}$)**: 无量纲归一化相关量，$\rho_{ij} = \frac{\text{cov}(X_i, X_j)}{\sigma_i \sigma_j} \in [-1, +1]$。$\rho > 0$ 表示正相关，$\rho < 0$ 表示负相关。
- **Jacobian Matrix (雅可比矩阵 $J$)**: 向量值函数 $\vec{Y} = \vec{f}(\vec{X})$ 的一阶偏导数矩阵，矩阵元 $J_{ij} = \frac{\partial f_i}{\partial X_j}$。
- **Error Propagation Law (协方差误差传播定律)**: 多维非线性变换下的一阶泰勒方差展开定理：$V_Y = J V_X J^T$。

---

## 2. 估计理论与极大似然 (Estimation Theory and Maximum Likelihood)

- **Estimator (估计量 $\hat{\theta}$)**: 仅依赖于样本观测数据 $\vec{x}$ 的统计量，用于推断母体未知真实参数 $\theta$。
- **Unbiasedness (无偏性)**: 估计量的数学期望严格等于待估参数的真值：$E[\hat{\theta}] = \theta$。
- **Consistency (相合性 / 一致性)**: 当样本容量 $N \to \infty$ 时，估计量依概率收敛于参数真值：$\lim_{N \to \infty} P(|\hat{\theta} - \theta| < \varepsilon) = 1$。
- **Efficiency (有效性)**: 在所有无偏估计量中具有最小方差的性质；若估计量方差达到 Cramér-Rao 下限，称为完全有效估计量。
- **Likelihood Function (似然函数 $L(\vec{\theta})$)**: 在给定观测样本 $\vec{x} = (x_1, \dots, x_N)$ 下，关于未知待估参数 $\vec{\theta}$ 的联合概率密度函数：$L(\vec{\theta}) = \prod_{i=1}^N f(x_i; \vec{\theta})$。
- **Log-Likelihood (对数似然函数 $\ln L(\vec{\theta})$)**: 似然函数的自然对数，通常采用求极大化 $\ln L$ 或极小化负对数似然（Negative Log-Likelihood, NLL $= -\ln L$）。
- **Score Function (得分函数 $S(\theta)$)**: 对数似然关于待估参数的一阶导数向量：$S(\vec{\theta}) = \nabla_{\vec{\theta}} \ln L$。极大似然估计解满足似然方程 $S(\hat{\vec{\theta}}) = 0$。
- **Fisher Information Matrix (Fisher 信息矩阵 $I(\vec{\theta})$)**: 得分函数方差或对数似然二阶导数负期望构成的正定方阵：$I_{jk}(\vec{\theta}) = -E\left[ \frac{\partial^2 \ln L}{\partial \theta_j \partial \theta_k} \right]$。
- **Cramér-Rao Lower Bound (CRLB, 克拉美-罗不等式)**: 任何无偏估计量协方差矩阵的理论极小下限：$V(\hat{\vec{\theta}}) \ge I(\vec{\theta})^{-1}$。极大似然估计在大样本极限下渐近达到 CRLB。
- **Profile Likelihood (剖面似然 / 轮廓似然 $L_{\text{prof}}(\theta_1)$)**: 在将其他冗余干扰参数（Nuisance parameters $\vec{\theta}_2$）在每个固定的物理参数 $\theta_1$ 处极小化边缘消解后的条件似然函数：$L_{\text{prof}}(\theta_1) = \sup_{\vec{\theta}_2} L(\theta_1, \vec{\theta}_2)$。

---

## 3. 最小二乘与非线性拟合 (Least Squares and Nonlinear Fitting)

- **Least Squares Method (最小二乘法 / LS)**: 寻求使测量值与理论模型预测值之间加权残差平方和 $\chi^2(\vec{\theta})$ 达到极小值的参数估计方法。
- **Chi-Square Objective Function ($\chi^2$ 目标函数)**: $\chi^2(\vec{\theta}) = (\vec{y} - \vec{f}(\vec{\theta}))^T V_y^{-1} (\vec{y} - \vec{f}(\vec{\theta}))$；独立误差下退化为 $\sum_{i=1}^N \frac{(y_i - f_i(\vec{\theta}))^2}{\sigma_i^2}$。
- **Degrees of Freedom (自由度 $\nu$ / ndf)**: 独立观测点数减去待估自由参数个数：$\nu = N - m$。
- **Reduced Chi-Square (约化 $\chi^2$ / $\chi_\nu^2$)**: $\chi^2 / \nu$。当模型合理且数据满足高斯误差假设时，其数学期望为 1；显著偏离 1（如 $> 1.5$ 或 $< 0.6$）预示模型欠拟合或误差估计过大/过小。
- **Normal Equations (正规方程组)**: 线性最小二乘法下导数等于零导出的线性代数方程组：$(J^T W J) \hat{\vec{\theta}} = J^T W \vec{y}$。
- **Gauss-Newton Algorithm (高斯-牛顿算法)**: 基于一阶雅可比近似展开 Hessian 矩阵的非线性最小二乘迭代算法：$\vec{\theta}^{(k+1)} = \vec{\theta}^{(k)} + (J^T W J)^{-1} J^T W (\vec{y} - \vec{f})$。
- **Levenberg-Marquardt Algorithm (LM 算法 / 自适应阻尼阻抗最小二乘)**: 在高斯-牛顿 Hessian 对角线上增加可控阻尼参数 $\lambda$ 的混合优化算法：$(J^T W J + \lambda D) \Delta\vec{\theta} = J^T W \Delta\vec{y}$。兼备最陡下降法的全局鲁棒性与高斯-牛顿法的二次收敛速度。

---

## 4. 假设检验与区间估计 (Hypothesis Testing and Interval Estimation)

- **Null Hypothesis ($H_0$, 原假设 / 零假设)**: 待检验的默认基准命题（如“无新物理信号”、“无三轴摆动成分”、“纯 $M1$ 多极性”）。
- **Alternative Hypothesis ($H_1$, 备择假设 / 备选假设)**: 零假设被排除时接受的竞争命题（如“存在摆动激发现象”、“存在微弱电四极 $E2$ 成分”）。
- **Type I Error ($\alpha$, 第一类错误 / 拒真概率 / 显著性水平)**: 零假设 $H_0$ 为真时却被错误拒绝的概率，常规设定为 0.05、0.01 或 $5\sigma$ 对应门槛。
- **Type II Error ($\beta$, 第二类错误 / 受伪概率)**: 零假设 $H_0$ 为假时却被错误接受的概率；其补集 $1 - \beta$ 称为**检验功效（Statistical Power）**。
- **Likelihood Ratio Test (似然比假设检验 / LRT)**: 以极大似然比统计量 $\lambda = \frac{L(\hat{H}_0)}{L(\hat{H}_1)}$ 评估两竞争模型优劣的严格统计检验。
- **Wilks' Theorem (威尔克斯定理)**: 当零假设成立、参数空间嵌套且正则条件满足时，检验统计量 $-2 \ln \lambda$ 在大样本极限下严格服从自由度为 $\Delta k$（自由参数数目之差）的 $\chi^2$ 分布。
- **p-value ($p$ 值)**: 在零假设 $H_0$ 成立的前提下，获得与当前实验观测统计量同样极端或更极端的样本结果的累积概率。
- **Gaussian Significance ($Z$, 高斯等效显著性)**: 将 $p$ 值通过单侧标准正态反累积分布函数映射所得的显著性度量：$Z = \Phi^{-1}(1 - p)$。物理学上 $Z \ge 3.0\sigma$ 称为观测证据（Evidence），$Z \ge 5.0\sigma$ 称为确证发现（Discovery）。
- **Confidence Level (CL, 置信水平 / 置信度 $1 - \alpha$)**: 重复多次相同实验所构造的置信区间覆盖待估参数真实值的长期频率占比（如 68.27%、90%、95%、99.73%）。
- **Coverage Probability (覆盖几率 / 覆益率)**: 给定参数真实值 $\mu$ 时，置信带区间包含 $\mu$ 的理论计算概率。若覆盖几率小于标称置信水平（Coverage $< 1 - \alpha$），称为**欠覆盖（Undercoverage）**，在实验物理中必须严厉杜绝。
- **Feldman-Cousins Unified Approach (FC 统一区间方法)**: 基于似然比排序原则（Likelihood Ratio Ordering）构造置信带的方法，彻底解决边界约束（如非负信号 $S \ge 0$）下 Neyman 构造出现的空集与翻转偏差（Flip-flopping），自然在置信上限与双侧测量区间之间平滑转换。

---

## 5. 极小化算法与 MINUIT 误差 (Minimization and MINUIT Error Analysis)

- **Hessian Matrix (海森矩阵 $H$)**: 目标函数对所有参数的二阶偏导数矩阵：$H_{ij} = \frac{\partial^2 \chi^2}{\partial \theta_i \partial \theta_j}$。在极小点处必须为正定矩阵。
- **MIGRAD (梯度极小化与抛物线误差分析)**: MINUIT 中的核心极小化程序，采用可变度量拟牛顿法（Davidon-Fletcher-Powell 或 BFGS 算法），收敛后由逆 Hessian 给出对称的抛物线协方差误差：$V = 2 H^{-1}$。
- **MINOS (轮廓似然非对称误差分析)**: MINUIT 中基于轮廓似然扫描的非对称误差计算程序，通过在多维参数空间沿超曲面 $\chi^2_{\text{prof}}(\theta_j) = \chi^2_{\min} + \Delta\chi^2_{\text{cut}}$ 追踪交点，精确确定非线性强扭曲参数的下限 $\theta_j^-$ 与上限 $\theta_j^+$。
- **HESSE (局部曲率误差矩阵重构)**: 在目标函数极值点处通过有限差分数值计算二阶导数海森矩阵，并求逆获取完整的参数协方差矩阵。
- **Dual-Root Degeneracy (双根退化 / 参数多解歧义)**: 由于非线性物理模型在参数空间存在对称性或局部次极小（例如角分布系数 $a_2(\delta)$ 对应两个截然不同的混合比根 $\delta_1 \approx 0$ 与 $\delta_2 \sim 3 - 8$），导致剖面似然曲线上出现两个分离极小点的现象。

---

## 6. 蒙特卡罗方法 (Monte Carlo Methods)

- **Pseudo-Random Number Generator (PRNG, 伪随机数发生器)**: 确定性算法生成的周期极长、统计分布均匀的伪随机数列（如 Mersenne Twister MT19937，周期为 $2^{19937} - 1$）。
- **Inverse Transform Sampling (逆变换抽样法)**: 设目标变量的累积分布函数为 $F(x)$，对区间 $[0, 1]$ 上的均匀随机数 $u$ 求解 $x = F^{-1}(u)$，生成精确服从 $F(x)$ 的随机抽样。
- **Acceptance-Rejection Sampling (舍选抽样法 / 冯·诺依曼舍选法)**: 构造包络函数 $g(x) \ge f(x)$，在二维空间均匀投点，仅保留落在曲线 $f(x)$ 下方的点，实现对任意复杂非归一化概率密度的精确抽样。
- **Importance Sampling (重要性抽样法)**: 在蒙特卡罗多重数值积分中，通过引入与被积函数形状高度相似的参考分布 $g(\vec{x})$，大幅降低抽样方差的方差缩减技术。
