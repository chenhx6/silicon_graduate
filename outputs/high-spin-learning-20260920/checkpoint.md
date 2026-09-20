---
type: research-checkpoint
run_id: high-spin-20260920
updated: 2026-09-20
status: complete
---

# 高自旋文献全量学习 checkpoint

## Current state

- User start instruction: `请硅基研究生开始学习`
- Plan: `docs/plans/2026-09-20-high-spin-127-ingest-and-identity-audit.md`
- Input snapshot: `docs/plans/2026-09-20-high-spin-127-input-snapshot.json`
- Original entries: 127
- User-confirmed contamination excluded: 9
- Valid external files: 118
- Unique SHA-256: 110
- Exact duplicate entries: 8
- Raw batch: `raw/papers/gpt/high-spin-20260920/`

## Completed in this checkpoint

1. Re-read the final plan and input snapshot.
2. Rechecked all 127 original paths against `/workspace/zotero-reference/高自旋/`.
3. Confirmed the nine user-deleted contamination paths are absent.
4. Copied one canonical PDF for each of the 110 remaining unique hashes into the isolated raw batch; copy hashes were verified.
5. Mapped the eight duplicate entries to their canonical copied file paths.
6. Created `ledger.json` with one row for every original item, preserving excluded entries, duplicate mappings, raw paths, hashes, bytes and initial reading/self-audit states.
7. Completed full reading of HS-001 (`Gade 2015`) and created `knowledge/sources/gade-2015-gamma-rays-come-in-twos.md`; the source is explicitly marked as News & Views and does not replace the Walz direct experiment.
8. Added the first append-only state event to `ledger-events.jsonl` and linked the source from `knowledge/index.md`.
9. Completed full visual reading of scanned HS-002 (`Zheng et al. 2002`), created its source page, and updated `knowledge/methods/angular-distribution.md` with the array-specific `f_ADO` and `R_ADO` boundaries.
10. Completed full reading of HS-003 (`Jahangir et al. 2026` arXiv v1), created its TPSM source page, and updated `knowledge/models/triaxial-projected-shell-model.md` with the `K0−2` γ2 boundary.
11. Completed full reading of HS-004 (`Zheng et al. 2013` PRC), created its `91Ru` source page, and updated `knowledge/methods/linear-polarization-asymmetry.md` and `knowledge/methods/compton-polarimetry.md` with the EXOGAM `A/Q/P` calibration and ground-state-assumption boundary.
12. Completed full reading of HS-005 (`Meyer et al. 1978` PRC), created its `61Ni/67Zn` decay-spectroscopy source page, and recorded its low-intensity-line, chemical-separation and MSDI/ASDI/cluster-model boundaries.
13. Completed canonical full reading of HS-006 (`Jensen et al. 2001` NPA 695), created the `165Tm` source page, linked its DSAM and alignment boundaries, and audited HS-007 as an exact same-hash duplicate without rereading or creating a second source.
14. Completed full reading of HS-008 (`Simpson et al. 1983` NIM), created its sectored-GeLi polarimeter source page, and linked the historical `P/A/Q/F` detector-response baseline to the Compton/polarization methods.
15. Completed full reading of HS-009 (`Garcia-Raffi et al. 1995` NIM A), created its non-orthogonal polarimeter source page, and updated the polarization project with the `Q1/Q2/Q3` response and CLUSTER merit boundary.
16. Completed full OCR-assisted reading of HS-010 (`Hara & Sun 1995` PSM review), created its historical review source page, and updated the TPSM model page with the projection/configuration-mixing lineage and axial-shape inference boundary.
17. Completed full reading of HS-011 (`Taras 1971` CJP), created its phase-defined polarization/mixing-ratio source page, and linked its convention and multi-solution boundaries to angular-distribution, polarization and mixing-ratio methods.
18. Completed full reading of the Butler 1973 three-GeLi source, later reconciled to its actual ledger ID HS-016; the original HS-012 row is reserved for Petrache 2018.
19. Completed full reading of HS-013 (`Logan et al. 1974` NIM), created its generalized background-inclusive polarimeter-merit source page, and linked its source/efficiency/Q boundary to the Compton method map.
20. Completed full reading of HS-014 (`Taras 1970` NIM), created its particle-gamma angular-correlation source page, and linked Method II, finite-counter and δ-branch boundaries to angular-distribution/mixing-ratio methods.
21. Completed full reading of HS-015 (`Bargholtz & Tegnér 1987` NIM A), created its high-spin γγ directional-correlation source page, and linked its asymptotic coefficient reduction/triple-correlation boundary to the angular-correlation method.
22. Audited the actual HS-012 Petrache 2018 electronic reprint against the existing canonical source page; no material claim change was found, and D5 versus D1-D4 confidence gradients were preserved.
23. Read HS-017's 74Br supplementary material and attached it to the existing Guo 2024 parent source; the transition table and upper-limit rows are now locally auditable without counting a second experiment.
24. Completed full reading of HS-018 (`Stephens 1975` RMP), created its Coriolis/rotation-alignment review source page, and linked its mechanism-attribution boundary to alignment/backbending concepts.
25. Completed full reading of HS-019 (`Ionescu-Bujor et al. 1998` NPA), created its `129,131Ce` TDPAD/static-moment source page, and linked its PTR shape anchor into the `131Ce` collective-mode project.
26. Completed full reading of HS-020 (`Li & Wang 2024` NST), created its `144Ba` PC-PK1 3D-lattice cranking-CDFT source page, and linked the model result to octupole deformation/softness, CDFT and the high-spin evidence map; pairing, parity-projection and public-data readiness boundaries remain explicit.
27. Completed full reading of HS-021 (`Garcia-Raffi et al. 1997` NIM A), created its GEANT3/Stokes Monte Carlo source page, and linked the geometry, threshold, multiple-scatter and `M=εQ²` boundaries to Compton-polarimetry methods.
28. Audited HS-022's 21-page FZR-156 preprint against the existing canonical Frauendorf–Meng NPA 617 source: the TAC/PRM, planar/aplanar, chirality, transition and `134Pr` sections were reread; no material claim change was found, and the preprint is recorded as an alternate version rather than an independent source.
29. Completed full reading of HS-023 (`Schirmer et al. 1984` PRL), created a direct `40Ca/90Zr` two-photon-decay source and concept page, and linked Crystal-Ball PAF rejection, γγ angular correlation and polarization branch selection to the coincidence/polarimetry methods; HS-024/HS-025 remain user-confirmed exclusions.
30. Completed full reading of HS-026 (`Frauendorf 2018` Phys. Scr. invited review, 80 pages), created its source page, and linked the rotating-mean-field/TAC framework, harmonic and transverse wobbling, chirality, magnetic rotation, band termination and tidal-wave boundaries to the Wiki; cited examples remain review-level and non-independent.
31. Completed full reading of HS-027 (`Königshofen et al. 2001` PRC), created the `130Ba` three-angle mixing-ratio source page, and linked Rose–Brink convention, M1 corrections, B(E2) implications and the unresolved-δ boundary to angular-correlation/mixing-ratio methods.
32. Completed full reading of HS-028 (`Gaffney et al. 2013` Nature), created the `220Rn/224Ra` radioactive-beam Coulomb-excitation source and method page, and linked direct E3/Q3 evidence, GOSIA fit boundaries and static-pear versus soft-octupole distinctions to the octupole knowledge layer.
33. Audited HS-029's five-page PRL electronic reprint against the existing canonical Ayangeakaa `133Ce` source: both MχD pairs, DCO/angular assignments, `4.1×10^9` event total, RMF/TPRM parameters and lifetime gap were reread; no material claim change was found, and the reprint is recorded as an alternate version rather than an independent experiment.
34. Completed full reading of HS-030 (`Freire-Fernández et al. 2024` PRL), created the isolated `72Ge32+` S+IMS/Schottky two-photon source and storage-ring method page, and linked the `23.9(6) ms` total rate, polarizability decomposition and SI/raw-data boundaries to the two-photon concept.
35. Completed full reading of HS-031 (`Greiner 1966` Nuclear Physics), created its historical proton/neutron deformation–gR tensor source, and linked the model's M1/E2 mixing and scalar-gR limitations to the observable/magnetic-rotation map.
36. Completed canonical full reading of HS-032 (`Twin et al. 1970` NPA), created its `40K` joint angular-distribution/γγ-correlation/Compton-polarization source page, and audited HS-033/HS-034 as exact same-hash duplicate rows with no independent source count.
37. Completed full reading of HS-035 (`Butler & Nazarewicz 1996` RMP, 73 pages), created its reflection-asymmetry evidence-map source page, and linked the static/soft/vibrational, E1/E3, parity-restoration and high-spin boundaries to the octupole knowledge layer.
38. Completed full reading of HS-036 (`Walz et al. 2015` Nature), created the direct `137Ba` competitive double-γ source, linked it to Gade and the two-photon concept, and preserved the separate HS-116 supplementary-material audit route.
39. Completed full reading of HS-037 (`Liang 2016` arXiv review), created its pseudospin/Dirac/SUSY source page, and linked pseudospin symmetry, alignment and covariant shell-evolution boundaries without conflating pseudospin with signature partners.
40. Recorded HS-038 as the user-confirmed contamination exclusion, then audited HS-039's fifteen-page Ding 2021 PRC PDF against the existing canonical source: reactions/event totals, `R_ac`, Tables I–II, CSM/QTR/PES and conclusion were reread with no material claim change.
41. Completed full reading of HS-040 (`Wadsworth et al. 1977` J. Phys. G), created its `61Ni` level/mixing/DSAM source page, and linked the historical three-GeLi/polarization and lifetime lineage to methods and the Meyer `61Ni` source.
42. Completed full reading of HS-041 (`Falkoff 1948` Phys. Rev. letter), created its successive-γ polarization-correlation source, and linked the historical `A` sign/phase formalism to angular-correlation and polarization methods; the unrelated preceding scan-page text remains excluded.
43. Completed full chapter-by-chapter reading of HS-042 (`Alder et al. 1956` RMP, 111 pages), created its Coulomb-excitation theory/method source, and linked classical/quantum/higher-order and normalization boundaries to the modern GOSIA method page; HS-043 remains excluded.
44. Recorded HS-043 as the user-confirmed contamination exclusion, then completed full reading of HS-044 (`Bass et al. 1972` NIM), created its symmetric two-crystal Compton-polarimeter source and linked threshold/angle/response boundaries to the Compton method map.
45. Completed full reading of HS-045 (`Klein & Nishina 1929` Z. Phys.), created its historical free-electron Compton-response source, and explicitly separated intensity cross-section theory from later polarization/detector sensitivity.
46. Completed full reading of HS-046 (`von der Werth et al. 1995` NIM A), created POLALI/MINIPOLA source page, and linked kinematic-gate, geometry, threshold, `Q/ε/F` calibration boundaries to the Compton method map.
47. Completed full reading of HS-047's in-scope Haxel–Jensen–Suess 1949 letter, created the historical magic-number source, and excluded unrelated neighboring letters on the scan page.
48. Completed full reading of HS-048 (`Reed et al. 2016` Phys. Lett. B), created the `187,189,191Re` triaxiality source page and linked signature/M1-E2/γ-band evidence with PTR/PES/TRS softness boundaries; HS-049 remains excluded.
49. Recorded HS-049 as the user-confirmed contamination exclusion, then completed full reading of HS-050 (`Hamilton & Davies 1968` NPA), created its Ge/NaI cascade-separation and summing-polarimeter source page, and linked the convention/correction boundaries to angular-correlation methods.
50. Completed full reading of HS-051 (`Samanta et al. 2019` PRC), created its modern `61Ni` clover/RADO/RDCO/polarization and `fpg` shell-model source page, and linked it to the Wadsworth/Meyer lineage reconciliation.
51. Completed full reading of HS-052 (`Nolan & Sharpey-Schafer 1979` RPP, 88 pages), created its lifetime-method review source, and linked DSAM/RDM/stopping/feeding boundaries to the lifetime evidence map.
52. Audited HS-053's six-page published Petrache PRC PDF against the existing canonical/electronic-reprint source: the five-pair `136Nd` scheme, D5 evidence and TAC/CDFT caveats agree; no material claim change. HS-054 remains excluded.
53. Completed full reading of HS-055 (`Walker & Dracoulis 2001` Hyperfine Interactions), created its exotic-isomer/K-trap review source, and linked axial symmetry, forbiddenness and K-mixing limits to high-spin lifetime interpretation.
54. Completed full reading of HS-056 (`Frauendorf 2015` IJMPE, 38 pages), created its quadrupole-mode review source, and linked Bohr/ATDMF/GCM/IBM, γ-softness, tidal-wave/TPSM and adiabaticity boundaries to the collective-mode map.
55. Completed full reading of HS-057 (`Gore et al. 2005` EPJ A), created the Mo/Ru/Pd γ-band staggering source and linked fast odd-even reversals to γ-soft/rigid diagnostic limits.
56. Completed full reading of HS-058 (`Heyde & Wood 2011` RMP, 55 pages), created its shape-coexistence review source and linked shell/mean-field/IBM, E0/E2/radius and symmetry-restoration companion-observable boundaries.
57. Completed full reading of HS-059 (`Schmid et al. 1998` NIM A), created the segmented-Gammasphere confined/shared polarization source, and linked Monte Carlo `Q(E)` and high-background `197Pb` parity limits to Compton methods.
58. Completed full reading of HS-060 (`Krane, Steffen & Wheeler 1973` NDT, 56 pages), created its generalized DCO/orientation source and linked statistical-tensor, geometry and phase-convention boundaries to DCO/angle methods.
59. Completed full reading of HS-061's three-page Nuclear Data Sheets spin/parity proposition sheet, created a strong/weak evidence checklist source for batch-wide self-audit, and preserved its non-universal threshold caveat.
60. Completed full reading of HS-062 (`Lister & Butterworth 2013` Nature News & Views), created its secondary pear-shape/EDM context source, and linked it to the direct Gaffney source without counting an independent experiment.
61. Completed full reading of HS-063 (`Möller et al. 2006` PRL), created its global FRLDM axial-asymmetry source, and linked global PES/γ-band/mass-residual results with zero-point and direct-observable boundaries.
62. Completed full reading of HS-064 (`孟杰 2009` 中文《原子核是否存在手性》), created its secondary chiral-fingerprint review source, and linked its TAC/TPRM/RMF and lifetime-gap boundaries without counting a new experiment.
63. Completed full reading of HS-065 (`Suzuki & Kimura 2021` arXiv), created its AMD/GCM N=28 shell-evolution/triaxiality source, and preserved projected-model/interband-E2 boundaries.
64. Completed full reading of HS-066's one-page Macchiavelli 2018 PRC erratum, created a correction-scope source page and recorded that it does not materially affect the high-spin batch.
65. Completed full reading of HS-067 (`Droste et al. 1999` NIM A), created its PPCO two-polarimeter source and linked PP1/PP2/AA1/AA2, alignment and DCO-combination boundaries to Compton methods.
66. Completed full reading of HS-068 (`Gade et al. 2025` Nature Physics), created the FRIB/GRETINA `62Cr` shape-coexistence source, and linked excited `0+`, knockout momentum, LNPS/DNO-SM and model-shape boundaries.
67. Completed full reading of HS-069 (`McCutchan et al. 2007` PRC), created its `S(J)/S(4)` γ-band staggering source and linked vibrator/γ-soft/axial/triaxial model limits.
68. Audited HS-070's arXiv Nomura 2021 preprint against the existing canonical PRC source, then audited HS-071 as an exact duplicate row; equations/Figs.1–4/model limitations agree and no independent source is added.
69. Completed full reading of HS-072 (`Starosta et al. 1999` NIM A), created the EUROGAM-II PDCO source page, and linked its CLOVER `Q(E)` calibration, integrated-mode correction and joint `P`–`R_DCO` branch boundary; the 490-keV case remains E2 versus ΔI=0 M1/E2 ambiguous.
70. Completed full reading of HS-073 (`Rees et al. 2011` PRC), created the `156Er` non-yrast source page, and linked its γ-band `S(4)≈−1`/γ-soft comparator, second-`0+` systematics, Gammasphere angular ratios and competing `(νi13/2)2` versus `(νh9/2,f7/2)2` alignment interpretation.
71. Recorded HS-074 as the user-confirmed contamination exclusion; its missing source remains excluded and no scientific processing was performed.
72. Completed full 69-page reading of HS-075 (`Hübel 2005` PPNP), created the magnetic-rotation review source, and linked the multi-observable shears/TAC chain, antimagnetic-rotation distinction, review-lineage boundary and magnetic-versus-core-rotation L3 comparator.
73. Completed full reading of HS-076 (`Hamilton 1969` NPA), created the `194,196Pt` mixing-ratio source, and linked high-resolution cascade separation, Biedenharn convention, `δ=−(30^{+39}_{−19})`/`+4.03(12)` results, the theory conflict and unresolved 759-keV branch warning.
74. Completed full reading of HS-077 (`Jones et al. 1995` NIM A), created the four-crystal CLOVER calibration source, and linked the `P/A/Q` separation, 197–1368 keV `Q(E)`, 60-keV threshold and geometry-specific response boundary.
75. Completed full 79-page reading of HS-078 (`Aprahamian, Langanke & Wiescher 2005` PPNP), created the nuclear-astrophysics structure source/concept, and linked reaction-network, shell/cluster, level-density, deformation, weak-rate and model-regime boundaries; it adds no independent A≈130 high-spin evidence.
76. Completed full 53-page reading of HS-079 (`Pfützner et al. 2012` RMP), created the drip-line radioactivity source/concept, and linked separation-energy, barrier, shell/pairing, proton/alpha, true-2p, β-delayed and neutron-continuum boundaries.
77. Completed full 42-page reading of HS-080 (`Rose & Brink 1967` RMP), created the phase-defined angular-distribution source, and linked `B_K`/`R_K`, γγ correlation, δ sign, operator phase, state order and parity/alignment boundaries.
78. Completed full 56-page reading of HS-081 (`Der Mateosian & Sunyar 1974` ADNDT), created the high-spin `A2/A4` reference-table source, and linked Gaussian `σ/J` attenuation, joint alignment–δ identifiability and the angular-distribution/γγ sign warning.
79. Completed full 89-page reading of HS-082 (`Åberg, Flocard & Nazarewicz 1990` Annual Review), created the mean-field shape source, and linked HF/HFB–Nilsson–Strutinsky, rotation/high-spin, triaxiality, octupole, superdeformation, shape coexistence and intrinsic-to-laboratory projection boundaries.
80. Completed full reading of HS-083 (`Mukhopadhyay et al. 2007` PRL), created the `135Nd` chiral-vibration/static-chirality source, and linked DSAM `B(M1)/B(E2)` partner similarity, TAC+RPA phonon splitting, critical-spin and nucleus-specific transfer boundaries.
81. Completed full reading of HS-084 (`Ma et al. 1990` PRC), created the `131Ba` competing-alignment source, and linked ten-band coincidence data, signature splitting, DCO/δ, proton/neutron crossing frequencies and opposite CSM/TRS shape-driving interpretations.
82. Completed full reading of HS-085 (`Eldridge et al. 2018` EPJA), created the Mo/Ru/Pd IPAC mixing-ratio source, and audited HS-086 as an exact duplicate; 37 δ branches remain in `(A2,A4)` uncertainty space with E2 dominance and the `110Ru` sign-trend boundary.
83. Completed full reading of HS-087 (`Miller et al. 2007` NIM A), created the side-irradiated SeGA polarization source, and linked `Q≈0.14(2)`, `FM≈5.9×10^-6`, geometric asymmetry and finite-angle/fast-beam response boundaries.
84. Completed full reading of HS-088 (`Krane & Steffen 1970` PRC), created the `110Cd` 25-correlation δ source, and linked explicit emission-matrix-element convention mapping, Compton-background control and vibrational/extra-pair model boundaries.
85. Completed full reading of HS-089 (`Aoki et al. 1975` NIM), created the simultaneous-angle Ge(Li) summing-polarimeter source, and linked the `φ=0/30/60/90°` annihilation benchmark, majority-anticoincidence background reduction and ring-reflector efficiency/threshold tradeoff.
86. Completed full reading of HS-090 (`Rahaman et al. 2024` PRC), created the `40K` INGA source, and linked RDCO/RADO/IPDCO/δ multimethod assignment, `σ/J=0.3` alignment and run-specific calibration boundaries with the sd–pf shell-model interpretation.
87. Completed full reading of HS-091 (`Das et al. 2020` PRC), created the `37Ar` INGA source, and linked level-scheme extension to 10.5 MeV, RDCO/RADO/IPDCO/δ, `σ/J=0.3`, Doppler/calibration handling and sd–pf/two-level-mixing boundaries.
88. Completed full 48-page reading of HS-092 (`Fagg & Hanna 1959` RMP), created the historical polarization source, and linked alignment versus polarization, Compton/photoelectric analyzers, direction–polarization/circular correlations and convention/response boundaries.
89. Completed full reading of HS-093 (`Bisoi et al. 2014` PRC), created the `34Cl` DSAM/shell-model source, and linked level-scheme extension, RDCO/IPDCO/δ, `B(E2)≈8–20 W.u.` collectivity, stopping/feeding and sd–pf configuration boundaries.
90. Audited HS-094's 44-page LBNL-41340 Schmid preprint against canonical HS-059/NIM A source; segmented Gammasphere design, `Q(E)`, Monte Carlo and `197Pb` parity application agree, so it is an alternate version with no independent source count.
91. Completed full 39-page reading of HS-095 (`Kramp et al. 1987` NPA), created the `16O` two-photon-decay source, and linked `(6.6±0.5)×10^-4` branching, Crystal-Ball PAF/Compton rejection, `2E1/2M1` interference and inverse matrix-ratio branches.
92. Recorded HS-096 as the user-confirmed contamination exclusion (metal substitutions in carbonic anhydrase); source absent and no scientific processing performed.
93. Completed full reading of HS-097 (`Williams et al. 1975` NPA), created the `61Ni` low-lying-level source, and linked DSAM lifetimes, angular-correlation/polarization/mixing-ratio assignments, shell-model strengths and lineage boundaries to Meyer/Wadsworth/Samanta.
94. Completed full 87-page reading of HS-098 (`Ragnarsson, Nilsson & Sheline 1978` Physics Reports), created the shell-effects/deformation concept/source, and linked magic numbers, shape-dependent shell gaps, Strutinsky, high-spin stability and intrinsic-to-observable boundaries.
95. Completed full reading of HS-099 (`James, Twin & Butler 1974` NIM), created the angular-correlation statistics source, and linked alignment/model covariance, design-matrix rank, χ²/F tests, `arctanδ` confidence contours and non-identifiability conditions.
96. Completed full reading of HS-100 (`Grodner et al. 2018` PRL), created the `128Cs` TDPAD g-factor source, and linked `g=+0.59(1)`, core-rotation admixture, near-planar bandhead geometry and chiral critical-frequency boundary.
97. Completed full reading of HS-101 (`Garg et al. 2015` PRC), created the `135Pr` possible-magnetic-rotation source, and linked RDCO/IPDCO M1/E2 evidence, 3qp→5qp TAC crossing and the explicit missing-lifetime/B(M1)/B(E2) boundary.
98. Recorded HS-102 as the user-confirmed contamination exclusion (maturation of adrenal medulla IV); source absent and no scientific processing performed.
99. Completed full reading of HS-103 (`Liu et al. 1996` PRC), created the A≈130 signature-inversion/spin-crosswalk source, and linked revised `I0` systematics, particle–triaxial-rotor comparison and unresolved Cs reference choices.
100. Completed full reading of HS-104 (`Henderson et al. 2014` PRC), created the `98Mo` two-photon upper-limit source, and linked the `95% CL <1×10^-4` limit, DSSD/Gammasphere normalization, efficiency/energy-sharing and shape-coexistence model boundaries.
101. Completed full 54-page reading of HS-105 (`Davidson 1965` RMP) and audited HS-106–HS-108 as exact duplicate rows; collective rotor/vibration and odd-particle coupling boundaries are retained without extra source counts.
102. Completed full reading of HS-109 (`Schlitt et al. 1994` NIM A), created the fourfold sectored-Ge NRF polarimeter source, and linked `Q≈20% @0.5 MeV`, `≈9.5% @4.4 MeV`, efficiency/FOM and `162Dy` parity-sign boundaries.
103. Completed full 16-page reading of HS-110 (`Der Mateosian & Sunyar 1974` attenuation tables), created the Gaussian `α2/α4` source, and linked `σ/J`, worked `Ji=10→Jf=8` example, high-spin table range and alignment-model boundary.
104. Completed full reading of HS-111's four-page 1970 Nuclear Data Sheets spin/parity proposition sheet, created a version-separated source, and linked strong/weak evidence hierarchy, DCO/polarization heuristics and non-universal threshold boundaries.
105. Completed full reading of HS-112 (`Vaillancourt & Taras 1974` NIM), created the three-multipole angular/polarization formula source, and linked Rose–Brink correction, Eq.32 angular→polarization recipe, `E1/M2/E3` two-δ and alignment boundaries.
106. Completed full reading of HS-113 (`Droste et al. 1996` NIM), created the PDCO formal precursor, and linked unified DCO/PDCO/PPCO statistical tensors, geometry, deorientation and Gaussian-alignment transfer boundaries.
107. Completed full reading of HS-114 (`Ewan et al. 1969` Physics Letters B), created the single-planar-GeLi source, and linked 0.8–4.4 MeV `Q` calibration, `102Ru` application and photoelectric/geometry response boundaries.

108. Completed the attached-material audit for HS-116 (Walz 2015 Supplementary Information). The 14 pages, Eqs.(2–19), Tables 1–4 and Fig.1 were read; efficiency/gate fractions, sequential-Compton geometry, six polarizability paths, QPM state space and the ~10% average-denominator systematic are now attached to the Walz source without adding an independent experiment.
109. Completed full reading of HS-117 (Yamazaki 1967), created the aligned-angular-distribution coefficient source, and linked statistical tensors, Gaussian `σ/J` attenuation, cascade `U_k` propagation and the angular-distribution/γγ-correlation δ-sign warning.
110. Completed full reading of HS-118 (Suffert, Endt & Hoogenboom 1959), created the proton-capture Compton-polarization source, and linked `P/R/p` corrections, eight-line ambiguity resolution and the high-energy pair-production/bremsstrahlung boundary.
111. Completed full reading of HS-119 (Mukhopadhyay et al. 2008), created the `136Nd` DSAM/TAC+RPA source, and linked the factor-of-2–3 `B(E2)` partner difference and distinct-configuration band-mixing interpretation as a direct counterexample to energy-degeneracy-only chirality.
112. Completed full reading of HS-120 (Petrache et al. 2006), created the `134Pr/136Pm` critical-analysis source, and linked 4-qp crossings, alignment difference and `Q0,1/Q0,2=2.0(4)` to the necessary-observable chirality gate.
113. Completed full 76-page reading of HS-121 (Lange, Kumar & Hamilton 1982), created the E0/E2/M1 review/data-compilation source, and linked Krane–Steffen sign conventions, PPQ/IBM comparison, table-quality footnotes and E0/E2 shape-coexistence limits.
114. Completed full reading of HS-122 (Bucher et al. 2016), created the direct `144Ba` E3/Coulomb-excitation source, and linked `B(E3)=48^{+25}_{−34} W.u.`, `Q3`, `β3` and GOSIA/rigid-rotor/higher-multipole boundaries.
115. Completed full reading of HS-123 (Dey et al. 2026), created the `116Cs` multifaceted-decay source, and linked the 7.66-MeV octupole-resonance assignment, delayed two-proton correlation, possible `12C` emission and unavailable-data L4 stop.
116. Completed full in-scope reading of HS-124 (Hamilton 1948), created the successive-quanta direction–polarization formalism source, and explicitly excluded the adjacent Corben article; relative-parity and detector-efficiency boundaries are retained.
117. Completed full 20-page reading of HS-125 (Herzáň et al. 2015), created the `193Bi` spectroscopy source, and linked RDCO/IPDCO calibration, `29/2±` isomers, `B(E2)` hindrance, oblate configuration interpretations and the unconfirmed SD absolute-strength boundary.
118. Audited HS-126 as an alternate APS PDF of the existing Guo 2024 PRL; minor typesetting/reference differences only, no claim or numerical change, no new experiment/source count.
119. Completed full reading of HS-127 (Söderström et al. 2020), created the independent `137mBa` competitive-double-γ source, and linked `8.7σ`, `2.62(30)×10⁻6`, energy-sharing discrimination, E3M1/M2E2 conflict and data/code availability boundary.

## Not yet completed

- Final repository verification: run wiki lint, `git diff --check`, raw-hash/protected-BibTeX checks, link/statistics reconciliation and final report update.
- Batch-wide post-ingest self-audit: verify every valid row's source mapping/locator/independence and summarize L3/L4 units; no valid row remains unread.
- Optional QMD index refresh if the local tool is available; record unavailable tooling rather than treating it as a scientific blocker.

## Resume instruction

Read this checkpoint, `ledger.json` and `ledger-events.jsonl`. All 127 rows now have terminal row states: 118 valid inputs are read/reused/attached/audited, nine are the user-confirmed exclusions. The next action is final verification and batch-wide self-audit, not another PDF.

## Safety state

Safety state update: HS-040 is now included in the processed source/method set; its historical `61Ni` assignment and DSAM boundaries remain separate from the prior Meyer/Williams source lineages.

Source and method/model pages for processed HS-001 through HS-039 were intentionally updated under the user's start authorization; HS-012 reused the existing canonical Petrache page, HS-016 reused the Butler source page created during ID reconciliation, HS-017 attached the supplied Guo supplement to its parent source, HS-022 reused the canonical Frauendorf–Meng source with an alternate-version audit, HS-024/HS-025/HS-038 remain excluded, HS-026 is a review-level theory bridge rather than an independent experiment, HS-027 is a direct low-spin `130Ba` experiment with convention and geometry boundaries, HS-028 is a direct `220Rn/224Ra` E3/Q3 benchmark with GOSIA/static-shape boundaries, HS-029 reused the human-reviewed canonical Ayangeakaa source with an alternate-version self-audit, HS-030 is a direct storage-ring total 2γ-rate measurement with SI and multipole-decomposition boundaries, HS-031 is a historical theory bridge with proton/neutron deformation and g-tensor assumptions, HS-032 is the canonical Twin joint-method source, HS-033/HS-034 are duplicate-row self-audits, HS-035 is a review-level reflection-asymmetry evidence map rather than an independent experiment, HS-036 is a direct `137Ba` competitive 2γ observation with attached SI pending, HS-037 is an arXiv symmetry review with pseudospin/signature separation, and HS-039 reused the human-reviewed Ding source with a published-version self-audit. Existing user untracked files remain untouched. The copied PDFs are ignored by the repository `*.pdf` rule and remain local raw evidence unless the user later specifies a publication-safe handling route.
