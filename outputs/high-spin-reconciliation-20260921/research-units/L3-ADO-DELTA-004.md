---
type: research-unit
unit_id: L3-ADO-DELTA-004
created: 2026-09-21
updated: 2026-09-21
status: completed-method-boundary
review_status: unreviewed
---

# L3: alignment, δ and detector-response identifiability

## Question

When do angular-distribution, DCO/ADO and polarization observables identify a unique mixing-ratio branch?

## Evidence

- Yamazaki 1967 links `p_k`, `B_k`, `F_k` and cascade `U_k`, with Gaussian m-substate attenuation and an explicit sign warning (PDF pp.1–3, Eqs.1–15).
- Der Mateosian–Sunyar 1974 tabulates mixed-multipole coefficients and attenuation; the worked intersection of `A2/A4` constrains `(σ/J,δ)` only within the alignment model (PDF pp.407–412, Fig.2).
- Suffert 1959 and later CLOVER/PDCO sources show how physical polarization, count asymmetry and detector `Q(E)` add electric/magnetic information, but retain geometry and energy dependence.
- James–Twin–Butler 1974 warns that alignment-model covariance and design-matrix rank can make a nominal δ solution non-identifiable (PDF method sections).

## Decision

A mixing-ratio interval is usable only with transition identity, state-order/sign convention, reaction alignment, detector efficiency/geometry and response uncertainty. The sign of one asymmetry or a historical table value is insufficient. Multiple branches remain valid when their uncertainty contours overlap after nuisance parameters are varied.

## Reverse test

Recompute a selected transition under alternative `σ/J`, side-feeding and `Q(E)` calibrations. If the preferred branch changes, the original single-branch claim is not robust. If both branches remain separated across a declared uncertainty envelope, the identification becomes stronger.

## L4 readiness and stop

The present batch supplies formulas and published outcomes but no complete common response/event package for a user-specific L4 fit. This L3 method boundary is complete; reopen when the user's P-ADO data and exact array calibration are supplied.

## Sources

- [[yamazaki-1967-aligned-angular-coefficients]], [[der-mateosian-sunyar-1974-angular-coefficients]], [[der-mateosian-sunyar-1974-attenuation-coefficients]].
- [[suffert-1959-proton-capture-polarization]], [[james-twin-butler-1974-angular-correlation-statistics]].
- [[high-spin-angular-polarization-mixing-ratio]], [[multipole-mixing-ratio]].
