---
type: synthesis
title: "Shape-sensitive observables and claim boundaries"
aliases: [shape-observable-matrix, 形状观测量判据矩阵]
created: 2026-10-03
updated: 2026-10-03
status: ai-draft
review_status: unreviewed
scope: quadrupole-gamma-octupole-shape-coexistence
confidence: medium
sources: [davidson-1965-rotations-vibrations-deformed-nuclei, heyde-wood-2011-shape-coexistence-review, zamfir-casten-1991-gamma-softness-triaxiality, ionescu-bujor-1998-static-moments-129-131ce, petrache-1998-highly-deformed-lifetimes-131ce-nd, ensdf-2006-131ce-levels, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, nomura-2018-odd-mass-ba-octupole, gaffney-2013-pear-shaped-rn-ra, liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, guo-2020-pseudospin-chiral-quartet-131ba]
tags: [shape-observables, gamma-softness, shape-coexistence, octupole, evidence-matrix]
---

# Shape-sensitive observables and claim boundaries

## Question and Scope

This matrix maps measured or derived observables to the narrowest shape claim they can support. It covers quadrupole deformation, gamma softness versus localization, octupole collectivity, and shape coexistence. Model deformation coordinates and potential-energy minima remain model results, not measured transition matrix elements or moments.

## Shape coordinates recalled before source review

In a multipole surface description, beta-two sets the quadrupole-deformation amplitude, while gamma specifies the orientation within the quadrupole shape family under a stated convention. Beta-three is the leading octupole coordinate and changes sign under spatial reflection. A nonzero or soft beta-three degree of freedom can produce octupole correlations without a sharply localized static reflection-asymmetric minimum.

Gamma-softness means that the collective potential and wave function extend appreciably along gamma. Gamma-rigidity means localization around a non-axial gamma value, a stronger statement. Shape coexistence refers to distinct low-lying structures with different quadrupole or electromagnetic properties in the same nucleus. A single band, fitted gamma value, or model minimum does not establish it.

## Evidence Matrix

| Question | Supporting evidence | Limitation and alternative | Current decision |
|---|---|---|---|
| What does gamma staggering identify? | ZC91-1/ZC91-2 compare ideal gamma-unstable and Davydov limits. | ZC91-4 shows sensitivity to weak gamma dependence; only low-spin even-even scope transfers directly. | Use as one diagnostic, not a unique rigidity measurement. |
| What establishes 131Ce shape multiplicity? | IB98-2 measures a state-specific isomer moment; PE98-7 reports high-deformation Q0, and ENS06-2 maps this result to Band A/SD-1. ENS06-4 lists SD2→SD1 links. | Qs and Q0 are not like-for-like. The evaluation does not map either SD band to Alwaleedi Bands 1–7. | PE98→SD1 identity is resolved; normal-SD relation and coexistence interpretation remain open. |
| Does A≈130 have direct E1-link evidence for octupole correlations? | GU20-10 reports eight E1 links from 131Ba D7 to D3-D6. | The E1 links are direct; octupole correlations are the authors' interpretation. GU20-14 gives beta-three only as tentative RAT-PRM input; GU20-16 records no lifetimes or absolute reduced probabilities, and no direct B(E3) or static beta-three is measured here. | A≈130 has a target-region E1 network; it does not establish static octupole deformation or transfer to 131Ce. |
| Does a small E1 moment mean weak octupole collectivity? | BU16-1 and EXT146-1 report direct B(E3) values with equal 48-W.u. central values in 144Ba and 146Ba; EXT146-2 records a much smaller E1 moment in 146Ba. | The E3 uncertainties are large and asymmetric; both studies share GOSIA/CHICO2/GRETINA methods, while covariance is unavailable. The occupancy explanation for E1 variation is a model result. | Use E3 as the collectivity observable and treat E1 variation as a separate quantity; retain dynamic-versus-static limits from GA13-2 and GA13-6. |
| Does a large E3/Q3 settle static versus dynamic octupole shape? | GA13-3 gives Q3 systematics across spin; GA13-2 compares 220Rn and 224Ra. | GA13-6 states that the E2/E3 matrix elements do not distinguish a projected quadrupole-octupole shape from an octupole vibration of a quadrupole shape. | Add parity-band energy systematics, E1/E3 branching and model shape reconstruction; keep the shape label at author/model level. |
| What does an odd-mass near-neutron-rich Ba model imply? | NOM18-2 predicts beta-three-soft nonzero minima in 144Ba/146Ba cores; NOM18-3/NOM18-4 make the odd-A result state-dependent, with E3-rich higher states in 145Ba. | DD-PC1 surfaces are axial; sdf-IBFM boson-fermion strengths are fitted, and the 147Ba ground-state spin is not reproduced without an unjustified occupation change. These are model outputs for N=87–91, not 131Ce measurements. | Use as a model-transfer boundary: enhanced even-core B(E3) need not put octupole character into every odd-A low-lying state. |

## Observable-to-claim matrix

| Observable | Narrow claim it can support | What it cannot establish alone | Necessary companions and conditions |
|---|---|---|---|
| Gamma-band energy staggering | For low-spin even-even nuclei, correctly assigned gamma-band energies can distinguish ideal gamma-unstable and fixed-gamma rotor limits. Zamfir–Casten define S(J,J−1,J−2) and show opposite limiting phases. | One staggering value does not uniquely measure gamma stiffness. Weak gamma dependence, band mixing, and level misassignment can move the indicator. Do not transfer the even-even low-spin rule directly to an odd-A high-spin band. | Several consecutive levels, secure spin assignments, stated definition and convention, plus E2 matrix elements or a model comparison that allows gamma fluctuations. |
| Absolute B(E2) values | A lifetime, branching, and multipolarity analysis can constrain a state-to-state quadrupole transition strength and its collectivity. | One B(E2), or one branching-derived ratio, does not uniquely determine beta-two, gamma localization, or shape coexistence. Intrinsic Q0 conversions add rotor and axiality assumptions. | Relevant in-band and interband E2 matrix elements, lifetimes and feeding treatment, and where available quadrupole invariants or radii. |
| Spectroscopic static quadrupole moment Qs | A calibrated moment constrains the quadrupole distribution of the specific measured state and can test a state-specific configuration or rotor calculation. | Qs is not the intrinsic Q0 of a rotational band. Moments from different spins or experiments are not like-for-like; one state does not establish neighboring-band shapes. | Spin/parity and sign convention, calibration, state identity, and a consistent model or a set of moments and transition matrix elements across compared states. |
| Interband transition connections | A resolved transition establishes a level-scheme connection; branching and multipolarity can constrain how structures communicate. | A drawn link or energy coincidence alone does not establish configuration mixing, a common intrinsic shape, or shape coexistence. | Secure level identities and multipolarity, absolute strengths or mixing ratios, and a crosswalk of band labels across experiments. |
| Low-lying 0+ states, E0 strength, and charge radii | Their combined pattern can support competing configurations with different mean-square charge radii and quadrupole structures. E0 strength is a sensitive mixing indicator in a specified two-configuration treatment. | An excited 0+ level or E0 transition alone does not uniquely identify two shapes; pairing, vibration, intruder configurations, and mixing can contribute. | E0 plus state-specific E2 strengths or moments, radii or isotope shifts, configuration-sensitive spectroscopy, and symmetry restoration/configuration mixing in quantitative calculations. |
| E3 matrix elements or B(E3) | Coulomb-excitation E3 strength directly establishes octupole transition collectivity; Q3 and beta-three can be inferred with stated geometry assumptions. | Enhanced E3 alone does not decide whether octupole motion is dynamic/soft or a stable static reflection-asymmetric shape. Beta-three conversion is model-dependent. | Opposite-parity level sequences, E1 links or moments, energy displacement and branching, spin dependence, and dynamic-versus-static model comparison with uncertainties. |
| Calculated beta-two/gamma/beta-three minima | A stated model and parameter set can generate candidate shapes, softness, or configuration-mixing patterns to compare with data. | A minimum or fitted deformation is not an experimental shape measurement and does not independently confirm a collective-mode assignment. | Model space, interactions, parameter sensitivity and covariance, then tests against state-resolved moments and transition strengths. |

The gamma staggering formula and ideal-limit values are in [[zamfir-casten-1991-gamma-softness-triaxiality]] ZC91-2. Its limited transfer range and sensitivity to weak gamma dependence are in ZC91-4. The coexistence companion set is summarized in [[heyde-wood-2011-shape-coexistence-review]] HW11-1/HW11-3; the separation of collective-model observables from shape images is stated in [[davidson-1965-rotations-vibrations-deformed-nuclei]] DV65-1.

## Synthesis

No single energy ratio, transition strength, moment, band connection, or calculated minimum uniquely maps to a shape label. Claims become stronger when state identity is secure and several state-resolved observables agree under compatible conventions. The gamma, coexistence, and octupole questions require different companion sets; they should not be collapsed into one generic deformation score.

## Worked A≈130 comparison: 131Ce

Two shape-sensitive results exist for 131Ce, but they constrain different states with different observables.

| Evidence | Direct or derived result | Boundary |
|---|---|---|
| Ionescu-Bujor et al. TDPAD | For the 9− isomer, measured g = −0.189(7) and absolute quadrupole-moment magnitude |Q| = 0.92(10) eb; see [[ionescu-bujor-1998-static-moments-129-131ce]] IB98-2. | Fitted epsilon-two and gamma are particle-plus-triaxial-rotor outputs, not direct measurements; see IB98-3. This is one state, not a survey of Bands 1–7. |
| Petrache et al. DSAM | The high-deformation yrast band gives Q0 = 7.3(4) eb; beta-two = 0.38(2) is quoted under an axial conversion; see [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-7/PE98-12. | ENS06-2 later identifies the 1998Pe01 result with evaluated SD-1. ENS06-4 adds links to SD-2. Neither the original paper nor these SD subfiles maps the sequence to Alwaleedi normal-deformed Bands 1–7. |

The TDPAD isomer and Petrache DSAM remain different experiments and observables; their Qs and Q0 values are not like-for-like. ENSDF resolves one additional edge: the Petrache Q0 result is SD-1, and the evaluation lists two SD2→SD1 transitions. It does not connect either SD band to Alwaleedi Bands 1–7. The evidence gap is narrower: PE98→SD-1 and SD1↔SD2 are mapped; the normal-SD relation remains unresolved. ENSDF is a compilation of upstream measurements, not an independent experiment.

## Octupole cross-region check

Bucher et al. report a 0+ to 3− E3 matrix element for 144Ba and B(E3; 3− to 0+) = 48(+25/−34) W.u. from sub-barrier Coulomb excitation; yields and contaminant controls are described in [[bucher-2016-144ba-direct-octupole]] BU16-1/BU16-3. The inferred Q3 and beta-three retain rotor, E1/E3-sign, and higher-multipole assumptions (BU16-2). This is direct evidence for strong octupole collectivity, with a more conditional inference about static shape.

Nomura et al. 2018 provide a theoretical state-dependence control for the neutron-rich Ba region. DD-PC1 axial surfaces give soft nonzero beta-three minima in 144Ba and 146Ba cores, but the fitted sdf-IBFM assigns most low-lying states in 143,145,147Ba to sd configurations; in 145Ba, octupole character instead appears in selected higher states with predicted E3 branches. The 147Ba ground-spin mismatch and an unaccepted 25% occupation adjustment limit the model. These predictions support an excitation- and orbital-dependent octupole interpretation, not an A≈130 experimental assignment ([[nomura-2018-odd-mass-ba-octupole]] NOM18-1/NOM18-3/NOM18-4/NOM18-5).

A separate Coulomb-excitation run on 146Ba reports B(E3; 3−→0+) = 48(+21/−29) W.u. ( [[bucher-2017-146ba-direct-octupole]] EXT146-1). Its central value equals the 144Ba central value, while the 2017 paper reports an E1 moment over an order of magnitude smaller than in 144Ba (EXT146-2). The authors use SCCM/GCM to explain the E1 change through neutron-orbital occupancy (EXT146-3); that is not a direct measurement of the microscopic cancellation mechanism.

Gaffney et al. compare direct Coulomb-excitation matrix elements in 220Rn and 224Ra. Their data support weaker, more vibration-like octupole motion in 220Rn and stronger, more coherent, static-like collectivity in 224Ra; shape labels remain author/model interpretation. See [[gaffney-2013-pear-shaped-rn-ra]] GA13-1/GA13-2 and spin dependence in GA13-3. Table 2 gives fitted/derived Q3=2180(130) and 2520(90) e fm³; the ratio Ra/Rn is 1.16(8) under independent-error propagation, a modest difference rather than an order-of-magnitude separation. More importantly, the authors state that the measured E2/E3 matrix elements alone do not distinguish a projected quadrupole-octupole shape from octupole vibration (GA13-6); their static-like interpretation also uses shape reconstruction and systematics. In 78Br, opposite-parity E1 links are direct, while octupole-correlation and octupole-soft interpretations combine ratios, energy displacement, and a model beta-two–beta-three potential; see [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] L16-9/L16-11/L16-13. The A≈130 evidence is not empty: Guo et al. report eight E1 links from 131Ba D7 into positive-parity D3-D6 (GU20-10). The authors interpret them as octupole correlations across configurations, but beta-three=0.05 is a tentative RAT-PRM input and absolute E3/lifetimes are absent (GU20-11/GU20-14/GU20-16). This is direct target-region E1 connectivity, not a static-shape measurement or a 131Ce result.

## Counter-evidence

- Gamma staggering can change under weak gamma dependence, mixing, or uncertain level assignments.
- A low-lying 0+ state, E0 strength, or B(E2) change can also reflect pairing, vibration, intruder configurations, or configuration mixing.
- Strong E3 transitions can occur with dynamic octupole motion; the 220Rn/224Ra comparison shows why spin dependence and the rest of the E1/E2/E3 matrix matter.
- A model PES with multiple minima is not itself evidence that distinct laboratory states have been observed.

## Minimum discriminating sets

- For gamma-soft versus gamma-rigid: a run of gamma-band energies with secure assignments, transition-level E2 strengths or moments, and a calculation that allows gamma fluctuations and reports sensitivity to the potential.
- For shape coexistence: identify two state families in the same isotope, measure state-resolved E0/E2 strengths or moments and radii where possible, then close the interband identity/mixing map. A lone low-lying 0+ state or model PES is insufficient.
- For static octupole deformation versus soft correlations: combine E3 strength and covariance with opposite-parity sequences, E1 links/branching or energy displacement, and dynamic and static shape calculations. Keep B(E3), fitted Q3, and inferred beta-three as separate evidence layers.
- For 131Ce, the next useful datum is a verified level-and-transition crosswalk between the TDPAD isomer, normal-deformed sequences, and DSAM high-deformation band. Do not compare Qs and Q0 numerically or upgrade the coexistence label before that.

## Model Dependence

The gamma-soft/gamma-rigid staggering endpoints are model limits, not direct gamma coordinates. Converting E2 strengths or static moments to beta-two, gamma, or intrinsic Q0 requires a stated rotor, axiality, operator, and state-mixing treatment. Converting the 144Ba E3 element to beta-three uses an assumed beta-two and geometry; the measured E3 matrix element remains the more direct quantity. PTR and other mean-field parameters should be recorded as model outputs with sensitivity, not as measured shapes.

## Limitations and Missing Evidence

The synthesis does not reanalyse the raw TDPAD, DSAM, or Coulomb-excitation data. The 131Ce transition-level crosswalk and common state-resolved E2/E0 matrix are absent. GOSIA event yields, fit covariance, response and input files are not available here, so the reported 144Ba fit is not reproducible as an L4 analysis. A≈130 target-region E1 links are available in 131Ba, but this source provides no direct E3 strength, lifetime, or measured beta-three; the 131Ce question remains nucleus-specific. Cross-region cases calibrate interpretation only.

## Sources

- [[davidson-1965-rotations-vibrations-deformed-nuclei]] — DV65-1.
- [[heyde-wood-2011-shape-coexistence-review]] — HW11-1, HW11-3, HW11-4.
- [[zamfir-casten-1991-gamma-softness-triaxiality]] — ZC91-1, ZC91-2, ZC91-4.
- [[ionescu-bujor-1998-static-moments-129-131ce]] — IB98-2, IB98-3.
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] — PE98-7, PE98-12, PE98-13.
- [[ensdf-2006-131ce-levels]] — ENS06-1 through ENS06-6; evaluated band crosswalk and scope limits.
- [[bucher-2016-144ba-direct-octupole]] — BU16-1, BU16-2, BU16-3.
- [[bucher-2017-146ba-direct-octupole]] — EXT146-1, EXT146-2, EXT146-3.
- [[nomura-2018-odd-mass-ba-octupole]] — NOM18-1 through NOM18-6; state-dependent model predictions and transfer limits.
- [[gaffney-2013-pear-shaped-rn-ra]] — GA13-1, GA13-2, GA13-3.
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] — L16-9, L16-11, L16-13.
- [[guo-2020-pseudospin-chiral-quartet-131ba]] — GU20-10, GU20-11, GU20-14, GU20-16.

## Source independence and review state

Davidson 1965 and Heyde–Wood 2011 are reviews/frameworks, not independent experiments. Zamfir–Casten 1991 is a model comparison, not a new spectrum. The 131Ce TDPAD and DSAM campaigns use different reactions and data, while sharing some collaborators. Bucher 144Ba and 146Ba are separate isotope runs but share collaborators and GOSIA/CHICO2/GRETINA methods; their fit systematics are therefore not fully independent. Nomura 2018 is a fitted CDFT/IBFM calculation by the same group as the 2017 odd-mass gamma-soft work, not an independent experiment or an independent model family. Gaffney 220Rn/224Ra, 78Br, and Guo 131Ba are separate acquisition lineages; the latter E1 transitions remain an author-interpreted octupole-correlation handle.
The Guo paper also retains quartet-identity and absolute-strength limitations. Existing review metadata and claim-level needs_review states are unchanged; this synthesis is an AI-draft and is not human-reviewed.
