---
type: source
title: "von der Werth et al. 1995 - Two Compton polarimeter constructions for modern standard gamma spectroscopy"
aliases: [von der Werth 1995 POLALI MINIPOLA]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Two Compton polarimeter constructions for modern standard γ-spectroscopy"
authors: [A. von der Werth, F. Becker, J. Eberth, S. Freund, U. Hermkens, T. Mylaeus, S. Skoda, H. G. Thomas, W. Teichert]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1995
volume: 357
pages: "458-466"
pii: "0168-9002(95)00025-9"
canonical_source: "von der Werth et al., NIM A 357, 458-466 (1995)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1995_Von Der Werth et al_Two Compton polarimeter constructions for modern standard γ-spectroscopy.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1995_Von Der Werth et al_Two Compton polarimeter constructions for modern standard γ-spectroscopy.pdf"
raw_sha256: "54db57f926f99e069186e99a5b373ef5cb79f234eec43cc6ff84c82e80563021"
nuclei: [56Fe, 24Mg, 28Si, 66Zn, 67Zn]
reactions: [56Fe(p,pγ), 24Mg(p,pγ), 28Si(p,pγ), 66Zn(alpha,nγ), 67Zn(alpha,nγ)]
experiments: [cologne-polali-minipola]
models: [klein-nishina-response]
observables: [polarization-sensitivity, coincidence-efficiency, figure-of-merit, Compton-asymmetry]
methods: [compton-polarimetry, kinematic-Compton-gate]
tags: [POLALI, MINIPOLA, Compton, detector-response, Euroball]
---

# Two Compton polarimeter constructions for modern standard γ spectroscopy

## Bibliographic Record

- A. von der Werth *et al.*, *NIM A* **357**, 458–466 (1995), PII `0168-9002(95)00025-9`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1995_Von Der Werth et al_Two Compton polarimeter constructions for modern standard γ-spectroscopy.pdf`。
- 9-page method paper; title/PII, POLALI/MINIPOLA schematics, technical tables and calibration figures checked.

## Scope and Reading Depth

- PDF pp.458–466 fully read: five-detector POLALI, four-segment planar MINIPOLA, Klein–Nishina/asymmetry formalism, kinematic gate Eq.(8), Tables 1–3, Figs.1–10 and conclusions.
- Not covered: raw calibration matrices and modern Monte Carlo response.

## Method Logic and Key Evidence

- POLALI: a low-efficiency central HPGe scatterer plus four analyzers parallel/perpendicular to the reaction plane; list-mode `E_s,E_c` data are summed and gated by Compton kinematics (`θ∈70°–110°`) to reject multiple-scatter/background events.
- MINIPOLA: four-segment planar Ge in an anti-Compton shield; high coincidence efficiency but no unique scatterer/absorber ordering, so the full kinematic gate cannot be applied.
- Calibration uses known E2/E1/M1-E2 transitions (`56Fe`, `24Mg`, `28Si`, `66/67Zn`) to derive `Q=A/P`, geometric asymmetry and coincidence efficiency. Figure of merit is `F=Q²ε` (paper's notation).
- The paper reports POLALI high `Q` with lower efficiency and MINIPOLA lower `Q` with compact high efficiency; both are designed as modular devices for OSIRIS/NORDBALL/EUROBALL-era arrays.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VW95-1 | POLALI and MINIPOLA implement complementary sensitivity–efficiency compromises for modern γ arrays. | method-result | direct | PDF pp.458–462, Figs.1–5, Tables 1–2 | true |
| VW95-2 | POLALI's Compton-kinematic gate (`70°–110°`) suppresses multiple-scatter/background and raises sensitivity. | detector-response | direct | PDF pp.461–462, Eq.(8), Fig.6 | false |
| VW95-3 | `Q`, efficiency and `F=Q²ε` are calibrated across 0.18–2.5 MeV with known-polarization reactions and remain geometry/threshold specific. | method-validation | direct | PDF pp.462–466, Tables 2–3, Fig.10 | true |

## Summary

The POLALI/MINIPOLA paper is a practical detector-design bridge between historical Ge(Li) polarimeters and modern segmented arrays, explicitly separating sensitivity, efficiency, kinematic gating and figure of merit.

## Competing Interpretations and Limitations

POLALI's response depends on geometry, gate, threshold and gain matching; MINIPOLA's segmentation loses scatter-order information. Calibration lines and quoted `Q/F` values cannot be transplanted to another array without response simulation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| VW95-AR-1 | Response chain | Compton energies → kinematic angle gate → coincidence asymmetry → `Q/P` and `F`. | PDF pp.461–466 | self-checking |
| VW95-AR-2 | Transfer condition | Detector-specific `Q(E)`, efficiency and gate; modern use requires geometry and multiple-scatter audit. | Tables 1–3/Fig.10 | self-checking |
| VW95-AR-3 | Failure condition | Unordered MINIPOLA scatter, crosstalk, thresholds and background can bias asymmetry. | PDF pp.460–463 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]] and historical detector-response lineage with Garcia-Raffi 1995/1997 and Bass 1972.
- Persistence: update Compton method map and modern-array response protocol.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `VW95-P0-1`: POLALI/MINIPOLA `Q`, efficiency and `F` are device-specific; no universal calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
