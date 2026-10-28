---
type: research-note
title: "144Ba/146Ba E1-E3 evidence chain and SCCM model boundary audit"
aliases: [ba e1 e3 model boundary 046, barium E1 E3 evidence audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, bernard-2016-144ba-sccm-octupole]
created_from: Day26 read-only source audit
promotion_target: octupole-mr-amr-evidence-gradient
tags: [144Ba, 146Ba, E1, E3, SCCM, GCM, evidence-boundary, units]
---

# 144Ba/146Ba E1-E3 evidence chain and SCCM model boundary audit

## Research Trigger

Can the archived BU16/BU17/ Bernard source chain support a direct numerical comparison of E1 and E3 observables, and can collective-amplitude plots be used as substitutes for projected transition kernels?

## Grounded Evidence

| ID | Claim | Tier | Locator | Boundary |
|---|---|---|---|---|
| BA046-1 | BU16/BU17 use a reduced E3 matrix element with the upward `0+ -> 3-` convention while quoting downward `B(E3;3- -> 0+)`; the reverse B differs by the initial-state factor 7. | definition plus direct report | `BU16-D26-001`; `BU17-D26-005`; BU16 PDF p.4 Table I | The factor seven is a direction convention, not an inter-experiment mismatch. |
| BA046-2 | BU17 lists experimental E1 amplitude `0.000223(+10/-8) eb^(1/2)` and SCCM amplitude `0.00474`; central amplitude ratio is ~21.26 and squared ratio ~451.8. | direct table plus arithmetic | `BU17-D26-001`; BU17 PDF p.3 | Missing full covariance prevents exact model-data validation. |
| BA046-3 | Bernard's `F=N^(1/2)f` is a collective amplitude; observables require a double coordinate sum with a non-diagonal operator kernel. | direct model method | `BE16-D26-005`; Bernard PDF p.2 Eqs.4-5 | Similar F densities do not determine E1/E3 strengths. |
| BA046-4 | BU16/BU17 E3 values are experimental GOSIA observables; Bernard's `0.460 eb^(3/2)` and downward `25 W.u.` are SCCM model results. | evidence-tier separation | `BU16-1`; `EXT146-1`; `BE16-D26-007` | Model numbers cannot be relabeled as measurements. |

## Provisional Reasoning

The E1 comparison is dimensionally meaningful only after keeping the reduced-amplitude unit `eb^(1/2)` explicit. The large numerical difference between the experimental and SCCM centers should be reported as a model-data discrepancy or model-boundary issue, not as exact agreement. The source itself says the experimental E1 constraint is largely inherited from earlier lifetimes and branching ratios.

The E3 comparison requires transition direction bookkeeping. Since `B(E3;0+ -> 3-) = 7 B(E3;3- -> 0+)`, a quoted `48 W.u.` downward strength cannot be compared to an upward value without applying the degeneracy factor.

The SCCM/GCM method further separates coordinate-space similarity from transition strength. A collective amplitude plot can show where projected states draw support in deformation space, but the measured strength comes from coherent integration of the amplitudes with the projected non-diagonal operator kernel. This is the specific reason a similar F plot does not imply similar E1 strength.

## Open Questions

1. The complete GOSIA covariance or joint likelihood for the 146Ba E1/E3 fit is unavailable.
2. Production SCCM transition kernels and code are unavailable.
3. The E1/E3 relative sign is not an absolute experimental phase measurement.
4. The broad E3 intervals cannot distinguish static rigid octupole shape from dynamic softness without additional observables.

## Assumptions

The audit uses printed matrix-element conventions and does not reconstruct GOSIA likelihoods, covariance or production SCCM kernels.

## Competing Explanations

E1 cancellation, shape softness, orbital occupation and fit priors can affect the same observables; no single explanation is promoted beyond the sources' model scope.

## Transfer Conditions

Unit and degeneracy rules transfer only when initial spin, transition direction and reduced-matrix-element convention are explicit.

## Failure Conditions

An F plot, mean-field minimum or orbital occupancy cannot substitute for a projected non-diagonal electromagnetic kernel or direct measurement.

## Falsification or Reverse Tests

Acquire joint GOSIA covariance and production SCCM kernels, then reproduce the E1/E3 comparison without changing transition direction or model/data tier.

## Knowledge Impact and Learning Decision

`supports` the direct-observable → derived-strength → model-explanation ladder; `revises` any claim that an F-plot or orbital occupancy alone reproduces an absolute E1 matrix element; `limits` use of SCCM values as experimental facts. This note is a Codex source self-audit and remains `unreviewed`.

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[bernard-2016-144ba-sccm-octupole]]

## Review Status

Read-only audit; no human review performed.

## Human Review

No human review has been performed; `review_status` remains `unreviewed`.

## Promotion or Rejection History

2026-10-29: Research-note schema repaired after parallel audit; scientific scope unchanged.
