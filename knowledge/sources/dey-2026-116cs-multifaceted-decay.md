---
type: source
title: "Dey et al. 2026 - Multifaceted decay of 116Cs"
aliases: [Dey 2026 116Cs decay]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Multifaceted Decay of 116Cs"
authors: [J. Dey, U. Datta, O. Tengblad, P. Das, A. Rahaman, B. K. Agrawal, S. Chakraborty, A. Gottberg, M. Kowalska, K. Mahata, S. Mandal, M. Madurga, E. Nacher, E. Rapisarda, N. Warr, W. Sengupta, C. Sharma, T. Stora]
journal: "Physical Review Letters"
year: 2026
volume: 137
pages: "012501"
doi: "10.1103/ztcl-lpdf"
citation_key: Dey_2026
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/ztcl-lpdf"
library_file: "raw/papers/gpt/high-spin-20260920/衰变/2026_Dey et al_Multifaceted Decay of Cs 116.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/衰变/2026_Dey et al_Multifaceted Decay of Cs 116.pdf"
raw_sha256: "f44415e0934f0550238adf9853d41760e1bf456f311f30b5c8dba27dbe442563"
nuclei: [116Cs, 116Xe, 115I, 104In]
reactions: [ISOLDE-spallation-fragmentation]
experiments: [ISOLDE, DSSD, PAD, Clover]
models: [density-dependent-point-coupling, relativistic-Hartree-Bogoliubov, QRPA, Lednicky-Lyuboshits-correlation]
observables: [delayed-proton, delayed-two-proton, alpha-decay, cluster-radioactivity, octupole-resonance, relative-momentum]
methods: [particle-spectroscopy, gamma-spectroscopy, Bayesian-peak-fit, chi-square-fit]
tags: [116Cs, proton-drip-line, two-proton-decay, cluster-emission, octupole-resonance]
---

# Multifaceted decay of `116Cs`

## Bibliographic Record

- J. Dey *et al.* (ISOLDE Collaboration), *Phys. Rev. Lett.* **137**, 012501 (2026), published 29 June 2026; the PDF records a 17 July 2026 correction adding the collaboration name.

## Scope and Reading Depth

- The six-page PRL was read end-to-end, including setup, delayed-particle spectra, Tables I–II, Figs.1–6, octupole-resonance assignment, two-proton correlation, heavy-cluster analysis, data/code availability and conclusion.

## Experiment and Main Findings

`116Cs` was implanted at ISOLDE and studied with thin/thick DSSDs, silicon-pad detectors and four Clover arrays. The delayed γ half-life fit gives `T1/2=0.86(15) s` for the low-spin component, consistent with prior work; the longer-lived `6+` isomer is `3.85(13) s` (PDF pp.1–2, Fig.2). Six `116Xe` proton-unbound states at `5.45(2), 5.95(6), 6.4(1), 7.02(3), 7.53(4), 7.66(8) MeV` are fitted with both χ² and Bayesian methods (Table I, pp.2–3).

The broad `7.66(8) MeV` state is assigned `3−`/low-energy isoscalar octupole resonance using EC/β+ and log-ft information plus density-dependent point-coupling RHB+QRPA calculations (p.3, Fig.3). Proton decay from it populates comparable `11/2−` and `11/2+` states in `115I`, providing a parity-sensitive companion observation rather than a direct E3 matrix element.

Delayed two-proton events are selected by two-hit DSSD conditions, timing, front/back energy equality and cross-talk rejection. The opening-angle distribution peaks at `39(3)°` with width `13.4(44)°`; roughly `27(11)%` of the events fall in this direct/simultaneous-like component (p.4, Fig.4). Lednicky–Lyuboshits fits favor a large scattering length around `15 fm` and emission-point radius `d≈2.6 fm`, but low statistics and overlap with the broad octupole state limit the correlation inference.

Energy deposition above the delayed-α endpoint is interpreted as possible `12C` cluster emission. The inferred branch is about `2.7(18)×10⁻5%`, with `log10 T1/2(s)=6.5(3)`; Table II compares it with UDL/Horoi estimates (pp.4–5, Fig.5). Data are not public; authors offer data on reasonable request and code on request.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DEY26-1 | Six `116Xe` proton-unbound states are fitted consistently in χ²/Bayesian analyses. | experiment-result | direct | PDF pp.2–3, Table I | true |
| DEY26-2 | The 7.66-MeV state is assigned as a low-energy isoscalar octupole resonance with parity-tagged proton decay. | model-linked-assignment | mixed | PDF p.3, Fig.3 | true |
| DEY26-3 | Delayed 2p and possible `12C` emission are reported, with low-statistics/correlation boundaries. | exotic-decay-result | direct | PDF pp.4–5, Figs.4–5, Table II | true |

## Summary

Dey *et al.* combine particle and γ spectroscopy to expose several drip-line decay channels; the exotic-decay claims remain model- and statistics-sensitive.

## Competing Interpretations and Limitations

- The broad octupole state overlaps the 2p-decay energy region, complicating a unique parent-state assignment.
- The `12C` interpretation is based on excess energy deposition and low-count statistics, not a full mass-resolved event reconstruction.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| DEY26-AR-1 | State identity | Peak positions agree between χ² and Bayesian fits, but widths differ; the 7.66-MeV `3−` assignment combines decay-systematics and model support. | PDF pp.2–3, Table I, Fig.3 | self-checking |
| DEY26-AR-2 | Two-proton correlation | Opening angle and relative momentum support a direct/correlated component, but the broad parent-state overlap and small counts prevent a unique decay-mechanism proof. | PDF p.4, Fig.4 | self-checking |
| DEY26-AR-3 | Cluster claim | High energy deposition is compatible with `12C`, yet the branch is a low-statistics inference and is not an identified particle-by-particle mass measurement. | PDF pp.4–5, Fig.5, Table II | self-checking |
| DEY26-AR-4 | L4 readiness | Raw data and analysis code are not publicly deposited; no reproducible L4 re-fit is possible from the supplied paper. | PDF p.6, data/code availability | stopped-input-missing |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[drip-line-radioactivity]], [[octupole-correlation]] and proton/cluster-decay evidence; it is an exotic-decay comparator, not an A≈130 high-spin band source.
- L3 question: how can parity-tagged proton decay and two-proton correlation be combined without promoting a model-supported octupole assignment to direct E3 evidence?
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DEY26-P0-1`: Preserve low-statistics, model-assignment and unavailable-data boundaries for the `2p`/`12C` claims.

## Extracted Pages

- Nuclei/methods: `116Cs`, `116Xe`, [[drip-line-radioactivity]], [[octupole-correlation]]。
