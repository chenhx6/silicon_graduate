---
type: project
title: "跨质量区未闭合现象、束流实验与探测器 prospectus"
aliases: [cross-mass phenomena prospectus, IMP-DRAGON RIBLL experiment design, detector-array research prospectus]
created: 2026-11-01
updated: 2026-11-01
status: active
review_status: unreviewed
project_stage: exploratory-l3-and-experiment-design
confidentiality: private
nuclei: [131xe, 131ba, 133ce, 78br, 132sn, 135pr, 137pr, 144ba, 146ba]
tags: [cross-mass, experiment-design, beam-proposal, imp-dragon, ribll, detector-array, l3, candidate-l4]
---

# 跨质量区未闭合现象、束流实验与探测器 prospectus

## Agent active summary

本页是 2026-11-01 Day29 continuation 形成的 L3 研究 prospectus。它把跨质量区
现象缺口、IMP-DRAGON/RIBLL 方法谱系、历史装置学位论文经验和 `DRAGON-X` 概念
阵列连接起来，服务于后续反应率/响应建模与束流申请。当前六条候选路线均保持
`unreviewed`/`provisional`；没有把理论预测、设计推断、装置额定值或缺失输入写成
实验事实，也没有推进 Day30 学分。

## Research Question

哪些核结构现象已经在其它质量区得到直接或较强证据，而在 A≈130 或某个明确特殊
质量区仍只有相对分支、模型参数或未闭合的竞争解释？能否用现有的
IMP-DRAGON、RIBLL/后续束流线和一个可重排的辅助探测器系统，把这些问题推进到
真正可申请束流、可执行分析和可证伪 belief revision？

本项目默认采用大胆假设、小心验证：先允许提出有创新性的跨区类比和新装置构想，
再用 primary source、反应运动学、response simulation、负对照和独立 holdout
检查它们。假设可以先进入 provisional L3；只有真实输入、可复现分析和失败检查
完成后才进入 candidate-L4。

## Current Hypotheses

- `H1`: `131Xe` 的 branch/parity ambiguity 可以由共同 response、偏振、转换电子和
  partner-resolved lifetime 联合闭合。
- `H2`: `131Ba/133Ce` 的 E1 网络可能对应 A≈130 的八极关联，但 direct E3 可能
  证实或推翻“强八极 analog”。
- `H3`: `78Br` 的 E1-connected parity network 仍值得用 RIB/高灵敏 γ 实验搜索 quartet
  companion observables。
- `H4`: `132Sn` 已有直接单声子 E3 benchmark；若两声子 quartet 仍保留相干多态
  网络，说明双幻核中可继续追踪八极玻色子；碎片化则说明阻尼和组态混合主导。
- `H5`: `135/137Pr` 的 MR/AMR 标签可能在绝对 lifetime 和 crossover E2 闭合后修订。

## Evidence Available

当前 evidence 来自 `knowledge/sources/` 的直接论文、装置原件、学位论文和明确标记
为 provisional 的理论研究笔记。装置页给 response/design constraints；核结构 source
页给 level、transition、lifetime、E1/E3 或 mixing-ratio 事实。project 只组织候选
和实验设计，不把模型参数、toy 结果或装置额定值当作目标核素实测。

## Thesis-Derived Engineering Lessons

三篇历史装置学位论文提供了比“探测器参数表”更重要的负面经验：

| Thesis lesson | Evidence | Design consequence |
|---|---|---|
| Gamma Ball 的模拟与实测全能峰效率可以相差很大，不能只报告 Geant4 名义效率 | [[yan-duo-2015-csr-coulomb-excitation-detector-system-thesis]] `DD-20260910-CSR-01`; [[yue-ke-2010-hirfl-csr-gamma-ball-csi-thesis]] `DD-20260910-CSI-02` | 每次 proposal 必须给 source/beam calibration、solid angle、trigger、threshold、add-back 和 measured-vs-simulated closure |
| `E–Range`、`ΔE–E`、TOF 和位置联合后，粒子鉴别才有机会在相近能量/同位素之间稳定 | [[yan-duo-2015-csr-coulomb-excitation-detector-system-thesis]] `DD-20260910-CSR-02`, `DD-20260910-CSR-03`; [[sun-2003-ribll-radioactive-ion-beam-line]] `RBL03-5` | DRAGON-X/RIB proposal 必须保存 event-level PID，而不是只保留选后 γ 谱 |
| 数字 DAQ 的事件头、波形、pile-up 分解、触发和 I/O 是物理响应的一部分 | [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] `DD-20260910-MT-010`, `DD-20260910-MT-014`, `DD-20260910-MT-017` | 新阵列要在设计阶段做 data-volume/deadtime/pile-up budget，并保留可重放波形或足够的诊断摘要 |
| 快定时和高分辨能谱应分开建模，再通过统一 timestamp/covariance 合并 | [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] `DD-20260910-MT-015`; [[li-2025-imp-dragon-hpge-array]] `ID25-5` | LaBr3、HPGe、BGO、Si/electron 各自有 response block，不能用一个“总效率”代表联合实验 |

## Detector Development Map

| Development line | Strength | What `DRAGON-X` should borrow |
|---|---|---|
| Segmented HPGe tracking: [[akkoyun-2012-agata-instrument-response]] | PSA, interaction-point reconstruction, tracking, Doppler correction and replayable response stages | retain raw traces/metadata, version PSA/tracking, quantify threshold and P/T tradeoffs |
| Particle-assisted tracking: [[assie-2021-mugast-agata-vamos]] | light-particle kinematics + AGATA direction + VAMOS heavy PID for two-body Doppler correction | couple event identity and emitter momentum to γ response; preserve three-system shared covariance |
| In-beam polarization and event geometry: [[longfellow-2026-gretina-energy-ordering-polarization]] | Lorentz angle transform, first-interaction Doppler correction, energy-dependent `Q(Eγ)` and Compton-plane response are separate objects | define `Q(Eγ,θ,ξ)`, alignment and recoil-vector nuisance; do not treat a clover asymmetry as a geometry-free number |
| Conversion-electron/polarization calibration: [[garnsworthy-2019-griffin-facility]] | PACES-compatible electron configuration, pair-specific cross-talk, finite-geometry angular response and polarization calibration | give electron transport and pairwise Compton response their own calibration blocks and covariance |
| Compact radioactive-beam γ setup: [[rosiak-2018-132sn-enhanced-octupole]] | MINIBALL + DSSSD + HIE-ISOLDE safely measures high-energy γ from a low-rate RIB | benchmark high-energy efficiency, particle angle and Doppler correction before adding new physics |
| Domestic high-efficiency modular HPGe: [[li-2025-imp-dragon-hpge-array]] | coaxial/clover HPGe, BGO suppression, polarization, LaBr3 hybrid and auxiliary Si/CsI | make detector geometry reconfigurable around the observable, not around a fixed array count |
| Large solid-angle scintillator method: [[yue-ke-2010-hirfl-csr-gamma-ball-csi-thesis]] | CsI(Tl)+APD Gamma Ball design, high efficiency and external-target kinematics | keep measured-vs-simulated efficiency closure and optical/packaging calibration |
| FPGA/list-mode DAQ: [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] | timestamps, waveforms, programmable trigger, pile-up handling and multi-detector synchronization | design data volume, deadtime and pile-up limits before claiming high-rate capability |

The international direction is moving toward tracking and particle-assisted Doppler
correction; the domestic direction offers compact high-efficiency HPGe/BGO, hybrid timing
and large-solid-angle scintillator systems. `DRAGON-X` should combine their response
contracts while keeping the ability to replay raw event information.

### Neutron-detector development relevant to `132Sn`

The neutron module should follow the low-energy spectroscopy direction of VANDLE/NEXT/NEDA,
not the high-energy NeuLAND geometry by default:

- [VANDLE](https://repository.lsu.edu/physics_astronomy_pubs/6248/) demonstrates modular plastic-scintillator time-of-flight detection, configurable
  geometry, GEANT4 response modeling and β/γ/neutron coincidence workflows.
- [NEXT](https://doi.org/10.1016/j.nima.2015.10.055) develops segmented thin plastic layers so the first interaction position and TOF
  are better constrained; its hybrid operation opposite a γ array is directly relevant
  to a neutron-unbound `132Sn` doorway.
- [NEDA](https://doi.org/10.1016/j.nima.2021.165658) shows how a neutron array can be integrated with AGATA-like γ spectroscopy for
  multiplicity and reaction-channel selection.
- [NeuLAND](https://doi.org/10.1016/j.nima.2011.10.021) provides the high-energy multi-neutron tracking design vocabulary; its
  geometry and energy range should not be copied blindly into a low-energy
  `132Sn` particle-decay experiment.

The practical `DRAGON-X` choice is a modular, segmented low-energy neutron wall with
configurable flight path, calibrated γ cross-talk rejection and event-level TOF/position
records. The neutron design must be optimized against the predicted decay energy and
target geometry, not selected from nominal efficiency alone.

## Evidence Anchors

| Cross-mass anchor | What is stronger elsewhere | A≈130 or target-region gap |
|---|---|---|
| `144Ba/146Ba` direct octupole | Direct Coulomb-excitation `B(E3)` measurements provide an E3-first benchmark (`BU16-1`; `BU17` source page) | `131Ba` has an evaluated weak `79.918-keV` E3 control (`ENSDF131BA-1/2`), but no strong high-spin E3/lifetime matrix; the Guo E1 network and tentative `β3` input remain separate (`GU20-10`, `GU20-14`, `GU20-16`) |
| `74Br` multi-observable chiral/wobbling | A same-configuration three-band experiment combines ADO, polarization, DSAM lifetimes and absolute strengths (`GU24-1`–`GU24-7`) | `131Xe` has detailed identity/mixing-ratio conflict but no partner-resolved lifetime or absolute EM matrix; its 2020/2023 data share one acquisition |
| `78Br` octupole–chiral quartet idea | E1 connectivity and octupole-correlation hypothesis are experimentally present, while a quartet remains a future search target (`L16-D27-R047-1`–`3`) | A≈130 analogs have coupled parity/band networks, but no direct E3 and no completed parity–chirality quartet closure |
| RIB experiments | RIBLL provides event-by-event beam identification, focal-plane diagnostics, secondary target and optional polarization/TOF modes (`RBL03-1`–`7`) | Rare exotic-state experiments need a combined beam/PID/γ response contract rather than γ spectra alone |
| `132Sn` two-phonon octupole | `208Pb` supplies a strong one-phonon E3 control, a `0+` candidate and a new quadrupole-coupling constraint, while its full quartet remains unclosed (`HE25-2`–`HE25-5`) | No direct `0^+,2^+,4^+,6^+` two-phonon octupole closure is recorded for `132Sn`; this is a high-risk RIB route |
| `110Cd` versus `135/137Pr` MR/AMR | `110Cd` supplies an absolute lifetime/`B(E2)` benchmark | A≈130 Pr candidates still rely heavily on relative strengths and need absolute crossover-E2/lifetime closure |

## Candidate Experiments

### A. `131Xe`: branch identity, parity version and absolute EM closure

**Bold hypothesis.** The 794-keV parity conflict and 882-keV double-root problem can be
resolved by one acquisition that measures the target line, its conversion-electron/γ
response and a partner-resolved lifetime/absolute branch in a common nuisance model. If
the large-`|δ|` and small-`|δ|` branches remain separated after response folding, the
experiment can decide whether the current low-spin structure is more consistent with a
signature partner, wobbling-like excitation or another configuration.

**Starting point.** Reuse the known `130Te(α,3n)131Xe` reaction family and the existing
INGA transition network (`BNK20-1`–`BNK20-6`), but do not treat a repeat of the old
acquisition as independent evidence. The new value comes from response and companion
observables: compact IMP-DRAGON HPGe+BGO, selected clover polarimeters, LaBr3 timing and
an electron/conversion subsystem.

**Minimum observables.**

- event-level 794/880/882 peak counts, sidebands, random windows and gate lineage;
- clover polarization or equivalent Compton response for the 882 branches;
- K-shell electron/γ ratio with calibrated electron transport for the 794-keV parity test;
- partner-resolved lifetime or absolute branch normalization, preferably for the same
  1046-keV parent;
- run-by-run energy, efficiency, deadtime, feeding/alignment and detector-pair covariance.

**Falsifier.** A branch is weakened only when its response-folded joint prediction set is
excluded by all core lines and the absolute EM holdout, with the conclusion stable under
alignment, feeding and calibration sensitivity. If the sets overlap, the experiment has
still produced a valuable readiness result: current observables cannot uniquely identify
the mode.

### B. `131Ba/133Ce`: A≈130 octupole analog of the direct-E3 region

**Bold hypothesis.** The E1 network in `131Ba` and the candidate triaxial/collective
structures around `133Ce` may be the odd-A, configuration-dependent continuation of the
strong octupole correlations seen in `144Ba/146Ba`, but a direct E3 measurement could
show that the analogy fails because E1 connectivity is produced by mixing rather than a
large static octupole matrix.

**Measurement.** Use a stable-beam fusion-evaporation campaign with a reaction channel
family around `122Sn(13C,4n)131Ba` or an optimized `A≈130` Ce channel, selected after
PACE/evaporation and beam-energy scans. This is a candidate family, not a frozen beam
request. IMP-DRAGON should run in compact HPGe+BGO mode with clover polarization and a
fast-timing subsystem; a recoil/charged-particle tag is required if the channel purity
does not close from γ gates alone.

**Beam-proposal discriminant.** Use the adopted `79.918-keV` E3 and its very small
`B(E3)=0.00087(3) W.u.` as a low-energy conversion-electron/γ response and negative
control (`ENSDF131BA-1/2`), then pre-register one high-spin direct-E3 sensitivity
target, such as `B(E3)≥10 W.u.`, as a design threshold only; it is not an existing
`131Ba` result. Use the known `549-keV` D6→D3 and `715/721-keV` D8→D7 M1/E2 links
as same-run efficiency, angular-distribution and feeding controls. The core request is
state-identity closure plus one lifetime and absolute E3 branch; clover polarization,
LaBr3 timing and electron detection are optional modules activated only if the PACE and
response pilot shows that they separate the remaining hypotheses.

Under the adopted complete-IT condition, `α=80.1` makes the control transition
electron dominated (`f_e≈98.8%`, `f_γ≈1.23%`, `ENSDF131BA-5`). This reverses the
usual assumption that the weak γ line alone is the convenient calibration anchor:
electron transport, threshold and coincidence losses must be measured before using
the control to constrain a high-spin E3 response.

**Minimum observables.**

- direct E3 candidate yields and at least one lifetime measurement;
- E1 links, branching fractions and conversion-electron/γ information;
- state-resolved parity and transition identity;
- a neighboring control channel with known E2/E1 response;
- a model-independent count/efficiency ledger before converting to `B(E3)` or `β3`.

**Falsifier.** If E1 links persist but direct E3 strength is weak after feeding and
branching corrections, the “A≈130 direct-octupole analog” hypothesis is falsified and
the result becomes a configuration-mixing/softness case. If E3 and E1 observables both
support a coherent matrix-element pattern, the result becomes a strong cross-mass
candidate while the static-shape label remains model dependent.

### C. `78Br`: absolute-strength test of an octupole–chiral quartet prediction

**Bold hypothesis.** The `78Br` E1-connected positive/negative band network can contain
the predicted parity–chirality coupling, but the present evidence may be insufficient
because the direct E3/absolute-strength and partner-resolved geometry observables were
not measured. The most efficient first test is a stable-beam repeat with lifetime and
absolute-strength capability; a RIBLL-type experiment is a higher-risk follow-up if the
stable-beam channel cannot populate the missing states.

**Starting point.** The existing `70Zn(12C,p3n)78Br` campaign already collected large
γγ and proton–γγ samples and established the E1-connected band network (`L16-1`,
`L16-14`). The new experiment should add DSAM/RDDS, absolute branching and direct E3
sensitivity rather than simply repeat the level-scheme statistics.

**Optional RIB route.** If a radioactive-beam production calculation is favorable, use a
RIBLL-type fragment-separator mode with F0 production, Br–ΔE–Br purification, F2/F4
TOF/ΔE diagnostics and a secondary target or implantation station. The 2003 RIBLL paper
proves the architecture and operating modes, not the current `78Br` yield. The proposal
must calculate production, purity, beam spot, stopping and rate before beam time.

**Detector concept.** Surround the secondary target with a compact HPGe/BGO array and
clover polarimeters; place Si/CsI particle detectors at forward angles and a fast
timing layer for isomer/feeding control. For a decay mode, add a position-sensitive
implantation detector and β/charged-particle veto. The event record must preserve incoming
beam identity, outgoing particle/implant position and γ coincidence time.

**Falsifier.** Missing E1/E3 links after a sensitivity-calibrated search, or a partner
band with incompatible parity/feeding, lowers the quartet hypothesis. A null result is
scientifically useful only if the efficiency, background and production limit are
reproducible.

### D. `132Sn`: two-phonon octupole quartet in the N=82 region

**Grounded update.** HIE-ISOLDE/MINIBALL has already measured the first `3^-_1` state
and a direct E3 strength in `132Sn` (`ROS18-1`/`ROS18-2`; [[rosiak-2018-132sn-enhanced-octupole]]).
The experiment is therefore
anchored to a real one-phonon observable rather than a theory-only starting point.
The central-energy audit in [[132sn-two-phonon-continuum-readiness-20261101]] places the
harmonic scale near `8.7038 MeV`, above the derived `S_n(132Sn)≈7.3533 MeV`; the first
proposal should therefore include neutron decay and continuum response rather than assume
a bound γ quartet. The 2025 `208Pb` Coulomb-excitation result is a useful control:
it leaves the full quartet unclosed and points to a possible `800–1500 keV`
quadrupole–octupole coupling scale, so the `132Sn` proposal must test a doorway and
its fragmentation rather than assume a clean harmonic multiplet
([[henderson-2025-208pb-deformation-collectivity]] `HE25-2`–`HE25-5`).

**Bold hypothesis.** The measured low-lying `3^-_1` vibration in doubly magic `132Sn`
can generate a recognizable `3^-⊗3^-` quartet near twice the one-phonon energy. The
strong form predicts four members and a partially coherent E3 decay network; the weaker
form predicts only a fragmented, damped two-phonon response.

**Beam-line concept.** Use RIBLL-II/CSR, FRIB or RIBF with Coulomb excitation,
inelastic scattering or transfer, adding a neutron array to the γ/particle system. The
present RIBLL1 paper supplies the architecture, not the required `132Sn` yield. The
proposal must calculate production, beam purity, target choice, recoil/scattered-particle
acceptance, neutron efficiency and γ efficiency before beam time.

**Minimum observables.**

- particle-tagged excitation and scattered-particle kinematics;
- `0^+,2^+,4^+,6^+` candidate energies and γγγ topology;
- E3-sensitive branching and lifetime/fast-timing information;
- feeding from higher states and an efficiency model for unobserved branches;
- a neighboring N=82 control nucleus to separate shell-specific damping from detector loss.

**Falsifier.** If four members cannot be found within the predicted energy scale, or the
E3 strength fragments beyond a declared closure threshold, the pure harmonic quartet is
rejected in favor of quasiparticle mixing/damping. A sensitivity-limited null result
must be reported as a limit, not a physical absence.

### E. `135/137Pr`: MR/AMR transition-strength closure

**Bold hypothesis.** The A≈130 Pr bands that currently look magnetic-rotation-like from
relative intensities may change classification once absolute lifetimes and weak
crossover E2 transitions are measured. The decisive observable is the joint evolution of
absolute `B(M1)`, `B(E2)` and alignment through the proposed crossing region.

**Measurement.** Use a high-statistics fusion-evaporation campaign with multi-angle
HPGe, recoil/evaporation-particle tagging and RDDS/DSAM. Use the `110Cd` lifetime and
absolute `B(E2)` case as a response/analysis benchmark, while retaining the Pr-specific
configuration and feeding model.

**Falsifier.** If the absolute strengths and crossover lines cannot be reproduced by the
same configuration and a common stopping/feeding contract, the MR/AMR label is downgraded
to a relative-intensity candidate. If a shared TAC/core-coupling model predicts and the
experiment measures the full absolute pattern, the A≈130 comparison becomes a stronger
cross-mass result.

### F. `133I`: quasi-continuum γSF low-energy enhancement

**Bold hypothesis.** The odd-A, near-`N=82` nucleus `133I` has a reproducible low-energy
γSF enhancement below about `2 MeV`, with a measurable dipole character that can be
tested against an `M1`-recoupling interpretation.

**Starting point.** A public 2026 OCL experiment record identifies
`130Te(α,pγ)133I` and a SiRi–OSCAR particle–γ γSF/NLD programme. The public record is
an experiment/access anchor; it does not close whether `133I` has LEE or whether the
enhancement is M1. The apparent NVA thesis-PDF probe is an HTML shell rather than a
readable manuscript (`[[uio-2026-133i-thesis-announcement]]` `UIO26-3`), so the
thesis-level result remains unavailable. [[133i-low-energy-gamma-strength-function-candidate-20261101]]

**Minimum observables.**

- γSF and NLD from two non-overlapping initial-excitation windows;
- a validated population contrast for those windows, using particle kinematics and
  an explicit spin-distribution model; two particle gates alone are not evidence for
  two independent spin populations;
- threshold, summing, discrete-line leakage and particle–γ random controls below
  `2 MeV`;
- a `3–4 MeV` response control and known E1/M1 reference transitions;
- γ angular distribution or Compton polarization for the low-energy excess;
- NLD, spin-population, unfolding, efficiency and non-statistical-feeding nuisance
  profiles plus an independent holdout.

**Falsifier.** A low-energy excess that disappears under response, threshold, unfolding
or feeding controls is a response/non-statistical candidate. An excess that survives but
has unresolved E1/M1 character remains an L3 γSF result. If the population contrast is
not independently closed, the two-window comparison cannot promote the magnetic
interpretation; only a stable dipole-character observable and holdout can do so.

## Proposed Detector: `DRAGON-X` Hybrid Response Array

`DRAGON-X` is a design concept, not an existing instrument. It is optimized for the
specific ambiguity where a γ spectrum alone cannot distinguish branch, configuration,
collective mode and feeding.

| Module | Proposed role | Design requirement |
|---|---|---|
| 12–16 coaxial HPGe + BGO | weak cascade and high-resolution level placement | compact high-efficiency geometry; retain BGO veto and event-level add-back |
| 4–8 clover HPGe | linear polarization and selected-angle angular distributions | place at calibrated 90°/forward/backward rings; preserve Compton scatter pairs |
| 4–8 LaBr3(Ce) | ps timing and fast coincidence | independent fast digitizer; do not mix its timing response with HPGe energy response |
| segmented Si / CsI(Tl) | charged-particle/recoil and beam-particle tagging | ΔE–E/TOF or recoil veto with position and threshold calibration |
| fast/moderated neutron array | continuum doorway and neutron-decay tagging for `132Sn` | energy-dependent efficiency, TOF, gamma-neutron cross-talk veto and calibrated thresholds |
| compact electron detector | K-shell conversion-electron/γ ratio | magnetic/electrostatic transport map, threshold scan, random/accidental control |
| PPAC/fiber/implantation layer | incoming/outgoing beam identity or decay position | timestamped position and rate monitoring |
| unified list-mode DAQ | joint covariance and post-hoc gate replay | 100/500-MHz paths, FPGA timing, deadtime/livetime records and waveform sampling for fast channels |

The design borrows verified component ideas from IMP-DRAGON and the HIRFL thesis
lineage, but its combined performance is not yet measured. For the `132Sn` continuum
route, the neutron module is a required physics subsystem rather than an optional
upgrade: without its efficiency and cross-talk response, an above-threshold γ excess
cannot be separated from background or beam contamination. The first engineering
milestone is a Geant4 + digitizer response prototype with geometry, thresholds,
background templates, deadtime and calibration covariance. A design should be rejected
if it improves nominal efficiency while losing the raw observables needed to separate
branch and feeding hypotheses.

### `DRAGON-X` operating modes and response closure

`DRAGON-X` should be treated as three switchable, separately calibrated configurations,
rather than one instrument whose nominal module list is assumed to operate optimally for
every question:

1. **High-resolution/polarization mode:** HPGe/BGO plus calibrated clover or tracked
   Compton pairs for `131Xe` parity/branch and `135Pr` mixing-ratio tests. The response
   package must retain first-interaction geometry, `Q(Eγ,θ,ξ)`, alignment nuisance,
   pair-specific cross-talk and random/sideband windows.
2. **Particle-assisted Doppler mode:** segmented Si/light-particle kinematics, recoil
   PID and γ interaction-point reconstruction for fusion-evaporation and transfer
   channels. The response must include the event-level recoil vector, vertex/target
   depth, stopping history, PID confusion and shared covariance.
3. **RIB–neutron–decay mode:** beam identity, particle tag, low-energy neutron wall,
   γ array and (when required) implantation/decay layer for `132Sn` or isomer routes.
   The response must include `ε_n(E_n,θ,multiplicity)`, γ–n cross-talk, threshold scans,
   beam-only/empty-target controls, implant–decay correlation and deadtime.

The minimum cross-mode ledger therefore contains five response blocks: γ tracking and
polarization, recoil/vertex, particle PID, neutron or electron transport, and the
joint trigger/livetime covariance. A high nominal HPGe efficiency cannot compensate for
an absent block when the scientific claim depends on a branch, a feeding path or a
rare coincidence.

## Beam-Application Structure

A future beam request should contain:

1. **Physics case:** one bold hypothesis and one explicit alternative.
2. **Observable contract:** target lines, control lines, lifetime/polarization/E3 companion
   observables and the event identity needed for each.
3. **Reaction and beam scan:** candidate reaction family, energy scan, target thickness,
   expected channel competition and a rate range; no single yield without a production
   calculation.
4. **Detector response:** geometry, efficiency, resolution, Compton/electron response,
   timing, particle PID and covariance products.
5. **Analysis and falsifier:** count-level likelihood, nuisance profile, holdout line,
   negative controls, expected failure modes and belief-revision table.
6. **Feasibility gates:** beam time estimate, calibration runs, target survivability,
   radiation/safety, data volume and a stop rule if the key companion observable is not
   measurable.

## Current Decision

- Priority 1: `131Xe` because the object identity and branch design are already mature and
  can produce a focused response/lifetime proposal.
- Priority 2: `131Ba/133Ce` direct-E3 analog because it connects a strong cross-mass
  phenomenon to a concrete A≈130 evidence gap.
- Priority 3: `135/137Pr` MR/AMR absolute-strength closure because stable-beam access is
  more practical than a new RIB campaign and the missing observable is sharply defined.
- Priority 4: `78Br` absolute-strength/quartet test; begin with the known stable-beam
  channel and keep RIBLL as a production-risk follow-up.
- Priority 5: `132Sn` two-phonon octupole quartet because its scientific payoff is high but
  production, purity and particle–γ efficiency are the dominant risks.
- Priority 6: `133I` γSF/LEE because the stable-beam route is attractive, but the public
  record has not yet closed the low-energy response or electromagnetic character.

The six routes are complementary. The first, second, third, fifth and sixth are
stable-beam or controlled reaction proposals; the fourth and the `132Sn` route are
higher-risk RIB or radioactive-beam proposals.
None is yet a final beam-time application: reaction yield, target-specific response and
statistical sensitivity remain to be calculated.

## Risks and Blockers

- `131Xe` 仍缺 event-level counts、conversion-electron response、共同 Cov 和新 lifetime
  producer。
- `131Ba/133Ce` 的候选 reaction family 需要 PACE/evaporation、target heating、channel
  purity 和 real response 计算；当前没有 target-specific yield。
- `78Br`/`132Sn` 的 RIB 产额、纯度、束斑、靶上停止和 γ efficiency 未闭合。
- `DRAGON-X` 是概念设计；其 combined performance、cost、mechanical integration、
  radiation load 和 DAQ throughput 尚未测量。
- `132Sn` 的单声子 E3 已有 primary benchmark，但两声子 quartet 的 continuum energy、
  neutron width, feeding, multi-state E3 和反应率仍需独立理论/response 计算，不能
  直接写成正式申请的确定预测。

## Next Actions

1. 为 `131Xe` 和 `131Ba` 各建立一个最小 reaction-rate/response input manifest。
2. 对 `78Br` 查 primary production/half-life/beam-yield；对 `132Sn` 以 ROS18 的
   HIE-ISOLDE/MINIBALL response 作为基准，计算 neutron–particle–γ sensitivity 和
   continuum background，先排除装置上不可行的候选。
3. 用 IMP-DRAGON 的实际 ring geometry 和 RIBLL 的 F2/F4 identity contract 建立
   `DRAGON-X` response prototype。
4. 对 `135/137Pr` 以 `110Cd` 为方法 benchmark，冻结 absolute lifetime/crossover-E2
   的 beam-request observables。
5. 把通过 feasibility gate 的一条路线扩写成一页正式束流申请草案。

## Human Review

This project is a Codex-generated L3 prospectus and remains `unreviewed`. It deliberately
contains bold hypotheses and design inferences; source facts, model interpretations and
future experiment predictions are kept in separate rows.
