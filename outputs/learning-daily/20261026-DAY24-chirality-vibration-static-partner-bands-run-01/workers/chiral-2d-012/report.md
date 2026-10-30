# CH16 two-coordinate collective Hamiltonian: what it adds, and what remains open

**Conclusion from the direct original:** this2016 method paper adds theta dynamics and theta–phi kinetic coupling, restores two reflection/signature classes, and actually shows high-frequency reopening of the gaps plus a high-spin PRM comparison. In its stated schematic model the authors interpret the late motion as **longitudinal wobbling about an intermediate-axis principal rotation**, after the chiral-rotation region. This is more than a statement of intent. It does **not** show that adding theta alone solves CH13's high-frequency discrepancy: the boundary condition also changes, the baseline cranking inertia fails badly at low spin, and a subsequent1.10MeV assumed vibrational frequency improves that comparison without a microscopic determination. No real-nucleus experimental mode or transition rate is established here.

## Identity, original and reading receipt

Fresh Crossref metadata and the official arXiv API confirm **Q.B.Chen, S.Q.Zhang, P.W.Zhao, R.V.Jolos and J.Meng**, *Two-dimensional collective Hamiltonian for chiral and wobbling modes*, **Physical Review C94,044301(2016)**, DOI **10.1103/PhysRevC.94.044301**, publication2016-10-03.

Actual scientific body: **official arXiv1609.06967v2**, URL `https://arxiv.org/pdf/1609.06967v2`; HTTP200, `application/pdf`, valid `%PDF`, **6543288bytes**, **30pages**, SHA256 **158efcad3d6f9c69ec61ee3a427ace3aa54ba0e6be7dfbb6419226f3078332be**. The PDF sidebar says **4Oct2016 v2**; title-page/typeset date says **March3,2022**. These are separate fields; no new scientific edition/year is inferred from the typesetting date. PRC VoR was not separately obtained. Every locator below belongs to this30-page v2.

The complete30-page text was read: main text PDF1–27 and references27–30. All **12figures** were visually inspected on fresh renders. The paper has **no numbered tables**. All **Eqs1–36** were read and their formula-bearing pages visually checked: PDF4–8,11,14,16,19,22–24. Visual inspection additionally covered PDF9–10,13,17–18,21,25. Active recall was frozen before opening the body in `active-recall.md`, explicitly CH13/Wiki-primed and unscored. `receipt.json` preserves hashes, metadata and coverage. No author script/model producer was run, no independent spectrum was replayed, no spectrum residual/CI was manufactured.

## Wiki overlap and true new information

Initial scoped search finds the just-created CH13 source and its theta/second-vibration gap, but no CH16 source page. CH13 Ref44 is explicitly cited in the new original; it is the earlier one-coordinate calculation, not an independent experiment. The new source closes a **method-literature link**: two-coordinate kinetic tensor, periodic boundary comparison, extra theta sectors, density definition and a direct PRM energy comparison. It does not close135Nd/134Pr experimental normalizers, lifetimes, g factors or model-input provenance.

## Coordinate, potential and kinetic contract

The coordinates are the **orientation of the cranking rotational axis**, not beta/gamma shape coordinates or nuclear spatial parity. Eq10 defines

`omega=(omega sin(theta)cos(phi), omega sin(theta)sin(phi), omega cos(theta))`.

The quantization domain in Eq7 is **theta∈[0,pi], phi∈[−pi/2,pi/2]**. The calculation is performed **at fixed rotational frequency in the rotating frame** (PDF5 just after Eq7). At each frequency, V and B are supplied from TAC, then the collective Hamiltonian is solved. Full V(theta,phi)=E′(theta,phi) is retained rather than minimizing theta separately at every phi as in CH13 (PDF5–6 Eqs8–13 and opening of PDF6).

Classical Eq4 has

`T=1/2 B_thetatheta theta_dot² + 1/2 B_thetaphi theta_dot phi_dot + 1/2 B_phitheta phi_dot theta_dot + 1/2 B_phiphi phi_dot²`.

**The cross mass is retained and generally nonzero.** B_thetaphi=B_phitheta makes the tensor symmetric; the statement “antisymmetric” in PDF6/10 refers to its *coordinate reflection dependence*, not an antisymmetric matrix. Under either phi→−phi or theta→pi−theta, the diagonal components are even and the cross component is odd. Fig2 actually displays its positive and negative lobes. Setting it to zero everywhere would change this model.

The mass formulas Eqs14–17 are particle–hole **cranking** sums over matrix elements of `(partial_a omega)·j` with `(epsilon_m−epsilon_i)^3` denominators. **The residual interaction is neglected** to obtain these formulas; the cited ASCC theory is motivation, not a claim that a fully self-consistent ASCC mass was solved here. PDF7 relates this to the Omega→0 limit of the adiabatic-perturbation inertia Eq20 and explicitly warns of underestimated mass at low frequency. The numerator contains omega² (Eqs18–19), adding a low-frequency suppression. “Microscopic basis” must not be expanded to “approximation-free inertia”.

The schematic system is pi(h11/2)^1⊗nu(h11/2)^−1, **gamma=−30deg, C_pi=.25MeV, C_nu=−.25MeV, J0=40hbar²/MeV**; axes1/2/3=s/i/l (PDF8 SecIII). Particle/hole sign is explicitly carried in C in Eq11. Eq13's irrotational inertias give J_s=J_l=10 and J_i=40hbar²/MeV at that gamma, by direct substitution; this is source-parameter geometry, not measured inertia. No target-nucleus pairing/CDFT/multiorbital fit is performed. Pairing is only discussed as a possible future regularizer of near-degenerate cranking denominators (PDF11).

## Pauli operator, measure, basis and boundary

Eq6 defines **w=detB=B_thetatheta B_phiphi−B_thetaphi B_phitheta**. Eq5 is the divergence-form Pauli kinetic operator,

`T_hat=−hbar²/(2sqrt(w)) partial_a[sqrt(w)(B^−1)^{ab}partial_b]`.

For two coordinates, `sqrt(w)B^−1=(1/sqrt(w))*[[B_phiphi,−B_thetaphi], [−B_phitheta,B_thetatheta]]`; expansion gives the two diagonal and two mixed terms printed in Eq5. **The inner product is sqrt(w)dtheta dphi** (Eq7), not a flat measure or an independently added sin(theta)dtheta dphi. In regular positive-definite regions, the quadratic form is `hbar²/2 ∫sqrt(w) (partial_a f)* (B^−1)^{ab}(partial_b g)`, provided the periodic boundary terms cancel. This is a conditional mathematical reading of the source operator, not a numerical check of the author's whole grid or singular-point treatment.

Basis Eqs21–24 divides each normalized trigonometric product by **w^(1/4)**. The sqrt(w) in the inner product cancels its squared denominator, explaining the displayed flat-Fourier normalization. The sectors are conventionally `(P_theta,P_phi)=(++),(+−),(−+),(−−)` with cos/sin choices in the corresponding theta/phi variables. Eq25 imposes **period pi in theta and in phi**. These are not CH13's Dirichlet walls at phi=±pi/2.

Crucially, **the new paper also changes its one-dimensional comparison to periodic boundaries**: Eq30 and PDF16 explicitly contrast this with Ref44's old box condition, and motivate periodicity because minima can sit on the boundary. Figs6–7 are therefore a useful same-paper comparison, but **not a clean “old CH13 result plus theta only” ablation**. For selected theta-zero-phonon states, the periodic1D and2D counterparts become close at high frequency; new theta-excited states have no1D counterpart (PDF17–19).

The paper shows very large masses/small-denominator “singularities” near theta≈90deg or phi≈±90deg and suggests pairing might remove them (PDF11). **No producer code, full B/w grid, explicit minimum-determinant scan, singular-point regularization details or basis-cutoff convergence study is provided in this read body.** Smooth plots and a Fourier basis do not independently certify w>0 everywhere or numerical self-adjointness across singular loci. This is a reproducibility gap, not an identified failure of the reported calculation.

## Symmetry and probability definitions: preserve two literal boundaries

The basis makes theta reflection and phi reflection transparent. PDF20 identifies P_phi with the chiral operator T*R2(pi), and P_theta with T*R3(pi), equivalent to signature R1(pi) combined with P_phi. Thus chiral pairs differ in P_phi at fixed P_theta; signature pairs differ in P_theta at fixed P_phi. These are **collective-coordinate labels**, not nuclear intrinsic spatial parity, and cannot be mapped to arbitrary experimental band ordinals without other information.

Two exact-source cautions matter:

1. **PDF7 paragraph immediately before Eq21 reverses the association in one “respectively” sentence:** it names P_theta/P_phi then phi→−phi/theta→pi−theta. Eqs21–24, the mode discussion PDF15 and the operator definitions PDF20 consistently attach the subscripts to their own coordinates. Report the basis/operator convention and retain this local prose ambiguity; do not silently promote the reversed sentence into a new physical definition.
2. **Fig5 has a correct explicit coordinate-density contract:** PDF14 Eq28 `rho(theta,phi)=|Psi(theta,phi)|² sqrt(w)` and Eq29 `∫dtheta dphi rho=1`. But **PDF19 Eq31 literally writes** `P(theta)=∫dphi |Psi(theta,phi)|²`, without sqrt(w), and Fig7 caption points to Eq31. That is not generally the normalized theta marginal of Eq28/29 for variable w. The physical marginal under that norm would be `∫dphi rho`, which is a mathematical inference, not a replacement transcription of Eq31. Actual plotting-code convention is unavailable. Fig7 therefore supports the authors' qualitative correspondence discussion but does not provide a certified normalized theta-frequency distribution or a quantitative experimental fluctuation width. This boundary does not by itself prove the producer plotted a wrong quantity.

## What high-frequency problem is actually addressed?

There are direct model results, with clear locators:

- **TAC landscape:** Fig1/PDF9 moves from phi=0 planar minima at low frequency to nonzero phi around hbar*omega≈.20MeV. Around≈.70MeV the minima reach theta=90deg,phi=±90deg, i.e. principal-axis rotation about i. Theta softness becomes important in the high-frequency landscape. These are this schematic model's sampled regimes, not universal experimental transition thresholds.
- **Additional motion:** Fig4/PDF13 has four sectors; Fig5/PDF14 shows the theta- and phi-nodal patterns and rho. PDF15 distinguishes theta and phi excitation directions. Their near equality at high frequency is linked to the special gamma=−30deg and equal s/l inertias, not a general two-mode degeneracy for all real triaxial nuclei.
- **Reopening gaps:** **Fig8/PDF21** explicitly plots chiral and signature partner gaps; the text PDF20–21 says all decrease up to .60MeV then rise slightly above it. The inset shows the late increase. The authors connect it to particle/hole Coriolis alignment toward i and vibration about the principal-axis minimum. They call this **longitudinal wobbling**, where wobbling frequency increases with rotational frequency. The label is an author model interpretation supported by their coordinate/energy analysis, **not an experimental wobbling assignment or a synonym for chiral vibration**.
- **Actual comparison, not just promise:** **Fig9/PDF23** compares angular momenta vs frequency with PRM bands1/2 and TAC; **Fig10/PDF24** compares E(I). PDF23 states that PRM and2DCH show four high-spin signature branches that TAC cannot provide, and identifies the favored band1 branch with(++), while PRM unfavored band1/favored band2 are nearly degenerate and correspond to(+−)/(−+). The paper claims reasonable high-spin energy agreement; a fresh plot inspection supports the displayed qualitative alignment but supplies no numerical residual/independent parameter validation.

Therefore the CH13 omitted-theta gap is **partly addressed at the schematic-method level**: extra motion, symmetry sectors and late spectral reopening have now been represented and compared with the corresponding PRM. It is **not closed as an exclusive explanation of the precise CH13 Fig8 turnover**. The models use changed boundaries and inertia choices; CH13's described “second chiral vibration” and CH16's late longitudinal-wobbling interpretation cannot be equated solely from a returning energy gap. No explicit same-input/boundary/mass one-at-a-time ablation or projected mode-overlap tracking between those papers is provided. Numerical .35MeV from CH13, .60/.70MeV here, or a continuous collective angle cannot be imported as a134Pr/135Nd experimental spin boundary.

## Low-spin failure, correction and angular-momentum mapping

Baseline **Fig10 and PDF23–24** show a serious model limitation:2DCH reduced energies decrease with spin up to about I≈20hbar, contrary to the displayed PRM/TAC trends. The authors attribute this to neglect of vibrational frequencies in the inertia in a harmonic-like single-well region. This adverse result must accompany the high-frequency success claim.

They then use Eq20/36 with **assumed constants hbar*Omega_theta=hbar*Omega_phi=1.10MeV**. **Fig11/PDF25** shows improved low-spin PRM spectra; **Fig12/PDF25** shows larger, more moderately varying inertia due to denominator cancellation. **PDF24 explicitly says microscopic derivation of these frequencies is unresolved.** This is a demonstrated sensitivity/correction prescription, not an independent microscopic prediction of1.10MeV or experimental extraction. Near denominator cancellation and other-frequency extrapolation need their own validity/convergence checks; no new CI is available.

The comparison with PRM retains a frequency/good-spin boundary. **Eqs32–34/PDF22** obtain J_coll by averaging the TAC angular-momentum magnitude with the collective probability measure, then apply **I_coll=J_coll−1/2**. **Eq35/PDF23** uses E=E′+omega*J. This is not exact angular-momentum projection of the collective state; PRM is the calculation here with good I. The agreement shown is meaningful model benchmarking with that mapping, not proof that the fixed-frequency collective eigenstates have exact laboratory I or complete EM matrix elements. No new tau, delta, g or B(E2)/B(M1) dataset is produced in this paper. The2018 electromagnetic PartII was found in metadata but **not read or used** in this one-paper unit.

## All figures: what was visually checked

| Figure / PDF page | Direct content and use |
|---|---|
|1 /9 | Six2D Routhian surfaces .10/.20/.30/.50/.70/.90MeV; varying color scales, absolute-minimum stars and eventual i-axis minima |
|2 /10 | B_thetatheta/B_thetaphi/B_phiphi at .10/.50/.90; mixed-term sign lobes, changing scales and singular ridges |
|3 /11 | Minimum-point masses and curvatures vs frequency; distinct curvature behavior around sampled regime changes |
|4 /13 | Four-sector levels at six frequencies; low-frequency energies extremely high, near high-frequency(+−)/(−+) degeneracy |
|5 /14 | Four-sector normalized rho profiles at .10/.50/.90; explicit Eq28/29 measure contract |
|6 /17 | Periodic1D vs2D levels with correspondence lines; extra theta modes and frequency-dependent matches |
|7 /18 | Phi wavefunctions at theta78deg and plotted P(theta); caption points to unweighted Eq31, so normalized marginal boundary retained |
|8 /21 | Chiral/signature gaps, late-frequency inset and reopening above.60MeV |
|9 /23 | I−40omega reference plot comparing2DCH/PRM/TAC; collective spin mapping Eq32–34 |
|10 /24 | Reduced E(I) benchmark with0.007I(I+1) subtraction; high-spin agreement and low-spin adverse trend |
|11 /25 | Same spectrum after assumed1.10MeV inertia correction; improved low-spin trend |
|12 /25 | Corrected masses and cranking first-level gaps; explicit denominator/sensitivity mechanism |

## Atomic claim drafts for leader knowledge writeback

All use `needs_review:true`, direct `arxiv1609.06967v2` provenance and model-only scope. Suggested source slug: `chen-2016-two-dimensional-collective-chiral-wobbling` (leader decides). These are not all independent evidence; they are facets of the same theoretical source.

| Candidate | Statement | Kind | Exact locator |
|---|---|---|---|
|CH16-D24-001|The2DCH uses orientation theta/phi at fixed rotating frequency, full V=E′ and a symmetric mass tensor retaining B_theta_phi; theta is dynamical rather than minimized out.|direct-model-construction|PDF4 Eqs3–6;PDF5 Eq7/10/12;PDF6 opening|
|CH16-D24-002|Pauli operator has mixed derivatives and detB measure sqrt(w)dtheta dphi. Fourier bases carry w^−1/4 and period pi in both coordinates.|direct-quantization-and-boundary|PDF4 Eq5/6;PDF5 Eq7;PDF7–8 Eqs21–25|
|CH16-D24-003|The mass is a residual-interaction-neglected cranking prescription, not a solved full ASCC mass; Omega0/omega² suppresses low-frequency inertia and small gaps cause large-mass ridges.|approximation-and-reproducibility-boundary|PDF6 Eqs14–19;PDF7 Eq20/discussion;PDF10–11 Fig2/ridges|
|CH16-D24-004|Parameters are a singleh11/2 particle-hole schematic rotor,gamma−30deg,C_pi/nu=±.25MeV,J0=40; no real-nucleus fit or new experiment. Pairing regularization is suggested, not performed.|input-and-scope|PDF8 SecIII;PDF11 ridgeparagraph;PDF26–27 conclusion|
|CH16-D24-005|The1D comparison is also changed to periodic boundaries, unlike CH13's box. Some theta-zero-phonon states have1D counterparts; extra theta-excited states do not. This is not a theta-only ablation against the old figure.|source-comparison-and-inference-boundary|PDF16 Eq30/discussion;PDF17–19 Figs6–7|
|CH16-D24-006|Four sectors separate P_phi chiral partners and P_theta signature partners in this model. They are collective reflection labels, not nuclear spatial parity. One preceding prose sentence reverses the associations, while bases and later operator discussion fix the working convention.|symmetry-and-literal-boundary|PDF7 pre-Eq21;PDF8 Eqs22–24;PDF20 operatorparagraph|
|CH16-D24-007|Fig5 rho=|Psi|²sqrt(w) is normalized in dtheta dphi; Eq31 literally defines P(theta)=∫|Psi|²dphi without that weight. Treat Fig7's P(theta) separately from a normalized physical marginal until producer convention is known.|measure-and-producer-boundary|PDF14 Eqs28–29/Fig5;PDF18 Fig7caption;PDF19 Eq31|
|CH16-D24-008|Fig8 gaps fall through.60MeV then rise; authors interpret the late i-axis principal-rotation/particle-hole-alignment vibrations as longitudinal wobbling after chiral rotation. It is a model-mode transition, not synonymous naming or an experimental threshold.|direct-result-and-author-interpretation|PDF20–21 Fig8/discussion;PDF9 Fig1|
|CH16-D24-009|Figs9–10 actually benchmark2DCH against schematic PRM, including high-spin four-branch structure, while the baseline has a pronounced low-spin energy failure. This gives bounded method support, not complete quantitative validation.|direct-model-benchmark-and-adverse-evidence|PDF22–24 Eqs32–35/Figs9–10|
|CH16-D24-010|Assumed hbarOmega_theta=Omega_phi=1.10MeV in the mass formula improves low-spin PRM comparison; microscopic Omega remains unresolved.|assumed-input-and-result-boundary|PDF24 Eq36/lastparagraph;PDF25–26 Figs11–12|
|CH16-D24-011|J_coll is a measure-weighted average of TAC magnitude with I_coll=J_coll−1/2, not exact I projection; fixed-frequency states/PRM good-I states require their explicit comparison mapping.|comparison-coordinate-and-inference|PDF22 Eqs32–34;PDF23 Eq35|
|CH16-D24-012|CH16 partially addresses CH13's omitted theta/high-frequency behavior through additional sectors and PRM comparison, but changed boundaries/mass and a later wobbling interpretation prevent declaring the exact old second-vibration discrepancy uniquely solved or transferring its frequencies to real nuclei.|cross-source-synthesis-inference|CH13-D24-008/009;CH16PDF16/20–26|

## Stop state and remaining research nodes

This one-paper source unit is complete at its declared version/model scope. Remaining nodes are actual B/V grids and solver convergence/singular treatment; identity-preserving, same-boundary/mass1D↔2D comparisons; microscopic finite-frequency inertia; exact EM operators and real-nucleus inputs; distinguishing late chiral vibration from wobbling using more than gap reopening. These are research boundaries, not a demand to recreate the author producer before using the source for ordinary discussion.

Outputs are confined to the assigned worker prefix and temporary originals/renders to `tmp/day24-chiral-2d-012/`. Shared canonical/raw/PLAN/Bib/Git, sessions and course credits were untouched. Scientific drafts require leader incorporation into `knowledge/`; outputs are not their long-term source page.
