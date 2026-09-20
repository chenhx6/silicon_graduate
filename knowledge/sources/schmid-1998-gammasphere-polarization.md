---
type: source
title: "Schmid et al. 1998 - Gamma-ray polarization sensitivity of the Gammasphere segmented germanium detectors"
aliases: [Schmid 1998 Gammasphere polarization]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method-paper-and-application
reading_depth: deep-read
title_original: "Gamma-ray polarization sensitivity of the Gammasphere segmented germanium detectors"
authors: [G. J. Schmid, A. O. Macchiavelli, S. J. Asztalos, R. M. Clark, M. A. Deleplanque, R. M. Diamond, P. Fallon, R. Kruecken, I. Y. Lee, R. W. MacLeod, F. S. Stephens, K. Vetter]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1998
volume: 417
pages: "95-110"
pii: "S0168-9002(98)00624-X"
canonical_source: "Schmid et al., NIM A 417, 95-110 (1998)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium.pdf"
raw_sha256: "66502edb2f0ff2d09321d3b388767ea98736b83865b90f128fdd1e46921b2a2c"
alternate_versions: ["raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium2.pdf"]
alternate_sha256: "bdb397650e5b8cc92f358e386f52703604dd0962184364004eb8985f76998558"
nuclei: [56Fe, 24Mg, 109Ag, 197Pb, 176Yb]
reactions: [24Mg(p,pγ), 56Fe(p,pγ), 109Ag(p,pγ), 176Yb(26Mg,5n)197Pb]
experiments: [gammasphere-polarimetry]
models: [Klein-Nishina-response, shears-mechanism]
observables: [polarization-sensitivity, Compton-asymmetry, parity, Q(E), figure-of-merit]
methods: [compton-polarimetry, Monte-Carlo-detector-response]
tags: [Gammasphere, segmented-Ge, polarization, detector-response, 197Pb]
---

# Gamma-ray polarization sensitivity of Gammasphere segmented Ge detectors

## Bibliographic Record

- G. J. Schmid *et al.*, *NIM A* **417**, 95–110 (1998), PII `S0168-9002(98)00624-X`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium.pdf`。

## Scope and Reading Depth

- PDF pp.95–110 fully read: segmented detector design/Doppler correction, Klein–Nishina polarization formalism, conventional and two-fold definitions, calibration reactions, Monte Carlo, Tables/Figs.1–10 and `197Pb` shears-band application.
- Not covered: raw Gammasphere matrices and full Monte Carlo source.
- Alternate-version audit: the 44-page LBNL-41340 preprint/eScholarship copy was reread by section (Secs.1–7, calibration, Monte Carlo and `197Pb` application). It is an earlier/alternate presentation of the same NIM A source, not an independent experiment; no material claim change was found.

## Key Results

- Gammasphere segmented Ge detectors used as two-fold Compton polarimeters yield `Q(E)` from about 5% at 415 keV to 4% at 1368 keV; Monte Carlo agrees within ~20% over measured energies.
- Segmentation improves Doppler resolution and permits confined/shared event asymmetry, but cannot measure a true up/down versus left/right asymmetry without detector rotation; new definitions are required.
- High-background `176Yb(26Mg,5n)197Pb` data demonstrate the sign of linear polarization and support negative parity for Shears Band 1, despite relatively poor sensitivity.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SG98-1 | Segmented Gammasphere Ge detectors provide a low-sensitivity but practical two-fold Compton polarimeter for high-spin arrays. | method-result | direct | PDF pp.95–100 | true |
| SG98-2 | Experimental `Q(E)` and Monte Carlo response agree within about 20% from 415–1368 keV. | method-validation | direct | PDF pp.95–110, Fig.10 | true |
| SG98-3 | A high-background `197Pb` application uses polarization sign to support negative parity of Shears Band 1. | application-result | mixed | PDF pp.95–110, application section | true |

## Summary

Schmid *et al.* establish the Gammasphere segmented-Ge response layer, its new confined/shared asymmetry definition and its limitations in high-background high-spin spectroscopy.

## Competing Interpretations and Limitations

Detector segmentation, energy thresholds, geometry, response Monte Carlo and background determine `Q`; polarization sign alone is not a complete parity proof without multipolarity/configuration context. The `197Pb` parity application remains source-specific.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SG98-AR-1 | Response chain | Segmented charge signals → confined/shared counts → calibrated asymmetry → `Q(E)` → `P`. | PDF Secs.2–3 | self-checking |
| SG98-AR-2 | Transfer condition | `Q` and 20% simulation agreement are geometry/energy/background-specific. | PDF Tables/Figs. | self-checking |
| SG98-AR-3 | Failure condition | No detector rotation, crosstalk/background and weak statistics limit asymmetry/parity inference. | PDF Sec.3/application | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]] and high-spin parity/multipolarity evidence map.
- Persistence: link to Simpson/Garcia-Raffi/Bass/von der Werth detector lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SG98-P0-1`: Gammasphere `Q(E)` and parity inference are array/background specific; preserve detector-response calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
