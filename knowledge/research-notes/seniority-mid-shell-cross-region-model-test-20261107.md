---
type: research-note
title: "Single-j seniority cancellation: exact model, symmetry countercheck, and cross-region theory audit"
aliases: []
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [book-jain-nuclear-isomers, book-suhonen-from-nucleons-to-nucleus, frauendorf-2014-transverse-wobbling, sensharma-2019-two-phonon-wobbling-135pr, rojeeta-devi-2021-multiphonon-transverse-wobbling-133ba, petrache-2018-chiral-bands-even-even-136nd, liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, xiao-2022-chirality-octupole-correlations-74as, zagrebaev-2001-superheavy-synthesis-survival]
created_from: project
promotion_target: high-spin-isomers-and-decay-modes-systematics
tags: [seniority, e2, particle-hole-symmetry, exact-diagonalization, cross-region, chirality, wobbling, ikeda, superheavy]
---

# Single-j seniority cancellation and cross-region theory audit

**Evidence status:** an independent, finite-space L4 **model and methodology test**, plus a targeted read-only audit of existing syntheses. This is not a measurement, a fitted nuclear calculation, an assignment of shape, or a survey of all literature. Original files are read-only; identities and SHA-256 values are in `outputs/l4/20261107-isomer-cross-region/seniority/run-manifest.json`. The exact code and numerical records are `system/scripts/isomer_seniority_transfer_validation.py` and `outputs/l4/20261107-isomer-cross-region/seniority/results.json`.

## Research Trigger

Does the same-seniority mid-shell E2 cancellation survive an actual many-fermion calculation, and does a weak rotationally scalar two-body perturbation necessarily undo it? The model has 12 identical-fermion magnetic substates in one \(j=11/2\) orbit, pair degeneracy \(\Omega=(2j+1)/2=6\), and \(n=2,4,6,8,10\). Antisymmetrized Slater determinants are exact in each \(M\) sector. In the pure pairing limit the same-\(v=2\) \(J=10\) and \(J=8\) states are degenerate: the calculation tests reduced E2 strengths, without supplying a nonzero photon energy or an isomer half-life.

## Assumptions

The pairing, added \(J=2\) channel, and one-body tensor are specified by

\[
H=-A^\dagger_{00}A_{00}+\epsilon\sum_{M=-2}^2 A^\dagger_{2M}A_{2M},\quad
A_{JM}=\sum_{a<b}\sqrt2\langle jm_a\,jm_b|JM\rangle c_b c_a,\quad \langle j\Vert Q_2\Vert j\rangle=1.
\]

The \(A_{JM}^{\dagger}\lvert0\rangle\) two-particle states are normalized. Energies are in units of the pairing coefficient and strengths are in the square of the chosen dimensionless one-body reduced matrix element; no \(e^2\mathrm{fm}^4\), effective charge, empirical interaction, absolute half-life, or random seed is implied. For \(\epsilon=0\), highest-weight \(J_i=10,v=2\) and \(J_f=8,v=2\) states are identified by the exact pairing eigenvalue. The \(M=10\) initial state is lowered to \(M=8\); \(Q_{20}\) and a Wigner–Eckart coefficient determine \(B(E2)=|\langle J_f\Vert Q_2\Vert J_i\rangle|^2/(2J_i+1)\). An independent \(M_i=9,q=-1\) component checks the angular normalization.

Jain, Maheshwari and Goel, *Nuclear Isomers: A Primer*, printed pp. 41–43 (PDF pp. 52–54), especially Eqs. (3.15), (3.20) and (3.21), explicitly distinguish **even ranks \(L>0\)**, same seniority and \(\Delta v=2\), and odd-rank tensor behavior. In this limited single-\(j\) setting, for corresponding pure \(v=2\) states,
\[
\frac{B_n}{B_2}=\left(\frac{\Omega-n}{\Omega-2}\right)^2.
\]
Do not extend this theorem to arbitrary odd-rank operators, arbitrary mixed-seniority transitions, multiple orbitals, or every experimental isomer. The source's generalized-seniority Sn discussion, printed p. 60 (PDF p. 71), explicitly models a different combined \(h_{11/2},d_{3/2},s_{1/2}\) valence space. For \(^{130}\)Sn, \(N=80\) is **two neutron holes relative to \(N=82\)**; two \(h_{11/2}\) holes in this single-orbit model are not the six holes needed for half filling. That counting alone does not establish the measured state as a pure two-hole configuration or explain its lifetime. The separate local Jain skill erroneously calls \(^{130}\)Sn and \(^{210}\)Po half-shell examples; the skill is not an authority overriding the original text.

**Cross-shell parity condition (analytic model inference).** For a seniority \(v\) state, \(n-v\) must be a nonnegative even integer: pairs change \(n\) by two. The \(h_{11/2}\) orbit has \(\Omega=6\), so the even-\(n\), \(v=2\) chain includes \(n=6\), exactly at the zero of the reduction factor. By contrast, \(g_{9/2}\) has \(\Omega=5\); its exactly half-filled configuration has \(n=5\), which cannot contain a \(v=2\) state. The same even-\(n\), \(v=2\) chain instead has the nearest occupancies \(n=4\) and \(n=6\): relative to its \(n=2\) matrix element, the reduction factors are \(+1/3\) and \(-1/3\), respectively, and both squared strength ratios are \(1/9\). These are single-\(j\), same-seniority analytical consequences for corresponding states, not a second numerical simulation or a measurement of any nucleus. Other seniorities and multi-orbit spaces require their own analysis.

## Provisional Reasoning

### Exact numerical results and controls

\(B_2=0.01561596298438403\) in model units. Ratios below use **the same unperturbed \(B_2\) denominator**. At \(\epsilon=0\), numerical roundoff leaves \(B_6/B_2=3.51\times10^{-30}\), not a measured residual.

| \(n\) | pure pairing | \(\epsilon=0.001\) | \(\epsilon=0.01\) | \(\epsilon=0.05\) |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 | 1 |
| 4 | 0.25 | 0.2504610766 | 0.2546360678 | 0.2736834297 |
| 6 | \(3.51\times10^{-30}\) | \(1.18\times10^{-29}\) | \(6.25\times10^{-30}\) | \(4.78\times10^{-30}\) |
| 8 | 0.25 | 0.2504610766 | 0.2546360678 | 0.2736834297 |
| 10 | 1 | 1 | 1 | 1 |

At each \(\epsilon\) the code follows the eigenstate with the largest overlap with the pairing reference, separately for each \(J\) and \(n\). At \(n=6,\epsilon=0.05\), squared overlaps are \(0.9997751\) for \(J=10\) and \(0.9998963\) for \(J=8\). Hence the perturbation changes the wavefunctions while leaving the observed mid-shell cancellation at roundoff. At \(n=4,8\), strengths do change. At \(n=2\), a scalar two-body interaction cannot change the unique fixed-\(J\) two-particle state; \(n=10\) is the two-hole endpoint in this model.

**Opposite-signature negative control.** At \(n=6\) and \(\epsilon=0\), the initial \(J_i=10,v_i=2\) state has pairing energy \(-1\) and particle–hole signature \(-1\). The \(J_f=8,v_f=4\) pairing eigenspace has energy \(-1/3\), signature \(+1\), and dimension three. Project \(Q_{20}|10,8\rangle\) into that entire eigenspace and normalize the resulting \(J_f=8,M_f=8\) doorway. Its strength is \(B=0.1083018902567772\), or \(6.935332157554365\) times the unperturbed \(n=2,\ v=2\to2\) reference, in the same arbitrary model units. The independent sum over all three orthonormal \(v=4\) final states is \(0.10830189025677717\). Thus a same-shell, half-filled **\(\Delta v=2\)** E2 transition is explicitly nonzero. The final state is higher in energy in this pairing Hamiltonian, so the stated \(10\to8\) strength is an upward excitation, not a radiative decay branch. The normalized doorway is identified by its projection, energy, angular momentum and seniority; because the final eigenvalue is degenerate, its orientation depends on the E2 operator and individual basis-state strengths are not uniquely fixed. The summed strength is invariant under rotations in this degenerate eigenspace. This is a model counterexample to “all mid-shell E2 transitions vanish,” not an experimentally observed branch.

The result revises the naive prior that *any* nonpairing mixing lifts the cancellation. Explicitly constructing \(C c_m^\dagger C^{-1}=(-1)^{j-m}c_{-m}\), the code checks at \(n=6\) that \(C^\dagger H C=H\), \(C^\dagger Q_{20}C=-Q_{20}\), and both tracked states have \(C\)-eigenvalue \(-1\). This symmetry forces their \(Q_{20}\) matrix element to zero even when the states are no longer pure pairing eigenstates. It does **not** force all mid-shell E2 transitions to vanish: opposite particle–hole signatures may connect, and multi-orbit mixing, effective operators or other interactions can change this symmetry argument.

**Verification and convergence:** this is complete diagonalization in each finite single-\(j\) sector, not an iterative truncation; the sampled perturbation scan tests sensitivity, not convergence to a real nucleus. Tests assert normalized coupled pairs and one-body tensor, two known 3j values, full \(H\)-\(J_+\) commutators (largest Frobenius norm \(2.18\times10^{-15}\)), eigenstate residuals and highest-weight conditions, two Wigner–Eckart components, reversal and rephasing of the determinant basis, independent eigenvector sign, the \(n=2\) control, all five analytic ratios, and the nonzero opposite-signature doorway and degenerate-space sum. State overlaps are recorded rather than assuming a band assignment through an untested level crossing. The parent independently checked 205 Wigner 3j values against SymPy 1.14.0 (maximum absolute error \(5.55\times10^{-17}\)) and four exact axial \(K=0\) Clebsch–Gordan cases; the receipt is `outputs/l3/20261107-isomer-cross-region/independent-algebra-check.json`. This validates selected algebraic building blocks only, not an independent full many-body solver. A separate shell-model implementation and a three-body or multiorbit symmetry-breaking scan would provide stronger independent validation. Failures abort rather than generating a success record.

## Grounded Evidence

The direct-source locators and analytical conditions are given above and in the following source-specific autonomous triage:

- **Jain, Eqs. (3.15), (3.20)–(3.21), printed pp. 42–43:** retain as direct support for the same-seniority and \(\Delta v=2\) distinction; the numerical doorway is this task's model result, not the book's measurement.
- **Suhonen, Eqs. (17.63)–(17.74), printed pp. 541–543 and p. 545:** retain the bare-operator, complete-space identity and model-space caveat; effective-\(g_A\) scaling is the stated algebraic inference.
- **Frauendorf–Dönau 2014, PDF p. 6:** use the axis-labeled frozen-alignment expression and its validity restriction; do not transfer its instability unconditionally to another rotor.
- **Sensharma 2019 and Rojeeta Devi 2021, each PDF p. 1:** retain their reported multiphonon interpretations as independent literature counterexamples to a claim of no reports; they do not independently settle competing interpretations.
- **Petrache 2018, PDF pp. 2 and 5:** retain the even-even and multiquasiparticle example as an author interpretation with model support, not a universal chirality criterion.
- **Liu 2016, PDF pp. 4–5, and Xiao 2022, PDF p. 1:** distinguish observed linking transitions from octupole/chiral interpretations; Liu describes a chirality–parity quartet as a future possibility.
- **Zagrebaev 2001, PDF pp. 6–7 and 9:** retain its cascade and spin-dependent survival as a model-dependent source; the audit of the source-page locators describes the version inspected and may be superseded by the parent's correction.

## Competing Explanations

The following source-specific audit preserves alternative interpretations and conditional model boundaries. It records corrections suggested for the versions originally audited; the parent has subsequently integrated corrections in the syntheses, so this historical list must not be read as a description of their current contents. The suggested corrections are not direct measurements.

1. **`knowledge/synthesis/universal-triaxial-collective-mechanics-and-cross-region-migration.md`, §§1–3:** remove the stated necessary-and-sufficient particle/hole, exact orthogonality and fixed \(\gamma\) cuts; they describe one favorable ideal geometry, not all possible chiral states or an automatic symmetry breaking. The operator triple product has the simple product of components only in that aligned classical limit, and an exact symmetry eigenstate need not have a nonzero signed chirality expectation. Petrache et al. 2018, *Evidence of chiral bands in even-even nuclei*, PDF p. 2 (printed 041304-1) explicitly treats odd-A and multiquasiparticle/even-even possibilities and distinguishes vibration from localized static geometry; PDF p. 5, Table I and surrounding text, gives model-dependent configurations. Near-degeneracy and transition patterns alone are not sufficient proof. Do not replace one universal threshold with another.
2. **Same page, §1 wobbling:** the printed symmetric-rotor expression around the largest-inertia \(m\) axis has the wrong pair of differences: with \(A_k=\hbar^2/(2\mathcal J_k)\), the stable ideal rigid-rotor factor is \(2I\sqrt{(A_s-A_m)(A_l-A_m)}\), within the high-spin convention. For a quasiparticle frozen on the short axis, set \(\bar A_s=A_s(1-j/I)\) and use \(2I\sqrt{(A_m-\bar A_s)(A_l-\bar A_s)}\); here \(I,j\) are dimensionless and \(A\) has energy units. Frauendorf–Dönau 2014, PDF p. 6, Eqs. (11)–(15), (23)–(24), uses the classical magnitude \(J=\sqrt{I(I+1)}\), and explicitly warns that the harmonic frozen-alignment approximation fails near instability. The page's asserted transverse formula lacks both required axis-dependent terms and does not vanish at its own quoted critical spin in general. The latter is conditional on the frozen alignment, inertia ordering and convention; no generic transition into chirality follows. Source PDF p. 9 describes *decreasing* frequency in the authors' \(^{163}\)Lu and \(^{135}\)Pr transverse interpretation, contradicting a universal Lu increasing-frequency claim.
3. **Same page, barrier and migration assertions:** \(\gamma\)-shape, chiral orientation, and normal-to-superdeformed decay-out barriers live in different collective coordinates and need not have the same saddle, inertia, or dynamical path. A one-dimensional local \(\hbar\sqrt{C/B}/2\) is a harmonic estimate under a specified kinetic metric, units, and potential; it supplies neither a universal necessary-and-sufficient rigidity test nor numerical mass-region exclusions. In particular, Sensharma et al. 2019, PDF p. 1, report an \(n_\omega=2\) \(^{135}\)Pr candidate; Rojeeta Devi et al. 2021, PDF p. 1, report \(n_\omega=0,1,2\) bands in \(^{133}\)Ba. These are reported interpretations and do not settle competing low-spin wobbling interpretations. They directly refute a blanket assertion that two-phonon candidates have not been reported in \(A\sim130\), not prove every assignment. Keep finite-resolution, configuration, E2/M1 mixing-ratio and alternative-mode disputes visible.
4. **`knowledge/synthesis/triaxial-collective-evolution-across-mass-regions.md`, §§2–4:** replace the region-wide “only” and strict control by Fermi level with configuration- and spin-dependent hypotheses; \(^{136}\)Nd is an even-even multiparticle candidate, and \(^{133}\)Ba is an author-reported hole-like transverse candidate. Decreasing wobbling energy is evidence in context, not a unique mode classifier; rigid versus \(\gamma\)-soft comparisons require the same states, tensor observables, inertia and uncertainty model. These corrections follow from the original papers cited in items 1–3.
5. **`knowledge/synthesis/octupole-and-chiral-coexistence-in-transitional-nuclei.md`, §§1–3:** distinguish intrinsic symmetry-broken configurations from finite-nucleus parity/chiral symmetry eigenstates, and treat four-band interpretation as a model hypothesis, not an automatic four-eigenbranch consequence. Liu et al. 2016, PDF pp. 4–5, reports eight E1 links between the positive- and negative-parity yrast bands and interprets octupole correlations; its conclusion discusses a chirality–parity quartet as a **future possibility**. Xiao et al. 2022, PDF p. 1, identifies two positive-parity and one negative-parity bands in \(^{74}\)As and suggests octupole correlations; it does not establish the purported continuous transition. Withdraw the invented universal energy-gap/\(D_0\) gates; derive transition rates with stated rotational assumptions and compare competing explanations.
6. **`knowledge/synthesis/high-spin-isomers-and-decay-modes-systematics.md`, §§1–3:** change “任意偶极或四极” to an even-rank \(L>0\), one-body, same-seniority statement with its model conditions and correct the \(^{130}\)Sn example. The page's fixed \(K\)-hindrance numerical change is not a unique triaxial signature. For Gamow–Teller, Suhonen, *From Nucleons to Nucleus*, printed pp. 541–545 (PDF pp. 552–556), Eqs. (17.63)–(17.74), derives \(S_--S_+=3(N-Z)\) with the **bare** spin–isospin operator and complete final sets; p. 545 discusses missing spin–orbit partners in truncated spaces. If the operator is uniformly multiplied by \(q=g_A^{\rm eff}/g_A\), that operator's summed difference scales as \(q^2\); it does not change the bare-operator identity. Experimental windows, many-body truncation, currents, operator convention and nucleus all matter; neither a universal percentage nor a single proven quenching mechanism follows from the identity.
7. **Same page, survival:** the product \(\prod_i\Gamma_{n,i}/(\Gamma_{n,i}+\Gamma_{f,i})\) is a restricted neutron-versus-fission branching approximation, and replacing each denominator by \(\Gamma_f\) additionally assumes \(\Gamma_n\ll\Gamma_f\). An exclusive \(xn\) yield requires the energy/spin-dependent cascade and terminal channel, with relevant \(\gamma\), charged-particle and other widths when non-negligible. Zagrebaev et al., PRC 65 014607, PDF p. 1 Eq. (1), PDF pp. 6–7 §IV and Eq. (10), explicitly includes \(\Gamma_{\rm tot}\), energy integration, competing emission and reaction-dependent model inputs; PDF p. 9 discusses spin-dependent survival. It does not support universal numerical survival, shell-barrier values or the absolute assertion that every macroscopic barrier vanishes. **Source-page audit:** the version of `knowledge/sources/zagrebaev-2001-superheavy-synthesis-survival.md` inspected in the original audit cited a purported Fig. 12 and Table 1 for universal-looking values; neither locator was found in the inspected 14-page original, whose numbered figures end at Fig. 10. Later source-page corrections may supersede this historical observation. Do not use those claims until independently rechecked.

## Transfer Conditions

The seniority result migrates to a different region only after specifying orbit degeneracy, particles **or** holes and their effective valence core, state correspondence and approximate seniority, the E2 operator, and the particle–hole symmetry or its actual breaking. Predictions for a real nucleus additionally need level energies, lifetimes, branches, conversion, mixing and an interaction with quantified uncertainties. Compare \(\Delta v=0\) and \(\Delta v=2\) transitions, rather than using one suppressed branch as a unique shape diagnosis. This exact calculation answers the bounded single-\(j\) question; it does not establish the size of symmetry breaking in any nucleus. Stop reason: the requested finite model and direct source checks are complete; independent many-orbit/three-body calculation and nucleus-specific comparison remain open research, not an implied measurement.

## Failure Conditions

The reduction formula cannot be transferred unchanged when the state correspondence, \(n-v\) parity, pure single-orbit seniority or assumed one-body E2 operator fails. A zero for one same-signature branch also fails as a claim that every mid-shell E2 matrix element is zero.

## Falsification or Reverse Tests

The \(n=6\), \(J_i=10,v_i=2,C=-1\) to the threefold-degenerate \(J_f=8,v_f=4,C=+1\) space gives a nonzero, basis-invariant summed strength. The pairing ratios, particle–hole operator checks, two tensor components, and rotation within the final degenerate eigenspace are the explicit reverse tests recorded above and in `verification.json`.

## Open Questions

How large is symmetry breaking in a specified multi-orbit or three-body model, and do the corresponding state assignments and electromagnetic observables survive a nucleus-specific comparison? An independent full many-body solver remains a useful further check.

## Human Review

No user review event recorded; autonomous audit and the independent algebra building-block check are described above.

## Promotion or Rejection History

2026-11-07: Created and independently audited as provisional research reasoning. The proposed promotion target is `high-spin-isomers-and-decay-modes-systematics`; this note does not claim that the model result has been promoted.
