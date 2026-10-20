---
type: source
title: "Kuti et al. 2014 - Multiple chiral doublet bands of identical configuration in 103Rh"
aliases: [Kuti 2014 103Rh, identical-configuration MχD in 103Rh]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Multiple Chiral Doublet Bands of Identical Configuration in 103Rh"
authors: [I. Kuti, Q. B. Chen, J. Timár, D. Sohler, S. Q. Zhang, Z. H. Zhang, P. W. Zhao, J. Meng, K. Starosta, T. Koike, E. S. Paul, D. B. Fossan, C. Vaman]
journal: Physical Review Letters
year: 2014
volume: 113
pages: 032501
doi: 10.1103/PhysRevLett.113.032501
language: English
canonical_source: https://doi.org/10.1103/PhysRevLett.113.032501
citation_key: kuti_2014_MultipleChiral
raw_file: "raw/papers/2014_Kuti et al_Multiple Chiral Doublet Bands of Identical Configuration in Rh 103.pdf"
raw_sha256: EF327AD2D7B55A71B72C356BB2789F107B1E1D464DAA59C181BEC44ABF88A0B2
nuclei: [103rh]
reactions: ["96Zr(11B,4n)103Rh"]
experiments: [lbnl-gammasphere-103rh-b11-40mev]
models: [constrained-covariant-density-functional-theory, tac-cdft, particle-rotor-model]
observables: [dco-ratio, bm1-be2-ratio, angular-momentum-alignment, same-spin-energy-displacement]
methods: [gamma-gamma-coincidence, dco-ratio, configuration-fixed-cdft, tilted-axis-cranking, particle-rotor-model]
tags: [experiment-ingest, project-ingest, a100, odd-a, nuclear-chirality, multiple-chiral-doublet-bands]
---

# Multiple Chiral Doublet Bands of Identical Configuration in `103Rh`

## Bibliographic Record

Physical Review Letters 113, 032501 (2014), DOI `10.1103/PhysRevLett.113.032501`. The protected BibTeX key is `kuti_2014_MultipleChiral`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all five PDF pages; experimental setup, partial level scheme and DCO logic; Bands 1–6 identity; same-spin separations, alignments and experimental `B(M1)/B(E2)` ratios; constrained CDFT, TAC-CDFT and PRM inputs/results; limitations and conclusion.
- Not covered: raw coincidence matrices, efficiency calibration details, the complete `103Rh` level scheme, or the cited 2004/2006 `103Rh` spectroscopy and 2011 PRM papers in full.
- Coverage caveats: parity assignments use an explicit electromagnetic-character assumption; the paper does not tabulate lifetime-separated absolute strengths; the detailed TAC-CDFT angular-momentum analysis is deferred to a future publication.

## Extracted Pages

- PDF p.1: motivation, experiment and start of spin/parity method.
- PDF p.2: partial level scheme, DCO values and Bands 3–6 links.
- PDF p.3: alignment grouping, constrained CDFT and TAC-CDFT configuration/shape results.
- PDF p.4: PRM inputs, energies and `B(M1)/B(E2)` comparison.
- PDF p.5: alignment discrepancy, same-configuration MχD conclusion and references.

## Paper Question and Scientific Motivation

The paper asks whether chirality survives not only a change of configuration but also an increase of intrinsic excitation within one configuration. It therefore searches beyond the lowest two bands of a configuration and tests whether the third and fourth negative-parity bands form a second chiral doublet alongside the yrast pair (PDF pp.1,3-5).

## Method and Design Logic

- High-fold Gammasphere coincidences extend known Bands 3/6 and establish new Bands 4/5 (PDF pp.1-2; Figs.1-2).
- DCO ratios classify stretched quadrupole and dipole links; spin/parity assignments combine those ratios with a stated E2/M1 assumption (PDF pp.1-2).
- Same-spin energy differences, experimental `B(M1)/B(E2)` ratios and Harris-reference alignments group Bands 3/4 and 6/5 (PDF pp.2-3; Figs.3-4).
- Constrained CDFT identifies candidate configurations/shapes, TAC-CDFT follows them with rotation, and PRM compares four quantum bands and transition ratios with the observations (PDF pp.3-5; Fig.4).

## Summary

The experiment reports three proposed doublet structures in `103Rh`: positive-parity Bands 1/2 and two negative-parity pairs, Bands 3/4 and Bands 6/5. The two negative pairs are assigned the same effective `πg9/2^-1⊗νh11/2g7/2` configuration and interpreted as yrast and excited chiral doublets. This is the paper's first-evidence claim for same-configuration MχD. The durable experimental result is four mutually linked negative-parity bands with small pairwise separations and similar ratios/alignments; identical configuration, aplanar geometry and robustness against intrinsic excitation remain model-supported interpretations with visible PRM and frozen-core limitations.

## Experimental or Theoretical Setup

- `96Zr(11B,4n)103Rh` at `40 MeV`, LBNL 88-inch cyclotron.
- Enriched self-supporting `96Zr` target, `500 μg/cm²`.
- Gammasphere; about `9×10^8` four-and-higher-fold events; RADWARE 2D/3D sorting.
- With a stretched-quadrupole gate, `R_DCO≈1.0` and `≈0.5` are expected for stretched quadrupole and dipole transitions.
- Alignment reference: `K=1/2`, Harris `J0=7 ħ²/MeV`, `J1=15.7 ħ⁴/MeV³`.
- CDFT/TAC-CDFT effective interaction: PC-PK1. PRM uses `γ=20°`, `β=0.29/0.26` and moments of inertia `23/25 ħ²/MeV` for positive/negative parity; negative-parity calculation uses Coriolis attenuation `ξ=0.85`.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU14-1 | The experiment accumulated about `9×10^8` four-and-higher-fold Gammasphere events following `96Zr(11B,4n)` at `40 MeV`. | experimental-fact | direct | PDF pp.1-2 | true |
| KU14-2 | Known Bands 3 and 6 were extended to `39/2` and `35/2`, and new Bands 4 and 5 were established through triple coincidences. | experimental-fact | direct | PDF p.2; Figs.1-2 | true |
| KU14-3 | The `674/1007-keV` links from Band 5 to B and `574/700-keV` links from Band 4 to 6 have quadrupole-like DCO values, while `396/391-keV` 4→3 and 5→6 links have dipole-like values. | method-result | direct | PDF p.2 | true |
| KU14-4 | Negative parity for Bands 4/5 additionally assumes that comparable quadrupole/dipole decays to a band are E2/M1; DCO alone does not determine electric versus magnetic character. | evidence-boundary | direct | PDF pp.1-2 | true |
| KU14-5 | Bands 3–6 are four mutually linked negative-parity `ΔI=1` bands; same-spin differences are about `300 keV` for 3/4 and `100 keV` for 6/5, with similar experimental `B(M1)/B(E2)` values. | experimental-fact | direct | PDF pp.2-3; Figs.1,4 | true |
| KU14-6 | All four bands have alignment near `9ħ`; the strongest pairwise similarities are 3/4 and 5/6, motivating the yrast 3/4 and excited 6/5 grouping. | derived-observable | direct | PDF p.3; Fig.3 | true |
| KU14-7 | Bands 4 and 6 are sufficiently close that their energy ordering changes with spin, so “yrast/excited” labels describe pair grouping rather than a fixed ordering of every member. | evidence-boundary | direct | PDF p.3 | true |
| KU14-8 | Earlier positive-parity Bands 1/2 retain the proposed `πg9/2^-1⊗ν(h11/2)^2` configuration; this paper's numbering is not explicitly crosswalked to Suzuki 2008's lifetime-measured “Band 3.” | source-crosswalk-boundary | direct | PDF pp.2,4; comparison with Suzuki 2008 | true |
| KU14-9 | Constrained CDFT gives a γ-soft ground-state minimum near `β=0.25, γ=20°`, a positive-parity candidate near `β=0.29, γ=11°`, and two triaxial negative-parity candidates. | model-result | indirect | PDF p.3 | true |
| KU14-10 | TAC-CDFT selects an effective negative-parity `πg9/2^-1⊗νh11/2g7/2` description, with neutron angular momenta mainly along the short axis and the proton hole mainly along the long axis. | model-result | indirect | PDF p.3 | true |
| KU14-11 | The TAC-CDFT geometry discussion is incomplete in this Letter because calculation details are explicitly deferred to a forthcoming publication. | model-boundary | direct | PDF p.3 | true |
| KU14-12 | Positive-parity PRM reproduces energies and similar ratios, while the slower experimental ratio decrease is attributed to the frozen-rotor approximation; a prior PRM study supplies the vibration→near-static→vibration evolution. | model-result | indirect | PDF p.4; Fig.4 | true |
| KU14-13 | Negative-parity PRM produces two doublets and reasonably reproduces Bands 3–6, but Bands 5/6 lie about `200 keV` too high, attributed to missing complex correlations. | model-result | indirect | PDF p.4; Fig.4 | true |
| KU14-14 | The sharp alignment increase of Bands 5/6 near `ħω=0.45 MeV` is not reproduced and is attributed to the frozen core. | model-discrepancy | direct | PDF p.5; Fig.3 | true |
| KU14-15 | The authors interpret weak ratio staggering in 3/4 as chiral vibration and reproduce a 5/6 staggering near `I=15.5`, but the ratios are not lifetime-separated absolute strengths for all four bands. | author-interpretation | indirect | PDF pp.4-5; Fig.4 | true |
| KU14-16 | The same-configuration MχD and robustness-against-intrinsic-excitation conclusions depend on assigning both negative-parity pairs to the same effective configuration. | evidence-boundary | indirect | PDF pp.4-5 | true |

## Nuclear Structure Information

| Structure | Parity / role | Assignment and boundary |
|---|---|---|
| Bands 1/2 | positive-parity earlier candidate | `πg9/2^-1⊗ν(h11/2)^2`; PRM-supported chiral-vibrational evolution; direct crosswalk to Suzuki's Band-3 lifetime label unresolved |
| Bands 3/4 | negative-parity yrast candidate pair | first two bands of effective `πg9/2^-1⊗νh11/2g7/2`; ≈`300-keV` separation |
| Bands 6/5 | negative-parity excited candidate pair | third/fourth bands of the same assigned configuration; ≈`100-keV` separation; PRM energy/alignment discrepancies |
| Bands A/B | previously known reference bands | constrained CDFT agrees with earlier low-quasiparticle configuration assignments; not part of the three chiral pairs |

## Competing Interpretations and Limitations

- Similar energies, ratios and alignments can establish related rotational structures without directly measuring handedness.
- The identical-configuration conclusion depends on CDFT/TAC-CDFT/PRM mapping rather than a model-independent configuration observable.
- The PRM uses fixed deformation, a frozen rotor/core, a single-j Hamiltonian and fitted inertias/attenuation; the observed discrepancies expose those approximations.
- Experimental ratios do not replace absolute lifetimes and matrix elements for both members of both negative-parity pairs.
- Positive-pair comparison across Suzuki 2008 and Kuti 2014 requires a source-level band-number crosswalk not supplied in Kuti's text.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The strongest new fact is a four-band negative-parity manifold grouped into two closely related pairs; same-configuration MχD is the joint experimental-model interpretation. | KU14-2 to KU14-7, KU14-9/10/13 | unreviewed |
| AR-2 | Assumptions | Parity, identical configuration and handed geometry depend respectively on an E2/M1 assumption and model assignments. | KU14-4, KU14-9 to KU14-11 | unreviewed |
| AR-3 | Failure condition | Different configurations, strong configuration mixing or a nonchiral four-band collective solution would invalidate the robustness claim without erasing the observed bands. | KU14-13/14/16 | unreviewed |
| AR-4 | Reverse test | Measure lifetimes/mixing ratios throughout Bands 3–6 and compare a dynamical model that treats shape/core fluctuations with explicit nonchiral alternatives. | Full paper | unreviewed |
| AR-5 | Cross-source identity | Preserve Suzuki's one-sided lifetime result without assigning it to Kuti Band 1 or 2 until the earlier Ref.19/Ref.14 schemes are directly crosswalked. | KU14-8 | unreviewed |
| AR-6 | Research decision | Store three candidate pairs, but reserve the MχD-identical-configuration label for the two negative-parity pairs. | Full paper | unreviewed |

## Knowledge Impact and Learning Decision

- Effect: `supports` an experimental-model case for same-configuration MχD and `limits` it through assignment, absolute-strength and model-dynamics gaps.
- Persistence: create source/experiment and two negative-pair pages; extend the existing positive-pair page, `103Rh`, MχD concept and chirality project.
- Review state: all `KU14-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **KU14-4 — parity logic.** Keep the electromagnetic-character assumption separate from the DCO measurements.
- **KU14-8 — band-number crosswalk.** Do not map Suzuki's lifetime Band 3 directly onto Kuti Band 1 or 2 without reading the earlier schemes.
- **KU14-10/11/16 — same-configuration geometry.** Preserve CDFT/TAC-CDFT dependence and the deferred calculation details.
- **KU14-13/14 — model discrepancies.** Retain the `≈200-keV` energy excess and missing alignment jump as active limitations.
- **KU14-15 — ratio semantics.** Do not rewrite plotted `B(M1)/B(E2)` ratios as absolute partner-band matrix elements.

## Related Knowledge and Project Relations

- [[103rh]], [[103rh-chiral-doublet-candidate]], [[103rh-negative-parity-yrast-chiral-doublet]], [[103rh-negative-parity-excited-chiral-doublet]].
- [[lbnl-gammasphere-103rh-b11-40mev]].
- [[multiple-chiral-doublet-bands]], [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `kuti_2014_MultipleChiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2014_Kuti et al_Multiple Chiral Doublet Bands of Identical Configuration in Rh 103.pdf`.

## Day18原件复核纠正：负宇称候选与正宇称寿命基准分域

2026-10-21 的 checkpoint048 原件 self-audit 核读主raw，SHA-256 `ef327ad2d7b55a71b72c356bb2789f107b1e1d464daa59c181bec44abf88a0b2`；并定向核[[suzuki-2008-lifetimes-103rh-104rh]]原PDF3–4（SHA-256 `f9c421090b33da94206f9d1d4ebd36ad0f5be79ee1dcd6a19fe38b32a7ec5927`）。前文KU14-1–16与原review记录保持，不新增实验或课程学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU14-D18-1 | **superseded（2026-10-21）**：旧追加段将不合Suzuki原表的数字用于解释Kuti负宇称带，并宣称“100%分母驱动”；该数据与排他因果结论撤回。本文的模型差异可保留为作者报告/解释，但不能与错误跨域寿命桥接合并裁决MχD。旧result-037/contract-037不再验证原结论，由KU14-D18-2–11替代。 | superseded-task-audit | corrected-and-boundary | 本段KU14-D18-2–11；旧kuti14-103rh-mxd-result-037及contract-037 | true |
| KU14-D18-2 | Kuti本文以负宇称Bands3–6的相对γ强度、B(M1)/B(E2)、能量与对齐研究同组态MχD，未报告这些带的DSAM/RDDS寿命分离绝对强度。此为本文及本次已核材料的readiness边界，不能扩成“截至今日整个文献领域均无寿命”的穷尽结论。 | source-coverage-boundary | direct-and-boundary | PDF pp.1–5，尤p.2带身份、pp.3–5/Figs.3–4 | true |
| KU14-D18-3 | 本文Bands1/2为正宇称，Bands3–6为负宇称；Suzuki测寿命的103Rh Band3为正宇称，不是Kuti的负宇称Band3。与Kuti正宇称Bands1/2的精确编号对应也仍需早期scheme核对；同核或同band数字不能代替身份crosswalk。 | parity-and-band-identity-boundary | direct-and-cross-source | Kuti PDF p.2与p.4 Fig.4；Suzuki PDF p.3 Tables I/III；本页KU14-8；SU08-4/6 | true |
| KU14-D18-4 | Suzuki原TableIII的103Rh值为25/2+、27/2+、29/2+，对应BM1=2.3(4)、1.8(2)、1.2(4) μN²，BE2=.077(14)、.14(3)、.11(4) e²b²；对应TableI寿命为.95(17)、1.0(1)、.72(23) ps。该绝对强度基准只涉及一条正宇称候选成员，并采用pure M1及旧分支输入。 | companion-reported-data-and-assumptions | direct | [[suzuki-2008-lifetimes-103rh-104rh]] SU08-4/6/7/13；原PDF p.3 Tables I/III | true |
| KU14-D18-5 | 旧037脚本写入的27/2+、29/2+、31/2+及BM1 .46/.40/.35、BE2 .18/.35/.20不合上述Suzuki原表，不能继续作为实验输入或正宇称benchmark。由其算出的2.56→1.14→1.75亦不保留为原实验比值。 | erroneous-input-correction | direct-and-boundary | 旧037脚本suzuki_data；Suzuki原PDF p.3 TableIII | true |
| KU14-D18-6 | Suzuki作者把所测正宇称103Rh及104Rh的弱比值交错归因于BE2、而BM1随spin递减；其结论没有给“100%排他因果”分解，并明确称BE2交错尚待理论解释、要求伙伴及更高spin寿命。该结果可以说明比值不能定位单独矩阵元，不能直接裁决Kuti不同宇称/组态的负宇称M1选择律。 | companion-author-interpretation-and-transfer-limit | direct-and-boundary | Suzuki PDF pp.3–4正文、Tables IV/V及总结；SU08-8/11/13/14 | true |
| KU14-D18-7 | Kuti实际PRM采用β=.29（正宇称）和.26（负宇称）、γ=20°；旧037脚本β=.20及固定K=1/2的Q0/BE2示例不是该文实际输入重构。即使算术成立，也须另标几何条件，不能称本文PRM的绝对强度输出。 | model-input-correction | direct-and-boundary | PDF p.3末段至p.4首段与Q0公式；旧037脚本beta/cg_ref | true |
| KU14-D18-8 | 作者报告PRM给Bands5/6的能量约比实验高200 keV，可能与单j Hamiltonian未充分包含复杂关联有关。这是模型差异与作者解释，不是实验证实的唯一误差来源。 | model-discrepancy-and-author-explanation | direct | PDF p.4右栏；Fig.4 | true |
| KU14-D18-9 | 原Fig.3及p.5指出Bands5/6在ħω约.45 MeV的对齐跳增未再现，作者称可能与frozen core有关；不能把“可能”改为确定因果或据此单独否定同组态MχD。 | model-discrepancy-and-boundary | direct | PDF p.3 Fig.3；p.5首段 | true |
| KU14-D18-10 | Bands4/6很接近且能量排序随spin改变，是作者明确保留的配对边界。相近能量本身不抹掉其依据对齐/比值提出的3/4和6/5分组；这些分组与同组态/手征归属仍属实验加模型解释。 | pair-grouping-boundary | direct-and-interpretation | PDF p.3左栏对齐分组段；pp.4–5讨论 | true |
| KU14-D18-11 | 本次完整核读Kuti五页正文主线及全部图注，视觉核PDF3 Fig.3/模型输入与PDF4 Fig.4；Suzuki仅定向原读PDF3–4并视觉核Tables I/III，不声称其全文新读。旧037脚本不读declared raw、status=passed为固定赋值；未取得新原谱、伙伴寿命或联合协方差，不生成实验CI。 | current-reading-and-producer-scope | direct-and-boundary | Kuti主raw PDF pp.1–5；Suzuki PDF pp.3–4；旧037脚本主体 | true |

旧[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/kuti14-103rh-mxd-contract-037.json)及[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/kuti14-103rh-mxd-result-037.json)在本段原结论用途上标为 **superseded**，不重跑或覆盖。后续优先区分正负宇称的真实母态/伙伴，补测或取得同一组负宇称伙伴的绝对强度与混合比，再比较具体模型和替代解释。
