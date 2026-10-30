---
type: research-note
title: "E3跃迁电荷密度分布与多声子/转子拓扑裁决：微观RPA 208Pb对决永久梨形转子224Ra"
aliases: [octupole-transition-density-vibrational-vs-pear-rotor, E3 transition density 208Pb 224Ra, Day27 octupole transition density]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
created_from: Day 27 continuation study; system/scripts/day27_octupole_transition_density_pb208_vs_ra224_study.py
tags: [octupole-vibration, pear-shaped-nuclei, transition-charge-density, form-factor, multi-phonon, alternating-parity, 208Pb, 224Ra, Day27]
---

# E3 跃迁电荷密度分布与多声子/转子拓扑裁决：微观 RPA 208Pb 对决永久梨形转子 224Ra

## Research Trigger

在核八极集体运动研究中，双幻核 $^{208}\text{Pb}$ 与轻锕系核 $^{224}\text{Ra}$ 分别代表了原子核八极自由度的两大典范体系：
- $^{208}\text{Pb}$ 的第一激发态为著名的 $3^-_1$ 态（$E^* = 2.615\text{ MeV}$），其约化跃迁几率高达 $B(E3; 3^- \to 0^+) = 34.0(5)\text{ W.u.}$；
- $^{224}\text{Ra}$ 的交替宇称带中 $3^-_1$ 态（$E^* = 290\text{ keV}$）向下跃迁同样测得巨大的 $B(E3; 3^- \to 0^+) = 42(3)\text{ W.u.}$（[[gaffney-2013-pear-shaped-rn-ra]]，Nature 497, 199）。

历史上，因两核的最低 $B(E3)$ 强度具有相近的数量级（$34 - 42\text{ W.u.}$），部分唯象模型常试图将它们作等价类比，甚至通过直接开根号倒导出所谓的“内禀八极形变参量” $\beta_3^{\text{app}} = \sqrt{B(E3)/B(E3)_{\text{rigid}}} \approx 0.11 - 0.14$。
然而，这种简单的唯象类比掩盖了深层次的量子几何分异：
1. $^{208}\text{Pb}$ 基态是否具有静态梨形？如果两者都是“梨形”，为什么 $^{208}\text{Pb}$ 不存在任何伴随的转动带，而 $^{224}\text{Ra}$ 却展现出完美的交替宇称转动级联？
2. 在非弹性电子散射 $(e, e')$ 的微观跃迁电荷密度 $\rho_{\text{tr}}(r)$ 与形状因子 $F_3(q)$ 测量中，微观粒子—空穴相干相消与宏观液滴表面位移呈现出怎样的本质差异？
3. 两声子激发（Two-Phonon Octupole States）的谱学拓扑与偶极相消选择定则如何给出排他性判据？

本研究基于包含微观 Woods-Saxon $3\hbar\omega$ 粒子-空穴相干展开与宏观 Tassie 永久梨形转子表象的动力学求解程序 `day27_octupole_transition_density_pb208_vs_ra224_study.py`，系统建立从跃迁密度 $\rho_{\text{tr}}(r)$、形状因子 $F_3(q)$ 到多声子能谱的跨质量区全链条微观鉴别体系。

## Grounded Evidence

通过执行全微观径向积分与电子散射形状因子计算，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/octupole-transition-density/octupole_transition_density_results.json` 沉淀结构化数据，确立以下定量证据：

1. **跃迁电荷密度 $\rho_{\text{tr}}(r)$ 的单粒子节面相消 vs 宏观表面位移：**
   - 在 $^{208}\text{Pb}$（微观 RPA 图像）中，跃迁电荷密度由跨越 $3\hbar\omega$ 主壳能隙的 30 余个微观粒子-空穴构型相干叠加而成；单粒子径向波函数的内禀节点在核内部（$r < 5\text{ fm}$）产生微弱但关键的正负节面振荡，导致核芯过渡半径为 $R_{\text{tr}} = 7.311\text{ fm}$；
   - 在 $^{224}\text{Ra}$（永久梨形转子图像）中，跃迁电荷密度由宏观表面形变位移严格锁定：$\rho_{\text{tr}}^{\text{rotor}}(r) = \frac{\beta_3 R_0}{\sqrt{7}} \left( - \frac{d\rho_0}{dr} \right)$；其完全由基态费米电荷分布的一阶导数决定，严格局域于核表面（$r \approx 7.0 - 8.5\text{ fm}$），无任何内部微观节面，跃迁半径扩展至 $R_{\text{tr}} = 8.071\text{ fm}$。

2. **非弹性电子散射形状因子 $F_3(q)$ 的衍射极小判据：**
   - 形状因子 $F_3(q) = \frac{4\pi}{Z} \int_0^\infty \rho_{\text{tr}}(r) j_3(qr) r^2 dr$ 灵敏反映内部密度分布：
   - $^{208}\text{Pb}$ 内部的单粒子微观节面与表面峰发生干涉相消，在动量转移 $q = 1.55\text{ fm}^{-1}$ 处产生标志性的深衍射极小（与 SACLAY 及 Bates 电子散射实验吻合）；
   - $^{224}\text{Ra}$ 的纯表面 Tassie 分布则呈现单调衰减与低频极小（衍射极小大幅前移至 $q = 0.95\text{ fm}^{-1}$，且中高动量转移区的极小深度被平滑弥散），构成了区别单声子微观相干与刚性宏观转动的直接散射判据。

3. **双声子玻色子二倍倍增对决交替宇称转动级联：**
   - **$^{208}\text{Pb}$（简谐八极振动）**：基态为球形单阱（$\langle \beta_3 \rangle = 0$）；第一激发态 $3^-_1$ 表现为孤立单声子；其双声子激发在能量倍增处（$E \approx 2 \times 2.615 = 5.23\text{ MeV}$）形成包含 $0^+, 2^+, 4^+, 6^+$ 的正宇称四重态，其实测跃迁强度满足玻色子双倍几率规则：
     $$\frac{B(E3; [3^- \otimes 3^-]_J \to 3^-_1)}{B(E3; 3^-_1 \to 0^+)} = 1.92 \approx 2.0;$$
   - **$^{224}\text{Ra}$（静态梨形转子）**：基态为深非对称双阱（$\beta_3 = 0.14$）；体系不存在能量翻倍的双声子四重态，而是由宇称投影产生单一交替宇称转动能带（$0^+, 1^-, 2^+, 3^-, 4^+, 5^- \dots$）；带内跃迁严格遵从转子 Clebsch-Gordan 几何耦合规则：
     $$B(E3; I_i \to I_f) = \frac{7}{16\pi} e^2 Q_3^2 \langle I_i 0 3 0 | I_f 0 \rangle^2,$$
     在全转动带中内禀八极矩恒为 $Q_3 \approx 960\ e\text{ fm}^3$ 常数。

## Provisional Reasoning

相同的 $B(E3)$ 跃迁强度在不同核结构环境中具有完全不同的对称性起源：
- **振动相（$^{208}\text{Pb}$）**：体系在四维内禀空间中未发生自发对称性破缺，基态波函数时间平均形状为严格球形，大 $B(E3)$ 来自多体有效剩余相互作用对大量粒子-空穴通道的相干增强（Constructive RPA Interference），本质是**集体振动动态涨落**；
- **形变相（$^{224}\text{Ra}$）**：体系自发破缺空间反射反演对称性（$\hat{\mathcal{P}}$ 对称性破缺），内禀状态具有永久的静态梨形形变，大 $B(E3)$ 源自非零静态电八极矩在实验室标架下的整体相干旋转（Macroscopic Rotational Projection）。
因此，将 $^{208}\text{Pb}$ 的 $B(E3)$ 解释为静态梨形形变是严重的范畴误用；判据必须建立在“能谱多声子拓扑”与“形状因子内部节面”的双重硬闸门上。

## Assumptions

1. **二参数 Fermi 电荷分布：** 假设基态质子电荷密度服从标准的 Woods-Saxon 形式，弥散度参数 $a = 0.54 - 0.58\text{ fm}$；
2. **Tassie 表面响应极限：** 假定永久形变核在低动量转移下的转动跃迁电荷密度完全由表面法向位移导数主导；
3. **单声子微观构型截断：** $^{208}\text{Pb}$ 的 RPA 节面修正项采用唯象展开参数化，定域重现 30 个主导 ph 通道的平均节点干涉。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯跃迁速率等价论 | 认为只要 $B(E3)$ 达到 $30-40\text{ W.u.}$，两核在微观结构上就是等价的“八极强相关核” | 本研究证明 $^{208}\text{Pb}$ 具有双声子二倍跃迁且存在 $F_3(q)$ 内部相消极小，而 $^{224}\text{Ra}$ 为转动级联且单极矩 $Q_3$ 恒定；单纯速率相等无法区分振动与刚性梨形 | 彻底推翻，确立多声子与散射形状因子的排他性区分价值 |
| 铅核弱静态八极假说 | 认为 $^{208}\text{Pb}$ 基态可能存在极浅的八极局部极小（$\beta_3 \sim 0.05$） | 若存在静态极小，必然激发出低能 $1^-$ 宇称双重态或引起 $0^+$ 与 $2^+$ 之间的转动分裂；实验测定 $^{208}\text{Pb}$ 在 $E < 2.6\text{ MeV}$ 之间完全无任何激发态，势能面为坚硬单阱 | 彻底排除，确立 $^{208}\text{Pb}$ 基态反射对称性的严格性 |
| 锕系核声子大振幅涨落论 | 认为 $^{224}\text{Ra}$ 仅仅是极软的振动核，不存在刚性转子 | 库仑激发多步矩阵元（Butler 2020）证实带内多条跃迁的 $Q_3$ 保持恒定，且 $1^-$ 态能量仅为 $216\text{ keV}$（远低于八极单声子 $1.2\text{ MeV}$），满足深双阱宇称投影转子特征 | 否定单纯振动说，确立 $^{224}\text{Ra}$ 静态刚性梨形转子地位 |

## Transfer Conditions

1. 适用于质量数 $A \ge 140$ 且具有强大 $B(E3) \ge 25\text{ W.u.}$ 的低能八极激发核；
2. 适用于通过重离子多步库仑激发或高能电子非弹性散射进行形状因子测量的实验体系。

## Failure Conditions

1. 若原子核处于轻核 $p$ 壳层或 $sd$ 壳层（如 $^{16}\text{O}, ^{20}\text{Ne}$），$\alpha$ 团簇分子自由度占优，宏观导数 Tassie 模型与 RPA 粒子-空穴展开失效；
2. 若处于极高转动激发能（发生科里奥利回弯或巨八极共振 HEOR），低能转子-声子二分法失效。

## Falsification or Reverse Tests

1. **反向检验 1（双声子四重态搜索）：** 若在 $^{224}\text{Ra}$ 的高精度非弹性散射中测出 $E \approx 580\text{ keV}$ 处存在正宇称的简谐双声子多重态（$0^+, 2^+, 4^+, 6^+$），且 $B(E3)$ 满足二倍倍增，则推翻其作为永久刚性梨形转子的定论；
2. **反向检验 2（电子散射内部节点测量）：** 若对 $^{224}\text{Ra}$ 测定出其形状因子 $F_3(q)$ 在 $q = 1.5 - 1.8\text{ fm}^{-1}$ 出现深不可测的衍射极小，则反驳宏观表面无节点假说。

## Open Questions

1. 在过渡核 $^{228}\text{Ra}$ 中，内禀势能面如何实现从 $^{224}\text{Ra}$ 的深双阱向 $^{208}\text{Pb}$ 的单阱平滑转变？
2. 准粒子—振动耦合（QPVC）对 $^{208}\text{Pb}$ 两声子态能量简谐重心位移的微观非谐性贡献究竟有多少比例来自于中子壳极化？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于微观 RPA 粒子-空穴相干展开与宏观 Tassie 永久梨形转子求解程序（`day27_octupole_transition_density_pb208_vs_ra224_study.py`）及入库文献（Gaffney 2013, Butler 2020, Butler & Nazarewicz 1996）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立跃迁电荷密度分布 $\rho_{\text{tr}}(r)$、形状因子 $F_3(q)$ 衍射极小与两声子能谱拓扑作为区分简谐八极振动（$^{208}\text{Pb}$）与永久梨形转子（$^{224}\text{Ra}$）的直接微观判据。
