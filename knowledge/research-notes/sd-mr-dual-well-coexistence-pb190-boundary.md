---
type: research-note
title: "A≈190 铅区 SD/MR 共存与微观多阱形变拓扑边界"
aliases: [Pb190 SD MR dual well coexistence, superdeformation magnetic rotation Pb]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 A≈190 Pb SD/MR coexistence worker study
promotion_target: superdeformation, magnetic-rotation, shape-coexistence
tags: [A190, Pb, superdeformation, magnetic-rotation, shears, shape-coexistence, double-well]
evidence_sources: [astier-1997-193pb, bouneau-1997-196pb, van-severen-1998-pb-quadrupole, hubel-2005-magnetic-rotation-review, clark-2000-shears-mechanism]
---

# A≈190 铅区 SD/MR 共存与微观多阱形变拓扑边界

## Research Trigger

本轮问题是检验 A≈190 铅区是否能在同一个核内同时容纳超形变（SD）和剪刀磁转动（MR）两类高自旋结构，并把这种共存写成可计算的多阱形变—算符对照。题设给出的“194,196Pb 具有 SD 与 MR”方向是有文献支持的，但题设中的所有数值并非同一来源、同一观测量或同一核素的直接测量。因此本笔记把 196Pb 作为最完整的同核锚点，把 193Pb 作为有原始同核“SD+dipole”共存摘要的交叉锚点，把 194,195Pb 主要用于 SD Qt 系统学。

## Grounded Evidence

### 同核共存的直接证据

| ID | 实验事实或来源陈述 | 证据定位 | 证据层/边界 |
|---|---|---|---|
| E1 | Astier 等在 193Pb 的同一 EUROGAM II 实验中报告 5 条新的 ΔI=1 偶极级联；同文并列讨论 6 条 SD 带。偶极带的两个最强带给出 B(M1)/B(E2)>10 μN²/(e²b²)，SD signature-partner 交叉跃迁平均值为 0.15(4) μN²/(e²b²)。 | Astier et al., Z. Phys. A 358, 195–196 (1997), DOI `10.1007/s002180050305`, 摘要；PDF pp.195–196，Fig.1–2及正文。 | 原始实验摘要/短文；比值不是两个带类的逐态绝对 B(M1) 或 B(E2) 全表。 |
| E2 | 196Pb 有 9 条被归入 MR 的 M1 带，其中 8 条连接到低能级；同一核的 SD 结构由 yrast 与多个 excited SD bands 组成。 | Hübel, Prog. Part. Nucl. Phys. 54, 1–69 (2005), DOI `10.1016/j.ppnp.2004.06.002`, PDF pp.13–19, Figs.11–16；原始 MR 谱系为 Ref.[36] A.K. Singh et al., Nucl. Phys. A 707, 3 (2002)。 | 综述汇编的谱学事实；MR 带的原始逐带数据应回到 Ref.[36]。 |
| E3 | 同一 196Pb 又有 SD yrast 与 excited SD bands；Bouneau 等报告三条 excited SD bands 向 yrast SD band 的疑似 E1 衰变，并以 RPA 比较解释为 octupole-vibrational structures。 | Bouneau et al., Z. Phys. A 358, 179–180 (1997), DOI `10.1007/s002180050299`, 摘要与 PDF p.179–180；Hübel 2005 PDF pp.3, 11–12。 | 原始 SD 短文；“疑似 E1”和八极振动是作者解释，不是静态 beta3 直接测量。 |
| E4 | Hübel 综述对 196Pb 的 MR 带有 DSAM/RDM 寿命路线：最强 M1 带测得 DSAM，低自旋 band 1 有 RDM，另有四条 M1 带的 DSAM；Fig.24 展示 B(M1) 随自旋的实验曲线。 | Hübel 2005 PDF pp.25–27, Fig.24；pp.49–55 的 196Pb TAC 对照。 | 综述对原实验的整合；数值曲线不能替代原始寿命论文。 |
| E5 | 196Pb band 1 的 B(M1) 在交叉前从约 2.4 降到 0.7 μN²，交叉后约 9 μN²，再随自旋降到 1.8 μN²；Hübel 将跃升归因于 i13/2 中子对排列导致剪刀重新张开。 | Hübel 2005 PDF pp.49–50，Band-termination 段落，引用 [51,52,55]。 | 综述转述的原始寿命结果；是配置交叉条件下的非单调例子，不是所有 MR 带的单调定理。 |

### SD 四极矩与 MR 弱形变的分层

| ID | 数值或观测 | 证据定位 | 解释边界 |
|---|---|---|---|
| E6 | 194Pb band 1、195Pb bands 1–2、196Pb band 1 的 SD yrast Qt 约 20 eb；193Pb 为 Qt=17.3(7) eb。 | van Severen et al., Phys. Lett. B 434, 14–20 (1998), DOI `10.1016/S0370-2693(98)00819-3`, abstract（Crossref/OpenAlex 记录与 DOI 元数据）。 | 这是由 DSAM centroid shift/lineshape 导出的 transition quadrupole moment；不是 beta2 的直接观测。 |
| E7 | 196Pb SD excited band 的 E1/E2 分支分析采用 yrast SD Qt=(19.5±0.4) eb，并估得 B(E1)=(1.0±0.2)×10⁻⁴ W.u.；文中明确没有直接寿命来给出 E1 几率。 | Hübel 2001, Spectroscopy of superdeformed Pb isotopes, arXiv:nucl-ex/0104027v1, PDF pp.5–7, Table 2；原始实验 DOI 见 Bouneau 1997。 | 说明 SD 内部强 E2 与跨带 E1 的观测层，不能把该 E1 当作 MR 的 M1。 |
| E8 | MR band-head 的静态四极矩明显小于 SD Qt。在 194Pb 与 196Pb，11− isomer 的 Qs 分别为 4.48(86) b、3.41(66) b，强耦合假设下给出 δ2=−0.20(4)、−0.15(3)。 | Hübel 2005 PDF pp.38–40, Figs.36–37。 | Qs 是谱学静态矩，单位 b；不可直接等同于 SD 的 Qt（eb）或直接写成 Q0=2–3 eb。δ2 也依赖强耦合和 oblate 假设。 |
| E9 | 193Pb MR band 1 的 2584-keV 29/2− band head 有 g=0.68(3)，与 [π(h9/2 i13/2)11− ⊗ ν i13/2−1]29/2− 的 gcalc=0.71(4) 一致；Hübel 据此支持近垂直的 proton-particle/neutron-hole 耦合。 | Hübel 2005 PDF pp.33–35, Figs.31–33, configuration discussion。 | 这是 MR 配置和静态磁矩约束；并非 196Pb 的同一带配置。 |
| E10 | 在 MR Pb bands 中，带能给出的 J(2) 可约 20 hbar²/MeV，而 SD 旋转谱的 J 近似恒定；196Pb 的 SD4 例给出 J(2) 约 100 hbar²/MeV。 | Hübel 2005 PDF pp.3, 41–42；Bouneau 1997 PDF p.180（SD4 段落）。 | 20 与约100 是综述/短文中的量级锚点，不是本笔记重新从完整 level scheme 数值微分所得。 |

### 机制与算符的 grounded 约束

- SD：Hübel 将 196Pb SD 带视为大稳定形变、近恒定转动惯量的电四极转动谱（PDF pp.3–4）；Hübel 2001 对 193Pb 给出 [761]3/2、[642]3/2、[624]9/2 等高形变 Nilsson/准粒子候选（PDF pp.2–4，Table 1）。因此“nu j15/2 intruder 参与 A≈190 SD”有具体配置支持，但“所有 SD 都由 nu j15/2 与 pi i13/2 同时驱动”超出当前证据。
- MR：Clark–Macchiavelli 2000 将 Pb 区 MR 归因于高-j 质子粒子与中子空穴的剪刀闭合，B(M1) 随横向磁矩下降，弱 E2 与小形变需联合判定（PDF pp.5–8, 13–18, 23–27）；Hübel 2005 给出半经典关系 B(M1) 正比 sin²(theta)、B(E2) 正比 sin⁴(theta) 及 P2(theta) 有效相互作用（PDF pp.57–64, Eqs.17–26）。
- 算符边界：SD 的 E2 强度由集体 Q0 与转子几何控制；MR 的 M1 由粒子—空穴横向磁矩控制，E2 仍可含核芯极化。单凭能级等间距或一个 B(M1)/B(E2) 比值无法判定势阱身份。

## Provisional Reasoning

### 1. 由实验事实得到的“同核双结构”图像

196Pb 是最适合当前问题的同核例：一组 near-spherical/weakly deformed 的 MR M1 bands（Hübel pp.13–19, 25–27, 49–55）与另一组 SD E2 bands（Hübel pp.3–4, 11–12；Bouneau 1997）在同一核素中出现。193Pb 则由 Astier 原始短文直接把 dipole 与 SD 结构放在同一反应、同一论文中。由 Qt 约 20 eb 对 SD 和 MR 的小 Qs、δ2 约束综合来看，可以把它们作为多准粒子势能面上不同构型/形变极小的实验代理；“存在两个静态深极小阱及其隧穿劈裂”仍是模型语言，当前证据没有直接测出完整二维势能面或阱间隧穿劈裂。

### 2. 可复现的双阱模型

`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/sd-mr-coexistence/sd_mr_doublewell.py` 定义一个透明的形变坐标模型：

    V(beta2) = 600 (beta2 - 0.10)^2 (beta2 - 0.50)^2 MeV

两个极小在 beta2=0.10 和 0.50，中点 beta2=0.30 的势垒为 0.96 MeV。这个势垒是演示输入，不是 196Pb 的实验或自洽 HFB 结果。脚本同时输出 Q0、B(E2)、shears B(M1) 和两条 J(2) 轨迹，且在 JSON 中保留所有输入与单位。

### 3. 关键算符和动力学对比

脚本采用 R0=1.2 A^(1/3) fm、Q0=(3/sqrt(5π)) Z R0² beta2，以及

    B(E2) = 5/(16π) Q0² I(I−1)/[(2I−1)(2I+1)]

和示意性的

    B(M1) = 3/(8π) (g_eff j_eff sin(theta))² mu_N²。

在 A=194、Z=82 下，beta2=0.10 给 Q0=2.995 eb，和弱形变 MR 的量级相符；beta2=0.50 给 Q0=14.98 eb，而不是 20 eb。若把 van Severen 的导出 Qt 约 20 eb 与这个液滴换算强行视为同一量，则需要 beta2 约 0.67。因此题设“beta2=0.45–0.55 且 Q0=19–21 eb”存在约 30%–35% 的定义或参数不一致；脚本把 reported_SD_Qt=20 eb 和 beta2_SD=0.50 分列并自动报告该边界。

脚本输出的 illustrative J(2)_SD=95±2 hbar²/MeV，J(2)_MR 从约 49 降至 15 hbar²/MeV，用于复现“SD 平缓大惯量、MR 中等且随剪刀闭合下降”的动力学对照；它们不是对某一条实验带重新拟合的数值。Hübel 对 196Pb 还记录了配置交叉后 B(M1) 的重新增强，故 MR 的下降只在单一配置区间内成立。

## Assumptions

- 双阱只在 beta2 一维坐标中示意；没有把 gamma、beta4、beta6、配对、准粒子占据和核芯极化显式量子化。
- SD 观测 Qt 用于实验强度尺度，beta2 用于脚本几何尺度，二者不默认相等。
- MR 的 g_eff=0.80、j_eff=6.5 和 theta(I) 是可审计的演示输入；Hübel/Clark 的有效 g 和配置因核素、带和模型而异。
- B(E2) 采用 K=0 转子因子只作尺度比较；MR 带的实际 E2 需要逐带寿命、分支和混合分析。
- 所有模型输出均标记为 toy_scale_model_not_experiment，不得升级成 194,196Pb 的直接 PES 或实测 B(E2) 表。

## Competing Explanations

- SD 与 MR 的共存可来自不同多准粒子配置在同一平均场上的竞争，也可来自同一宏观形变坐标上的配置极小；当前谱学证据不能唯一选择“两个静态深阱”而排除软势面、多配置混合或形变随频率演化。
- MR 的 B(M1) 下降可以由剪刀闭合解释，但 196Pb 的交叉后反弹表明准粒子对齐、配置更换和核芯旋转也可主导曲线。
- SD 带的 Qt 约 20 eb 可能与形变定义、半径参数、有限自旋转换有关；不能用单一液滴换算直接否定寿命导出的 Qt，但必须保留换算不一致。
- “弱/无 M1”是 SD 纯 E2 带的选择性描述；SD excited-band 的 E1 links（196Pb）是另一通道，不能与 MR 的 ΔI=1 M1 混写。

## Transfer Conditions

只有同时具备同核的 SD band identity、MR/dipole band identity、绝对或相对寿命、Qt/Qs、多极性和配置/对齐证据时，才能把本框架迁移到 194Pb 或 195Pb。迁移到 Hg/Bi 需重新核对 Z=82 壳隙、准粒子轨道、配对和反应选择性；不能把 196Pb 的 9 条 MR 带或 193Pb 的比值直接复制。

## Failure Conditions

- 把 Hübel 综述中的 MR 数值当作独立于 Ref.[36,51,52,55] 的新实验。
- 把 Qs（b）、Qt（eb）和 Q0（模型内禀矩）混为一个量，或把 δ2 直接写成实验 beta2。
- 以 ΔI=1 或 ΔI=2 的能级规则单独判定 MR/SD；必须回到多极性、寿命、矩和配置。
- 将脚本的 0.96 MeV 势垒、J(2) 或 B(M1) 曲线宣称为 196Pb 的自洽计算或实验回归。
- 忽略 196Pb 配置交叉后 B(M1) 重开，从而把单调下降误写成全自旋硬判据。

## Falsification or Reverse Tests

- 若从同一 196Pb MR 带的逐态寿命得到的 B(M1) 与 B(E2) 不支持单配置的 sin²(theta)/sin⁴(theta) 相对演化，则必须引入配置混合、核芯 E2、形变或有效 g 演化。
- 若 196Pb 或 194Pb 的 SD Qt、寿命和旋转频率无法由同一 SD 构型解释，双阱图像须改为多配置/软势面图像。
- 若原始 196Pb MR level scheme 的连接、偏振或寿命复核显示带并非 M1 主导，则“同核 SD+MR”结论降级为 SD+dipole 候选。
- 用自洽 HFB/TAC/GCM 计算检查是否同时出现正常/弱形变与 SD 极小，并比较势垒、零点涨落及 configuration projected overlaps；只有此类计算才可把本脚本的拓扑比喻升级为模型结果。

## Open Questions

- 196Pb MR 九带的逐带绝对 B(M1)、B(E2)、配置和 J(2) 是否能从 Singh 2002 与寿命原件完整重建？
- 194Pb 是否存在与其 SD yrast 带在同一核素、同一实验谱系中明确连接的 MR 带，而不是仅有独立的 11− isomer 和邻近 Pb MR 系统学？
- Qt 约 20 eb 与 beta2 约 0.5 的差异主要来自形变定义、有限自旋转换、半径参数还是文献中不同 Qt/Q0 约定？
- 196Pb SD excited-band 的 E1 八极振动结构与 MR 多准粒子配置是否存在可观测的混合或竞争？
- 是否可以取得 194Pb 的自洽多维 PES 和 196Pb 的 TAC/HFB 配置投影，以定量估计阱间耦合而非仅用双阱示意？

## Human Review

本笔记为 Codex self-audit，review_status: unreviewed。已核对 Astier 1997、Bouneau 1997 原始短文，Hübel 2001 arXiv 短文和 Hübel 2005 综述的定位；van Severen 1998 的数值目前由 DOI 元数据/摘要交叉核验，仍需人工回看全文表格和定义。没有把任何内容写成 human-reviewed。

## Promotion or Rejection History

2026-10-29：建立 A≈190 Pb SD/MR 同核共存边界。supports 196Pb 的 SD+MR 共存、193Pb 的 SD+dipole 同核实验事实以及 Clark/Hübel 的算符判据；limits 把 194,196Pb 的所有题设数值视作直接同源测量、把 SD Qt 与 beta2 直接等同、把 MR 单调闭合推广到配置交叉后全带；provisional 双阱势能面和 SD/MR 曲线仅由 worker 脚本示意。
