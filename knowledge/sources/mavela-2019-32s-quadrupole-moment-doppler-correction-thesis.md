---
type: source
title: "Lihleli Mavela 2019 MSc thesis：32S 第一 2+ 态谱学四极矩"
aliases: [Mavela 32S quadrupole thesis, 32S spectroscopic quadrupole moment, Doppler correction thesis]
created: 2026-09-11
updated: 2026-09-11
status: ai-draft
review_status: unreviewed
source_type: thesis-experiment-and-method
reading_depth: deep-read
title_original: "Determination of the Spectroscopic Quadrupole moment of the first 2+ excited state in 32S"
authors: [Lihleli Mavela]
advisor: [J. N. Orce]
journal: "University of the Western Cape MSc thesis"
year: 2019
pages: 94
doi:
arxiv:
language: en
canonical_source: "Lihleli Mavela, Determination of the Spectroscopic Quadrupole moment of the first 2+ excited state in 32S, University of the Western Cape, 2019."
zotero_item_key:
citation_key:
zotero_uri:
library_file: "raw/papers/degree dissertation/硕士论文_多普勒修正.pdf"
raw_file: "raw/papers/degree dissertation/硕士论文_多普勒修正.pdf"
raw_sha256: "4c656a983a0502eaef7c551dfaf6e13539ce472f8e76aea6299ad09cfc112ccf"
nuclei: [32s, 194pt]
reactions: ["194Pt(32S,32S*)194Pt*"]
experiments: []
models: [gosia, semi-classical-coulomb-excitation]
observables: [spectroscopic-quadrupole-moment, diagonal-e2-matrix-element, gamma-yields]
methods: [safe-coulomb-excitation, gamma-particle-coincidence, doppler-correction, gosia]
tags: [degree-dissertation, 32s, coulomb-excitation, quadrupole-moment, gosia, doppler-correction]
---

# Mavela 2019：`32S` 第一 `2+` 态谱学四极矩

## Bibliographic Record

Lihleli Mavela，*Determination of the Spectroscopic Quadrupole moment of the first 2+ excited state in 32S*，University of the Western Cape MSc thesis，2019，PDF 94 页。原始文件 SHA-256 为 `4c656a983a0502eaef7c551dfaf6e13539ce472f8e76aea6299ad09cfc112ccf`。

## Scope and Reading Depth

- Completed `reading_depth`: `deep-read`。
- Covered scope: title/declaration/abstract and contents (PDF pp.i–v); Coulomb-excitation and quadrupole-moment theory (pp.1–23); AFRODITE/S3 setup, safe-energy condition and Doppler correction (pp.24–35); calibration, particle–γ coincidence and GOSIA analysis (pp.36–51); discussion and conclusion (pp.52–54); GOSIA input appendix (pp.68–94). Abstract, GOSIA-result and conclusion pages were visually checked.
- Not covered: raw yields, original GOSIA executable/input provenance beyond the appendix, all cited experiments and a full independent re-fit.
- Coverage caveats: the abstract was visually rechecked at physical PDF p.3 / printed p.i and prints `Q_S(2_1+) = -0.10 ± 0.7 eb`; the GOSIA result pages at physical PDF pp.59–60 / printed pp.50–51 and the conclusion at physical PDF p.63 / printed p.54 agree on `-0.099 ± 0.068 eb`. L3 localization is complete, but the intended abstract uncertainty remains unresolved.

## Paper Question and Scientific Motivation

The thesis determines the spectroscopic quadrupole moment of the first excited `2+` state in `32S` through the Coulomb-excitation reorientation effect, testing the shape evolution near the end of the sd shell and the tension between a prolate spectroscopic moment and some mean-field expectations (abstract; PDF pp.1–23).

## Method and Design Logic

The experiment used `120.3 MeV` `32S` beams on a `1 mg/cm²` `194Pt` target at iThemba LABS. The safe condition kept the minimum nuclear-surface separation above `6.5 fm`; an upstream double-sided CD-type S3 silicon detector measured scattered particles and AFRODITE clovers measured γ rays emitted at about `0.09c`. GOSIA compared angular-dependent integrated γ yields with Coulomb-excitation calculations, using the diagonal `⟨2_1+‖E2‖2_1+⟩` matrix element as a fit parameter (PDF pp.24–35, 48–54).

## Key Evidence and Reasoning Chain

1. Safe-energy geometry and Rutherford scattering → suppress nuclear-interaction contamination (PDF pp.24–25, 52–54).
2. S3 particle–γ coincidence and Doppler correction → obtain angle-dependent `2_1+→0_1+` yields (PDF pp.31–47).
3. GOSIA reorientation fit → extract diagonal E2 matrix element and convert it to `Q_S` (printed pp.50–51; physical PDF pp.59–60).
4. Main-text conclusion → adopts `⟨2_1+‖E2‖2_1+⟩=-0.131±0.090 eb` and `Q_S=-0.099±0.068 eb`; the abstract's `±0.7 eb` is preserved as a source conflict, not silently corrected (abstract physical PDF p.3 / printed p.i; conclusion physical PDF p.63 / printed p.54).

## Summary

The thesis reports safe Coulomb excitation of `32S` at 120.3 MeV on `194Pt`, with `2_1+` at about 2230.6 keV. The detailed GOSIA/conclusion value is `Q_S(2_1+)=-0.099±0.068 eb`, corresponding to a prolate spectroscopic sign under the thesis convention. The abstract prints `-0.10±0.7 eb`, which is incompatible in uncertainty scale with the main text; this batch resolves the locator-level conflict but does not infer the intended abstract uncertainty.

## Experimental or Theoretical Setup

- Beam/target: `120.3 MeV 32S` on `1 mg/cm² 194Pt`; safe separation `>6.5 fm`.
- Detectors: AFRODITE HPGe clovers plus a 24-ring/32-sector double-sided S3 silicon detector.
- Analysis: particle–γ coincidence, Doppler correction, angular yields and GOSIA reorientation fits.
- Model: semi-classical Coulomb excitation and GOSIA; numerical matrix elements are analysis/model outputs constrained by measured yields.

## Key Results

| issue_id | priority | source_and_locator | core_claim | claim_kind | evidence_level | locator | conflict_or_gap | competing_explanations | l3_l4_route | research_status | stage_conclusion | knowledge_increment | remaining_uncertainty | next_autonomous_route | needs_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DD-20260910-32S-01 | P0 | Abstract pp.i–ii、PDF pp.24–35、52–54 | `194Pt(32S,32S*)194Pt*` at 120.3 MeV with AFRODITE+S3 is a safe Coulomb-excitation reorientation experiment for `32S 2_1+`. | experimental-fact | direct | Abstract pp.i–ii；PDF pp.24–35、52–54 | Raw angular yields and full coincidence selection are not available in the thesis bundle. | Background, stopping and angular acceptance corrections can affect the reorientation fit. | L3：核对 safe-energy criterion、detector geometry and yield definition；L4 not started. | completed | Experimental design and locator are established; no claim of independent re-fit. | 新知识 | Raw spectra and covariance are missing. | Recover yield tables and reproduce geometry/normalization from the appendix. | true |
| DD-20260910-32S-02 | P0 | Abstract physical PDF p.3 / printed p.i；GOSIA result physical PDF pp.59–60 / printed pp.50–51；conclusion physical PDF p.63 / printed p.54；GOSIA appendix pp.68–94 | Abstract reports `Q_S=-0.10±0.7 eb`; detailed GOSIA text and conclusion give `⟨2_1+‖E2‖2_1+⟩=-0.131±0.090 eb` and `Q_S=-0.099±0.068 eb`. | experimental-fact | direct | Abstract physical PDF p.3 / printed p.i；physical PDF pp.59–60 / printed pp.50–51；physical PDF p.63 / printed p.54；GOSIA appendix pp.68–94 | Abstract-vs-main uncertainty differs by an order of magnitude; visual page checks rule out OCR transcription as the source of the discrepancy. | Most likely explanations are a source typographical or decimal-place error in the abstract, but no correction is assumed without an author/version check. | L3：completed locator-level conflict localization using abstract, GOSIA result and conclusion page images; L4 remains stopped unless raw yields and full GOSIA provenance become available. | completed | 详细 GOSIA 正文和结论内部一致，阶段采用 `Q_S=-0.099±0.068 eb` as the thesis's detailed result; the abstract `±0.7 eb` remains an unresolved source conflict and `needs_review`. | 纠正知识 | Exact intended abstract uncertainty and any erratum/version history remain unresolved. | Locate author repository/version, institutional metadata or later publication and cross-check whether the abstract uncertainty was corrected. | true |
| DD-20260910-32S-03 | P1 | PDF pp.12–23、48–54 | Reorientation-effect sensitivity to the diagonal E2 matrix element supports a prolate-sign interpretation under the thesis convention. | author-interpretation | indirect | PDF pp.12–23、48–54 | Spectroscopic sign is not a direct image of intrinsic shape and depends on convention/model mapping. | Shell-model, collective and pairing descriptions can differ even for the same `Q_S` sign. | L3：compare `Q_S` convention with independent `32S` measurements; L4 not started. | completed | Treat `Q_S` sign as a measured spectroscopic observable with model-dependent shape interpretation. | 总结知识 | Cross-source convention and uncertainty comparison is incomplete. | Build a `32S` quadrupole-moment provenance table with sign conventions. | true |
| DD-20260910-32S-04 | P1 | PDF pp.48–51、68–94 | GOSIA is the analysis route; no manifest, code provenance, parameter sweep or negative check exists in this batch, so no L4 result is claimed. | model-result | direct | PDF pp.48–51、68–94 | Reproducibility is limited by missing raw yields and environment. | Alternative GOSIA normalization or nuisance treatment could change the uncertainty. | L3：audit input/output provenance; L4 remains stopped until reproducible inputs exist. | stopped | Stopped for data/provenance, not for scientific contradiction. | 边界/失败知识 | Cannot independently reproduce the quoted error. | Obtain raw yield tables and GOSIA input/output, then perform sensitivity and negative-control checks. | true |

## Nuclear Structure Information

This is a `32S` electromagnetic-structure measurement; it does not establish a complete level scheme beyond the `2_1+` state used in the reorientation analysis.

## Authors' Interpretation

The thesis interprets the negative spectroscopic quadrupole moment as a prolate intrinsic-frame shape and discusses disagreement with some mean-field/pairing calculations. The shape language remains an interpretation layered on the spectroscopic observable.

## Model Results

GOSIA and semi-classical Coulomb-excitation calculations provide the matrix-element extraction. The diagonal E2 matrix element and `Q_S` are analysis outputs constrained by data, not a model-independent photograph of the intrinsic density.

## Competing Interpretations and Limitations

- Abstract/main-text uncertainty conflict is localized to abstract physical PDF p.3 / printed p.i versus detailed result/conclusion physical PDF pp.59–60 and p.63; it must remain visible until an author version or erratum is checked.
- Safe Coulomb-excitation conditions reduce nuclear interactions but do not remove all calibration, feeding and stopping uncertainties.
- A sign of `Q_S` does not by itself distinguish all possible collective/pairing mechanisms.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-32S-1 | Observable reconstruction | Reorientation yields constrain a diagonal E2 matrix element, which is then converted to `Q_S`. | DD-20260910-32S-01/02；PDF pp.48–54 | unreviewed |
| AR-32S-2 | Conflict localization | Visual checks localize the abstract `±0.7 eb` versus detailed-result/conclusion `±0.068 eb` discrepancy; the adopted working value follows the detailed GOSIA/conclusion text, while the abstract intent remains unresolved. | DD-20260910-32S-02 | unreviewed |
| AR-32S-3 | Shape boundary | Prolate wording is a model/convention interpretation layered on the spectroscopic sign. | DD-20260910-32S-03 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki has Coulomb-excitation and quadrupole-moment method context but lacked this thesis's raw locator and explicit abstract/main conflict.
- Effect of this source: `extends` safe Coulomb-excitation evidence and `corrects` overconfident single-value summaries by preserving the uncertainty conflict.
- Persistence decision: source-only; no duplicate `32S` experiment page is created in this batch.
- Review state: `unreviewed`; all claims retain `needs_review: true`.

## Related Knowledge and Project Relations

| relation_type | target | specific_relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | Event-by-event/geometry corrections are part of the particle–γ yield chain. |
| methodological-bridge | [[transition-quadrupole-moment]] | Connects measured electromagnetic matrix elements to collective-shape interpretation. |
| related-source | [[hayes-2005-k-conservation-178hf]] | Both use Coulomb-excitation yield/model inference, but are independent experiments. |

## Human Review Triage

### P0

- `DD-20260910-32S-01/02`：核对 safe condition、GOSIA matrix element、abstract/main uncertainty conflict localization and adopted working value.

### P1

- `DD-20260910-32S-03/04`：核对 sign convention, model boundary and reproducibility stop reason.

## Extracted Pages

- PDF pp.i–v：title, abstract and contents.
- PDF pp.24–35：safe Coulomb excitation and detector design.
- PDF pp.48–54、68–94：GOSIA result, conclusion and input appendix.

## Non-source Notes and Follow-up

摘要、方法、GOSIA 结果和结论页已实际读取，关键数值已用视觉页面核对；`DD-20260910-32S-02` 的 L3 冲突定位已完成，但摘要意图仍未由外部版本闭合。未修改 raw、受保护 BibTeX、GOSIA 输入文件或相关 source 页审核状态。
