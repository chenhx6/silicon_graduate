# Day27 independent RAT-PRM source audit

## Scope and status

Completed the bounded primary-source check of arXiv:1902.00191v1. All files created by this sidecar are inside `tmp/day27-rat2019-audit/`. No knowledge/source page, handoff, script, report outside this directory, run state, or Git state was changed. No Liu2016 full-text rereading or legacy potential-algebra work was performed.

This is a source-specific scientific self-audit, not human review, an experimental reanalysis, or a claim of manuscript admission. The source is available. An attempted nonexistent v2 returned HTTP 404; that does not affect the successful v1 retrieval.

## Verified identity, retrieval, and read coverage

- Actual title: *Multiple chiral doublet bands with octupole correlations in reflection-asymmetric triaxial particle rotor model*.
- Authors, in source order: Y. Y. Wang, S. Q. Zhang, P. W. Zhao, J. Meng.
- Identifier/version: arXiv:1902.00191v1 [nucl-th]; official abstract lists submission on February 1, 2019, and only v1. The downloaded PDF title page is internally dated February 4, 2019. These are distinct dates, not evidence of a v2.
- Related journal DOI, as listed in the official abstract metadata: `10.1016/j.physletb.2019.04.014`. The publisher article was not independently fetched or compared.
- Official abstract retrieval URL: `https://arxiv.org/abs/1902.00191`.
- Exact PDF retrieval URL: `https://arxiv.org/pdf/1902.00191v1`; response URL unchanged; HTTP content type `application/pdf`.
- Local PDF: `arxiv-1902.00191v1.pdf`, 340,748 bytes.
- PDF SHA-256: `cefe9aeb1fcf8be56c6808825faf95f486246254c231893320ee62f9a9907aae`.
- Abstract HTML SHA-256: `ad1a12c2ec6a7c7546875f32099c8303732ea436d0f74be40bb6e2a62a9c2f9d`.
- Recorded PDF retrieval clock: `2026-10-29T20:36:02.094687+00:00`. This is the executing clock stored in `retrieval.json`; the supplied environment context separately labels the current date as 2026-10-30.
- Coverage: all 17 PDF pages extracted and read. Mainline: title/abstract p. 1, Introduction pp. 2-3, Formalism pp. 3-6, Numerical Details pp. 6-7, Results and Discussion pp. 7-13, Summary pp. 13-14. References pp. 14-17 inspected for identity/dependency context, not independently verified.
- All five figures and captions visually inspected: Fig. 1 p. 7; Fig. 2 p. 9; Fig. 3 p. 10; Figs. 4 and 5 p. 11. Key equation pages 3-6 and Eq. (21) p. 12 visually checked against extracted text. Page images are retained in this directory.
- Locator convention throughout this report: printed page number equals the one-based PDF page number, including the numbered title page. No journal-page conversion is implied.

An initial unversioned browser preview incorrectly suggested a different title, length, and version. Direct official HTML metadata, the versioned PDF, and the official HTML full text at `https://arxiv.org/html/1902.00191v1` agree on the identity above. The preview was excluded from scientific evidence. The HTML rendering displays a regenerated date; the printed PDF and submission metadata govern the dates reported here.

## Five conclusions

1. **The reported nonzero octupole input is beta3 = 0.02, not a value above 0.1.** The baseline is beta2 = 0.28 and gamma = 16.3 degrees. Figure 2 compares gamma = 16.3 and 21.3 degrees. There is no reported beta3 scan, threshold at 0.1, or calculated chiral solution explicitly identified at beta3 > 0.1. Therefore this source supplies neither a quantitative counterexample to, nor evidence for, the OLD threshold claim. Locators: Sec. III, p. 6, first paragraph; Fig. 2 and caption, p. 9; full mainline pp. 1-14.

2. **At the model level, a fixed reflection-asymmetric intrinsic input and calculated chiral geometry can coexist.** With the above beta3, the authors identify chiral geometry for the negative-parity bands through proton, neutron, and rotor angular-momentum components. This supports compatibility within this RAT-PRM application. It does not establish a universal deformation range or a static chiral limit for every band. The positive-parity solution lies close to the intermediate-short plane and has a large partner splitting. Locators: Eqs. (1)-(5), pp. 3-4; Figs. 3-4 and discussion, pp. 9-11; Summary, pp. 13-14.

3. **Static reflection-asymmetric equilibrium in the real nucleus is not established here.** The paper reports that MDC-CDFT gives beta3 = 0 and an octupole-soft potential; the authors adopt beta3 = 0.02 to represent octupole correlations. A fixed asymmetric model input is therefore not an experimental measurement of a permanent pear shape, nor a demonstrated self-consistent finite-beta3 minimum. The core parity-splitting parameter remains E(0-) = 3 MeV, and states are constructed with good total parity. Locators: p. 6, Sec. III, first paragraph; p. 7, second paragraph; Eq. (2), p. 3; Eqs. (13)-(16), p. 5.

4. **This identifier does not contain the special idealized chirality-parity selection-rule result described in the request.** It develops a realistic quasiparticle RAT-PRM application to 78Br. It supplies parity-projected, angular-momentum-coupled states and electromagnetic matrix elements, but no special selection-rule table, extra chirality-parity quantum-number classification, or idealized symmetry-limit derivation. Consequently such rules and their assumptions cannot be attributed to this paper without identifying another primary source. Locators: all of Sec. II, pp. 3-6, especially Eqs. (13)-(20); all five figures; full mainline pp. 1-14.

5. **The experimental comparison has significant interpretive limits.** Gamma affects the calculated E1 strengths; the calculated E1/E2 ratios generally underestimate the data. The model changes the proposed negative-parity configuration to proton g9/2 coupled to neutron f5/2, and the authors explicitly call for additional microscopic or experimental support. The plotted data are taken from their Ref. [11], not a new independent experiment. Locators: Fig. 1 caption, p. 7; Fig. 2 and discussion, p. 9; configuration discussion, p. 13; Ref. [11], p. 14.

## Actual inputs and assumptions

| Item | What the paper actually specifies | Printed/PDF locator |
| --- | --- | --- |
| Baseline shape | beta2 = 0.28, gamma = 16.3 degrees; MDC-CDFT beta3 = 0, adopted RAT-PRM beta3 = 0.02 | Sec. III, p. 6, first paragraph |
| Gamma comparison | 16.3 versus 21.3 degrees in the plotted RAT-PRM E1/E2 comparison; abstract/summary round to 16 and 21 | Fig. 2 legend/caption, p. 9; pp. 1, 13 |
| Earlier alternative shape | beta2 = 0.32, gamma = 21.3 degrees is attributed to earlier cranked-shell-model work; do not silently substitute beta2 = 0.32 for this paper's baseline | p. 8, first full paragraph |
| Rotor | Irrotational inertias J_k = J_0 sin^2(gamma - 2k*pi/3); J_0 = 14 hbar^2/MeV and E(0-) = 3 MeV adjusted to spectra | Eq. (2) and following paragraph, p. 3; p. 7 |
| Intrinsic model | One quasiproton and one quasineutron; deformed Nilsson field and BCS pairing; Delta = 12/sqrt(A) MeV | Eqs. (1), (3)-(5), (10)-(12), pp. 3-5; p. 7 |
| Occupancy/model space | lambda_p = 44.6 MeV, lambda_n = 47.6 MeV; initial g9/2 m_z = 1/2 proton and g9/2 m_z = 5/2 neutron; 13 levels around each Fermi level | pp. 6-7, Sec. III |
| Shape expansion | General beta30, beta31, beta32, beta33 field; volume and center-of-mass corrections neglect higher-order deformation terms | Eq. (5), Eqs. (6)-(9) and following text, p. 4 |

The scalar beta3 in Sec. III is not accompanied by a complete numerical table for every beta3mu coefficient in Eq. (5). This audit preserves the source's scalar notation; it does not infer an undocumented nonaxial-octupole input set or impose a numerical beta30 identification as a separately verified fact.

## What can be said about selection rules

**Direct source content.** The basis is symmetrized with `(1 + S_2)`, where `S_2 = P R_2` is described as reflection in the plane perpendicular to axis 2; parity projection uses `(1 +/- p)`; total states have good angular momentum and parity. The intrinsic core and the single-particle potential share the same spatial orientation. These are the explicit construction assumptions on p. 5, Eqs. (13)-(16). They are not an additional demonstrated chirality-parity classification.

**Standard quantum-mechanical consequence, identified here as inference.** With good total parity and electromagnetic tensors of rank lambda, parity permits electric transitions with `p_f p_i = (-1)^lambda` and magnetic transitions with `p_f p_i = (-1)^(lambda+1)`, together with the usual angular-momentum triangle condition. Thus E1 connects opposite parities, whereas E2 and M1 preserve parity. This is the ordinary parity/tensor constraint applied to Eqs. (17)-(20), pp. 5-6, not a special selection-rule theorem quoted from the authors. It does not make all parity-allowed transitions strong or nonzero.

**Strength assumptions actually used.** M1 uses the effective proton/neutron/rotor gyromagnetic factors in Eq. (18). E2 neglects the valence-particle contribution relative to the core. E1 retains valence contributions and uses recoil-corrected effective charges, `N e/A` for the proton and `-Z e/A` for the neutron. These choices affect strengths and interference; they are not a beta3-driven prohibition on chirality. Locators: Eqs. (18)-(20) and adjacent discussion, p. 6; g-factor prescription, p. 7.

**Unverified extra rules.** Any stronger claim of exact transition zeros or alternating allowed branches based on an additional discrete quantum number requires a primary derivation identifying that symmetry, its Hamiltonian limit, and how the transition operators transform. This paper does not supply those premises. No special gamma limit, exact proton-neutron exchange symmetry, ideal particle-hole restriction, or extra quantum number is imported into this audit.

## Geometry and static-limit caution

Figures 3-4 plot root-mean-square components, not signed classical vector components or a direct handedness probability. The negative-parity interpretation uses proton angular momentum mainly in the intermediate-short plane, appreciable neutron alignment along the long axis, and rotor alignment mainly along the intermediate axis. The associated axes are 1 = intermediate, 2 = short, 3 = long at gamma = 16.3 degrees (p. 9).

Equation (21), p. 12, defines effective angles from expectation values. The same page warns that angles near 90 degrees at bandheads can occur in chiral vibration when the rotor angular momentum is small. Accordingly, neither these angles alone nor finite root-mean-square components prove localization in two static handed minima.

The source does not demonstrate an ideal fourfold near-degeneracy from simultaneous static reflection and chiral breaking. Its Introduction, p. 2, presents chirality-parity quartets as a possibility. The actual model uses a finite parity-splitting parameter and discusses distinct configurations. A claim that this calculation proves a stable static pear-shaped chiral quartet would exceed its reported evidence.

## Disposition of the OLD claim

The sentence "all beta3 > 0.1 prohibits chirality" should not be attributed to this source. The defensible source-specific finding is:

> Wang et al.'s RAT-PRM application uses beta3 = 0.02 with triaxiality and obtains negative-parity angular-momentum geometry interpreted as chiral. It does not test a universal beta3 = 0.1 exclusion threshold or establish static octupole deformation experimentally.

Logical boundary: a result at 0.02 cannot falsify a statement restricted to values above 0.1. Conversely, a fixed-asymmetric-field calculation with chiral geometry shows that this model does not treat reflection asymmetry and chirality as categorically incompatible. A quantitative counterexample above 0.1 remains unverified by this bounded source check.

## Remaining limitations and stop reason

The requested identifier is fully checked for the assigned questions. No broader literature search, numerical reproduction, deformation scan, separate idealized selection-rule paper, publisher-version comparison, or new experimental review was undertaken. The missing idealized selection-rule attribution and missing beta3 > 0.1 test remain explicit evidence gaps for the parent, not inferred results. This sidecar stops because its assigned primary-source audit is complete.
