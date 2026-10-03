---
type: source
title: "Nomura et al. 2018 - Octupole correlations in neutron-rich odd-mass barium isotopes"
aliases: [Nomura 2018 odd-mass Ba octupole, 143Ba 145Ba 147Ba octupole model]
created: 2026-10-03
updated: 2026-10-03
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Signatures of octupole correlations in neutron-rich odd-mass barium isotopes"
authors: [K. Nomura, T. Nikšić, D. Vretenar]
journal: "Physical Review C"
year: 2018
volume: 97
pages: "024317"
doi: "10.1103/PhysRevC.97.024317"
arxiv: "1711.09587v2"
citation_key: nomura_2018_Signaturesoctupole
citation_key_origin: DOI-and-arXiv-metadata
citation_key_verified: 2026-10-03
canonical_source: "https://doi.org/10.1103/PhysRevC.97.024317"
raw_file: "raw/papers/gpt/day5-20261003/nomura-2018-odd-mass-ba-octupole.pdf"
raw_sha256: 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be
data_url: "https://arxiv.org/pdf/1711.09587v2"
data_sha256: 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be
data_bytes: 791515
retrieved: 2026-10-03
nuclei: [142ba, 143ba, 144ba, 145ba, 146ba, 147ba]
reactions: []
experiments: [adopted-spectroscopy-used-for-model-comparison]
models: [density-functional-theory, DD-PC1, interacting-boson-model, interacting-boson-fermion-model]
observables: [beta2-beta3-energy-surface, level-energy, spin-parity, b-e2, b-e3, orbital-occupation]
methods: [constrained-relativistic-hartree-bogoliubov, particle-core-coupling]
tags: [octupole, odd-mass-barium, model-result, beta3-softness, state-dependence]
---

# Nomura et al. (2018): octupole correlations in neutron-rich odd-mass barium isotopes

## Bibliographic Record

Crossref identifies K. Nomura, T. Nikšić, and D. Vretenar, Physical Review C 97, 024317 (2018), DOI 10.1103/PhysRevC.97.024317. The paper is available as arXiv:1711.09587v2. The arXiv PDF is 11 pages, 791,515 bytes, SHA-256 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be.

## Scope and Reading Depth

The full paper and its seven figures, nine tables, methods, parameter adjustment, odd-A comparisons, and conclusions were read. The study calculates even-even 142,144,146Ba cores and odd-mass 143,145,147Ba; it does not report new measurements. The model is axial in beta-two and beta-three and does not include gamma softness.

## Model and Evidence Chain

Constrained relativistic Hartree-Bogoliubov calculations with DD-PC1 and finite-range separable pairing generate axial beta-two/beta-three energy surfaces, neutron single-particle energies, and occupation probabilities. These are mapped to an sdf interacting-boson model and an interacting-boson-fermion model. Fourteen boson-fermion parameters are adjusted to selected 145Ba low-energy spectra; the neighboring 143Ba and 147Ba parameter sets are then chosen under a gradual-variation assumption. This is a calibrated model comparison, not an independent experiment or parameter-free prediction.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NOM18-1 | The calculation uses axial beta-two/beta-three CDFT+IBFM, with the sdf boson core, odd neutron, and boson-fermion strengths fitted to selected odd-Ba data, especially 145Ba. | model-method | direct | PDF pp.1-4, Secs. II–IV, Table III | true |
| NOM18-2 | DD-PC1 even-core surfaces give 142Ba a beta-three=0 minimum, while 144Ba and 146Ba have nonzero beta-three minima near 0.1 that are soft in the beta-three direction. | model-result | direct | PDF p.5, Fig.1 and text below | true |
| NOM18-3 | For 143Ba, 145Ba, and 147Ba, the calculated lowest positive- and negative-parity states are predominantly odd-neutron plus sd-boson configurations; the paper concludes octupole deformation does not determine their lowest near-ground states. | model-result | direct | PDF pp.6-10, Figs.3-7, Tables V-IX, Conclusions | true |
| NOM18-4 | The 145Ba calculation assigns higher states, including a 15/2− candidate, substantial f-boson/octupole character and predicts E3 transitions to the ground-state band; these are model strengths, not newly measured B(E3) values. | model-result | direct | PDF pp.7-8, Fig.6, Table VII and discussion | true |
| NOM18-5 | For 147Ba, the calculated ground-state spin is 3/2− while the experimental assignment is 5/2−; changing the 1h9/2 occupation by 25% can repair the ordering, but the authors reject that adjustment as unjustified. | model-limit | direct | PDF p.9, Fig.7, Table IX and discussion | true |
| NOM18-6 | The odd-Ba results are state- and orbital-occupation dependent: enhanced even-core octupole collectivity does not imply octupole dominance in the odd nucleus's lowest bands. | model-synthesis | direct | PDF p.10, Conclusions | true |

## Summary

The calculation separates three levels of claim: even-even Ba core surfaces with soft nonzero beta-three minima; odd-neutron low states whose wave functions are mainly in the sd space; and selected higher odd-A states with substantial f-boson content and predicted E3 transitions. The paper supports an excitation- and occupation-dependent model picture. Its beta-three landscapes and transition strengths are calculations, not new observations.

## Competing Interpretations and Limitations

- The axial model cannot test gamma softness, gamma rigidity, or triaxial particle-core coupling.
- Boson-fermion strengths are fitted to selected 145Ba spectra; 143Ba and 147Ba depend on assumed smooth parameter evolution.
- The 147Ba ground-state spin mismatch remains; the authors' 25% occupation sensitivity check is not accepted as a justified refit.
- Predicted E3 strengths for odd-A states await matching measurements. Agreement with cited Ba data is not an independent measurement.
- 143,145,147Ba have different proton/neutron occupations from 131Ce (Z=58, N=73); quantitative beta-three or low-state assignments cannot be transferred to 131Ce.

## Knowledge Impact and Learning Decision

- Effect: supports state- and occupation-dependent octupole expectations while limiting transfer from 144/146Ba even-core E3 measurements to neighboring odd-A structures.
- Relation to [[bucher-2016-144ba-direct-octupole]] and [[bucher-2017-146ba-direct-octupole]]: the calculation supplies an axial model interpretation of their even-core region, not a second data set.
- Review state: unreviewed; this page does not mark model outputs as experimental facts or as human-reviewed.

## Extracted Pages

- Models: density-functional theory, sdf-IBM, IBFM.
- Nuclei: 142Ba, 143Ba, 144Ba, 145Ba, 146Ba, 147Ba.
- Related source: [[nomura-2017-odd-mass-gamma-soft-shape-transitions]]; same authors/model family, a separate calculation and not an independent experimental lineage.

## Sources and Relationships

- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[gaffney-2013-pear-shaped-rn-ra]]
- [[nomura-2017-odd-mass-gamma-soft-shape-transitions]]
- [[shape-observable-matrix]]
