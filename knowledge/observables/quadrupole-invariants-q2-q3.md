---
type: observable
title: 四极形状不变量（q2, q3, cos 3gamma）
aliases: [quadrupole invariants, Kumar-Cline invariants, q2, q3, model-independent shape invariants]
created: 2026-11-06
updated: 2026-11-21
status: active
review_status: unreviewed
observable_kind: model-independent-shape-observable
symbol: q2, q3, cos(3\gamma)
units: q2: e^2*b^2, q3: e^3*b^3, cos(3\gamma): dimensionless
tags: [triaxiality, quadrupole-deformation, model-independent, shape-closure]
---

# 四极形状不变量（Quadrupole Invariants: $q_2, q_3, \cos 3\gamma$）

## Definition

Kumar–Cline 不变量是电四极张量 \(Q_{2\mu}\) 的转动标量矩。完整的实验 E2 矩阵元给出标量矩，结合几何约定可定义有效的电荷形状参数。

## How It Is Obtained

### 1. 二次不变量 $q_2$（四极总形变大小）

$$q_2(I)=\sqrt5\langle I|[Q_2\times Q_2]^{(0)}|I\rangle
=\frac{1}{2I+1}\sum_{\alpha',I'}|\langle \alpha'I'\|Q_2\|I\rangle|^2.$$

求和包括全部可达中间态以及允许的静态矩阵元。几何映射中 \(q_2\) 与 \(\langle\beta^2\rangle\) 成正比。

### 2. 三次不变量 $q_3$（三轴不对称度）

$$q_3(I)=-\sqrt{\frac{35}{2}}\langle I|\bigl[\,[Q_2\times Q_2]^{(2)}\times Q_2\,\bigr]^{(0)}|I\rangle.$$

这里采用轴向长形给正 \(q_3\) 的约定。展开时需要两次中间态求和和各三矩阵元乘积的相对符号。\(q_2\) 与 \(q_3\) 的这一归一见 [[henderson-2020-quadrupole-invariant-convergence]] 的原文核查。

## Diagnostic Use

### 3. 模型无关三轴不对称角 $\cos 3\gamma$
通过二次项与三次项的标度商，严格定义内禀有效三轴偏离角：
$$\cos 3\gamma_{\text{eff}} = \frac{q_3(I)}{[q_2(I)]^{3/2}}$$
- $\cos 3\gamma = +1 \implies \gamma = 0^\circ$（严格长椭球 Prolate）；
- $\cos 3\gamma = -1 \implies \gamma = 60^\circ$（严格扁椭球 Oblate）；
- $\cos 3\gamma = 0 \implies \gamma = 30^\circ$（最大三轴形变 Triaxial）。

## Model Dependence

### 基态 \(K_4\) 的双跃迁近似

Casten 二版 Eqs. (11.6)–(11.7)、(11.16)、(11.20) 区分全闭合的 \(K_4=q_4/q_2^2\) 与 IBA 给出的近似 \((7/10)B(E2;4_1^+\to2_1^+)/B(E2;2_1^+\to0_1^+)\)。即使 \(Q\) 作用于基态后主要产生 \(2_1^+\)，四次矩仍依赖 \(Q\) 再作用于 \(2_1^+\) 时的外连矩阵元。首支跃迁占 \(q_2\) 的份额可用于检查第一步截断，\(K_4\) 还要用相应外连路径或模型对照单独检验。书中的 \(^{152}\mathrm{Sm}\) 对照见 [[book-casten-nuclear-structure-simple-perspective]]，二版 PDF 466–468、印刷 pp.448–450。

[[werner-2000-ibm-quadrupole-invariants]] 的约 10% 为 ECQF 网格中双跃迁 \(K_4\) 的模型误差。[[werner-2005-k3-five-observables]] 的 \(7\%\) 和 \(8\%\) 则衡量有界分母下的三次近似差 \(|\,|K_3^{\rm appr}|-|K_3|\,|/(1+|K_3|)\)。五观测量公式另外使用 \(Q_s(2_1^+)\) 的符号和 \(Q\)-声子相位关系。[[werner-2006-shape-invariant-structural-evolution]] 为逐初态核查 \(q_2\) 截断的例子。更一般的闭合与误差条件见 [[henderson-2020-quadrupole-invariant-convergence]]。

## Failure Modes and Ambiguities

### 中间态通道截断

在近期关于 A~130 区域奇 Ba 同位素链（$^{129\text{--}137}\text{Ba}$）的四极闭合深入研究中发现了一个关键物理陷阱：
1. **受限自旋通道伪相消**：如果仅截断计算单个特定自旋通道（例如由基态 $11/2^-$ 经由单极 $E2$ 激发的全组 $15/2^-$ 态），虽然该受限通道在理论强度上贡献了 $99.5\%$ 以上的分支，但仅贡献了完整 $q_2$ 不变量的 $20\% \sim 28\%$；
2. **有效角的越域与相消**：在受限子通道中，由于干涉交叉相消，受限 $z_{\text{channel}} = q_3 / q_2^{3/2}$ 经常出现 $> 1.0$ 的非物理越域；只有完整求和包含全自旋通道（$I' = 7/2, 9/2, 11/2, 13/2, 15/2$）后，电荷形状不变量才恢复物理自洽。
这一发现确立了在低能核结构中使用不变量时，**严禁使用单通道替代完整电荷几何闭合**的铁律。

## Sources

- [[kumar-1972-quadrupole-shapes-original-metadata]]
- [[cline-1986-nuclear-shapes-coulomb-excitation]]
- [[henderson-2020-quadrupole-invariant-convergence]]
- [[quadrupole-invariant-spin-channel-precedents]]
