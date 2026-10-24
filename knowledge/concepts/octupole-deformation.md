---
type: concept
title: 八极形变
aliases: [octupole deformation, stable octupole deformation]
created: 2026-07-13
updated: 2026-09-21
status: active
review_status: unreviewed
concept_type: nuclear-shape
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [octupole, reflection-asymmetry, deformation]
---

# 八极形变（Octupole Deformation）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

核形状具有 reflection-asymmetric octupole component；stable octupole deformation 要求比一般 correlations/softness 更强的静态局域证据。

## Necessary Assumptions

需区分动态涨落、软势能面与稳定非零 `beta3` minimum，并结合 alternating-parity/electromagnetic evidence。

## Discriminating Observables

接近零的 opposite-parity `delta E`、增强 E1 strengths、parity-doublet systematics 和稳定 PES minimum 等联合约束。

## Supporting Evidence

[[aberg-flocard-nazarewicz-1990-mean-field-shapes]] supplies the mean-field octupole/reflection-asymmetry background and explicitly separates intrinsic `β3` minima from parity-restored laboratory spectroscopy.

[[li-2024-144ba-octupole-cdf-3d-lattice]] provides a self-consistent PC-PK1 3D-lattice mean-field example for `144Ba`: a nonzero `β30≈0.13` minimum and nearly persistent `β30≈0.128` to `I≈24ℏ`. This is a model order parameter; the paper explicitly lacks pairing and parity projection, so it does not by itself establish measured parity splitting or a quantum alternating-parity spectrum.

[[gaffney-2013-pear-shaped-rn-ra]] provides a direct E3/Q3 Coulomb-excitation benchmark: `224Ra` has stronger, more coherent octupole collectivity than `220Rn`, but the conversion from fitted matrix elements to a pear-shaped/static interpretation remains model- and isotope-systematics dependent.

[[bucher-2016-144ba-direct-octupole]] adds a direct neutron-rich-Ba benchmark: sub-barrier `144Ba+208Pb` Coulomb excitation with CHICO2/GRETINA gives `B(E3;3−→0+)=48^{+25}_{−34} W.u.`, `Q3=1.73^{+0.45}_{−0.62}×10³ efm³` and inferred `β3=0.17^{+0.04}_{−0.06}`. The E3 matrix element is direct; the static-shape/β3 conversion still carries rotor, higher-multipole and E1-sign assumptions.

[[bucher-2017-146ba-direct-octupole]] extends the direct-E3 layer to `146Ba`: `B(E3;3−→0+)=48^{+21}_{−29} W.u.` despite a strong suppression of the intrinsic E1 moment. This neighboring-isotope result shows that E1 magnitude is not a one-to-one proxy for octupole strength; the occupancy-sensitive microscopic explanation remains model dependent.

Day 21 Checkpoint 006 证据门审计（[[experimental-claim-boundaries]]，基于 `octupole-ba-audit-006.json`）确立关键物理推断边界：$B(E3) \approx 48\text{ W.u.}$ 测量的是初末态之间的八极跃迁矩阵元，物理上对应八极涨落方均根振幅 $\sqrt{\langle \beta_3^2 \rangle} \approx 0.17$，既可产生自静态深势阱，也可产生自八极柔软势能面（$\Delta V_{\text{barrier}} < 0.5-1.0\text{ MeV} < E_{\text{ZPE}} \sim 1.0-1.5\text{ MeV}$）的动态零点涨落。伴随观测量中，$^{144,146}\text{Ba}$ 低自旋交错能带存在高达 $\Delta E(1^-) \sim 650\text{ keV}$ 的声子能级偏移（相较于 $^{224}\text{Ra}$ 的 $174\text{ keV} \to 0$），激发态 $E3$ 矩阵元未提供脱离转子约束的统计确证，因而 $^{144,146}\text{Ba}$ 基态属于八极柔软核而非静态刚性梨形核。

[[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] is the historical review anchor for separating stable octupole minima, octupole softness/vibration, parity restoration and E1/E3 observables; it is not an independent experiment.

当前来源没有把 `74As` 或 `78Br` 建立为 stable octupole-deformed nucleus。

## Counter-evidence and Competing Interpretations

Liu 2016 的 `78Br` ratios/`delta E` 明显不同于 `224Th`，PES 为 [[octupole-softness]]。Xiao 2022 的 `74As` relative `B(E1)/B(E2)`/`δE` 同样接近 `78Br` 而偏离 `224Th`，且没有 lifetime/absolute E1 evidence。

## Related Nuclei and Bands

- [[78br]] 仅作为 correlations/softness 的边界案例。
- [[74as]] 仅作为 correlations 的边界案例。

## Our Current Position

不得将 `74As/78Br` 的八极关联改写为 stable octupole deformation。

## Sources

- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]
- [[xiao-2022-chirality-octupole-correlations-74as]]
- [[li-2024-144ba-octupole-cdf-3d-lattice]]
- [[gaffney-2013-pear-shaped-rn-ra]]
- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]

## Evolution Log

- 2026-07-13：建立 stable-deformation 排除边界。
- 2026-08-11：加入 `74As` 对 `78Br/224Th` 的 comparison；relative ratios 不升级为 static deformation。
- 2026-09-20：加入 `144Ba` 3D-lattice CDFT 的 stable-mean-field example；明确 `β30` 模型结果、PES softness、pairing omission 与 parity-projection boundary。
- 2026-09-20：加入 `220Rn/224Ra` direct E3/Q3 Coulomb-excitation benchmark；分离测量矩阵元与 static-pear interpretation。


## Day21 checkpoint124：条件证据与量词纠正

[[bucher-2016-144ba-direct-octupole]] BU16-1/2保B(E3)=48(+25/−34)W.u.及作者强八极支持；有限宇称位移/大E3与静态解释需共同模型审查，不得从650keV或统一零点能直接反判静态形变。[[xiao-2022-chirality-octupole-correlations-74as]] XA22-15仅限其比较解释。
