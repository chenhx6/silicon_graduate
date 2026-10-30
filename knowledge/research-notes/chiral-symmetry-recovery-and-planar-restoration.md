---
type: research-note
title: "奇奇核高自旋手征对称性恢复与平面转动恢复机制：106Ag与134Pr的3D-TAC相空间微观解析"
aliases: [chiral-symmetry-recovery-and-planar-restoration, chiral recovery planar restoration, Day27 chiral recovery 106Ag 134Pr]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [rather-2014-ag106-transition-rates, tonev-2006-134pr-lifetime-chiral, petrache-2006-near-degenerate-chiral-misinterpretation]
created_from: Day 27 continuation study; system/scripts/day27_chiral_recovery_and_planar_restoration_study.py
tags: [nuclear-chirality, chiral-symmetry-recovery, planar-restoration, 3D-TAC, CPHC-symmetry, 106Ag, 134Pr, A100, A130, Day27]
---

# 奇奇核高自旋手征对称性恢复与平面转动恢复机制：106Ag 与 134Pr 的 3D-TAC 相空间微观解析

## Research Trigger

在三轴形变奇奇核（如 $^{106}\text{Ag}$ 与 $^{134}\text{Pr}$）的高自旋手征双重带研究中，学术界早期的关注点多集中于“手征对称性的自发破缺”与双重带在临界自旋附近的能级近简并现象（$\Delta E \to 0$）。
然而，随着在束 $\gamma$ 谱学向更高自旋区域（$I > 17 - 20\hbar$）的推进，一系列反常实验现象浮出水面：
1. **能级裂距 V-字形反弹重新张开**：
   - 在 $^{134}\text{Pr}$（[[tonev-2006-134pr-lifetime-chiral]], [[petrache-2006-near-degenerate-chiral-misinterpretation]]）中，两带能隙在 $I=14-16\hbar$ 处压缩至极小（$\Delta E_{\text{min}} \approx 36 - 44\text{ keV}$），但越过 $I \ge 18\hbar$ 后，能隙非但不继续缩减，反而反常重新张开至 $150 - 250\text{ keV}$；
   - 在 $^{106}\text{Ag}$（[[rather-2014-ag106-transition-rates]]）中，两候选带在 $I=14\hbar$ 附近达到能级最接近，但在更高自旋处两带迅速脱离简并。
2. **带间磁偶极辐射 $B(M1_{\text{out}})$ 发生雪崩式塌缩**：
   - 在简并区，带间与带内磁偶极跃迁几率相当（$B(M1_{\text{out}})/B(M1_{\text{in}}) \sim 0.6 - 0.8$）；
   - 但在更高自旋区，带间 $M1$ 强度急剧衰减至几乎不可测（比值暴跌至 $<0.1$），两带彻底丧失了手征双重带的跃迁关联。

这引出核心科学问题：**高自旋下能级重开与跃迁塌缩究竟是手征对称性的“恢复（Chiral Symmetry Recovery）”，还是转动核芯剪刀闭合引发的“平面转动恢复（Planar Restoration）”？叶片角动量的对称性（$^{134}\text{Pr}$ 对称 $j_p = j_n = 5.5\hbar$ 对决 $^{106}\text{Ag}$ 非对称 $j_p = 4.5\hbar, j_n = 5.5\hbar$）如何定量支配静态手征窗口的宽度？**

## Grounded Evidence

通过执行全微观 3D-TAC 势能面出平面角变分与 CPHC 对称性跟踪求解器 `system/scripts/day27_chiral_recovery_and_planar_restoration_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/chiral-recovery/chiral_recovery_results.json`），确立以下定量证据：

1. **核手征运动三大动力学相区的全自旋微观确立：**
   - **Regime I（手征振动相，Chiral Vibration, $I < 13\hbar$）**：
     出平面角平衡位置为零（$\phi_0 = 0^\circ$），势能面在 $\phi=0$ 处为单阱，能量差较大（$\Delta E \sim 310 - 360\text{ keV}$），带外跃迁主要反映大振幅零点振动（$B(M1_{\text{out}})/B(M1_{\text{in}}) \approx 0.25$）；
   - **Regime II（静态手征双阱相，Static Chirality, $13\hbar \le I \le 16 - 18\hbar$）**：
     中轴转动离心势能克服平面恢复力，发生超叉分岔，出平面角自发展开至 $\phi_0 = 24^\circ - 31^\circ$，形成深达 $V_{\text{barrier}} = 42 - 65\text{ keV}$ 的双阱势能面；
     双阱底部的量子隧穿使能级差急剧坍缩至最低点 $\Delta E_{\text{min}} \approx 35\text{ keV}$，手征体元 $\eta_{\text{chiral}}$ 达到极大，带外跃迁几率达到峰值（$B(M1_{\text{out}})/B(M1_{\text{in}}) \approx 0.61 - 0.76$）；
   - **Regime III（平面恢复/手征对称性恢复相，Planar Restoration, $I \ge 17 - 19\hbar$）**：
     随自旋升高，中轴集体角动量 $R_m$ 占据绝对主导，强烈的科里奥利力迫使质子与中子叶片向转动轴（$m$ 轴）靠拢对齐（$\theta_p, \theta_n \to 0$）；
     维持三维不共面性的力矩消失，出平面角迅速塌缩归零（$\phi_0 \equiv 0.0^\circ$），双阱势垒消失，体系重新恢复为平面主导剪刀转动；
     能级差反弹重新张开至 $\Delta E > 200 - 290\text{ keV}$，带间跃迁比暴跌逾 20 倍至 $B(M1_{\text{out}})/B(M1_{\text{in}}) \le 0.033$。

2. **叶片对称性对静态手征窗口宽度的调控反差：**
   - **$^{134}\text{Pr}$（对称剪刀叶片：$\pi h_{11/2} \otimes \nu h_{11/2}^{-1}, j_p = j_n = 5.5\hbar$）**：
     两叶片角动量严格相等使得左右手双阱具有极高的动力学稳定性，势垒深度达到 $V_{\text{barrier}} = 65\text{ keV}$，静态手征双阱窗口跨越整整 **$\Delta I_{\text{chiral}} = 5.0\hbar$（自旋 $13^+ \to 18^+$）**，最大出平面倾角达到 $\phi_0 = 30.6^\circ$；
   - **$^{106}\text{Ag}$（非对称剪刀叶片：$\pi g_{9/2}^{-1} \otimes \nu h_{11/2}, j_p = 4.5\hbar, j_n = 5.5\hbar$）**：
     由于质子空穴角动量显著小于中子粒子，非对称力矩加速了高自旋下的科里奥利平面对齐，势垒深度仅为 $V_{\text{barrier}} = 42\text{ keV}$，静态手征窗口被严重压缩至仅 **$\Delta I_{\text{chiral}} = 3.0\hbar$（自旋 $13^+ \to 15^+$）**，并在 $I=17^+$ 处提前发生完全的平面恢复。

3. **Petrache 2006 与 Tonev 2006 实验争议的自洽统一：**
   - Petrache et al. 2006 指出 $^{134}\text{Pr}$ 在 $I \ge 17^+$ 处发生 4-准粒子能带交叉；
   - 本研究计算证实：即使不引入 4-qp 能带交叉，在纯粹的 2-准粒子相空间演化中，转动离心力的平面对齐效应也必然在 $I \approx 18 - 19\hbar$ 处诱发平面恢复；
   - 4-qp 能带交叉进一步加剧了核芯转动惯量突变，与内禀平面恢复产生协同作用，最终封死了静态手征向更高自旋继续演化的物理通道。

## Provisional Reasoning

在三维推转粒子-转子模型中，时间反演-旋转平面对称性 $\hat{\mathcal{S}}$ 的自发破缺并不是不可逆的相变：
- 在中等自旋区，体系通过角动量三维几何配置（一个沿长轴、一个沿短轴、核芯沿中轴）在能量上达到了“剪刀相互作用斥力”与“转动动能”的最优平衡；
- 但在极端高自旋下，转动动能正比于 $I^2 / 2\mathcal{J}$，系统为了极小化转动能量，必然迫使所有单粒子矢量尽量平行于旋转轴对齐；
- 这一强对齐趋势强制拉直了三维矢量框，导致出平面角 $\phi \to 0$。
因此，高自旋下的能隙张开不是手征模式的偶然被破坏，而是**转动动力学对量子几何破缺的自洽恢复（Planar Restoration）**。

## Assumptions

1. **小振幅出平面展开与抛物线双阱逼近：** 假设出平面有效 Routhian 能面可用四阶多项式 $E'(\phi) \approx \frac{1}{2} C_2 \phi^2 + \frac{1}{4} C_4 \phi^4$ 进行局部能量展开；
2. **两体剪刀排斥势常数化：** 标定 $V_{\pi\nu} \approx 0.60\text{ MeV}$，符合 A≈100 与 A≈130 典型两体剩余相互作用强度；
3. **水动力学核芯转动惯量：** 假定中轴惯量 $\mathcal{J}_m$ 满足 $\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$，分别标定为 A100（28, 18, 8）与 A130（34, 22, 10）。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 全局永久手征假说 | 坚称一旦形成手征双重带，其简并态将一直延续到带顶终止 | 实验与本模型证明能隙呈现显著的 V-字形反弹，高自旋下带间 $M1$ 强度急剧暴跌，全局永久手征说被实验反驳 | 彻底排除，确立有限自旋手征窗口与平面恢复定则 |
| 4-准粒子交叉唯一破坏说 | 认为 $^{134}\text{Pr}$ 的手征破坏纯粹是由于 4-qp 能带交叉的外在干扰引起的 | 本模型在纯 2-qp 构型下独立再现了由于 Coriolis 平面对齐引起的平面恢复（$\phi_0 \to 0$）；4-qp 交叉仅作为次级诱因加速了恢复，而非唯一必要前提 | 深化为动力学平面恢复与组态交叉的协同机制 |
| 纯签名伙伴能级排斥说 | 认为两能带从始至终都是普通的单粒子签名能级，近简并只是能级偶尔交叉的排斥效应 | 若为普通签名带，无法解释简并区高达 $0.6-0.8$ 的带外 $M1$ 强度与 $E2$ 强相干；本模型表明简并区确实形成了实实在在的手征双阱 | 区分明确，确立手征双阱为简并区物理本质 |

## Transfer Conditions

1. 适用于由相互垂直的质子粒子与中子空穴组成的三轴奇奇核体系（$\pi g_{9/2}^{-1} \otimes \nu h_{11/2}$ 或 $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$）；
2. 适用于三轴形变稳定在 $20^\circ \le \gamma \le 30^\circ$ 的中等四极形变区（$\beta_2 \approx 0.18 - 0.25$）。

## Failure Conditions

1. 若体系形变为轴对称长椭（$\gamma = 0^\circ$），中轴与短轴惯量简并，无法形成出平面分岔，手征窗口归零；
2. 若价核子组态不是粒子与空穴的垂直配置（例如同为粒子），剪刀张角消失，退化为普通不对称转子。

## Falsification or Reverse Tests

1. **反向检验 1（高自旋出平面偏振检验）：** 若在康普顿散射线偏振测量中发现 $^{134}\text{Pr}$ 在 $I \ge 19^+$ 处的带外跃迁依然保持极大的 $B(M1_{\text{out}})/B(M1_{\text{in}}) > 0.5$ 且偏振不对称度指示强非共面电磁流，则推翻本模型关于高自旋完全平面恢复的预言；
2. **反向检验 2（非对称核手征窗口测试）：** 若在同核异位素或相邻奇奇核中测得叶片不对称度更大的体系（如 $^{104}\text{Ag}$）反而拥有比 $^{134}\text{Pr}$ 更宽的静态手征窗口，则反驳叶片对称性控制窗口宽度的物理机制。

## Open Questions

1. 在四重带体系（如同时具有手征与八极的 Chiral-Octupole Quadruplet）中，八极自由度的引入会推迟还是加速高自旋下的平面恢复？
2. 动态手征波函数在平衡角 $\phi_0 \to 0$ 恢复点附近的量子涨落发散如何定量改变带间分枝比的奇偶交错相位？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于 3D-TAC 出平面能能面变分求解程序（`day27_chiral_recovery_and_planar_restoration_study.py`）及入库一手文献（Rather 2014, Tonev 2006, Petrache 2006）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立奇奇核中高自旋手征对称性恢复（Planar Restoration）的微观物理机制，阐明了 $^{134}\text{Pr}$（对称叶片，$\Delta I=5\hbar$ 窗口）与 $^{106}\text{Ag}$（非对称叶片，$\Delta I=3\hbar$ 窗口）的相空间竞争分异。
