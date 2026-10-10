---
type: synthesis
title: "Chirality, wobbling and competing explanations in high-spin bands"
aliases: [手征与 wobbling 竞争解释证据综合]
created: 2026-09-21
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
scope: high-spin-chirality-wobbling-competition
confidence: low
sources: [mukhopadhyay-2007-135nd-chiral-vibration-static, mukhopadhyay-2008-136nd-transition-rates, petrache-2006-near-degenerate-chiral-misinterpretation, guo-2024-chiral-wobbler-74br, chakraborty-2023-131xe-wobbling-origin, lv-2021-tilted-precession-135nd, grodner-2018-128cs-chiral-g-factor, grodner-2011-bm1-staggering-structural-composition, grodner-2006-128cs-chiral-doublet-lifetimes, chen-2017-128cs-angular-momentum-projection-chirality, koike-2003-128cs-chiral-doublet-bands, suzuki-2008-lifetimes-103rh-104rh, lange-kumar-hamilton-1982-multipole-admixtures, zhu-2003-135nd-composite-chiral-pair, lv-2019-chirality-135nd-reexamined]
tags: [chirality, wobbling, gamma-softness, shape-coexistence, evidence-map]
---

# Chirality, wobbling and competing explanations in high-spin bands

## Question and Scope

This page compares candidate labels across nuclei while preserving band identity, observable type, source dependence and model assumptions.

## Evidence Matrix

| Evidence | Supports | Does not establish alone |
|---|---|---|
| Near-degenerate same-parity `ΔI=1` bands | Candidate partner relationship | Chirality; crossings and configuration mixing can mimic it |
| Similar alignment and `B(M1)/B(E2)` | Stronger partner test | A universal static geometry |
| E2-dominated interband links and energy dependence | Wobbling candidate | One-phonon identity without band mapping and lifetimes |
| Low-`|δ|` M1-dominated `ΔI=1` links | Ordinary signature-partner interpretation in the `131Xe` yrast/yrare comparison | This is a different nucleus and does not classify the `135Nd` D5/D6 pair; `135Nd` markers still lack a line-resolved δ/E2 fraction. ([[chakraborty-2023-131xe-wobbling-origin]] C23-2/3/7) |
| `135Nd` D1/TiP1/TiP2 mixing-ratio control | Lv 2021 measures TiP1→D1 `δ=-0.32(5), -0.48(14)` and TiP2→TiP1 `δ=-0.26(8)`, with quoted E2 fractions about 6–19%; the authors treat selected links as M1-dominated and reject wobbling for these bands in favor of tilted precession. | Same isotope, but different bands/campaign from MU07 D5/D6; the measured mixing-ratio pattern must not be transferred as a D5/D6 assignment. ([[lv-2021-tilted-precession-135nd]] LV21-9/10/11/17) |
| Aplanar TAC/PRM geometry | Model support | Direct laboratory observation of handedness |
| g factor or TDPAD geometry | Core/particle angular-momentum constraint | Complete band interpretation without transition strengths |
| γ-band staggering / γ-soft model result | Shape-dynamics comparison | Unique γ-rigid or chiral assignment |

## Synthesis

Mukhopadhyay 2007 supplies a strong, nucleus-specific chiral-vibration to static-chirality strength pattern in `135Nd`. Mukhopadhyay 2008 and Petrache 2006 show why the same reasoning cannot be transferred from energy proximity alone. Guo 2024 supplies a rich `74Br` chiral-wobbler candidate with ADO, polarization, DSAM and PRM; its attached supplement closes the transition table but not the configuration/model dependence. Grodner 2018 provides a geometry-sensitive `128Cs` counterexample where the bandhead is nearly planar. The evidence therefore supports a graded candidate map rather than one universal fingerprint checklist.

Chakraborty 2023 adds an experimental `131Xe` control: small E2 admixtures in selected `ΔI=1` links support an unfavoured signature-partner reading of the studied sequence and lead the authors to exclude wobbling for that sequence despite a triaxial model context. This demonstrates how line-resolved mixing ratios can distinguish an alternative in one case; it is not transferable proof about `135Nd`, whose MU07 graph points are not transition-indexed.

Lv 2021 adds a same-isotope but different-band control: measured low-|δ|/M1-dominated TiP1→D1 and TiP2→TiP1 transitions support the authors' tilted-precession reading rather than their predominant-E2 wobbling criterion. This shows that `135Nd` contains another measured mode-discrimination example, but D1/TiP bands cannot be merged with MU07's D5/D6 chiral pair.

The same Lv 2021 measurement gives Table-II mixing ratios `δ=-0.32(5), -0.48(14)` for the two reported TiP1→D1 links and `-0.26(8)` for TiP2→TiP1, corresponding to quoted E2 fractions of about 6–19% (LV21-9/10). This supplies a concrete same-nucleus example of line-resolved electromagnetic mode discrimination while preserving the different-band and different-campaign boundary.

### `135Nd` model evolution: 3D-TAC and TAC+RPA

Zhu 2003's 3D-TAC calculation describes planar angular-momentum orientation at lower frequency, an aplanar/static-chirality interval near `I≈19`, and a return toward planarity at higher frequency; the authors call the static interval transient. Mukhopadhyay 2007's TAC+RPA treatment likewise associates low-spin behavior with chiral vibration and the critical-frequency approach with a softening RPA mode and static-chirality onset, about one spin unit above the closest experimental partner-band approach. These are qualitatively compatible descriptions of the onset for the same `135Nd` band pair, not independent experimental confirmations. The MU07 plotted B(E2) out/in central estimates rise from about `0.14` at `31/2−` to `0.50` at `37/2−`; an endpoint sensitivity check separates the first two increments but the `35/2−` and `37/2−` ranges overlap, and no `39/2−` interband marker is present. This is consistent with spin-dependent interband strength but cannot locate a static onset from the plotted values. Preserve the 2003 high-spin return-to-planarity prediction; do not read the 2007 local onset result as proof that a static regime persists indefinitely. The model curves and geometry remain theory results, separate from Zhu's level-scheme experiment and MU07's distinct DSAM lifetime/strength campaign.

### `135Nd` 电磁比值判别卡（DAY10）

这张卡把 MU07 的中心值复算与模式解释分层，保留 `135Nd` D5/D6（早期称 Band A/B）的线身份、误差和模型边界。

| Evidence layer | Direct source or calculation | Interpretation limit |
|---|---|---|
| Intraband strengths | MU07 Table I 给两带寿命及由 DSAM 派生的 `B(M1)`、`B(E2)`；同初始自旋的两带中心值接近（[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-1/5/7）。 | `B` 与 lifetime 来自同一测量链；中心值商不产生第二份独立证据，39/2 的弱 `B(E2)` 分母特别敏感（MU07-14/15）。 |
| Interband strengths | Figs.2–3 的开圆点是 Band B→Band A 实验点；曲线分别是 TAC intraband 与 RPA interband 计算（MU07-6/8）。四个图估 E2 out/in 中心值约为 `0.14, 0.24, 0.48, 0.50`，M1 out/in 约为 `0.031, 0.057, 0.036, 0.11`（31/2−–37/2−）。 | 开圆点不是逐线表列值；覆盖/协方差未给，后两个 E2 输入端点范围重叠，且 39/2− 没有带间点（MU07-8/13/15）。 |
| 作者的模式解释 | TAC+RPA 把低自旋区描述为取向振动，并把 RPA 能量软化到零后、约比实验双带最近点高一个单位自旋的解解释为 static chirality onset（MU07-2/3）。 | Onset 是依赖 TAC/RPA 的模型结果；局部强度趋势与此解释相容，但不能由 `B(M1)/B(E2)` 单独证明几何或静态区持续范围。 |
| 独立几何量 | `128Cs` bandhead 的 `g=+0.59(1)` 由两个 TDPAD 测量报告（[[grodner-2018-128cs-chiral-g-factor]] GR18-1）。PRM+CDFT 以 `⟨ô⟩≈0.15` 解读为近 planar（GR18-3/4）。 | g 因子是直接测得的磁矩量；近 planar 是模型几何解释。不同核素和 TDPAD/DSAM 链形成比较控制，不是 MU07 的独立重复。 |
| 替代机制 | `136Nd` 两条近简并负宇称带在 `I≈17ℏ` crossing 附近出现明显不同的 `B(E2)`（约 2–3 倍），作者以不同组态/带混合解释（[[mukhopadhyay-2008-136nd-transition-rates]] MU08-1/2/3/4）；另有 `103,104Rh` 中 `B(M1)` 下降、弱 ratio staggering 定位在 `B(E2)` 分母（[[suzuki-2008-lifetimes-103rh-104rh]] SU08-8/13）。 | 两者均为不同核素的比较，不直接否定 `135Nd`；SU08 的 `B(M1)` 还依赖 pure-M1 和先前 branching 输入（SU08-7）。MU08 是独立 `136Nd` 4n/DSAM 数据集，但属同一 Gammasphere/DSAM 方法链。 |

#### 中心值复算与单位

按 MU07 Table I 打印中心值直接相除，匹配自旋的带内商为：

| `I` | Band A `B(M1)/B(E2)` | Band B `B(M1)/B(E2)` | Band B/A quotient-of-quotients |
|---|---:|---:|---:|
| 31/2− | 7.8125 | 9.6429 | 1.2343 |
| 33/2− | 6.8750 | 7.5000 | 1.0909 |
| 35/2− | 7.5000 | 7.8571 | 1.0476 |
| 37/2− | 5.3125 | 5.8621 | 1.1034 |
| 39/2− | 16.1538 | 17.2727 | 1.0693 |

前两列的单位均为 `μN²/(e²b²)`，是 Table I 派生 B 值的复算商，不是无量纲量，也不等于同一跃迁的 `δ²`。同一条 M1/E2 混合跃迁才满足 `δ² = Tγ(E2)/Tγ(M1) = [0.835 Eγ(MeV)]² × B(E2)[e²b²]/B(M1)[μN²]`（[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1）。Table I 按初始自旋列值但未逐行列 `Eγ`/终态自旋；在缺少经核实的具体线映射时，不从商反解 `δ`。39/2− 的 `B(E2)=0.13(3),0.11(3)` 较弱；把括号端点当作矩形输入范围只得 `11.25–24.0` 与 `11.43–27.5` 两个重叠敏感区间，不是置信区间（MU07-14/15）。

`Tγ(XL) ∝ Eγ^(2L+1) B(XL)`，因此 B-strength out/in 也不是 photon-branch out/in。例如 31/2− 的 M1 图估商 `0.084/2.7≈0.0311`；只有采用候选 `648/226 keV` 线映射、同一母态与 M1 分量的条件下，`Γγ,out/Γγ,in≈(648/226)^3×0.0311≈0.73`。这是条件性 partial-rate 变换，不是实测计数比或完整支路比（MU07-8/10；[[zhu-2003-135nd-composite-chiral-pair]] ZH03-3）。E2 out 点的身份还可读作 ΔI=1 mixed-line 的 E2 分量或 ΔI=2 crossover；31/2− 两种候选能量会给出约 `27` 与 `138` 的不同条件率商，且两种读法都要求 Table-I E2 分母与特定带内线相配。2019 Table I 只核对较晚 campaign 中的候选线类，未绑定 MU07 空圆（[[lv-2019-chirality-135nd-reexamined]] LV19-9；MU07-10/11/16）。因此不以这组条件数值定位静态模式起点。

`Q_t` 也不由无标记的 B(E2) 列唯一给出：需要明确是哪条 E2 线、能量/自旋映射以及适用的 `K` 或转子矩阵元。这里的图估带间点尚未与具体 ΔI=1 mixed link 或 ΔI=2 crossover 唯一对应；因此保留为待判，不报告唯一 `Q_t`。

#### 独立性与最小判别组合

- MU07 Table I、Figs.2–3 的带内值和开圆带间值属于同一 `100Mo(40Ar,5n)` Gammasphere/DSAM strength chain，不是互相独立的测量。Zhu 2003 给早期 partial scheme，Lv 2019 给后续 campaign 的线类 cross-check；这些来源帮助限制 transition identity，但不把它们的能量或 B 值倒灌成 MU07 的实测绑定（MU07-6/9/15；ZH03-3；LV19-9）。
- 能支持该模型解释的组合至少要保持：逐线身份与分支账本、同线的 mixing-ratio/偏振信息、伙伴分辨寿命和绝对强度、以及与模型独立的几何或组态观测。缺项时，强度相似或 out/in 趋势只提高候选一致性，不足以唯一判静态手征。
- 目前判决为 **supports with limits**：MU07 的寿命派生 partner strengths 和 E2 带间上升与作者的振动→静态 TAC+RPA 图景相容；Suzuki 的分母反例与 Grodner 的模型依赖几何对照限制比值的唯一性。没有新证据改变 `135Nd` 的候选层级或把模型 onset 升为实验事实。

### B(M1) staggering is structure-dependent (Grodner 2011)

Grodner 用 R_yT 对称与相位约定推导强手征极限下的带内/带间振幅，并指出 B(M1) staggering 还要求特定的奇粒子组态和三轴芯性质；它不是由手征对称性单独保证的普遍指纹（[[grodner-2011-bm1-staggering-structural-composition]] GRODNER11-1/2/3/4/5/6/8/9）。作者将 Cs 的强交错与单粒子结构联系，并把 104Rh/135Nd 的弱交错或缺失解释为不同结构/极限（GRODNER11-7）。

该文的 128Cs 输入引用 Grodner 2006，135Nd 输入引用 MU07，因此它是既有数据的理论解释，不增加独立实验行（GRODNER11-10/11）。这条解释限制“有 M1 交错即可认定几何”，也限制“无交错即可排除手征”：结构与对称极限都影响该观测量。

### Hamamoto 2011：特殊模型下的 A 量子数跃迁规则

Koike, Starosta & Hamamoto 2004 是该规则的理论前身：同样以 gamma=90°、同单-j 质子粒子/中子空穴和 A 对称构造 E2/M1 强弱关系（[[koike-2004-chiral-bands-selection-rules]] KOIKE04-1/2/3/4）。2004 文明确说明 selection rule 对其 Hamiltonian 的任何本征态都成立，不以实现手征几何为条件；Hamamoto 2011 因而不是独立的几何验证（KOIKE04-5/11；HM11-16/17）。

Hamamoto 在同一单-j 壳的质子粒子—中子空穴构型、gamma=90°（Lund 约定 gamma=-30°）与指定粒子-转子算符下构造对称算符 A。对集体芯 E2，delta-C=0 与 delta-R3 非零导出 delta-A 非零；指定 g 因子下 M1 的强度也偏好 delta-A 非零。图2(a)把这些条件画成允许的 E2 与较强 M1 跃迁，图2(b)的计算在 13<I<24 给出近简并伙伴带，图3显示模型几何只在中等自旋可能呈手征（[[hamamoto-2011-selection-rule-chiral-geometry]] HM11-1/5/7/8/9/10/11/12）。

作者称 128Cs 与 126Cs 的已报电磁性质符合该规则，但引用的 128Cs 实验是 Grodner 2006，故不增加独立转移强度数据；同一文章总结 134Pr 的两条带内 B(E2) 至少相差约两倍，且若干 M1 跃迁违反规则（HM11-13/14/15/17）。后两者是作者对既有数据的概述。它们使选择规则成为有边界的模型判据，而非可从能量近简并或 B(M1)/B(E2) 单一趋势直接读取的几何量。

| 判据层 | Hamamoto 模型给出的测试 | 证据边界 |
|---|---|---|
| E2 与对称量子数 | 在指定集体芯算符下，E2 需 delta-A 非零 | 需要对应态的 A 赋值和逐线跃迁强度；实验带标签本身不给出 A |
| M1 强弱 | 指定粒子-转子 M1 算符下，delta-A 非零跃迁较强 | 强弱依赖同-j 构型、质子-中子交换对称性与选定 g 因子 |
| 规则与几何的区分 | Koike 2004 也给出同一 A 对称下的 E2/M1 强弱预期 | 2004 文明确说规则适用于其 Hamiltonian 的任意本征态、无论是否形成手征几何；规则吻合本身不足以证明几何（KOIKE04-3/4/5） |
| 双带与几何 | 计算模型在中等自旋有近简并和非共面候选区 | 是该模型的数值结果，不是实测几何 |
| 跨核检验 | 作者称 Cs 数据与规则相容、134Pr 比较不相容 | 128Cs 数据复用 Grodner 2006；Petrache 2006 的 branch-derived Q0,1/Q0,2=2.0(4)为 134Pr E2 非等价提供直接文献定位（PE06-2），但不是 Hamamoto M1 违例的逐线复核，且属于同文引用的既有证据 |

适用边界是明确的：gamma、构型、算符截断和 g 因子偏离该极限都可能改变选择规则；近简并本身也不保证 A 对称赋值适用（HM11-16）。因此本轮决策为 **limits**：加入一个可测试的对称量子数判据，同时保留其模型条件与数据谱系。

### 126Cs 独立实验比较：电磁比值与判据边界

Wang 2005 thesis reports a separate 126Cs experiment: 65-MeV 116Cd(14N,4n) at NORDBALL, about 8×10^8 gamma-gamma events, and an expanded Band 1–7 level scheme (WS05-1). For positive-parity Bands 1–2 it reports similar pre-crossing alignments, comparable branch-derived B(M1)/B(E2) ratios, and odd-even staggering; several bandhead spins remain tentative (WS05-2/3). The author interprets the pair as a chiral candidate using a particle-rotor calculation with epsilon2=0.244 and gamma=-24° (WS05-4).

Wang 2005 thesis Sec. 4.3 对其 Ref. [34] Koike et al. 2004 的 M1 规则作了相反转述：它称同 A 态间更易发生 M1、异 A 态间 M1 禁止（[[wang-shouyu-2005-126cs-123i-chiral-thesis]] WS05-7）；而 Koike 2004 的原文称同 A 的 M1 matrix elements 约比异 A 小一个数量级，且 Hamamoto 2011 保持同一方向（[[koike-2004-chiral-bands-selection-rules]] KOIKE04-4；[[hamamoto-2011-selection-rule-chiral-geometry]] HM11-8）。Wang 的 E2 方向（同 A E2 近禁戒）与 Koike04相符，但 M1 方向存在未解决的 source-level conflict。故不能把 126Cs 的 B(M1)/B(E2) ratio similarity 当成 Koike/Hamamoto M1 selection-rule 的验证；暂不以“不同约定”或“笔误”替任何来源消解差异。

This is a distinct isotope/reaction/array from the 128Cs Koike/Grodner campaigns, so it adds a separate experimental comparison. It does not provide an independent replication of the 128Cs result or a direct measurement of Hamamoto's A quantum number. The thesis reports ratios and model interpretation, not a partner-resolved absolute B(E2)/B(M1) matrix; it also uses 134Pr as a counterexample to universal energy/staggering criteria (WS05-5).

| Evidence layer | 126Cs result | Relevance to the A-rule test |
|---|---|---|
| Experimental setup and scheme | 65-MeV 116Cd(14N,4n), NORDBALL; Bands 1–7 and tentative bandhead assignments (WS05-1/2) | Separate isotope data, but spin uncertainty propagates into transition matching |
| Electromagnetic ratio | Comparable Band 1/2 B(M1)/B(E2) with odd-even staggering (WS05-3) | Ratio compatibility is not the same as absolute, line-resolved A-changing strength |
| Author/model interpretation | Positive-parity pair is “very likely” chiral in the thesis; PRM comparison uses epsilon2=0.244, gamma=-24° (WS05-4) | Model support is conditional; no experimental A labels or direct geometry |
| Counterexample handling | Thesis cites 134Pr alignment, ratio, and lifetime differences as a non-universal case (WS05-5) | Supports retaining crossings/configuration and shape alternatives |


### 126Cs 的独立 DSA 强度实验：Grodner et al. 2011

Grodner et al. 使用 120Sn(10B,4n)、55 MeV 与 Warsaw/OSIRIS II 数据链，对 126Cs 测得 13 个寿命并由寿命/分支派生 26 个绝对转移概率（Tables 1–2；GR126-1/2/3/4/5）。这与 Wang 2005 thesis 的 116Cd(14N,4n)/NORDBALL acquisition 不同，是一条独立的 126Cs DSA 数据集；但该实验引用 Wang et al. 2006 作为 ΔI=1 pure-M1 / multipolarity 依据，故 level/multipolarity provenance 仍需分层。

论文报告 126Cs partner bands 的 inband B(E2)/B(M1) 大致相近、spin-dependent inband M1 staggering，并在 Fig.3 中报告 interband B(M1) staggering 与 inband staggering 反相；作者据此称观察到 Koike 2004 预测的一组电磁选择规则（GR126-6/7/12）。它把 126Cs 的证据提升到 lifetime-derived absolute strengths 和 interband M1 pattern 层，但 A 量子数仍不是观测标签。作者同时强调 M1 staggering 还依赖 S-symmetry 所需的 same-j particle-hole configuration 和大三轴形变，不由手征几何单独保证（GR126-8/9）。

来源图3的像素文件未从本轮可访问的 INSPIRE XML endpoint 取得；因此这里只记录其 caption/正文报告的相位关系，不对 interband B(M1) 点做像素读数。Tables 1–2 的定量输出是绝对 B 值，但图形线身份和 Wang thesis 对 Koike M1 规则的反向转述仍保留为未解决边界。Bhat et al. 2014 Ref. [18] 重用这组测量，不作为第二份 126Cs 实验（BHA14-7）。


### Wang 2006 NORDBALL 线表与比值重算

Wang et al. 2006 明确重分析 Komatsubara 1993 的同一 NORDBALL 116Cd(14N,4n)126Cs coincidence acquisition；王守宇 2005 thesis 因而不是第二份 126Cs 观察数据。Wang06 新增扩展能级图、Table I 的 gamma intensity/ADO/spin table 和由同一数据派生的 B(M1)/B(E2)、B(M1)in/B(M1)out ratios，不含寿命或 absolute B（[[wang-2006-126cs-candidate-chiral-doublet]] WS06-1/2/3/4/7/11；[[wang-shouyu-2005-126cs-123i-chiral-thesis]] WS05-1）。

用 Koike 2003 Eq.(7) 的同母态强度式，在 delta=0 的 pure-M1 假设下重算 Table-I 的 I=14、15 中心值：

B(M1)/B(E2) = 0.697 × Eγ(E2,MeV)^5 / Eγ(M1,MeV)^3 × Iγ(M1)/Iγ(E2) × 1/(1+delta²).

| Band / I | Eγ(M1) (keV), Iγ(M1) | Eγ(E2) (keV), Iγ(E2) | B(M1)/B(E2), μN²/(e²b²) |
|---|---|---|---:|
| yrast 14+ | 343.2, 17.8(2.6) | 739.2, 48.2(5.5) | 1.41 ± 0.26 |
| yrast 15+ | 463.5, 26.7(2.5) | 807.0, 12.6(1.6) | 5.08 ± 0.80 |
| side 14+ | 344.4, 6.4(1.0) | 671.1, 5.7(0.8) | 2.61 ± 0.55 |
| side 15+ | 426.5, 11.7(1.5) | 771.0, 9.4(1.2) | 3.05 ± 0.55 |

The errors propagate only the printed relative-intensity errors as independent statistical terms; no covariance, efficiency-systematic or line-specific delta is provided. The central odd/even factor is 3.61 in yrast and 1.17 in the side band, matching the paper’s stronger yrast and weaker side-band staggering. This reconstructs relative-strength fingerprints from the shared NORDBALL data, not an absolute lifetime-based B value or an A-state assignment (WS06-4/7/8; KOIKE03-9).

### 126Cs branch-derived ratio sensitivity to differential mixing

Using the same Eq. (7) factor `1/(1+δ²)`, a conditional line-specific treatment gives `R_i(δ_i)=R_i(0)/(1+δ_i²)`. The odd/even ratio is therefore `S(δ)=S(0)(1+δ_even²)/(1+δ_odd²)`. A common δ for both spins cancels from S; a spin-dependent δ does not. From the rounded Table-I reconstructions above, `S(0)=5.08/1.41=3.60±0.87` for yrast and `3.05/2.61=1.17±0.32` for the side band, propagating only the printed intensity errors as independent terms. If the even-spin branch is set to δ=0, the central-value odd-spin magnitudes that would reduce S to 1 are about 1.61 and 0.41, respectively. As an illustration only, δ_odd=0.50 and δ_even=0 give S≈2.88 for yrast but S≈0.94 for the side band. These are sensitivity scenarios, not measured mixing ratios; the paper gives no line-specific δ or covariance, and the side-band central staggering is already modest relative to its intensity-only uncertainty. This makes a line-resolved mixing-ratio measurement a necessary companion for testing whether the weak side-band alternation is robust (WS06-7/8).

Grodner et al. 2011 say that their DSA extraction treats ΔI=1 branches as pure M1 because the cited Wang06 estimate places the E2 admixture below 10% (GR126-10). As a conditional translation only, if “10%” means `f_E2=Iγ(E2)/(Iγ(M1)+Iγ(E2))<0.10`, then `δ²=f_E2/(1−f_E2)<1/9`. Allowing odd- and even-spin branches to take any values within that bound gives `S/S(0)` between 0.90 and 1.11; the side-band central factor would remain about 1.05–1.30. This nominal bound is not an independent line-by-line measurement: it is a cited pure-M1 assumption, and the side-band `1.17±0.32` intensity-only estimate still includes unity. It narrows the illustrative large-δ scenario under the paper’s assumption, while leaving the need for direct δ and covariance data intact (GR126-10; WS06-7/8).

Grodner et al. 2011 later measured a separate Warsaw/OSIRIS II DSA data set with lifetimes and absolute B values. It uses Wang06 Ref. [12] for transition/multipolarity context; this does not make the NORDBALL and DSA acquisitions the same data (GR126-1/2/3/10).

### 126Cs DSA Table 1/2 与 NORDBALL 的线能交叉核对

Grodner11 DSA Tables 1–2 的 I=14–17 初始自旋与 M1/E2 γ 能量可同 Wang06 Table I 对上，最大圆整差为 0.9 keV。DSA 的 `B(M1)/B(E2)` Weisskopf-unit quotient 在 I=15/14 给出 yrast 6.96、side 2.40；Wang06 Table-I intensity reconstruction 给出 3.60、1.17。两条独立反应/数组链在这个自旋窗口都保留“yrast 的中心交错强于 side-band”的排序，但数值幅度不同。它是跨采集的一致性检查而非重复计数；Grodner11 的 pure-M1 多极性依据仍引用 Wang06（GR126-4/5/10；WS06-4/7/8）。

不能把该排序推广为一条连续稳定的比值律：Grodner11 Table 1 的 I=16+ yrast 415-keV in-band M1 是 `≤0.02 W.u.`，而同一初始自旋的 253-keV M1 分支为 0.45 W.u.、但末态带标签未给出，不能替代该上限。Table 1/2 的匹配分支中心 quotient 在 I=17/16 给出 yrast 下限约 11.45、side 约 0.23；联合 B-value covariance 不可得，因此不报不确定度或显著性。A/S 标签仍未观测，电磁比值不单独判定几何（GR126-4/5；WS06-4）。


### Prochniak 2011：CPHC 的 S 对称与 M1 交错机制

Prochniak et al. 定义 S=PαCπν：Pα 是五维形变坐标空间的 alpha-parity（不是普通空间宇称），Cπν 交换质子粒子与中子空穴。若核心 Bohr 哈密顿量在 Pα 下不变，CPHC 本征态可标记 s=±1；same-s E2/M1 矩阵元在模型条件下受到抑制（[[prochniak-2011-cphc-s-symmetry-transition-rules]] PS11-1/2/3/4/5/7）。

该 S 对称与 Koike04 的 A 算符不同。S 论文在 gamma-soft Wilets–Jean core 中保留 S-invariance；刚性 Davydov–Filippov core 需最大三轴 gamma=π/6。对 A≈130 输入 gR=0.44、gπ=1.22、gν=−0.21，有 gR−(gπ+gν)/2 = −0.065；这离严格零值不远，模型因此得到 same-s M1 非零但较小的预期（PS11-5/6/7/8）。这是 model-parameter check，不是测得的 126Cs g factors。

Grodner 2011 126Cs DSA 论文引用此 S-symmetry 工作解释 interband/inband B(M1) 相位交错，并指出 stagger 不能只归因于 chirality（[[grodner-2011-126cs-chiral-selection-rules]] GR126-8/9）。因此 S-symmetry 为 M1 staggering 提供额外机制；它不能替 Koike A 标签或逐线数据，也不消解 Wang05 thesis 对 A-rule M1 方向的转述冲突（WS05-7；KOIKE04-4）。

### A 与 S 对称量子数的区别

| 项目 | Koike/Hamamoto 的 A | Prochniak 的 S |
|---|---|---|
| 对称算符 | 中间主轴转动与质子—中子交换的组合（KOIKE04-2；HM11-5） | 形变坐标空间 alpha-parity Pα 与质子—中子交换 Cπν 的组合；Pα 不是空间宇称（PS11-1/2） |
| 模型条件 | gamma=90°、同单-j 质子粒子/中子空穴的特殊粒子-转子 Hamiltonian（HM11-1/2） | CPHC Hamiltonian，核心 Bohr Hamiltonian 需满足 Pα 不变；同-j 空间（PS11-3/7） |
| M1/E2 强弱 | 同 A E2 禁戒；同 A M1 较弱（KOIKE04-3/4） | 同 s 的 E2 受抑；特定 g 因子组合下同 s M1 抑制（PS11-4/5） |
| 几何含义 | 规则可适用于未形成手征几何的模型本征态，因此一致性不是充分几何证据（KOIKE04-5） | S 对称及其交错是 Hamiltonian 结构特征，不能直接当作实测非共面几何（PS11-7/9） |

现有来源没有给出实验能级的 A 与 s 逐态映射。将两组量子数并作一个标签会掩盖 Wang05 的 A-rule 转述冲突和 Grodner11 的 S-symmetry 解释之间的区别。

### CPHC S-symmetry 的参数抵消检查

Prochniak Eq.(9) 的严格 same-s M1 抑制条件是 gR−(gπ+gν)/2=0。对论文给出的 A≈130 参数，gR−(gπ+gν)/2=0.44−(1.22−0.21)/2=−0.065。这个小但非零残差与作者“same-s M1 非零但很小”的模型判断一致；它不能作为 126Cs 的实测磁矩或几何结果（PS11-5/6）。


### Prochniak 2011 EPJA：CPHC 的 S 对称与手征指纹非唯一性

Rohoziński et al. 的 15 页 EPJA 论文是 Prochniak Acta Phys. Pol. B 42, 465 短文之后的完整 S-symmetry 研究；该 EPJA 文在 Ref. [28] 明确列出 Acta 短文。它把 S=PαCπν 定义为 Koike A 操作在 CPHC 模型中的 generalization，同时保留不同的算符实现和适用条件（[[rohozinski-2011-cphc-s-symmetry-chirality]] CPHC11-2/4/5/12；[[prochniak-2011-cphc-s-symmetry-transition-rules]] PS11-1/3）。

| 模型情形 | 计算结果 | 对几何判别的意义 |
|---|---|---|
| 同 j 粒子-空穴配置、Pα 对称核心（WJ γ-soft、gamma well/barrier） | S 对称保留；近简并伙伴带、相似的带内 E2/M1 与 regular staggering 可同时出现（CPHC11-4/6/9） | 作者未在计算中假设角动量非共面；同一电磁指纹并非手征几何独占 |
| 不同 proton/neutron-hole orbitals | Cπν 对称破缺，带间隔变大，staggering 变弱或不规则（CPHC11-10） | 配置本身能改变 M1/E2 模式 |
| Pα 非对称核心 | S 对称破缺，regular staggering 消失，带间跃迁变弱（CPHC11-11） | 形变势/核心对称性也是条件 |
| 刚性 Davydov–Filippov 核心 | 类似的 Pα 操作要求 gamma=π/6（CPHC11-3） | 此限制只针对该刚性核心构造；不能转为通用实验 gamma 判据 |

S-symmetry 的 same-s M1 suppression 还有一个参数条件。论文给出的 A≈130 g values 为 gR=0.44、gπ=1.22、gν=−0.21，满足 gR−(gπ+gν)/2=−0.065，而精确抵消要求0；这是接近零的模型输入组合，不是 126Cs 磁矩测量（CPHC11-7/8）。因此 Grodner11 把 interband/inband M1 相位交错联系到 S-symmetry（GR126-8/9），不构成逐态 A/s assignment，也不能单独确认左右手几何。


## Model Dependence

### 128Cs 同核交叉核验：强度、几何与数据谱系

Grodner 2006 的 128Cs DSAM strength chain 给出了 yrast/side 带的 lifetime-derived B(E2)、B(M1) 与 side→yrast B(M1)；B(M1) 提取采用 pure-M1 假设，侧馈参数借用 131La 并进入寿命误差范围（[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-2/3/4/5/6）。Chen 2017 的角动量投影图把这些已发表数据作为 Ref. [14] 比较输入，而非独立实验；其几何分布是模型结果，且固定形状造成高自旋 B(E2) 趋势偏离（[[chen-2017-128cs-angular-momentum-projection-chirality]] CHEN17-3/4/5/6/7/8）。因此同一组 strength points 不能被重复计作实验确认。

三篇 128Cs 工作的证据层次不同：2006 年是从 DSAM 寿命和分支派生的 transition strengths；2017 年计算在 I≈11ℏ、14ℏ、18ℏ 给出振动、static-like 与减弱/回到平面取向的 spin-dependent geometry；2018 年的 g=+0.59(1) 是 bandhead 磁矩观测，而近 planar 几何来自 PRM+CDFT 解释（[[grodner-2018-128cs-chiral-g-factor]] GR18-1/3/4）。它们形成互补量的比较，不是三份独立的同一观测，也不能据 bandhead g 因子验证全自旋区的模型几何。

Koike 2003 的 Fig.1/Fig.4 明确以 Y/S/L 标记 yrast、side 和 linking transitions；Chen 2017 Fig.2 的 Band A 实验能量在重叠自旋处低于 Band B，因此带级顺序支持 A≈yrast、B≈side。Koike 2003 Table VII 给出五条 side→yrast mixed ΔI=1 link 的逐线身份和 DCO；这些 2003 link 标识不自动等于 2006 DSAM Fig.4/Chen Fig.2 中每个 B 值点的逐线 binding。Koike 2003 来源页 [[koike-2003-128cs-chiral-doublet-bands]] KOIKE03-2/4/5/6/7。

| Eγ (keV) | side→yrast assignment | gate | RDCO |
|---:|---|---|---:|
| 509 | 11+→10+ | 143 keV, 10+→9+ | 0.82(9) |
| 532 | 12+→11+ | 349 keV, 11+→10+ | 0.87(10) |
| 622 | 13+→12+ | 273 keV, 12+→11+ | 0.65(14) |
| 571 | 14+→13+ | 408 keV, 13+→12+ | 0.86(13) |
| 639 | 16+→15+ | 464 keV, 15+→14+ | 0.63(16) |

### 128Cs 五条连接线对 A 规则的检验边界

Hamamoto/Koike 规则若要逐线检验，需要知道同一跃迁的 A 初末态，并比较相应 M1/E2 强度。Koike 2003 Table VII 给出五条 side→yrast mixed ΔI=1 线的线能、自旋、gate 与 DCO，但未给这些五条线的逐线 mixing ratio/absolute B 分解；Table VI 的 δ 是选定的 yrast-band transitions，不是这五条 side→yrast links。Grodner 2006 Figure 4 的 out-B(M1) 点只有三个候选映射，且不是表列逐线绑定。

| Eγ (keV) | Table VII assignment / RDCO | Grodner Figure 4 crosswalk | 对 A 规则的测试状态 |
|---:|---|---|---|
| 509 | 11+→10+ / 0.82(9) | L509 在 scheme；I=11 不在强度点列 | 无 B(M1) marker，不能测试强弱规则 |
| 532 | 12+→11+ / 0.87(10) | I=12 可候选对应 L532 | 只有候选图点，无逐线绝对 B 或 A 标签 |
| 622 | 13+→12+ / 0.65(14) | Y622/L622 重叠，I=13 marker 不唯一 | 线身份与 marker 对应未闭合 |
| 571 | 14+→13+ / 0.86(13) | I=14 可候选对应 L571 | 只有候选图点，无逐线绝对 B 或 A 标签 |
| 639 | 16+→15+ / 0.63(16) | I=16 可候选对应 L639 | 只有候选图点，无逐线绝对 B 或 A 标签 |

所以 Table VII 的 mixed M1/E2 与 DCO 是结构/多极类别证据，Fig.4 提供部分强度线索；二者尚未组成逐线 selection-rule 判决。依据现有图表不能把 yrast/side 标签改写为 A=±1，也不能把“与规则相容”提升为直接手征几何证据（[[koike-2004-chiral-bands-selection-rules]] KOIKE04-5/9；[[koike-2003-128cs-chiral-doublet-bands]] KOIKE03-5/6；[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-10）。

对 Koike 2003 的 11+ yrast 母态，用 Table II 348.6-keV 11+→10+ M1/E2 强度 64.1、651.7-keV 11+→9+ E2 强度 9.1 和 Eq.(7)，得到 λ=9.1/64.1=0.14197、B(M1)/B(E2)=13.62 μN²/(e²b²)；用 Table VI 的 δ=-0.16 加回 δ² 项为 13.28，变化约 2.50%。该中心值复算的输入误差并不完整列在 Table II，因此不附正式置信区间（KOIKE03-4/5/9）。它显示比值依赖同母态 branch、能量与混合假设，不能替代独立几何量。

实验谱系也要分层：Koike 2003 的 47-MeV Stony Brook γγ/DCO 测量确定 Y/S/link 的初始线路与自旋；Grodner 2006 是 55-MeV Warsaw/OSIRIS II 的独立 DSAM 寿命/强度 campaign，但沿用 Koike 的 spin/parity assignments；Chen 2017 再把 2006 strength points 作为 Ref.[14] 比较输入；Grodner 2018 的 TDPAD g 因子则是另一个观测量。故 2003/2006 可以是不同实验数据集，但 level-scheme label 有明确依赖，2017 不能重复计数为第三份强度测量。

跨 campaign 的线能和自旋 crosswalk 得到图级支持：Koike Table VII 的 linking energies 508.9、532.0、621.6、571.1、638.6 keV，在 Grodner 2006 Figure 2 的 128Cs 方案中分别以 509、532、622、571、638 keV 标注，均在取整误差内；对应的 side→yrast spin links 也一致（[[koike-2003-128cs-chiral-doublet-bands]] KOIKE03-6；[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-9）。

Grodner Figure 4 的 out-of-band B(M1) 面板在 I=12、13、14、16 有图点，I=15 为上限；同图 line-energy spectrum 标出 L532、L571、L639，支持 I=12/14/16 的候选 marker-line 对应。I=13 的 622-keV 峰标作 Y622/L622，未分离时不能唯一归属；I=11 的 L509 在该 strength 面板没有对应图点。故能映射的是若干图点/线类，I=13 仍有重叠，不能把 Figure 4 转成逐线 B 表（[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-10）。

TAC, PRM, RPA, IBFM and γ-soft models use different degrees of freedom, fitted parameters and quantization assumptions. Their geometry and band labels remain model results until tied to the experimental chain.

## Counter-evidence

Crossings, configuration mixing, γ vibration, signature partners and shape coexistence can mimic selected fingerprints. In `134Pr`, Petrache et al. report near-degeneracy across `13<I<19` while Band 1/2 cross between `I=15` and `16`; the bands differ in alignment by about `2ħ` at `14<I<18`, and a branching/two-band-mixing analysis gives `Q0,1/Q0,2=2.0(4)` (PE06-1/2). These are direct counter-evidence to treating energy proximity as a sufficient condition; the inferred shape ratio depends on the adopted mixing model and does not quantitatively fit the `135Nd` strengths. Mukhopadhyay 2008 supplies a separate `136Nd` strength-disparity counterexample; different nuclei remain independent examples, not one common dataset.

### `134Pr` crossing and shape-difference control

| Evidence | Supports | Boundary | Locator |
|---|---|---|---|
| The near-degenerate interval contains a Band 1/Band 2 crossing at I=15–16 and an alignment difference of about `2ħ` for `14<I<18`. | A finite near-degenerate same-parity band interval can coexist with crossing and configuration/alignment divergence. | This does not establish the detailed 135Nd crossing mechanism and does not prove all near-degenerate pairs nonchiral. | [[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-1 |
| The reported `Q0,1/Q0,2=2.0(4)` follows a branching-based two-band mixing analysis. | A source-specific strength comparison challenges the ideal identical-shape partner assumption. | `Q0` is model-derived from simplified mixing; it is not a direct static-shape measurement or a fit to MU07. | [[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-2 |

## Limitations and Missing Evidence

Partner-resolved absolute strengths, lifetimes, g factors and common-input model comparisons remain incomplete for many candidate pairs.

## Required comparison protocol

For each pair, preserve the sequence:

1. verify level and band identity;
2. verify spin, parity and multipolarity using the local detector/convention calibration;
3. compare alignments and kinematic moments;
4. compare partner-resolved lifetimes and absolute strengths;
5. test crossing, configuration mixing, γ vibration and shape coexistence;
6. compare model geometry only after the experimental chain is fixed.

## Open L3 questions

- What is the minimum independent observable set for a candidate chiral pair?
- How can wobbling and signature-partner hypotheses be compared with common response and common error treatment?
- Which external post-2020 measurements materially change the candidate ranking?

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]], [[zhu-2003-135nd-composite-chiral-pair]], [[mukhopadhyay-2008-136nd-transition-rates]]
- [[chakraborty-2023-131xe-wobbling-origin]]
- [[lv-2021-tilted-precession-135nd]]
- [[petrache-2006-near-degenerate-chiral-misinterpretation]], [[petrache-2018-chiral-bands-even-even-136nd]]
- [[guo-2024-chiral-wobbler-74br]], [[grodner-2018-128cs-chiral-g-factor]], [[frauendorf-2018-beyond-unified-model]]
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]], [[wobbling-motion]], [[wobbling-vs-signature-partner]]

## Self-audit

- Same-source and review lineages are not counted as independent evidence.
- Model geometry is labeled as model output; experimental observables retain their own boundaries.
- This synthesis is a Codex self-audit and remains unreviewed.

## Evolution Log

- 2026-10-09: Add the existing `131Xe` low-`|δ|` M1-dominated signature-partner result as an experiment-specific contrast for wobbling; it does not classify the `135Nd` pair. Source review states remain unchanged.
- 2026-10-09: Add the measured D1/TiP1/TiP2 mixing-ratio control as a same-nucleus but different-band mode-discrimination example; do not assign it to MU07 D5/D6.
- 2026-10-09: Add the Day10 MU07 matched-spin strength quotients, conditional photon-rate example, `δ²`/`Q_t` identity boundary, and GR18/SU08 comparison controls. These are source-grounded calculations and cross-nucleus comparisons; no source or project review status changes.
