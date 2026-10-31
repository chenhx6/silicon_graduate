---
type: project
title: "Sigma-over-I uncertainty in P-ADO mixing-ratio extraction"
aliases: [sigma over I uncertainty, sigma/I uncertainty, P-ADO sigma over I, alignment uncertainty in P-ADO, NST sigma-over-I evidence map]
created: 2026-07-08
updated: 2026-07-13
status: active
review_status: human-reviewed
project_stage: evidence-map
confidentiality: private
nuclei: []
tags: [pado, mixing-ratio, angular-distribution, polarization, alignment, sigma-over-i, evidence-map, nst-writing-support]
---

# Sigma-over-I Uncertainty in P-ADO Mixing-Ratio Extraction

## Active Summary for Agents

Current task: the earlier synthesis-planning round is complete, and a new four-source gamma-spectroscopy-method ingest has been attached to this project as additional evidence about how `delta` extraction can still remain assumption- or branch-dependent even when DCO, polarization, or ICC constraints are added.

Completed source rows: [[draper-1970-gaussian-substate-side-feeding]]; [[zobel-1980-magnetic-substate-distributions]]; [[zobel-1983-energy-projectile-alignment]]; [[cejnar-1996-spin-deorientation-alpha-2n-gamma]]; [[radeck-2012-deorientation-lifetime-98ru-rdds]]; [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]; [[chiara-2012-cu65-cu67-core-coupled-protons]]; [[summary-2013-bases-spin-parity-assignments]]; [[gray-2020-hyperfine-fields-g-factor-measurements]]; [[ekstrom-1979-spin-alignment-attenuation-a61-a67]]; [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]]; [[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]]; [[kramer-flecken-1989-use-dco-ratios]]; [[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]]; [[rusev-2009-multipole-mixing-ratios-11b]]; [[diamond-1966-nuclear-alignment-heavy-ion-reactions]].

In-progress / pending source rows: the 2026-07-12 four-source method round has now been user-reviewed. The project-level notes were accepted in that review round; the only intentionally retained claim-level recheck is source note `RU09-6`, where branch selection still depends on author-side physical-plausibility judgment.

Synthesis readiness: ready for bounded writing-support synthesis, but not yet ready for user-code-facing equations, a universal numeric prior, or final manuscript wording without further source-to-user notation mapping.

High-risk scope boundary: keep Draper/Cejnar `sigma`, project/user `sigma/I`, Lauritsen `sigma/J`, Ekstrom `alpha2/alpha4`, Ionescu `rho2/rho4`, Zobel attenuation coefficients, and Radeck `Gk/Qk` distinct.

## Research Question

Why is it unsafe or model-dependent to preset a single `sigma/I` value when extracting in-beam gamma-ray mixing ratios from angular-distribution and polarization observables?

## Synthesis Readiness

- Status: ready for bounded writing-support synthesis.
- Source coverage: the original 11-source alignment/deorientation package is reviewed; four new method sources extend the project toward ICC, DCO and polarization-only `delta` extraction boundaries, but they are not yet human-reviewed.
- Structural audit: no known missing `citation_key`, missing `raw_file`, missing locator, or missing claim-kind blocker was found in the audited project/source chain.
- Evidence categories completed: Gaussian substate formalism; CNR / alignment attenuation estimates; Gaussian-hypothesis limitations; feeding-aware population models; fusion-evaporation projectile / energy / feeding dependence; deorientation / attenuation evidence; experimental-practice evidence; empirical expectation and failure examples; implications for P-ADO motivation.
- Unresolved P0: none at the project-note level after the 2026-07-12 review round.
- Unresolved P1: user-data-specific mapping of reaction conditions, detector geometry, calibration transitions, and whether the user's code convention matches `sigma/J` or another normalized width.
- Recommendation: yes, proceed to NST introduction writing-support at the bounded framework level; no, do not yet write code-facing equations or a universal `sigma/I` prior.
- Writing-support synthesis: [[sigma-over-i-assumptions-and-mixing-ratio-extraction]]

## Scope

This is an evidence map / writing-support project for NST paper and future thesis text. It is not a final synthesis, not a paper conclusion, and not a claim that all P-ADO analyses fail. The goal is to assemble source-level evidence that alignment, magnetic-substate population, side feeding, reaction conditions, and attenuation treatment can change the angular-distribution response used in `delta` extraction.

## Current Hypotheses

- H1: Presetting a single `sigma/I` can hide feeding- and condition-dependent alignment uncertainty.
- H2: P-ADO should expose the coupling between `delta` and alignment/population assumptions rather than treat alignment as a universal constant.
- H3: The accumulated source set motivates caution but does not yet define a final prior range for user data.

## Evidence Available

Current evidence consists of Draper 1970 formal side-feeding treatment, Zobel 1980 attenuation/ALY/Gaussian-condition analysis, Zobel 1983 projectile/energy/feeding dependence in `67Ga`, Ekstrom 1979 compiled spin-alignment attenuation factors plus MANDY/CNR uncertainty and Gaussian-limitation arguments, Ionescu 1981 feeding-aware angular-distribution analysis in `167Tm`, Cejnar 1996 spin-deorientation calculation in `Pd(alpha,2n gamma)Cd` reactions, Radeck 2012 time-dependent deorientation correction in inverse Coulomb excitation + RDDS, Lauritsen 2025 modern tracking-array angular-distribution / polarization formalism, Chiara 2012 as a spectroscopy practice example using assumed `sigma/I`, Summary 2013 as reference-guide high-spin assignment background with typical `sigma/I = 0.3`, Gray 2020 as a TDPAD / `g`-factor boundary case where empirical `sigma/I` expectations can fail, plus a new 2026-07-12 method bundle on ICC-based `delta` extraction, DCO geometry/multi-solution boundaries, and polarization-asymmetry branch ambiguity from Rezynkina 2017, Kramer-Flecken 1989, Kibedi 2008, and Rusev 2009.

## Symbol Mapping

| Symbol or term | Source-level meaning | Project boundary |
|---|---|---|
| `sigma` in Draper 1970 | Gaussian width of side-feeding magnetic-substate population `P_sigma(M)` | Do not equate directly with `sigma/I`; use as evidence that width assumptions are model choices. |
| `A2`, `A4` | Legendre angular-distribution coefficients for `W(theta)` | Observables affected by population/alignment and transition properties. |
| `rho_k` in Ionescu 1981 | Statistical-tensor factor built from magnetic-substate population `Pm(Ji)`; Fig.3 uses `rho2` and `rho4` for pure-`E2` tests | Related to attenuation-factor language, but not identical notation; do not silently relabel `rho_k` as `alpha_k`. |
| `alpha2`, `alpha4` in Ekstrom 1979 | Spin-alignment attenuation factors reduced from pure-E2 angular distributions | Alignment descriptors constrained by pure-E2 data; not the same symbol layer as Gaussian width `sigma` or user-code `sigma/I`. |
| MANDY / CNR alignment estimate | Compound-nucleus-reaction-model prediction for alignment/population parameters derived from transmission probabilities | A model-based alignment estimate that needs its own uncertainty budget; not the same thing as P-ADO marginalization over `sigma/I`. |
| `sigma` in Ionescu 1981 | Width parameter for the Gaussian side-feeding contribution to the substate population | In the improved model it describes side feeding only, not the total population of a level. |
| attenuation coefficients in Zobel 1980/1983 | Alignment attenuation descriptors for partial alignment relative to complete alignment | Related to alignment, but not identical to Gaussian `sigma` or normalized `sigma/I`. |
| `U_lambda` in Cejnar 1996 | Deorientation coefficient for a particle or gamma transition from `Ji` to `Jf` carrying angular momentum `L` | Propagates orientation flow through reaction routes; not the same as `sigma`, `sigma/I`, `sigma/J`, or measured attenuation coefficients. |
| `Gk(t)` / `Gk(d)` in Radeck 2012 | Time- or distance-dependent attenuation factor for hyperfine-driven deorientation in RDDS angular correlations | Related deorientation correction, but not a side-feeding Gaussian width or detector `Qk`. |
| `Qk` in Radeck 2012 | Detector finite-solid-angle correction in the angular-correlation function | Detector geometry term; do not confuse with nuclear alignment/deorientation attenuation. |
| `Pm(J)` in Lauritsen 2025 | Magnetic-substate distribution for level spin `J`, usually Gaussian with respect to the beam axis | Direct bridge from alignment population to `alpha_k(J)` and normalized `sigma/J`; still not automatically identical to user-code `sigma/I`. |
| `sigma/J` in Lauritsen 2025 | Normalized Gaussian width characterizing `Pm(J)`; `sigma/J = 0` indicates full alignment | Closest source-level notation to project `sigma/I`; must be mapped to the user's convention before paper wording. |
| `sigma/I` in Summary 2013 | Typical magnetic-substate population parameter used in high-spin angular-distribution and DCO assignment heuristics | Practice-level orientation parameter; keep it as guide-level background rather than a universal default. |
| `alpha_k` in Lauritsen 2025 | In source angular correlations: detector solid-angle attenuation; in in-beam angular distributions: nuclear alignment/deorientation attenuation from `Pm(J)` | Preserve local formula context; do not merge detector and nuclear attenuation meanings. |
| `R(t)` amplitude in Gray 2020 | TDPAD observable depending on both alignment `B2` and the field-free fraction `p` after implantation | A reduced amplitude does not uniquely diagnose weaker alignment or more field-free sites without independent information. |

## Source-by-Source Evidence Table

| Source | Strategy | Direct contribution to project | Key claim IDs | Review priority |
|---|---|---|---|---|
| [[draper-1970-gaussian-substate-side-feeding]] | theory-ingest + method-ingest + project-ingest | Shows that stretched-E2 `A2/A4` depend on Gaussian side-feeding width, cascade feeding, and side-feeding intensities; provides exact treatment and allowed coefficient-space boundaries. | DR70-1 to DR70-10 | P0 resolved: DR70-3, DR70-6, DR70-7 |
| [[diamond-1966-nuclear-alignment-heavy-ion-reactions]] | experiment-ingest + foundational-method-ingest + sigma-over-I-project-ingest | Early heavy-ion entrance-alignment and stretched-E2 `A2/A4` evidence; explains same-state pure-transition calibration before mixed E2/M1 `delta` extraction and records Gaussian/deorientation limits. | D66-1 to D66-11 | Source reviewed 2026-07-13; no source-level P0 remains |
| [[zobel-1980-magnetic-substate-distributions]] | experiment-ingest + method-ingest + project-ingest | Shows that angular-distribution-only fitting has more unknowns than measured coefficients unless alignment is known or modeled; documents ALY/Gaussian assumptions, their conditions, and lifetime/Doppler effects on attenuation coefficients. | Z80-1 to Z80-13 | P0 resolved: Z80-2, Z80-3, Z80-10 |
| [[zobel-1983-energy-projectile-alignment]] | experiment-ingest + method-ingest + project-ingest | Shows that attenuation coefficients vary with projectile, incident energy, and direct/cascade feeding balance; warns against combining angular-distribution and polarization data from different conditions. | Z83-1 to Z83-10 | P0 resolved: Z83-5, Z83-8, Z83-9 |
| [[cejnar-1996-spin-deorientation-alpha-2n-gamma]] | theory-ingest + method-ingest + project-ingest | Calculates spin deorientation through angular-momentum routes, tests the side-feeding Gaussian hypothesis, and shows that the imposed `sigma` interval can change `delta` extraction. | C96-1 to C96-11 | P0 resolved: C96-4, C96-5, C96-10 |
| [[radeck-2012-deorientation-lifetime-98ru-rdds]] | method-ingest + experiment-ingest + project-ingest | Demonstrates time-dependent deorientation correction with particle-gamma angular correlations and separates `Rk`, `Bk`, `Qk`, `Gk`, and deorientation correction factors in inverse Coulomb excitation + RDDS. | R12-1 to R12-12 | P0 resolved: R12-3, R12-7, R12-8, R12-10 |
| [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] | method-review-ingest + project-ingest | Provides modern tracking-array formalism connecting `delta`, `alpha_k`, Gaussian `Pm(J)`, `sigma/J`, response functions, DCO, and linear polarization. | L25-1 to L25-16 | P0 resolved: L25-5, L25-7, L25-8, L25-14, L25-15 |
| [[chiara-2012-cu65-cu67-core-coupled-protons]] | experiment-ingest + targeted-ingest + project-ingest | Gives a concrete spectroscopy practice example where `sigma/I = 0.5` is assumed to reproduce known transitions and a different assumed `sigma/I` changes the fitted `delta` for one `65Cu` line. | CH12-1 to CH12-8 | P0 resolved: CH12-3, CH12-5 |
| [[summary-2013-bases-spin-parity-assignments]] | reference-guide-ingest + targeted-ingest + project-ingest | Records high-spin assignment heuristics for angular distributions and DCO ratios at a typical `sigma/I = 0.3`, making the practice background explicit while keeping it at guide level. | SB13-1 to SB13-7 | P0 resolved: SB13-2, SB13-4, SB13-7 |
| [[gray-2020-hyperfine-fields-g-factor-measurements]] | experiment-ingest + method-ingest + project-ingest | Shows in a TDPAD / `g`-factor context that empirical alignment expectations such as `sigma/I ≈ 0.35` can fail and that reduced `R(t)` amplitude does not uniquely diagnose field-free implantation. | G20-1 to G20-9 | P0 resolved: G20-4, G20-6, G20-7 |
| [[ekstrom-1979-spin-alignment-attenuation-a61-a67]] | experiment-ingest + method-ingest + project-ingest | Compiles pure-E2 angular distributions into `alpha2/alpha4`, tests MANDY/CNR alignment estimates, prescribes an uncertainty budget, and argues that a simple Gaussian magnetic-substate population is too restrictive. | EK79-1 to EK79-9 | Source P0 resolved on 2026-07-09; synthesis P0 now concerns notation boundary and paper-gate wording. |
| [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] | experiment-ingest + method-ingest + project-ingest | Shows in `165Ho(alpha,2n)167Tm` that the global Gaussian hypothesis fails and that a feeding-aware model with Gaussian side feeding plus discrete direct feeding can improve spin and `delta` analysis. | IO81-1 to IO81-10 | Source P0 resolved on 2026-07-09; synthesis P0 now concerns feeding-aware wording and notation boundary. |
| [[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]] | method-ingest + project-ingest | Adds an ICC-based graphical/PDF route to `delta`, emphasizing asymmetric uncertainty propagation and the failure of naive inversion when ICC errors are large. | RZ17-1 to RZ17-7 | Reviewed on 2026-07-12; no claim correction requested. |
| [[kramer-flecken-1989-use-dco-ratios]] | method-ingest + theory-ingest + project-ingest | Gives the DCO-ratio definition, the experimental `R_DCO` intensity ratio, geometry/alignment dependence, efficiency-correction practice, the low-spin `I < 6` deviation from the near-constant `sigma/I` heuristic, and the explicit statement that one DCO ratio can map to several spin/`delta` solutions. | KF89-1 to KF89-8 | Reviewed on 2026-07-12; low-spin `sigma/I` wording and experimental-formula note corrected. |
| [[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] | review-ingest + theory-ingest + project-ingest | Supplies the BrIcc mixed-transition ICC formalism, `delta`/energy uncertainty propagation, vacancy-treatment boundary, and interpolation cautions for ICC-based `delta` work. | KB08-1 to KB08-8 | New review needed: BrIccFO default wording, interpolation boundary, nonunique-multipolarity handling. |
| [[rusev-2009-multipole-mixing-ratios-11b]] | experiment-ingest + method-ingest + project-ingest | Shows a polarization-asymmetry-only `delta` extraction route and explicitly demonstrates that one measured asymmetry can correspond to two `delta` solutions, with branch selection still requiring author-side physical-plausibility judgment. | RU09-1 to RU09-7 | Reviewed on 2026-07-12; keep `RU09-6` as a source-level human-recheck note. |

## Experimental-Practice Evidence

## Early Heavy-Ion Alignment Foundation

Diamond 1966 is an early source for the reaction-side premise behind this project. It links heavy-ion entrance orbital angular momentum to an approximately aligned compound nucleus, compares stretched-E2 `A2/A4` values with a Gaussian `m=0` reference, and explains that a pure transition from the same state can calibrate alignment before a mixed-transition `delta` fit. The source also reports deviations from the Gaussian reference and warns that extranuclear interactions can attenuate the alignment. This is foundational context, not a universal `sigma/I` prior; D66-1..11 were source-reviewed on 2026-07-13.

The article7-9 sources add a different layer from the earlier formalism and deorientation papers. They show that assumed or typical orientation parameters are embedded in real spectroscopy practice and reference-guide language, but that these assumptions remain notation-sensitive and context-sensitive.

Chiara 2012 is the most direct spectroscopy example: a working `sigma/I` value is chosen because it reproduces known transitions, and a single transition's fitted `delta` changes when the assumed alignment changes. Summary 2013 is weaker scientifically but important culturally: it documents that high-spin assignment heuristics are often quoted with a typical orientation parameter, here `sigma/I = 0.3`. Gray 2020 is the counterweight: in an isomeric TDPAD context, an empirical `sigma/I ≈ 0.35` expectation can fail, and amplitude alone does not tell you whether the issue is alignment or field-free implantation.

## Supplemental Core Evidence

Ekstrom 1979 strengthens the older alignment-limitation evidence chain from a complementary direction. Instead of starting from a fit ambiguity alone, it compiles pure-E2 data into `alpha2/alpha4`, tests CNR/MANDY alignment estimates against experiment, gives an explicit uncertainty prescription for those estimates, and warns that too-small alignment errors can lead to faulty spin/parity or mixing-ratio assignments.

Ionescu 1981 then shows what to do when a global Gaussian substate-population model fails in a carefully measured case. It uses pure-E2 transitions and their `rho2/rho4` behavior to test the Gaussian hypothesis, finds it inadequate for `167Tm`, and replaces it with a model that keeps Gaussian side feeding but adds discrete direct gamma-feeding contributions explicitly before fitting mixed transitions.

## Low-Spin Sensitivity Audit

Current audit result: the 11-source package does not yet provide a clean, source-backed universal statement that `sigma/I` must vary strongly across all low-spin `I < 10` cases.

What the current source set does support is a narrower, project-level caution:

- Draper 1970 and Lauritsen 2025 make clear that the population width is tied to the discrete magnetic-substate distribution and to spin normalization, so raw `sigma` and normalized `sigma/I` / `sigma/J` should not be treated as spin-blind constants.
- Ionescu 1981 shows that a single global Gaussian hypothesis can already fail in a case where population details matter before mixed-transition `delta` fitting.
- Chiara 2012 shows that practical `delta` extraction can move when the assumed alignment width changes.
- Summary 2013 makes the common `sigma/I = 0.3` language explicitly high-spin and heuristic; it is not direct low-spin evidence.

Therefore, the present project can justify higher caution about low-spin reuse of a preset width, but it cannot yet claim a universal low-spin law for `sigma/I`.

## Evidence Map

| ID | Project statement | Source basis | claim_kind | Boundary / gap | needs_review |
|---|---|---|---|---|---|
| SIO-PROJ-1 | Even before mixed `M1/E2` transitions are fitted, angular-distribution coefficients for stretched E2 transitions depend on magnetic-substate population and feeding history. | DR70-2 to DR70-7 | Wiki synthesis / project note | Based on a stretched-E2 side-feeding formalism; not a direct P-ADO calculation. | false |
| SIO-PROJ-2 | A single Gaussian width can be a useful model input in selected comparisons, but Draper 1970 treats it as an assumed side-feeding population form rather than an experimental constant. Final-level populations may be mixed `bar(P)(M)` distributions rather than single Gaussians. | DR70-3, DR70-8, DR70-9 | Wiki synthesis / project note | Need later P-ADO notation mapping before equating Draper `sigma` with normalized `sigma/I`. | false |
| SIO-PROJ-3 | If alignment is known, angular distributions can constrain multipolarity and mixing ratio; if not, attenuation parameters and `delta` create an underconstrained fit unless extra information or a population model is supplied. Zobel's three routes are model-estimated attenuation coefficients, additional polarization/conversion data, or a one-parameter magnetic-substate distribution. | Z80-1 to Z80-4 | Wiki synthesis / project note | This is the direct method argument for why silently fixing `sigma/I` can make `delta` extraction assumption-dependent. | false |
| SIO-PROJ-4 | Gaussian or ALY-based alignment assumptions are conditional, with explicit risks from side feeding, isomers, short lifetimes, Doppler broadening, lifetime-dependent shifts of attenuation-coefficient pairs, and feeding-component mixtures. | Z80-7 to Z80-13 | Wiki synthesis / project note | Does not imply Gaussian assumptions are invalid in all cases; it identifies conditions that must be checked. | false |
| SIO-PROJ-5 | Alignment attenuation can change with projectile, incident energy, and the direct/cascade feeding balance, so a preset alignment parameter is condition-specific rather than universally transferable. | Z83-3 to Z83-8 | Wiki synthesis / project note | Based on `67Ga`; generalization to user data requires reaction-specific checks. | false |
| SIO-PROJ-6 | Combining angular-distribution and polarization constraints for `delta` should preserve beam/projectile/target consistency or explicitly model condition differences. | Z83-9 | Wiki synthesis / project note | This is a methodological caution, not a ban on combining datasets. | false |
| SIO-PROJ-7 | Spin-deorientation calculations connect a Gaussian side-feeding width to reaction-specific angular-momentum routes, projectile energy, quasicontinuum feeding, and discrete-level feeding corrections. | C96-2 to C96-9 | Wiki synthesis / project note | Cejnar 1996 is a statistical-model result for `Pd(alpha,2n gamma)Cd`; it is relevant background, not a universal `sigma/I` prescription. | false |
| SIO-PROJ-8 | The `sigma` region used in angular-distribution fitting can change the extracted `delta` branch or sign, so P-ADO writing should expose the alignment-width assumption instead of hiding it as a fixed constant. | C96-10 | Wiki synthesis / project note | Based on Cejnar Fig.7 for one `851.2 keV` transition; user data require their own `sigma/I` mapping. | false |
| SIO-PROJ-9 | Time-dependent deorientation can be measured through angular-correlation perturbations and encoded as `Gk(t/d)` factors; this supports treating alignment response as an experimental/model input with uncertainty. | R12-5 to R12-10 | Wiki synthesis / project note | Radeck 2012 is inverse Coulomb excitation + RDDS; use as related method background, not direct fusion-evaporation `sigma/I` evidence. | false |
| SIO-PROJ-10 | Modern fitting language must keep detector solid-angle attenuation `Qk`, nuclear alignment `Bk`/`alpha_k`, time-dependent deorientation `Gk`, and side-feeding Gaussian `sigma` / `sigma/J` separate before using them in `delta` extraction. | R12-7, R12-8; C96-5; L25-4 to L25-8; Z80-1 to Z80-4 | Wiki synthesis / project note | Lauritsen 2025 resolves the formalism vocabulary, but user P-ADO implementation details remain unmapped. | false |
| SIO-PROJ-11 | Lauritsen 2025 supplies the direct formula chain needed for P-ADO wording: `delta` enters transition-dependent `Amax_k`, in-beam `alpha_k(J)` describes nuclear alignment/deorientation, `alpha_k(J)` can be computed from `Pm(J)`, and `Pm(J)` is usually parameterized by Gaussian `sigma/J`. | L25-5 to L25-8 | Wiki synthesis / project note | This maps source notation, but does not prove the user's `sigma/I` is numerically identical to Lauritsen `sigma/J`. | false |
| SIO-PROJ-12 | Tracking-array response-function and polarization/DCO constraints do not remove alignment-width assumptions; they help separate detector response, angular distribution, parity/multipolarity ambiguity, and nuclear population assumptions. | L25-2, L25-10, L25-12 to L25-15 | Wiki synthesis / project note | Based on GRETINA examples and formalism; user detector/code path still needs mapping. | false |
| SIO-PROJ-13 | In practical spectroscopy work, an assumed `sigma/I` may be selected because it reproduces known reference transitions, and a different assumed value can change the fitted `delta` for a specific line. | CH12-3 to CH12-5 | Wiki synthesis / project note | Based on one `65Cu` angular-distribution analysis and one `1115 keV` example; not a universal fitting rule. | false |
| SIO-PROJ-14 | Reference-guide high-spin assignment heuristics explicitly use a typical `sigma/I = 0.3`; this is background for spectroscopy practice, not a universal fusion-evaporation prior. | SB13-1 to SB13-5 | Wiki synthesis / project note | Source is a Nuclear Data Sheets guide, not an original measurement or a theory derivation. | false |
| SIO-PROJ-15 | In an isomeric TDPAD / `g`-factor context, reduced `R(t)` amplitudes can indicate weaker-than-expected alignment and do not uniquely determine the field-free fraction; empirical `sigma/I ≈ 0.35` expectations may fail and require independent alignment checks. | G20-3 to G20-8 | Wiki synthesis / project note | Host-specific Fe/Gd implantation and hyperfine-field physics; useful boundary case, not a direct P-ADO fitting prescription. | false |
| SIO-PROJ-16 | Angular-distribution interpretation of spin/parity or mixing ratio requires externally constrained alignment information or an explicit population model; when CNR/MANDY alignment estimates are used, they need a nontrivial uncertainty budget rather than a near-fixed value. | EK79-2, EK79-5, EK79-6 | Wiki synthesis / project note | Ekstrom 1979 uses `alpha2/alpha4` and MANDY/CNR estimates, not user-code `sigma/I`; use it as alignment-uncertainty evidence, not as a direct prior prescription. | false |
| SIO-PROJ-17 | A simple Gaussian magnetic-substate population can be too restrictive for the compiled `A = 61-67` alignment data discussed in Ekstrom 1979. | EK79-7, EK79-9 | Wiki synthesis / project note | This is a limitation on one simple population family, not a universal rejection of all Gaussian-like models. | false |
| SIO-PROJ-18 | Pure-E2 transitions can be used to test and calibrate a population model; in `167Tm`, the global Gaussian hypothesis fails, while a model that combines Gaussian side feeding with discrete direct feeding gives better angular-distribution fits and sharper spin assignments. | IO81-3 to IO81-7 | Wiki synthesis / project note | Source is a detailed `165Ho(alpha,2n)167Tm` case study; it supports feeding-aware modeling, not a universal replacement formula for every reaction. | false |
| SIO-PROJ-19 | Angular-distribution-based `delta` extraction can depend on first constraining the population-width model from competing pure-E2 transitions; this is a concrete source-level example that feeding-aware alignment modeling may be needed before trusting mixed-transition assignments. | IO81-8, IO81-9 | Wiki synthesis / project note | The fitted width parameter describes side feeding in the improved model, not a direct one-to-one replacement for user-code `sigma/I`. | false |
| SIO-PROJ-20 | When unmodeled gamma feeding is appreciable, direct-population alignment estimates can become unreliable once the reaction energy lies sufficiently above the relevant particle-emission threshold. | EK79-8, EK79-9 | Wiki synthesis / project note | In EK79 the `E ≳ 2 MeV` wording belongs only to the Fig.5 `62Ni(alpha,n)65Zn` example; for `(alpha,p)` the effective above-threshold scale is lowered by the proton Coulomb barrier by about `2-3 MeV`, so this is not a universal numeric threshold. | false |
| SIO-PROJ-21 | Even when one uses ICC rather than angular-distribution coefficients, `delta` extraction still inherits theory-table, interpolation, transition-energy, and mixing-ratio uncertainty; BrIcc treats these pieces explicitly rather than assuming a fixed exact `alpha`. | KB08-2, KB08-3, KB08-6 | Wiki synthesis / project note | This is an ICC-method boundary, not direct evidence about user-data alignment. | false |
| SIO-PROJ-22 | ICC-based `delta` intervals can be asymmetric and effectively non-Gaussian; when the relative experimental ICC uncertainty becomes large, naive inversion of the mixed-transition ICC formula can bias the inferred central `delta` value. | RZ17-3 to RZ17-7 | Wiki synthesis / project note | Rezynkina 2017 uses a `251Fm` example and a graphical/PDF comparison, not a fusion-evaporation in-beam case. | false |
| SIO-PROJ-23 | DCO ratios compress gamma-gamma angular-correlation information, but their interpretive power depends on detector geometry, gate convention, efficiency correction, and alignment width; Kramer-Flecken 1989 also flags that the near-constant `sigma/I` heuristic itself deviates in the low-spin `I < 6` region, and a single measured DCO ratio may correspond to several spin or `delta` solutions. | KF89-1 to KF89-6 | Wiki synthesis / project note | Relevant as a general spectroscopy boundary; not a direct statement about the user's current detector geometry. | false |
| SIO-PROJ-24 | A polarization-related asymmetry observable can also admit two `delta` branches for the same measured value; selecting one branch may require additional physics judgment rather than asymmetry alone. | RU09-5, RU09-6 | Wiki synthesis / project note | Rusev 2009 uses polarized-photon NRF asymmetry, not in-beam clover Compton asymmetry. The transfer is conceptual, not one-to-one. | false |

## User-Analysis Normalization Note (Not a Source Claim)

The following note belongs to the user's current code / analysis convention, not to the 11-paper source package:

- `sigma` is the Gaussian standard deviation of the magnetic-substate population `Pm(I)`.
- `sigma/I` is that width divided by the spin `I` of the current level.
- In the user's current `P(m)` evaluation, values below `1E-12` are treated as numerically zero.
- For aligned states, `P(-m) = P(m)`; for oriented states, `P(-m) != P(m)`.
- In that implementation, half-integer spin levels are approximately full aligned by `sigma ~ 0.19`, while integer spin levels are approximately full aligned by `sigma ~ 0.13`.

This note is useful for later code-facing mapping, but it must not be cited as source-backed literature evidence.

## How This Supports P-ADO / NST Introduction

Draper 1970 supports a cautious wording: the alignment or population-width parameter used in angular-distribution calculations is a model-dependent representation of how the emitting state was populated. A normalized Gaussian side-feeding population can feed a final level that is simultaneously populated by other components, producing a mixed `bar(P)(M)` rather than a single Gaussian with one transferable width.

Zobel 1980 adds the direct angular-distribution-analysis reason: two measured angular-distribution coefficients cannot by themselves determine alignment and `delta` without extra information or a model. The paper's three routes out of the ambiguity are exactly the choices later P-ADO writing must make explicit: estimate attenuation coefficients, add independent polarization/conversion information, or impose a one-parameter substate-population form.

Zobel 1983 adds the experimental context: alignment changes with projectile, energy, and feeding balance, and angular-distribution/polarization constraints should be kept condition-consistent.

Ekstrom 1979 sharpens that caution in a more operational way. It says directly that angular distributions by themselves do not settle spin/parity or `delta` unless alignment is otherwise constrained, and it attaches an explicit uncertainty prescription to model-predicted alignment. It also contributes two distinct boundaries that should not be merged: the simple Gaussian family can be too restrictive, and direct-population alignment estimates can become unreliable once relevant particle-emission thresholds and unmodeled gamma feeding become important.

Ionescu 1981 provides the clearest feeding-aware bridge in this project. It shows a workflow in which pure-E2 transitions are first used to test and calibrate the population model, after which mixed transitions are analyzed for `delta` within the resulting width range.

Chiara 2012, Summary 2013, and Gray 2020 together supply the practice/background/boundary layer: assumed normalized widths exist in spectroscopy language, but they are heuristic, conditional, and not universally transferable.

## Evidence Gaps

- Need mapping from the user's actual P-ADO implementation to source symbols before writing final equations.
- Need source-level check of whether later P-ADO notation uses `sigma/I`, `sigma/J`, or another normalized width convention; Lauritsen 2025 gives `sigma/J`, but user-code mapping remains open.
- Need decide how, or whether, Cejnar-style reaction-route deorientation calculations can be approximated for the user's actual reaction and detector conditions.
- Need map whether any Radeck-style time-dependent deorientation or detector `Qk` correction exists in the user's P-ADO code path.
- Need user-data-specific check of reaction, beam energy, target, detector geometry, feeding pattern, and polarization/ADO acquisition conditions.
- Need determine whether the user's analysis has Chiara-like calibration transitions that could test an assumed alignment-width parameter empirically.
- Need determine whether the user's data contain pure-E2 calibration transitions that could support an Ionescu-style population-model constraint before mixed-transition fitting.
- Need assess whether any Ekstrom-style alignment uncertainty budget or Ionescu-style discrete-feeding term can be approximated realistically for the user's reaction and observed feeding pattern.
- Need check whether isomeric feeding or delayed components could make Gray-style amplitude/alignment cautions relevant to the user's data.
- Need stronger direct evidence, if available, before promoting the current low-spin caution into a universal low-spin `sigma/I` statement.
- Day28 added [[pado-shared-alignment-null-profile]]: a real [[zobel-1983-energy-projectile-alignment]] table-level profile rejects the single shared `sigma/J` null across projectile/energy conditions at quoted errors, while leaving condition-specific and feeding-aware P-ADO models open; the feeding-aware companion remains [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]].
- Need map more explicitly how ICC, DCO and polarization constraints would be combined in the user's actual P-ADO or in-beam analysis path, rather than treating them as interchangeable generic diagnostics.

## Writing-Support Synthesis Status

[[sigma-over-i-assumptions-and-mixing-ratio-extraction]] is now the bounded writing-support synthesis for this project. It should be used for NST / thesis motivation only after human review of terminology mapping and claims-ready / claims-not-ready boundaries.

## Claims Not Yet Ready for Paper Evidence Gate

| Candidate | Why not ready |
|---|---|
| `sigma/I` must always be fitted rather than fixed | Current source supports model dependence but does not evaluate all practical P-ADO cases. |
| A universal prior range for `sigma/I` | No source in this project has yet established a transferable numerical range. |
| Draper Gaussian `sigma` equals P-ADO `sigma/I` | Explicitly not ready; symbol mapping remains unresolved. |
| Summary 2013 typical `sigma/I = 0.3` can be used as a default `sigma/I` value | Not ready; the guide gives a heuristic assignment-context value, not a validated universal P-ADO default. |
| The literature already proves a universal low-spin growth of `sigma/I` uncertainty | Not ready; the present 11-source set only supports indirect caution, not a universal low-spin law. |
| Gray 2020 proves that empirical alignment widths should be replaced by `sigma/I ≈ 0.9` | Not ready; that inference is host-specific, isomer-specific, and conditional on the full-field assumption. |

## Risks and Blockers

- Source symbols are not identical; `sigma`, `sigma/I`, attenuation coefficients, `alpha2/alpha4`, and feeding fractions must remain separated.
- Rusev-style polarization asymmetry, in-beam clover Compton asymmetry, DCO ratios and ICC constraints are complementary but not interchangeable observables.
- Summary 2013, Chiara 2012, Gray 2020, and Radeck 2012 should not be promoted into universal P-ADO priors.
- A single DCO or asymmetry value can still leave branch ambiguity; these new method sources should not be rewritten as "one observable proves `delta`."
- The present low-spin caution is partly an indirect project inference; it is not yet a universal source-backed rule.
- User data conditions and P-ADO implementation details are not yet mapped to the source notation.

## Next Actions

1. Human-review the synthesis-level terminology mapping and paper-evidence-gate boundaries.
2. Map the actual P-ADO code/input convention for `sigma/I` to the source-level variables.
3. Check whether the user's data include pure-E2 calibration transitions and a reconstructible feeding history that would support an Ionescu-style constraint on the population model.
4. Decide whether the user's analysis path could realistically incorporate ICC-based or polarization-based external constraints, and if so, which observable definitions match the actual experiment.
5. Add user-data-specific reaction, detector, and feeding-condition records before turning the project into code-facing or manuscript-facing text.

## Related Pages

- [[magnetic-substate-population]]
- [[side-feeding]]
- [[deorientation]]
- [[sigma-over-i]]
- [[angular-distribution]]
- [[angular-distribution-coefficient]]
- [[multipole-mixing-ratio]]
