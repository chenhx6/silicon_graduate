---
type: source
title: "Frauendorf 2015 - The low-energy quadrupole mode of nuclei"
aliases: [Frauendorf 2015 quadrupole mode, tidal wave TPSM review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review-theory
reading_depth: deep-read
title_original: "The low-energy quadrupole mode of nuclei"
authors: [S. Frauendorf]
journal: "International Journal of Modern Physics E"
year: 2015
volume: 24
article: 1541001
pages: "1-38"
doi: "10.1142/S0218301315410013"
citation_key: Frauendorf_2015
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1142/S0218301315410013"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/进动/理论/2015_Frauendorf_The low-energy quadrupole mode of nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/进动/理论/2015_Frauendorf_The low-energy quadrupole mode of nuclei.pdf"
raw_sha256: "6503190945574eb2a19dc10555f4abc8866340dc3b84e0ff72068fcb0d9010d5"
nuclei: [102Pd, 152Sm, 62Ni]
reactions: []
experiments: []
models: [Bohr-Hamiltonian, ATDMF, GCM, IBM, TPSM, tidal-wave]
observables: [quadrupole-vibration, gamma-softness, gamma-band-staggering, B(E2), tidal-wave]
methods: [collective-model, generator-coordinate, projected-shell-model]
tags: [quadrupole, triaxiality, gamma-soft, tidal-wave, TPSM, review]
---

# The low-energy quadrupole mode of nuclei

## Bibliographic Record

- S. Frauendorf, *International Journal of Modern Physics E* **24**, 1541001 (2015), DOI `10.1142/S0218301315410013`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/三轴/进动/理论/2015_Frauendorf_The low-energy quadrupole mode of nuclei.pdf`。
- 38-page review; chapter equations/figures and model limitations read.

## Scope and Reading Depth

- Full review read: Bohr Hamiltonian/γ signatures, microscopic ATDMF, GCM, IBM mapping, tidal-wave approach, triaxial projected shell model (TPSM), applications and critical assessment of adiabaticity/decoherence.
- Key concepts checked: 5D quadrupole coordinates, γ-soft/rigid regions, zero-point energy, `102Pd/152Sm/62Ni` examples, `B(E2)` patterns and nonadiabatic coupling.
- Not covered: re-running cited GCM/IBM/TPSM codes or all post-2015 applications.

## Key Results

- The Bohr Hamiltonian classifies quadrupole spectra by potential shape and zero-point fluctuations; γ-softness is a wave-function extent, not simply a nonzero triaxial minimum.
- Microscopic ATDMF, GCM and IBM mappings provide complementary parameter routes but inherit adiabatic assumptions; high-lying/multiphonon states decohere through quasiparticle coupling.
- Tidal-wave and TPSM approaches extend spectral calculations beyond the adiabatic region, linking yrast `B(E2)`/moments of inertia and angular-momentum projection to quadrupole collectivity.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FR15-1 | Low-energy quadrupole structures require separating β/γ potential shape, zero-point fluctuations and quasiparticle decoherence. | review-framework | direct | PDF pp.1–8, Figs.1–3 | true |
| FR15-2 | Microscopic BH parameters can be derived via ATDMF/GCM and mapped to IBM, but model mappings are not direct experimental shape measurements. | model-framework | direct | PDF Secs.3–5 | true |
| FR15-3 | Tidal-wave and TPSM methods address nonadiabatic/high-spin quadrupole spectra beyond simple BH/IBM assumptions. | model-framework | direct | PDF Sec.6 | true |

## Summary

Frauendorf's review provides the quadrupole-mode counterpart to the rotating-mean-field review: γ-softness, triaxiality, vibrational collectivity, tidal waves and projected-shell-model spectra are organized with explicit adiabatic/decoherence limits.

## Competing Interpretations and Limitations

Energy ratios and `B(E2)` patterns are not unique shape classifiers; model parameters, zero-point fluctuations, pairing and quasiparticle coupling can alter γ-soft/rigid assignments. Tidal-wave/TPSM results remain model calculations rather than direct triaxial observables.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| FR15-AR-1 | Concept chain | 5D quadrupole potential → wave-function/ZPE → E2/energy observables → model comparison. | PDF Secs.2–6 | self-checking |
| FR15-AR-2 | Transfer condition | Cross-nucleus use needs matched potential, boson number, pairing and adiabaticity. | PDF Secs.3–7 | active-L3 |
| FR15-AR-3 | Independence | Review; `102Pd/152Sm/62Ni` examples are cited data/calculations, not new experiments. | Scope/Refs. | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[octupole-softness]]-style potential/wave-function separation, γ-softness diagnostics and [[tidal-wave]]/TPSM model map.
- Persistence: source/index and A≈130 collective-mode project relation.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `FR15-P0-1`: do not infer γ-rigid/γ-soft or direct triaxiality from one energy ratio or model fit.

## Extracted Pages

- Concepts: [[triaxial-deformation]], [[gamma-soft-deformation]], [[tidal-wave]]。
- Models: [[triaxial-projected-shell-model]]。
