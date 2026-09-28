---
type: source
title: "Radford et al. 2005 - Coulomb excitation and transfer reactions with neutron-rich radioactive beams"
aliases: [130Sn B(E2) Coulomb excitation, Radford 2005 Sn transition strength]
created: 2026-09-29
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: journal-article-coulomb-excitation-experiment
reading_depth: deep-read
citation_key: Radford2005EPJA130Sn
title_original: "Coulomb excitation and transfer reactions with neutron-rich radioactive beams"
authors: [D.C. Radford, et al.]
journal: European Physical Journal A
year: 2005
volume: 25
issue: Supplement 1
pages: 383-387
doi: 10.1140/epjad/i2005-06-205-y
language: en
canonical_source: doi:10.1140/epjad/i2005-06-205-y
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/radford-2005-130sn-coulex-source.pdf"
raw_sha256: 9d3325519c41ddf1440b76f2b45dbac0788617ee0c2a872435c6e82b15b123ed
nuclei: [126sn, 128sn, 130sn, 132te, 134te, 136te, 132sn, 134sn]
reactions: ["126Sn/128Sn/130Sn Coulomb excitation on natural carbon"]
experiments: [hribf-coulomb-excitation-sn126-130]
models: [winther-deboer-coulomb-excitation]
observables: [b-e2, first-2plus-energy]
methods: [inverse-kinematics-coulomb-excitation, gamma-ray-detection, Rutherford-normalization]
tags: [sn130, sn128, n80, n82, b-e2, coulomb-excitation, preliminary-result]
---

# Coulomb excitation of neutron-rich Sn isotopes in the HRIBF program

## Bibliographic Record

D.C. Radford et al., European Physical Journal A 25, Supplement 1, 383–387 (2005), DOI 10.1140/epjad/i2005-06-205-y. Crossref metadata and the publisher PDF agree on the title and article locator. The five-page article reports direct inverse-kinematics Coulomb-excitation results for 126,128,130Sn; its Table 1 explicitly labels the Sn B(E2) results preliminary.

## Scope and Reading Depth

The full five-page publisher PDF was read and visually inspected, including Fig. 1 gamma spectra, Table 1 B(E2) values, Fig. 2 isotope/isotone systematics, Fig. 3 single-neutron systematics and Fig. 4 transfer spectra/Table 2. The source is a short proceedings article and does not provide event-level yields, a complete uncertainty budget or covariance information for the 130Sn B(E2).

## Summary

Radford et al. report B(E2;0+→2+) measurements for the first 2+ states of even-even 126–130Sn by inverse-kinematics Coulomb excitation at HRIBF. Their Table 1 gives 130Sn B(E2)=0.023(5) e2b2, with E(2+)=1221 keV in Fig. 1. The value is explicitly preliminary. The pure 130Sn beam had an 11% metastable 7− component; the paper reports that other elements contributed less than 1%. The authors call the 130Sn strength very small, “around 1.4 single-particle units,” but the proceedings article does not define this unit phrase on the cited pages.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RAD05-1 | The paper reports inverse-kinematics Coulomb-excitation measurements of B(E2;0+→2+) for the first 2+ states in 126,128,130Sn. | experimental-fact | direct | Journal p.383, Abstract | true |
| RAD05-2 | Table 1 gives B(E2;0+→2+)=0.023(5) e2b2 for 130Sn and marks the Sn results preliminary. | derived-observable | direct | Journal p.384, Table 1 | true |
| RAD05-3 | The pure 130Sn spectrum contains a 2+ peak labelled at 1221 keV, consistent with the adopted first-excited level energy. | experimental-fact | direct | Journal p.384, Fig. 1 | true |
| RAD05-4 | The same Table 1 gives 0.10(3) e2b2 for 126Sn and 0.073(6) e2b2 for 128Sn, enabling an even-Sn comparison on one reported measurement scale. | derived-observable | direct | Journal p.384, Table 1 | true |
| RAD05-5 | The 128Sn and 130Sn beams were formed from purified molecular SnS+; intensities were about 3×10^6 and 5×10^5 s−1, and 8.5%/11% of the respective ions were in a metastable 7− state. | experimental-method | direct | Journal p.384, Sec. 2 | true |
| RAD05-6 | Scattered carbon recoils detected by HyBall provided a clean trigger and Rutherford normalization; CLARION clover detectors measured gamma rays, and Winther–DeBoer calculations were used to extract B(E2). | experimental-method | direct | Journal pp.384–385, Sec. 2 | true |
| RAD05-7 | The authors state that the 130Sn B(E2) is very small, around 1.4 single-particle units. | author-interpretation | direct | Journal p.387, Conclusion | true |
| RAD05-8 | Figure 2 combines this work’s 126–130Sn points with separate 132,134Sn values from Varner et al.; those 132,134Sn values are not measurements of the Radford 130Sn beam. | source-lineage | direct | Journal p.385, Fig. 2 caption and discussion | true |
| RAD05-9 | The short proceedings paper does not give event-level 130Sn yields, an uncertainty decomposition or covariance for its preliminary B(E2) value. | evidence-boundary | direct | Journal pp.384–387, complete article | true |

## Competing Interpretations and Limitations

The direct 130Sn result fills a coverage gap left by the retrieved NuDat page, but it is explicitly preliminary and has no published yield table or detailed error decomposition in this five-page proceedings paper. The measured beam contained an 11% 7− isomeric component. Although other chemical elements were reported below 1%, the article does not expose a complete covariance model for beam state composition, gamma efficiency, Doppler/solid-angle corrections or Winther–DeBoer extraction.

The article’s phrase “around 1.4 single-particle units” is retained as author wording. A standard Weisskopf-unit conversion of the tabulated 0.023(5) e2b2 gives a different numerical normalization; Gray’s later thesis lists 5.9(1.3) W.u. for the 130Sn core and cites this Radford article. The relation between the article’s “single-particle units” phrase and that W.u. re-tabulation is not defined here and should not be silently equated.

The 132Sn B(E2) comparison has a separate source boundary: Varner et al. report preliminary 0.11±0.03 e2b2 with incomplete photon-efficiency calibration, while NuDat 3 exposes both 0.11(3) in an adopted-level field without a printed unit and 5.5(15) W.u. in a gamma-table field. Those are distinct evaluation fields; their input lineage has not been resolved in this source page.

## Extracted Pages

- Journal p.383: abstract and experiment scope.
- Journal p.384: Fig. 1, Table 1 and Sn beam composition/intensities.
- Journal p.385: method, Rutherford normalization, Winther–DeBoer extraction and Fig. 2 comparison.
- Journal pp.386–387: transfer program, conclusions and “single-particle units” wording.
- Table 1 and Fig. 1 provide the task-relevant 130Sn B(E2) and level-energy locators.

## Related Knowledge

- [[ame2020-sn132-mass-curvature]]
- [[iaea-livechart-132sn-134te-levels]]
- [[varner-2005-coulomb-excitation-132-134sn]]
- [[gray-2021-thesis-electromagnetic-moments-z50]]
- [[a130-shell-gap-orbital-observable]]
