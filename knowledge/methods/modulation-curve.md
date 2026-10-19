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

### 分区、角与Q名称的实际对照

[[tsuzuki-2021-sicdte-template-polarimetry]] T21-5/8/9/10：空间16区ν与φbin是两个索引维度；独立Ba null不同于同Krdata的MLE/modulationfit回代。T21 Eq8以Q为modulation、Π=Q/Q100；Go以Q′为modulation、P=Q′/Q_G；Morse已读UNCpreprint又是A0=Q_M Pbar/2。先比同一harmonic/P/response对象，再谈factor/效率/Σ，不能按Q名字对齐。

同pointsource的plane normal反号不改共同轴cos2φ（T21-12）；错误order仍可改incomingaxis、θ/ARM与selection，所以符号控制与全response控制不能互相替代。原T21统计/系统及作者线性合成值分开，两个同data的P不作独立平均。

### Endpoint计数差与cos2拟合系数要显式换号

[[bizzeti-2015-agata-triple-cluster-polarimetry]] B15-7–9：若N(φ)=a0+a2cos2φ、φ0/90正好为parallel/perp，则(N90−N0)/(N90+N0)=−a2/a0。源文操作以+a2/a0，需保留两namedquantity/anglezero的边界，不能只因都叫As就复制。Eq1/2与Jones pureE2 probe可用ψ旋转π/2映射，实际producer/beamplane与E-fieldplane仍未核。

对R(φ)及R(φ+π)取平均会消oddharmonics，cos2保留；regionwise不同P/效率不能只靠该对称化消除。sourceTables3/4的分析能力是modelP与实验As之比；同MC no-tracking/Table5不计新独立实验，bin-integrated sinc与unknownfitweights各自保存。


### 三种旧记号的同一计数映射

[[fagg-hanna-1959-polarization-measurements]] FH59-5/8/9原件分开：

| source中的量 | 原定义/对象 | 在同一plane-axis和response对象下的映射 |
| --- | --- | --- |
| FH59 p | J0/J90，光子electric强度比 | P_plane=(p−1)/(p+1)，不是SU59的p |
| FH59 linear R | dσ90/dσ0或相应finitegeometryresponse ratio | Q=(R−1)/(R+1) |
| FH59 r=N0/N90 | EqIII1 (p+R)/(pR+1) | r=(1−QP)/(1+QP)，A=(1−r)/(1+r)=QP |
| SU59 P | electricnormal减plane，见SEH59-4 | P_SU=−P_plane；先按Fig3读counterroles |
| FH59 circular R | EqIII3 2(N+−N−)/(N++N−) | 另一个observable；2及磁化方向不可省 |

这些恒等式只给匹配轴/两方向response的重参数化，不将原p当成现代Q，也不认证两实验角平均一致。unpolarized或R=1的r=1、pureparallel的r→1/R均有解析控制。
