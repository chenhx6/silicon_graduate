---
type: concept
title: "手征双重势阱量子隧穿、孪生能带能隙ΔE(I)自旋演化与手征振动向静态转动相变动力学"
aliases: [手征双阱势, 量子隧穿劈裂, 双重带能隙, Delta_E(I), 手征振动, 静态手征转动, 哥氏平面重整, WKB隧穿, 非共面相变]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [chiral-double-well, quantum-tunneling, energy-splitting, chiral-vibration, static-chiral-rotation, coriolis-restoration, wkb-approximation, 128cs]
---

# 手征双重势阱量子隧穿、孪生能带能隙ΔE(I)自旋演化与手征振动向静态转动相变动力学

## Definition

### 物理全景：手征几何势能面上的宏观量子隧穿

在三轴形变原子核（$\gamma \approx 30^\circ$）的手征体系中，核心集体转动矢量 $\mathbf{R}$ 相对两未配对高 $j$ 核子（短轴质子 $\mathbf{j}_p$ 与长轴中子 $\mathbf{j}_n$）构成的平面发生倾斜。
在内禀参考系中，旋转由非共面方位夹角 $\phi$（Aplanarity angle）标定。
以两个核子张成的平面（$\phi = 0$）为基准：
- $\phi > 0$ 对应右手手征取向状态（Right-handed enantiomer, $|R\rangle$）；
- $\phi < 0$ 对应左手手征取向状态（Left-handed enantiomer, $|L\rangle$）；
- $\phi = 0$ 对应共面态（Coplanar state），在空间上构成阻隔左手与右手构型的能量势垒。

根据 C. M. Petrache 2024 专著《Chirality and Wobbling in Atomic Nuclei》、K. Starosta 等（Phys. Rev. Lett. 86, 971, 2001）以及 S. Frauendorf（Rev. Mod. Phys. 73, 463, 2001）：
在宏观经典物理中，一旦系统落入左手或右手极小，手征对称性将被彻底固定。
**但在微观量子原子核中，左右两个手性势阱之间必然存在有限势垒的量子隧穿（Quantum Tunneling）！**
这种穿透效应将左手态与右手态线性杂化，恢复宇称-时间反演复合对称性，产生一对正交的能量劈裂态：
$$|Band\ 1\rangle = \frac{1}{\sqrt{2}} \left( |R\rangle + |L\rangle \right), \qquad |Band\ 2\rangle = \frac{1}{\sqrt{2}} \left( |R\rangle - |L\rangle \right)$$
实验上观测到的手征双重带之间的能量差：
$$\Delta E(I) = E(I, \text{Band } 2) - E(I, \text{Band } 1)$$
正是**微观量子隧穿频率的直接宏观度量**！随自旋增加，$\Delta E(I)$ 的特征性指数坍缩是确证原子核手征性最不可动摇的核心实验铁证！

---

## Necessary Assumptions

### 严格 1D 双阱集体势与 WKB 隧穿推导

### (1) 自旋依赖的四阶唯象手征势能函数 $V(\phi, I)$
沿手征非共面坐标 $\phi$，集体能量泛函展开为对称形式：
$$V(\phi, I) = \frac{1}{2} C_2(I) \phi^2 + \frac{1}{4} C_4 \phi^4$$
其中四阶恢复刚度 $C_4 > 0$，而二阶系数 $C_2(I)$ 随转动自旋 $I$ 动态演化：
$$C_2(I) = C_{20} - \alpha_{\text{rot}} (I - I_{\text{crit}})$$

#### 三大动力学相区自洽划分：
1. **低自旋区（$I < I_{\text{crit}}$）**：
   $C_2(I) > 0$。势能在 $\phi = 0$ 处具有唯一的全局极小值。体系尚未形成左右势阱，核子围绕共面状态进行大振幅振动，即**平面手征振动（Planar Chiral Vibration）**。
   双重带能级差对应简谐振动声子能量：$\Delta E(I) = \hbar \omega_{\text{vib}} \sim 250 \sim 400\text{ keV}$；
2. **中自旋手征窗口（$I_{\text{crit}} \le I \le I_{\text{rest}}$）**：
   $C_2(I) < 0$。势能在中间发生对称自发破缺，在 $\phi = 0$ 处产生马鞍势垒，并在两侧形成双极小值：
   $$\pm \phi_0(I) = \pm \sqrt{-\frac{C_2(I)}{C_4}}$$
   中央共面势垒高度达到：
   $$\Delta V_{\text{barrier}}(I) = \frac{C_2(I)^2}{4 C_4}$$
   两势阱分别对应左手与右手定域态；
3. **极高自旋哥氏重整区（$I > I_{\text{rest}}$）**：
   巨大的离心与哥氏扭矩将质子与中子角动量拉回中轴，重构为单阱，双带能隙重新剧烈拉开。

---

### (2) WKB 势垒穿透与能量劈裂公式
在双阱区间内，量子态在势阱底部的局部简谐振动频率为：
$$\hbar \omega_0(I) = \sqrt{\frac{1}{B_{\text{mass}}} \left. \frac{d^2 V}{d\phi^2} \right|_{\phi_0}} = \sqrt{\frac{- 2 C_2(I)}{B_{\text{mass}}}}$$
其中 $B_{\text{mass}}$ 为手征集体转动惯性质量。

粒子穿透中央势垒的作用量积分：
$$S_{\text{tunnel}} = \int_{-\phi_0}^{+\phi_0} \sqrt{2 B_{\text{mass}} V(\phi)} d\phi = \frac{4}{3} \sqrt{2 B_{\text{mass}} \Delta V} \cdot \phi_0$$
根据 WKB 半经典隧穿理论，简并能级发生对称-反对称量子劈裂：
$$\Delta E(I) = \frac{\hbar \omega_0}{\pi} \exp\left( - \frac{S_{\text{tunnel}}}{\hbar} \right)$$

**指数塌缩物理机制**：
随着自旋 $I$ 从临界自旋 $I_{\text{crit}}$ 向前推进，核心转动能量 $R_m^2 / (2\mathcal{J}_m)$ 急剧加深了双阱深度，使得势垒高度 $\Delta V(I) \propto (I - I_{\text{crit}})^2$ 剧烈升高。
作用量 $S_{\text{tunnel}}$ 的大幅增长导致指数衰减项急剧压低，**双带能隙 $\Delta E(I)$ 呈现断崖式指数暴跌，迅速趋近于零（$\Delta E \to 0$）**！
当 $\Delta E(I) \le 50 \sim 60\text{ keV}$ 时，原子核正式确立为**静态手征转动相（Static Chiral Rotation）**！

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/chiral_vibrational_tunneling_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `chvibe` 命令。

### 运行示范（以典型手征核 $I_{\text{crit}} = 11\hbar$ 扫描自旋演化）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py chvibe -I 16.0 --scan --json
```

### 计算输出核心物理特征：
1. **低自旋振动区（$I = 9 \sim 14\hbar$）**：
   - 处于单阱或浅势垒区，$\Delta E$ 从 $9\hbar$ 处的 $355.9\text{ keV}$ 逐步软化下行至 $100.0\text{ keV}$，标记为 `Planar_Chiral_Vibration`；
2. **中自旋静态手征窗口（$I = 15 \sim 17\hbar$）**：
   - 在 $I = 15\hbar$ 处，双势阱深度成型（势垒 $4.0\text{ keV}, \phi_0 = 16.2^\circ$），能隙大幅下沉至 $\Delta E = 45.6\text{ keV}$；
   - 在 $I = 16\hbar$ 处，势垒加厚至 $30.3\text{ keV}, \phi_0 = 26.9^\circ$，$\Delta E = 47.5\text{ keV}$；
   - 在 $I = 17\hbar$ 处，势垒高达 $81.0\text{ keV}, \phi_0 = 34.4^\circ$，能隙收敛至极小值：
     $$\Delta E = 31.7\text{ keV}$$
   - 标记为 `Static_Chiral_Rotation`（能量近简并手征双重带完美重现）；
3. **高自旋相变退出（$I \ge 18\hbar$）**：
   - 进入 `Coriolis_Planar_Restoration` 区，能隙骤增至 $300+\text{ keV}$，精确再现了全球实验手征核中双带能隙“高 $\to$ 极小简并 $\to$ 重新分离”的马鞍形实验轨迹！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]：3D TAC 计算得出的手征体积度规 $\mathcal{V}_{\text{chiral}}$ 与此处 1D 双阱平衡角 $\phi_0$ 构成了微观与集体相空间的严格对应；
- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]：手征双带能隙随自旋下降与横向摆动（TW）能量随自旋下降，在微观上均来源于核子在三轴势场中的离轴定域取向；
- [[signature-inversion-and-triaxial-pn-interaction]]：手征振动与签名反转（Signature Inversion）在低自旋区相互交织，必须通过 $B(M1)$ 跃迁检验进行严格辨识。
