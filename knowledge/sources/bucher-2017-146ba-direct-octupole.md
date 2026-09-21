---
type: source
title: "Bucher et al. 2017 - Direct evidence for octupole deformation in 146Ba"
aliases: [Bucher 2017 146Ba direct E3]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Direct Evidence for Octupole Deformation in 146Ba and the Origin of Large E1 Moment Variations in Reflection-Asymmetric Nuclei"
authors: [B. Bucher, S. Zhu, C. Y. Wu, R. V. F. Janssens, R. N. Bernard, L. M. Robledo, T. R. Rodriguez, D. Cline, A. B. Hayes, A. D. Ayangeakaa, M. Q. Buckner, C. M. Campbell, M. P. Carpenter, J. A. Clark, H. L. Crawford, H. M. David, C. Dickerson, J. Harker, C. R. Hoffman, B. P. Kay, F. G. Kondev, T. Lauritsen, A. O. Macchiavelli, R. C. Pardo, G. Savard, R. Vondrasek]
journal: "Physical Review Letters"
year: 2017
volume: 118
pages: "152504"
doi: "10.1103/PhysRevLett.118.152504"
citation_key: Bucher_2017
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevLett.118.152504"
alternate_source: "https://arxiv.org/abs/1703.05268"
raw_file: "raw/papers/gpt/high-spin-20260920/external-146ba/PDFs/Direct_Evidence_for_Octupole_Deformation_in_146Ba_and_the_Origin_of_Large_E1_Moment_Variations_in_Reflection-Asymmetric_Nuclei.pdf"
raw_sha256: "c49cb44350cd24f25d172efe405cd9e78360692eb4087bb3eef1801534264beb"
nuclei: [146Ba, 144Ba, 148Ba, 208Pb]
reactions: [sub-barrier-coulomb-excitation]
experiments: [CARIBU, ATLAS, CHICO2, GRETINA]
models: [GOSIA, symmetry-conserving-configuration-mixing, Gogny-D1S-HFB]
observables: [B(E3), B(E1), Q3, electric-dipole-moment, octupole-collectivity]
methods: [coulomb-excitation, gamma-ray-tracking, particle-gamma-coincidence]
tags: [146Ba, octupole, E3, E1, external-research]
---

# Direct evidence for octupole deformation in `146Ba`

## Bibliographic Record

- B. Bucher *et al.*, *Phys. Rev. Lett.* **118**, 152504 (2017), DOI `10.1103/PhysRevLett.118.152504`.
- Local full text: lawful arXiv copy `1703.05268`, SHA-256 recorded in `EXT-20260921-001`.

## Scope and Reading Depth

- Six-page manuscript read end-to-end: motivation, CARIBU/ATLAS/CHICO2/GRETINA setup, GOSIA fit, Table I, `B(E3)`/`B(E1)` comparison, SCCM/GCM interpretation, orbital-occupancy explanation and alternative high-spin interpretations.
- No SI was requested or supplied. The local copy is used for evidence audit; the published DOI is the bibliographic anchor.

## Question and Evidence

The paper tests whether the sharp reduction of the intrinsic electric-dipole moment in `146Ba` signals weakened octupole collectivity. A `659 MeV` `146Ba` beam was Coulomb excited on `208Pb`; CHICO2 separated `A=146` products and GRETINA measured the γ yields. GOSIA fitted E1/E2/E3 matrix elements, then released rigid-rotor coupling when estimating uncertainties (PDF pp.2–3, Fig.1–2, Table I).

The direct ground-state E3 matrix element is `0.65(+0.14/−0.20) eb^{3/2}`, corresponding to `B(E3;3−→0+)=48(+21/−29) W.u.`. This is essentially the same strength as the `144Ba` result. The small E1 strength is therefore not evidence for quenched octupole collectivity; the SCCM calculation attributes the E1 suppression to neutron-orbital occupancy and cancellation of intrinsic dipole contributions (PDF pp.3–5, Table I, Figs.3–5).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EXT146-1 | Direct Coulomb excitation measures `B(E3;3−→0+)=48(+21/−29) W.u.` in `146Ba`. | experiment-result | direct | PDF pp.2–3, Table I | true |
| EXT146-2 | `146Ba` has strong octupole collectivity despite a more than order-of-magnitude dipole-moment reduction relative to `144Ba`. | cross-isotope-result | mixed | PDF pp.1, 3–5 | true |
| EXT146-3 | SCCM/GCM connects E1 variation to neutron-orbital occupancy and projected intrinsic-state overlap. | model-result | mixed | PDF pp.3–5, Figs.3–5 | true |

## Summary

This external source materially strengthens the octupole evidence ladder: direct E3 strength persists from `144Ba` to `146Ba`, while E1 strength varies independently with microscopic occupancy.

## Counter-evidence and Competing Interpretations

- Sudden band alignment and the `146Ba` high-spin behavior had motivated hypotheses of quenched octupole strength, a reflection-symmetric shape, or aligned octupole phonons; the direct E3 result rejects the first as a sufficient explanation while leaving the alternatives as model questions.
- GOSIA uncertainties are statistics limited, and E1 matrix elements are constrained mostly by prior data rather than new yields.

## Model Dependence

The SCCM calculation uses axially symmetric quadrupole and octupole coordinates, angular-momentum/parity/particle-number projection and Gogny D1S. It explains E1 variation within that model space; it does not turn the inferred `β2/β3` landscape into a model-independent laboratory shape measurement.

## Limitations and Missing Evidence

- Raw event matrices, full GOSIA covariance and SCCM code are unavailable.
- `146Ba` is a related but independent experiment, so it strengthens the isotope systematics without replacing the `144Ba` source.

## Competing Interpretations and Limitations

The high-spin alignment and sudden E1 reduction had motivated quenched-octupole, reflection-symmetric-shape and aligned-octupole-phonon explanations. The direct E3 result rules out a simple “small E1 means weak octupole” inference, while the detailed microscopic occupancy mechanism remains model dependent.

## Knowledge Impact and Learning Decision

- Effect: `supports` and `revises` [[octupole-deformation]], [[octupole-correlation]], [[octupole-and-rare-electromagnetic-decay]] and the `144Ba` direct-E3 evidence map.
- External increment: direct neighboring-isotope E3 evidence separates octupole strength from E1 dipole-moment size.
- Review state: Codex self-audited; not `human-reviewed`.

## Extracted Pages

- Nuclei/concepts: `146Ba`, [[octupole-deformation]], [[octupole-correlation]], [[octupole-and-rare-electromagnetic-decay]]。

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[octupole-deformation]], [[octupole-correlation]], [[octupole-and-rare-electromagnetic-decay]]
