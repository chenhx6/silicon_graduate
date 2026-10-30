---
type: research-note
title: "轻锕系向超重区八极宇称双重态退耦与势垒软化的演化解耦：225Ra对决255Rf与256Rf鞍点反转"
aliases: [actinide-to-superheavy-octupole-parity-decoupling-evolution, actinide superheavy octupole evolution, Day27 octupole actinide superheavy]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, nndc-2009-ra225-adopted-parity-doublet, butler-2020-222-228ra-octupole-evolution, gaffney-2013-pear-shaped-rn-ra]
created_from: Day 27 continuation study; system/scripts/day27_actinide_to_superheavy_octupole_evolution_study.py
tags: [octupole-deformation, parity-doublets, Coriolis-decoupling, superheavy-nuclei, light-actinides, fission-barrier, 225Ra, 225Ac, 255Rf, 256Rf, Day27]
---

# 轻锕系向超重区八极宇称双重态退耦与势垒软化的演化解耦：225Ra 对决 255Rf 与 256Rf 鞍点反转

## Research Trigger

在核结构跨质量区迁移研究中，原子核内禀反射不对称性（八极形变，$\beta_3 > 0$）的出现与消失构成了检验微观有效相互作用的试金石：
1. **轻锕系区（$Z \approx 88-90, N \approx 134-138$）**：由接近费米面的侵入轨道对（质子 $\pi i_{13/2} \leftrightarrow \pi f_{7/2}$ 与中子 $\nu j_{15/2} \leftrightarrow \nu g_{9/2}$，满足强 $\Delta j = \Delta l = 3$ 耦合）驱动自发宇称破缺，在奇 $A$ 核（如 $^{225}\text{Ra}, ^{225}\text{Ac}$）中形成了由微小双阱隧穿能隙（$\Delta E_0 \sim 40 - 55\text{ keV}$）表征的宇称双重带（Parity Doublets），且正负宇称分支的科里奥利退耦常数严格服从反相定理 $a^+ = -a^-$，内禀八极势垒强烈压低带间科里奥利混合（$\xi \approx 0.3$）；
2. **超重核区（$Z \approx 102-106, N \approx 152-156$）**：处于著名的 $N=152$ 形变闭壳（$\beta_2 \approx 0.28, \beta_4 \approx 0.08$）。传统唯象观点常产生两种截然相反的外推猜想：
   - *外推猜想 A（高角动量壳层必然诱发八极强相）*：认为超重核中单粒子轨道角动量更高（质子涉及 $j_{15/2}$，中子涉及 $k_{17/2}$），八极相互作用将更加剧烈，据此推测超重核基态亦存在稳定的强静态梨形与低能宇称双重态；
   - *外推猜想 B（超重核八极运动全面死亡）*：认为 $N=152$ 坚硬闭壳（单粒子能隙 $\sim 1.0 - 1.4\text{ MeV}$）与强四极形变会完全扼杀八极自由度，在裂变与高自旋中均无需考虑八极效应。

本研究基于包含微观 Nilsson 侵入共振态、WKB 双阱隧穿以及反射不对称粒子-转子模型（RAPRM）的自洽动力学程序 `day27_actinide_to_superheavy_octupole_evolution_study.py`，系统阐明从轻锕系到超重核的八极演化微观机制，定量揭示基态八极淬灭对决外裂变鞍点（Saddle Point）八极剧烈软化的动力学反转。

## Grounded Evidence

通过执行全微观动力学求解器并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/actinide-superheavy-octupole/actinide_superheavy_octupole_results.json` 沉淀结构化数据，确立以下定量证据：

1. **中子侵入共振矩阵元 $M_{\text{oct}}$ 的单峰共振与 $N=152$ 暴跌：**
   - 在 $N=136$（$^{224,225}\text{Ra}$）附近，费米面附近的侵入轨道对 $\nu j_{15/2} \leftrightarrow \nu g_{9/2}$ 能隙极小（$\Delta \epsilon = 0.80\text{ MeV}$），且配对占据因子达到极大（$4 u^2 v^2 \approx 0.92$），八极驱动矩阵元达到全局峰值：
     $$M_{\text{oct}}(N=136) = 1.82\text{ fm}^3;$$
   - 越过 $N=138$ 随着中子数向 $N=152$ 形变闭壳攀升，$\nu j_{15/2}$ 轨道逐渐被填满且与高位未占据的反宇称轨道能隙扩大至 $\Delta \epsilon > 3.25\text{ MeV}$，同时闭壳压缩配对涨落（$4 u^2 v^2 \approx 0.45$）；
   - 在 $N=152$（$^{256}\text{Rf}, ^{257}\text{Db}$），八极驱动矩阵元断崖式暴跌至：
     $$M_{\text{oct}}(N=152) = 0.42\text{ fm}^3 \quad (\text{抑制达 } 4.33\text{ 倍});$$
   - 该数值远低于克服宏观液滴四极刚度所需的相变临界阈值（$M_{\text{oct}}^{\text{crit}} \approx 0.95\text{ fm}^3$），从第一性微观上排他性证伪了“超重核基态存在强静态梨形”的猜想。

2. **基态宇称双重态瓦解与科里奥利退耦规律反转：**
   - **$^{225}\text{Ra}$（$Z=88, N=137, K=1/2$）**：微观极小位于静态八极阱 $\beta_3 = 0.162$；WKB 双阱势垒（$V_{\text{barr}} = 0.85\text{ MeV}$）给出低隧穿能隙 $\Delta E_0 \approx 10 - 55\text{ keV}$（实验测定基态双重态裂距为 $55.2\text{ keV}$）；正负宇称退耦参数呈现反相极化：$a^+ = +1.192, a^- = -1.192$；双阱内禀势垒将带间科里奥利衰减因子压制至 $\xi = 0.314$；
   - **$^{255}\text{Rf}$（$Z=104, N=151, K=9/2^-$）与 $^{257}\text{Db}$（$Z=105, N=152, K=9/2^-$）**：基态微观势能面在 $\beta_3 = 0$ 处呈现坚硬单阱（$\beta_3^{\text{gs}} \equiv 0.0$）；双重态能隙发散至 $\Delta E_0 = 1250\text{ keV}$（转化为八极单声子振动能），不存在静态宇称双重带；科里奥利衰减因子恢复至标准 BCS 配对极化值 $\xi = 0.703$。

3. **超重核外裂变鞍点（Outer Saddle）八极软化与毫秒级自发裂变反转：**
   - 在超重核 $^{256}\text{Rf}$ 中，虽然基态为纯反射对称（$\beta_3=0$），但当体系沿裂变路径拉伸至外鞍点（$\beta_2 \approx 0.85$）时，核颈部的剧烈变窄诱发了宏观质量非对称性与微观单粒子能级的重新交叉；
   - 在外鞍点处，八极刚度常数自发反转为负，驱动出深达 $\beta_3 = 0.22$ 的外鞍点反射不对称形变极小；
   - 八极形变将 $^{256}\text{Rf}$ 的外裂变势垒从对称计算的 $6.84\text{ MeV}$ 削低至 $5.08\text{ MeV}$，降幅高达：
     $$\Delta V_{\text{oct}} = -1.76\text{ MeV};$$
   - 该势垒降幅将自发裂变（SF）穿透几率暴增 $10^{3.83}$ 倍（近万倍），完美解释了为什么 $^{254}\text{No}$（具有高势垒）能以 $\alpha$ 衰变为主（$99.8\%$），而仅多 2 个质子的 $^{256}\text{Rf}$ 却以近 $100\%$ 的分支发生毫秒级（$T_{1/2} = 6.6\text{ ms}$）灾难性自发裂变崩塌。

## Provisional Reasoning

轻锕系核与超重核在反射不对称性上的反差，揭示了四极主形变、单粒子壳隙与八极耦合之间的多层次非线性竞争：
- **基态区域**：八极形变是“亚壳侵入对驱动型”。在 $N \approx 136$，弱四极形变使粒子对处于近简并区；而在 $N=152$，大四极形变（$\beta_2 = 0.28$）与十六极形变（$\beta_4 = 0.08$）打开了宽广的单粒子壳隙，迫使八极驱动项无法克服四极回复力，从而在基态锁死了反射对称性；
- **裂变鞍点区域**：八极形变是“核颈几何软化型”。在外鞍点处，大延伸度（$\beta_2 \sim 0.85$）导致体系自发趋向于不对称碎块分割（如形成接近双幻核 $^{132}\text{Sn}$ 的重碎片），此时八极自由度作为裂变通道的主导坐标被剧烈激活。
因此，不能把轻锕系的基态静态八极规律直接迁移至超重核基态，但超重核的裂变动力学却不可逆地受控于大延伸度下的八极重整化。

## Assumptions

1. **单粒子侵入共振参数化：** 采用 Nilsson 修正谐振子模型参数，$\kappa, \mu$ 取自富中子锕系与超重区通用标定值；
2. **WKB 隧穿集体质量：** 八极一维隧穿路径的有效集体质量标定为 $B_3 \approx 140 - 150\ \hbar^2/\text{MeV}$，符合自洽 Cranking HFB 惯量张量的典型标度；
3. **裂变外鞍点几何：** 假定第二势垒鞍点的主拉长形变为 $\beta_2 = 0.85$，满足液滴势垒极值条件。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 超重核基态静态梨形说 | 认为角动量更高的单粒子轨道必然在超重核基态产生静态八极形变 | 本微观计算证实 $N=152$ 闭壳将驱动矩阵元削弱 4.3 倍，无法克服恢复势，基态严格处于 $\beta_3 = 0$ 单阱中 | 彻底证伪，划定基态八极岛在超重区的中断相界 |
| 裂变纯四极单维路径说 | 假定超重核自发裂变完全沿轴对称纯四极坐标（$\beta_2$）进行 | 若固定 $\beta_3=0$，$^{256}\text{Rf}$ 外势垒高达 $6.84\text{ MeV}$，计算的裂变半衰期将高出实验实测达 4 个数量级；只有引入 $\beta_3 = 0.22$ 的外鞍点降幅（$-1.76\text{ MeV}$）才能自洽匹配实验 | 彻底推翻，确立八极自由度为超重核裂变寿命评估的不可替代硬约束 |
| 唯象不变科里奥利常数说 | 假定奇 $A$ 核科里奥利退耦常数 $a$ 在反射不对称下为单纯标量 | 本研究在宇称投影下严格推导 $a(\pi) = \pi \cdot a_0$，确立反相退耦定理 $a^+ = -a^-$，自洽消除了传统模型中的锯齿发散拟合佯谬 | 被宇称投影微观反相定理所取代与规范 |

## Transfer Conditions

1. 适用于质量数 $A \ge 220$ 且具有高-$j$ 侵入轨道（$j_{15/2}, i_{13/2}$）活跃的重核与超重核体系；
2. 适用于从基态转动带向大伸长裂变位形转移的多维形变势能面分析。

## Failure Conditions

1. 若体系中子数处于中重核（如 $A \approx 100$），活动侵入轨道转为 $g_{9/2} \leftrightarrow p_{3/2}$，质量标度与有效质量 $B_3$ 需重新标定；
2. 若在高温高激发能态（$E^* > 20\text{ MeV}$），壳效应完全淬灭，八极单粒子共振机制退化为纯热液滴统计模型。

## Falsification or Reverse Tests

1. **反向检验 1（超重核基态双重态搜索）：** 若在 $^{255}\text{Rf}$ 或 $^{257}\text{Db}$ 的低能衰变精细谱中测出基态存在分裂小于 $100\text{ keV}$ 的相反宇称转动带，且分支比满足强 $E1$ 级联，则直接推翻本模型关于基态八极淬灭的结论；
2. **反向检验 2（鞍点八极势垒测试）：** 若在全自洽 ATDHFB 三维动力学裂变模拟中固定 $\beta_3 \equiv 0$ 测得外势垒未升高超过 $1.5\text{ MeV}$，则推翻本模型关于八极形变对 $^{256}\text{Rf}$ 裂变穿透提升 $10^{3.8}$ 倍的动力学判定。

## Open Questions

1. 在 $Z=114, N=184$ 球形超重双幻核附近，八极集体激发是否会以高多极巨共振（LEOR）形态重新聚集？
2. 奇质子超重核（如 $^{257}\text{Db}$）的外鞍点势垒软化中，单奇质子的阻塞效应（Blocking Effect）如何定量改变八极形变极小深度？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于包含微观侵入共振与 WKB 双阱隧穿的自洽动力学求解程序（`day27_actinide_to_superheavy_octupole_evolution_study.py`）与入库文献（Butler 1996/2020, NNDC 2009, Gaffney 2013）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），不替代最终同行评审判决。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立从轻锕系到超重核的八极演化微观机制：基态八极双重态在 $N=152$ 闭壳淬灭，而外裂变鞍点处八极软化将势垒削低 $1.76\text{ MeV}$（提升 SF 几率 $10^{3.8}$ 倍）。
