---
type: method
title: Spin/parity assignment
aliases: [spin parity assignment, spin assignment, parity assignment, Jpi assignment, J^pi assignment]
created: 2026-07-09
updated: 2026-10-08
status: ai-draft
review_status: unreviewed
method_type: level-assignment
tags: [spin-parity, assignment, angular-distribution, dco, gamma-spectroscopy]
---

# Spin/Parity Assignment

## Purpose

Spin/parity assignment combines level-sequence logic, transition properties, and selected experimental observables to constrain `J^pi` for nuclear states.

## Inputs and Assumptions

- reliable level-sequence and coincidence relations;
- at least one transition-property handle such as angular distribution, DCO, polarization, conversion, or lifetime information;
- an explicit statement of what is measured directly and what is inferred from heuristic band regularity or comparison with known patterns.

## Typical Inputs

- transition energies and coincidence relations;
- candidate spin sequence and band context;
- angular distribution or angular-correlation information;
- DCO ratios, linear polarization, conversion coefficients, lifetimes, or band regularity when available.

## Source-Level Practice Boundary

[[summary-2013-bases-spin-parity-assignments]] is the main background source currently ingested for this page. It is a reference guide rather than an original experiment. For high-spin states it records practical heuristics for angular distributions and DCO ratios using a typical orientation parameter `σ/I = 0.3`, and it also distinguishes stronger arguments from weaker arguments for rotational-band assignments.

This page therefore treats spin/parity assignment as a method bundle, not as a single observable. In particular, a quoted "typical orientation parameter" from a guide should not be promoted into a universal `sigma/I` prescription.

## What It Can Establish

When several observables are mutually consistent, spin/parity assignment can narrow or fix plausible `J^pi` values for states and transitions.

## What It Cannot Establish Alone

No single rule is universal across detector geometry, reaction mechanism, and feeding history. Regular level spacing alone is usually weaker than angular-distribution, angular-correlation, polarization, conversion, or lifetime evidence.

## Assignment Evidence Dependencies

自旋、宇称和多极性应逐项列明观测、固定输入和条件推断。同一个含假设的角分布/DCO 拟合输出三个标签，不会产生三份独立证据。观测通道互补、统计独立和实验谱系独立是不同问题；同一事件样本的角分布与偏振计数要保留协方差，共用 response/alignment 或已知 spin anchor 也要明确。

| Claim | 常见约束 | 必须记录的条件或依赖 |
|---|---|---|
| spin / ΔJ | 级联、角分布、角关联/DCO 的候选比较 | 末态 spin anchor、gate multipolarity、alignment；由 band regularity 固定的输入不能再算作观测结果 |
| parity change | 已约束的 photon rank L、E/M 性质 + 已知末态宇称 | 若 E/M 是用待定 parity 选择的拟合模型，parity 结论有循环依赖；需要独立或互补的偏振/转换约束 |
| photon multipolarity | angular rank 和 E/M 候选的联合响应 | 选律仅排除不允许候选；低阶截断不排除允许高阶成分；single-gamma angular rank K 和 photon rank L 不等同 |
| mixing ratio sign | 约定明确的干涉敏感角分布/偏振/角关联 | 算符、bra/ket 顺序、发射/吸收、first/second cascade γ 与响应；率或普通ICC只有 δ² |
| absolute strength / hindrance | 寿命、完整分支、能量、已知多极与参考尺度 | 未观测分支、内转换、E0、feeding、效率与协方差；一个 lifetime 本身不提供唯一多极 |

[[rose-brink-1967-phase-defined-angular-distributions]] 的 RB67-2/3/4/7/8 分开 population、geometry、polarization、interference 与 integrated width；[[lange-kumar-hamilton-1982-multipole-admixtures]] 的 LKH82-1/4/5 分开 γ 振幅约定、级联相位和 E0/ICC。这张表是基于这些 formalism 的分析性证据审计，不是新实验。三条合成跃迁及所有允许高阶候选见 [[multipole-mixing-ratio]]；题设 Jπ 标签不具有实测证据。


实际依赖反例见 [[multipole-mixing-ratio]] 的“布居未知时，角分布和偏振可以共享多极歧义”：在固定题设Jπ但布居分别为high-M/low-M时，pure E1/pure M2能给相同pointwise方向/偏振强度。因此增加一个measurement channel不自动消除共用population的条件推断；该L2反例不声明所有γ观测或真实核素都相同。独立布居校准须来自另一个已建立的约束，不能重用待判multipole拟合。依据 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-10/11/12；实际实验还需响应、背景、gate/feeding与协方差。

## Selection Exclusions and Model Zeros

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-8–11 区分普遍 triangle/parity 过滤与 generator-only 模型零值。常数乘 total J 在 rotationally invariant H 中不连不同能量态，完整 M1 current 却不必与 J 成比例；模型项为零不能当作 measured forbidden/hindered 标签。指定模型还需同阶 operator 与 wave-function corrections，以及 long-wave、projection、pairing、configuration-space 条件。大 δ 丢失绝对尺度，不能取代 partial rate/B 与参考强度。自由振幅反例证明观测存在形式多解，真实核中的可实现性和先验可信度仍需独立模型与数据核验。

## Independent Calibration and Parity Null Tests

依据 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-23，须把极化证据归于实际测量的那条 γ 与其 gate。γ1 的 E/M 全体 duality 在 first-direction tag 且 first-pol 未测时产生相同中间密度，γ2 polarization 不直接区分 γ1 type；first-linear tag 可能增加 joint 信息。已知能级宇称可支持链式推断，但不能把共享推断重复计为独立观测。

RB67-24 的 J=2 参考线只在事先支持的 symmetric-diagonal 模型中校准 full population；joint covariance/uncertainty、same selection、orientation/coherence 与 response 是额外证据。母态谱 floor 不自动迁移到下游条件态。LKH82-15/16 的高阶截断先验也须独立于目标低阶拟合。

RB67-25 的 null-converse 控制说明，odd-K absence 不能证明确定宇称；odd accepted shape 须先验证响应和 population/axis 条件。本轮没有核素 parity assignment 或新实验事实，所有模型和校准条件都保留在证据依赖链中。

## High-Spin Reference Coverage

[[rose-brink-1967-phase-defined-angular-distributions]] RB67-26 说明 pure-E2 参考对 J3 的 population rank6 可盲；同参考全 photon state 的布居也可给不同 target W。不要把未测 tensor 设零后得到的名义 fullρ 当作独立标定。Group 数超过 normalization/A2/A4 map rank 时，positivity 本身无法认证统一正谱 floor；目标特定下限需另做优化。参考 E2 purity 也不能由 absent K6 自证，original 3→1 triangle 仍允许 M3/E4。保留 source 条件、same-selection 与 physical-model 先验，不把合成 node 赋给真实跃迁。

## Related Pages

- [[angular-distribution]]
- [[angular-correlation]]
- [[dco-ratio]]
- [[linear-polarization-asymmetry]]
- [[multipole-mixing-ratio]]

## Sources

- [[summary-2013-bases-spin-parity-assignments]]
- [[chiara-2012-cu65-cu67-core-coupled-protons]]
- [[rose-brink-1967-phase-defined-angular-distributions]]
- [[lange-kumar-hamilton-1982-multipole-admixtures]]

### Four-Multipole Local Identifiability

合成2+→2+在固定Jπ、完整M1/E2/M3/E4、未知aligned布居下，完整单γ方向与线偏振仅有四个normalized形状系数。RB67-13的exact内域seed证明五变量映射rank4、存在改变multipole fractions的一维同观测解族；独立固定布居后同点rank3只是局部改进，isotropic点仍不唯一。多个观测通道须列明共享布居与模型先验；Gaussian或低阶截断不增加独立证据。未给定的same-parent2+→0+ pure-E2参考设计可校准B2/B4，须匹配gate/feeding/axis/response；详见[[rose-brink-1967-phase-defined-angular-distributions]]与[[multipole-mixing-ratio]]。这不是实测spin/parity赋值或L4结果。

RB67-14补充一个已知非等权布居的精确global pair：U保留S与所有normalized单γ方向/偏振二次型，四个γ份额不同而两个解各自local rank3。独立calibration与局部拟合的满秩不能单独排除离散global branch；完整候选、multi-start/global certificates及额外observable要按setup核验。此处数据为合成theory，73-check证书与fixed-convention/final-channel解释见[[rose-brink-1967-phase-defined-angular-distributions]]。

RB67-15的合成3+→1+完整模型在指定内点为6×5 rank5，可局部联合约束relative amplitudes与population；这不等于Jπ标签或观测彼此独立，也不证明global唯一。PureE2恒K6零，isotropy/cancellation也能隐藏K6；数据/响应/全部候选和covariance须分别核验。

RB67-16 further给CaseC两个local rank5但global同观测分支；一个higher mixture甚至在B6非零时与pureE2同全部curve、A6/C6均0。Full-model/global branches与观测灵敏度要在local parameter rank之外核验。合成证书不可作为实际spin/parity或measured higher-multipole结果。

## Cascade Constraints, Coherence and Normalization

RB67-17 的同一合成2+→2+→0+/pureE2末支证明，单γ相同可在离轴、已知非等权布居和保持中间态相干时被joint intensity区分；沿axis、random初态或理想dephasing对该U pair均盲。此判别依赖independent gate/ordering、population/axis、response、feeding与lifetime/time-window/deorientation，不能只列“又测了级联”就当无条件独立支持。Odd Q相干可位于even K tensor，不能混成odd K/parity mixing。

RB67-18原内域seed的四shape/五unknown映射加入一个normalizedW12后rank4→5，只给固定Jπ/real-amplitude/diagonal-population模型的局部逆；已知布居的rank3→3仍可增进global-branch判别。Isotropic控制仅补一个组合，未完整反演。ConditionalW12/W1与W12是等价替代行，不能双计；未知coincidence normalization是额外nuisance，需独立处理统计covariance和calibration。详见[[rose-brink-1967-phase-defined-angular-distributions]]与[[multipole-mixing-ratio]]，无真实spin/parity赋值或L4结果。

LKH82-12/KB08-D8-4进一步限定ICC证据：penetration修正要对相容reference model/允许参数域，FO/NH空穴与NP/SC核流近似不同。固定δ时标量ICC不给其sign，并不排除linear penetration参数的信息；一个K-shell系数不是完整total-lifetime输入。旧人审记录不扩展到本次新附录。

RB67-19的计算区间证书还给同五idealoutputs的另一正布居/不同fractions分支，两点均localrank5；结论限unknown-population模型，不能移用到独立fixed-population切片。盒中唯一只限该盒，参数admissible不证明真实核可实现或同等modelprior。RB67-20的预定secondary角点比值可分该pair，但需要同一选样/时间窗和独立relative efficiency/acceptance标定；没有真实计数、响应或finite-count significance。局部rank、全局branch、模型迁移与校准的独立性分别核验。
