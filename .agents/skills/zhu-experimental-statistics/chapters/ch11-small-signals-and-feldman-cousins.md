# 第 11 章：区间估计、物理边界与 Feldman-Cousins 统一方法

**来源专著**：朱永生《实验物理中的概率和统计（第二版）》（科学出版社 2006）
**对应页码**：印刷 pp. 415–460 / 扫描 PDF pp. 431–476

---

## 1. 核心理论推导与数学基础

### 1.1 经典 Neyman 置信区间构造原理
设测量观测值 $x$ 服从概率分布 $f(x; \theta)$。给定置信水平 $1 - \alpha$（如 $90\%$ 或 $68.27\%$）：
- 对每一个假定的参数真实值 $\theta$，构造观测空间中的接受域 $[x_1(\theta), x_2(\theta)]$，满足：
  $$P(x_1(\theta) \le x \le x_2(\theta) \mid \theta) = \int_{x_1(\theta)}^{x_2(\theta)} f(x; \theta) dx \ge 1 - \alpha;$$
- 在二维平面 $(\theta, x)$ 上联结所有接受域边界形成置信带；
- **带间反演**：实验测得具体数值 $x_{\text{obs}}$ 时，作垂直或水平截线截取置信带，获得关于参数的置信区间 $[\theta_{\text{low}}(x_{\text{obs}}), \theta_{\text{high}}(x_{\text{obs}})]$；
- **覆益率 (Coverage Probability)**：对任意固定的真实参数 $\theta$，置信区间覆盖真实值的概率必须严格满足：
  $$\text{Coverage}(\theta) = P\left(\theta_{\text{low}}(x) \le \theta \le \theta_{\text{high}}(x) \mid \theta\right) \ge 1 - \alpha.$$

### 1.2 物理边界效应与经典方法的崩溃
在实验物理测量中，许多物理量具有确定不变的物理边界约束（如信号强度 $S \ge 0$、分支比 $B \ge 0$、中微子质量平方 $m_\nu^2 \ge 0$）。
设已知泊松本底期望为 $b$，待测物理信号为 $\mu \ge 0$，总观测计数 $n \sim \text{Poisson}(\mu + b)$。
1. **空集与负区间缺陷**：当本底发生向下统计涨落（如已知本底 $b = 3.0$，而实测总计数 $n = 0$），经典双侧中心构造置信带给出的区间可能完全落在负值区（如 $[-3.0, -0.6]$），与物理边界 $\mu \ge 0$ 产生空集；
2. **翻转偏差 (Flip-flopping)**：若实验者在观测到大计数时选择报告双侧区间，而在观测到低计数时人为切换为报告“$90\%$ CL 上限”，这种根据数据观测结果动态决定区间类型的主观行为将导致严重的**欠覆盖（Undercoverage）**，名义 $90\%$ 的置信带实际覆盖率会急剧塌缩至 $85\%$ 甚至更低！

---

## 2. Feldman-Cousins (FC) 统一构造方法

### 2.1 似然比排序原则 (Likelihood Ratio Ordering Principle)
Feldman 与 Cousins (1998) 提出基于极大似然比商值 $R$ 排序的无偏构建法则：
$$R(n; \mu) = \frac{P(n \mid \mu + b)}{P(n \mid \hat{\mu}_{\text{phys}} + b)},$$
其中 $\hat{\mu}_{\text{phys}}$ 为受物理边界严格约束的最大似然估计量：
$$\hat{\mu}_{\text{phys}} = \max(0, n - b).$$
- 当 $n > b$ 时，$\hat{\mu}_{\text{phys}} = n - b$，$P(n \mid \hat{\mu}_{\text{phys}} + b) = P(n \mid n)$；
- 当 $n \le b$ 时，受非负物理边界约束，$\hat{\mu}_{\text{phys}} = 0$，$P(n \mid \hat{\mu}_{\text{phys}} + b) = P(n \mid b)$。

### 2.2 接受域算法流程
对每个确定的 $\mu \ge 0$：
1. 对所有可能的非负整数计数 $n = 0, 1, 2, \dots$，严格计算泊松概率 $P(n \mid \mu + b)$ 与排序商值 $R(n; \mu)$；
2. 将所有 $n$ 按照 $R(n; \mu)$ 从大到小降序排列；
3. 依序将排序居先的 $n$ 逐步加入接受域集 $\Omega(\mu)$，累加概率，直到累积和首次满足：
   $$\sum_{n \in \Omega(\mu)} P(n \mid \mu + b) \ge 1 - \alpha;$$
4. 确定该 $\mu$ 下的最小接受计数 $n_1(\mu) = \min \Omega(\mu)$ 与最大接受计数 $n_2(\mu) = \max \Omega(\mu)$。

### 2.3 FC 统一方法的颠覆性优势
- **零翻转偏差**：完全无需人工主观判断，算法在低计数时自然输出单侧上限（如 $[0, \mu_{\text{up}}]$），在高计数时自然平滑过渡为双侧对称测量带；
- **无空集困扰**：即使本底大幅向下涨落测得 $n = 0$，区间的下限始终为 $0$，绝不会出现空集或负数区间；
- **严格覆盖率保证**：离散泊松分布下，所有 $\mu \ge 0$ 均有 $\text{Coverage}(\mu) \ge 1 - \alpha$，彻底杜绝假阳性假阴性失真。

---

## 3. 核物理应用实战：微弱集体跃迁分支比上限确定

在在束 $\gamma$ 谱学寻找高自旋态三轴多声子摆动（Multiphonon wobbling）$n_w=2 \to n_w=1$ 弱电四极跃迁时，受强本底干扰未见清晰尖锐峰。
- 实验设定：拟合道区估算本底计数 $b = 4.2$ 个事件，测得观测计数 $n_{\text{obs}} = 2$；
- 经典方法：若强行扣除本底净计数为 $-2.2 \pm 2.4$，无法合理解释；
- **FC 统一推断 ($90\%$ CL)**：查阅或调用 FC 计算程序直接给出物理信号区间：
  $$\mu \in [0.00, 2.68] \text{ counts}.$$
结合探测器绝对全能峰效率 $\epsilon$ 与母带流强 $N_{\text{parent}}$，严格给出物理分支比的 $90\%$ CL 科学上限：
$$B_{\text{wobbling}} < \frac{2.68}{\epsilon \cdot N_{\text{parent}}}.$$

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/zhu-advanced-statistics-and-parameter-estimation-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`feldman-cousins` 子命令)
- **上游来源**：`knowledge/sources/book-zhu-probability-statistics-in-physics.md`
