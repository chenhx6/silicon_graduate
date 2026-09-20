---
type: source
title: "Yamazaki 1967 - Tables of coefficients for angular distributions from aligned nuclei"
aliases: [Yamazaki 1967 angular-distribution tables]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: reference-tables
reading_depth: deep-read
title_original: "Tables of Coefficients for Angular Distribution of Gamma Rays from Aligned Nuclei"
authors: [T. Yamazaki]
journal: "Nuclear Data, Section A"
year: 1967
volume: 3
pages: "1-23"
canonical_source: "Yamazaki, Nuclear Data A 3 (1967)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1967_Yamazaki_Tables of coefficients for angular distribution of gamma rays from aligned.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1967_Yamazaki_Tables of coefficients for angular distribution of gamma rays from aligned.pdf"
raw_sha256: "e807782c580a0313ee3763f56df1dd424e5c97925d70e3d30a79a8b534c81f70"
nuclei: [generic]
reactions: [particle-xn-alignment]
experiments: [gamma-angular-distribution]
models: [statistical-tensor, gaussian-magnetic-substate-alignment]
observables: [A2, A4, A6, angular-distribution, mixing-ratio, attenuation]
methods: [angular-distribution, ADO, reference-tables]
tags: [aligned-nuclei, angular-distribution, high-spin, tables]
---

# Tables of coefficients for angular distributions from aligned nuclei

## Bibliographic Record

- T. Yamazaki, *Nuclear Data, Section A* **3** (1967), pp.1–23.

## Scope and Reading Depth

- The 23-page scan was read end-to-end: introduction, Eqs.(1–15), Figs.1–3, references, Table I and the integral- and half-integral-spin Table II coefficient pages. The dense scanned tables were checked visually on the page images; they are tabulations, not a new experiment.

## Core Method

The paper starts from statistical-tensor populations `p_k(J)` of an aligned state. For a mixed `L1/L2` transition it writes

`W(θ)=1+A2 P2(cosθ)+A4 P4(cosθ)`,

with `A_k` built from alignment tensors and `F_k` Racah/Clebsch–Gordan coefficients (PDF pp.1–3, Eqs.1–5). Complete-alignment tensors `B_k(J)` are tabulated for integer and half-integer spin (Table I). Partial alignment is represented by attenuation `α_k(J)=p_k(J)/B_k(J)` and `A_k=α_k A_k^max` (p.2, Eqs.9–10).

The practical one-parameter approximation is a Gaussian magnetic-substate population, `P_m∝exp[-m²/(2σ²)]`. The figures show that `α4` falls rapidly with `α2` and `α6` is usually negligible; therefore `σ/J` or `α2` can often parameterize the alignment only after the reaction mechanism is justified (pp.2–3, Figs.2–3). For a preceding transition `Ji→Jf`, the state tensor propagates through `U_k(Ji L1 L2 Jf)` and the previous alignment, making cascade feeding explicit (p.3, Eqs.12–15).

## Key Results

- Table IIa gives `F_k`, `B_kF_k` and `U_k` functions for integral spins; Table IIb supplies the corresponding half-integral-spin entries through the tabulated spin ranges (pp.7–23).
- The paper explicitly warns that the sign of `δ` inferred from a single-transition angular distribution is opposite to the sign from the corresponding `Ji→Jf→J` γ–γ correlation under its stated ordering (p.2). This is a convention mapping, not a physical sign reversal.
- The Gaussian population follows the heavy-ion “random walk” alignment picture and is a useful approximation, not a universal prior; non-Gaussian feeding and side-feeding must be tested against the measured coefficients.
- Angular distributions alone constrain combinations of spin sequence, alignment and multipole mixing; the tables do not replace polarization, DCO, lifetime or level-scheme evidence.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| YA67-1 | `B_k`, `F_k` and `U_k` tables provide aligned-state angular-distribution coefficients for integer and half-integer spins. | method-result | direct | PDF pp.1–3, 7–23, Eqs.1–15, Tables I–II | true |
| YA67-2 | Gaussian attenuation connects measured `A_k` to `σ/J`, but this is a feeding/alignment model assumption. | method-boundary | direct | PDF pp.2–3, Figs.2–3 | true |
| YA67-3 | δ signs require an explicit angular-distribution versus γγ-correlation convention map. | convention-boundary | direct | PDF p.2 | true |

## Summary

Yamazaki's tables provide the tensor and attenuation backbone for aligned-state angular-distribution analyses, with the useful warning that alignment and sign conventions are part of the measurement identity.

## Competing Interpretations and Limitations

- Gaussian magnetic-substate populations and single-parameter alignment may fail for non-Gaussian or strongly side-fed states.
- A table coefficient is not a detector-independent measured coefficient and cannot alone resolve spin, alignment and δ.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| YA67-AR-1 | Tensor chain | Population/statistical tensor → `F_k` angular coefficients → attenuation → measured `A_k`. | PDF pp.1–3, Eqs.1–15 | self-checking |
| YA67-AR-2 | Alignment identifiability | Treating `σ/J` or `α2` as one free parameter is a Gaussian-model choice; higher tensors can carry information when statistics permit. | PDF pp.2–3, Figs.2–3 | self-checking |
| YA67-AR-3 | Convention safety | Map state order, operator phase and angular-distribution versus γ–γ correlation before transferring a δ sign. | PDF p.2 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-momentum-alignment]], [[angular-correlation]] and the later Der-Mateosian–Sunyar coefficient tables.
- Reusable rule: keep complete-alignment coefficients, attenuation factors and detector/feeding corrections as separate evidence layers; do not quote a table entry as an experiment-specific `A2/A4`.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `YA67-P0-1`: Preserve the δ sign/state-order warning and the Gaussian-alignment assumption before using the tables for spin or mixing-ratio assignments.

## Extracted Pages

- Methods: [[angular-distribution]], [[angular-correlation]], [[angular-momentum-alignment]]。
