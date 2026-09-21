---
type: system-overview
graph-excluded: true
created: 2026-07-01
updated: 2026-09-21
---

# Knowledge Base Health Dashboard

## Current Snapshot: 2026-09-21 High-spin full reconciliation

The high-spin corpus has completed source-level reading and is now in full knowledge-base reconciliation. The original 127-row ledger contains 118 valid rows, 9 user-confirmed exclusions, 110 unique hashes and 8 exact duplicate rows. This phase updates affected knowledge nodes and creates four cross-source synthesis pages; it does not treat source-page completion as human review or final paper evidence.

| metric | current value | note |
|---|---:|---|
| source / nucleus / band / experiment pages | 244 / 59 / 63 / 37 | Global Wiki counts after the high-spin ingest and one external `146Ba` source; high-spin rows remain separately tracked in the batch ledger. |
| concept / method / model / observable pages | 48 / 21 / 15 / 20 | Includes high-spin method, octupole, two-photon and drip-line additions. |
| project / synthesis pages | 11 / 11 | Four new high-spin synthesis pages and the source-provenance registry are self-audited and remain unreviewed. |
| high-spin ledger | 127 rows / 118 valid / 9 excluded | `102` source-created, `8` reused audits, `7` duplicate audits, `1` attached-material audit. |
| unique high-spin hashes | 110 | Distinct file content, not independent papers or experiments. |
| source pages unreviewed | 184 | Global lint governance count; no claims were automatically promoted to `human-reviewed`. |
| claim-level `needs_review: true` | 1106 | Existing and new paper-use review queue; locator/kind gaps are tracked separately. |
| automated lint | 0 errors / 79 warnings / 1106 info | After the residual pass: 19 local-BibTeX keys and 55 Crossref-verified DOI keys were restored, graph-orphan sources are routed through the provenance registry, and only three channel-underdetermined reactions remain warnings. |
| QMD | 526 documents indexed | Vector refresh state is recorded separately; QMD remains a retrieval aid, not an evidence gate. |

The current reconciliation is organized around four themes: angular/polarization/mixing-ratio methods; lifetimes/strengths/deformation; chirality/wobbling competition; and octupole/rare electromagnetic decay. External literature may be added when a concrete evidence gap requires it; each external source receives its own identity, hash, locator and independence record.

The whole `knowledge/` directory was audited on 2026-09-21. Structural errors are cleared (`lint errors=0`). A residual pass restored 19 citation keys that uniquely match the read-only local BibTeX exports, then restored 55 more from unique Crossref DOI records without modifying the protected bibliography. An explicit source-provenance registry routes the 59 formerly index-only source pages. The remaining 76 citation-key gaps have no unique usable local/external record (or have an unresolved arXiv-version identity); three reaction strings remain channel-underdetermined (`xn`, `xnyp`, `xnyalpha`) and are not falsely balanced. These are metadata/graph/parser boundaries, not scientific conclusions.

The provenance registry is [[source-provenance-coverage-map]]; it is a navigation and ownership record, not a scientific review. QMD was refreshed and compacted after the pass: 532 Markdown documents are indexed, 2,172 current vectors are present, no vectors are pending, and the previous 873 orphan chunks were removed from the cache.

## Current Snapshot: 2026-09-05 Degree Dissertation Batch

The degree-dissertation batch has completed content ingestion: 15 degree dissertations are represented (Ding 2012 already present; Alwaleedi 2013 re-read; 13 new thesis sources) plus one additional 1974 `103Pd` experiment report. The batch adds A≈130 shape/wobbling, `100Sn` independent decay baselines, fast timing, K-mixing, fission-isomer and low-energy reaction method evidence. All new claims remain source-level `unreviewed` with `needs_review: true`; this is not a paper-level admission or human-review event.

| metric | current value | note |
|---|---:|---|
| source pages | 109 | Includes 14 new source pages plus the existing Ding/Alwaleedi thesis records; the `103Pd` report is explicitly marked as an experiment report, not a dissertation. |
| nucleus / band / experiment pages | 59 / 63 / 37 | Added a lightweight `100Sn` page and touched only directly related `Ru/Ba/Pr/Au` and experiment relation pages. |
| concept / method / model / observable pages | 43 / 19 / 15 / 20 | Added GT-strength, signature-inversion and lifetime anchors; no schema or lint configuration changes. |
| project / synthesis pages | 9 / 7 | No new project/synthesis page; cross-source REFLECT is recorded in the batch report and remains provisional. |
| source pages unreviewed | 49 | New thesis/report sources remain page-level unreviewed; Alwaleedi retains its earlier status. |
| claim-level `needs_review: true` | 691 | Includes the batch claims and pre-existing review queues; no claim was cleared automatically. |
| claim missing locator / kind | 0 / 0 | Current lint result. |
| raw hash coverage | 109/109 | New source hashes match their PDF files; raw PDFs and extracted raw images remain outside Git staging. |
| automated lint | 0 errors / 89 warnings / 691 info | Warnings are existing reaction/element/orphan/citation-key notices plus protected raw changes. |
| commit/push status | content complete; one-time publish pending | Git is intentionally decoupled from content ingest; `script/git20260905.cmd` performs explicit staging and a non-force `HEAD:main` attempt. |

The batch keeps thesis/journal shared-data lineages separate, especially `131Ba`, `108,112Ru`, `135Pr`, `187Au` and `100Sn`. The `100Sn` GSI (Hinke 2010) and RIKEN (Lubos 2016) results are independent candidate lineages, not silently averaged. `178Hf` key pages were checked visually/OCR because the PDF text layer is unreliable. `Pálffy 2006` and Chen 2014 remain source-only or method-oriented relative to the current high-spin focus.

## Current Snapshot: 2026-08-11 Nuclear-chirality 23-paper corpus WIP

The ordered corpus from Petrache 1996 through Bark 2024 is fully ingested in one local rolling `WIP ingest:` commit. Each of the 23 target PDFs has a source page with citation key, raw hash, reading coverage, locator-level claims, analytical reconstruction and Human review triage. The corpus remains unreviewed working knowledge: completing ingest does not promote candidate chirality, MχD, octupole/pseudospin coupling or model geometry to confirmed claims.

| metric | current value | note |
|---|---:|---|
| source pages | 94 | Added 23 ordered corpus source pages; reviews/censuses remain secondary evidence and are not counted as replications. |
| nucleus / band / experiment pages | 56 / 58 / 36 | Selective structure pages only; review tables did not trigger mechanical page generation. |
| concept / method / model / observable pages | 41 / 19 / 15 / 19 | Added RDDS/DDCM and DSAM coverage and updated chirality/MχD/octupole/TPRM boundaries. |
| project / synthesis pages | 9 / 7 | Final 23-paper REFLECT is persisted inside the existing nuclear-chirality project; no duplicate synthesis page. |
| source pages unreviewed | 34 | The 23 corpus sources remain source-level unreviewed unless an earlier source already had an independent review state. |
| claim-level `needs_review: true` | 576 | Includes corpus source/AR/project/REFLECT claims plus pre-existing review queues. |
| claim missing locator / kind | 0 / 0 | Current lint result. |
| raw hash coverage | 94/94 | All source raw hashes match; protected `wiki-inbox.bib` remains user-managed and unstaged. |
| automated lint | 0 errors / 69 warnings / 576 info | Warnings are existing reaction/element/orphan notices plus the protected raw BibTeX dirty signal. |
| corpus review boundary | local WIP; user review pending | Priority review: provenance independence, realistic fingerprint limits, `106Ag` counterexample, `193/194Tl` pairing ambiguity, source-table/formula errors and all source P1 triage. |

The final evidence architecture separates stable experimental band/link identities, partner-resolved absolute strengths, model geometry, counterexamples/nulls and source independence. Wang 2023's charge-inconsistent `82Ge` rows are reconciled to `82Se` only at the related-review level by Bark 2024; Bark's own polarization Eq.(5) is algebraically inconsistent and quarantined. QMD was refreshed after this snapshot so the full 23-paper WIP is locally searchable.

## Current Snapshot: 2026-07-28 Continuous Research-Learning v2 candidate

This snapshot records the locally validated v2 architecture and the completed-provisional `131Ce` L3/L4 pilot. Li 2004 claims LI04-1–4 passed claim-level human visual review; the source page, LI04-5, band mapping and collective-mode conclusions remain unreviewed or provisional as recorded. Remote main/tag publication is not claimed while Git push authentication is blocked.

| metric | current value | note |
|---|---:|---|
| source pages | 74 | Added Alwaleedi 2013 plus Singh 2016, Li 2004 and Petrache 1998 lifetime lineages. |
| nucleus / band pages | 24 / 25 | Added `131Ce`; no speculative per-band page expansion. |
| concept / method / model / observable pages | 40 / 17 / 15 / 19 | Reused existing owners; added no parallel analysis framework. |
| project / synthesis pages | 9 / 7 | Added the `131Ce/133Ce` collective-mode discrimination project. |
| source pages unreviewed | 14 | Li 2004 remains page-level unreviewed despite LI04-1–4 claim review. |
| claim-level `needs_review: true` | 231 | Remaining items are reviewed on use; this count is not a task queue. |
| claim missing locator / kind | 0 / 0 | Current lint result. |
| automated lint | 0 errors / 102 warnings / 231 info | A clean public checkout lacks ignored raw PDFs, so most warnings are expected `RAW_MISSING`; remaining warnings are existing reaction/element/orphan notices. The integration worktree separately reports its protected user BibTeX dirty signal. |
| v2 acceptance | local release candidate | Thesis tests 3/3, lifetime tests 6/6, system tests 10/10 and three Paper Card audits 14/14 pass. |

## Current Snapshot: 2026-07-25 experimental wobbling batch review

This snapshot records completion of a rough page-level human review of 15 experimental/reanalysis wobbling sources after all PDF-title/DOI/BibTeX and duplicate checks passed. The review accepted the current evidence-calibrated wording and explicit limitations without correction; it does not convert page-level review into exhaustive claim-by-claim paper certification.

| metric | current value | note |
|---|---:|---|
| source pages | 70 | Added 15 ordered source notes; 14 are `deep-read`, Guo 2024 is `read` because its key Supplemental Material table is not in the supplied raw PDF. |
| nucleus / band pages | 23 / 25 | Added 13 lightweight nucleus pages and `163Lu` TSD3; updated `163Lu` TSD1/TSD2. |
| concept / method / model / observable pages | 40 / 17 / 15 / 19 | Updated the wobbling concept only; no new method/model/observable page was required. |
| project / synthesis pages | 8 / 7 | Updated low-spin wobbling and chirality projects; added [[experimental-wobbling-evidence-strength-map]]. |
| source pages unreviewed | 10 | The 15 experimental/reanalysis sources are now page-level `human-reviewed`; ten previously deferred theory/review sources remain unreviewed. |
| claim-level `needs_review: true` | 209 | The rough page-level review did not clear 102 source claims mechanically; claim-specific paper use still triggers targeted verification. Synthesis/project and previously deferred claims also remain pending. |
| claim missing locator / kind | 0 / 0 | Current lint result. |
| raw hash coverage | 70/70 | All source pages have matching raw hashes. |
| automated lint | 0 errors / 28 warnings / 209 info | `page_unreviewed=161`, `source_unreviewed=10`; warnings are existing reaction/element/orphan configuration notices plus the protected user BibTeX dirty state. |
| review boundary | page-level review complete; final push authorized | Guo 2024 remains `reading_depth: read` because the Supplemental Material is absent. Exact or paper-facing reuse still returns to the recorded locators and P0/P1 prompts. |

## Current Snapshot: 2026-07-16

This snapshot records the operational closure of the continuous wobbling-source batch. Petrache 2016, Chakraborty 2023 and Mullins 1993 were reviewed at source level; PE16-2 now distinguishes the two ATLAS target assemblies, and the Mullins DOI/pagination are corrected. The ten theory/review sources and the WOB-REFL/WOB-PROJ-REF analytical notes remain unreviewed working knowledge with `needs_review: true`; their review is deferred until actual use rather than retained as an active batch WIP.

| metric | current value | note |
|---|---:|---|
| source pages | 55 | Includes the 13 main papers in this batch; the Chen publisher erratum is linked as a correction, not a separate full source page. |
| concept / method / model / observable pages | 40 / 17 / 15 / 19 | Added only minimal source links for magnetic rotation, antimagnetic rotation, shears, band termination and TAC. |
| project / synthesis pages | 8 / 6 | Updated the existing low-spin wobbling project and synthesis with batch REFLECT notes; no duplicate project was created. |
| source pages unreviewed | 10 | The ten theory/review source pages remain unreviewed under the `review deferred until use` strategy. |
| claim-level `needs_review: true` | 107 | Lint total after clearing only PE16-1..12 and MU93-1..10; theory/review and batch-reflection claims remain pending targeted review. |
| claim missing locator / kind | 0 / 0 | Current lint result. |
| raw hash coverage | 55/55 | All source raw-file hashes match after the Clark hash correction. |
| review boundary | batch operationally closed | Three experimental source pages were reviewed; theory/review and batch-reflection claims remain provisional and require targeted review before consequential use. |

## Current Snapshot: 2026-07-13

This snapshot records the completed two-source nuclear-alignment and rotating-symmetry ingest. Diamond 1966 and Frauendorf 2001 have deep-read source notes with claim-level human review complete; the new pages connect heavy-ion magnetic-substate alignment, Routhian/TAC symmetry classification, magnetic and antimagnetic rotation, shears, band termination and reflection asymmetry. Page-level review remains distinct from claim-level `needs_review`.

| metric | current value | note |
|---|---:|---|
| source pages | 43 | Added Diamond 1966 and Frauendorf 2001. |
| concept / method / model / observable pages | 40 / 17 / 15 / 19 | Added rotating-mean-field, symmetry, magnetic/antimagnetic, shears, termination, reflection-asymmetry and Routhian anchors. |
| project pages | 8 | Added [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] evidence map. |
| source pages unreviewed | 0 | Diamond 1966 and Frauendorf 2001 source notes were moved to `review_status: human-reviewed`. |
| source claim-level `needs_review: true` | 0 | D66-1..11 and F01-1..15 were cleared by user review on 2026-07-13. |
| claim missing locator / kind | 0 / 0 | Lint found no missing locator or claim kind in source tables. |
| raw hash coverage | 43/43 | All source raw-file hashes match. |
| review boundary | source review complete | The Diamond/Frauendorf source claims are reviewed; newly linked theory pages remain independently reviewable at page level. |

## Previous Snapshot: 2026-07-13

This snapshot records the completed joint source-review finalization for Meng 2010, Ayangeakaa 2013 (`133Ce`), and Liu 2016 (`78Br`). The user reviewed all three source pages; the finalization clarified the semiclassical TAC tunneling boundary, the `133Ce` bandhead and `135Nd` systematics, the `78Br` quartet future-observation wording, and the role of `S(I)`. Derived project/concept/nucleus/band pages retain independent page-level review status.

| 项目 | 当前状态 | 说明 |
|---|---:|---|
| source pages | 38 | 新增 Meng 2010、Ayangeakaa 2013、Liu 2016 |
| nucleus / band pages | 10 / 24 | 新增 `78Br` 与 `133Ce`/`78Br` 四个 source-specific MχD pair pages |
| concept / observable / method pages | 31 / 16 / 15 | 新增 chirality dynamics、MχD、triaxial shape coexistence、octupole terminology、`S_chiral(I)`、E1/E2、`delta E` 与 ADO |
| project pages | 7 | 新增 `[[nuclear-chirality-and-multiple-chiral-doublet-bands]]` evidence map |
| reviewed source claims | 39 | `M10-1..11`、`A13-1..13`、`L16-1..15` 均为 `needs_review: false`；无缺失 locator/kind |
| review boundary | source review complete | 三篇 source 已 human-reviewed；project 与派生知识页仍保留独立 page-level review 状态，正式论文使用仍按 claim-specific evidence gate 回原文核验 |

## Previous Snapshot: 2026-07-12

This snapshot reflects the finalized review round for the four gamma-spectroscopy method sources added on 2026-07-12: Rezynkina 2017, Kramer-Flecken 1989, Kibedi 2008, and Rusev 2009. The user review accepted the method/project bundle, corrected the KF89 `sigma/I` low-spin boundary and experimental `R_DCO` formula linkage, and required the Rusev branch-selection note to remain tightly framed as an author-judgment statement rather than a direct observable fact.

| metric | current value | note |
|---|---:|---|
| source pages | 35 | Added four method-oriented source pages in the completed review round. |
| nucleus pages | 9 | No new nucleus page was added in this round. |
| experiment pages | 14 | No new experiment page was added in this round. |
| concept pages | 21 | `[[sigma-over-i]]` was minimally extended with the KF89 low-spin `I < 6` boundary. |
| method pages | 14 | Added `[[internal-conversion-analysis]]`; `[[dco-ratio]]` was minimally extended with the experimental `R_DCO` formula and low-spin boundary. |
| observable pages | 13 | Added `[[internal-conversion-coefficient]]`. |
| model pages | 14 | No new model page was added in this round. |
| project pages | 6 | `[[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]` was re-reviewed and minimally tightened. |
| synthesis pages | 6 | No new synthesis page was added in this round. |
| source pages unreviewed | 0 | The four new method-source pages were moved to `review_status: human-reviewed`. |
| page-level unreviewed | 100 | Current lint governance count after this review-finalization round. |
| source claim-level `needs_review: true` | lint summary currently 0 | Project-note queue is clear; the Rusev branch-selection caveat was kept narrow in source wording rather than promoted to a project-level review queue. |
| project claim-level `needs_review: true` | 0 | `SIO-PROJ-21`--`SIO-PROJ-24` were accepted in this review round. |
| claim missing locator | 0 | Lint found no locator gaps. |
| source missing raw_file / citation_key | 0 / 0 | Lint found no source metadata gaps. |
| raw hash coverage | 35/35 | Lint reports all source pages matched raw hashes after this round. |
| wikilinks | 1545 | Lint count after the method-review finalization round. |

## Current Snapshot: 2026-07-10

This snapshot reflects the finalized sigma-over-I synthesis-planning round after user review. The bounded writing-support synthesis, the sigma-over-I project evidence map, and the related terminology pages used in this round were reviewed on 2026-07-10. The user also confirmed that the current 11-source package does not yet contain direct low-spin-specific `sigma/I` sensitivity evidence strong enough to support a universal low-spin claim.

| metric | current value | note |
|---|---:|---|
| source pages | 31 | No new source page was added in this review-finalization round. |
| nucleus pages | 9 | Added [[152dy]] as a narrow Lauritsen 2025 `152Dy` experiment/observable entry. |
| experiment pages | 14 | Added [[atlas-gretina-152dy-ca48-191mev]]. |
| concept pages | 21 | `[[sigma-over-i]]` and `[[magnetic-substate-population]]` were revised and user-reviewed for terminology boundaries. |
| method pages | 13 | Added spin-parity-assignment, TDPAD, and g-factor measurement method anchors. |
| observable pages | 12 | `[[spin-alignment-attenuation-factor]]` was revised and user-reviewed for EK79 threshold wording and notation boundaries. |
| model pages | 14 | Added [[compound-nucleus-reaction-model]]. |
| project pages | 6 | `[[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]` is now user-reviewed after synthesis planning. |
| synthesis pages | 6 | Added and user-reviewed [[sigma-over-i-assumptions-and-mixing-ratio-extraction]]. |
| source pages unreviewed | 0 | The two new article10-11 source pages were moved to `review_status: human-reviewed`. |
| source claim-level `needs_review: true` | 0 | EK79-1--EK79-9, IO81-1--IO81-9, and follow-up IO81-10 were cleared by user review on 2026-07-09. |
| project claim-level `needs_review: true` | 0 | The current sigma-over-I project/synthesis wording round has no remaining claim-level review queue. |
| claim missing locator | 0 | Lint found no claim locator gaps. |
| source missing raw_file / citation_key | 0 / 0 | Lint found no missing source raw/citation metadata. |
| raw hash coverage | 31/31 | Lint reports all source pages matched raw hashes after this round. |
| wikilinks | 1481 | Lint count after the synthesis-planning and review-finalization round. |

## Previous Snapshot: 2026-07-09

This snapshot reflects the finalized article10-11 supplemental ingest after user review corrections and the additional Ionescu branching-ratio / model-dependent-`delta` follow-up note. Ekstrom 1979, the Ionescu 1981 source package, and the follow-up IO81-10 note were user-reviewed on 2026-07-09.

| metric | current value | note |
|---|---:|---|
| source pages | 31 | Added Ekstrom 1979 and Ionescu 1981 for the sigma-over-I supplemental alignment-limitation round. |
| nucleus pages | 9 | Added [[152dy]] as a narrow Lauritsen 2025 `152Dy` experiment/observable entry. |
| experiment pages | 14 | Added [[atlas-gretina-152dy-ca48-191mev]]. |
| concept pages | 21 | Added [[direct-feeding]]. |
| method pages | 13 | Added spin-parity-assignment, TDPAD, and g-factor measurement method anchors. |
| observable pages | 12 | Added [[spin-alignment-attenuation-factor]] and updated attenuation-coefficient boundary. |
| model pages | 14 | Added [[compound-nucleus-reaction-model]]. |
| project pages | 6 | Updated sigma-over-I evidence map. |
| source pages unreviewed | 0 | The two new article10-11 source pages were moved to `review_status: human-reviewed`. |
| source claim-level `needs_review: true` | 0 | EK79-1--EK79-9, IO81-1--IO81-9, and follow-up IO81-10 were cleared by user review on 2026-07-09. |
| project claim-level `needs_review: true` | 0 | SIO-PROJ-16--SIO-PROJ-19 were cleared by user review on 2026-07-09. |
| claim missing locator | 0 | Lint found no claim locator gaps. |
| source missing raw_file / citation_key | 0 / 0 | Lint found no missing source raw/citation metadata. |
| raw hash coverage | 31/31 | Lint reports all source pages matched raw hashes after this round. |
| wikilinks | 1430 | Lint count after adding the IO81 branching-ratio follow-up note. |

| 指标 | 当前值 | 说明 |
|---|---:|---|
| 正式来源数 | 23 | `knowledge/sources/`；新增 Draper 1970、Zobel 1980 与 Zobel 1983 的 sigma-over-I/P-ADO alignment sources |
| 核素页数 | 8 | `knowledge/nuclei/`；新增 `135Nd` |
| 能带页数 | 20 | `knowledge/bands/`；新增 `135Nd` D1/TiP1/TiP2 |
| 概念页数 | 19 | `knowledge/concepts/`；新增 magnetic-substate population、spin alignment、side feeding 与 sigma-over-I |
| 实验页数 | 13 | `knowledge/experiments/`；新增 JUROGAM II `100Mo(40Ar,5n)135Nd` 数据集 |
| 模型页数 | 13 | `knowledge/models/`；新增 interacting boson-fermion model |
| 观测量页数 | 11 | `knowledge/observables/`；新增 angular-distribution coefficient 与 attenuation coefficient |
| 方法页数 | 8 | `knowledge/methods/`；新增 angular-distribution |
| 综合页数 | 5 | `knowledge/synthesis/`；新增 low-spin wobbling + γ-soft + TiP/IBFM cross-project synthesis |
| 项目页数 | 6 | `knowledge/projects/`；新增 sigma-over-I uncertainty in P-ADO mixing-ratio extraction |
| 人工确认的高置信度结论 | 0 | 必须有确认记录 |
| 页面级人工审阅页 | 36 | 23 个 source 页 + 13 个其他知识页；sigma-over-I project 已完成本轮人工审核 |
| 页面级 unreviewed | 90 | 自动 lint governance 统计 |
| source 页 unreviewed | 0 | 23 个 source 页当前均已完成人工页面级审阅 |
| 页面级 needs-human-review | 0 | 当前无页面级待人工复核页 |
| claim-level `needs_review: true` | 0 | 当前 source 与 project/synthesis claim 审核队列均已清零 |
| project-level synthesis `needs_review: true` | 0 | 当前跨来源 project / synthesis notes 已完成本轮人工审核 |
| claim 缺失 locator | 0 | 自动解析 source `Key Results` 表 |
| claim 缺失 claim kind | 0 | 使用 schema 字段 `claim_kind` |
| source 缺失 raw_file | 0 | 自动统计 source frontmatter |
| source 缺失 citation key | 0 | 自动统计 source frontmatter |
| 开放问题数 | 12 | `knowledge/questions.md`；新增 P-ADO / NST `σ/I` mapping 问题 |
| 断裂链接 | 0 | 1254 个 Wikilink 已检查 |
| Raw 哈希异常 | 0 | 23/23 个来源页与原文件一致 |
| 自动 lint | 0 error / 10 warning / 0 info | warning 含用户 BibTeX/raw 工作树改动、未配置元素与 `1p4n` |

自动 lint 全绿只表示没有达到失败阈值的结构问题，不表示科学内容已经全部完成人工复核。
