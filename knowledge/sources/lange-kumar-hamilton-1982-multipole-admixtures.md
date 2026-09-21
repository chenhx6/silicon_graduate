---
type: source
title: "Lange, Kumar & Hamilton 1982 - E0-E2-M1 multipole admixtures in even-even nuclei"
aliases: [Lange Kumar Hamilton 1982 mixing-ratio review]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: review-and-data-compilation
reading_depth: deep-read
title_original: "E0-E2-M1 multipole admixtures of transitions in even-even nuclei"
authors: [J. Lange, Krishna Kumar, J. H. Hamilton]
journal: "Reviews of Modern Physics"
year: 1982
citation_key: lange_1982_E0E2M1
volume: 54
pages: "119-185"
doi: "10.1103/RevModPhys.54.119"
canonical_source: "https://doi.org/10.1103/RevModPhys.54.119"
library_file: "raw/papers/gpt/high-spin-20260920/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf"
raw_sha256: "ed925a0577a9257903806acd209c1db707529e86a5bfd9a301a83d597bf78ffb"
nuclei: [even-even-nuclei]
reactions: [decay-spectroscopy, angular-correlation, conversion-electron]
experiments: [historical-mixing-ratio-database]
models: [single-particle, rotational, rotation-vibration, pairing-plus-quadrupole, interacting-boson]
observables: [E2-M1-mixing-ratio, E0-E2-mixing-ratio, internal-conversion, B(E2), B(M1), monopole-matrix-element]
methods: [angular-correlation, angular-distribution, linear-polarization, internal-conversion]
tags: [mixing-ratio, E0, E2, M1, review, even-even]
---

# E0–E2–M1 multipole admixtures in even-even nuclei

## Bibliographic Record

- J. Lange, K. Kumar & J. H. Hamilton, *Rev. Mod. Phys.* **54**, 119–185 (1982), DOI `10.1103/RevModPhys.54.119`.

## Scope and Reading Depth

- The 76-page RMP was read section-by-section and table-by-table: Introduction; definitions and sign conventions; collective, rotational, rotation–vibration, microscopic PPQ and IBM models; the adopted E2/M1 and E0/E2 compilation (Tables I–IX); data-quality notes; and the comparison/conclusions through the final references. Dense table pages were visually checked where OCR was unreliable.

## Definitions and Convention Rules

For allowed E2/M1 transitions the review defines `δ²=T(E2)/T(M1)` and relates it to reduced `B(E2)/B(M1)` with the appropriate photon-energy and angular-momentum factors (PDF pp.121–122, Eqs.2.1–2.6). It adopts the positive-root Krane–Steffen convention, while stressing that experimental signs also depend on the alignment axis, Clebsch–Gordan/Racah factors, state order and emission/absorption convention (pp.121–123, Eqs.2.7–2.11). E0/E2 mixing is defined through conversion-electron coefficients and nuclear monopole matrix elements `ρ(E0)` (p.123, Eqs.2.12 onward).

The review's first-order rotation–vibration treatment gives selection-rule and angular-momentum dependence for β/γ-to-ground-band transitions. It shows why E2-dominated collective transitions can nevertheless acquire sensitive M1 admixtures through band mixing, and why signs can vary with nucleus and transition even when the macroscopic deformation looks similar (pp.124–133, Eqs.3.14–3.47).

## Model Comparison and Data Audit

The model survey compares the single-particle/Weisskopf limit, rigid-rotor and rotation–vibration estimates, PPQ/quasiboson and self-consistent time-dependent Hartree–Bogolyubov methods, dynamic deformation, and IBM (pp.123–132). PPQ generally captures the signs and a broad set of magnitudes better than IBM, while IBM can fit selected magnitudes; neither removes the nucleus- and transition-specific sensitivity of the M1 matrix element (pp.178–180, Tables V–VI). E0 data show large β→ground-band values and very small γ→ground-band values, but E0 strength is not a unique β-band signature because two-quasiparticle states can also produce large values (pp.180–183, Tables VII–IX).

The adopted data table is a critical survey through January 1980, not a homogeneous new experiment. It excludes or downgrades cases with unresolved close-lying transitions, inconsistent `A2/A4`, NaI summing, unknown gating multipolarity, hyperfine attenuation or incompatible results; numerous nucleus-specific footnotes document these decisions (pp.133–167). In heavy even-even systems, the table shows very large E2/M1 ratios compared with the single-particle limit, but the spread and sign changes remain real structure information rather than a universal deformation meter.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LKH82-1 | δ is a convention-dependent reduced E2/M1 matrix-element ratio; signs require an explicit phase/state-order map. | convention-boundary | direct | PDF pp.121–123, Eqs.2.1–2.15 | true |
| LKH82-2 | PPQ generally captures signs and broad magnitudes better than IBM in the reviewed comparisons, but neither is universal. | model-comparison | mixed | PDF pp.123–132, 178–180, Tables V–VI | true |
| LKH82-3 | The historical E0/E2/M1 compilation is heterogeneous and preserves detector/feeding/branch-quality exclusions in footnotes. | data-compilation | direct | PDF pp.133–167, Tables I–IX | true |

## Summary

This RMP is a convention- and provenance-aware bridge from historical mixing-ratio measurements to collective and microscopic model tests.

## Competing Interpretations and Limitations

- Review tables are not independent experiments and must be traced to the cited primary source for numerical use.
- E0 strength and E2/M1 magnitude are sensitive to configuration mixing, band assignment and model assumptions; neither is a stand-alone deformation observable.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| LKH82-AR-1 | Definition chain | `δ` is a reduced-matrix-element ratio with convention-dependent sign; `δ²` alone loses interference information. | PDF pp.121–123, Eqs.2.1–2.15 | self-checking |
| LKH82-AR-2 | Model hierarchy | Collective limits organize trends, but microscopic configuration mixing is needed for sign/magnitude variations; PPQ and IBM are not interchangeable evidence. | PDF pp.123–132, Tables V–VI | self-checking |
| LKH82-AR-3 | Compilation reliability | Table values are curated from heterogeneous angular-correlation, angular-distribution, polarization and conversion data; footnotes preserve unresolved branches and detector-era failures. | PDF pp.133–167, Table I notes | self-checking |
| LKH82-AR-4 | E0 interpretation | Large E0/E2 is compatible with β collectivity but can also arise from quasiparticle/shape-coexistence configurations. | PDF pp.169–183, Tables VII–IX | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-distribution]], [[angular-correlation]], [[linear-polarization-asymmetry]] and the batch-wide evidence/convention checklist; it supplies the historical bridge for HS-076, HS-081, HS-088 and HS-112.
- Reusable rule: retain sign convention, state order, alignment attenuation, gate complexity and table footnotes alongside every adopted δ; never treat a review compilation as independent experimental evidence.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `LKH82-P0-1`: Before paper-level numerical reuse, return to the cited primary angular-correlation/polarization paper and the exact table footnote; the review's adopted value is a traceable index, not a replacement source.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-distribution]], [[angular-correlation]], [[linear-polarization-asymmetry]]。
