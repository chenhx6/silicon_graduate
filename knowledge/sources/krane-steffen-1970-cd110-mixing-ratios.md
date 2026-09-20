---
type: source
title: "Krane and Steffen 1970 - E2/M1 mixing ratios in 110Cd"
aliases: [Krane Steffen 1970 Cd110 mixing ratios]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-formalism
reading_depth: deep-read
title_original: "Determination of the E2/M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110"
authors: [K. S. Krane, R. M. Steffen]
journal: "Physical Review C"
year: 1970
volume: 2
pages: "724-734"
doi: "10.1103/PhysRevC.2.724"
canonical_source: "Krane & Steffen, Phys. Rev. C 2, 724-734 (1970)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1970_Krane et al_Determination of the E2M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1970_Krane et al_Determination of the E2M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110.pdf"
raw_sha256: "ab82cb483425ba984a8c30b35f118b4713e186d53899fcbbba6a19dd444377f1"
nuclei: [110Cd, 110Ag]
reactions: [110Ag-beta-decay]
experiments: [two-GeLi-directional-correlation]
models: [vibrational-model, extra-pair-model, Rose-Brink, Biedenharn]
observables: [E2-M1-mixing-ratio, directional-correlation, gamma-width, quadrupole-moment]
methods: [gamma-gamma-directional-correlation, high-resolution-GeLi]
tags: [110Cd, mixing-ratio, angular-correlation, vibrational-nucleus]
---

# E2/M1 mixing ratios in `110Cd`

## Bibliographic Record

- K. S. Krane & R. M. Steffen, *Phys. Rev. C* **2**, 724–734 (1970), DOI `10.1103/PhysRevC.2.724`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1970_Krane et al_Determination of the E2M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110.pdf`。

## Scope and Reading Depth

- PDF pp.724–734 fully read: `110Ag→110Cd` level structure, Ge(Li) 1–2/1–3/1–4 directional correlations, 25-correlation fit, explicitly defined reduced operators, convention conversion, all mixed-transition δ values and vibrational/extra-pair discussion.
- Not covered: raw coincidence matrices and later model calculations.

## Key Results

- High-resolution two-Ge(Li) directional correlations and coincidence gating determine a consistent set of 25 cascade correlations. Compton background was explicitly investigated and shown to bias directional-correlation coefficients if untreated (PDF pp.724–727).
- The reported E2/M1 amplitude ratios are `δ(447)=−0.45(20)`, `δ(620)=−0.80(50)`, `δ(678)=−0.25(20)`, `δ(687)=−1.1(+?−?)`, `δ(707)=−1.0(3)`, `δ(818)=−1.20(15)`, `δ(1384)=−0.37(3)`, `δ(1505)=−0.55(10)`; the paper also gives corresponding Bohr–Mottelson multipole-moment ratios (PDF p.724, abstract and conclusion tables).
- The formalism defines δ using reduced emission matrix elements with the initial state on the right and maps them explicitly to Rose–Brink and Biedenharn conventions. This resolves sign/order ambiguity before comparing the 25 fits (PDF pp.726–728, Eqs.3–14).
- The measured nonzero M1 admixtures and crossover E2 transitions challenge a pure harmonic-vibration picture of `110Cd`; the authors discuss extra-pair/anharmonic and microscopic quadrupole–pairing interpretations (PDF pp.724–726).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KS70-1 | A consistent set of E2/M1 δ values is obtained from 25 Ge(Li) directional correlations after Compton-background control. | mixing-ratio-result | direct | PDF pp.724–728, abstract | true |
| KS70-2 | Explicit operator/state-order definitions and conversion to Rose–Brink/Biedenharn conventions are necessary for δ sign comparison. | convention-boundary | direct | PDF pp.726–728, Eqs.3–14 | false |
| KS70-3 | Nonzero M1 admixtures and crossover E2 decay challenge a pure harmonic-vibration description of `110Cd`. | structure-interpretation | mixed | PDF pp.724–726 | true |
| KS70-4 | Directional-correlation coefficients require explicit Compton-background and detector-response checks. | method-boundary | direct | PDF pp.724–725 | false |

## Summary

Krane and Steffen demonstrate how a complete high-resolution directional-correlation network can determine a mutually consistent set of E2/M1 mixing ratios. The source is an important convention and background-control anchor for later δ tables, while its anharmonic-vibration interpretation remains model dependent.

## Competing Interpretations and Limitations

- Some δ uncertainties are broad/asymmetric and branch solutions depend on the adopted spin sequence and convention. The printed scan/OCR obscures part of the 687-keV asymmetric interval; retain the source locator rather than silently symmetrizing it.
- Pure-vibration, displaced-oscillator and extra-pair models can reproduce different subsets of level energies, moments and transition strengths; δ data alone do not select a unique microscopic Hamiltonian.
- Ge(Li) Compton background and unresolved coincidence contributions can distort A coefficients; high-resolution gating is part of the measurement identity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KS70-AR-1 | Correlation chain | Cascade identity/background correction → directional-correlation coefficients → reduced-matrix-element fit → δ set across transitions. | PDF pp.724–728 | self-checking |
| KS70-AR-2 | Convention chain | Emission matrix elements (initial state right) → Rose–Brink/Biedenharn map → comparable δ signs. | PDF Sec.III, Eqs.3–14 | self-checking |
| KS70-AR-3 | Model boundary | δ/M1 admixtures constrain vibration/extra-pair models but do not uniquely determine shape or collectivity. | PDF Sec.I and discussion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-correlation]], [[angular-distribution]], [[rose-brink-1967-phase-defined-angular-distributions]] and the `110Cd` γ-vibration comparator.
- New reusable rule: a directional-correlation δ value is only portable with its operator convention, cascade order, background correction and spin sequence.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KS70-P0-1`: Preserve Compton-background, convention and spin-sequence boundaries; do not merge the printed δ values with Rose–Brink or Hamilton values without conversion.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-correlation]], [[angular-distribution]]。
