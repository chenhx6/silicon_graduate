**135/137Ba source-energy comparison package**

This sidecar preserves the twelve frozen Fig. 5(c) source points, the original comparison contract/results, and both original producers. It contains no paper full text, original figure, PDF crop, source tarball or source TeX. Source paths and hashes remain recorded in `source-identities.json` and the unchanged frozen files.

The source is the archived arXiv:1704.07101v2 version of Nomura et al., PRC 96, 014304 (2017). The source PDF's physical p.7, Fig. 5(c), and original TeX804–809/851–856 establish the plotted theory panel and energy reference. The `ba.level.pdf` member's hash and vector-path coordinates are retained without distributing the figure.

The original `source-freeze.json` is copied byte-for-byte. Its historical `kernel_comparison_has_not_run` flag describes the moment of that freeze, before the original comparison. It is not rewritten to describe this later package replay.

**Route A: reproduce the model comparison from package files**

This route reads the frozen CSV/JSON. It does not extract the source figure again, access the Wiki's `raw/`, or require PyMuPDF.

Retain this layout, either in the complete existing data package or in a minimal copy:

```text
data/
  chain-contract.json
  code/
    LICENSE
    single_j_ibfm.py
    paired_single_j_em.py
    paired_single_j_rotor.py
  revision-v2/source-replay/
    source-points-frozen.json
    source-points-frozen.csv
    source-freeze.json
    comparison-contract.json
    source-identities.json
    package-index.json
    replay_model.py
    REPLAY.md
    producers/
      extract_source.py
      compare_fixed_chain.py
    expected/
      comparison.json
      comparison.csv
      run-original.json
```

The verified numerical environment is Python 3.12.3, NumPy 2.5.4 and SciPy 1.18.1. The original producer sets native thread environment variables before numerical imports and checks the loaded OpenBLAS libraries through Linux `/proc/self/maps`. A different platform/BLAS requires an explicitly recorded thread-verification adapter. No original source-code implementation by Nomura/PBOS is included or claimed reproduced.

From any working directory, supplying your copied data root and a fresh result directory:

```bash
python3 -B /path/to/data/revision-v2/source-replay/replay_model.py \
  --output /path/to/new-source-replay-results
```

The adapter loads the unchanged `producers/compare_fixed_chain.py` and the three existing `data/code/` modules. It changes only input/output locations, dependency verification, and verification-scope metadata. It keeps the original Hamiltonians, \(N_B=5/4\), signed \(Q_{jj}\), state choice, energy zero, extraction tolerance and plot-grid comparisons unchanged. Every included file is hash-checked against `package-index.json`; the original producer, source JSON and scientific contract also have fixed expected hashes.

Historical source hashes remain recorded, but Route A does **not** mark absent paper/archive/TeX bytes as verified. Its new `run.json` replaces the original broad `all_locked_inputs_unchanged` claim with a statement limited to packaged numerical inputs/modules, and explicitly records that source originals were not reverified. The untouched `expected/run-original.json` retains the original run's historical claims.

`verification.json` checks all twelve source points against CSV/JSON, all twelve comparison rows, the two summaries, and the original parameters. Numerical replay tolerances are absolute \(10^{-8}\) and relative \(10^{-10}\); they test reproduction of the saved calculation, not agreement with the plotted source. In contrast, the original \(\pm0.5/\pm1\) keV source-grid windows retain their 0.002-keV extraction allowance.

Expected source differences, excluding each fixed \(11/2^-\) zero:

| Nucleus | Maximum absolute difference / keV | RMS difference / keV | Within one-keV grid window |
|---|---:|---:|---:|
| 135Ba | 1.895698513231 | 1.238344020928 | 2/5 |
| 137Ba | 3.128164915321 | 1.991746777146 | 3/5 |

The twelve saved source energies are 918,448,0,404,691,1180 keV for 135Ba and 1122,414,0,607,968,1880 keV for 137Ba, in spin order \(7/2,9/2,11/2,13/2,15/2,17/2\). The comparison uses \(E(J^-_{\rm lowest})-E(11/2^-_{\rm lowest})\). Figure legends do not print same-spin ordinals; the fixed lowest-state convention is preserved.

For an isolated audit, the optional argument `--forbid-external-root /path/to/wiki` rejects file opens under that root outside the selected data package and fresh output. It is an I/O check, not a parameter or model change. The packaging task executed Route A once using a minimal copied data tree with no raw originals and this guard enabled.

**Route B: repeat source extraction with locally held originals**

This is a separate operation. It requires PyMuPDF (original extraction recorded version 1.28.2), the original local canonical PDF, arXiv source archive, archived TeX, and the historical 129Ba extractor used as a method reference. All four local paths/hashes are listed in `source-identities.json`. The archive supplies `ba.level.pdf`; it is deliberately absent from this package.

The unchanged original extractor assumes the Wiki's relative directory layout and creates output files exclusively. To use it, construct a **fresh local scratch tree**, distinct from this package and the existing frozen sidecar. The following recipe verifies and copies the required local bytes, places the original producer at its expected relative depth, obtains the figure member from the local archive, and executes only source extraction:

```bash
python3 -B - /path/to/data /path/to/local/wiki /path/to/new-local-scratch <<'PY'
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tarfile

data, wiki, scratch = (Path(p).resolve() for p in sys.argv[1:])
sidecar = data / "revision-v2/source-replay"
identity = json.loads((sidecar / "source-identities.json").read_text())
scratch.mkdir(parents=True, exist_ok=False)
for item in identity["originals"]:
    original = wiki / item["path"]
    assert hashlib.sha256(original.read_bytes()).hexdigest() == item["sha256"]
    target = scratch / item["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(original, target)

local = scratch / "outputs/l4/20261106-a130-next-evidence/source-chain-replay"
(local / "source-assets").mkdir(parents=True)
extractor = sidecar / "producers/extract_source.py"
freeze = json.loads((sidecar / "source-freeze.json").read_text())
assert hashlib.sha256(extractor.read_bytes()).hexdigest() == freeze["extractor"]["sha256"]
shutil.copyfile(extractor, local / "extract_source.py")
figure = identity["figure_member"]
with tarfile.open(scratch / figure["local_container_path"]) as archive:
    content = archive.extractfile(figure["name"]).read()
assert hashlib.sha256(content).hexdigest() == figure["sha256"]
(local / "source-assets/ba.level.pdf").write_bytes(content)
subprocess.run([sys.executable, "-B", str(local / "extract_source.py")],
               cwd=scratch, check=True)
PY
```

This creates local source-containing scratch material, not a public package addition. Route B was **not executed during packaging**. It is the documented way to run the supplied original extractor when the required local raw files are available. A fresh extraction records a new timestamp and therefore a new JSON hash even when point values agree. It must not replace the historical source freeze or silently change the comparison contract's expected hash.

**Interpretation boundary**

The few-keV differences remain. Reproduction of these twelve comparisons does not demonstrate exact identity with the authors' executed PBOS cards, unprinted parameter precision, eigenvectors or electromagnetic operator run. The \(A-1\) core assignment is text-supported reconstruction; 135Ba-to-134Ba is explicit in the positive-parity discussion (TeX918–927), while per-nucleus \(N_B\) and a137Ba executed deck are not supplied.

Fig.5(c) has no \(19/2^-\) series or higher same-spin states. The detailed135Ba Fig.9 is positive parity (TeX899–913). Neither route validates an experimental isomer assignment, a19/2 energy, an electromagnetic transition, the whole isotope chain, or a correction to published code. No new electromagnetic fit or Hamiltonian variant is part of this package.
