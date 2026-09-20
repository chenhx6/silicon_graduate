---
type: source
title: "Bass et al. 1972 - Symmetrical two-crystal Compton polarimeter for gamma rays"
aliases: [Bass 1972 two-crystal polarimeter]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Symmetrical two-crystal Compton polarimeter for gamma rays"
authors: [R. Bass, S. Brinkmann, C. von Charzewski, H. Hanle]
journal: "Nuclear Instruments and Methods"
year: 1972
volume: 104
pages: "33-43"
pii: "0029-554X(72)90293-5"
canonical_source: "Bass et al., Nucl. Instr. Methods 104, 33-43 (1972)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1972_Bass et al_Symmetrical two-crystal compton polarimeter for gamma rays.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1972_Bass et al_Symmetrical two-crystal compton polarimeter for gamma rays.pdf"
raw_sha256: "4f6bfed154b9c2dbe60bae672a2a998f3777b31879746ffeff5bd63040d3994d"
nuclei: [40Ar, 24Mg, 60Co]
reactions: [24Mg(p,p'γ), 56Fe(p,p'γ)]
experiments: [frankfurt-two-crystal-polarimeter]
models: [klein-nishina-scattering]
observables: [polarization-sensitivity, coincidence-efficiency, peak-to-compton]
methods: [compton-polarimetry]
tags: [Compton-polarimeter, two-crystal, detector-response, polarization]
---

# Symmetrical two-crystal Compton polarimeter for gamma rays

## Bibliographic Record

- R. Bass *et al.*, *Nuclear Instruments and Methods* **104**, 33–43 (1972), PII `0029-554X(72)90293-5`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1972_Bass et al_Symmetrical two-crystal compton polarimeter for gamma rays.pdf`。
- 11-page method paper; title/author/PII and NaI/Ge(Li) test geometry checked.

## Scope and Reading Depth

- PDF pp.33–43 fully read: symmetric two-crystal principle, threshold/angle acceptance, polarized-source production, NaI and Ge(Li) construction, Tables 1–3, Figs.1–7, coincidence/anticoincidence response and conclusions.
- Not covered: raw spectra, modern Monte Carlo response and later detector implementations.

## Method Logic and Key Evidence

- Two massive crystals touch along an interface parallel to the incident beam; rotate the interface between 0°/90°, use coincidence-to-anticoincidence full-energy counts `N(φ)` and define `Q=[N(0)-N(90)]/[N(0)+N(90)]=R P`.
- Equal threshold `E_th` selects an effective Compton-angle range; lower thresholds raise efficiency but change `R`. The paper maps threshold versus accepted scattering angle (Fig.2).
- NaI tests cover 0.2–4.4 MeV; Ge(Li) tests use 28-cm³ coaxial crystals and thresholds 50–1500 keV. Coincidence operation improves peak-to-Compton and suppresses photoelectric/escape backgrounds.
- Detector-specific tables report efficiency ratio `N` and polarization sensitivity `R`; values vary strongly with energy and threshold (Tables 2–3), so they are not universal constants.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BA72-1 | Symmetric two-crystal coincidence/anticoincidence asymmetry measures incident linear polarization with efficiency `R`. | method-result | direct | PDF pp.33–35, Eqs./Figs.1–2 | false |
| BA72-2 | Threshold controls accepted Compton angles and the sensitivity–efficiency trade-off. | detector-response | direct | PDF pp.34–36, Fig.2, Tables 2–3 | false |
| BA72-3 | NaI/Ge(Li) tests achieve usable sensitivity over 0.2–4.4 MeV and improve peak-to-Compton compared with anticoincidence/singles. | method-validation | direct | PDF pp.35–43, Tables 1–3, Figs.6–7 | true |

## Summary

Bass *et al.* establish a compact symmetric two-crystal Compton polarimeter whose threshold-dependent coincidence asymmetry trades efficiency against polarization sensitivity and improves spectral background conditions.

## Competing Interpretations and Limitations

`R` depends on crystal geometry, threshold, energy, source distance and angular acceptance; alignment, gain matching, accidental coincidences and multiple scattering require calibration. Historical values should not be transferred to modern arrays without response simulation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BA72-AR-1 | Formula chain | Compton coincidence/anticoincidence counts → asymmetry `Q` → calibrated `R` → physical polarization `P`. | PDF pp.33–35 | self-checking |
| BA72-AR-2 | Transfer condition | Use only with matched threshold/geometry and detector-specific `R(E,E_th)`. | PDF Tables 2–3 | self-checking |
| BA72-AR-3 | Failure condition | Multiple scattering, background/gain mismatch and threshold-dependent angle acceptance can bias `R`. | PDF pp.34–43 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` detector-response lineage for [[compton-polarimetry]] and [[linear-polarization-asymmetry]].
- Persistence: add source to Compton method map; preserve `R`/efficiency separation.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[compton-polarimetry]] | Early symmetric two-crystal geometry and threshold-dependent `R`. |
| supports | [[linear-polarization-asymmetry]] | Detector-level asymmetry and response calibration. |

## Human Review Triage

### P0

- `BA72-P0-1`: quoted `R` values are detector/threshold-specific and cannot be used as modern universal calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
