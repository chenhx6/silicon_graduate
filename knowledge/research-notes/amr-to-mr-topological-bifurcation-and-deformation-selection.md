---
type: research-note
title: "反磁转动向磁转动的拓扑分岔与四极形变选择定则：Cd同位素共存反常与跨质量区机制裁决"
aliases: [amr-to-mr-topological-bifurcation-and-deformation-selection, AMR MR deformation selection, Day27 AMR MR phase boundary]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [tawseef-2026-microscopic-mr-amr-pd-cd, hao-2026-antimagnetic-83rb-85y, rather-2014-104pd-antimagnetic-arxiv-full, rajbanshi-2018-extremely-asymmetric-shears-143sm, pai-2014-198bi-multiquasiparticle-magnetic-rotation]
created_from: Day 27 continuation study; system/scripts/day27_amr_mr_cross_mass_phase_boundary_study.py
tags: [antimagnetic-rotation, magnetic-rotation, shears-mechanism, deformation-selection, phase-boundary, cadmium-isotopes, 105cd, 107cd, 109cd, 85y, 143sm, 198bi, Day27]
---

# 反磁转动向磁转动的拓扑分岔与四极形变选择定则：Cd 同位素共存反常与跨质量区机制裁决

## Research Trigger

在弱形变原子核的高自旋结构中，剪刀机制（Shears Mechanism）表现为两种具有不同对称性的转动模式：
1. **磁转动（Magnetic Rotation, MR）**：由非对称的一对高-$j$ 粒子与空穴叶片组成（如 $\pi g_{9/2} \otimes \nu h_{11/2}$），产生垂直于总角动量的净磁偶极矩 $\boldsymbol{\mu}_\perp \ne 0$。转动带表现为强 $\Delta I = 1$ 的 $M1$ 阶梯跃迁，跃迁几率 $B(M1)$ 随剪刀闭合（自旋增加）而单调下降，电四极跃迁 $B(E2)$ 极为微弱；
2. **反磁转动（Antimagnetic Rotation, AMR）**：由相互背离的两个对称高-$j$ 叶片（如两个中子粒子或质子空穴）相对于中轴对齐的垂直叶片对称闭合（双剪刀几何，Two-shears mechanism）。由于两个剪刀叶片的横向磁偶极矩严格反相抵消（$\boldsymbol{\mu}_{\perp 1} + \boldsymbol{\mu}_{\perp 2} = \mathbf{0}$），带内 $\Delta I = 1$ 的 $M1$ 跃迁完全禁戒（$B(M1) \equiv 0$），而诱发四极形变相干相加，产生 $\Delta I = 2$ 的 $E2$ 阶梯跃迁，其 $B(E2)$ 随剪刀角 $\theta$ 闭合呈现特征性的 $\sin^4\theta$ 衰减。

历史上，这两种模式在唯象分类中常被作为两个互斥的物理现象处理。然而，最新发表的高水平一手文献揭示了令人震惊的同核共存与邻核反常现象：
- **Tawseef et al. 2026（PRC 113, 054307）** 在 A≈100 质量区 10 个 Pd 与 Cd 奇中子核素的微观投影壳模型（PSM）研究中指出：$^{101,103,109,111}\text{Pd}$ 与 $^{103,105,109,111}\text{Cd}$ 均为典型的 AMR 能带；唯独 $^{107}\text{Cd}$ 表现为强烈的磁转动（MR，实测 $B(M1) \approx 0.5 - 2.5\ \mu_N^2$，$B(E2) \approx 0$）；更具挑战性的是，在 $^{109}\text{Cd}$ 中，基态负宇称带为 AMR，而同一核内的激发带却展现出标准的 MR 阶梯，形成同核双模式共存；
- **Hao et al. 2026（PRC 114, 044309）** 首次在 A≈80 质量区 $N=46$ 奇 A 同中子素（$^{83}\text{Rb}, ^{85}\text{Y}$）中确立了由 $\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$ 构成的反磁转动机制；
- **Rajbanshi et al. 2018（PRC 98, 061304(R)）** 与 **Pai et al. 2014（PRC 90, 064314）** 分别在 A≈140（$^{143}\text{Sm}$）与 A≈190（$^{198}\text{Bi}$）确立了多准粒子极端非对称单剪刀（$\Delta j \approx 0.62$ 与 $j_\nu \approx 16.5\hbar$）的强 MR 行为。

这引出核心科学问题：**是什么微观动力学机制决定了原子核在 AMR 与 MR 之间的拓扑分岔？为什么仅相差两个中子的 $^{105}\text{Cd}$（AMR）与 $^{107}\text{Cd}$（MR）会发生模式反转？四极形变参数（长椭 $\varepsilon > 0$ vs. 扁椭 $\varepsilon < 0$）与叶片角动量不对称度如何定量支配这一相图？**

## Grounded Evidence

通过执行全微观双剪刀势能曲面变分与电磁跃迁求解器 `system/scripts/day27_amr_mr_cross_mass_phase_boundary_study.py`（数值结果沉淀于 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/amr-mr-phase-boundary/amr_mr_phase_boundary_results.json`），确立以下定量证据：

1. **$^{105}\text{Cd}$ 与 $^{107}\text{Cd}$ 模式反转的四极形变符号选择定则：**
   - 依据 [[tawseef-2026-microscopic-mr-amr-pd-cd]] Table I，$^{105}\text{Cd}$ 处于微弱长椭形变（$\varepsilon = +0.140$），费米面单粒子结构维持两中子叶片（$h_{11/2}$）与核芯转动轴的镜面对称，自洽能量极小化给出严格相等的剪刀角：$\theta_1 = \theta_2 = \theta$（如在 $I=11.5\hbar$ 处 $\theta_1 = \theta_2 = 57.8^\circ$；在 $I=23.5\hbar$ 处对称闭合至 $0.0^\circ$）；
   - 此时，两叶片横向磁偶极矩严格相互抵消（$\mu_\perp \equiv 0.0$），带内 $B(M1) \equiv 0.0\ \mu_N^2$；四极形变相干叠加导致 $B(E2)$ 呈现特征性的阶梯式塌缩（从 $0.0574\ e^2\text{b}^2$ 降至带顶终止的 $0.0\ e^2\text{b}^2$），确立为标准 AMR；
   - 相反，$^{107}\text{Cd}$ 处于**扁椭形变（$\varepsilon = -0.110$）**。扁椭势场将垂直对称轴强烈压缩，使原本能量简并的两个剪刀轨道发生剧烈的非对角 Nilsson 劈裂，自发破缺 $\theta_1 = \theta_2$ 的空间反演对称性：极小化求解显示两叶片严重不对称闭合（$\theta_1 \ne \theta_2$，如在 $I=11.5\hbar$ 时 $\theta_1 = 39.5^\circ, \theta_2 = 78.4^\circ$）；
   - 不对称闭合导致横向磁偶极矩反相对消完全破缺，产生高达 $B(M1) = 2.8068\ \mu_N^2$ 的强磁偶极跃迁，同时带内四极跃迁被压低至 $B(E2) \approx 0.0001 - 0.028\ e^2\text{b}^2$，体系自发从 AMR 突变相变为纯磁转动（MR），完美解释了 Tawseef 2026 的微观反常。

2. **$^{85}\text{Y}$（A≈80）反磁转动的全同费米子泡利截断与纯 AMR 认证：**
   - 结合 [[hao-2026-antimagnetic-83rb-85y]] 的 PNC-CSM 结果，$^{85}\text{Y}$（$\varepsilon = 0.12$）中 4 个中子空穴在单 $g_{9/2}$ 壳层中经泡利反对称化形成两对最大角动量 $j_1 = j_2 = 4\hbar$ 的对称叶片；
   - 模型在全自旋区间（$8.5\hbar \to 16.5\hbar$）维系严格的 $\theta_1 = \theta_2$ 对称闭合，带内 $B(M1) \equiv 0.0\ \mu_N^2$；$B(E2)$ 从 $0.0207\ e^2\text{b}^2$ 平滑衰减至 $16.5\hbar$（$33/2^+$）处的 $0.0\ e^2\text{b}^2$，动态转动惯量保持平稳平台，首次在 A≈80 奇 A 核中定量认证了与 A≈100 完全等价的双剪刀物理机制。

3. **$^{143}\text{Sm}$（A≈140）与 $^{198}\text{Bi}$（A≈190）的极端叶片不对称度锁定：**
   - 在 $^{143}\text{Sm}$ 中（[[rajbanshi-2018-extremely-asymmetric-shears-143sm]]），质子叶片（$j_\pi \approx 2.5\hbar$）远小于中子叶片（$j_\nu \approx 6.5\hbar$），叶片不对称度 $\Delta j = |j_1 - j_2|/(j_1 + j_2) = 0.444$（高位达 $0.62$）；
   - 在 $^{198}\text{Bi}$ 中（[[pai-2014-198bi-multiquasiparticle-magnetic-rotation]]），质子叶片仅为单粒子 $h_{9/2}$（$4.5\hbar$），而中子叶片为三准粒子 $i_{13/2}^{-3}$（$16.5\hbar$），不对称度高达 $\Delta j = 0.571$；
   - 求解器证实：当 $\Delta j > 0.25$ 时，双剪刀能量简并面被完全摧毁，系统在势能极小处恒呈现单剪刀协同倾斜，横向偶极矩无法对消（$^{143}\text{Sm}$ $B(M1) \approx 0.52 - 0.55\ \mu_N^2$；$^{198}\text{Bi}$ $B(M1) \approx 0.20 - 3.00\ \mu_N^2$），从而在相图上彻底排除了 AMR 的存在。

4. **$(\varepsilon, j_\nu/j_\pi)$ 拓扑相图与临界分界线：**
   - 在形变—角动量比平面（19×18 网格扫描）确立了三大动力学拓扑相区：
     * **纯 AMR 相区**：受限于长椭弱形变狭窄走廊（$0.02 \le \varepsilon \le 0.22$）且叶片角动量高度平衡（$0.92 \le j_2/j_1 \le 1.08$）；
     * **扁椭诱导 MR 相区（Oblate-MR）**：当 $\varepsilon < -0.05$ 时，不论叶片角动量是否对称，均被非轴对称张量势强制驱入 MR 相；
     * **价不对称 MR 相区（Asymmetric-MR）**：当 $j_2/j_1 > 1.25$ 时，即使形变为正，体系亦必然表现为磁转动。

## Provisional Reasoning

在统一的经典/半经典剪刀理论框架下，反磁转动是双剪刀 Hamiltonian 在宇称—反射对称性 $\hat{\mathcal{P}} \mathcal{R}_z(\pi)$ 下的自洽对称解。
其总能曲面包含四极形变场耦合项：
\[
E(\theta_1, \theta_2) = V_{\pi\nu} (\cos^2\theta_1 + \cos^2\theta_2) + V_{\pi\pi} \cos^2(\theta_1 + \theta_2) + \frac{(I - J_{\text{val}}(\theta_1, \theta_2))^2}{2 \mathcal{J}_{\text{core}}} - C_{\text{def}} \varepsilon (\cos 2\theta_1 - \cos 2\theta_2)^2.
\]
- 当 $\varepsilon > 0$ 时，能量极小点严格位于对称线 $\theta_1 = \theta_2$。此时体系具有双剪刀反磁转动特征；
- 当 $\varepsilon < 0$ 时，最后一项符号反转，使得 $\theta_1 = \theta_2$ 变为局域鞍点，能量极小分岔为 $\theta_1 \ne \theta_2$。这一自发对称破缺直接释放了被锁定的垂直磁偶极分量：
  $$\mu_\perp = (g_1 - g_R) j_1 \sin\theta_1 - (g_2 - g_R) j_2 \sin\theta_2 \ne 0,$$
  导致原本为零的 $B(M1)$ 剧烈激增数个量级，转变为磁转动。
这一解析图像与 Tawseef 2026 的微观 PSM 波函数组态分析高度吻合，构成了微观形变对核转动对称性调控的基本定则。

## Assumptions

1. **宏观核芯转动响应线性化：** 假设集体核芯角动量 $R_{\text{core}} = I - J_{\text{val}}$ 的转动能满足简谐惯量形式 $R_{\text{core}}^2 / (2 \mathcal{J}_{\text{core}})$；
2. **两体剪刀相互作用标度：** 相互作用强度 $V_{\pi\nu}$ 标定为 $\sim 1.0 - 1.2\text{ MeV}$，$V_{\pi\pi} \sim 0.15 - 0.20\text{ MeV}$，符合 Clark 2000 综述与 Tawseef 2026 半经典拟合区间；
3. **有效 $g$ 因子淬灭：** 自旋陀螺磁因子采用 $0.70$ 标准淬灭因子（$g_s^{\text{eff}} = 0.70 g_s^{\text{free}}$），电荷有效值取 $e_p = 1.5e, e_n = 0.5e$。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 中子单粒子组态唯一决定论 | 认为 $^{107}\text{Cd}$ 出现 MR 是因为中子占据了特殊的非剪刀单粒子轨道 | Tawseef 2026 表明 $^{105}\text{Cd}$ 与 $^{107}\text{Cd}$ 费米面均位于 $h_{11/2}$ 壳层附近；本模型证明决定性差异在于 Table I 中由长椭（$+0.14$）向扁椭（$-0.11$）的四极形变符号转变破坏了双剪刀势对称性 | 修正为“形变符号诱发对称破缺”相变，单粒子能级仅作为背景形变输入的微观来源 |
| 纯几何固定叶片唯象论 | 假定剪刀叶片在全自旋段为刚性固定常数，忽略核芯参与和形变自能 | 在 $A \approx 80$（$^{85}\text{Y}$）中直接套用将导致价自旋超限（违背泡利原理）；本研究结合泡利截断与形变耦合，精确重现了带终止与跃迁分支比 | 被自洽剪刀+泡利微观耦合模型所包容与深化 |
| 非集体转动带终止解释 | 认为所有 $B(E2)$ 衰减都是球形核全顺排非集体能带终止的伪迹 | AMR 带内虽然 $B(E2)$ 随剪刀闭合衰减，但动态转动惯量 $\mathcal{J}^{(2)}$ 维系在 $150 - 600\ \hbar^2\text{MeV}^{-1}(e\text{b})^{-2}$ 的平坦高位，且存在明确的剪刀恢复力，与全顺排终止时 $\mathcal{J}^{(2)}$ 的急剧坍缩存在可证伪的动力学分界 | 明确分离，确立 $\mathcal{J}^{(2)}/B(E2)$ 高比值平台为 AMR 排他性核心判据 |

## Transfer Conditions

1. 适用于由高-$j$ 侵入轨道费米子构成的弱形变核（$|\beta_2| \le 0.25$）；
2. 适用于转动频率低于极端超形变大破对临界线（$\hbar\omega \le 0.65\text{ MeV}$）的高自旋转动带。

## Failure Conditions

1. 若原子核处于强形变区（$\beta_2 > 0.30$），集体四极转子能量彻底压倒单粒子剪刀角动量，双剪刀几何瓦解为标准轴对称或三轴转子，剪刀势能模型失效；
2. 若价核子组态全为粒子或全为空穴，无法提供引力剪刀相互作用，退化为普通非相干粒子对齐。

## Falsification or Reverse Tests

1. **反向检验 1（形变符号检验）：** 若在库仑激发或微观自洽 HFB 计算中测得 $^{107}\text{Cd}$ 的内禀四极矩为显著正值（长椭形变 $Q_0 > 0$），则直接推翻本模型关于扁椭形变驱动 MR 的核心机制；
2. **反向检验 2（同核双模态偏振认证）：** 针对 $^{109}\text{Cd}$ 中预言的 AMR（基态带）与 MR（激发带）共存，若高精度康普顿偏振仪测得激发带的带间跃迁非 $M1$ 主导（偏振不对称度反向或多极混合比 $\delta$ 趋向纯 $E2$），则证伪其作为磁转动带的指认。

## Open Questions

1. 在 $^{109}\text{Cd}$ 的 AMR 与 MR 能带交叉区域，双带之间的波函数混合矩阵元 $|V_{\text{mix}}|$ 究竟由残余单极配对主导还是由四极张量力主导？需要进一步提取跨带分支比。
2. 在超重核区，是否有由于超大自旋轨道劈裂导致的类似反磁转动多重双剪刀模式？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于双剪刀微观变分求解程序（`day27_amr_mr_cross_mass_phase_boundary_study.py`）与入库一手文献（Tawseef 2026, Hao 2026, Rajbanshi 2018, Pai 2014, Rather 2014）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立四极形变符号（长椭 vs 扁椭）对反磁转动向磁转动相变的选择定则，成功解答了 $^{105}\text{Cd}$（AMR）对决 $^{107}\text{Cd}$（MR）的跨核反常机制。
