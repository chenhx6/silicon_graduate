---
type: concept
title: "实验数据统计、协方差误差传播、泊松低计数极大似然与双根判据分选"
aliases: [实验物理统计, 误差传播, 协方差矩阵, 泊松似然, Baker-Cousins, 皮尔悖论, PPP, 双根判据, 多极混合比, 内转换系数分选, 偏振分选]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [experimental-statistics, covariance-propagation, baker-cousins-deviance, low-count-poisson, double-root-ambiguity, mixing-ratio-delta, peelles-puzzle, internal-conversion]
---

# 实验数据统计、协方差误差传播、泊松低计数极大似然与双根判据分选

## 1. 物理全景：从原始谱仪计数到可信物理结论的统计严密性

在实验核物理、束内 $\gamma$ 射线谱学与衰变数据评价中，实验物理学家直接面对的是探测器记录的离散脉冲计数（Counts）。
将这些离散计数转化为精确的物理量（能级寿命 $\tau$、电四极跃迁强度 $B(E2)$、磁偶极跃迁强度 $B(M1)$、多极混合比 $\delta$、截面 $\sigma$ 与形变参数）时，**统计处理的严谨性直接决定了科学发现的生死存亡**。

根据朱永生《实验物理中的概率和统计》（科学出版社）、O. Behnke 等《Data Analysis in High Energy Physics》以及 S. Baker & R. D. Cousins（NIM 221, 437, 1984）：
1. **多变量非对角协方差误差传播（Covariance Propagation）**：
   当测量变量之间存在共同的物理约束（如符合矩阵归一化、能级流强守恒）或共享相同的刻度因子（如靶厚度、束流积分流强、全能峰绝对探测效率）时，不同能级或通道的测量值之间存在显著的**非对角协方差（Covariance）**。忽视协方差、简单套用独立误差加和，将导致极度失真的 $\chi^2$ 拟合与严重系统偏倚（著名的核数据评价皮尔悖论，Peelle's Pertinent Puzzle, PPP）；
2. **极弱计数区 Poisson 极大似然与 Baker-Cousins 偏差（Baker-Cousins Deviance）**：
   在核物理前沿（如超重核合成、滴线核奇异衰变、弱衰变分支），每个道址仅有 $0 \sim 5$ 个计数。此时经典的 Neyman 最小二乘法（$\chi^2 = \sum (n_i - \mu_i)^2 / n_i$）在 $n_i = 0$ 时数学奇异发散，并在低计数时产生剧烈的**向下负偏倚**（系统性低估真实峰面积达 $30\%\sim 50\%$）。必须全面采用基于泊松分布的 Baker-Cousins 似然比 $\chi^2_\lambda$ 范式；
3. **角分布与 DCO 比值分析中的“双根判据”（Double-Root Ambiguity）**：
   实验上测得的在束 $\gamma$ 射线角分布系数 $a_2$ 或定向关联比值 $R_{\text{DCO}}$，由跃迁的多极混合比 $\delta(E2/M1)$ 决定。由于该依赖关系是关于 $\delta$ 的二次方程，数学反演必然产生两个实数根 $\delta_1$（通常极小，表示主要为 $M1$）与 $\delta_2$（通常极大，表示主要为 $E2$）。如何利用电子内转换系数（BrIcc）、线偏振度（Linear Polarization）与 Weisskopf 跃迁单粒子极限建立物理排除判据，是核谱学家的基本功。

---

## 2. 严格数学统计形式与误差矩阵算法

### (1) 多变量非线性协方差传播定理
设输入参量为 $n$ 维随机矢量 $\mathbf{x} = (x_1, \dots, x_n)^T$，其协方差误差矩阵为 $n \times n$ 阶实对称正定矩阵 $\mathbf{V}_x$：
$$(\mathbf{V}_x)_{ij} = \text{cov}(x_i, x_j) = \langle (x_i - \bar{x}_i)(x_j - \bar{x}_j) \rangle$$
输出参量为 $m$ 维矢量 $\mathbf{y} = \mathbf{f}(\mathbf{x}) = (f_1(\mathbf{x}), \dots, f_m(\mathbf{x}))^T$。
在输出参量围绕均值的一阶泰勒线性展开下，输出协方差矩阵 $\mathbf{V}_y$ 为：
$$\mathbf{V}_y = \mathbf{J} \mathbf{V}_x \mathbf{J}^T$$
其中 $\mathbf{J}$ 为 $m \times n$ 阶雅可比（Jacobian）矩阵：
$$J_{ik} = \frac{\partial f_i}{\partial x_k}$$
各输出量的方差即为对角元 $\sigma_{y_i}^2 = (\mathbf{V}_y)_{ii}$，归一化相关系数矩阵为：
$$\rho_{ij} = \frac{(\mathbf{V}_y)_{ij}}{\sigma_{y_i} \sigma_{y_j}} \in [-1, 1]$$

---

### (2) 共同标定不确定度合成与皮尔悖论（Peelle's Pertinent Puzzle, PPP）消除
在多通道核谱实验中，测量值 $y_i$ 受独立统计方差 $\sigma_{\text{stat}, i}^2$ 与共同相对标度不确定度 $\eta = \sigma_c / c$（如靶厚误差 $5\%$、束流积分误差 $3\%$）共同影响：
$$y_i = c \cdot x_i$$
总协方差矩阵形式为：
$$V_{ij} = \delta_{ij} \sigma_{\text{stat}, i}^2 + y_i y_j \eta^2$$
#### 经典陷阱（PPP 效应）：
若直接采用实验测量值构造协方差 $V_{ij} = y_i y_j \eta^2$，在利用广义最小二乘法（GLS）拟合多个不同实验组的截面时，由于低值测量点的绝对协方差人为偏小，拟合权重反常偏向低值点，导致加权平均结果**反常低于所有实验测量值**！
**正确解决方案**：在每次迭代中，必须使用理论模型期望值 $\mu_i \mu_j \eta^2$ 替代数据测量值 $y_i y_j \eta^2$ 构建权重矩阵，彻底消除非线性标度扭曲。

---

### (3) 低计数泊松拟合：Baker-Cousins 似然比 $\chi^2_\lambda$
对于计数较弱的谱线道址，观测计数 $n_i$ 服从均值为 $\mu_i$ 的 Poisson 分布：
$$P(n_i; \mu_i) = \frac{\mu_i^{n_i} e^{-\mu_i}}{n_i!}$$
构造极大似然对数比检验统计量（Likelihood Ratio Deviance）：
$$\lambda = \prod_i \frac{P(n_i; \mu_i)}{P(n_i; n_i)}$$
根据 Wilks 定理，其检验统计量渐近服从自由度为 $\nu$ 的卡方分布：
$$\chi^2_\lambda = - 2 \ln \lambda = 2 \sum_i \left[ \mu_i - n_i + n_i \ln\left(\frac{n_i}{\mu_i}\right) \right]$$
**边界约定**：当 $n_i = 0$ 时，$\lim_{n \to 0^+} n \ln(n/\mu) = 0$，此时单道贡献严格为 $2\mu_i$。

| 统计量类型 | 数学定义 | 低计数表现（$n_i \le 5$） | 奇异性 |
| :--- | :--- | :--- | :--- |
| **Neyman $\chi^2$** | $\sum (n_i - \mu_i)^2 / n_i$ | **严重系统负偏倚**（低估面积） | $n_i = 0$ 时除以零奇异发散 |
| **Pearson $\chi^2$** | $\sum (n_i - \mu_i)^2 / \mu_i$ | 无除零奇异，但参量估计收敛较慢 | 极值拟合非线性强 |
| **Baker-Cousins $\chi^2_\lambda$** | $2 \sum [\mu_i - n_i + n_i \ln(n_i/\mu_i)]$ | **无偏、标准一致、严格满足泊松统计** | **完全连续无奇异** |

---

## 3. 多极混合比 $\delta(E2/M1)$ 的双根判据分选协议

在在束 $\gamma$ 谱学中，对于初态自旋为 $I_i$、末态自旋为 $I_f$ 的混合跃迁（$M1 + E2$），定向分布系数 $A_2$（或规整化 DCO 比值 $R_{\text{DCO}}$）可表达为：
$$A_2(\delta) = B_2(I_i) \cdot \frac{F_2(I_f, 1, 1, I_i) + 2 \delta F_2(I_f, 1, 2, I_i) + \delta^2 F_2(I_f, 2, 2, I_i)}{1 + \delta^2}$$
式中 $B_2(I_i)$ 为核自旋取向参数（Alignment Parameter，通常 $0.8 \sim 0.9$），$F_k$ 为纯几何 Racah 耦合系数。

将实验测量值 $A_2^{\text{exp}}$ 代入，整理为关于 $\delta$ 的标准一元二次方程：
$$\left(F_{22} - \frac{A_2^{\text{exp}}}{B_2}\right) \delta^2 + 2 F_{12} \delta + \left(F_{11} - \frac{A_2^{\text{exp}}}{B_2}\right) = 0$$
判别式 $\Delta = (2F_{12})^2 - 4 (F_{22} - A_2/B_2)(F_{11} - A_2/B_2) \ge 0$ 时，数学上必然产生两个实数解：
$$\delta_1 \approx -0.1 \sim +0.2 \quad (\text{绝对值小, 近似纯 } M1), \qquad \delta_2 \approx +3 \sim +10 \quad (\text{绝对值大, 近似纯 } E2)$$

### 三重物理仲裁协议（Tri-Evidence Arbitration Protocol）
为了在 $\delta_1$ 与 $\delta_2$ 之间挑出真根、剔除数学伪根，必须采用如下互不相关的物理证据链：

1. **电子内转换系数（Internal Conversion Coefficient, $\alpha_K$）仲裁**：
   混合跃迁的理论 $K$ 壳层内转换系数为：
   $$\alpha_K(\delta) = \frac{\alpha_K(M1) + \delta^2 \alpha_K(E2)}{1 + \delta^2}$$
   由于低激发区 $\alpha_K(M1)$ 与 $\alpha_K(E2)$ 存在显著差异（往往相差 2 到 5 倍），通过磁谱仪或 HPGe 与 Si(Li) 符合测得的实验 $\alpha_K^{\text{exp}}$，能够以**决定性的区分度**直接判定：
   - 若实测 $\alpha_K^{\text{exp}} \approx \alpha_K(M1)$，则真解必为 $\delta_1$；
   - 若实测 $\alpha_K^{\text{exp}} \approx \alpha_K(E2)$，则真解必为 $\delta_2$；
2. **康普顿极化仪线偏振度（Linear Polarization, $P(90^\circ)$）仲裁**：
   利用 Clover 探测器四叶晶体横向散射与纵向散射的非对称度 $N_{\perp} - N_{\parallel}$ 提取偏振度 $P$：
   对于正宇称无翻转跃迁（如 $M1+E2$）：
   $$P(90^\circ) = \frac{3 a_2 \delta^2 - \dots}{1 + \delta^2} > 0$$
   线偏振度对多极混合比 $\delta$ 的符号和量级极度敏感，能够提供正交判据；
3. **Weisskopf 单粒子跃迁上限阻尼判据（Weisskopf Hindrance Rule）**：
   若某一根（例如大根 $\delta_2$）结合测得的能级寿命反演出的跃迁几率，要求 $B(E2) > 1000\text{ W.u.}$（物理上不可想象的超集体度）或使得伴随的 $B(M1) < 10^{-7}\text{ W.u.}$（极端反常受阻），则该根可被作为非物理数学伪根直接予以剔除！

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/experimental_uncertainty_covariance_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `stats` 命令。

### 运行示范（以协方差合成、低计数 Baker-Cousins 检验与双根仲裁为例）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py stats \
  --demo-baker --demo-cov --solve-roots \
  --A2 -0.28 --A2-err 0.04 --alpha-exp 0.033 --alpha-M1 0.035 --alpha-E2 0.012
```

### 计算输出核心物理特征：
1. **共同系统标度协方差合成**：对于 4 个测量点，在 $4\%$ 的系统刻度相对误差下，成功合成了非对角协方差矩阵，点间相关系数达到 $\rho \approx 0.38 \sim 0.50$，为后续无偏最小二乘拟合提供了严格协方差基准；
2. **极弱计数检验（含零计数）**：在包含 $0, 1, 2$ 等低计数的泊松通道中，Neyman $\chi^2$ 发生除零崩溃（`Undefined (n_i = 0)`），而 Baker-Cousins 极大似然给出了精确的 $\chi^2_\lambda = 1.554$，成功规避了零计数奇异与低计数假收敛；
3. **双根多极混合比仲裁**：
   - 二次方程给出两实根：$\delta_1 = -0.139 \pm 0.055$（主要为 $M1$），$\delta_2 = +6.135 \pm 2.079$（主要为 $E2$）；
   - 内转换系数 $\alpha_K$ 仲裁：$\delta_1$ 预言 $\alpha_K = 0.0346$，与实验测量值 $\alpha_K^{\text{exp}} = 0.0330$ 高度吻合（残差仅 $0.0016$）；而 $\delta_2$ 预言 $\alpha_K = 0.0126$（残差高达 $0.0204$）；
   - **自动裁决：`Root 1 (delta = -0.139) selected by internal conversion`**，完全消除了实验解的二义性！

---

## 5. 与相关前沿概念的交叉引用
- [[angular-distribution-and-multipole-mixing-ratios]]：经典的角分布双根模型在本文中得到了基于转换电子与偏振证据的完整物理闭环；
- [[internal-conversion-coefficients-bricc]]：BrIcc 高精度内转换系数直接充当双根判据仲裁的第一准则；
- [[ado-polarization-joint-spectroscopy]]：将 DCO/ADO 与 Clover 散射偏振测量联合，从第一性原理上消除多极混合比的非物理伪根。
