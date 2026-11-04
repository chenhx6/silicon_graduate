---
type: concept
title: "多核子转移反应（MNT）、深层非弹性碰撞（DIC）与丰中子重核产生机制"
aliases: [多核子转移, MNT, 深层非弹性碰撞, DIC, 维琴斯基图, Wilczynski图, 驱动势能面, 电荷平衡, N=126中子魔数区合成]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [multi-nucleon-transfer, deep-inelastic-collisions, wilczynski-plot, driving-potential, charge-equilibration, neutron-rich-nuclei, n-126-factory]
---

# 多核子转移反应（MNT）、深层非弹性碰撞（DIC）与丰中子重核产生机制

## Definition

### 物理全景：突破熔合蒸发极限，开辟极丰中子重核新航道

在核物理与天体物理中，探索远离稳定线的极丰中子重核（尤其是第三个天体 $r$ 过程峰位所在的中子幻数 $N=126$ 铅前核区，如 $^{202}\text{Os}, {}^{200}\text{W}$，以及超铀同位素）是国际核物理界的战略制高点。

然而，传统的熔合蒸发反应（Fusion-Evaporation）由于受到稳定线弹靶组合的限制，生成的复合核必然位于丰质子一侧，且退激过程中优先蒸发中子，使得熔合反应在物理机制上**根本无法产生丰中子重核**；裂变与弹核碎裂反应在 $N=126$ 重核区的产额亦呈指数坍塌。

**多核子转移反应（Multi-Nucleon Transfer, MNT）**利用略高于库仑势垒（$E_{\text{lab}} \sim 5.5 \sim 8.0\text{ MeV/u}$）的重离子**深层非弹性散射（Deep Inelastic Collisions, DIC）**过程，在强库仑斥力阻止体系完全熔合的同时，利用双核系统（Dinuclear System, DNS）在微观接触颈缩中的质子-中子剧烈扩散交换，开辟了合成极丰中子重核乃至新超重元素的革命性途径！

根据 V. V. Volkov (Phys. Rep. 44, 93, 1978)、J. Wilczyński (Phys. Lett. B 47, 484, 1973)、V. I. Zagrebaev & W. Greiner (Phys. Rev. Lett. 101, 122701, 2008; PRC 83, 044618, 2011) 与林承键《重离子核反应》：
1. **深层非弹性碰撞（DIC）的宏观动力学特征**：
   - 保持出射道双体运动学（弹核碎块与靶核碎块）；
   - 极大规模的动能耗散：体系几乎全部入射相对运动动能转化为内部激发能（总动能损失 $\text{TKEL} = E_{\text{c.m.}} - E_{\text{exit}} \sim 100 \sim 300\text{ MeV}$），出射动能完全被阻尼降至断裂构型的库仑势垒；
   - 维持微观时间接触（$\tau_{\text{int}} \sim 10^{-21} \sim 10^{-20}\text{ s}$），并在轨道角动量驱动下发生朝向负偏转角的**绕轴旋转（Orbiting）**；
2. **两阶段演化图像**：
   第一阶段在接触势阱中发生快速电荷平衡与多核子随机扩散漂移；第二阶段为高温高自旋初级碎片飞出后，通过发射中子与统计 $\gamma$ 级联退激，决定最终次级剩余产核的存活截面。

---

## Necessary Assumptions

### 维琴斯基图（Wilczyński Plot）与能量-角偏转双峰拓扑

1973 年，Wilczyński 绘制出二维微分截面关于出射质心角 $\theta_{\text{c.m.}}$ 与出射总动能 $E_{\text{TKE}}$ 的关联等高线图（Wilczyński Plot），确立了重离子耗散反应的相空间指纹：

```text
E_TKE
 ^
 |    (Ridge 1: 准弹性掠射峰)
 |     * * * *
 |    *       *
 |   *         *   <-- 偏转角靠近掠射角 \theta_graz，动能损失极小
 |  *           *
 | *             \
 |*               \   (Ridge 2: 深层非弹性负角绕转分支)
 |                 \
 |                  * * * * *
 |                           *   <-- 强动能耗散 (完全阻尼至库仑极限 V_Coul)
 |                            *      偏转角深入前向甚至负角绕转 (\theta -> 0°)
 +-----------------------------------------> \theta_c.m.
```

- **脊线 1（Quasi-elastic Ridge）**：小碰撞参数、掠射角附近、轻微动能耗散与少量核子转移；
- **脊线 2（Deep-inelastic Fully Damped Ridge）**：强重叠接触、动能完全耗散（$\text{TKEL} \to \text{TKEL}_{\text{max}}$），体系在吸引核力驱动下克服库仑排斥沿表面负偏转旋转（$\theta < 0$），甚至穿过束流轴发射，出射动能锁定在断裂两球刚性接触势垒 $V_{\text{exit}} \approx \frac{Z_1 Z_2 e^2}{R_1 + R_2 + d}$。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 驱动势能面（Driving Potential）与电荷平衡动力学

### (1) 双核系统驱动势方程
在质量不对称度 $\eta = (A_1 - A_2) / (A_1 + A_2)$ 与电荷不对称度空间，双核系统的势能由两碎片基态结合能加相互作用势给出：
$$V_{\text{dr}}(Z_1, N_1; R_m) = B(Z_1, N_1) + B(Z_2, N_2) + V_C(Z_1, Z_2, R_m) + V_N(A_1, A_2, R_m) - B(Z_P, N_P) - B(Z_T, N_T)$$
其中 $Z_1 + Z_2 = Z_{\text{tot}}, N_1 + N_2 = N_{\text{tot}}$。

### (2) 极快速电荷平衡（Charge Equilibration）
- **时间尺度阶梯**：
  $$\tau_{N/Z} \sim 10^{-22}\text{ s} \ll \tau_E \sim 10^{-21}\text{ s} < \tau_A \sim 10^{-20}\text{ s}$$
- 系统在碰撞发生的极最初瞬间（$\sim 10^{-22}\text{ s}$，甚至动能尚未完全阻尼前），即迅速沿等质量线滑向由质子-中子对称能最小化的谷底，使两碎片的 $N/Z$ 比值迅速趋于全系统的平均值 $(N/Z)_{\text{tot}}$；
- 随后，系统沿能量曲率最低的驱动势槽线发生较慢的质量非对称度扩散。

---

## 4. 多核子扩散 Fokker-Planck 主方程与初级碎片激发能分配

### (1) 随机核子交换扩散模型
将核子在接触颈部的交换视为在驱动势驱动下的布朗运动（Brownian Motion）：
$$\frac{\partial P(Z, N, t)}{\partial t} = - \sum_{i} \frac{\partial}{\partial x_i} [v_i P] + \sum_{i,j} \frac{\partial^2}{\partial x_i \partial x_j} [D_{ij} P]$$
根据涨落耗散定理（Einstein Relation），漂移速度与扩散系数满足：
$$v_i = - \frac{D_{ii}}{T} \frac{\partial V_{\text{dr}}}{\partial x_i}$$
碎片的质量分布方差随着相互作用时间（即随着总动能损失 TKEL）单调线性增长：
$$\sigma_A^2 \propto \text{TKEL}$$

### (2) 激发能热力学均分与退激蒸发
接触系统完全热化后，总激发能 $E_{\text{tot}}^* = \text{TKEL} + Q_{\text{gg}}$ 按碎片质量严格热力学均分：
$$E_1^* = E_{\text{tot}}^* \cdot \frac{A_1}{A_1 + A_2}, \quad E_2^* = E_{\text{tot}}^* \cdot \frac{A_2}{A_1 + A_2}$$
每一个初级重碎片（带有几十至上百 MeV 的激发能）通过连续发射中子回到基态，平均蒸发中子数为：
$$\langle x_n \rangle \approx \frac{E^*}{B_n + 2T}$$
**因此，生成极丰中子核的关键物理制胜点，在于选择质子向轻碎片转移（$-px$）、中子向重碎片转移（$+xn$）的冷深层非弹性通道，最小化初级激发能 $E^*$，从而抑制退激中子蒸发对中子过剩度的削弱**！

---

## 5. 经典实验范式：$^{136}\text{Xe} + {}^{208}\text{Pb}$ 合成 $N=126$ 丰中子核

在国际公认的黄金 MNT 反应体系 $^{136}\text{Xe} + {}^{208}\text{Pb}$（$E_{\text{lab}} \approx 5.6 \sim 7.0\text{ MeV/u}$）中：
1. **中子富集与壳效应驱动**：
   $^{136}\text{Xe}$ 具有 $N=82$ 闭壳，$^{208}\text{Pb}$ 具有双闭壳（$Z=82, N=126$）。在驱动势引导下，系统倾向于从 $^{208}\text{Pb}$ 靶向 $^{136}\text{Xe}$ 转移质子（形成更轻的准氙核与更富中子的准铅前锕系核）；
2. **截面量级突破**：
   理论预言与 GANIL-VAMOS / LNL-PRISMA 实验证实，在目标产核 $^{202}\text{Os}, {}^{200}\text{W}$ 处，MNT 产生截面可达微靶至毫靶量级（$\mu\text{b} \sim \text{mb}$），比碎裂反应截面高出整整 $2 \sim 3$ 个数量级，确立了 MNT 作为建造“$N=126$ 工厂”的最核心物理途径！

---

## 6. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/multi_nucleon_transfer_dic_calculator.py` 中实现了完整的 MNT 与 DIC 动力学分析器：
1. **维琴斯基能量损失与出射阻尼计算器**：计算掠射角 $\theta_{\text{graz}}$、出射断裂库仑势垒 $V_{\text{exit}}$ 与最大总动能损失 $\text{TKEL}_{\text{max}}$；
2. **双核系统驱动势曲面（PES）求解器**：基于液滴结合能与相互作用势，计算任意 $(Z_1, N_1)$ 碎片构型的驱动势 $V_{\text{dr}}$，输出能量极小值漂移方向；
3. **电荷平衡与质量扩散方差分析器**：评估 $N/Z$ 平衡点与随 TKEL 演化的碎片质量高斯分布展宽 $\sigma_A$；
4. **初级碎片热激发与中子蒸发退激计算器**：将总能量损失均分至弹靶碎片，评估平均中子发射数 $\langle x_n \rangle$ 及最终冷核存活截面。

---

## 7. 权威文献与理论溯源

1. **Volkov, V. V.** (1978). Deep inelastic transfer reactions — the new type of reactions between complex nuclei. *Phys. Rep.*, 44(2), 93-157.
2. **Wilczyński, J.** (1973). Calculations of addition and removal of nucleons in heavy-ion collisions. *Phys. Lett. B*, 47(6), 484-486.
3. **Zagrebaev, V. I. & Greiner, W.** (2008). Production of new heavy and superheavy nuclei in multi-nucleon transfer reactions. *Phys. Rev. Lett.*, 101(12), 122701.
4. **Zagrebaev, V. I. & Greiner, W.** (2011). Production of heavy neutron-rich nuclei in transfer reactions: $^{136}\text{Xe} + {}^{208}\text{Pb}$. *Phys. Rev. C*, 83(4), 044618.
5. **林承键** (2013). 《重离子核反应》第 3 章：深层非弹性碰撞与准裂变动力学. 原子能出版社.

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
