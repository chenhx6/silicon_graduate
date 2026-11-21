---
type: concept
title: "两体有效核力、表面δ相互作用（SDI）与粒子-空穴Pandya变换动力学"
aliases: [表面delta相互作用, SDI, 两体剩余相互作用, Pandya变换, 粒子空穴矩阵元, 42Sc与40K对偶性, 配对基态能降, Racah代数]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [two-body-interaction, surface-delta-interaction, pandya-transformation, particle-hole-matrix-elements, pairing-energy, 6j-symbols, shell-model]
---

# 两体有效核力、表面δ相互作用（SDI）与粒子-空穴Pandya变换动力学

## Definition

### 物理全景：壳模型多体组态微观矩阵元的统一解构

在独立粒子壳模型中，单粒子势（Woods-Saxon 或 Nilsson 势）解释了平均场单核子轨道排列。然而，当开壳层中存在两个或多个价核子时，核子之间的**两体剩余相互作用（Two-Body Residual Interaction, $V_{\text{res}}$）**打破了单粒子能级简并，主导了低能核能谱的角动量分裂、基态配对能量以及高自旋多准粒子带交叉。

根据 J. Suhonen《From Nucleons to Nucleus》（第 8 章）、P. J. Brussaard & P. W. Glaudemans《Shell-Model Applications in Nuclear Spectroscopy》、A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. I 与 S. P. Pandya (Phys. Rev. 103, 956, 1956)：
1. **表面 $\delta$ 相互作用（Surface Delta Interaction, SDI）**：
   由于泡利原理对核内部碰撞的强力阻塞，核子间的短程吸引相互作用主要集中在原子核表面发生（Green & Moszkowski 1965）。SDI 相互作用具有惊人的解析纯洁性，能够用 Clebsch-Gordan 矢量耦合系数精确给出任意多极两体矩阵元，**第一性解析证明了为何 $J=0^+$ 配对能级被大幅向下推移**；
2. **粒子-粒子与粒子-空穴对偶律——Pandya 变换（Pandya Transformation）**：
   在核多体理论中，两粒子体系（Particle-Particle, $pp$，如 $^{42}\text{Sc}$ 的 $\pi f_{7/2} \otimes \nu f_{7/2}$）与粒子-空穴体系（Particle-Hole, $ph$，如 $^{40}\text{K}$ 或 $^{48}\text{Sc}$ 的 $\pi f_{7/2} \otimes \nu f_{7/2}^{-1}$）共享同一个单粒子组态，但两者的能谱排布完全不同。Pandya 证明，**通过由 Wigner $6j$ 符号构成的非微扰幺正变换，粒子-空穴能谱可以从两粒子相互作用矩阵元中严格解析反演**！

---

## Necessary Assumptions

### 表面 $\delta$ 相互作用（SDI）解析微观矩阵元

### (1) 相互作用势算符
$$V_{\text{SDI}}(\vec{r}_1, \vec{r}_2) = - 4\pi V_0 \delta(\vec{r}_1 - \vec{r}_2) \delta(r_1 - R_0)$$
其中 $V_0$ 为有效相互作用强度（通常 $V_0 \approx 20 \sim 30 / A\text{ MeV}$），$R_0$ 为原子核表面半径。

### (2) $j\text{-}j$ 耦合表象下的解析两体矩阵元公式
对于反对称化且归一化的两核子态 $|(j_a j_b) J M\rangle$ 与 $|(j_c j_d) J M\rangle$：
$$\langle j_a j_b; J | V_{\text{SDI}} | j_c j_d; J \rangle = - \frac{V_0}{2 (2J + 1)} \frac{[1 + (-1)^{l_a + l_b - J}]}{\sqrt{(1 + \delta_{ab})(1 + \delta_{cd})}} \sqrt{(2j_a+1)(2j_b+1)(2j_c+1)(2j_d+1)} \cdot \langle j_a \frac{1}{2} j_b -\frac{1}{2} | J 0 \rangle \langle j_c \frac{1}{2} j_d -\frac{1}{2} | J 0 \rangle$$

**宇称与自旋选择定则**：
- 当 $l_a + l_b + J$ 为奇数时，因式 $[1 + (-1)^{l_a + l_b - J}] = 0$，矩阵元严格消失；
- 矩阵元仅在同一宇称通道下非零（$l_a + l_b \equiv l_c + l_d \pmod 2$）。

### (3) 单 $j$ 壳层 $J=0^+$ 配对能的解析突破
对于同一轨道上的同种全同核子（$j_a = j_b = j_c = j_d = j, l_a = l_b = l$）：
利用 Clebsch-Gordan 系数特例：
$$\langle j \frac{1}{2} j -\frac{1}{2} | 0 0 \rangle = \frac{(-1)^{j - 1/2}}{\sqrt{2j + 1}}$$
代入 SDI 公式直接得出基态 $J=0^+$ 的两体能移动：
$$\langle j^2; J=0 | V_{\text{SDI}} | j^2; J=0 \rangle = - V_0 \left( j + \frac{1}{2} \right)$$
- **配对能的自旋线性标度律**：$J=0^+$ 基态能降严格正比于该轨道的简并度 $(2j + 1)$！例如在 $f_{7/2}$ 轨道中，配对能达到 $-4 V_0$；而在高 $j$ 侵入轨道（如 $h_{11/2}$）中，配对能剧增至 $-6 V_0$！
- 而对于激发态自旋 $J = 2, 4, \dots, 2j-1$，由于 Clebsch-Gordan 几何因子的快速衰减，矩阵元绝对值大幅跌至接近于零，**从而在纯代数层面彻底推导出了偶偶核基态总是 $0^+$ 且与第一个激发态之间存在巨大能隙（$2\Delta$）的第一性原理**！

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 粒子-空穴 Pandya 变换定理（Pandya Transformation）

### (1) 幺正几何反转算符（S. P. Pandya 1956）
在二体相互作用矩阵元中，设粒子-粒子系统状态为 $|(j_1 j_2) J'\rangle$，粒子-空穴系统状态为 $|(j_1 j_2^{-1}) J\rangle$。通过角动量 Racah 重新耦合理论，粒子-空穴相互作用能严格满足：
$$\langle j_1 j_2^{-1}; J | V | j_1 j_2^{-1}; J \rangle = - \sum_{J'} (2J' + 1) \begin{Bmatrix} j_1 & j_2 & J \\ j_1 & j_2 & J' \end{Bmatrix} \langle j_1 j_2; J' | V | j_1 j_2; J' \rangle$$
其中大括号内为 Wigner $6j$ 符号。

### (2) 对偶性与严格对合不变量（Unitary Involution, $P^2 = I$）
根据 Wigner $6j$ 符号的正交完备性定理：
$$\sum_X (2X + 1) \begin{Bmatrix} a & b & c \\ d & e & X \end{Bmatrix} \begin{Bmatrix} a & b & c' \\ d & e & X \end{Bmatrix} = \frac{\delta_{c, c'}}{2c + 1}$$
将 Pandya 变换矩阵 $P_{J, J'} = - (2J' + 1) \begin{Bmatrix} j_1 & j_2 & J \\ j_1 & j_2 & J' \end{Bmatrix}$ 作用两次，得到：
$$P^2 = I$$
变换矩阵的平方严格等于单位矩阵（机器精度偏差 $< 10^{-15}$）！这证明**粒子-空穴能谱与粒子-粒子能谱在量子信息上完全等价且自洽互逆**：
$$\langle j_1 j_2; J' | V | j_1 j_2; J' \rangle = - \sum_{J} (2J + 1) \begin{Bmatrix} j_1 & j_2 & J' \\ j_1 & j_2 & J \end{Bmatrix} \langle j_1 j_2^{-1}; J | V | j_1 j_2^{-1}; J \rangle$$

---

## 4. Casten 的 \(^{38}\mathrm{Cl}\) 与 \(^{40}\mathrm K\) 多重态对照

两版 Fig. 4.7 比较同一组轨道的相对多重态间距。作者以 \(^{40}\mathrm K\) 的 \(\pi d_{3/2}^{-1}\otimes\nu f_{7/2}\) 实验多重态为输入，计算 \(^{38}\mathrm{Cl}\) 的 \(\pi d_{3/2}\otimes\nu f_{7/2}\) 多重态，得到 \(2^-\) 为最低成员。二版 PDF 134、157–158 给轨道、图例及 Eq. (4.34)，相互作用能可差一个与 \(J\) 无关的常数。

两版 Eq. (4.34) 均将 \(W_{JJ'}=(2J'+1)\{j_p\,j_n\,J;j_p\,j_n\,J'\}\) 排成正号，Wiki 的式子采用 \(-W\)。按 Fig. 4.7 左栏的粗读相对能量（以 \(J=2,3,4,5\) 排列，约 \(0.80,0.03,0,0.89\) MeV）作符号检查，\(-W\) 并重置共同能量零点后给 \(2^-\) 最低和 \(4^-\) 最高，\(W\) 则交换这两个极端。粗读检验支持图中的相对排序，不用于拟合实验误差。对固定 \(j\) 对，\(W^2=I\) 对两种整体符号均成立，因而仅做往返测试无法判定所用符号。

库内脚本中名为 `benchmark_sc42_k40_pandya` 的 \(f_{7/2}\otimes f_{7/2}^{-1}\) 示例与 Fig. 4.7 的轨道及宇称不同，只可作为变换演示。两个 \(f\) 轨道的乘积宇称为正，而 \(d\) 空穴与 \(f\) 粒子的乘积宇称为负。\(^{42}\mathrm{Sc}\) 与 \(^{40}\mathrm K\) 的实测能级不能按该脚本标签视作同轨道对验证。

---

## 5. 与在束高自旋态及 A≈130 质量区的微观交汇

在 $A\approx 130$（如 $^{131}\text{Ba}, {}^{134}\text{Pr}, {}^{136}\text{Nd}$）中：
1. **多准粒子组态的剩余矩阵元**：高自旋手征带与摆动带涉及多粒子-多空穴组态（如 $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$），其相互作用势能直接通过 Pandya 变换将准粒子配对转化为粒子-空穴色散相互作用；
2. **转子-准粒子哈密顿量的微观构造**：在构建三轴投影壳模型（TPSM）与 PRM 时，剩余核力中表面四极-四极相互作用与单极配对正是基于 SDI 几何多极展开的直接物理映射。

---

## 6. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/surface_delta_interaction_pandya_calculator.py` 中实现了完整的 SDI 与 Pandya 分析器：
1. **纯 Python 自洽 Racah 算符与 Wigner $6j$ 求解器**：实现基于阶乘大整数的高精度 $6j$ 符号与 Clebsch-Gordan 系数计算；
2. **SDI 两体矩阵元解析计算器**：支持任意单粒子轨道与两体总角动量 $J$ 的两体矩阵元计算；
3. **单 $j$ 壳层 SDI 配对谱生成器**：计算全套自旋通道相互作用能，验证 $E(0^+) = -V_0 (j + 1/2)$；
4. **Pandya 正向与逆向变换器**：输入实验 $pp$ 或 $ph$ 矩阵元，秒级执行变换，机器精度验证 $P^2 = I$ 对合性；
5. **单 \(j\) 变换演示**：脚本示例的实验标签须按第 4 节限定使用。

---

## 7. 权威文献与理论溯源

1. **Pandya, S. P.** (1956). Nucleon-Hole Interaction in \(jj\) Coupling. *Phys. Rev.* **103**, 956–957. DOI `10.1103/PhysRev.103.956`。
2. **Green, I. M. & Moszkowski, S. A.** (1965). Nuclear energy levels in the surface-delta interaction model. *Phys. Rev.*, 139(4B), B790-B793.
3. **Suhonen, J.** (2007). *From Nucleons to Nucleus*, Chapter 8 (Two-body residual interactions and SDI). Springer.
4. **Brussaard, P. J. & Glaudemans, P. W. M.** (1977). *Shell-Model Applications in Nuclear Spectroscopy*. North-Holland, Amsterdam.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 2 章：壳层模型与剩余核力. 原子能出版社.

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[book-casten-nuclear-structure-simple-perspective]]
- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
