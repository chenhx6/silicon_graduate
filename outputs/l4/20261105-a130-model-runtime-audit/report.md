---
type: l4-report
title: "A≈130 模型与代码运行时审计回执"
created: 2026-11-05
updated: 2026-11-05
status: complete
visibility: private
publication_status: internal-audit
review_status: unreviewed
tags: [a130, model-runtime, hfodd, bigstick, dirhb, root, geant4]
---

# A≈130 模型与代码运行时审计回执

## Scope

本回执汇总 2026-11-05 对公开模型/代码路线和当前容器运行时的定向只读审计。
它是运行与可复现性记录，不是任何目标核素的实验结果。

## Runtime baseline

- CPU：20 logical / 10 physical cores。
- Memory：约 7.5 GiB effective ceiling；审计时可用约 5.6 GiB。
- Disk：工作文件系统剩余约 1.58 TB。
- Compiler/toolchain：GCC/GFortran、CMake、Ninja 可用。
- MPI：`mpifort`/`mpirun` 不可用。
- Eigen：未安装。
- BLAS/LAPACK development link：当前不可用。
- GPU：本轮未确认。

## Verified commands and results

| Tool | Result | Evidence boundary |
|---|---|---|
| ROOT 6.40.04 | PyROOT `TH1D` create/fill/read smoke test passed | 不等于实验拟合或响应校准 |
| Geant4 11.4.2 | material fixture passed; datasets check passed | 不等于真实阵列 geometry/response |
| HFODD v2.73y | official `la132-a.dat` benchmark compiled and ran; `.rec`/`.rev` produced | 不等于 odd-A/odd-odd TAC-CDFT |
| BIGSTICK | serial build and bundled sd-shell benchmark passed; basis dimension 44,133 | 不等于 A≈130 SN100 high-spin calculation |
| DIRHB | public paper/code route located; compilation not completed | no numerical DIRHB result admitted |
| ArbModel | blocked by missing `Eigen/Dense` | no IBM result admitted |
| KSHELL | blocked by rank mismatch/linking and absent BLAS/LAPACK | no KSHELL result admitted |
| NPTool | executable absent; successor source not acquired in this unit | historical source object only |

## Decision record

The first paper should not depend on a complete TPSM/TAC-CDFT/SN100 calculation.
The highest-value immediate route is the P-ADO table-level profile/coverage paper,
because its single innovation is already represented by a reproducible local analysis
package. `133Ce` remains the higher-value nuclear-structure route but requires event or
matrix provenance, response covariance, producer lineage and a holdout before mode
identifiability claims can be promoted.

## Limitations

HFODD and BIGSTICK source snapshots used for the runtime checks were obtained by a
delegated read-only worker; the durable archive keeps the public BIGSTICK snapshot and
the HFODD official index plus the Mendeley access failure, but not a complete HFODD
source package. The report therefore records the benchmark result and its provenance
boundary without claiming a fully reproducible third-party HFODD source replay from
this directory alone.
