# Frozen-parameter Ba129 Hplus continuation — 2026-11-05

All thirty mapped references now pass the forward, nested-grid, selected-gap and reverse-path checks. **Twenty-eight pass every declared control.** C60 best and C120 start1 pass completely; the C120 start0 **19/2 pair remains flagged** because its full-path BCS+ weight comparison under a common +100 MeV reference shift exceeds the predeclared tolerance. The final forward branch is resolved, but the complete acceptance test has not passed for that pair.

These are mathematical **Hplus-connected references** at fixed parameters. They do not establish physical one-quasiparticle selection, resolve the accepted source sign/label/trace issue, validate the full model, or certify a reproduction of the original authors' code. No parameters were fitted here.

The consolidated result is [refined-results.json](refined-results.json); the thirty state rows are in [refined-state-results.csv](refined-state-results.csv), and the eighteen spin-sector diagnostics in [spin-diagnostics.csv](spin-diagnostics.csv). [verification.json](verification.json) records provenance, anchor arithmetic and the located control failure. The earlier [results.json](results.json) and uniform-grid paths remain as an explicitly superseded, partly unresolved audit trail.

**Inputs and labels.** Exact values were read from the parent JSON files, with SHA-256 checks before and after computation. All three records have zero active-bound masks; their parent optimizations nevertheless used finite declared bounds.

| Case | Exact record, relative to `outputs/l4/20261105-ba129-model-readiness/` | Parent RMS excluding anchor, keV | Source SHA-256 prefix |
|---|---|---:|---|
| C60 best | `model-fit-C60/energy-calibration.json`, `best` (start 0) | 71.9718707014784 | `5ff728d2ac6c362e` |
| C120 start0 | `model-fit-free-inertias-C120/energy-calibration.json`, `starts[start=0]` | 39.925201699389206 | `3365fe1b6f3dc6eaa` |
| C120 start1 | same file, `starts[start=1]` | 43.26487795913006 | same |

The RMS values are **parent computation, not independently refitted**. Full input, contract and module hashes, and the exact parameters, are in `refined-results.json → input_sha256 / cases[].parameters`. The Nambu module hash is `700970f514b27a4d7333f0c1a4c3a96c91db4ab3ae24f9756d3640eadb8fc02d`; the frozen rotor hash is `1d9dd8814892556e7731b41dd2edd98ab83951fca168711fcb5951f8ca647908`.

Both old contracts specify the same ten labels and the **11/2, ordinal 0, Ex278.81 keV anchor**. The reconstructed t=0 relative energies match the stored parent comparisons exactly in this run. The mapped 9/2 state is an ordinary tracked row, never the anchor. The reported shift is

\[
\delta E_i=1000\{[E_i(1)-E_{11/2,0}(1)]-[E_i(0)-E_{11/2,0}(0)]\}\ {\rm keV},
\]

with matrix energies in MeV. Absolute anchor shifts are +10.996784728, +172.755338759 and −45.476825529 keV for C60 best, C120 start0 and C120 start1, respectively.

**Numerical procedure.** Construction uses the unchanged `paired_single_j_nambu.build_nambu` and `hamiltonian_at` with the supplied sign convention for K. The path scales K only; Delta remains 1 MeV. Seeds are obtained as `X† Xplus ψ_plus`, using the actual original-coordinate embeddings and the old Hplus ordinals. Selection uses neither the sign of total energy nor the upper half of an interleaved spectrum.

Only the one or two mapped states at each spin are assigned, with a one-to-one maximum-squared-overlap assignment. The complement requires no individual labels. We record the best-versus-alternative assignment margin, individual overlaps, selected-projector principal-angle fidelity, BCS+ coordinate weights, gaps to the unselected complement and to all other states, and eigen-residuals. BCS+ weight is a coordinate-sector weight, not a particle count or a transfer strength.

The uniform grids were 33 → 129 → 513 → 2049, stopping when the declared tests passed. Three failed C120 start0 sectors then received bounded local bisection under the same tolerances. The supplement allowed at most 18 iterations and 16,385 nodes per spin; no cap was reached. C60 stopped at 129 everywhere; C120 start1 required 513 at 13/2 and 19/2 and 129 elsewhere. C120 start0 used 129 at 9/2–13/2 and nonuniform meshes of 2,088 / 2,091 / 2,115 nodes at 15/2 / 17/2 / 19/2.

For a fixed set of energy ranks, the interval gap diagnostic is
\[
g_{\rm lower}=\min(g_{\rm left},g_{\rm right})-\|K\|_2\Delta t
              -2(10^{-10}\ {\rm MeV}).
\]
Each eigenvalue is Lipschitz with constant \(\|K\|_2\); using the nearer endpoint gives this conservative bound for differences of two eigenvalues. Both complement and individual gaps must have positive bounds. This is a floating-point diagnostic with a stated residual allowance, not a directed-rounding proof. Rank stability is checked along the final path. It prevents a large sampled overlap from concealing a skipped narrow avoided crossing.

| Case | Minimum selected step overlap² | Minimum selected-projector fidelity | Minimum sampled complement gap, keV | Minimum interval gap bound, keV | All controls |
|---|---:|---:|---:|---:|---|
| C60 best | 0.999997136 | 0.999996958 | 27.478424 | 21.012303 | 10/10 |
| C120 start0 | 0.995194048 | 0.995194047 | 0.000785952 | 0.000418866 | 8/10; joint 19/2 pair flagged |
| C120 start1 | 0.999442435 | 0.999379468 | 21.182393 | 10.698297 | 10/10 |

The final minimum alternative-assignment margins are 0.999994650, 0.990388118 and 0.998903763. There are no final assignment ties or rank jumps. The maximum selected eigen-residual is \(7.59\times10^{-14}\) MeV.

**State results.** Each case cell is **anchor-relative shift in keV / endpoint BCS+ weight**. Level energies identify the predeclared mapping; the table does not assert new experimental energies.

| Mapped level label, keV | I; Hplus ordinal | C60 best | C120 start0 | C120 start1 |
|---:|---|---:|---:|---:|
| 182.04 | 9/2; 0 | −10.619 / 0.999942 | −81.964 / 0.982892 | −122.310 / 0.960974 |
| 278.81 | 11/2; 0; anchor | 0 / 0.998152 | 0 / 0.968898 | 0 / 0.959350 |
| 643.6 | 13/2; 0 | +12.862 / 0.995981 | +19.090 / 0.960371 | −125.730 / 0.124853 |
| 797.4 | 15/2; 0 | +22.435 / 0.994445 | −291.627 / 0.100063 | +15.858 / 0.252459 |
| 883.43 | 13/2; 1 | +8.306 / 0.997131 | +3.812 / 0.964368 | +43.838 / 0.941753 |
| 1210.0 | 15/2; 1 | +13.457 / 0.996380 | +86.554 / 0.942796 | +189.498 / 0.881258 |
| 1318.4 | 17/2; 0 | +32.559 / 0.992751 | −77.080 / 0.102296 | −539.189 / 0.275219 |
| 1475.4 | 19/2; 0 | +44.120 / 0.990783 | −359.896 / 0.083886 † | −497.224 / 0.175404 |
| 1545.3 | 17/2; 1 | +26.457 / 0.994404 | −88.616 / 0.920584 | +182.765 / 0.858007 |
| 1845.0 | 19/2; 1 | +38.406 / 0.992548 | +88.129 / 0.107460 † | +278.689 / 0.448526 |

† Forward/nested-grid/reverse and gap checks pass, but the joint 19/2 sector fails the declared full-path reference-shift weight control. These two rows remain candidate results under that acceptance policy. The located tolerance exceedance is in ordinal 0; retaining both rows as flagged follows the joint spin-sector rule, not evidence that both states individually fail.

C60 retains at least 0.99078 BCS+ weight at the endpoint. Several continued C120 references acquire predominantly BCS− character. In C120 start0, the 17/2 ordinal-1 endpoint weight is 0.92058, but its minimum along the path is only 0.04819. Endpoint weights alone therefore conceal substantial exchange of sector character. These results support no physical-state-selection claim.

**Narrow-crossing and control audit.** The sampled C120 start0 minima occur at:

| I | t at sampled minimum | Selected/complement gap | Smallest grid interval |
|---|---:|---:|---:|
| 15/2 | 0.5990371704101562 | 23.137791 eV | \(1.90735\times10^{-6}\) |
| 17/2 | 0.5694580078125 | 614.190460 eV | \(3.05176\times10^{-5}\) |
| 19/2 | 0.4567323923110962 | 0.785952 eV | \(1.19209\times10^{-7}\) |

The 2,049-point uniform 15/2 and 19/2 ordinal-0 candidates jumped energy rank. Resolving those avoided crossings changes their reported relative shifts from +142.894 to −291.627 keV and from +333.915 to −359.896 keV. These rejected uniform candidates must not be reused as accepted adiabatic results. The positive final interval bounds and unchanged ranks apply only to the refined paths.

All reverse paths recover the forward eigenpairs and original seeds; minimum return fidelity is 0.9999999999999964. With K set to zero along a dummy five-point path, maximum energy error is \(3.02\times10^{-14}\) MeV and maximum BCS+ weight error is \(1.11\times10^{-15}\).

Under a common +100 MeV shift, corrected energies agree within \(1.99\times10^{-13}\) MeV across the audit. The only failed tolerance is C120 start0, 19/2 ordinal 0 at **t=0.4567326307296753**: BCS+ weights 0.3815502340190007 and 0.3815502914356118 differ by **\(5.74166\times10^{-8}\)**, exceeding \(10^{-8}\). The local gap is 0.811019 eV; the shifted eigen-residual is \(1.18\times10^{-13}\) MeV. Adding/subtracting the scalar reference itself introduces a matrix difference of norm \(1.42\times10^{-14}\) MeV. These diagnostics are consistent with sensitivity of a very narrow crossing to floating-point eigensystem errors; higher-precision confirmation has not been performed. Endpoint weight differences are below \(2.8\times10^{-15}\), but endpoint agreement does not override the full-path control failure. Tolerances were not relaxed.

Ordered-gap controls also pass. At I=1/2, included only as a numerical subspace control, the full plus projector matches the upper-d set on all 129 nodes for each case. Initial block gaps are 2.532182, 5.109591 and 3.251479 MeV. Among the mapped states, the ordered-block condition holds for C120 start0 at 9/2, 11/2 and 13/2, with gaps 2.842170, 1.569364 and 1.318890 MeV; its mapped labels agree with the upper-d construction throughout. The C60 and C120 start1 blocks already interleave at every mapped spin, so that shortcut was inapplicable there. For example, C120 start0 15/2 ordinal 0 starts at full index 47 although d=48.

**Reproduction and limits.** From `/workspace/wiki`, run:

```bash
python3 -B outputs/l4/20261105-ba129-controlled-pairing/continuation/run_continuation.py
python3 -B outputs/l4/20261105-ba129-controlled-pairing/continuation/run_adaptive_refinement.py
python3 -B outputs/l4/20261105-ba129-controlled-pairing/continuation/verify_continuation.py
```

The runners write only into this continuation directory; their logs are `run.log`, `adaptive-run.log` and `verification.log`. The final two commands use the first run's saved inputs and results. `spin-diagnostics.csv` is a compact projection of `refined-results.json → cases[].spin_results`; detailed paths and endpoint vectors remain in the three case subdirectories.

This audit covers exactly three frozen parent minima, the specified ten labels and this particular linear coupling path. It supplies no fit improvement, uncertainty propagation, physical number projection, EM or transfer forecast. A positive numerical gap or reversible continuation does not settle the source's physical-particle/hole versus BCS-sector distinction. The sole remaining numerical failure is the strict reference-shift weight tolerance described above; additional numerical precision/stability work would be needed to remove that flag under the present policy. The original PDFs, frozen cores, fit inputs, PLAN, get-paper and other sessions' files were not modified. No commit was made.

**Primary-source applicability addendum — Protopapas and Klein (1997).** The archived original is `raw/papers/gpt/query/20261105-pairing-rotor-foundations/protopapas-klein1997-prc55-699.pdf`, SHA-256 `b7ba75ea84348c3c6f877be6ce21c522428d19f9f226f6f1929111313c284053`. The relevant selection discussion is **§VII, printed p.709, PDF page 11/15**; §III concerns single-particle transition operators.

In §VII the authors first diagonalize the part antisymmetric under particle–hole conjugation, identify its positive-energy half through the BCS limit, and then restore the symmetric part. They describe projector tracking and subsequently a fixed-angular-momentum noncrossing prescription that retains energy ordering. The core-particle formulation in §VI, Eqs. (6.5)–(6.7), places the same core-excitation operator in both diagonal blocks. These are source statements within their formalism.

The frozen calculation here starts with the **full rotor already present in both diagonal blocks**:
\[
H_K(t)=
\begin{pmatrix}
A+E&tK\\tK^\dagger&A-E
\end{pmatrix}.
\]
It follows specified Hplus eigenvectors at this interleaved starting spectrum. Thus its selected references do not acquire the paper's physical-half identification. In our own matrix convention, switching on the common rotor instead would give the distinct family
\[
H_R(s)=
\begin{pmatrix}
sA+E&sK\\sK^\dagger&sA-E
\end{pmatrix},\qquad 0\le s\le1.
\]
These families share an endpoint and have different starting operators and seed subspaces. This second formula is an algebraic comparison in our convention, not an established identification with the authors' KKDF construction.

That identification remains unmapped: their U,V are coefficients of fractional parentage to the A±1 even cores [p.701, Eqs. (2.11)–(2.12)]; their energy reference and core excitations are defined in Eqs. (2.16)–(2.19); and their normalization is specified by Eqs. (2.22)–(2.24), pp.701–702. Our normalized orthogonal Nambu vectors have not been related to those conventions. Similar common-core matrix terms alone do not establish that relation.

A comparison of rotor-switch-on and K-switch-on paths is a **future controlled test only**. It would need explicit seed-projector, symmetry-sector and gap checks, including treatment of degeneracy at the zero-rotor limit. It has not been run here. This addendum changes no runner, numerical result, continuation label, tolerance or acceptance status: the bounded K(t) audit is complete with its recorded 28/30 all-control acceptance and the joint 19/2 control flag.
