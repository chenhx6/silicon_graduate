---
type: method
title: "Compton Polarimetry Modulation Curve"
aliases: [modulation curve, azimuthal modulation curve, Q-prime modulation factor]
created: 2026-07-13
updated: 2026-07-13
status: active
review_status: unreviewed
method_type: detector-response-analysis
tags: [modulation-curve, compton-polarimetry, detector-response]
---

# Modulation Curve

## Purpose

A modulation curve summarizes the azimuthal response of a Compton polarimeter after the chosen event and background treatment. It is a detector-level bridge to polarization, not a nuclear-structure model result.

## Inputs and Assumptions

- Measured azimuthal events, a response or unpolarized reference distribution, background treatment and a defined angle convention.
- The accepted event multiplicity, Compton-angle range and detector coverage are held fixed when comparing amplitudes.

## Source Forms

- Go 2024 defines a measured-minus-background azimuthal distribution divided by the unpolarized simulation and fits `A(1+Q' cos(2(phi-phi0)))`. The fitted `Q'` is proportional to the degree of polarization and is converted to a full-polarization sensitivity only after `P` is inferred.
- Longfellow 2026 fits `W_C(xi)=N(1-A0 cos(2xi))`, with `A0=1/2 Q Pbar` after integrating over GRETINA's laboratory-angle and Compton-angle coverage.

## Review Boundary

The two forms use different normalization and angle conventions. They should not be compared by numerical amplitude alone without matching background, source-response, event-selection, coverage and sign conventions.

## What It Can Establish

It can characterize a detector modulation amplitude and, with calibrated `Q` or `Q'`, support a polarization estimate.

## What It Cannot Establish Alone

It cannot make a detector modulation into a unique multipolarity, parity or mixing-ratio assignment without nuclear and response constraints.

## Sources

## Sources

- [[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]]
- [[longfellow-2026-gretina-energy-ordering-polarization]]

### 模板归一应保留统计对象

[[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]] G24-17/23/24：能谱归一νj、φhist与background/MC templates的来源和共有事件须先定义，才能判fixedscale、profile或conditional likelihood。Go原分区/producer/Cov未取得，不以推导代原CI。

对另声明的signal-only μi=νsi(P)、si>0、D=Σni>0、S=Σsi，scaleprofile为νhat=D/S，shape项为Σni ln(si/S)。有效Fisher信息

`Ieff=ν[Σ(s′i)²/si−(Σs′i)²/S]=ν/S Σi<j si sj(s′i/si−s′j/sj)²`。

纯scale变化s′i/si相同时，ν与P不可辨；S′=0时profile与固定scale的P信息相同。该特例既不证明原pipeline有bias，也不把data-derived scale一概视为无信息。实际background、finiteMC、eventcut和sharedfit需扩展统计模型。若同event的energy/φ marginals来自共同Poisson cells，Cov(Ee,Dφ)=μeφ，不能默认二者独立。

幅度归一另按G24-22与[[morse-2022-gretina-polarization-sensitivity]] M22-5保存：Q′=Q_G P、A0=Q_M Pbar/2，sameharmonic/同P合同下Q_G=Q_M/2。detectorresponse/efficiency/selection不同仍不能裸迁实际Q或F；数据声明/producer缺口需实际输入，不用digitized曲线当rawcounts。

M22这里的原式来自已核UNC author-preprint，VoR未取得，跨版本实际producer仍需另核；不将公式设计当对作者程序的错误判决。
