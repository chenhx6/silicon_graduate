---
type: source
title: "Chiara et al. 2001 - Spectroscopy and lifetime measurements in 108,110In"
aliases: [Chiara 2001 108In 110In shears lifetimes, Chiara Ref. 16 for Mukhopadhyay 2008]
created: 2026-10-09
updated: 2026-10-09
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: skimmed
title_original: "Spectroscopy in the Z=49 108,110In isotopes: Lifetime measurements in shears bands"
authors: [C. J. Chiara, D. B. Fossan, V. P. Janzen, T. Koike, D. R. LaFosse, G. J. Lane, S. M. Mullins, E. S. Paul, D. C. Radford, H. Schnare, J. M. Sears, J. F. Smith, K. Starosta, P. Vaska, R. Wadsworth, D. Ward, S. Frauendorf]
journal: Physical Review C
year: 2001
volume: 64
pages: "054314"
doi: "10.1103/PhysRevC.64.054314"
canonical_source: "https://doi.org/10.1103/PhysRevC.64.054314"
publisher: American Physical Society
language: en
citation_key: ""
raw_file: "raw/papers/gpt/high-spin-20261009/2001_Chiara et al_Spectroscopy in 108,110In isotopes_Lifetime measurements in shears bands.pdf"
raw_sha256: "5672ffce1e4049245b3107e6132af0ff7501d14182a03d803cd66828e6660a4e"
nuclei: [108in, 110in]
experiments: [Gammasphere, 8pi, DSAM-backed-target]
observables: [lifetime, branching-intensity, B(M1), B(E2), transition-multipolarity]
methods: [Doppler-shift-attenuation, LINESHAPE, gamma-gamma-coincidence]
tags: [108in, 110in, lifetime, branching, shears-band, internal-conversion]
---

# Chiara et al. (2001): `108In/110In` lifetimes and branching-to-strength method

## Bibliographic Record

- C. J. Chiara *et al.*, *Phys. Rev. C* **64**, 054314 (2001), DOI `10.1103/PhysRevC.64.054314`.

### Access and local original

- Crossref metadata resolves the author order, title, journal, volume and DOI. The official APS abstract page exposes the standard `citation_pdf_url`; the HTTPS publisher PDF endpoint returned HTTP 200 with `application/pdf` and a valid `%PDF-1.3` body in this run.
- Unpaywall reports `is_oa=false`, `has_repository_copy=false`, and no OA locations; the exact arXiv DOI query returned zero records. The file was obtained from the directly accessible official APS publisher endpoint, not an OA repository. No institutional login or challenge was used. The APS article page had no supplement link; no SI file was found there.
- Raw PDF: `raw/papers/gpt/high-spin-20261009/2001_Chiara et al_Spectroscopy in 108,110In isotopes_Lifetime measurements in shears bands.pdf`; 440,801 bytes; SHA-256 `5672ffce1e4049245b3107e6132af0ff7501d14182a03d803cd66828e6660a4e`.

## Scope and Reading Depth

- Targeted reading for MU08 Ref. [16]: PDF p.1 abstract; p.7 Table III intensity-normalization caption; pp.18–19 Sec. IV.C DSAM analysis, Eqs. (2)–(3), and Table V; p.29 conclusions.
- The article covers separate `108In` and `110In` level schemes, DSAM lifetimes, reduced strengths and TAC comparisons. This source note captures the cited lifetime/branch/ICC procedure and its limits, not every band assignment or model comparison in the full article.
- Not covered: complete level-scheme and TAC audits for both isotopes, every Table V/VI row, raw detector spectra, original LINESHAPE code and stopping-power inputs.

## Lifetime-to-Strength Procedure Relevant to Ref. [16]

For the backed-target analyses, angle-dependent coincidence spectra were fitted with LINESHAPE. The `108In` transition intensities used in that fit came from efficiency-corrected broadened-peak counts normalized to a stopped transition lower in the cascade; the authors note that the thin- and backed-target `108In` datasets used different reactions and could populate high-spin states differently (PDF p.18, Sec. IV.C).

The paper converts fitted level lifetimes to partial transition lifetimes using the observed branching ratios, then calculates `B(M1)` or `B(E2)` with the transition energy and partial lifetime. Internal-conversion effects are included and described as small. `ΔI=1` dipole lines are treated as predominantly pure M1 with minimal E2 admixture (`δ≈0`); where an E2 crossover is not observed within experimental sensitivity, its crossover intensity is assumed to be zero (PDF p.19, Eqs. (2)–(3) and text following the equations; Table V caption).

Table III reports efficiency-corrected `108In` intensities normalized to 100 for the 213-keV reference transition (PDF p.7, Table III caption). Table V then tabulates the fitted level lifetime, M1 and E2 transition energies/intensities where observed, and derived strengths; its caption states that lifetimes are adjusted for branching ratios and internal conversion. Those relative-intensity and observed-branch procedures do not, by themselves, demonstrate a complete absolute photon-per-parent ledger for every level.

The fit errors include covariance between in-band and side-feeding lifetimes, but quoted errors omit stopping-power-model systematics that may reach ±20% (PDF p.18, Sec. IV.C; PDF p.19, Table V caption). The original analyses use data and bands specific to `108In/110In`; they are a methodological precedent, not independent evidence for a `136Nd` branching denominator.

## Key Results

| ID | Statement | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| CHI01-1 | The paper reports DSAM lifetimes for four `ΔI=1` and one `ΔI=2` bands in `108In/110In`, together with reduced transition strengths for the dipole bands. | experimental-fact | direct | single | PDF p.1, abstract | true |
| CHI01-2 | The authors derive partial `τ(Mλ)` from fitted level lifetimes and observed branching ratios, include internal-conversion corrections in `B(M1)/B(E2)`, and give the rate formulas in Eqs. (2)–(3). | experimental-method | direct | single | PDF p.19, Eqs. (2)–(3) and paragraph below | true |
| CHI01-3 | The dipole transitions are treated as nearly pure M1 (`δ≈0`); if an E2 crossover is not observed within experimental sensitivity, its crossover intensity is assumed to be zero. | analysis-assumption | direct | single | PDF p.19, paragraph below Eqs. (2)–(3) | true |
| CHI01-4 | Table III intensities are corrected for detector efficiency and normalized to 100 for the 213-keV reference line; Table V uses branch/IC-adjusted partial lifetimes and propagates lifetime-fit errors to the strengths. | evidence-boundary | direct | single | PDF p.7, Table III caption; PDF p.19, Table V caption | true |
| CHI01-5 | In-band/side-feeding lifetime covariance is included in the fit-derived uncertainty, while stopping-power systematic errors are excluded and may reach ±20%. | method-limitation | direct | single | PDF p.18, Sec. IV.C, uncertainty paragraph | true |
| CHI01-6 | For the `108In` Band 2 `15−` Table V row, the two listed observed gamma intensities are `31.6` for the 527.8-keV M1 line and `2.0` for the 864.2-keV E2 crossover. Dividing only these two entries by their sum gives relative shares `0.9405` and `0.0595`; these are shares of the two listed observed photon intensities, not absolute per-parent photon probabilities or a complete all-channel branch ledger. | our-inference | indirect | single | PDF p.19, Table V, `I=15−` row | true |

## Summary

Chiara *et al.* provide a directly readable precedent for extracting partial M1/E2 transition lifetimes from DSAM-fitted level lifetimes, observed branching ratios and internal-conversion corrections. Their published choices include a nearly pure-M1 assumption for dipole transitions and setting an E2 crossover to zero when no crossover is seen within sensitivity. These details help interpret the procedure cited by MU08, but do not identify MU08's line-by-line branch denominator or prove that its `136Nd` ledger is complete.

## Competing Interpretations and Limitations

- The tabulated transition intensities are efficiency corrected and normalized to a reference gamma ray; this is a relative intensity scale and is not by itself an absolute photon-per-parent ledger.
- The published `108In/110In` branch and conversion choices are method examples. They should not be transferred as measurements or exact settings for MU08's distinct `136Nd` experiment.
- The line-shape lifetime fit includes in-band/side-feeding covariance, but quoted lifetime uncertainties omit stopping-power systematics that may reach ±20%.
- No raw event data, detector response, original LINESHAPE input, or complete per-parent channel inventory was available in this targeted read.

## Extracted Pages

- PDF p.1: title, abstract and experiment overview.
- PDF p.7: Table III efficiency correction and reference-line normalization caption.
- PDF pp.18–19: Sec. IV.C DSAM analysis, partial lifetime/strength Eqs. (2)–(3), Table V caption and uncertainties.
- PDF p.29: conclusions; the lifetime and strength results are interpreted as shears-band evidence for the studied indium isotopes.

## Knowledge Impact and Learning Decision

- Effect: `methodological-bridge` to [[mukhopadhyay-2008-136nd-transition-rates]]; the cited article's identity, method text and access route are now directly checked.
- The branch-normalization/complete-channel gap in MU08 remains open because Chiara et al. describe their own `108In/110In` analysis, not the detailed `136Nd` line-by-line photon ledger.
- Review state remains `unreviewed`; this direct source audit is Codex self-audit, not human review.
