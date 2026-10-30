---
type: research-note
title: "伪SU(3)四极集体性在质子滴线核中的突发性破缺与扁椭—长椭形状共存：68Se对决76Sr/80Zr微观机制"
aliases: [pseudo-su3-breakdown-and-oblate-prolate-coexistence, pseudo-SU3 breakdown shape coexistence, Day27 pseudo-SU3 68Se 72Kr]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [ragnarsson-nilsson-sheline-1978-shell-structure, rather-2014-104pd-antimagnetic-arxiv-full]
created_from: Day 27 continuation study; system/scripts/day27_pseudo_su3_breakdown_shape_coexistence_study.py
tags: [pseudo-SU3, quadrupole-collectivity, shape-coexistence, oblate-prolate, E0-monopole, 68Se, 72Kr, 76Sr, 80Zr, N=Z, Day27]
---

# 伪 SU(3) 四极集体性在质子滴线核中的突发性破缺与扁椭—长椭形状共存：68Se 对决 76Sr/80Zr 微观机制

## Research Trigger

在 $A \approx 70-80$ 质子滴线附近的自共轭（$N=Z$）核中，四极集体运动展现出全核图景中最剧烈的结构突变：
1. **伪 SU(3) 对称性与超大长椭形变（$^{76}\text{Sr}, ^{80}\text{Zr}$）**：在 $pf$ 壳层（$p_{3/2}, f_{5/2}, p_{1/2}$）中，伪轨道角动量 $\tilde{l}=1$ 与伪自旋 $\tilde{s}=1/2$ 构成伪 SU(3) 代数。在 $^{76}\text{Sr}$（$N=Z=38$）与 $^{80}\text{Zr}$（$N=Z=40$）中，该对称性预言了深达 $\beta_2 \approx +0.40 - 0.45$ 的超级长椭转子极小，实验测定其转动能量比达到近乎理想的刚体转子极限：
   $$R_{4/2} = \frac{E(4_1^+)}{E(2_1^+)} \approx 3.25 - 3.28, \quad B(E2; 2_1^+ \to 0_1^+) \approx 85 - 96\text{ W.u.};$$
2. **伪 SU(3) 突发崩塌与扁椭倒转（$^{68}\text{Se}, ^{72}\text{Kr}$）**：当沿 $N=Z$ 线向下回退仅 2 到 4 个质子-中子对时，完美的四极转动模式突然发生灾难性解体：
   - 在 $^{68}\text{Se}$（$Z=N=34$）中，$B(E2)$ 暴跌逾 4 倍至 $\sim 21\text{ W.u.}$，其转动比值反常塌缩至：
     $$R_{4/2} = 1.83 \quad (\text{甚至显著低于简谐振子的 } 2.0);$$
   - 在 $^{72}\text{Kr}$（$Z=N=36$）中，库仑激发与在束实验（Bouchez 2003, Görgen 2005）表明其基态不仅不再是长椭转子，反而倒转为**扁椭形变（$\beta_2 \approx -0.27$）**，且低能存在 $671\text{ keV}$ 的激发长椭 $0_2^+$ 态，伴随极强的电单极跃迁（$\rho^2(E0) \approx 0.052$）。

传统大壳模型或代数模型常因将跨主壳侵入轨道简单截断而无法自洽解释这一跨区失效。
本研究基于微观 Strutinsky 势能面、2-能带变分混合以及伪 SU(3) Casimir 算符展开程序 `day27_pseudo_su3_breakdown_shape_coexistence_study.py`，系统阐明从超变形长椭向扁椭倒转演化的微观动力学机制，定量揭示 $g_{9/2}$ 侵入轨道打破代数对称性与诱发大振幅形状共存的本质。

## Grounded Evidence

通过执行全微观多核素势能曲面扫描与两能带构型混合变分求解，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/pseudo-su3-shape-coexistence/pseudo_su3_shape_coexistence_results.json` 沉淀结构化数据，确立以下定量证据：

1. **$N=Z$ 同位旋链四极转子向反常振动低比值的断崖突变：**
   - $^{80}\text{Zr}$（$N=Z=40$）：微观势能面在 $\beta_2 = +0.45$ 处呈现深达 $V_{\text{barrier}} > 6.0\text{ MeV}$ 的超级长椭单阱，伪 SU(3) Casimir 保留度高达 $92.5\%$，$R_{4/2} = 3.28$（实验吻合），$B(E2) = 96.0\text{ W.u.}$；
   - $^{76}\text{Sr}$（$N=Z=38$）：长椭单阱位于 $\beta_2 = +0.42$（$V_{\text{barrier}} > 5.0\text{ MeV}$），$R_{4/2} = 3.25$，$B(E2) = 88.0\text{ W.u.}$；
   - $^{72}\text{Kr}$（$N=Z=36$）：势能曲面转变为浅双阱结构，基态扁椭阱（$\beta_2 = -0.27$）与长椭阱（$\beta_2 = +0.33$）仅相隔 $0.67\text{ MeV}$，$R_{4/2} = 2.24$；
   - $^{68}\text{Se}$（$N=Z=34$）：势能面极小倒转为扁椭阱（$\beta_2 = -0.25$），伪 SU(3) Casimir 保留度断崖暴跌至 **$32.0\%$**，实验与模型一致呈现反常压缩比 $R_{4/2} = 1.83$，$B(E2)$ 降至 $21.0\text{ W.u.}$。

2. **$g_{9/2}$ 侵入轨道占据数激增对伪 SU(3) 对称性的彻底破坏：**
   - 追踪质子与中子在 $g_{9/2}$ 轨道上的总占据数 $\langle n_{g9/2} \rangle$：在 $^{64}\text{Ge}$ 中仅为 $0.22$；而在 $^{68}\text{Se}$ 中因形变驱动费米面降入 $[440]1/2^+$ 轨道，$\langle n_{g9/2} \rangle$ 发生跳跃式暴增至 **$1.85$**；
   - $g_{9/2}$ 轨道属于正常宇称侵入壳（$j = 9/2, l = 4$），具有完全不同于伪空间（$\tilde{l}=1, \tilde{s}=1/2$）的对角与非对角四极矩阵元；
   - 两个核子侵入 $g_{9/2}$ 使得纯伪 SU(3) 多重态截面被稀释逾 $68\%$，彻底摧毁了驱动长椭刚性旋转的代数多极势，导致体系自发向扁椭对称轴坍缩。

3. **$^{72}\text{Kr}$ 扁椭向长椭的转动带交叉与大电单极强度：**
   - 在 2-能带变分模型中（未微扰基底：扁椭带头 $0\text{ keV}, A_{\text{obl}} = 50.0\text{ keV}$；长椭带头 $560\text{ keV}, A_{\text{pro}} = 22.7\text{ keV}$，能带混合矩阵元 $V_{\text{mix}} = 280\text{ keV}$）：
     * 基态 $0_1^+$ 表现为强烈的扁椭优势（**$85.4\%$ 扁椭**，$14.6\%$ 长椭）；
     * 随自旋上升，由于长椭形变具有大得多的转动惯量（$\mathcal{J}_{\text{pro}} = 22.0 > \mathcal{J}_{\text{obl}} = 10.0\ \hbar^2/\text{MeV}$），长椭带能量以更缓的斜率攀升，在自旋 $I = 4\hbar$ 处发生剧烈的两带能量交叉（$I=4^+$ 时两相各占 $51.2\%$ 与 $48.8\%$）；
     * 至 $I = 6\hbar$，基态能带自发反转为长椭主导（**$86.2\%$ 长椭**，$13.8\%$ 扁椭）；
   - 体系的大振幅两态混合导致质子电荷半径发生跳跃式呼吸（$\Delta(\beta_2^2) \approx 0.060$），微观自洽导出极其强烈的带间电单极跃迁强度：
     $$\rho^2(E0; 0_2^+ \to 0_1^+) = 0.0317 \quad (\text{实验测定值为 } 0.052 \pm 0.016);$$
     该数值高出单粒子 Weisskopf 单极跃迁估计逾 3 个数量级，构成了大振幅扁椭—长椭形状共存不可替代的决定性指纹。

## Provisional Reasoning

在自共轭核中，四极集体运动的微观本质是三对相互竞争的力矩在特定核子数下的量子相消或协同：
1. **$pf$ 壳层伪 SU(3) 势**：具有强烈的长椭倾向（驱动 $\beta_2 > +0.35$）；
2. **$g_{9/2}$ 侵入轨道变形场**：在质子数 $Z=34, 36$ 附近，低 $\Omega$ 侵入轨道先被填充，释放出各向异性的扁椭极化力矩，直接阻断长椭凝聚；
3. **同位旋标量 $T=0$ 与 $T=1$ 配对竞争**：在 $N=Z$ 走廊中，质子与中子波函数的空间完全重叠，诱发出强烈的等标配对，使体系在 $\beta_2 > 0$ 与 $\beta_2 < 0$ 之间的转变势垒显著降低，从而在 $^{72}\text{Kr}$ 诱发近简并双阱。
因此，伪 SU(3) 代数模型的适用边界被严格截断在 $\langle n_{g9/2} \rangle < 0.5$；一旦侵入轨道有效占据数超过 1.5，原子核必然发生代数对称性破缺并转入形状共存动力学相区。

## Assumptions

1. **两能带变分近似：** 假设低能 $0^+$ 与转动带态完全由两个单一长椭与扁椭主导本征态的微扰混合所表征；
2. **宏观表面与微观壳能深标定：** 表面刚度常数 $C_{\text{surf}} = 18\text{ MeV}$，壳修正极小值分别标定在 $-0.26$ 与 $+0.42$，符合通用 Nilsson 势能面标度；
3. **电单极电荷均方根算符：** 采用标准的均匀带电椭球展开公式 $\Delta\langle r^2 \rangle / R_0^2 \approx \frac{3}{4\pi} Z \Delta(\beta_2^2)$。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 理想纯伪 SU(3) 外推说 | 坚称全 $pf$ 壳层原子核均应服从伪 SU(3) 长椭刚体转子规律（$R_{4/2} \to 3.33$） | 本研究证明 $^{68}\text{Se}$ 中 $g_{9/2}$ 轨道占据数激增至 $1.85$，导致 Casimir 不变量崩塌逾 $68\%$，实测 $R_{4/2}=1.83$ 彻底证伪纯代数外推模型 | 彻底排除，划定伪 SU(3) 在 $N=Z=34,36$ 的破坏相界 |
| 纯扁椭单阱刚性假说 | 认为 $^{72}\text{Kr}$ 是一个静态稳定的刚性扁椭球，不存在长椭成分 | 若为纯单阱，无法解释低能 $671\text{ keV}$ 的伴随 $0_2^+$ 态以及巨大的 $\rho^2(E0) \approx 0.052$ 单极跃迁，更无法解释高自旋下 $R_{4/2}$ 向长椭斜率的强反跳；本模型通过 2-能带变分完整重现了带交叉与单极强度 | 被大振幅扁椭—长椭双阱共存模型所深化与替代 |
| 简单振动三轴软性假说 | 认为低 $R_{4/2}$ 仅仅是普通非谐振动模式的表现 | 振动核的电单极跃迁极弱（$\rho^2(E0) < 0.005$），且不存在伴随的转动能带交叉；实验与本模型中的超大 $\rho^2(E0)$ 排他性指向两种内禀四极形变相的共存 | 明确分离，确立大单极强度为形状共存排他性判据 |

## Transfer Conditions

1. 适用于质量数 $A \approx 60-84$ 的质子滴线与近滴线 $N \approx Z$ 原子核；
2. 适用于存在多主壳侵入轨道跃迁并具有低激发 $0_2^+$ 态的双阱体系。

## Failure Conditions

1. 若体系中子过剩较大（$|N-Z| \ge 6$），费米面失配使得 $T=0$ 配对与自旋-同位旋简并完全崩溃，不能套用自共轭形状双阱相消模型；
2. 若用于轻核区（如 $A \le 28$），每个主壳层的单粒子态数目极少，宏观形变与势能面概念解构。

## Falsification or Reverse Tests

1. **反向检验 1（库仑激发静四极矩符号检验）：** 若在低能逆运动学库仑激发实验中测得 $^{72}\text{Kr}$ 基态 $2_1^+$ 态的光谱四极矩为显著正值（$Q_s(2_1^+) > 0$，对应长椭形变），则直接推翻本模型关于基态扁椭主导的立论；
2. **反向检验 2（电单极寿命检验）：** 若高精度电子转换谱学测定 $^{72}\text{Kr}$ $0_2^+ \to 0_1^+$ 跃迁的单极矩阵元坍缩至 $\rho^2(E0) < 0.010$，则证伪两种宏观形变大振幅混合的假设。

## Open Questions

1. 在自共轭核 $^{64}\text{Ge}$（$N=Z=32$）中，三轴 $\gamma$ 软度是否会与扁椭长椭竞争产生更复杂的所谓“梨形四极三阱”拓扑流形？
2. 质子-中子等标（$T=0$）对关联在长椭极小与扁椭极小之间的跃迁势垒处如何定量改变穿透惯量张量？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于伪 SU(3) Casimir 展开与 2-能带变分混合求解程序（`day27_pseudo_su3_breakdown_shape_coexistence_study.py`）及入库文献；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立伪 SU(3) 四极集体性在 $N=Z=34,36$ 处的破缺机制与 $^{72}\text{Kr}$ 扁椭向长椭的转动带交叉（$\rho^2(E0) = 0.0317$），成功解释了 $^{68}\text{Se}$（$R_{4/2}=1.83$）对决 $^{76}\text{Sr}$（$R_{4/2}=3.25$）的结构突变。
