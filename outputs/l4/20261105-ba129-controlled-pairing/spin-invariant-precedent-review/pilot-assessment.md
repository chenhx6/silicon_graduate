# Assessment of the five-isotope core-only pilot

**Judgment:** this is a substantive advance beyond the analytic controls. It supplies a concrete, source-parameterized isotope-chain example in which a selected angular channel is numerically saturated while its effective shape coordinate evolves quite differently from the complete tensor-moment coordinate. That is a credible basis for developing a focused odd-Ba paper. It is not yet a demonstrated claim of priority, a replay of Nomura's EM figures, or a measured-shape result.

The promising contribution is the **quantitative separation of total charge collectivity, physical particle-core redistribution among angular channels, and the regime dependence of a shape conversion**. The restricted observables remain legitimate rotation-invariant scalars.

**Evidence inspected.** The parent result is `spin-invariant-probe/chain-core-only-v1.json`, SHA-256 `6a530f851325a33845ce8b90a84535723e75eb9e1ff4d1fc2ae574a20eb95f6c`. Its contract hash matches `spin-invariant-chain-contract.json`; all five parameter records and both recorded producer hashes match. The contract is an internal prospective chain specification after the initial 129Ba pilot, not external preregistration. Each isotope's Hamiltonian is held fixed across the diagnostic comparisons; parameters differ across isotopes as declared.

This assessment checks stored-number arithmetic and provenance, not independent diagonalization. The stored quadratic direct/RME closure agrees within \(2.57\times10^{-11}\) in the stated units. Independent cubic closure evidence is not attached in this JSON; existing parent/independent checks should be linked to these cases and producer versions before manuscript use. No model was rerun or fitted here.

The operator is \(e_B=1,\ e_F=0,\ \chi'_{E2}=+0.35\). “Full” means complete within the declared finite model space. Angle labels below are folded rigid-equivalent coordinates constructed from moments, not measurements or certificates of rigidity.

| Odd Ba A | Full folded angle, deg | J+2, n=5 proxy, deg | J+2, all states, deg | \(P(R_{\rm core}=0)\) | \(\sqrt{Q_{2,\rm odd}/Q_{2,\rm core}}\) |
|---:|---:|---:|---:|---:|---:|
| 129 | 29.914 | 29.343 | 29.412 | 0.781 | 0.981 |
| 131 | 28.682 | 27.663 | 27.583 | 0.805 | 0.979 |
| 133 | 27.109 | 17.537 | 17.422 | 0.768 | 0.992 |
| 135 | 28.561 | 3.749 | 3.944 | 0.489 | 0.941 |
| 137 | 28.151 | 16.653 | 16.408 | 0.727 | 0.992 |

All values are parent computations, read from the artifact. The 137Ba \(P(R=0)\) value is 0.726660, outside the approximate 0.77–0.81 range in the task summary. Also, \(P(R=0)\) includes excited zero-spin core states: the separate 135Ba core-ground-state probability is 0.432372.

**What the new result establishes within this model.**

The five-state sum captures 99.589–99.854% of the complete J+2-channel quadratic strength, but only 20.554–28.905% of the complete \(Q_2\). Importantly, the actual cubic proxy was also evaluated with all states of that channel: doing so changes its angle by at most **0.2444 degrees**. Thus the large discrepancy is not explained by the five-state cutoff within J+2. This conclusion does not rely on assuming that quadratic saturation alone guarantees cubic convergence.

The full folded coordinate spans **2.805 degrees** across the five cases; the n=5 proxy spans **25.594 degrees**. The largest same-state separation is **24.812 degrees in 135Ba**, and remains 24.616 degrees with every J+2 state. The complete moments and the restricted diagnostic therefore emphasize different structural information for this chain.

This is more informative than a fixed-spin geometric prefactor: all five initial spins are 11/2. The isotope dependence must involve the changing states and matrix-element network. In 135Ba the large separation accompanies a reduction of the R=0 core component and an 11.435% reduction of \(Q_2\) relative to its own uncoupled core. This is evidence of association within the model, not yet proof that R=0 depletion causes the cubic-proxy minimum. A signed cubic loop-sector analysis is needed to distinguish redistribution from interference/cancellation.

The quadratic decomposition already supplies a more specific structural clue: the \(J'=J=11/2\) channel contains **35.93%** of full \(Q_2\) in 135Ba, compared with **7.45%** in 129Ba and **7.85%** in 131Ba. This channel includes both the diagonal element and transitions to other states of the same spin; it must not be equated with the static quadrupole moment alone. Thus real redistribution is visible directly, although its relation to the cubic minimum still requires the signed loop analysis.

Two qualifications matter:

- **Near-unity odd/core ratios are not constant collectivity along the chain.** At unit boson charge the full odd-system \(Q_2\) values are 86.993, 70.626, 57.372, 38.786 and 28.911. The last is 0.3323 times the first. These are substantial changes in the declared model, even though odd-particle polarization relative to each associated core is modest. Absolute charge comparisons additionally require the isotope-specific calibrations.
- **The beta scale is not an independent third piece of evidence.** For this fixed J and the stated prescription, the stored numbers obey
  \[
  \left(\frac{\beta_{\rm proxy}}{\sqrt{Q_2}}\right)^2
  =17.5\,f_{5,J+2},
  \]
  where the numerator denotes the recorded radius-prefactor-free beta scale and \(f_{5,J+2}\) is the fraction of full \(Q_2\) in the first five J+2 states. The 1.897–2.249 ratios are an algebraic re-expression of that fraction and the bandhead conversion. They should not be counted as independent confirmation, nor labeled a measured-beta error.

**Meaning of “effective.”** An effective quantity can be a deliberately chosen, useful observable. A well-converged channel proxy may be more sensitive to particle-core recoupling than the complete charge moment, and that sensitivity can be valuable physics. Calling it effective does not ensure that its numerical value is an intrinsic beta or gamma in every coupling regime. The pilot supports testing that conversion and separating the information carried by the two quantities; it does not establish that one observable is valid and the other invalid.

The full folded angle is likewise not the unique physical shape. Report the underlying signed cubic ratios as well: here they are approximately \(+0.00449,-0.06897,-0.15078,-0.07530,-0.09664\). Folding removes their sign distinction, and a mean angle near 30 degrees alone cannot decide gamma softness or rigidity. The core-only tensor probes the bosonic part of the coupled odd-nucleus wavefunction; it is not the complete electromagnetic operator.

**Novelty against the inspected precedents.** The earlier [source audit](audit.md) and [evidence matrix](evidence-matrix.csv) remain the basis of this assessment; no exhaustive new priority search is claimed.

- **Nomura2016**, PRC94,064310, Eq.(8), Fig.10 and adjacent discussion, already demonstrates DeltaJ-dependent indicators in odd Eu/Sm and relates them to weak/strong coupling. “Odd-particle coupling changes a restricted proxy” is therefore not a sufficient contribution.
- **Werner2005/2006 and Henderson2020** already cover approximation quality, finite-spin behavior and convergence. The contribution would be the quantitative separation on these declared odd-Ba states, including a mechanism, not a new closure identity or the observation that omitted channels exist.
- **Bally2022**, EPJA58,187, Table2 and p.16 of the archived preprint, already finds differing deformation estimates in 128Xe and declines a Kumar analysis of 129Xe because its spectroscopy is inadequate. The current model must therefore earn its nuclear interpretation through validated states and intermediate E2 matrix elements.
- **Rouoof2025**, PRC111,054309, Sec.IV C, already compares limited and larger microscopic E2 networks and spin-dependent shape diagnostics. The present stronger distinction is saturation *inside a selected spin channel* versus coverage and interpretation of the complete tensor moments, in an odd-A chain.

The added value is plausible and specific: a fixed-J isotope-chain control separates a nearly saturated restricted strength from total charge moments, and identifies a pronounced coupled-structure anomaly. Whether that separation is new in the relevant literature remains a claim to substantiate, not a consequence of a search miss. A larger angle difference than an earlier paper is not itself novelty.

**Journal value and the decisive next result.** My assessment has moved from “analytic motivation only” to **“credible focused-paper pilot, with the primary physical case still outstanding.”** For EPJA, a bounded, well-validated odd-Ba study could be a coherent regular research article if it explains this separation and its practical interpretation. For PRC, a clear nuclear-structure mechanism and a robust conclusion from the electromagnetic case would provide the stronger submission argument. This is judgment about the scientific case, not an editorial ranking or acceptance forecast.

The highest-value remaining work is:

1. **Complete the calibrated \(e_F=0.125\) case on the same frozen states.** In the core-only limit a common charge scale cancels from normalized ratios. With both terms present, the relative scale \(e_F/e_B\) changes boson–fermion cross terms in \(Q_2\) and several mixed terms in \(Q_3\). Because some full cubic ratios are small, the effect cannot be assumed negligible. Calibration is therefore more than fixing an absolute beta scale.
2. **Explain 135Ba through contributions, not correlation alone.** Resolve core-R components, signed cubic spin-pair sectors and cancellations; link any existing independent contraction checks to this chain. Use a limited, declared coupling/state control if needed to establish causation. P(R=0) by itself cannot determine the cubic invariant.
3. **Establish robustness without fitting the discrepancy.** Separate uncertainty in operator/calibration choices from model-parameter scenarios. Determine whether the structural interpretation survives plausible choices, or precisely identify its regime of validity. More isotope curves alone would not answer this.
4. **Validate the intended physical scope and preserve the replay boundary.** Use the available spectra and E2/moment constraints for the 11/2-negative-parity sector. The unresolved zero-spin Fig.13 replay with literal chi'=+0.35 prevents attributing published trends solely to spin-channel closure. It need not prevent a clearly defined independent model study, but it does prevent presenting this pilot as a correction or reproduction of those published curves.

If the large separation persists in the calibrated electromagnetic case and a microscopic mechanism is identified, the candidate gains a substantive physics argument. If it disappears there, the core-only result remains a legitimate control and a regime warning, but the claim about physical odd-Ba charge inference must be narrowed. Either outcome should be reported without selecting operator choices to preserve the anomaly.

A supportable present claim is: **In this declared core-only h11/2 IBFM chain, near-complete convergence of the selected J+2 strength does not make its effective angle track the complete folded charge-moment coordinate; the largest separation accompanies substantial particle-core reconfiguration.** It is a model-control statement, not a measured-shape claim or an assertion that the source authors were wrong.

The derived [pilot-summary.csv](pilot-summary.csv) and [pilot-checks.json](pilot-checks.json) retain the numerical comparison, hashes and arithmetic scope. Reproduce those read-only checks with:

```bash
python3 -B outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-precedent-review/assess_pilot.py
```

Only assessment products in this review directory were written. The parent pilot, contract, model producers, calibration work and frozen continuation were not modified; no fit or commit was performed.
