---
type: source
title: "Der Mateosian and Sunyar 1974 - Tables of angular-distribution coefficients for mixed multipolarities"
aliases: [Der Mateosian Sunyar 1974 angular tables]
created: 2026-09-21
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: reference-tables
reading_depth: deep-read
title_original: "Tables of Angular-Distribution Coefficients for Gamma Rays of Mixed Multipolarities Emitted by Aligned Nuclei"
authors: [E. Der Mateosian, A. W. Sunyar]
journal: "Atomic Data and Nuclear Data Tables"
year: 1974
volume: 13
pages: "407-462"
pii: "0092-640X(74)90008-4"
doi: "10.1016/0092-640X(74)90008-4"
canonical_source: "Der Mateosian & Sunyar, ADNDT 13, 407-462 (1974)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of angular-distribution coefficients for gamma rays of mixed.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of angular-distribution coefficients for gamma rays of mixed.pdf"
raw_sha256: "90b23807ddc39006a7c17cc05d8dc030139c39802675823c6560f222486d6eeb"
nuclei: [generic]
reactions: [heavy-ion-alignment]
experiments: [gamma-angular-distribution]
models: [Gaussian-magnetic-substate-alignment, Yamazaki-coefficients]
observables: [A2, A4, angular-distribution, mixing-ratio, alignment-width]
methods: [reference-tables, ADO, angular-distribution-fit]
tags: [angular-distribution, ADO, mixing-ratio, alignment, tables]
---

# Tables of angular-distribution coefficients for mixed multipolarities

## Bibliographic Record

- E. Der Mateosian & A. W. Sunyar, *At. Data Nucl. Data Tables* **13**, 407–462 (1974), PII `0092-640X(74)90008-4`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of angular-distribution coefficients for gamma rays of mixed.pdf`。

## Scope and Reading Depth

- PDF pp.407–462 (56 pages) fully read: introduction, use instructions, alignment/attenuation equations, worked `J_i=6→J_f=5` example, integral-spin and half-integral-spin tables, definitions and sign/convention notes.
- Not covered: the preceding attenuation-coefficient paper's complete tables and later computerized replacements.

## Key Results

- The reference tables extend Yamazaki coefficients to mixed multipolarities and high spins: integral `1≤J≤26`, half-integral `1/2≤J≤51/2`, and mixing-amplitude ratio `δ` from 0.01 to 100 over logarithmic steps (PDF pp.407–412).
- For a partially aligned state with Gaussian magnetic-substate width `σ`, the measured coefficients are `α_k A_k^max`, with `α_k` determined by `σ/J`; the tables list `A_2^max(+)`, `A_2^max(−)`, `A_4^max` and quadrupole-intensity fraction `Q=δ²/(1+δ²)` (PDF pp.408–412, Eqs.1–6).
- The worked `J_i=6→J_f=5` example shows how two measured coefficients can be intersected in the `(σ/J,δ)` plane: for `α_2 A_2=−0.66825` and `α_4 A_4=0.02811`, the common solution is `σ/J=0.4`, `δ=0.5` under the chosen sign/geometry (PDF pp.409–410, Fig.2 and table).
- The authors explicitly warn that the sign of δ inferred from a single angular-distribution measurement can be opposite to the sign deduced from a γ–γ angular-correlation cascade under the alternate ordering/convention (PDF p.409).
- The tables are a computational convenience, not a universal alignment prior: measured coefficients, detector/finite-angle corrections and a compatible attenuation table must be matched before solving for δ (PDF pp.409–410).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DMS74-1 | The tables provide mixed-multipole `A_2/A_4` coefficients for integer and half-integer high spins. | reference-result | direct | PDF pp.407–412, tables pp.412–462 | false |
| DMS74-2 | Joint consistency of `A_2` and `A_4` can constrain both alignment width and δ, but the solution is geometry/convention dependent. | method-result | direct | PDF pp.409–410, Fig.2 | true |
| DMS74-3 | Angular-distribution and γ–γ-correlation δ signs may be opposite under the paper's stated cascade/convention mapping. | convention-boundary | direct | PDF p.409 | true |
| DMS74-4 | The tables do not supply a universal `σ/J` prior or replace detector/attenuation calibration. | limitation | direct | PDF pp.408–410 | false |
| DMS74-5 | Ji6→Jf5例题列delta magnitude=.5、sigma/J=.4，正文明确使用negative sign列，A2max=−1.09423、A4max=.12468，attenuated为−.66825/.02811。因此不应把例题的.5未标记地当正signed delta。本任务在该局部native convention复现，非新实验。 | signed-example-and-replay | direct-and-derived | printed409/PDF3 worked paragraph；printed410/PDF4 table/Fig2 | true |
| DMS74-6 | 表头A2MAX(+)/A2MAX(−)分开，A4MAX在明确D/Q例题中为even-delta项，Q=delta²/(1+delta²)是该组分强度分数。不能把Q当polarimeter sensitivity或几何因子；D/Q的A4无linear项源于L1+L2<4，不能自动外推E2/M3。 | table-symbol-and-multipole-boundary | direct-and-derived | printed408 Eq5；printed409 Fig1/example；printed411 table explanation | true |
| DMS74-7 | 原例分别让alpha2 A2max、alpha4 A4max等于两项已知数，只在本例交点配成同一sigma/J；作者也说明真实误差会把曲线变成bands。这个假设例题不证明任意spin/feeding/geometry下全局唯一。 | inverse-consistency-boundary | direct-and-self-audit | printed409 Eq7；printed410 Fig2/table及说明 | true |

## Summary

Der Mateosian and Sunyar turn the Rose–Brink/Yamazaki formalism into practical high-spin coefficient tables. Their worked example demonstrates the correct use: fit alignment and mixing together by requiring both angular coefficients to agree, while retaining the sign conversion and attenuation model as part of the evidence identity.

## Competing Interpretations and Limitations

- `A_2/A_4` alone can have multiple `(σ/J,δ)` intersections once experimental errors, feeding and finite-angle attenuation are included.
- The Gaussian magnetic-substate assumption is a model for alignment; non-Gaussian populations or side feeding can shift the extracted δ.
- The sign warning is not a physical contradiction with Rose–Brink; it flags the need for operator/state-order convention mapping between single-transition angular distributions and γγ cascades.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DMS74-AR-1 | Table chain | `δ` and pure-multipole coefficients → attenuation `α_2/α_4` from `σ/J` → measured `A_2/A_4`. | PDF Eqs.1–7, pp.408–410 | self-checking |
| DMS74-AR-2 | Identifiability | Two coefficient constraints intersect the alignment/mixing parameter plane; uncertainty bands can produce multiple solutions. | PDF Fig.2 and worked table | self-checking |
| DMS74-AR-3 | Transfer condition | Use only with the same spin sequence, convention, gate/geometry and compatible attenuation calculation. | PDF pp.409–412 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]], [[angular-momentum-alignment]] and ADO calibration practice.
- New reusable rule: store both the theoretical table coefficient and the experimentally attenuated coefficient; never cite a table value as a detector-independent measured `A_2/A_4`.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DMS74-P0-1`: Preserve the angular-distribution versus γγ-correlation sign warning and the Gaussian-alignment/attenuation assumptions before reusing any tabulated δ branch.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]]。

## 2026-10-17原件回核：negative-column例题与两个参数层

本次核56页raw hash，读printed407–411全部说明/例题/限制，视觉核Fig1/2与table explanation，并定向检查表格结构；未重逐行核所有dense tables。原DMS74-1–4/review保持，新5–7 true。Crossref核DOI90008-4/issue5/pages407–462；不与preceding DOI90007-2混成一个work。

[新primary control](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ms74-primary-controls.json)用作者Ji6→5假设例题、sigma/J=.4与明确negative column，得到maxA2=−1.09423454/maxA4=.12467532，alpha=.61070321/.22547021，partialA=−.66825254/.02811057，均在原表末位舍入内。反号控制给A2=.34941788但A4相同，说明相同delta²或fraction不能认证sign。8/12-node quadrature差约2.3e−15；这只是该局部source-defined实现/归一控制，不是普遍KS/RB转换或新采集。

[[der-mateosian-sunyar-1974-attenuation-coefficients]] DA74-5–7提供另层alpha与pure reference。[[se21-alignment-calibration-consistency]]保存当前实际校准行的应用条件；本表本身不提供SE21的detector response、efficiency、gatedevents或covariance，不能代替这些输入。
