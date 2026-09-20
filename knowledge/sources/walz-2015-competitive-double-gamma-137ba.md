---
type: source
title: "Walz et al. 2015 - Observation of the competitive double-gamma nuclear decay"
aliases: [Walz 2015 137Ba competitive 2γ decay]
created: 2026-09-20
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Observation of the competitive double-gamma nuclear decay"
authors: [C. Walz, H. Scheit, N. Pietralla, T. Aumann, R. Lefol, V. Yu. Ponomarev]
journal: Nature
year: 2015
volume: 526
pages: "406-409"
doi: "10.1038/nature15543"
canonical_source: "https://doi.org/10.1038/nature15543"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2015_Walz et al_Observation of the competitive double-gamma nuclear decay.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2015_Walz et al_Observation of the competitive double-gamma nuclear decay.pdf"
raw_sha256: "4177a89672ef1362d9dc35ff1292c7550c2db477fe34b61abaec4c72475b9c45"
supplementary_raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/SUPPLEMENTARY INFORMATION.pdf"
supplementary_raw_sha256: "e02bb09bae8f80252a4dca64fe2d487d2c05f292abda1f3a5249ff614a70e2d9"
nuclei: [137Ba, 137Cs]
reactions: [137Cs-beta-decay]
experiments: [laBr3-five-detector-double-gamma]
models: [quasiparticle-phonon-model, second-order-electromagnetic-decay]
observables: [competitive-two-photon-branching, gamma-gamma-angular-correlation, energy-sum-spectrum, time-correlation, aE2M2, aM1E3]
methods: [gamma-gamma-coincidence, fast-timing, angular-correlation]
tags: [137Ba, competitive-double-gamma, two-photon-decay, LaBr3, QPM]
---

# Observation of the competitive double-gamma nuclear decay

## Bibliographic Record

- C. Walz *et al.*, *Nature* **526**, 406–409 (2015), DOI `10.1038/nature15543`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2015_Walz et al_Observation of the competitive double-gamma nuclear decay.pdf`。
- 4-page Nature Letter; the separate `SUPPLEMENTARY INFORMATION.pdf` in the batch is attached material audited as HS-116, not an independent experiment.

## Scope and Reading Depth

- PDF pp.406–409 fully read: setup/obstacles, Figs.1–4, energy/time gates, background subtraction, angular-correlation formalism Eq.(1–2), Table 1, QPM comparison and conclusion.
- Figure audit: five-LaBr3 geometry and Compton/random backgrounds (Fig.1), 72° energy/time spectra and level scheme (Fig.2), 144° spectrum (Fig.3), fitted energy/angular correlation and QPM terms (Fig.4).
- The attached 14-page Supplementary Information (HS-116) was read end-to-end, including Methods, Eqs. (2–19), Supplementary Tables 1–4 and Supplementary Fig. 1. Raw spectra, detector-response files and full QPM inputs remain unavailable.

## Paper Question and Experimental Logic

The experiment asks whether a very weak double-γ branch can compete directly with an allowed single-γ decay from the `11/2−` 661.66-keV isomer of `137Ba`, and whether its energy/angle dependence identifies the virtual multipole paths.

1. Populate the `137Ba` isomer through `137Cs` β− decay; record 52.7 days with five large-volume LaBr3:Ce detectors at 72° and 144° pair openings, thick lead shields and `|Δt|≤1.2 ns` prompt gates.
2. Subtract random coincidences using a wide `20–76 ns` side gate and suppress Compton backgrounds with lead plus `|E1−E2|<300 keV` (72°) or `<250 keV` (144°).
3. Fit the continuous energy spectrum and angular correlation to the coherent quadrupole–quadrupole (`Aqq`, `aE2M2`), octupole–dipole (`Aod`, `aM1E3`) and interference (`Ax`) terms of Eq.(1), while excluding sequential decay through the 283.5-keV `1/2+` state.

## Key Evidence and Reasoning Chain

- The 72° energy-sum peak at `661.6(1.6) keV` has `693(95)` counts after random subtraction; its time-difference spectrum is centered at zero with about 1 ns FWHM, inconsistent with Compton-scatter delays of ±0.8 ns.
- Individual photon energies are continuous rather than peaking at the sequential 283.5-keV cascade energies, excluding the main sequential-decay alternative. The allowed single-γ branch to the ground state is much stronger, so the measured ratio is a competitive branch.
- The 144° group gives a consistent peak at `664.2(2.8) keV` with `307(78)` counts, establishing a pronounced angular correlation.
- Simultaneous energy/angular fitting yields `Γγγ/Γγ=(2.05±0.37)×10⁻6`, `aE2M2=133.9(2.8) e²fm⁴MeV⁻1` and `aM1E3=110.1(4.2) e²fm⁴MeV⁻1`; QPM predicts 2.69×10⁻6, 142.60 and 19.50 respectively (Table 1). The dominant `Aqq` term and positive interference sign are reported; the QPM `aM1E3` mismatch is a model-level discrepancy.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W15-1 | A competitive double-γ branch from the `137Ba` `11/2−` isomer is observed with branching ratio `(2.05±0.37)×10⁻6` relative to the allowed single-γ decay. | experimental-result | direct | PDF pp.406–409, Figs.2–4, Table 1 | true |
| W15-2 | Energy-sum, continuous individual-photon spectra, prompt timing and 72°/144° angular correlation exclude dominant Compton, random or sequential-decay alternatives. | background-control | direct | PDF pp.406–408, Figs.1–3 | true |
| W15-3 | The double-γ differential width is dominated by the `Aqq` E2–M2 path with an interference contribution from `Aod` M1–E3. | model-data-result | mixed | PDF pp.408–409, Eq.(1), Fig.4, Table 1 | true |
| W15-4 | QPM reproduces the total branch and `aE2M2` reasonably but predicts a smaller `aM1E3`; the matrix-element interpretation remains model-dependent. | model-comparison | mixed | PDF p.408, Fig.4, Table 1 | true |

## Summary

Walz *et al.* provide the first firm observation of a competitive nuclear double-γ decay in a transition where single-γ decay is allowed. Joint energy, timing and angular evidence suppress backgrounds, while the fitted multipole-path coefficients expose new off-diagonal polarizability/susceptibility information.

## Competing Interpretations and Limitations

Residual Compton scattering, random coincidences and sequential decay are addressed but depend on lead shielding, timing/energy gates and sideband scaling. The multipole-path decomposition is based on second-order formalism and QPM comparison; it is not a direct measurement of each virtual-state sum. The Supplement fixes the efficiency/gate and QPM bookkeeping, but raw spectra, detector-response files and full QPM inputs remain necessary for a complete independent re-fit.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| W15-AR-1 | Background chain | Prompt timing + random sideband + energy-difference cut + lead shield + angular cross-check form a joint background test. | PDF Figs.1–3 | self-checking |
| W15-AR-2 | Sequential alternative | Continuous photon spectra and no delayed cascade signature disfavor the 283.5-keV `1/2+` path; SI needed for full efficiency/cascade subtraction. | PDF p.407 | provisional |
| W15-AR-3 | Model attribution | `aE2M2/aM1E3` are coherent virtual-state sums, not isolated measured transitions; QPM is a model comparison. | PDF pp.408–409 | self-checking |
| W15-AR-4 | Independence | Direct `137Ba` experiment; Gade 2015 is a secondary commentary and Schirmer 1984 is a different direct `40Ca/90Zr` experiment. | Source lineage | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and `revises` [[two-photon-nuclear-decay]] by closing Gade's direct-source gap; supplies a competitive-branch background-control benchmark complementary to Schirmer 1984 and Freire-Fernández 2024.
- Persistence: update the concept/source lineage and retain the audited SI as attached material (HS-116); do not count it as a second experiment.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[two-photon-nuclear-decay]] | Direct `137Ba` competitive branch and multipole-path evidence. |
| supports | [[gade-2015-gamma-rays-come-in-twos]] | Closes the commentary's Walz source gap; Gade remains secondary. |
| methodological-bridge | [[gamma-gamma-coincidence]] | Timing/random/energy/angular controls for rare branches. |
| limits | [[schirmer-1984-double-gamma-40ca-90zr]] | Different nuclei and allowed-single-γ competition; not a duplicate experiment. |

## Human Review Triage

### P0

- `W15-P0-1`: branching ratio and `aE2M2/aM1E3` require the supplied SI and detector-response/gate definitions before paper-level numeric reuse.

### P1

- `W15-P1-1`: QPM mismatch in `aM1E3` and virtual-state completeness remain model uncertainties.

## Supplementary-material audit (HS-116, 2026-09-21)

- The 14-page SI identifies the setup as five 3''×3'' LaBr3:Ce detectors at 22 cm, `1.50(5)%` full-energy efficiency at 661.66 keV, `603(18) kBq` 137Cs, 12.5/8.5 cm lead at 72°/144°, a 250-MHz SIS3316 digitizer, 35-min gain recalibration, plastic vetoes and a 2.4-ns prompt gate containing `90(3)%` of γγ events (SI p.1).
- QPM uses Woods–Saxon single-particle states, constant monopole pairing, a separable particle–hole interaction and BCS→QRPA→quasiparticle⊗phonon diagonalization; roughly 5000 intermediate states per spin/parity are included. Experimental energies are substituted for the low-lying levels when forming the α coefficients because the calculated `11/2−` energy is too low (SI pp.1–2, Supplementary Table 1).
- The differential branching ratio δ is integrated only to `E0/2` to avoid Bose double counting, evaluated at the central detector-pair angle (72° or 144°), and obtained from efficiency-corrected γγ/single-γ counts (SI pp.2–4, Eqs.2–12). The measured `δ=1.65(25)×10⁻6` (72°) and `0.63(19)×10⁻6` (144°) are only 86% and 80% of the full values because of the `|E1−E2|<300/250 keV` gates; the total branching correction is applied in Table 1 (SI p.5).
- The SI explicitly models the angle-dependent sequential-Compton background: its 72° and 144° sum peaks are about 603 and 650 keV, respectively, explaining the tighter 144° gate (SI pp.5–6). This makes the background argument more quantitative but does not replace an independent response re-analysis.
- The full polarizability expression (SI Eqs.13–17) contains six α paths. Statistics restrict the fit to `αE2M2` and `αM1E3`; the other four are set to zero because the QPM predicts smaller contributions. The two free parameters are fitted jointly to the 72° energy spectrum and the 144° point, with an estimated ~10% systematic from the average-energy denominator approximation (SI pp.6–8).
- Supplementary Tables 2–4 and Fig.1 provide the running sums, final QPM α values and Legendre coefficients. The dominant QPM terms are `αE2M2=42.60` and `αM1E3=9.47 e²fm⁴/MeV` among the listed stretched paths; non-stretched E2E3/E3E2 terms are stated to have negligible effect (SI pp.11–14).

### Attached-material self-audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| W15-SI-1 | Efficiency and gate correction | SI closes the local definition of δ and explains the 86%/80% restricted-gate fractions; full response files are still absent. | SI pp.2–5, Eqs.2–12 | self-checking |
| W15-SI-2 | Sequential-Compton rejection | The 72°/144° sum-energy separation and tighter 144° gate are explicit, but residual background remains an experimental systematic rather than a theorem. | SI pp.5–6 | self-checking |
| W15-SI-3 | Model identifiability | Six α paths exist, but only two are fitted and four are fixed to zero from QPM expectations; `aE2M2/aM1E3` are therefore constrained model parameters, not separately observed matrix elements. | SI pp.6–8, Eqs.13–19 | self-checking |
| W15-SI-4 | Approximation boundary | The `En−Ei≫Ei` average-energy approximation is acknowledged as imperfect and assigned ~10% systematic uncertainty. | SI p.8 | self-checking |

The SI audit closes the prior attached-material gap. It does not clear `needs_review` for paper-level numerical reuse, because raw spectra, detector-response curves and QPM inputs are not supplied.

## Extracted Pages

- Nuclei: `137Ba` (source-level).
- Concepts: [[two-photon-nuclear-decay]]。
- Methods: [[gamma-gamma-coincidence]], [[angular-correlation]]。

## L3/L4 Follow-up

- L3 question: how do energy/timing/angular gates constrain virtual multipole-path coefficients in competitive 2γ decay, and which additional observable separates QPM alternatives? HS-116 closes the supplied SI audit; HS-127's independent energy-sharing result is now the key comparator, while raw response re-fitting remains unavailable.
- No L4 run: raw spectra/response/code are unavailable; this is a direct reported experiment with attached-material readiness pending.
