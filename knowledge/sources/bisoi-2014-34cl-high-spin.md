---
type: source
title: "Bisoi et al. 2014 - High spin spectroscopy in 34Cl"
aliases: [Bisoi 2014 34Cl high spin]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "High spin spectroscopy in 34Cl"
authors: [Abhijit Bisoi, M. Saha Sarkar, S. Sarkar, S. Ray, D. Pramanik, R. Kshetri, Somnath Nag, K. Selvakumar, P. Singh, A. Goswami, S. Saha, J. Sethi, T. Trivedi, B. S. Naidu, R. Donthi, V. Nanal, R. Palit]
journal: "Physical Review C"
year: 2014
volume: 89
pages: "024303"
doi: "10.1103/PhysRevC.89.024303"
canonical_source: "Bisoi et al., Phys. Rev. C 89, 024303 (2014)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2014_Bisoi et al_High spin spectroscopy in 34 Cl.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2014_Bisoi et al_High spin spectroscopy in 34 Cl.pdf"
raw_sha256: "bc0af718ffb496f135abe2a51b82f87d208776fce155926a8604e8c05d126f85"
nuclei: [34Cl, 34S, 26Al]
reactions: [27Al-12C-alpha-n]
experiments: [INGA, DSAM, RDCO, IPDCO]
models: [large-basis-shell-model, sd-pf-cross-shell, two-level-mixing]
observables: [level-scheme, lifetime, B(E2), B(M1), RDCO, IPDCO, mixing-ratio]
methods: [gamma-gamma-coincidence, DCO, linear-polarization, Doppler-shift-attenuation]
tags: [34Cl, INGA, high-spin, DSAM, collectivity, shell-model]
---

# High-spin spectroscopy in `34Cl`

## Bibliographic Record

- A. Bisoi *et al.*, *Phys. Rev. C* **89**, 024303 (2014), DOI `10.1103/PhysRevC.89.024303`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2014_Bisoi et al_High spin spectroscopy in 34 Cl.pdf`。

## Scope and Reading Depth

- PDF pp.024303-1–13 fully read: INGA/Pixie-16 experiment, RDCO/IPDCO/δ, level scheme to 10.6 MeV, DSAM line-shape lifetimes, Tables I–V, shell-model truncations/configuration mixing and conclusion.
- Not covered: raw event list and full shell-model code.

## Key Results

- `27Al(12C,αn)` at 40 MeV with 15 INGA clovers produced about `6×10^8` γ–γ events; the `34Cl` scheme was extended to 10.6 MeV. RDCO, IPDCO and δ assign multipolarities and parity, while DSAM provides lifetimes for selected states (PDF pp.1–4, Tables I–V).
- IPDCO confirms electric/magnetic character (e.g., 491-keV electric and 461-keV magnetic lines); DCO and Krane–Steffen δ values are listed for dozens of transitions under `σ/J=0.3` and clover `Q(E)` calibration (PDF pp.2–5, Table I).
- DSAM line shapes use 50,000 recoil histories, PACE4 momentum distributions and Northcliffe–Schilling stopping powers. Selected E2 transitions have `B(E2)≈8–20 W.u.`, indicating onset of collectivity; higher levels have larger E2 strengths and short lifetimes (PDF pp.5–9, Table V).
- Large-basis sd–pf shell-model calculations require cross-shell pf involvement for negative-parity and high-spin positive-parity states; two-level mixing is used for selected configuration admixtures (PDF pp.8–12, Tables III–IV).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI14-1 | `34Cl` high-spin scheme reaches 10.6 MeV with RDCO/IPDCO/δ and DSAM evidence. | experiment-result | direct | PDF pp.1–9, Tables I–V | true |
| BI14-2 | Selected E2 lifetimes give `B(E2)≈8–20 W.u.` and evidence for emerging collectivity. | collectivity-result | direct | PDF pp.5–9, Table V | true |
| BI14-3 | sd–pf cross-shell configurations are needed to reproduce negative-parity/high-spin states. | model-result | mixed | PDF pp.8–12 | true |
| BI14-4 | DSAM feeding/stopping and `σ/J`/Q calibration limit lifetime and δ transfer. | limitation | direct | PDF pp.2–9 | false |

## Summary

Bisoi *et al.* connect a detailed multimethod level scheme to DSAM electromagnetic strengths in `34Cl`. The direct evidence supports a transition from single-particle to collective high-spin behavior, while pf-shell configuration mixing and two-level admixtures remain model interpretations.

## Competing Interpretations and Limitations

- DSAM lifetimes are sensitive to side feeding, stopping powers, recoil distributions and gates; upper limits are retained where statistics are insufficient.
- `B(E2)` enhancement indicates collectivity but does not uniquely determine a shape or deformation parameter.
- Large-basis shell-model truncations and effective interactions influence configuration mixing; model agreement is not a direct wave-function measurement.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BI14-AR-1 | Assignment chain | Coincidences → RDCO/IPDCO/δ → multipolarity/spin/parity; preserve weak/tentative levels. | PDF pp.2–5, Table I | self-checking |
| BI14-AR-2 | Lifetime chain | Doppler line shapes + PACE4/SRIM + side feeding → τ → B(E2)/B(M1). | PDF pp.5–9, Table V | self-checking |
| BI14-AR-3 | Model transfer | sd–pf shell-model and two-level mixing explain configuration content, not direct shape. | PDF pp.8–12 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]], [[angular-distribution]], [[linear-polarization-asymmetry]] and light-nucleus collectivity comparators.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `BI14-P0-1`: Keep DSAM/model/lifetime boundaries explicit; `B(E2)` enhancement is not a unique deformation proof.

## Extracted Pages

- Methods/observables: [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]], [[angular-distribution]]。
