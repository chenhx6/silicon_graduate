# Finite-spin shape-invariant precedent audit

**Assessment:** the general-spin algebra, finite-spin applications, and comparisons between shape estimators already have substantial precedent. A potentially focused contribution would be a **quantitative separation of charge collectivity, angular-channel redistribution and shape-conversion regime limits in odd-A Ba/Xe**, using verified IBFM wavefunctions and the same E2 operator. The restricted RME functions are rotation-invariant, projection-based scalars and can be valid defined observables. Their difference from standard complete charge-polynomial moments does not, by itself, make the source formulas algebraically wrong. This audit establishes neither that the published numerical results are wrong nor that the proposed comparison would be novel.

**Source/operator replay boundary.** The parent task reports that the literal \(J=0\) core calculation with \(\chi_{E2}=+0.35\) currently does not reproduce the published Fig.13 gamma values. This is an unresolved reproduction issue already at zero spin: published trends cannot be attributed solely to finite-spin closure. The parent also supplies two regime controls: the strong-coupling axial \(K=J\) control fails to recover rigid \(\gamma=0\) through the gamma conversion; the weak-coupling \(R=0\), \(h_{11/2}\) spectator control gives a beta factor of approximately **2.16025** without changing the core. These are **parent-supplied control results, not independently rerun or source-located by this audit**, and are not experimental data. They delimit conversion regimes; they do not invalidate the restricted scalar observables or establish the cause of the published curves.

The requested collection is dated 2026-11-06. Actual host UTC readings during acquisition were on **2026-11-05**, and the manifest preserves those readings rather than substituting the directory date. Source IDs below resolve to exact root-relative originals, SHA-256, size and reading locators in [source-inventory.json](source-inventory.json). [evidence-matrix.csv](evidence-matrix.csv) separates established precedent from applicability limits; [search-log.md](search-log.md) records coverage.

**1. What Nomura2017 actually prints.** The archived PDF p.11 and the supplied TeX agree. With \(M_{ab}=\langle a\Vert Q\Vert b\rangle\), Eqs.(12)–(15) use
\[
q^{N17}_2=\sum_{i=1}^{5}M_{J,J'_i}M_{J'_i,J},\qquad J'=J+2,
\]
\[
q^{N17}_3=\sqrt{7/10}\left|
\sum_{i,j=1}^{5}M_{J,J'_i}M_{J'_i,J'_j}M_{J'_j,J}
\right|,
\]
\[
\beta_{\rm eff}=\frac{4\pi}{3ZR_0^2}
\sqrt{\frac{q^{N17}_2}{2J'+1}
\langle J'J;20|JJ\rangle^{-2}},\qquad
\gamma_{\rm eff}=\frac13\arccos
\frac{q^{N17}_3}{(q^{N17}_2)^{3/2}}.
\]
The CG coefficient above is the paper's compact \((J'2J0|JJ)\). The text explicitly orders the retained \(J'\) states by excitation energy. Fig.14 applies the construction to \(1/2^+,3/2^+,5/2^+,11/2^-\) states of odd Ba/Xe. Exact source locators: **N17**, PDF p.11; TeX lines **1267–1282, 1306–1311**; Ref.42/43 identification at PDF p.13 and `.bbl` lines 436–454.

**The citation establishes a zero-spin charge-moment identity.** Werner et al.2000 explicitly define ground-state moments in \(0_1^+\), then derive the simple \(0\to2\to0\) and \(0\to2\to2\to0\) expressions. Their cubic quantity also uses a magnitude. Thus that magnitude convention is inherited, not newly introduced in Nomura2017. The cited derivation does not establish equality of the nonzero-J restricted diagnostic to complete charge-polynomial moments. Defining and studying that restricted diagnostic remains legitimate. **W00:** author-preprint pp.2–4, Eqs.(3)–(4), (8)–(11), (15)–(21).

**2. The established general-spin reference.** Cline's printed p.698 gives an intermediate-state expansion for a general state \(s\), including a 6j coefficient, and pp.699–700 discuss missing strength and operator-dependent identities. Nonzero-spin applications appear in Figs.8 and 10. Modern explicit formulas are also available in **H20**, Eqs.(7)–(10), **RZ21**, Eqs.(5)–(6), and **B22**, Appendix A, Eqs.(30)–(31).

For ordinary reduced matrix elements of a Hermitian rank-two tensor, a convenient Cline convention is
\[
Q_2(J)=\langle Q\cdot Q\rangle_J
=\frac{1}{2J+1}\sum_a
|\langle aJ_a\Vert Q\Vert J\rangle|^2
=\sum_a B(E2;J\to aJ_a),
\]
and
\[
Q_3(J)=
-\sqrt{\frac{35}{2}}\frac{(-1)^{2J}}{2J+1}
\sum_{a,b}
\begin{Bmatrix}2&2&2\\J_b&J&J_a\end{Bmatrix}
M_{J,aJ_a}M_{aJ_a,bJ_b}M_{bJ_b,J}.
\]
The latter denotes the signed expectation of
\(-\sqrt{35/2}[[Q\times Q]^{(2)}\times Q]^{(0)}\).
All allowed intermediate spins and states enter; individual tensor phases and normalizations must follow the same convention throughout. These are literature formulas, not a new derivation in this audit.

The following are **equation-level implications**, not certification of the original implementation:

- At \(J=0\), E2 selection forces both intermediate spins in the cubic loop to 2. The simple coefficient is appropriate there; finite state truncation and magnitude/sign interpretation remain separate issues.
- At nonzero J, increasing \(n\) within \(J+2\) cannot restore omitted spin channels. With the usual RME convention, the printed \(q^{N17}_2\) is \((2J+1)\) times the retained upward \(J\to J+2\) strength. This is not the complete \(Q_2(J)\).
- The beta CG factor is compatible with a bandhead rotor conversion under an axial \(K=J\) interpretation. That interpretation is our comparison, not a stated proof in N17. A beta conversion factor does not establish that the separate gamma conversion recovers an intrinsic angle in either strong- or weak-coupling limits.
- A magnitude cubic diagnostic folds the sign information distinguishing the two sides of \(30^\circ\); when its real arccos is defined, it returns \(0^\circ\)–\(30^\circ\). This can be an intentional convention. It is not the signed Cline quantity.
- The restricted RME functions **are rotation-invariant, projection-based scalars** when the selected levels denote complete magnetic multiplets and consistent RME conventions are used. An “effective” proxy can be a valid defined observable without being a standard complete charge-polynomial moment. The issue is the physical interpretation and the domain of its shape conversion.
- At fixed J across isotopes, changes in the distribution of strength among angular channels are real particle-core structure within the model. Such changes must not automatically be called artifacts or removed as nuisance geometry.

A useful proposed decomposition, with nonzero denominators and converged sums in the declared model space, is
\[
S_{J'}(J)=\sum_\nu B(E2;J\to J'_\nu),\qquad
f_{J'}(J)=\frac{S_{J'}(J)}{Q_2(J)},\qquad
c_5(J)=\frac{\sum_{\nu=1}^{5}B(E2;J\to(J+2)_\nu)}{S_{J+2}(J)}.
\]
Under the usual RME convention,
\[
q^{N17}_2=(2J+1)\,Q_2(J)\,f_{J+2}(J)\,c_5(J).
\]
This bookkeeping identity separates total charge collectivity, angular-channel fraction and retained-state saturation. At fixed J the prefactor is constant, while both \(Q_2\) and \(f_{J+2}\) can contain physical isotope dependence. The cubic quantity also requires signed loop-sector and interference information; quadratic strength fractions alone cannot determine it. This is a proposed analysis organization, not a new numerical result or novelty claim.

**3. Closest precedent and what it does not establish.**

| Source and exact locator | What is already established | Boundary for this candidate |
|---|---|---|
| **W05**, PRC71,054314; preprint pp.2–5, Eqs.(7)–(15), Secs.III–IV | Restricted-observable estimates of cubic invariants are explicitly compared with rotor/IBM results; the most severe truncation can be inadequate. | Ground-state study, not the odd-A \(J+2\) prescription. |
| **W06**, Rev. Mex. Fis. S52(4),103; printed p.104 Eqs.(1)–(13), p.106 Sec.5/Fig.3 | General-J scalar definitions are separated from ground-state expansions. IBM \(q_2\) evolution is studied up to J=10; the apparent critical point shifts with spin. | Finite-spin dependence and shifted transition signals are already known, but this is even-even IBM. |
| **N16**, PRC94,064310; preprint p.9 Eq.(8), pp.10–11 Fig.10/discussion | An average of five downward transitions with \(\Delta J=1\) or 2 is introduced by analogy to a q-invariant. Different channel choices produce different trends in odd Eu/Sm, related to weak/strong coupling. | Particularly strong counterargument to claiming that channel-sensitive odd-A proxies were previously unnoticed. It does not provide the cubic Ba/Xe comparison. |
| **N18**, PRC97,064314; archived arXiv1803.07802v2 pp.8–10, Eqs.(5)–(9), Ref.17 | The later paper sums all allowed \(J',J''\), uses a signed cubic expression, and generalizes the beta conversion; it cites N17 as prior work. | The printed cubic expression still has a constant \(-\sqrt{7/10}\), without explicit general-J 6j weights; the printed quadratic expression is also not the normalized closure above. This is a changed definition, **not a verified correction**. Publisher PDF access failed. |
| **H20**, PRC102,054306; Eqs.(7)–(10), Tables I–II, Sec.III | Explicit general-spin formulas and systematic finite-network convergence analysis already exist. | Its quantitative convergence sample is lighter even-even nuclei; five states is not a universal guarantee for odd Ba/Xe. |
| **B22**, EPJA58,187; preprint Table2/p.9, p.16, Table5/p.18, Appendix A/p.21 | Direct Xe precedent: for \(^{128}\)Xe, collective-wavefunction and Kumar estimates give \(\gamma_c=21^\circ\), \(\gamma_k=39^\circ\); the authors discuss weak intermediate-state transition matrix elements. They explicitly omit \(^{129}\)Xe Kumar parameters because of the poor spectrum and interpretational concerns. | Already demonstrates that different shape estimates can disagree in this mass region. It does not quantify N17's finite-spin prescription. |
| **R25**, PRC111,054309; preprint pp.12–17, Sec.IV C/Figs.11–14 | Microscopic spin-dependent invariants and truncation checks compare a larger calculated E2 network with the experimentally accessible subset. Shape diagnostics can change with configuration mixing. | Even-even TPSM. Its “full” network is the declared bands through I=10, not complete physical closure. |
| **Q26**, arXiv2604.10972; pp.9–11, Sec.III C/conclusions | A further microscopic comparison finds that gamma-band staggering and invariant-based shape assessments need not correlate. | Preprint; a different proxy and even-even systems. Not evidence of a correction to N17. |

The exact same-region Gogny-IBFM follow-up **N17G**, PRC96,064316, was also acquired and screened. Its model/E2 discussion is a useful robustness comparator, but the targeted full-text search did not identify an invariant-correction discussion. This is a bounded screening result, not a claim about all later uses of the formula.

**4. Correction/discussion search.** The N17 publisher landing page, both pages of its 34-entry citing-article index, its current Crossref record, and its arXiv history were examined. The arXiv history lists v1 on **April 24, 2017** and v2 on **July 8, 2017**. The acquired Crossref record has no `update-to` entry and an empty `relation` object; the saved landing page has no identified correction link.

No direct formal correction of N17 Eqs.(12)–(15), or full quantified reanalysis of its odd-A Ba/Xe curves with the complete closure, was identified **within these routes**. This is not an absence or novelty proof. The 34 citing records received title/bibliographic screening, with targeted full-text follow-up; they were not all read in full.

A related positive hit was checked rather than discarded: **E21**, EPJA57,292, is an erratum to a Bose–Fermi phase-transition paper. Its entire one-page publisher text changes a **funding project number**, not a shape-invariant formula. N18 is the most relevant formula change actually found; its text treats N17 as supportive precedent and does not identify itself as a correction.

**5. Strongest counterarguments to a focused paper.**

1. **The quantities can be deliberate, valid observables.** N16 explicitly presents an analogy and discusses channel dependence. Inequality to a complete charge moment is not an algebraic error. A useful study must distinguish physical redistribution from a shape-conversion failure, with the intended interpretation and regime stated.
2. **The methodological comparison is established.** W05/W06, H20, B22 and R25 already cover approximation quality, finite spin, differing shape definitions and missing networks. Neither a 6j derivation nor a single rigid-rotor failure supports a broad methodological novelty claim.
3. **Printed equations do not prove what generated the figures.** Source TeX verifies the manuscript formula, not hidden matrix-element conventions, normalization, code or postprocessing. The parent-reported \(J=0,\chi_{E2}=+0.35\) mismatch to Fig.13 makes this limitation concrete. A faithful source/operator replay must precede any attribution of published trends to spin-channel closure; a separately defined implementation may be studied on its own terms.
4. **Wavefunction errors can dominate the observable.** B22's explicit \(^{129}\)Xe exclusion is a relevant warning. Matching energies alone does not validate the signed E2 network, especially transitions among intermediate states. A single-j negative-parity model cannot certify the positive-parity multi-orbit states in N17 Fig.14.
5. **A complete invariant is not a unique static shape.** Moment ratios, charge-versus-mass deformation, amplitude fluctuations, configuration mixing and noncommuting effective E2 operators remain distinct issues. C86 pp.699–700 specifically limit identities based on commuting E2 components. A change in \(\gamma_{\rm eff}\) alone does not establish a change in gamma softness or rigidity.
6. **The original physical conclusion may survive.** N17 uses PES and spectral trends as well as the E2 diagnostic. A changed curve may leave the broader phase-transition interpretation intact. The paper must state which inference changes and which remains supported.

**6. Minimum useful result for an EPJA/PRC manuscript — research judgment, not an editorial guarantee.**

The same scientific floor applies to both venues:

- **Verified common input and source replay.** Freeze the Hamiltonian, model space, state identities and E2 operator; obtain or independently reproduce the relevant IBFM wavefunctions and signed RMEs. Resolve or explicitly retain the zero-spin Fig.13 mismatch before claiming a replay of published trends. Reproduce a declared subset of spectra, EM matrix elements and plotted indicators. If only the \(h_{11/2}\) sector is validated, restrict claims accordingly.
- **Separate the contributions.** On those same wavefunctions report total charge moments, angular-channel fractions, within-channel state saturation, signed versus folded cubic quantities, and the beta/gamma conversion. Compare the printed \(J+2,n=5\) observable with converged versions and complete scalar moments without treating the former as invalid by definition. Preserve physical fixed-J redistribution; do not silently change effective charges or refit while attributing differences to closure.
- **Independent algebra and regime checks.** Use the parent/Planck work for the rigid axial \(K=J\), weak \(R=0\) spectator and general-spin controls, retaining the provenance of the two parent-supplied failures above. Add zero-spin reduction, direct tensor-versus-RME contraction, state rephasing and basis-completeness checks where applicable. This audit has not run or certified those controls. Conversion failures must be tied to a stated coupling regime.
- **A quantitative consequence.** Determine how much isotope dependence arises from charge collectivity, how much from real particle-core redistribution, and where interpreting the diagnostic as intrinsic beta/gamma fails. Show whether resulting shape or transition inferences change beyond plausible operator/model uncertainties, or establish a useful regime of stability. Report small-\(Q_2\) and out-of-domain arccos cases; do not hide them by clipping.
- **Physics validation and reproducibility.** Test against available E2 strengths, quadrupole moments and branching/sign constraints; distinguish fitting inputs from checks. Release sufficient parameters/RMEs and analysis code to repeat the comparison, subject to actual source/code permissions.

For a **focused EPJA application**, a well-validated, explicitly limited odd-A sector or sequence could support a paper if it yields a consequential separation of these structural contributions and a useful regime prescription, with B22 and N16/N18 treated as central comparators. For a **PRC submission**, the same evidence should support a clear nuclear-structure conclusion and demonstrate its relevance beyond one transcription or normalization issue. Journal choice cannot supply a missing physics result. A textbook identity and a toy conversion failure alone do not establish the proposed Ba/Xe result. A correction claim would additionally require identifying an actual erroneous assertion or implementation, rather than merely comparing two different legitimate observables.

The defensible working question is: **How do total charge collectivity and its angular-channel distribution separately evolve in odd-A Ba/Xe, and under which coupling regimes can the associated effective proxies be interpreted as intrinsic shape parameters?** The comparison must retain the source/operator replay boundary. That is a testable contribution candidate, not an established claim of priority.

**Audit limits and artifacts.** Fourteen source PDFs are inventoried with actual reading scopes; eleven were newly acquired, along with seven metadata/index artifacts. Two failed retrievals remain recorded, including the inaccessible N18 publisher PDF. No author code was certified; no IBFM wavefunctions, parent counterexamples, fits or numerical continuation were modified or recomputed. The original Kumar1972 paper was not newly acquired; historical credit is supported by the inspected method papers, not falsely represented as a fresh reading of that original.

New originals and their manifest are confined to `raw/papers/gpt/query/20261106-spin-invariant-precedents/`. Extracted source text and page images are confined to `tmp/ba129-spin-invariant-precedents/`. Reports and acquisition/verification helpers are confined to this report directory. No changes to knowledge pages, PLAN, get-paper, frozen cores or other sessions' files; no commit.

Recheck this collection from the repository root with:

```bash
python3 -B outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-precedent-review/finalize_evidence.py
python3 -B system/scripts/wiki_archive_gate.py check --root . -- raw/papers/gpt/query/20261106-spin-invariant-precedents/manifest.json
```
