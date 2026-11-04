---
type: concept
title: "原子核高自旋能带光滑终止（Band Termination）、CNS微观动力学与价角动量耗尽法典"
aliases: [能带终止, 能带光滑终止, Band Termination, 旋转Nilsson-Strutinsky, CNS模型, 过渡四极矩塌缩, 价角动量耗尽]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [band-termination, cranked-nilsson-strutinsky, high-spin-physics, transition-quadrupole-moment, dynamic-moment-of-inertia, valence-space, dsma]
---

# 原子核高自旋能带光滑终止（Band Termination）、CNS微观动力学与价角动量耗尽法典

## Definition

### 物理全景：从集体转动到单粒子非集体激发的连续相变

在变形原子核的高自旋前沿，一个最引人入胜的量子多体现象是**能带光滑终止（Smooth Band Termination）**：一个在低自旋下展现出高度集体转动特性（强 $B(E2)$ 跃迁、规则的转动能谱）的转动带，随着自旋增加并不发生不连续的裂片或带交叉，而是**光滑演化直至价核子角动量全部沿转轴对齐，最终终结于一个纯粹的非集体单粒子激发态**！

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II、T. Bengtsson & I. Ragnarsson (Nucl. Phys. A 436, 14, 1985)、A. V. Afanasjev et al. (Phys. Rep. 322, 1, 1999) 与 S. Frauendorf (Rev. Mod. Phys. 73, 463, 2001)：
1. **微观角动量耗尽机制（Valence Angular Momentum Exhaustion）**：
   在某一固定价核子组态（如费米面外占据特定侵入轨道 $h_{11/2}, i_{13/2}$）下，闭壳核芯在低自旋下被视为无转动态（球形惯性背景）。转动带的总角动量 $I$ 最初由核芯集体转动与准粒子微弱对齐提供；随着转动角速度 $\omega$ 增加，Coriolis 力驱动每一个价核子在变形势阱中逐步克服配对关联，向转轴方向单粒子对齐。当所有价核子的内禀角动量在转轴上的投影均达到其泡利极限量（$m_j = j, j-1, \dots$）时，**该价核子空间在几何与代数上再也无法提供额外的转动角动量，能带发生不可逆的物理终止**！
2. **三轴几何形变连续演化轨迹**：
   在 $(\varepsilon_2, \gamma)$ 伦德奎斯特（Lundqvist）平面上：
   - 低自旋：体系处于绕垂直于对称轴转动的轴对称长椭集体转动（Prolate Collective, $\gamma = 0^\circ$）；
   - 中自旋：核子对齐打破轴对称性，驱动核进入显著的三轴形变过渡态（Triaxial, $0^\circ < \gamma < 60^\circ$）；
   - 终止态：当所有核子完全对齐于对称轴（此时对称轴成为转轴），体系演变为绕对称轴旋转的**非集体扁椭态（Oblate Non-collective, $\gamma = 60^\circ$）**！

---

## Necessary Assumptions

### 旋转 Nilsson-Strutinsky（CNS）微观形式理论

旋转 Nilsson-Strutinsky（Cranked Nilsson-Strutinsky, CNS）模型是在高自旋下完全消除经验配对力的人工假象、严格按单粒子轨道追踪构型的第一性自洽平均场模型：
1. **单粒子 Routhian 哈密顿量**：
   $$h^\omega = h_{\text{sp}}(\varepsilon_2, \gamma, \varepsilon_4) - \hbar\omega j_x$$
2. **总能量与角动量求和**：
   对于指定的质子与中子轨道占据构型 $\pi [p_1, p_2] \otimes \nu [n_1, n_2]$：
   $$E_{\text{tot}}(I) = E_{\text{macro}}(\varepsilon, \gamma) + \sum_{i \in \text{occ}} \varepsilon_i^\omega + \hbar\omega I_x - \tilde{E}_{\text{Strut}}$$
   其中总转动惯量与转轴角动量为所有占据单粒子态的期待值代数和：
   $$I_x = \sum_{i=1}^A \langle j_x \rangle_i$$
3. **终止态自旋最大值闭合定理**：
   对于一组指定的主壳层价核子，其理论终止自旋由单粒子磁量子数 $m_i$ 在泡利不相容原理下的代数最大值严格决定：
   $$I_{\text{term}} = \sum_{k=1}^{Z_{\text{val}}} m_j^{(k)}(\text{proton}) + \sum_{m=1}^{N_{\text{val}}} m_j^{(m)}(\text{neutron})$$

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 实验确证能带终止的三大物理判据

在实验数据分析中，严禁仅凭“能级断裂看不到了”或“回弯（Backbending）”断言为能带终止！确立能带终止必须经过以下三项刚性检验：

### (1) 过渡四极矩 $Q_t \to 0$ 塌缩判据（核心金标准！）
根据三轴转子的电四极辐射几何定理，带内跃迁的过渡四极矩 $Q_t$ 随非对称角 $\gamma$ 剧烈变化：
$$Q_t(I) = Q_0 \frac{\cos(\gamma(I) + 30^\circ)}{\cos 30^\circ}$$
- 在低自旋（$\gamma = 0^\circ$）：$Q_t = Q_0$（具有极强的集体 $E2$ 辐射）；
- 在能带终止态（$\gamma = 60^\circ$）：$\cos(60^\circ + 30^\circ) = \cos 90^\circ \equiv 0$！**过渡四极矩 $Q_t$ 发生灾变性塌缩，严格归零**！
- **经典实验实证**：在 $^{109}\text{Sb}$（Afanasjev 1999, Wadsworth 1998）中，通过高精度 DSAM 多普勒线形分析，实测证明 $Q_t$ 从 $29/2^+$ 态的 $2.85 \pm 0.25\ e\text{b}$ 经 5 个跃迁平滑暴跌至 $49/2^+$ 态的 $\le 0.35\ e\text{b}$（跌落幅度达 $88\%$），直接证实了集体性的消亡！

### (2) 动力学转动惯量 $\mathcal{J}^{(2)}$ 的陡峭骤降
动力学转动惯量反映了转动动能对自旋的二阶响应：
$$\mathcal{J}^{(2)} = \frac{4}{\Delta E_\gamma} = \frac{4}{E_\gamma(I+2) - E_\gamma(I)}$$
随着能带向终止态靠拢，能级间距 $\Delta E_\gamma$ 急剧拉宽（离心能惩罚），导致 $\mathcal{J}^{(2)}$ 呈现特征性的**陡峭俯冲式暴跌**，甚至跌入负值区域，与常规刚体转动的平坦惯量截然相反。

### (3) 刚体转动参考能量减除曲面（$E - E_{\text{RR}}$）的特征深尖点（Cusp）
定义减除刚体转子参考能量后的过剩能量：
$$E_{\text{diff}}(I) = E(I) - \frac{\hbar^2}{2\mathcal{J}_{\text{RR}}} I(I+1), \quad \frac{\hbar^2}{2\mathcal{J}_{\text{RR}}} \approx 0.015 A^{-5/3}\text{ MeV}$$
在 $E - E_{\text{RR}}$ 随自旋 $I$ 的演化曲线上：
- 能带终止态对应极深、极陡峭的**局部能量极小值尖谷（Sharp Cusp）**；
- 若要在终止态自旋之上继续增加自旋，体系必须强行激发跨闭壳核芯粒子（产生新的高能粒子-空穴激发），能量线图立刻向上剧烈反弹，产生极大的能量跃升惩罚！

---

## 4. 与 $A\approx 130$ 质量区的谱学交汇

在 $A\approx 130$ 质量区（如 $^{131}\text{Ce}, {}^{132}\text{Ce}, {}^{135}\text{Nd}$）中：
1. **价核子组态**：质子填充 $\pi h_{11/2}, g_{7/2}, d_{5/2}$，中子占据负宇称 $\nu h_{11/2}$ 与正宇称 $s_{1/2}, d_{3/2}$；
2. **三轴驱动源**：当质子对向转轴完全对齐、中子对也相继耗尽内部自旋时，体系由 $\gamma \approx 20^\circ$ 的中等三轴形变被强制牵引向 $\gamma = 60^\circ$ 的非集体扁椭终止态；
3. **摆动带与手征带的天然边界**：三轴手征双重带与摆动运动的存在严格依赖于有限的核心四极形变（$\beta_2 > 0.15$ 与三轴性 $\gamma \approx 20^\circ \sim 30^\circ$）。**能带一旦趋近终止点，由于 $Q_t \to 0$ 与形状扁长化，手征几何三面体与摆动恢复力坍缩崩溃**，因此能带终止界定了三轴集体激发态存在的终极自旋上限！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/band_termination_cns_calculator.py` 中实现了完整的能带终止分析器：
1. **价空间最大自旋代数评估器**：从质子/中子单粒子侵入轨道排布计算严格的最大终止自旋 $I_{\text{term}}$；
2. **平滑终止四极矩 $Q_t(I)$ 演化拟合器**：依据三轴非对称角 $\gamma(I)$ 轨迹反演 $Q_t(I)$ 与 $B(E2)$ 的理论暴跌曲线；
3. **动力学转动惯量 $\mathcal{J}^{(2)}$ 崩溃检验器**：从实测级联 $\gamma$ 能量梯度诊断终止特征；
4. **刚体转子参考减除（$E - E_{\text{RR}}$）尖点探测器**：自动定位终止态自旋 cusp 峰位与越过终止态的激发惩罚能。

---

## 6. 权威文献与理论溯源

1. **Bengtsson, T. & Ragnarsson, I.** (1985). Rotational bands and particle-hole excitations at very high spin. *Nucl. Phys. A*, 436(1), 14-82.
2. **Afanasjev, A. V., Fossan, D. B., Lane, G. J., & Ragnarsson, I.** (1999). Termination of rotational bands: absolute spin assignments and microscopic configurations. *Phys. Rep.*, 322(1-2), 1-104.
3. **Wadsworth, R. et al.** (1998). Loss of collectivity in the smooth terminating band in $^{109}\text{Sb}$. *Phys. Rev. Lett.*, 80(6), 1174-1177.
4. **Frauendorf, S.** (2001). Spontaneous symmetry breaking in rotating nuclei. *Rev. Mod. Phys.*, 73(2), 463-514.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 8 章：高自旋态与形变核转动能谱. 原子能出版社.

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
