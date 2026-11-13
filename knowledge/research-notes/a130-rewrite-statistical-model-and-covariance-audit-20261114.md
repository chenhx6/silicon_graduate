---
type: research-note
title: "A130 统计推断模型与协方差网络审计：似然条件、边界约束与误差传递界限"
aliases: [A130 statistical model and covariance audit, 谱学统计推断模型与协方差网络审计]
created: 2026-11-14
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "在在束 γ 谱学微观物理量提取中，如何构建联合前向似然、界定协方差传递适用范围，并厘清物理边界轮廓似然与 Feldman-Cousins 区间构建的理论区别？"
evidence_sources: [book-zhu-probability-statistics-in-physics, book-behnke-data-analysis-hep, book-bonamente-statistics-scientific-data, baker-cousins-1984-histogram-fits]
created_from: human-instruction
promotion_target:
tags: [a130, statistical-inference, likelihood-ratio, covariance-propagation, physical-boundary, feldman-cousins, wilks-theorem, forward-model]
---

# A130 统计推断模型与协方差网络审计：似然条件、边界约束与误差传递界限

## Research Trigger

在 A130 论文第 5 章第 5.10 节（统计推断与实验结果接口）的方法重写与父审深度校对中，梳理出核物理能谱反演中一系列常见但易被忽视的统计假定与数学边界问题：
1. **分箱独立泊松假定**：将多探测器离散计数能谱机械套用独立泊松连乘积，忽略了单次核反应退激发射多光子（级联多重度 $M_\gamma > 1$）引入的跨能仓物理相关，以及硬件触发与缓存容量引入的多项约束；
2. **不相关与独立性的混淆**：在误差传播公式中将“协方差为零”错误等同于“统计独立”，未严格区分一阶截断充分条件与高阶独立性要求；
3. **峰面积与校正产额协方差的因果混淆**：混淆原始解谱拟合净峰面积 $A_i$ 的局域协方差与探测效率校正后强度 $I_i$ 的跨能区协方差，强行假定所有效率相关必为正或分支比相关必为负；
4. **Wilks 定理自由度与 Hessian 缩放**：混淆轮廓似然检验统计量自由度与模型全参数维数，以及在最小化目标函数为 $-\ln\mathcal{L}$ 或 $-2\ln\mathcal{L}$ 时遗漏协方差估计的系数 2；
5. **物理边界约束与 Feldman-Cousins 构造**：在物理非负边界（$\mu \ge 0$）附近，误将连续轮廓似然截断 $\Delta\chi^2 = 2.71$ 当作通用的 Feldman-Cousins 覆盖，并在图示受限轮廓时错误移动观测中心值；
6. **蒙特卡罗推演分布与贝叶斯后验的界限**：将输入测量误差的前向采样推演（Pushforward Distribution）未加论证地称为贝叶斯后验分布。

本笔记系统形式化上述统计推断规范与数学推导，为在束核谱学数据处理与结果汇报保留可复用的方法与适用边界。

## Grounded Evidence

本笔记基于四项已完成原件物理核读的权威统计物理专著与权威论文：
1. [[book-zhu-probability-statistics-in-physics]]：
   - 朱永生 2006 专著《实验物理中的概率和统计（第二版）》（科学出版社，原件 `raw/books/实验物理中的概率和统计_朱永生著.pdf`，SHA-256: `e97062665497c597609d58c23dfa977824c43e73d3ae8cb4ca3c0855e381894b`，全书 671 物理页，本笔记所核章节偏移：印刷页码 + 16 = 物理 PDF 页码）；
   - 第 3 章 §3.9 误差传播公式（印刷第 67–70 页 / PDF 第 83–86 页）：式 (3.9.4)–(3.9.15) 推导了一阶 Taylor 展开下的协方差传播矩阵 $\mathbf{V}_y \approx \mathbf{J}\mathbf{V}_x\mathbf{J}^T$，指明该式仅在均值邻域内近似成立，并在正文中明确强调不相关变量（协方差为零）弱于统计独立性；
   - 第 11 章 §11.2 似然比顺序求和方法（印刷第 377–379 页 / PDF 第 393–395 页）：式 (11.2.2) 给出物理非负受限极大似然估计 $\mu_{\mathrm{best}} = \max(0, n - b)$，式 (11.2.3) 给出广义似然比排序比值 $R(n \mid \mu) = P(n \mid \mu + b) / P(n \mid \mu_{\mathrm{best}} + b)$，式 (11.2.4) 给出按 $R$ 降序累加构建 Neyman 接受带的标准算法；
   - 第 12 章 §12.2.2 复合假设的似然比检验（印刷第 394–398 页 / PDF 第 410–414 页）：证明了在大样本与参数空间内部正则条件下，轮廓似然比统计量 $-2\Delta\ln\lambda(\boldsymbol{\theta})$ 渐近服从自由度等于待测参数维数 $m = \dim(\boldsymbol{\theta})$ 的 $\chi^2$ 分布。
2. [[book-behnke-data-analysis-hep]]：
   - Olaf Behnke 等 2013 专著《Data Analysis in High Energy Physics》（Wiley-VCH，原件 `raw/books/Data Analysis in High Energy Physics, A Practical Guide to Statistical Methods (Olaf Behnke, Kevin Kroninger, Gregory Schott etc.) (Z-Library).pdf`，SHA-256: `18cf194b5cd4e86d8413244cf913fe5699de211a68e4a5d1164709e92fcbe84c`）；
   - Chapter 2 §2.3 Parameter Estimation（印刷第 37–38 页 / PDF 第 55 页）：明确指出 Wilks 定理中卡方自由度 $m$ 仅取决于待检验的物理参数集合大小，与通过轮廓极小化剖面消除的扰动参数维数无关，并对比了全局轮廓似然与局部对称 Hessian 抛物线近似的失效边界；
   - Chapter 4 §4.3 Frequentist Methods（印刷第 122–123 页 / PDF 第 138–139 页）：Table 4.2 给出泊松小信号均值在存在已知本底下的 Feldman-Cousins 统一区间数值表，阐述似然比排序规则如何自然消除非物理负值与空集困境。
3. [[book-bonamente-statistics-scientific-data]]：
   - Massimiliano Bonamente 2022 专著《Statistics and Analysis of Scientific Data (3rd Edition)》（Springer，原件 `raw/books/Statistics and Analysis of Scientific Data (Graduate Texts in Physics), 3rd Edition (Massimiliano Bonamente) (Z-Library).pdf`，SHA-256: `e5197dffd54d527b9d6925b92eeae34e0859e0062063861f2e54abf333d2b2ca`）；
   - Chapter 3 §3.3 The Poisson Distribution（印刷第 55–59 页 / PDF 第 76–80 页）：说明泊松分布与计数建模；下文独立稀疏化及级联事件的条件分析为本任务的模型推演，不把该页段当作完整点过程定理的直接引文；
   - Chapter 5 §5.2 Error Propagation Formulas（印刷第 83–87 页 / PDF 第 103–107 页）：推导多变量误差传播一般矩阵形式，例 5.3（印刷第 86 页 / PDF 第 106 页）专门给出了包含共享本底扣除时的方差与协方差传播推导。
4. [[baker-cousins-1984-histogram-fits]]：
   - Steve Baker & Robert D. Cousins 1984 论文《Clarification of the use of chi-square and likelihood functions in fits to histograms》（NIM 221 (1984) 437–442，原件 `raw/papers/gpt/learning-daily/20261013-DAY13-doppler-correction-recoil-velocity/baker-cousins-1984-histogram-fits-kekscan.pdf`，SHA-256: `e687601ebec8241a46db58aeeccffa2b4b252fe62c79db5b44ec51092e7c245a`）；
   - Sections 2 & 4（pp. 437–442）：建立了直方图多仓离散泊松计数似然的标准形式，定义了似然比偏离度统计量并阐明了小计数直方图中 Neyman 与 Pearson 加权最小二乘拟合的固有系统偏差。

## Provisional Reasoning

### 1. 前向联合似然与分箱独立性条件

在核谱学实验中，测得的能谱直方图 $\mathbf{n} = \{n_1, n_2, \dots, n_K\}$ 通常被写为独立泊松因子的乘积：
$$
\mathcal{L}_{\mathrm{binned}}(\boldsymbol{\theta}, \boldsymbol{\nu} \mid \mathbf{n}) = \prod_{k=1}^K \frac{\mu_k(\boldsymbol{\theta}, \boldsymbol{\nu})^{n_k} e^{-\mu_k(\boldsymbol{\theta}, \boldsymbol{\nu})}}{n_k!}.
$$
必须澄清该模型的适用前提：
1. **多光子事件的跨仓相关**：在多光子退激级联中，单个反应事件可贡献多个光子（级联多重度 $M_\gamma > 1$）。若不加符合门控，同一物理事件中发射的多个光子被探测器阵列同时记录，会在不同能量分箱中产生非零的事件级协方差。把泊松母事件互斥地分配至能量类别可得到独立泊松计数；对于可多重命中的事件，则须估计跨仓相关是否可忽略，符合门控本身不保证独立；
2. **束团微观泊松化与稀疏化**：在束流强度与接受概率近似稳定、事件之间可忽略相关的时间片内，可以用泊松点过程近似母事件。对互斥事件类别的独立稀疏化给出独立泊松计数；若一个母事件可产生多次记录，则得到的是聚类计数，小效率可能压低高阶相关，却不能单凭 $\varepsilon_k \ll1$ 断言各仓独立。束团结构、速率变化、触发及死时间须另行检查；
3. **辅助标定测量的联合概率密度**：完整的实验似然必须联合纳入探测器效率曲线、环境本底以及靶厚度等辅助标定数据 $\mathbf{a} = \{a_m\}$。由于辅助测量本身往往共享相同的放射源刻度或拟合模型，辅助约束不能简单写成不相关的单变量高斯乘积，而应表述为联合概率密度 $p_{\mathrm{aux}}(\mathbf{a} \mid \boldsymbol{\nu})$：
   $$
   \mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\nu} \mid \mathbf{n}, \mathbf{a}) = \left[ \prod_{k=1}^K \frac{\mu_k(\boldsymbol{\theta}, \boldsymbol{\nu})^{n_k} e^{-\mu_k(\boldsymbol{\theta}, \boldsymbol{\nu})}}{n_k!} \right] \times p_{\mathrm{aux}}(\mathbf{a} \mid \boldsymbol{\nu}).
   $$
   将这些扰动参数 $\boldsymbol{\nu}$ 纳入联合似然，能够定量描述由于参数不确定度诱导的宏观协方差；而对于多光子聚类等底层物理相关性，则需借助多维符合矩阵或事件级似然进行单独建模。

### 2. 协方差结构、行和约束与活时间分解

1. **总体理论方差与代入估计量**：
   对于瞬发--偶然符合扣除后的净信号 $S = P - aR$（其中 $a = \Delta T_P / \Delta T_R$ 为常数），在不重叠时间片与独立泊松假设下，总体均值 $\mu_P, \mu_R$ 满足理论总体方差：
   $$
   \mathrm{Var}(S) = \mu_P + a^2 \mu_R.
   $$
   在实际实验数据处理中，总体均值未知，广泛采用样本观测计数作为代入估计量（Plug-in Estimator）：
   $$
   \widehat{\mathrm{Var}}(S) = P + a^2 R.
   $$
   在科学论述中，必须严格区分理论方差恒等式与样本代入估计量，不可混同。
2. **一阶 Taylor 展开与不相关条件**：
   对于非线性映射 $\mathbf{y} = \mathbf{g}(\mathbf{x})$，误差传播矩阵为 $\mathbf{V}_y \approx \mathbf{J} \mathbf{V}_x \mathbf{J}^T$。标量方差为：
   $$
   \sigma_{y_i}^2 \approx \sum_k J_{ik}^2 \sigma_{x_k}^2 + 2 \sum_{k < l} J_{ik} J_{il} \mathrm{Cov}(x_k, x_l).
   $$
   交叉项消失的充分条件是一阶不相关（$\mathrm{Cov}(x_k, x_l) = 0$）或交叉项由于导数符号代数相消。不相关性弱于统计独立性：协方差为零并不保证变量完全独立，但在均值邻域的一阶截断下，不相关性已足以使平方和公式成立。
3. **行和约束与协方差符号**：
   对于同一母能级退激的全部总跃迁分支比 $\mathbf{b} = \{b_1, \dots, b_m\}$，归一化条件 $\sum_{k=1}^m b_k = 1$ 施加了刚性线性约束：
   $$
   \sum_{j=1}^m \mathrm{Cov}(b_i, b_j) = \mathrm{Cov}\left( b_i, \sum_{j=1}^m b_j \right) = \mathrm{Cov}(b_i, 1) = 0.
   $$
   由于对角方差 $\mathrm{Var}(b_i) > 0$，非对角协方差之和必然为负：$\sum_{j \ne i} \mathrm{Cov}(b_i, b_j) = -\mathrm{Var}(b_i) < 0$。但是，这并不意味着每一个非对角元 $\mathrm{Cov}(b_i, b_j)$ 都必须为负；所有非对角协方差恒为负是独立试验固定总数的多项分布（Multinomial）的特殊性质（$\mathrm{Cov}(n_i, n_j) = -N p_i p_j$）。在一般谱学测量中，若分支比由包含共同探测效率参数的各跃迁产额综合导出，某些分支对之间的协方差可能因共同校正因子的涨落而呈现正值。
4. **单道活时间份额与符合因式分解**：
   在单探测器谱中，强度校正为 $I_i = A_i / (\varepsilon(E_i) \cdot \mathrm{LT})$，其中 $\mathrm{LT} \in (0, 1]$ 为无量纲的活时间份额（Live-Time Fraction），该式假定了效率与活时间测量独立且信号无时间相关丢失。但在多探测器符合测量中，各探测单元受公共触发逻辑与硬件 FIFO 缓存制约，联合活时间包含各通道间的死时间阻塞相关性，不可简单表示为单道活时间的标量乘积。

### 3. 渐近 Wilks 定理、轮廓曲率与 Hessian 缩放

1. **Wilks 定理的自由度**：
   设全参数为 $(\boldsymbol{\theta}, \boldsymbol{\nu})$，其中 $\boldsymbol{\theta}$ 为 $m$ 维待测物理参数，$\boldsymbol{\nu}$ 为 $p$ 维伴随扰动参数。构建轮廓似然比统计量：
   $$
   \lambda(\boldsymbol{\theta}) \equiv \frac{\mathcal{L}(\boldsymbol{\theta}, \hat{\hat{\boldsymbol{\nu}}}(\boldsymbol{\theta}))}{\mathcal{L}(\hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\nu}})}, \quad q(\boldsymbol{\theta}) = -2\ln\lambda(\boldsymbol{\theta}).
   $$
   根据 Wilks 定理，在零假设处于参数空间内部（无物理边界截断）且大样本正则极限下：
   $$
   q(\boldsymbol{\theta}) \xrightarrow{d} \chi^2_m.
   $$
   其卡方自由度等于待测参数维数 $m = \dim(\boldsymbol{\theta})$，与伴随参数维数 $p$ 无关。
2. **Hessian 目标函数的系数 2 约定**：
   若以负对数似然 $F_1(\boldsymbol{\theta}) = -\ln\mathcal{L}$ 为目标函数，其在极小值处的 Hessian 矩阵为观测 Fisher 信息阵 $\mathbf{H}_1 = \nabla^2(-\ln\mathcal{L})$，协方差矩阵近似为：
   $$
   \mathbf{V}_{\boldsymbol{\theta}} \approx \mathbf{H}_1^{-1}.
   $$
   若以检验统计量 $F_2(\boldsymbol{\theta}) = -2\ln\mathcal{L} = 2 F_1$ 为目标函数，其 Hessian 矩阵为 $\mathbf{H}_2 = \nabla^2(-2\ln\mathcal{L}) = 2\mathbf{H}_1$，协方差矩阵满足：
   $$
   \mathbf{V}_{\boldsymbol{\theta}} \approx 2 \mathbf{H}_2^{-1}.
   $$
   在数据分析与代码实现中，若将二阶导数矩阵直接求逆而混淆了 $F_1$ 与 $F_2$，会导致协方差被错误放大或缩小 2 倍。

### 4. 物理边界、似然重标度与 Feldman-Cousins 统一构造

1. **物理边界下的似然统计量重标度**：
   当待测参数存在物理非负约束 $\mu \ge 0$ 时，若无约束极大似然估计处于统计负涨落点 $\hat{\mu} < 0$（例如 $\hat{\mu} = -0.6$，方差 $\sigma^2 = 1.0$）：
   - 无约束抛物线为 $q_{\mathrm{un}}(\mu) = (\mu - \hat{\mu})^2 = (\mu + 0.6)^2$；
   - 物理受限极大似然估计为 $\hat{\mu}_{\mathrm{phys}} = \max(0, \hat{\mu}) = 0$；
   - 严格定义在物理区域 $\mu \ge 0$ 上的检验统计量必须以物理受限极大似然值归一：
     $$
     q_{\mathrm{phys}}(\mu) = -2\ln\frac{\mathcal{L}(\mu)}{\mathcal{L}(\hat{\mu}_{\mathrm{phys}})} = (\mu - \hat{\mu})^2 - (0 - \hat{\mu})^2 = (\mu + 0.6)^2 - 0.6^2 = \mu^2 + 1.2\mu \quad (\mu \ge 0).
     $$
   - 必须特别注意：受限检验统计量满足 $q_{\mathrm{phys}}(0) = 0$ 且随 $\mu > 0$ 单调上升，但底层的观测数据中心值仍然是 $\hat{\mu} = -0.6$；绝不能为了使函数在 0 处取极小而将似然模型写成 $(\mu - 0)^2$（后者意味着人为篡改了实测数据，将观测值捏造为 0）。
2. **Feldman-Cousins 接受带反演与连续截断的本质区别**：
   - 经典的 Feldman-Cousins 统一方法是针对特定生成模型（如已知本底 $b$ 下的泊松计数 $n \sim \mathrm{Poisson}(\mu + b)$），在真实参数 $\mu \ge 0$ 空间上逐点构造 Neyman 接受带 $[n_1(\mu), n_2(\mu)]$；
   - 对每一个假定 $\mu$，计算所有整数观测值 $n$ 的似然比 $R(n \mid \mu) = P(n \mid \mu + b) / P(n \mid \mu_{\mathrm{best}} + b)$，按 $R$ 从大到小排序依次加入接受集，直到 $\sum P(n \mid \mu + b) \ge \text{CL}$；
   - 由于可观测计数 $n$ 为离散整数，接受区间的边界在参数 $\mu$ 扫描中呈现阶梯状跃变，其真实的频率学覆盖概率（Coverage Probability）通常高于名义置信水平（阶梯状过覆盖，Over-coverage）；
   - 在连续轮廓似然曲线上截取 $\Delta\chi^2 = 2.71$ 仅仅是渐近正态极限下一维单侧 $95\%$ 置信限的简单标尺，绝不能将连续抛物线截断等同于 Feldman-Cousins 离散接受带反演。

### 5. 蒙特卡罗误差推演与贝叶斯后验的因果界限

当利用非线性函数 $\mathbf{y} = \mathbf{g}(\mathbf{x})$ 进行数值误差传递时，常见的做法是对输入参量 $\mathbf{x}$ 进行随机抽样并计算 $\mathbf{y}$ 的样本分布：
1. **前向推演分布（Pushforward Distribution）**：若输入样本从测量仪器误差分布（如高斯测量误差）中抽取，输出直方图反映的是测量误差在非线性映射下的外推传播；
2. **后验成立的充分条件**：一个充分条件是输入样本已经来自于参数在给定测量数据下的条件后验概率分布 $p(\mathbf{x} \mid \mathbf{d})$（包含明确声明的先验分布与数据似然），此时经由 $\mathbf{g}(\mathbf{x})$ 映射的输出样本构成 $\mathbf{y}$ 的贝叶斯后验分布。仅仅在输入误差上形式化附加一个平坦先验，并不足以将前向推演分布直接作为贝叶斯后验解释。

## Assumptions

1. 假定核衰变事件的时间序列在宏观时间尺度上满足平稳泊松点过程；
2. 假定在束角分布与能谱拟合的局部参数空间内，似然函数关于微观参数二阶连续可微；
3. 假定仪器系统误差（如探测器效率与靶厚度）已通过独立的离线或在线辅助实验完成参数化标定。

## Competing Explanations

1. **小信号拟合出现负峰面积的解释**：
   - 解释 A（统计下涨落）：物理真实跃迁几率 $\mu \ge 0$ 为微弱正值，但由于环境散射连续本底较强，局域计数发生正常的泊松统计下涨落导致 $\hat{\mu} < 0$；
   - 解释 B（本底模型过高估计）：由于背景门跨越了邻近未分辨特征峰或康普顿边缘，局域线性插值过度扣除了本底，造成虚假负峰；
   - 解释 C（死时间或触发丢失）：高计数率下该通道发生脉冲堆积或通道丢失，导致表观记录数异常亏损。

## Transfer Conditions

1. 适用于基于 HPGe/Clover 探测器阵列的低能核结构在束 $\gamma$ 谱学实验数据分析；
2. 适用于从特征谱峰面积反演跃迁几率 $B(E2)$、$B(M1)$、寿命 $\tau$、混合比 $\delta$ 及衰变分支比等标准核物理参数的统计推断；
3. 适用于微弱谱线处于物理非负边界附近的上限评估，以及二次多极角分布的多解分支报告。

## Failure Conditions

1. 当重叠峰、本底与峰形参数存在强简并时，局域多高斯拟合协方差可能不足以描述不确定度；可采用完整前向谱模型、轮廓似然、参数模拟或声明先验的贝叶斯分析，并检验可辨识性。MCMC 是取样方法，本身不修复错误响应模型；
2. 当数据获取系统处于极度饱和状态（输入计数率接近麻痹型死时间极大值）时，探测器响应严重非线性，恒定活时间份额因式分解假设彻底失效；
3. 当频率学参数空间存在边界、参数不可辨识或样本过小时，Wilks 近似可能失效；可用适当的采样分布计算或覆盖检验构造频率学区间。贝叶斯先验截断与 Wilks 的模型正则条件应分别讨论。

## Falsification or Reverse Tests

1. **协方差行和归一检验**：在数据分析程序中提取所有出射分支比的协方差矩阵，检验任意一行元素之和 $\sum_{j=1}^m \mathrm{Cov}(b_i, b_j)$ 是否在浮点精度内严格归零；
2. **受限似然零点检验**：对于观测值 $\hat{\mu} = -0.6$，检验受限似然比检验统计量 $q_{\mathrm{phys}}(\mu) = \mu^2 - 2\hat{\mu}\mu$ 在 $\mu = 0$ 处是否精确取零，且对所有 $\mu > 0$ 严格单调递增；
3. **Hessian 因子 2 逆变检验**：对比数值优化程序输出的 $-\ln\mathcal{L}$ 与 $-2\ln\mathcal{L}$ 的二阶导数矩阵，验证由二者求出的参数方差是否完全一致（检查系数 2 是否正确配平）。

## Open Questions

1. 在包含上百个微弱谱线与数十个核素混合出射道的大规模在束实验中，如何构建计算可行的高维联合似然，避免过简化的分箱独立近似？
2. 对于深能级衰变中具有多个复杂中间异能态的级联系统，如何建立考虑时间关联的非泊松事件聚类点过程严格似然？

## Human Review

本笔记由执行代理根据 2026-11-13 与 2026-11-14 父审合同要求独立撰写，形式化第 5.10 节相关的统计推断理论、边界条件与数学推导；未记录新的用户审核事件。

## Promotion or Rejection History

2026-11-14：建立第 5.10 节统计推断模型与协方差网络审计永久知识笔记，记录前向测量似然条件、非线性协方差传递、渐近 Wilks 定理自由度、物理边界轮廓似然重标度与 Feldman-Cousins 统一区间的数学理论界限。

2026-11-14 总控复核：补全两项原件路径；撤回无来源的固定光子多重度量级，将点过程稀疏化标为条件化模型推演；修正 MCMC 必需论及先验导致 Wilks 失效的概念混用。该复核不是用户审核事件。
