---
type: source
title: "Bazzacco et al. 1998 - Rotational bands in 133Nd"
aliases: [Bazzacco 1998 133Nd rotational bands, Rotational bands in 133Nd]
created: 2026-09-26
updated: 2026-09-26
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Rotational bands in 133Nd"
authors: [D. Bazzacco, F. Brandolini, G. Falconi, S. Lunardi, N. H. Medina, P. Pavan, C. Rossi Alvarez, G. de Angelis, D. De Acuna, M. De Poli, D. R. Napoli, J. Rico, D. Bucurescu, M. Ionescu-Bujor, C. A. Ur]
journal: Physical Review C
year: 1998
volume: 58
pages: 2002-2021
doi: 10.1103/PhysRevC.58.2002
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.58.2002
citation_key: bazzacco_1998_Rotationalbands
raw_file: "raw/papers/gpt/_incoming/20260926-day1-n73/1998_Bazzacco_rotational-bands-133Nd.pdf"
raw_sha256: 0beaa99e10c9e19f088975237d573738ed694ae543ba1a57d5dd3c87b2bda22b
nuclei: [133nd, 131ce, 129ba]
reactions: ["104Pd(32S,2pn)133Nd", "105Pd(32S,2p2n)133Nd"]
experiments: [gasp-133nd-s32-pd]
models: [particle-plus-triaxial-rotor-model, interacting-boson-fermion-model, cranked-shell-model]
observables: [gamma-gamma-coincidence, dco-ratio, alignment, signature-splitting, bm1-be2-ratio]
methods: [gamma-gamma-coincidence, dco-ratio, lifetime-context]
tags: [a130, n73-isotone, high-spin, signature-splitting, configuration-assignment]
---

# Bazzacco 等（1998）：`133Nd` 转动带与 N=73 组态比较

## Bibliographic Record

D. Bazzacco 等，*Physical Review C* **58**, 2002–2021 (1998)，DOI `10.1103/PhysRevC.58.2002`。本轮从 APS 的公开 harvest PDF 取得；文件哈希见 frontmatter。

## Scope and Reading Depth

- 六页期刊 PDF 全文阅读并核对 Fig.3 level schemes、Fig.7 positive-parity alignments/routhians、Fig.10 signature-splitting comparison、Table I DCO rows 和相关讨论。
- 本轮只核验它作为 Ding 2021 refs.48 的 `133Nd` 原始实验来源；它不构成 `131Ce` 的新数据，也不把模型参数移植到目标核。
- 页面保持 `status: ai-draft`、`review_status: unreviewed`；claim-level `needs_review` 保留。

## Key Evidence and Reasoning Chain

两条 `32S` + Pd 反应、GASP γγγ 数据 → DCO/decay-pattern 自旋宇称与 level scheme → 正宇称 bands 6/8/9 和负宇称 bands → alignment/routhian、`B(M1)/B(E2)` 与 PTRM/CSM/IBFM 比较。Band 9 被作者/模型识别为主导 `ν[404]7/2` 的正宇称结构；Fig.10 展示另一个负宇称 band 2 的强 signature splitting 和三轴参数敏感性。对 Ding 2021 的 N=73 comparison，最直接可复用的是 `133Nd` `[404]7/2+` 的 band identity/extension 与 alignment context。

## Summary

Bazzacco 等提供了 N=73 `133Nd` 的原始高自旋谱学与 DCO 赋值。作者明确说明 DCO 约定：以 stretched quadrupole gate 时，stretched E2 约为 1、纯 dipole 约为 0.5；混合 M1+E2 的值依赖 `δ`。Band 9 的低能正宇称结构由 `ν[404]7/2` 主导，具有约 `I=1ℏ` 初始 alignment、无明显 signature splitting，并延伸到高自旋；该结果支持 Ding 2021 将 `133Nd` 作为 N=73 `[404]7/2+` contextual comparator，但其 PTRM/CSM 解释仍是 model layer。

## Experimental or Theoretical Setup

| Item | Source-grounded value |
|---|---|
| reactions | `104Pd(32S,2pn)133Nd` at 135 MeV and `105Pd(32S,2p2n)133Nd` at 155 MeV |
| detector | GASP, 31 Ge thin-target or 38 Ge thick-target configurations plus BGO inner ball |
| data | about `2×10^9` and `1.2×10^9` triple coincidences for thin/thick experiments |
| assignments | DCO matrices with detectors at 90° versus 34°/146°; decay patterns and known low-energy anchors |
| models | IBFM-1 for positive parity, PTRM/CSM/TRS for high-spin structures |

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BAZ98-1 | Two independent `32S+Pd` experiments with GASP established a rich `133Nd` level scheme containing nine structures, including positive-parity bands 6, 8 and 9. | experimental-fact | direct | PDF pp.2002-2005, Figs.1-3 | true |
| BAZ98-2 | With a stretched quadrupole gate, the DCO ratio is approximately 1 for stretched quadrupole transitions and 0.5 for pure dipoles; mixed transitions depend on the sign and value of `δ`. | method-fact | direct | PDF p.2003, DCO-method paragraph and Table I | true |
| BAZ98-3 | Spin/parity assignments use DCO analysis and decay patterns; ten linking transitions connect the highly deformed band to normal-deformed states and support its spin/parity assignment. | experimental-criterion | direct | PDF pp.2003-2005, Table I and linking discussion | true |
| BAZ98-4 | Positive-parity band 9 is dominated by the spherical `g7/2` orbital coupled to the core ground-state band in the IBFM description. | model-result | direct | PDF pp.2011-2012, Fig.3(b) discussion | true |
| BAZ98-5 | The ground-state band 9 has an initial alignment of about `1ℏ`, no signature splitting, and is identified with the `[404]7/2` Nilsson configuration; the source compares its alignment behavior with `129Ba` and `131Ce`. | author-interpretation | indirect | PDF pp.2016-2017, Fig.7 and band-9 discussion | true |
| BAZ98-6 | The experimental `B(M1)/B(E2)` ratios and alignment behavior are compared with PTRM/Donau-Frauendorf estimates; `Q0=4.8 eb` is imported from lifetime measurements and is not newly measured here. | model-assisted-inference | direct | PDF pp.2015-2019, Eqs.4-6 and Fig.9 | true |
| BAZ98-7 | The source's signature-splitting and triaxiality discussion is model-sensitive; Fig.10 shows a negative-parity band whose splitting is reproduced with `γ≈−22°`, while other bands are described as axial or γ-soft alternatives. | model-result | direct | PDF pp.2016-2017, Fig.10 and discussion | true |
| BAZ98-8 | The `133Nd` `[404]7/2` and `129Ba/131Ce` comparison is a cross-nucleus contextual relation; it does not provide a new `131Ce` measurement or prove a unique γ shape. | source-independence-boundary | contextual | PDF pp.2016-2019, band-9 comparison and conclusion | true |

## Nuclear Structure Information

- `133Nd` is an N=73 isotone and a direct source for the `133Nd` entry in Ding 2021's Fig.4/5 comparison.
- Band 9 is the relevant positive-parity `[404]7/2` contextual band; its direct handles are level placements, DCO/decay patterns, alignment and branching-derived ratios.
- The source also contains other bands and HD links; those are not silently merged into the `[404]7/2` continuity claim.

## Authors' Interpretation

The authors use DCO, decay patterns, alignment, `B(M1)/B(E2)` and models to assign the bands. The `[404]7/2` and γ/axial interpretations remain source-local, parameter-dependent interpretations.

## Model Results

IBFM-1 reproduces the low-lying positive-parity band pattern qualitatively; PTRM/CSM/TRS compare band energies, alignments, signature splitting and `B(M1)/B(E2)`. The model parameters and imported `Q0` are not direct observables.

## Competing Interpretations and Limitations

- DCO ratios are geometry/gate dependent and mixed transitions require a `δ` convention; they do not by themselves establish a unique configuration.
- Band 8 and band 9 have different model descriptions; the absence of a band in neighboring nuclei is contextual, not a null measurement of the mechanism.
- The `[404]7/2` comparison to `131Ce` and `129Ba` is inherited systematics and cannot replace target-specific electromagnetic data.
- `Q0=4.8 eb` is imported from lifetime measurements; it is not an independent Bazzacco 1998 lifetime result.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| BAZ98-AR-1 | Directness | GASP coincidences, DCO ratios, placements and linking transitions are direct; orbital, triaxiality and IBFM/PTRM labels are interpretation/model layers. | BAZ98-1 to BAZ98-7 | self-checking |
| BAZ98-AR-2 | N=73 crosswalk | Band 9 supplies an original `133Nd` `[404]7/2` contextual anchor for Ding 2021; it does not close `131Ce` evidence. | BAZ98-5, BAZ98-8 | self-checking |
| BAZ98-AR-3 | Independence | The two `133Nd` reaction datasets are direct experiments within one paper; the `129Ba/131Ce` comparison is imported prior work and is not a third Bazzacco experiment. | BAZ98-1, BAZ98-8 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` the N=73 configuration-continuity context and `limits` any attempt to infer a unique γ shape from the comparison.
- The source closes the `133Nd` side of Ding 2021's refs.48 at the source-page level; Byrne 1992 remains the missing `129Ba` full-text leg.
- Review status remains `unreviewed`; no human review was claimed.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[131ce-collective-mode-discrimination]] | Original N=73 `133Nd` contextual comparator for the `[404]7/2` continuity row. |
| supports | [[ding-2021-131ba-133ce-signature-splitting]] | Verifies refs.48 source identity and its DCO/alignment boundary. |
| nucleus | `133Nd` | High-spin bands and DCO-based assignment; no dedicated nucleus page is present in this Wiki snapshot. |

## Human Review Triage

### P0

None identified.

### P1

- `BAZ98-5`, `BAZ98-8`: preserve the difference between the original `133Nd` band-9 evidence and the later Ding contextual comparison.
- `BAZ98-2`: verify DCO gate convention before any paper-level δ reuse.

### P2/P3

- OCR typography and historical detector nomenclature; no scientific harmonization made.

## Extracted Pages

- Nucleus: `133Nd` (a dedicated nucleus page is not yet present in this Wiki snapshot)
- Project: [[131ce-collective-mode-discrimination]]
- Related source: [[ding-2021-131ba-133ce-signature-splitting]]

## Non-source Notes and Follow-up

The third N=73 source, Byrne 1992 `129Ba`, remains closed at the full-text boundary in this run. Do not use Ding's Fig.4/5 values as a substitute for its original tables.
