# Fixed-shape unpaired particle–rotor control

This self-contained computational supplement preserves the frozen five-point
rigid-core control. It demonstrates that the restricted \(J+2\) proxy can change
at exactly fixed intrinsic charge geometry. It does not establish unchanged
geometry in the separate IBFM calculation or describe a fitted Ba nucleus.

## Figure input and frozen results

**The canonical figure input is [summary.csv](summary.csv) in this package
root.** Its filename and bytes are unchanged from the original calculation.

- SHA-256: `6ec8ce0c3e9f29d065c2ba8282f2d5727b967acfeedf81dd893439a2fcacad34`
- Size: 5295 bytes.
- Twenty rows: \(C=0,1,2,4,8\) MeV, each with `proxy_n=1,5,10,all`.
- Five out-of-domain outcomes retain their raw arguments and empty angle cells.
- `frozen/summary.csv` is an identical archival copy, not independent evidence.

[frozen/results.json](frozen/results.json) contains the full compact diagnostics;
[frozen/cubic-spin-sectors.csv](frozen/cubic-spin-sectors.csv) contains the
nineteen allowed ordered spin-pair sectors at each coupling.
The original [proof](frozen/proof.md), [report](frozen/report.md), protocol,
checks, execution log, and closeout records are preserved verbatim.
Historical Wiki links inside those documents are provenance references, not
runtime dependencies.

## Original producer and new adapter

[frozen/run_control.py](frozen/run_control.py) is the **unchanged original
scientific producer**. Its bytes, the protocol, and all three necessary local
modules in `dependencies/` are copied exactly. Although two module filenames
contain `paired`, the producer uses their pure spin, D2, CG, and product-RME
helpers. It does not call the paired solver or a Nambu projection.

[reproduce.py](reproduce.py) is a **new packaging adapter**. It contains no
Hamiltonian, electromagnetic, invariant, or proxy calculation. It:

1. Checks every listed package file against [inventory.json](inventory.json).
2. Copies the original protocol, original producer, and three dependencies
   into a new virtual repository root with their original relative paths.
3. Executes that unchanged producer exactly once, with isolated Python
   (`-I -B`), a new working directory, and one-thread BLAS environment settings.
4. Compares the five complete-moment results, all twenty proxy outcomes, both
   CSV tables, and the key validation diagnostics against the packaged references.
5. Writes a receipt, a twenty-row comparison CSV, and the replayed results to
   the specified output directory. Existing files are not overwritten.

The relative layout is needed because the original producer locates its
modules and checks input hashes relative to its own path. The adapter preserves
that code instead of editing its path handling. No Wiki checkout, Wiki `raw/`
directory, external scientific dataset, network access, or credentials are
needed at runtime.

## Running the complete control

Prerequisites are Python 3 and installed NumPy/SciPy. The validated environment
was Python 3.12.3, NumPy 2.5.4, and SciPy 1.18.1; [requirements.txt](requirements.txt)
records those numerical-library versions. No dependency installation or
configuration change is performed by the adapter.

From any directory, after copying this package:

```bash
python3 /path/to/rigid-control/reproduce.py \
  --output-dir /path/to/new-rigid-replay \
  --work-dir /path/to/new-rigid-work
```

Both named directories must be new and outside the package. The optional
`--work-dir` defaults to a newly created system temporary directory. The work
directory is retained for inspection; the adapter does not delete it.
For the manuscript packaging run, both output and work paths were explicitly
assigned within the authorized workspace.

This executes the full original five-point calculation, including its
independent geometric, Euler-integral, D2, spectator, phase, and truncation
controls. It does not add a grid or tune parameters.

The floating comparison rule is
`abs(replayed-reference) <= 1e-10 + 1e-10*abs(reference)`.
Integer counts, labels, boolean flags, and null/defined-angle states must agree
exactly. UTC timestamps, execution times, and platform-specific BLAS library
names are excluded from numerical identity comparison. Actual replay timing
and available runtime BLAS thread counts are recorded separately.

## Frozen model and interpretation boundaries

The initial state is the lowest \(I=11/2\) state, with \(j=11/2\),
\(\gamma=20^\circ\), core-only intrinsic charge amplitude \(\mathcal Q=1\),
and fixed unsorted inertias

\[
\mathcal J_k=\frac43(30)\sin^2(\gamma-2\pi k/3)
=(38.793852416,16.527036447,4.679111138)\ \hbar^2/{\rm MeV}.
\]

The Hamiltonian is explicitly unpaired:

\[
H=\sum_k\frac{(I_{k,\mathrm{right}}-j_k)^2}{2\mathcal J_k}+C Q_j,
\quad I_{\mathrm{right}}=(J_x,-J_y,J_z),
\]
\[
Q_j=
\frac{\cos\gamma[3j_z^2-j(j+1)1]
+\sqrt3\sin\gamma(j_x^2-j_y^2)}{4j(j+1)} .
\]

Here \(C\) is in MeV in this precise normalization; it is not an IBFM coupling
or an implicitly normalized spherical-harmonic field coefficient.
The charge operator remains fixed while \(C\) changes.

All physical D2 states for \(I=1/2,\ldots,15/2\) are retained. The resulting
216 multiplets/2448 magnetic states contain every required rank-2 channel for
the initial \(11/2\) quadratic and cubic moments. This is not a globally
complete infinite rotor. Complete moments are geometrically \(q_2=1\) and
\(q_3=\cos60^\circ=0.5\); the all-\(J+2\) proxy changes from 0.322617 to
1.026250, with an undefined real angle at the last point. No material
out-of-domain argument is clipped.

## Provenance and validation receipt

[inventory.json](inventory.json) records package-relative paths, source paths,
roles, byte counts, SHA-256 digests, and actual copy/generation times. Source
repository paths are historical provenance only; runtime inputs come from this
package. The root figure CSV has its own entry pointing to the same frozen
source as the archival duplicate.

The one independently executed package replay is recorded in
[validation/replay-receipt.json](validation/replay-receipt.json), with
[validation/comparison-proxies.csv](validation/comparison-proxies.csv) and
[validation/execution.log](validation/execution.log). The exact inventory
snapshot checked by that execution is preserved as
[validation/inventory-at-replay.json](validation/inventory-at-replay.json).
The final package inventory additionally registers those later validation
records; this distinguishes the execution snapshot from the completed package.

The original producer and every copied dependency remain byte-identical.
The adapter, this README, requirements record, inventory, and replay records
are new packaging/validation artifacts, identified separately from the
original scientific production.
