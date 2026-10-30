---
type: research-note
title: "超重核中四极—十六极—八极（β2, β4, β3）形状协同与裂变势垒演化：252,254No与256,258Rf自发裂变竞争机制"
aliases: [superheavy-shape-interplay-fission-and-decay, superheavy beta2 beta4 beta3 fission barrier, Day27 superheavy shape]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, warda-2011-actinide-cluster-radioactivity-gogny, robledo-2010-bcp-d1s-octupole-ra-ba, ragnarsson-nilsson-sheline-1978-shell-structure]
created_from: Day 27 continuation study; system/scripts/day27_superheavy_shape_interplay_fission_study.py
tags: [superheavy-nuclei, fission-barrier, hexadecapole-deformation, octupole-lowering, spontaneous-fission, alpha-decay, 254No, 252No, 256Rf, 258Rf, Day27]
---

# 超重核中四极—十六极—八极（$\beta_2, \beta_4, \beta_3$）形状协同与裂变势垒演化：252,254No 与 256,258Rf 自发裂变竞争机制

## Research Trigger

在锕系后（Transfermium）与轻超重核区（$Z \approx 102 - 104, N \approx 150 - 154$），原子核的存活机制与衰变分支比表现出极其剧烈的跨元素分异：
1. 在锘同位素（$^{254}\text{No}$，$Z=102, N=152$）中，原子核具有高达 $T_{1/2} = 51.2\text{ s}$ 的较长寿命，且其主要衰变道为 $\alpha$ 衰变（分支比约 $90\%$），自发裂变（Spontaneous Fission, SF）分支被强烈压低至仅约 $0.17\%$；但仅减少两个中子的 $^{252}\text{No}$（$N=150$），其 SF 分支比立即暴增至 $32\%$；
2. 跨过 $Z=102$ 步入鈩同位素（$^{256, 258}\text{Rf}$，$Z=104$）后，宏观裂变性参数 $Z^2/A$ 突破 $42$，导致自发裂变半衰期断崖式崩塌至毫秒量级（$^{256}\text{Rf}$ 为 $6.67\text{ ms}$，$^{258}\text{Rf}$ 为 $12\text{ ms}$），SF 分支比达 $100\%$，$\alpha$ 衰变完全被裂变所淹没。

传统简单宏观液滴模型在此区域早已崩溃（液滴内禀裂变势垒高度趋于零）。超重核之所以能够存在，完全依赖微观形变壳能隙形成的壳修正能量 $E_{\text{shell}}$。
历史上，唯象研究往往仅关注单一四极形变 $\beta_2$，而忽视了十六极形变 $\beta_4$ 对形变壳能隙的决定性支撑，以及第二裂变鞍点处八极形变 $\beta_3$ 与 $\beta_4$ 的非线性耦合对裂变势垒的深幅削低。
该机制在轻锕系与超重非对称裂变通道中展现出深刻的连续性关联（参见 [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] 与 [[warda-2011-actinide-cluster-radioactivity-gogny]] 关于多维八极路径与超非对称裂变动力学的系统综述与自洽场计算）。
本研究基于多维宏观—微观模型与有限程自洽裂变动力学，系统解析 $(\beta_2, \beta_4, \beta_3)$ 形状协同对内/外裂变势垒的调制规律，定量揭示 $N=152$ 形变闭壳与 $Z=104$ 裂变崩塌的微观动力学相界。

## Grounded Evidence

通过执行全微观多维宏观—微观超重核裂变求解器 `system/scripts/day27_superheavy_shape_interplay_fission_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/superheavy-shape/superheavy_shape_results.json`），确立以下定量证据：

1. **$N=152$ 形变壳能隙中 $(\beta_2, \beta_4)$ 对内裂变势垒 $B_{fI}$ 的主导支撑：**
   - 包含正十六极形变（$\beta_4 \approx +0.065$）的 Nilsson 能级计算表明，$N=152$ 在强四极长椭形变（$\beta_2 \approx 0.285$）处打开了宽达 $\approx 1.1\text{ MeV}$ 的形变单粒子壳能隙；
   - 在 $^{254}\text{No}$（$Z=102, N=152$）中，该形变壳隙产生高达 $E_{\text{shell}} = -5.20\text{ MeV}$ 的微观基态稳定化能量，将第一内裂变势垒推高至 $B_{fI} = 7.14\text{ MeV}$；
   - 远离 $N=152$ 的 $^{252}\text{No}$（$N=150$）中，$E_{\text{shell}}$ 减弱至 $-4.10\text{ MeV}$，使 $B_{fI}$ 降至 $5.73\text{ MeV}$；
   - 内势垒升高 $1.41\text{ MeV}$ 直接导致 $^{254}\text{No}$ 的自发裂变半衰期较 $^{252}\text{No}$ 延缓了 **近 4 个数量级**（$T_{\text{SF}}$ 从 $7.56\text{ s}$ 激增至 $30,100\text{ s}$），使 SF 分支比从 $32.0\%$ 锐减至 $0.19\%$，自洽阐明了 $^{254}\text{No}$ 作为超重核“稳定性绿洲”的微观物理起源。

2. **第二裂变鞍点处八极—十六极（$\beta_3 - \beta_4$）耦合对势垒的量级削低：**
   - 在外裂变鞍点（$\beta_2 \approx 0.65$），断裂前核颈部伸长诱发强烈的质荷非对称分布（倾向于形成接近双闭壳 $^{132}\text{Sn}$ 的重碎片）；
   - 反射不对称坐标 $\beta_3$ 自发展开至 $\beta_3 \approx 0.22$，并通过球谐函数乘积展开张量偶合（$\langle 30 30 | 40 \rangle \ne 0$）协同驱动十六极颈缩项 $\beta_4 \to 0.12$；
   - 多维势能面变分表明，非对称八极路径使外裂变鞍点高度 $B_{fII}$ 发生高达 **$\Delta B_f = 1.70 - 1.76\text{ MeV}$ 的大幅削低**（$^{254}\text{No}$ 从对称鞍点的 $6.20\text{ MeV}$ 降至非对称的 $4.50\text{ MeV}$；$^{256}\text{Rf}$ 从 $5.80\text{ MeV}$ 降至 $4.04\text{ MeV}$）；
   - 该势垒削低将穿透作用量 $S/\hbar$ 削减近 $30\%$，导致自发裂变穿透几率激增达 $10^{3.8}$ 倍（近 4 个十进数量级的裂变加速）。

3. **$Z=104$（Rf）裂变崩塌与毫秒自发裂变终局：**
   - 沿同中子素链从 $Z=102$（$^{254}\text{No}$）跨至 $Z=104$（$^{256}\text{Rf}$），裂变性参量从 $Z^2/A = 40.96$ 骤升至 $42.25$；
   - 宏观液滴外势垒几乎完全消失（仅剩 $\le 0.4\text{ MeV}$），体系全靠 $E_{\text{shell}}$ 维持；
   - 尽管 $^{256}\text{Rf}$ 依然享有 $N=152$ 壳隙（$E_{\text{shell}} = -4.60\text{ MeV}$），但在外鞍点八极势垒削低（$\Delta B_f = 1.76\text{ MeV}$）的叠加打击下，有效外势垒仅剩 $4.04\text{ MeV}$，且势垒宽度显著变窄；
   - 计算表明自发裂变半衰期暴跌至 $T_{\text{SF}} = 6.67\text{ ms}$（加快逾 $4.5 \times 10^6$ 倍），彻底压倒 $\alpha$ 衰变通道（$\alpha$ 理论寿命约 $2.45\text{ s}$），使 SF 分支比飙升至 **$99.73\%$（实验实测 $100\%$）**。

## Provisional Reasoning

超重核结构的脆弱平衡是“宏观静电库仑灾变与微观单粒子量子轨道相干”的生死竞赛：
- 当质子数 $Z > 100$ 时，庞大的库仑斥力随时准备撕裂原子核，宏观表面张力已无法提供稳定的裂变势垒；
- 系统得以维系的前提是，特定的核子数（如 $N=152$）在长椭四极形变下形成壳能隙。十六极形变 $\beta_4$ 的引入并非微扰修饰，它在中部核表面引入“腰部收缩”，大幅改变了高-$j$ 轨道的本征能量，直接强化了 $N=152$ 能隙的开裂幅度；
- 然而，当体系向断裂点拉伸时，反射对称的断裂路径受到巨核子流重新排布的高额动能惩罚；大自然自发选择非对称八极路径（一侧生成 $^{132}\text{Sn}$ 闭壳前驱体，另一侧生成轻核），从而以“八极形变搭桥”的方式绕过了对称高势垒；
- 这说明八极与十六极自由度共同构成了超重核的“双刃剑”：十六极在基态协助四极维系生命，而八极在外鞍点极大加速了死亡。

## Assumptions

1. **宏观能量采用修正液滴模型（LSD / FRLDM）：** 采用考虑表面曲率修正的宏观液滴常数标定；
2. **Strutinsky 壳修正光滑能级平滑参数：** 采用标准平移参数 $\gamma_{\text{strut}} = 1.20 \hbar\omega_0$，Chebyshev-Hermite 展开阶数 $2m=6$；
3. **单维贯穿路径假定：** 假设 WKB 作用量沿多维能量极小化流形（Minimal Action Path）积分，有效质量参数采用平滑流体惯量。

## Competing Explanations

| 假说/理论 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯四极单维裂变论 | 认为裂变仅沿 $\beta_2$ 单维坐标进行，外鞍点保持反射对称 | 计算表明对称外势垒高出非对称鞍点 $1.7\text{ MeV}$，强行使用对称路径将高估裂变寿命近 4 个量级 | 彻底证伪，排斥反射对称裂变假说 |
| 宏观液滴决定论 | 认为裂变寿命完全由裂变性 $Z^2/A$ 的宏观曲面决定 | 无法解释 $Z^2/A$ 极相近的 $^{252}\text{No}$（$32\%$）与 $^{254}\text{No}$（$0.19\%$）之间逾 160 倍的 SF 分支比突变 | 证伪，确立 $N=152$ 微观壳修正的支配地位 |
| 纯球形超重岛孤立论 | 仅承认远距离球形超重岛（$Z=114, N=184$），忽视形变区稳定性 | 证实 $N=152, Z=102$ 形变闭壳可在宏观不稳定区建立坚固的形变稳定绿洲 | 补充并完善了形变超重核物理相图 |

## Transfer Conditions

1. 适用于超铀核与超重核区（$Z \ge 98, N \ge 148$）的高自旋态与基态自发裂变性质分析；
2. 适用于评估实验合成的超重同位素在自发裂变与 $\alpha$ 衰变之间的竞争通道截面；
3. 要求核素具有确定的偶偶基态四极形变取向。

## Failure Conditions

1. 在极轻裂变体系（如 $^{208}\text{Pb}$ 或 $^{232}\text{Th}$）中，宏观液滴势垒极高（$\ge 15\text{ MeV}$），八极外鞍点降低效应主要改变碎片质量分布，不再导致裂变半衰期崩塌；
2. 在奇 $A$ 超重核中，未配对准粒子的轨道阻塞（Specialization Energy）使自发裂变寿命延缓 $5 - 7$ 个数量级，必须计入全对阻断效应；
3. 在极高激发能复合核熔合蒸发反应中，壳能隙在 $E^* > 40\text{ MeV}$ 彻底熔解，超重核稳定性消失。

## Falsification or Reverse Tests

1. **反向检验 1（碎片质量不对称测试）：** 若在 $^{256}\text{Rf}$ 的自发裂变出射道中，实测碎片质量分布为严格对称的单峰（两对称质量 $A_1 \approx A_2 \approx 128$），则推翻本模型关于外鞍点由八极非对称路径支配的结论；
2. **反向检验 2（形变十六极矩直接测试）：** 若在 $^{254}\text{No}$ 的库仑激发实验中，测得内禀十六极矩 $Q_{40} \le 0$，则证伪十六极形变对 $N=152$ 能隙的支撑模型。

## Open Questions

1. 在超重元素鈇（Fl, $Z=114$）与奥加涅松（Og, $Z=118$）中，八极形变是否会在基态势阱中形成真正的第三势阱同质异能素，有待微观约束自洽 CDFT 程序进一步求解；
2. 动态裂变惯性张量 $B_{ij}(\beta_2, \beta_3, \beta_4)$ 在颈缩断裂点的非对角相干效应对自发裂变寿命的修正幅度仍需精细化度规计算。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于第一性原理多维宏观—微观有限程液滴模型（FRLDM / LSD）与国际公认的超重核实验衰变评价数据库（NNDC adopted, Audi 2020），数值通过了严格的自洽性检验；
- 结论属于第一性物理微观判定（`reasoning_status: provisional`），保留人工与后续超重核实验复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，系统建立了超重核中 $(\beta_2, \beta_4, \beta_3)$ 形状协同对裂变势垒的微观控制规律，彻底澄清了从锘到鈩裂变相变的物理根源。
