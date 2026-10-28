---
type: concept
title: 八极关联
aliases: [octupole correlation, octupole correlations]
created: 2026-07-13
updated: 2026-09-21
status: active
review_status: unreviewed
concept_type: reflection-asymmetric-correlation
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [octupole, reflection-symmetry, collective-motion]
---

# 八极关联（Octupole Correlation）

## Definition

相反宇称轨道与 E1 collectivity 等共同反映的 reflection-asymmetric correlations；不等同于稳定非零八极形变。

## Necessary Assumptions

需要相反宇称结构的可靠连接和 spin/parity assignments，并排查 configuration mixing 与普通 E1 decay。

## Discriminating Observables

E1 links、`B(E1)/B(E2)`、[[energy-displacement]]、相反宇称轨道耦合与 `beta30` PES。

## Supporting Evidence

[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 报告八条 Band 1–3 E1 links，并用 branching/energy systematics 与 MDC-CDFT softness 支持 `78Br` octupole correlations。

[[guo-2020-pseudospin-chiral-quartet-131ba]] 在 `131Ba` 建立从负宇称 D7 到正宇称 D3-D6 的多条直接 E1 links，并比较同初态 relative E1 ratios；它把 octupole correlations 延伸到 pseudospin-chiral quartet 与另一 chiral-doublet candidate 的连接。RAT-PRM `β3=0.05` 是 tentative input，不是 stable octupole deformation 的测量。

[[xiao-2022-chirality-octupole-correlations-74as]] 在 `74As` 建立三条 Band-3→Band-1 E1 links，并比较 relative `B(E1)/B(E2)` 与 `δE`。其结果接近 `78Br` correlations、明显偏离 stable-octupole `224Th`；另有 `372.4-keV` low-lying E1，但不属于这三条 band-to-band links。

[[li-2024-144ba-octupole-cdf-3d-lattice]] supplies a theory-side contrast: a self-consistent `144Ba` `β30` minimum and stable mean-field evolution, but no parity projection or quantum parity splitting. It anchors the model layer without converting octupole correlations in `74As/78Br` into stable deformation.

[[gaffney-2013-pear-shaped-rn-ra]] supplies a direct experimental E3/Q3 layer: `220Rn` and `224Ra` Coulomb-excitation matrix elements distinguish weaker from stronger octupole collectivity, while the static-versus-vibrational label still requires model and parity-systematics checks.

[[bucher-2016-144ba-direct-octupole]] supplies a stronger direct E3 comparator in neutron-rich Ba (`B(E3)=48^{+25}_{−34} W.u.`). It anchors the observable layer without making `E1` links or relative `B(E1)/B(E2)` ratios in `74As/78Br` equivalent to a measured static `β3`.

[[bucher-2017-146ba-direct-octupole]] shows a comparable direct E3 strength in `146Ba` (`48^{+21}_{−29} W.u.`) while its E1 dipole moment is strongly reduced. The pair of Ba measurements supports an E3-first evidence ladder and separates octupole strength from isotope-dependent dipole cancellation.

[[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] supplies the pre-1996 theoretical/experimental evidence map, emphasizing E1 cancellation sensitivity, collective E3 strength, opposite-parity orbital couplings and the need to keep static, soft and vibrational interpretations separate.

[[wang-2023-experimental-studies-nuclear-chirality-china]] 的 Br-isotope review synthesis 把 measured/calculated doublet splitting 与 E1-related systematics 合并，提出 octupole correlations 可能使 chirality evolution 提前。但 Fig.12 的 TPRM 本身保持 reflection symmetry，跨核素数据也来自异质来源，因此“catalyze chirality”只保留为可检验的二级解释，不写成因果事实。

## Counter-evidence and Competing Interpretations

`74As/78Br` ratios 与 `δE` 都明显偏离 stable-octupole `224Th`；因此不支持无条件 stable deformation 表述。`74As` 还缺 lifetimes/absolute E1 strength，Band 3 的 `f5/2/p3/2` occupation 也未解开。

## Related Nuclei and Bands

- [[78br]]，Bands 1 与 3。
- [[74as]]，Bands 1 与 3。
- [[131ba]]，D7 与 D3-D6。

## Our Current Position

保留为多观测量加模型支持的 author interpretation。

## Sources

- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]
- [[guo-2020-pseudospin-chiral-quartet-131ba]]
- [[xiao-2022-chirality-octupole-correlations-74as]]
- [[wang-2023-experimental-studies-nuclear-chirality-china]]
- [[li-2024-144ba-octupole-cdf-3d-lattice]]
- [[gaffney-2013-pear-shaped-rn-ra]]
- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]

## Evolution Log

- 2026-07-13：建立 correlations 与 stable deformation 的边界。
- 2026-08-11：加入 `131Ba` direct E1 network 与 RAT-PRM comparison；保留 relative-strength、tentative-β3 和 stable-deformation exclusions。
- 2026-08-11：加入 `74As` 三条 Band-3→Band-1 E1、relative ratios/`δE` 与 `224Th` counter-benchmark；分离额外 low-lying E1。
- 2026-08-11：加入 Wang 2023 Br-isotope octupole/chirality cross-source hypothesis，并明确 reflection-symmetric model 与因果边界。
- 2026-09-20：加入 `144Ba` CDFT theory-side contrast；保持 correlations、softness 与 stable mean-field deformation 的三层分离。
## Day 25 正式核验：八极关联微观驱动机制与偶极相消反例

在 Day 25 研学窗口的深入推演中，结合 [[bucher-2016-144ba-direct-octupole]]（BU16-D25P-A005-01）、[[bucher-2017-146ba-direct-octupole]]（BU17-D25P-A005-01）与本 run 独立分析工件 day26-octupole-overlap-control-018.json，确立了八极关联的微观单粒子驱动规律与关键证伪边界：

1. **$\Delta l = \Delta j = 3$ 轨道对费米面驱动机制**：
   八极关联的微观起源来自费米面附近满足 $\Delta l = \Delta j = 3$ 的相反宇称单粒子轨道对之间的强烈相干八极耦合（$\langle j_1 \Vert r^3 Y_3 \Vert j_2 \rangle$）。在典型八极关联区，核心母轨道对包括：
   - 钡—钕区（$Z \approx 56, N \approx 88$）：质子 $\pi(d_{5/2}, h_{11/2})$ 与中子 $\nu(f_{7/2}, i_{13/2})$；
   - 镭—钍区（$Z \approx 88, N \approx 134$）：质子 $\pi(f_{7/2}, i_{13/2})$ 与中子 $\nu(g_{9/2}, j_{15/2})$；
   - 砷—溴区（$Z, N \approx 34–38$）：质子与中子 $\pi,\nu(p_{3/2}, g_{9/2})$。

2. **反例确证：E1 强度的剧烈起伏不能脱离八极关联单独解释**：
   - $^{144}\text{Ba}$ 与 $^{146}\text{Ba}$ 直接库仑激发实测 $B(E3)$ 均维持在 $\approx 48\text{ W.u.}$ 的高集体性水平（置信区间在 $[19, 69]\text{ W.u.}$ 高度重叠），表明全核八极电荷多极跃迁集体性稳定存在；
   - 然而两核的内禀偶极矩幅值相差超过一个数量级（$D_0 \approx 0.13\text{ e fm} \to 0.015\text{ e fm}$）；
   - 微观自洽 Gogny D1S SCCM 计算确证：偶极算符 $\hat{D}_z = e \frac{N}{A} \sum_p z_p - e \frac{Z}{A} \sum_n z_n$ 中质子与中子符号相反，中子数增加时特定低 $K$ 轨道（$h_{9/2}, f_{7/2}, i_{13/2}$，占据 $0.40, 0.27, 0.20$）的占据引起中子质心反向移动，产生内禀偶极相消点。这确立了 **$E1$ 跃迁强度的微弱决不代表八极关联的猝灭，亦不可用弱 $E1$ 否定八极形变**。
