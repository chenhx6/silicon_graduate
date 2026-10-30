# Incremental gyro audit: fixed-frequency versus fixed-angular-momentum minima

Task010 extends worker008 only where there is new information: complete planar stationary-root inventories, exact global-minimum certificates, the low-I D branch, the critical quartic direction, and explicitly changed degenerate/zero-gyro limits. It does not repeat HF/RPA fitting or introduce a new nuclear dataset. All scientific results here are conditional calculations for the OL02 four-page parameter model, `needs_review: true`.

Only this worker prefix was written. No shared canonical/raw/PLAN/Bib/Git changes, new agent/run/session/credit or external retrieval. Reproducible Python: `gyro_global_contract.py`; executed output: `global-checks.json`. Parent must integrate reusable knowledge under its ownership; this is an audit artifact.

## Source and fixed model

Actual body remains `tmp/day24-critical-tac-007/arxiv-0211075v1.response`, SHA256 `3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb`, four pages. This is the three-author 25Nov2002 v1, not the unread 2004 journal body. Worker008 freshly read all four pages and independently checked figures;010 reuses that inspection rather than claiming a new figure fit.

Source locators: PDF2 Eqs2–4 and uniform-rotation definition; PDF2 left column aboveFig2 for parameters and already included δ𝒥; PDF3 Eq5/Fig3 for extra planar roots, Eqs6–7/Fig4 for aplanar onset and low-I yrastD; PDF4 Fig6 axis/caption for reference-subtracted energy. PDF3 HF continuation and PDF4 Ref6 retain the actual numerical-method boundary.

Axis order is(s,m,l); take

\[
\mathcal J=\operatorname{diag}(8.5,31,20)\quad[\hbar^2/\mathrm{MeV}],\qquad
s=(5.43,0,5.00)\quad[\hbar].
\]

These fixed positive effective inertias already contain the small odd-nucleon transverse response. No δ𝒥 is added. The gyros are frozen, both s/l spins are nonzero, and 𝒥m is strictly the largest. Changing any of those conditions changes the problem; a limit is identified explicitly below.

## Two different constrained problems

|Problem|Objective and constraint|Stationarity|Multiplier units|
|---|---|---|---|
|Fixed magnitudeω0|R(w)=−½wᵀ𝒥w−s·w; wᵀw=ω0²|Extremize R+½μ(w²−ω0²): (μ1−𝒥)w=s, hence I=𝒥w+s=μw.|μ:ℏ²/MeV, same units as inertia|
|Fixed magnitudeI0|H(I)=½(I−s)ᵀ𝒥⁻¹(I−s); IᵀI=I0²|Extremize H−½λ(I²−I0²): w=𝒥⁻¹(I−s)=λI.|λ:MeV/ℏ², inverse inertia|

For finite nonzero multipliers and nonzero vectors, λ=1/μ maps stationary states. It does **not** say that the two different objectives select the same global branch at arbitrary fixedω0 andI0. On a stationary branch |I|=abs(μ)|w|. Negativeμ permits anti-aligned w andI; the Euler equation w×I=0 requires collinearity, not positive alignment on every branch.

At |w|=0 or |I|=0 the sphere collapses to one point and its gradient constraint is singular: ordinary Lagrange-multiplier reasoning must not be applied as a regular chart. At I=s, w0, the fixed-I multiplier isλ0, whileμ diverges in the fixed-ω continuation. These are coordinate/constraint limits, not a measured phase transition.

## Tangent Hessians and an exact global certificate

At a stationary w*, permissible first-order perturbations obey δw·w*=0. The constrained Hessian is 𝒦ω=μ1−𝒥 restricted to that tangent plane. At stationary I*, δI·I*=0 and 𝒦I=𝒥⁻¹−λ1 restricted to its tangent plane. The different units, constraints and normalizations mean their eigenvalues must not be compared as frequencies.

There is a stronger, exact identity for any other point on the **same** sphere:

\[
R(w)-R(w_*)=\tfrac12(w-w_*)^T(\mu1-\mathcal J)(w-w_*),
\]
\[
H(I)-H(I_*)=\tfrac12(I-I_*)^T(\mathcal J^{-1}-\lambda1)(I-I_*).
\]

Proof: expand the quadratic objective, use its stationary gradient, then use equal norms to replace w*·δw orI*·δI by−δ²/2. These identities hold for every equal-norm point, not only the other enumerated stationary points.

Thus μ≥max𝒥 certifies a global fixed-ω minimum; λ≤min(1/𝒥) certifies a global fixed-I minimum. Strict inequalities make the quadratic difference positive for every distinct point. At μ=𝒥m andλ=1/𝒥m the certificate is semidefinite in full3-space, so the sphere geometry and the location of the zero direction must still be checked. These are sufficient certificates; an arbitrary stationary point without such a certificate is not called global merely because its local tangent curvature was computed.

## Global branch selection: why Fig4 has low-I D

The norm of the gyro vector is S=√(5.43²+5.00²)=7.381388758ℏ. The critical values remain ℏωc=.514639046MeV andIc=15.953810437ℏ.

|Range / ensemble|Global selection in this fixed model|Certificate and physical meaning|
|---|---|---|
|0<ω<ωc, minimizeR at fixedω|PlanarA, μ>𝒥m|Positive definite μ1−𝒥; the other outer planar solution is not the lowestR.|
|ω=ωc|A meets aplanar branch at wm0|One tangent quadratic zero direction, but a positive quartic cost; only one minimum at the joining point.|
|ω>ωc|Two aplanar ±wm minima, μ=𝒥m|Exact equalR, positive tangent Hessian at either nondegenerate point; no quantization of their coupling.|
|0<I<S, minimizeH at fixedI|PlanarD, λ<0 andμ<0|𝒥⁻¹−λ1 positive definite; w andI point oppositely. This is a true low-I energy minimum even though it is not a fixed-ω R minimum.|
|I=S|I=s,w0,H0|λ0, μ-chart diverges. This is the unconstrained quadratic-H minimum intersecting the sphere.|
|S<I<Ic|PlanarA,0<λ<1/𝒥m|Again exact global certificate.|
|I=Ic andI>Ic|Joining point, then two aplanar minima|λ=1/𝒥m; sphere geometry gives isolated quartic point and then two minima.|

This supplies an independent explanation of OL02 PDF3's statement that the classical yrast sequence first followsD, thenA, then the chiral branch. It also shows why a fixed-ω plot of the lowestR cannot simply be relabeled as the entire fixed-I yrast curve.

Concrete same-frequency warning from the calculation: at ℏω=.6MeV, the planarA stationary state has|I|=17.555718365ℏ andR=−7.326829288MeV, while the aplanar minimum has|I|=18.6ℏ andR=−7.371583636MeV. TheirR difference compares equalω and differentI. It is not a same-I experimental energy gap. At I=5ℏ, the fixed-I minimum hasλ≈−.03779079MeV/ℏ²,μ≈−26.46147ℏ²/MeV and|ω|≈.18895395MeV/ℏ; its anti-alignment cannot be dropped from the low-I yrast discussion.

## Full planar roots and local versus global behavior

For fixedω, planar roots solve

\[
\omega^2=s_s^2/(\mu-\mathcal J_s)^2+s_l^2/(\mu-\mathcal J_l)^2.
\]

There is one real root on each outer interval and, above Eq5's separate1.282266726MeV/ℏ threshold, two further roots in(𝒥s,𝒥l). At equality those two coincide in a double root. This is not the .514639 aplanar onset. The script brackets each interval, derives the middle minimum analytically, and inventories all resulting real stationary states; it does not select a branch from a single initial guess.

|Fixed ℏω,MeV|Distinct planar states|Distinct aplanar states|Global minimum|
|---|---:|---:|---|
|.2,.5|2|0|A|
|ωc≈.514639|2|0 additional, since it coincides withA|A joining point|
|.6,1.28|2|2|aplanar pair|
|1.3|4|2|aplanar pair|

Atω=.6 the planar roots haveμ≈−1.331253 and29.259531. The first has two negative tangent curvatures (local maximum ofR);A has one negative and one positive tangent curvature (saddle). Both aplanar signs have tangent eigenvalues≈3.217730 and20.329027ℏ²/MeV (strict local minima). Their stronger global certificate is semidefinite in ambient3-space. Atω=1.3, the newly present middle planar roots include a local maximum and a saddle; their appearance does not displace the global aplanar minima.

For fixedI, the planar secular equation uses I_s=ss/(1−λ𝒥s),I_l=sl/(1−λ𝒥l). Its poles and middle-root threshold are different: the latter is17.959922745ℏ for the selected parameters. That is a continuous constrained-root inventory threshold, not an experimental spin or a second chiral onset. At I=18.6 or30ℏ, four planar stationary states plus two aplanar states exist; the exact certificate selects the aplanar pair.

## Critical null direction: positive fourth order

At ωc let w*=(a,0,b),a=ss/(𝒥m−𝒥s),b=sl/(𝒥m−𝒥l). A tangent displacement alongm has zero quadratic curvature. Stay exactly on the sphere with

\[
w(t)=\sqrt{1-t^2/\omega_c^2}\,w_*+t\,e_m.
\]

The global difference certificate then gives

\[
\Delta R=\tfrac12 C\left[1-\sqrt{1-t^2/\omega_c^2}\right]^2
=\frac{C}{8\omega_c^4}t^4+O(t^6),
\quad C=(\mathcal J_m-\mathcal J_s)a^2+(\mathcal J_m-\mathcal J_l)b^2>0.
\]

The coefficient is6.385077328ℏ⁴/MeV³ when t is inMeV/ℏ. Direct finite-displacement costs at t=.04,.02,.01 are positive and converge to this quartic coefficient. Therefore the zero tangent quadratic direction does not create a continuous circle of equally minimal states at the threshold. The fixed-I construction replaces the ambient metric by𝒥⁻¹−1/𝒥m and gives coefficient 1.6018945935385565e-05 MeV/ℏ⁴. Three finite displacements of1,.5,.25ℏ independently check positive cost and convergence to that coefficient; the same isolated-point logic holds. No collective mass or real-time normal-mode calculation has been supplied, so this is not labeled anRPA frequency or a measured soft mode.

## Degenerate and zero-gyro limits: declare the changed problem

|Limit|What actually follows|What does not follow|
|---|---|---|
|ss→0 with distinct inertias andsl fixed|The fixed formula tends toωc=abs(sl/(𝒥m−𝒥l)), butws0 for all such stationary states; the vector lies in them-l plane.|A finite formal threshold is not three-axis chirality.|
|Both gyros0,distinct inertias|Ordinary triaxial quadratic rotor: ±m are the global minima on either nonzero sphere, and there is no positive finite onset from gyro competition.|No physical two-gyro nuclear chiral interpretation is imported.|
|𝒥s→𝒥m withss nonzero|At equality,(μ−𝒥s)ws=ss cannot be satisfied withμ=𝒥m and finitews. The distinct-inertia aplanar construction fails.|An infinite formula is not a quantitative nuclear exclusion threshold.|
|Explicit changed model𝒥s=𝒥m=31,𝒥l20,ss0,sl5,ω.6|wl=5/11 andws²+wm²=ω²−wl²; a full circle of stationary, isoenergetic global minima appears. A tangent zero direction persists along the circle.|This symmetry-degenerate family is not the isolated ±handed pair of the original model.|

The script checks four angles on that last circle against Cartesian Euler stationarity, equalR and a tangent zero eigenvalue; this is a deliberately changed-model control. It isolates true continuous degeneracy from the original threshold's positive quartic cost. All conclusions involving which nuclear axis/shape is realized remain outside this algebraic limit exercise.

## Fig6 reference-energy constant

In momentum variablesH=½Σ(Ik−sk)²/𝒥k. Onμ=𝒥m,Ik=𝒥mωk. Subtracting the actual Fig6 reference yields

\[
H-I^2/(2\mathcal J_m)
=-\tfrac12\left[s_s^2/(\mathcal J_m-\mathcal J_s)+s_l^2/(\mathcal J_m-\mathcal J_l)\right]
=-1.791583636\ \mathrm{MeV}.
\]

This is the source's horizontal classical chiral curve after rigid-rotor subtraction, not a Routhian. The result applies on both signs and all allowed magnitudes with the fixed parameters. It is neither a finite-quantum splitting nor the experimental350keV difference. Worker008 already checked the original ordinate and visual scale; no new plot digitization was needed.

## Execution and remaining route

The independent script executed successfully with72 bounded controls, including root inventories, exact objective-difference identities, global certificates, singular λ0/μ∞ chart, critical quartic costs and the explicitly changed symmetry-degenerate model. Counts summarize finite computations; correctness rests on the stated equations and assumptions. Tolerances are floating-point checks, not physical uncertainties or experimental confidence intervals.

The classical source parameter problem is now saturated for this task. More decimal precision or more sampling of the same sphere will not resolve actualHF behavior. The next informative route, if pursued, is explicitHF branch-continuation inputs/output and convergence, shape and effective-inertia variation, and a separate dynamical/quantum treatment before assigning normal modes or finite-system states. OL02's reportedHF onset.6MeV, method approximations, and planar/axial-l experimental alternative stay as source statements; none is certified by the fixed-parameter global algebra. No complexHF producer was chased in this worker.
