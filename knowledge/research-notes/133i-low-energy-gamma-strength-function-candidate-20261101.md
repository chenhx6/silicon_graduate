---
type: research-note
title: "`133I` 低能 γ 射线强度函数上弯与 M1 字符：A≈130 候选实验"
aliases: [133I low-energy gamma strength, 133I gammaSF upbend, A130 LEE candidate]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [indico-2026-133i-gamma-strength-record, larsen-2026-133i-oslo-preliminary, uio-2026-133i-thesis-announcement, schwengner-2013-m1-upbend-brink-axel, ronning-2026-70zn-magnetic-lee]
created_from: "2026-11-01 Day29 non-overlapping candidate-pool sidecar"
promotion_target: "cross-mass-phenomena-detector-beam-prospectus-20261101"
nuclei: [133i, 138la, 139la, 140la, 56fe, 95mo, 70zn]
reactions: [130te-alpha-p-gamma-133i]
observables: [gamma-strength-function, nuclear-level-density, gamma-angular-distribution, compton-polarization, dipole-character]
methods: [oslo-method, particle-gamma-coincidence, particle-gamma-gamma, angular-distribution, compton-polarization]
tags: [133i, a130, gamma-strength-function, low-energy-enhancement, m1, brink-axel, experiment-design, l3]
---

# `133I` 低能 γ 射线强度函数上弯与 `M1` 字符：A≈130 候选实验

## Research Trigger

The cross-mass candidate-pool review found that the existing A≈130 routes focus on
discrete level identity, absolute electromagnetic strengths, E3 networks or β/γ decay
response. A public OCL record supplies a separate stable-beam γSF/NLD route for `133I`,
so the question is worth preserving as a bounded L3 candidate.

## Research Question

在奇质量、接近 `N=82` 的 `133I` 中，准连续区 `Eγ≲2 MeV` 是否存在低能
γ 射线强度函数（γSF）上弯（low-energy enhancement, LEE），并且能否用
角分布或 Compton 偏振把 dipole/M1 字符与响应伪影、非统计 feeding 和
NLD/自旋分布假设区分开？这条路线与离散能带的 `131Xe`、`135Pr`、
`135Nd/134Pr`、`132Sn` 两声子和 `100Sn` β/γ 响应问题不重复。

## Grounded Evidence

| ID | Narrow statement | claim_kind | evidence_level | exact locator | status |
|---|---|---|---|---|---|
| ILEE-1 | The public OCL record and Book of Abstracts identify an already-performed `130Te(α,pγ)133I` study using SiRi–OSCAR to extract NLD/γSF for `132I(n,γ)133I`; they do not report a closed `133I` LEE or multipolarity result. | experiment-record/access-boundary | targeted-abstract | [[indico-2026-133i-gamma-strength-record]] `OCL26-1`, `OCL26-2` | needs_review |
| ILEE-2 | `138La` γSF work reports an enhancement below about `2 MeV` and compares two non-overlapping initial-excitation windows; its electromagnetic composition remains an explicit follow-up question. | cross-mass experimental-context | primary abstract/figure | [Kheswa et al. 2017](https://www.osti.gov/pages/servlets/purl/1378552), abstract, Fig. 7(a), Fig. 8 discussion | needs_review |
| ILEE-3 | Independent `95Mo` particle–γ–γ work and `56Fe` particle-scattering γ work establish that LEE can be tested with different reaction paths and that dipole character requires an additional observable beyond a low-energy excess. | cross-mass experimental-context | primary abstract/method | [Wiedeking et al. 2012](https://pubmed.ncbi.nlm.nih.gov/22680714/) abstract/method; [Larsen et al. 2013](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.111.242504) abstract and angular-distribution discussion | needs_review |
| ILEE-4 | A 2026 `70Zn` result provides a current high-value comparison in which the magnetic interpretation of LEE is directly tested; it is a comparison anchor, not evidence for `133I`. | cross-mass comparison | primary article/metadata | [Ronning et al. 2026](https://doi.org/10.1038/s41586-026-10758-3), article identity and abstract | needs_review |
| ILEE-5 | A 2026 OCL presentation gives `Eα=24 MeV` for `130Te(α,pγ)133I`, identifies the fall-2025 experiment and says only a few data files had been sorted; it labels the analysis preliminary and provides no final γSF/LEE/M1 result. | dependent-experiment-readiness | targeted presentation | [[larsen-2026-133i-oslo-preliminary]] `LAR26-1`, `LAR26-2` | needs_review |
| ILEE-6 | An official UiO publication entry summarizes Grieg's thesis as identifying a `133I` low-energy enhancement and pygmy dipole resonance in the first indirect `132I(n,γ)133I` rate measurement. | institutional-secondary-report | secondary announcement | [[uio-2026-133i-thesis-announcement]] `UIO26-1` | needs_review |
| ILEE-7 | The NVA handle record for the announced thesis resolves to a media blog post with no associated artifacts in the retrieved API response; a locally staged file named `grieg-133i-thesis.pdf` is an HTML shell rather than a readable PDF, so the thesis manuscript remains unavailable through this route. | access-and-lineage-boundary | direct metadata-and-file-probe | [[uio-2026-133i-thesis-announcement]] `UIO26-2`, `UIO26-3` | needs_review |
| ILEE-8 | The independent `70Zn` primary demonstrates a magnetic LEE inference by combining two spin/parity-selective beta-decay parent states, total-absorption excitation-population information, Geant4 response unfolding, partial-NLD treatment and a parity-asymmetry correction; this is a method template, not evidence for `133I`. | cross-mass-method-transfer | direct-primary-plus-inference | [[ronning-2026-70zn-magnetic-lee]] `RON26-2`–`RON26-6` | needs_review |

These records establish a preliminary OCL acquisition and a secondary institutional report
of upbend/PDR, but not a thesis-level primary result. The `133I` result remains open until
the full analysis, response contract and electromagnetic-character test are recovered.
The NVA-named `.pdf` probe is invalid as a manuscript because it is an HTML shell
(`UIO26-3`).

## Provisional Reasoning

The most informative experiment is a joint γSF and response analysis with two excitation
windows and a dipole-character observable. This is a design inference from the available
method context and is not a measurement of `133I`.

### New cross-mass constraint from `70Zn`

The `70Zn` primary changes the design priority: two `E_x` windows can test
excitation-window stability, but they cannot by themselves identify M1 versus E1 when
the spin/parity population is unknown. For `133I`, the existing `130Te(α,pγ)` route
must therefore add either a validated spin/parity-selective population contrast, an
independent angular-distribution/Compton-polarization observable, or a calibrated
dipole-control network in the joint response model. The `70Zn` parent-state selectivity
and parity correction cannot be copied into a stable-beam `133I` Oslo analysis.

## Bold Hypothesis and Alternatives

**Bold hypothesis:** `133I` has a reproducible low-energy γSF enhancement whose dominant
component is dipole, with an `M1` contribution associated with high-`j` proton–neutron
recoupling near the shell-closure region.

Competing explanations are:

1. a genuine M1 component from recoupling or a scissors-like tail;
2. an E1 or mixed-dipole statistical component;
3. unresolved discrete lines or non-statistical feeding;
4. Oslo unfolding, threshold, summing, response or spin-distribution bias;
5. a local γSF feature that changes with initial excitation and therefore violates the
   assumed Brink–Axel transfer.

The positive outcome should therefore be phrased as “LEE plus constrained dipole
character”; it should not immediately be called proof of a single microscopic mechanism.

## Assumptions

- The public OCL record corresponds to the stated `130Te(α,pγ)133I` channel and
  SiRi–OSCAR analysis context.
- The candidate analysis can preserve event identity, low-energy response and at least
  two non-overlapping initial-excitation windows.
- Cross-mass LEE examples are comparison evidence, not a prior that forces an A≈130
  enhancement.

## Minimal Observable Contract

The same `133I` acquisition should provide:

- γSF and NLD from at least two non-overlapping initial-excitation windows;
- particle–γ and, where available, particle–γ–γ event identity with random/sideband
  controls;
- an efficiency and threshold response below `2 MeV`, including summing and discrete-line
  leakage;
- a `3–4 MeV` γ control region and known E1/M1 reference transitions;
- an angular-distribution or Compton-polarization observable for the low-energy excess;
- an explicit nuisance profile for NLD, spin population, unfolding regularization,
  beam/target background, particle efficiency and γ response;
- a holdout window or independent reaction path before assigning an electromagnetic
  character.

The first analysis should fit counts and response-folded γSF jointly. A low-energy
intensity increase alone is insufficient to identify `M1`.

## Competing Explanations

The explicit alternatives are high-`j` M1 recoupling, E1 or mixed dipole radiation,
scissors-like M1 strength, unresolved discrete feeding, and threshold/unfolding/NLD or
spin-distribution bias.

## Feasibility and Independence

The stable `130Te(α,pγ)133I` route is attractive because it does not require a rare
isotope beam or the `132Sn` neutron-continuum apparatus. The Book of Abstracts and
preliminary presentation say the study was already performed, so the first high-information
action is to obtain the full analysis, producer and response ledger. A new beam request is
justified only if the existing acquisition lacks the low-energy response or dipole-character
observable. If
the public `133I` dataset is reused, it remains one acquisition; an independent
angular/polarization run or a distinct reaction path must be tracked as separate evidence.

The cross-mass comparison is informative because `56Fe`, `95Mo`, `138La` and `70Zn`
provide different reaction methods and mass regions. Their differing source lineages
do not make a universal mechanism automatic; they only justify a falsifiable transfer
question for `133I`.

## Transfer Conditions

The comparison transfers only the observable contract: excitation-window stability,
response-folded γSF and an independent electromagnetic-character test. It does not
transfer a universal M1 mechanism, strength scale or Brink–Axel prior.

## Belief Revision and Stop Conditions

- **LEE and dipole character survive all response and excitation-window controls:** raise
  `133I` to a candidate beam/analysis proposal and compare its strength systematics with
  `70Zn`, `95Mo` and `138La`.
- **LEE survives but M1/E1 remains unresolved:** retain an L3 γSF observation with a
  dipole-character readiness boundary; do not claim scissors or recoupling.
- **LEE disappears under threshold/unfolding/feeding controls:** revise toward a
  response or non-statistical explanation.
- **Only one excitation window survives:** do not test Brink–Axel transfer or promote
  the result beyond a bounded observation.

Stop before L4 if event-level counts, low-energy response, NLD/spin alternatives or
the independent holdout are unavailable. No `133I` event data, γSF, M1 strength or
Bayes factor was generated in this note.

## Failure Conditions

Stop at L3/readiness if the low-energy efficiency, summing correction, particle–γ
random model, NLD/spin profile or holdout is unavailable. A null result without a
response-calibrated sensitivity limit cannot be called physical absence.

## Falsification or Reverse Tests

- Repeat the extraction with alternative unfolding regularization and threshold windows.
- Fit the low-energy region with response and non-statistical feeding templates.
- Reverse the analysis on a known dipole-control transition and a `3–4 MeV` control region.
- Compare the two excitation windows under a common response covariance.

## Knowledge Impact and Learning Decision

`supports`: a stable-beam A≈130 γSF route can test a phenomenon already observed or
investigated in several other mass regions with a different observable contract.

`revises`: the cross-mass candidate pool is not limited to discrete-band identity and
absolute electromagnetic-strength problems; quasi-continuum response is a distinct,
high-information route.

`limits`: the public record, preliminary presentation and institutional announcement are
access/readiness/secondary-report anchors, not a closed thesis-level primary result for
LEE or M1 character. This page remains `unreviewed` and provisional.

## Open Questions

- Does the full `133I` analysis actually report an LEE below `2 MeV`?
- Are the OCL event-level producer, response matrix, NLD/spin priors and covariance
  package accessible for an independent reanalysis?
- Can a stable angular-distribution or Compton-polarization observable be added without
  changing the acquisition lineage?
- What reaction-yield and low-energy efficiency budget is required for a new run?

## Promotion or Rejection History

| Date | event | previous state | new state | reason |
|---|---|---|---|---|
| 2026-11-01 | candidate-pool discovery | not selected | provisional L3 | non-overlapping stable-beam γSF route identified; public result remains incomplete |

## Human Review

This page is a Codex self-audit. It does not set `human-reviewed` and does not replace
full-text ingestion of the cited primary sources.
