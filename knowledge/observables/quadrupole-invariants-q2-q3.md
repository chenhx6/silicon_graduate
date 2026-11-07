---
type: observable
title: 四极形状不变量（q2, q3, cos 3gamma）
aliases: [quadrupole invariants, Kumahora-Sugawara invariants, q2, q3, model-independent shape invariants]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
observable_kind: model-independent-shape-observable
symbol: q2, q3, cos(3\gamma)
units: q2: e^2*b^2, q3: e^3*b^3, cos(3\gamma): dimensionless
tags: [triaxiality, quadrupole-deformation, model-independent, shape-closure]
---

# 四极形状不变量（Quadrupole Invariants: $q_2, q_3, \cos 3\gamma$）

## Definition

由 Kumar、Cline、Kumahora 与 Sugawara 等人基于转动不变量代数发展的**模型无关核四极形状标定体系**。该体系通过对任意核态 $|\Psi\rangle$ 计算电四极张量算符 $Q_{2\mu} = \sum_i e_i r_i^2 Y_{2\mu}(\theta_i, \phi_i)$ 的零阶标量收缩算符（标量积），从纯粹实验跃迁几率与静态矩中直接反演原子核内禀电荷分布的内禀形变度 $q_2$（对应 $\beta_2^2$）和不对称度 $q_3$（对应 $\beta_2^3 \cos 3\gamma$），无需预先假定任何转子或平均场模型。

## Tensor Formalism and Intermediate State Summation

### 1. 二次不变量 $q_2$（四极总形变大小）
$$q_2(I) = \langle I | [Q_2 \times Q_2]^{(0)} | I \rangle = \frac{1}{\sqrt{2I+1}} \sum_{I'} (-1)^{I - I'} \langle I || Q_2 || I' \rangle \langle I' || Q_2 || I \rangle W(2 2 I I; 0 I')$$
经 Racah 6j 符号化简后，严格表达为全部可达中间态 $I'$ 的约化矩阵元模方求和：
$$q_2(I) = \frac{1}{2I+1} \sum_{I'} |\langle I || Q_2 || I' \rangle|^2$$
它定量表征基态或特定激发态所感受到的全空间总四极形变有效均方根：$q_2 \propto \beta_2^2$。

### 2. 三次不变量 $q_3$（三轴不对称度）
$$q_3(I) = -\sqrt{\frac{7}{10}} \langle I | [[Q_2 \times Q_2]^{(2)} \times Q_2]^{(0)} | I \rangle = \frac{\sqrt{35}}{10} \frac{1}{2I+1} \sum_{I' I''} \langle I || Q_2 || I' \rangle \langle I' || Q_2 || I'' \rangle \langle I'' || Q_2 || I \rangle W(2 2 I I''; 2 I')$$

### 3. 模型无关三轴不对称角 $\cos 3\gamma$
通过二次项与三次项的标度商，严格定义内禀有效三轴偏离角：
$$\cos 3\gamma_{\text{eff}} = \frac{q_3(I)}{[q_2(I)]^{3/2}}$$
- $\cos 3\gamma = +1 \implies \gamma = 0^\circ$（严格长椭球 Prolate）；
- $\cos 3\gamma = -1 \implies \gamma = 60^\circ$（严格扁椭球 Oblate）；
- $\cos 3\gamma = 0 \implies \gamma = 30^\circ$（最大三轴形变 Triaxial）。

## Channel-Restricted Warning: The Spin-Channel Redistribution Trap

在近期关于 A~130 区域奇 Ba 同位素链（$^{129\text{--}137}\text{Ba}$）的四极闭合深入研究中发现了一个关键物理陷阱：
1. **受限自旋通道伪相消**：如果仅截断计算单个特定自旋通道（例如由基态 $11/2^-$ 经由单极 $E2$ 激发的全组 $15/2^-$ 态），虽然该受限通道在理论强度上贡献了 $99.5\%$ 以上的分支，但仅贡献了完整 $q_2$ 不变量的 $20\% \sim 28\%$；
2. **有效角的越域与相消**：在受限子通道中，由于干涉交叉相消，受限 $z_{\text{channel}} = q_3 / q_2^{3/2}$ 经常出现 $> 1.0$ 的非物理越域；只有完整求和包含全自旋通道（$I' = 7/2, 9/2, 11/2, 13/2, 15/2$）后，电荷形状不变量才恢复物理自洽。
这一发现确立了在低能核结构中使用不变量时，**严禁使用单通道替代完整电荷几何闭合**的铁律。
