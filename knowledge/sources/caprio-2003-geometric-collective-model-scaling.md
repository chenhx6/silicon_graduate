---
type: source
title: "Caprio 2003 - Scaling and limits of the geometric collective model"
aliases: [Caprio 2003 GCM 054303]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Simplified approach to the application of the geometric collective model"
authors: [M. A. Caprio]
journal: "Physical Review C"
year: 2003
volume: 68
pages: "054303"
doi: "10.1103/PhysRevC.68.054303"
arxiv: "nucl-th/0310013v1"
canonical_source: "Caprio, Phys. Rev. C 68, 054303 (2003)"
raw_file: "raw/papers/gpt/query/20261121-caprio-gcm-scaling/Caprio2003-arxiv-v1.pdf"
raw_sha256: "dfc3aff09186a606de7a0f6b680df5729adf09c8fb4c5cf16e25fa5e1935a62d"
archive_required: true
nuclei: [102Pd]
models: [geometric-collective-model, Bohr-Hamiltonian]
observables: [excitation-energy, B-E2, quadrupole-shape]
tags: [collective-model, scaling, finite-nuclei, gamma-softness]
---

# Geometric collective model scaling and the \(^{102}\mathrm{Pd}\) test

## Bibliographic Record

M. A. Caprio, *Phys. Rev. C* 68, 054303 (2003), DOI `10.1103/PhysRevC.68.054303`. The 15-page local reading copy is arXiv `nucl-th/0310013v1`, submitted 2 October 2003. The 2019 date in the title block is retained as a compilation date. The APS full-text endpoint returned HTTP 401.

## Scope and Reading Depth

The main argument, analytic scaling, extrema, numerical maps, \(^{102}\mathrm{Pd}\) illustration, appendix and references were read in the local v1. Key equations and figures were checked in the rendered PDF. The EPAPS grid and extraction code, and line-by-line comparison to the journal edition, remain outside this coverage.

## Summary

The paper truncates the collective Hamiltonian to the leading kinetic term and the \(\beta^2,\beta^3\cos3\gamma,\beta^4\) potential terms. Reparameterizing \(V\) gives \(d\) for potential shape, \(e\) for radial scale, and \(f\) for energy scale. With the stated scaling laws, \(d\) and \(S=1/(B_2e^2f)\) describe a family of equivalent normalized spectra. Linear E2 operators also give invariant \(B(E2)\) ratios under this rescaling.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| CAP03-1 | Matching the \(\beta^2\) coefficient of Eqs. (4) and (6) gives \(d=112C_2C_4/(9\sqrt{5}C_3^2)\) with \(e=C_3/C_4,\ f=C_3^4/C_4^3\). | derivation | direct | arXiv PDF pp.2–3, Eqs. (4), (6)–(7) |
| CAP03-2 | For the stated prolate-sign convention, \(0<d<1\) has spherical and prolate local minima. At \(d=8/9\) the minima are degenerate. The nonzero radial extrema merge at \(d=1\). The quantum spectrum also depends on kinetic scale \(S\). | model-result | direct | arXiv PDF pp.3–7, Eqs. (8)–(13), Figs. 1–7 |
| CAP03-3 | The \(^{102}\mathrm{Pd}\) GCM example with \(d=-43\), \(S=56\times10^{42}\,\mathrm{MeV}^{-2}\mathrm{s}^{-2}\) improves selected branching comparisons relative to the ideal \(E(5)\) calculation. Three quoted transitions still have calculated strengths two to three times the observed values. | model-and-data-comparison | direct | arXiv PDF pp.11–13, Sec. V and Figs. 11–14 |

## Competing Interpretations and Limitations

- The angular dependence is linear in \(\cos3\gamma\), allowing axial extrema or \(\gamma\) independence in this truncation. Describing a rigid triaxial minimum requires additional model terms. Small excitation splittings or a broad probability distribution in \(\gamma\) do not suffice to infer such a minimum.
- A quadratic term in the E2 operator scales differently from the linear term and generally removes the exact invariance of \(B(E2)\) ratios. The basis truncation leads to convergence failures for some strongly deformed cases or multiple minima, as indicated by the upper-basis weight in Fig. 10(b).
- The \(^{102}\mathrm{Pd}\) data come from Ref. 33. The paper discusses the 1593 keV \(0^+\) level as a likely intruder and considers the 1658 keV level in its collective comparison. The model uses previous data as calibration and comparison, and the intruder interpretation depends on the isotonic comparison.
- [[book-casten-nuclear-structure-simple-perspective]] second-edition Eq. (6.82) prints \(\sqrt2\) in the forward \(d\) conversion. The coefficient in the same textbook's potential, its inverse \(C_2\) expression, and Eq. (7) here instead require \(\sqrt5\).

## Extracted Pages

- PDF pp.1–4, Hamiltonian, scaling, conversion and extrema.
- PDF pp.5–11, spectral regimes, numerical maps, convergence and EPAPS scope.
- PDF pp.11–15, \(^{102}\mathrm{Pd}\), conclusion, dilation appendix and references.
