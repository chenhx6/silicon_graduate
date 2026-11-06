**Five-Ba operator-sensitivity control: fixed Hamiltonians and lowest \(11/2\) states**

**Completed: 35 settings, with no Hamiltonian or state refit.** The decline of full \(q_2\) and of the selected-channel quadratic quantities along \(^{129,131,133,135,137}\)Ba survives all seven prescribed settings. Cubic signs, formal angle trends, and the \(^{135}\)Ba proxy's arccos-domain violation are operator-sensitive. The domain violation survives the sampled \(e_F\) changes and quoted-margin calibration endpoints, but disappears for both alternate \(\chi_E\) operators. Its survival is not required for the distinction between full moments and the selected-channel proxy.

The [contract](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-operator-control/operator-sensitivity-contract.json) was frozen at **2026-11-06 03:26:08 UTC**, before this run started at **03:30:27 UTC**. It is an internal prospective sensitivity contract made after disclosure of the parent primary, not an external preregistration. Contract SHA-256:
`688386441deb562b19f7dc5df8b3abeb522976fd9daebf367a4781ca2e53de1e`.

The [driver](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-operator-control/driver.py) uses the existing read-only IBFM and scalar-invariant modules. Compact outputs are [operator-results.csv](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-operator-control/operator-results.csv), [results.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-operator-control/results.json), and [run.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-operator-control/run.json). No full RME matrix or state-pair contribution table is serialized.

**Frozen controls and calibration**

Each isotope uses the printed Hamiltonian inputs in the parent's chain contract, the parent's signed \(Q_{jj}=-1.081027387032316\), and the lowest \(J=11/2\) state. The Hamiltonian and that state's eigenvector are computed once and reused for all seven operators. Their hashes are unchanged across the controls. The \(Q_{jj}\) value also agrees with \(-\sqrt{525/(143\pi)}\) for the declared \(h_{11/2}\), unit-normalized \(Y_2\) convention.

The operator is
\[
T(E2)=e_B Q_{\chi_E}
-\frac{e_F(1-2v^2)Q_{jj}}{\sqrt5}\,[a^\dagger\times\tilde a]^{(2)}.
\]

The seven settings are primary \((\chi_E,e_F)=(0.35,0.125\,e\,b)\); \(e_F=0.0625\) and \(0.25\,e\,b\) at primary \(\chi_E\); the alternate operators \(\chi_E=0\) and \(\chi_E=\chi_H\), each with \(e_F=0.125\,e\,b\); and lower/upper quoted-margin \(B_\downarrow\) calibration endpoints at primary \(\chi_E,e_F\). These are one-factor sensitivity settings, not posterior draws or a fitted operator selection.

For each alternate operator, \(e_B>0\) is independently recalibrated to the corresponding core's same selected \(B_\uparrow=5B_\downarrow\):
\[
e_B=\sqrt{B_\uparrow^{\rm target}/B_\uparrow(e_B=1,\chi_E)}.
\]
No calibration is adjusted to reduce a full-versus-selected discrepancy.

| Core | Selected \(B_\downarrow\) \((e^2b^2)\) | Quoted margin used | Central \(B_\uparrow\) \((e^2b^2)\) |
|---|---:|---:|---:|
| \(^{128}\)Ba | 0.2765251611 | 0.0237021567 | 1.3826258057 |
| \(^{130}\)Ba | 0.2326000000 | 0.0022000000 | 1.1630000000 |
| \(^{132}\)Ba | 0.1720000000 | 0.0120000000 | 0.8600000000 |
| \(^{134}\)Ba | 0.1358000000 | 0.0022000000 | 0.6790000000 |
| \(^{136}\)Ba | 0.0814000000 | 0.0014000000 | 0.4070000000 |

The \(^{128}\)Ba margin is the supplied **linearized half-life-only** propagation. The separate gamma-energy contribution is not included, and the ICC uncertainty is unreported; this is not a complete uncertainty. Other rows use the selected quoted \(B_\uparrow\) margins divided by five. No confidence level, probability distribution, or cross-isotope covariance is assigned. Simultaneous lower/upper chain settings and four endpoint combinations for a given isotope pair are deterministic sensitivity checks, not a joint confidence band. The selected numbers and calibration-file hash remained unchanged during this run.

**Primary replay and what is summed**

“Full” denotes direct contraction of all five E2 components within this declared finite model space, checked against complete reduced-ME \(6j\) closure. It is not complete experimental nuclear strength. The restricted \(n=5\) and “all” quantities retain the lowest five, or all, **\(J'=15/2\)** multiplets in increasing calculated energy order. “All” in that column does not mean all angular-momentum channels.

The full signed ratio is \(c=q_3/q_2^{3/2}\). For comparison with the absolute-value proxy, the reported full folded angle is \(\arccos|c|/3\), only when the argument is in the real domain. Signed \(q_3\), signed \(c\), and signed-angle fields are retained separately in the data.

| Odd Ba | Full \(q_2\) \((e^2b^2)\) | Full signed \(q_3\) \((e^3b^3)\) | Full signed \(c\) | Proxy \(c_{n=5}\) | Proxy \(c_{\rm all\,15/2}\) | All-\(15/2\) fraction of full \(q_2\) |
|---|---:|---:|---:|---:|---:|---:|
| 129 | 1.531871411 | +0.010473198 | +0.005523901 | 0.038880978 | 0.035138258 | 0.290125009 |
| 131 | 1.263918212 | −0.099532932 | −0.070046807 | 0.129367144 | 0.133389129 | 0.276737484 |
| 133 | 0.946368676 | −0.133174083 | −0.144653578 | 0.632158819 | 0.636864480 | 0.243508931 |
| 135 | 0.676622790 | −0.028118636 | −0.050521277 | **1.026114565** | **1.024144143** | 0.200252256 |
| 137 | 0.476765595 | −0.021958680 | −0.066703538 | 0.729020038 | 0.738227245 | 0.215839252 |

These reproduce the parent's declared primary to a maximum absolute difference of \(1.78\times10^{-15}\) over the checked calibration and moment/proxy fields. This is an internal primary replay, not a reproduction of the source authors' E2 implementation or figures.

**The \(^{135}\)Ba domain result is conditional**

For this isotope \(\chi_H=-0.24\). “Outside” means an undefined real proxy angle; the raw ratio is kept without clipping.

| Setting | Recalibrated \(e_B\) \((e\,b)\) | Full signed \(c\) | Full folded angle | Proxy \(c_{n=5}\) | Proxy \(c_{\rm all}\) | Proxy domain, both sums |
|---|---:|---:|---:|---:|---:|---|
| Primary | 0.1298423795 | −0.050521277 | \(29.034704^\circ\) | 1.026114565 | 1.024144143 | Outside |
| \(e_F=0.0625\) | 0.1298423795 | −0.062962666 | \(28.796706^\circ\) | 1.003498598 | 1.001492049 | Outside |
| \(e_F=0.25\) | 0.1298423795 | −0.025401277 | \(29.514819^\circ\) | 1.071086382 | 1.069183082 | Outside |
| \(\chi_E=0\) | 0.1262899066 | +0.288151303 | \(24.417563^\circ\) | 0.946961363 | 0.947074609 | Inside |
| \(\chi_E=\chi_H=-0.24\) | 0.1239642059 | +0.492434701 | \(20.166422^\circ\) | 0.847550825 | 0.848262929 | Inside |
| Lower \(B_\downarrow\) margin | 0.1287863426 | −0.050316465 | \(29.038620^\circ\) | 1.026484738 | 1.024514894 | Outside |
| Upper \(B_\downarrow\) margin | 0.1308898964 | −0.050721149 | \(29.030882^\circ\) | 1.025753257 | 1.023782270 | Outside |

For \(\chi_E=0\), the valid proxy angles become \(6.248144^\circ\) and \(6.241410^\circ\), for \(n=5\) and all \(15/2\) states respectively. For \(\chi_E=\chi_H\), they are \(10.684575^\circ\) and \(10.658921^\circ\). They remain substantially different from the corresponding full folded angles even after the domain violation disappears.

The weakest surviving violation is the all-state value \(1.001492049\) at \(e_F=0.0625\), well above the numerical closure residuals. This establishes survival at the sampled settings, not over an arbitrary continuous operator family. No full moment ratio leaves the real domain in these 35 rows.

**Trend comparisons and reversals**

The frozen comparisons cover adjacent isotope pairs and the \(129\to137\) endpoint. A trend reversal requires opposite nonzero difference signs beyond the declared tolerance; an undefined angle is recorded as a domain issue, never assigned a trend.

- Full \(q_2\), full beta, both restricted quadratic contributions, and both literal beta proxies decrease at every adjacent step in all seven settings. No quadratic/beta trend reversal is found.
- The \(e_F\) settings and the quoted-margin endpoints preserve the primary's defined trend directions, cubic signs, and domain statuses. The four lower/upper calibration combinations for each predeclared isotope interval also produce no reversal.
- Both alternate \(\chi_E\) operators change full \(q_3\) from negative to positive in \(^{131,133,135,137}\)Ba. \(^{129}\)Ba remains positive. These are operator-sensitivity results on unchanged eigenstates, not evidence of a change in the Hamiltonian's intrinsic shape.
- The formal folded-angle conclusions can reverse, and full versus selected trends can disagree even when both angles exist.

The complete within-setting disagreements are shown below for the all-\(15/2\) proxy. The \(n=5\) proxy has the same direction in every listed interval.

| Alternate operator | Interval | Full folded angle | All-\(15/2\) proxy angle |
|---|---|---|---|
| \(\chi_E=0\) | \(131\to133\) | \(25.256487\to27.086867^\circ\), increases | \(29.250947\to20.031757^\circ\), decreases |
| \(\chi_E=0\) | \(129\to137\) | \(23.985223\to25.790572^\circ\), increases | \(26.278159\to17.673909^\circ\), decreases |
| \(\chi_E=\chi_H\) | \(131\to133\) | \(22.248585\to24.224638^\circ\), increases | \(27.640957\to21.864030^\circ\), decreases |
| \(\chi_E=\chi_H\) | \(135\to137\) | \(20.166422\to13.035918^\circ\), decreases | \(10.658921\to27.093641^\circ\), increases |
| \(\chi_E=\chi_H\) | \(129\to137\) | \(21.086590\to13.035918^\circ\), decreases | \(24.850606\to27.093641^\circ\), increases |

The machine-readable comparison records retain all 16 metric/interval reversals relative to the primary, four proxy domain-status changes, and eight full-\(q_3\) sign changes. These counts include related quantities and intervals; they are not independent statistical tests.

Across all 35 settings, the complete \(15/2\) channel carries **14.12%–29.24%** of full \(q_2\), while the first five \(15/2\) states retain **99.588%–99.939%** of that channel's quadratic strength. Near-convergence in the selected spin therefore coexists with a substantial distinction from full angular closure. A converged selected-channel scalar remains a legitimate channel-sensitive quantity; it does not become the full charge-polynomial moment.

These controls do not classify fixed-\(J\) isotope-dependent redistribution as an unphysical artifact. Different isotopes have different frozen Hamiltonians and eigenstates, and channel fractions may encode real particle–core dynamics. Within one isotope, this study holds those dynamics fixed and varies the E2 operator/calibration only. It does not replace the separate \(^{135}\)Ba coupling-causality study.

**Checks and limits**

The maximum direct-versus-complete-reduced differences are \(4.95\times10^{-13}\,e^2b^2\) for \(q_2\) and \(8.55\times10^{-13}\,e^3b^3\) for signed \(q_3\). Calibration replay differs from target \(B_\uparrow\) by at most \(6.66\times10^{-16}\,e^2b^2\). All 35 closures are complete within the declared model space. Both loaded NumPy and SciPy OpenBLAS libraries report **one thread**. Runtime was 100.28 s; the source-module and selected-calibration hashes remained unchanged.

The operator alternatives are explicitly alternate operators, and the quoted margins are incomplete sensitivity information, not a posterior. No probability is attached to a reversal or domain status. The isotope trend is conditional on the selected core calibrations as well as the fixed Hamiltonians; it is not an independent empirical determination of collectivity. Formal signed/folded angles do not establish gamma rigidity, softness, or a collective-mode assignment. The robust result in this compact scan is the persistence of the full-versus-selected distinction; the particular outside-domain event and cubic/angle trend interpretations are conditional on the operator.

All files written by this task are in this new operator-control directory. Existing modules, model data, the chain contract, parent primary, calibration source, other session work, `get-paper`, and `PLAN.md` were not modified. No commit was made.
