# Claim-to-evidence map

The fields below concern this manuscript. A source's historical review label
does not establish a claim; direct evidence, applicability and dependence do.

| ID | Claim and scope | Evidence | Disposition |
| --- | --- | --- | --- |
| C1 | The declared h11/2 IBFM uses printed Hamiltonian parameters and a stated A−1 core assignment. | Nomura2017 Eqs.1–8, Tables I/III/V; `data/chain-contract.json`; input audit in Wiki | Supported as an explicit reconstruction, not author run-card recovery |
| C2 | Complete q2/q3 require all allowed intermediate spins under the specified RME convention. | Cline1986 p.698; Henderson2020; independent direct/6j closures and axial/spectator controls | Established theory; no novelty claim |
| C3 | Five J+2 states saturate that channel but cover only a fraction of complete q2 in the five primary states. | `data/results/calibrated-chain.json`, every primary `restricted` entry | Supported within the finite model space |
| C4 | 135Ba has z5=1.026115 and z_all=1.024144 for the primary operator. | Same file, 135Ba; operator sensitivity replay | Supported; angle undefined. A property of this operator, not a physical shape singularity |
| C5 | Complete small q3 in 135Ba results from signed cancellation across spin sectors. | Same file, `signed_cubic_spin_pairs`; independent 6j/direct equality | Supported algebraic decomposition; finite model |
| C6 | With exchange/monopole/core/E2 fixed, the sampled quadrupole path changes static strength and restricted interference while q2 varies by less than 2.6%. | `data/results/quadrupole-path.json`; five sampled gaps and bidirectional overlaps | Supported model intervention. No claim about every unsampled value or the unique mechanism in the actual nucleus |
| C7 | Alternate chiE operators remove the particular domain crossing and change cubic signs/trends. | All 35 rows of `data/results/operator-sensitivity.json` | Conclusion-changing qualification retained in the main text |
| C8 | 137Ba static moment is compatible with its calibration target; 135Ba is overpredicted and 136Ba has unresolved calibration branches. | `data/static-moment-constraints.json`; Nomura2017 TableVI; ENSDF135/136/137 precise records | Supported, with calibration dependence and model limitation visible |
| C9 | The model does not reproduce the source's invariant figures. | Wiki `spin-invariant-source-replay/report.md`, source figure vectors and v1/v2 comparison | Explicit reconstruction boundary; not evidence of an error by the authors |
| C10 | Selected diagnostics have conditional utility and related prior studies exist. | Nomura2016 Eq.8/Fig.10; Werner2005; Henderson2020; Bally2022; Rouoof2025 Sec.IV C; Lawrie–Orce2025 Eqs.11–15 | The article cannot claim discovery of truncation, finite-spin dependence or invariant algebra |
| C11 | A Qs-only match along the fixed-operator path retains a large angle separation but changes the calculated spectrum. | `data/results/moment-matched.json` and its energy CSV | Conditional calibration; no new global fit or independent static validation |
| C12 | Calibration to 136/137Ba central moment alternatives can improve unused 135Ba Qs predictions while making full cubic ratios outside-domain. | `data/results/calibrated-operator-predictions.json`; every finite branch retained | Conditional at averaged core Bup; source covariance and physical admissibility remain unresolved |
| C13 | Vogt2017 assigns a tentative 137Ba 15/2 target, but its measured 589-ns lifetime and 0.46-W.u. strength concern the upper 19/2 transition. | `data/vogt2017-transition-constraints.json`; accepted manuscript Fig.6, TableII, Fig.7, TableIII | Supports target availability, not an absolute experimental Rstat denominator |
| C14 | At exactly fixed gamma=20° charge geometry, the unpaired rotor has q2=1/q3=.5 while its all-15/2 ratio varies from .322617 to1.026250. | `data/revision-v2/rigid-control/frozen/{protocol.json,proof.md,results.json}`; independent package replay | Supported counterexample for the declared rotor. Does not establish unchanged IBFM or empirical Ba geometry; no new invariant theorem claimed |
| C15 | Fixed135/137Ba calculation reproduces the ordering of the six displayed negative-parity source series, with maximum nonreference residuals1.896/3.128keV. | `data/revision-v2/source-replay/`; frozen Nomura arXiv-v2 Fig5(c) points and comparison | Energy-only subset. No19/2/higher same-spin source states, author run card, wavefunction or EM certification |
| C16 | The tested137Ba modeled decay schemes, under two candidate parent identities and seven existing operators, give E2-only half-life upper bounds no larger than .000281041ns, incompatible with589(20)ns under those conditions. | `data/revision-v2/isomer-check/`; all28 strengths,14 sums,84 open E2 branches; Vogt2017 same decay as C13 | Conditional model failure retained in main Discussion. Not a model-independent experimental bound, not all-IBFM exclusion, not direct falsification of the initial11/2 cubic loop |

The internal assessment supports a bounded EPJA model-study contribution,
subject to the stated scientific limits; this is not an editorial decision.
The primary static discrepancy and calibration alternatives limit an empirical
shape claim. The measured static/first-transition ratio remains unavailable
from the audited inputs: a tentative target assignment does not supply its
parent lifetime or an absolute strength.

The full library contains separate pairing/rotor and angular-distribution
investigations. They provide research context, but do not add independent
support to this manuscript's single claim and are excluded from its main text.

The independent unpaired rigid-charge control in C14 is part of this manuscript
because it tests the same shape-inference question. It does not import the
earlier paired/Nambu study as supporting evidence. C13 and C16 share one
experimental decay lineage; the strength and lifetime are not independent
likelihood terms. The seven operators in C16 are primary, core-only and the
five conditional moment calibrations, distinct from the seven-setting family
used per isotope in the earlier35-case sensitivity analysis.

The Bohr–Mottelson reference denotes the actual World Scientific1998 reissue,
whose PDF p6 gives Singapore, ISBN9810239807 and the original1975 edition.
The new reference is for standard particle–rotor kinematics; no unsupported
historical claim from the Wiki source page is used.
