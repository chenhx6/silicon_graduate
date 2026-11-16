---
type: synthesis
title: "Sigma-over-I assumptions and P-ADO mixing-ratio extraction"
aliases: [sigma-over-I assumptions synthesis, sigma/I writing-support synthesis, P-ADO mixing-ratio extraction synthesis]
created: 2026-07-10
updated: 2026-11-16
status: ai-draft
review_status: human-reviewed
scope: sigma-over-i-pado-writing-support
confidence: medium
high_confirmed_by:
high_confirmed_date:
sources: [draper-1970-gaussian-substate-side-feeding, ekstrom-1979-spin-alignment-attenuation-a61-a67, zobel-1980-magnetic-substate-distributions, ionescu-1981-improved-angular-distribution-analysis-particle-xn, zobel-1983-energy-projectile-alignment, cejnar-1996-spin-deorientation-alpha-2n-gamma, radeck-2012-deorientation-lifetime-98ru-rdds, chiara-2012-cu65-cu67-core-coupled-protons, summary-2013-bases-spin-parity-assignments, gray-2020-hyperfine-fields-g-factor-measurements, lauritsen-2025-gamma-angular-formalism-tracking-arrays, chen-2026-pdm-probability-density-mapping]
tags: [sigma-over-i, pado, mixing-ratio, angular-distribution, writing-support, evidence-matrix]
---

# Sigma-over-I Assumptions and P-ADO Mixing-Ratio Extraction

## Active Summary for Agents

- This is a bounded writing-support synthesis built from 11 human-reviewed source notes plus the sigma-over-I project evidence map, and the current wording round has now passed user review.
- The source set is sufficient for NST / thesis introduction-level motivation about alignment-population uncertainty, but not yet for user-code-facing equations or a universal numerical `sigma/I` prior.
- Keep `sigma`, `sigma/I`, `sigma/J`, `alpha2/alpha4`, `alpha_k`, `rho2/rho4`, attenuation coefficients, `U_k`, `G_k`, `Q_k`, and TDPAD `R(t)` amplitude distinct.
- High-risk boundary sources are [[summary-2013-bases-spin-parity-assignments]], [[chiara-2012-cu65-cu67-core-coupled-protons]], [[gray-2020-hyperfine-fields-g-factor-measurements]], and [[radeck-2012-deorientation-lifetime-98ru-rdds]]: they are useful background or boundary cases, not universal P-ADO priors.

## Question and Scope

What can the current 11-source evidence base safely support about alignment-population assumptions in P-ADO-style mixing-ratio extraction, and where do the remaining notation, feeding-model, reaction-condition, and low-spin-boundary gaps still block stronger paper claims?

### Scope and Limits

- This page is for writing support, not for replacing source notes or drafting manuscript paragraphs.
- The target use is NST introduction / method motivation and later thesis introduction / method framing.
- The synthesis supports bounded statements about model dependence, notation mapping, and condition dependence.
- The synthesis does not establish a universal `sigma/I` prior, does not validate the user's code convention, and does not convert old alignment papers into direct P-ADO antecedents.

## Evidence Matrix

| Theme | Safe support in current source set | Main source anchors | Main boundary |
|---|---|---|---|
| Gaussian substate formalism | Gaussian widths are model parameters tied to magnetic-substate population descriptions, not neutral constants | DR70-3; L25-5 to L25-9 | Do not equate Draper `sigma`, Lauritsen `sigma/J`, and user-code `sigma/I` without mapping |
| Alignment attenuation / CNR prediction | Angular distributions alone underconstrain alignment and `delta`; model-predicted alignment needs uncertainty treatment | Z80-2 to Z80-4; EK79-2 to EK79-6 | Ekstrom `alpha2/alpha4` and Zobel attenuation coefficients are not Gaussian widths |
| Gaussian-limitation / feeding-aware evidence | Simple global Gaussian assumptions can fail; pure-E2 transitions can calibrate a better population model before mixed-transition fitting | EK79-7 to EK79-9; IO81-3 to IO81-9 | This is conditional failure evidence, not a universal anti-Gaussian theorem |
| Reaction / feeding / deorientation dependence | Alignment-sensitive quantities vary with projectile, beam energy, feeding, and attenuation treatment | Z83-5 to Z83-10; C96-4 to C96-10; R12-7 to R12-10 | Radeck is related method background, not direct fusion-evaporation `sigma/I` prior evidence |
| Experimental practice / heuristic defaults | Assumed or typical `sigma/I` values appear in practice, but they are heuristics or calibration choices | CH12-3 to CH12-5; SB13-2 to SB13-4; G20-4 to G20-8 | Practice-level defaults are not universal priors |
| Low-spin caution | The current source set justifies caution about transplanting fixed-width heuristics into low-spin use, but only indirectly | DR70-3; IO81-3 to IO81-9; CH12-3 to CH12-5; SB13-2 to SB13-4; L25-7 to L25-9 | The current 11-source package does not yet prove a universal low-spin law for `sigma/I` |

## Synthesis

### Terminology and Symbol Mapping

| Symbol or term | Source anchor | Safe synthesis wording | Unsafe shortcut |
|---|---|---|---|
| `sigma` in Draper 1970 | DR70-3 | Gaussian width of side-feeding magnetic-substate population | "the same thing as user-code `sigma/I`" |
| attenuation coefficients in Zobel 1980/1983 | Z80-1; Z83-1 | alignment attenuation descriptors inferred from angular-distribution analysis | "the Gaussian width itself" |
| `alpha2`, `alpha4` in Ekstrom 1979 | EK79-1 to EK79-5 | spin-alignment attenuation factors reduced from pure-E2 data | "normalized `sigma/I`" |
| `rho2`, `rho4` in Ionescu 1981 | IO81-3 to IO81-5 | statistical-tensor factors used to test a population model with pure-E2 transitions | "Ekstrom-style attenuation factors" |
| `sigma` in Ionescu 1981 | IO81-5 to IO81-9 | width of the Gaussian side-feeding component only | "the total population width of the level" |
| `U_k` in Cejnar 1996 | C96-4 to C96-5 | deorientation-flow factor along reaction routes | "the fitted P-ADO `sigma/I`" |
| `G_k(d)` in Radeck 2012 | R12-7 to R12-10 | time-dependent deorientation attenuation in RDDS angular correlations | "fusion-evaporation side-feeding width" |
| `Q_k` in Radeck 2012 | R12-7 | detector finite-solid-angle factor | "nuclear alignment attenuation" |
| `alpha_k(J)` in Lauritsen 2025 | L25-5 to L25-8 | nuclear alignment/deorientation attenuation in the in-beam angular-distribution formula | "always detector attenuation" |
| `sigma/J` in Lauritsen 2025 | L25-7 to L25-9 | normalized Gaussian width attached to `Pm(J)` | "automatically identical to the user's `sigma/I`" |
| `sigma/I = 0.3` in Summary 2013 | SB13-2 to SB13-4 | guide-level high-spin heuristic | "validated universal default" |
| `sigma/I ≈ 0.35` in Gray 2020 | G20-4 to G20-8 | empirical prompt-decay expectation imported into a TDPAD boundary discussion | "directly measured universal truth" |

### Gaussian Substate Formalism

[[draper-1970-gaussian-substate-side-feeding]] provides the oldest formal baseline in this source set. Even for stretched-E2 transitions, the observable `A2/A4` response depends on spin, side-feeding intensity, and the assumed form of the magnetic-substate population. The key methodological lesson is not "Gaussian is correct," but that a Gaussian width is already a model reduction of a more complicated population problem.

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] provides the modern notation bridge. In its in-beam angular-distribution chain, `delta` enters `Amax_k`, the state population enters through `Pm(J)`, and `Pm(J)` is usually parameterized by Gaussian `sigma/J`. This is the cleanest current source-level bridge from population assumptions to the curvature actually fitted in angular-distribution work.

### Alignment Attenuation and CNR Prediction Evidence

[[zobel-1980-magnetic-substate-distributions]] makes the central underconstraint explicit: two angular-distribution coefficients do not determine alignment and `delta` simultaneously unless extra information or a model is supplied. The paper's three escape routes are model-estimated attenuation coefficients, complementary observables such as polarization or conversion, or a one-parameter magnetic-substate distribution.

[[ekstrom-1979-spin-alignment-attenuation-a61-a67]] adds a stronger operational warning. It treats alignment prediction as a model output with its own uncertainty budget, not as a silent constant. Its specific prescription `Delta alpha2^MANDY = max{0.15 alpha2^MANDY, 0.04}` and its warning about faulty spin/parity or `delta` assignments are directly useful for writing bounded cautionary statements.

## Counter-evidence

The present 11-source package does not justify a universal statement that `sigma/I` must vary strongly in every low-spin case. It justifies a narrower caution:

- many practical `sigma/I` defaults are imported from high-spin guide or calibration language rather than from low-spin calibration papers;
- low-spin sensitivity is supported mainly indirectly, through formalism, feeding dependence, and selected case studies;
- no source in the current set establishes one universal low-spin numerical prior or one universal low-spin variation law.

## Gaussian-Substate Hypothesis Limitations

The current source set does not support a universal anti-Gaussian statement. It supports a narrower conclusion: a single simple Gaussian may be too restrictive, and when it is used it must be justified case by case.

[[ekstrom-1979-spin-alignment-attenuation-a61-a67]] contributes two distinct limitations that should not be merged. First, a simple Gaussian family is too restrictive for its compiled `A = 61-67` `alpha2/alpha4` data. Second, direct-population alignment estimates become unreliable when the reaction energy lies sufficiently above the relevant particle-emission threshold and unmodeled gamma feeding is appreciable. The familiar `E ≳ 2 MeV` wording belongs only to the Fig.5 `62Ni(alpha,n)65Zn` example, while `(alpha,p)` cases sit effectively `2-3 MeV` lower because of the proton Coulomb barrier.

[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] shows a different failure mode: a global Gaussian hypothesis does not describe the `167Tm` pure-E2 dataset well enough. [[zobel-1980-magnetic-substate-distributions]] and [[zobel-1983-energy-projectile-alignment]] frame the boundary conditions under which Gaussian-like assumptions may still be practical.

### Feeding-Aware Population Models

[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] is the clearest source-level template for this section. It first uses pure-E2 transitions to test the population model through `rho2/rho4`, then replaces a global Gaussian with a model that combines Gaussian side feeding and discrete direct feeding, and only after that fits mixed transitions for `delta`.

[[draper-1970-gaussian-substate-side-feeding]] and [[cejnar-1996-spin-deorientation-alpha-2n-gamma]] support the same broader lesson from different directions: feeding history matters, and the width parameter being fitted or calculated usually describes only one component of the population problem. A synthesis statement can therefore say that feeding-aware modeling is a demonstrated option, not a universal requirement for every reaction.

### Fusion-Evaporation Alignment and Projectile / Energy / Feeding Dependence

[[zobel-1983-energy-projectile-alignment]] is the cleanest experimental anchor for condition dependence. In `67Ga`, alignment attenuation varies with projectile, beam energy, and the balance between direct and cascade feeding. This is strong evidence against transferring one fixed alignment-width assumption between unlike conditions without explicit justification.

[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] strengthens the reaction-specific side of this argument by showing how side-feeding width estimates can depend on route-by-route deorientation calculations. Together these sources support a bounded introduction-level statement that alignment assumptions are reaction- and feeding-history dependent.

### Deorientation / Attenuation Evidence

[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] shows how deorientation enters the reaction-route calculation and how a wrong `sigma` interval can alter the `delta` inference for a mixed transition. [[radeck-2012-deorientation-lifetime-98ru-rdds]] adds a different but useful methodology lesson: attenuation may be time dependent and must be separated from detector solid-angle terms such as `Qk`.

The safe synthesis boundary is that deorientation belongs in the same family of population / attenuation assumptions that affect inferred observables, but Cejnar and Radeck are not interchangeable and Radeck is not direct fusion-evaporation `sigma/I` evidence.

### Experimental-Practice Evidence

[[chiara-2012-cu65-cu67-core-coupled-protons]] is the strongest practice-level example in the set. It shows that an assumed `sigma/I` may be chosen because it reproduces known transitions, and that a different assumed value shifts the fitted `delta` for a specific transition.

[[summary-2013-bases-spin-parity-assignments]] does not strengthen the theory base, but it documents how a typical orientation parameter enters high-spin assignment heuristics. This is useful because it shows that fixed-width assumptions exist in everyday spectroscopy language, even when they are only heuristic.

### Empirical Alignment Expectation and Failure Examples

[[gray-2020-hyperfine-fields-g-factor-measurements]] supplies the most useful failure-style boundary case. It shows that an empirical alignment expectation such as `sigma/I ≈ 0.35` can fail in an isomeric TDPAD context, and that a reduced amplitude does not uniquely diagnose weaker alignment rather than a different field-free fraction.

The safe synthesis use of Gray 2020 is therefore negative and methodological: empirical defaults can fail, and an amplitude-like observable can compress more than one physical uncertainty into the same reduced signal.

## Model Dependence

The current source set supports a strong model-dependence claim, but not a universal low-spin law. For low-spin caution in particular:

- Lauritsen's normalized `sigma/J` language shows why raw width and spin-scaled width must be separated.
- Draper and Ionescu show that discrete substate structure and feeding details can matter before one reaches a broad high-spin heuristic regime.
- Summary 2013 shows that the familiar `sigma/I = 0.3` language is explicitly high-spin guide practice, not direct low-spin calibration.

A separate user-analysis calibration note is stored on [[sigma-over-i]] and should not be promoted into source-backed synthesis wording.

## Implications for P-ADO Mixing-Ratio Extraction

- The current evidence base supports saying that P-ADO should expose the coupling between `delta` and alignment-population assumptions rather than hide those assumptions in one silent fixed width.
- The evidence base supports using pure-E2 or otherwise calibration-grade transitions, when available, to constrain a population model before trusting mixed-transition `delta` values.
- The evidence base supports warning that projectile, beam energy, feeding pattern, and deorientation treatment can change the relevant alignment descriptor.
- The evidence base supports caution about transplanting high-spin heuristic `sigma/I` values into low-spin use without explicit calibration.
- The evidence base does not yet support one universal numeric prior, one universal Gaussian prescription, or a direct equation-level mapping from all source notations to the user's code input.

## Writing Hooks for NST Introduction

- Angular-distribution fitting imports alignment information even when the paper only reports `delta`.
- A single preset `sigma/I` is a population-model assumption, not a neutral detector setting.
- Pure-E2 transitions can act as calibration transitions for the population model before mixed-transition inference.
- Experimental practice, review heuristics, and boundary-case methods all show that empirical defaults exist, but they are not universally transferable.

## Writing Hooks for Thesis Introduction / Method Motivation

- Distinguish magnetic-substate population, attenuation coefficients, and normalized width conventions before comparing papers.
- Treat feeding history as part of the observable model, not as invisible background.
- Use the older alignment and deorientation papers to motivate why a code-facing `sigma/I` parameter deserves explicit uncertainty treatment.
- Present P-ADO as a framework that can make hidden alignment assumptions inspectable.

## 2026-11-16: direct calibration, transfer, and empirical spin trends

The recovered user-designated 15-page PDM draft is locally available as `raw/writing/pado/20260723.pdf`, SHA-256 `f19b52b872432f6d615dae9350eef42d12cff27cfb621a041f09720699f74421`. Its Sec.II.D, PDF p.4, lines270–322 gives a more specific calibration argument than a generic statement that alignment depends on feeding. Source identity and reading scope are recorded in [[chen-2026-pdm-probability-density-mapping]] CH26-PDM-CAL-01–05.

| Calibration route | What is required or assumed | Why precise target-state σ/I can remain unavailable | Evidence and boundary |
|---|---|---|---|
| Matched reference | A known stretched E2 transition from the same initial state under identical coincidence selection as the mixed transition | A suitable E2 reference may have insufficient counts | CH26-PDM-CAL-02, PDF p.4 lines279–287. Author's prescription and practical limitation, not a measured count deficit for the current Au case. |
| Transfer from a proxy | Another gate or a stronger state with the same I is taken as a reasonable approximation | Feeding and event selection can reweight the ensemble; transfer bias need not be known | CH26-PDM-CAL-01/03, lines270–294. Draper1970/Cejnar1996/Zobel1983 give related feeding and reaction context, not a universal numerical transfer error. |
| Empirical σ/I(I) parametrization | Several strong E2 references constrain an assumed spin trend | Sparse calibration information and measurement errors propagate; smooth evolution is not a general dynamical theorem | CH26-PDM-CAL-04, lines295–305. Conditional empirical approximation, not a universal low-spin prior or a new spin law. |

These are calibration uncertainties **within a declared population model**. Whether one Gaussian width can reproduce all relevant angular moments is a separate adequacy question, addressed by Ionescu1981/Ekstrom1979. The `167Tm` example must not become the sole explanation of why σ/I is hard to calibrate in an unrelated experiment.

The practical implication is to propagate adopted-alignment uncertainty into δ while retaining the response model, domain and weighting assumptions (CH26-PDM-CAL-05). Same spin does not establish equal populations; different gates do not prove unequal populations. A precise matched calibration remains possible with suitable data and model checks. The draft's Gray2020 citation retains the host-specific TDPAD boundary already recorded above; it is not direct prompt-reaction σ/I calibration evidence.

## Claims Ready for Paper Evidence Gate

Ready here means the source basis, locator chain, and project boundary are already in place; human review of wording is still required before manuscript use.

| ID | Bounded claim | Source basis |
|---|---|---|
| SIO-SYN-1 | Angular distributions alone do not uniquely determine alignment and `delta`; extra model input or complementary observables are needed. | Z80-2 to Z80-4; EK79-2; L25-12 |
| SIO-SYN-2 | Alignment descriptors used in angular-distribution analysis are model- and condition-dependent rather than universal constants. | DR70-3; Z83-5 to Z83-9; EK79-5 to EK79-9 |
| SIO-SYN-3 | Pure-E2 transitions can be used to test or calibrate a population model before mixed-transition `delta` fitting. | EK79-1 to EK79-5; IO81-3 to IO81-8; L25-9 |
| SIO-SYN-4 | Projectile, beam energy, and feeding balance can change the relevant alignment attenuation in fusion-evaporation reactions. | Z83-5 to Z83-10 |
| SIO-SYN-5 | Practice-level assumed `sigma/I` values exist, but they should be cited as heuristics or calibration choices rather than universal priors. | CH12-3 to CH12-5; SB13-2 to SB13-4; G20-4 to G20-8 |

## Limitations and Missing Evidence

- Need mapping from the user's actual P-ADO implementation to source symbols before writing final equations.
- Need direct, source-backed low-spin studies if the project later wants to claim more than bounded caution about low-spin `sigma/I` use.
- Need determine whether the user's data contain pure-E2 calibration transitions that could support an Ionescu-style population-model constraint before mixed-transition fitting.
- Need determine whether reaction-specific feeding and deorientation information can be reconstructed well enough for code-facing use.

## Claims Not Ready for Paper Evidence Gate

| Candidate | Why not ready |
|---|---|
| One universal prior range for `sigma/I` in P-ADO fits | No source in the current set establishes a transferable numerical prior across reactions, feeding patterns, and methods. |
| Direct equality between Draper `sigma`, Lauritsen `sigma/J`, and user-code `sigma/I` | The notation mapping is related but still not source-backed one-to-one. |
| A code-facing prescription for the user's actual P-ADO implementation | The current synthesis does not yet map the user's detector geometry, fitting path, and parameter convention. |
| A universal rejection of Gaussian population models | The evidence supports conditional failure or over-restriction, not a theorem that Gaussian forms are always wrong. |
| A universal low-spin `sigma/I` law | The present source set supports indirect caution only, not a universal low-spin formula or prior. |
| Using Gray 2020 as a direct correction to prompt fusion-evaporation `delta` fits | Its host-specific TDPAD context is only a boundary example. |
| Using Radeck 2012 as direct primary evidence for prompt fusion-evaporation `sigma/I` | Its inverse-Coulomb-excitation RDDS context is method background, not direct prior evidence. |

## Human Review Priorities

- P0: terminology and symbol mapping. Check that `sigma`, `sigma/I`, `sigma/J`, `alpha2/alpha4`, `rho2/rho4`, attenuation coefficients, `U_k`, `G_k`, and `Q_k` remain separated and locally defined.
- P0: low-spin caution boundary. Check that the synthesis says "indirect caution" rather than claiming a universal low-spin law.
- P0: Ekstrom threshold wording. Check that the particle-emission-threshold phrasing and the Fig.5 / `(alpha,p)` boundary are preserved correctly.
- P0: implications for P-ADO mixing-ratio extraction. Check that the synthesis motivates explicit uncertainty handling without overstating what the sources prove.
- P0: claims ready / not ready for paper evidence gate. Check that guide, practice, review, theory, and experiment layers are not mixed.
- P1: writing hooks. Check that they are motivation hooks rather than disguised manuscript prose.

## Confidence Notes

The synthesis is medium confidence as a bounded writing-support framework because the source set is complete, human-reviewed, and internally cross-checking. Confidence remains below high because the user-code notation mapping, reaction-specific calibration strategy, low-spin-boundary wording, and paper-gate phrasing still require targeted human review.

## Sources

- [[draper-1970-gaussian-substate-side-feeding]]
- [[ekstrom-1979-spin-alignment-attenuation-a61-a67]]
- [[zobel-1980-magnetic-substate-distributions]]
- [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]]
- [[zobel-1983-energy-projectile-alignment]]
- [[cejnar-1996-spin-deorientation-alpha-2n-gamma]]
- [[radeck-2012-deorientation-lifetime-98ru-rdds]]
- [[chiara-2012-cu65-cu67-core-coupled-protons]]
- [[summary-2013-bases-spin-parity-assignments]]
- [[gray-2020-hyperfine-fields-g-factor-measurements]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- Project: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]
