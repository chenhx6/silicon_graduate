---
type: source
title: "Probing 93mMo Isomer Depletion with an Isomer Beam"
aliases: [Guo 2022 Mo93m isomer beam, Guo 2022 PRL null-limit]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "Probing 93mMo Isomer Depletion with an Isomer Beam"
authors: [S. Guo, B. Ding, X. H. Zhou, Y. B. Wu, J. G. Wang, S. W. Xu, Y. D. Fang, C. M. Petrache, E. A. Lawrie, Y. H. Qiang, Y. Y. Yang, H. J. Ong, J. B. Ma, J. L. Chen, F. Fang, Y. H. Yu, B. F. Lv, F. F. Zeng, Q. B. Zeng, H. Huang, Z. H. Jia, C. X. Jia, W. Liang, Y. Li, N. W. Huang, L. J. Liu, Y. Zheng, W. Q. Zhang, A. Rohilla, Z. Bai, S. L. Jin, K. Wang, F. F. Duan, G. Yang, J. H. Li, J. H. Xu, G. S. Li, M. L. Liu, Z. Liu, Z. G. Gan, M. Wang, Y. H. Zhang]
journal: Physical Review Letters
year: 2022
volume: 128
pages: 242502
doi: 10.1103/PhysRevLett.128.242502
language: en
canonical_source: doi:10.1103/PhysRevLett.128.242502
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2022_Guo et al_Probing Mo 93 m Isomer Depletion with an Isomer Beam.pdf"
raw_sha256: ec3d4f308c1083124d5c8be87417c39ec2804f9568ba6f7901d84d15c7b24652
archive_required: true
nuclei: [93mo, 92zr, 91zr, 90zr]
reactions: ["12C(86Kr,5n)93mMo"]
observables: [isomer-depletion-upper-limit, isomer-decay-yields, coincident-gamma-spectra]
methods: [secondary-isomer-beam-line, ribll-hirfl-csr, implantation-gamma-coincidence, anti-compton-clover-array]
tags: [mo93m, isomer-beam, ribll, null-limit, neec-refutation-under-beam-foil, experimental-control]
---

# Guo et al. (2022): Probing \(^{93\text{m}}\)Mo Isomer Depletion with an Isomer Beam

## Bibliographic Record

S. Guo, B. Ding, X. H. Zhou, Y. B. Wu, J. G. Wang, S. W. Xu, Y. D. Fang, C. M. Petrache, E. A. Lawrie, Y. H. Qiang, Y. Y. Yang, H. J. Ong, J. B. Ma, J. L. Chen, F. Fang, et al., "Probing \(^{93\text{m}}\)Mo Isomer Depletion with an Isomer Beam," *Physical Review Letters* **128**, 242502 (2022), DOI: `10.1103/PhysRevLett.128.242502`. Primary PDF is 6 pages, SHA-256: `ec3d4f308c1083124d5c8be87417c39ec2804f9568ba6f7901d84d15c7b24652`.

## Scope and Reading Depth

The 6-page Letter was read completely. Locators examined: secondary beamline RIBLL layout (PDF p. 2 / printed p. 242502-2, Fig. 1), HPGe \(\gamma\)-ray spectra and 268-keV fit inset (PDF p. 3 / printed p. 242502-3, Fig. 2a--c), upper limit formulas Eqs. (1)--(3) and Table I coefficients (PDF p. 3--4 / printed p. 242502-3--4), and relativistic theory comparison (PDF p. 4 / printed p. 242502-4, Eqs. 4--5).

## Summary

The authors re-investigate \(^{93\text{m}}\)Mo isomer depletion using a secondary isomer beam at HIRFL-CSR / RIBLL to isolate stopping from primary reaction backgrounds. Selecting \(^{93\text{m}}\text{Mo}^{36+}\) ions at 460 MeV, they observe 570 counts in the 266.5--269.5 keV window against an estimated Compton background of 596 counts, with no statistically significant peak above background. With \(1.763(1) \times 10^6\) spontaneous isomer decay photons detected at 263 keV during beam-on, an upper limit \(P_{\text{max}} \approx 2 \times 10^{-5}\) is extracted using the \(3\sigma\) background lower bound.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-1 | Delivers 460-MeV 93mMo36+ ions through 35-m RIBLL beamline (purity ~0.6%), isolating stopping foil from prompt reaction gamma-rays. | experimental-design | direct experimental report | printed p.242502-2, Fig. 1 | true |
| GU22-2 | In 266.5-269.5 keV window, observes 570 counts vs estimated 596 Compton background counts (3-sigma lower limit 523 counts; no significant peak). | experimental-null-result | direct measurement | printed p.242502-3, Fig. 2c inset | true |
| GU22-3 | Detects 1.763(1)e6 263-keV isomer decay photons during beam-on; extracts upper bound of ~50 peak counts using 3-sigma background lower bound and 95% Gaussian fraction. | quantitative-limit | derived value | printed p.242502-3--4, Eqs. (1)--(3) | true |
| GU22-4 | Establishes upper limit P_max ~ 2e-5 (factor of 500 below Chiara 2018), consistent with relativistic atomic theory (~2.3e-12 at 460 MeV). | quantitative-limit | derived experimental bound | printed p.242502-3--4, Table I | true |

## Competing Interpretations and Limitations

Guo 2022 strengthens counterevidence against the 1% claim under its specific stopping conditions (460-MeV ions in carbon foil). It does not represent a unique forensic reconstruction of the 2018 ATLAS target environment, nor does it disprove NEEC as a physical process, because the theoretical NEEC rate in carbon (\(\sim 10^{-11}\)) remains far below the \(2 \times 10^{-5}\) sensitivity threshold.

## Extracted Pages

- mo93m
- isomer-beam
- ribll
- neec
