---
type: source
title: "Nandi et al. 2020 - First Observation of Multiple Transverse Wobbling Bands of Different Kinds in 183Au"
aliases: [Nandi 2020 183Au multiple transverse wobbling]
created: 2026-07-16
updated: 2026-11-27
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "First Observation of Multiple Transverse Wobbling Bands of Different Kinds in 183Au"
authors: [S. Nandi, G. Mukherjee, Q. B. Chen, S. Frauendorf, R. Banik, Soumik Bhattacharya, Shabir Dar, S. Bhattacharyya, C. Bhattacharya, S. Chatterjee, S. Das, S. Samanta, R. Raut, S. S. Ghugre, S. Rajbanshi, Sajad Ali, H. Pai, Md. A. Asgar, S. Das Gupta, P. Chowdhury, A. Goswami]
journal: Physical Review Letters
year: 2020
volume: 125
pages: 132501
doi: 10.1103/PhysRevLett.125.132501
canonical_source: https://doi.org/10.1103/PhysRevLett.125.132501
citation_key: nandi_2020_FirstObservation
raw_file: "raw/papers/2020_Nandi et al_First Observation of Multiple Transverse Wobbling Bands of Different Kinds in.pdf"
raw_sha256: 3981DC7A1A1EA109C167D60A0B8FB6B0A8B0B7667D00C61D6AA34572C042F511
nuclei: [183au]
reactions: ["169Tm(20Ne,6n)183Au"]
experiments: []
models: [particle-rotor-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, transverse-wobbling, multiple-wobbling, shape-coexistence]
---

# Multiple transverse wobbling bands in `183Au`

## Bibliographic Record

PRL 125, 132501 (2020), DOI `10.1103/PhysRevLett.125.132501`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, INGA experiment, two parity families, DCO/polarization, mixing ratios, `E_wob`, PRM/HFA and shape-coexistence interpretation.
- Not covered: independent CDFT/PRM reproduction or older band-assignment sources.
- Coverage caveats: shape coexistence is inferred through configuration-dependent wobbling/model results, not measured by an independent shape observable.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test whether two parity/configuration families in `183Au` can host different transverse-wobbling bands and clarify whether E_wob must always decrease (PDF pp.1-2).

## Method and Design Logic

- Establish positive/negative-parity band links, determine E2/M1 character with DCO and polarization, map E_wob versus spin, and use PRM/HFA turning-spin behavior to interpret both families (PDF pp.2-5, Figs.1-5).

## Key Evidence and Reasoning Chain

- Large-E2 wobbling links versus low-δ signature links → band-role separation; opposite E_wob slopes → spin intervals on different sides of I_m; model mapping → two TW candidates and inferred shape coexistence.

## Summary

The paper reports two one-phonon transverse-wobbling candidates based on `πi13/2` and `πh9/2` configurations. It emphasizes that transverse `E_wob` may first rise and later fall, so a decreasing trend is not claimed as universally necessary.

## Experimental or Theoretical Setup

`169Tm(20Ne,6n)183Au` at 146 MeV with the VECC K-130 cyclotron, thick 23 mg/cm² target and eight-clover INGA.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NA20-1 | Positive- and negative-parity yrast/side-band pairs were connected by `ΔI=1` transitions and assigned `πi13/2` and `πh9/2` families. | experimental-fact | direct | PDF pp.2-3, Fig.1 | true |
| NA20-2 | Combined `R_DCO` and polarization fits yield large-E2 links for the proposed wobbling bands and low-`δ` M1 links for associated signature-partner bands. | experimental-criterion | direct | PDF pp.3-4, Fig.2 | true |
| NA20-3 | Negative-parity `E_wob` decreases with spin, while positive-parity `E_wob` increases over the observed range. | experimental-fact | direct | PDF p.4, Fig.3 | true |
| NA20-4 | PRM/HFA calculations introduce a turning spin `I_m`, allowing the transverse mode to rise below and fall above it. | model-result | direct | PDF pp.4-5, Figs.3-5 | true |
| NA20-5 | Authors suggest both side bands are transverse wobbling and present the positive-parity case as the first observed increasing branch of TW. | author-interpretation | indirect | PDF p.5, Summary | true |
| NA20-6 | Authors infer triaxial shape coexistence from wobbling candidates built on two parity/configuration families. | author-interpretation | indirect | PDF p.5 | true |

## Nuclear Structure Information

Two parity families are assigned πi13/2 and πh9/2 configurations with separate yrast/side-band pairs. Their measured link character is stronger evidence than the inferred coexistence of two triaxial shapes.

## Authors' Interpretation

The authors interpret both side bands as transverse wobbling and infer triaxial shape coexistence; the positive-parity increasing-E_wob branch is framed as below the model turning spin.

## Model Results

PRM/HFA reproduce the slope reversal through I_m. Configuration assignments, δ branches and deformation inputs remain dependencies rather than direct shape measurements.

## Competing Interpretations and Limitations

The “shape coexistence” conclusion is more model dependent than the measured transition character. Multiple band families do not alone prove two stable triaxial minima; independent lifetimes/shape observables would strengthen it.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| NA20-AR-1 | Core reconstruction | Transition character is primary, while the sign of the E_wob slope depends on the observed spin interval relative to the model turning spin. | Key Results and Competing Interpretations above | unreviewed |
| NA20-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| NA20-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| NA20-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| NA20-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| NA20-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Transition character is primary, while the sign of the E_wob slope depends on the observed spin interval relative to the model turning spin.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| limits | [[transverse-wobbling]] | Adds model-conditioned increasing-before-decreasing `E_wob`. |
| limits | [[triaxial-shape-coexistence]] | Candidate wobbling families support but do not independently prove shape coexistence. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- P0: none identified.

### P1

- `NA20-1`/`NA20-2`, Fig.2 — Review configuration assignment and δ branch separation between wobbling and signature links. Evidence: DCO/polarization fits; Agent inference: wrong family assignment would undermine both TW cases.
- `NA20-4`/`NA20-6`, Figs.3-5 — Review the turning-spin explanation and whether two candidates justify shape coexistence. Agent inference: the energy-slope revision is model-conditioned and the coexistence claim is not an independent shape measurement. Risk: the model-dependent coexistence conclusion may be overstated.

### P2/P3

- P2: exact population and transition-value transcription. P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[183au]]
- Concepts: [[transverse-wobbling]], [[triaxial-shape-coexistence]]
- Methods: [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

Keep “clear experimental evidence” and “first observation” attributed to the authors.

## 2026-11-27 — 馆藏原件与覆盖核对

- {"range": "1–2", "sections": "出版信息、摇摆能谱公式、TW 惯量条件、INGA 实验及部分谱图和能级图（第2页图1）"}
- {"range": "3–4", "sections": "带间跃迁及 δ（第3页图2）、E_wob 未编号公式与实验趋势（第3页正文、第4页图3）、跃迁几率比、PRM 输入与 HFA 转折自旋（第4页图4及表 I）"}
- {"range": "5–6", "sections": "归一化 HFA 对照（第5页图5）、横向摇摆与形状共存解释、致谢、作者脚注及参考文献"}
- 本次获取的具体覆盖：通读物理第1至6页的提取文本，包括正文、未编号公式、表 I、图1至图5的图注与提取标签、致谢和文献 [1] 至 [35]。五幅图的图注均可读，原图待核。正文实读范围与 Wiki 的既有范围相符，建议接受同版全文覆盖，更新下列证据归类及定位。逐项图证据仍待核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 作者报告新增 14 条 γ 射线并建立带（6）。对 DCO 比和线偏振的联合比较给出，带（3）→（2）及（5）→（4）的 ΔI＝1 跃迁约有 90% E2 分量，带（1）→（2）及（6）→（4）的相应跃迁约有 1% E2 分量。 | 实验报告 | source-reported | 物理第2页图1及第3页图2和正文。能级连接、拟合分支和混合比字形待核第2、3页。 | true |
| A17-2 | 由实测能级按相邻 yrast 态均值扣除式求得的 E_wob，在各自观测区间内随自旋对正宇称带上升、对负宇称带下降。 | 实验能级导出量 | source-reported | 物理第3页未编号的 E_wob 公式及正文，第4页图3(a)、(b)。实验点和两面板的轴尺度待核第4页。 | true |
| A17-3 | PRM 采用 CDFT 形变输入和能谱拟合惯量，对比观测区间的 E_wob 和由 γ 强度求得的跃迁几率比，并高估 B(M1out)/B(E2in)。HFA 以拟合惯量估算正、负宇称组态的转折自旋分别为 16.5ℏ 和 7.5ℏ，归一化曲线将两组数据分别置于上升段和下降段。 | 模型结果 | source-reported | 物理第3至4页模型正文，第4页图3、图4和表 I，第5页图5。惯量列、转折值及归一化比较待核第4、5页。 | true |
| A17-4 | 作者沿用 πi13/2 正宇称与 πh9/2 负宇称组态指认，结合带间跃迁、准粒子取向与模型，将带（5）和（3）均解释为横向摇摆，并将两个组态上的摇摆带视为三轴形状共存的证据。 | 作者解释 | source-reported | 物理第3页带指认和文献 [18]，第4页表 I，第5页图5及结论。组态映射和图例待核第3至5页。 | true |

VECC K-130 以 146 MeV 的 20Ne 束轰击 23 mg/cm² 的 169Tm 靶，经 169Tm(20Ne,6n)183Au 反应布居。INGA 使用八台克洛弗 HPGe 和两台平面 HPGe LEPS，记录 1.5×10⁹ 个二重及以上符合事件。组态沿用文献 [18]，PRM 使用 CDFT 形变及能谱拟合惯量，HFA 采用谐振与冻结取向近似。

- 将 NA20-1 拆成实验建立的 ΔI＝1 连接（第2页图1、第3页正文）和沿用文献 [18] 的组态指认（第3页正文），分别标注证据属性。
- 将 NA20-2 的图2定位改为物理第3页，将方法表述细化为实测 DCO 比和线偏振与不同 δ 下的计算值联合比较。
- 将 Wiki 的“PRM/HFA reproduce the slope reversal through I_m”改为“PRM 对比两个实测区间的能量趋势和跃迁比，HFA 估算转折自旋并给出归一化的上升、下降分支”。
- 物理第2页图1的能级与箭头标签在提取时交叠。第3页图2曲线旁的混合比字形抽取为 G，逐值引用前按原图核定。第1、3页公式的等号和括号有抽取乱码，第4页配对公式根号断行，第5页图5组态前缀抽取为 S/Q。公式及图例的逐字转录分别核对上述物理页。
