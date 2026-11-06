**The complete/restricted distinction survives all three prospectively chosen
adopted-moment matches. The out-of-domain proxy excursion does not survive at
these matches.** The alternative central target of +0.98 eb gives the same
qualitative outcome. These statements concern the evaluated targets on the
fixed Gamma-only path; they are not a continuous-interval coverage claim.

At the adopted central +0.96 eb, the signed-moment root is
Gamma0 = 0.37929361596143757 MeV. The complete signed ratio is −0.0920071991,
whereas the all-J+2 proxy's nonnegative raw argument is 0.7974544482.
Their conditional folded/full and proxy coordinates are 28.2403° and 12.3708°,
a difference of 15.8695°. The original Gamma0 = 0.6 result remains
z_proxy,all = 1.0241441427 with an undefined angle; it was not clipped or replaced.

The separate [prospective protocol](moment-match-protocol.json) was frozen at
2026-11-06T04:15:55.602132+00:00. The targets +0.88, +0.96, +1.04 and the
alternative +0.98 eb were fixed before new root or proxy calculations.
[Signed-Qs roots](moment-match-roots.json) were completed at
04:18:59.642091 UTC, before the diagnostic stage began at 04:19:13.814715 UTC.
Only Qs entered root selection. Each target had one detected sign-changing
bracket, [0.30, 0.45] MeV; Brent's method used absolute and relative tolerances
of 1e-12. Each root also has a recorded sign-changing certificate at
Gamma_root ± 1e-8 MeV. Across the 37 distinct Qs evaluations, Qs was strictly
increasing at the sampled points. This does not exclude tangent roots or paired
crossings between unexamined samples.

The source is the existing official adopted ENSDF artifact
`raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc135-adopted-text.ens`.
L107 identifies the 268.218(20)-keV 11/2− isomer; **L111** gives
`MOME2=+0.96 8 (1983Mu12,1989Ra17)`. L112 gives the neutron h11/2-hole
configuration; L113 identifies laser spectroscopy for the moments.
The protocol records its SHA-256 and locators. The literal margin `8` is
0.08 eb here. The lower/upper targets are arithmetic quoted-margin endpoints,
not inferred confidence limits. The +0.98(0.08)-eb paper alternative was supplied
by the user and is kept separate; this task did not reverify its original-paper
provenance or combine it statistically with the adopted value.

The fixed model uses nB = 5, j = 11/2, eps_d = 0.38 MeV, kappa = −0.124 MeV,
chi = −0.24, v² = 0.81 and signed Qjj = −1.081027387032316.
Lambda0 = 1 and A0 = −0.9 remain fixed. The E2 operator retains
eB = +0.1298423794528743 eb, eF = 0.125 eb and chi_E2 = +0.35;
eB comes from the existing 134Ba core Bup = 0.679 e²b² calibration.
Only Gamma0 changes. Every target refers to the lowest-energy J = 11/2 state.

The signed matching convention is

\[
Q_s=\sqrt{\frac{16\pi}{5}}\langle J,J|Q_{20}|J,J\rangle
 =\sqrt{\frac{16\pi}{5}}\,
 \frac{\langle JJ,20|JJ\rangle}{\sqrt{2J+1}}R_{ii}.
\]

The first expression was evaluated in an independently solved stretched
M = 11/2 block during root finding. The second uses the diagonal RME from the
complete M = 1/2 registry after roots were frozen. The numerical RME-to-Qs
factor is +0.7115738032710673. Matching preserves the sign; in particular the
Gamma0 = 0 endpoint has Qs = −0.0194281784 eb. The complete closure always uses
the M = 1/2 registry, which contains 226 multiplets accounting for all
3024 product-space states.

| Target Qs, eb | Role | Gamma0, MeV | Full q2, e²b² | Full q3, e³b³ |
|---:|---|---:|---:|---:|
| +0.88 | Adopted minus quoted margin | 0.333784450 | 0.693019203 | −0.058812114 |
| +0.96 | Adopted central | 0.379293616 | 0.690864150 | −0.052833672 |
| +1.04 | Adopted plus quoted margin | 0.436829943 | 0.687442927 | −0.045514341 |
| +0.98 | Paper alternative central | 0.392286455 | 0.690144703 | −0.051143962 |

| Target Qs, eb | Full signed ratio | Proxy5 raw | Proxy-all raw | Full folded coordinate | Proxy-all coordinate | Coordinate difference |
|---:|---:|---:|---:|---:|---:|---:|
| +0.88 | −0.101941 | 0.726635 | 0.724653 | 28.0497° | 14.5200° | 13.5297° |
| +0.96 | −0.092007 | 0.798968 | 0.797454 | 28.2403° | 12.3708° | 15.8695° |
| +1.04 | −0.079853 | 0.876441 | 0.875113 | 28.4733° | 9.6472° | 18.8261° |
| +0.98 | −0.089204 | 0.817806 | 0.816370 | 28.2941° | 11.7590° | 16.5351° |

Here the full signed ratio is q3/q2^(3/2); its folded coordinate is
acos(|ratio|)/3. The proxy is sqrt(7/10)|C|/S^(3/2), with S the J+2 RME
strength sum and C its unweighted middle-state chain. Its sign is removed by
definition, so the contrast is not attributed to an opposite sign alone.
All four proxy5 and proxy-all arguments lie within their real-angle domain.
The 13.53°–18.83° differences at the three adopted targets are conditional
coordinate discrepancies, not measured differences in intrinsic nuclear shape.
Numerical root digits express reproducibility, not parameter precision.

The signed-network mechanism persists after static matching. At +0.96 eb,
complete q2 is only 2.1048% above the original primary value. Its static
fraction falls from 0.336925 to 0.219548, the other-same-J fraction is 0.074693,
and the entire J+2 sector accounts for 0.219193 of q2.
The matched static contribution, 0.1516775545 e²b², follows algebraically
from the consumed Qs datum and is not independent evidence for the mechanism.
The relevant additional calculation is the off-diagonal and cross-spin network:
the full cubic positive and negative spin-pair sums are
+0.2396170737 and −0.2924507457 e³b³, leaving −0.0528336720 e³b³.
Their cancellation fraction, defined as 1−|net|/sum|spin-pair sums|, is 0.900701.
The all-J+2 chain instead has S = 1.8171909989 e²b² and
C = 2.3348432545 e³b³, producing the much larger raw proxy argument.
The middle-diagonal/off-diagonal parts of C are +0.7474491743 and
+1.5873940801 e³b³. This retains the distinction between a restricted
unweighted chain and complete signed 6j closure.

The core projections accompany that explanation. They are not used alone to
claim causation:

| Target Qs, eb | Static q2 fraction | Other-same-J fraction | P(core R0) | P(core R2) | Mean n_d |
|---:|---:|---:|---:|---:|---:|
| +0.88 | 0.183907 | 0.086069 | 0.720059 | 0.276749 | 2.323746 |
| +0.96 | 0.219548 | 0.074693 | 0.668438 | 0.329762 | 2.325543 |
| +1.04 | 0.258946 | 0.062003 | 0.609977 | 0.385579 | 2.329965 |
| +0.98 | 0.229029 | 0.071643 | 0.654511 | 0.343489 | 2.326361 |

Full P(R) distributions, the separate core-ground R0 probability, signed cubic
spin-pair sums, proxy diagonal/off-diagonal summaries, and direct/6j values
are in [moment-match-results.json](moment-match-results.json). No eigenvector,
full RME matrix or individual cubic state-pair tensor is serialized.

State identity is resolved at the stated sampling. The lowest same-J ordinal
is zero in every case, and both directions of maximum-overlap matching to
the adjacent known Gamma0 = 0.30 and 0.45 states also select ordinal zero.

| Target Qs, eb | Next same-J gap, MeV | Squared fidelity to Gamma0=0.30 | Squared fidelity to Gamma0=0.45 |
|---:|---:|---:|---:|
| +0.88 | 0.546481 | 0.996470 | 0.972527 |
| +0.96 | 0.581269 | 0.982811 | 0.991086 |
| +1.04 | 0.632532 | 0.956675 | 0.999740 |
| +0.98 | 0.592206 | 0.977560 | 0.994288 |

When the four matched points are inserted into the known path, all adjacent
bidirectional best ranks remain zero. Within the 0.30-to-0.45 segment the
minimum adjacent squared fidelity is 0.994810. These diagnostics support
local reorientation of the same lowest branch at the sampled points; they
do not prove a continuous-parameter no-crossing theorem.

Static matching also changes the low negative-parity spectrum appreciably.
The prospective panel contains the lowest two states for
J = 7/2, 9/2, 11/2, 13/2, 15/2, 17/2 and 19/2.
Every energy is relative to that Hamiltonian's lowest 11/2− state;
the positive-parity nuclear ground state is outside this single-j space.
Selected central-match changes are:

| Model level | Primary Gamma0=0.60, MeV | Qs=+0.96 match, MeV | Change, MeV |
|---|---:|---:|---:|
| 7/2−, lowest | 0.919362 | 0.643687 | −0.275675 |
| 9/2−, lowest | 0.449896 | 0.241402 | −0.208493 |
| 13/2−, lowest | 0.404585 | 0.339114 | −0.065471 |
| 15/2−, lowest | 0.691863 | 0.526642 | −0.165221 |
| 11/2−, next | 0.805218 | 0.581269 | −0.223950 |
| 19/2−, lowest | 1.417896 | 1.136287 | −0.281608 |

The lowest 9/2− and 13/2− ordering reverses between the primary and every
matched case. This is a cross-spin spectral change, despite preservation of
the lowest 11/2 branch. The largest absolute shift in the 14-level panel is
0.432150, 0.368434 and 0.280247 MeV for the three adopted targets respectively;
the alternative central gives 0.349196 MeV. All panel rows and the primary
reference are in [moment-match-energies.csv](moment-match-energies.csv).
Same-J energy ranks in this panel are not assigned experimental bands.
No energy objective or experimental energy likelihood was optimized.

All four complete 6j closures pass, with no missing required entries.
The maximum absolute direct/6j discrepancies are 1.75e-14 e²b² in q2 and
4.94e-14 e³b³ in q3. The maximum stretched/RME Qs difference is 6.33e-15 eb;
the maximum RME target residual is 9.11e-15 eb. Core-R probabilities
normalize to within 1.12e-15. Independent M-block lowest-state energies
agree to within 2.05e-14 MeV. Known-grid gaps and signed moments also replay
within the frozen tolerances.

The implementation is [moment-match-run.py](moment-match-run.py), with separate
`roots` and `diagnostics` phases; the readable scalar table is
[moment-match-summary.csv](moment-match-summary.csv).
[moment-match-checks.json](moment-match-checks.json) records the final audit,
artifact hashes and preservation checks. BLAS thread variables were set to one
before numerical imports. Runtime threadpool introspection was unavailable;
no package was installed to add it.

The resulting claim is narrowly conditional: a fixed-operator model state can
match the adopted static moment while retaining a large complete/restricted
coordinate discrepancy. The severe proxy-domain failure at the original
primary is absent at the prescribed matched cases. The static datum has been
used to determine Gamma0, so this is not an independent validation or a
posterior constraint. Its spectral consequences and unvaried model/operator
assumptions remain material limitations. No continuous envelope, global refit,
shape-rigidity inference or new experimental fact is claimed. Work stops after
the frozen targets and diagnostics; the original artifacts and manuscript are
preserved.
