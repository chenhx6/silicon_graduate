---
type: source
title: "Grodner et al. 2018 - g factor of the 128Cs chiral-band isomer"
aliases: [Grodner 2018 128Cs g factor]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-PRM-CDFT
reading_depth: deep-read
title_original: "First Measurement of the g Factor in the Chiral Band: The Case of the 128Cs Isomeric State"
authors: [E. Grodner, J. Srebrny, Ch. Droste, L. Próchniak, S. G. Rohoziński, M. Kowalczyk, M. Ionescu-Bujor, C. A. Ur, K. Starosta, T. Ahn, M. Kisieliński, T. Marchlewski, S. Aydin, F. Recchia, G. Georgiev, R. Lozeva, E. Fiori, M. Zielińska, Q. B. Chen, S. Q. Zhang, L. F. Yu, P. W. Zhao, J. Meng]
journal: "Physical Review Letters"
year: 2018
volume: 120
pages: "022502"
doi: "10.1103/PhysRevLett.120.022502"
canonical_source: "Grodner et al., Phys. Rev. Lett. 120, 022502 (2018)"
library_file: "raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf"
raw_sha256: "c71ec59160c444c34ab7f340db5f045c1f26456bc1741197ec62caea7f4efbf2"
nuclei: [128Cs, 128Xe]
reactions: [122Sn-10B-4n]
experiments: [TDPAD, GAMIPE, LEPS]
models: [particle-rotor, constrained-CDFT, angular-momentum-additivity]
observables: [g-factor, Larmor-precession, orientation-parameter, chiral-geometry]
methods: [time-differential-perturbed-angular-distribution]
tags: [128Cs, chirality, g-factor, TDPAD, planar-aplanar, particle-rotor]
---

# g factor of the `128Cs` chiral-band isomer

## Bibliographic Record

- E. Grodner *et al.*, *Phys. Rev. Lett.* **120**, 022502 (2018), DOI `10.1103/PhysRevLett.120.022502`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/g-factor/2018_Grodner et al_First Measurement of the g Factor in the Chiral Band.pdf`。

## Scope and Reading Depth

- PDF pp.022502-1–5 fully read: `122Sn(10B,4n)128Cs` production, TDPAD at two facilities, 56-ns isomer, Larmor fits/attenuation, angular-momentum additivity, generalized three-component g-factor equation, PRM+CDFT geometry and conclusions.
- Not covered: raw time spectra and full PRM/CDFT code.

## Key Results

- The `Iπ=9+`, `T1/2=56 ns` isomeric bandhead g factor is measured as `g=+0.59(1)` independently at Orsay and SUNY using TDPAD; `1/λ2≈300 ns` describes spin deorientation (PDF pp.1–3, Table I, Fig.2).
- A two-component `πh11/2⊗νh11/2^-1` additivity estimate gives `g≈0.50–0.52`, below experiment; the discrepancy requires nonzero even-even core rotation (`j_R=2,4,...`) and a three-vector g-factor relation (PDF pp.3–4, Eq.2, Table II).
- The generalized g factor depends on scalar products of `j_p`, `j_n`, and `j_R`; the normalized triple-product orientation `⟨(jp×jn)·jR⟩/sqrt(...)` is near zero for the fitted configuration. PRM+constrained-CDFT with `β≈0.23`, `γ≈23.8°` gives `g≈0.58` and an almost planar (`⟨ô⟩≈0.15`) bandhead rather than ideal chirality (PDF pp.4–5, Eqs.2–3, Fig.4).
- The result indicates a critical rotational frequency: characteristic chiral geometry may emerge only above a minimum spin/frequency, so low-spin bandheads with chiral-like transition patterns are not automatically static chiral configurations (PDF pp.1, 4–5).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR18-1 | `128Cs` isomer g factor is `+0.59(1)` from two independent TDPAD measurements. | experiment-result | direct | PDF pp.1–3, Table I | true |
| GR18-2 | The measured g factor requires core-rotation admixtures beyond a two-vector proton–neutron additivity model. | structure-inference | mixed | PDF pp.3–4, Eq.2, Table II | true |
| GR18-3 | PRM+CDFT reproduces the g factor for an almost planar bandhead, not ideal aplanar chirality. | geometry-result | mixed | PDF pp.4–5, Fig.4 | true |
| GR18-4 | Chiral geometry can have a critical-spin/frequency onset; transition fingerprints alone are insufficient at low spin. | interpretation-boundary | mixed | PDF pp.1, 4–5 | false |

## Summary

Grodner *et al.* provide a direct magnetic-moment geometry test of a proposed chiral band. The measured `g=0.59(1)` demonstrates the importance of core rotation and shifts the `128Cs` bandhead away from ideal static chirality; it is a strong counterexample to assigning low-spin chirality from near-degenerate bands and E2/M1 fingerprints alone.

## Competing Interpretations and Limitations

- The g-factor geometry inference relies on particle-rotor/CDFT configurations, core `g_R`, deformation and model-space choices.
- A near-planar bandhead does not rule out chiral geometry at higher spin; the conclusion is about spin-dependent onset, not the entire band.
- TDPAD attenuation, field calibration and spin assignment (`9+`) are experimental inputs; unobserved converted transitions in the level scheme remain a boundary.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GR18-AR-1 | TDPAD chain | Magnetic precession modulation `R(t)` → Larmor frequency → g factor with attenuation correction. | PDF Eq.1, Table I, Fig.2 | self-checking |
| GR18-AR-2 | Geometry chain | Three-vector g relation → scalar products/triple product → planar/aplanar orientation ranking. | PDF Eq.2–3, Fig.3 | self-checking |
| GR18-AR-3 | Transfer condition | Compare only with nucleus-specific PRM/CDFT and spin/frequency; g factor is a companion observable, not a universal chirality threshold. | PDF pp.3–5 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[nuclear-chirality]], [[tilted-axis-cranking]], [[g-factor-measurement]], [[time-differential-perturbed-angular-distribution]] and the counter-evidence map for chiral fingerprints.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `GR18-P0-1`: Preserve the distinction between measured g factor and model-inferred geometry; do not promote `g=0.59` into a universal planar/aplanar classifier.

## Extracted Pages

- Concepts/methods: [[nuclear-chirality]], [[tilted-axis-cranking]], [[g-factor-measurement]]。
