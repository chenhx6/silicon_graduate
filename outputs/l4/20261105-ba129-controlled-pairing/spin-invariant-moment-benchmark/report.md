The fixed implementation reproduces the parent's five signed \(Q_s(11/2^-)\) values and is consistent with the adopted \(^{137}\)Ba calibration moment. It does **not establish exact replay of the source's EM calculations**: the \(^{136}\)Ba calibration-state central value and the printed \(^{135}\)Ba prediction differ. Calibration consistency, additional EM comparisons, and rotational-closure checks have distinct evidential roles.

All calculations use
\[
Q_s(J)=\sqrt{16\pi/5}\,
\langle J,M=J|T^{(E2)}_{20}|J,M=J\rangle
\]
in **signed e b**, with the frozen Hamiltonian, \(\chi_E=+0.35\), \(e_F=0.125\) e b, and positive \(e_B\) determined only from the existing core-\(B(E2)\) calibration JSON. The signed \(h_{11/2}\) matrix element \(Q_{jj}=-1.0810273870\) was independently reconstructed from the stretched \(Y_{55}\) angular density and the declared CG convention; no radial factor was inserted. Source Tables I/III/V were checked against the contract's numerical entries. Boson counting and the Table-V-to-kernel parameter mapping remain the declared contract conventions, not recovered author run cards.

The local [Nomura2017 PDF](</workspace/wiki/raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf>), p. 4, Eqs. (7)–(8) and following paragraph, explicitly names \(^{136}\)Ba \(2_1^+\) as the \(\chi_E\) calibration target and \(^{137}\)Ba \(11/2_1^-\) as the neutron-charge target. It gives **no numerical experimental or calculated moment for either there**. Corresponding [arXiv-v2 TeX](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:549) locators are lines 549–582; Tables I/III/V are PDF pp. 3–4, TeX lines 298–302, 389–393 and 514–518.

| State | Fixed model \(Q_s\), e b | Source comparison, e b | Role |
|---|---:|---|---|
| \(^{129}\)Ba \(11/2_1^-\) | −0.1634833003 | No value established in this bounded source check | Prediction |
| \(^{131}\)Ba \(11/2_1^-\) | +0.1423371803 | Same boundary | Prediction |
| \(^{133}\)Ba \(11/2_1^-\) | +0.9426011932 | Same boundary | Prediction |
| \(^{135}\)Ba \(11/2_1^-\) | +1.1769302905 | Nomura: theory +1.13, experiment +0.98(8); archived adopted: +0.96(8) | Additional EM comparison |
| \(^{137}\)Ba \(11/2_1^-\) | +0.7729628798 | Archived adopted +0.78(9) | Calibration consistency |
| \(^{136}\)Ba \(2_1^+\) | −0.3032374652 | Several evaluated alternatives; see below | Calibration-state check |

For \(^{137}\)Ba, \(e_B=0.1256400432\) e b. The same-state boson and fermion contributions are **+0.6947535900** and **+0.0782092898** e b. The total differs from adopted +0.78 by −0.0070371 e b. The [adopted ENSDF](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc137-adopted-text.ens:60), lines 60–69, and PDF p. 1 locate the 661.659-keV state, \(Q=+0.78(9)\), and references 1983Mu12/1989Ra17. Its conflicting historical \(Q\approx-0.05\) alternative is retained separately. Agreement at this source-named fitting target is **not independent EM validation**.

For \(^{136}\)Ba, [adopted lines 58–61](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-adopted-text.ens:58), PDF p. 1, preserve constructive/destructive alternatives: **−0.19(6)/+0.07(7)**, **+0.01(5)/+0.25(5)** and **−0.19(17)/+0.02(18)**. The fixed result differs from the negative central value by −0.1132375 e b: about 1.89 or 0.67 quoted margins for the two negative determinations. These are descriptive comparisons, not significance tests. The source does not specify which numerical target/branch it used; exact central-value calibration replay is unresolved. No alternative was selected to improve agreement.

For \(^{135}\)Ba, Nomura Table VI, PDF p. 9/[TeX line 993](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:993), supplies the directly tabulated negative-parity row. The reconstructed total exceeds the printed theory by **0.0469303 e b** and the paper-quoted experiment by **0.1969303 e b**. Its boson contribution, 1.1255734 e b, rounds to the printed 1.13; this numerical proximity does **not** prove that the author omitted a fermion term. The [archived adopted value](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc135-adopted-text.ens:107) is +0.96(8), not +0.98(8); both are retained without averaging or treating them as independent measurements.

The existing core archives add limited checks: \(^{130}\)Ba gives model **−0.5695005** versus principal alternatives **−1.02(16)/−0.09(16)**; \(^{134}\)Ba gives **−0.2750540** versus **−0.26(8)/+0.15(8)**. All historical alternatives and exact locators are in [source-constraints.json](source-constraints.json). Shared Coulomb-excitation provenance with the charge-calibrating \(B(E2)\) values prevents assuming statistical independence.

Other directly tabulated constraints are retained without extending the model: Table VI gives \(^{135}\)Ba magnetic moment theory **−1.161**, experiment **−1.001(15) \(\mu_N\)**; adopted \(^{137}\)Ba gives **−0.992(26) \(\mu_N\)**. The paper's moment-column header prints \(\mu_N^2\), which is dimensionally inappropriate for a magnetic moment. Magnetic calibration is outside the frozen E2 contract. The adopted isomer lifetimes and \(B(M4)=2.50(7)\), 2.719(9) W.u. concern parity-changing decays to \(3/2^+\), outside this single-negative-parity E2 space; they are not E2 holdouts.

Actual validation: the numerical benchmark exited 0 under one-thread BLAS; the source-extraction script also exited 0. Direct stretched-state moments agree with independently extracted \(M=1/2\) odd-state RMEs within **\(4.09\times10^{-14}\) e b**; the core \(M=2\)/\(M=0\) check is within **\(2.38\times10^{-14}\)**. Parent-moment differences are below **\(1.49\times10^{-13}\)**. Fixed inputs and shared modules remained unchanged. [benchmark-results.json](benchmark-results.json) records hashes, charge calibration, decomposition and checks; both CSV files contain the numerical sidecar.

The two missing NNDC datasets were lawfully saved in [the new raw collection manifest](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/manifest.json); the scoped archive gate passed. These are evaluated summaries, not original experimental reanalyses or an exact 2017 NNDC snapshot. Source pages/text were not copied into publishable output artifacts.

The available support is therefore a consistent \(^{137}\)Ba calibration anchor plus imperfect, partly ambiguous additional static-moment comparisons. Energy agreement cannot substitute for these EM checks. Neither these moments nor full scalar closure establish physical intrinsic shape, and the published EM/invariant figures remain unreplayed.
