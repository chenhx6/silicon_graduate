---
type: research-note
title: "`132Sn` 两声子八极 quartet 的中子连续谱可行性边界"
aliases: [132Sn two-phonon octupole continuum boundary, 132Sn octupole doorway readiness]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [rosiak-2018-132sn-enhanced-octupole, ame2020-sn132-mass-curvature]
created_from: "2026-11-01 cross-mass experiment design continuation"
promotion_target: "cross-mass-phenomena-detector-beam-prospectus-20261101"
nuclei: [132sn, 131sn]
observables: [e3, excitation-energy, neutron-decay, gamma-neutron-coincidence, feeding, resonance-width]
methods: [safe-coulomb-excitation, radioactive-beam, neutron-array, gamma-array, invariant-mass, response-simulation]
tags: [132sn, two-phonon-octupole, continuum, neutron-threshold, experiment-design, l3-readiness]
---

# `132Sn` 两声子八极 quartet 的中子连续谱可行性边界

## Research Trigger

Rosiak et al. 直接测得 `132Sn` 的第一 `3−` 状态和 E3 强度，因此可以把两声子
八极搜索从纯理论问题推进到能量可行性检查。关键问题是：简谐 `3−⊗3−` doorway
是否仍位于束缚区，还是已经跨过中子分离阈值，必须转成粒子—γ符合与连续谱实验。

## Grounded Evidence

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SN2PH-1 | Rosiak primary reports `E(3−_1)=4351.9 keV` in `132Sn`. | experimental-fact | direct | [[rosiak-2018-132sn-enhanced-octupole]] `ROS18-1` | true |
| SN2PH-2 | AME2020 gives mass excesses `ME(131Sn)=-77264.579 keV`, neutron mass excess `ME(n)=8071.31806 keV` and `ME(132Sn)=-76546.554 keV`. | evaluated-mass | direct | [[ame2020-sn132-mass-curvature]] `AME20-131SN-1`, `AME20-N-1`, `AME20-132SN-1` | true |
| SN2PH-3 | Using `S_n(132Sn)=ME(131Sn)+ME(n)-ME(132Sn)`, the derived one-neutron separation energy is `7353.293 keV`; treating the three tabulated uncertainties as independent gives a conditional `±4.125 keV`, while the full AME covariance is not used. | derived-mass | derived | AME2020 values in `SN2PH-2`; formula stated in this note | true |
| SN2PH-4 | The harmonic two-phonon energy scale is `2E(3−)=8703.8 keV`, about `1350.507 keV` above the derived one-neutron threshold; the uncertainty is dominated by the one-phonon energy and mass evaluation, not a measured resonance width. | experiment-design-inference | derived | `SN2PH-1` and `SN2PH-3` | true |
| SN2PH-5 | If a doorway at the central harmonic scale decays directly to the `131Sn` ground state, a nonrelativistic two-body estimate gives `E_n≈1340.28 keV` and daughter recoil `E_R≈10.23 keV` in the parent rest frame; this is a scale for response design, not a predicted resonance energy or branching ratio. | experiment-design-inference | derived | `SN2PH-4` and the two-body kinematic relation stated below | true |

## Provisional Reasoning

The threshold comparison does not prove that a physical quartet exists, nor does it prove
that every member must be unbound. It changes the default experiment design: a naive
bound-state γγγ search at `2E(3−)` is incomplete. If a two-phonon doorway survives with
anharmonic shifts smaller than roughly `1.35 MeV`, it is expected to couple to neutron
decay and possibly appear as a broad resonance or fragmented particle–hole strength.

The strong hypothesis is therefore:

> `132Sn` retains a recognizable two-octupole doorway above `S_n`, whose spin-dependent
> neutron decay and residual γ branches can be measured in coincidence.

The weaker alternative is quasiparticle/continuum fragmentation with no identifiable
four-member pattern. Both alternatives are experimentally useful if the response and
neutron efficiency are known.

## Assumptions

- The Rosiak `3−_1` state is the relevant one-phonon doorway for the harmonic estimate.
- The harmonic estimate is only a scale; anharmonic shifts, coupling to `2p2h` states and
  continuum self-energy can move or fragment the candidates.
- AME mass excesses are used for a central threshold calculation; no full correlated
  uncertainty on the derived `S_n` is claimed.
- A neutron-unbound state can still have an observable γ branch if electromagnetic decay,
  angular momentum barriers and detector acceptance make the branching measurable.

## Competing Explanations

1. A coherent two-phonon doorway survives but is broadened by neutron emission.
2. The apparent strength is distributed over quasiparticle/particle–hole states and no
   quartet identity remains.
3. A low-lying candidate is a different cross-shell configuration that happens to lie
   near `2E(3−)`.
4. Missing γ strength is caused by detector threshold, neutron coincidence loss, feeding
   or beam contaminants rather than nuclear fragmentation.

## Experiment Design

The experiment should combine a `132Sn` radioactive beam, a high-efficiency γ array and
an efficient neutron detector:

- retain the Rosiak HIE-ISOLDE/MINIBALL logic as the one-phonon response benchmark;
- use a particle detector for scattered beam/recoil kinematics;
- add a moderated or fast neutron array with calibrated energy-dependent efficiency;
- record γ–neutron–particle timestamps and preserve unobserved/threshold windows;
- search for both direct population of states near `2E(3−)` and neutron-decay daughter
  states that tag the parent resonance.

The target observable is a joint resonance/feeding model, not a γ-only level placement.
The first feasibility calculation must scan neutron energy, angular momentum barrier,
state width, γ branching, beam purity and array efficiency.

For the central excess in `SN2PH-4`, a direct decay to the `131Sn` ground state would
have `E_rel≈1350.507 keV`. In the parent rest frame, the two-body estimate
`E_n=E_rel M_d/(M_d+m_n)` gives `E_n≈1340.28 keV`, while
`E_R=E_rel m_n/(M_d+m_n)` gives `E_R≈10.23 keV` for `M_d≈131m_n`.
This estimate applies only to that decay branch and central energy. Decay to an excited
daughter, anharmonic shifts, recoil corrections and continuum coupling change the
available energy. It nevertheless gives a concrete first response window: the neutron
subsystem should be calibrated through roughly the sub-MeV to few-MeV region, rather than
being selected solely from a high-energy multi-neutron specification.

### Daughter-state response windows

The central doorway scale can be split further using the adopted low-lying `131Sn`
levels. The `0.0-keV` ground state and `331.73(10)-keV` `(1/2+)` state are evaluated
levels (`ENSDF131SN-2`, `ENSDF131SN-4`); the `1654.53(8)-keV` `(5/2+)` state is a
separate evaluated level (`ENSDF131SN-5`). Applying
`E_rel = 2E(3−) − S_n − E_x(daughter)` and the same nonrelativistic two-body
partition used above gives the following conditional central windows:

| `131Sn` daughter | `E_x` (keV) | `E_rel` (keV) | `E_n` (keV) | response consequence |
|---|---:|---:|---:|---|
| ground state `(3/2+)` | 0.00 | 1350.51 | 1340.28 | primary neutron calibration/TOF window |
| `(1/2+)` level | 331.73(10) | 1018.78 | 1011.06 | second neutron window with a distinct γ tag |
| `(5/2+)` level | 1654.53(8) | −304.02 | closed at the central harmonic scale | only opens after a positive doorway shift or a different parent energy |

Here `E_n≈E_rel×131/132` and the recoil is `E_rel/132`; the table is a
response-design calculation, not a prediction of decay branching or resonance
centroids. The unresolved `131Sn` `(11/2−)` isomer is deliberately excluded because
the adopted evaluation leaves its absolute excitation as `0.0+X`
(`ENSDF131SN-3`). The first neutron-wall calibration should therefore span both
approximately `1.01` and `1.34 MeV` windows and retain separate daughter-γ tags.
Treating the `1.65-MeV` daughter as an available branch without an energy shift would
create a false response channel.

### Anharmonic-shift scan

Let `δ` be the shift of a candidate doorway relative to the central harmonic scale
`2E(3−)`, with positive `δ` meaning a higher parent excitation. For each evaluated
daughter state,

`E_rel(δ) = 2E(3−) + δ − S_n(132Sn) − E_x(131Sn)`.

Using the same two-body partition as above, the channel-opening conditions are:

| `131Sn` daughter | channel opens when | central `E_n` at `δ=0` | design meaning |
|---|---:|---:|---|
| ground `(3/2+)` | `δ > −1350.507 keV` | remains open across a broad downward shift |
| `331.73-keV (1/2+)` | `δ > −1018.777 keV` | second low-energy tag remains open for most plausible shifts |
| `1654.53-keV (5/2+)` | `δ > +304.023 keV` | high daughter tag discriminates an upward shift or a different doorway |

Representative response points are: at `δ=−500 keV`, the ground and 331.73-keV
channels have neutron energies of approximately `844` and `515 keV`; at `δ=0`,
approximately `1340` and `1011 keV`; and at `δ=+500 keV`, approximately `1836`,
`1507` and `194 keV`, respectively. These are kinematic response-design values,
not resonance centroids, widths or branching predictions. The scan implies that a
neutron wall covering only the central `1.0–1.4 MeV` region could miss the
high-daughter discriminator if the doorway is shifted upward, while a response
contract spanning roughly `0.2–2.4 MeV` is a more robust first feasibility envelope.
The upper envelope is a design choice for calibration coverage, not a claim about
the physical resonance spectrum.

### Conditional partial-wave discriminator

The candidate two-octupole doorway has positive parity. The evaluated `131Sn` ground,
331.73-keV and 1654.53-keV daughter states are also positive parity, so neutron decay
to these states requires even orbital angular momentum `l`. The detailed parent spin
and spectroscopic factors are unknown, but angular-momentum coupling gives a useful
conditional discriminator: a `0+` doorway can connect to the `131Sn(1/2+)` state with
an `s`-wave neutron, whereas its connections to the `3/2+` ground and `5/2+` state
require at least a `d`-wave neutron. For higher-spin doorway members, more partial
waves are allowed and this simple ordering must be replaced by a coupled-channel
calculation.

As an engineering scale only, taking `R=1.2(131^(1/3)+1) fm≈7.29 fm` and the
neutron reduced-mass coefficient `ħ²/(2μ)≈20.9 MeV fm²` gives a surface centrifugal
scale `l(l+1)ħ²/(2μR²)≈2.36 MeV` for `l=2`. This number is not a neutron
penetrability or a width prediction: optical-potential, finite-range, spectroscopic
factor and resonance-energy inputs are missing. It does imply that the
331.73-keV daughter tag should be retained as a high-priority low-energy
partial-wave discriminator, while a null or weak branch cannot by itself reject the
doorway without those missing structure inputs.

## Response Contract

The minimum event record is

$$
D=(D_{\mathrm{beam}},D_{\mathrm{part}},D_{\gamma},D_n,D_{\mathrm{time}}).
$$

- `D_beam`: incoming isotope, focal-plane position, TOF, rigidity setting and beam
  contaminant probabilities;
- `D_part`: DSSSD/particle angle, energy loss, recoil or scattered-particle identity and
  target energy-loss correction;
- `D_gamma`: calibrated energy, Doppler angle, HPGe/clover segment, BGO veto and
  gamma-gamma gates;
- `D_n`: neutron flight time, position, multiplicity, pulse-shape/threshold class and
  energy-dependent efficiency;
- `D_time`: common timestamp, trigger/live-time, random windows and detector deadtime.

The forward model must include a response matrix
`R(E_n,theta_n,multiplicity | geometry,threshold,TOF)` and a separate gamma response
`G(E_gamma,theta_gamma | Doppler,efficiency,BGO)`. Gamma–neutron cross-talk, beam-decay
background, target-scattered neutrons, random coincidences and unobserved feeding need
explicit templates. A single nominal neutron efficiency cannot substitute for this
contract.

The first likelihood should be a joint count/TOF likelihood for signal, sideband and
random windows. A resonance hypothesis may be parameterized by centroid, width,
spin-dependent branching and residual gamma decay; a fragmentation hypothesis should
allow several doorway components with a shared response but independent feeding. The
analysis must profile beam purity, neutron efficiency, gamma efficiency, target loss,
deadtime and cross-talk nuisance parameters before comparing the hypotheses.

## Calibration and Go/No-Go

Required calibration blocks are:

1. monoenergetic or well-characterized neutron efficiency/TOF points across the expected
   energy range;
2. gamma source and in-beam efficiency points near the `3−` and candidate doorway
   energies;
3. beam-only, target-only, empty-target and no-neutron-control runs;
4. prompt/random timing windows and gamma-neutron cross-talk characterization;
5. a neighboring reaction channel with known particle/γ topology.

Go to a candidate-L4 analysis only when the response matrices, calibrations, background
templates and a negative control are present. If the neutron response is missing, stop at
the threshold/readiness design even if a γ excess is visible.

## Falsification or Reverse Tests

- If no excess survives in particle–γ–neutron data after response-folded background
  subtraction, set a sensitivity limit on coherent two-phonon doorway strength.
- If excesses appear but fragment across many states with no common E3/feeding pattern,
  reject the pure quartet and favor continuum mixing.
- If a four-state pattern is found below threshold after a large anharmonic shift, revise
  the continuum assumption and return to a bound-state γγγ analysis.
- If the result depends on an unmeasured neutron efficiency or missing beam contaminant,
  stop at readiness and do not claim nuclear falsification.

## Transfer Conditions

The threshold-first design transfers to other two-phonon searches when a one-phonon energy,
separation threshold, particle-decay channel and detector response are known. The
`1.35 MeV` difference is specific to `132Sn` and is not a universal quartet criterion.

## Failure Conditions

Stop before beam time if the `132Sn` rate, neutron efficiency, target survival, or
particle–γ–neutron response cannot be calibrated. Stop before L4 if the proposed
two-phonon energy region is above threshold but the experiment has no neutron observable.

## Open Questions

- What are the predicted spin-dependent energies and widths of the four coupled
  `3−⊗3−` doorway states after continuum self-energy?
- Can HIE-ISOLDE/Miniball-like γ efficiency be combined with a neutron array at the
  required target geometry?
- Which daughter states provide the cleanest neutron-decay tag?
- Does a modern shell-model/MCSM/QRPA calculation predict a coherent E3 sum or fragmented
  strength above `S_n`?

## Knowledge Impact and Learning Decision

`supports`: the `132Sn` route is scientifically attractive and can be designed around a
direct one-phonon E3 benchmark.

`revises`: the default target is a neutron-unbound continuum doorway, not a conventional
bound quartet γ cascade.

`limits`: this is a central-energy feasibility inference. It is not a measured resonance,
width, branching ratio or completed reaction-rate calculation.

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-01 | threshold-first `132Sn` prospectus audit | bound-quartet candidate | provisional continuum-readiness | `2E(3−)=8.7038 MeV` exceeds derived `S_n=7.3533 MeV` by about `1.35 MeV` | [[cross-mass-phenomena-detector-beam-prospectus-20261101]] |

## Human Review

This note is a Codex self-audit and remains `unreviewed`. The threshold arithmetic is
reproducible from the cited source rows, while the resonance/doorway interpretation and
detector design are provisional research inferences.
