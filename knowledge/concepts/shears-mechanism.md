---
type: concept
title: "Shears Mechanism"
aliases: [shears mechanism, shears bands]
created: 2026-07-13
updated: 2026-10-25
status: ai-draft
review_status: unreviewed
concept_type: angular-momentum-generation
confidence: low
tags: [shears, magnetic-rotation, angular-momentum-alignment]
---

# Shears Mechanism

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

In the shears picture, high-j particle and hole angular-momentum vectors act as blades. Their gradual alignment increases the total angular momentum along a band, while the interaction and induced polarization determine the opening angle and transition strengths.

## Evidence Boundary

The mechanism is an interpretation of a configuration and its calculated angular-momentum geometry. A smooth energy sequence or changing B(M1) is not an independent proof without configuration, multipolarity and lifetime information.

## Relation to Alignment

This angular-momentum alignment is distinct from reaction-produced magnetic-substate alignment used in angular-distribution analysis. The two meanings must not be merged in `sigma/I` or P-ADO work.

## Necessary Assumptions

- The particle and hole blades belong to a resolved or explicitly proposed configuration.
- The interaction and any quadrupole polarization are specified before interpreting the angular-momentum path.

## Discriminating Observables

Spin-dependent angular momentum, frequency, B(M1), B(E2), and lifetime trends are used together.

## Supporting Evidence

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[chiara-2001-108-110in-shears-band-lifetimes]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]

## Counter-evidence and Competing Interpretations

Configuration crossing, quasiparticle alignment and ordinary collective rotation can change the same observables.

## Our Current Position

Keep shears-blade alignment distinct from reaction alignment and magnetic-substate population.

Day23纠正：旧Day21的“跨组态全段单调骤降、6–10倍与固定大比值”认证撤回，不作为本页判据。[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D22-R098-1/2的实际108In表既有组态内下降，也有alignment附近回升；[[clark-2000-shears-mechanism]] CL00-D23-001/002限定了角度和组态范围。新增为Codex self-audit，needs_review:true。

## Sources

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[chiara-2001-108-110in-shears-band-lifetimes]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[angular-momentum-alignment]]

## Review Status

New concept page; review pending.


## Day23 两blade几何的适用域

令经典无core模型I=jπ+jν、m=μ/μN=gπjπ+gνjν，jπ/jν/I均以ℏ为单位，χ为两blade夹角。以I方向为纵轴，在I²>0时

$$m_\perp^2=(g_\pi-g_\nu)^2\frac{j_\pi^2 j_\nu^2\sin^2\chi}{I^2},\qquad
I^2=j_\pi^2+j_\nu^2+2j_\pi j_\nu\cos\chi.$$

这是由m×I=(gπ−gν)jπ×jν得到的条件代数；半经典跃迁估计B(M1)/μN²=3mperp²/(8π)。[[clark-2000-shears-mechanism]] CL00-D23-001的sin²θπ使用的是**单blade相对I角**。等长两blade时θπ=θν=χ/2，从而B(M1)∝sin²(χ/2)，不能仍把χ叫同一个θ。TAC相对密度主轴的倾角又是另一对象；137Pr的25°/26°平均tilt不是实测shears开角。有限j的sqrt(j(j+1))处方、core R、changing configuration及量子涨落另需给定，不能把此无core代数当全量子禁戒或核态角度反演。

`system/scripts/day23_shears_geometry.py`以声明的整数/有理数向量检查投影恒等式、等长半角、平行极限、相同g抵消、互换与尺度平方；6项exact controls通过。chosen vectors无核素对应，不产生新角度、B、δ或τ。

实际实验比较须保留[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-12/13/16的τ—branch—ICC与feeding/stopping边界；[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-D22-R098-1/2只有相对B(M1)/B(E2)且43/2打印输入未闭合，不能把比值下降叫已测绝对M1下降。以上均needs_review:true。
