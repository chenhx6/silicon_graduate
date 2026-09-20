---
type: source
title: "Eldridge et al. 2018 - E2/M1 mixing ratios from gamma-vibrational bands"
aliases: [Eldridge 2018 gamma-band mixing ratios]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "E2/M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational bands of 102,104,106,108Mo, 108,110,112Ru, and 112,114,116Pd"
authors: [J. M. Eldridge, B. Fenker, J. H. Hamilton, C. Goodin, C. J. Zachary, E. Wang, A. V. Ramayya, A. V. Daniel, G. M. Ter-Akopian, Yu. Ts. Oganessian, Yu. X. Luo, J. O. Rasmussen, S. J. Zhu]
journal: "European Physical Journal A"
year: 2018
volume: 54
pages: "15"
doi: "10.1140/epja/i2018-12426-5"
canonical_source: "Eldridge et al., Eur. Phys. J. A 54, 15 (2018)"
library_file: "raw/papers/gpt/high-spin-20260920/振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf"
raw_sha256: "a244b7e49fb513f057119bce603c0790a5cf381bd7a909f9c2996d033e1439b7"
nuclei: [102Mo, 104Mo, 106Mo, 108Mo, 108Ru, 110Ru, 112Ru, 112Pd, 114Pd, 116Pd]
reactions: [252Cf-fission]
experiments: [Gammasphere, IPAC]
models: [gamma-vibrational-band, Greiner-proton-neutron-deformation]
observables: [E2-M1-mixing-ratio, g-factor, attenuation, gamma-band]
methods: [integral-perturbed-angular-correlation, gamma-gamma-angular-correlation]
tags: [gamma-band, mixing-ratio, IPAC, Mo, Ru, Pd, gamma-softness]
---

# E2/M1 mixing ratios from γ-vibrational bands

## Bibliographic Record

- J. M. Eldridge *et al.*, *Eur. Phys. J. A* **54**, 15 (2018), DOI `10.1140/epja/i2018-12426-5`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf`。

## Scope and Reading Depth

- PDF pp.1–11 fully read: Krane–Steffen δ definition/convention, Greiner comparison, Gammasphere `252Cf` IPAC setup, attenuation/g-factor extraction, Tables 1–4, Figs.1–11, contamination controls and conclusions.
- Not covered: raw event files, the Goodin thesis and later evaluated level schemes.

## Key Results

- A `62 μCi 252Cf` source inside Gammasphere produced `5.7×10^11` triple-and-higher coincidences with 101 working HPGe detectors and 64 pair angles. IPAC angular correlations were fit with `W(θ)=1+G2A2P2+G4A4P4` (PDF pp.1–3, Eq.7).
- Ground-band `2+` g factors and attenuation factors were measured first. Average `G2,G4` were `0.78(6),0.6(2)` for `104–108Mo` and `0.85(6),0.7(2)` for `108–112Ru`; `102Mo` and Pd cases used near-unity corrections (PDF pp.3–4, Table 1).
- Across 37 γ-band→ground-band transitions in Mo, Ru and Pd, 30 (≈81%) are pure/near-pure E2 (`|δ|≥3`) within 1.5σ in `(A2,A4)` space, and all are compatible with pure/near-pure E2 within 3σ. Multiple δ branches, including `±∞` pure-E2 limits and very large opposite-sign solutions, are retained when the oval intersects the uncertainty region (PDF pp.4–9, Tables 2–4, Figs.4–10).
- The `102Mo` 1244.9-keV level is confirmed as a `3+γ` state from the unique angular-correlation oval. The sign trend of `δ(E2/M1)` changes around `110Ru`, supporting Krane's predicted shape transition, while Greiner's proton/neutron-deformation theory systematically underpredicts magnitudes and does not predict sign changes (PDF pp.3–10, Fig.11).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EL18-1 | γ-band→ground-band transitions in ten Mo/Ru/Pd isotopes are predominantly E2, with 37 measured δ values and explicit multi-branch uncertainty. | experiment-result | direct | PDF pp.4–9, Tables 2–4 | true |
| EL18-2 | The δ sign trend changes near `110Ru`, consistent with a model-predicted shape transition but not a direct γ-rigidity proof. | systematics-interpretation | mixed | PDF pp.9–10, Fig.11 | true |
| EL18-3 | IPAC attenuation/g-factor corrections are necessary and isotope/feeding dependent. | method-result | direct | PDF pp.2–4, Table 1 | false |
| EL18-4 | Greiner's model underpredicts δ magnitudes and cannot reproduce sign changes in this dataset. | experiment-model-conflict | mixed | PDF pp.9–10, Fig.11 | true |

## Summary

Eldridge *et al.* provide a large, cross-isotope γ-band mixing-ratio data set. The direct result is predominantly E2 decay from γ bands to ground bands; the shape-transition interpretation is a systematics/model layer, and IPAC ovals preserve branch ambiguity rather than forcing a single δ solution.

## Competing Interpretations and Limitations

- δ uncertainty is expressed in `(A2,A4)` space; a finite error oval may wrap around `δ=±∞`, allowing both signs or pure-E2 limits. A single numerical central value can hide this topology.
- IPAC depends on attenuation `Gk`, g factors, lifetimes, hyperfine fields and contamination/gates. Similar energies in fission partners required extra gates and can bias coefficients if not controlled.
- The Krane shape-transition comparison and Greiner theory are interpretations; a sign change in δ is not a standalone measurement of γ softness/rigidity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| EL18-AR-1 | IPAC chain | Detector-pair angular bins → `A2/A4` → attenuation correction from `g`/lifetimes → δ oval intersection. | PDF Eqs.5–9, Tables 1–4 | self-checking |
| EL18-AR-2 | Branch topology | Parameterized `A2,A4` oval can have two or unbounded δ branches; retain all within stated σ. | PDF pp.4–9, Tables 2–4 | self-checking |
| EL18-AR-3 | Shape transfer | δ sign/magnitude trend → model shape comparison only after common Krane convention and attenuation controls. | PDF pp.9–10, Fig.11 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-correlation]], [[gamma-soft-deformation]], [[gamma-band-energy-staggering]] and cross-isotope A≈130/neighbor shape diagnostics.
- New reusable rule: report δ as a branch set in `(A2,A4)` space; do not collapse `±∞` or opposite-sign solutions without a physical or independent constraint.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `EL18-P0-1`: Preserve IPAC attenuation/g-factor and δ-oval branch boundaries; the `110Ru` shape-transition interpretation is not a direct standalone observable.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-correlation]], [[gamma-soft-deformation]], [[gamma-band-energy-staggering]]。
