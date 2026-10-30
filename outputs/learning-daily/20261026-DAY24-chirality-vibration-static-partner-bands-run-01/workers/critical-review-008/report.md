# Independent review: OL02 critical frequency and the 135Nd map

Reviewed only `knowledge/sources/olbratowski-2002-critical-frequency-preprint.md`, the final critical-frequency section of `knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`, and the actual four-page 2002 v1. Existing startup/evidence rules reused. No external retrieval, HF producer investigation, shared-page/raw/Git edits, new agent/session/run/credit. All new mathematical observations below are conditional review calculations, `needs_review: true`; no human-review status changes.

**Verdict:** no blocking scientific defect found in the inspected source or map. Their distinctions between classical onset, reported HF continuation, quantum spectra and experimental states survive independent checks. The inertia-response contribution is not double counted; the 2002 v1 versus unread 2004 journal body boundary is explicit. Two optional clarity improvements are listed; neither is a discovered incorrect claim.

## Severity findings

|Severity|Finding and scope|Evidence / disposition|
|---|---|---|
|P0|None in inspected scientific material.|No invented clock, quantum-spin assignment, absolute strength or unsupported experiment certification found. This is not a repository-wide/security audit.|
|P1|No correction required for formulas, units, source parameters, HF inputs or interpretation boundary.|Independent derivation and 25 bounded numerical controls below agree with the source. No HF convergence or quantum validity is certified by those controls.|
|P2 advisory|Explicitly writing **I=μω** would clarify why μ has inertia units and why μ=𝒥m is branch-specific.|PDF2 Eqs3–4 plus I=𝒥ω+s imply this identity. For arbitrary stationary branches, ω×I=0 means collinearity; μ can be negative for an anti-aligned planar branch. The current pages retain the exact cross-product form and do not make the incorrect stronger claim that all branches require positive parallel alignment.|
|P2 advisory|If Fig6 is used in later quantitative comparison, preserve its plotted ordinate **E−I²/(2𝒥m)**.|PDF4 Fig6 axis and caption subtract a rigid-rotor reference. It is not the rotating-frame Routhian E−ω·I. The current pages do not mislabel it; adding the ordinate would make reuse safer.|
|Already isolated original ambiguities|PDF2 post-Eq1 prose swaps “long and short” relative to its formula; PDF4 opening text says decreasing inertia differences lowers ωcrit.|The source already quotes these as v1 literal/conditional boundaries. No silent correction or unqualified 2004 attribution was found. With fixed positive nonzero gyro spins and both positive inertia gaps reduced, Eq7 instead raises ωcrit; no universal γ dependence follows without specifying how both gaps and spins change.|

## Actual direct source and visual checks

Body: `tmp/day24-critical-tac-007/arxiv-0211075v1.response`, 252547 bytes, 4 PDF pages, SHA256 `3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb`, independently recomputed. Page1 visibly has three authors and the arXiv v1 date25Nov2002. All four pages were independently read in native text and freshly inspected as rendered full-page images (`pdf01.png`…`pdf04.png`). No 2004 VoR body or metadata service was opened in this review.

|Locator in 2002 v1|Direct support checked|
|---|---|
|PDF1 right column/Fig1|132La πh11/2 particle/νh11/2 hole; β≈.25, γ≈45°; preliminary non-selfconsistent s/l response probe around converged ω0 field. Fig1 is not a selfconsistent arbitrary-direction TAC continuation.|
|PDF2 Eq1 and preceding/following paragraphs|jp≈ss e_s+δ𝒥l ωl e_l, jn≈sl e_l+δ𝒥s ωs e_s; formula and later gyro definition agree, despite the intervening reversed prose order.|
|PDF2 left column, above Fig2|ss=5.43ℏ,sl=5.00ℏ; 𝒥s/m/l=8.5/31/20ℏ²MeV⁻¹, from axial selfconsistent slopes. Explicit sentence says these values already contain δ𝒥s,δ𝒥l.|
|PDF2 right column, Eqs2–4|Uniform rotation means constant body-frame ω; I=𝒥ω+s; ω×I=0; constrained Routhian extrema and branch equation ωm(μ−𝒥m)=0.|
|PDF3 Eq5/Fig3|A distinct threshold for additional planar solutions; not Eq7's aplanar onset. The μ-axis unit is ℏ²/MeV.|
|PDF3 Eqs6–7/Fig4|Fixed s/l components on μ=𝒥m branch; meeting point with planarA at ωm0; source-parameter classical threshold≈.51MeV. Fig4 I and E are classical curves.|
|PDF3 right column, middle/lower paragraphs|Reported HF chiral continuation from ℏω=.6MeV, not found below despite attempts; explicitly higher than frequencies where the experimental candidate pair appears. No certified continuous HF numerical bifurcation location/error or search completeness is supplied.|
|PDF4 Fig5|Distinct HF points and classical lines; ω components in MeV/ℏ, not direct measured angular-momentum components.|
|PDF4 Fig6, caption and text immediately below|Plot subtracts I²/(2𝒥m); author tentatively assigns lower/upper experimental bands to planar/axial-l HF branches and discusses roughly350keV splitting. This remains an alternative interpretation, not a new independent experiment.|
|PDF4 Ref6|HFODD v2.00k; N0=14 spherical shells; SKM*; no pairing; only parity conserved; time-odd mean-field components switched off. “Selfconsistent” is within these specified approximations.|
|PDF4 Ref10|Effective inertias need not correspond to those of a massive rigid body of the same shape. No geometric rigid-body inertia substitution is justified by the model label.|

## Independent derivation, units and branch condition

Let the degrees of freedom be the three body-frame angular-velocity components with fixed magnitude ω; fix positive diagonal inertias and a fixed spin vector s=(ss,0,sl), with both ss/sl nonzero. This is the declared classical model, not a finite quantum particle-rotor calculation.

From L=½ωᵀ𝒥ω+s·ω, I=∂L/∂ω=𝒥ω+s and H=ω·I−L=½ωᵀ𝒥ω. Set R=H−ω·I=−L. Stationarity of R+½μω² gives

\[
(\mu-\mathcal J_s)\omega_s=s_s,\quad
(\mu-\mathcal J_m)\omega_m=0,\quad
(\mu-\mathcal J_l)\omega_l=s_l.
\]

Thus **I=μω**, which independently establishes ω×I=0. Here s and I have unitsℏ, ω has MeV/ℏ, and μ and 𝒥 have ℏ²/MeV; every term in the constrained functional has MeV. μ is neither an angular frequency nor a moment of inertia to be fitted separately after selecting the aplanar branch.

For nonzero ωm, μ=𝒥m. When 𝒥m differs from 𝒥s,l,

\[
\omega_s^*=s_s/(\mathcal J_m-\mathcal J_s),\qquad
\omega_l^*=s_l/(\mathcal J_m-\mathcal J_l),\qquad
\omega_c^2=(\omega_s^*)^2+(\omega_l^*)^2.
\]

The two nonzero m components exist only for **ω>ωc**; at equality they coincide at a single planar point. Algebraic stationarity with these fixed parameters is not quantization of the two signs. If one gyro spin vanishes, the corresponding s/l component vanishes, so a formal threshold from the remaining term is not a three-nonzero-component chiral solution. If an inertia difference vanishes while its gyro spin remains nonzero, the stationarity equation has no such finite solution; the singular formula is not an experimental exclusion bound.

For planar ωm0, minimize the direct radius

\[
\omega(\mu)^2=s_s^2/(\mu-\mathcal J_s)^2+s_l^2/(\mu-\mathcal J_l)^2
\]

between𝒥s and𝒥l. Its minimum gives Eq5, (ss^(2/3)+sl^(2/3))^(3/2)/|𝒥l−𝒥s|. An independent scalar minimization finds μ≈14.4080875ℏ²/MeV and agrees with that formula. This threshold creates additional planar extrema, not the μ=31 aplanar onset.

## Independent fixed-I route and curvature boundary

An independent momentum-space Hamiltonian is

\[
H(\mathbf I)=\tfrac12\sum_k(I_k-s_k)^2/\mathcal J_k.
\]

On the stationary aplanar branch, the fixed-|ω| constrained Routhian Hessian is diag(𝒥m−𝒥s,0,𝒥m−𝒥l) restricted to δω·ω=0. Separately, fixed-|I| energy variation has Hessian diag(1/𝒥s−1/𝒥m,0,1/𝒥l−1/𝒥m) restricted to δI·I=0. For the supplied strictly largest𝒥m and nonzeroωm, both tangent restrictions are positive definite. At the meeting point there is one zero tangent direction; it becomes the negative m-direction curvature of the continued planarA branch aboveωc.

This confirms the pages' bounded local-curvature statement. A zero constrained curvature is not, by itself, a calculated collective mass, harmonic/RPA frequency, tunneling splitting, finite-system order parameter or quantum-spin assignment. The calculations here neither construct an HF stability matrix nor identify a spurious/physical RPA mode.

The same fixed-I route supplies the independent Fig6 check:

\[
H-I^2/(2\mathcal J_m)
=-\tfrac12\left[s_s^2/(\mathcal J_m-\mathcal J_s)+s_l^2/(\mathcal J_m-\mathcal J_l)\right]
\]

on either aplanar sign. This constant is −1.791583636MeV, consistent with the horizontal black classical-chiral line near−1.79 in the freshly viewed Fig6. This visual comparison verifies the plotted quantity at the displayed scale; it is not a precision digitization or experimental fit. Substituting the Routhian would give a different function and would fail this interpretation.

## Actual numerical controls

Independent implementation: `review_checks.py`; executed output: `review-checks.json`. It does not read or reuse the parent007 implementation. It uses source parameters, direct Cartesian cross products, a separate momentum Hamiltonian and SVD-generated tangent bases.

|Quantity|Independent result|Scope|
|---|---:|---|
|ℏωs*,ℏωl*|.241333333,.454545455MeV|Conditional model components|
|ℏωc|.514639046MeV|Classical source-parameter onset|
|Icrit=𝒥mωc|15.953810437ℏ|Continuous vector magnitude; no rounding to experimentalI=16 or quantum√I(I+1)|
|ℏωthr|1.282266726MeV|Separate additional-planar threshold|
|At ℏω=.6, abs(ℏωm)|.308458509 MeV|Both signs checked; model abs(I)=18.6ℏ, not an HF point or adopted quantum spin|
|Atℏω=.5|ωm²<0|No real aplanar component in this fixed model|
|Fig6 reduced constant|−1.791583636MeV|Reference-subtracted classical energy|

25 controls pass: direct Eq5 minimization; distinct thresholds; Cartesian Euler residuals and I=𝒥mω; velocity/momentum Hamiltonian agreement; both ± branches; threshold zero versus positive post-threshold tangent curvatures; planarA curvature sign change; Fig6 constant; rescaling/gyro limits and monotonicity under specified positive-gap changes. Numerical tolerances only bound floating-point discrepancies in these finite algebraic checks, not nuclear uncertainty.

## Unverified quantities and completion limit

Not checked or reconstructed: HFODD input decks, occupied orbital tracking/blocking details, oscillator-frequency/basis truncation convergence, initial seeds and continuation step size, shape changes along actual branches, time-odd/pairing sensitivity, δ𝒥 numerical decomposition, full dynamic stability, collective mass, actual RPA spectrum, quantum Hamiltonian/±handed mixing, 132La primary experimental state/branch inventory, experimental frequency definitions/errors, or 2004 VoR scientific content. Source-stage storage remains staging; this worker did not archive raw.

The current source/map already leave these scientific limits open and do not use extra algebraic digits to close them. No correction request is required before parent integration within the stated research scope. Optional μ and Fig6-ordinate clarifications can be added without claiming that the original producer or a real-nucleus threshold has been independently validated.
