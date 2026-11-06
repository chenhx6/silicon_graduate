**Independent case/source replay audit — declared \(^{129}\mathrm{Ba}\) single-j IBFM**

Review date: **2026-11-06**, as specified for this task. The existing `20261105` run directory is retained. Machine-reported UTC timestamps remain separately recorded as observed; the container reported November 5 during the audit. No directory or provenance timestamp was rewritten to reconcile that clock difference.

**Finding.** The declared \(^{128}\mathrm{Ba}\)-core, \(N_B=8\), signed-\(Q_{hh}\) calculation closely reproduces the **published theoretical low-energy subset**. All five core points agree within 0.365 keV; all six odd negative-parity points agree within 0.721 keV. It is not an exact match at every apparent 1-keV rounding interval: \(15/2_1^-\) is 0.720 keV above the source's 485-keV plot point.

The case's E2 normalization and photon-anchor arithmetic reproduce independently. The 482.605-keV energy RMS, the nonyrast discrepancies and the photon-ratio failures remain. In particular, the 604.7-keV branch requires a negative magnetic scale to match its central ratio, because its calculated E2 contribution alone is already too large. The empirical 157-keV decay also connects states ordered oppositely in the model, so its tabulated photon result is a strength diagnostic using measured phase space, not a self-consistent predicted downward decay.

This supports a **partial source-spectrum replay** of the displayed states. It does not certify the original PBOS producer, an author input deck, unprinted excited states or the original author's \(^{129}\mathrm{Ba}\) electromagnetic matrix elements.

**Inputs and independence.** The following existing files were read and preserved:

- `system/scripts/ba129_ibfm_prediction.py`
- `outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-v1/prediction.json`
- The frozen IBFM, energy and photon contracts named by that prediction.
- The SHA-locked kernel and the adopted \(^{128}\mathrm{Ba}\) ENSDF input.
- `raw/papers/gpt/query/20261105-nomura2017-input-audit/nomura2017-v2-source.tar.gz`
- The exact extracted `even.level.pdf` and `ba.level.pdf`, plus the supplied paper-page renders.

The source archive SHA-256 is `f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf`; it matches the archive inspected in the earlier input audit. The two extracted figure PDFs are byte-identical to the archive members.

The new source extraction reads no prediction, model output, experimental energy list or parent exploratory marker JSON. Axis labels and series identities were checked visually against paper pp. 6–7. The source-only point file was frozen before opening the numerical case record:

```text
source-points-frozen.json SHA-256
46b90e618a4c95c377bb61c7f59eb782d05c3f35f4be5418f0dded1d784ac45d
```

The parent supplied an expectation of agreement, so this is not a blind study. Independence here means that source calibration and marker identification were determined from the original figure geometry and labels, without adjusting them to model values.

**Vector extraction and precision.** Coordinates below are PDF points with origin at the top left and \(y\) increasing downward. Axis calibration uses the ends of explicitly labeled ticks; the remaining ticks check linearity. It does not use text-box centers or the bounding rectangle of the plotting panel as energy anchors.

| Source panel | Axis anchors | Frozen mapping |
|---|---|---|
| `even.level.pdf`, Fig. 3(a) | \(E=0\): \(y=182.828170776\); \(E=4\): \(y=11.739074707\) | \(E[\mathrm{MeV}]=4.274455239445-0.02337963138445\,y\) |
| `ba.level.pdf`, Fig. 5(c) | \(E=0\): \(y=349.191955566\); \(E=1.5\): \(y=226.985458374\) | \(E[\mathrm{MeV}]=4.286089081868-0.01227430647684\,y\) |

The odd-panel lower border is at \(y=357.339050293\), corresponding to approximately **−0.1 MeV**, not zero. Treating the panel bottom as the zero-energy axis would corrupt the extraction.

The \(N=72\) and \(N=73\) coordinates are independently fixed by the neutron-number ticks: \(x=62.268123627\) and \(x=61.899257660\), respectively. Each selected marker is verified against the endpoint of its corresponding colored connecting curve.

Marker geometry was handled separately:

- Circles use the symmetry center of their eight Bezier segments.
- Squares use their rectangle center; diamonds use opposite-vertex symmetry.
- For the particular up/down/left triangles in these files, the plotted anchor is the tip/base midpoint convention. It agrees with the bounding-box center and the connecting-curve vertex. Their polygon centroid is not generally the data coordinate. For example, using the down-triangle centroid for core \(0_2^+\) would shift the extracted energy by **+23.380 keV**; for odd \(9/2_1^-\), by **+12.274 keV**. A left triangle's centroid shifts \(x\), even when its \(y\) is unchanged.
- The five-point star uses the rotational center of its five outer tips. The odd \(17/2_1^-\) anchor is \(y=250.367630005\). Its bounding-box midpoint is approximately \(y=250.081153870\), which would spuriously increase the recovered energy by **3.516 keV**. The true center independently agrees with the connecting-curve vertex.

The [star-center crop](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-case-review/star-anchor.png) and [triangle-anchor crop](/workspace/wiki/tmp/ba129-controlled-pairing/ibfm-case-review/triangle-anchor.png) display these source-only checks.

The other labeled tick residuals are at most \(2.23\times10^{-4}\) keV for the core and \(1.25\times10^{-4}\) keV for the odd panel. The recovered source energies lie within \(2.47\times10^{-4}\) keV of an integer-keV lattice. That is numerical extraction precision from encoded vector paths, **not experimental or theoretical accuracy**.

The table uses integer-keV plot values. A ±0.5-keV comparison is only a declared nearest-keV rounding sensitivity; the original plotting data and rounding rule are unavailable. It must not be presented as an author uncertainty or confidence interval. The odd \(15/2_1^-\) mismatch cannot be explained by that nearest-keV envelope alone.

**Core spectrum: all five requested Fig. 3(a) points.** Energies are relative to the computed \(0_1^+\). No energy offset was fitted.

| \(^{128}\mathrm{Ba}\) state | Source plot (keV) | Exact declared core calculation (keV) | Calculation − plot (keV) |
|---|---:|---:|---:|
| \(2_1^+\) | 348 | 348.063923 | +0.063923 |
| \(4_1^+\) | 962 | 962.352309 | +0.352309 |
| \(6_1^+\) | 1811 | 1810.800782 | −0.199218 |
| \(0_2^+\) | 2101 | 2101.259430 | +0.259430 |
| \(2_2^+\) | 1300 | 1299.635950 | −0.364050 |

Locator: Nomura, Nikšić and Vretenar, PRC **96**, 014304 (2017), DOI `10.1103/PhysRevC.96.014304`, arXiv-v2 manuscript p. 6, Fig. 3(a), \(N=72\). These are **theory-panel points**, not the experimental core energies.

**Odd negative-parity spectrum: all six requested Fig. 5(c) points.** The plot's zero is the lowest negative-parity \(9/2_1^-\) state. The parent case uses the \(11/2_1^-\) state as its comparison reference. The audit removes that bookkeeping difference by subtracting the computed \(9/2_1^-\) eigenvalue; it does not tune an offset.

| \(^{129}\mathrm{Ba}\) state | Source plot (keV) | Exact declared calculation (keV), relative to \(9/2_1^-\) | Calculation − plot (keV) |
|---|---:|---:|---:|
| \(7/2_1^-\) | 110 | 110.424757 | +0.424757 |
| \(9/2_1^-\) | 0 | 0.000000 | 0.000000 |
| \(11/2_1^-\) | 81 | 80.772634 | −0.227366 |
| \(13/2_1^-\) | 467 | 466.707126 | −0.292874 |
| \(15/2_1^-\) | 485 | 485.720422 | **+0.720422** |
| \(17/2_1^-\) | 1213 | 1213.123761 | +0.123761 |

Locator: the same manuscript p. 7, Fig. 5(c), \(N=73\). The \(7/2_1^-\) value is recovered from a fresh solve; it is not one of the ten states in the parent's experimental comparison.

The near agreement supports the declared \(128/8\) construction and its tensor normalization as a numerical reconstruction of this displayed spectrum. It does not establish that the authors executed exactly the same input values, counting card or code. The 0.720-keV residual is retained; no core change, parameter change, matrix sign change or marker redefinition was made to remove it.

**Energy failure outside the displayed subset.** The audit reproduces every parent-recorded core and odd-case energy to numerical precision. The stated **482.605462-keV RMS** uses **nine residuals from ten mapped states**, excluding the fixed \(11/2_1^-\) reference. If its exactly zero residual is included in the denominator, the ten-row RMS is 457.839741 keV. Neither quantity is an experimental \(\chi^2\) or a likelihood.

The following case states are outside the published Fig. 5(c) subset:

| Conditional state match | Experimental relative energy (keV) | Model relative energy (keV) | Residual (keV) |
|---|---:|---:|---:|
| \(13/2_2^-\), \(E_x=883.43\) keV | 604.620 | 1073.303821 | **+468.683821** |
| \(15/2_2^-\), \(E_x=1210.0\) keV | 931.190 | 1640.225578 | **+709.035578** |
| \(17/2_2^-\), \(E_x=1545.3\) keV | 1266.490 | 1817.431631 | **+550.941631** |
| \(19/2_1^-\), \(E_x=1475.4\) keV | 1196.590 | 1011.021043 | −185.568957 |
| \(19/2_2^-\), \(E_x=1845.0\) keV | 1566.190 | 2572.957903 | **+1006.767903** |

These rows retain the existing increasing-energy ordinal map. They have not been reassigned to improve agreement. The old energy-contract filename still contains rotor-specific fields, but the IBFM case consumes its state data, ordinals and reference only; no old rotor gap, inertia or optimization bounds enter this calculation.

Agreement with the original paper's displayed lowest states therefore does not repair the extended case's higher-state mismatch. These residuals test the present declared state correspondence; they are not an accusation that the source plotted these unprinted states incorrectly.

**Independent E2 normalization check.** The audit inspected the frozen adopted ENSDF text at lines 48–53: \(2_1^+\) level energy 284.00 keV, half-life \(105(9)\) ps, sole listed 284.10-keV E2 photon with relative intensity 100 and \(\alpha_{\rm tot}=0.0539\). The photon energy, not the slightly different level energy, is used in the \(E_\gamma^5\) factor.

With the contract's declared \(C_{E2}=1.2239\times10^{13}\ {\rm s}^{-1}{\rm MeV}^{-5}/(e^2b^2)\),

\[
B_\downarrow(E2)=
\frac{\ln2}
 {T_{1/2}(1+\alpha_{\rm tot})C_{E2}E_\gamma^5}
=0.27652516113300324\ e^2b^2.
\]

This correctly distinguishes half-life from mean lifetime and includes conversion once. The numerical rate coefficient was kept frozen; it was not replaced by another convention or more digits.

Direct core wavefunction contraction, without calling the parent's calibration routine, gives

\[
B_{\rm unit}(0_1^+\to2_1^+)=78.54029693797942,
\]
\[
e_B=\sqrt{\frac{5B_\downarrow}{B_{\rm unit}(0\to2)}}
=0.1326801823613452\ e\,b,\qquad
\frac{e_F}{e_B}=\frac{0.125}{e_B}=0.9421150753288176.
\]

The factor five is the upward/downward detailed-balance factor, not an extra photon rate factor. The core's theoretical first-\(2^+\) energy is 348.064 keV, as in the source theory panel; using the experimental 284.10-keV photon to extract the calibration strength is consistent with the declared empirical-charge prescription, not a claim that the model predicts the observed core energy exactly.

The normalized operator actually tested is

\[
\overline T(E2)=\frac{T(E2)}{e_B}
=Q_{\chi'=0.35}
-\frac{e_F}{e_B}\frac{(1-2v^2)Q_{hh}}{\sqrt5}
[a^\dagger_h\times\widetilde a_h]^{(2)}.
\]

The independently assembled block matrix agrees with the runner's normalized E2 matrix to \(8.88\times10^{-16}\) in maximum entry. The signed \(Q_{hh}=-\sqrt{525/(143\pi)}\), occupation \(v^2=0.453\), Hamiltonian \(\chi=-0.18\), and separate EM \(\chi'=+0.35\) are unchanged. The fermion/boson relative amplitude is retained; physical E2 strengths are \(e_B^2\overline B_Q\), not a pure-core approximation.

This is a central-value calibration using an adopted input. It neither propagates the quoted lifetime uncertainty nor proves the unprinted \(e_B\) used by the 2017 authors. The source's displayed spectra provide no transition-specific \(^{129}\mathrm{Ba}\) EM benchmark for that stronger claim.

**Phase space, magnetic scale and anchor.** For every case pair, the target changes \(I\) by one unit and the reference changes \(I\) by two. Direct contractions confirm the reference particle-\(j\) M1 RME vanishes. For the target, \(L+j=J\) has zero RME between different total spins; the largest checked \(L+j\) RME is \(1.33\times10^{-15}\). Hence no physical \(g_B\) needs to be invented:

\[
T(M1)_{fi}=\sqrt{\frac3{4\pi}}(g_j-g_B)j_{fi},
\qquad I_f\ne I_i .
\]

Using the same eigenvector phases for both tensors and the frozen **measured** photon energies,

\[
r_\gamma=a+\eta b,\qquad
a=\left(\frac{E_t}{E_r}\right)^5
\frac{\overline B_{Q,t}}{\overline B_{Q,r}},\qquad
b=\frac{E_t^3}{E_r^5}
\frac{B_{j,t}}{\overline B_{Q,r}}.
\]

Here \(a\) is dimensionless, \(b\) has units \({\rm MeV}^{-2}\), and \(\eta\) has units \({\rm MeV}^2\). In a fully specified common-unit rate convention,
\[
\eta=
\frac{C_{M1}}{C_{E2}}\frac3{4\pi}
\frac{(g_j-g_B)^2}{e_B^2}.
\]
The case determines this combination from the old photon anchor; it does not separately determine a \(g\) factor or its sign. There is no missing \(3/(4\pi)\) in the runner's particle-\(j\) coefficient: it belongs to the fitted common scale. The diagonal magnetic moment would require the total-\(J\) term and is outside this test.

The 153.8/518.6-keV anchor gives
\[
a_{\rm anchor}=0.0012266405404,\qquad
b_{\rm anchor}=0.00469360951186\ {\rm MeV}^{-2},
\]
\[
\eta=\frac{0.074-a_{\rm anchor}}{b_{\rm anchor}}
=15.5047750085879\ {\rm MeV}^{2}>0.
\]

The scale is not clipped or re-estimated from the other five branches. Photon intensities are compared with radiative widths; no extra \((1+\alpha)\) factor is applied to these photon ratios. The separate core half-life calibration correctly contains its conversion correction.

The full direct-contraction and scalar-arithmetic replay reproduces the recorded numerical strength fields to at most \(7.11\times10^{-15}\) absolute difference. Both E2 and M1 components enter an integrated photon intensity incoherently; their relative phase still matters within the E2 boson/fermion sum, but \(\eta\) cannot determine a signed physical \(\delta\).

| Target/reference photons (keV) | Role | Calculated \(r_\gamma\) | Reported central ratio | Calculated/reported | Individually required \(\eta\) (\({\rm MeV}^2\)) |
|---|---|---:|---:|---:|---:|
| 153.8 / 518.6 | Scale anchor | 0.074000 | 0.074000 | 1.000 | 15.5048 |
| 521.0 / 674.8 | Withheld | 0.099940 | 1.060976 | 0.0942 | 566.3734 |
| 157.0 / 678.0 | Withheld | 0.027343 | 0.066583 | 0.4107 | 37.8608 |
| 526.6 / 634.9 | Withheld | 2.393510 | 0.928571 | 2.5776 | 3.4926 |
| 364.7 / 461.6 | Withheld | 0.457595 | 3.936364 | 0.1162 | 358.8266 |
| 604.7 / 701.3 | Withheld | 2.774548 | 0.608333 | 4.5609 | **−13.9172** |

The last row has \(a=1.632996644>0.608333333\). Holding the declared wavefunctions, E2 calibration, state map and reference purity fixed, **no nonnegative magnetic contribution can reproduce that central ratio**, even if that row were considered alone. This is a conditional central-value failure of the specified test. It is not a confidence level, an experiment-independent rejection of all IBFM variants, or a unique mode determination.

**Kinematic limitation exposed by the audit.** The photon contract expressly fixes measured photon energies, while taking matrix elements from the model. That is a coherent way to isolate a wavefunction-strength test, but it is not a complete prediction of the decay scheme:

| Target photon used in the test (keV) | Energy difference of the mapped model states (keV) |
|---|---:|
| 521.0 | 727.403339 |
| **157.0** | **−121.330083** |
| 526.6 | 1440.606776 |
| 364.7 | 385.934491 |
| **153.8 anchor** | **19.013296** |
| 604.7 | 1073.303821 |

For the 157-keV target, the mapped \(19/2_1^-\) parent lies below the mapped \(17/2_1^-\) daughter. The nonzero tabulated strength remains a mathematically defined matrix element; it cannot be called a predicted downward photon at the model's own energies. The anchor's 19.013-keV model spacing versus 153.8-keV empirical spacing similarly shows why the magnetic scale depends on the declared empirical-kinematics protocol. No alternative phase-space choice or new scale fit was performed.

**Scope of the conclusion.** The original-source agreement substantially strengthens the numerical plausibility of the chosen \(128/8\) construction for the lowest displayed levels. It does not close the source's missing run-card/producer information or validate unprinted higher states and EM wavefunctions. The extended case's energy and central photon-ratio mismatches survive an independent case-level audit.

The numerical eigensolver used here is the same SHA-locked new kernel, not a second independently implemented Hamiltonian. Independence comes from the source-vector extraction, the new case wrapper, direct EM contractions, independent core-charge algebra and explicit checks against the frozen output. Original-author numerical production has not been certified.

The parent-reported 25 kernel tests were not rerun; this task performed the requested case/source checks. The audit re-solve and arithmetic took approximately 0.530 seconds, with `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`. No Hamiltonian parameters, state ordinals, core choice or old contracts were changed.

**Artifacts.**

- [Source-only vector extraction and frozen calibration](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/source-points-frozen.json)
- [Source spectrum comparison CSV](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/source-comparison.csv)
- [Full ten-state comparison CSV](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/energy-comparison.csv)
- [Photon and kinematic audit CSV](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/photon-comparison.csv)
- [Machine-readable case audit, diagnostics and preserved-input hashes](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/case-audit.json)
- [Source-only extraction procedure](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/extract_source_points.py)
- [Independent case audit procedure](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/ibfm-case-review/audit_case.py)

The scripts refuse to overwrite their frozen output files. All new analytical outputs are confined to this review directory. Publisher-figure crops are confined to the new temporary review directory. Protected inputs were hash-checked before and after the numerical audit; there were no Git actions or edits to the kernel, case runner, prior outputs, source records, get-paper or `PLAN.md`.
