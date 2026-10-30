# Critical TAC onset — direct author-version source unit

**Main result:** the actual early author manuscript derives a configuration- and inertia-dependent onset of *uniform classical/aplanar mean-field rotation*. It does not calculate a finite-nucleus quantum doublet splitting or determine an experimental universal minimum spin. For its 132La input, the algebraic estimate is hbar*omega_crit=0.51464 MeV; the self-consistent HF search reports chiral solutions only from 0.6 MeV. The authors explicitly note that this is higher than the frequencies where the candidate experimental bands appear and retain a planar/axial-l alternative interpretation.

## Identity, access and version contract

Fresh Crossref metadata verifies **“Critical Frequency in Nuclear Chiral Rotation”**, P. Olbratowski, J. Dobaczewski, J. Dudek and W. Płóciennik, Physical Review Letters **93**, 052501 (2004), DOI **10.1103/PhysRevLett.93.052501**; deposited publication date 2004-07-29. The anticipated DOI was checked, not simply adopted.

The actual acquired body is **arXiv:nucl-th/0211075v1, 25 November 2002**, with **three authors**: Olbratowski, Dobaczewski and Dudek. Official URL `https://arxiv.org/pdf/nucl-th/0211075v1` returned HTTP200 `application/pdf`, **252547 bytes**, valid `%PDF`, **4 pages**, SHA256 **3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb**. The arXiv API associates it with the PRL DOI; this association does not erase its author/date/version difference from the 2004 four-author metadata.

Exactly three motivated body routes were used:

1. Official arXiv, following its title+author API result: full four-page manuscript acquired.
2. Crossref-registered APS harvest endpoint `https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.93.052501/fulltext`: HTTP401, 69-byte JSON, no PDF.
3. Coauthor Dobaczewski's actual institutional homepage, then its “Earlier submitted papers” link and target article link: `https://users.fuw.edu.pl/~dobaczew/earlier.html` identifies this title with PRL93(2004)052501 and the 2002 arXiv item; `https://users.fuw.edu.pl/~dobaczew/chir43w/chir43w.html` supplies readable author-hosted HTML, HTTP200, 41413 bytes, SHA256 **e8bf9524c7da3e384fd7c9bf61c85427284e3b3c8f7381e92d5a319b500aff90**. It also has the same three-author early manuscript, not demonstrably the final four-author VoR.

**VoR body remains unverified.** All numerical/formula claims below must be attributed to this explicit 2002 v1 author manuscript. The author HTML's LaTeX2HTML equation numbers differ from the PDF; use PDF Eq. labels below and HTML anchor names only as navigation aids. No final-version equivalence or word-for-word comparison was completed.

## Actual reading coverage

All four PDF pages were read as text and freshly rendered at 1.6× for visual inspection. **Figs1–6 and Eqs1–7, including 4a–c, were visually read.** No source claims were found for this exact article in the initial scoped knowledge search; existing GR18-4 contains the generic critical-frequency statement. The new information is the actual derivation, parameter dependency, model/quantization boundary and adverse comparison/alternative in the directly read v1, not a newly measured critical frequency.

- PDF1: premise, pi(h11/2)^1 nu(h11/2)^-1 in 132La, beta≈.25/gamma≈45deg, non-self-consistent single-particle response probe and Fig1.
- PDF2: Eq1 gyro approximation, separate self-consistent axial cranking extraction/Fig2, Kerman–Onishi parallelism, constant-inertia gyroscope model and variational Eqs2–4.
- PDF3: extra-planar-branch threshold Eq5/Fig3; chiral branch Eqs6–7, Fig4; actual HF continuation/search and experiment-frequency mismatch.
- PDF4: Figs5–6, experimental comparison and planar/axial-l alternative, conclusion and numerical/method footnotes in references6/10.

## Derivation, with its assumptions attached

In PDF2 Eq1 and the following axial-cranking paragraph, odd-proton and odd-neutron-hole alignments are approximately frozen along s and l. Small perpendicular response contributes delta J_s/l already included in the extracted inertias. These should **not be added a second time** to the subsequent classical tensor.

The frozen-body model uses constant diagonal J_s,J_m,J_l and gyro vector s=(s_s,0,s_l), with total I=J*omega+s. It seeks **uniform rotations**: omega constant in the body frame and omega×I=0, hence I parallel to omega. This uniformity condition is essential; the calculation does not model an arbitrary time-dependent precession or vibrational trajectory.

At fixed |omega|, extrema of R=−L=H−omega·I follow from

`R + mu*omega^2/2 = [(mu-J_s)omega_s^2+(mu-J_m)omega_m^2+(mu-J_l)omega_l^2]/2 - s_s*omega_s-s_l*omega_l`.

Thus Eq4 gives `omega_m(mu-J_m)=0`, `omega_s=s_s/(mu-J_s)`, `omega_l=s_l/(mu-J_l)`.

- **Planar branch:** omega_m=0; omega and I lie in s–l plane with both frozen spins. The additional planar solutions appearing only above Eq5, **omega_thr**, are a different threshold from the chiral bifurcation.
- **Aplanar branch:** mu=J_m; s/l components are fixed by Eq6, while `omega_m=±sqrt(omega^2-omega_crit^2)`. Eq7 is

`omega_crit = sqrt[(s_s/(J_m-J_s))^2 + (s_l/(J_m-J_l))^2]`.

At equality omega_m=0 and this branch meets planar A; strictly nonzero m components and two handed signs require omega>omega_crit. With J_m the largest inertia, the constrained Routhian has nonnegative Hessian diagonal `(J_m-J_s,0,J_m-J_l)` and positive curvature on the tangent plane at a genuine chiral solution. This local-minimum statement is a conditional algebraic inference from this model, not a source-reported general stability theorem for arbitrary microscopic motion. Source PDF3 after Eq7 places the yrast line on the chiral branch beyond the critical point specifically because J_m is largest.

The denominator gaps and fixed alignment assumptions matter. Coincident J_m=J_s or J_l with a nonzero corresponding frozen spin makes this formula singular; weak/vanishing alignments or changing inertias alter the branch and must be rederived. These are model-domain observations, not measured nuclear boundaries.

## Source parameters and one conditional algebra check

PDF2, axial-cranking paragraph immediately before Fig2, gives **s_s=5.43 hbar, s_l=5.00 hbar, J_s=8.5, J_m=31, J_l=20 hbar²/MeV**. Fig2 describes the slopes up to hbar*omega≤.5MeV. The independent arithmetic in `conditional-algebra.json` uses only these printed parameters:

| Quantity | Result | Scope |
|---|---|---|
| hbar*omega_s / hbar*omega_l on chiral branch | .2413333333 / .4545454545 MeV | Eq6 |
| hbar*omega_crit | **.5146390463 MeV** | Eq7; compatible with source .51 |
| hbar*omega_thr | **1.2822667260 MeV** | Eq5; compatible with source 1.28; extra planar branches, not chiral onset |
| Classical I_crit=J_m*omega_crit | **15.95381044 hbar** | Continuous classical magnitude, not an assigned experimental quantum spin |
| At hbar*omega=.50MeV | omega_m²<0 | No real aplanar solution under these frozen parameters |
| At .60MeV | omega_m=.3084585093 MeV/hbar; |I|=18.6hbar | Conditional classical branch, not the actual HF solution |
| omega×I arithmetic residual | ≤8.9e−16 in declared units | Verifies stationarity algebra for chosen check points; no HF producer replay |

The source's **HF onset .6MeV is distinct from the classical .51464MeV estimate**. It is a reported numerical search/continuation result; no raw HF trajectories, search step or error bar were recovered, so a more precise HF critical point is not inferred.

## Microscopic inputs, counterevidence and quantum boundary

**Inputs and scope:** PDF1 has pi(h11/2)^1 nu(h11/2)^−1 in 132La and approximately stable beta=.25/gamma45deg. PDF4 reference6 explicitly describes **Skyrme HF without pairing**, **HFODD v2.00k**, **14 spherical oscillator shells**, **SKM***, only parity conserved and **time-odd fields switched off** due to their uncertainty. The Fig1 s.p. response is deliberately **non-self-consistent**, starting from omega=0, whereas the axial bands and planar/chiral HF branches are self-consistent within those stated constraints. “Self-consistent” does not mean pairing/time-odd contributions were included.

**Adverse comparison and alternative:** PDF3 final paragraph and PDF4 Fig6/discussion explicitly say the HF .6MeV onset is significantly higher than the frequency at which the two experimental candidate bands appear. PDF4 discusses the roughly350keV observed band separation and offers lower=planar, upper=axial-l HF solutions as a tentative alternative that also reproduces the energy separation. Those are competing model descriptions, not proof of either experimental geometry. The final summary retains the tension rather than claiming a matched measured phase boundary.

**Finite quantum splitting:** The ±omega_m solutions are degenerate handed classical/mean-field branches. Neither Eqs2–7 nor the acquired calculation quantizes their tunneling or computes a laboratory partner splitting/phonon spectrum from the broken-symmetry states. Source PDF2 explicitly distinguishes the classical features from particle-core approaches to resulting quantum states; PDF4 compares different HF stationary branches to bands. Therefore .51464/.6MeV cannot be used to certify an experimental static-chirality spin or exclude low-spin chiral vibration. The continuous Icrit above is not I(I+1), an angular-momentum-projected eigenstate, or an experimental spin threshold. This manuscript's 132La inputs cannot be transferred numerically to 128Cs or 135Nd.

**Literal-v1 ambiguities to preserve:** PDF2 after Eq1 says spins s_s/s_l are fixed “along the long and short axes, respectively,” reversing Eq1 and PDF1/Fig1's s-proton/l-neutron mapping; the conditional check follows the explicit Eq1, later model definition and Eq6. PDF3 last paragraph says larger inertia differences lower omega_crit, consistent with Eq7, but PDF4 first paragraph literally says moving gamma toward30deg could “decrease the differences” and lower omega_crit. The latter wording is not algebraically consistent at fixed nonzero s_s/s_l, so it must not be reused as an established monotonic rule without the final version/actual deformation–inertia mapping. These are bounded ambiguities in the acquired v1; they are not a judgment that the four-author2004 published paper contains them or is wrong.

## Reusable claim drafts for leader writeback

All drafts retain `needs_review:true` and explicit `arxiv:nucl-th/0211075v1` version attribution. Suggested new source identity should preserve the 2004 PRL citation metadata and separate **actual_body_version: 2002 v1** rather than replacing the publication author list with the manuscript's three names.

| Candidate ID | Draft statement | Kind/evidence | Exact locator |
|---|---|---|---|
| OL04-D24-001 | The acquired2002 v1 author manuscript associated with PRL93,052501 derives chiral uniform-rotation onset from frozen s/l gyroscopes and a constant diagonal inertia tensor: omega_m=0 or mu=J_m; the latter fixes omega_s/l and requires omega≥omega_crit of Eq7. At equality it is planar; two nonzero handed signs occur above it. | author-model-derivation; direct version-specific body | PDF2 Eqs2–4 and uniform-rotation paragraph; PDF3 Eqs6–7 |
| OL04-D24-002 | Printed132La s_s/s_l=5.43/5.00 and J_s/J_m/J_l=8.5/31/20 give classical hbar*omega_crit=.514639MeV; Eq5's1.282267MeV extra-planar-branch threshold is distinct. The source reports HF chiral continuation from.6MeV, not a measured critical frequency or finite quantum splitting. | source-parameter-conditional-algebra plus author numerical result | PDF2 pre-Fig2 inputs; PDF3 Eqs5/7 and HF continuation paragraph; conditional-algebra.json |
| OL04-D24-003 | HF uses132La fixed particle-hole configuration, SKM*, no pairing,14 oscillator shells and time-odd fields off. Frozen s.p. probe is non-self-consistent; axial and planar/chiral bands are self-consistent within these inputs. Extracted inertias already include the small odd-nucleon transverse response. | model-input-and-scope | PDF1 configuration/Fig1; PDF2 Eq1/axial paragraph; PDF4 Ref6 |
| OL04-D24-004 | This v1 explicitly finds HF onset above experimental candidate-band frequencies and retains planar/axial-l as a tentative alternative reproducing their energy separation. Aplanar mean-field onset is model support/limitation, not exclusive laboratory doublet identification or a universal minimum spin for128Cs/135Nd. | author competing interpretation plus inference boundary | PDF3 last paragraph; PDF4 Fig6/discussion/conclusion |
| OL04-D24-005 | Official arXiv PDF and author HTML agree on the early three-author manuscript; the verified2004 PRL metadata has four authors including Płóciennik. APS full body was not accessible. Eq1 axis-prose reversal and the later inertia-gap wording ambiguity remain bounded to this read v1 pending final-version comparison. | version-lineage-and-literal-boundary | PDF1 author block; PDF2 Eq1 prose; PDF3 last/PDF4 first paragraphs; crossref.json; author-earlier.json |

## Output and scope

`receipt.json` consolidates routes, hashes, actual reading coverage and version boundary. All output is in this worker prefix; temporary PDF, text and renders are in `tmp/day24-critical-tac-007/`. No canonical/raw/PLAN/Bib/Git/session/credit modifications occurred. The reusable scientific drafts above are for leader incorporation into `knowledge/`, not a standalone long-term source in outputs.
