# E2 loop phase: state convention versus missing transition information

**Selection-rule boundary first:** the actual 022 block is ΔI=2 E2. M1 is forbidden on those edges, so no same-edge M1/E2 δ exists there. A δ on another ΔI=1 edge does not generally fix this E2 loop. This is a clarification of scope; 022 and the root project did not claim otherwise. The illustrative mixed-allowed counterexample below uses two initial I=3 states and two final I=2 states, not actual 134Pr inputs.

**Overlap reconciliation:** root identified the same loop relation and identical ±4 counterexample in existing `lange-kumar-hamilton-1982-multipole-admixtures` LKH82-D24P-004/005, including the distinction from a single-γ δ. Accordingly026 is a verified-no-op/self-audit of that existing result, not a new theorem or source. Its useful operational refinement is the explicit ΔI=2 M1 prohibition and separate allowed-spin scope for the generic example. Shared pages were not changed by this worker.

**Result:**022's central information claim is correct, with the necessary qualifications below. After conversion to four E2 amplitudemagnitudes, four unsigned strengths fix the Frobeniusnorm, but generically leave an invariant loopphase needed for abs(detM) and the singularvalues. This is not the arbitrary phase of an individual state or the sign ofdetM itself. A single signed M1/E2 mixingratio does not universally determine the four-edge E2loop. In the particular022 block,I→I−2,M1 is forbidden by the rank1 selectionrule, so a mixedline necessarily belongs elsewhere unless the spinblock itself is changed.

This is a bounded Day25 uncredited methodcomponent inside Day24. Worker number026 is not Day26; that card remainsclosed. No newpaper, actual134Prphase, response/beamtimeestimate, datafit, sourceHamiltonianchange, canonical/raw/Git write or coursecredit. New mathematical statements are `needs_review:true`.

## State phases and the forward reduced-matrix-element block

Let finalstates be f1,f2 with the sameJf, initialstates i1,i2 with the sameJi, and M_aj=〈f_a||E2||i_j〉. Fix the electromagnetic reduced-matrix-element and multipole conventions. Independent **state** rephasings are

\[
|f_a\rangle\mapsto e^{i\eta_a}|f_a\rangle,
\qquad |i_j\rangle\mapsto e^{i\chi_j}|i_j\rangle,
\qquad M\mapsto D_f^\dagger M D_i.
\]

Each entry transforms asM_aj→e^(−iηa+iχj)M_aj. Since a common shift of allfourstatephases has no effect, there are three effective phaseconventions for a connected nonzero2×2block. Four complexentryphases therefore leave one invariant phase. The invariant can be chosen as

\[
L=M_{11}M_{22}M_{12}^*M_{21}^*,\qquad
\Phi=\arg L.
\]

All four phasefactors cancel exactly inL. With nonzeroentries, one may choose threedesiredentryphases by stateconvention, but thefourth must retainΦ. If thephysical setting permits allfourRMEs to be real, the residual is a discrete **loop sign**, Lpositive ornegative. A zeroentry breaks this loop:Φ is then undefined, its interferenceamplitude vanishes, and the determinantmagnitude may already be fixed by the remainingmagnitudes. The missing-phase statement is therefore generic, not a universalclaim for every singular/selection-rule-limitedblock.

Invariants under these stateconventions include all fourmoduli, all row/columnnorms, the Frobeniusnorm, L, abs(detM), and singularvalues. However,

\[
\det M\mapsto e^{i(\chi_1+\chi_2-\eta_1-\eta_2)}\det M.
\]

Thus the complexphase ofdetM, or its sign in a real convention, is **not** itself physical state-phase information. Changing the sign of one whole row orcolumn changes that determinant sign but notL or the singularvalues. TraceM is also not an invariant of independent initial/final rephasings; it would require identification of the two spaces and a common similaritytransformation. The observable2×2block is a forwardmap between distinctspinspaces, not automatically a symmetricmatrix. Hermiticity relates it to the reverse-spinblock, not to an equality between its two forward off-diagonalelements.

## What four unsigned strengths determine

Write M=[[a,b],[c,d]]. Then

\[
S=\|M\|_F^2=|a|^2+|b|^2+|c|^2+|d|^2,
\]
\[
D=|\det M|^2=|ad|^2+|bc|^2-2\operatorname{Re}(ad b^*c^*)
=r^2+s^2-2rs\cos\Phi,
\]
\[
\sigma_\pm^2=\frac{S\pm\sqrt{S^2-4D}}2,
\qquad r=|ad|,\quad s=|bc|.
\]

Fourmoduli determineS,r,s, but not generallycosΦ and henceD. For a generalcomplexblock, D lies in[(r−s)²,(r+s)²] asΦ varies. In an otherwise unrestrictedrealblock with fournonzeroentries only the twoendpoint choices occur. Extra physicalconstraints may restrict these choices; none is inferred here for actual134Pr. OnlycosΦ enters these singularvalues; even a measuredD would not necessarily determine the fullorientedphase±Φ.

Care is needed with “width.” Raw E2photonpartialrates carry Eγ^5 and the reduced-strength normalization. The amplitudemagnitudes in these equations are obtained only after removing those knownkinematic factors and using a consistentB(E2)=abs(RME)²/(2Ji+1) convention. Because Ji iscommonwithinthisblock, its factor iscommon; the fourphotonenergies generally are not. The sum of fourunadjustedrawγrates is not automatically the Frobeniusnorm ofM.

Population lifetimes plus completebranching,conversion/multipolarityaccounting can establish absolute partialrate magnitudes. They do not add a coherent RMEphase merely by establishing an absoluteclock. Once the fourmagnitudes arealreadyknown, an additional populationτ contains no missingloopsign by itself. A genuine phase-sensitive time/angularresponse would be additionalinformation, not a consequence of a lifetimevalue alone.

This qualifies022's wording precisely: **ratios alone** leave columnnorms andsigns; **fourabsoluteE2magnitudes** remove thenormambiguity but generally retain theloop ambiguity. No claim is made that a singularvalue is itself measured by a conventional lifetimeexperiment.

## An invariant is not automatically an observed interference

L is a property of the operatorblock and states that cannot be changed by arbitrary phaseconventions. It can enter suitably coherent closed-pathresponses or other combinations that tie the four amplitudes together. That is different from asserting that independent spontaneousdecays to orthogonallevels interfere in the suppliedbranchingdata. They ordinarily contribute separate probabilities to such width measurements; those measurements supplyabs(M)^2,notL.

Whether any particular nuclearresponse can identifyL requires its own coherent pathways, operators, level resolution, initialpreparation and response/calibrationmodel. This note proposes no universalexperimental sufficientset or uncalibratedmeasurementbudget. Absence of phaseinformation in the specifieddata is an informationboundary, not proof thatL is unobservable inprinciple or that any chosen measurement will recoverit.

## Why one signed M1/E2 mixingratio is insufficient

On an individualtransition where bothmultipoles are allowed, choose a stated convention and write

\[
\delta_{aj}=\kappa_{aj}\,
\frac{M^{E2}_{aj}}{M^{M1}_{aj}}.
\]

κ contains the energy,unit and radiation-multipole conventions. Both RMEs acquire the **same** statephasefactor, soδ is state-gaugeinvariant. A signedrealδ fixes the relative E2/M1 sign on thatoneedge under the real/conventionassumptions; it does not fix an absolute E2sign acrossstates. Even a knowncomplexδ gives only thatoneoperator-relativephase. No generalrelation to the otherthreeE2edges follows.

In022's actualPE06blocks,17→15 and18→16 haveΔI2. A rank1M1operator cannot connect thoseedges; the E2blockitself has no physicalsame-edgeM1/E2δ. A signedδ from a nearbyΔI1mixedtransition belongs to a differentstatepair. Connecting it to the E2loop requires additional actualstate/operator relations or interferenceinformation; the energy/bandlabels alone do not providethatbridge.

To demonstrate the general claim in a **different, explicitly mixed-allowed block**, take same-parity Ji=3→Jf=2 so both M1 andE2are allowed, and use normalizedarbitrarymultipoleunits:

\[
M_A^{E2}=\begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad
M_B^{E2}=\begin{pmatrix}1&2\\3&-4\end{pmatrix},\qquad
M^{M1}=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Set κ11=1 by the normalization of this illustrativeedge. Both systems have the same fourE2strengths[[1,4],[9,16]], the same M1magnitudes and δ11=+1. With identicalenergies andotherchannels they can have the same integratedpartialrates andpopulationclocks. Yet

|Quantity|A|B|
|---|---:|---:|
|FrobeniusnormsquaredS|30|30|
|LoopL|+24|−24|
|abs(detM)²|4|100|
|Singularvaluessquared|29.866069,.133931|26.180340,3.819660|

The differingL proves these twoE2blocks are **not** related by statephasechoices. Changing onlyoneE2entrysign is not a gaugetransformation of thefullstates/operators. By contrast, flippingonecomplete row in **both** E2andM1changesa stateconvention and leavesδ,Landallmagnitudesunchanged. For a mixedline on anychosenedge, a change on anotheredge can supply the same typeofcounterexample. This is a conditionalcounterexample, not a symmetric-Q/source-alpha fit or an actual134Prphase assignment.

The result does not say thatsignedδ is uninformative; it supplies important localinterferenceinformation. It says thatoneedge'slocaloperatorphase is not theentirefour-edge E2loop. Additional justifiedcross-edgerelations could change the identificationproblem, but they must be stated as additional input.

## Reproducible check and completion

`loop_phase_check.py` verifies the complex row/column rephasinglaw, invariantL/moduli/singularvalues, the determinantphase law, the analyticD/SVD identities, the nondegeneraterealcounterexample and a shortcomplexphaseinterpolation. Results are in `loop-phase-results.json`. It does not fitdata, recoverphysicalRMEphases, impose a physicalM1onPE06'sΔI2edges or changeitsenergyHamiltonian. No controlcount is used as scientific certification.

The 022 claim is therefore retained with the explicit distinctions **phaseconvention vsloop**, **ratio vsabsolutestrength**, **invariant vsa measuredcoherentresponse**, and **allowedmixededge vsΔI2E2block**. No further numericalscan can produce the missing physicalphasewithout new, actuallyconstraining input.
