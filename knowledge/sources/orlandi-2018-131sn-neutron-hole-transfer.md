---
type: source
title: "Orlandi et al. 2018 - Neutron-hole states in 131Sn and spin-orbit splitting"
aliases: [Orlandi 2018 131Sn neutron removal, N81 neutron-removal levels]
created: 2026-09-29
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: journal-article-transfer-experiment
reading_depth: deep-read
citation_key: Orlandi2018PLB
title_original: "Neutron-hole states in 131Sn and spin-orbit splitting in neutron-rich nuclei"
authors: [R. Orlandi, et al.]
journal: Physics Letters B
year: 2018
volume: 785
pages: 615-620
doi: 10.1016/j.physletb.2018.08.005
language: en
canonical_source: doi:10.1016/j.physletb.2018.08.005
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/orlandi-2018-131sn-surrey-delivery.pdf"
raw_sha256: 0d743eefaa6f6d62d60aa1b7a5ac4d9e87b3327ababd45a3fc04b3232cd3f684
related_raw_files: ["raw/papers/gpt/day2-shell-gap-20260928/doaj-orlandi-2018-131sn.json", "raw/papers/gpt/day2-shell-gap-20260928/openaire-orlandi-2018-131sn.json"]
repository_url: "https://openresearch.surrey.ac.uk/view/delivery/44SUR_INST/12140132340002346/13140326740002346"
nuclei: [131sn, 132sn, 133sn, 207pb, 208pb]
reactions: ["132Sn(d,t)131Sn", "132Sn(d,p)133Sn", "208Pb(d,t)207Pb"]
experiments: [hribf-132sn-neutron-removal]
models: [dwba, woods-saxon, one-body-spin-orbit]
observables: [differential-cross-section, spectroscopic-factor, single-particle-energy-splitting, rms-radius]
methods: [inverse-kinematics-transfer-reaction, distorted-wave-born-approximation]
tags: [sn131, sn132, sn133, n82, neutron-hole, spin-orbit, transfer-reaction]
---

# Neutron-hole states in 131Sn and spin-orbit splitting

## Bibliographic Record

R. Orlandi et al., Physics Letters B 785, 615–620 (2018), DOI 10.1016/j.physletb.2018.08.005. OpenAIRE resolved the DOI to a University of Surrey repository delivery URL. The saved PDF has a repository cover labelled “Document Version: Text”, identifies the published-version DOI, and states the article is open access under CC BY. It is a Surrey-hosted article copy; the ScienceDirect endpoint was not used to retrieve the file. The PDF is seven pages including the repository cover and six journal pages (615–620).

## Scope and Reading Depth

Deep-read of all six article pages, including the full argument from motivation and reaction design through measured spectrum, DWBA analysis, spin-orbit comparison and conclusion. Figures 1–5 and Eqs. (1)–(3) were inspected visually. The paper has no data tables; the reported spectroscopic factors and angular distributions are in Fig. 3 and its discussion, while the level spectrum is in Fig. 2. The repository PDF, DOAJ JSON and OpenAIRE record are hash-verified in the run source manifest.

## Summary

The paper reports the first heavy-region inverse-kinematics neutron-removal study 132Sn(d,t)131Sn at HRIBF/ORNL. The 0–65-keV 3/2+ / 11/2− doublet is unresolved at the approximately 270-keV summed energy resolution. DWBA fits give S(s1/2)=2.4(2) for the 332-keV state and S(d5/2)=6.4(1.8) for the 1654-keV state. For the unresolved doublet, a pure d3/2 fit gives S=5.0(5); assuming a full h11/2 strength of 12 changes the fitted d3/2 value to 4.3(5), close to its maximum 2j+1=4. Other optical potentials shift extracted factors by roughly 10–20% without changing the occupancy picture.

The article combines these hole-state results with 133Sn particle-state energies from earlier 132Sn(d,p) measurements. It reports that normalized spin-orbit splitting for weakly bound 3p states is about 50% lower than for well-bound 2d states. Woods–Saxon calculations with one common spin-orbit strength reproduce the observed trend; the authors explain it through extended weakly bound radial wavefunctions and reduced surface amplitude, not through a weaker spin-orbit potential.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ORL18-1 | The neutron-removal experiment used inverse-kinematics 132Sn(d,t)131Sn at HRIBF/ORNL with a 580-MeV (about 4.4-MeV/u) 132Sn beam. | experimental-fact | direct | Journal p.617, Sec. 2, reaction setup | true |
| ORL18-2 | Triton differential cross sections were normalized from elastic deuteron scattering; deviations from Rutherford cross sections were below 5%, and DWBA angular distributions were fitted with TWOFNR. | experimental-method | direct | Journal p.617, Sec. 2, cross-section normalization and DWBA paragraph | true |
| ORL18-3 | The summed 131Sn spectrum has peaks at 0–65, 332 and about 1654 keV; the 0–65-keV doublet is unresolved at about 270-keV summed FWHM. | experimental-fact | direct | Journal p.617, Fig. 2 and spectrum discussion | true |
| ORL18-4 | For the unresolved 0–65-keV doublet, a pure d3/2 DWBA fit gives S(d3/2)=5.0(5); if S(h11/2)=12 is assumed, the summed fit gives S(d3/2)=4.3(5). | derived-observable | contextual | Journal p.618, Fig. 3(b) and fit discussion | true |
| ORL18-5 | The 332-keV 1/2+ state gives S(s1/2)=2.4(2); the article contrasts it with a prior sub-Coulomb value 4(3). | derived-observable | contextual | Journal p.618, Fig. 3(c) and fit discussion | true |
| ORL18-6 | The 1654-keV 5/2+ state gives S(d5/2)=6.4(1.8), consistent within uncertainty with the maximum 2j+1=6. | derived-observable | contextual | Journal p.618, Fig. 3(d) and fit discussion | true |
| ORL18-7 | The proposed 7/2+ single-hole state near 2343 keV was not observed in this experiment. | experimental-fact | direct | Journal p.618, paragraph following the Fig. 3 fits | true |
| ORL18-8 | Alternative deuteron/triton optical model potentials shift extracted spectroscopic factors by about 10–20% but leave the same qualitative occupancy picture. | model-boundary | direct | Journal p.618, opening paragraph | true |
| ORL18-9 | The 207Pb(d,t) control fit for the 207Pb p1/2 ground state gives S=1.9(1), with only statistical errors shown, consistent with full occupancy. | derived-observable | contextual | Journal p.618, Fig. 3(a) and comparison discussion | true |
| ORL18-10 | The cited 132Sn 2d5/2 and 2d3/2 neutron-hole binding energies are −9.007(4) and −7.353(4) MeV, respectively, giving a central spin-orbit splitting of 1.654 MeV. | derived-observable | contextual | Journal p.619, Fig. 4(a) discussion | true |
| ORL18-11 | The normalized Δso/(l+1/2) for weakly bound 3p orbits is reported to be about 50% lower than for well-bound 2d orbits; the 2f reduction is smaller. | reported-result | contextual | Journal p.620, conclusion; Fig. 4(a) | true |
| ORL18-12 | Because unobserved levels could alter the Sn spin-orbit values, the authors adopt an average uncertainty of ±150 keV for the comparison. | uncertainty-boundary | direct | Journal p.618, Fig. 4 discussion | true |
| ORL18-13 | A Woods–Saxon calculation with r0=1.27 fm and a=0.67 fm reproduces the splittings using one spin-orbit strength per nucleus, with C=−0.3344 for 132Sn and C=−0.3168 for 208Pb. | model-result | direct | Journal p.619, Fig. 4 and Woods–Saxon parameter discussion | true |
| ORL18-14 | The calculated rms radii are 7.48/8.29 fm for 3p3/2/3p1/2, 5.32/5.34 fm for 2d5/2/2d3/2, and 6.21/6.83 fm for 2f7/2/2f5/2; the mean nuclear radius is 6.47 fm. | model-result | direct | Journal p.619, Fig. 5 and radial-wavefunction discussion | true |
| ORL18-15 | The authors attribute reduced weakly bound 3p splitting to radial extension and a smaller surface-wavefunction amplitude, without invoking a weaker spin-orbit strength. | author-interpretation | direct | Journal p.619, Fig. 5 discussion and p.620 conclusion | true |
| ORL18-16 | The authors interpret the large extracted low-lying hole strengths as corroboration of the robust N=82 closure in 132Sn. | author-interpretation | direct | Journal p.618, Fig. 3 discussion and p.620 conclusion | true |
| ORL18-17 | The retrieved Surrey PDF has a repository cover labelled “Document Version: Text” and gives the published-version DOI; the copy is CC BY and contains six journal pages after its cover. | evidence-boundary | direct | Repository PDF p.1 cover and journal pp.615–620 | true |
| ORL18-18 | The 133Sn particle-side energies used in the spin-orbit comparison are cited to prior 132Sn(d,p) work, including Jones et al.; they are not a second measurement in this 131Sn neutron-removal experiment. | source-lineage | direct | Journal pp.616, 619–620; Refs. [17]–[19] | true |

## Source Lineage and Independence

The 132Sn(d,t) neutron-removal cross sections are a distinct reaction dataset from the 132Sn(d,p) particle-addition measurements of Jones et al. and earlier work. The article reuses those published 133Sn energies for its cross-shell spin-orbit comparison; it does not remeasure them. Both reactions concern 132Sn at HRIBF, so shared facility or beam-systematic overlap is possible even though the reaction datasets differ. The 207Pb control is an external comparison dataset, not a repeat of the Sn measurement.

## Competing Interpretations and Limitations

The unresolved 0–65-keV doublet is the main state-separation limitation. A pure d3/2 fit yields 5.0(5), above the simple occupancy maximum 4; the 4.3(5) value depends on assuming a full h11/2 occupancy of 12. The extraction changes 10–20% under other optical potentials. The 1654-keV d5/2 strength has a large 1.8 uncertainty, and a proposed 7/2+ state near 2343 keV was not observed. The authors also assign ±150-keV average uncertainty to spin-orbit splittings because unobserved states could shift the comparison.

The measured transfer strengths support substantial single-hole character below N=82; they do not by themselves measure the total particle-hole shell gap. The reported 3p/2d splitting trend combines the present 131Sn hole-side data with earlier 133Sn particle-side levels. The Woods–Saxon fit is a model result and supports the radial-extension explanation, but the absolute single-particle energies and potential assumptions remain model-sensitive.

## Extracted Pages

- Journal pp.615–616: motivation, prior competing spin-orbit interpretations and orbital map, Fig. 1.
- Journal p.617: reaction beam/target/detector method, Fig. 2 spectrum and Fig. 3 differential cross sections.
- Journal pp.618–619: Fig. 3 spectroscopic factors, missing-state/systematic boundaries, Eqs. (1)–(3), Fig. 4 spin-orbit comparison and Fig. 5 radial amplitudes/radii.
- Journal p.620: radial-extension interpretation, conclusion and future proton-transfer measurements.
- No tabulated dataset appears in the six-page article; the numerical strengths are in the text and Fig. 3.

## Related Knowledge

- [[ensdf-131sn-neutron-hole-levels]]
- [[ensdf-133sn-transfer-levels]]
- [[jones-2010-133sn-single-particle-transfer]]
- [[ame2020-sn132-mass-curvature]]
- [[a130-shell-gap-orbital-observable]]
