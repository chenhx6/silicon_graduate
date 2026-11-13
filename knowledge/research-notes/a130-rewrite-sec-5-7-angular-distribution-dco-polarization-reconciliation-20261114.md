---
type: research-note
title: "A130博士论文第5.7节角分布、DCO与线偏振理论一致性核查与对齐"
aliases: [a130-sec-5-7-angular-dco-polarization-reconciliation, section-5-7-formalism-reconciliation]
created: 2026-11-14
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "project：A130论文5.7的原件/约定与反演核验"
promotion_target: ""
tags: [angular-distribution, dco, linear-polarization, mixing-ratio, doctoral-dissertation-a130]
evidence_sources: [book-hamilton-electromagnetic-interaction, lange-kumar-hamilton-1982-multipole-admixtures, campaign-g07-gorgen-2004-163lu-quadrupole-moments]
---

# A130 博士论文第 5.7 节角分布、DCO 与线偏振理论一致性核查与对齐

## Research Trigger

在 A≈130 区域非个人成果博士前置研究学位论文重写中，第 5.7 节《角关联、偏振和 $\delta$ 反演》建立了从在束 $\gamma$ 谱学空间角分布、双探测器方向角关联（DCO）与 Clover 康普顿线偏振度反演核态自旋宇称 $I^\pi$ 及电四极/磁偶极振幅混合比 $\delta(E2/M1)$ 的统一形式体系。
经过独立窄审（T19）核查原件并由领导审查接受，本研究笔记记录针对第 5.7 节全部 10 项审计发现（F01–F10）的实际原件溯源、数学推导与规范对齐。

## Provisional Reasoning

### 1. 统计取向张量 $B_k(I_i)$ 与去取向因子 $U_k$（F01, F04）
- **Clebsch-Gordan 次序与相位**：
  在所选轴对称量子化基下，母态统计取向张量定义为
  $$B_k(I_i) \equiv \sqrt{2I_i + 1} \sum_{M_i} (-1)^{I_i - M_i} \langle I_i M_i I_i (-M_i) \mid k 0 \rangle P(M_i).$$
  Clebsch-Gordan 系数的自变量次序使得该定义与 Hamilton 经典专著第 12 章式~(12.73)（PDF 529，印刷页 518）相差一个 $(-1)^k$ 相位：$B_k = (-1)^k B_k^{\mathrm{Hamilton}}$。对于未分析偏振的角分布所使用的偶数阶（$k=0,2,4$），$(-1)^k = +1$，二者完全一致；对于奇数阶（如 $I=1/2$ 时），$B_1 = -B_1^{\mathrm{Hamilton}}$。归一化性质 $B_0(I_i) \equiv 1$ 对任意满足 $\sum_{M_i} P(M_i) = 1$ 的布居分布恒成立。
- **无重复去取向因子原则**：
  若母态经由单一未观测前级级联退激至 $I_i$，前级级联退取向为 $B_k(I_i) = B_k(J_{\mathrm{CN}}) \prod_m U_k(m)$（Hamilton 式~(12.209)–(12.213)，PDF 563）。一旦目标态的实际取向度由 $B_k(I_i)$ 表征，角分布展开式 $W(\theta) = \sum_{k} B_k(I_i) A_k(\delta) Q_k P_k(\cos\theta)$ 与拟合表观系数 $a_k = B_k(I_i) Q_k A_k(\delta)$ 中绝不可再次乘入相同的 $U_k$。

### 2. 奇阶消失的物理机制：布居对称性 vs 螺旋度求和（F02）
- 沿束流轴的轴对称性保证方位角量子数 $q = 0$。磁子能级布居对称性 $P(M_i) = P(-M_i)$ 是取向张量奇阶严格为零（$B_{\mathrm{odd}} = 0$）的充要条件。
- 然而，即使母态具有非零奇阶取向（$P(M_i) \ne P(-M_i)$），对于具有确定宇称的核态之间的通常单光子电磁跃迁，未分析光子偏振时必须对出射光子的两个螺旋度（$\lambda = \pm 1$）求和。由 Hamilton 式~(12.180)–(12.189)（PDF 553–555），螺旋度求和产生因子 $\sum_{\lambda=\pm 1} \lambda^k = 1 + (-1)^k = 0$（当 $k$ 为奇数时）。因此，未分析偏振强度的奇阶消失是由宇称守恒与螺旋度相消共同决定的。
- 张量阶数受三角定则严格截断：$k \le \min(2I_i, 2L_{\max})$。对于偶极与四极混合辐射（$L_{\max}=2$），级数仅包含 $k=0,2,4$。

### 3. 多极混合比与正干涉相位的 Krane-Steffen（KS）体系（F03）
- **混合比定义与算符量纲**：
  $$\delta(E2/M1) \equiv \frac{\sqrt{3}}{10} \frac{E_\gamma}{\hbar c} \frac{\langle I_f \| \mathcal{M}(E2) \| I_i \rangle}{\langle I_f \| \mathcal{M}_S(M1) \| I_i \rangle} = \frac{\sqrt{3}}{10} \frac{E_\gamma}{\hbar} \frac{\langle I_f \| \mathcal{M}(E2) \| I_i \rangle}{\langle I_f \| \mathcal{M}_\mu(M1) \| I_i \rangle}.$$
  与第 5.9 节及附录 A 完全一致，算符 $\mathcal{M}_S(M1) \equiv \mathcal{M}_\mu(M1)/c$ 具有电荷型量纲 $e\cdot\mathrm{fm}$，配合动量因子 $k_\gamma = E_\gamma/(\hbar c)$（$\mathrm{fm}^{-1}$）；或采用磁矩型算符 $\mathcal{M}_\mu(M1)$（$\mu_N$）与频率因子 $E_\gamma/\hbar$，导出严格无量纲纯数。
- **干涉项符号与体系转换**：
  角分布系数 $A_k(\delta) = \frac{F_k(1 1) + 2\delta F_k(1 2) + \delta^2 F_k(2 2)}{1 + \delta^2}$ 中的正交叉干涉项 $+2\delta F_k(1 2)$ 严格对应于 Krane-Steffen（KS）约定（Hamilton 式~(12.185)，PDF 553；Lange 等人 1982 式~(2.8b)，PDF 4，印刷页 122）。在发射退激过程中，Krane-Steffen 约定与 Rose-Brink（RB）约定的混合比相差一个负号：$\delta_{\mathrm{KS}} = -\delta_{\mathrm{RB}}$。将正干涉式误标为 Rose-Brink 会造成自相矛盾。

### 4. 康普顿线偏振度与响应参数（F05, F09）
- **偏振度定义与缔合 Legendre 展开**：
  $$P(\theta) \equiv \frac{W_\parallel(\theta) - W_\perp(\theta)}{W_\parallel(\theta) + W_\perp(\theta)} = \frac{\sum_{k \ge 2, \,\mathrm{even}} B_k(I_i) A_k^{\mathrm{pol}}(\delta) Q_k^{\mathrm{pol}} P_k^2(\cos\theta)}{\sum_{k \,\mathrm{even}} B_k(I_i) A_k(\delta) Q_k P_k(\cos\theta)}.$$
  若采用 Hamilton 的偏振系数 $A_{k2}$（Hamilton 第 15 章式~(15.9)–(15.15)，PDF 727–728），缔合 Legendre 多项式 $P_k^2(\cos\theta)$ 前须包含归一化因子 $2\sqrt{\frac{(k-2)!}{(k+2)!}}$（$k=2$ 时为 $1/\sqrt{6}$；$k=4$ 时为 $1/\sqrt{90}$）。
- **物理量区分**：
  $Q_k^{\mathrm{pol}}$ 为偏振张量的几何有限立体角衰减因子；偏振度由实验不对称度 $A_{\mathrm{exp}} = (N_\perp - a N_\parallel)/(N_\perp + a N_\parallel)$ 提取时使用的 $Q(E_\gamma)$ 为康普顿偏振仪的偏振灵敏度/分析本领（Analyzing Power），二者不可混淆。
- **原件页码纠正**：
  Hamilton PDF 355 对应印刷页 344，为第 10 章内转换系数测量；真实的线偏振理论位于第 12 章式~(12.198)（PDF 556）及第 15 章（PDF 727–728）。

### 5. DCO 二次有理反演的严格求解与边界（F06）
- **去分母伪根筛除**：
  由 $R_{\mathrm{DCO}} = N(\delta)/D(\delta)$ 交叉相乘得到二次方程 $(n_2 - R d_2)\delta^2 + (n_1 - R d_1)\delta + (n_0 - R d_0) = 0$。求得的任何有限根 $\delta^*$ 必须检验 $D(\delta^*) \ne 0$；分母为零的点为代数去分母引入的伪根，必须剔除。
- **纯多极端点与齐次投影坐标**：
  引入齐次坐标 $\delta = u/v$（$v \to 0$ 对应 $|\delta| \to \infty$），二次型为 $(n_2 - R d_2)u^2 + (n_1 - R d_1)uv + (n_0 - R d_0)v^2 = 0$。当 $d_2 \ne 0$ 且 $R = n_2/d_2$ 时，方程在 $v=0$ 处成立。极限端点 $\delta \to \pm\infty$ 在物理上代表同一纯四极辐射态，且物理比值在无穷远具有良好极限 $n_2/d_2$，并非物理响应的奇异极点。
- **双解保留准则**：
  判别式大于零时给出的两个有限实根均为数学与实验统计相容解。在缺乏高精度偏振或内转换独立鉴别前，必须如实保留两支候选解，严禁用理论模型偏好人为舍弃其中之一。

### 6. 教学图脚本的正定性证明（F08）
在示意图脚本 `system/scripts/a130_angular_branch_figure.py` 中：
- 分子 $N(\delta) = 0.65 - 0.30\delta + 1.10\delta^2$（判别式 $-2.77 < 0$）与分母 $D(\delta) = 1.05 + 0.15\delta + 0.95\delta^2$（判别式 $-3.9675 < 0$）在实数域恒为正。
- 未偏振强度 $W(\delta) = 1.00 + 0.10\delta + 0.80\delta^2$（判别式 $-3.19 < 0$）恒为正。
- 正交偏振分量强度 $W + H = 0.55 + 0.70\delta + 1.45\delta^2$（判别式 $-2.70 < 0$）与 $W - H = 1.45 - 0.50\delta + 0.15\delta^2$（判别式 $-0.62 < 0$）在实数域恒为严格正。
- 因此 $|P(\delta)| < 1$ 恒成立，无需且不可使用 `np.clip` 掩盖非物理输入；图例明确标注为假设观测带（Hypothetical Band），图注声明为代数教学模型。


## 父增量核验与边界

来源入口：[[book-hamilton-electromagnetic-interaction]]、[[lange-kumar-hamilton-1982-multipole-admixtures]]、[[campaign-g07-gorgen-2004-163lu-quadrupole-moments]]。T19的原件与符号窄审已实际重放；本轮检查增量正文及图的系数/根/偏振值。Q(E)和Q_k均无量纲，作用不同；P=A/Q要求已标定的非零分析本领。线偏振是电磁指定的额外约束之一，可与内转换和其它锚点联合使用。观测是否统计独立仍要核共同事件和校准。

Apol系数吸收Hamilton所列2sqrt[(k−2)!/(k+2)!]因子。纯高阶端点的有限比值结论以d2非零为前提；所有根都需保持原响应定义域。广义最小二乘可在声明的均值与协方差近似下使用，不自动给非正则情形的精确覆盖。

勘误目前只取得题录和访问响应，未取得正文；不知其具体修改，不采用候选Bib中‘勘误不改公式’的无来源断言。原始Lange/Hamilton公式的核查与该未读勘误的内容分开。

本次为Agent自审，未记录人工审核事件。

## Grounded Evidence

本页的主要原件入口为 [[book-hamilton-electromagnetic-interaction]]、[[lange-kumar-hamilton-1982-multipole-admixtures]] 与 [[campaign-g07-gorgen-2004-163lu-quadrupole-moments]]。前述各推导保留具体页段与约定；Lange 勘误正文尚未取得，不以其元数据支持公式。Lu 的历史混合比是共享外部输入，非寿命论文逐态重测。

## Assumptions

轴对称取向张量的写法保留量子化轴和磁子态分布假设；混合比使用一致的发射约定及干涉系数。实际 DCO 与偏振响应还依赖探测几何、门选与校准。

## Competing Explanations

一个 DCO 比值可容许分离的混合比分支。不同理论偏好不能替代新的区分观测；偏振约束也须保留响应和共同事件引入的相关。

## Transfer Conditions

跨论文转换混合比符号时同时转换几何干涉项。只有对比同一跃迁、自旋序列与对应响应，才可将额外观测用于分支排序。

## Failure Conditions

遗漏未观测级联的去取向、把分母视为固定常数，或无视点源角分布与有限几何积分的区别，均可使反演失去所声明适用性。

## Falsification or Reverse Tests

对候选根回代原二次有理式，并检查分母非零、响应非负与极限；在完整约定变换后比较同一可观测量，不能只翻转混合比符号。

## Open Questions

未知装置的角响应与偏振灵敏度仍需其实际标定；本页不预测用户数据会保留哪一个根。

## Human Review

记录的是执行者、Terra 窄审及总控核验，没有新增用户审核事件。

## Promotion or Rejection History

2026-11-14：保留正文5.7已接受的条件修正；补齐知识页结构，来源和竞争分支仍按原件与显式约定判断。
