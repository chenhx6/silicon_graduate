---
type: source
title: "Mukhopadhyay et al. 2008 - Electromagnetic transition rates in high-spin bands in 136Nd"
aliases: [Mukhopadhyay 2008 136Nd transition rates]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic transition rates in high-spin bands in 136Nd"
authors: [S. Mukhopadhyay, D. Almehed, U. Garg, S. Frauendorf, T. Li, P. V. Madhusudhana Rao, X. Wang, S. S. Ghugre, M. P. Carpenter, S. Gros, A. Hecht, R. V. F. Janssens, F. G. Kondev, T. Lauritsen, D. Seweryniak, S. Zhu]
journal: "Physical Review C"
year: 2008
volume: 78
pages: "034311"
doi: "10.1103/PhysRevC.78.034311"
canonical_source: "https://doi.org/10.1103/PhysRevC.78.034311"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf"
raw_sha256: "ea77d7d033051369d19aad2f82a542e91e262eb490d518b246f7f04c2d0dcd2c"
nuclei: [136Nd]
reactions: [100Mo-40Ar-4n]
experiments: [Gammasphere, BLUE, LINESHAPE, DSAM]
models: [tilted-axis-cranking, random-phase-approximation, quadrupole-quadrupole]
observables: [lifetime, B(M1), B(E2), Qt, chiral-vibration, band-mixing]
methods: [doppler-shift-attenuation, gamma-gamma-coincidence, high-fold-spectroscopy]
tags: [136Nd, chirality, band-mixing, DSAM, transition-rates]
---

# Electromagnetic transition rates in high-spin bands in `136Nd`

## Bibliographic Record

- S. Mukhopadhyay *et al.*, *Phys. Rev. C* **78**, 034311 (2008), DOI `10.1103/PhysRevC.78.034311`.

## Scope and Reading Depth

- The six-page PRC article was read end-to-end: introduction, Gammasphere/BLUE and DSAM gates, Fig.1 level scheme, Fig.2 line-shape fits, Table I branching data, Table II lifetimes/strengths, TAC+RPA Hamiltonian and Figs.3–5.

## Experiment and Evidence

`100Mo(40Ar,4n)` at 175 MeV populated `136Nd`; about `2.5×10^9` fivefold-and-higher Gammasphere events were sorted angle-by-angle. BLUE matrices, careful double gates, ring-dependent background subtraction and 5000 Monte Carlo recoil histories were used in LINESHAPE DSAM fits (PDF pp.1–3, Fig.1). Stopping powers came from SRIM; side-feeding was represented by a five-transition cascade whose quadrupole moments were varied.

The two negative-parity bands cross near `I≈17ℏ` and have strong linking transitions. Table II shows markedly different strengths: Band 1 `B(E2)=0.26(3),0.08(1),0.14(2),0.11(2) e²b²` for `I=16–19ℏ`, whereas Band 2 gives `0.54(8),0.51(7),0.44(6),0.04(1) e²b²`; `Qt` similarly differs (`~0.95–1.73 eb` versus `~0.67–2.50 eb`). Systematic stopping-power uncertainties may reach 15% (p.3, Table II, Fig.4).

## Interpretation and Model Boundary

Self-consistent TAC with a QQ interaction reproduces the broad rotational energies using two distinct four-quasiparticle configurations, approximately `πh11/2²⊗νh11/2d3/2` and `πh11/2g7/2⊗νh11/2²`, with a configuration crossing near `I≈17ℏ` (pp.3–5, Fig.3). Pairing is neglected for these high-spin configurations. RPA around each TAC minimum gives collective phonons around `100–400 keV`; the authors interpret these as chiral-vibrational modes, while noting fragmentation/noncollective solutions in one configuration (p.5, Fig.5).

The different `B(E2)` patterns contradict treating the two near-degenerate bands as one ideal chiral pair. The authors instead attribute their closeness to band mixing between distinct configurations; this does not exclude future chiral vibration built on either configuration (pp.4–6).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU08-1 | DSAM strengths of the two `136Nd` bands differ markedly, especially in `B(E2)`. | experiment-result | direct | PDF pp.2–4, Table II, Fig.4 | true |
| MU08-2 | TAC with two configurations plus RPA phonons explains a band-crossing/mixing scenario. | model-interpretation | mixed | PDF pp.3–6, Figs.3–5 | true |
| MU08-3 | Near-degenerate energy and linking transitions do not establish an ideal chiral pair. | counter-evidence | mixed | PDF pp.4–6, Fig.4 | true |

## Summary

The `136Nd` lifetime study is a direct electromagnetic-strength counterexample that forces partner-resolved transition probabilities into the chirality evidence gate.

## Competing Interpretations and Limitations

- DSAM stopping/feeding and 15% stopping-power systematics propagate into the strengths.
- TAC omits pairing for the selected configurations and RPA fragmentation complicates a universal chiral-vibration interpretation.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| MU08-AR-1 | Lifetime-to-strength chain | DSAM line shapes → lifetimes → branching-normalized `B(M1)/B(E2)` and `Qt`; stopping/side-feeding choices are part of the inference. | PDF pp.2–4, Tables I–II | self-checking |
| MU08-AR-2 | Chiral-pair test | Near-degenerate energies and links are outweighed by large, spin-dependent E2-strength differences; electromagnetic rates are a direct counterexample to energy-only chirality. | PDF pp.4–6, Fig.4 | self-checking |
| MU08-AR-3 | Model scope | TAC configurations and RPA phonons explain a band-crossing/mixing scenario; pairing omission and fragmented RPA solutions limit universal transfer. | PDF pp.3–5, Fig.5 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `limits` early `136Nd` chiral-band claims and `supports` [[nuclear-chirality]], [[tilted-axis-cranking]], [[random-phase-approximation]], [[doppler-shift-attenuation-method]] and the HS-012/HS-053 Petrache evidence map.
- L3 unit: compare this lifetime-strength counterexample with the later D5-strengthened `136Nd` pair; retain chronological model revision rather than a single “136Nd chirality” label.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MU08-P0-1`: Preserve the 15% stopping-power/feeding uncertainty and the distinction between distinct configurations, band mixing and any later chiral interpretation.

## Extracted Pages

- Nucleus/project: `136Nd`, [[nuclear-chirality-and-multiple-chiral-doublet-bands]]。
- Methods/models: [[doppler-shift-attenuation-method]], [[tilted-axis-cranking]], [[random-phase-approximation]]。
