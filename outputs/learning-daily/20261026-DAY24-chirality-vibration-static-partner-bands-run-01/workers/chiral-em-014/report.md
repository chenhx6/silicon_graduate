# PartII electromagnetic outputs: local-rate averaging, not collective transition amplitudes

**Direct answer:** this paper calculates **intraband** B(M1) and B(E2) by averaging **already-squared local semiclassical TAC B values** with the probability density of a **single** collective state. It does **not** construct coherent transition amplitudes between different collective states, sectors or exact angular momenta. It therefore partially fills CH16's electromagnetic-output gap—smooth intraband strength trends and fluctuation corrections—but does not recover signed interband RME, inter-sector selection-rule amplitudes, M1/E2 relative phase, experimental mixing ratios or a full decay network. The paper explicitly acknowledges failure to reproduce PRM odd–even strength staggering because I is not a good quantum number.

## Identity, original and coverage

Fresh Crossref and official arXiv metadata verify **X.H.Wu, Q.B.Chen, P.W.Zhao, S.Q.Zhang and J.Meng**, *Two-dimensional collective Hamiltonian for chiral and wobbling modes. II. Electromagnetic transitions*, **Physical Review C98,064302(2018)**, DOI **10.1103/PhysRevC.98.064302**, published2018-12-03. Initial scoped Wiki search found no existing source or claims for this exact PartII, only unrelated articles sharing the064302 article number; CH16 is the direct predecessor, cited as Ref1 in the actual paper.

Actual body: **arXiv1809.04418v2**, `https://arxiv.org/pdf/1809.04418v2`, HTTP200 `application/pdf`, valid `%PDF`, **276035bytes**, **17pages**, SHA256 **7d7c12ebc754f23721bd5367acc050c54dd3cf0f03f2f7480de407c1f3493dcb**. PDF sidebar/date identifies **13Sep2018v2**, titlepage is dated**14Sep2018**. It precedes the December journal publication; VoR was not separately obtained or compared. All locators below belong to this17-page author version.

Reading: **all17text pages**, including main text1–14 and references14–17; **all4figures** and their legends/axes were visually inspected (PDF9–12); **allEqs1–21** visually read on PDF4–7/11. There are **no numbered tables**. Active recall was frozen before body reading and explicitly marked CH16-primed/unscored. No author code, original grids or independent spectrum/EM producer was run; no confidence interval or quantitative fit metric is claimed.

## What the electromagnetic operator prescription actually is

PDF5 **Eqs6–8** define local TAC rates as sums of squares of orientation-dependent components:

- Eq6: semiclassical B(M1), using intrinsic magnetic moments `mu_k=sum_(p,n)(g_tau−g_R)<j_(tau,k)>`.
- Eq7: intraband B(E2,I→I−2), with `Q20=Q0*cos(gamma)`, `Q22=Q0*sin(gamma)/sqrt(2)`.
- Eq8: intraband B(E2,I→I−1), a different angular combination of the same quadrupole moments.

The angles used inside those formulas are **theta_J,phi_J, the direction of total angular momentum**, not automatically the collective coordinates theta,phi specifying the cranking omega vector. **PDF6 Eqs9–10** forms `J_k=<j_k>+J_k(inertia)*omega_k` and obtains the orientation from its components. At a self-consistent TAC minimum I/J is parallel to omega, so the two directions coincide; away from that minimum they generally differ. This distinction is essential because the collective average samples off-minimum orientations. A replay must handle quadrants consistently; the printed tangent formulas alone do not document an actual branch/atan2 implementation.

For1DCH, **PDF6 Eqs11–13** state

`B_CH[X] = integral_(−pi/2)^(pi/2) dphi sqrt(B(phi))*|Psi(phi)|²*B_TAC[X](phi)`.

For2DCH, **PDF7 Eqs15–17** state

`B_CH[X] = integral_0^pi dtheta integral_(−pi/2)^(pi/2) dphi sqrt(w(theta,phi))*|Psi(theta,phi)|²*B_TAC[X](theta,phi)`.

Here X denotes the particular M1 or E2 channel. The determinant `w=detB` and the full Pauli operator, including cross-mass derivatives, are retained in **PDF4 Eqs3–5**. Measures are sqrt(B)dphi and sqrt(w)dtheta dphi. The rate weights are not unweighted |Psi|² and not flat angular histograms.

This is an **expectation of a positive local rate function**, `Bbar_i=<B_TAC>_(rho_i)`. There is no Psi_f, no collective transition kernel `T_fi(theta,phi;theta′,phi′)`, no final-state I_f wavefunction or coherent sum before squaring in these formulas. The displayed collective state index selects the density used for a band's local in-band rate; I→I−1/2 labels in B_TAC do not turn that single-density average into an exact between-I matrix element.

### Consequences for phase and selection rules

These are deductions from the explicitly printed prescription, not claims that the authors attempted and failed a full coherent calculation:

1. Any wavefunction changes that preserve its |Psi|² leave this EM functional unchanged. The formula does not access relative phases between distinct collective states, or interference between different orientation points. States' densities/nodes can still produce different averaged rates, so “phase blind” does not mean all symmetry sectors must have equal B values.
2. Even/odd reflection labels categorize the collective eigenstates but the **intraband rate average is not an off-diagonal transition operator connecting two such labels**. Consequently one cannot derive inter-sector/chiral/signature transition cancellation or a complete selection-rule matrix from Figs1/3.
3. M1 and E2 strengths are averaged separately. Their relative signed amplitude/phase is not supplied, so this source does not generate signed delta, polarization or interference observables. A numerical ratio of averaged B values would not repair that loss.
4. The paper lists **interband E2 dominance for wobbling** and **vanishing high-spin interband E2 in an ideal chiral limit** as background criteria on **PDF3**. It then explicitly limits its new calculation to **intraband** rates. Those interband criteria are **not tested by the new curves**.

No reading here says every probability-averaged observable is invalid. This is a well-defined fluctuation correction to the specified semiclassical local rate. Its domain simply differs from full coherent quantum transition spectroscopy.

## Shared inputs and inherited model version

**PDF7 SecIII:** oneh11/2 proton particle plus oneh11/2 neutron hole; gamma=−30deg; C_pi=.25MeV, C_nu=−.25MeV; irrotational inertias with J0=40hbar²/MeV. Effective g differences are **g_p−g_R=1, g_n−g_R=−1** and **Q0=1eb**. The same assignments are used in **1DCH,2DCH,TAC and PRM** comparisons. These are declared schematic common inputs, not measured g values/Q moments or fit results for135Nd/133Ce.

**PDF7–8 opening SecIV** explicitly says the calculation follows PartI/CH16 and its **periodic boundary** basis. Thus this follows the later periodic scheme, **not the original CH13 box/wall boundary**.1D potential theta-minimization is restated in PDF4;1D inertia is referred to Ref70/CH13 and2D potential/masses to Ref1/CH16, rather than reprinted in full.

**Important unresolved version detail:** PartI displayed both a baseline Omega_theta=Omega_phi=0 cranking mass and an assumed1.10MeV mass correction for low-spin spectra. This PartII body says “follow the same … calculations” but does **not explicitly print an Omega choice, new mass grid, basis-cutoff convergence or a separate low-spin inertia calibration**. A search/read of all17pages found no explicit1.10MeV value or new equation selecting it. Therefore it is **not established here whether every displayed EM curve uses the baseline or corrected finite-Omega inertia**. The implementation/inherited-version contract remains incomplete without the actual input/producer. Do not claim that PartII independently fixes the PartI low-spin spectral failure or chooses a microscopic Omega.

The initial theoretical ancestry GCM/ATDHF/ASCC is reviewed but does not change this inherited cranking-mass limitation. No new residual-interaction-complete ASCC calculation, pairing solution, multi-orbital nucleus-specific calibration, good-I projection or original-code recovery is shown.

## What the four figures actually support, including failures

| Figure / PDF | Direct content | Bound on inference |
|---|---|---|
|**Fig1 /9**|1DCH(+)/(−) in-band M1,deltaI2E2,deltaI1E2 vsI; left=TAC comparison,right=PRM band1/2. E2deltaI2 trends/scale close; M1 anddeltaI1E2 PRM alternate strongly while CH curves remain smooth.|Model benchmark with common declared inputs, not experimental data. Large pointwise alternating deviations cannot be called complete quantitative agreement.|
|**Fig2 /10**|1D effective azimuth `phi_eff=<|phi|>` compared with TAC phi; fluctuations leave phi_eff below90deg at high spin.|An absolute/folded moment, not signed phi/handedness or a measured angle.|
|**Fig3 /11**|2DCH lowest(++),(+−),(−+),(−−) in-band rates; same local-rate comparison channels. Four curves are close yet distinct; smooth rates miss PRM odd–even structure.|No off-diagonal transitions between the plotted sectors. No fitted residual/CI or higher-configuration validation supplied.|
|**Fig4 /12**|2D effective cranking angles `phi_eff=<|phi|>` and `theta_eff=<pi/2−|pi/2−theta|>`; low-spin nonzero folded phi, high-spin values short of90deg.|Folded coordinate moments characterize model spread. Similar folded means do not uniquely determine geometry, localization or all coherent transition amplitudes.|

### Explicit retained failure: odd–even staggering

**PDF9–10** says there is a “noticeable difference” for1DCH B(M1) and B(E2,I→I−1): PRM has strong odd–even staggering whereas CH does not. **PDF13** repeats this for2DCH and attributes it to angular momentum not being a good quantum number. The summary **PDF13–14** retains the B(M1) limitation. PRM Ref22 is the Koike/Starosta/Hamamoto selection-rule model lineage, not new measurement. A defensible result is **reasonable smooth trends/amplitudes apart from staggering**, not recovery of the detailed discrete selection-rule pattern.

### High-spin behavior and what it means

**PDF8–9/12–13:** in this schematic TAC, around **I≈37hbar** the stationary axis becomes i and the local M1 drops to zero; CH densities sample a spread around that orientation and their averaged M1 remains small but nonzero/smooth. The source calls high-spin fluctuations theta/phi wobbling. This supplies a particular model mechanism for avoiding an exactly-zero local mean-field rate, **not a measured wobbling assignment, a universal37hbar threshold or proof of static chirality**.

As a small source-parameter check, the **local** Eq7 at theta_J=phi_J=90deg with Q0=1eb,gamma=−30deg gives `B(E2,I→I−2)=5/(32*pi)=.049735919716e²b²`; Eq8 goes to zero. This matches the displayed roughly.05 plateau scale. `conditional-local-limit.json` records this algebra; it is **not** a replay of any collective curve. M1 vanishing at that orientation also requires vanishing transverse intrinsic magnetic components, as in the aligned stationary-model solution; angular coordinates alone do not null an arbitrary mu vector.

**PDF13** says near I≈15hbar the effective folded theta/phi values of all four states become nearly equal and “might be regarded as a signal” for static chirality. Keep that **author-provisional/model** wording. A common pair of folded mean angles is insufficient by itself to establish the full distribution, signed orientation, tunneling splitting or a laboratory order parameter. The current source does not add such missing coherence by averaging rates.

### Low-spin reading boundary

The figures include low spins and show the general in-band trends, but no new independent low-spin spectral test or finite-Omega sensitivity panel is given. **PartI's baseline low-spin energy failure remains part of the inherited validity envelope** until the actual mass prescription used for these states is identified. The explicit new failure acknowledged here is absent staggering; it is present over the PRM spin sequence, not confined to one end. Do not infer that close deltaI2E2 curves validate every mass/boundary/phase ingredient.

## Spin mapping, observables and transferable scope

**PDF6 Eq14 and PDF7 Eq18** use `J_coll=∫measure |Psi|² J_TAC`, then **I_coll=J_coll−1/2**. This is an expectation-value mapping, not exact laboratory angular-momentum projection. The authors explicitly invoke its lack of goodI to explain absent staggering. They compute smooth intraband rates along these mapped bands at sampled cranking frequencies; no exact initial/final-I collective-wavefunction pair is used.

The paper creates no new experimental tau, gamma branching ratios, conversion coefficients, mixing ratio, polarization, g factor or covariance. **It cannot be cited as an independent135Nd/133Ce partner-band measurement, a signed interbandRME calculation, or a complete counterpart to MU07/QI09 EM predictions.** A future nucleus-specific use would need actual configurations/inertias/shape/EM inputs, a controlled mass and boundary prescription, and a proper coherent transition framework if cross-band rates or phase-dependent observables are requested.

## Literal formula boundary in this read version

**PDF4 Eq2** prints the1D Pauli term with no trailing `partial_phi` after `1/sqrt(B(phi))`; the visual formula itself has this omission, so it is not merely text extraction. The referenced CH13 operator and the source's own2D Eq4 have the expected second-derivative divergence structure. Treat Eq2 as a **literal author-version transcription boundary**, not a newly defined first-order Hamiltonian or evidence of an executed-producer error; do not silently replace the equation when quoting this body. This does not alter the unambiguous positive-rate averages Eqs11–17. No claim is made about whether the final PRC typesetting corrected it.

## Atomic draft claims for leader knowledge writeback

All use `needs_review:true`, actual arxiv1809.04418v2 provenance, model-only kind. Suggested source slug `wu-2018-two-dimensional-collective-electromagnetic-transitions`; leader controls canonical persistence.

|Candidate|Statement|Kind|Exact locator|
|---|---|---|---|
|WU18-D24-001|PartII computes intraband M1/deltaI2E2/deltaI1E2 by averaging local semiclassical TAC B values with a single collective-state probability measure; it does not evaluate coherent off-diagonal collective transition amplitudes.|direct-method-and-scope|PDF3 endintro;PDF6 Eqs11–13;PDF7 Eqs15–17|
|WU18-D24-002|The local formulas use theta_J/phi_J from totalJ, generally differing from crankingtheta/phi off the stationary solution; collective sampling must preserve that mapping.|direct-coordinate-contract|PDF5 Eqs6–8/laterparagraph;PDF6 Eqs9–10|
|WU18-D24-003|Separate squared-rate averages retain density/nodal effects but not between-state relativephase or orientation-interference amplitudes. Foursector rates are not a complete intersector selection-rule or signedRME matrix.|labelled-method-inference|PDF5–7 Eqs6–17;PDF11 Fig3|
|WU18-D24-004|The shared benchmark inputs are singleh11/2 particle-hole,gamma−30deg,C_pi/nu±.25MeV,J0=40,gp−gR=1,gn−gR=−1,Q0=1eb acrossCH/TAC/PRM; these are not target-nucleus measured EM inputs.|direct-input-contract|PDF7 SecIII|
|WU18-D24-005|Periodicity andCH16 calculation lineage are explicit, but PartII does not identify the exact Omega/inertia variant amongPartI baseline/corrected versions; low-spin spectral repair and actualproducer convergence remain unverified.|inherited-input-and-reproducibility-boundary|PDF4 modelrefs;PDF7–8 SecIVopening;whole-body absence ofOmega choice|
|WU18-D24-006|Figs1/3 show smooth in-band scales/trends and nonzero high-spinCH M1, but PRM odd–even M1/deltaI1E2 staggering is not reproduced. Authors attribute this toI notgood; keep failure with the benchmark support.|direct-benchmark-and-adverse-evidence|PDF9–10 Fig1discussion;PDF11 Fig3;PDF13 conclusion|
|WU18-D24-007|Effectiveangles usefolded|phi| andpi/2−|pi/2−theta|; they describe modelspread, not signed handedness. AuthorI≈15static signal language is provisional and cannot certifygeometry frommeans alone.|direct-definition-and-inference-boundary|PDF8 Eq19;PDF11 Eqs20–21;PDF13 firstparagraph|
|WU18-D24-008|Jcoll is measure-averagedJTAC withIcoll=Jcoll−1/2, not exactIprojection; this limits detailed discrete selection-rule reproduction.|direct-comparison-contract|PDF6 Eq14;PDF7 Eq18;PDF10/13Igoodparagraphs|
|WU18-D24-009|The source lists interband E2 diagnostics as background but calculates onlyintraband outputs; it leavescross-band amplitudes,phase,delta andexperimentalτ/branch networks open.|source-scope-and-transfer-boundary|PDF3intro;PDF5–7method;PDF13–14summary|
|WU18-D24-010|Readv2's1DPauli Eq2 omits the trailing derivative; retainthat literalversion boundary and refer toCH13/2DEq4 forthe established operator, without inferring anauthorcodefailure.|literal-version-boundary|PDF4Eq2/Eq4;CH13PDF5Eq11|

## Completion state

The bounded one-paper unit is complete at this author-version/method scope. It **partially resolves the missing intraband EM output**, while **coherent interband/phase/selection-rule amplitudes and exactI remain open**. No failed endpoint was looped, no additional paper was opened to fill those gaps, and no model result was promoted to experiment. Only this worker prefix and `tmp/day24-chiral-em-014/` were written; shared canonical/raw/PLAN/Bib/Git, sessions and course credits were untouched.
