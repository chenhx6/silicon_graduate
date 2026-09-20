---
type: project
title: "Gamma-soft deformation evidence map"
aliases: [γ-soft deformation evidence map, γ 软形变证据图]
created: 2026-07-05
updated: 2026-08-04
status: active
review_status: human-reviewed
project_stage: seed-evidence-map
confidentiality: private
nuclei: [128xe, 130xe, 131ce, 133ce, 136sm]
tags: [gamma-softness, gamma-rigidity, a130, deformation, evidence-map, data-analysis]
---

# Gamma-soft Deformation Evidence Map

## Project Position

本页是 γ 软形变（gamma-soft deformation）的证据工作台，不是论文草稿、最终综述结论或完整文献清单。它把已审核 source 中的实验事实、模型结果、作者解释和跨来源问题分层组织；论文级使用仍须回到 source、raw 与精确 locator。

## Research Question

- 在当前 Wiki 中，哪些证据支持把一个核的低能形变背景描述为 γ-soft，而不是仅仅“存在三轴性”？
- 如何区分 [[gamma-soft-deformation]]、[[gamma-rigid-deformation]] 与一般 [[triaxial-deformation]]？
- 形状相变、配对振动、带交叉与随自旋形变变化如何共同影响 A≈130 及邻近核的谱学解释？
- 这些背景证据能为未来 `131Ce/133Ce` 数据和 low-spin collective-band interpretation 提供什么，不能提供什么？

## Current Hypotheses

以下只作为待检验框架，不是结论：

- `131Ce/133Ce` 的形变背景可能位于 γ-soft 与局域三轴极限之间，并随自旋、奇粒子耦合或带交叉改变；
- pairing softness、shape coexistence 和准粒子对齐可能与 γ softness 共同塑造低能与中高自旋谱；
- 只有多观测量和匹配模型一致时，才应提高具体 soft/rigid 判断的强度。

## Motivation

`131Ce/133Ce` 等奇 A 核的能带解释容易受到固定三轴形状、γ-soft 芯、奇粒子极化、配对、带交叉和组态混合等先验影响。先建立形变背景证据图，可避免由单一拟合 γ、单个 staggering 指标或一种带标签过早指认 wobbling、chirality 或 signature partner。

用户当前研究重点是：手征双重带（chiral doublet bands）和 wobbling bands 是稳定三轴形变研究中的重要候选集体指纹。按照本 Wiki 的证据门，这一研究重点不改写为“观察到候选带即证明 γ-rigid”；仍需分别闭合三轴形变背景、模式判据和竞争解释（FM97-1 至 FM97-6；PDF pp.5-16；F24-1 至 F24-7；PDF pp.1-26）。

## Evidence Available

当前已审核核心证据由五篇 source 构成：一篇低能偶偶判据来源、三篇共享或相邻理论方法链的 Nomura 理论来源，以及一篇独立 `136Sm` 寿命实验及模型比较。Nomura 2022 已补入 γ-soft IBFM odd-mass bands 与 low-spin wobbling alternative 的直接桥接；它不自动改变本页既有 project-level notes 的审核状态。Frauendorf 2024 仅提供 low-spin relation 背景。2026-08-04 的自测另接入未审核的 `131Ce` Singh 2016 寿命来源：它补上目标核 `Q_t` 入口，但只直接约束 E2 集体性/core response，γ-soft 标签仍为 TRS/作者解释。Rees 2011 提供独立的 `156Er` 非 yrast、γ-band staggering 与 competing-alignment comparator；它扩展跨质量区证据，但不替代 A≈130 的目标核数据。

## Seed Sources

| Source | 类型 | 本 project 中的角色 | 直接性与独立性边界 |
|---|---|---|---|
| [[zamfir-casten-1991-gamma-softness-triaxiality]] | phenomenology / model comparison | γ-unstable 与 `γ=30°` rigid rotor 的低能偶偶 γ-band staggering 判据 | 独立的奠基判据来源；数据集较早，只覆盖低自旋偶偶核 |
| [[nomura-2017-odd-mass-gamma-soft-shape-transitions]] | theory source | A≈130 Ba/Xe 偶偶芯势能面、IBFM 奇 A 谱学演化与态依赖形状不变量 | model result / author interpretation；粒子-芯耦合逐核拟合 |
| [[nomura-2021-pairing-triaxial-vibrations-gamma-soft]] | theory source | `128,130Xe` 的 pairing-plus-triaxial collective space 与 γ-softness ratios | 与 Nomura 2017 共享作者/SCMF→IBM 方法链，不按独立实验复现计数 |
| [[babra-2019-deformation-change-136sm]] | experiment source + model comparison | `136Sm` yrast 寿命、`Q_t` 与带交叉处形变演化案例 | 寿命/`Q_t` 为直接实验；γ-soft 与稳定三轴标签来自 TRS/TPSM 和作者解释 |
| [[nomura-2022-questioning-wobbling-ibfm]] | theory source, source reviewed | `135Pr/133La/127Xe/105Pd` 的 γ-soft core + odd-fermion bands 与 E2/M1 predictions | 与 Nomura 2017/2021 共享方法链；couplings fitted；`127Xe` 有异常 `δ`；不是新实验 |
| [[frauendorf-2024-wobbling-review]] | review/background | γ-soft 芯与奇 A collective-band interpretation 的关系入口 | 只用于 relation/future bridge，不替代 wobbling 原始实验来源 |
| [[singh-2016-lifetime-131ce-133pr]] | experiment source + TRS interpretation, unreviewed | `131Ce` Band-1-like yrast 寿命/`Q_t` 与目标核形变讨论入口 | 寿命直接约束 E2 集体性；四个有限点的下降仅 `0.64σ`，γ-softness 依赖 TRS/作者解释 |
| [[rees-2011-156er-nonyrast-gamma-soft]] | experiment + model interpretation | `156Er` weak non-yrast bands, `S(4)≈−1`, second-`0+`/γ-band proximity and competing `(νi13/2)2` vs `(νh9/2,f7/2)2` alignment | direct level/coincidence and angular-ratio facts; γ-soft/configuration labels remain interpretation and geometry-dependent |
| [[eldridge-2018-gamma-band-mixing-ratios]] | multi-isotope IPAC experiment | 37 γ-band→ground-band `δ(E2/M1)` values in Mo/Ru/Pd, predominantly E2; `110Ru` sign trend | attenuation/g-factor and δ-oval branches are explicit; shape-transition reading is model/systematics, not direct γ rigidity |

## Gamma-soft Deformation Concepts

- γ-soft 表示势能面沿 γ 方向较平坦、集体波函数具有显著 γ 涨落；不等于 `γ=0`，也不等于某个固定非零 γ。
- γ-rigid 要求低能波函数在非零 γ 极小附近足够局域；“三轴模型拟合成功”比这一要求弱。
- Wilets-Jean/O(6) 与 Davydov-Filippov 是理想极限，不是所有真实核必须二选一的标签。Nomura 2021 的两个诊断量对同一核分别靠近不同参考线，直接展示了这一限制（NOM21-7；PDF p.4, Fig.3）。

## Shape-phase Transition Evidence

- Zamfir–Casten 给出 γ-unstable 与 `γ=30°` rigid rotor 相反的 γ-band staggering 相位，并强调中间 `S` 值不等于中间势能刚度（ZC91-1 至 ZC91-4；PDF pp.1-4, Figs.1-2）。
- Nomura 2017 的 DD-PC1 RHB 势能面把 `134Ba/132Xe` 放在近球形到 γ-soft 的过渡区；IBFM 能级和形状不变量在 N≈76-78 呈现态依赖变化（NOM17-1 至 NOM17-9；PDF pp.5-12, Figs.1-15）。
- Fig.13 的 `γ_eff` 峰值只对应偶偶 `0+_1`；奇 A Figs.14-15 的不同低能态在不同中子数增加或降低，不能套用统一峰值模板（NOM17-7/NOM17-8；PDF pp.11-12）。

## Pairing and Triaxial Shape Vibration Evidence

- Nomura 2021 在 `(α,β,γ)` SCMF→IBM 映射中显式耦合配对坐标 α 与三轴形状坐标；动力学配对主要降低激发 `0+` 态，显式三轴自由度对 γ 带更关键（NOM21-1 至 NOM21-6；PDF pp.1-4, Figs.1-3）。
- 完整计算的 `E2γ` 靠近 W-J/O(6) 参考，而 `R3γ` 位于 W-J 与 D-F 之间并向 D-F 靠近；两个量不把 `128,130Xe` 一致归到同一纯极限（NOM21-7；PDF p.4, Fig.3）。
- 模型不区分质子、中子配对坐标，并缺少较高激发多准粒子组态；对未来奇 A Ce 不能直接照搬。

## Experimental Deformation-change Case

- Babra 2019 直接测得 `136Sm` yrast 8+ 至 20+ 态的寿命或上限，并提取 `Q_t`；12+ 以上 `Q_t` 总体下降，支持带交叉后集体性减弱（B19-1 至 B19-5、B19-8；PDF pp.1-3, Table I; p.6, Fig.8）。
- 推转准粒子、TRS 与 TPSM 把交叉和 `Q_t` 变化联系到准粒子对齐及从低频 γ-soft 极小到较稳定三轴极小的形变演化（B19-6 至 B19-12；PDF pp.4-9, Figs.6-10）。
- 直接实验层只建立寿命、`Q_t`、alignment/`J^(2)` 与交叉；`β2≈0.22, γ≈-25°` 和“稳定三轴”是模型结果/作者解释。

## Model Landscape

| 模型/框架 | 当前用途 | 主要边界 |
|---|---|---|
| [[gamma-unstable-model]] / O(6) | γ-independent 理想参考 | 真实核通常不完全 γ independent |
| [[davydov-triaxial-rotor-model]] | 固定 γ 的 rigid-triaxial 参考 | 固定 γ 拟合不证明波函数局域 |
| [[interacting-boson-model]] / [[interacting-boson-fermion-model]] | 势能面映射、低能谱、奇粒子-芯耦合、配对振动扩展；Nomura 2022 的 low-spin alternative | 映射与模型空间依赖；IBFM 耦合逐核拟合，模型 band matching 不是 observed identity |
| [[covariant-density-functional-theory]] / RHB/RMF+BCS | 生成 `(β,γ)` 或 `(α,β,γ)` SCMF 势能面 | 泛函、配对与约束依赖；模型 γ 非直接测量 |
| [[cranked-shell-model]] / TRS | 追踪准粒子交叉和随频率变化的竞争极小 | 宏观-微观参数与 pairing 依赖 |
| [[triaxial-projected-shell-model]] | 比较固定形变基底上的能级与 E2 集体性 | 输入形变和基底截断依赖；切换两套输入不等于连续形状测量 |

## Observable / Diagnostic Handles

| 观测量/诊断量 | 能约束什么 | 不能单独建立什么 |
|---|---|---|
| [[gamma-band-energy-staggering]] | 低自旋偶偶 γ 带相对 W-J/D-F 极限的相位 | 势能面刚度的唯一数值反演；奇 A 高自旋直接分类 |
| `E2γ` 与 `R3γ` | 低能偶偶 γ 带能量/B(E2) 对几何极限的相对位置 | 两指标不一致时的唯一标签；`131Ce/133Ce` 无条件阈值 |
| E2 四极形状不变量、`β_eff/γ_eff` | 指定态的集体形状分布指标 | 直接测得的静态 γ；跨态统一临界点 |
| [[transition-quadrupole-moment]] / lifetime | 带内 E2 集体性和随自旋变化 | γ 符号、γ 刚性或具体势能极小的唯一识别 |
| alignment、[[moments-of-inertia]]、band crossing | 准粒子对齐与转动响应变化 | 单独证明 pairing collapse 或特定形状 |
| 微观/宏观-微观 PES | 给定模型中的极小位置、宽度与竞争形状 | 直接实验事实或模型无关形状 |

## Cross-source Project Notes

| ID | Project-level statement | Source basis | Reverse-test boundary / evidence gap | needs_review |
|---|---|---|---|---|
| GSD-PROJ-1 | γ-soft 是势能面与波函数涨落性质，不是一个固定 γ 数值或单一能带标签 | ZC91-1 至 ZC91-4；NOM21-1/NOM21-7 | 尚缺现代多观测量、模型一致的 nucleus-specific validation | false |
| GSD-PROJ-2 | A≈130 的形状相变背景在偶偶芯和奇 A 低能态中可留下相关但不完全同形的信号 | NOM17-1 至 NOM17-9 | Nomura 2017 为单一 IBFM/EDF 实现；奇 A 耦合逐核拟合 | false |
| GSD-PROJ-3 | pairing softness 可与 γ softness 同时存在，并显著改变激发 `0+` 结构 | NOM21-1 至 NOM21-9 | 仅 `128,130Xe` 示例；缺质子/中子配对坐标分离与多准粒子空间 | false |
| GSD-PROJ-4 | `136Sm` 的直接实验结果是第一带交叉附近及其后 `Q_t` 总体下降、E2 集体性减弱；TRS 给出低频 γ-soft 极小和交叉后较稳定三轴极小，TPSM 用两套形变输入分别改善交叉前后描述，作者据此提出 γ-soft→rigid/stable-triaxial transition | B19-1 至 B19-12；PDF pp.1-9, Table I, Figs.5-10 | 形状转变不是由 `Q_t` 单独测得；TRS/TPSM 有参数依赖，第二交叉以上还有 oblate/triaxial/highly-deformed-prolate 竞争极小；非 Ce 核 | false |
| GSD-PROJ-5 | 形变背景应在 low-spin band interpretation 之前建立，但本身不能确认 wobbling、chirality 或 signature partner | 四个核心 source；[[low-spin-wobbling-controversies]] | 需要逐带电磁判据、band identity 与专门模型；当前 project 不改判已有争议 | false |
| GSD-PROJ-6 | 对 `131Ce/133Ce`，最低可行证据链应联合能级系统学、寿命/绝对 E2、形状不变量或匹配势能面，并显式处理奇粒子与带交叉 | 截至 2026-07-06 的四源方法边界 | 当时 Wiki 尚未覆盖 `131Ce` nucleus-specific lifetime source；该历史缺口由 GSD-PROJ-8 更新 | false |
| GSD-PROJ-7 | γ-soft core 可在 IBFM 中产生与 reported low-spin wobbling candidates 相近的 odd-mass bands，因此 γ-softness 只限定形变/芯动力学背景，不能单独决定 wobbling、TiP 或其他 band identity | NOM22-2 至 NOM22-15, PDF pp.2-10 | Nomura 2022 source 已审；四核模型有拟合/空间限制，`131Ce/133Ce` 未计算 | false |
| GSD-PROJ-8 | Singh 2016 已补入 `131Ce` nucleus-specific 寿命/`Q_t`，但四个有限点的自旋趋势仅 `0.64σ`；这些数据约束 E2 集体性/core response，不独立建立 γ-softness | SI16-1 至 SI16-7；PDF pp.5-10, Table 1, Figs.5,9-12；[[131ce-collective-mode-discrimination]] | γ-soft/nonaxial 标签主要来自 TRS/作者解释；缺多带 absolute E2、shape invariants 与 common-input soft-vs-rigid calculation | false |

## Evidence Gaps

- `131Ce` 已有 Band-1-like nucleus-specific 寿命/`Q_t`，但仍缺低能 γ 带/形状不变量、多带绝对 E2 及能区统一的高自旋寿命矩阵；
- `133Ce` 现有来源尚未形成与本 project 相同输入、相同 γ 约定下的 soft-vs-rigid 检验；
- 缺现代 Coulomb-excitation E2 matrix elements 与不变量分析，用于独立约束 A≈130 偶偶芯；
- 缺 common-input calculation 同时比较 γ-soft collective Hamiltonian/IBM、固定三轴模型和奇粒子耦合；
- Nomura 2017 与 2021 共享作者和 SCMF→IBM 方法链，理论证据并非完全独立；
- `136Sm` 的 `Q_t` 下降直接约束集体性，但第二交叉以上多极小和形状共存仍未由寿命闭合；
- 当前没有对“γ-softness 如何改变具体 low-spin wobbling/TiP 近似条件”的 nucleus-specific 计算。
- Nomura 2022 提供 IBFM alternative，但没有计算 `131Ce/133Ce`，也没有检验 TiP geometry 或 wobbling approximation；不能填补目标核的 nucleus-specific 缺口。

## Relation to Low-spin Wobbling Controversies

[[low-spin-wobbling-controversies]] 负责 band identity、mixing ratio、polarization、wobbling approximation 与 phonon quantization。本 project 只提供形变动力学背景：

- γ-softness 不由大 `abs(δ)` 或一条 E2-dominated link 直接标记；
- γ-soft 芯与某些奇 A collective-band 模式可在模型中共存，但这不建立 wobbling 身份；
- Nomura 2022 显示同一类 γ-soft background 也可进入 IBFM non-wobbling interpretation；该理论 challenge 与 TiP alternative 分属不同机制链；
- 手征双重带与 wobbling bands 是稳定三轴性研究的重要候选指纹；它们的模式指认与 γ-rigid 形变判断仍是两条需要交叉约束的证据链；
- 若形变背景随自旋或带交叉改变，固定转子输入和低自旋近似应重新检验；
- 本页不修改 `135Pr/187Au` 的任何支持或反证结论。

跨主题的分层 case map、TiP/IBFM 区分、共享实验判据与未来 `19F+116Sn` 数据入口统一见 [[low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations]]；该 synthesis 不改变本页已审核 GSD-PROJ statements。

## Relation to Future User Data

未来 `131Ce/133Ce` 数据按以下层级接入：

1. observed facts：能级、跃迁、符合、寿命、分支、DCO/角分布/偏振；
2. diagnostic quantities：γ-band staggering、`Q_t/B(E2)`、alignment、`J^(1/2)`；
3. model results：PES 宽度/极小、奇粒子-芯耦合、pairing 与 band-crossing sensitivity；
4. interpretations：γ-soft、γ-rigid/stable-triaxial、shape coexistence 或其他竞争图像；
5. synthesis：只有在 source 与数据层分别闭合后，才讨论对 collective-band identity 的影响。

## Risks and Blockers

- 四篇核心 source 不是完整领域书目；
- Nomura 2017/2021 不是相互独立的理论复现；
- `136Sm` 不是 Ce，邻核比较不能替代目标核证据；
- `131Ce` 当前缺 nucleus-specific source，`133Ce` 也缺与本 project 同口径的寿命/不变量链；
- project 与 synthesis 的 14 条跨来源 statements 已由用户审核；论文级使用仍须回到 source、raw、locator，并重新执行 paper evidence gate。
- GSD-PROJ-7 已通过用户审核；Nomura 2022 source 级复核不会自动推导到其他未写明的项目。

## Next Actions

1. GSD-PROJ-8 的 targeted human review 已完成；未来 paper-level 使用仍回到 Singh 2016 原文和 locator 复核。
2. 继续补充 `131Ce/133Ce` 的多带绝对 E2、shape invariants 与 common-input soft-vs-rigid source；不以邻核替代。
3. 补充 `128-134Xe/Ba/Ce` 的现代 E2 matrix-element / Coulomb-excitation 来源。
4. 为 `131Ce/133Ce` 设计 common-observable、common-convention 的 soft-vs-rigid 模型比较。
5. 新数据出现多带寿命或绝对 E2 后，优先更新 `Q_t/B(E2)` 与带交叉前后形变背景。

## Related Sources and Pages

- Concepts: [[gamma-soft-deformation]], [[gamma-rigid-deformation]], [[triaxial-deformation]]
- Synthesis: [[gamma-soft-vs-gamma-rigid-diagnostics]]；[[low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations]]
- Parent context: [[a130-high-spin-collective-modes-evidence-map]]
- Low-spin relation: [[low-spin-wobbling-controversies]]
- Target-nucleus update: [[singh-2016-lifetime-131ce-133pr]]；[[131ce-collective-mode-discrimination]]

## Update Log

- 2026-08-04：每周自测接入 `131Ce` Singh 2016 寿命入口；保留既有已审核 GSD-PROJ-6 为历史边界。用户随后完成 GSD-PROJ-8 targeted review，接受 `Q_t` 不独立证明 γ-softness 的分层。
