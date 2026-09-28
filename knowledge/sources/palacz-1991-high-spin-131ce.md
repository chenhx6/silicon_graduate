---
type: source
title: "Palacz et al. 1991 - High spin states in 131Ce"
aliases: [Palacz 1991 131Ce high spin, High spin states in 131Ce]
created: 2026-09-26
updated: 2026-09-26
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "High spin states in 131Ce"
authors: [M. Palacz, Z. Sujkowski, J. Nyberg, J. Bacelar, J. Jongman, W. Urban, W. Hesselink, J. Nasser, A. Plompen, R. Wyss]
journal: "Z. Phys. A - Hadrons and Nuclei"
year: 1991
volume: 338
pages: 467-468
doi: 10.1007/BF01295780
language: en
canonical_source: https://doi.org/10.1007/BF01295780
citation_key: palacz_1991_Highspinstates
raw_file: "raw/papers/gpt/_incoming/20260926-day1-n73/1991_Palacz_high-spin-states-131Ce.pdf"
raw_sha256: e230b4a7874b139ed0f0da70b2520e25076ead4d338311ff6bce66f53d54ef7b
nuclei: [131ce]
reactions: ["117Sn(18O,4n)131Ce"]
experiments: [nordball-131ce-18o]
models: [cranked-shell-model, total-routhian-surface]
observables: [gamma-gamma-coincidence, alignment, routhian, signature-splitting]
methods: [gamma-gamma-coincidence, doppler-correction]
tags: [a130, n73-isotone, high-spin, signature-splitting, configuration-assignment]
---

# Palacz 等（1991）：`131Ce` 高自旋能级与正宇称 `g7/2` 带

## Bibliographic Record

M. Palacz 等，*Z. Phys. A* **338**, 467–468 (1991)，DOI `10.1007/BF01295780`。本轮从 Springer 公共 PDF 端点取得并保存到 `raw/papers/gpt/_incoming/20260926-day1-n73/`；文件哈希见 frontmatter。

## Scope and Reading Depth

- 两页短文全文阅读并视觉核对 Fig.1 能级纲图和 Fig.2 alignment/routhian 图。
- 本轮只核验它作为 Ding 2021 refs.47 的 `131Ce` 原始实验来源；没有把它与后来的 `131Ce` HD 或 Bands 1–7 论文合并。
- 页面保持 `status: ai-draft`、`review_status: unreviewed`；claim-level `needs_review` 全部保留。

## Key Evidence and Reasoning Chain

`117Sn(18O,4n)131Ce`、NORD-BALL 15 个反康 Ge 和约 `10^8` 事件 → γγ coincidence level scheme → 五条正/负宇称带和不完整 linking → alignment/routhian 与 quasiparticle assignment。作者把正宇称低自旋带的 `g7/2` 强耦合结构与 N=73 系统学联系起来，但没有把全部 linking 或模型输出写成直接组态测量。

## Summary

这篇短文提供 `131Ce` N=73 高自旋实验的原始谱学锚点：能级纲图延伸到约 `I=51/2`，正宇称带 II–IV 与负宇称带 I、V 并存；带 II–IV/V 的作者分析采用 `K=7/2`，正宇称最低带被解释为强耦合 `g7/2` neutron band。作者同时报告部分 linking chain 不完整、带 III 的能量和强度存在 bypass/不闭合问题，因此它是 configuration-continuity evidence，而不是闭合的 target-nucleus electromagnetic proof。

## Experimental or Theoretical Setup

| Item | Source-grounded value |
|---|---|
| reaction | `117Sn(18O,4n)131Ce`, 85 MeV `18O` beam |
| detector | NORD-BALL, 15 Compton-suppressed Ge plus 10 BaF₂ multiplicity detectors |
| data | about `10^8` events; Doppler-corrected γγ matrices and gated spectra |
| level coverage | states up to `I=51/2`, `E_x≈8 MeV` |
| analysis | coincidence placements, assumed earlier low-lying spin/parity anchors, alignments and routhians with Harris parameters `J0=13.4 ℏ² MeV⁻¹`, `J1=30.0 ℏ⁴ MeV⁻³` |

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PAL91-1 | The `117Sn(18O,4n)131Ce` experiment used NORD-BALL with 15 Compton-suppressed Ge detectors and populated states up to about `51/2` and `8 MeV`. | experimental-fact | direct | PDF p.467, abstract and experiment paragraph | true |
| PAL91-2 | The coincidence-based level scheme contains five bands: positive-parity bands II–IV and negative-parity bands I and V; some positive/negative linking chains are incomplete. | experimental-fact | direct | PDF pp.467-468, Fig.1 and text | true |
| PAL91-3 | The authors report that a strong energy splitting between signature partners in negative-parity band I is compatible with a triaxial-shape interpretation, while band V has little splitting and a large initial alignment. | author-interpretation | indirect | PDF p.467, discussion beside Fig.2 | true |
| PAL91-4 | For N=73 and `β2≈0.2`, the lowest positive-parity band is described as a strongly coupled `g7/2` neutron band crossed by two 3-qp bands. | author-interpretation | indirect | PDF p.468, text below Fig.2 | true |
| PAL91-5 | Alignments and routhians were extracted with assumed `K=7/2` for bands II–V and `K=3/2` for band I; these assignments are analysis/model handles rather than direct orbital measurements. | model-assisted-inference | direct | PDF p.467, paragraph before Fig.2 | true |
| PAL91-6 | Incomplete linking, bypass cascades whose energies do not add to the stated excitation energies, and unsupported strength in links between bands V and I limit a unique band crosswalk. | method-limitation | direct | PDF p.467, right-column discussion and Fig.1 | true |

## Nuclear Structure Information

- The source is an N=73 `131Ce` high-spin experiment and is therefore a direct source for the `131Ce` entry in Ding 2021's N=73 comparison.
- The positive-parity `g7/2` statement is an author assignment supported by strong coupling, alignment/routhian comparison and systematics; it is not a standalone orbital measurement.
- The level scheme and links are not the same object as the later `131Ce` normal-deformed Bands 1–7 or the independent highly deformed band; no band identity is transferred across those pages.

## Authors' Interpretation

The authors interpret the observed bands through quasiparticle configurations and use signature splitting, alignment and routhians to distinguish prolate/oblate or triaxial tendencies. These statements remain source-local interpretations and depend on assumed low-lying spin/parity anchors and model parameters.

## Model Results

The alignment/routhian plots and Harris reference provide a CSM-style configuration crosswalk. They are model-assisted handles, not direct measurements of `β2`, `γ`, or a unique quasiparticle wave function.

## Competing Interpretations and Limitations

- The short note reuses earlier low-lying spin/parity assignments and does not provide transition-level mixing ratios or lifetimes for the full high-spin scheme.
- Incomplete linking and bypass cascades prevent a closed feeding/decay graph for every band.
- The triaxial/prolate/oblate language is an interpretation of splitting and alignment; it does not replace direct electromagnetic observables.
- The source does not resolve the Byrne 1992 `129Ba` lineage or establish independence from later `131Ce` analyses.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| PAL91-AR-1 | Directness | Reaction, array, coincidence scheme and level placements are direct; orbital and shape labels are author/model layers. | PAL91-1 to PAL91-5 | self-checking |
| PAL91-AR-2 | Crosswalk boundary | The source is sufficient to verify that Ding's `131Ce` N=73 citation points to a real high-spin experiment, but incomplete links limit a full independent band-by-band re-fit. | PAL91-2, PAL91-6 | self-checking |
| PAL91-AR-3 | Independence | This is a separate `117Sn(18O,4n)` `131Ce` experiment from Ding's 2021 `133Ce/131Ba` reactions; it is contextual evidence, not a new Ding dataset. | PAL91-1 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and `limits` the N=73 configuration-continuity row in the A≈130 evidence map.
- The source confirms a direct `131Ce` high-spin experimental anchor, while incomplete links and model-dependent assignments prevent promotion to a unique `νg7/2` or triaxial-shape fact.
- Review status remains `unreviewed`; no `human-reviewed` state was set.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[131ce-collective-mode-discrimination]] | Direct N=73 `131Ce` source behind the `[404]7/2+` contextual comparison. |
| supports | [[ding-2021-131ba-133ce-signature-splitting]] | Verifies the identity of the cited `131Ce` prior experiment without counting it as a Ding 2021 measurement. |
| nucleus | [[131ce]] | High-spin scheme and configuration handles; not a crosswalk to the later HD or Bands 1–7 pages. |

## Human Review Triage

### P0

None identified.

### P1

- `PAL91-2`, `PAL91-6`: incomplete links and bypass cascades should be checked against the full earlier `131Ce` level-scheme papers before paper-level use.
- `PAL91-4`/`PAL91-5`: preserve the author/model boundary for the `g7/2` assignment and do not treat `K=7/2` as a direct measurement.

### P2/P3

- OCR typography in the historical two-page PDF; no scientific correction made.

## Extracted Pages

- Nucleus: [[131ce]]
- Project: [[131ce-collective-mode-discrimination]]
- Related source: [[ding-2021-131ba-133ce-signature-splitting]]

## Non-source Notes and Follow-up

Byrne 1992 (`129Ba`) remains blocked at the full-text evidence boundary. Do not infer its level or alignment values from Ding captions alone.
