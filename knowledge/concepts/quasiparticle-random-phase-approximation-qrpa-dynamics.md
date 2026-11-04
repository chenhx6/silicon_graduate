---
type: concept
title: "准粒子无规相位近似（QRPA）、基态关联与超流核多体集体振动动力学"
aliases: [QRPA, 准粒子无规相位近似, pnQRPA, 基态关联, X与Y振幅, 粒子-粒子相互作用gpp, 无规相位近似, 双贝塔衰变矩阵元]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [qrpa, pnqrpa, bcs-quasiparticle, ground-state-correlations, double-beta-decay, gpp-parameter, ikeda-sum-rule, collective-vibrations]
---

# 准粒子无规相位近似（QRPA）、基态关联与超流核多体集体振动动力学

## Definition

### 物理全景：超越平均场的谐振子小振幅量子涨落理论

在开壳层原子核中，费米面附近的核子由于短程吸引配对力形成 BCS 超流体态（Superfluid Vacuum, $|\text{BCS}\rangle$）。然而，真实的原子核不仅具有静态平均场与静态对能隙，而且表现出强烈的动力学表面集体振动（如低激发态 $2_1^+, 3_1^-$ 声子）与高激发态巨多极共振（如 IVGDR, ISGQR, GTGR）。

**准粒子无规相位近似（Quasiparticle Random-Phase Approximation, QRPA）**是现代低能核物理中处理开壳超流核集体振动、电磁跃迁几率与双贝塔衰变（$0\nu\beta\beta / 2\nu\beta\beta$）核基质元的最强大微观自洽理论。

根据 J. Suhonen《From Nucleons to Nucleus》（第 18–19 章）、P. Ring & P. Schuck《The Nuclear Many-Body Problem》（第 8 章）与 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II（第 6 章）：
1. **基态关联的量子引入（Ground-State Correlations）**：
   在较初级的准粒子塔姆-丹科夫近似（QTDA）中，假定真空是刚性的（$|\text{HF}\rangle$ 或 $|\text{BCS}\rangle$），激发态仅由向前传播的双准粒子激发算符 $A^\dagger$ 构成；
   而 QRPA 允许基态真空中存在**虚双准粒子涨落（$Y$ 振幅）**，将体系扩展至既包含向前传播（Forward-going, $X$ 振幅）又包含向后传播（Backward-going, $Y$ 振幅）的时间对称时间依赖 Hartree-Fock-Bogoliubov（TDHFB）小振幅极限；
2. **跃迁强度的相干暴增与能量下移**：
   基态关联的引入使得集体振动声子的能量从非相干单粒子间距（$\sim 2\Delta$）向下压低，同时使得电多极跃迁振幅正比于 $(X + Y)$。$X$ 与 $Y$ 的同相相干叠加，**直接解释了低激发 $2_1^+$ 态 $B(E2)$ 跃迁几率达到单粒子 Weisskopf 单位数十至数百倍的巨大集体相干增强**！

---

## Necessary Assumptions

### QRPA 运动方程与非厄米超矩阵本征值问题

### (1) 声子生成算符与准粒子双重表象
定义多极性为 $J M$ 的双准粒子对算符：
$$A_{ab}^\dagger(JM) \equiv [a_a^\dagger a_b^\dagger]_{JM}$$
QRPA 声子算符表示为：
$$Q_\nu^\dagger(JM) = \sum_{a \le b} \left[ X_{ab}^\nu A_{ab}^\dagger(JM) - (-1)^{J-M} Y_{ab}^\nu A_{ab}(J, -M) \right]$$
真空间隙条件定义关联物理基态 $|\text{QRPA}\rangle$：
$$Q_\nu(JM) |\text{QRPA}\rangle = 0$$

### (2) QRPA 运动方程（Equation of Motion, EOM）
通过在粒子数和平均场下计算对易子期望值：
$$\langle \text{BCS} | [\delta Q, [H, Q_\nu^\dagger]] | \text{BCS} \rangle = \omega_\nu \langle \text{BCS} | [\delta Q, Q_\nu^\dagger] | \text{BCS} \rangle$$
严格推导出著名的 **QRPA 超矩阵本征方程**：
$$\begin{pmatrix} \mathcal{A} & \mathcal{B} \\ -\mathcal{B}^* & -\mathcal{A}^* \end{pmatrix} \begin{pmatrix} X^\nu \\ Y^\nu \end{pmatrix} = \omega_\nu \begin{pmatrix} X^\nu \\ Y^\nu \end{pmatrix}$$
其中矩阵元为：
- $\mathcal{A}_{ab, cd} = (\varepsilon_a + \varepsilon_b) \delta_{ab, cd} + \mathcal{V}_{ab, cd}^{11}$（对角主导为双准粒子能量之和）
- $\mathcal{B}_{ab, cd} = \mathcal{V}_{ab, cd}^{20}$（全微观源于基态虚激发相互作用）

### (3) 正交归一化条件（Bose 玻色型对易关系）
由于声子算符在近似下满足玻色子对易关系 $[Q_\nu, Q_{\nu'}^\dagger] = \delta_{\nu\nu'}$，波函数振幅必须满足非紧致双曲正交归一化：
$$\sum_{a \le b} \left( |X_{ab}^\nu|^2 - |Y_{ab}^\nu|^2 \right) = 1$$
这一条件保证了物理本征能量 $\omega_\nu$ 成对出现（$+\omega_\nu$ 与 $-\omega_\nu$）。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 质子-中子 QRPA（pnQRPA）与粒子-粒子相互作用参数 $g_{pp}$

在电荷交换反应（如 $(p, n), (n, p)$）与单/双贝塔衰变中，体系涉及质子向中子（或中子向质子）的转换，对应由**质子-中子对算符 $[a_p^\dagger a_n^\dagger]_{JM}$ 构成的 pnQRPA 框架**。

### (1) 剩余相互作用的两大通道：$g_{ph}$ 与 $g_{pp}$
在 pnQRPA 中，有效核力残余相互作用被精细拆分为两大具有截然不同物理效应的通道：
1. **粒子-空穴通道（Particle-Hole, $ph$）**：由参数 $g_{ph}$ 调控，表现为排斥相互作用，将伽莫夫-泰勒巨共振（GTGR）推向高激发能区（$E_x \sim 15\text{ MeV}$）；
2. **粒子-粒子通道（Particle-Particle, $pp$）**：由参数 $g_{pp}$ 调控，表现为质子-中子对之间的吸引超流相互作用。

### (2) 双贝塔衰变（$0\nu\beta\beta / 2\nu\beta\beta$）对 $g_{pp}$ 的极端敏感性
在计算无中微子双贝塔衰变核基质元 $M^{0\nu}$ 与两中微子双贝塔衰变 $M^{2\nu}$ 时：
$$M^{2\nu} = \sum_m \frac{\langle 0_f^+ || \hat{\beta}^- || 1_m^+ \rangle \langle 1_m^+ || \hat{\beta}^- || 0_i^+ \rangle}{E_m - (E_i + E_f)/2}$$
- 随着吸引性粒子-粒子强度 $g_{pp}$ 从 0 逐步增加至实际物理值（$g_{pp} \sim 0.9 \sim 1.1$），中间态 $1_m^+$ 的跃迁基质元发生剧烈的相消干涉，$M^{2\nu}$ 急剧下跌并在 $g_{pp} \approx 1.0$ 附近穿过零点！
- **临界失稳（QRPA Collapse）**：若 $g_{pp}$ 过强，超矩阵的最小本征值将跌入虚数区（$\omega^2 < 0$），标志着球形 BCS 费米真空发生动力学相变坍缩，体系在基态自发涌现质子-中子配对形变！

### (3) Ikeda 求和定则在 pnQRPA 下的绝对守恒
Suhonen（2007）严格推导证明：即便包含复杂的基态涨落（$Y \ne 0$），在 pnQRPA 闭合空间下，伽莫夫-泰勒算符严格自洽守恒：
$$S_-(GT) - S_+(GT) = \sum_m B(GT_-; 0_{\text{g.s.}}^+ \to 1_m^+) - \sum_m B(GT_+; 0_{\text{g.s.}}^+ \to 1_m^+) \equiv 3(N - Z)$$
没有任何求和强度因非谐振效应或基态关联而丢失，体现了微观规范对称性的纯洁性。

---

## 4. 与低能高自旋及在束谱学的深度交织

在三轴形变与在束 $\gamma$ 谱学中：
1. **低自旋声子向高自旋转子的过渡**：
   在弱形变与过渡核区（如 $^{102}\text{Pd}, {}^{130}\text{Ba}$），低自旋态为典型的 QRPA 单声子与双声子四极激发（$2_1^+, 0_2^+, 2_2^+, 4_1^+$）；随着自旋增加至 $I \ge 6\hbar$，系统克服谐振子恢复力，平滑过渡至大振幅潮汐波（Tidal Waves）行波转动或三轴刚性转子模式；
2. **剪刀模式（Scissors Mode）的微观解构**：
   在形变核中，质子超流流体与中子超流流体发生反相微幅剪切角振荡，在 $E_x \sim 3\text{ MeV}$ 产生具有特征性 $M1$ 跃迁的磁偶极剪刀模式（$J^\pi = 1^+$），其激发能量与跃迁几率由 pnQRPA 唯象微观精确重现。

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/qrpa_matrix_vibrational_calculator.py` 中实现了完整的微观 QRPA 与 pnQRPA 分析器：
1. **QRPA 超矩阵本征求解器**：输入双准粒子能量与残余相互作用矩阵元，构建并精确对角化非厄米超矩阵 $\begin{pmatrix} \mathcal{A} & \mathcal{B} \\ -\mathcal{B} & -\mathcal{A} \end{pmatrix}$，输出复能谱与规范化双曲归一振幅 $(X, Y)$；
2. **基态关联与集体增强因子评估器**：计算声子能量降低量及电多极相干跃迁增强倍数 $(X+Y)^2$；
3. **pnQRPA 粒子-粒子 $g_{pp}$ 灵敏度扫描器**：动态扫描 $g_{pp}$ 对最低 $1^+$ 态能量与双贝塔衰变矩阵元消长行为的影响；
4. **QRPA 真空稳定性检验器**：计算辛海森矩阵正定性，自动诊断系统是否发生对称性自发破缺相变。

---

## 6. 权威文献与理论溯源

1. **Ring, P. & Schuck, P.** (1980). *The Nuclear Many-Body Problem*, Chapter 8 (The Random Phase Approximation). Springer-Verlag.
2. **Suhonen, J.** (2007). *From Nucleons to Nucleus*, Chapters 18 & 19 (Two-Quasiparticle Mixing by QRPA and pnQRPA). Springer.
3. **Vogel, P. & Zirnbauer, M. R.** (1986). Suppression of the two-neutrino double beta decay by nuclear-structure effects. *Phys. Rev. Lett.*, 57(25), 3148-3151.
4. **Civitarese, O., Faessler, A., & Tomoda, T.** (1987). Suppression of the two-neutrino $\beta\beta$ decay by the proton-neutron-quasiparticle interaction. *Phys. Lett. B*, 194(1), 11-14.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 8 章：原子核集体运动与微观多体模型. 原子能出版社.

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
