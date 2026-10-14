---
type: method
title: "Event-by-Event Doppler Correction"
aliases: [gamma-ray Doppler correction, Doppler energy correction]
created: 2026-07-13
updated: 2026-10-14
status: active
review_status: unreviewed
method_type: in-beam-gamma-spectroscopy
tags: [doppler-correction, in-beam, gamma-ray-tracking]
---

# Doppler Correction

## Purpose

In an in-beam experiment, the detected gamma-ray energy is corrected event by event using the residue velocity and the measured emission direction. Longfellow 2026 gives `E_gamma=E_gamma,lab (1-beta cos(theta_lab))/sqrt(1-beta^2)`.

跨source的简明观测/输入/失败条件入口见 [[doppler-velocity-validation-contract]]；本页保留详细公式、quantitative exercises与各source适用条件。

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

对理想Markov Lorentz level，母态energywidth为 `Γi=ℏ/τi`；忽略photon recoil、且两level为独立narrow Lorentz mass profiles时，transition-gap width为 `Γi+Γf`。精确photon-energy的局部width映射另见后面的recoil derivative条件。detectorGaussian、thermal/recoilDoppler、stopping/displacement/feeding和未分辨components是其它kernel，不能直接把所有σ/FWHM相加或用观测总FWHM反推τ。

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

## 已知 speed 不等于唯一的 velocity vector

[[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-1/3、[[crespi-2023-agata-tracking-performance]] C23-8/9 说明energy inverse需要emitter vector与photon方向。以下是本任务明确的common-velocity calibration fixture，不据此声称CR13或其它实测fit存在这种歧义。

设速度大小β已知、方向u未知，known-rest-photon E0、measured lab photon方向ni/energyEi满足

$$\mathbf n_i\cdot\mathbf u=\frac{1-E_0/(\gamma E_i)}{\beta},\qquad |\mathbf u|=1.$$

一条photon只给cone/projection。两个nonparallel ni给一个plane内的particular solution u∥；剩余为 `u=u∥±√(1−|u∥|²) h`，h为两photon方向张成plane的normal。因此可有两个mirror directions；若`|u∥|>1`，exact noiseless模型无解，真实误差需要likelihood处理，不裁剪成确定方向。

[day13_vector_identifiability.py](../../system/scripts/day13_vector_identifiability.py)自设β=.07、E0=1000keV，n1=(0,0,−1)、n2=(.8,0,−.6)。`u=(.03,±.02,.999349789)`两解都近beam-forward方向，lab energies同为932.326566/958.909930keV。各branch的two-tangent Jacobian都是rank2，**full local rank仍不排除global mirror ambiguity**；101个共平面方向的energy最大差仅2.3×10⁻13keV。新增n3=(0,1,0)使两解预测相差2.793137keV，第三noncoplanar constraint在该模型中恢复原方向；实际能否判别还依centroid/geometry/covariance精度。

这个fixture使用不同calibration emitters共享constant vector，不是忽略有限质量γ反冲后仍宣称精确的真实cascade。若同event的γ有不同emission/stopping/feeding stages，或knownE0实际只是rounded levelgap，方程前提需另核。独立particle tracking、完整目标/first-IP geometry或额外kinematic constraints可以排除分支；单速TOF、共平面peak或局部拟合误差条本身不能保证全局唯一性。β=0极限能量与方向无关，此时不要用除β的projection式。

## Cartesian 输入的完整 Jacobian：避免重复计入角误差

[[crespi-2023-agata-tracking-performance]] C23-8、[[ljungvall-2020-agata-ganil-performance]] LG20-7/8/14 和VD16-1/2提供vector/position误差的source语境。若θ已经从velocity与位置计算，选择raw inputs `x=(E_lab,bx,by,bz,vx,vy,vz,gx,gy,gz)`，v为emission vertex、g为first-IP、b为v/c无量纲速度，所有vector在同一frame，位置同用mm。令 `r=g−v, R=|r|, n=r/R`，则

$$f=E\gamma(1-\mathbf b\cdot\mathbf n),\qquad
J_E=\gamma(1-\mathbf b\cdot\mathbf n),$$
$$\nabla_{\mathbf b}f=E\left[\gamma^3\mathbf b(1-\mathbf b\cdot\mathbf n)-\gamma\mathbf n\right],\qquad
\nabla_{\mathbf r}f=-\frac{E\gamma}{R}\left[\mathbf b-(\mathbf b\cdot\mathbf n)\mathbf n\right],$$
$$\nabla_{\mathbf g}f=\nabla_{\mathbf r}f,\quad
\nabla_{\mathbf v}f=-\nabla_{\mathbf r}f,\quad
\sigma_f^2=J\Sigma_xJ^{\mathsf T}.$$

位置derivative单位keV/mm，速度derivative单位keV；r方向的radial位移一阶不改photon direction。若用这个Σx已包含b/point方向误差，不再额外叠加同一θ误差；若改用scalar(E,β,θ) coordinates，则应转换同一covariance，不能把derived θ误差当独立的新输入。

[day13_vector_position_jacobian.py](../../system/scripts/day13_vector_position_jacobian.py)自设10×10Σ、R235mm、θ35°，验证finite differences、scalar longitudinal derivative、radial零项、β=0 regular极限以及MC。max有限差分绝对误差1.24×10⁻6（按各参数单位），MC σ相对差最大.0954%。β=.07例的σ1.897904keV仅属于这个Σ，不是实际source resolution。

共同coordinate-origin平移v/g、或共同frame rotation同时旋转b/v/g，都保持f。这是coordinate一致性；**physical target单独移动而detector固定并不取消**。自设β=.07下physical1mm transverse target shift给约−.14846keV，而把同一10mm坐标origin uncertainty误当v/g各自独立，会凭空增加6.56997keV²variance。真实target、track和detectoralignment的共享误差是否抵消必须由其生成/测量定义决定，不能将frame invariance当作免除实际geometry calibration的理由。

## Energy-dependent IP response：平均 variance 与混合谱

[[ljungvall-2020-agata-ganil-performance]] LG20-8/14使用 `p(Ei)=1.9+4.4√(100keV/Ei) mm FWHM` 的one-dimensional position模板；Ei是first interaction的deposit energy，不能换成full γ energy。[[crespi-2023-agata-tracking-performance]] C23-4/5/15也区分nominal simulation smear、algorithm调参和真正event uncertainty。以下是用该公式作**声明模板**的两组能量例题，不核准其测量范围之外的外推，也不重拟合GANIL数据。

设known vector、固定geometry、小角度Gaussian position error、Gaussian intrinsic comparator，conditional σE(Ei)才有定义。混合样本的variance为

$$\mathrm{Var}(E)=\sigma_B^2+\frac{k^2}{R^2[2\sqrt{2\ln2}]^2}\langle p(E_i)^2\rangle,$$

当各组mean相同时成立。用 `⟨p⟩²` 替换 `⟨p²⟩` 会丢掉 `Var(p)`；不同mean时还要加between-group variance。总体profile是Gaussian mixture，通常不再是单Gaussian，不能把总σ乘2.355当成实际half-height FWHM。

[day13_heterogeneous_response.py](../../system/scripts/day13_heterogeneous_response.py)自设E0=1000keV、β=.3、θ90°、R150mm、correctedGaussian comparator2.6keV；first-IP deposits50/1000keV的weights为.2/.8，模板p为8.12254/3.29140mm。结果：

| 量 | 值 (keV) | 定义 |
|---|---:|---|
| mixture half-height FWHM | 7.484993 | 直接由归一化mixture的half-height求根。 |
| same-variance Gaussian FWHM | 9.706038 | mixtureσ乘Gaussian factor，仅是等variance comparator。 |
| 先平均p再平方所得Gaussian宽度 | 8.903350 | 低估variance的代入，不是mixture实际FWHM。 |

以实际half-height W为中心门half-width，mixture接受.932989，而相同W的纯Gaussian接受.981468。就算所有conditional kernels都Gaussian，平均响应仍不足以给完整gate fraction。

当true σi已知、各组确有同mean，inverse-variance centroid精度可改善；本例每trial1000events、20000trials的ordinary/weighted理论σ为.130342/.103888keV，MC为.129925/.104137。若某组存在offset或σi估错，这个共享mean/knownvariance前提便失败，权重本身不能验证calibration。C23-15的实际tracking改进仍是作者未证实建议，不因toycentroid成功升格。

积分variance/归一化误差 `<3×10⁻16`，equal-width Gaussian极限与conditionalcentroid MC检查通过。未含actual first-hit energy distribution、depth/orientation dependence、PSA–energy/velocity covariance、natural Lorentz tails或真实selection；实际widthfit还需窗口/background/line identity，不能据一个reportedGaussianwidth唯一反推所有position response。

## 到达时间的 retardation 与 Doppler factor

[[aladili-2009-agata-doppler-simulation]] AA09-4的flight、[[senyigit-2014-agata-neutron-rejection]] SY14-4的TOF/path条件，以及前面的delayed-vertex例题说明必须区分proper等待、lab emission与detector timestamp。下面从恒速geometry推导时间关系，非source实际计时分析或寿命测量。

发射核以恒定β沿+z，proper等待t、lab emission time γt；nominal source到固定first-IP向量为 `R0 n0`，真实发射位置为 `d=βγct`。令 `R(t)=|R0 n0−d ez|`，到达时间减去已知prompt flight reference `R0/c` 后为

$$a(t)=\gamma t+\frac{R(t)-R_0}{c},\qquad
\frac{da}{dt}=\gamma[1-\beta\cos\theta_{true}(t)]\equiv D(t).$$

所以 `E_lab(t) [da/dt]=E0`。这个factor同时联系energy与proper-to-arrival时间；lab emission time仍是γt，两者是不同时间对象。对small displacement/far detector，D近似常数，proper exponential τ对应arrival尺度约Dτ，而不是只乘γ。

[day13_retarded_arrival_time.py](../../system/scripts/day13_retarded_arrival_time.py)独立用photon Lorentz boost与数值arrival derivative核验上述乘积，并包括isotropic-rest angular bunching、planar projected area/distance²的detected-event权重。自设β=.3、properτ10ps、R150mm、理想arrival gate10ps：

| nominal angle | far arrival mean Dτ (ps) | finite geometry detected mean (ps) | detected ideal gate fraction | 再加自设1000ps Gaussian jitter后的fraction |
|---:|---:|---:|---:|---:|
| 35° | 7.90673 | 7.98228 | .714402 | .500805 |
| 90° | 10.48285 | 10.46077 | .615892 | .499816 |
| 145° | 13.05896 | 12.92016 | .538940 | .498835 |

lab emission mean为10.48285ps，finite detector的conditioned mean还受geometry/acceptance改变。1000ps jitter是自设counterexample；它展示ideal ps门预测不能脱离response，不把它当SY14实测time resolution或任何已提取τ。

48/96点quadrature最大差6.1×10⁻12，boosted photon×numeric time-slope的energy误差<6.4×10⁻8keV，conditionalgate/moments MC最大差.0755%；static与far-detector极限通过。实际start reference、flightpath、walk/jitter/offset、particle/γtime gates、stopping与feeding都须入packet。Energy校正、逐eventtimestamp和arrival gate选择不能互相代替。

## 一阶速度敏感度为零时的二阶边界

[[crespi-2023-agata-tracking-performance]] C23-8 Eq.(7)给 `Jβ=E_lab γ³(β−cosθ)`。在fixed lab direction、`cosθ=β0` 时一阶速度项为零；这只限定局部first-order propagation。

若保持lab photon energy不变，而用于校正的β有小估计误差δβ，则在该点

$$E_{corr}-E_0\simeq\tfrac12 E_0\gamma_0^4(\delta\beta)^2.$$

对声明的Gaussian longitudinal estimator error σβ，leading mean为 `.5E0γ0⁴σβ²`、σ为 `E0γ0⁴σβ²/√2`。若另一fixture改变实际发射β、由它生成lab energies，再用固定β0校正，leading residual符号相反。两种fixture的energy/velocity covariance与数据对象不同，不能作为同一实验的两份独立error相加。

[day13_zero_sensitivity_curvature.py](../../system/scripts/day13_zero_sensitivity_curvature.py)自设三组参数，固定lab direction且不含其它response/selection：

| E0 (keV) / β0 / σβ | Jβ=0的lab angle | leading mean magnitude (keV) | leading σ (keV) |
|---|---:|---:|---:|
| 1000 / .07 / .002 | 85.986° | .002020 | .002856 |
| 1000 / .20 / .020 | 78.463° | .217014 | .306904 |
| 15000 / .50 / .020 | 60° | 5.333333 | 7.542472 |

Finite-difference二阶导数最大relative差2.5×10⁻8，exactMCσ与leading结果最大差.699%；zero-noise与opposite residual signs检查通过。δβ² profile非Gaussian，不能把σ乘2.355当真实FWHM。第一行尺度很小、最后一行为自设高速度/大不确定度例题，不给任何source peak tail归因；actualintrinsic/angle/position/history/selection仍须完整预算。选择一阶零点并不完成整体resolution优化。

## Narrow level width 到 photon width 的反冲映射

[[tunl-2017-12c-level-widths]] T12C-1/2 的Γcm是evaluated level width。自由two-body公式用mass-energy `mi=Mi c², mf=Mf c²` 给photon `e=(mi²−mf²)/(2mi)`，其local slopes为

$$\frac{\partial e}{\partial m_i}=\tfrac12\left(1+\frac{m_f^2}{m_i^2}\right),\qquad
\frac{\partial e}{\partial m_f}=-\frac{m_f}{m_i}.$$

仅在**两个独立、窄Lorentz mass-profile与一阶energy mapping**的声明模型下，photon Lorentz FWHM近似为 `Γph≈.5(1+q²)Γi+qΓf`，q=mf/mi；这是Cauchy widths相加，不是Gaussian variance公式。heavy/recoil-neglected极限q→1才回到Γi+Γf。Broad/interfering levels、matrix-element/phase-space变化、final-state选择或mass–velocity covariance需完整模型，不以这个局部式替代。

`day13_photon_recoil_width.py`新增两mass derivatives的finite-difference核验，最大absolute差3.9×10⁻9。沿A12/gap15.110MeV的既有mass-number例题，用Γi43.6eV、稳定ground Γf0，局部映射Γph≈43.541182eV，差约−.058818eV，小于源quoted1eV的total-width uncertainty。它没有替换评价表、没有测新的photon line width；先前Voigt例题使用.0436keV只是natural-width尺度comparision，已注明不是实际response分解。原mi/mf mass-number/atomic-versus-nuclear边界继续保留。

## Light-ejectile 两体反冲与 conditional rigidity velocity

[[assie-2021-mugast-agata-vamos]] AS21-8提供另一条直接方法路线：19O(d,p)20O的1.673-MeV γ，经lightparticle energy/position重建heavy-ion momentum后FWHM7.1keV，而meanbeamβ=.126给10.2keV。两种处理共享同次acquisition/VAMOS20Otag，改善同时涉及speed/direction与kinematic约束，不从总差反推出单一PSA/velocity resolution或独立replication。

### Two-body 输入与发射阶段

在声明的binary channel与同一reaction vertex，four-momentum满足 `PH=Pbeam+Ptarget−Plight`，heavy velocity为 `bH=c pH/EH`。Light energy和两方向分量提供与heavy TOF/track不同的信息；仍需已知beam/target species、reaction-depth beam energy、target/light energy loss与共同coordinate/calibration。若有额外unseenparticles或后续stopping，不能把该PH无条件代所有γ发射时的vector。

AS21-17的20O run使用Au backing，source因此未能用VAMOS完成target-loss/thickness路线；它没有报告本任务需要的完整backing/lifetime/emission-vector packet。AS21-12的particleEx×γenergy可帮助区分direct/feeding entrypoint，但不是完整stopping history。Commissioning16O段的CH2/d-channel打印对应（AS21-14）也保留，不拿它当已核定的targetmanifest。

### Rigidity speed 与 integer PID

AS21-9/10先识别integer A/q，再用mass-number形式 `βγ=Bρ q/(3.107A)`（Bρ以Tm）重建β和heavyflight；conditional derivative为

$$\frac{\delta\beta}{\beta}=(1-\beta^2)\frac{\delta(B\rho)}{B\rho},\qquad
\frac{\delta T}{T}=\frac{\delta L}{L}-\frac{\delta\beta}{\beta},\quad T=\frac{L}{\beta c}.$$

完整variance须含path/rigidity covariance。Source的.2%resolution未明确σ/FWHM convention；其⌊A⌋/⌊q⌋记号也不是本任务取得的执行rounding code，不推荐据数学floor符号替真实PID regions。

[day13_rigidity_pid_covariance.py](../../system/scripts/day13_rigidity_pid_covariance.py)自设A20/q8/β.126、L7m、两个relative designσ各.002。ρpath,rigidity为−.8/0/+.8时，flight σ约.697635/.520001/.232611ns；MC最大relative差.201%，derivative FD差<8.8×10⁻12。这不是重现source~800ps，因为真实path、width convention与clock packet未给。

同一Bρ若假定A19/q8、A21/q8、A20/q7，β变为.132518/.120089/.110456；这些只是physically allowed O charge/mass-label模式的counterexample，不给actualmis-ID probability。正确mode可有很小continuous error，wrong mode仍带来不同gamma angle residual或TOF。Knownreaction channel、独立line与actualPID confusion matrix能排除模式；不能仅据conditional errorbar证明PID正确。

Light TOF还需 `Tlight=Theavy−TMUGAST−VAMOS` 的实际time difference/start/path/clock/walk covariance。Source改善的1.4ns与电子jitter边界属于其high-rate配置，不移植为本run timingσ。Particle、γ和heavy tag的联合事件是互补约束，同时共享beam/target/DAQ；不按三个subsystems计三份独立实验。

### Exact two-body 与反应 entrypoint 的可证伪例题

[day13_two_body_entrypoint.py](../../system/scripts/day13_two_body_entrypoint.py)使用明确的synthetic masses：beam19u、deuteron/proton rest masses、groundheavy由自设Q5.4MeV定义；beamT152MeV与Ex1.673/3.570MeV仅为AS21-3/8的scale-inspired输入，不是actual19O/20O mass/target/backing模型。

对三light角度解二体mass shell，使用测得的light four-vector可恢复heavy vector与entry Ex；随后逐γ两体衰变保持各mass shell与four-momentum。不是从较低γ的line identity先假定所有events都直接布居这个母态。AS21-12的实际particleEx×γenergy图正是支持检查direct/feeding entrypoint的source evidence。

合成高entry3.570先发feedingγ再发lower1.673γ，反演必须用lower emitter的四矢量。若强制把lower mass当reaction entry并允许beamenergy自由变化，constraint有两个解，beamT≈10.73376/66.21207MeV，都远离本例已知152MeV；lowerγ校正分别偏−124.023/−59.074keV。Knownbeam或真实particlemissingmass可以排除这两wrong-entryhypotheses，不能只以某次拟合得到root就称模型成立。

首轮程序因误假定全区间单根而失败；检查显示massconstraint在beamT≈32.56055MeV处有内部minimum，两个endpoint同号却有两内部roots。已用解析stationary condition分别bracket并保留两解。这个失败/修复记录是本任务建模验证，不是sourcecode错误。

在该特定gamma方向下，遗漏feedingγ、直接以prefeeding reaction vector校正lowerγ只差约−.01865keV，展示entrypoint误判与γrecoil是不同机制；不把这个小值移植到其它角度/能量。自设four-input independentΣ（beamTσ.1MeV、lightTσ.01MeV、θ/φσ各.1°）给restγσ.059621keV，MC.059667；未含target/beamspot/PSA/history，不能用它解释实测7.1keV。全部mass-shell、stagedinverse和covariance检验通过，actualsourcepacket仍缺。

## Post-degrader reference 保留的 velocity-history 信息

[[lemasson-2023-agata-vamos-fission-history]] LS23-8 的Fig6是直接边界：以measuredvd校正，after-degraderγ落在U reference，before-degrader vt>vd落在angle-dependentS band。U仍在运动，不是stopperβ0。Collinear与backwardangle近似下，`Ecorr/E0=Dd/Dt<1`；使用trueinstantaneousβem可恢复所有E0，却不再单靠这个energy变量保留原lifetimehistory。应同时保存lab、reference-corrected、使用的vector/stage与gates，按分析目标选择校正。

[day13_degrader_reference_history.py](../../system/scripts/day13_degrader_reference_history.py)自设βt=.12、βd=.09、16.7μmfoil、properlevelτ3.8ps/feeder0或7.5ps；sourceLS23的centralτ与厚度仅给illustrativescales。Labβ在foil内线性减小，properclock独立积分；gap=.470mm时：

| history | before / inside / after foil（unconditional） |
|---|---|
| direct levelτ3.8ps | .967065 / .004269 / .028666 |
| feeder7.5ps+level3.8ps | .674235 / .020041 / .305725 |

在self-chosenideal120–170°cap、correctedGaussianσ1keV及E0±5keV门后，两种history的gatefraction约.02972/.31960，而且选中样本主要是afterfoil；这个门不保留原unconditionalS/Upopulation。Beforefoil γ用postreference在120/145/170°分别偏−21.1399/−31.1653/−36.0982keV。Finitefoil、feeding和energy/angleselection分别影响line profile，不能只拿peakheight/width推出τ。

Stagefractions analytic/MC最大差.000925，proper-clock/grid与truthinverse/staticequal-speed检查通过。实际Mg stoppingpower、straggling、finitearea、nuclearalignment、vertexdisplacement和velocitycovariance未给；本fixture不拟合sourceFig6/7或测新τ。

## Focal-plane delayed 样本的 survival 与速度选择

LS23-3/11/12给约760cmflight、v2.9–4cm/ns与FPgasstopping/lateγ的source尺度。若初始isomerpropermeanlifeτ、labflightT、之后瞬时停止，且停后理想window为[a,b]，则

$$P_{alive,FP}=e^{-T/(\gamma\tau)},\qquad
P_{late}=e^{-T/(\gamma\tau)}[e^{-a/\tau}-e^{-b/\tau}].$$

这里“alive”指FP时仍在isomer，不是离子是否存在；γ衰变后sameisotope仍可被PID。实际window/start、finite stopping、branch/ICC、ε/background另需packet，不能据latepeak缺失直接排isomer。

[day13_delayed_survival_selection.py](../../system/scripts/day13_delayed_survival_selection.py)自设uniformvelocity、instantstop、unit photon/detector efficiency，window100ns–200μs取sourcecapability尺度，非originalexecutedgate。Properτ100ns时，FP平均isomersurvival.112365、理想lateprob.041337；selectedmeanv由3.45变3.51428cm/ns，fast/slow survivalratio2.0655。τ1ms时lateprob仅.18113，即使几乎全部isomers到FP也会被finitewindow丢掉许多。

132Te sourcehalf-life28.1μs须转meanτ40.53973μs；同toy得到survival.994570、totalidealprob.984957，不能当该实验真实efficiency或decaybranch。Independentintegration/MC最大prob差.000787，half/mean、zero-flight及full-window极限通过。Prompt/delayed样本可因survival有不同velocitypopulation，sameisotope标签不自动恢复相同jointresponse。

## 20O progress report 的 RF 与 lifetime–energy contract

[[ciemala-2019-20o-dsam-analysis-status]] CO19-2/3/6/9/10/12明确是18O+Ta deep-inelasticdata，非AS21的19Otransfer/Aubacking。VAMOS v=D/T、mass/charge联合RFtime与energycal；PARIS–RFdrift信息修正mass稳定，但同reference不能当独立绝对velocityvalidation。

CO19-7/8的long1674-keVline（sourceτ10.5ps）与short2396-keVline有不同angletrend；zeroaverage不等alloutside，shortcentroid差也不唯一给τ。Source明确preciserestγenergy缺口，需要jointτ/Eγχ²；320/200fs是引用NN/NN+NNN模型，below~300fs只是其初步解释，没有finalbestfit/CLlimit或absoluteB（CO19-1/9/13）。

Generator用currentβ作forwardshift，target内发γ后ion继续输运到targetend；同样叫“γemittervelocity”的输出仍需emission/exitstage标识（CO19-10/12）。This is a variable-contract boundary, not proof of a source-code bug. Actualsimulations/corrections必须与measuredlatevector/response匹配，不能将truthinverse的collapsed能谱当lifetimefit模板。RFcycle/nearest-charge/calibrationcovariance与fullmodelpacket缺失时，保留readiness而不补出τ。

### Unknown Eγ 与 lifetime：centroid 和 full shape 的信息不同

CO19-9的jointτ/Eγ要求可用一项声明的designexercise检验，不能以原图的几个centroid直接测τ。 [day13_lifetime_energy_design.py](../../system/scripts/day13_lifetime_energy_design.py)自设properclock线性slowing β.105→.10、duration.13ps、E0=2396keV、correctedGaussianσ1.5keV、pointangles130/150/170°，isotropic-rest条件angularJacobian参与归一化。它不是source的reaction-depth/stopping/feeding/geometry generator。

在syntheticτ=.20ps的数据分布上固定另一hypothesis τ=.32ps：

| 比较的量 | 结果 | 范围 |
|---|---|---|
| 只以三个centroid拟合common E0 | E0_alt=2395.104079keV；residual−.166083/+.032079/+.134043keV | 未给真实centroid/Σ误差，不据此接受或排sourceτ。 |
| 用完整normalizedprofiles再优化E0 | E0_alt=2395.780664keV；meanKL=.02843494/conditionalphoton | 假定所有slowing/response参数准确，未fit原实验。 |

自设N1000/10000时，expected`2N KL`约56.87/568.70仅是**此exact model下的designinformation metric**，不是sourceχ²、CL或NNNforce证据。Restenergy可吸收centroid差，fullshape可能保留更多tail/mixture信息；若真实stopping/feeding/response/calibration uncertain，它们还可削弱或改变这个辨识性。

Profile归一化与96/192timequadrature差<2.2×10⁻15，independentimportanceMC mean最大差.00353keV；no-loss、largeτoutside与same-modelKL0极限通过。τ.20/.32只是sourceCO19-1理论scale-inspired hypotheses，不是本任务测得值或physics-modelranking。实际jointfit应保存template/version/Σ与independent energycalibration/held-outline条件。

## Direct calibration controls 与 history 控制的边界

[[ziliani-2019-agata-calibration-controls]] ZL19-1/2/4/8/9给同July2017experiment的实际checks：GGPcrystal TS重放对齐后，tightpromptgate使P/B提高>2、photopeakcounts损失<4%；coreenergy用Eu/AmBe及中间Pb/Mg环境energyanchors。既是有价值的data preparation，也不能把P/B换成P/T、countsretention换absoluteε、resolution换centroidaccuracy/Σ。

该直接reference把CO19-8的known~27fs18Ocontrol定位到1938.2(2)keV（printedτ26.5(29)fs），1981.93(9)keV则对应τ2.80(7)ps。两近energyline在同isotope标签下有不同centroid/shape角趋势，支持target-emissionhistory检查；仍需matchingpopulation/feeding/velocity与response，不能宣称每个gate/γ是independentreplication。静止energyanchor与knownshortτcontrol检查不同项，不能为了窄峰把shortline的physicalshift强制归零。

ZL19-6的百分比resolution并未全文明示σ/FWHM；ZL19-7的2754.007keV为Mg环境energyreference，不是Eu-decay分支。Doingenergycalibration与usingknownper-sourcephotonintensity做absolute ratecalibration需要不同输入，source-spectrum同出现不保证同emitter或normalization。

### Shared calibration references 的协方差

对各crystal线性energyfit `E=a_k+g_k channel`，同一referenceenergy误差会共同进入多个(a_k,g_k)。若独立centroid统计误差σstat相同、另有commonzero误差σsys，N个等权crystal合并后的简单模型为 `σmean²=σsys²+σstat²/N`，而不是把common项也除N。这是本任务variance分解，不是ZL19报告的实际uncertainty。

自设σsys=.10keV、σstat=.20keV、N31，得到σmean≈.106255keV；若把totalerror当31份完全independent则≈.040161keV。SourceTableI的widthpercent、tabulatedanchorerror或lastfitresidual都不能单独给出这两个输入。需要referenceΣ、channelcentroid/fitcovariance、run-time stability与energy-dependentresponse，并在held-outline/angle上核验transfer；共有RF/energy/calibration不能重复计独立证据。

## 20O 两次独立寿命测量的速度与馈入对照

[[ciemala-2020-c16-o20-lifetimes]] CI20-1/2/3/6 与 [[zanon-2023-o20-high-precision]] ZA23-1/2/3/7 为两次独立采集。前者20O2+2总τ150(+80/−30)fs，后者70(10)fs（作者90%区间70(14)fs）。这是报告数值的张力；2023作者明确说原因未完全理解。不能将旧partialτ190fs与新totalτ70fs直接比较，也不把两个quotedinterval当独立Gaussian误差求精确σ或pooled值。

| 检查项 | 2020：18O+Ta | 2023：19O(d,p)+CD2/Au | 可检验的必要伴随观测 / 反证 |
|---|---|---|---|
| 入口速度 | VAMOS末速度/角度经reaction/stopping/depth模型迭代重建；按state条件化。 | 质子能量/角度给反应点速度/Ex，SI各state有不同β分布。 | 比较state-conditioned初/末分布、spectrometer acceptance、particle标定/beamprior及propagatedΣ；不能把测量与重建误差都叫同一βresolution。 |
| 发射历史 | thickTa中reactiondepth/energy-loss及direct/dissipative混合。 | 薄CD2产生、Au develop DSAM线形。 | 独立stopping输入、thickness/depth与材料变更；同一个τ在多个有效transport条件能否解释线形。 |
| 馈入 | 本次未取得逐entrygate的完整feedingpacket。 | Ex门选2+2/3+1；SI首次观测1156.0keV3+1→2+2、BR28(1)%。 | Ex迁移矩阵、gate边界扫描与tagged1156coincidence；若gate leakage约束远低于造成偏差所需feeding，削弱该解释。28%本身不等目标samplefeeding。 |
| τ–Eγ | 最优2394.6±1.0keV/150fs，三角区联合拟合。 | SI谱学2396.1(2)keV、τ/E联合扫描；二维Δχ²2.3/4.6。 | 固定/约束/自由E的profile对照、独立energycalibration及actualχ²grid；不能先把restenergy当无误差再解释τ差。 |
| 响应/controls | 19Oshort2779线140(+50/−40)fs vs引用92(19)fs；long2371线extendedvalley。 | long20O2+1两target的E/FWHM data/sim对照。 | held-outenergy/angle/state、非Gaussiantails和逐配置response；若不同nuisance都通过longcontrol，该control不能独占cause。 |
| 独立性 | 与2019CO19/ZL19同July2017谱系；旧图/重放为依赖检查。 | 与MUGAST/AS21为另一data/method链；main/SI非独立实验。 | 两实验独立采集仍可用相同仪器原理、stopping库或nuclear reference；共享数值covariance需manifest证据，不假定0或完全相关。 |

以上矩阵为`our-inference/synthesis`，sourcefacts由CI20-1–8、ZA23-1–10回链。另一个待检验机制是两最佳restenergy差与τ–Eγ相关共同影响寿命；它只是本任务候选，尚未取得原数值面/模板，未证明它解释80fs差。

### Feeding branch 与目标样本 fraction

ZA23-4/5给的是3+1→2+2 branching `b=.28`。若入射布居为P2/P3、2+2-entry门对直接/上态接受率为A2/A3，忽略其它feeding时，所选2+2样本的feedfraction为

`f = P3 b A3 / (P2 A2 + P3 b A3)`。

这是本任务明确的两入口模型，不是source报出的f；真实模型还需γ效率、particle/ion/coincidence条件和其它入口。若P2=P3且A2=A3，f=.21875；改变P3/P2或Ex leakage会改变f，而不改变b。若上态先等54fs再在目标态等70fs，未分辨样本的平均发射等待时间为 `70 + f×54 fs`，是meanhistory而非单指数拟合τ。即使这一模型f=1也只到124fs；它不能单凭28%支路就宣称造成旧150fs。真实DSAM线形对transport/选择与未见上态敏感，不能把此meanbound当对2020实际feeding的排除结论。

### Ex门泄漏与错设单寿命拟合：受限设计练习

[day13_entry_gate_feeding_design.py](../../system/scripts/day13_entry_gate_feeding_design.py)以ZA23-2/3/4/5的问题为动机，**自设**ExGaussianσ、布居比例、gate、transport与Gaussian能量response；不是两次experiment的refit。Ex中心4.071/5.228MeV、branch.28、τ2=.070/τ3=.054ps取source-scale，β.126→.08在自设properT=.4ps线性下降，之后constant；忽略photonrecoil、其它feeding、alignment与真实Au-stopping。

直接等待密度`h2(t)=exp(−t/τ2)/τ2`；两步cascade密度`h32(t)=[exp(−t/τ2)−exp(−t/τ3)]/(τ2−τ3)`，相等τ极限为Erlang2。按入门f混合，精确forward用emissionβ、correction用exitβ，并将isotropicrest-photon的点labangle权重`D_em^−2`纳入条件化。故进入Ex门的f还不严格等每个γ角样本的detectedf；meanwaiting、conditionalenergyshape与错设fitτ是三种量。

自设P3/P2=10、2+entry门4.071±.2MeV时：Exσ=.25/.5/.75MeV对应f=.000314/.180708/.466922。保持σ=.5，gatecenter移−.1/0/+.1MeV给f=.124381/.180708/.255055；这些大σ/布居只是设计反例，不估实际MUGAST漏门。实际gate-falsifier需data测得迁移矩阵，而不能从branch.28直接填f。

| 自设entry f | 真proper等待均值/fs | 无feeding、固定E最佳τ/fs | 无feeding、profileE最佳τ/fs | Profile E−2396.1/keV | 最小每photon mean KL |
|---|---:|---:|---:|---:|---:|
| 0.00 | 70.0 | 70.000 | 70.000 | +0.000 | 2.92433e-18 |
| 0.05 | 72.7 | 72.683 | 72.579 | +0.028 | 3.93359e-05 |
| 0.20 | 80.8 | 80.713 | 80.108 | +0.157 | 0.000958845 |
| 0.50 | 97.0 | 96.712 | 94.048 | +0.668 | 0.0096873 |
| 0.90 | 118.6 | 117.984 | 107.621 | +2.464 | 0.0416219 |
| 1.00 | 124.0 | 123.300 | 108.370 | +3.498 | 0.0502578 |

Shape fit是三个点角130/150/170°、equal conditional samples的expectedKL投影，无实际histogram/χ²/CL。f=.5时mean97fs、fixedEτ96.71fs、profileEτ94.05fs/E+ .768keV；有可吸收部分但非零残余KL。该具体结果支持把τ/E、feeding和response共同检验，不能据此估旧150fs的cause或给新实验的feedingupperlimit。

Probability/energy归一化最大误差2.3×10⁻16，128/256timequadrature密度差2.6×10⁻15；equalτErlang、cascade survival独立积分、600k独立MC time/importance-energy moments、f0还原τ70fs及零velocityloss下shape失去τ/f信息均通过。误差预算只覆盖这个声明的模型，未验证source transport/Exresolution/实际置信区间。

### 寿命到strength的条件链

ZA23-6/11/12：τ与branches给partialradiative rate，M1/E2混合再需δ。2+2→2+1使用先前测δ−.18(8)，3+1两支δ未知而用USDB .13/.019。若以这些B分量测试模型，必须保留δ输入的模型依赖与共享τ/branch covariance。精确寿命本身不能替代δ、internalconversion/其它decaychannel和独立response；不因TableI列名“experimental”把每个3+分量当纯实验事实。

## TKEL 展开、速度tuning与90°的适用条件

[[ciemala-2021-deep-inelastic-lifetime-method]] CM21-1/2/3/5/6/7/8补出具体链：TOF以102nsRF给v=D/T，PARIS–RF漂移修正、入口DC方向/beamspot门、静止energyanchors/trace重放；校正β先含DC能损，再以knownlong19O1375.80和13C3853.170keV线做.4%/.7%velocitytuning。后两个百分数是校准变化，不是σ/FWHM；同线再符合energy不能计成独立velocityvalidation，需要held-outline/angle和sharedenergy/RFΣ。

初速度展开按100靶层、randomdepth、逐态measuredacceptedangle、TOFσ1ns与TKELΔ2MeV/nmax10递归subtraction；direct19O1471state的knownkinematics末速度对Zieglerstoppingvariation有作者<5%的1σ约束。有效输入更多了，但basisoverlap、normalization/负residual处理、reactiondepthprior与gateconditions仍需closurepacket；“measuredacceptedangle”不能无响应修正外推为full4π布居。

CM21-9/11把sensitivity与Tcross约130fs联系，模型范围约.2–4Tcross；long2371line只有lower-limitvalley、极短3842line强依赖精确energy。该比例不是所有materials/β/response的普适规律。CM21-13的frontsegment/fulltracking只是同data两处理，改变precision而不增加独立experiment。

### 印刷公式与生产执行边界

CM21-4 Eq.(1)印除以D，却把分子定义为measuredlabenergy；标准rest恢复为`E0=E_lab D`，生成为`E_lab=E0/D`，D=`γ(1−βcosθ_lab)`。按印刷标签做roundtrip会得`E0/D²`。这是文档审计，不定位生产代码错误；原paperformula不覆盖、不静默修正，actualfields/templates仍需逐步replay。

**版本修订已核实**：CM21-14/15的publisherp.6写`Eγ0=Eγ×D`，明确measuredEγ/correctedEγ0且定义aftertargetreference。上段冲突只限v1文字标签；正式版使用一致inverse，已经反证“该正式文档也混用lab/rest”的候选。Productioncode/τ本身未因v1label被否定。引用时优先正式定义，v1/currentarXiv的不同版本边界保留。

CM21-8/9的生成发射速度与分析finalvelocityreference应分别保存。Sourcep.12明确correctedline-shape使用aftertargetfinalβ；其它段落的“atdecayvelocity used Dopplercalculation”不能直接证明truthvelocity进入了最终correctedoutput。

CM21-15/19正式版提供更多约束：`v_after=vV+T/[vV² f(θ,φ)]`，材料T按Z从LISE起步并用longγfine-tune，source文字称f正比DCpath；这个T是velocitycorrectionparameter，不能与TOF的时间T当同量。PublisherFig.14全靶sum初分布是黄线、first10layers是绿线，v1的绿线midtarget说明不可沿用到final图。ActualT/f参数、Σ、residualsubtraction和entryfeedingpacket仍未取得。 同式固定T/v时Δv∝1/f，与文字path比例的通常能损monotonicity还需T/f定义和代码核验；不自动将printedf作为真实geometry来外推其它trajectory。

CM21-17/18正式版明确所示controls的totalerrors含stopping/background/ionvelocitysystematics，按80%CL区域描述，并称cumulativelifetime含可能feeding；作者基于未见populatingγ认为所考虑cases贡献可忽略。CI20原2020所报1σ、CM21v1的1σ、CM21final80%、ZA23的joint68/90%各守本版本，不能换成统一Gaussianerror，也不能把后续80%表述无说明地重标2020所有数字。非观测feeding需efficiency/threshold/entrypopulation上界才成为定量反证，2023新branch不自动给2017sample的f。

### 90°只是低速一阶的shift控制

CM21-12的“90°unaffected”在精确式下需要限定。对labθ=90°，`E_lab=E0/γ_em`；使用exitβ校正后 `E_corr/E0=γ_exit/γ_em`，只有emission/exit速度一致才完全归零。不同历史仍留下约 `E0(β_exit²−β_em²)/2` 的transverseresidual。点角处消去一阶longitudinalshift很有价值，±10°角区还需积分角response和covariance；不把它当无速度依赖的绝对energyanchor。

Source强调90°可解τ/E相依是有用设计动机；真正验证应保留exactboost、finite-angle、energycalibration与angle/βcorrelation。该限定不是否定扩大角覆盖，而是规定其可独立约束哪一项。

自设E0=2396.1keV、βem=.105/βexit=.1，exactpoint90corrected residual−1.24073keV（二阶−1.22800）；βem=.126/βexit=.08时−11.45322keV（二阶−11.35272）。这些参数不代表CM21实际transport；展示β²项可与keVenergyprecision同量级。另自设β=.1/θ150°的scalar标准inverse与independentinversefourvector均还原2396.1keV；按v1lablabel做除D回到2009.08681keV，−387.01319keV仅是该文字counterfactual。正式版定义已通过标准roundtrip，不能把此偏差归给source实验。原细节保留于本run的`cm21-convention-90-control-exercise.json`，方程/假设在本页，未成为outputs-only知识。

## RF周期编号与连续速度精度的不同信息

CM21-1的RF102ns/TOF、AS21-9/10的integerA/Q与rigidityspeed为动机。以下仅是**RF周期编号丢失的假想模型**；实际VAMOS是否已保存/解卷k，要查rawtimestamp/productioncode。若只保留phase，`T=phase+kP+offset`；连续TOF误差小，仍可能存在离散k/ionicq解。

[day13_rf_tof_alias_design.py](../../system/scripts/day13_rf_tof_alias_design.py)自设mass=A u、恒定flightβ、无材料loss、Z8、equalA17–21/q5–8priors。固定Bρ=0.741630Tm、true(19,8)β.1，并选path使(20,6)另一β.071426...的flighttime恰好多一个102ns周期。Path约7.643762m为刻意构造，非真实VAMOSgeometry。

| 量 | 分支(19,8) | 分支(20,6) |
|---|---:|---:|
| Flight/ns | 254.968470 | 356.968470 |
| Period index k | 2 | 3 |
| RF phase/ns | 50.968470 | 50.968470 |
| β | .100000 | .071426 |
| 自设mass-proxy kineticenergy/MeV | 89.1612 | 47.7045 |

两解rigidity/phase完全闭合；加入自设independentenergyσ2MeV后该假想数据的错分支强烈受限。局部自设phaseσ1ns/pathσ.01m给truebranchβσ.00041345，500kMC得.00041354；两个β相差约69个局部σ，仍有同phase/rigidity的全局分支。不能用localprecision排除latentdiscretealias，也不能把条件于同PID的rigidityβ再当独立验证。

以自设1375.80keV/150°光子，correctbranch还原restenergy；另一分支给1341.1544keV，偏−34.6456keV。这只是纠错敏感性：未确定restenergy/lineidentity的光子不能自动充当独立clock。真实case还要mass精值、field/path/material、chargeexchange、clock/PID/covariance和population，不报告实际周期误判率。

反证/必要观测：有absoluteperiodindex、独立totalenergy或ionicq、可靠knownline/anglehold-out时，所构造alias可被排除。Raw仅RFreference不自动表示仅有phase；明确这些信息已存的pipeline不适用此反例。算法period/rigidityphaseclosure、independentenergy、MCvariance、精确γroundtrip与derivative检查通过。

## 计数统计量、joint区域与寿命轴区间

[[baker-cousins-1984-histogram-fits]] BC84-1/2/3/4/5/6/7/9提供ZA23-10（Neyman/rebin≥10/jointΔχ²）的直接方法入口。Bin模型应为积分`y_i=∫bin ν(E;τ,E0,η)dE`；Pearson`Σ(n−y)²/y`、Neyman`Σ(n−y)²/n`与Poissondeviance `2Σ[y−n+n ln(n/y)]`有不同finitecount性质。原counts含backgroundsubtraction/sharedgate时，不直接把subtractedbin当independentPoisson。

### 均匀Poissonrate的可解析反例

[day13_count_statistic_regions.py](../../system/scripts/day13_count_statistic_regions.py)是自设32个相同meanμ的independentPoissonbins，200k重复。三种score分别给Neyman的harmonicmean、Pearson的RMS和Poisson的arithmeticmean；这是rate模型，**不是τ/Eline-shape**。

| 自设μ/bin | 全MC最小observedcount | Neyman估计mean | Pearson估计mean | Poisson估计mean |
|---:|---:|---:|---:|---:|
| 50 | 17 | 49.011092 | 50.481935 | 49.999741 |
| 100 | 50 | 99.018430 | 100.480297 | 99.996956 |
| 200 | 132 | 199.036816 | 200.493577 | 200.009983 |

所有observedbins≥10，而Neyman在μ50case的bias约−.989count/bin；三scoreclosedform代入与PoissonMC无偏范围检查通过。它反证“仅≥10就保证无偏”的额外假设，不证明ZA23的τ偏长/偏短，也不说明MLE在任意非线性τ/E或边界问题都无偏。BC84-10的WLS简述须同时核data-dependentweights：1/n不显式依赖参数，但与dataerrors相关。真实τ/E方向、binning、背景、normalization与response要用本实验packet验证。

### 二参数区域、投影和profile的不同覆盖

另一个明确自设的regularGaussiancontrol取στ10fs、σE.4keV、ρ−.8；不是source covariance，也不将reported±10fs当其Gaussianσ。坐标是估计量相对真值的δτ/δE。对完整C的quadraticdistance `q=xᵀC⁻¹x`，joint二参数概率`1−exp(−Δq/2)`；将jointellipse投影到τ轴的概率为`erf(sqrt(Δq/2))`。Profile掉E时则`q_profile=(δτ)²/στ²`。

| 自设Δq | Joint two-parameter概率 | Ellipse投影τ轴概率 | 忽略offdiagonal后MC joint概率 |
|---:|---:|---:|---:|
| 1 | 39.347% | 68.269% | 48.389% |
| 2.3 | 68.336% | 87.063% | 71.742% |
| 3.21888 | 80.000% | 92.721% | 80.329% |
| 4.6 | 89.974% | 96.803% | 88.130% |

1M独立GaussianMC核joint/projection与analyticCDF，energyprofileidentity通过。Joint68.3%区域的τ投影约87.1%，不能把两类区间当同定义；ρ丢失也改变coverage。上述只为regularGaussian模型，不能用它反推CI20、CM21的total80%或ZA23原报误差/τ差异σ。需要实际统计量、nuisance处理与confidence construction。

### Overall normalization与计数信息

BC84-4/6/7：`Lp=P(N;N0) Lmultinomial(n|N)`；模型有完全自由overallscale `y_i=a g_i(shape)` 时PoissonMLE保持Σy=Σn，pointestimate可与multinomial等价；interval不自动相同。若`y_i=a g_i+b_i`有固定background、外部yield/efficiency或prior约束，freeoverallscale的充分条件可能不成立，不能无说明删除总rate项。现有selfchosenconditionalshape/KL练习主动排除了总yield信息，保留各自边界；不当成actualextendedlikelihood。

Validationpacket应包含bin edges/counts、rebinrule、各背景观测/normalization、simulation统计量与templateintegrals、相关Σ、拟合参数/nuisance约束、point/interval/GOF各自定义和pseudoexperimentclosure。Sourcepaper/这两toy没有替代这些输入，L4refit仍未ready。

## 同一发射等待分布不唯一对应目标态寿命

CM21-18的cumulativelifetime/feeding与ZA23-2/3/5/7的entryselection问题，可以用一个**自设、可解析的反例**深入检查；此为`our-inference`，不是来源给的feeder数值或20O差异原因。[day13_exact_feeding_history.py](../../system/scripts/day13_exact_feeding_history.py)验证整个properemissiontime分布，补充前面的meanwaiting/错设KL练习。

令纯直接布居模型的等待为`Exp(τeff)`。另一模型目标态固有τl<τeff，上态τu=τeff；直接布居fraction `r=τl/τeff`，feedingfraction `f=1−r`。若等候时间独立、上态γ反冲/transport区别忽略，研究目标γ的properwaiting density为

$$
h(t)=\frac{r}{\tau_l}e^{-t/\tau_l}
+\frac{1-r}{\tau_{eff}-\tau_l}
\left(e^{-t/\tau_{eff}}-e^{-t/\tau_l}\right)
=\frac{1}{\tau_{eff}}e^{-t/\tau_{eff}}.
$$

Laplace form也精确相同：`[r+(1−r)/(1+sτeff)]/(1+sτl)=1/(1+sτeff)`。相同的是整个分布；不只mean/variance或有限bin图。只要两模型使用同一recoiltrajectory/properclock、同一研究γ及共同response `K(o|t)`，`∫K(o|t)h(t)dt`也相同。多角覆盖、更高statistics或相同targetγ的held-out重处理本身不能排除这个特定的history竞争者。

自设τeff120fs、目标τl60fs、上态τu120fs、f=.5：propermean均120fs、variance均14400fs²，但目标固有寿命不同。沿既有自设β.126→.08/proper.4ps、Eγ2396.1keV/Gaussianσ2keV、130/150/170°计算，normalizedenergyprofile最大差1.4×10⁻17；timedensity差1.8×10⁻15/ps、归一化和generalr/端点Laplace检验通过。独立600kMC两等待样本KS statistic .000788，三角importance-weightedenergy moments相容；这个KS只作模拟一致性检查。

条件与反证必须同时保留：actual upperγrecoil、不同状态transport/alignment/角关联、feeder标签、γmultiplicity/trigger或particleEx entryselection可能使K不再共同，从而打破退化。对pre-angular-selection parentpopulation和unit4π targetacceptance，自设feedγtagε=.25时alternative预测tagfraction.125，直接-only模型0；逐角acceptedγ样本需另计算conditionalf/ε，不能移用该分母。这是提出独立伴随观测的例子，不估本实验ε或f。若directentry已经受可靠门/布居/branch/upperτ约束，竞争者可被排除。

ZA23的已知3+1τ54fs不是本构造的120fs上态，BR.28也不是f=.5。本反例不证明它造成CI20的150fs，也不重判实际τ/B。它支持具体的验证契约：漂亮的targetγfit还需独立entry/feeding信息；cumulativeτ与目标固有τ的区别须随branch/δ/absolute-strength链保留。代码只验证声明的共同轨迹/无feederrecoil模型，source-experiment remains not-ready for refit。

## Cascade recoil 对共同响应假设的限定

上段exactfeeding identity假设共同K。另一项自设练习[day13_cascade_recoil_response.py](../../system/scripts/day13_cascade_recoil_response.py)加入upper→lower+γ的two-body recoil，隔离其中一个failurecondition；source动机为CM21-18/ZA23-5的feeding以及T12C-1/2的level/photon区分，具体数值为任务推导，不是source实际cascade。

设mass-energy mU=mL+gap，upper-rest photon `k=gap(2mL+gap)/(2mU)`、lowerenergy`eL=mU−k`、recoil`u=k/eL`。下态在自己restframe发研究γE0；在parentframe固定方向n′时`E′=E0/[γr(1−u·n′)]`。用parent-reference的Dopplerinverse会还原E′，未必E0。Code用反向/正向四向量boost独立核scalar式、aberration与mass-shell/能量动量守恒。

本模型parent恒速、upper与targetγ各isotropic，未含实际cascadealignment/角关联，Gaussianσ2keV为自设correctedenergyresponse。Fixedlabangle条件使用recoil角权重Drec⁻²；角平均归一化1、meanE′=γrE0、var(E′)=E0²γr²u²/3。Mean为u²效应、width为u效应。Feedfraction自设.5，E0=2396.1keV，mass=A u proxy，不作actualstateassignment。

| 自设A/gap | Feed-only recoilσ/keV | 混合Gaussian后σ/keV | Fixedresponse KL/photon | 自由mean/σ后KL边界 |
|---|---:|---:|---:|---|
| 20/0.1MeV | 0.007426 | 2.000006892 | 1.1876e-11 | <1e-12，数值未分辨 |
| 20/1.0MeV | 0.074254 | 2.000689097 | 1.187e-07 | <1e-12，数值未分辨 |
| 20/3.0MeV | 0.222751 | 2.006192688 | 9.5775e-06 | 1.083e-11 |
| 130/1.0MeV | 0.011424 | 2.000016313 | 6.6532e-11 | <1e-12，数值未分辨 |

A20/gap1MeV下extra recoilσ.07425keV，50%mix使σ2变2.000689keV。响应严格已知时chosen10000photons的expected2N×KL约.002374，仅是此model的designmetric；自由Gaussianmean/σ吸收大部分差异，residualKL<1e−12不报精密物理显著性。表的massscaling不能移植为实际A≈130或20O的responsebudget。

角度积分/解析moments、600k独立MC、嵌套Lorentzboost、zero-gap/large-mass/zero-boost与profile归一化通过。这个constant-flight模型没有重做foil τfit；若正确知道lower发射速度，使用它是另一reference，并不等于本例刻意忽略kick的parentreference。实际stopping、upper/target角关联、alignment、trigger/tag、source-responseΣ可能改变signature；独立entry/feeding标签仍是重要约束。

## 等有效停止率下，末速度缺少反应深度信息

CM21-6/7/19的TKEL/depth/response重建要求把测得末速度与输入prior分开。一项自设1Dfoil例题[day13_depth_prior_velocity.py](../../system/scripts/day13_depth_prior_velocity.py)只验证其中一个特殊information-loss极限；**不复制CM21反应或productiongenerator**。

设massproxy20u、共线foilL4μm、beam100MeV、固定channelkineticloss4MeV、有效constantSbeam/Sprod2.5MeV/μm。Energybookkeeping为`Ti(x)=Ebeam−Sbeam x−loss`、`Tf=Ebeam−loss−Sprod L+(Sprod−Sbeam)x`。等有效S时Tf=86MeV/β.09575459与x无关，而stateentryenergy和剩余减速历史依赖x。这个盲点只限已声明模型，已知实际geometry/beam-product stoppingcontrast可排除它。

Relativisticproperclock写`eta=acosh(1+T/M)`、`deta/dproper=−S c/M`，出foil后eta恒定。最大propercrossing.134879ps；独立路径积分与解析clock差4.4e−14ps以下。SourceCM21的Tcross130fs只是动机尺度，本例数值不代表真实foil时间。

入口x prior取uniform、front-triangular 2(L−x)/L²、back-triangular 2x/L²。三case真实τ均80fs、Eγ2396.1keV、Gaussianσ1.5keV；对130/150/170°条件能谱以错误uniformprior做selfexpectedKL拟合：

| 自设真depthprior | 末能量/MeV | 150°correctedmean/keV | 固定E/错uniform最佳τ/fs | ProfileE/错uniform最佳τ/fs | ProfileE−2396.1/keV | Residual meanKL/photon |
|---|---:|---:|---:|---:|---:|---:|
| uniform | 86.0 | 2393.846699 | 80.000 | 80.000 | +0.000000 | 5.27356e-16 |
| front | 86.0 | 2392.810189 | 42.586 | 40.054 | +0.101302 | 0.00139576 |
| back | 86.0 | 2394.881413 | 172.825 | 190.726 | -0.128567 | 0.00861837 |

这说明在特殊equal-S极限，相同exitvelocity不独立验证entrydistribution；错误prior可给不同pseudo-trueτ/E。非零residualKL也说明完整shape/已知response可反证错模型，并非任意τ/depth都不可辨识。Uniformtruth有一个optimizerstart nonsuccess，另两start恢复τ80fs；flag完整保留，未宣称每个start成功。上述不解释真实150/70fs差异，也不计算实验χ²/CL。

Equal-S三prior的500k独立MC验证constantexit及propertime/角beaming/能谱moments；probabilityprofile归一化误差2.3e−16、96/48与192/96quadrature差3.0e−15，longτoutside/no-losslimits通过。把Sprod改2或3（Sbeam仍2.5）使Tf slope非零，front/back finalmean差约.667MeV；depth重新可被exitenergy约束。Independententrykinematics也能区分91/93.33/88.67MeV尺度的初分布，而不仅重复同末速度。

ActualCM21-21是倾斜45°靶、非共线beam/product和有限θ/φ接受，另有two-bodykinematics/TKEL、beam/depth/stopping/straggling。它不自动满足此counterexample。实际validation需要physicalprior、effectivepath/材料law、acceptedstate条件、独立entry约束与fullsourcecode/Σ；本例只固定这种依赖关系，不评估sourceprior错误或source结果bias。

## 固定代码对象的velocity字段：输入、状态和单位

[[nptool-2019-reaction-velocity-code-object]]审计的是2019公开commit的Reaction/Nucleus对象。README已指迁往GitLab，新站本次网络不可读；actuale775/2017commit、caller和当前软件未attest。这份静态sourceaudit没有运行第三方ROOT/Geant4，也不指认论文pipeline错误。

NP19-1/2/3/4/5：constructor第一token设Beam，第二Target；API轻粒子kineticenergy用MeV、角用rad。初始化beam+z/targetrest，light向量默认为(p sinθ,0,p cosθ)，P4=P1+P2−P3和Ex=P4.M−配置Mass4。对真正reaction-pointvector，caller还须提供vertex处的总beamenergy、lightenergy-loss修正、mass/state、φ/worldrotation与Σ；common框架名不能替productionbinding。

| 字段/路线 | Source实际行为 | 验证时须保存的条件 |
|---|---|---|
| ReconstructRelativistic与Reaction Lab4 getter | 前者returnEx并更新Reaction四向量；后者可取最近该向量。 | 调用顺序、输入epoch、physicalmass/beam/light条件与globalframe。 |
| SetNuclei3与GetNucleus4 | 前者额外更新Nucleus对象；只有Reconstruct不自动更新另一容器。 | Nucleus缓存/Exc/mass和getterpath，不能将不同容器字段当同次结果。 |
| Nucleus Mass()/SetEnergyImpulsion/GetBeta | Mass含Exc；setter从P.E−对象Mass取得K再算β，而非直接P.P/P.E。 | on-shell/质量状态一致性，或声明不同约束估计器与其Σ；改Exc后refresh路径要核。 |
| GetVelocity/GetTimeOfFlight | energy/mass转换；此版velocity为cm/ns，TOF为s/m的inverse-speed量，无path。 | data-origin与单位；真实flight须乘D，模型字段不自动是测量clock。 |
| Bρ conversion | 默认ionicQ取核Z。 | 实际ionicq/PID与mass/velocitystage；相同input派生字段非独立证据。 |
| Nucleus DopplerCorrection | 用storedβ和caller suppliedθ作标准inverse。 | angle必须相对recoil、frame一致；函数不自动选input/emission/exitstage或重建3D方向。 |
| Angle-only energy helper/IsAllowed | 前者某些branch50/50随机，后者仅labtotalenergy条件。 | physicalbranch/acceptance与完整invariantdomainguard，不能当independentvelocity/allowedchannel证明。 |

如果独立rawclock的T/D先换成source约定s/m并作为SetTimeOfFlight输入，它可以带来新的测量信息；从SetKineticEnergy派生GetTimeOfFlight则没有新的clock。结论应沿producer/caller追踪，不能只看字段名。

### 质量状态与invariantβ的quant sanity

任务用generic20u/Ex4.071MeV、trueβ.126构造真实on-shellP，未读取source精确mass-table。P的invariantmass=Mground+Ex；若同一E改用Mground重算scalarβ，则得.127694794，直接fourvectorβ为.126。以自设Eγ2396.1keV/relative150°，错误mass假设下校正到2399.795128keV，+3.695128keV。这是**条件counterfactual**，不是NPTool运行结果或actuale775shift。正确mass/更新路径可避免；测量噪音下有意不同mass-shellprojection须明确估计器/Σ。

另自设mass19u/beam8AMeV，输入总kin152MeV给nominalbeamβ.130223；若错按总8MeV为.030057。它只是totalMeV/per-A单位检查，不拿beamβ替重核recoilβ。β.1对应该legacyvelocity2.99792458cm/ns与inverse-speed3.33564095e−8s/m；D8m给266.851276ns。

最后genericm1=20u/m2=2u/m3=1u/m4=21u+5MeV的endothermic例，在Tbeam10MeV时labtotalenergy必要条件满足，但s<(m3+m4)²；exactlabthreshold55.00671MeV。它限定旧IsAllowedhelper的证明力，不称实际(d,p)case调用错误或当前软件同样实现。

上述on-shell、unit/path和thresholdsanity检查通过，数据/公式同步在本页；run-dir的nptool-object-contract-physics-check.json只作回执。源码字节/hash、单位/header和函数locator已固定，实际实验caller/校准/transport/rawdata未取得；L3objectaudit和L4experimentalrefit分别记录。

## 有限能量 bin：积分、边界与重分 bin

[[baker-cousins-1984-histogram-fits]] BC84-2（报告 PDF pp.4–5, Eq.(1)）规定预测为 bin 内积分。下面是本任务的合成 Doppler 练习，[代码](../../system/scripts/day13_finite_bin_lineshape.py)复用已声明的 entry/feeding 核；没有取得原实验 bin、计数或模板。

对 Gaussian 混合中心 μ_k、概率 w_k、宽度 σ，固定 bin [l_i,h_i) 的预测为

`P_i = Σ_k w_k [Φ((h_i−μ_k)/σ)−Φ((l_i−μ_k)/σ)]`。

ROI 内固定入选总数时，使用 `p_i=P_i/Σ_ROI P_i`；中点式 `f((l_i+h_i)/2) Δ_i` 即使再归一化，也未必恢复正确 shape。变动 ROI 后须重新计算条件分母；若利用丢失的计数，则还需要总 trials、效率和 extended likelihood。正尾的两个 CDF 接近 1 时，应改用 survival 差计算，避免数值相消。

自设 E0=2396.1 keV、proper τ=70 fs，已知 entry feeding fraction 0.2、upper τ=54 fs，β 从 0.126 在 0.4 ps 内线性降到 0.08；point angles 为 130/150/170°，exit-reference 校正后 Gaussian σ=2 keV。各角度以等权的**期望条件直方图**联合拟合 τ/E，没有背景或抽样拟合。

| bin 宽度 / keV | 边界移动 / bin 宽度 | 错中点式最佳 τ / fs | 最佳 E0 / keV | 残余平均 KL / 入选光子 |
|---:|---:|---:|---:|---:|
| 0.5 | 0 | 70.014943 | 2396.096521 | 2.642×10⁻7 |
| 2 | 0 | 70.238819 | 2396.044369 | 6.405×10⁻5 |
| 5 | 0 | 71.144513 | 2395.877434 | 0.001545 |
| 10 | 0 | 77.014502 | 2396.269236 | 0.019129 |
| 20 | 0 | 80.317373 | 2394.446523 | 0.064912 |
| 20 | 0.5 | 72.881943 | 2393.920386 | 0.018178 |

固定主 ROI 为 E0+[−140,+20] keV；最后一行整体移动 10 keV，仍覆盖几乎全部此模型概率，各行各自条件化。因此最后两行说明边界敏感性，不等于用完全相同入选样本做了两次独立实验。所有精确积分拟合恢复 τ70 fs，最大误差 6.4×10⁻7 fs；三次起点的 flags 保留，不以此证明全局唯一性。数值方向依赖这套输入，不能套成 ZA23 的寿命偏差。

### 正确积分也不能恢复粗 bin 丢失的信息

固定同一 ROI、对齐边界时，细 bin 概率相加等于粗 bin 概率。本例最大差 1.2×10⁻16；对非均匀 bin 的独立连续积分差 6.7×10⁻16。它们核验实现一致性，同事件的重分 bin 不提供独立证据。

条件概率的局部 Fisher 矩阵为 `F_ab=N Σ_i (∂_a p_i)(∂_b p_i)/p_i`。对齐合并的粗 bin 只有细 bin 的信息或更少；本例对 (lnτ,E0) 数值验证 `F_fine−F_coarse` 为正半定。每角度自设 N=10000 时：

| bin 宽度 / keV | τ 局部标准误差 / fs | E0 局部标准误差 / keV |
|---:|---:|---:|
| 0.5 | 0.475723 | 0.042688 |
| 5 | 0.484338 | 0.048339 |
| 10 | 0.517248 | 0.068929 |
| 20 | 0.559019 | 0.094268 |

这些是已知 response/feeding/transport 下的局部设计值，不是实际寿命误差或有限样本 coverage。细化到 1/0.5/0.25 keV 时，中点与积分的 total variation 递减；无减速时恢复单 Gaussian。独立生成 600000 个 proper-time/feeding/能量事件，以角 beaming 权重计算 5-keV bin 概率，最大标准化差约 2.46。首次 ImportError 在分析前修复，失败记录保留。

这组练习支持保存精确 bin edges、固定或数据依赖 rebin 规则、ROI 和条件分母；完整 shape 的残余差或边界稳定性可反证过粗的中点实现。它没有提供实际代码 binding、背景、模板统计量或 source 的 χ²/区间，实验 L4 readiness 不变。

## 共用背景观测如何连接 bin 与角度组

BC84-4/5 的 Poisson/counting-model 区分为方法背景；以下共享背景关系由本任务推导，**不是 BC84 或核实验报告的具体 sideband 实现**。[代码](../../system/scripts/day13_shared_background_covariance.py)使用两个互不重叠的 on 计数流，以及一份独立 off 总计数。两个 on 谱的信号 shape 来自前述已声明的合成核，背景 shape q_i 在此例中严格已知。

设 `D_gi~Poisson(A_g p_gi+q_i B)`，`M~Poisson(rB)`，所有 D 和 M 条件独立；A_g 为各组入选信号期望数，B 为各组背景期望数，r 为已知 off/on exposure。两个组共享同一估计 `Bhat=M/r`，扣除后的 `Y_gi=D_gi−q_i Bhat` 因而满足

`Cov(Y_gi,Y_hj)=δ_gh δ_ij (A_g p_gi+q_i B)+(B/r) q_i q_j`。

后一项在同组跨 bin、跨组之间均存在，不是新独立计数。扣除后的数值也可为非整数或负数，不能直接当独立 Poisson bin。此例 on 流没有事件重叠；实际共用 γ 门还需另加事件重叠产生的协方差。

### 联合 on/off 信息与局部误差传播

联合 likelihood 是 `∏_gi Pois(D_gi;A_g p_gi+q_i B) × Pois(M;rB)`。在真值处令 D 为 on 计数协方差、Q 为背景 shape 堆叠向量、J 为信号均值的导数，profile 掉 B 的局部 Fisher 矩阵等于

`Jᵀ [D+(B/r)QQᵀ]⁻¹ J`。

这来自 Schur complement/Woodbury 恒等式，验证的是本模型的局部信息；固定真值权重的 GLS 并不替代有限样本非线性 likelihood 或 coverage 检查。若用对角权重 W 拟合，实际线性估计器协方差为 `L C_full Lᵀ`，`L=(JᵀWJ)⁻¹JᵀW`；只报 `(JᵀWJ)⁻¹` 会遗漏已声明的交叉项。

自设 150/170° 两组，各 A_g=10000、B=4000，5-keV bin、E0+[−100,+10] keV ROI；q 是20%均匀加80%宽 Gaussian 的已知条件 shape。拟合参数为 lnτ、E0 和两组自由 lnA_g，真 τ70 fs。以下均为局部标准误差，单位 fs：

| off/on exposure r | 完整 C 的最佳局部 GLS | 对角权重估计器报告值 | 同一对角估计器按真实 C 传播 |
|---:|---:|---:|---:|
| 0.25 | 1.222987 | 0.856819 | 1.460071 |
| 1 | 0.997956 | 0.832553 | 1.029839 |
| 4 | 0.877933 | 0.826071 | 0.880633 |

r=0.25 时，漏掉交叉项使该对角估计器的 τ 方差低估约2.904倍；这不是原实验误差的修正系数。r→∞ 时，共享 off 不确定度消失，on 计数噪声仍保留。联合 Poisson profile 与完整 C 的局部参数协方差差<5.3×10⁻18。

独立生成120000组 on/off 计数，并应用**固定真值处的线性估计器**，完整和对角估计器的实际方差与公式最大相对差分别约0.338%和0.254%；约2.22%的扣除后 bin 数值为负。没有做原实验或全非线性 τ 拟合。

### 忽略相关项不保证同一方向的偏差

设两个量各有独立 variance v=100、共有误差 variance c=400，完整 covariance 的两行为 `(v+c,c)` 和 `(c,v+c)`。差的 variance 为2v=200，对角近似却给1000；和的 variance 为2v+4c=1800，对角近似给1000。相关项对不同线性组合可以抵消或增强，不能泛称“忽略 covariance 一律低估所有误差”。

真实分析须保存各 on/off 观测身份、是否共享事件、transfer/exposure、背景 shape 的不确定度与能量依赖。用独立 off 数据或改变共享关系可以反证本例的 rank-one 项；若 q、r 或背景成分未知，则需扩展模型。多角度投影和背景重复引用不增加实验独立性，原 ²⁰O L4 重拟合仍缺输入。

## 有限模板与共同模拟事件的协方差

BC84-2/9 提供 bin/有限样本的方法背景；以下 weighted-template 关系为本任务推导。[代码](../../system/scripts/day13_finite_template_covariance.py)用已声明的 proper-time/feeding/response 核生成模板，不使用原实验或 Geant4 模板库。Barlow–Beeston1993 的身份已核但全文未取得，未将本节归作该论文公式或实现。

对 N 个独立生成事件，记 `r_i=w·1{event in bin i}`、`u=w·1{event in ROI}`，归一化概率估计为 `qhat_i=Σr_i/Σu`。令 `q_i=E[r_i]/E[u]`、`z_i=(r_i−q_i u)/E[u]`，则 delta method 的 leading covariance 为

`Cov(qhat_i,qhat_j)≈E[z_i z_j]/N`。

这是 ratio estimator 的 1/N 近似，不保证有限 N 无偏。Σ_i z_i=0，归一化方向没有方差，完整概率 covariance 因此有约束/零方向；不能把各 bin 概率一概当独立测量直接反演该矩阵。固定**入选**N的无权重模板退化为 `(diag q−qqᵀ)/N`。固定生成数且有 ROI 丢失时还需入选率，不能把 generated N 与 selected N 混用。

### 参数扫描点共用随机数时的交叉项

若 lifetime hypotheses a、b 共用同一批 base variates，其 cross covariance 为 `C_ab≈E[z_a z_bᵀ]/N`。因此

`Cov(qhat_b−qhat_a)=C_b+C_a−C_ab−C_abᵀ`。

自设 150°、5-keV bin、τ_a70fs/τ_b72fs，其余输入与有限 bin 练习相同；直接等待、feeding tag/上态等待和 Gaussian noise 均共用。每份模板 N=2000 时，差值 covariance 的 trace 为独立模板条件下的约0.10816，8000组独立模板库测得0.10866。共用随机数减少差值噪声，同时使扫描点相关；它没有增加独立生成事件数。

同一个 hypothesis 与同样事件重放时，差值严格为零，但单个模板仍有有限误差。此例主 bin 的 p≈0.187031，其概率标准误差≈0.008675。故相邻模板差平滑或同版本 replay 一致，不证明 template truth 或无限统计量。

### 模板误差进入数据比较的条件

若入选数据 N_d 与模拟事件独立，固定 N_d 的计数 covariance 为 `C_data=N_d(diag p−ppᵀ)`；在已声明的 leading 近似下，预测 `N_d qhat` 的模板 covariance 为 `C_template=N_d² E[zzᵀ]/N_MC`。数据减预测时二者相加；若模拟/校准利用同一数据，则还需其 cross 项。

以自设 N_d=10000 和真值处的 lnτ score 为一个固定投影，仅改变生成模板数：

| N_MC | 计入模板误差后的投影 SD / 只算数据 SD |
|---:|---:|
| 1000 | 3.363854 |
| 2000 | 2.481483 |
| 10000 | 1.425325 |
| 100000 | 1.050312 |

这不是 τ 拟合标准误差、区间膨胀系数或源实验的 MC 统计预算。它只展示此 score 投影下的独立数据/模板噪声；N_MC→∞ 恢复数据项。权重、ROI、模拟分配和 data-dependent tuning 改变时需重算。

800000个独立 pilot 事件估计协方差矩，另8000组每组2000事件的模板库核验 a/b/shared-difference/independent-difference 的 covariance，Frobenius 相对差约3.4–4.1%。同 hypothesis 差为零、归一化零方向、无权重 fixed-selected-N 和无限模板极限通过。输入、两套 seed 与 dependency hash 保存于代码/运行回执；上述不是实际模板库复现。

必要实验输入是生成与入选数、权重、参数点间 event IDs/seeds、归一化/ROI、response 和 data-calibration 依赖。共同事件的交叉项若被独立 bank 替换，就应消失；这提供可检验控制。可靠 smoothing 或额外模拟可改善特定估计器，但不能通过重复同一事件使独立样本数增长。

## 自适应 bin 边界也是观测的一部分

ZA23-10 报告 rebin 后每 bin 至少10计数，实际细节未取得。BC84-2/4/9 提供 histogram/counting/finite-N 方法背景；下例为本任务自设规则，不复制 ZA23，也不以它判断原结果有偏。[代码](../../system/scripts/day13_adaptive_bin_observation.py)只拟合抽象 shape fraction p，不是 τ 或 branching ratio。

每个独立小直方图固定有 N=40 个光子，两个原始 bin 的计数为 X 和 N−X，`X~Binomial(N,p)`。若 `10≤X≤30` 则保留两 bin，否则合并为单一40计数的 bin。最终所有输出 bin 都≥10，但“保留/合并”的边界由同一数据选择。

合并输出的概率为 `m(p)=P_p(X<10)+P_p(X>30)`。完整观测 likelihood 包含保留组的原计数，以及每个合并决定的 m(p)；并非把合并组写成总概率1就已保留全部观测。若实验含 K 个保留组、C 个合并组、保留第一 bin 总计数 S，除参数无关常数外：

`log L(p)=S log p+(40K−S) log(1−p)+C log m(p)`。

若忽略最后一项，把随机边界当固定，估计为 `p_naive=S/(40K)`，只利用被截断选择的计数。true p=.25 时，其大样本极限为

`p × P(9≤Binomial(39,p)≤29) / P(10≤Binomial(40,p)≤30) = 0.298296581`。

这是规则/分布的精确期望，不因所有输出 bin≥10而消失。完整观测 likelihood 在期望数据上的最佳值为0.250000000002；若只保留被选组且条件化，则需要另一明确的 selection normalizer，不能混用这两种观察设计。

自设每次实验64个独立小直方图，8000次重复：

| 估计对象/观测方式 | p估计的 MC mean | MC standard deviation |
|---|---:|---:|
| 忽略边界规则 | 0.298259 | 0.007652 |
| 完整“计数+合并决定”likelihood | 0.249663 | 0.009147 |
| 全部原始两 bin 计数 | 0.249834 | 0.008519 |
| 独立 pilot 选择边界，随后独立 science counts | 0.249975 | 0.011679 |

完整模型在有限64组下不被宣称精确无偏；MC mean 与真值仍有约−0.000337的差，未验证 interval coverage。独立 pilot 控制中，science counts 不再受同一选择截断，但也不保证最终 science bin 都≥10。p=.5 的对称控制使本例 naive 大样本偏差为零，说明规则影响依赖 shape。

观测概率归一化、期望模型真值恢复、1061种实际整数统计量的粗网格优化对照、独立 pilot 和对称控制通过；不以这些 checks 证明任意输入的全局唯一最大值。真实 rebin 可能采用其它算法/规则，应保存细 bin 原计数、输出 edges 和选择过程，或通过完整算法的 pseudoexperiments 核验。这个例子不能给实际 Doppler τ 的偏差方向。

## 共享事件、总计数设计与重放的信息

BC84-2/4 区分 fixed-N 与 Poisson 采集；下面的 event-mark covariance 为本任务推导，[代码](../../system/scripts/day13_event_overlap_information.py)使用已声明的合成单光子线形。实际多光子事件、权重、门重叠和背景须另给 event marks，未复现任何来源的独立性处理。

设 H_i=Σ_events h_i(event)。固定独立事件数 N 时，`Cov(H_i,H_j)=N[E(h_i h_j)−E(h_i)E(h_j)]`；若独立总数为 Poisson(λ)，law of total covariance 给 `Cov(H_i,H_j)=λE(h_i h_j)`。

互斥单光子 bin 在 Poisson 采集中可独立 thinning；fixed N 则有负交叉项。两门 A/B 有重叠概率 p_AB 时，Poisson covariance 为 λp_AB，fixed-N covariance 为 N(p_AB−p_Ap_B)。不能只凭“两张投影”判断独立，或凭存在共有总N就给 Poisson 互斥 bin 添加 fixed-N 交叉项。

自设平均/固定10000事件、150°，门 E0+[−70,−20]和E0+[−50,−5] keV，p_A≈.241749、p_B≈.081529、p_AB≈.0718335。Poisson/fixed-N 两门 covariance 分别约718.335/521.239 count²；150000重复的 covariance 矩阵与公式相对差约0.478%/0.289%。互斥控制也验证 Poisson cross=0、fixed N cross<0。

### 同一事件的不同粗投影可细化观测

对同一 point angle，把 photon 分别以 fixed β_ref=.08/.10 校正，只使能量乘已知 factor1.0180442。同一光子在两 histogram 中的 joint-bin 概率来自原能量区间的交集，cross covariance 不为零。两种 monotone 映射和同一样本已知时，结合 cumulative counts 可恢复两套边界的联合细分；这能取回单个粗投影丢失的分辨信息，但没有增加 raw events。

此例两投影在共同原能量 ROI 内各29 bins，边界联合为57 bins。每组同一10000光子的局部 τ/E0 标准误差为：

| 观测/计算方式 | τ SE / fs | E0 SE / keV |
|---|---:|---:|
| 单独投影A | 0.834595 | 0.085657 |
| 单独投影B | 0.832294 | 0.084319 |
| 联合细分边界的一份观测 | 0.825051 | 0.079154 |
| 错当A/B完全独立，直接加Fisher信息 | 0.589322 | 0.060090 |

精确 bin 概率与 Fisher refinement 控制验证联合细分的信息不少于任何单个投影；本例的独立加法则过高。同样的 Poisson 总数被两次显示时，总数差 variance 为0，和的 variance 为40000，而独立近似给20000。正确 covariance、零方向和极限检查通过。

这些是已知 transport/response/feeding 的局部设计，不是实际 τ 区间。若 raw events 本来完整保留，确定性 replay 不增加它们包含的信息；若只剩粗 summaries，额外投影可能改善 summaries 的分区。事件 ID、共同样本/ROI、校正映射与门定义应保留，独立 detector 或 line 标签也不能替代 acquisition 谱系核对。

## 非线性 τ/E 区域：有限计数、边界与不可识别极限

BC84-1/5/9 区分点估计、区间和有限样本性质；以下 nonlinear-count closure 为本任务分析，[代码](../../system/scripts/day13_nonlinear_interval_closure.py)没有重标 ZA23/CI20/CM21 的置信定义。它采用已声明的指数 proper-time/线性β history 核，这次设**无馈入**，Gaussian σ2keV和三 point angles严格已知；各角度固定入选数，固定5-keV bins和 ROI，不包含源实验 nuisance。

Likelihood 为各组 conditional multinomial。拟合 (lnτ,E0)，自设 τ domain20–250fs、E0 shift±8keV；20fs下界只是数值模型的边界控制，不是物理最小寿命或 source prior。联合 region 的统计量是 `q=2[log L(hatτ,hatE)−log L(τ_true,E_true)]`，不是 τ轴的投影/一参数 profile。

Regular、可识别、真值在 domain 内部的二维局部 Gaussian 极限才给 χ²2。若真值位于一个光滑 lower-bound、另一方向可自由变化，whitened score 在半平面的投影给 `0.5 χ²1+0.5 χ²2`。无减速时 shape 不依赖 τ，只有 E 可识别，则相应 regular energy 极限为 χ²1；任意数值τ输出都没有寿命意义。

以 χ²2 的 68.3%/95% 阈值2.297707/5.991465比较，每场景2000独立计数实验：

| 自设场景 | 每角度入选数 | 68.3%二维阈值的实测覆盖 | 95%二维阈值的实测覆盖 |
|---|---:|---:|---:|
| 内部真τ70fs | 25 | 0.6760 | 0.9390 |
| 内部真τ70fs | 1000 | 0.6950 | 0.9530 |
| 真τ20fs在自设下界 | 25 | 0.7995 | 0.9755 |
| 真τ20fs在自设下界 | 1000 | 0.7810 | 0.9735 |
| 无减速，τ不可识别 | 1000 | 0.8610 | 0.9860 |

下界局部 mixture 在这两个阈值的概率为0.776717/0.967812；无减速的一维概率为0.870435/0.985625。覆盖的 MC standard errors 已保存在回执，68.3%列约0.0077–0.0105；有限计数的偏离须连同 MC 误差评估，不宣称普遍精确的 χ² calibration。内部场景增加统计量的结果与 regular 模型相容，不能把相容当作 source 的全部 nuisance 已验证。

每次拟合使用两起点，动态场景再用 coarse τ/E bank 核 minimum；无减速只检验 energy fit 和寿命梯度为零。个别 optimizer 起点失败保留：下界1000计数场景有18/21次两个起点分别失败，其中11次用 Powell 恢复。所有计数实验最终有可核结果，没有按失败状态剔除 experiment，也不称所有起点成功。

解析 τ/E gradient 与有限差分最大差2.4×10⁻9，和既有无馈入核的 bin probability 差1.7×10⁻16，128/256 quadrature差2.2×10⁻14；无减速 τ独立检查通过。各场景计数数组用 seed131431、顺序/shape/dtype/hash可再生；拟合本身不消耗随机数。

这一结果支持把拟合 domain、可识别性、joint/profile定义、完整 nuisance 和 finite-count closure 一起保存。它未测试真实 feeding/背景/模板统计或执行版本，局部 covariance 或某个“68.3%”标签均不能单独证明实际 τ 区间覆盖率。

## 速度 nuisance：正确统计量仍须正确的 forward model

[[baker-cousins-1984-histogram-fits]] BC84-1/5/9 给出统计方法背景，ZA23-2 与 CM21-15/16/22 提供入口重建、晚速度校准的来源语境。以下[分析](../../system/scripts/day13_velocity_nuisance_interval.py)延续无馈入 τ70fs/E0=2396.1keV 的合成核，不测 source 的 β误差或 τ偏差。

生成 β_in=.126、exit reference=.08，拟合时错误固定 β_in=.125；其余时间 history、point angles、5-keV bin、Gaussian corrected σ2keV 已知。在期望数据上，错模型的 pseudo-true τ≈71.426680fs、E0 shift≈−2.013528keV。它主要偏移 E0，并不以这个值解释实际20O的150/70fs差异。

另一模型把入口 β作为一个**全局 nuisance**，并加一份独立、无偏的 Gaussian observation `Yβ~N(β_in,σβ²)`，自设σβ=.001。Likelihood 同时含 γ conditional counts 和 `(Yβ−β_in)²/(2σβ²)`；它不是每事件速度重建，不是从相同γ计算的 getter，也没有使用 source 的 tuning 幅度作为σβ。True τ/E region 的比较在两端都 profile 掉该 nuisance。

每场景2000实验，用二维68.3%/95%阈值：

| 模型 | 每角度入选数 | τ/E 联合真值覆盖，68.3%阈值 | τ/E 联合真值覆盖，95%阈值 |
|---|---:|---:|---:|
| 错误固定入口β | 25 | 0.1290 | 0.3830 |
| 错误固定入口β | 1000 | 0/2000 | 0/2000 |
| 入口β nuisance +独立观测 | 25 | 0.6885 | 0.9485 |
| 入口β nuisance +独立观测 | 1000 | 0.7020 | 0.9565 |

0/2000不证明真实 coverage 为零；该 MC fraction 的95%双侧精确二项区间上界约0.001843。其余 MC intervals 也由下面的同数据审核保存。正确模型下的观察值与标称概率在 MC 误差尺度上相容，不能以此验证 source 的真实模型、velocity calibration 或所有 nuisance。

三参数概率与固定β版本一致，analytic gradient/finite differences 最大差2.1×10⁻9，128/256 quadrature差1.9×10⁻14，profile Fisher 的 Schur block 与完整 covariance 一致。Counts 和独立 β观测都有 seed/hash；失败起点保留并恢复，不丢 experiment。自设1000计数/角度的联合局部β SE≈.000299 是 γ+tag 的模型信息，不是实际探测器分辨率。

### 联合真值、τ profile 与联合区域投影

[同数据审核](../../system/scripts/day13_velocity_region_semantics.py)重建以上计数/β观测，核对 hash，并计算一参数τ profile与二维 joint region 在τ轴的投影。它没有增加独立模拟证据。

令 qτ 在固定τ真值处 profile E及速度 nuisance，qpair 固定τ/E真值而只 profile velocity。qτ≤qpair。名义68.3%的一参数阈值为1.001284，二维阈值2.297707；投影二维 region 的τ coverage 用后一个阈值作用于 qτ。

| 同一组实验 | 每角度数 | τ/E pair覆盖 | 一参数τ profile覆盖 | 二维region的τ投影覆盖 |
|---|---:|---:|---:|---:|
| 错误固定β | 25 | 0.1290 | 0.6815 | 0.8720 |
| 错误固定β | 1000 | 0/2000 | 0.4820 | 0.6930 |
| 入口β nuisance +独立观测 | 25 | 0.6885 | 0.7030 | 0.8780 |
| 入口β nuisance +独立观测 | 1000 | 0.7020 | 0.6805 | 0.8710 |

低计数下 E0偏移已让 joint pair覆盖下降，τ轴却仍可相容；高计数下本例τ profile也受错设影响。不能把 joint pair的失败直接写成同数值的τ interval失败，或把投影概率当一参数标称概率。所有数据身份和 original joint results 重放一致，qτ不超过qpair的逐实验控制通过；精确二项 MC区间仅描述模拟比例，不是核寿命区间。

独立 tag若有偏、与 γ calibration共享误差，或测的是 exit/after-DC 而非该 β_in，就需要另一 joint model。此例的正确 closure只在声明的 transport/response/无馈入 family内成立；source的实际 caller、velocity stage、model alternatives和Σ仍不可由窄 region证明。

## 长寿命校准线：有限 history 与估计量选择

CM21-15/16/22（正式PDF pp.6–7/Fig.9）用 known long-lived γ nominal energies 调整 **after-target** velocity/T，报告 oxygen/carbon tuning幅度0.4%/0.7%；它们不是入口速度误差或σβ，原文这段没有给本任务的整线均值/density mode算法。Source Fig.9 和本文例题不能相互代替。

[条件练习](../../system/scripts/day13_long_control_velocity_estimator.py)借用1375.80keV/τ1.27ps与3853.170keV/τ12.4ps两个 control尺度；自设 proper crossing .13ps、β从.10线性到.09、无馈入、各向同性rest photons、point angles和 **lab** Gaussian σ1keV。Crossing数值/trajectory不是 source实测或实际LISE/DC模型。τ≫crossing时仍可能有少量靶内发射，比例与已声明 history/selection有关。

在150°，两个 control的 pre-photon靶内 fraction≈9.730%/1.043%，角beaming条件后的 fraction≈9.650%/1.034%。如果分别取整条线第一矩和 density最大位置，再错以“全在晚速度发射”的单速关系反演：

| 自设control尺度 | exit reference后的整线mean残差 / keV | density mode残差 / keV | mean给的 apparentβ | mode给的 apparentβ |
|---|---:|---:|---:|---:|
| 1375.80keV /1.27ps | −0.600972 | −0.009845 | .090488588 | .090008003 |
| 3853.170keV /12.4ps | −0.177573 | −0.000356 | .090051542 | .090000103 |

True lateβ为.09；正确的有限history mean模型恢复它，但使用了已声明的 trajectory和control τ。整线mean、mode和实际Gaussian/多成分拟合peakcenter是不同估计量，ROI/背景/response可改变它们。不可从图示峰心自动挑选上表哪一列适用，也不以本例解释 source的0.4%/0.7%调整。

自设2396.1keV photon真的在β=.09晚发射时，使用第一control的 apparent mean/mode β作reference，在150°分别给+1.04711/+0.017146keV误差；第二control给+.110429/+.000222keV。这些是同一假定速度的reference敏感性，不是20O能量校准偏差或实际τ重拟合。

两个control各700k独立proper-time/noise事件验证mean；128/256 quadrature差4.6×10⁻13keV，finite-history inversion、longτ和equal-speed极限通过。Mode从bounded optimizer后用analytic density score root细化并核粗网格，避免大绝对能量的相对容差掩盖小mode shift；初估与细化值均保留。

必要 packet包括control身份/τ及不确定度、外部 E0 anchors及共有Σ、拟合objective/窗口/背景/response、velocity stage、DC/material模型与held-out controls。晚速度控制可支持该reference，却不自动测得入口/depth history；如果实际pipeline已建入有限history，则不能套用本例的late-only错模型。

### 固定角度与母/子frame是这个例题的边界

[当前校准例题的适用性审核](../../system/scripts/day13_calibration_applicability_audit.py)复用本轮已验证的 displaced-vertex/photon-recoil关系，逐项隔离先前固定角度模型的遗漏；没有新增实验输入。CM21-15明确从targetcenter与firstinteraction构造γ方向，NP19-5/7要求标明物理对象/更新状态；下面数值不能代为评价其实际实现。

一个独立的**恒定晚母核β=.09、无停止**fixture取point planar detector R150mm、nominal150°。若仍从初始targetvertex构造方向：

| control尺度 | 无条件meanflight / mm | 错vertex的correctedmean残差 / keV | density mode残差 / keV |
|---|---:|---:|---:|
| 1375.80keV /1.27ps | .034406 | −.006580 | −.006580 |
| 3853.170keV /12.4ps | .335932 | −.178361 | −.174095 |

正确知道emissionvertex后，信号的精确反演回到E0。R、planar response、constantβ和τ是选择的，不是CM21的真实几何；此fixture不等于前述有限foil history，不能把两表残差相加成实际校准。它限定“mode对靶内小尾部不敏感”的解释：mode仍可受发射点位移影响。

另一个独立fixture是自由单γ衰变。给定母系rest photon Eγ和daughter massproxy Mf，`Mi=Eγ+sqrt(Mf²+Eγ²)`；daughterframe photon为 `(Mi/Mf) Eγ`。以A19/1375.80keV和A13/3853.170keV的mass-number proxy，daughterframe相对parentframe分别高约.106953/1.226258keV。源nucleus的精确mass、后续gamma/material/粒子history及实际reference对象没有取得，故它们不是source校正量。

96/128 geometry mean/mode差<2×10⁻13keV、已知vertex反演、static/far-detector与fourmomentum/frameinverse检查通过；这组dependent应用不作为新的独立证据。若直接把correctedenergy称作母系restenergy，必须匹配该母核发射瞬间的vector；选用exit/residue等另一个reference也可用于history分析，但forwardmodel必须预测相同observable。

实际packet因而还需first-IP/vertex/coordinate关系、位移可忽略的精度依据，及reference粒子/状态/epoch和gamma-recoil/material treatment。固定角度、无photonkick或无限长control的数学极限，各自只验证相应条件；source pipeline是否已处理这些效应仍unknown。
