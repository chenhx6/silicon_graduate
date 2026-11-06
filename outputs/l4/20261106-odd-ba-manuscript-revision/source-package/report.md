**Source-energy revision package completed; one isolated model replay passed**

The new sidecar is [data/revision-v2/source-replay](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/data/revision-v2/source-replay/REPLAY.md). It contains the twelve frozen135/137Ba source points, original comparison contract, expected JSON/CSV, original run record, unchanged extraction/comparison producers, source identities, an explicit verification adapter and a separate package index. It includes no paper full text or original figure.

The original45 registered data files and their main manifest are protected by [baseline-existing-data.json](baseline-existing-data.json). No existing data file, manuscript, shared README or main manifest is part of this revision. The new sidecar index is `package-index.json`; no `outputs/manifest.json` was created.

**What was executed**

A minimal data tree was assembled under `isolated-package/data/`, containing only the new sidecar, the existing chain contract, the three existing kernel/helper modules and their existing license. It contains no Wiki `raw/`, source figures or source TeX. From that isolated tree, the following comparison was executed exactly once:

```bash
python3 -B data/revision-v2/source-replay/replay_model.py \
  --output /workspace/wiki/outputs/l4/20261106-odd-ba-manuscript-revision/source-package/portable-run \
  --forbid-external-root /workspace/wiki
```

[portable-run/verification.json](portable-run/verification.json) records:

| Check | Result |
|---|---|
| Frozen source points checked | 12 |
| Comparison rows checked | 12 |
| Largest numeric difference from frozen comparison | 0 |
| 135Ba maximum absolute kernel-minus-source difference | 1.8956985132309683 keV |
| 137Ba maximum absolute kernel-minus-source difference | 3.1281649153208946 keV |
| 135Ba descriptive RMS, excluding reference | 1.2383440209278411 keV |
| 137Ba descriptive RMS, excluding reference | 1.9917467771457564 keV |
| Rejected external Wiki file-open attempts | 0 |
| Original source files read by model replay | No |
| New electromagnetic calculations or parameter variants | None |

The source-grid differences were preserved, not minimized or refitted. Both loaded OpenBLAS libraries report one thread in [portable-run/run.json](portable-run/run.json). The numerical producer and runtime modules retain their frozen hashes.

**Verification adapter and provenance**

The adapter invokes the original `compare_fixed_chain.py` without changing its scientific operations. It redirects file locations, verifies the frozen inputs and existing packaged modules, and scopes the new run metadata to the files actually present. It does not repeat the original run's broad assertion that all historical source bytes were reverified.

The original `source-freeze.json` is copied byte-for-byte, including its historical timestamp and pre-comparison flag. The source-point JSON retains SHA-256 `bc4dbed2c29f65ae8f9546cd146005efa6dbb64eb08ef23781ede6f907b91d22`. The frozen scientific comparison contract retains SHA-256 `cc3b8cc2f677635593f739cd450fb1c5fdcdac54dcdbe0a94075391a63b9f940`.

`source-identities.json` records the canonical arXiv-v2 PDF, source archive, TeX, figure member and historical method reference. Local source bytes were hash-checked during packaging; they were not included in the package or read during the isolated model replay. The omitted original chain-parameter wrapper remains identified by its historical hash in the frozen contract/package dependency mapping; its numerical inputs are already fixed in the contract.

**Separate source-extraction route**

The package's `REPLAY.md` gives two concrete routes:

- Model comparison: use the frozen CSV/JSON and existing package kernel. No source PDF, archive, TeX, Wiki modules or PyMuPDF is required.
- Original-source extraction: use the local raw originals and historical method reference at their recorded hashes, plus PyMuPDF, in a fresh scratch layout. This route was documented but not executed during packaging. It produces a new extraction record and must not overwrite the existing freeze.

The raw-source route is necessary to renew the figure reading itself. A package-only comparison checks the saved extraction against the fixed model; it does not independently re-read the paper.

The preserved scientific boundaries are the few-keV differences, text-supported but not executed-run-explicit \(A-1/N_B\) reconstruction, absence of19/2 and higher same-spin source points, and missing author PBOS/wavefunction/EM run identity. This packaging result makes no claim about a published-code correction, experimental state correspondence, whole-chain validation or manuscript readiness.

Final integrity checks are recorded in [package-check.json](package-check.json). All writes for this task are confined to the two assigned directories. No commit was made.
