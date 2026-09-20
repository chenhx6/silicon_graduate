---
type: source
title: "Rahaman et al. 2024 - Spectroscopic study of 40K"
aliases: [Rahaman 2024 40K spectroscopy]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "Spectroscopic study of 40K"
authors: [Rozina Rahaman, Abhijit Bisoi, Ananya Das, Y. Sapkota, Arkabrata Gupta, S. Ray, S. Sarkar, Yashraj, A. Sharma, Bharti Rohila, I. Ahmed, Kaushik Katre, S. Dutt, S. Kumar, R. P. Singh, R. Kumar, S. Muralithar]
journal: "Physical Review C"
year: 2024
volume: 109
pages: "024318"
doi: "10.1103/PhysRevC.109.024318"
canonical_source: "Rahaman et al., Phys. Rev. C 109, 024318 (2024)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2024_Rahaman et al_Spectroscopic study of K 40.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2024_Rahaman et al_Spectroscopic study of K 40.pdf"
raw_sha256: "b5010c6bb7a48625e01ff56741ad919c70f226ca9dfc487fb40c0201a1c15f05"
nuclei: [40K, 40Ca, 40Ar]
reactions: [27Al-19F-alpha-np]
experiments: [INGA, clover-RDCO-RADO-IPDCO]
models: [large-basis-shell-model, sd-pf-cross-shell]
observables: [level-scheme, RDCO, RADO, IPDCO, mixing-ratio, shell-configuration]
methods: [gamma-gamma-coincidence, DCO, ADO, linear-polarization]
tags: [40K, INGA, high-spin, level-scheme, shell-model, RDCO, IPDCO]
---

# Spectroscopic study of `40K`

## Bibliographic Record

- R. Rahaman *et al.*, *Phys. Rev. C* **109**, 024318 (2024), DOI `10.1103/PhysRevC.109.024318`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2024_Rahaman et al_Spectroscopic study of K 40.pdf`。

## Scope and Reading Depth

- PDF pp.024318-1–13 fully read: `27Al(19F,αnp)` at 68 MeV, 12-clover INGA geometry, calibration and matrix construction, RDCO/RADO/IPDCO definitions, level scheme, Tables I–II, shell-model restrictions and conclusions.
- Not covered: raw event list, full shell-model code and later evaluated levels.

## Key Results

- About `10^8` twofold γ–γ events were recorded with 12 clovers at 148°, 90°, 57° and 32°. Six levels and fourteen transitions were added to the `40K` scheme; most spin/parity assignments were confirmed or revised using RDCO, RADO and IPDCO (PDF pp.1–4, Fig.5, Tables I–II).
- The analysis uses `σ/J=0.3` alignment from known `37Ar/42Ca` transitions for theoretical RDCO calculations. For the setup, pure dipole/pure quadrupole RADO references are about 0.6/1.6; positive/negative IPDCO identifies electric/magnetic character under the clover convention (PDF pp.2–4, Eqs.1–4, Figs.3–4).
- Examples include confirmation of `3352.9 keV (6+)` via a negative-polarization 810.4-keV M1 decay, `3872.2 keV (7+)` from mixed RDCO/RADO/IPDCO, and revision of `4811.7` and `5332.7 keV` levels to `8−` based on E1 decays (PDF pp.4–6, Table I).
- Krane–Steffen δ values are reported for many transitions and generally agree with prior work. Large-basis shell-model calculations use sd/pf cross-shell restrictions to interpret configurations and high-spin level density (PDF pp.4–12).
- Energy calibration required run-by-run online γ lines because the `66Ga` high-energy source showed shifts; this is a practical identity/calibration boundary for the high-energy transitions (PDF p.2).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RH24-1 | Six new levels/fourteen transitions extend `40K` and most assignments are jointly constrained by RDCO/RADO/IPDCO. | experiment-result | direct | PDF pp.1–6, Fig.5, Tables I–II | true |
| RH24-2 | The assumed `σ/J=0.3` and setup-specific RADO references enter RDCO/δ assignments. | method-boundary | direct | PDF pp.2–4 | false |
| RH24-3 | Large-basis sd–pf shell-model restrictions provide microscopic configuration interpretation. | model-result | mixed | PDF pp.8–12 | true |
| RH24-4 | Run-by-run calibration was needed after high-energy source shifts. | calibration-boundary | direct | PDF p.2 | false |

## Summary

Rahaman *et al.* provide a modern low-mass high-spin spectroscopy case with a complete `RDCO+RADO+IPDCO+δ` evidence chain and shell-model interpretation. The source is useful for cross-checking method identities and for preserving alignment/calibration conditions when comparing `40K` assignments to older directional-correlation work.

## Competing Interpretations and Limitations

- RDCO/RADO values are geometry and alignment dependent; `σ/J=0.3` is transferred from reference transitions, not independently fitted for every band.
- Weak lines, contamination and high-energy calibration shifts can affect level placement and δ; the paper retains tentative assignments where evidence is incomplete.
- Shell-model restrictions and effective interactions interpret configurations but do not directly measure deformation or collectivity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| RH24-AR-1 | Assignment chain | Coincidence relationships → RDCO/RADO → IPDCO sign/magnitude → δ and spin/parity assignment. | PDF Eqs.1–4, Tables I–II | self-checking |
| RH24-AR-2 | Calibration chain | Run-specific energy/efficiency calibration → angle matrices → detector-response corrected observables. | PDF p.2 and methods | self-checking |
| RH24-AR-3 | Model transfer | sd–pf shell-model wave functions interpret levels; no direct shape label is inferred without companion observables. | PDF pp.8–12 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]] and spin/parity assignment audit.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `RH24-P0-1`: Preserve the transferred alignment/calibration conventions and separate shell-model configuration labels from direct level/multipolarity observations.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[compton-polarimetry]], [[multipole-mixing-ratio]]。
