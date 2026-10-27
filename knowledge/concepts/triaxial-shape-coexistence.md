---
type: concept
title: 三轴形状共存
aliases: [triaxial shape coexistence]
created: 2026-07-13
updated: 2026-10-27
status: active
review_status: unreviewed
concept_type: nuclear-shape-coexistence
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [triaxiality, shape-coexistence, multiple-chiral-doublet]
---

# 三轴形状共存（Triaxial Shape Coexistence）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

同一原子核中不同低激发组态对应多个具有三轴形变的候选结构或势能极小。它是模型—实验联合解释，不等于仅由多条带或能量近简并直接观测到多个三轴形状。

## Necessary Assumptions

需要区分不同组态/形变极小，并检验其与实验带头、能谱和电磁 observables 的对应；还需统一 `gamma` convention。

## Discriminating Observables

组态相关能带、带头能量、绝对 E2 observables/lifetimes、势能面与多个模型的一致性。

## Supporting Evidence

[[aberg-flocard-nazarewicz-1990-mean-field-shapes]] is the historical mean-field backbone for competing minima, rotation-induced triaxiality and the need for projection/configuration mixing before assigning laboratory bands.

[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]] 的 RMF 为 `133Ce` states a/b 给出不同三轴形变与组态，TPRM 对相应双带作比较；论文据此解释为 triaxial shape coexistence。

[[guo-2022-possible-chiral-multiple-chiral-thallium-isotopes]] 的 PK1 constrained RMF 在 `192-198Tl` 中得到多个局域三轴极小值，并把它们称为 triaxial shape coexistence 的例子；`199,200Tl` 没有合适的三轴极小值。这里的 coexistence 是单一 mean-field landscape 的模型结果，尚未由 band-to-minimum mapping 或绝对 E2 observables 独立约束。

## Counter-evidence and Competing Interpretations

单一模型的多个极小、拟合能量或近简并带不能排除 gamma softness、带混合和不同组态但相近形变等解释。

## Related Nuclei and Bands

- [[133ce]]；[[133ce-positive-parity-mchd-pair]]、[[133ce-negative-parity-mchd-pair]]。
- [[192tl]]、[[193tl]]、[[194tl]]、[[195tl]]、[[196tl]]、[[197tl]]、[[198tl]]；[[199tl]] 与 [[200tl]] 为模型 null controls。

## Our Current Position

保留为 author/model-supported interpretation；`133Ce` 缺本文候选带的 lifetime/absolute transition-probability 独立约束，Tl 链还缺预测极小值到逐条实验带的映射与转动量子计算。

旧Day21 checkpoint009的量化认证已撤回：50–100keV普适强mixing门、186Pb固定混合百分比、E0排他唯一形状反演以及“必须E0+多步Coulex”的强制组合不再采用。原记录及025保存副本保留；实际原件校准见[[heyde-wood-2011-shape-coexistence-review]] HW11-D25P-001–006。低0+能级可有信息，但需随具体结构/空间/观测讨论，不从一组能级直接认证未混合刚性shape。

124撤回本节旧科学认证与自设阈值；旧全文保存在superseded-124，原review/flags保持。

## Day 25 正式核验：三轴形状共存与核手征性的鉴别边界

Day 25 主线建立三轴形状共存（triaxial shape coexistence）与手征双重带（chiral doublet bands）的严格判据边界，并固化至 [[chirality-shape-coexistence-companion-matrix]]：

1. **物理机制与波函数本质**：
   - **核手征性（Chirality）**：属于在单一三轴形变势能极小（或稳定的动态三轴平均形变）背景下，价粒子（短轴）、集体转动（中轴）与价空穴（长轴）三根相互垂直的角动量分量形成的非共面 aplanar 空间三角架。在实验室系中通过隧穿恢复时间反演与 $\mathcal{R}(\pi)$ 联合对称性，形成波函数结构对称、形状相同、能量近简并的宇称相同双重态；
   - **形状共存（Shape Coexistence）**：源于单粒子能级壳效应与残余相互作用（如粒子-空穴激发与质子-中子四极相互作用），在同一原子核中形成两个或多个不同的平衡形变极小值（不同的 $\beta_2, \gamma$），并在各自势能极小上发展出独立的转动带。

2. **核心鉴别观测量与实验反证**：
   - **内禀四极矩 $Q_0$ 与绝对 $B(E2)$ 阶梯**：理想手征双重带要求两带具有在实验误差内完全一致的内禀四极矩与带内绝对 $B(E2)$；而在形状共存中，不同形变极小通常导致显著不同的四极矩。[[petrache-2006-near-degenerate-chiral-misinterpretation]] (PE06) 通过两带解混合模型表明，134Pr 在能级近简并区（$I=14–18$）的四极矩比值高达 $Q_{0,1}/Q_{0,2} = 2.0(4)$，直接排除了理想手征带，而支持不同形状或多准粒子带交叉解释；
   - **单极跃迁 $E0$ 与混合矩阵元**：根据 [[heyde-wood-2011-shape-coexistence-review]] (HW11)，强 $E0$ 跃迁 $\rho^2(E0) = Z^2/R_0^4 a^2(1-a^2)[\Delta \langle r^2 \rangle]^2$ 是形状共存与能级混合的有力间接探针；而纯手征带同自旋态之间不以强 $E0$ 跃迁为主导特征；
   - **带间跃迁与手征选择定则**：手征双重带具有特征的 $\Delta I=1$ 带间 $M1$ 与 $E2$ 跃迁交错规律；形状共存带之间的跃迁通常受不同内禀形状波函数空间重叠小的阻尼，在未发生强反交叉混合时带间连接较弱；
   - **自旋演化动力学**：手征带随自旋增加呈现从手征振动（chiral vibration）到静态手征转动（static chirality）的相干演化（如 135Nd 负宇称对，Mukhopadhyay 2007）；形状共存则表现为不同准粒子组态在转动驱动下经历各自独立的退对与交叉。

3. **方法警示**：
   - 能量近简并（near-degeneracy）是手征对称性破缺恢复的必要表现，绝非充分条件。带交叉、偶然简并或形状共存均可在有限自旋窗口内伪造近简并能谱；
   - 必须通过涵盖母态归属、实测寿命 $\tau$、绝对电磁跃迁几率 $B(E2)/B(M1)$、以及独立结构 holdout（如 $g$ 因子或 $Q_s$）的最小伴随观测量组合进行严格模式甄别。

## Sources

- [[heyde-wood-2011-shape-coexistence-review]]
- [[meng-2010-open-problems-nuclear-chirality]]
- [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]
- [[guo-2022-possible-chiral-multiple-chiral-thallium-isotopes]]

## Evolution Log

- 2026-07-13：由 Meng 2010 理论背景与 Ayangeakaa 2013 实验—模型链建立。
- 2026-08-11：加入 Guo 2022 `192-200Tl` 多极小值/无极小值系统学，并保留单一 mean-field 与未建立 band mapping 的边界。


## Day21 checkpoint124：条件证据与量词纠正

[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D21-R45-1/4的Q比依赖两带模型，不是三轴形状共存的无模型实证。[[yao-2012-34si-beyond-mean-field-bubble]] YA12-D21-R124-3保作者might indicate量词；一个E0强度在给定模型中约束混合幅度与半径差的组合，不分别唯一识别两者。寿命不是一切结构判断的普适必要条件。


## Day24内Day25预习：逐伙伴比较的证据层

[[chirality-shape-coexistence-companion-matrix]]按134Pr、135Nd两个family及136Nd各pair分开实验与模型。[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25P-001/002的解混合Q比不是直接β比；[[lv-2019-chirality-135nd-reexamined]] LV19-D25P-003/004的新相对谱学与旧absoluteEM/模型校准分别保留；[[petrache-2018-chiral-bands-even-even-136nd]] PE18-D25P-001–004的真实D5比值与D3模型几何不拼成同pair实测形状。近能/多极小/多个pair均不自动建立实验刚性形状共存，也不使手征与共存必为互斥命题。

最小companion设计须按母态/段/response绑定，缺量时降级具体结论而非设普适模式终判；新综合needs_review:true。此为无学分preview，旧review/撤回保持，不开启Day26。

### E0与形状坐标不是同一个反演

[[heyde-wood-2011-shape-coexistence-review]] HW11-D25P-001–006把E0、电四极矩/跃迁率、radii与transfer按direct/indirect/hints分层。源two-config Eq14约束mixing×Δ⟨r²⟩，不是不加条件的Δβ²或γ测量；energygap也不能独立消去半径差未知。E0小/未见有不同原因，不能普遍否定所有shape差别。

E0不局限0+；odd/highspin与SD结构需自己的同态/同spin/配置和测量响应，不能强制所有体系同时有E0与multistepCoulex。对角E2、绝对transition strength或其它结构信息如何组合，取决于实际可分辨预报；这保留E0和CoulEx的强约束力，也保留原源不同技术路线的适用域。

### 形状涨落与近简并双带的竞争

[[tonev-2006-134pr-lifetime-chiral]] TO06-D24-003/004/005的134Pr实验B(E2)不对称和M1走势，对特定刚性三轴计算构成反证；IBFFM形状涨落提供作者支持的一条解释。[[tonev-2007-134pr-dynamic-chirality]] TO07-D24-006将其表述为弱涨落主导手征并保留未揭示的内禀对称性，计算能隙和I=15交叉仍不成功。这不能升级成实验已排除一切刚性共存、或唯一证明β/γ涨落因果机制。

多个极小、量子涨落和配置混合可以共存，按具体空间/态/预报区分；没有适用于所有核的“寿命+偏振+B”的强制充分组合。companion应围绕实际未用于定标的可分预报选择，缺项只降低相应结论。详[[chirality-shape-coexistence-companion-matrix]]，新增综合needs_review:true。
