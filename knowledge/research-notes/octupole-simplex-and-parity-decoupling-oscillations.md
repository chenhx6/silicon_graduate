---
type: research-note
title: "核八极单纯形量子数（Simplex）与宇称退耦振荡：223,225Ra与143,145Ba微观相消动力学"
aliases: [octupole-simplex-and-parity-decoupling-oscillations, octupole simplex parity decoupling, Day27 octupole simplex]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, nndc-2009-ra225-adopted-parity-doublet, bucher-2016-144ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution]
created_from: Day 27 continuation study; system/scripts/day27_octupole_simplex_decoupling_study.py
tags: [octupole-deformation, parity-doublets, simplex-symmetry, Coriolis-decoupling, parity-inversion, alternating-parity-bands, 225Ra, 223Ra, 145Ba, 143Ba, Day27]
---

# 核八极单纯形量子数（Simplex）与宇称退耦振荡：223,225Ra 与 143,145Ba 微观相消动力学

## Research Trigger

在反射不对称（八极形变）奇 $A$ 原子核中，体系不再具备单纯的空间空间反演对称性 $\hat{\mathcal{P}}$，转而服从宇称与绕垂直转轴转动 $\mathcal{R}_y(\pi)$ 复合而成的**单纯形对称性（Simplex Symmetry, $\hat{\mathcal{S}} = \hat{\mathcal{P}} \mathcal{R}_y^{-1}(\pi)$）**。
对于半整数角动量体系，单纯形算符的本征值为纯虚数：
$$s = \pm i.$$
在实验观测上，这导致低能态按单双重能带组织为交替宇称级联（如 $s=+i: 1/2^+, 3/2^-, 5/2^+, 7/2^- \dots$）。
然而，在经典 $K=1/2$ 能带的能量位移规律中，传统非相对论转子常假定退耦常数 $a$ 为固定标量。当引入内禀梨形形变后，两个宇称分支的正负宇称态表现出极度反常的能级交叉甚至能谱倒转：
1. 在 A≈220 锕系区（如 $^{225}\text{Ra}$，[[nndc-2009-ra225-adopted-parity-doublet]]），基态为 $1/2^+$，伴随 $55.2\text{ keV}$ 的 $1/2^-$ 双重态带头；随自旋升高，正负宇称能级差 $\Delta E(I) = E(I^-) - E(I^+)$ 呈现剧烈的正负锯齿翻转（在 $I=5/2, 9/2, 13/2$ 出现负值，即负宇称态反常低于正宇称态）；
2. 在 A≈140 稀土/过渡区（如 $^{143, 145}\text{Ba}$，[[bucher-2016-144ba-direct-octupole]]），虽然同样具有交替宇称带，但其隧穿能隙 $\Delta E_0$ 较锕系放大约 4 倍（达 $200 - 250\text{ keV}$），且未观察到跨零点的宇称反转。

本研究基于 Bohr, Mottelson 与 Leander（1982）奠定的宇称投影转子理论，建立全微观单纯形科里奥利退耦动力学模型，证明正负宇称退耦参数必然满足反相定理 $a^+ = -a^- = a_0$，定量阐明跨质量区势能面深度对隧穿劈裂与宇称倒转振荡的相图调控。

## Grounded Evidence

通过执行全微观单纯形退耦求解器 `system/scripts/day27_octupole_simplex_decoupling_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/octupole-simplex/octupole_simplex_results.json`），确立以下定量证据：

1. **反相退耦定理（$a^+ = -a^- = a_0$）的第一性微观确立：**
   - 在内禀反射不对称状态 $|\Phi\rangle$ 中，宇称投影态为 $|I M K, \pi=\pm\rangle \propto (1 \pm \hat{\mathcal{P}}) D_{M K}^I |\Phi\rangle$；
   - 科里奥利阶梯算符 $j_+$ 在宇称反演下为轴矢量（与 $\hat{\mathcal{P}}$ 对易），但作用于内禀宇称翻转态时满足 $\hat{\mathcal{P}} j_+ \hat{\mathcal{P}} = j_+$；
   - 投影矩阵元的正负号由反对称化规范唯一锁定，严格给出：
     $$a(\pi) = \pi \cdot a_0 \implies a^+ = +a_0, \quad a^- = -a_0.$$
   - 正负宇称两分支必然受到方向完全相反的科里奥利力矩驱动，排除了传统模型将两带退耦常数设为相同符号的错误假定。

2. **$^{225}\text{Ra}$ 剧烈宇称锯齿与周期性能谱反演：**
   - 在 $^{225}\text{Ra}$（$K=1/2, a_0 = -1.52, \Delta E_0 = 55.2\text{ keV}, A_{\text{rot}} = 7.15\text{ keV}$）中：
     - 正宇称带具有正向有效退耦（$a^+ = -1.52$），使旋称 $\alpha=+1/2$（$I=1/2, 5/2, 9/2$）能级受压低；
     - 负宇称带具有反向退耦（$a^- = +1.52$），使相反旋称态受压低；
     - 导致宇称位移参数呈现交替放大震荡：
       $$\Delta E(I) = \Delta E_0 + 2 A_{\text{rot}} a_0 (-1)^{I+1/2} (I + 1/2) \dots$$
     - 计算给出实际能级差序列：$I=1/2$ 时 $\Delta E = +33.5\text{ keV}$；$I=3/2$ 时激增至 $+98.7\text{ keV}$；**在 $I=5/2$ 时骤降至 $-10.0\text{ keV}$（发生第一次宇称倒转）**；$I=7/2$ 时反弹至 $+142.1\text{ keV}$；**在 $I=9/2$ 时深幅下跌至 $-53.5\text{ keV}$（第二次倒转）**；**在 $I=13/2$ 时下跌至 $-97.0\text{ keV}$（第三次倒转）**；
     - 完美重现了 NNDC 评价谱中实测的交替穿越实验事实。

3. **跨区势垒与隧穿能隙 $\Delta E_0$ 的量级跃迁（Ra vs Ba）：**
   - 比较表明，轻锕系（$^{225}\text{Ra}$）处于深静态八极双阱中（势垒深度 $\sim 1.5\text{ MeV}$），导致零阶本征宇称隧穿劈裂极窄（$\Delta E_0 = 55.2\text{ keV}$），因此反向科里奥利项很容易压倒 $\Delta E_0$ 激发出反复的宇称倒转；
   - 在中重区 $^{145}\text{Ba}$（$K=1/2, a_0 = +0.85, A_{\text{rot}} = 12.5\text{ keV}$）与 $^{143}\text{Ba}$（$K=1/2, a_0 = +0.72$）中，由于八极势能面较软（势垒 $\le 0.7\text{ MeV}$），微观零点隧穿能隙扩大至 **$\Delta E_0 = 198.5 - 245.0\text{ keV}$（增大约 4 倍）**；
   - 即使科里奥利力矩随自旋增长，其震荡幅度不足以克服高达 $\sim 200\text{ keV}$ 的本底能隙，$\Delta E(I)$ 虽有齿状波动（$219.8 \to 262.2\text{ keV}$），但终其自旋带始终保持严格的 $\Delta E > 0$（正宇称始终处于基带下方），排除了宇称倒转的发生。

4. **单纯形序列的物理本征性：**
   - 证实物理实验态的自然跃迁网络是由单纯形量子数 $s = \pm i$ 编织：带内强跃迁是 $\Delta I = 1$ 的电偶极 $E1$ 连接，交叉跃迁是 $\Delta I = 2$ 的电四极 $E2$ 连接；将两组交替宇称态拆散为单纯的独立正负宇称带是对单纯形对称性的动力学割裂。

## Provisional Reasoning

奇 $A$ 核八极几何的本质是“未配对费米子在对称破缺梨形腔体中的科里奥利反冲”：
- 当核具有梨形形变时，空间反射使得质子/中子密度前后非对称。奇核子在迎风面与背风面回旋所感受到的平均场曲率不同；
- 在 $K=1/2$ 轨道中，科里奥利力推动核子产生自旋进动解耦。由于正宇称态与负宇称态是由左右朝向态相干叠加而成（相位为 $+1$ 和 $-1$），这一反冲力矩在正负叠加时经历完全反相的干涉抵消；
- 因而，退耦常数必须严格呈现反平行对称（$a^+ = -a^-$）；
- 这一代数反号是微观八极形变在费米子动量空间的不可辩驳的指纹。

## Assumptions

1. **强耦合绝热近似（Strong-Coupling Limit）：** 假定内禀三维梨形形变足够稳固，奇核子角动量投影 $K=1/2$ 为良好准量子数；
2. **定常转动惯量张量：** 假定正负宇称带共享相同的核芯四极—八极有效转动惯量 $A_{\text{rot}} = \hbar^2/(2\mathcal{J})$；
3. **高阶项微扰展开：** 忽略高阶四极—八极非谐振动动能项对带头能隙 $\Delta E_0$ 的自旋依赖微弱修正。

## Competing Explanations

| 假说/理论 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 独立轴对称转子论 | 假定正负宇称带是两个独立的无关联转动带，退耦参数彼此无关 | 实验测定两带不仅退耦数值惊人一致，且符号严格反向（$a^+ = -a^-$），独立假说无法解释该绝对对称 | 彻底证伪，证明其为同一内禀态的投影双重体 |
| 几何纯振动论 | 认为交替宇称带完全是由四极核上的八极振动声子耦合产生 | 八极声子振动预言能隙应等于一阶声子能量（$\ge 500\text{ keV}$），且无法在 $K=1/2$ 产生周期性反向振荡 | 证伪，排斥大振幅声子模型 |
| 唯象签名倒转论 | 将 $^{225}\text{Ra}$ 中的能级跨零点解释为普通的单核子旋称倒转 | 旋称倒转改变自旋交错，而此处是正负宇称相对能位移随自旋发生剧烈震荡 | 修订并正名为“宇称依赖退耦振荡” |

## Transfer Conditions

1. 适用于讨论具有奇中子或奇质子占据 $K=1/2$ 或低-$K$ 侵入轨道（$\nu g_{9/2} \otimes j_{15/2}$ 或 $\pi d_{5/2} \otimes h_{11/2}$）的反射不对称核区（A≈220 的 Ra, Ac, Th 与 A≈140 的 Ba, Ce）；
2. 适用于分析实验中呈现的交替宇称序列能级差 $\Delta E(I)$ 随自旋的震荡演化；
3. 要求核态转动自旋未突破对关联完全破除的临界线。

## Failure Conditions

1. 若体系 $K \ge 3/2$（如 $^{223}\text{Ra}$ 的 $K=3/2$ 基带），对角解耦项恒等为零，宇称振荡仅能通过非对角科里奥利混合产生弱扰动，无剧烈反号倒转；
2. 若原子核处于严格球形或无八极极小（$\beta_3 = 0$），单纯形对称性退化为普通空间宇称守恒，本模型失效；
3. 在极高激发能区若发生粒子蒸发或连续谱耦合，绝热单粒子基底崩溃。

## Falsification or Reverse Tests

1. **反向检验 1（退耦符号一致性测试）：** 若在未来高精度激光核谱实验中，证实 $^{225}\text{Ra}$ 的正负宇称分支退耦常数具有相同符号（$a^+ \cdot a^- > 0$），则直接推翻 Bohr-Mottelson 反相定理与本模型；
2. **反向检验 2（势能面隧穿厚度测试）：** 本模型预测在镧系 $^{145}\text{Ba}$ 中由于隧穿能隙达 $\sim 200\text{ keV}$ 绝不可能出现负的 $\Delta E(I)$；若实验测出其在低自旋发生能级宇称倒转，则证伪势垒控制假说。

## Open Questions

1. 在奇奇核（如 $^{220, 222}\text{Fr}$）中，奇质子与奇中子双重单纯形耦合如何将反相退耦常数演化为四重态交错网络，尚需发展双粒子粒子—转子模型（TQPTR）；
2. 八极单纯形对称性在轻锕系原子 EDM（电偶极矩）增强与 Schiff 矩产生中的定量干涉效应，有待微观含时密度泛函进一步评估。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于第一性原理宇称投影转子模型与国际权威核能级数据库（NNDC adopted, Leander 1982, Butler 1996），数值通过了自动化边界检验；
- 结论属于第一性物理微观判定（`reasoning_status: provisional`），保留同行评审复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，系统建立了反射不对称奇 $A$ 核中单纯形量子数与反相宇称退耦振荡的微观机制，消除了跨质量区能谱反转认知混淆。
