---
type: source
title: "Mukhopadhyay et al. 2007 - From chiral vibration to static chirality in 135Nd"
aliases: [Mukhopadhyay 2007 135Nd chirality]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "From Chiral Vibration to Static Chirality in 135Nd"
authors: [S. Mukhopadhyay, D. Almehed, U. Garg, S. Frauendorf, T. Li, P. V. Madhusudhana Rao, X. Wang, S. S. Ghugre, M. P. Carpenter, S. Gros, A. Hecht, R. V. F. Janssens, F. G. Kondev, T. Lauritsen, D. Seweryniak, S. Zhu]
journal: "Physical Review Letters"
year: 2007
volume: 99
pages: "172501"
doi: "10.1103/PhysRevLett.99.172501"
citation_key: Mukhopadhyay_2007
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Mukhopadhyay et al., Phys. Rev. Lett. 99, 172501 (2007)"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf"
raw_sha256: "9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425"
nuclei: [135Nd]
reactions: [100Mo-40Ar-5n]
experiments: [Gammasphere, DSAM, LINESHAPE, BLUE]
models: [tilted-axis-cranking, random-phase-approximation, PQTAC, chiral-vibration]
observables: [lifetime, B(M1), B(E2), partner-band-energy-splitting, interband-transition]
methods: [Doppler-shift-attenuation, gamma-gamma-coincidence, high-fold-spectroscopy]
tags: [135Nd, chirality, chiral-vibration, static-chirality, TAC, RPA, DSAM]
---

# From chiral vibration to static chirality in `135Nd`

## Bibliographic Record

- S. Mukhopadhyay *et al.*, *Phys. Rev. Lett.* **99**, 172501 (2007), DOI `10.1103/PhysRevLett.99.172501`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf`。

## Scope and Reading Depth

- PDF pp.172501-1–4 fully read: experiment/reaction and DSAM/BLUE/LINE­SHAPE analysis, Table I lifetimes and `B(M1)/B(E2)`, Figs.1–4, PQTAC+RPA model and conclusions.
- Not covered: the earlier `135Nd` level-scheme paper's full raw spectra and later reanalyses.

## Key Results

- `100Mo(40Ar,5n)` at 175 MeV was measured with Gammasphere; about `2.5×10^9` fivefold-and-higher events were analyzed. Lifetimes were extracted for Band A spins `29/2−`–`43/2−` and Band B `31/2−`–`39/2−` with angle-gated DSAM line shapes and SRIM stopping powers (PDF pp.1–2, Fig.1, Table I).
- Intraband electromagnetic strengths of the two bands are nearly identical within uncertainties. Representative `B(E2)` values are about `0.28–0.32 e^2b^2` at the band heads and decline/redistribute with spin; `B(M1)` values show the characteristic odd-even staggering and are broadly shared by the partner bands (PDF pp.2–4, Table I, Figs.2–3).
- The TAC calculation with the `{π(h11/2)^2, νh11/2}`-type three-quasiparticle configuration reproduces energies and intraband strengths. RPA around the TAC minimum supplies the phonon splitting and interband transition strengths, allowing a transition from chiral vibration to static chirality as spin increases (PDF pp.2–4, Eqs.1–3, Fig.4).
- The RPA phonon energy approaches zero near the TAC critical frequency; the calculated static-chirality onset is about one spin unit above the closest experimental partner-band approach. The low-spin mode is a chiral vibration dominated by orientation fluctuations; the high-spin mode is tunneling between left/right configurations (PDF pp.3–4).
- The authors argue that `135Nd` has more nearly identical partner transition rates than `134Pr`, because the additional `h11/2` quasiproton delays the instability and keeps the vibration near harmonic over a longer spin range (PDF pp.1, 4).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-1 | Near-identical intraband `B(E2)`/`B(M1)` strengths in Bands A/B support a chiral-partner interpretation for `135Nd`. | experiment-result | direct | PDF pp.2–4, Table I, Figs.2–3 | true |
| MU07-2 | TAC+RPA reproduces energies and electromagnetic strengths and describes a chiral-vibration to static-chirality transition. | model-interpretation | mixed | PDF pp.2–4, Eqs.1–3, Fig.4 | true |
| MU07-3 | The RPA phonon energy tends to zero at the TAC instability; the static-chirality onset is model- and spin-resolution-dependent. | transition-boundary | mixed | PDF pp.3–4 | true |
| MU07-4 | DSAM lifetimes/strengths depend on stopping powers, line-shape gates and configuration assumptions. | limitation | direct | PDF pp.2, Table I | false |

## Summary

Mukhopadhyay *et al.* provide an early direct electromagnetic-strength test of the `135Nd` chiral pair. The data support nearly identical partner-band transition rates, while TAC+RPA supplies the dynamical bridge from chiral vibration to static chirality. The static label remains a model-linked interpretation tied to the critical-spin and tunneling picture.

## Competing Interpretations and Limitations

- Similar in-band strengths are necessary/strong evidence for chiral partners but are not independent of band identity, DSAM feeding and multipole assignments.
- TAC is a mean-field intrinsic solution; RPA harmonic fluctuations describe the low-lying partner splitting but may break down near the instability where anharmonicity grows.
- The calculated critical spin differs slightly from the experimental closest approach; the comparison should not be read as a precise universal transition point.
- `135Nd` is a channel-/nucleus-specific reference. Its electromagnetic pattern cannot be transferred to `135Pr`, `187Au` or other wobbling/chiral candidates without their own transition-strength evidence.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MU07-AR-1 | Experimental chain | Gammasphere coincidence gates → angle-dependent Doppler line shapes → lifetimes → `B(M1)/B(E2)` for both bands. | PDF pp.1–3, Table I, Figs.1–3 | self-checking |
| MU07-AR-2 | Model chain | PQTAC mean field → RPA phonon around the TAC minimum → partner splitting/interband rates; TAC intraband strengths remain baseline. | PDF pp.2–4, Eqs.1–3, Fig.4 | self-checking |
| MU07-AR-3 | Identity transfer | Chiral label requires partner-band energy, parity, geometry and electromagnetic similarity; this source is not a wobbling proof. | PDF pp.1–4 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[nuclear-chirality]], [[tilted-axis-cranking]], [[random-phase-approximation]], [[doppler-shift-attenuation-method]] and the `135Nd` experimental TiP/chirality reference map.
- New reusable rule: use absolute lifetimes and partner-band `B(E2)/B(M1)` similarity as a companion-observable test; do not infer static chirality from energy degeneracy alone.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MU07-P0-1`: Preserve DSAM/feeding and TAC+RPA interpretation boundaries; `135Nd` is a nucleus-specific chiral reference, not a universal band-identity template.

## Extracted Pages

- Concepts/projects: [[nuclear-chirality]], [[tilted-axis-cranking]], [[random-phase-approximation]], [[doppler-shift-attenuation-method]]。
