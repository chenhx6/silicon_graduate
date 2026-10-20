---
type: source
title: "Wang et al. 2013 - High-spin level structure of 104Ag"
aliases: [Wang 2013 104Ag, 104Ag high-spin structure]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "High-spin level structure of the doubly odd nucleus 104Ag"
authors: [Z. G. Wang, M. L. Liu, Y. H. Zhang, X. H. Zhou, B. T. Hu, N. T. Zhang, S. Guo, B. Ding, Y. D. Fang, J. G. Wang, G. S. Li, Y. H. Qiang, S. C. Li, B. S. Gao, Y. Zheng, W. Hua, X. G. Wu, C. Y. He, Y. Zheng, C. B. Li, J. J. Liu, S. P. Hu]
journal: Physical Review C
year: 2013
volume: 88
pages: 024306
doi: 10.1103/PhysRevC.88.024306
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.88.024306
citation_key: wang_2013_Highspinlevel
raw_file: "raw/papers/2013_Wang et al_High-spin level structure of the doubly odd nucleus 104 Ag.pdf"
raw_sha256: 366246ACEC6C6B5A46169606B125683BBD58C9D512A980A3910E5B23D837039C
nuclei: [104ag]
reactions: ["97Mo(11B,4n)104Ag"]
experiments: [ciae-hi13-104ag-b11-50mev]
models: [axial-rotor-plus-two-quasiparticle, tilted-axis-cranking]
observables: [ado-ratio, bm1-be2-ratio, energy-staggering-parameter, angular-momentum-alignment]
methods: [gamma-gamma-coincidence, ado-ratio, systematics-comparison]
tags: [experiment-ingest, project-ingest, a100, odd-odd, nuclear-chirality, magnetic-rotation, electric-quadrupole-rotation]
---

# High-Spin Level Structure of `104Ag`

## Bibliographic Record

Physical Review C 88, 024306 (2013), DOI `10.1103/PhysRevC.88.024306`. The protected BibTeX key is `wang_2013_Highspinlevel`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all nine PDF pages; experiment/ADO calibration; complete Table I and Bands A-F scheme; spin-parity assignments; A/B chiral fingerprints; C single-particle interpretation; D/E electric-quadrupole configurations/mixing; F magnetic-rotation assignment; summary.
- Not covered: raw coincidence matrix, detector efficiencies, the earlier `104Ag` band-identification papers, or the cited axial-rotor/TAC/chiral-model sources in full.
- Coverage caveats: the paper reports no lifetimes or polarization; ratios in Fig.4 are not absolute strengths and their derivation is referred to earlier work; several spins/parities/configurations are tentative or systematics based.

## Extracted Pages

- PDF pp.1-2: motivation, experiment/ADO, construction and assignments of Bands A-E and band-like C.
- PDF pp.3-4: full transition table and start of configuration discussion.
- PDF pp.5-6: complete A-F level scheme, A/B energy/`S(I)`/ratio/alignment fingerprints and candidate claim.
- PDF p.7: C, D/E and F configuration/systematics interpretations.
- PDF p.8: summary and references.
- PDF p.9: references only.

## Paper Question and Scientific Motivation

The experiment maps the coexistence of single-particle excitations, electric-quadrupole and magnetic rotation, and possible nuclear chirality in the particle-hole nucleus `104Ag`. For the chiral question it asks whether linked negative-parity Bands A/B share `πg9/2^-1⊗νh11/2` and exhibit the common energy, staggering and alignment fingerprints used in A≈100 candidates (PDF pp.1,4-6).

## Method and Design Logic

- A higher-statistics fusion-evaporation γ-γ experiment reconstructs Bands A-F from coincidences, intensity balances and energy sums (PDF pp.1-5; Figs.1-3; Table I).
- ADO ratios from asymmetric angle matrices separate stretched quadrupole (`≈1.2`) from pure dipole (`≈0.8`) transitions and support spin changes (PDF pp.1-2).
- Bands A/B are compared through same-spin energy separation, `S(I)`, `B(M1)/B(E2)`, `B(M1)in/B(M1)out` and quasiparticle alignment (PDF pp.5-7; Figs.4-5).
- Bands C-F are assigned by low-lying multiplet logic, Ag-isotope systematics and prior theoretical work, not by new dedicated calculations (PDF pp.6-7; Fig.6).

## Summary

More than 40 new γ rays revise and extend a six-structure A-F scheme. The paper suggests negative-parity A/B as a `πg9/2^-1⊗νh11/2` chiral-doublet candidate: their separation falls below `300 keV` at `I=15`, `S(I)` is smooth/similar, ratio staggering is in phase and alignments are nearly identical. A subsection calls them “true chiral partners,” but the abstract/summary retain “candidate,” and no lifetime, polarization or dedicated `104Ag` chiral calculation is provided. Positive-parity D/E are assigned electric-quadrupole rotational bands with `d5/2/g7/2` configurations and mixing; F retains a prior magnetic-rotation/four-quasiparticle interpretation.

## Experimental or Theoretical Setup

- `97Mo(11B,4n)104Ag` at `50 MeV`, CIAE HI-13 tandem.
- `2.0 mg/cm²`, `94.25%` enriched `97Mo` target on `8.0 mg/cm²` natural Pb backing.
- Thirteen Compton-suppressed HPGe detectors at forward, `90°` and backward angles.
- At least two suppressed detectors within an `80 ns` prompt window; `1.5×10^8` coincidence events.
- Energy/efficiency standards: `60Co`, `133Ba`, `152Eu`; resolution `2.0-2.5 keV` FWHM at `1332.5 keV`.
- ADO definition `R_ADO=Iγ(40° or 140°)/Iγ(90°)` with all-angle gates; typical stretched-E2/pure-dipole values `1.2/≈0.8`.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W13-1 | The experiment records `1.5×10^8` prompt γ-γ events with 13 suppressed HPGe detectors following `97Mo(11B,4n)` at `50 MeV`. | experimental-fact | direct | PDF pp.1-2 | true |
| W13-2 | Coincidences, intensity balances and energy sums establish a revised six-structure A-F scheme with more than 40 new γ rays. | experimental-fact | direct | PDF p.2; Figs.1-3; Table I | true |
| W13-3 | ADO ratios use typical values `1.2` for stretched quadrupole and `≈0.8` for pure dipole transitions. | method-result | direct | PDF pp.1-2 | true |
| W13-4 | New Band-B links establish a proposed `(10−)` bandhead at `2212 keV`, `(11−)` at `2711 keV` and a linked extension to `16−`; several assignments remain parenthesized. | experimental-assignment | direct | PDF pp.2-5; Fig.1; Table I | true |
| W13-5 | Band A inherits a `πg9/2^-1⊗νh11/2` assignment from earlier axial-rotor-plus-two-quasiparticle calculations; the same configuration is suggested for B from neighboring-systematics. | author-interpretation | indirect | PDF pp.4-5 | true |
| W13-6 | A/B are linked by strong M1 transitions; same-spin separation decreases with spin and is below `300 keV` at `I=15`, but does not reach the degeneracy reported for `104Rh`. | experimental-fact | direct | PDF p.5; Figs.1,4a | true |
| W13-7 | The remaining separation is interpreted as γ-soft chiral vibration by analogy, without a new shape calculation for `104Ag`. | author-interpretation | indirect | PDF p.5 | true |
| W13-8 | A/B have broadly smooth/similar `S(I)`, in-phase ratio staggering and nearly identical quasiparticle alignments. | derived-observable | direct | PDF pp.5-7; Figs.4-5 | true |
| W13-9 | `B(M1)/B(E2)` and `B(M1)in/B(M1)out` in Fig.4 are ratio fingerprints referenced to earlier methodology; no lifetime-separated absolute strengths or mixing ratios are reported here. | evidence-boundary | direct | PDF pp.5-6; Fig.4 | true |
| W13-10 | The discussion calls A/B “true chiral partners,” while the abstract and summary call them candidate chiral doublet bands. | source-language-conflict | direct | PDF pp.1,6,8 | true |
| W13-11 | No dedicated `104Ag` TAC/PRM calculation or measured angular-momentum geometry is presented for A/B. | model-boundary | direct | Full paper | true |
| W13-12 | Based on candidate systematics, the authors propose `N=57` as the low-neutron-number border for A≈100 chiral nuclei but state more data are required. | author-interpretation | indirect | PDF p.6 | true |
| W13-13 | Positive-parity D/E are assigned `πg9/2^-1⊗νd5/2` and `πg9/2^-1⊗νg7/2`; staggering/strong links are interpreted as configuration mixing by Ag-isotope analogy. | author-interpretation | indirect | PDF pp.2,7; Fig.6 | true |
| W13-14 | Band-like C is associated with the `2+` isomer and a low-lying proton-neutron multiplet, but the configuration discussion remains tentative. | author-interpretation | indirect | PDF pp.2,6-7 | true |
| W13-15 | Band F retains an earlier magnetic-rotation assignment and is proposed as a four-quasiparticle `πg9/2^-1⊗ν(g7/2/d5/2)(h11/2)^2` structure by comparison with `106,108Ag`. | author-interpretation | indirect | PDF p.7 | true |

## Nuclear Structure Information

| Structure | Parity / role | Assignment and boundary |
|---|---|---|
| A/B | negative, linked candidate doublet | common `πg9/2^-1⊗νh11/2` suggested; candidate overall despite local “true” wording |
| C | positive band-like multiplet | connected to `2+` isomer; detailed particle/hole content tentative |
| D/E | positive electric-quadrupole rotational bands | `d5/2`/`g7/2` configurations with mixing inferred from systematics |
| F | positive magnetic-rotational band | earlier TAC-supported assignment; four-quasiparticle identity proposed by analogy |

## Competing Interpretations and Limitations

- A/B fingerprints are not independent proof: energy separation persists, ratios are nonabsolute and alignment similarity can follow a common configuration without handedness.
- The paper has an internal wording gradient from “true partners” to “candidate”; the conservative stable status is candidate.
- γ softness/chiral vibration is imported from systematics, not established by a `104Ag` potential-energy or dynamical calculation.
- D/E and F configurations depend heavily on neighboring Ag nuclei and prior calculations; several spins are tentative.
- No lifetimes, mixing ratios, linear polarization, g factors or dedicated quantum chiral calculation are supplied.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The durable advance is the revised A-F scheme and a strongly fingerprinted A/B candidate, not confirmed chirality. | W13-2, W13-4 to W13-11 | unreviewed |
| AR-2 | Assumptions | Common configuration, γ softness and ratio staggering depend on earlier/systematic inputs; absolute electromagnetic equality is not measured. | W13-5, W13-7, W13-9 | unreviewed |
| AR-3 | Failure condition | Lifetime/mixing-ratio data or a dedicated model favoring ordinary configuration mixing/signature partners could overturn the chiral interpretation while retaining A/B. | Full paper | unreviewed |
| AR-4 | Reverse test | Measure absolute in-/out-of-band matrix elements and compare chiral PRM/TAC dynamics against γ-soft/configuration-mixing alternatives on the same bands. | W13-9 to W13-11 | unreviewed |
| AR-5 | Transfer condition | The proposed `N=57` boundary is a provisional census statement, not an exclusion theorem for lower-N nuclei. | W13-12 | unreviewed |
| AR-6 | Research decision | Persist A/B as a candidate with a source-language conflict; persist D/E and F as separate electric and magnetic rotation references. | Full paper | unreviewed |

### Companion Evidence Audit

- A-F scheme, links and ADO values: `observed/assigned`.
- A/B common configuration and chiral vibration: `systematics/model interpretation`.
- A/B absolute matrix-element equality: `not measured`.
- D/E mixing and F four-quasiparticle identity: `analogy/prior-model interpretation`.
- `N=57` lower border: `provisional author systematics`.

## Knowledge Impact and Learning Decision

- Effect: `supports` a `104Ag` candidate and collective-mode coexistence map, while `limits` confirmation and lower-border wording.
- Persistence: create source, nucleus, experiment, A/B candidate, D/E electric-rotation and F magnetic-rotation pages; update the chirality project.
- Review state: all `W13-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **W13-10 — source-language conflict.** Decide whether any downstream prose may quote the local “true chiral partners” phrase; default status remains candidate.
- **W13-5/7/11 — configuration/shape/model scope.** Keep inherited configuration and γ-soft analogy separate from new experimental facts.
- **W13-8/9 — ratio and alignment semantics.** Do not rewrite fingerprints as absolute partner-band matrix-element equality.
- **W13-12 — low-N border.** Preserve “candidate census + more data required,” not a physical exclusion boundary.

### P2/P3

- P2: verify parenthesized spin/parity labels before precision reuse.
- P3: audit band C particle/hole notation directly against the printed formulas if a separate C page is later needed.

## Related Knowledge and Project Relations

- [[104ag-bands-a-b-chiral-doublet-candidate]], [[104ag-bands-d-e-electric-quadrupole-rotation]], [[104ag-band-f-magnetic-rotation]].
- [[ciae-hi13-104ag-b11-50mev]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `wang_2013_Highspinlevel` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2013_Wang et al_High-spin level structure of the doubly odd nucleus 104 Ag.pdf`.

## Day18 更正审计：A/B 对齐原图、寿命报告范围与跨核类比边界

checkpoint047 重新核对本文全部 9 页主线、Table I 和 Fig. 4–5，并按 Fig. 5 的频率定义及 Harris 参考从 Table I 能级独立复算。原 raw SHA256 `366246ACEC6C6B5A46169606B125683BBD58C9D512A980A3910E5B23D837039C` 匹配。此前 `WS13-D18-1` 的复合结论已被本节取代；原 W13 与 AR claims、frontmatter 和 review 标记均保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WS13-D18-1 | **superseded / 更正**：撤回此前关于 A/B 出现约 3 ℏ 高自旋对齐落差、全核无寿命、邻核结果已证伪 104Ag，以及实测四极矩下降的复合断言。旧脚本输出不能验证这些断言；以下原子化条目给出重新核查的范围。 | evidence-correction | superseded | 本节 WS13-D18-2–7；旧 Day18 复合 claim | true |
| WS13-D18-2 | Fig. 5 实际绘出的 A 带对齐点覆盖 I=10–18，B 带覆盖 I=11–15；在共同的 I=13–15 区域两曲线相近。原图没有 B 带 I=16 或 18 的对齐点，不支持用这些自旋构造约 3 ℏ 带间落差。 | derived-observable | direct | PDF p.7 / 024306-7, Fig. 5；p.6 对齐讨论 | true |
| WS13-D18-3 | 使用 Table I 能级与 Fig. 5 的 Ix=√[I(I+1)−K²]、中心频率定义，取 K_A=8、K_B=10 及 J0=7、J1=15 的 Harris 参考，独立复算得到 I=13/14/15 的 A/B 对齐约为 7.492/7.516、8.159/8.314、8.922/8.456 ℏ；这是能级派生重建，不是新增组态或寿命测量。 | task-reconstruction | derived | PDF pp.3–4, Table I；p.7, Fig. 5 caption | true |
| WS13-D18-4 | 作者用本核能量、S(I)、跃迁比和对齐特征及多个邻核类比提出 A/B 手征解释；106Ag 的 Joshi 2007（Ref.17）是其中一个类比。p.6 局部称 “true chiral partners”，但摘要和总结仍称 candidate，不能将该引文链单独视为确证或证伪。 | author-interpretation | direct | PDF pp.1,5–6,8；Refs.11,13,15,17 | true |
| WS13-D18-5 | 本文未报告 A/B 带的寿命或分别标定的绝对 B(M1)、B(E2)；其 Fig. 4 给出比值指纹。本文的报告范围不能支持“104Ag 全核、全部后续文献均无 DSAM/RDDS 寿命”的穷尽断言。 | evidence-boundary | source-scope | 全文；PDF p.6, Fig. 4 | true |
| WS13-D18-6 | 旧脚本自行取 β=0.18/0.12 并用 A=104、Z=47 的轴对称线性 Q0 公式得到约 2.039/1.360 eb；这些 β 与 Q0 不是本文实测 Qt，也不是本文导出的 2qp/4qp 形变。比值 2.25 是所选 Q0 比的平方；β/Q0 比为 1.5，不能称“形变下降 2.25 倍”。 | calculation-boundary | task-self-audit | 旧 day18_wang13_104ag_chiral_boundary_audit.py 的输入/公式；本文无对应数值 | true |
| WS13-D18-7 | Bark 2024 §6 回顾了 106Ag 的寿命、对齐可加性及模型支持的 2qp/4qp 解释，并指出同期其它解释；本次未取得或原读其所引 Lieder 2014 primary。该邻核案例可提示检验路线，不能据此推断 104Ag 的同类结构已被证伪。 | cross-source-boundary | review-reported-and-inference | Bark 2024 PDF pp.22–23 / 24302-22–23, §6；非 Wang 2013 实测 | true |

必要 companion 为 [[bark-2024-investigations-nuclear-chirality-ithembalabs]] 的上述定向范围；其综述不能替代所引 primary。旧分析合同与结果仅作为历史运行记录保留，其固定 `passed` 不代表四项科学核查通过。本节保留候选解释和后续直接来源缺口，不授课程学分，也不升级任何 review 状态。
