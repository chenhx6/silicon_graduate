---
type: source
title: "Chen et al. 2017 - Chiral geometry in symmetry-restored states: 128Cs"
aliases: [Chen 2017 128Cs angular-momentum projection]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Chiral geometry in symmetry restored states: Chiral doublet bands in 128Cs"
authors: [F. Q. Chen, Q. B. Chen, Y. A. Luo, J. Meng, S. Q. Zhang]
journal: "Physical Review C"
year: 2017
volume: 96
article_number: "051303"
doi: "10.1103/PhysRevC.96.051303"
arxiv: "1708.07282v1"
canonical_source: "https://doi.org/10.1103/PhysRevC.96.051303"
full_text_url: "https://arxiv.org/pdf/1708.07282v1"
downloaded_pdf_sha256: "d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6"
nuclei: [128Cs]
models: [angular-momentum-projection, particle-number-projection, pairing-plus-quadrupole]
observables: [energy-spectrum, B(E2), B(M1), K-distribution, angular-momentum-orientation]
methods: [symmetry-restoration, Hill-Wheeler-equation]
tags: [128Cs, chirality, angular-momentum-projection, transition-strengths, spin-dependent-geometry]
citation_key: "Chen_2017"
raw_file: "raw/papers/codex-day10/chen-2017-128cs.pdf"
raw_sha256: "d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6"
---

# Chiral geometry in symmetry-restored states: chiral doublet bands in 128Cs

## Bibliographic Record

- F. Q. Chen, Q. B. Chen, Y. A. Luo, J. Meng, and S. Q. Zhang, *Phys. Rev. C* **96**, 051303 (2017), DOI 10.1103/PhysRevC.96.051303.
- arXiv version 1: [1708.07282](https://arxiv.org/abs/1708.07282v1), posted 2017-08-24. DOI, title, author list, volume, and article number were checked against Crossref; the arXiv metadata identifies this version.
- The full text was read from the arXiv PDF. The temporary PDF copy had SHA-256 d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6.

## Scope and Reading Depth

The main line was read from the model definition through the symmetry-restored basis, transition-strength comparison, K-distributions, angular-momentum orientation profiles, conclusions, and the references relevant to the experimental input. Figures 1–4 and Eqs. (1)–(11) were inspected. This is a theoretical calculation; its plotted experimental points are imported comparison data.

## Model and Observable Chain

The authors diagonalize a pairing-plus-quadrupole Hamiltonian in a basis with angular-momentum and particle-number projection. The orientation analysis uses distributions of angular-momentum components along the intrinsic short, intermediate, and long axes, plus the tilted-angle profile in the intrinsic frame. The calculation takes the Hamiltonian parameters from Ref. 40 and constrains the deformation to (β, γ) = (0.20, 30.0°); the blocked configuration is the lowest πh11/2 and fourth νh11/2 orbital. These are model inputs, not measurements made in this paper.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CHEN17-1 | The starting Hamiltonian contains spherical single-particle, quadrupole-quadrupole, monopole-pairing, and quadrupole-pairing terms. | model-definition | model | PDF Eq. (1) | true |
| CHEN17-2 | The working basis restores angular momentum and neutron/proton number before configuration mixing. | model-definition | model | PDF Eq. (3) | true |
| CHEN17-3 | The 128Cs calculation fixes (β, γ)=(0.20,30.0°) and blocks a low πh11/2 orbital with the fourth νh11/2 orbital. | model-input | model | printed p. 5 | true |
| CHEN17-4 | Figure 2 compares calculated partner-band energies and intra/inter-band transition strengths with the data available from Ref. [14]. | model-comparison | mixed | Figure 2 | true |
| CHEN17-5 | The calculated B(E2) agrees near the bandhead but departs from the data at higher spin; the authors attribute the trend to the frozen nuclear shape. | model-limit | model | printed p. 5 | true |
| CHEN17-6 | The calculated K-distributions show chiral-vibration behavior near I=11ℏ, a static-chirality region around I=14ℏ, and a weakened pattern by I=18ℏ. | model-result | model | Figure 3 | true |
| CHEN17-7 | The calculated angular-momentum profiles place band A mainly in an s-l plane at I=11ℏ, in two handed orientations at I=14ℏ, and back toward a planar i-s orientation at I=18ℏ. | model-result | model | Figure 4 | true |
| CHEN17-8 | The transition-strength points in Figure 2 are comparison data cited to Grodner et al. 2006, rather than a new experiment in the AMP paper. | source-lineage | direct | Reference [14] | true |

## Figure-Level Reading

- Figure 2 places experimental points and AMP curves on the same energy and B-value panels. The authors report good energy reproduction and similar B(E2) in the two bands; the high-spin B(E2) trend does not follow the data because the shape is frozen. The M1 staggering appears in the calculation, but no geometry is directly measured by these strength curves.
- Figure 3 presents model K-distributions at I=11, 14, 18ℏ. The authors interpret the low-spin distributions as vibration about the s-l plane, the I=14ℏ distributions as two-handed orientations, and the less similar partner distributions at I=18ℏ as a weakening of static chirality.
- Figure 4 gives model angular-momentum orientation profiles. At I=11ℏ, band A is mainly planar while band B has two orientations; at I=14ℏ, both bands have paired orientations with finite tunneling probability; at I=18ℏ, the static-chirality pattern disappears in the model. This is a spin-dependent theoretical geometry, not a direct experimental assignment.

## Limitations and Evidence Boundary

The calculation imports the transition-strength and energy data cited as Ref. [14], fixes the deformation and blocked orbitals, and does not provide an experimental response/covariance reanalysis. The reported high-spin B(E2) mismatch is an explicit model limitation. A separately measured 128Cs g factor may be a complementary observable, but the present paper does not calculate that g factor; the different spin points and model frameworks prevent treating the two articles as a direct validation pair.

The detailed band-label crosswalk between Chen et al.'s A/B and the 2006 paper's yrast/side labels is not asserted here without a transition-by-transition verification.

## Summary

This is a symmetry-restored model study of the 128Cs partner bands. It calculates spin-dependent angular-momentum geometry and electromagnetic strengths, while reusing rather than independently remeasuring the Grodner 2006 data.

## Key Results

- CHEN17-1/2/3 describe the pairing-plus-quadrupole Hamiltonian, projection procedure, and fixed-shape inputs.
- CHEN17-4/5 compare calculated transition strengths with the 2006 data and show a high-spin B(E2) deviation.
- CHEN17-6/7 give spin-dependent K and angular-momentum geometry; CHEN17-8 identifies reuse of the Grodner 2006 experiment.

## Competing Interpretations and Limitations

The calculated geometry is model output, not a direct observation. The fixed-shape calculation departs from the high-spin B(E2) data, and the plotted experimental strengths are reused from Grodner 2006 rather than an independent dataset.

## Extracted Pages

- [[chirality-wobbling-competition-evidence]]
- [[grodner-2006-128cs-chiral-doublet-lifetimes]]
