---
type: output
title: "高自旋文献全量学习报告"
created: 2026-09-20
updated: 2026-09-21
status: final-verification
review_status: unreviewed
tags: [high-spin, full-text-learning, l3, l4, 2026-09-20]
---

# 高自旋文献全量学习报告

本报告是执行中的持久化报告。最终结论必须等有效来源完成全文学习、知识关联和摄入后自我审核后再写入；当前只记录启动与恢复状态。

## Input and execution baseline

- 127 original ledger entries, including 9 user-confirmed contamination exclusions.
- 118 valid external PDF files and 110 unique SHA-256 values.
- 8 exact duplicate entries are mapped to five canonical files; they will not be reread as independent papers, but every duplicate row will receive an explicit post-ingest audit result.
- Canonical copied PDFs are isolated under `raw/papers/gpt/high-spin-20260920/`.
- Per-item state is in `ledger.json`; recovery state is in `checkpoint.md`.

## Reading policy

All valid independent sources are learned in full-text mode. The record must distinguish identity verification, reading coverage, source mapping, knowledge impact, L3/L4 research and self-audit. Metadata, abstract-only reading, text extraction, PDF copying or an existing `deep-read` label cannot close an item.

## Current status

The batch has entered active ingest. HS-001 through HS-115 are durably recorded in the ledger and source graph; the original intermediate prose above is retained as execution history. The final durable update below supersedes the old “next HS-020” pointer.

### Final durable update (2026-09-21)

All 118 valid rows now have terminal states: 102 new source pages, 8 reused/alternate-version audits, 7 exact-duplicate row audits, and 1 attached Walz supplement audit. The 9 user-confirmed contamination rows remain excluded. HS-116 closes Walz's SI gap; HS-117–HS-125 and HS-127 add the source pages listed in the checkpoint; HS-126 is an alternate Guo PDF with no material change. The ledger records 110 unique hashes separately from 118 valid rows and 127 original entries.

The highest-impact synthesis changes are: (1) Söderström 2020 independently confirms `137mBa` competitive double-γ decay at `8.7σ` and uses energy sharing to favor E3M1 over Walz's Aqq-dominant interpretation; (2) Mukhopadhyay 2008 and Petrache 2006 make partner-resolved electromagnetic strengths, alignment and crossing alternatives mandatory for chirality claims; (3) Bucher 2016 supplies direct `144Ba` E3 strength, keeping E3 matrix elements separate from inferred static `β3`; and (4) Yamazaki/Lange/Hamilton/Suffert preserve the convention, alignment and detector-response chain behind every δ/polarization transfer.

L3 units are recorded per source. L4 is not claimed for this batch: available papers either lack raw event/response/code inputs or provide only author-request/final-data routes. Dey 2026 and Söderström 2020 are explicitly input-limited rather than silently treated as reproducible re-analyses.

### Latest durable update

HS-020 (`Li & Wang 2024`) is fully read as a `144Ba` PC-PK1 3D-lattice cranking-CDFT theory source. The paper reports a `β30≈0.13` ground-state minimum and average `β30≈0.128` to `I≈24ℏ`, but explicitly omits pairing and parity projection; therefore parity splitting and a quantum alternating-parity spectrum are not established. The cited Science Data Bank is recorded as a candidate-L4 route, not yet a reproducible L4 run. The next durable unit is HS-021.

HS-021 (`Garcia-Raffi et al. 1997`) is fully read as a GEANT3/Stokes Compton-polarimeter method source. It validates polarization-aware multiple-scatter transport against five-coaxial, four-coaxial and CLOVER configurations, while showing that `Q` and `M=εQ²` depend on geometry, thresholds, angle windows and background/calibration conditions. The next durable unit is HS-022.

HS-022 is the FZR-156 preprint version of the existing Frauendorf–Meng 1997 NPA theory source. Its 21 pages were reread end-to-end; the TAC/PRM, planar/aplanar, chirality, transition-probability and `134Pr` comparison chain agrees with the canonical journal source. It is therefore an alternate-version audit, not a new independent source or experiment. The next durable unit is HS-023.

HS-023 is fully read as a direct `40Ca/90Zr` rare two-photon-decay PRL. Crystal-Ball timing/multiplicity, PAF kinematic rejection, corrected γγ angular correlations and Compton polarization jointly select the `2E1/2M1` branches and constrain `2E2` contributions. Its branching and matrix-element values remain detector- and intermediate-state-model dependent; HS-024/HS-025 are confirmed exclusions. The next durable unit is HS-026.

HS-026 is fully read as Frauendorf's 80-page 2018 invited review. It connects the Unified Model to rotating mean field, TAC/cranked-shell classification, harmonic and transverse wobbling, chiral aplanar rotation, magnetic/shears rotation, band termination, tidal waves and coherence length. It explicitly limits semiclassical angular-momentum conservation, tunnelling and interband-transition claims; all cited nuclei remain review-level routes to original sources. The next durable unit is HS-027.

HS-027 is fully read as the direct `130Ba` three-angle γγ angular-correlation experiment. Eighteen mixing ratios are extracted under the Rose–Brink convention, dominant M1 components correct earlier B(E2) discrepancies, and one transition remains non-unique. The detector geometry, reference-transition and branch assumptions are retained; the next durable unit is HS-028.

HS-028 is fully read as the direct `220Rn/224Ra` radioactive-beam Coulomb-excitation Nature paper. MINIBALL+GOSIA extracts E1/E2/E3 matrix elements and shows stronger, more coherent octupole collectivity in `224Ra` than `220Rn`; the paper keeps GOSIA-input, model-conversion and static-versus-vibrational boundaries explicit. The next durable unit is HS-029.

HS-029 is the electronic-reprint version of the existing Ayangeakaa `133Ce` PRL source. It was reread end-to-end and confirms the two MχD candidate pairs, DCO/angular assignments, RMF/TPRM inputs, attenuation factor and explicit lack of lifetime measurements. No material claim changed; the reprint is an alternate-version audit, not an independent experiment. The next durable unit is HS-030.

HS-030 is fully read as a direct isolated `72Ge32+` two-photon-decay PRL. S+IMS/Schottky spectroscopy gives `T1/2=23.9(6) ms` and `E_x=692.8(19) keV`, about ten times faster than prior scaling; the result measures total `M2γγ`, while E1/M1/E2 decomposition remains model constrained pending the attached SI/raw-data audit. The next durable unit is HS-031.

HS-031 is fully read as Greiner's 1966 historical collective model. It derives a proton/neutron deformation-difference magnetic tensor that links lowered `g_R` and M1/E2 mixing, reproducing broad historical trends but retaining simplified pairing, vibrational and data-uncertainty boundaries. The next durable unit is HS-032.

HS-032 is fully read as the canonical `40K` joint angular-distribution/γγ-correlation/Compton-polarization experiment. It assigns spins/parities and mixing ratios while explicitly showing that polarization alone can be non-unique and that Biedenharn/MANDY versus Rose–Brink signs must be mapped. HS-033 and HS-034 are exact duplicate rows, each individually self-audited without rereading or adding a source count. The next durable unit is HS-035.

HS-035 is fully read as the 73-page Butler–Nazarewicz RMP. It provides the historical reflection-asymmetry framework—static octupole versus softness/vibration, E1/E3 and parity bands, beyond-mean-field restoration, and high-spin/fission extensions—while remaining a review-level source map rather than new independent evidence. The next durable unit is HS-036.

HS-036 is fully read as the direct Walz `137Ba` competitive double-γ Nature Letter. Five LaBr3 detectors, timing/random subtraction, lead shielding, energy-sharing and 72°/144° correlations establish a `(2.05±0.37)×10⁻6` competitive branch and fit `Aqq/Aod` virtual paths; the attached SI/response audit remains pending at HS-116. The next durable unit is HS-037.

HS-037 is fully read as Liang's 21-page arXiv review of nuclear pseudospin symmetry and its SUSY representation. It establishes the Dirac `dΣ/dr≈0` condition, deformed/RMF/SRG symmetry-breaking framework and alignment applications, while explicitly warning that near-degenerate high-spin bands are not pseudospin partners without configuration/wave-function evidence. HS-038 is a confirmed contamination exclusion; the next durable unit is HS-039.

HS-039 is the published-PDF alternate version of the existing Ding `131Ba/133Ce` signature-splitting source. It was reread end-to-end and confirms the reactions/event totals, `R_ac` calibration, `νg7/2[404]7/2+` assignments, CSM/QTR/PES mechanism and conclusion that triaxiality and low-j `s1/2` mixing jointly control splitting. No material claim changed; the row is an alternate-version audit. The next durable unit is HS-040.

HS-040 is fully read as the historical `61Ni` level-scheme experiment. γγ coincidences, angular distributions, three-GeLi polarization, Rose–Brink mixing ratios and DSAM lifetimes establish a low-energy baseline while preserving assignment disagreements and stopping/feeding boundaries. The next durable unit is HS-041.

HS-041 is fully read as Falkoff's one-page 1948 polarization-correlation letter. Its successive-γ `A` coefficient/sign and `60Co/46Sc` example provide a historical formalism precursor; the scan's unrelated neighboring text and detector-response details are excluded. The next durable unit is HS-042.

HS-042 is fully read as the 111-page Alder–Bohr–Mottelson–Winther Coulomb-excitation RMP. It establishes the classical/quantum/WKB trajectory framework, higher-order and detector/normalization limits, and rotational/vibrational matrix-element applications underlying modern GOSIA analyses. HS-043 is a confirmed contamination exclusion; the next durable unit is HS-044.

HS-044 is fully read as the Bass symmetric two-crystal Compton-polarimeter method paper. Coincidence/anticoincidence asymmetry, threshold-dependent angle acceptance and NaI/Ge(Li) response tables provide a historical detector benchmark; HS-043 remains excluded. The next durable unit is HS-045.

HS-045 is fully read as the Klein–Nishina 1929 Dirac scattering paper. It supplies the free-electron relativistic Compton response underlying later polarimetry, while explicitly excluding polarization and detector-response calculations. The next durable unit is HS-046.

HS-046 is fully read as the POLALI/MINIPOLA Compton-polarimeter construction paper. It quantifies the modular five-detector versus segmented-planar trade-off, kinematic gating and detector-specific `Q/ε/F` calibration. The next durable unit is HS-047.

HS-047 is fully read within scope as the Haxel–Jensen–Suess 1949 magic-number letter. The oscillator plus strong spin–orbit argument for `2,8,20,28,50,82,126` is recorded as historical shell-model background; unrelated neighboring scan-page letters are excluded and no modern shell-gap claim is inferred. The next durable unit is HS-048.

HS-048 is fully read as the direct `187,189,191Re` experiment/model paper. Increasing signature splitting, falling γ-bandhead energies and M1/E2 mixing jointly support increasing triaxiality, while PTR/PES/TRS comparisons retain γ-softness and rotation-stabilization alternatives; HS-049 is a confirmed contamination exclusion. The next durable unit is HS-050.

HS-050 is fully read as the `192Pt` Ge/NaI angular-correlation and summing-polarimeter experiment. Composite cascade equations, random/background subtraction and polarization resolve E2/M1 mixing ratios while retaining cascade-weight and phase-convention limits. The next durable unit is HS-051.

HS-051 is fully read as the modern `61Ni` TIFR clover/shell-model study. It adds 17 transitions, re-places six lines, extends the scheme to ~7 MeV, and uses RADO/RDCO/polarization plus `fpg+g9/2` calculations; its source lineage must remain separate from Wadsworth 1977 and Meyer 1978. The next durable unit is HS-052.

HS-052 is fully read as the 88-page Nolan–Sharpey-Schafer lifetime-method review. It provides the DSAM/RDM, stopping, feeding, timing, blocking and indirect-width framework needed to interpret the batch's lifetime sources; no historical review example is counted as a new experiment. The next durable unit is HS-053.

HS-053 is the published PRC version of the existing Petrache `136Nd` source. It was reread end-to-end and confirms the five-pair scheme, D5 partner-ratio evidence and TAC/CDFT caveats; no material claim changed, and the row is an alternate-version audit rather than a new experiment. HS-054 is a confirmed contamination exclusion; the next durable unit is HS-055.

HS-055 is fully read as the Walker–Dracoulis exotic-isomer review. It links high-spin/K traps and forbiddenness to axial symmetry, but preserves the decisive role of configuration mixing, decay-path availability and K mixing; cited isomer examples are review-level, not new experiments. The next durable unit is HS-056.

HS-056 is fully read as Frauendorf's 38-page low-energy quadrupole-mode review. Bohr/ATDMF/GCM/IBM, γ-softness, tidal waves and TPSM are connected while adiabatic/decoherence and model-fit limits are retained. The next durable unit is HS-057.

HS-057 is fully read as the short `252Cf` fission γ-band-systematics paper. Mo/Ru/Pd γ-band odd-even staggering reverses rapidly with spin/neutron number; the authors explicitly reject a one-model or backbending-only explanation and call for microscopic γ-soft/triaxial treatment. The next durable unit is HS-058.

HS-058 is fully read as the Heyde–Wood 55-page shape-coexistence RMP. It separates shell/mean-field/IBM mechanisms and establishes E0, E2, radii, 0+ energies and configuration evidence as a companion-observable set; no single band/0+ is promoted to coexistence proof. The next durable unit is HS-059.

HS-059 is fully read as the segmented-Gammasphere polarization method paper. It establishes confined/shared asymmetry definitions, measured-versus-Monte-Carlo `Q(E)` and a high-background `197Pb` parity example, while retaining array-specific response and sign limits. The next durable unit is HS-060.

HS-060 is fully read as the 56-page Krane–Steffen–Wheeler generalized DCO review. It formalizes oriented-state statistical tensors, multipole conventions, geometry coefficients and practical tables, reinforcing that DCO/R_ac is a compressed, setup-dependent observable. The next durable unit is HS-061.

HS-061 is fully read as the compact Nuclear Data Sheets spin/parity-assignment checklist. It codifies strong versus weak evidence and high-spin DCO/polarization/angular-distribution requirements; its typical thresholds are retained as setup-specific guidance rather than universal rules. The next durable unit is HS-062.

HS-062 is fully read as the two-page Nature News & Views commentary on Gaffney's pear-shaped Rn/Ra experiment. It adds EDM/Schiff-moment context but remains secondary; all quantitative nuclear claims route to the direct HS-028 source. The next durable unit is HS-063.

HS-063 is fully read as the global FRLDM axial-asymmetry PRL. It predicts selected triaxial ground-state regions and correlates them with γ bands and improved mass residuals, but retains model-minimum/zero-point and non-direct-observable boundaries. The next durable unit is HS-064.

HS-064 is fully read as Meng Jie’s Chinese review of nuclear chirality. It consolidates geometry/fingerprints and TAC/TPRM/RMF limitations while explicitly requiring lifetimes/absolute strengths and primary-source verification; it contributes no independent experiment count. The next durable unit is HS-065.

HS-065 is fully read as Suzuki–Kimura’s AMD/Gogny-D1S+GCM study of N=28 shell-gap erosion. It predicts triaxial/γ-soft projected shapes and interband-E2 diagnostics near `42Si`, but all deformation/shell-evolution results remain model outputs. The next durable unit is HS-066.

HS-066 is fully read as a one-page Macchiavelli PRC erratum for `11,12Be` Nilsson spectroscopic factors. The corrected formulas/Table II are recorded with the original-paper/data gap; it produces no material change to this high-spin batch. The next durable unit is HS-067.

HS-067 is fully read as the PPCO method paper. It derives two-polarimeter four-count observables and shows how PPCO+DCO contours reduce spin/parity/multipole ambiguities, while detector `Q`, alignment and cascade order remain explicit inputs. The next durable unit is HS-068.

HS-068 is fully read as Gade et al.'s 2025 FRIB/GRETINA `62Cr` experiment. A low-lying excited `0+` state is established with γγ/multiplicity, knockout momentum and shell-model/DNO-SM support; direct evidence and model shape labels remain separated. The next durable unit is HS-069.

HS-069 is fully read as McCutchan et al.'s `S(J)/S(4)` γ-band staggering systematics. It maps phase/magnitude patterns across vibrator, γ-soft, axial and rigid-triaxial limits but preserves the non-unique, companion-observable boundary. The next durable unit is HS-070.

HS-070 is the arXiv version of the existing Nomura `128,130Xe` pairing/triaxial-vibration source; it was reread end-to-end with no material claim change. HS-071 is an exact duplicate row, individually self-audited without rereading or extra source count. The next durable unit is HS-072.

HS-072 is fully read as Starosta et al.'s EUROGAM-II PDCO method test. The CLOVER `Q(E)` calibration and four direction-pair geometries are combined with `R_DCO`; the `647 keV` transition is selected as E1 within tested hypotheses, while the `490 keV` transition remains stretched-E2 versus ΔI=0 M1/E2 ambiguous. Integrated-mode polarization is qualitative unless solid-angle/efficiency corrections and the transferred alignment parameter are justified. The next durable unit is HS-073.

HS-073 is fully read as Rees et al.'s `156Er` Gammasphere study. Weak non-yrast bands, a near-degenerate second `0+`/γ-band head and persistent `S(4)≈−1` staggering provide a non-A≈130 γ-soft comparator; angular-intensity ratios and alignment plots support, but do not uniquely prove, the band-9 `(νh9/2,f7/2)2` interpretation against competing configuration/shape explanations. The next durable unit is HS-074.

HS-074 is the user-confirmed contamination exclusion (N-isopropyl dopamine derivative source); the original file is absent and no scientific processing was performed. The next durable unit is HS-075.

HS-075 is fully read as Hübel's 69-page magnetic-rotation review. It consolidates high-fold spectroscopy, DSAM/RDM, g-factor and quadrupole moments, TAC and `P2(θ)` shears modeling, and the weaker antimagnetic-rotation evidence. The durable rule is multi-observable and lineage-aware: decreasing `B(M1)`, weak/decreasing `B(E2)`, configuration, moments and termination must be kept separate from review-level model labels. The next durable unit is HS-076.

HS-076 is fully read as Hamilton's high-resolution `194,196Pt` mixing-ratio experiment. Ge–NaI γγ correlations and a summing polarimeter give `δ=−(30^{+39}_{−19})` for `194Pt` and `+4.03(12)` for `196Pt` in the Biedenharn convention; the latter conflicts with the then-current theory, while the 759-keV correlations expose an unresolved-transition/level-scheme warning. The next durable unit is HS-077.

HS-077 is fully read as Jones et al.'s four-crystal EUROGAM CLOVER calibration. It separates physical `P`, count asymmetry `A` and detector sensitivity `Q=A/P`; `Q` falls from `0.34(9)` at 197 keV to `0.121(5)` at 1368 keV for the tested 60-keV threshold. The fit is a geometry- and threshold-specific response, not a universal CLOVER constant. The next durable unit is HS-078.

HS-078 is fully read as the 79-page Aprahamian–Langanke–Wiescher nuclear-astrophysics review. It maps masses, thresholds, shell/cluster structure, level densities, deformation, electromagnetic/GT strengths and weak rates into reaction-network regimes, while preserving direct/R-matrix/Hauser–Feshbach boundaries and model spread. It adds no independent A≈130 high-spin evidence. The next durable unit is HS-079.

HS-079 is fully read as Pfützner et al.'s 53-page RMP review. It separates separation-energy limits from observed decay modes, and connects β-delayed particles, proton/α radioactivity, true two-proton three-body decay, shell/pairing and neutron-continuum constraints. Review lineage and the true-2p/sequential/democratic distinction remain explicit; it adds no independent A≈130 high-spin experiment. The next durable unit is HS-080.

HS-080 is fully read as Rose–Brink's 42-page phase-consistent angular-distribution review. It derives the interaction multipoles and `B_K`/`R_K` tensor chain, defines δ through reduced matrix elements, and shows how γγ correlations multiply population and response tensors. The key audit boundary is operator phase, state order, parity and alignment: δ signs cannot be compared across Hamilton/Taras/DCO sources until that map is explicit. The next durable unit is HS-081.

HS-081 is fully read as Der Mateosian–Sunyar's 56-page high-spin coefficient tables. It extends mixed-multipole `A_2/A_4` values to integer `J≤26` and half-integer `J≤51/2`, uses Gaussian `σ/J` attenuation, and demonstrates a joint `(σ/J,δ)` intersection. It explicitly warns that angular-distribution and γγ-correlation δ signs can differ by convention. The next durable unit is HS-082.

HS-082 is fully read as the 89-page Åberg–Flocard–Nazarewicz mean-field shape review. It maps HF/HFB and Nilsson–Strutinsky methods through quadrupole/triaxial, rotating high-spin, octupole, superdeformed and coexistence regimes, while keeping intrinsic minima, symmetry restoration, configuration mixing and laboratory observables separate. It adds theory backbone, not an independent high-spin experiment. The next durable unit is HS-083.

HS-083 is fully read as Mukhopadhyay et al.'s `135Nd` PRL. Gammasphere DSAM lifetimes give nearly identical partner-band intraband `B(E2)`/`B(M1)` patterns; TAC+RPA reproduces energies/strengths and models the evolution from chiral vibration to static chirality as the phonon softens. DSAM feeding and the model critical-spin offset remain explicit, and the result is a nucleus-specific reference rather than a universal chiral template. The next durable unit is HS-084.

HS-084 is fully read as Ma et al.'s `131Ba` high-spin study. Ten bands, angular distributions, DCO ratios and mixing ratios establish a direct band/multipolarity map; proton and neutron `h11/2` alignments near `ℏω≈0.43 MeV` drive opposite near-prolate/near-oblate CSM/TRS minima, explaining signature-splitting changes and decoupled `ΔI=2` bands. The γ labels and uncertain bands remain model/geometry dependent. The next durable unit is HS-085.

HS-085 is fully read as Eldridge et al.'s ten-isotope Gammasphere IPAC study, and HS-086 is an exact same-hash duplicate row. Thirty-seven γ-band→ground-band δ determinations are predominantly E2; IPAC attenuation/g-factor corrections and `(A2,A4)` oval topology preserve multiple branches, including `±∞` pure-E2 limits. The `110Ru` sign trend supports a model/systematics shape-transition reading, not direct γ rigidity. The next durable unit is HS-087.

HS-087 is fully read as Miller et al.'s side-irradiated SeGA Compton calibration. A `249Cf` α–γ source gives `Q≈0.14(2)` near 350 keV and `FM≈5.9×10^-6` after geometric and finite-angle corrections; the result supports fast-beam parity-sensitive polarimetry but must not be transferred outside the tested orientation and energy range. The next durable unit is HS-088.

HS-088 is fully read as Krane–Steffen's `110Cd` 25-correlation Ge(Li) study. It gives a consistent E2/M1 δ set after Compton-background control and defines the emission-matrix-element/state-order map to Rose–Brink/Biedenharn conventions. The nonzero M1/crossover strengths challenge a pure harmonic-vibration picture, while δ portability remains convention- and spin-sequence dependent. The next durable unit is HS-089.

HS-089 is fully read as Aoki et al.'s Ge(Li) detector-method paper. A machined single-crystal polarimeter measures four azimuths simultaneously and reproduces the annihilation benchmark `2.47±0.30` versus `2.50`; a ring-reflector summing spectrometer reduces continuous background by ~20 while sacrificing efficiency and imposing a practical ~300-keV threshold. The next durable unit is HS-090.

HS-090 is fully read as Rahaman et al.'s `40K` INGA study. Six levels and fourteen transitions are added or reassigned using RDCO/RADO/IPDCO and Krane–Steffen δ values; `σ/J=0.3`, setup-specific RADO references and run-by-run high-energy calibration are explicit. sd–pf shell-model calculations supply configuration interpretation but not direct shape evidence. The next durable unit is HS-091.

HS-091 is fully read as Das et al.'s `37Ar` INGA study. The level scheme reaches 10.5 MeV with 18 new transitions/eight levels; RDCO/RADO/IPDCO/δ jointly assign spins and parities under `σ/J=0.3`, while sd–pf shell-model restrictions and two-level mixing interpret configurations. Calibration, Doppler-shift and low-statistics boundaries remain explicit. The next durable unit is HS-092.

HS-092 is fully read as Fagg–Hanna's 48-page polarization review. It separates alignment from polarization, derives direction–polarization/circular-correlation logic, surveys Compton/photoelectric/deuteron analyzers and preserves historical detector/sign conventions. It is a method backbone, not an independent high-spin experiment. The next durable unit is HS-093.

HS-093 is fully read as Bisoi et al.'s `34Cl` INGA study. The scheme reaches 10.6 MeV, with RDCO/IPDCO/δ assignments and DSAM lifetimes; selected E2 strengths of roughly `8–20 W.u.` indicate emerging collectivity. sd–pf cross-shell calculations and two-level mixing explain configurations, while stopping/feeding and calibration boundaries remain explicit. The next durable unit is HS-094.

HS-094 is the alternate LBNL-41340 preprint of the canonical Schmid Gammasphere polarization paper. It was reread section-by-section and matches the canonical `Q(E)`/Monte Carlo/`197Pb` application; no independent source or claim change is added. The next durable unit is HS-095.

HS-095 is fully read as Kramp et al.'s `16O` two-photon-decay study. The Crystal-Ball/particle setup obtains `Γ2γ/Γtot=(6.6±0.5)×10^-4`, rejects Compton and positron-annihilation-in-flight backgrounds, and uses angular interference/polarization to retain inverse `2E1/2M1` matrix-ratio branches. The polarizability/susceptibility interpretation remains model dependent. The next durable unit is HS-096.

HS-096 is the user-confirmed contamination exclusion (metal substitutions in carbonic anhydrase); the original file is absent and no scientific processing was performed. The next durable unit is HS-097.

HS-097 is fully read as Williams et al.'s `61Ni` low-energy multimethod study. Seventeen states below 2.2 MeV combine DSAM lifetimes, angular correlations, Ge(Li) polarization and particle–γ coincidence; revised `Jπ` assignments and M1/E2 strengths are compared with shell-model predictions. DSAM stopping/feeding and Rose–Brink convention boundaries keep this source distinct from the Meyer/Wadsworth/Samanta `61Ni` lineage. The next durable unit is HS-098.

HS-098 is fully read as the 87-page Ragnarsson–Nilsson–Sheline shell-structure review. It maps magic numbers, shape-dependent shell gaps, Strutinsky/Nilsson corrections, high-spin stability, superdeformation and shape isomers, while preserving the distinction between intrinsic model minima and laboratory observables. It adds theory backbone, not an independent experiment. The next durable unit is HS-099.

HS-099 is fully read as James–Twin–Butler's statistical angular-correlation method paper. It requires alignment-model variance in the design matrix, uses effective degrees of freedom `n−rank`, recommends `arctanδ` confidence contours, and explicitly identifies alignment/δ compensation as a non-identifiability condition. The next durable unit is HS-100.

HS-100 is fully read as Grodner et al.'s `128Cs` PRL. Two independent TDPAD measurements give `g=+0.59(1)` for the 56-ns bandhead; the generalized three-vector relation and PRM+CDFT show core-rotation admixture and an almost planar bandhead (`⟨ô⟩≈0.15`) rather than ideal chirality. The result supports a critical-frequency onset boundary for chiral geometry. The next durable unit is HS-101.

HS-101 is fully read as Garg et al.'s `135Pr` high-spin study. RDCO/IPDCO establish a negative-parity ΔI=1 band with M1/E2 links and E2 crossovers; TAC 3qp→5qp configurations reproduce the crossing and motivate a possible magnetic-rotation interpretation. No lifetimes or absolute `B(M1)/B(E2)` are provided, so the MR label remains provisional. The next durable unit is HS-102.

HS-102 is the user-confirmed contamination exclusion (maturation of adrenal medulla IV); the original file is absent and no scientific processing was performed. The next durable unit is HS-103.

HS-103 is fully read as Liu et al.'s A≈130 `πh11/2⊗νh11/2` signature-inversion systematics. Revised bandhead-spin crosswalks make low-spin inversion systematic and agree with particle–triaxial-rotor calculations, but Cs reference choices remain incompatible and the inferred γ interpretation is systematics/model dependent. The next durable unit is HS-104.

HS-104 is fully read as Henderson et al.'s `98Mo` two-photon upper-limit experiment. DSSD conversion-electron normalization and delayed Gammasphere searches give `Γ2γ/Γ<1×10^-4` at 95% CL; efficiency/energy-sharing and Feldman–Cousins boundaries remain explicit, so non-observation is not a zero branch or direct shape verdict. The next durable unit is HS-105.

HS-105 is fully read as Davidson's 54-page collective-model review; HS-106–HS-108 are exact same-hash duplicate rows. Surface vibrations, rotor limits, odd-particle coupling, electromagnetic/decay probes and model assumptions are preserved as historical theory context, with no extra source count. The next durable unit is HS-109.

HS-109 is fully read as Schlitt et al.'s fourfold sectored-Ge NRF polarimeter paper. It reports `Q≈20%` at 0.5 MeV and `≈9.5%` at 4.4 MeV, ~25% coincidence efficiency and an NRF `162Dy` parity-sign demonstration; all values are detector/threshold/NRF-geometry specific. The next durable unit is HS-110.

HS-110 is fully read as Der Mateosian–Sunyar's 16-page attenuation-table companion. Gaussian `m`-substate populations produce tabulated `α2/α4` through integer `J=26` and half-integer `51/2`; the `Ji=10→Jf=8`, `σ/J=0.3` example gives attenuated `A2=0.3126`, `A4=−0.0717`. `σ/J` remains a reaction/feeding model parameter, not a universal prior. The next durable unit is HS-111.

HS-111 is fully read as the distinct 1970 Nuclear Data Sheets proposition sheet. It separates strong from weak bases for spin/parity assignments, lists setup-specific DCO/polarization/angle heuristics and explicitly downgrades interpolation, nonobservation and generic g-factor arguments. It is kept separate from the later compact proposition compilation. The next durable unit is HS-112.

HS-112 is fully read as Vaillancourt–Taras's three-multipole formalism. Rose–Brink phases, complete angular-distribution interference terms and the Eq.32 angular→linear-polarization recipe cover arbitrary mixtures, with `E1/M2/E3` requiring two δ ratios; identifiability and phase conventions remain explicit. The next durable unit is HS-113.

HS-113 is fully read as Droste et al.'s PDCO formal precursor. One statistical-tensor expression unifies DCO, PDCO and PPCO, with explicit emission/detector planes, `cos2φ` terms, deorientation coefficients and Gaussian alignment; later Starosta/Droste implementations inherit these geometry boundaries. The next durable unit is HS-114.

HS-114 is fully read as Ewan et al.'s single-planar-GeLi polarization letter. Calibration spans 0.8–4.4 MeV; `102Ru` E2 lines are positive while an 833-keV mixed line has opposite asymmetry. The detector demonstrates parity/mixing sensitivity but its `Q(E)` is energy/geometry/photoelectric specific. The next durable unit is HS-115.
