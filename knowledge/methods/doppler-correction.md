---
type: method
title: "Event-by-Event Doppler Correction"
aliases: [gamma-ray Doppler correction, Doppler energy correction]
created: 2026-07-13
updated: 2026-10-13
status: active
review_status: unreviewed
method_type: in-beam-gamma-spectroscopy
tags: [doppler-correction, in-beam, gamma-ray-tracking]
---

# Doppler Correction

## Purpose

In an in-beam experiment, the detected gamma-ray energy is corrected event by event using the residue velocity and the measured emission direction. Longfellow 2026 gives `E_gamma=E_gamma,lab (1-beta cos(theta_lab))/sqrt(1-beta^2)`.

## Inputs and Assumptions

- Residue velocity or `beta`, a target position and an event-by-event interaction direction.
- A stated frame convention and an energy peak or transition gate to which corrected events are compared.

## What It Can Establish

It can place events in a consistent rest-frame energy gate and support Doppler-corrected spectra or full-energy event selection.

## What It Cannot Establish Alone

It does not replace the Lorentz angular aberration, detector-response calibration or nuclear-population model used for angular distributions and polarization.

## Sources

Doppler energy correction places an interaction event in the correct full-energy peak and supports event selection. It does not replace the Lorentz aberration that maps center-of-mass and laboratory angles for angular distributions or polarization. The two corrections should be documented separately.

## Source

- [[longfellow-2026-gretina-energy-ordering-polarization]]
- [[tracking-array]]

## Day 13 preview: velocity uncertainty and stopping history

Let `θ_lab` be the angle from the residue-velocity vector to the detected photon direction. The rest-frame energy is

$$E_0=E_{\gamma,lab}\,\gamma(1-\beta\cos\theta_{lab}),\qquad \gamma=(1-\beta^2)^{-1/2}.$$

For small independent uncertainties in measured energy, `β` and angle, first-order propagation uses

$$\sigma_{E_0}^2\simeq[\gamma(1-\beta c)\sigma_{E_{lab}}]^2+[E_{lab}(\gamma^3\beta(1-\beta c)-\gamma c)\sigma_\beta]^2+[E_{lab}\gamma\beta\sin\theta\,\sigma_\theta]^2,$$

where `c=cos(θ_lab)` and `σ_θ` is in radians. Correlated `β`/angle estimates require covariance terms. In the low-`β` limit, the fractional velocity and angle contributions approach `cos(θ)σ_β` and `β sin(θ)σ_θ`; the sign convention and angle frame still need to match the cited experiment.

### Illustrative uncertainty calculation

For a hypothetical `E_0=1000 keV` line, use Klemme's reported mean `β=0.016`, assume the residue velocity is parallel to the beam, take `θ_lab=31.7°` at the edge of its first detector ring, and assume independent uncertainties `σ_β=0.001`, `σ_θ=1°`, `σ_E_lab=1 keV`. The Lorentz transform gives `E_lab=1013.671 keV` and returns `E_0=1000.000 keV`; first-order propagation gives `σ_E0=1.308 keV`. The velocity term alone is `0.847 keV`; this demonstrates why a mean recoil speed cannot stand in for its uncertainty. The energy, velocity uncertainty, angular uncertainty and beam-axis alignment assumption are illustrative, not Klemme measurements or an event-level velocity reconstruction.

### Event correction versus stopping analysis

The S3 ring/sector hit position and particle-γ gate in Mavela's `32S` Coulomb-excitation experiment determine which directions/events enter the Doppler-corrected yield (DD-20261012-32S-05). Klemme's `134Nd` recoil-distance analysis instead retains shifted/unshifted components over target-stopper distances. Its mean recoil speed was `1.6% c`; for lifetimes below about `2 ps`, the roughly `1.1 ps` Au-stopper slowing time required a finite-stopping correction (KL99-4/17). Correcting a photon energy to a residue rest frame does not remove the physical velocity history used by DSAM/RDDS to infer a lifetime.

The following is a diagnostic design aid, not a claim that any one spectral pattern uniquely determines its cause:

| Candidate cause | Expected spectral behavior | Useful companion check |
|---|---|---|
| Residual velocity/direction error | A corrected centroid or width retains detector-angle dependence; residual trends can follow `cosθ_lab`. | Recheck recoil-vector and interaction-point reconstruction, detector ring/sector mapping, and a known transition under the same gate. |
| Deceleration or post-stop emission | Shifted/unshifted fractions or line shape change with target-stopper distance; short-lifetime cases may need finite-stopping treatment. | Compare distance-resolved gated components and a stopping-power sensitivity, as in the Klemme DDCM/finite-stopping chain (KL99-2/4). |
| Two nearby transitions | Two rest-frame centroids persist after angle correction and can have different coincidence partners. | Use separate γγ gates, energy sums and contamination checks; do not infer a doublet from width alone. |

These signatures can coexist. A single broad peak or a corrected centroid alone cannot distinguish them without angle, gate and distance-resolved companion data.

These sources establish a geometry/gating and stopping-history boundary, but they do not provide a reusable covariance package for arbitrary detector arrays or events. The analysis remains source-specific until β, hit position, response and their uncertainties are supplied.

#### Conditional consequence if the printed ring-20 β were applied

The two-body check gives a model `β_true=0.07025267` at the Appendix C ring-20 angle; the printed array instead gives `β_used=0.71259276` (DD-20261013-32S-15/16). If a `2230.57-keV` transition were emitted at the model speed but corrected using the printed value, the ratio would be

$$\frac{E_{corr}}{E_0}=\frac{\gamma(\beta_{used})(1-\beta_{used}\cos\theta_\gamma)}{\gamma(\beta_{true})(1-\beta_{true}\cos\theta_\gamma)},\qquad \gamma(\beta)=(1-\beta^2)^{-1/2}.$$

| Hypothetical `θγ` from the outgoing residue velocity | `E_corr/E_0` | `E_corr` (keV) | Residual (keV) |
|---:|---:|---:|---:|
| 60° | 0.94856 | 2115.832 | −114.738 |
| 90° | 1.42184 | 3171.506 | +940.936 |
| 120° | 1.86299 | 4155.534 | +1924.964 |

These directions are illustrative γ–recoil angles, not measured AFRODITE crystal positions; `β_true` is a simplified two-body model value, not event data. The calculation shows that literal production use would be a major ring-specific problem, while the summed thesis spectra cannot establish whether ring 20 used that value or how many events it contributed. The highest-value check is the ring-20-only corrected line and its centroid/width relative to adjacent rings, using the executed sorter and matched calibration. No raw ring-gated spectrum or response/covariance is available, so this is a conditional consequence, not a correction to the source or a result about the published `Q_S`.

#### Possible ring-24 listing anomaly

Extrapolating the ring-angle trend from rings 22–23 predicts `β24=0.0717129405`; the printed `β24=0.0712114` is lower by about `0.00050154`. The digit-substitution candidate `0.0717114` differs from the extrapolation by only `−1.54×10⁻6` (`−0.00215%`) (DD-20261013-32S-22). This suggests a second possible array transcription issue, but the printed value remains unchanged pending the production file and ring-24 spectrum.

#### Elastic-like versus excited-projectile kinematics

Using the Appendix C ring angles, nominal `T_lab=120.3 MeV`, `m_a=32u` and `m_T=194u`, compare the printed β array against two conditional two-body calculations: elastic projectile `E_x=0` and the emitting `2_1+` state `E_x=2.23057 MeV`. Replace ring20 by the local decimal-shift candidate, then exclude ring20 from the residual calculation:

| Assumed final projectile state | RMS residual, excluding ring20 | RMS, excluding ring20 and ring24 |
|---|---:|---:|
| Elastic-like `E_x=0` | `0.000167687` | `0.000154722` |
| Excited `E_x=2.23057 MeV` | `0.000982494` | `0.000998916` |

The table is about 5.9–6.5 times closer to the elastic-like calculation under these simplified inputs. This suggests the listed β values may use elastic-like kinematics or another velocity convention; it does not prove how the authors generated the array. Both models use mass-number masses, a ground-state target and no energy-loss, target-depth or response terms.

#### Target-mass sensitivity and the thesis isotope mismatch

The thesis has an internal target label conflict: one S3 setup paragraph on PDF file p.41 / printed p.32 says `196Pt`, while Chapter 3 and the GOSIA Appendix D input state `194Pt` at `120.3 MeV` (DD-20261013-32S-25). Repeating the simplified model with `m_T=196u`, and excluding the candidate rings 20 and 24, gives:

| Target mass input | `E_x=0` RMS residual | `E_x=2.23057 MeV` RMS residual |
|---|---:|---:|
| `194u` | `0.000154722` | `0.000998916` |
| `196u` | `0.000032926` | `0.000815665` |

The printed beta array is numerically closest to the `196u`, `E_x=0` model under these assumptions, but the thesis GOSIA input explicitly lists `194Pt`. The residual comparison can flag a possible mass/state convention carried into the beta array; it cannot identify the physical target or the executed sorting input (DD-20261013-32S-26).

If the ring20 decimal-shift candidate `β_used=0.071259276` were used where the excited-projectile model gives `β_true=0.07025267`, the conditional residual for a `2230.57-keV` line would be:

| Hypothetical `θγ` from the outgoing residue velocity | Corrected line residual (keV) |
|---:|---:|
| 0° | −2.255 |
| 60° | −1.004 |
| 90° | +0.160 |
| 120° | +1.244 |
| 180° | +2.258 |

These angles are illustrative, not measured detector directions. A small state-assumption difference can create a residual of order a few keV, but no angle-gated peak fits, event velocities or matched response are available to test it (DD-20261013-32S-23).

### Sources

- [[longfellow-2026-gretina-energy-ordering-polarization]] L26-8 — event-by-event energy transform and its separation from angular aberration.
- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261012-32S-05/06/07/08/09 and DD-20261013-32S-10/11/12/13/14/15/16/17/18/19 — S3 position/gating, repository inventory/search, Appendix C ring β inputs, 9%/7% wording, geometry, conditional ring-20 impact and residual design.
- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-20 — local interpolation suggests `0.071259276` as a likely printed-list decimal correction, not a verified production value.
- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-22/23 — potential ring-24 digit issue and elastic-like versus excited-projectile velocity-model check; these do not establish the production sorter convention.
- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-25/26 — internal `194Pt`/`196Pt` text conflict and target-mass model sensitivity; not an independent target identification.
- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-24 — as-printed S3 `y` component cancels ring angle under the same spherical-coordinate convention used for clovers; execution and intended convention remain unverified.
- [[mehl-2015-ithembalabs-coulomb-sorting-thesis]] ME15-1/2/3/4/5 — independent 20Ne+194Pt run; S3 at 15 mm, ring-angle mapping and GEANT4-derived β method, not Mavela event data.
- [[klemme-1999-lifetimes-134nd-neighbors]] KL99-2, KL99-4, KL99-17 — shifted/unshifted distance diagnostics, velocity, ring geometry and finite-stopping correction.

### Source-level velocity conflict

Mavela's abstract associates `9% c` with γ-ray emission, while Sec.4.3 writes `v_p≈7% c` (DD-20261012-32S-06). A relativistic incident-beam estimate for `120.3 MeV` `32S` using `M≈32u` gives `β≈0.089572`, matching the 9% scale, but the abstract does not identify it as the incident speed. More directly, Appendix C's printed sorting code sets `d_target2s3=-1.30`, lists `angdis[1:24]` and ring-indexed `beta[1:24]`, and applies `beta(rr)` in the Doppler loop (DD-20261013-32S-14). The listed ring β values are mostly `0.0673–0.0716`, which supports the analysis section's ≈7% correction scale; however, ring 20 is printed as `0.71259276` (DD-20261013-32S-15/16), and the executed sorter version is unavailable. Thus the displayed code supports a post-scattering ring correction around 7%, while the abstract's 9% wording and the ring-20 outlier remain unresolved. Total spectra still show no angle-gated centroids or applied-code provenance (DD-20261012-32S-07).

#### Conditional two-body stage check

The thesis places S3 upstream for back-scattered particles and gives its dimensions/rings (DD-20261012-32S-05). The setup prose omits its distance, but Appendix C supplies `d_target2s3=-1.30` beside `d_target2ge=19.60`; the main text says the HPGe clovers are 19.6 cm from target, making a centimeter interpretation plausible but not explicitly declared (DD-20261013-32S-14/16).

$$E_a+m_T=\sqrt{p_b^2+(m_a+E_x)^2}+\sqrt{p_a^2+p_b^2-2p_ap_b\cos\theta_{lab}+m_T^2},\quad E_a=\sqrt{p_a^2+m_a^2},$$

using `m_a=32u`, `m_T=194u`, `T_lab=120.3 MeV`, `E_x=2.23057 MeV`, and an unexcited target. The outgoing speed is `β_b=p_b/√(p_b²+(m_a+E_x)²)`: it is `0.07000` at `θ_lab=114.32°`, `0.06487` at `150°`, and `0.06343` at `180°`. These are calculated kinematic possibilities, not measured S3 gates or an event-level reconstruction. Because the abstract attaches `9% c` to γ emission, this calculation does not settle whether the text describes two stages, rounded values or a source error; the target state, ring-angle acceptance and correction input remain unknown (DD-20261013-32S-10).

Figure 3.8 gives S3 active diameters of 22 and 70 mm, hence radii `r=11–35 mm` (DD-20261012-32S-05). Under a nominal centered face-on mount, `θ_lab=180°−atan(r/d)`. Appendix C lists `d_target2s3=-1.30` beside `d_target2ge=19.60`; the same-unit interpretation is `d≈−13 mm`, supported by the main text's 19.6-cm clover distance. Its ring-angle array spans `2.39969–1.93024 rad` (`137.49°–110.59°`), consistent with the geometry, and its ring β table is near 7% except ring 20 (DD-20261013-32S-14/15/16). The distance unit and executed sorter version are not explicit, so treat this as the printed code configuration, not proof of every analyzed event.
The source's `angdis[1:24]` array spans 2.39969–1.93024 rad and `beta[1:24]` supplies one correction speed per ring. Using the two-body assumptions above at each listed ring angle, the 23 non-ring-20 code β values differ from the model by RMS `0.0009825` (maximum absolute difference `0.0010158`); ring 20's model β is `0.07025267`, while the printed input is `0.71259276`, a factor `10.14` larger (DD-20261013-32S-14/15/16). This comparison checks scale and exposes an array outlier; its systematic offset may reflect target excitation, energy loss or another velocity convention, so it cannot replace the printed value or prove the executed result.

#### Local smoothness check of the ring-20 entry

Appendix C gives ring 19 `(θ=1.98381 rad, β=0.0711295921)`, ring 20 `(1.97192 rad, β=0.71259276)`, and ring 21 `(1.96067 rad, β=0.0713829171)` (DD-20261013-32S-15). Linear interpolation between rings 19 and 21 at the printed ring-20 angle predicts `β20=0.0712597578`. The decimal-shift candidate `0.071259276`—the printed number divided by ten—differs by `−4.82×10⁻7`, or `−0.000676%` (DD-20261013-32S-20). This strongly favors a missing-zero/decimal transcription in the printed array, but the interpolation neither edits the source value nor shows what was used in the executed sorter.

#### Printed S3 direction transformation

Appendix C p.74 prints `xb=d sinφ sinθ`, `yb=d sinθ`, and `zb=d cosφ sinθ` for the S3 hit vector, with `θ=angdis[rr]`; the clover vector on the same page uses the conventional `y=d cos(theta)` form. Algebraically the printed S3 vector has norm `|d sinθ|√2`, so after normalization `angdis[rr]` cancels and, for `d<0`, its polar angle relative to `+y` is fixed at `135°`. The listed ring angles span `110.595°–137.492°` (DD-20261013-32S-14/24). Under a shared spherical convention, the printed coordinate transform therefore does not carry the ring-dependent polar direction into the dot product. The thesis does not state a different convention or show that this listing matches production code; verify the executable and ring-gated centroids before attributing an analysis effect.
#### Independent iThemba S3 apparatus comparator

Mehl 2015 reports a separate `20Ne+194Pt` acquisition with AFRODITE and the same S3 family: for its 73-MeV backward run, S3 was 15 mm from the target and the authors report 113.4°–141.5° coverage; their 96-MeV forward run used a different angle range. The thesis computes ring θ from the target distance and ring inner/outer radii, and says β≈0.08c came from GEANT4 elastic-peak simulations (Mehl source [[mehl-2015-ithembalabs-coulomb-sorting-thesis]] ME15-1/3/4/5). A ring-edge calculation using 15 mm and the reported radii gives about 113.2°–142.6°, within roughly a degree of the reported bounds. This is an apparatus/method cross-check across a different run, not data or β transferred to Mavela. Mavela's Appendix C independently lists `d_target2s3=-1.30` and its own β array.
#### Wrong-β angle-residual discriminator

If the true residue speed is `β_t` but the correction uses `β_c`, then

$$E_{corr}(\theta_\gamma)=E_0\frac{\gamma_c(1-\beta_c\cos\theta_\gamma)}{\gamma_t(1-\beta_t\cos\theta_\gamma)},\qquad \gamma_i=(1-\beta_i^2)^{-1/2}.$$

For the conditional Mavela hypothesis `E_0=2230.57 keV`, `β_t=0.07000` and `β_c=0.0895718`, the exact transform predicts:

| Hypothetical `θγ` from the projectile velocity | `E_lab` (keV) | `E_corr` using `β_c` (keV) | Residual from `E_0` (keV) |
|---:|---:|---:|---:|
| 0° | 2392.579 | 2187.063 | −43.507 |
| 60° | 2305.801 | 2211.423 | −19.147 |
| 90° | 2225.098 | 2234.079 | +3.509 |
| 120° | 2149.854 | 2255.202 | +24.632 |
| 180° | 2079.531 | 2274.943 | +44.373 |

The sign-changing residual is a model prediction, not measured Mavela data; these angles are not AFRODITE crystal angles and response widths/centroid errors are unavailable. Appendix C's listed ring β array is near 0.07, so the table is a counterfactual test of applying the 9% incident-beam scale as a correction. A useful data test would fit the same transition's angle-gated corrected centroids against reconstructed `cosθγ`, with calibration lines and event-level projectile vectors. A common energy calibration shift would not by itself create this signed angular trend; direction or interaction-position errors could also do so (DD-20261013-32S-12/14/15).

For an illustrative `E_lab=1000 keV` photon, changing `β` from `0.070` to `0.08957` changes `E_0=E_lab γ(1−β cosθ)` by about `18.2 keV` at `θ=0°` and `1.58 keV` at `θ=90°`. The angle endpoints are sensitivity examples, not detector angles or a measured Mavela line. For Mavela's displayed sorting code, use the ring-dependent β array only as the printed configuration; verify the executed version and the ring-20 outlier before replay.

## Doppler correction 诊断表：峰位、峰宽与停止

本表为跨实验的诊断设计，`claim_kind: synthesis / our-inference`，不是从某种峰形直接指定原因。Mavela Eqs.(4.5),(4.6) 明确使用 photon–projectile 夹角，Fig.4.17 展示总校正谱；Klemme Fig.1 则保留同一跃迁的距离相关 shifted/unshifted 分量。这些实验独立，但本表和以下算式不是第三份独立实验。

| 待区分原因 | 有价值的观察 | 最小伴随观测或检验 | 反证与结论边界 | 原文 locator |
|---|---|---|---|---|
| 整体速度或核素/反应道速度用错 | 已知线的校正峰心随实际 γ–反冲夹角变化，前后角偏差可反号。 | 同一 emitter 的逐角环峰心、事件 β/方向、执行 sorter 与独立 energy calibration。 | 方向/位置误差也会形成角度残差；总谱窄峰不足以选 β。 | Mavela DD-20261013-32S-27；DD-20261012-32S-07 |
| 速度 spread 或未完全校正 | 峰宽随角度、粒子 ring 或反应道 gate 变化。 | 实际 β 分布、β–角度 covariance、相同能量的静止校准响应。 | 峰宽随角度变化仍可能由角分辨率造成；三种 variance 可有完全相同曲线。 | Mavela Eq.(4.6)；下方低速多解推导 |
| γ 交互位置、顶点或方向重建错误 | 不同 crystal/sector/ring 产生不同残差；某些几何条件下加重宽化。 | γ interaction-point/particle-vector/vertex metadata、position calibration，先核实坐标 convention。 | 不可用探测器到束轴的名义 θ 替代 γ–反冲夹角；粒子 ring 命中也不等于已测完整 β。 | Mavela DD-20261013-32S-27；DD-20261013-32S-24；Longfellow L26-8 |
| 反冲减速或停止后发射 | 同一跃迁的 shifted/unshifted 比例随 stopper distance 改变，或出现连续减速分量。 | 距离/时间分辨的同门谱、feeding 与 stopping-power sensitivity。 | 双峰不一定是两条跃迁；一律用初始 β 校正会制造残余分量。 | Klemme KL99-2；KL99-4；KL99-18 |
| 两条近邻跃迁 | 正确匹配各 emitter/velocity 后仍有两组静止系能量，且符合伙伴或 feeding 不同。 | 两个独立 γγ gate、energy sums、逐角度/时间比较、response-aware fits。 | 若尚未排除停前/停后分量或污染，双峰/宽峰不是新能级证据。 | Klemme Fig.1 的同跃迁反例；Mavela Fig.4.17 的总谱边界 |
| 真实物理宽化或探测器响应 | 宽度可能在不同角度/门下持续存在。 | 校准源 response、独立 lifetime 与 line identity，及未校正速度历史。 | 对 ps 寿命，本征自然宽度 Γ=ℏ/τ 远小于 keV；不能把 keV 宽峰直接称为自然寿命线宽。 | Klemme Table II（寿命输入）；Γ 关系为通用物理背景 |
| 把一种 emitter 的校正用于另一种 | projectile/target 或污染核素的线表现不同。 | 保留 raw 与各 emitter-corrected 谱、核素/反应道 gate、效率与计数谱身份。 | Mavela 用 uncorrected target line 和 corrected projectile line 作不同 yield 输入；没有证明 target β=0。 | Mavela DD-20261013-32S-28 |
| 以校正谱替代角分布/偏振的 frame 处理 | 能量 gate 已恢复但角分布仍可能有 boost/acceptance 改变。 | 分别记录 energy transform、angular aberration 与响应。 | 能量校正成功不等于完成 angular/polarization Lorentz transformation。 | Longfellow L26-8；Relativistic Correction Boundary |

### 精确 Jacobian 与协方差练习

从 Mavela Eq.(4.6) 反演记 `f(E,β,θ)=E γ(1−β cosθ)`，其中 θ 是实验室 photon direction 相对发射核速度的夹角。对 `x=(E,β,θ)`，正确的一阶传播是

$$\sigma_f^2=J\Sigma J^{\mathsf T},\quad
J=\left(\gamma(1-\beta c),\ E[\gamma^3\beta(1-\beta c)-\gamma c],\ E\gamma\beta\sin\theta\right),\quad c=\cos\theta.$$

角度以 rad 输入，β 为无量纲；若只有 β–θ 相关，还需加 `2 Jβ Jθ Cov(β,θ)`。β 的无量纲 fractional coefficient 为

$$\frac{J_\beta}{f}=\frac{\beta-c}{(1-\beta^2)(1-\beta c)},\qquad
\frac{J_\theta}{f}=\frac{\beta\sin\theta}{1-\beta c}.$$

固定速度与几何的整体误差产生 signed bias；随机 spread 才进入 variance，不能把二者混为一个 σ。

[[crespi-2023-agata-tracking-performance]] C23-8 的原Eq.(7)独立给出相同导数，且明确说明其Eq.(6)为简化而忽略correlation。`Jβ=E_lab γ³(β−cosθ)`，故在固定lab angle的一阶速度敏感度为零时，`cosθ=β`；β=.07/.20/.50对应约85.986°/78.463°/60°。90°只是β→0的近似。这个零点并不使photon-angle uncertainty或intrinsic response消失，也不是总分辨率/efficiency的普遍最优角度。

**自设例题：** `E0=1000 keV, β=0.07, σE_lab=1 keV, σβ=0.002, σθ=2°`，先取三项独立；所有数值均非 Mavela 或 Klemme 测量。

| θ_lab | E_lab (keV) | E0 反演 (keV) | energy / β / angle signed σ contributions (keV) | 合成 σE0 (keV) |
|---:|---:|---:|---|---:|
| 35° | 1058.226372 | 1000.000000 | +0.944977 / −1.597270 / +1.486764 | 2.377966 |
| 90° | 997.546991 | 1000.000000 | +1.002459 / +0.140689 / +2.443461 | 2.644848 |
| 145° | 943.449018 | 1000.000000 | +1.059941 / +1.690147 / +1.325506 | 2.395211 |

90° 只有一阶低速的 β 系数为零；精确相对论项仍非零，而角度项在本例较大。丢弃 γ 因子会将三行反演值都变成 `997.546991 keV`，即共同偏低 `2.453009 keV`，这可与 calibration scale 混淆。

在35°保持相同 marginal σ，只令 `ρβθ=−0.8,0,+0.8`，所得 σ 分别为 `3.0748,2.3780,1.3620 keV`；145° 则为 `1.4672,2.3952,3.0531 keV`。所以未给 covariance 时不能把 quadrature 结果写成该实验的完整分辨率。

复算代码为 [day13_doppler_diagnostics.py](../../system/scripts/day13_doppler_diagnostics.py)，固定 `seed=1313`、每种 covariance `200000` 个 Gaussian draws。有限差分相对误差最大 `2.44×10⁻9`，forward/inverse 误差最大 `1.14×10⁻13 keV`，九种 MC σ 相对一阶传播最大差 `0.171%`。这些检查验证推导与数值实现，没有构成实验数据再分析；大误差、非 Gaussian tails、β/方向多解需要重建完整响应。

### 低速峰宽多解：角覆盖本身不足以分离三个 nuisance

在低 β、独立小误差、固定 `E0` 且角度无关的 detector variance 假设下，

$$V(\theta)=A+B\cos^2\theta+C\sin^2\theta,
\quad A=\sigma_{response}^2,\ B=E_0^2\sigma_\beta^2,\ C=E_0^2\beta^2\sigma_\theta^2.$$

由于 `cos²θ+sin²θ=1`，设计矩阵 `[1,cos²θ,sin²θ]` 只有 rank 2。变换 `(A,B,C)→(A+λ,B−λ,C−λ)` 给出完全相同的 variance 曲线，只要各项仍非负。本例 `(1,4,5.9705014)` 与 `(2,3,4.9705014) keV²` 在七个测试角度的 variance 差为零，却对应不同的 response、σβ 与 σθ。后一组为 `σresponse=1.4142 keV, σβ=0.0017321, σθ=1.82484°`。

这是真实的**推导层反例**，不证明某实验采用这些 nuisance 值。独立 energy-response calibration、particle/tracking geometry 和 β 信息至少要约束其中一项；feeding/angle dependence、非 Gaussian 或精确相对论高阶项会改变模型，不能把 rank-2 结论无条件推广到所有拟合。

### 停止历史 toy 的边界与符号检验

自设无 feeding、固定方向、`p(t)=exp(−t/τ)/τ` 和 `β(t)=β_i exp(−t/t_s)`。则

$$\langle\beta\rangle=\frac{\beta_i}{1+\tau/t_s},\qquad
\operatorname{Var}\beta=\frac{\beta_i^2}{1+2\tau/t_s}-\langle\beta\rangle^2.$$

若一律使用 β_i 校正，一阶 mean residual 为 `E0(⟨β⟩−β_i) cosθ`。取自设 `E0=1000 keV, β_i=0.016, τ=t_s=1.1 ps`，MC exact residual 在35°/90°/145°为 `−6.502/+0.085/+6.615 keV`；90°的一阶 residual 为零但二阶项不为零。Klemme 报告 Au slowing time 约1.1 ps，却没有给出本 toy 的指数 law 或 τ=1.1 ps，不能用这些数值重拟合其寿命或移植到 Mavela。

Klemme Table I 的 `6g+` 从 `1.38(4)` 到 corrected `1.63(6) ps`，中心值增加约18.1%；Table II adopted error 还包含 stopping-power 边界。这是对“能量校正后就不用停止模型”的实验反证。由 adopted 1.63 ps 与通用 `Γ=ℏ/τ` 可得母态自然width约 `4.04×10⁻7 keV`；若6g+→4g+的末态采用4.94ps，idealtransitionLorentzwidth为Γi+Γf≈`5.37×10⁻7 keV`，远小于本例的 keV 响应/运动学宽度。

### 最小可复核数据包与研究判断

优先取得同一已知 line 的 `ring/sector × γ crystal × particle/γ gate` 切片、raw/各 emitter-corrected energy、executed code hash、vertex/γ/particle coordinates、β生成输入和 joint covariance、energy response 与 stopping/feeding metadata。先比较峰心及宽度对角度/距离/门的改变，再试两线模型；variance alone 的多解需由独立 calibration 解除。

本次 self-audit 的 prior belief 是“逐角度峰宽可以帮助辨别速度/方向误差”；revised belief 是“它可否定部分输入，却在上述低速模型中无法独自分解 response/velocity/angle 三项”。触发证据是 Mavela Eq.(4.6)、Klemme Fig.1/finite-stopping 和 rank-2 代数反例。现有 A≈130 集体模式排序不变；没有新的 event/response/covariance，实验 L4 为 `not-ready`。页面仍为 `unreviewed`，推导明确为 Codex self-audit。

#### 独立的多线峰反例

[[herzan-2015-193bi-spectroscopy]] HE15-5 / PDF p.10 Fig.5(a) 明确把154-keV门下标作约323-keV的峰解释为315/320/323/327-keV quadruplet。它是独立于32S和134Nd的直接多线反例，不能把这样的宽峰全部归入β或stopping。具体三层级联、互斥branch和同带近邻line的门控边界见 [[level-scheme-reconstruction]]；没有把该装置分辨率移植到Mavela。

## Recoil vector、共同 vertex 与校正门的响应

### 独立实验对照：改善项与主导 floor

[[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3在同一98Zr1222.9-keV数据中，以直接recoil-vector/target-point重建替代旧focal-plane推回角度，width从8.6(1)降到5.5(1)keV。[[crespi-2013-agata-high-energy-doppler-response]] CR13-3在独立12C15.1MeV实验中，segment→PSA位置精细化仅从122变为119keV；作者认为未逐事件测recoil vector是主要floor。前者支持共同重建，后者反证photon position alone必然达到intrinsic resolution；数值不跨阵列迁移。

### 三维形式与共享位置的协方差

定义无量纲速度向量 `b=v/c`、从发射点到first γ interaction的 `r=rγ−rt`、`n=r/|r|`，精确反演为 `E0=E γ(1−b·n)`。其梯度为

$$\nabla_bE_0=E[\gamma^3b(1-b\cdot n)-\gamma n],\qquad
\nabla_{r_\gamma}E_0=-\frac{E\gamma}{R}[b-(b\cdot n)n],\qquad
\nabla_{r_t}E_0=-\nabla_{r_\gamma}E_0.$$

最后一式只是在b固定时的偏导；若b本身由同一target/ion coordinates重建，必须加入完整chain rule和joint covariance。不能把photon方向与recoil方向各自的“靶点误差”当成两个独立nuisance。

在一维小角直线toy中，两plane距target为L1、L2，D=L2−L1，独立坐标误差为σ1、σ2。则 `xt=(L2 x1−L1 x2)/D`，`α≈(x2−x1)/D`，

$$\operatorname{Cov}(x_t,\alpha)=-\frac{L_2\sigma_1^2+L_1\sigma_2^2}{D^2},\quad
\sigma_\alpha^2=\frac{\sigma_1^2+\sigma_2^2}{D^2},\quad
\sigma_{x_t}^2=\frac{L_2^2\sigma_1^2+L_1^2\sigma_2^2}{D^2}.$$

取source-inspired `L1=174,L2=279mm, σ1=0.073,σ2=0.084mm`（VD16-1/2），在这些自设primitive-independent假设下得到 `σα=1.0599mrad, σxt=0.23875mm, ρ=−0.9730`。与原Table1 scale相容并不证明作者使用该完整covariance。actual plane/reference-wire定义、track fit、scattering/path maps会改变输入。

对自设 `E0=1000keV, β=0.07, photon radiusR=235mm`，γ点固定，只有上述plane noise，`δθrel=−cosθ δxt/R−δα`。full-covariance σ在35°/90°/145°分别为 `0.01343/0.07419/0.07137keV`，若错误去掉cross term则为 `0.05740/0.07419/0.05117keV`。这只隔离recoil/vertex贡献，不是total resolution，γ point/β/response项未加入。primitive finite differences与300000-drawMC复核的最大σ相对差约0.185%。代码见 [day13_doppler_geometry_gates.py](../../system/scripts/day13_doppler_geometry_gates.py)。

### 有限角 bin：用中心角不等于逐事件校正

对自设uniform polar-angle bin `θ=θ0+u, u∈[−h,h]`，用θ0校正各event，得到

$$\frac{E_{corr}}{E_0}=\frac{1-\beta\cos\theta_0}{1-\beta\cos(\theta_0+u)}.$$

小h下mean bias约为

$$\langle E_{corr}-E_0\rangle\simeq\frac{E_0h^2}{6}
\left[-\frac{\beta\cos\theta_0}{1-\beta\cos\theta_0}
+\frac{2\beta^2\sin^2\theta_0}{(1-\beta\cos\theta_0)^2}\right].$$

在E0=1000keV、β=0.07、half-bin10°条件下，35°/90°/145°的exact-quadrature mean bias分别为 `−0.28990/+0.04946/+0.28962keV`，产生σ为 `4.2821/7.0330/3.8274keV`；逐event正确θ反演残差小于1.2×10⁻13keV。uniform polar bin不是uniform solid angle或该实验真实W(θ)，不能用此数替作者做geometry correction。64/128点Gaussian quadrature与zero-β极限通过；small-bin二阶近似及measure选择明确。

### 峰门迁移：能量校正也是计数选择的一部分

对Gaussian corrected line `E−E0~N(Δ,σ²)`、固定±w峰门，接受率为

$$a(\Delta,\sigma)=\Phi\left(\frac{w-\Delta}{\sigma}\right)
-\Phi\left(\frac{-w-\Delta}{\sigma}\right).$$

若efficiency校准ε未包含该selection，angle-count ratio成为 `R_gate=R_true a1/a2`，而非只除以ε。Gaussian只是本题response；tails、neighbour lines、gate background和joint covariance需actual response重新积分。

用此前synthetic σ35/90/145=2.3780/2.6448/2.3952keV、E0=1000keV、βtrue0.07、w3keV且保持σ固定，zeroβbias的a145/a90已不等于1。假定trueN145/N90=1.30，zeroβbias时gate ratio约1.381；校正速度再整体偏高0.002时，centroid residual在145°/90°为1.6924/0.1427keV，gate ratio约1.1945。差异是选择响应，不是新的alignment、multipolarity或collective结构。

固定整数keV门、按各角度±kσ门和response-fit积分应做匹配对照；±kσ在非Gaussian/tails/contamination时也不能保证相同efficiency。Crespi CR13-5/6的FEP/algorithm/multiplicity事实支持记录整条selection链，但没有实测本题gate bias。

### Thematic REFLECT：energy、trajectory 与 selection 不能分开验收

此前Mavela总谱/printed β、Klemme同line stopping双分量已使“校正后窄峰等于速度正确”受到限制。VD16-3进一步给出直接vector/vertex重建的独立改善对照；CR13-3/5说明缺recoil information会形成floor，而tracking selection还会改变FEP效率。共同vertex covariance与fixed-gate数值反例把这条证据链推进到可检验设计：应在primitive coordinates/TOF/path输入层传播covariance，再评估line identity与angle-dependent gate response，而不是只报告一个峰宽。

三篇/多篇引用不自动独立：Mavela/UWC PDF为同一thesis；VAMOS图中两种processing为同一E680数据；Crespi四种processing和PACE4/Geant4是共享inputs。VAMOS、Crespi、Klemme的独立性仅用于方法cross-check，不代表独立复测某A≈130带。自设计算为our-inference，没有改变Q_S、B值或集体模式排名。剩余高信息路线是能损/straggling、发射时间/vertex、first-point错误与gate-covariance，其输入缺口不结束整个Day13学习窗口。

## 发射位置、forward/inverse 约定与 first-interaction 顺序

### Mean flight distance 不能替代发射概率

[[aladili-2009-agata-doppler-simulation]] AA09-4用约16.5/10μm mean flight与约0.5μm target比较，支持主要在靶外发射。其“γ在靶外”若理解为概率1则过强；对source-inspired toy假设constantβ、uniform reaction depth、single exponential proper lifetimeτ，无feeding/energy loss，lab mean flight为 `ℓ=βγcτ`。remainingtargetdistanceu均匀在[0,d]，

$$P_{inside}=1-\frac{\ell}{d}(1-e^{-d/\ell}),\qquad
P_{inside}\simeq\frac{d}{2\ell}\quad(d\ll\ell).$$

用source的τ/β和自设均匀0.5μm深度，52Crτ1.0099ps/β.0548的ℓ16.616μm，Pinside1.4896%；38Arτ.578ps/β.0589的ℓ10.224μm，Pinside2.4059%。若在靶入口产生，则约2.9643%/4.7728%。这是方法反例，actualreaction depth、能损、feeding、backing与gate需要重新积分，不是实际source fraction。sourceEq6.8印1.15×10⁻5m=16.5μm数值冲突仍见AA09-4，未改原件。

在本single prompt exponential假设下，after1mm probability很小；有long feeding或未知delayed component时须用effective emission-time distribution，不能仅引用level τ。代码 [day13_doppler_conventions_decay.py](../../system/scripts/day13_doppler_conventions_decay.py)以analytic、128点quadrature和500000drawMC校验，MC relative differences最大0.593%，thin-target/static limits通过。

### 对keV resolution，约定一致性与近似误差要独立检查

exactforward `E_lab=E0 sqrt(1−β²)/(1−βcosθ)` 与linearforward `E_lab=E0(1+βcosθ)` 各有consistent inverse。不能因为β<0.1就混用。linearforward加exactinverse的ratio为 `(1−β²cos²θ)/sqrt(1−β²)`，二阶bias约 `E0 β²(1/2−cos²θ)`。在E0=1434keV、β.0548、90°时约+2.158keV；sourceAl-AdiliFigs6.17/6.20的centroid约1436keV只与该counterfactual量级相容，缺exec-code不能确定原因。case假设和falsifier见provisional [[doppler-forward-inverse-convention-check]]；一般consistent-roundtrip原则可复用。

source同时给exact和approx式，实际MGT/sortpax未复现，不能将approximation讨论写成已知代码bug。需要保存生成式、calibration、E0输入、lab frame、校正式和每步centroid，再比width。先作zero-nuisance/knownvector roundtrip，再开reaction和positionspread；exact-exact与linear-linear数值max残差≤1.2×10⁻13keV。

### Add-back 与不同 deposit 的方向

同一incoming γ经多个Compton/photoelectric interactions的total deposited energy，在full absorption时属于**同一个incoming photon**。正确Doppler factor使用从emissionvertex到firstinteraction的方向，不能给每个deposit套各自从target到该hit的径向角。若所有deposits共用正确incomingfactor，能量线性相加与先sum后correct等价。

自设E0=1000keV、β.07、firstpoint距target235mm、θfirst60°；沿+x方向Compton散射30°、50mm后photoabsorption。labdeposits为220.425/813.303keV，secondhit径向角65.133°。正确firstpoint校正sum得1000keV；对两个deposit分别用各自径向角得1004.537keV；若highestdeposit当firstpoint则得1005.766keV。两hit符合Comptonenergy/momentum relationship，后续full absorption为明确设定；不是Crespi/Longfellow原event。

这个可运行反例限制“最高能量deposit永远是firstinteraction”，并不否定CrespiCR13-5/LongfellowL26-8在具体energy/multiplicity背景下的方法表现。sequence假设、PSA/clustering/threshold与gate-efficiency需共同验证；low-multiplicity高能与多γcascade不可直接换算法。

## 速度信息的 stage 与独立校准

### Kinetic energy、TOF 与发射时速度

对已知mass M和发射时kinetic energy T，`γ=1+T/(Mc²)`，`β=sqrt(1−γ⁻²)`，

$$\frac{\partial\beta}{\partial T}=\frac{1}{Mc^2\gamma^3\beta}.$$

mass-number近似M=32u，自设T=50/75/120.3MeV时β为0.057848/0.070805/0.089572；若自设σT=0.5MeV，σβ分别0.0002885/0.0002351/0.0001850。Mavela的120.3MeV是**入射**能量，S3deposit是经过scattering、target/foil/dead-layer甚至γemission之后的探测输入；不先重建stage、emitter/particle identity和energy-loss，就不能直接把这两个T代成发射β。原DD-20261013-32S-27/28与ringβ边界保留。这里没有新32Svelocity测量。

对TOF方法 `β=L/(ct)`，

$$\frac{\sigma_\beta^2}{\beta^2}=\frac{\sigma_L^2}{L^2}+\frac{\sigma_t^2}{t^2}-\frac{2\operatorname{Cov}(L,t)}{Lt}.$$

path length由track reconstruction决定，若与timing/vertex共享输入也要保留cross term。仅有VD16-2的TOF130psσ不能给通用σβ：在自设β=.07、σL=1mm、σt=.130ns独立条件下，L105mm/t5.003ns给σβ≈0.001937，L6000mm/t285.912ns给≈0.00003390。这两个path并非作者报告的flight measurement，同一个time-resolution scale在不同flight length下不可直接换成同一个relative speed precision。window/gas/target能损还决定flight速度与emission速度的关系。

### Incident、compound boost 与 residual mean 不能互换

用Klemme KL99-1/17的nominal28Si125MeV+110Pd作mass-number/mass-defect-neglected比较，入射β约0.09755；反应前systemcenter-of-mass boost `p_beam/(E_beam+M_targetc²)` 约0.01987，而paper报meanresidueβ=.016。这个scale区别显示不可把beamβ或理想compoundboost直接当Doppler发射输入；没有reaction-depth energy、Q/excitation、evaporation和gate/response包，差异不能确定哪一项造成，也不说明paperβ错误。多个蒸发粒子的未测momentum应进入residual-vector distribution而非单个全局β。

### 从同一峰优化 β 与 gain/offset 的弱识别性

对自设movingline centroids `y_i=a+g E0 sqrt(1−β²)/(1−βcosθ_i)`，未知offset a、gain g、β。低速一阶式只有intercept `a+gE0` 和slope `gE0β` 两个组合，因此3-column Jacobian rank2；更广anglecoverage本身不能解除该一阶歧义。exact式有高阶curvature可使rank3，却可能非常weak；独立static-source calibration、已知lineenergy与held-out line/ring validation仍有价值。

自设E0=1000keV、βtrue.07、g=1/a=0、35/60/90/120/145°：改β为.0701，并允许g=.99857136、a=1.42957379keV，五角centroid residual最大仅0.002577keV。以参数步长δβ=.001、δg=.001、δa=1keV比较，exact-Jacobian singular values约3.162/1.363/0.002043keV；这是局部scaled sensitivity，不是sourcefittedposterior或普适condition-number。实际independentcalibration可能排除该alternative，所以本反例不指控Crespi的优化无效；CR13-2仍只支持same-spectrum的meanvector，不能替代event-wise速度或独立校准。

[day13_recoil_speed_calibration.py](../../system/scripts/day13_recoil_speed_calibration.py)保留上述单位/假设、kinetic derivative finite-difference、TOF covariance、mass-numberboost与exact/linearcentroidrank检验。reconstruction顺序建议为particle/residueidentity→measuredenergy/TOF/track→loss/path/vertex与time模型→jointemissionvector→γfirstpoint/response→held-outline/gate验证；本次为methoddesign，不是source执行replay。

### 分层验证的最小矩阵

[[akkoyun-2012-agata-instrument-response]] AK12-1/5/6/7提供PSA/staticimaging/selection/replay入口；下表结合此前独立方法来源提出控制设计。

| 层 | 检查与能约束的对象 | 保留的依赖 / 失败条件 | 来源入口 |
|---|---|---|---|
| 静止energy sources | gain/offset/response与rate/threshold，避免把calibration混进βfit。 | calibrationenergy/geometry与movingrun匹配；同一峰拟合不能给独立calibration。 | Mavela calibration与CR13-1/2 |
| 静止Comptonimaging/scans | photonposition/basis/tilt，不需要recoilkinematics。 | sequence/energy/PSA与movingrun可共享；about5mm不是universalσ。 | AK12-1/2/5 |
| 独立particle/TOF/vertextracking | emitter方向、path/speedstage和共同vertex。 | jointcovariance、loss/path/stopping、PID及countercalibration；γ位置升级不能补缺失vector。 | VD16-1/2/3 |
| held-outmovingline/angle | β/coordinate/calibration在未用于优化的样本上是否迁移。 | lineidentity、feeding/stopping、response和globalfit参数共享；same-line最小width不是独立test。 | CR13-2/3与本任务centroidcounterexample |
| tracking/threshold/gate scan | FEPacceptance、tails、centroid/width与P/T变化。 | P/T与count-efficiency分开；neighbour/random/selectioncovariance不可忽略。 | AK12-4/6/7、CR13-5/6 |

这张设计矩阵为跨source synthesis/our-inference，sources提供各自条件证据，不宣称已完成实际runvalidation或几种modality都完全独立。minimumdata包须含original/replayedtraces或events、PSAbasis/code/calibration版本、detector/target coordinates、particle/path/timing输入、line/gate definitions、normalization/response与covariance；本轮尚未取得完整实验packet，继续研究下一项可改变判断的Doppler问题。

### Energy gate 恢复后，angular acceptance 仍在实验室 frame

[[lorentz-boost-correction]]保存源[[longfellow-2026-gretina-energy-ordering-polarization]]L26-2/3/8与本任务finite-acceptance推导：energyinverse与angleaberration/Jacobian不同操作。restisotropicE0=1000keV、β=.07时，energy可逐event精确恢复，但full-azimuth90±5°与145±5°两个labbin的solid-angle-normalizeddensityratio约0.894825，而非1；自设labenergy-dependentε再将它改为0.935502。

这不是测得alignment或sourcebias，realgeometry/response/feeding未提供；不通过更窄rest-energygate“修正”photon密度/angleframe。须分别记录E_lab/E0、eventboostdirection、lab/rest方向、raw和selectedphotons、各角度response与效率。boostvelocity不沿beam时，beamangle不是velocityangle；Mavela的particle角与Doppler夹角不能混写。

## Delayed emission vertex 与 feeding 的条件响应

[[aladili-2009-agata-doppler-simulation]] AA09-1/4要求发射不离target太远，并明说约1mmflight条件未研究；[[klemme-1999-lifetimes-134nd-neighbors]] KL99-2/4/15表明停止/feeding的gate条件会改变寿命分析。这些来源支持检查emissionhistory，但下面的fixed-speed/point-detector模型为our-inference，不是原数据重拟合。

### 已知速度仍会因 vertex 错位产生残差

自设速度沿+z且恒定，nominaltarget到γdetectorfirstpoint为 `r0=R n0`，proper decaytime为t，真实发射点为 `d ez`，其中 `d=βγct`。真实photon方向cosine为

$$c_{true}=\frac{R\cos\theta_0-d}{\sqrt{R^2+d^2-2Rd\cos\theta_0}},\qquad
\frac{E_{corr}^{nominal}}{E_0}=\frac{1-\beta\cos\theta_0}{1-\beta c_{true}}.$$

当d/R小且非共线，小位移leadingresidual为

$$\Delta E\simeq-\frac{E_0\beta d\sin^2\theta_0}{R(1-\beta\cos\theta_0)}.$$

所以b已知也不保证targetvertex正确；sourcevelocityvector与emissionpoint是两项输入。沿运动方向延迟的vertex误差在本geometry下产生同号低能residual，而speedbias的一阶cosθpattern通常可反号，globaloffset则近似共同常数。若anglecoverage/response不足，几种pattern仍可能耦合，不据一张谱选因。

### 条件采样与观察到的谱

对restisotropicphoton、面向nominaltarget的小planardetector，detected-event权重为labangularJacobian×projectedarea/距离平方；不能把unconditionaldecaytime分布直接当detectedtime分布。代码 [day13_doppler_displaced_vertex.py](../../system/scripts/day13_doppler_displaced_vertex.py)分别给unweighted和几何加权moments，以48/96点Laguerrequadrature复核。

自设E0=1000keV、θnominal90°：

| β / R(mm) | proper levelτ(ps) / feederτ(ps) | unconditional meanflight(mm) | detected meanresidual(keV) | detected σ(keV) |
|---|---|---:|---:|---:|
| .07 / 235 | 5 / 0 | .10519 | −.03133 | .03133 |
| .07 / 235 | 50 / 0 | 1.05185 | −.31287 | .31262 |
| .30 / 150 | 2 / 0 | .18856 | −.37655 | .37626 |
| .30 / 150 | 2 / 20 | 2.07417 | −4.08381 | 3.69398 |
| .50 / 150 | 10 / 0 | 1.73085 | −5.63406 | 5.56583 |

这些是明确parameterchoices，不是knownnuclei的τ/feeding测量；忽略stopping、photonrecoil、finitearea、angularalignment、actualcuts和response/covariance。displacement-onlyline倾向非Gaussian单侧tail，所列为σ，不把2.355σ自动当FWHM。quadraturemaxmean差约2.1×10⁻12keV，staticβ0极限通过。

### Feeding 与理想时间门

若同一constant-speednucleus的feeder与level等待时间均为独立exponential proper times，emissiontime为两者和；对τf≠τl，

$$P(t<T)=1-\frac{\tau_f e^{-T/\tau_f}-\tau_l e^{-T/\tau_l}}{\tau_f-\tau_l}.$$

τf=τl时回到Erlang2的 `1−e^(−T/τ)(1+T/τ)`。自设τl2ps/τf20ps、idealproper-time门T10ps，directfraction.993262而feedingfraction.326826；MC为.993422/.327514。actualγ-particletimestamp含emission/flightpath、response、walk与offset，不能把这10ps直接写成某实验gate设置。一个较短levelτ不排除长feeder造成较远vertex；gate选择会同时改变intensity与line-shape样本。

### 最小反证设计

在相同emitter/particlevector/PSAselection下比较具有不同已知prompt/feedinghistory的held-outline，保留raw/nominal/correct-vertexenergy、不同角度以及time/gate切片。globaltargetzoffset也可模拟一部分displacementpattern，须有独立promptvertex/calibration或timehistory；两近邻line还需coincidence/identity控制。缺输入时保留预测/失败条件，不能据本toy测量真实τ或修订absoluteB。

## Detector-origin 宽线、natural width 与 cut 语义

### 宽线不一定属于 target emitter

[[senyigit-2014-agata-neutron-rejection]] SY14-2/3/4提供独立detector-response反例：Ge(n,n′γ)line的high-energy侧约40keVbump可由Ge-recoilvisibledeposit与γenergy相加；27Al2211-keVline报告15keVFWHM的Dopplerbroadenedprofile。γTOF门抑制localGefeatures，却保留部分附近Fe/Al/Ba/Pb或annihilation真γ。因此“通过γtimegate”不等于“属于targetnucleus”，targetresiduevelocitycorrection也不能修复错误originidentity。

检验需匹配core/segment/tracked spectra、neutron-sensitiveTOF/particlelabel、detector/materiallineanchors和response，保留shield/geometry/gates。对正确targetframe进行energygate后，neighbour/background会怎样迁入该gate也必须重放；不能据cleaned全谱就删除反证。

### Natural width 的层级与量纲

对理想Markov Lorentz line，母态energywidth为 `Γi=ℏ/τi`；若末态也有finiteτ，transitionwidth包括 `Γi+Γf`。detectorGaussian、thermal/recoilDoppler、stopping/displacement/feeding和未分辨components是其它kernel，不能直接把所有σ/FWHM相加或用观测总FWHM反推τ。

Klemme的6g+τ1.63ps/4g+τ4.94ps给理想line约5.37×10⁻7keV。以Senyi引用27Almeanτ26.6fs（本轮未独立核验evaluation原文）估parentΓ为2.47×10⁻5keV，远小于reported15keV；这是基于sourceinput的scalecheck，不是独立寿命或Γ测量。source将此宽化解释为短τ使neutron-recoilingAl仍在运动时发射。未经directleveldata核验，不能把该τ转移到12C15.1-MeV或其它resonance；本次IAEALiveChart返回403challengeHTML，未当levelsCSV。

### TOF 分离也有 path/response 条件

sourceSY14-4的γtimeFWHM约9.8–7.7ns是在50cm与指定Eint下获得；source指出23.5cm分离受限。单能/直线toy中，2MeVneutron与γ在235/500mm的TOFseparation约11.249/23.934ns；10MeVneutron为4.632/9.855ns。actualneutronspectrum、detector厚度、walk/jitter/gates未建模，不能将这组kinematicnumbers直接变成rejectefficiency。recoilmass-numberelasticbound在A74/2MeV下约105keV，与source约100keVscale相容；pulse-height-defect约35keV是source引用context，没有从它拟合quenchinglaw。

### 不同分母、OR 与 AND

SY14-5的嵌套选择应用survivalproduct：`r_total=1−(1−r_first)(1−r_conditional)`。1040peak的57%再28%合为69.04%，不是85%；Co1332的9%再18.5%合为25.835%，与Table4rounded25.8%相容。标明rawcore/standardtracked/NRselected分母，jointcovariance缺失时不制造完整errorbar。

sourceSY14-6正文/Table2/Table4的acceptORgood与conclusion反向inequalitiesOR若被当rejectrule，其complement为ANDgood；二者不等价。4booleans的16种assignment中14种mixedcases不同，不是14/16experimentaldatafraction。strictinequality的数学complement还改变边界的<与≤；signedΔθ<40°也不自动变成|Δθ|<40°。需executedmgtpredicate、calibration/thresholddefinition、同一events和publisherversion核验后再reproducecuts，不自行替作者选择。

sourceSY14-7的部分Co列标签正文/表差异也保留；workingnumerics明确来自Table4，不能悄悄以更整齐的文字替换。源SY14-8的tracking/rawFEPcount ratio可超过100%，它不是absoluteprobability。 [day13_neutron_width_selection.py](../../system/scripts/day13_neutron_width_selection.py)复核Γunits、TOFscale、Table4中心比与DeMorgantruth table；它没有重演actualneutronrejection或推荐生产cut。

SY14-9又给出conditionalmonotonicity反例：若全部cuts是同一fixedstandardclusters、同一energy/lineidentity、相同peakcount/normalization上的post-filters，acceptORgood包含E1>30，而E1>30包含E1>45，因此combinedloss不得大于E1>45-onlyloss。Table2的Co1332两行中心值为18.5%与3.9%，不能由这些假设下的literalOR重现。这个结论不把差14.6percentagepoints当误差显著性，也不证明actualmgtwrong；retracking、clusterreassembly、峰拟合/背景处理或不同stagedefinition会改变前提。真正可复核的cutcontract必须记录executionstage与观测计数对象，不能只留threshold列表。

## Photon recoil：level gap、母核 frame 与子核 frame

### 评价宽度与 gamma branching 的不同分母

[[tunl-2017-12c-level-widths]] T12C-1/2核验了官方在线12C表：15.110MeV1+level的totalΓ=43.6(1.0)eV，而groundγpartial为38.5(.8)eV、totalγ为41.8(1.1)eV。centralmeanlife从totalΓ得15.10as；用groundpartial代total会增大约13.25%，得到的是partial-channel等效time，不是levelτ。

T12C-3的中心商Γγ0/Γγ=.92105、Γγ0/Γtotal=.88303，后者含α通道；Table14footnotee的92%属于γ-decaybranchcontext。CrespiCR13-1的92%linecontext与此denominator相容，但没有据此诊断其实际yieldnormalization。多项widths是shared/deduced，Table14gamma-partialcentral-sum与listedtotalγ差.94eV不自动是erratum（T12C-5），也不制造independentratioerrors。

TotalnaturalΓcm=.0436keV远小于CR13-3的119keVFWHM；它限制naturalwidth为主因，却不能独自分解kinematic/position/response。TUNL表是online2017KE05与2020revisioncompanion的有版本记录，不默认为未经修订的2017originalpaper，也不是Crespi的第二次实验。

### Free nucleus 的 two-body photon energy

对自由母核restmassMi、子核Mf和单photon，energy/momentum守恒给

$$E_\gamma^{(i)}=\frac{(M_ic^2)^2-(M_fc^2)^2}{2M_ic^2}
=\Delta\left(1-\frac{\Delta}{2M_ic^2}\right),\quad
\Delta=(M_i-M_f)c^2.$$

所以levelgapΔ不完全等于emitting-parent-restframe的photonenergy；差为daughterrecoilkineticenergy。mass-numberM≈Au、groundfinal的自设近似例子：

| A / gap | Parent-rest photon | gap−photon recoil energy |
|---|---:|---:|
| 12 / 15.110MeV | 15.099801MeV | 10.198843keV |
| 12 / 4.43982MeV | 4.438939MeV | .881388keV |
| 32 / 2.23057MeV | 2.230487MeV | .083452keV |
| 52 / 1.434MeV | 1.433979MeV | .0212keV |
| 130 / 1MeV | .999996MeV | .004129keV |

前两gap参考T12C-1/4，32/52为此前source-inspiredscales、130为自设比较；这些不是重新测量γenergy。精确值需要nuclear/atomicmass区别、finalexcitation、电子/介质/lattice条件与sourceE0定义。自由movingemittertoy不涵盖Mössbauer/lattice-recoilfree情形；Crespi仅写15.1MeV的roundedline标签，不能据表推断其精确sortinginput错了。

### Post-photon daughter velocity 不是 emitting parent velocity

对已测photonfour-vectork和**紧接这条γ后的**daughterfour-vectorPf，Pi=Pf+k；同particleterminalstate若随后还有未测γ/particle，则还需要它们的four-momenta或distribution。直接以terminalresidueTOF/track作为某intermediateparentvelocity，需评估γrecoil与missingemissions，不把stage差忽略为同一b。

在理想free two-body情形中，用正确parentvelocity反演得Eγ(i)；若用exactpost-daughtervelocity，会得到

$$E_\gamma^{(f)}=E_\gamma^{(i)}\frac{M_i}{M_f},$$

这是另一个合法restframe的energy，不能拿它作母核E0。上述A12/15.110toy的difference为20.411473keV；此bias在correctfour-vector计算中对任意labboost/γangle保持不变，不能用globalwrongβ的cosθ反号诊断代替。A32/2.23057为.166911keV，A130/1MeV为.008258keV，说明是否可忽略需结合energy/precisionbudget，不能只按massregion断言。

[day13_photon_recoil_width.py](../../system/scripts/day13_photon_recoil_width.py)对β0/.016/.07/.3/.5和多rest-emissionangles检查parent/daughter/photonfour-momentum、daughtermassshell和两种frameinversion；maxfour-momentumresidual1.46×10⁻11MeV，inverseerror≤7.2×10⁻15MeV。无实际particle/γevent重建或新Β值。

## Lorentz natural line 与 Gaussian response 的卷积

[[tunl-2017-12c-level-widths]] T12C-1/4 给出不同能级的 total natural Γ，[[crespi-2013-agata-high-energy-doppler-response]] CR13-3 给出观测峰宽。两者的物理对象不同；下面只检验线型数学，不拟合这些实验。

在孤立、指数衰变、稳定末态的近似下，母态振幅按 `exp(−t/2τ)` 衰减，其能量线型为 Lorentz：

$$L(x;\Gamma)=\frac{\Gamma/2}{\pi[x^2+(\Gamma/2)^2]},\qquad
G(x;\sigma)=\frac{e^{-x^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma},\qquad
V(x)=\int L(y)G(x-y)\,dy.$$

`x=E−E0`，Γ 是 Lorentz 的 FWHM；Gaussian 的 FWHM 则为 `2√(2ln2)σ`。`V` 是归一化 Voigt。Gaussian 核之间可相加 variance，Lorentz 核之间可相加 Γ；**Gaussian 与 Lorentz 的 FWHM 不能直接平方和**。先前的 `JΣJᵀ` 传播适用于已声明、有有限二阶矩的小扰动，不将 natural Γ 填入它的 σ 栏。

理想、无限支持的 Lorentz/Cauchy 核没有通常意义下的平均值与有限 variance；对称截断的中心或 principal value 不等于存在统计均值。真实发射过程有能量阈值、能量依赖矩阵元和有限观察窗，必要时应回到这些物理条件，不能用理想 Lorentz 的发散尾部给真实实验凭空添加误差。

### 定量反例与 finite energy gate

[day13_voigt_gate_response.py](../../system/scripts/day13_voigt_gate_response.py) 用直接卷积积分独立核验 SciPy Voigt，检查全域归一化与 Γ=0/σ=0 极限。全部宽度以 keV 输入，以下均为声明参数的例题：

| Lorentz Γ | Gaussian FWHM | Voigt FWHM | 直接平方和的错误值 | 参数身份 |
|---:|---:|---:|---:|---|
| .0436 | 119 | 119.023221 | 119.000008 | T12C-1 的 Γ 尺度与 CR13-3 的观测宽度尺度；119 在此**仅充当 Gaussian comparator**，不是已测响应分解。 |
| 20 | 20 | 32.751907 | 28.284271 | 自设同尺度反例，错误值低13.64%。 |
| 46 | 5 | 46.579592 | 46.270941 | T12C-4 的 broad-width 尺度与自设 Gaussian；不声称该态存在本例的已测 γ profile。 |

对20/20例题，设真实 Voigt FWHM 为 W，中心门 `|x|<W` 接受 .798321；具有相同 W 的纯 Gaussian 接受 .981468。门扩至 `|x|<2W` 时两者为 .901916/.999998。**相同 FWHM 不能保证相同 gate fraction**，只报拟合峰宽不足以校正门内强度、角分布或弱支路上限。

Γ=.0436、Gaussian comparator119 的 Voigt只增加约.0232keV FWHM，支持这个天然宽度尺度不能主导119keV峰；它没有识别实际 velocity/PSA/response 分量。直接卷积与 Voigt 最大差 `3.47×10⁻18 keV⁻1`，归一化误差 `<5×10⁻16`。这验证数学核与数值精度，不验证某个实验的实际线型选择。

### 反证和必要伴随输入

若改进独立 particle vector 后 core/segment/PSA 的宽化同向收缩，kinematic 解释获得支持；若 tail 随 tracking/threshold 改变，需保留 detector/selection 解释。Natural Γ 应来自适用的态/通道和版本记录；broad group 的 overlap/interference（T12C-6）还可能超出 Voigt 近似。实际 gate 强度至少需要完整线型、邻峰/背景、frame、效率、门的分母与共享事件 covariance；本例没有提供这些实验输入。

## Missing momentum 与发射前后的速度阶段

[[aladili-2009-agata-doppler-simulation]] AA09-2/9 的 reaction model 区分复合核与蒸发后的残核，Fig.6.12 的近各向同性是 CM per-solid-angle 语境；lab 角谱不同。[[crespi-2013-agata-high-energy-doppler-response]] CR13-2/3 的 mean vector 缺少事件测量，[[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3/5 则实际使用粒子 vector。它们支持检查输入阶段，但不能互相替代反应、响应或 data packet。

### 蒸发发生在目标 γ 之前

若所有粒子蒸发已在目标γ之前完成，particle recoil会使 **residual emitter vector** 分散；这解释为何 compound/beam 的平均 boost不能逐事件替代它。若已独立、准确地重建这个 residual emitter vector，此前蒸发的不确定度便不应再次叠加为同一项未知误差。

自由两体例题以CM静止的compound发射一颗固定 Tn=2MeV 的neutron，残核随后发射1-MeV gap对应的γ。设 neutron momentum为 p、残核激发质量为 Mr，γ在残核rest系各向同性，则误用compound frame后有

$$E_{\gamma,CN}=E_{\gamma,r}\gamma_r(1+\beta_r\cos\vartheta),\quad
\sigma_{E,CN}=\frac{E_{\gamma,r}p}{\sqrt{3}M_rc},$$

其中 `Mr c²` 用 MeV、`pc` 用 MeV 时，右式单位为 MeV。均值为 `γr Eγ,r`，理想线型为两端点之间的均匀 box，不能将其σ不加说明地当Gaussian FWHM。

| 自设 ground mass≈Au | 错用 CN frame 的σ (keV) | box half-range (keV) | mean bias (keV) |
|---:|---:|---:|---:|
| 12 | 3.167701 | 5.486620 | .015052 |
| 52 | .731083 | 1.266274 | .000802 |
| 130 | .292439 | .506519 | .000128 |

以上是固定能量、mass-number近似的例题，不是AA09/Crespi/Klemme的反应重算。对固定残核质量、独立各向同性的n颗粒子，leading momentum covariance为 `Σp=(Σj pj²/3)I`，同能量的σ按√n增加；真实顺序质量/能量、角各向异性、channel/particle gate及stopping都会改变这一近似。

[day13_missing_momentum_stages.py](../../system/scripts/day13_missing_momentum_stages.py)对静止与多lab boost核验四动量、mass shell和母系反演。正确使用γ发射前残核vector时恢复唯一Eγ,r；错误CN correction保留box分散。MC σ与解析值最大相对差.162%，四动量/mass-shell尺度残差 `<7×10⁻11MeV`，inverse误差 `<4×10⁻16MeV`。

### 若目标 γ 之后还有未观测粒子

这需要单独的阶段判断，**本例没有声称上述实验的低位束缚态γ之后还会蒸发neutron**。若某高激发路径确有晚粒子、且中间能级未知，已知terminal residue与一条photon并不唯一给出earlier parent vector。

令已测总四动量 `C=Pt+k`、未测neutron为q、初始母核质量Mi已知，则 `Pi=C+q`、`Pi²=Mi²` 只固定C-rest系中的neutron能量，仍留方向自由度。代码给相同terminal four-vector/1-MeV observed photon、相同Mi的三种方向解；earlier-parent rest photon energy分别为1000.504691、1000.000127、999.495564keV。中间核质量也随之变化，明确是**未知中间态**的条件反例。

若指定了同一个已知中间态，其invariant约束会减少这组自由度；完整测得后续particles/γ则可按四动量求和恢复parent。target loss、spectrometer trajectory、charge state和各阶段的event covariance还需实测/校准packet。应先画清 `compound → post-evaporation emitter → post-target-γ daughter → terminal residue`，确认存在的emissions与material crossings，再传播误差；不能把一个平均boost、一次TOF或末端PID等同于所有阶段速度。

## 两距离 position 标定：消去哪一项，留下哪些假设

[[soderstrom-2008-agata-position-design]] SD08-3/5/6 提出改变detector distance以减少reaction Monte Carlo依赖，并明确讨论近距离angle coverage/curved face造成的偏差。原p7 Eq.(4.4)印刷用未平方的W与1/d差；本页保留这个locator，不把下式写成作者已核准的更正或生产代码。

### 声明模型下的平方差

设同一line、同一β/angle及可迁移response的 **Gaussian** FWHM满足

$$W(R)^2=B^2+\frac{k^2p^2}{R^2},\qquad
p^2=\frac{W_c^2-W_f^2}{k^2(R_c^{-2}-R_f^{-2})}.$$

`B` 为确实相同的其它Gaussian宽化（keV），`p` 为一个相关方向的projected position FWHM（mm），`R` 是source到first-IP的有效距离（mm），`k` 为angular sensitivity（keV/rad）；在正确90°、E0固定的简化例中 `k=E0β`。点geometry只在small-angle和已声明p分布条件下使用，不将front-face距离无条件代入。此式是本任务推导，不能推广为任意尾部/Voigt/多线的FWHM平方和。

两不同R使 `[1,1/R²]` 两参数设计矩阵rank2，可同时估B²与k²p²；相同geometry内多测一个总宽度没有这个杠杆。它改变了此前固定geometry的width-only多解条件，但只在B/k/p确实可迁移时成立。两点也总能拟合这两个参数，不能仅以零残差证明模型正确。

### 定量误差与失败检查

[day13_two_distance_resolution.py](../../system/scripts/day13_two_distance_resolution.py)自设E0=1000keV、β=.07、k=70、p=5mm、B=3keV、R150/235mm，精确反演得5mm。两宽度measurement σ各.02keV时，ρ从−.8/0/+.8变动，p的linear σ分别.21029/.15702/.07133mm；MC最大relative差<.4%。共同误差在差量中可部分抵消，独立计算两份error不一定正确。

两个条件反例说明需要哪些伴随记录：

- 自设front distances40/140mm、两个first-IP均在其后30mm，若错用front distances，真实5mm会估成2.71694mm；用真实70/170mm距离恢复5mm。这不是source测得30mm平均深度。
- 近distance的B由3.0变为3.3keV，而far/held-out200mm仍为3.0，two-point fit给p=6.29647mm；其200mm预测FWHM3.54360keV与实际toy3.47311keV不同。第三geometry提供失败检查，但仍共享同一detector/calibration，不算另一个独立实验。

另自设R220/235mm、宽度σ.05keV，Gaussian measurement模拟约25.5%的 `p²` 估计为负；这是小几何杠杆与误差下的边界问题。不能静默clamp后把p=0写成已测分辨率，应报告原估计/likelihood、physical constraint和上限/区间的定义。

实际最小packet包括每geometry的target/first-IP/tilt、能量/角度接受率、particle vector及covariance、PSA/algorithm/version、同一line/peakfit/background定义、宽度间covariance和held-out geometry/energy。它们未取得时，两距离只能作为可检验设计。原SD08与AA09有共享模型谱系；2023综述 [[crespi-2023-agata-tracking-performance]] C23-4/5/8/14又说明PSA/FOM/static image的共同假设，不增加独立acquisition数。

## 门选择后的 likelihood 与未参与优化的验证

[[crespi-2023-agata-tracking-performance]] C23-4/5/12 提供FOM/单hit选择影响响应与效率的source语境；[[senyigit-2014-agata-neutron-rejection]] SY14-5/6/8/9 表明执行stage、threshold与计数分母还必须明确。下面的likelihood是本任务通用统计推导，未宣称来源已使用该式或某实验原拟合有偏。

### 条件分布必须归一化

若原observed energy残差分布为 `f(x|η)`，固定门/选择为 `S(x)`，则选中样本的density是

$$f_S(x|\eta)=\frac{S(x)f(x|\eta)}{Z(\eta)},\qquad
Z(\eta)=\int S(x)f(x|\eta)\,dx.$$

`η`可含centroid/width/β/calibration/feeding参数；若Z随它们变化，不能从likelihood中删除。对已知fixed [a,b] Gaussian门，`Z=Φ((b−μ)/σ)−Φ((a−μ)/σ)`。Naive普通Gaussian fit拟合的其实是被截断的样本moments，不能把较小σ等同更好的母分布resolution。

[day13_gated_likelihood.py](../../system/scripts/day13_gated_likelihood.py)自设母Gaussian μ1.2keV、σ2keV、固定门[−2,+2]keV，模拟100万条：

| 拟合与可用输入 | μ (keV) | σ (keV) | 解释 |
|---|---:|---:|---|
| 忽略门的普通Gaussian | .342411 | 1.050582 | 被截断样本的mean/σ；不是原resolution。 |
| 含Z的conditional likelihood | 1.203206 | 2.005365 | 在正确Gaussian/selection模型下恢复母参数。 |
| conditional加已知总trials的binomial selection likelihood | 1.195847 | 1.998986 | 总trials在toy中已知，额外接受率信息参与约束。 |

归一化误差 `<5×10⁻16`，门内mean/接受率MC、无门Gaussian极限和参数回收通过。Near-Z=1用Gaussian outside-tail的log概率计算，避免把舍入为1的Z当作无外侧events的证据。真实母谱未必Gaussian，还有背景/邻线、response、time/particle/FOM多变量选择；toy回收不能成为实际velocity测量。

### 强度与 shape 的不同信息

若总入射yield为N0、detector efficiency为ε，expected selected count为 `N0 ε Z(η)`。只有归一化门内shape不会提供N0；只给selected count又不能同时辨识N0/ε/Z。已知总trials的binomial项在toy中提供信息，真实run若无beam/source normalization与response不能假造这个输入。

实际extended likelihood应声明expected rate、门内shape与背景/mixture，再传播shared calibration/acceptance covariance。若门在拟合中随β/峰心移动，需重新定义selection和原event sample；本例只验证预先固定的门，不能直接移植为移动门的normalizer。

### 哪些 held-out 检查有额外约束

| 检查 | 能排除的失败 | 仍共享的边界 |
|---|---|---|
| 同source事件training/test split | 有限样本调参过拟合、随机波动 | 同basis/coordinate/gain/line identity的systematic会一起通过。 |
| 不参与β/FOM优化的已知line，跨energy/angle | 特定line的centroid/width拟合无法迁移 | feeding/velocity history不同可造成合法差异，需matched或independently known控制。 |
| 第三geometry或static image/particle vector | 在common-baseline或beam nuisance上增加失败检查 | 同PSA/code/calibration仍可共享，且geometry接受率需重算。 |
| 固定gate/FOM/threshold scan | counts/centroid/tails对selection的依赖 | 同一event重放高度相关，不能当多次实验提高显著性。 |

[[crespi-2013-agata-high-energy-doppler-response]] CR13-2用同谱优化mean vector不等同未参与优化的独立速度验证；[[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3的particle信息是互补约束而不是同谱窄化代用品。最小packet还需unselected/staged counts、gate定义、response/ε、rate归一化、line身份与joint covariance。缺输入时保存可证伪预测与readiness，不把多个toy的成功叠加成实验L4。

### GANIL 的直接 Doppler-position 对照

[[ljungvall-2020-agata-ganil-performance]] LG20-7/8/9/14 把98Zr line的width映射到六个detector的position response：VAMOS给particle vector，方向在该分析中近似精确，speed contribution另从mass-resolution输入添加；Geant4保留target energy loss/straggling和VAMOS acceptance。其IP law `∆ri=1.9+4.4√(100keV/Ei) mm FWHM` 是energy-dependent **one-dimensional FWHM**，不是角σ或每个point同样的5.1mm。实验/模拟peak宽均作Gaussian fits，然后用scale/interpolation比较，不能假定此近似适用于未知tail/overlap/feeding的其它line。

该source给平均5.1mm、六detector3.7–6.1mm与平均估计误差1mm；作者明确提醒sample spread也可来自统计误差。它是具有独立vector约束的实际method benchmark，不是原width-only rank2模型被全局否定，也不能取代本run缺失的production/code/event/covariance。

LG20-10/12又直接证明tracking的联合接受率影响γγ normalization。只有能量峰恢复，还不能从source效率直接获得实际beam angular/coincidence效率；[[tracking-array]]保存mix-stage与common-axis反例。LG20与C23-7/12是primary/review依赖谱系，VD16同设施98Zr case没有runmanifest时也不默认独立复测。
