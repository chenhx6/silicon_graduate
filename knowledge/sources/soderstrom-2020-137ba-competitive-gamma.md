---
type: source
title: "Söderström et al. 2020 - Electromagnetic character of the competitive gamma-gamma/gamma decay from 137mBa"
aliases: [Soderstrom 2020 137Ba competitive double gamma]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic character of the competitive γγ/γ-decay from 137mBa"
authors: [P.-A. Söderström, L. Capponi, E. Açıksöz, T. Otsuka, N. Tsoneva, Y. Tsunoda, D. L. Balabanski, N. Pietralla, G. L. Guardo, D. Lattuada, H. Lenske, C. Matei, D. Nichita, A. Pappalardo, T. Petruse]
journal: "Nature Communications"
year: 2020
volume: 11
pages: "3242"
doi: "10.1038/s41467-020-16787-4"
canonical_source: "https://doi.org/10.1038/s41467-020-16787-4"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2020_Söderström et al_Electromagnetic character of the competitive γγ-γ-decay from 137mBa.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2020_Söderström et al_Electromagnetic character of the competitive γγ-γ-decay from 137mBa.pdf"
raw_sha256: "fb8bd159bae6e5f1e2b9827e1bf2bce7cd98c126c7fef00f1bd41526154ec12a"
nuclei: [137Ba, 137Cs, 152Sm]
reactions: [137Cs-beta-decay]
experiments: [ELIGANT, CeBr3, ELI-NP]
models: [EDF-QPM, Monte-Carlo-shell-model, GEANT4]
observables: [competitive-two-photon-branching, energy-sharing, angular-correlation, alpha-M2E2, alpha-E3M1]
methods: [gamma-gamma-coincidence, fast-timing, angular-correlation]
tags: [137Ba, competitive-double-gamma, two-photon-decay, polarizability, E3M1]
---

# Electromagnetic character of the competitive γγ/γ decay from `137mBa`

## Bibliographic Record

- P.-A. Söderström *et al.*, *Nature Communications* **11**, 3242 (2020), DOI `10.1038/s41467-020-16787-4`.

## Scope and Reading Depth

- The eight-page open-access article was read end-to-end: motivation, Fig.1 decay scheme, Table 1, eleven-CeBr3 setup, Figs.2–5, differential-branching definition, energy-sharing fit, EDF+QPM/MCSM discussion, Methods Eqs.(6–9), Tables 2 and data/code availability.

## Independent Measurement

The experiment uses eleven 3''×3'' CeBr3 detectors at 40 cm, with 32.7° nearest-neighbor spacing and five correlation angles `32.7°, 65.5°, 98.2°, 130.9°, 163.6°`; ≥15 cm lead separates neighboring detectors. A 152Eu/60Co calibration and GEANT4 toolkit characterize efficiency and geometry (PDF pp.3–4, Fig.2). A `336 kBq 137Cs` source was run for 49.5 active days. Prompt coincidences use `|Δt|≤655 ps`; uncorrelated events use a 20–820 ns side window. Multiplicity-two and energy-difference cuts suppress cosmic-ray and backscatter backgrounds (pp.3–4, Fig.3).

The summed peak contains `990(170)` counts before final cuts and `960(100)` after the cosmic-ray condition (Fig.3). The differential branching ratio integrates `E_low=180` to `331 keV` (half the 662-keV transition) and is evaluated at all detector angles (p.4, Eq.4). Combined with the energy-sharing distribution, the fit gives `Γγγ/Γγ=2.62(30)×10−6` at `8.7σ`, compared with Walz's `2.05(37)×10−6` (Table 1, Figs.4–5).

## Electromagnetic Character and Model Comparison

Pure M2E2 and E3M1 paths have different energy-sharing shapes: M2E2 peaks near equal `331/331 keV`, while E3M1 is asymmetric near about `200/442 keV` (pp.4–5, Fig.5a). Angular data alone have two χ² minima; simultaneous angle plus energy-sharing data favor a substantial `αE3M1` and much smaller `αM2E2` than the original Walz interpretation (Fig.5b). Table 1 reports the present fitted values `αM2E2=±8.8(50)` and `αE3M1=±36.4(20) e²fm⁴/MeV` (sign branches), while EDF+QPM and MCSM give different `αM2E2` signs/magnitudes and more consistent E3M1 contributions.

The paper's MCSM analysis finds a strongly hindered `M2` transition (`B(M2)=13.5×10−3 μ²fm²`, about three orders below the EDF+QPM value), explaining suppression of the quadrupole–quadrupole component; EDF+QPM attributes E3M1 strength to a collective octupole phonon (pp.5–6, Table 2). The authors stress that model complexity does not yet resolve the remaining α-component discrepancy.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SO20-1 | An independent eleven-CeBr3 experiment confirms the `137mBa` competitive branch at `8.7σ` with `2.62(30)×10−6`. | experiment-result | direct | PDF pp.1, 3–5, Table 1 | true |
| SO20-2 | Energy-sharing data favor a substantial E3M1 contribution and a smaller M2E2 component. | path-discrimination | mixed | PDF pp.4–6, Figs.4–5 | true |
| SO20-3 | EDF+QPM and MCSM disagree on the quadrupole component; the MCSM M2 hindrance is a candidate explanation. | model-conflict | mixed | PDF pp.5–6, Tables 1–2 | true |

## Summary

Söderström *et al.* provide an independent total-branch confirmation and the strongest within-batch evidence that energy sharing, not angular correlation alone, is needed to identify the virtual multipole path.

## Competing Interpretations and Limitations

- Angular-only fits have local minima and the fitted α signs/order remain branch-dependent.
- Detector response, efficiency and cosmic-ray/Compton cuts are setup-specific; raw data and code are not openly deposited.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| SO20-AR-1 | Signal/background chain | Five angular points, time sideband, multiplicity/energy cuts and GEANT4/Gaussian fits jointly support a competitive branch; cosmic-ray and Compton residuals remain systematics. | PDF pp.3–5, Figs.2–4 | self-checking |
| SO20-AR-2 | Path identifiability | Angular correlation alone is degenerate; energy-sharing breaks the M2E2/E3M1 ambiguity but still leaves sign/ordering branches and model dependence. | PDF pp.4–6, Fig.5, Eq.5 | self-checking |
| SO20-AR-3 | Cross-paper conflict | The result directly revises Walz's dominant-Aqq interpretation while agreeing on the total branch within errors; it is a same-nucleus independent experiment, not a duplicate PDF. | PDF pp.1, 4–6, Table 1 | self-checking |
| SO20-AR-4 | Reproducibility | Final data points are deposited at the stated Mendeley DOI, while raw data and sorting/analysis code are available from authors on request. | PDF p.7, Data/Code availability | input-limited-L4 |

## Knowledge Impact and Learning Decision

- Effect: `revises` [[walz-2015-competitive-double-gamma-137ba]], [[two-photon-nuclear-decay]] and the `137Ba` polarizability evidence map; it promotes energy-sharing as the decisive companion observable for virtual-path identification.
- L3/L4: a public final-data DOI makes a limited re-analysis candidate, but raw detector response and full code are not public; no independent L4 re-fit is claimed here.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SO20-P0-1`: Before numerical reuse, reconcile the sign/ordering branches, detector-efficiency correction and the Walz/Söderström common definition of δ; preserve the model discrepancy instead of selecting one path by label.

## Extracted Pages

- Source relation: [[walz-2015-competitive-double-gamma-137ba]], [[two-photon-nuclear-decay]]。
- Methods/models: [[gamma-gamma-coincidence]], [[angular-correlation]]。
