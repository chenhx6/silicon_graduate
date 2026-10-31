---
type: research-note
title: "`135Nd` 2025 TiP 扩展：新 `17/2−` 态与同谱系边界"
aliases: [135Nd 2025 tilted precession extension, same-lineage TiP extension]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [lv-2021-tilted-precession-135nd, 135nd-134pr-transition-identity-ledger-20261031, partner-em-interval-loso-audit]
created_from: "2026-10-31 primary discovery and full-text reading"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135nd/tilted-precession/same-lineage/transition-identity
nuclei: [135nd]
observables: [transition-energy, b-e2-ratio, multipolarity, triaxiality, band-lineage]
tags: [135nd, tilted-precession, same-lineage, jurogam2, b-e2, p3]
---

# `135Nd` 2025 TiP 扩展：新 `17/2−` 态与同谱系边界

## Research Trigger

Lv et al. 2025 扩展了 `135Nd` 的低到高自旋谱学，报告新 `17/2−_3` 态和高自旋
band T。该来源对 P3 有价值，但其反应、阵列和事件谱系与 Lv 2021 TiP 论文相同，
必须作为同一实验谱系的 extension 处理。

## Grounded Evidence

| Claim | Locator | Evidence layer | Boundary |
|---|---|---|---|
| New `17/2−_3` state at about `1468 keV` is fixed by two E2-character transitions | PDF pp.1, 3–5; extracted text lines 67–77, 593–610 | experimental spectroscopy | no lifetime; apparent lifetime is not a new DSAM/RDDS measurement |
| The state decays through `752` and `908 keV` E2 branches to the two `13/2−` states | PDF pp.3–5; Table I; extracted lines 748–758 | transition identity and relative EM | absolute matrix elements and joint covariance are not supplied |
| `B(E2,752)/B(E2,908)=2.0(5)` | PDF p.5; extracted text lines 748–765 | derived relative transition-probability ratio | not an absolute `B(E2)` and not an independent lifetime measurement |
| High-spin band T contains seven E2 in-band transitions and is compared with CNS | PDF pp.3–6; extracted lines 470–490, 798–830 | experiment plus model interpretation | configuration/large-triaxiality conclusion is model-assisted |
| Experiment uses `100Mo(40Ar,5n)` at `152 MeV`, JUROGAM II, 39 detectors and `5.1×10^10` coincidence events | PDF p.2; extracted lines 130–140 | source-lineage and setup | same reaction/array/event family as Lv 2021; exact event overlap and covariance unavailable |

The primary identity is B. F. Lv et al., “Triaxiality and confirmation of low-spin tilted
precession in `135Nd`,” *Physical Review C* **111**, 054304 (2025), DOI
`10.1103/PhysRevC.111.054304`. The readable institutional copy is staged at
`tmp/day31-135nd-2025-lv-extension.pdf`, SHA-256
`d1cfd0c1336f19b8ff18161be0ba6ff123fcb1c273b2dc780bb38ee0d0012dec`.

## Provisional Reasoning

The `2.0(5)` ratio supports the paper's TiP1 interpretation: the `752-keV` branch to the
`13/2−` TiP1 state is stronger than the `908-keV` branch to the D1 `13/2−` state, consistent
with the authors' `ΔK=2` versus `ΔK=4` explanation. This is a conditional transition-network
argument. It does not identify a static shape, prove a unique tilted-precession geometry,
or replace a lifetime-resolved absolute EM matrix.

The new `17/2−_3` state's apparent decay speed is explained in the paper through the
non-K-forbidden `752-keV` path; it must not be recorded as a newly measured lifetime. Band T's
CNS comparison adds a high-spin shape/configuration model layer, not an experimental
measurement of `γ` or a new independent band structure.

## Assumptions

The `752/908` ratio is kept as the paper's reduced-transition-probability ratio under its
branch and state assignments. No absolute `B(E2)` is reconstructed from the printed ratio,
and no covariance is invented.

## Competing Explanations

The relative branch ratio can be affected by state identity, feeding, branch normalization
and configuration mixing. The `17/2−_3` energy displacement may involve shape differences,
core coupling or quasineutron configuration mixing. The high-spin band T may be described by
alternative cranked configurations if a common producer and full transition matrix are supplied.

## Transfer Conditions

This note can extend the P3 ledger to other same-campaign spectroscopy only when reaction,
array, state identity, branch definition and source lineage are explicitly matched. The
2025 ratio cannot be transferred to `135Pr`, `134Pr` or a different `135Nd` campaign.

## Failure Conditions

Stop a combined P3 fit if the 2025 and 2021 event overlap, branch normalization, or model
state mapping cannot be quantified. Stop any absolute-strength claim if no lifetime producer,
feeding correction and joint covariance are available.

## Falsification or Reverse Tests

A future common-response analysis should test whether the `752/908` ratio remains stable under
alternative state mappings, feeding nuisance and shared-lineage correlation. A lifetime or
absolute `B(E2)` measurement inconsistent with the ratio under the declared mapping would
lower the TiP1 interpretation, while agreement would still be conditional on the same state
identity and would not prove wobbling exclusion in every band.

## Open Questions

- Can the 2025 paper's line producer and response be aligned with the 2021 TiP1/TiP2 ledger?
- Is a lifetime or absolute transition matrix for the new `17/2−_3` state available elsewhere?
- Can the seven band-T E2 lines be mapped to an independent configuration-sensitive holdout?
- What shared nuisance and event-overlap covariance is required before comparing 2019, 2021 and
  2025 `135Nd` results?

## Knowledge Impact and Learning Decision

`supports`: P3 now includes a recent full-text same-lineage primary that adds transition
identity and relative E2 information for `135Nd`.

`limits`: it does not add a new independent experiment, absolute lifetime, full `B(E2)` matrix,
or unique static-chirality/wobbling verdict.

`revises`: future P3 writing must distinguish “same-lineage spectroscopy extension” from
“independent confirmation” and keep the `752/908` ratio separate from MU07 state-level `B` rows.

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | Lv 2025 primary extension audit | none | provisional same-lineage extension | full institutional PDF read; same JUROGAM II reaction/array as 2021, no new lifetime/Cov | [[post-30-day-nuclear-structure-paper-prospectus]] |

## Human Review

Codex self-audit; `review_status: unreviewed`, `reasoning_status: provisional`.
