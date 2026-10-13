---
type: method
title: "γ-ray tracking array analysis"
aliases: [tracking array, gamma-ray tracking array, γ-ray tracking array, GRETINA, AGATA, tracking-array response function]
created: 2026-07-09
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
method_type: gamma-ray-tracking
tags: [gamma-ray-tracking, angular-distribution, angular-correlation, linear-polarization, pado-support]
---

# γ-Ray Tracking Array Analysis

## Purpose

γ-ray tracking arrays use segmented HPGe crystals and tracking algorithms to reconstruct gamma-ray interaction positions and directions. They enable continuous-angle angular correlations, angular distributions and linear-polarization measurements.

## Inputs and Assumptions

- Calibrated segmented HPGe interaction positions and tracking output.
- Energy-, angle- and configuration-matched response functions or event-mixing references.
- Control of clustering holes, tracking halos, finite detector population and Doppler/Lorentz effects when relevant.
- Separate modeling of detector response and nuclear alignment/population assumptions.

## Source-Level Foundation

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] states that tracking arrays such as AGATA and GRETINA can determine photon interaction points with high precision, so conventional detector solid-angle attenuation coefficients can often be close to unity. The same source emphasizes that angular-distribution extraction remains non-trivial because tracking, decomposition, detector tiling and clustering effects create response functions that differ from older ring-detector arrays.

## Key Method Boundary

Tracking arrays can reduce one classical detector-geometry correction, but they do not remove the need to model nuclear alignment, magnetic-substate population, deorientation or feeding history. In Lauritsen 2025, detector solid-angle attenuation and nuclear alignment attenuation are explicitly different uses of `alpha_k`.

## Longfellow 2026 Connection

Longfellow et al. demonstrate a GRETINA in-beam path that orders interaction points by energy, uses event-by-event Doppler correction, and applies the laboratory-frame Lorentz angle transformation before comparing angular distributions and polarization. Their result is a method characterization under stated conditions, not a claim that simple ordering is universally superior to full tracking. See [[lorentz-boost-correction]], [[doppler-correction]] and [[longfellow-2026-gretina-energy-ordering-polarization]].

## Project Relevance

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this page is only an instrumentation/method anchor. It supports the statement that a modern tracking-array formalism still contains explicit `Pm(J)` and `sigma/J` assumptions for in-beam angular distributions; it does not provide a universal `sigma/I` prior.

## What It Can Establish

Tracking arrays can provide continuous-angle angular correlations, angular distributions and linear-polarization observables. With proper response treatment, they can help constrain multipolarity, parity, mixing ratio and alignment assumptions.

## What It Cannot Establish Alone

Tracking-array data do not remove the need for a population/alignment model. They do not by themselves define a transferable `sigma/I` value, and response-function systematics can still affect extracted angular-distribution coefficients.

## Sources

- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]

## Recoil information and high-energy tracking boundary

[[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3的98Zr校正line从8.6(1)降到5.5(1)keV，支持photon first point与独立recoil vector/target vertex的共同重建。[[crespi-2013-agata-high-energy-doppler-response]] CR13-3在另一个15.1MeV实验中将segment122keV改为PSA119keV，作者将剩余floor归于未逐事件测得的12C速度向量。这两个独立例子不能转移数值，但限制“PSA位置精细化足以保证intrinsic resolution”的判断。

Crespi CR13-5/6又展示效率/背景tradeoff：在single15.1MeV、pair-production重要、低background情况下，add-back+PSA+1HitID约为其standard mgt tracking FEP的4倍；而source多γ的neutron-capture sum peak则由tracking抑制。不能将4倍推广到高multiplicity级联、其它能区或算法；fixed peak gate的line身份/centroid/width与efficiency要同时验证。原[[longfellow-2026-gretina-energy-ordering-polarization]]的GRETINA energy-ordering结果保留其setup-specific范围。

## Position validation and selection response

[[akkoyun-2012-agata-instrument-response]] AK12-1/2指出PSA位置依赖basis、noise/cross-talk和多hit，crystaltilt/targetpoint在tracking阶段进入；Fig39的positionFWHM随γenergy变化，不可用一个nominal5mm当所有point的σ。AK12-5的静止60CoComptonimage验证减少recoilnuisance，与beamDopplercheck互补，但PSA/sequence/calibration仍共享。

AK12-6的实际threeATCsource测试中，P/T从16.8%提高至53.9%，tracking/rawFEP保留84.5%；该效率ratio的分母是rawcrystalspectrum，不是所有发射γ。threshold、single-hit拒绝、energy/multiplicity、passivematerial和gate共同定义selection。图表/algorithmreplays与同一sourceacquisition是dependent，不把更干净谱当作更强结构证据。AK12-7的rawtrace/replay链提供更改PSA/geometry/selection后复核的方法；原event未取得，不声称已复算source性能。

## Neutron background and executed cut semantics

[[senyigit-2014-agata-neutron-rejection]] SY14-2/4的Ge-recoildeposits会在γenergy高能侧形成bumps；TOF-labelledγ不自动是目标核，附近材料真γ仍可留在g门。SY14-5/8的count-ratiodenominators与P/T分开，algorithm可能重组clusters，trackingefficiency不直接是binomialprobability。

SY14-6/7定位body/table/conclusion的gatepredicate与Co列label冲突。acceptORgood与rejectORbad不互为补集，sign/equality也不能随意改写；未取得productionmgt/publisherversion和eventreplay前，保留literalconditions和reportedtables，不推荐自动实施某个假定cut。sourceTables2/3/4为同次数据或model比较，重复图/表不新增独立证据。
