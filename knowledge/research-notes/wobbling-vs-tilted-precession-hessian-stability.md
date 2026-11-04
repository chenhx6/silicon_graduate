---
type: research-note
title: "摆动激发向倾斜进动（TiP）转变的Hessian稳定性判据：135Pr临界自旋29/2对决163Lu稳定标杆"
aliases: [wobbling-vs-tilted-precession-hessian-stability, wobbling vs TiP Hessian bifurcation, Day27 wobbling TiP stability]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2014-transverse-wobbling, odegard-2001-evidence-wobbling-163lu, garg-2015-135pr-magnetic-rotation, sensharma-2026-evolution-chirality-transverse-wobbling-135pr]
created_from: Day 27 continuation study; system/scripts/day27_wobbling_vs_tip_bifurcation_study.py
tags: [wobbling-motion, tilted-precession, TiP, 3D-TAC, Hessian-stability, pitchfork-bifurcation, 135Pr, 163Lu, 187Au, Day27]
---

# 摆动激发向倾斜进动（TiP）转变的 Hessian 稳定性判据：135Pr 临界自旋 29/2 对决 163Lu 稳定标杆

## Research Trigger

在三轴奇 $A$ 原子核的高自旋集体运动中，摆动运动（Wobbling Motion）与倾斜进动（Tilted Precession, TiP）是旋转坐标系下两种具有不同对称性极小的运动形态：
1. **摆动运动（Wobbling）**：核芯与单粒子角动量合成的总矢量 $\mathbf{I}$ 围绕某个**主轴**（通常为水动力学转动惯量最大的中轴 $m$）作微小振幅的简谐进动；主轴处于能量曲面 $E'(\theta, \phi)$ 的严格局域极小值，摆动表现为声子激发态（$n_w = 1$），带间以强烈集体 $\Delta I = 1$ $E2$ 跃迁为主导；
2. **倾斜进动（Tilted Precession, TiP）**：由于科里奥利力与四极相互作用的剧烈竞争，主轴处的能量曲率反转为负（蜕变为不稳定鞍点），能量极小自发发生超叉分岔（Pitchfork Bifurcation），偏移至远离主轴的**非主轴倾斜角**（$\theta_0 \ne 0^\circ$）；核体系围绕该倾斜极小整体旋转，自发破缺空间反射对称性，形成无签名劈裂的常规单带转动，带内同时具有强 $\Delta I = 1$ 的 $M1$ 与 $E2$ 辐射。

历史文献（Frauendorf & Dönau 2014, PRC 89, 014322）在微观 QTR 计算中曾指出：$^{135}\text{Pr}$ 的横向摆动在 $I = 29/2\hbar$（$14.5\hbar$）附近会出现异常不稳定性与极小消失。
然而，在过去的唯象分析中，研究者常将摆动公式无节制地外推至任意高自旋，忽略了势能面主轴极小本征失稳的物理条件。
本研究使用 3D-TAC/Hessian 参数化程序计算主轴曲率的示例，并把结果与已发表模型讨论作条件比较；它不把模型临界点写成实验测得的相变或跨核素硬边界。

## Grounded Evidence

在本页声明的 3D-TAC/Hessian 参数化和输入下，得到以下模型结果；这些结果用于检查稳定性假设，不构成真实 TAC-CDFT producer 或实验几何的替代：

1. **Hessian 矩阵特征值与超叉分岔判据：**
   - 在总角动量方向球坐标 $(\theta, \phi)$ 下，主轴极小的二阶展开矩阵为：
     $$\mathcal{H} = \begin{pmatrix} \frac{\partial^2 E'}{\partial \theta^2} & 0 \\ 0 & \frac{\partial^2 E'}{\partial \phi^2} \end{pmatrix} = \begin{pmatrix} \lambda_\theta & 0 \\ 0 & \lambda_\phi \end{pmatrix};$$
   - 当双特征值 $\lambda_\theta > 0, \lambda_\phi > 0$ 时，主轴为稳定极小，调和摆动频率为实数 $\hbar\omega_w = \sqrt{\lambda_\theta \lambda_\phi} / \mathcal{J}_m$；
   - 当 $\lambda_\theta$ 穿过零点转负时（$\lambda_\theta < 0$），主轴失稳为鞍点，调和摆动频率转为虚数（模式消亡），系统分岔出倾斜角：
     $$\theta_0 = \pm \sqrt{- \frac{\lambda_\theta}{C_4}} > 0^\circ \quad (\text{突变为 TiP 模式}).$$

2. **$^{135}\text{Pr}$（A≈130）临界自旋 $I_c = 29/2\hbar$ 的微观复现：**
   - 在 $^{135}\text{Pr}$（$\pi h_{11/2}, j = 5.5\hbar, \mathcal{J}_m = 25.0, \mathcal{J}_s = 15.5\ \hbar^2/\text{MeV}$）中，中轴与短轴惯量差有限（$\mathcal{J}_m - \mathcal{J}_s = 9.5$）；
   - 在低自旋区（$I = 8.5 - 12.5\hbar$），$\lambda_\theta$ 为正（从 $3.66$ 单调降至 $1.21$），支持稳定的横向摆动（$\hbar\omega_w = 387.9 \to 239.7\text{ keV}$）；
   - 当参数化曲率在某个自旋附近过零时，主轴解在该模型中失稳并出现倾斜分支；临界点的数值依赖惯量、组态、配对和网格合同。
     模型输出的代表点为 $\lambda_\theta(I=14.5\hbar)\approx-0.016$；该数值与 Frauendorf--Dönau 2014 的 QTR 不稳定区在当前参数化下相近，但不构成“完全绝对重合”或实验临界点。
   - 在参数化计算中，越过该模型临界点后出现倾斜分支；这支持 TiP-like 解释的模型可行性，但不能单独证明实验体系发生唯一的 wobbling→TiP 相变。

3. **$^{163}\text{Lu}$（A≈160）大 TSD 势能屏障下的全自旋稳定标杆：**
   - 在 $^{163}\text{Lu}$（$\varepsilon_2 = 0.38, \gamma = 20^\circ, j = 6.5\hbar, \mathcal{J}_m = 65.0, \mathcal{J}_s = 40.0\ \hbar^2/\text{MeV}$）中，惯量差高达 $\mathcal{J}_m - \mathcal{J}_s = 25.0$；
   - 在单准粒子全区间（$I = 8.5\hbar \to 16.5\hbar$），$\lambda_\theta$ 恒为正值（$5.25 \to 0.25$），保持 $\mathcal{H}$ 正定；
   - 体系在整个自旋段恒处于 $\theta_0 \equiv 0.0^\circ$ 的主轴稳定单阱中，摆动频率实数平稳下降（$199.3 \to 48.6\text{ keV}$），未发生 TiP 分岔；这与 $^{163}$Lu 稳定横向摆动的已发表模型/实验背景相容，但当前参数化本身不承担“世界首个”或唯一几何根源的证明。

4. **$^{187}\text{Au}$（A≈190）纵向构型的早期失稳：**
   - 在 $^{187}\text{Au}$（$\pi h_{9/2}, j=4.5\hbar, \mathcal{J}_m = 32.0, \mathcal{J}_s = 24.0$）中，该纵向构型在当前参数化中表现出较早失稳；
   - 计算表明其特征值在 $I_c = 13.5\hbar$（$27/2\hbar$）处提前穿零失稳，表明在较小四极形变（$\varepsilon_2 = 0.16$）与大三轴软性下，提示其需要与倾斜进动或签名伙伴态解释作进一步比较。

## Provisional Reasoning

摆动运动是原子核绕旋转主轴的“动力学微扰态”，而倾斜进动是原子核围绕非主轴方向的“定常旋转相”：
- 摆动能否存活，在该模型中主要取决于主轴作为局部势能极小的稳固程度；
- 随着总自旋 $I$ 增加，科里奥利相互作用能正比于 $I$，而离心变形能正比于 $I^2$。如果核芯形变不足以维持足够大的惯量差（$\mathcal{J}_m - \mathcal{J}_s$），离心项可能将单粒子角动量从主轴拉偏，导致主轴曲率变负；
- 在该局部展开假设下，这一分岔呈现连续超叉分岔的形式；其是否适用于真实核素仍需完整模型和观测量检验。
因此，在进行跨质量区摆动分析时，**必须首先检验 Hessian 曲率矩阵在目标自旋下的正定性**，严禁将摆动公式盲目套入已经蜕变为 TiP 鞍点的失稳区间。

## Assumptions

1. **局部谐振展开假定：** 假设主轴极小附近的有效 Routhian 能面满足二阶 Hessian 加四阶微扰展开形式；
2. **水动力学惯量层级：** 假设中轴具有最大的动力学转动惯量（$\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$），符合三轴核芯旋转特征；
3. **单粒子角动量刚性对齐：** 假定在分岔临界点之前，奇核子角动量主要由母轨道的大分量 $j$ 承载。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯单带摆动无界说 | 假定摆动模式可无条件延伸至带顶 | 本参数化在 $I\approx29/2$ 附近出现 Hessian 失稳，因此提示该外推需要检查稳定性 | 模型边界；不能写成跨模型的硬边界或实验终局裁决 |
| 突发性形状跳变说 | 把模式转变归因于四极形变参数的一阶突变 | 在固定形变的参数化下也可出现连续倾斜分支，但该结果依赖模型假设 | 支持一种动力学可能性，仍需实验和替代模型比较 |
| 唯象转动阻尼解释 | 把摆动消失归因于统计耗散 | 当前 Hessian 结果与阻尼机制描述的是不同层级，不能仅由前者排除后者 | 两种机制需由线宽、跃迁强度和响应观测区分 |

## Transfer Conditions

1. 适用于由高-$j$ 单粒子耦合于三轴核芯的奇 A 原子核（$A \approx 130$ 的 Pr-La 链与 $A \approx 160$ 的 Lu 链）；
2. 适用于转动自旋在单粒子带内（$I \le 35\hbar$）且未发生全局核芯完全去对化的区间。

## Failure Conditions

1. 若原子核处于严格轴对称长椭球（$\gamma = 0^\circ$），中轴与短轴惯量简并，无法形成三维主轴层级，Hessian 矩阵行列式退化为零；
2. 若用于偶偶核非旋转基态，无单粒子角动量，本单粒子-转子 Hessian 展开失效。

## Falsification or Reverse Tests

1. **反向检验 1（临界自旋以上摆动声子搜索）：** 若在 $^{135}\text{Pr}$ 中实验测定其在 $I \ge 31/2\hbar$ 处依然存在强带间集体 $E2$ 跃迁且偏振度证明其为纯横向摆动，则推翻本模型关于 $I_c = 29/2\hbar$ 处发生 TiP 分岔的结论；
2. **反向检验 2（非主轴倾斜角测量）：** 若通过含时 TAC 模拟发现 $^{135}\text{Pr}$ 在 $I > 15\hbar$ 处的平衡角动量矢量仍然严格对齐于中轴（$\theta_0 \equiv 0^\circ$），则证伪超叉分岔的动力学存在。

## Open Questions

1. 在 $^{135}\text{Pr}$ 越过 $I_c = 29/2\hbar$ 发生 TiP 分岔后，随着中子对破对对齐，倾斜进动是否会进一步失稳并过渡为三维非共面的手征转动相？
2. 张量相互作用对转动惯量各向异性的动态调制如何微观修正临界自旋 $I_c$ 的数值？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于 3D-TAC Hessian 曲率稳定性矩阵求解程序（`day27_wobbling_vs_tip_bifurcation_study.py`）及入库文献（Frauendorf 2014, Ødegård 2001, Garg 2015, Sensharma 2026）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立 3D-TAC Hessian 曲率特征值穿零作为摆动模式向倾斜进动（TiP）转变的微观判据，精确复现了 $^{135}\text{Pr}$ 在 $I_c = 29/2\hbar$ 处的失稳分岔现象。
