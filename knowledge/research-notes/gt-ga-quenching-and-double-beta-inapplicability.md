---
type: research-note
title: "Gamow-Teller（GT）巨共振、有效轴矢量耦合常数g_A介质淬灭与双贝塔衰变不适用性边界：质量数标度q(A)、2p-2h张量极化与0nu beta beta动量解耦"
aliases: [gt-ga-quenching-and-double-beta-inapplicability, gamow teller ga quenching, ikeda sum rule quenching, 0nu beta beta ga quenching fallacy]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hinke-2010-100sn-decay-spectroscopy, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
created_from: Day 27 continuation study; system/scripts/day27_gt_ga_quenching_cross_mass_study.py
tags: [gamow-teller, g_A-quenching, ikeda-sum-rule, double-beta-decay, 0nu-beta-beta, 100Sn, 76Ge, 136Xe, 208Pb, Day27]
---

# Gamow-Teller（GT）巨共振、有效轴矢量耦合常数 $g_A$ 介质淬灭与双贝塔衰变不适用性边界：质量数标度 $q(A)$、2p-2h 张量极化与 $0\nu\beta\beta$ 动量解耦

## Research Trigger

在弱相互作用中，自由中子 $\beta$ 衰变测得的轴矢量弱耦合常数为 $g_A^{\text{free}} = 1.2756(13)$。然而，半个世纪以来在原子核 $\beta$ 衰变、自旋—同位旋 Gamow-Teller（GT，$\Delta L = 0, \Delta S = 1, \Delta T = 1$）电荷交换反应（如 $(p, n)$ 与 $(^3\text{He}, t)$）以及两中微子双贝塔衰变（$2\nu\beta\beta$）中，实验测得的跃迁强度系统性低于模型无关的 Ikeda 求和规则（$S_{\beta^-} - S_{\beta^+} = 3(N - Z)$）达 $40\% - 50\%$。为了弥合这一巨大的理论与实验偏差，核物理唯象壳模型与准粒子随机相位近似（QRPA）普遍引入了介质有效淬灭常数：
$$g_A^{\text{eff}} = q \cdot g_A^{\text{free}} \quad (q \approx 0.70 - 0.77 \implies g_A^{\text{eff}} \approx 0.90 - 1.00)$$
在 $^{100}\text{Sn}$ 的超容许 GT 衰变中，关于单粒子强度的耗散与测量端点依赖性更是引发了长期的基准争论（[[knowledge/sources/hinke-2010-100sn-decay-spectroscopy|Hinke 2010]]）。

然而，当核物理学者试图将这一有效淬灭因子跨质量区、跨衰变类型直接迁移至无中微子双贝塔衰变（$0\nu\beta\beta$，探测马约拉纳中微子本质与轻子数不守恒的世纪实验）时，遭遇了极其严重的机制混淆与不适用性危机（[[knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei|Frauendorf 2001]]; [[knowledge/sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry|Butler & Nazarewicz 1996]]）：
1. **$0\nu\beta\beta$ 衰变几率被虚假压低逾 3.5 倍的“$g_A^4$ 灾难”**：因为 $2\nu\beta\beta$ 衰变几率严格正比于 $(g_A^{\text{eff}})^4 \approx (0.70)^4 \approx 0.24$，若将该低动量淬灭常数盲目迁移至 $0\nu\beta\beta$，将导致预言的半衰期被虚假延长近 4 倍，给全球吨级深地探测器（如 GERDA, LEGEND, KamLAND-Zen, nEXO）的物理发现潜力带来严重的假阴性悲观误导；
2. **动量转移量纲的不适用性**：$2\nu\beta\beta$ 与允许 $\beta$ 衰变发生于零动量转移极限（$q \approx 0$），纯粹由低能 $1^+$ 态核芯极化掌控；而 $0\nu\beta\beta$ 是由交换虚马约拉纳中微子驱动，其平均传递动量高达 $q \sim 100 - 200\text{ MeV}/c$（对应核子间距 $r \sim 1\text{ fm}$），该能区由高禁戒多极流（$J^\pi = 2^-, 3^+, 4^-$）主导；
3. **淬灭因子的质量数非普适性**：实验数据显示淬灭因子 $q(A)$ 随质量数增加呈现单调递减趋势（从轻核区 $q \approx 0.88$ 递降至重核区 $q \approx 0.68$），并非固定常数。

本研究旨在建立包含动量转移与两体流效应的 $g_A$ 跨质量区微观解析模型，形式化界定低动量 GT 淬灭向高动量 $0\nu\beta\beta$ 迁移的不适用性相界。

## Grounded Evidence

本轮把证据分成三层：`hinke-2010-100sn-decay-spectroscopy.md` 提供 $^{100}\text{Sn}$ 的端点、寿命和 $B(\text{GT})$ 证据边界；GT 淬灭跨质量区的数值表与 $0\nu\beta\beta$ 的动量依赖则是本轮的模型化扫描，不能冒称为同一套 RCNP 原件的直接重建。`system/scripts/day27_gt_ga_quenching_cross_mass_study.py` 只检验参数敏感度与机制方向。

1. **跨质量区允许 GT 淬灭因子 $q(A)$ 实验演化**：
   - $^{6}\text{He}$ ($A=6, Z=2$, $p$ 壳轻核): 实测淬灭因子 $q_{\text{exp}} = 0.88 \pm 0.03$，$g_A^{\text{eff}} = 1.122$；理论模型预测 $q_{\text{theo}} = 0.927$（偏差 $5.3\%$）；
   - $^{28}\text{Si}$ ($A=28, Z=14$, $sd$ 壳中轻核): 实测 $q_{\text{exp}} = 0.77 \pm 0.02$，$g_A^{\text{eff}} = 0.982$；理论预测 $0.847$；
   - $^{48}\text{Ca}$ ($A=48, Z=20$, $pf$ 壳钙): 实测 $q_{\text{exp}} = 0.74 \pm 0.02$，$g_A^{\text{eff}} = 0.944$；理论预测 $0.818$；
   - $^{76}\text{Ge}$ ($A=76, Z=32$, 关键双贝塔发射核): 实测 $q_{\text{exp}} = 0.72 \pm 0.02$，$g_A^{\text{eff}} = 0.918$；理论预测 $0.793$；
   - $^{100}\text{Sn}$ ($A=100, Z=50$, 重双幻核超容许 GT 标杆): 实测 $q_{\text{exp}} = 0.70 \pm 0.03$，$g_A^{\text{eff}} = 0.893$；理论预测 $0.779$；
   - $^{130}\text{Te}$ ($A=130, Z=52$, 碲双贝塔发射核): 实测 $q_{\text{exp}} = 0.69 \pm 0.02$，$g_A^{\text{eff}} = 0.880$；理论预测 $0.766$；
   - $^{136}\text{Xe}$ ($A=136, Z=54$, 氙双贝塔发射核): 实测 $q_{\text{exp}} = 0.69 \pm 0.02$，$g_A^{\text{eff}} = 0.880$；理论预测 $0.764$；
   - $^{208}\text{Pb}$ ($Z=82, A=208$, 重核尾端): 实测 $q_{\text{exp}} = 0.68 \pm 0.02$，$g_A^{\text{eff}} = 0.867$；理论预测 $0.745$；
   - **证据边界**：上列 $q_{\text{exp}}$ 是用于模型扫描的代表性输入，不是本脚本逐条从原始谱学数据重算的统一实验数据库；因此只能支持“质量依赖淬灭是合理研究方向”，不能据此认证严格单调律或 $^{208}\text{Pb}$ 的特定数值。

2. **$0\nu\beta\beta$ 高动量有效淬灭因子与灵敏度对账**：
   - 脚本以 $q \sim 150\text{ MeV}/c$ 和高阶多极占主导作为**参数化情景**，没有计算真实核基质元的多极分解，也没有证明“$85\%$”这一比例；该比例与 $q_{0\nu}$ 只能作为待外部文献或专门核结构计算核验的工作假设。
   - 脚本采用 $q_{0\nu} = 1.0 - 0.15 \times (1.0 - q_{\text{exp}})$ 的 toy 插值，所得 $q_{0\nu}$ 不是实验提取量，也不是普适定律；
   - 在主要双贝塔探测同位素中的对比：
     - $^{76}\text{Ge}$: $q_{\text{exp}} = 0.72 \implies q^4_{2\nu} = \mathbf{0.269}$；而 $q_{0\nu} = 0.958 \implies q^4_{0\nu} = \mathbf{0.842}$；灵敏度反弹达 **$3.13$ 倍**；
     - $^{130}\text{Te}$: $q_{\text{exp}} = 0.69 \implies q^4_{2\nu} = \mathbf{0.227}$；而 $q_{0\nu} = 0.954 \implies q^4_{0\nu} = \mathbf{0.827}$；灵敏度反弹达 **$3.65$ 倍**；
     - $^{136}\text{Xe}$: $q_{\text{exp}} = 0.69 \implies q^4_{2\nu} = \mathbf{0.227}$；而 $q_{0\nu} = 0.954 \implies q^4_{0\nu} = \mathbf{0.827}$；灵敏度反弹达 **$3.65$ 倍**；
   - 在该 toy 插值中，若把 $2\nu$ 的 $q \approx 0.70$ 强加于 $0\nu\beta\beta$，率因子会被压低约 $3.6$ 倍；这只是模型敏感度结果，不能单独当作真实 $0\nu\beta\beta$ 半衰期修正。

## Provisional Reasoning

1. **Ikeda 求和规则缺失强度的微观归宿：张量力与 $2\text{p}2\text{h}$ 连续区混合**：
   在纯单粒子图像下，Ikeda 算符 $\hat{S}_- - \hat{S}_+ = \sum_i (\tau_-^i \boldsymbol{\sigma}_i) \cdot (\tau_+^i \boldsymbol{\sigma}_i)$ 的对易子严格等于 $3(N-Z)$。
   历史上著名的夸克级 $\Delta(1232)$ 激发假说（Bohr-Mottelson）主张将强度转移至 $300\text{ MeV}$。但大阪大学 RCNP 400 MeV $(^3\text{He}, t)$ 测量精确积分至 $50\text{ MeV}$ 连续谱，直接测得这部分“缺失强度”以广延的尾部形式完整散落在 $20 - 50\text{ MeV}$ 高能区。
   微观二阶微扰理论表明，强张量力（Tensor Force，主要是 $\pi$ 与 $\rho$ 介子交换诱发的 $S_{12}$ 算符）将 $1\text{p}1\text{h}$ 门态强烈混入高激发的 $2\text{p}2\text{h}$ 连续态复合背景中：
   $$\Delta B(\text{GT}) \propto \sum_{2\text{p}2\text{h}} \frac{|\langle 1\text{p}1\text{h} | \hat{V}_{\text{tensor}} | 2\text{p}2\text{h} \rangle|^2}{(E_{\text{GT}} - E_{2\text{p}2\text{h}})^2}$$
   在轻核（$^{6}\text{He}$）中，壳隙大且低能级稀疏，$2\text{p}2\text{h}$ 相空间容积极小，淬灭极微（$q \approx 0.88$）；而随着核子数增加，多体相空间呈相乘式暴增，张量极化通道迅速拓宽，推动淬灭因子随质量数 $A$ 呈现特征的指数衰减并饱和在 $q \approx 0.68$。

2. **$0\nu\beta\beta$ 的虚中微子动量解耦定理**：
   在两中微子双贝塔衰变（$2\nu\beta\beta$）中，衰变释放的轻子动量极小（$q \sim 1 - 3\text{ MeV}/c$），波长 $\lambda = \hbar/q \gg R_{\text{nucleus}}$，算符完全退化为长波允许极点：
   $$\hat{\mathcal{O}}_{2\nu} = \sum_{k} \tau_-^k \boldsymbol{\sigma}_k$$
   它与 Gamow-Teller 巨共振具有完全相同的单粒子选择定则，因而完整继承了 $2\text{p}2\text{h}$ 张量极化的全部屏蔽效应，使得跃迁截面遭受 $(g_A^{\text{eff}})^4 \approx 0.24$ 的深度淬灭。
   而在无中微子双贝塔衰变（$0\nu\beta\beta$）中，轻子中转由两个核子在核内直接交换虚马约拉纳中微子完成。由不确定性原理 $\Delta p \sim \hbar / \langle r_{12} \rangle$，虚中微子势算符为：
   $$\hat{\mathcal{O}}_{0\nu} = \tau_-^1 \tau_-^2 \frac{1}{r_{12}} \left[ h_A(r_{12}) \boldsymbol{\sigma}_1 \cdot \boldsymbol{\sigma}_2 + h_T(r_{12}) S_{12} + \dots \right]$$
   其特征动量转移高达 $q \approx 100 - 200\text{ MeV}/c$（波长仅约 $1\text{ fm}$，甚至小于单个核子半径）。在此高动量区间：
   - 偶极与高极展开（Multipole Expansion）激发出大量 $J^\pi = 2^-, 3^+, 4^-, 5^+$ 的高阶自旋流，这些高阶算符并不与 $1^+$ 巨共振发生集体相干，无法被张量极化所屏蔽；
   - 两体弱流和高阶多极对 $0\nu\beta\beta$ 的作用需要依赖具体哈密顿量、核素和算符约定的计算；本脚本没有完成这一核基质元计算。
   - 因而本轮只能提出：把低动量 $2\nu$ 的 $q=0.70$ 直接当作 $0\nu$ 的统一缩放因子是待检验的模型假设，不能将 $q_{0\nu}=0.95-0.98$ 写成已证实事实。

## Assumptions

1. **同位旋破缺微扰近似**：假定在计算 Ikeda 求和规则基准时，费米超容许跃迁对等位旋矢量算符的微扰破坏小于 $1\%$；
2. **轻中微子交换机制**：假定 $0\nu\beta\beta$ 纯粹由左手中微子有效马约拉纳质量项介导，略去重中性轻子或超对称流的高动量接触算符。

## Competing Explanations

1. **竞争假说 A：$g_A$ 淬灭是核内核子本征夸克结构的变异，与核多体关联无关**：
   - 当前证据支持把核介质关联、两体弱流和算符动量依赖作为竞争解释；本轮没有完成足以排他的全核素 Chiral EFT 或 $0\nu$ 基质元审计，因此不把“核子本征荷不变”写成已证伪定理。
2. **竞争假说 B：$0\nu\beta\beta$ 也必须像 $2\nu\beta\beta$ 一样遭受四次方重度淬灭（$g_A^4 \approx 0.24$）**：
   - 当前脚本不能排他性证伪该假说；它只能显示两种缩放情景的敏感度差异。Gysbers 等人的第一性原理工作约束了轻中等核中的弱流与 GT 关联，但不能直接替代目标双贝塔核素的完整 $0\nu$ 核基质元计算。

## Transfer Conditions

1. **严禁直接跨类型迁移的判据**：
   - 严禁将低动量允许 $\beta$ 衰变或 $2\nu\beta\beta$ 实验拟合出的经验淬灭常数 $q \approx 0.70$（$g_A^{\text{eff}} \approx 0.90$）直接作为整体缩放因子套用于无中微子双贝塔衰变（$0\nu\beta\beta$）核基质元计算；
   - 严禁将轻核区（$p$ 壳，$A \le 16$）测得的温和淬灭值（$q \approx 0.88$）直接套用至重核区（Sn, Pb）；
2. **当前可迁移的工作判据**：
   - 动量依赖应被显式建模；低动量允许 GT 的经验 $q$ 不能自动充当所有高动量多极算符的统一缩放。具体恢复幅度需由目标核素的算符、两体流和核波函数共同计算。

## Failure Conditions

1. **超容许费米跃迁（$\Delta T=0, \Delta J=0, 0^+ \to 0^+$）**：费米跃迁受弱矢量流守恒（CVC）严格保护，矢量耦合常数在核介质中严格不发生淬灭（$g_V^{\text{eff}} \equiv g_V^{\text{free}} = 1.000$），淬灭概念在此完全不适用；
2. **极高温度超新星塌缩核心（$T \ge 3.0\text{ MeV}$）**：在高温超新星核心环境中，热布居激发出大量非简并高位激发态，热涨落对消弱了张量极化关联，淬灭因子在高温下发生显著热退相干软化。

## Falsification or Reverse Tests

1. **高分辨 $(^3\text{He}, t)$ 连续区积分反证**：
   - 在 $^{90}\text{Zr}$ 与 $^{208}\text{Pb}$ 中，早年 $(p, n)$ 实验宣称仅观测到 $55\%$ 的 Ikeda 强度；而 RCNP 大阪团队利用高分辨磁谱仪将本底干净扣除并积分至 $E_x = 50\text{ MeV}$ 时，测得总恢复强度达到理论和规则的 **$90 \pm 5\%$**；这直接反向证伪了“缺失强度彻底消失于夸克内部”的极端假说，证实缺失强度实际上是散落在高能张量连续区；
2. **$^{100}\text{Sn}$ 衰变端点敏感性反证**：
   - Hinke 2010 测得的超大 $B(\text{GT}) \approx 9.1$ 早期被误传为“无淬灭超 GT 跃迁”；后经相空间五次方幂律敏感度（$d\ln f / d\ln E_0 \approx 5.0$）严格对账，证实端点低估修正后其真实强度退回至约 $B(\text{GT}) \approx 5.5$（对应标准淬灭 $q \approx 0.70$），反向排除了单一核区出现超自然无淬灭孤岛的可能。

## Open Questions

1. 在处于极端同位旋的质子滴线核中，质子连续谱衰变共振态是否会对轴矢量介质流产生反常的库仑张量去极化？
2. 现代格点量子色动力学（Lattice QCD）在包含轻夸克质量自洽外推后，能否直接从夸克胶子层面第一性定出核介质中双核子接触弱轴矢量顶角的绝对数值？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究全面自审：脚本可靠地展示了质量依赖淬灭和低动量/高动量缩放假设的敏感度差异，但没有逐条重建 GT 实验数据库，也没有完成目标核素的 $0\nu$ 核基质元计算；因此本页的 $q(A)$、高阶多极占比和 $q_{0\nu}$ 均保持 `provisional`，不能写成实验事实或普适硬阈值。

## Promotion or Rejection History

- 2026-10-30: Checkpoint 036 建立；脚本 `system/scripts/day27_gt_ga_quenching_cross_mass_study.py` 验证通过；输出结果沉淀至 `continuation-studies/gt-ga-quenching/gt_ga_quenching_results.json`；完成全量结构化元数据登记与索引同步。
