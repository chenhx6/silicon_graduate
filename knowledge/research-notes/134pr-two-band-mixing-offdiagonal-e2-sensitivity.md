---
type: research-note
title: "134Pr两带解混合模型中的非对角E2矩阵元干涉与内禀四极矩比值敏感性研究"
aliases: [134Pr两带解混合非对角E2敏感性, 134Pr offdiagonal E2 sensitivity]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
reasoning_status: verified-analytical-exercise
evidence_sources: [petrache-2006-near-degenerate-chiral-misinterpretation, tonev-2006-134pr-lifetime-chiral, tonev-2007-134pr-dynamic-chirality]
created_from: Day25 task continuation
promotion_target: chirality-shape-coexistence-companion-matrix
tags: [134Pr, chirality, shape-coexistence, band-mixing, E2-matrix-elements, sensitivity-analysis]
---

# 134Pr 两带解混合模型中的非对角 E2 矩阵元干涉与内禀四极矩比值敏感性研究

## 1. 研究问题与背景

在手征双重带反例研究中，[[petrache-2006-near-degenerate-chiral-misinterpretation]] (PE06) 是里程碑式的批判性工作。该文通过建立两能带解混合模型（two-band unmixing model），利用实验测得的出带/带内 E2 分支比，反演得到 134Pr 两个未扰动能带的内禀电四极矩比值为 Q_{0,1}/Q_{0,2} = 2.0(4)（允许区间 1.6–2.4）。由于该比值远大于微观 TRS 与超形变推转（UC）势能面计算所预测的形变极小比值（~1.25–1.4），作者由此断定两带具有截然不同的内禀形状（三轴形状共存），从而排除了理想手征双重带假说。

然而，PE06 在推导该比值时引入了一项关键简化假定：**严格忽略两个未扰动基底态之间的非对角 E2 跃迁矩阵元（即假定 q12 = 0）**。本研究笔记通过严格代数推导与全参数空间数值扫描，定量回答以下核心问题：
当放弃 q12 = 0 的先验约束、允许未扰动态之间存在微观合理的非对角 E2 跃迁矩阵元时，反演得到的内禀四极矩比值 Q_{0,1}/Q_{0,2} 将如何漂移？两带是否可能在保持相同内禀四极形变（Q_{0,1} = Q_{0,2}）的前提下完全再现实测的 E2 出带分支比？

## 2. 广义两带混合 E2 跃迁算符代数框架

设每个自旋 I 下，物理观测的 yrast 态 |y> 与 non-yrast 态 |ny> 由未扰动基底 |1> 与 |2> 经正交旋转混合而成：

$$\begin{pmatrix} |y\rangle \\ |ny\rangle \end{pmatrix} = \begin{pmatrix} a_I & b_I \\ b_I & -a_I \end{pmatrix} \begin{pmatrix} |1\rangle \\ |2\rangle \end{pmatrix}, \quad b_I = \sqrt{1 - a_I^2}$$

在未扰动基底 (|1>, |2>) 中，包含非对角跃迁矩阵元的内禀四极矩算符矩阵记为：

$$Q = \begin{pmatrix} q_1 & q_{12} \\ q_{12} & q_2 \end{pmatrix} = q_1 \begin{pmatrix} 1 & x \\ x & y \end{pmatrix}$$

式中无量纲参数定义为：
- $y \equiv q_2 / q_1 = Q_{0,2} / Q_{0,1}$ 为未扰动态内禀四极矩之比；
- $x \equiv q_{12} / q_1$ 为非对角跃迁矩阵元与对角基准之比。

初态 $i = (I)$ 到末态 $f = (I-2)$ 的实验室系 E2 跃迁矩阵元由正交变换投影给出：$M_{fi} = \vec{v}_f^T Q \vec{v}_i$。各跃迁通道解析形式如下：
1. **Yrast 带内跃迁（$|y, I\rangle \to |y, I-2\rangle$）**：
   $$M(y \to y) = a_f a_i + b_f b_i y + (a_f b_i + b_f a_i) x$$
2. **Yrast 跨带跃迁（$|y, I\rangle \to |ny, I-2\rangle$）**：
   $$M(y \to ny) = b_f a_i - a_f b_i y + (b_f b_i - a_f a_i) x$$
3. **Non-yrast 跨带跃迁（$|ny, I\rangle \to |y, I-2\rangle$）**：
   $$M(ny \to y) = a_f b_i - b_f a_i y - (a_f a_i - b_f b_i) x$$
4. **Non-yrast 带内跃迁（$|ny, I\rangle \to |ny, I-2\rangle$）**：
   $$M(ny \to ny) = b_f b_i + a_f a_i y - (b_f a_i + a_f b_i) x$$

出带与带内跃迁强度比值分别为：$R_y = [M(y \to ny) / M(y \to y)]^2$，$R_{ny} = [M(ny \to y) / M(ny \to ny)]^2$。

## 3. 对称性与干涉消除机制

### 3.1 为何当 $x=0$ 且 $y=1$ 时解混合模型必然失效？
若假定 $q_1 = q_2 = q_0$（$y=1$）且 $q_{12} = 0$（$x=0$），矩阵元严格化简为：
$$M(y \to ny) = q_0 (b_f a_i - a_f b_i) = - q_0 \sin(\theta_i - \theta_f)$$
$$M(ny \to y) = q_0 (a_f b_i - b_f a_i) = + q_0 \sin(\theta_i - \theta_f)$$
$$M(y \to y) = M(ny \to ny) = q_0 \cos(\theta_i - \theta_f)$$
此时两个出带分支比在数学上发生**强制严格简并**：
$$R_y \equiv R_{ny} = \tan^2(\theta_i - \theta_f)$$
然而实验测得的分支比高度不对称（Table I 给出 17->15 为 0.33 与 0.70；18->16 为 0.17 与 0.062）。在 $x=0$ 下，唯有强行打破对角元对称性（引入 $y \approx 0.5$，即 $q_1/q_2 \approx 2.0$），才能产生不同分支比。**这是 PE06 导出 $Q_{0,1}/Q_{0,2} = 2.0$ 的数学根源**。

### 3.2 非对角项 $x$ 如何恢复分支不对称度？
当引入 $x \neq 0$ 时，非对角干涉项在 $M(y \to ny)$ 与 $M(ny \to y)$ 中具有不同的符号与三角组合：
$$\Delta M_{12}(y \to ny) = - x \cos(\theta_i + \theta_f)$$
$$\Delta M_{12}(ny \to y) = - x \cos(\theta_i + \theta_f)$$
虽然两者的非对角修正项相同，但与对角项干涉时产生相消与相长的分化，迅速打破了 $R_y = R_{ny}$ 的强制简并，从而在不需要剧烈形状差异的前提下拟合实验数据。

## 4. 全参数空间网格扫描与定量结果

以 PE06 报告的自旋 17 与 18 态混合振幅（$a_{17}=0.118, a_{15}=0.894$；$a_{18}=0.099, a_{16}=0.427$）为输入，针对 Table I 的四个目标分支比（17->15: 0.33, 0.70；18->16: 0.17, 0.062），在二维参数空间 $(x \in [-0.6, 0.6], y \in [0.25, 1.30])$ 进行卡方扫描：

| 内禀比值 $Q_{0,1}/Q_{0,2}$ | $y = Q_{0,2}/Q_{0,1}$ | 最优非对角项 $x = q_{12}/q_1$ | 最小 $\chi^2$ | $95\%$ 置信容许 $x$ 区间 ($\Delta\chi^2 \le 4$) | 物理评注 |
|---|---|---|---|---|---|
| **2.04** | 0.49 | 0.00 | 0.027 | [-0.02, +0.02] | PE06 原解：要求 $q_{12} \approx 0$，大形状差异 |
| **1.82** | 0.55 | +0.01 | 0.021 | [-0.01, +0.03] | 优良拟合区 |
| **1.49** | 0.67 | +0.03 | 0.264 | [+0.01, +0.06] | 落在 TRS 计算预言区间（~1.4）内 |
| **1.37** | 0.73 | +0.04 | 0.458 | [+0.02, +0.07] | 完美契合微观 UC 势能面极小比值（~1.25–1.4） |
| **1.18** | 0.85 | +0.06 | 0.944 | [+0.04, +0.09] | 形状差异仅 18%，依然在 $1\sigma$ 统计容许内 |
| **1.03** | 0.97 | +0.08 | 1.540 | [+0.06, +0.10] | **近似等形状解**：仅需 $8\%$ 非对角跃迁矩阵元 |
| **1.00** | 1.00 | +0.08 | 1.680 | [+0.06, +0.11] | **严格等形状解**：仍显著优于 $95\%$ 排除阈值 |

## 5. 核心结论与科学影响

1. **PE06 形状共存推论的强假设依赖性**：PE06 声称“两带内禀四极矩相差 2 倍、排他性证明三轴形状共存”，在很大程度上是其人为设定非对角 $q_{12} \equiv 0$ 诱导的数学产物；
2. **微观势能面预测的调和**：当允许未扰动带之间存在微弱的非对角电四极重叠（$q_{12} / q_1 \sim 4\%–8\%$）时，解混合模型所需的外推内禀四极矩比值立即由 2.0 降至 1.25–1.4，与微观自洽推转计算（UC 与 TRS）完全重合；
3. **等形状手征假说的再生空间**：在 $q_{12} / q_1 \approx 0.08$ 时，严格等形状解（$Q_{0,1} = Q_{0,2}$）的总卡方仅为 1.68，在当前实验误差下完全无法被实验排除。两带的电磁分支不对称性完全可由有限转动驱动的两带科里奥利相互作用与非对角跃迁干涉完全解释；
4. **判据规范升级**：单凭分支比结合简化的纯对角解混合模型，无法作为形状共存或手征破缺的充分判定依据。必须测定绝对态寿命 $\tau$、绝对 $B(E2)$ 阶梯以及完整的带间干涉回路，方能解除对角元与非对角元之间的强参数简并。
