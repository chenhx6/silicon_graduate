---
type: concept
title: "Lorentz Boost Correction for In-Beam Gamma-Ray Angles"
aliases: [Lorentz angular correction, gamma-ray aberration correction, center-of-mass to laboratory angle correction]
created: 2026-07-13
updated: 2026-10-13
status: active
review_status: unreviewed
tags: [lorentz-boost, aberration, angular-distribution, linear-polarization]
---

# Lorentz Boost Correction

## Definition

For a moving emitter, Longfellow 2026 maps the laboratory angle to the center-of-mass angle with
`cos(theta)=(cos(theta_lab)-beta)/(1-beta cos(theta_lab))`, where `beta=v/c`. The laboratory angular distribution also carries a forward-compression solid-angle factor.

## Polarization Ratio

The same solid-angle factor is common to the numerator and denominator of the polarization ratio and cancels. The angle map does not cancel: the transformed angle remains in the Legendre and associated-Legendre functions and in the direction-polarization correlation.

## Necessary Assumptions

- `beta`, the beam axis, the event emission direction and the laboratory/center-of-mass coordinate convention must be specified.
- The same transformed direction must be used consistently in angular-distribution and direction-polarization calculations.

## Discriminating Observables

The laboratory angular distribution, polarization ratio, Compton-plane angle and event-by-event Doppler-corrected energy are separate checks on the transformation chain.

## Supporting Evidence

Longfellow 2026 gives the aberration relation, the common solid-angle factor, its cancellation in the polarization ratio and the separate Doppler-energy equation.

## Counter-evidence and Competing Interpretations

A small `beta` does not by itself prove that the angular correction is negligible; the size depends on angle and acceptance. Conversely, a common-factor cancellation in a ratio does not remove the angle transformation.

## Our Current Position

Treat Lorentz angular correction as an explicit in-beam formalism layer and report any numerical approximation. Do not substitute Doppler energy correction for angular aberration.

## Sources

This correction is not the same operation as Doppler correction of the gamma-ray energy. Both use event geometry and beta, but one transforms directions and the other transforms energy. Longfellow reports a 0 to -9% angular-distribution effect over the stated angular range and velocities, so beta should not be silently treated as zero without a quantitative check.

- [[longfellow-2026-gretina-energy-ordering-polarization]]

## Energy-corrected events retain a laboratory angular response

源L26-2/3/8的rawEq.(2)/(18)已于2026-10-13复核。对于速度沿所选polaraxis的toy，记 `c*=cosθ*`、`c_lab=cosθ_lab`，

$$c^*=\frac{c_{lab}-\beta}{1-\beta c_{lab}},\qquad
\frac{d\Omega^*}{d\Omega_{lab}}=\frac{1-\beta^2}{(1-\beta c_{lab})^2}\equiv J.$$

计数measure为**每个发射光子**，`W_lab=J W*(θ*)`，不另加入continuous-observer-arrival-time intensity因子。以E0=1000keV、restisotropic、β=.07的自设实验，exactenergyinverse可将所有photonenergy恢复1000keV，但J在forward/90°/backward为1.15054/0.99510/0.86916；“窄峰”不让J变成1。

在full-azimuth±5°lab bins中心90°和145°，先除各自labsolidangle，得到restisotropic情形下的labdensity145/90≈0.894825。若再乘自设labenergyresponse `ε(E_lab)=clip[0.5(E_lab/E0)^−0.8,0.01,0.99]`，同ratio≈0.935502。两者都不是Longfellow/GRETINA测量；它们展示energygate、angularcoordinate和labenergy-dependentresponse需要共同处理。

代码 [day13_doppler_aberration_acceptance.py](../../system/scripts/day13_doppler_aberration_acceptance.py)对β=0/.016/.07/.3/.5、isotropic与自设a2=.3/a4=.1检查whole-sphere归一化、Jacobian有限差分、finite-bin积分与MC、zeroβ及energyroundtrip；最大MCbin相对差1.69%，energyinverse残差≤6.9×10⁻13keV。realarray覆盖、alignment、feeding/polarization、tails和jointcovariance未建模；只有方法练习，没有新angular-coefficient或δ拟合。

**方向条件：**上述polaraberration式的angle是相对boostvelocityaxis。若recoilvector偏离beam/quantizationaxis，必须用同一event四矢量与完整坐标变换；不能把nominaldetector-to-beamθ代入velocity-axis公式后直接比较某个beam-axisW。源Longfellow的setup-specificframing不能无条件迁移到Mavelaback-scatteredprojectile或一般recoil角度。相关energy/vector/selection预算见 [[doppler-correction]]。
