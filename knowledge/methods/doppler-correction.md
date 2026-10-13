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

The thesis has an internal target label conflict: one S3 setup paragraph says `196Pt`, while Chapter 3 and the GOSIA Appendix D input state `194Pt` at `120.3 MeV` (DD-20261013-32S-25). Repeating the simplified model with `m_T=196u`, and excluding the candidate rings 20 and 24, gives:

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
