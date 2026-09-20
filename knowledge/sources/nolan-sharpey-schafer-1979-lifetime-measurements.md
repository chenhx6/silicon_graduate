---
type: source
title: "Nolan & Sharpey-Schafer 1979 - The measurement of the lifetimes of excited nuclear states"
aliases: [Nolan Sharpey-Schafer 1979 lifetime review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review-method
reading_depth: deep-read
title_original: "The measurement of the lifetimes of excited nuclear states"
authors: [P. J. Nolan, J. F. Sharpey-Schafer]
journal: "Reports on Progress in Physics"
year: 1979
volume: 42
pages: "1-87"
canonical_source: "Nolan & Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979)"
library_file: "raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf"
raw_sha256: "5e20f735e995021f4a0eb8c1a937acedeee53509caed3ffa2cd8ddaa794bbc4f"
nuclei: [lifetime-methods]
reactions: []
experiments: []
models: [DSAM-stopping, recoil-distance, electronic-timing]
observables: [nuclear-lifetime, gamma-energy-shift, attenuation-factor, transition-strength]
methods: [doppler-shift-attenuation-method, recoil-distance-method, electronic-timing, Coulomb-excitation]
tags: [lifetime, DSAM, RDM, Doppler-shift, review, nuclear-structure-method]
---

# The measurement of the lifetimes of excited nuclear states

## Bibliographic Record

- P. J. Nolan and J. F. Sharpey-Schafer, *Reports on Progress in Physics* **42**, 1–87 (1979).
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf`。
- 88-page review PDF (printed pp.1–87); full chapter map and method comparisons read.

## Scope and Reading Depth

- Fully read: Doppler-shift techniques (DSAM, stopping theories, RDM), electronic timing, blocking, fission isomers, indirect Coulomb/electron/resonance/capture methods, exotic techniques and accuracy/reliability comparison.
- Not covered: reanalysis of every historical lifetime experiment, modern stopping codes and post-1979 detector developments.

## Key Evidence and Method Logic

- Lifetime `τ=ℏ/Γ` links measured widths/decay probabilities to electromagnetic matrix elements; complementary spins, parities, branching, multipole mixing and conversion data are required for model comparison.
- DSAM compares Doppler shift/attenuation with recoil slowing time (~`3×10⁻13 s`), requiring electronic/nuclear stopping models, recoil velocity, feeding and side-feeding treatment.
- RDM compares decay time with recoil flight between foils (`~5 μm–2 cm`), while electronic timing and blocking cover other lifetime ranges.
- Indirect methods infer widths from Coulomb excitation, electron scattering, resonance fluorescence or capture; products of matrix elements and ground-state access impose boundaries.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NS79-1 | DSAM and RDM dominate direct lifetime measurements in the `10⁻18–10⁻6 s` range but rely on stopping/flight-time models. | method-framework | direct | PDF Ch.II, Fig.2 | true |
| NS79-2 | Lifetime interpretation requires complementary spin/parity, branching, mixing and conversion information. | method-boundary | direct | PDF pp.3–6 | false |
| NS79-3 | Coulomb excitation and other indirect methods measure matrix-element products/widths rather than direct decay time. | method-boundary | direct | PDF pp.4–6, Ch.VI | false |

## Summary

Nolan & Sharpey-Schafer is a foundational lifetime-method review that calibrates DSAM/RDM, stopping, feeding, timing and indirect-width assumptions. It is the method lineage for later `61Ni`, `165Tm`, `131Ce` and high-spin lifetime sources.

## Competing Interpretations and Limitations

Historical stopping powers, feeding models, detector resolution and side-feeding assumptions can dominate lifetime uncertainty. Direct and indirect methods are not interchangeable; each has a range, observable and input-data boundary.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| NS79-AR-1 | Method chain | Reaction/recoil → Doppler/timing/flight observable → stopping/response model → τ → transition strength. | PDF Chs.II–VIII | self-checking |
| NS79-AR-2 | Transfer condition | Reuse only with matching recoil velocity/material/feeding/detector and uncertainty model. | PDF Ch.II, Sec.VIII | active-L3 |
| NS79-AR-3 | Independence | Review; historical examples are not new experiments. | Scope/References | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and strengthens [[doppler-shift-attenuation-method]] and lifetime evidence boundaries.
- Persistence: link to Jensen 2001, Wadsworth 1977 and the `131Ce` lifetime project.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `NS79-P0-1`: lifetime-derived strengths cannot be reused without stopping/feeding and method-specific uncertainty mapping.

## Extracted Pages

- Methods: [[doppler-shift-attenuation-method]]。
