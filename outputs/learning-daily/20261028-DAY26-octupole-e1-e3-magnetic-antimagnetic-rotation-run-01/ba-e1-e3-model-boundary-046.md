---
type: audit
title: "144Ba/146Ba E1-E3 evidence and SCCM model-boundary audit"
created: 2026-10-28
updated: 2026-10-28
status: read-only-audit
review_status: unreviewed
---

# 144Ba/146Ba E1-E3 evidence and SCCM model-boundary audit

## Scope

This is a read-only audit of the archived BU16, BU17 and Bernard source pages. It checks units, transition direction, projected-GCM kernel definitions and the boundary between measured quantities and model outputs. It does not introduce a new experiment or re-fit the GOSIA likelihood.

## Findings

### E1 amplitude units and uncertainty

BU17 records the experimental 146Ba E1 reduced amplitude as `0.000223(+10/-8) eb^(1/2)` and the SCCM comparison value as `0.00474` (same reduced-amplitude unit). The printed central-value amplitude ratio is approximately `21.26`; squaring gives approximately `451.8` in strength. This is arithmetic on reported centers, not a validated model-data agreement. The experimental E1 constraint is mainly inherited from earlier lifetime and branching information, and the full correlated fit likelihood is unavailable (BU17-D26-001; BU17 PDF p.3 Table I and following paragraph).

### E3 direction and the factor of seven

BU16 and BU17 quote the reduced matrix element in the upward `0+ -> 3-` convention while reporting the commonly used downward strength `B(E3; 3- -> 0+)`. For the same reduced matrix element,

`B(E3; 0+ -> 3-) = 7 B(E3; 3- -> 0+)`,

because the initial-state degeneracy factors are 1 and 7. The factor of seven is therefore a direction convention. It must not be interpreted as a sevenfold disagreement between BU16 and BU17. The source values are `48 W.u.` with broad asymmetric errors, and the two centers are rounded values rather than proof of exact equality (BU16-D26-001; BU17-D26-005).

### F(q) versus the non-diagonal transition kernel

Bernard defines the collective amplitude as `F=N^(1/2)f`, where `N` is the norm kernel. The observable is evaluated through a double coordinate sum of the form

`f_f*(q) O(q,q') f_i(q')`.

Consequently, a plot of `|F(q)|^2`, even when the positive- and negative-parity densities look similar, does not determine an absolute E1 or E3 transition. The E1 cancellation question requires the projected odd-parity E1 kernel and coherent HWG amplitudes. Orbital occupations `v2`, a mean-field minimum, or visual F-plot overlap cannot replace that kernel (BE16-D26-005; BU17-D26-004; Bernard PDF p.2 Eqs.4-5).

### Model values versus experiment

The BU16/BU17 Coulomb-excitation E3 strengths are experimental observables obtained through the GOSIA yield-to-matrix-element chain, with the documented rotor and higher-multipole boundaries. Bernard's `0.460 eb^(3/2)` and downward `B(E3)=25 W.u.` are projected-GCM calculations. The BU17 SCCM amplitude `0.00474`, orbital occupations and calculated D0 sign trend are also model outputs. They can explain or test the data within their model spaces; they cannot be relabeled as measurements (BU16-1/2; EXT146-1/3; BE16-D26-007).

## Unresolved questions

- The complete correlated GOSIA likelihood and covariance for the 146Ba E1/E3 fit are unavailable.
- Production SCCM transition kernels and code are unavailable, so F-plot similarity cannot be independently converted into an E1-kernel audit.
- The relative E1/E3 sign is fit or model dependent and is not an absolute experimental phase measurement.
- The broad E3 intervals do not distinguish a rigid static pear shape from dynamic octupole softness without additional observables, such as parity-displacement systematics.

## Evidence locators

| Claim | Locator | Tier |
|---|---|---|
| 144Ba E3 amplitude and downward B(E3) | `BU16-D26-001`; BU16 PDF p.4 Table I | direct experiment plus angular-momentum conversion |
| 146Ba E1 amplitude and SCCM comparison | `BU17-D26-001`; BU17 PDF p.3 Table I | direct table plus model comparison |
| E3 direction factor seven | `BU16-D26-001`; `BU17-D26-005` | definition and algebra |
| F=N^(1/2)f and double-kernel observable | `BE16-D26-005`; Bernard PDF p.2 Eqs.4-5 | direct model method |
| SCCM 144Ba E3 value | `BE16-D26-007` | model calculation |

## Audit status

Read-only Codex source self-audit. No human review, commit, push, or full-repository lint was performed.
