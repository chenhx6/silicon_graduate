---
type: source
title: "Schlitt et al. 1994 - Sectored Ge Compton polarimeter for parity assignments"
aliases: [Schlitt 1994 sectored Ge polarimeter]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: method-paper-and-application
reading_depth: deep-read
title_original: "A sectored Ge-Compton polarimeter for parity assignments in photon scattering experiments"
authors: [B. Schlitt, U. Maier, H. Friedrichs, S. Albers, J. Bauske, P. von Brentano, R. D. Heil, R.-D. Herzberg, U. Kneissl, J. Margraf, H. H. Pitz, C. Wesselborg, A. Zilges]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1994
volume: 337
pages: "416-426"
pii: "0168-9002(94)91111-8"
canonical_source: "Schlitt et al., NIM A 337, 416-426 (1994)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1994_Schlitt et al_A sectored Ge-Compton polarimeter for parity assignments in photon scattering.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1994_Schlitt et al_A sectored Ge-Compton polarimeter for parity assignments in photon scattering.pdf"
raw_sha256: "d23380e6a8bea4be9e77c845ba125f3b934765744bad6a1f300a3301aae07684"
nuclei: [106Pd, 24Mg, 28Si, 12C, 162Dy]
reactions: [106Pd-gamma-gamma, 24Mg-p-p-gamma, 28Si-p-p-gamma, 12C-p-p-gamma, NRF]
experiments: [fourfold-sectored-Ge, Stuttgart-Dynamitron]
models: [Klein-Nishina, angular-correlation]
observables: [polarization, parity, Q, figure-of-merit, Compton-asymmetry]
methods: [Compton-polarimetry, photon-scattering]
tags: [sectored-Ge, Compton-polarimeter, parity, NRF, polarization]
---

# Sectored Ge Compton polarimeter for parity assignments

## Bibliographic Record

- B. Schlitt *et al.*, *NIM A* **337**, 416–426 (1994), PII `0168-9002(94)91111-8`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1994_Schlitt et al_A sectored Ge-Compton polarimeter for parity assignments in photon scattering.pdf`。

## Scope and Reading Depth

- PDF pp.416–426 fully read: polarization formalism, fourfold single-crystal Ge design, `Q(E)` calibration with `106Pd`/`24Mg`/`28Si`/`12C`, figure of merit, NRF `162Dy` application and appendix two-detector proposal.
- Not covered: raw calibration spectra and later tracking-array implementations.

## Key Results

- A true coaxial p-type Ge crystal with four insulated outer sectors provides horizontal/vertical Compton coincidences while the core measures total incident energy; apparatus asymmetry is below about 1% at 2–4 MeV (PDF pp.417–420, Figs.5–6).
- Calibrated sensitivity is about 20% at 0.5 MeV and 9.5% at 4.4 MeV, with `Q(E)=γCE(θ=90°)(a+bE)` and measured `a=0.304(16)`, `b=(8.9±0.8)×10^-5 keV^-1` for 150-keV thresholds (PDF pp.418–423, Table 3, Fig.11).
- The polarimeter has about 25% total efficiency, ≈25% coincidence efficiency near 3 MeV and a figure of merit comparable to four-crystal systems; the direct core-energy signal avoids summing-energy resolution loss (PDF pp.419–425, Table 4).
- NRF `162Dy` spectra demonstrate parity assignments: positive azimuthal asymmetry corresponds to M1/positive parity and negative to E1/negative parity, with weakly polarized lines suppressed in the difference spectrum (PDF pp.423–425, Figs.15–16).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SC94-1 | Fourfold sectored Ge provides a compact high-efficiency Compton polarimeter for NRF parity assignments. | method-result | direct | PDF pp.416–420, Table 4 | true |
| SC94-2 | `Q(E)` declines from ~20% at 0.5 MeV to ~9.5% at 4.4 MeV for the tested thresholds/geometry. | calibration-result | direct | PDF pp.421–423, Table 3, Fig.11 | true |
| SC94-3 | NRF `162Dy` parity signs are demonstrated with sum/difference spectra. | application-result | mixed | PDF pp.423–425, Figs.15–16 | true |

## Summary

Schlitt *et al.* establish a sectored-Ge polarimeter optimized for photon-scattering parity assignments. It trades some sensitivity against high coincidence efficiency and energy resolution, making detector geometry, thresholds and calibration central to any parity claim.

## Competing Interpretations and Limitations

- `Q(E)` and figure-of-merit values are geometry/threshold dependent; finite solid angle shifts the ideal Klein–Nishina analyzing power.
- Polarization sign determines parity only with known angular distribution/multipolarity and response correction.
- The NRF application is not equivalent to in-beam fusion-evaporation clover polarimetry; reaction-plane and alignment conventions differ.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SC94-AR-1 | Response chain | Sectored Compton H/V events → asymmetry `ε=QP` with `a(E)` correction → parity sign. | PDF Eqs.1–17, pp.417–423 | self-checking |
| SC94-AR-2 | Performance chain | `Q² ε_coin` → figure of merit; compare only at common energy/threshold. | PDF Eqs.26, Table 4 | self-checking |
| SC94-AR-3 | Transfer condition | Recalibrate geometry, thresholds and reaction-plane convention for modern arrays. | PDF pp.423–426 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and historical detector-response map.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SC94-P0-1`: Preserve detector/threshold/NRF convention boundaries; do not transfer `Q` or parity sign directly to another geometry.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
