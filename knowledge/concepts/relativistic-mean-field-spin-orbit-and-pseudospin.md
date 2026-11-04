---
type: concept
title: "相对论平均场（RMF）、协变自旋-轨道耦合与狄拉克赝自旋对称性（PSS）动力学"
aliases: [相对论平均场, RMF, 协变密度泛函, CDFT, 自旋轨道耦合起源, 赝自旋对称性, PSS, Ginocchio条件, 赝自旋手征四重带]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [relativistic-mean-field, covariant-density-functional, spin-orbit-coupling, pseudospin-symmetry, ginocchio-condition, dirac-equation, chiral-quartet]
---

# 相对论平均场（RMF）、协变自旋-轨道耦合与狄拉克赝自旋对称性（PSS）动力学

## Definition

### 物理全景：微观自旋-轨道力的自然起源与相对论协变结构

在非相对论量子核物理中，为了解释原子核幻数（28, 50, 82, 126），Mayer 与 Jensen（1949 年诺贝尔奖成果）必须在单粒子哈密顿量中人为引入唯象的强自旋-轨道相互作用势 $V_{SO}(r) \vec{l} \cdot \vec{s}$，其起源在非相对论框架下长期无法自洽推导。

而在基于量子强动理学介子场论的**相对论平均场理论（Relativistic Mean Field, RMF / 协变密度泛函 CDFT，Serot & Walecka 1986, Ring 1996, Meng 2006, 2016）**中：
1. **巨大标量势与矢量势的反号对消**：
   核子通过交换同位旋标量 $\sigma$ 介子感受到巨大的吸引标量势（$S(r) \approx -400\text{ MeV}$），同时通过交换同位旋矢量 $\omega$ 介子感受到巨大的排斥矢量势（$V(r) \approx +350\text{ MeV}$）；
2. **中心势与自旋-轨道势的绝妙重组**：
   - 束缚整个原子核的中心平均势是两者的微弱代数差：
     $$V_{\text{cent}}(r) = V(r) + S(r) \approx -50\text{ MeV}$$
   - 而从四分量狄拉克方程作非相对论 Pauli 二分量展开时，**自旋-轨道耦合势天然由两者的代数和决定**：
     $$V_{SO}(r) = \frac{1}{2 M^2} \frac{1}{r} \frac{d}{dr} \left[ V(r) - S(r) \right] \vec{l} \cdot \vec{s} \approx \frac{1}{2 M^2} \frac{1}{r} \frac{d}{dr} \left( 750\text{ MeV} \right) \vec{l} \cdot \vec{s}$$
     由于 $V - S \approx 750\text{ MeV}$ 具有极其陡峭的空间梯度，**核物理中巨大的强自旋-轨道劈裂在相对论狄拉克方程中自然涌现，无需引入任何人为唯象参数**！

---

## Necessary Assumptions

### 狄拉克赝自旋对称性（Pseudospin Symmetry, PSS）物理机制

### (1) 赝自旋能级简并之谜（Arima 1969, Hecht & Adler 1969）
1969 年，实验核物理学家在单粒子能级谱中发现了一个惊人的系统学规律：
单粒子态 $(n, l, j = l + 1/2)$ 与态 $(n-1, l+2, j = l+3/2)$ 具有近乎相同的单粒子能量（例如 $(2s_{1/2}, 1d_{3/2})$、$(2p_{3/2}, 1f_{5/2})$ 与 $(2d_{5/2}, 1g_{7/2})$）。
通过定义**赝轨道角动量（Pseudo-orbital angular momentum）**：
$$\tilde{l} = l + 1$$
与**赝自旋（Pseudospin）** $\tilde{s} = 1/2$，这两个单粒子态恰好构成以 $j = \tilde{l} \pm 1/2$ 为总角动量的**赝自旋双重态（Pseudospin Doublet）**，其能量近乎完全简并！

### (2) 相对论微观对称性确立（J. N. Ginocchio 1997, Meng et al. 1998）
这一长达近三十年的经验简并之谜，在 1997 年由 Ginocchio 通过狄拉克方程在相对论协变对称性层面彻底揭秘：
在球对称狄拉克方程中：
$$\begin{pmatrix} M + S(r) + V(r) & -\frac{d}{dr} + \frac{\kappa}{r} \\ \frac{d}{dr} + \frac{\kappa}{r} & -M - S(r) + V(r) \end{pmatrix} \begin{pmatrix} G(r) \\ F(r) \end{pmatrix} = E \begin{pmatrix} G(r) \\ F(r) \end{pmatrix}$$
其中狄拉克量子数 $\kappa = -(j + 1/2)$ 当 $j = l + 1/2$，而 $\kappa = +(j + 1/2)$ 当 $j = l - 1/2$。
通过对**狄拉克小分量波函数 $F(r)$** 作变换，Ginocchio 证明：
**当且仅当标量势与矢量势之和为常数或空间梯度为零时，狄拉克哈密顿量具备严格的 $SU(2)$ 赝自旋空间代数对称性**：
$$\frac{d}{dr} [V(r) + S(r)] = 0 \quad \text{或} \quad V(r) + S(r) = C$$
孟杰（J. Meng et al., PRL 82, 3819, 1999; PRL 91, 262501, 2003）进一步证明：由于原子核束缚势阱深度 $V + S \approx -50\text{ MeV}$ 远小于核子静止质量 $M \approx 938\text{ MeV}$，势能和在核内部极其平缓（$d(V+S)/dr \approx 0$），因而在真实有限核中，赝自旋对称性保持着极高精度的近似微观守恒！

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 赝自旋对称性破缺、壳演化与滴线反转

1. **势垒边界破缺（Surface Breaking）**：
   在原子核表面，$V(r)$ 与 $S(r)$ 逐渐趋于零，使得 $d(V+S)/dr$ 在核表层不可避免地出现非零峰值，导致真实单粒子态产生数百 keV 的细微赝自旋劈裂（$\\Delta E_{\text{PSS}} = E(\tilde{l} - 1/2) - E(\tilde{l} + 1/2) \sim 200 \sim 500\text{ keV}$）；
2. **滴线区空间弥散与赝自旋恢复**：
   在中子滴线区，由于核表面极度弥散（中子晕或中子皮），势能梯度 $d(V+S)/dr$ 较稳定核大幅减小，**理论预言在弱束缚滴线核区，赝自旋对称性将发生显著的恢复，能级简并度反而大幅提高**；
3. **形变核中的渐近量子数**：
   在轴对称变形势阱中，Nilsson 轨道表示为 $[N, n_z, \Lambda] \Omega$。赝自旋双重态对应渐近量子数 $[\tilde{N} = N-1, \tilde{n}_z = n_z, \tilde{\Lambda} = \Lambda \pm 1] \Omega$，在形变 Nilsson 能级演化图中平行为伴。

---

## 4. 实验前沿交汇：手征-赝自旋四重带（Pseudospin-Chiral Quartets）

在 $A\approx 130$ 质量区的奇核（如 $^{131}\text{Ba}$，Guo et al. 2020 PRL）：
1. **四重态几何起源**：
   价质子占据微观赝自旋双重轨道（如 $\pi [411]1/2$ 与 $\pi [413]3/2$，或 $\pi (2d_{5/2}, 1g_{7/2})$ 轨道组合），与高 $j$ 侵入轨道（$\pi h_{11/2}, \nu h_{11/2}$）同时耦合。
2. **两重离散对称性的双重破缺**：
   - 手征对称性破缺产生手征双重带（Chiral Doublets，具有左右手空间标架翻转不变性）；
   - 赝自旋自由度产生能量相近的伴随态；
   - 两者协同作用，在同一核素中衍生出四条具有相同正宇称、能级高度近简并的**手征-赝自旋四重带（Pseudospin-Chiral Quartet Bands，D3, D4, D5, D6）**，构成了目前低能核结构领域最复杂的非阿贝尔离散对称性微观物理形态！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/rmf_spin_orbit_pseudospin_calculator.py` 中实现了完整的相对论平均场与赝自旋分析器：
1. **相对论自旋-轨道势发生器**：从标量势 $S(r)$ 与矢量势 $V(r)$ 计算中心势 $V + S$ 与自旋-轨道势 $V_{SO}(r)$；
2. **单粒子自旋-轨道劈裂求解器**：计算轨道对（如 $1p_{1/2} - 1p_{3/2}$、$1d_{3/2} - 1d_{5/2}$）由 $V - S$ 梯度产生的理论能隙；
3. **狄拉克赝自旋微扰积分器**：对 Ginocchio 条件偏离度 $\frac{d}{dr}[V(r) + S(r)]$ 执行小分量微观积分，反演赝自旋双重态劈裂 $\Delta E_{\text{PSS}}$；
4. **手征-赝自旋四重带（Quartet）能级谱学检验器**：输入四带实验能谱，检验能量离散度、自旋交叉特征与赝自旋对称性判据。

---

## 6. 权威文献与理论溯源

1. **Serot, B. D. & Walecka, J. D.** (1986). The relativistic nuclear many-body problem. *Adv. Nucl. Phys.*, 16, 1-327.
2. **Ring, P.** (1996). Relativistic mean field theory in finite nuclei. *Prog. Part. Nucl. Phys.*, 37, 193-263.
3. **Ginocchio, J. N.** (1997). Pseudospin symmetry as a relativistic symmetry. *Phys. Rev. Lett.*, 78(3), 436-439.
4. **Meng, J., Sugawara-Tanabe, K., Yamaji, S., Ring, P., & Arima, A.** (1998). Pseudospin symmetry in relativistic mean field theory. *Phys. Rev. C*, 58(2), R628-R631.
5. **Meng, J., Sugawara-Tanabe, K., Yamaji, S., & Arima, A.** (1999). Pseudospin symmetry in acidic nuclei. *Phys. Rev. Lett.*, 82(19), 3819-3822.
6. **Liang, H., Shen, S., Zhao, P., & Meng, J.** (2015). Hidden symmetries in relativistic nuclear physics: Pseudospin and spin symmetries. *Phys. Rep.*, 570, 1-84.
7. **Guo, S. et al.** (2020). Evidence for pseudospin-chiral quartet bands in $^{131}\text{Ba}$. *Phys. Rev. Lett.*, 124(19), 192501.

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
