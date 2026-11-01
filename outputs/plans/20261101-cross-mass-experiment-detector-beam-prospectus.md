---
type: plan
title: "跨质量区现象与 IMP-DRAGON/RIBLL 实验、探测器设计初稿"
created: 2026-11-01
updated: 2026-11-01
status: draft
---

# 跨质量区现象与 IMP-DRAGON/RIBLL 实验、探测器设计初稿

## Objective

把五个候选问题推进到可以计算反应率、模拟响应并形成束流申请的状态：

1. `131Xe` 794-keV parity / 882-keV branch ambiguity；
2. `131Ba/133Ce` direct-E3 versus E1-mixing question；
3. `78Br` octupole–chiral quartet search with a RIBLL-type beam line。
4. `132Sn` two-phonon octupole quartet in the N=82 region；
5. `135/137Pr` MR/AMR absolute-strength closure。

## Phase 1: source and feasibility closure

- 回读 `li-2025-imp-dragon-hpge-array`、`sun-2003-ribll-radioactive-ion-beam-line` 及
  HIRFL Gamma Ball/DAQ 学位论文；
- 对每个候选冻结 target, beam, reaction family, state identity, observable and
  control-line ledger；
- 标注现有数据谱系，不把旧 acquisition 的重分析当独立 sensitivity；
- 对 `78Br` 先确认 production route、half-life、purity and stopping/target mode。
- 把 Yue 2010、Yan 2015 和 Wu 2020 的效率差异、PID、pile-up、DAQ 吞吐和快定时
  经验转成 detector response checklist。

## Phase 2: response and rate model

Build a minimal reproducible model with:

- reaction-channel scan rather than one guessed cross section;
- Geant4 detector geometry for HPGe/BGO/clover/LaBr3/Si/electron modules;
- Doppler, finite solid angle, BGO veto, Compton polarization, electron transport and
  deadtime;
- background templates, random windows, feeding and calibration covariance;
- expected signal, control and null channels.

Acceptance criteria: all observables have units, source identity, response mapping and
an uncertainty owner; no synthetic count is reported as an experimental fact.

Historical-thesis acceptance criteria: every nominal efficiency has a measured/calibrated
counterpart, every PID decision has a negative control, and every fast-timing claim has a
rate/pile-up and waveform-quality boundary.

## Phase 3: proposal packages

### Package A: `131Xe`

Lead with `130Te(α,3n)131Xe` as a known channel family. Request a focused campaign for
794/880/882 keV, selected control lines, conversion-electron/γ ratio, clover polarization
and at least one partner-resolved lifetime. Use `813` as holdout and `450` as sensitivity
line only after transition identity is frozen.

### Package B: `131Ba/133Ce`

Use the existing `122Sn(13C,4n)131Ba` source lineage as a feasibility anchor and optimize
the exact target channel for the chosen nucleus with an evaporation calculation. The
proposal must target direct E3/lifetime plus E1 network, not a static `β3` claim from a
single branch. Use the existing `549-keV` and `715/721-keV` M1/E2 links as same-run
controls, and treat a candidate `B(E3)≥10 W.u.` as a pre-registered sensitivity target,
not a current measurement.

### Package C: `78Br`

Start from the known `70Zn(12C,p3n)78Br` stable-beam channel and add DSAM/RDDS,
absolute branching and direct-E3 sensitivity to the existing E1-connected network. Keep
the RIBLL-type fragment-separator route as a follow-up only if a production calculation
shows a real advantage; do not request RIB time until yield, purity and stopping close.

### Package D: `132Sn`

Use RIBLL-II/CSR, FRIB or RIBF for Coulomb excitation, inelastic scattering or transfer.
Treat production, purity, particle acceptance, neutron efficiency and γ efficiency as the
critical feasibility gate. The central-energy check places the harmonic two-phonon scale
above `S_n`, so the proposal must test a neutron-unbound doorway with particle–γ–neutron
coincidences alongside a fragmented/damped alternative.

### Package E: `135/137Pr`

Use stable-beam fusion evaporation with recoil/particle tagging and RDDS/DSAM. Measure
absolute `B(M1)`, crossover `B(E2)` and alignment together, using `110Cd` as a method
benchmark without importing its configuration or response parameters.

## Phase 4: detector prototype

Prototype `DRAGON-X` as a modular array:

- compact HPGe+BGO core;
- selected clover polarization ring;
- LaBr3 fast timing layer;
- Si/CsI charged-particle or recoil tags;
- fast/moderated neutron module for above-threshold `132Sn` doorway searches;
- K-electron module where parity/ICC is central;
- PPAC/fiber/implantation position and unified list-mode DAQ.

The first prototype output is a response matrix and rate/deadtime budget, not a claim of
measured array performance.

## Stop and go criteria

- Go to candidate-L4 only when source identity, reaction/beam input, detector response,
  background, covariance and a negative control are available.
- Stop a route at L3/readiness when production yield, raw response, or an independent
  companion observable is missing.
- If a null result is sensitivity-limited, report the limit and its response contract;
  do not call it a physical falsification.

## Immediate next actions

1. Parse the full IMP-DRAGON and RIBLL PDFs into source-linked claims and verify lint.
2. Select one `131Xe` and one `131Ba/133Ce` reaction family for a rate-model pilot.
3. Search primary literature for `78Br` production and lifetime/decay observables.
4. Build a toy but explicitly labeled response budget for `DRAGON-X`.
5. After independent source checks, draft a one-page beam request with beam energy scan,
   target, detector configuration, calibration runs, expected observables and falsifiers.
