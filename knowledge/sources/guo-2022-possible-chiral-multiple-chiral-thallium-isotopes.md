---
type: source
title: "Guo et al. 2022 - Possible existence of chiral and multiple chiral nuclei in thallium isotopes"
aliases: [Guo 2022 Tl chirality, 192-198Tl constrained RMF chirality predictions]
created: 2026-08-11
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Possible Existence of Chiral and Multiple Chiral Nuclei in Thallium Isotopes"
authors: [Rui-Ju Guo, Xiao Lu, Bin Qi, Chen Liu, Shou-Yu Wang]
journal: Chinese Physics C
year: 2022
volume: 46
issue: 7
pages: 074107
doi: 10.1088/1674-1137/ac6248
language: English
canonical_source: https://doi.org/10.1088/1674-1137/ac6248
citation_key: guo_2022_Possibleexistence
raw_file: "raw/papers/2022_Possible existence of chiral and multiple chiral nuclei in thallium isotopes .pdf"
raw_sha256: 9376A208B1E54EF8AA532F78B878A4920954DB26B3896D5DBAE511E5D0331223
nuclei: [192tl, 193tl, 194tl, 195tl, 196tl, 197tl, 198tl, 199tl, 200tl]
reactions: []
experiments: []
models: [covariant-density-functional-theory]
observables: [bm1-be2-ratio]
methods: []
tags: [theory-ingest, project-ingest, a190, nuclear-chirality, multiple-chiral-doublet, thallium-isotopes, constrained-rmf]
---

# Possible Existence of Chiral and Multiple Chiral Nuclei in Thallium Isotopes

## Bibliographic Record

Chinese Physics C 46, 074107 (2022), DOI `10.1088/1674-1137/ac6248`. The protected BibTeX key is `guo_2022_Possibleexistence`.

## Scope and Reading Depth

- Completed reading depth: `deep-read`.
- Covered scope: all ten PDF pages; adiabatic and configuration-fixed constrained triaxial RMF setup; potential-energy curves; Tables 1-2; candidate-minimum selection; odd-odd and odd-mass configuration systematics; imported experimental energy and `B(M1)/B(E2)` comparisons; limitations and null cases.
- Not covered: original experimental papers behind Fig. 4, numerical wavefunctions, convergence files, pairing-inclusive calculations, rotational TAC/PRM spectra, or electromagnetic calculations for the predicted candidates.
- Coverage caveat: this is a theory prediction paper. It finds static constrained minima, not rotational partner bands or left/right angular-momentum geometry.

## Extracted Pages

- PDF pp.1-2: motivation, earlier Tl candidates, constrained RMF formalism, PK1 basis and no-pairing setup.
- PDF pp.3-4: odd-odd/odd-mass potential-energy curves, favorable `15°≤γ≤45°` display window, `199,200Tl` null controls, occupation notation and single-particle examples.
- PDF pp.5-6: complete candidate-minimum Tables 1-2.
- PDF pp.7-9: odd-odd and odd-mass candidate interpretation, secondary experimental systematics, prediction counts, limitations and summary.
- PDF pp.9-10: references.

## Paper Question and Scientific Motivation

The paper asks whether constrained triaxial relativistic mean-field calculations locate multiple low-lying minima in `192-200Tl` with both favorable triaxial deformation and suitable high-`j` particle-hole occupations, and therefore which isotopes/configurations merit experimental searches for chirality and MχD (PDF pp.1-3).

## Method and Design Logic

- Solve adiabatic and configuration-fixed constrained triaxial RMF equations with PK1. Dirac spinors use 12 major harmonic-oscillator shells and meson fields 20 shells (PDF p.2).
- Constrain `β=0-0.5`, while plotting only `β<0.3` because no suitable chiral configurations occur above it. At each fixed `β`, minimize in `γ` (PDF pp.2-3).
- Use the adiabatic curves to locate low-energy shapes, then trace fixed occupations to obtain configuration-specific minima. The figures shade `15°≤γ≤45°` as favorable for chirality and mark suitable minima with blue asterisks (PDF pp.2-3; Figs.1-2).
- Classify unpaired high-`j` occupations explicitly; low-`j` neutron `3p3/2`, `3p1/2` and `2f5/2` occupations are grouped as `(fp)` because the calculation cannot distinguish them reliably (PDF p.4).
- Compare selected previously measured energies and `B(M1)/B(E2)` values only as secondary systematics; the calculation itself does not produce the partner bands (PDF pp.7-9; Fig.4).

## Summary

The constrained PK1 calculation finds multiple candidate triaxial minima in `192-198Tl` and no suitable minimum in `199,200Tl`. For odd-odd `192,194,196,198Tl`, the recurring unpaired configuration is `πh9/2⊗νi13/2^-1`; `194Tl` also has a higher four-quasiparticle `πh9/2⊗ν(i13/2)^-3` candidate. For odd-mass `193,195,197Tl`, candidates combine a `πh9/2` particle with either two `i13/2` neutron holes or one low-`j` `(fp)` neutron plus one `i13/2` hole; `197Tl` additionally has a `πi13/2⊗ν(fp)^1i13/2^-1` candidate. The authors infer possible MχD throughout `192-198Tl`, but this is a necessary-condition screening result: no rotational spectrum, doublet splitting, aplanar geometry or transition network is calculated.

## Experimental or Theoretical Setup

- Relativistic mean-field Lagrangian with PK1; authors state NL3 and PC-PK1 give similar conclusions but only PK1 results are shown.
- 12 fermion and 20 meson harmonic-oscillator shells.
- Pairing neglected because of Pauli blocking.
- Both adiabatic and configuration-fixed constraints; `β` scanned and `γ` minimized.
- Valence protons referenced to `Z=82`; valence neutrons to `N=114`, except the grouped low-`j` `(fp)` subshells.
- No cranking frequency, angular-momentum orientation, symmetry restoration or laboratory-frame band calculation.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GT22-1 | The paper reports no new experiment; observed Tl bands and Fig.4 data are imported from earlier publications and ENSDF. | source-provenance | direct | PDF pp.1-2,7-9; Fig.4 | true |
| GT22-2 | Calculations use PK1, 12 fermion shells, 20 meson shells, adiabatic plus configuration-fixed triaxial constraints and no pairing. | model-input | direct | PDF p.2 | true |
| GT22-3 | The displayed favorable triaxial region is `15°≤γ≤45°`; blue-star minima additionally require a suitable unpaired high-`j` configuration. | model-selection | direct | PDF pp.2-3; Figs.1-2 | true |
| GT22-4 | Multiple triaxial local minima occur in `192-198Tl`, which the authors treat as examples of triaxial shape coexistence. | model-result | direct | PDF p.3; Figs.1-2 | true |
| GT22-5 | `199Tl` and `200Tl` have no suitable triaxial minimum in this calculation and are ruled out from the proposed candidate set, despite known high-`j` bands. | model-null-result | direct | PDF p.3; Figs.1-2 | true |
| GT22-6 | Candidate minima in odd-odd `192,194,196,198Tl` repeatedly have unpaired `πh9/2⊗νi13/2^-1`. | model-result | direct | PDF pp.5,7; Table 1 | true |
| GT22-7 | `192Tl` D*/H* have `(β,γ)=(0.21,39.84°)` and `(0.16,26.17°)`; their common unpaired pair but different total occupations/deformations motivates a two-pair MχD prediction distinct from the same-configuration `103Rh` mechanism. | model-interpretation | direct | PDF pp.5,7; Table 1 | true |
| GT22-8 | `194Tl` C*/H* have `(0.14,36.81°)` and `(0.17,18.80°)` with `πh9/2⊗νi13/2^-1`; I* at `(0.13,45.19°)` is a higher four-quasiparticle `πh9/2⊗ν(i13/2)^-3` candidate. | model-result | direct | PDF pp.5,7; Table 1 | true |
| GT22-9 | `196Tl` A*/E*/H* have `(0.13,34.88°)`, `(0.18,37.26°)` and `(0.12,42.75°)` with the same unpaired high-`j` pair, motivating three predicted doublets/six `ΔI=1` bands. | model-interpretation | direct | PDF pp.5,7; Table 1 | true |
| GT22-10 | `198Tl` B*/F* have `(0.11,39.43°)` and `(0.16,43.32°)` with `πh9/2⊗νi13/2^-1`; the authors connect them to the already reported pair and predict MχD. | model-interpretation | direct | PDF pp.5,7; Table 1 | true |
| GT22-11 | `193Tl` has five predicted candidate configurations: three positive-parity `πh9/2⊗ν(fp)^1i13/2^-1` and two negative-parity `πh9/2⊗ν(i13/2)^-2` cases. | model-result | direct | PDF pp.6-8; Table 2 | true |
| GT22-12 | `195Tl` has two positive-parity `πh9/2⊗ν(fp)^1i13/2^-1` and one negative-parity `πh9/2⊗ν(i13/2)^-2` candidate; its known five-quasiparticle bands are outside the present calculation. | model-result-boundary | direct | PDF pp.6,8; Table 2 | true |
| GT22-13 | `197Tl` has three positive-parity `πh9/2⊗ν(fp)^1i13/2^-1` candidates plus negative-parity `πh9/2⊗ν(i13/2)^-2` and `πi13/2⊗ν(fp)^1i13/2^-1` candidates. | model-result | direct | PDF pp.6,8; Table 2 | true |
| GT22-14 | The observed `197Tl` B2/B3 pair is assigned the last configuration, but missing `B(M1)/B(E2)` values leave its chirality open. | secondary-systematics | indirect | PDF pp.8-9; Fig.4 | true |
| GT22-15 | Experimental energy and ratio trends in `192,196Tl` are said to follow adjacent `194,198Tl` systematics, motivating partner searches; these comparisons do not establish the missing bands. | author-interpretation | indirect | PDF pp.7-8; Fig.4(a-h) | true |
| GT22-16 | Low-`j` neutron occupations are deliberately grouped as `(fp)` because `3p3/2`, `3p1/2` and `2f5/2` cannot be distinguished reliably; the high-`j` occupations control the classification. | model-boundary | direct | PDF p.4 | true |
| GT22-17 | Multiple favorable static minima are necessary-condition evidence only; the calculation does not generate rotational partner bands, aplanar angular-momentum geometry, tunnelling, splittings or electromagnetic strengths. | evidence-boundary | synthesis | Full paper | true |
| GT22-18 | Pairing is omitted, and the claim that NL3/PC-PK1 yield similar conclusions is not documented with corresponding tables or curves. | model-boundary | direct | PDF p.2 | true |

## Candidate-Minimum Map

| Nucleus | Candidate minima / configuration | Calibrated status |
|---|---|---|
| `192Tl` | D*/H*, `πh9/2⊗νi13/2^-1` | two model minima; two doublets predicted, none calculated |
| `193Tl` | 3 positive `(fp)i13/2^-1` + 2 negative `(i13/2)^-2` cases | five model candidate pairs |
| `194Tl` | C*/H* two-quasiparticle + I* four-quasiparticle | observed literature candidate plus further model possibilities |
| `195Tl` | 2 positive + 1 negative three-quasiparticle cases | three model candidates; five-quasiparticle states excluded |
| `196Tl` | A*/E*/H*, common unpaired high-`j` pair | three predicted doublets |
| `197Tl` | 3 positive + 2 negative three-quasiparticle cases | five predicted doublets; observed B2/B3 remains open |
| `198Tl` | B*/F*, common unpaired high-`j` pair | reported literature pair plus a second predicted pair |
| `199Tl` | no suitable minimum | model null control |
| `200Tl` | no suitable minimum | model null control |

## Competing Interpretations and Limitations

- A static constrained minimum does not show that a stable rotational band exists or that two bands are quantum chiral partners.
- `γ` is a model coordinate, and the shaded `15°-45°` region is a selection convention rather than an experimental observable.
- Shape coexistence is inferred from one mean-field energy landscape; softness, mixing and pairing could reorganize shallow minima.
- The `(fp)` grouping prevents orbital-specific assignments for the low-`j` spectator neutron.
- Existing `193-195,198Tl` candidates are cited as context and are not independent confirmations produced by this work.
- No predicted partner-resolved energies or transition probabilities are available for experimental falsification beyond broad configuration/minimum targeting.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The robust output is a map of favorable constrained minima and occupations, not a map of calculated chiral bands. | GT22-2 to GT22-6, GT22-17 | unreviewed |
| AR-2 | MχD semantics | Multiple minima motivate multiple searches, but each predicted doublet still requires an experimentally linked band pair and rotational quantum calculation. | GT22-7 to GT22-13, GT22-17 | unreviewed |
| AR-3 | Null controls | `199,200Tl` are valuable model-specific negative cases, not universal exclusions of chirality under other functionals/pairing treatments. | GT22-5, GT22-18 | unreviewed |
| AR-4 | Experimental gate | The strongest follow-up is partner-resolved spectroscopy with lifetimes/branching and configuration-sensitive calculations for `192,196,197Tl`. | GT22-14/15/17 | unreviewed |
| AR-5 | Transfer boundary | Do not resolve `(fp)` orbit labels or claim five-quasiparticle coverage in `195Tl`; both exceed the paper's model space. | GT22-12/16 | unreviewed |
| AR-6 | Research decision | Persist nine lightweight isotope pages and theory/concept links, but create no band page from unobserved minima. | Full paper | unreviewed |

### Companion Evidence Audit

- New levels, transitions or lifetimes: `none`.
- Deformation minima and occupations: `self-consistent constrained-RMF results`.
- Existing Tl bands and ratios: `secondary imported evidence`.
- Rotational doublets, handed geometry and tunnelling: `not calculated`.
- `199,200Tl` exclusion: `model-specific null result`.

## Knowledge Impact and Learning Decision

- Effect: extends the corpus from interpreting observed doublets to a full `192-200Tl` theory-screening chain, including positive and negative controls.
- Persistence: source; lightweight pages for all nine isotopes; update MχD, triaxial-shape-coexistence, CDFT and the corpus project. No experiment or band page is created.
- Review state: all `GT22-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **GT22-3/17 — candidate criterion.** Keep the favorable γ window and suitable occupations separate from an actual rotational chiral solution.
- **GT22-7 to GT22-13 — predicted pair counts.** These are counts inferred from minima, not observed or calculated doublet bands.
- **GT22-12 — `195Tl` model-space boundary.** The known five-quasiparticle system is explicitly unavailable here.
- **GT22-14/15 — secondary evidence.** Do not count Fig.4 as a new experimental dataset.
- **GT22-16 — `(fp)` notation.** Do not silently assign a specific low-`j` orbital.

### P2/P3

- P2: return to the original `193-195,198Tl` experiments before numerical reuse of Fig.4.
- P3: test the minima with pairing-inclusive CDFT and a rotational quantum model that predicts spectra and matrix elements.

## Related Knowledge and Project Relations

- [[192tl]], [[193tl]], [[194tl]], [[195tl]], [[196tl]], [[197tl]], [[198tl]], [[199tl]], [[200tl]].
- [[multiple-chiral-doublet-bands]], [[triaxial-shape-coexistence]], [[covariant-density-functional-theory]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `guo_2022_Possibleexistence` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2022_Possible existence of chiral and multiple chiral nuclei in thallium isotopes .pdf`.

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start": 1, "end": 2, "sections": "题录、摘要、引言、RMF 形式与数值设置、结果开头"}
- {"start": 3, "end": 4, "sections": "势能曲线及 γ 的模型讨论、图1–3图注、单粒子能级和占据记法"}
- {"start": 5, "end": 6, "sections": "表1双奇核和表2奇质量核的固定组态极小值"}
- {"start": 7, "end": 9, "sections": "双奇核及奇质量核候选、图4图注与既有数据比较、总结"}
- {"start": 9, "end": 10, "sections": "全部参考文献"}
- 本次获取的具体覆盖：逐页读完物理第1–10页的提取文本，包括式(1)–(3)、表1–2文字、图1–4图注及正文讨论和参考文献[1]–[98]。图面、图例与数据点未做视觉核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 绝热和固定组态约束三轴 RMF 采用 PK1、12个核子与20个介子谐振子主壳，省略配对，在给定 β 下对 γ 作能量最小化。计算在 ¹⁹²–¹⁹⁸Tl 找到多个三轴局部极小值，¹⁹⁹、²⁰⁰Tl 在此次筛选中无合适极小值。 | 模型设置与计算结果 | source-reported | 物理第2页第II节及式(1)–(3)，第3页图1–2及正文，第5–6页表1–2。图上阴影界线和标记待看第3页。 | true |
| A17-2 | 表1对 ¹⁹²、¹⁹⁴、¹⁹⁶、¹⁹⁸Tl 分别列出2、2、3、2个带星的共同高 j 质子粒子－中子空穴组态极小值。¹⁹⁴Tl 另列四准粒子组态 I*，γ 为45.19°。表2对 ¹⁹³、¹⁹⁵、¹⁹⁷Tl 分别列出5、3、5个带星候选。 | 模型结果 | source-reported | 物理第5页表1、第6页表2、第7–8页第III.A–B节。逐项引用能量或占据前须核第5–6页原表。 | true |
| A17-3 | 旧文献已报道 ¹⁹⁴、¹⁹⁸Tl 的候选带对以及 ¹⁹²、¹⁹⁶Tl 同组态的转动带。对图4(i–n)讨论的 ¹⁹⁷Tl 双中子空穴组态带，作者给出已有能谱比较并指出对应的 B(M1)/B(E2) 尚缺。 | 既有实验的转述 | source-reported | 物理第7页第III.A节、第8页图4图注、第9页第III.B节。图例、逐点数据及空缺面板待核第8页。 | true |
| A17-4 | 作者以具合适占据的三轴极小值提出 ¹⁹²–¹⁹⁸Tl 可能存在多重手征双带，并以相邻同位素的既有能谱和跃迁比值支持继续寻找 ¹⁹²、¹⁹⁶Tl 的伙伴带。这些是由静态极小值与实验系统学提出的预测。 | 作者解释与预测 | source-reported | 物理第7–9页第III.A–B节与第IV节，表1–2在第5–6页，实验比较图4在第8页。 | true |

图4图注列数据来源[24]、[60]、[61]、[64]、[65]、[94]–[98]，其中[98]为 ENSDF，条目见物理第10页。原实验与数据库记录未另行读取。本文新增证据为受约束的静态计算，未报告新实验。

- GT22-3 的 15°≤γ≤45° 应标为待核的图示区间。物理第3页提取只说明阴影有利于手征，未给出数值边界。第5页表1和第7页仍明确将 γ=45.19° 的 ¹⁹⁴Tl I* 列为候选，故不能把该区间写成严格截断。
- GT22-14 应拆开两项。物理第8页把 ¹⁹⁷Tl B2/B3 归于含 πi₁₃/₂ 的组态，并称其手征归属待定。第9页所述比值缺失对应图4(i–n)讨论的 πh₉/₂ 双中子空穴组态带。当前正文未把该缺失归给 B2/B3。
- 物理第5页表1的 ¹⁹⁸Tl F* 列出 E_tot=−1555.44 MeV，按同表 A 态的 −1555.14 MeV 得 −0.30 MeV，与所列 E_x=2.40 MeV 冲突。保留行号和疑点，核图前不指定替换值。¹⁹²Tl H* 的完整价中子占据在第5页表1与第7页叙述也有出入，逐轨道引用须核两页。
- 物理第2页 β 约束式的四极矩上下标和平方在提取中连写。物理第6页表2的表题 T1、列题 (β,γ)α、¹⁹⁷Tl J* 的 43,29° 和 ¹⁹⁹Tl E 的 i13/1 均需回看原页。第4页图3图注的点线与邻接正文的虚线用词不同，线型以原图核定。
