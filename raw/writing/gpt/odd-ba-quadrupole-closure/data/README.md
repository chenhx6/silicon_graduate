# Reproducible data and calculations

This directory contains public evaluated inputs, declared model parameters,
calculated results and the code required to regenerate the article's numbers.
It contains no private iThemba data and no publisher full-text files.

- `chain-contract.json`: fixed isotope, core, boson number and Hamiltonian inputs.
- `core-E2-calibration.json`: selected evaluated core strengths, original record
  locators, alternatives and uncertainty dependencies.
- `static-moment-constraints.json`: separately identified experimental/evaluated
  static moments and the source's model predictions.
- `results/calibrated-chain.json`: complete primary and core-only results.
- `results/operator-sensitivity.json`: all 35 operator/calibration settings.
- `results/coupling-controls.json`: common-coupling and term-removal controls.
- `results/quadrupole-path.json`: three new quadrupole-only interior points,
  two reused endpoints and bidirectional state tracking.
- `results/static-moments.json`: independent stretched-state contractions.
- `results/moment-matched.json`: conditional matches to the adopted 135Ba
  static moment and its quoted-margin endpoints along the fixed-operator path.
- `results/calibrated-operator-predictions.json`: all five distinct central
  calibration alternatives from the 136Ba and 137Ba moments, with 135Ba
  unused in those calibration equations.
- `vogt2017-transition-constraints.json`: the later primary experimental
  assignment and the distinction between 19/2 and 15/2 parent lifetimes.
- `code/`: frozen numerical modules, producers and portable execution adapters.

With Python 3, NumPy and SciPy installed, run from the article directory:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  python3 -B data/code/study.py --output /path/to/new-primary-run

python3 -B data/code/reproduce_controls.py operator \
  --output /path/to/new-operator-run
python3 -B data/code/reproduce_controls.py coupling \
  --output /path/to/new-coupling-run
python3 -B data/code/reproduce_controls.py quadrupole-path \
  --output /path/to/new-quadrupole-path-run
python3 -B data/code/reproduce_controls.py moment-match \
  --output /path/to/new-moment-match-run
python3 -B data/code/reproduce_calibrated_operator.py \
  --output /path/to/new-calibrated-operator-run
```

Each output directory must be new. The adapters create an isolated relative-path
layout required by the original frozen protocols and compare scientific output
fields with the supplied results. The original operator producer's direct
OpenBLAS thread check uses Linux `/proc`; the tested runtime is recorded in the
article's verification receipts. The primary solver does not require Linux.
There are no downloads or calls to an original Wiki checkout during replay.

The quadrupole-path producer deliberately reuses the exact frozen endpoint
scalars, recomputes their eigenvectors for tracking, and calculates the three
new interior scalar points. Run the coupling producer separately to regenerate
the endpoint scalar results. `reproduction-prerequisites/` preserves the small
earlier audit/probe artifacts whose hashes occur in the protocols; they are
provenance dependencies and are not extra independent measurements.

The moment-matching replay has an explicit portable protocol adapter:
`moment-match-protocol-original.json` preserves the research protocol, while
`moment-match-protocol.json` verifies the bundled extracted static-constraint
JSON instead of requiring an unbundled original ENSDF text. Noncomputational
historical log/report preservation checks are retained as metadata. Numerical
targets, root rules, parameters and the producer code are unchanged. The adapter
first freezes roots using only signed static moments, then calculates the
complete/restricted diagnostics. Matching a supplied moment is a conditional
calibration exercise, not independent validation or a simultaneous energy fit.

The final command keeps the original calibration producer and numerical
contract unchanged, but adapts its verifier to this numerical bundle.
The original protocol also hashed a mutable Wiki source page whose earlier
bytes are no longer available. The adapter verifies the frozen numerical
contract, original producer and all four runtime modules, while explicitly
recording historical evidence-file hashes as not reverified here. It also
relabels the generated verification metadata before writing, so the new run
does not claim verification of absent source files. No numerical equation,
parameter, target, branch selection or native thread check is changed.
The original strict-replay limitation is retained in
`../analysis/calibrated-operator-replay-boundary.md`.

All model quantities retain their declared units and state labels. Unknown
arccos angles are `null`, not zero. Parameter interventions and operator
alternatives are not posterior samples. The 128Ba quoted strength margin
contains the linearized half-life contribution only; missing ICC uncertainty
and cross-isotope covariance must not be silently replaced by zero.

The source articles' original code, complete input cards and electromagnetic
figures have not been reproduced. These files reproduce this explicitly
declared model family.
