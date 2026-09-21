---
type: source
title: "Freire-Fernández et al. 2024 - Measurement of the Isolated Nuclear Two-Photon Decay in 72Ge"
aliases: [Freire-Fernández 2024 isolated 2γ decay, 72Ge Schottky two-photon decay]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Measurement of the Isolated Nuclear Two-Photon Decay in 72Ge"
authors: [D. Freire-Fernández, W. Korten, R. J. Chen, S. Litvinov, Yu. A. Litvinov, M. S. Sanjari, H. Weick, et al.]
journal: "Physical Review Letters"
year: 2024
volume: 133
article: 022502
pages: "1-7"
doi: "10.1103/PhysRevLett.133.022502"
canonical_source: "https://doi.org/10.1103/PhysRevLett.133.022502"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2024_Freire-Fernandez et al_Measurement of the Isolated Nuclear Two-Photon Decay in 72 Ge.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2024_Freire-Fernandez et al_Measurement of the Isolated Nuclear Two-Photon Decay in 72 Ge.pdf"
raw_sha256: "3e35af6920c1c22c654fead0e1b9e36fa38ba2a2e39672f02011e65a62ad7dc7"
nuclei: [72Ge]
reactions: [78Kr+9Be-fragmentation]
experiments: [gsi-esr-schottky-isochronous-mass-spectrometry]
models: [second-order-electromagnetic-decay, shell-model-jj44-jun45]
observables: [two-photon-half-life, excitation-energy, electric-dipole-polarizability, magnetic-dipole-susceptibility, electric-quadrupole-polarizability]
methods: [Schottky-mass-spectrometry, isochronous-mass-spectrometry, storage-ring-lifetime]
tags: [two-photon-decay, 72Ge, isomer, storage-ring, Schottky, shape-coexistence]
---

# Measurement of the Isolated Nuclear Two-Photon Decay in 72Ge

## Bibliographic Record

- D. Freire-Fernández *et al.*, *Physical Review Letters* **133**, 022502 (2024), DOI `10.1103/PhysRevLett.133.022502`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2024_Freire-Fernandez et al_Measurement of the Isolated Nuclear Two-Photon Decay in 72 Ge.pdf`。
- 7-page open-access PRL; title/DOI, figures, Tables I–II and methods text checked. The batch's HS-116 file is the Walz 2015 supplementary information and is unrelated to this Freire-Fernández source; no Freire-Fernández supplement was supplied.

## Scope and Reading Depth

- PDF pp.1–7 fully read: 2γ formalism Eq.(1), storage-ring mass-spectrometry Eq.(2), S+IMS setup, Figs.1–2, Tables I–II, polarizability/susceptibility Eqs.(3–7), shell-model estimate, summary and future route.
- Figure/table audit: isomer/ground-state frequency-time spectrogram, half-life systematics, all lifetime/excitation-energy rows and uncertainty explanations.
- Not covered: raw Schottky spectra, `iqtools/rionid` code, a Freire-Fernández supplementary file and full shell-model matrix-element files.

## Paper Question and Experimental Logic

The paper asks whether the isolated two-photon decay of the low-lying `0_2^+` state in bare `72Ge32+` can be measured directly without γ-ray background, and whether the decay rate reveals unexpectedly large electric-dipole polarizability in a midshell nucleus.

1. Produce `72Ge` fragments from 441-MeV/u `78Kr` on 10-mm `9Be`, inject fully stripped ions into the ESR and use isochronous ion optics (`γ≈γ_t≈1.396`) to convert revolution frequency into mass/charge.
2. Use nondestructive 410- and 245-MHz Schottky resonant cavities to resolve `72mGe32+` from `72gGe32+` and follow the isomer population over milliseconds without foil detectors.
3. Fit exponential decay of the isomer trace, correct laboratory half-lives by Lorentz factors, derive excitation energy from frequency differences and compare the isolated 2γ half-life to previous high-energy two-photon data and Eq.(1) polarizability scaling.

## Key Evidence and Reasoning Chain

- The first excited `0+` isomer has measured `T1/2(rest)=23.9(6) ms` and `ω0=692.8(19) keV`; the isomeric ratio is `3.4(2)%` (Tables I–II, Fig.2).
- The measured half-life is about ten times shorter than the extrapolation from `16O`, `40Ca` and `90Zr`, implying `|M2γγ|≈70(2)×10⁻3 fm³` and a much larger cumulative polarizability than the doubly magic cases.
- Shell-model `jj44/JUN45` estimates give `|χM1|≈3.8×10⁻3 fm³` and `|αE2|≈4749 fm⁵`, corresponding `|ME2|≈0.8×10⁻3 fm³`; the authors therefore infer that enhanced electric-dipole polarizability likely dominates, but cannot separate `αE1` and `χM1` without γ angular correlations.
- The technique measures an isolated 2γ decay branch in bare ions, removing internal conversion and most direct/indirect photon backgrounds. It is not a γγ coincidence measurement and cannot independently determine the E1/M1 multipole mixture.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FF24-1 | Combined Schottky plus isochronous mass spectrometry directly measures the isolated `0_2^+→0_1^+` 2γ partial half-life in bare `72Ge32+`. | experimental-method-result | direct | PDF pp.1–5, Figs.1–2, Table I | true |
| FF24-2 | The rest-frame half-life is `23.9(6) ms` and excitation energy `692.8(19) keV`; isomeric ratio is `3.4(2)%`. | experimental-result | direct | PDF pp.4–5, Tables I–II | true |
| FF24-3 | The half-life is about ten times shorter than the previous scaling law, implying `M2γγ≈70(2)×10⁻3 fm³`. | experimental-result/derived | mixed | PDF p.4, Fig.2 and Eq.(1) | true |
| FF24-4 | Shell-model estimates suggest E1 polarizability dominates over M1 susceptibility/E2 polarizability, but individual terms cannot be separated without γ angular correlations. | model-inference | indirect | PDF pp.5–6, Eqs.(3–7) | true |
| FF24-5 | S+IMS extends nondestructive lifetime spectroscopy to isomers near 100 keV and millisecond half-lives. | method-result | direct | PDF pp.1, 5–6, Summary | false |

## Summary

Freire-Fernández *et al.* introduce a background-suppressed storage-ring method and directly measure the low-energy 2γ decay of bare `72Ge32+`. The unexpectedly short half-life is strong evidence for enhanced cumulative polarizability, while the E1/M1/E2 decomposition remains an open model-and-observable problem.

## Competing Interpretations and Limitations

The shorter half-life could reflect enhanced E1 polarizability, M1 susceptibility, E2 polarizability or a combination; shell-model estimates are incomplete because the `jj44` space omits relevant spin-orbit transitions and `0+` states are strongly mixed. Without γ angular correlations, the experiment measures the total `M2γγ`, not each multipole contribution. Ion-loss, frequency-resolution, Lorentz-correction and isomer-population systematics are controlled in the paper but raw traces/code are not supplied.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| FF24-AR-1 | Observable chain | Schottky peak area vs time → exponential decay → rest-frame half-life → Eq.(1) cumulative 2γ matrix element. | PDF pp.3–5, Fig.2, Table I | self-checking |
| FF24-AR-2 | Isolation condition | Bare ions suppress IC; S+IMS avoids destructive foil detectors and direct γ background. | PDF pp.2–4 | self-checking |
| FF24-AR-3 | Model decomposition | M1/E2 terms are estimates, not separately measured; E1 dominance is a calibrated inference. | PDF pp.5–6, Eqs.3–7 | provisional |
| FF24-AR-4 | Failure condition | Missing raw Schottky traces, code, shell-model files and SI prevent a full independent rerun; background/ion-loss and frequency fits remain source-local. | PDF pp.3–6 | active-L3 |
| FF24-AR-5 | Lineage | Extends Schirmer 1984/Gade/Walz-style two-photon evidence but uses a different storage-ring observable; it is not a γγ detector experiment. | Introduction and methods | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[two-photon-nuclear-decay]] and `revises` the method map by adding a direct isolated-ion lifetime route below the pair-creation threshold; it also opens an L3 question on separating polarizability components.
- Persistence: update the two-photon concept and rare-branch method map; retain the missing Freire-Fernández raw/code boundary.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[two-photon-nuclear-decay]] | Direct isolated `0+→0+` 2γ lifetime, complementary to γγ spectroscopy. |
| methodological-bridge | [[storage-ring-mass-spectrometry]] | S+IMS/Schottky method for nondestructive isomer lifetime and energy. |
| limits | [[schirmer-1984-double-gamma-40ca-90zr]] | Different observable: no angular-correlation multipole separation in the storage-ring result. |
| candidate-L3 | [[a130-high-spin-collective-modes-evidence-map]] | General rare-branch observable design, not an A≈130 direct source. |

## Human Review Triage

### P0

- `FF24-P0-1`: quote `23.9(6) ms` and `M2γγ` only as total isolated-branch results; do not state E1 dominance as directly measured until angular correlations or complete SI/model inputs are checked.

### P1

- `FF24-P1-1`: shell-model `jj44/JUN45` M1/E2 estimates and omitted orbital contributions limit the decomposition of the total matrix element.
- `FF24-P1-2`: Raw Schottky spectra, analysis artifacts and any Freire-Fernández supplementary file remain unavailable.

## Extracted Pages

- Concepts: [[two-photon-nuclear-decay]]。
- Methods: [[storage-ring-mass-spectrometry]]。
- Source lineage: [[schirmer-1984-double-gamma-40ca-90zr]], [[gade-2015-gamma-rays-come-in-twos]]。

## L3/L4 Follow-up

- L3 question: can storage-ring total 2γ rates plus γ angular-correlation or shell-model constraints separate `αE1`, `χM1` and `αE2` contributions across low-lying `0+` states? Discriminants are angular distributions, shell-model spaces and independent lifetime/branching data.
- No L4 run: raw Schottky time traces, SI/code and complete matrix-element inputs are not yet available locally.
