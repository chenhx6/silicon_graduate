---
type: source
title: "Twin, Olsen & Sheppard 1970 - Polarization and angular correlation measurements following the 40Ar(p,nγ)40K reaction"
aliases: [Twin 1970 40K polarization, 40Ar p n gamma 40K angular correlations]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-method
reading_depth: deep-read
title_original: "Polarization and angular correlation measurements following the 40Ar(p,nγ)40K reaction"
authors: [P. J. Twin, W. C. Olsen, D. M. Sheppard]
journal: "Nuclear Physics A"
year: 1970
volume: 143
pages: "481-496"
pii: "0375-9474(70)90543-9"
canonical_source: "Twin, Olsen & Sheppard, Nucl. Phys. A 143, 481-496 (1970)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf"
raw_sha256: "40cb4df52b26f0eabc9c86eba136fb68bc2da99d123a72276583483cc64dfd11"
nuclei: [40K, 40Ar, 40Ca]
reactions: [40Ar(p,nγ)40K]
experiments: [alberta-vande-graaff-gamma-polarimeter]
models: [compound-nuclear-statistical-model, rotation-vibration-context]
observables: [gamma-ray-angular-distribution, gamma-ray-polarization, gamma-gamma-angular-correlation, multipole-mixing-ratio]
methods: [angular-distribution, linear-polarization-asymmetry, compton-polarimetry]
tags: [40K, polarization, angular-correlation, mixing-ratio, historical-method]
---

# Polarization and angular-correlation measurements following the 40Ar(p,nγ)40K reaction

## Bibliographic Record

- P. J. Twin, W. C. Olsen and D. M. Sheppard, *Nuclear Physics A* **143**, 481–496 (1970), PII `0375-9474(70)90543-9`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1970_Twin et al_Polarization and angular correlation measurements following the 40Ar(p, nγ)40K reaction.pdf`。
- 16-page historical experiment/method paper; HS-033 and HS-034 are exact duplicate rows of this same PDF and will be audited without rereading.

## Scope and Reading Depth

- PDF pp.481–496 fully read: reaction/target, angular distributions, γγ correlations, Compton polarimeter and Rose–Brink polarization formalism Eqs.(1–3), efficiency factor `R`, compound-statistical-model grid search, Table 1/2, Figs.1–9 and conclusions.
- Figure/table audit: polarimeter geometry, χ²/mixing-ratio plots, spectra at 0°/90° analyzer, Legendre-coefficient maps, and all state/mixing-ratio rows in Table 2.
- Not covered: raw spectra/matrices, original MANDY code, modern response simulations and later 40K evaluations.

## Paper Question and Experimental Logic

The experiment identifies low-lying `40K` levels and multipole mixing ratios by combining near-threshold `40Ar(p,nγ)` angular distributions, γγ angular correlations and Compton polarization. Near threshold suppresses outgoing-neutron `l=1` transmission and stabilizes compound-population predictions.

1. Record Ge(Li) γ spectra at 0°, 30°, 45°, 60° and 90°; fit even Legendre coefficients `a2/a4` and compare with MANDY compound-nuclear predictions.
2. Measure γγ angular correlations with two NaI detectors and use grid-search χ² fits in population parameters and mixing ratios.
3. Use a Ge(Li)+two NaI Compton polarimeter at `θ≈82°`; normalize analyzer efficiencies at `θ=0°`, compute polarization efficiency `R` with Klein–Nishina/solid-angle correction, and fit polarization simultaneously with angular distributions.

## Key Evidence and Reasoning Chain

- The paper assigns `40K` states at 1.959 (`2+`), 2.047 (`2−`), 2.070 (`3−`), 2.103 (`1−`), 2.261 (`3+`), 2.290 (`1+`), 2.291 (`4` or `3`), 2.419 (`2`/`3`), 2.575 (`2`/`4`) and 2.625 (`0−`) MeV, with branching and δ values in Table 2.
- The `0.800-MeV` `2−→3−` 770-keV transition has an angular-distribution ambiguity; γγ correlation with a pure-quadrupole 844-keV reference resolves it as pure M1.
- The 1.959-MeV level is assigned `2+`: simultaneous angular distributions establish spin 2, while 1159-keV polarization selects positive parity and δ(1929 keV)≈−0.10(4).
- The 2.261-MeV level is assigned `3+` from angular distributions plus `−0.57±0.30` polarization; the paper explicitly shows polarization alone can fit `2−`, `3+` or `4−`, so spin information is required first.
- Negative-parity `p3/2 d3/2−1` states receive mixed E2/M1 ratios; positive-parity states at 1.644, 1.959, 2.261 and 2.290 MeV are identified as likely multi-particle configurations but no modern structure calculation is supplied.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TW70-1 | Combined angular distributions, γγ correlations and polarization assign spins/parities and mixing ratios for low-lying `40K` states. | experimental-method-result | direct | PDF pp.481–496, Table 2 | true |
| TW70-2 | The 770-keV `2−→3−` line is pure M1 after γγ-correlation resolution of the angular-distribution ambiguity. | experimental-result | direct | PDF pp.487–488, Fig.2 | true |
| TW70-3 | The 1.959-MeV state is `2+`; 1159-keV polarization and 1929-keV angular distribution/mixing support the assignment. | experimental-assignment | direct | PDF pp.489–490, Figs.3–4 | true |
| TW70-4 | The 2.261-MeV state is `3+`; polarization alone is non-unique and must be combined with angular distributions. | experimental-assignment/limitation | direct | PDF pp.491–492, Fig.6 | false |
| TW70-5 | Table 2 contains multiple δ solutions/uncertainties, including unresolved 2.291-MeV spin 3/4 and 2.419-MeV spin 2/3 cases. | ambiguity | direct | PDF pp.487–495, Table 2 | false |

## Summary

Twin *et al.* demonstrate a historical joint-analysis chain in which angular distributions constrain spin/population, γγ correlations resolve mixing-ratio branches and Compton polarization supplies parity/multipole information. The method's strongest lesson is complementarity: polarization alone is often non-unique.

## Competing Interpretations and Limitations

MANDY compound-statistical populations, Biedenharn versus Rose–Brink sign conventions, finite polarimeter efficiency `R`, near-threshold assumptions and limited detector response all affect δ. Several states retain alternative spin assignments or δ branches; positive-parity configuration language is qualitative and predates modern shell-model/DFT calculations.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| TW70-AR-1 | Observable chain | `a2/a4` angular distributions → γγ correlation → polarization `P=R^{-1}R_exp` → joint χ² δ/spin/parity. | PDF pp.482–487 | self-checking |
| TW70-AR-2 | Convention | MANDY uses Biedenharn δ sign; paper's formalism uses Rose–Brink, yielding opposite dipole–quadrupole sign. | PDF p.482 | self-checking |
| TW70-AR-3 | Transfer condition | `R≈0.21` at 1.5 MeV and analyzer geometry are detector-specific; do not transfer as modern Q. | PDF p.485 | self-checking |
| TW70-AR-4 | Failure condition | Polarization-only parity fits can be degenerate; population priors and `a2/a4` uncertainties can reorder spin/δ solutions. | PDF pp.491–492 | active-L3 |
| TW70-AR-5 | Duplicate lineage | HS-033/HS-034 are exact SHA-256 duplicates; no new source/experiment count. | Ledger identity | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` the joint angular-distribution/polarization method map and `limits` single-observable spin/parity assignments.
- Persistence: update [[angular-distribution]], [[linear-polarization-asymmetry]], [[compton-polarimetry]] and [[multipole-mixing-ratio]].
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[angular-distribution]] | Near-threshold population control and `a2/a4` grid search. |
| methodological-bridge | [[linear-polarization-asymmetry]] | Compton polarimeter efficiency and parity/multipole complement. |
| supports | [[multipole-mixing-ratio]] | Historical multi-observable δ extraction with explicit branch ambiguity. |

## Human Review Triage

### P0

- `TW70-P0-1`: map Biedenharn/MANDY signs to Rose–Brink before cross-source δ comparison; preserve unresolved states.

### P1

- `TW70-P1-1`: `R` and analyzer geometry are historical detector-specific values; modern response simulation is required for reuse.
- `TW70-P1-2`: qualitative positive-parity configuration labels are not direct modern structure assignments.

## Extracted Pages

- Nuclei: `40K` (source-level only).
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[compton-polarimetry]]。

## L3/L4 Follow-up

- L3 question: quantify how much joint `a2/a4`+γγ+polarization reduces δ/spin branch ambiguity under modern detector-response and convention mapping. No L4 inputs/code are available.
