# CH16 independent review: mass metric, domain and mode-comparison boundaries

Worker013 independently inspected the actual CH16 body after using012's report only as a locator guide. New claims and conditional derivations are `needs_review: true`; no author-error verdict, exact spectrum replay, numerical test count or human-review upgrade is claimed. Writes are confined to this013 worker prefix. No new retrieval/download, canonical/raw/PLAN/Bib/Git changes, session/run/agent/credit action.

**Verdict:**012's main scientific interpretation is supported: a real symmetric tensor retains mixed inertia; Pauli measure is √detB; the periodic1D comparison differs from CH13's box; late gap reopening and PRM benchmarking support the authors' bounded model interpretation, not an experimental mode or exact solution of the earlier second-vibration problem. A significant **additional P1 domain boundary** is worth recording: pole rank degeneration follows structurally from Eq19 under finite-gap assumptions, and the displayed w^−1/4 Fourier normalization does not certify finite kinetic energy or the solver's endpoint domain. The original producer is unavailable, so this is a conditional analytical audit, not evidence that the reported spectrum is wrong.

## Source identity and actual inspection

CH16 actual body: `tmp/day24-chiral-2d-012/chen2016-2d-arxiv160906967v2.pdf`,30pages,6543288bytes, SHA256 independently recomputed `158efcad3d6f9c69ec61ee3a427ace3aa54ba0e6be7dfbb6419226f3078332be`. Its arXiv sidebar says1609.06967v2/4Oct2016, title typeset dateMarch3,2022. Publication identity PRC94,044301(2016), DOI10.1103/PhysRevC.94.044301 comes from the existing receipt; no new metadata lookup or independent VoR check was performed. Every CH16 scientific locator below is to the30-page v2, not the journal body or a new2022 scientific version.

Native-text inspection covered PDF1,3–8,11–12,14–16,19–24,26–27, including all equations needed for this audit:1–26,28–36, plus the principal mode/mass/boundary/comparison discussion. Fresh full-page visuals were actually viewed for PDF4,6–8,14,16,19,21–25. This is a targeted independent review, not a claim to have independently reread or translated all30pages or all12figures. Owned text/renders preserve the checks.

CH13 actual comparison body: `tmp/day24-collective-chiral-008/chen2013-collective-chiral-arxiv.pdf`, SHA256 independently recomputed `bef6182263a6282ea6c4fc3e2fbae481bbf629e484dbf9668e3ea9e622342a2c`. Targeted native text PDF7/Eqs24–26,PDF10–11 wall discussion andPDF14–15 high-frequency discrepancy/fixed-frequency comparison was read directly. No fresh CH13 visual or VoR read is claimed here.

## Findings by severity

|Severity|Finding|Evidence and implication|
|---|---|---|
|P0|No blocking source-identity or fabricated-result problem identified.|Exact body hashes match; no data, lifetime, spin or EM value is supplied by this review. This is not a repository-wide security audit.|
|P1,additional conditional boundary|Positive-gap cranking mass is Gram-positive semidefinite, but strict detB>0 requires rank2. At θ0/π, Eq19 forces theφ column to vanish if gaps/matrix elements remain finite.|CH16PDF6/Eqs14–19 andPDF5/Eq7. Uniform strict positivity on the closed rectangle does not follow from the source formulas. A coordinate pole, not only the large-mass ridges discussed onPDF11, needs a domain/solver contract.|
|P1,additional conditional boundary|w^−1/4 Fourier functions may be L²-normalizable but outside the finite-kinetic-energy form domain near a regular pole.|Derived below from the actual Eq5/7/21–24 operator and mass scaling. Need endpoint treatment, admissible combinations/cutoffs, full metric grid and convergence before certifying a continuum Galerkin domain. No actual author implementation was obtained or judged.|
|P1,retain existing boundary|Eq31's literal unweighted P(θ) differs from the physical marginal of Eq28/29 under variablew.|PDF14 Eq28/29;PDF19 Eq31; both visually confirmed. Actual plotting convention unknown. Do not certify Fig7 normalization/width from that definition.|
|P1,retain comparison boundary|CH16 is not a theta-only ablation of CH13 or an exact good-I/experimental solution.|CH16PDF16/Eq30 explicitly changes1D boundaries too;PDF22/Eqs32–34 andPDF23/Eq35 define an averaged spin mapping;CH13PDF14–15 supplies its distinct comparison.|
|P2,literal-unit boundary|CH16Eqs14–17/20/36 print2Σ without an explicit numeratorℏ², unlike CH13Eq22; plots labelB asℏ²/MeV.|Keep original formulas and possible natural-unit convention separately. No explicit convention/producer was recovered that licenses silently inserting/deletingℏ² or declaring an error.|
|No correction required|Matrix symmetry versus reflection oddness, sector labels, high-frequency LW attribution and low-spin inertia caveat are correctly separated in012.|Direct locators below. The two existing local prose/density ambiguities are real original-literal issues, not grounds to discard the whole method.|

## Mass tensor: symmetry, Gram structure and strict positivity

Let D_a=(∂_aω)·j, a∈{θ,φ}, and A_a,t=〈m|D_a|i〉 for transitiont=(m,i), with Δ_t=ε_m−ε_i. For HermitianD, the two literal off-diagonal formulas are conjugates. The paper explicitly uses the real equalityBθφ=Bφθ (PDF6 belowEq19); under that declared real symmetry reduction the physical mass quadratic form can be written

\[
x^TBx=2\sum_t\frac{|x_\theta A_{\theta,t}+x_\phi A_{\phi,t}|^2}{\Delta_t^3}\ge0
\]

**provided all included Δ_t are strictly positive and finite**. Equivalently one takes the real part of the Hermitian Gram tensor for real coordinate velocities. Reality/equality is not proved for arbitrary complex transition data merely by printingEqs15/16; it is the real-model convention used here. If occupied/unoccupied tracking or a gap sign changes, this positivity argument must be checked again against actual inputs.

Positive semidefinite is not positive definite. StrictdetB>0 requires that no nonzero real pair(xθ,xφ) annihilates all transition amplitudes, i.e. rank2 over real response components. One dependent response direction givesdetB0 despite nonnegative diagonal entries. For a real symmetric2×2tensor, Bθθ>0 together withdetB>0 is a sufficient and necessary positive-definiteness criterion; detB>0 alone would also permit a negative-definite tensor if diagonal signs were unconstrained.

Eqs15/16 retain a mixed response. Their “antisymmetric” property in the paragraph belowEq19 means oddness as a function underφ→−φ orθ→π−θ; it does not meanBθφ=−Bφθ. On regular reflection-fixed lines, that odd function is zero, while away from them it need not vanish. Dropping mixed derivatives globally would change Eq5.

The finite-frequency prescription also has a conditional Gram reading: with positiveΔ_t and finite nonzero denominators, define Ã_a,t=A_a,t/[Δ_t²−ℏ²Ω_a²]. Eqs20/36 giveB_ab=2Σ_tΔ_t Re(Ã_a,tÃ_b,t*). Thus different signs in individual denominator factors do not by themselves imply an indefinite tensor; the same rank/reality/finite-gap conditions still matter. Exact denominator zeros and their regularization remain outside this finite formula. The assumed1.10MeV frequencies are not microscopically determined.

## Pole rank loss and the kinetic form domain

Eq19 contains an explicitsinθ factor. Atθ0 orπ, with finite active gaps and bounded matrix elements, Aφ0, soBφφ0 andBθφ0 anddetB0. If a gap also vanishes, the printed cranking expression is instead singular/undefined and requires separate limiting treatment; the finite-gap conclusion must not be applied through a0/0 expression.

On a regular finite-gap pole patch, a generic leading real metric consistent withEqs18–19 is

\[
B(\theta,\phi)=
\begin{pmatrix}a(\phi)&\theta b(\phi)\\
\theta b(\phi)&\theta^2c(\phi)\end{pmatrix}
+\text{higher orders},\quad
w=\theta^2d+\cdots,\quad d=ac-b^2>0,\ a>0.
\]

This is a **conditional local expansion**, not a recovered actual numerical tensor grid. It shows why strict positivity can hold inside while the chart degenerates at the endpoint. The analogous expansion holds inπ−θ at the other pole.

For the source's Pauli operator, the kinetic quadratic form in a regular patch is

\[
Q_T[\psi]=\frac{\hbar^2}{2}\int d\theta d\phi\,
\sqrt w\,(\partial_a\psi)^*(B^{-1})^{ab}(\partial_b\psi).
\]

Each theta-even trigonometric factor inEq21/22 has a nonzero constant leading value. Includingw^−1/4, writeψ~θ^−1/2f(φ), with f absorbingd^−1/4 and itsφ derivatives. Then the weighted norm near the pole behaves as∫dθdφ√d|f|²: it can be finite. But the leading kinetic integrand, before the commonℏ²/2factor, is

\[
\frac{\theta^{-2}}{\sqrt d}
\left[\frac c4|f|^2+b\operatorname{Re}(f^*f')+a|f'|^2\right]
=\frac{\theta^{-2}}{\sqrt d}
\left[a\left|f'+\frac{b}{2a}f\right|^2+\frac{d}{4a}|f|^2\right].
\]

The bracket is strictly positive wheref≠0 undera,d>0; an integral∫θ^−2dθ diverges. The mixed term therefore cannot generically cancel this divergence. This independently confirms the parent's supplied expansion, now tied to exact sourceEqs5/7/19/21–22.

Theta-odd factorssin2mθ have an extraθ, givingψ~θ^1/2f and generally a finite leading pole kinetic integral under these same regular assumptions. Particular even-sector **linear combinations** can cancel their constant leading coefficientf and change the asymptotics. A pole cutoff, transformed regular basis, appropriate endpoint/flux conditions or another implemented prescription might also alter the domain. None was recovered. Therefore normalization of the individual weighted Fourier functions is insufficient to certify that the author's actual diagonalization realizes a specified self-adjoint continuum operator or that it fails to do so.

This is a reproducibility/kinetic-domain limitation, not a computed instability or an experimental claim. No pole-grid scan, determinant minimum, regularization, kinetic matrix convergence or numerical spectrum was fabricated to close it.

## Pauli measure and periodic boundaries

PDF4/Eqs5–6 andPDF5/Eq7 give the divergence form

\[
T=-\frac{\hbar^2}{2\sqrt w}\partial_a
\left[\sqrt w\,(B^{-1})^{ab}\partial_b\right],\qquad
\langle f,g\rangle=\int\sqrt w\,f^*g\,d\theta d\phi.
\]

No separate sphericalsinθ weight is to be appended to that declared measure. The angular-coordinate Jacobian is encoded through the computed metric; the pole scaling just derived is consistent with√w~θ√d when regular. Inversion of the real tensor correctly placesBφφ in theθθ derivative andBθθ in theφφ derivative, with the two negative mixed terms printed inEq5.

The Green boundary form is the flux of√w timesB⁻¹ and derivatives. On a regular periodic domain, matching coefficients, wavefunctions and appropriate normal flux makes opposite-face terms cancel. Merely saying “the functions are periodic” without the coefficient/flux/domain contract is insufficient near a singular locus. Eqs21–25 describe weighted Fourier normalization and periodπ in both coordinates; they do not independently provide all the missing singular-endpoint numerical details.

Direct CH13PDF7/Eq26 imposesψ(±π/2)=0;PDF10–11 explicitly motivates that wall approximation using largeB. Direct CH16PDF16/Eq30 replaces its own1D comparison by periodic Fourier functions and explicitly contrasts withRef44'sbox. Thus Figs6–7 compare a periodic1D version and2DCH, with separate energy zeros normalized to their respective lowest levels; they do not isolate a theta-only causal change to the old CH13 spectrum. LargeB, singularB, periodicity and a Dirichlet wall are distinct mathematical inputs.

## Sector and energy comparisons: supported with their scope

The basis fixes(++),(+−),(−+),(−−) asθ/φ reflection labels. PDF7's one reversed “respectively” sentence is contradicted byEqs21–24 and the laterPDF20 operator paragraph. Using the explicit basis/operator convention, fixedPθ with oppositePφ labels chiral partners; fixedPφ with oppositePθ labels signature partners. These labels are not nuclear spatial parity or arbitrary observed band numbers.

Fig8/PDF21 actually shows late gap reopening; the inset supports a minimum around the sampled.60MeV point and increasing gaps thereafter. The author discussion attributes the late regime to vibrations near thei-axis principal rotation with particle/hole alignment and calls it longitudinal wobbling. This is a schematic-model interpretation with qualitative geometry/energy support, not a measured wobbling transition, a universal frequency threshold or a rename of every second chiral vibration.

Fig8's gaps are differences of collective rotating-frame levels at the **sameω**, using only the lowest state in each sector (PDF20). Eqs32–34/PDF22 average the TAC **magnitude**J_TAC overρ=√w|Ψ|², then applyI_coll=J_coll−½; this is neither exact good-I projection nor the magnitude of an averaged vector or an experimentally measuredJ². Sector-dependentJ_coll can differ at the sameω. Eq35/PDF23 then formsE=E′+ωJ to drawFig10 versus the mappedI. One cannot read Fig8 directly as a same-I laboratory energy gap.

Fresh Fig9/PDF23 andFig10/PDF24 inspection confirms an actual PRM benchmark, including favored(++), nearly degenerate(+−)/(−+) correspondence at high spin. It also confirms the adverse low-spin reduced-energy trend. Fig10 subtracts0.007I(I+1), andFig9 subtracts40ω from angular momentum; those references must survive reuse. Fig11/12/PDF25 show the changed spectrum/masses after an **assumed**ℏΩθ=ℏΩφ=1.10MeV. PDF24 explicitly calls microscopicΩ unresolved. Agreement after that assumption is conditional model benchmarking, not a parameter-free microscopic prediction.

CH13PDF14–15 reports renewed PRM separation aboveabout.35MeV while its1D separation still falls and calls the omitted behavior second chiral vibration; it explicitly compares atfrequency,notgoodI. CH16 supplies theta dynamics, extra sectors, late reopening and a PRM comparison, so it provides real partial method support. Boundary/inertia changes, different mode language, singular-domain/producer uncertainty and absent mode-overlap tracking prevent a claim that addingtheta alone uniquely solved that exact earlier discrepancy or an experimental counterpart.

## Literal units and remaining unknowns

CH16Eqs14–17/20/36 have literal2Σ expressions without an explicit overallℏ², while CH13Eq22 prints2ℏ²Σ. CH16Fig12 labelsB inℏ²/MeV and its PauliEq5 displaysℏ². With dimensionless angles, a physical kineticT=½Bqdot² requiresB unitsℏ²/MeV; inℏ1numerical conventions the same coefficients are often represented inMeV⁻¹. The exact choices forj matrix elements,ω versusℏω, derivative units and restoredℏ factors must be recovered from an explicit convention orproducer before comparing implementations. This review neither silently repairs the source formula nor calls it erroneous.

Still unavailable: actualV/B grids andgap/tracking data, real-tensor construction, determinant/rank checks away from poles, singular ridge/pole treatment, boundary flux prescription, Fourier cutoff and convergence, solver/plotting conventions behindEq31, exactEM operators, same-input/mass/boundary1D–2D ablation and mode overlaps, or a real-nucleusinput fit. These gaps do not block ordinary evidence-calibrated use of the paper; they limit stronger numerical and experimental conclusions.

No numerical test suite or synthetic spectrum was run for013. Its added result is the conditional Gram/rank/pole/kinetic-form derivation. The next informative route is the actualmetric/solver domain and convergence contract, not a new catalogue of toy tests or another full-paper translation.
