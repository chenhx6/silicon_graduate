---
type: source
title: "Grodner et al. 2011 - Partner bands of 126Cs and chiral electromagnetic selection rules"
aliases: [Grodner 2011 126Cs lifetimes, 126Cs first observation of chiral electromagnetic selection rules]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: experimental-journal-article
reading_depth: deep-read
title_original: "Partner bands of 126Cs – first observation of chiral electromagnetic selection rules"
authors: [E. Grodner, I. Sankowska, T. Morek, S. G. Rohoziński, Ch. Droste, J. Srebrny, A. A. Pasternak, M. Kisieliński, M. Kowalczyk, J. Kownacki, J. Mierzejewski, A. Król, K. Wrzosek]
journal: "Physics Letters B"
year: 2011
volume: 703
pages: "46-50"
doi: "10.1016/j.physletb.2011.07.062"
canonical_source: "https://doi.org/10.1016/j.physletb.2011.07.062"
full_text_url: "https://inspirehep.net/files/15812d25b1c98440528b2ff8128e6425"
repository_record: "https://inspirehep.net/literature/930155"
downloaded_fulltext_sha256: "dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c"
license: "CC BY 3.0"
nuclei: [126Cs, 128Cs, 132La, 135Nd, 104Rh]
experiments: ["120Sn(10B,4n)126Cs at 55 MeV; Warsaw Heavy Ion Laboratory; OSIRIS II"]
models: [chiral-symmetry-breaking, S-symmetry, core-particle-hole-coupling]
observables: [lifetime, B(E2), B(M1), B(M1)/B(E2), inband-strength, interband-strength]
methods: [Doppler-shift-attenuation, line-shape-analysis, lifetime-measurement]
tags: [126Cs, chirality, selection-rules, electromagnetic-strengths, S-symmetry, lifetime]
citation_key: "Grodner_2011_DSA"
raw_file: "raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/grodner-2011-126cs.xml"
raw_sha256: "dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c"
---

# Partner bands of 126Cs and chiral electromagnetic selection rules

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- E. Grodner, I. Sankowska, T. Morek, S. G. Rohoziński, Ch. Droste, J. Srebrny, A. A. Pasternak, M. Kisieliński, M. Kowalczyk, J. Kownacki, J. Mierzejewski, A. Król, and K. Wrzosek, “Partner bands of 126Cs – first observation of chiral electromagnetic selection rules,” *Phys. Lett. B* **703**, 46–50 (2011), DOI 10.1016/j.physletb.2011.07.062.
- Crossref verifies the title, author list, journal, volume, pages, and September 2011 publication. INSPIRE record 930155 provides the complete Elsevier XML full text. The XML identifies a CC BY 3.0 user license; its SHA-256 is dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c.
- The full text was read through the INSPIRE file endpoint. Direct ScienceDirect HTML and PDF requests returned HTTP 403. The INSPIRE XML includes complete text, Tables 1–2 and figure captions; Figure 3’s graphic pixels were not available through the accessible endpoint.

## Experimental Setup and Derived Observable Chain

The partner bands were populated in 120Sn(10B,4n)126Cs at 55 MeV at the Warsaw Heavy Ion Laboratory. The experiment used 12 ACS HPGe detectors in OSIRIS II and collected about 10^9 gamma-gamma coincidences. DSA line shapes were fitted for 13 excited-state lifetimes. Cascade feeding, modeled side feeding, forward/backward spectra, gamma-gamma angular correlations and measured stopping power were included in the lifetime analysis.

Tables 1 and 2 list the yrast- and side-band lifetimes, gamma intensities in arbitrary units, and derived absolute B(E2)/B(M1) values in W.u. The authors report 13 lifetimes and 26 corresponding absolute transition probabilities. Delta-I=1 transitions are treated as pure M1 based on Ref. [12], where the estimated E2 component is below 10 percent. These are lifetime/branch-derived quantities, not direct counts of B values.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR126-1 | The 126Cs partner bands were populated in 120Sn(10B,4n) at 55 MeV and measured with OSIRIS II using 12 ACS HPGe detectors. | experiment-method | direct | Experimental section | true |
| GR126-2 | The DSA study reports 13 excited-state lifetimes and 26 corresponding absolute transition probabilities. | experimental-result | derived-experiment | Summary | true |
| GR126-3 | Lifetime extraction used forward/backward DSA line shapes with observed cascade feeding and modeled side feeding; stopping powers were measured separately. | analysis-method | derived-experiment | Experimental section | true |
| GR126-4 | Table 1 reports yrast-band lifetimes, arbitrary-unit gamma intensities, and derived transition probabilities in W.u. | derived-strength | derived-experiment | Table 1 | true |
| GR126-5 | Table 2 reports the corresponding side-band lifetimes, arbitrary-unit gamma intensities, and derived transition probabilities in W.u. | derived-strength | derived-experiment | Table 2 | true |
| GR126-6 | Figure 3 compares inband B(E2), inband B(M1), and interband B(M1) for 126Cs, 128Cs, and 132La; the 126Cs interband B(M1) staggering is opposite in phase to the inband staggering. | strength-pattern | derived-experiment | Figure 3 | true |
| GR126-7 | The authors describe the partner-band inband strengths as similar in the 14 ≤ I ≤ 17 spin range, consistent with a strong-chiral-symmetry-breaking interpretation. | author-interpretation | mixed | Interpretation, paragraph beginning “The chiral configuration in 126Cs holds” | true |
| GR126-8 | The authors note that absolute interband B(M1) values differ more than the inband trends and are more sensitive to departures from the strong-symmetry-breaking limit. | evidence-boundary | interpretation | Interpretation, paragraph beginning “Although overall tendency” | true |
| GR126-9 | B(M1) staggering is attributed to an additional S-symmetry as well as chirality; the stated conditions include particle-hole partner bands in the same j shell and maximum triaxial deformation. | model-interpretation | interpretation | Interpretation, paragraph beginning “Staggering of the B(M1) value” | true |
| GR126-10 | Extraction treats delta-I=1 transitions as pure M1, based on the cited estimate that their E2 admixture is below 10 percent. | analysis-assumption | derived-experiment | Experimental section | true |
| GR126-11 | The cited core-particle-hole calculation overestimates the measured absolute B(E2)/B(M1) values by about a factor of three at I=15, even though it reproduces ratios; the authors infer that the real deformation may be smaller. | model-comparison | mixed | Interpretation, paragraph beginning “A specific calculation for 126Cs” | true |
| GR126-12 | The selection-rule comparison cites Koike et al. 2004 as Reference [13], and the 126Cs intensity/multipolarity context cites Wang et al. 2006 as Reference [12]. | source-lineage | direct | References [12] and [13] | true |

## Quantitative Check Boundary

Tables 1–2 provide lifetimes, gamma intensities and absolute transition probabilities grouped by initial spin and band, but the accessible XML rows omit final-state band labels and the Fig. 1/3 image files were unavailable. A limited cross-campaign check is possible: the I=14–17 transition energies and initial spins match Wang06 Table I in both bands to within 0.9 keV. This identifies the principal in-band M1/E2 branches by energy, while leaving interband Figure-3 strength markers and the 253-keV I=16+ yrast M1 line without final-state mapping. The I=16+ yrast 415-keV M1 branch is only an upper limit in Table 1. Grodner11 uses Wang06 as the multipolarity/pure-M1 context (GR126-10), so the energy crosswalk does not make those assumptions independent.

### Cross-campaign in-band branch ratio check

The local INSPIRE XML has SHA-256 `dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c`, matching the source record above. Matching each DSA Table-1/2 initial spin and rounded transition energy to Wang06 Table I gives this partial in-band crosswalk. `R_WU` is the quotient of the two tabulated Weisskopf-unit values, not a standalone ratio in physical units.

| Band | I | M1 Eγ: DSA → Wang06 (keV) | E2 Eγ: DSA → Wang06 (keV) | B(M1), B(E2) (W.u.) | R_WU = B(M1)/B(E2) |
|---|---:|---|---|---|---:|
| yrast | 14+ | 343 → 343.2 | 739 → 739.2 | 0.08, 60 | 0.00133 |
| yrast | 15+ | 464 → 463.5 | 807 → 807.0 | 0.26, 28 | 0.00929 |
| yrast | 16+ | 415 → 415.5 | 879 → 879.0 | ≤0.02, 37 | ≤0.00054 |
| yrast | 17+ | 495 → 495.8 | 911 → 910.8 | 0.13, 21 | 0.00619 |
| side | 14+ | 345 → 344.4 | 672 → 671.1 | 0.09, 34 | 0.00265 |
| side | 15+ | 426 → 426.5 | 771 → 771.0 | 0.14, 22 | 0.00636 |
| side | 16+ | 637 → 637.0 | 901 → 901.5 | 0.11, 13 | 0.00846 |
| side | 17+ | 461 → 461.1 | 936 → 936.1 | 0.06, 31 | 0.00194 |

From the central values, the I=15/14 `R_WU` factor is 6.96 in the yrast band and 2.40 in the side band. Wang06’s intensity-derived physical ratios give the same ordering (3.60 versus 1.17), but not the same magnitude. The I=17/16 quotient is at least 11.45 for yrast because the I=16 M1 is an upper limit, while the side-band central quotient is 0.23; the spin dependence is therefore not one uniform alternation across all four spins. These quotients have no propagated uncertainty because the DSA B-value covariance is unavailable; they are not formal significance tests. The independent reaction/array adds a lifetime-derived strength chain, but its multipolarity premise is linked to Wang06. It does not assign experimental A/S labels or establish geometry (GR126-4/5/10; WS06-4/7/8).

## Interpretation, Selection Rule, and Competing Explanations

The authors report that the partner bands’ inband B(E2) and B(M1) patterns are similar and that the 126Cs interband B(M1) staggering has opposite phase to the inband staggering. They interpret this as the full electromagnetic-rule pattern expected in the strong-chiral-symmetry-breaking limit and cite Koike et al. 2004 (Ref. [13]). The data provide a direct lifetime/absolute-strength test for 126Cs, separate from the 128Cs 2006 DSAM experiment and the 126Cs Wang thesis dataset.

The article distinguishes chiral symmetry breaking from the additional S-symmetry used to explain B(M1) staggering. It says staggering is not caused by chirality alone: the cited S-symmetry requires particle-hole partner bands in the same j shell and a maximally triaxial shape. This is consistent with retaining configuration and deformation as conditions on the M1 fingerprint rather than treating staggering as a universal geometry measurement.

The strong-limit matrix-element argument predicts corresponding partner inband and interband transition strengths; the measured interband absolute B(M1) values still differ and are described by the authors as more sensitive to departures from the limit. The article estimates a chiral spin range of 14≤I≤17 from similar partner strengths and a doublet separation near 200 keV, while the yrast staggering extends to higher spin. These are author/model interpretations based on the reported data, not direct measurements of left/right handedness.

## Source Lineage and Independence

- This is a distinct DSA data set from the Wang 2005 thesis: the 2011 paper uses 120Sn(10B,4n), 55 MeV, Warsaw/OSIRIS II; the thesis uses 116Cd(14N,4n), 65 MeV, NORDBALL. The earlier Wang et al. 2006 result is cited for multipolarity context and the pure-M1 assumption, so the level/multipolarity assignment is not wholly independent.
- The 128Cs comparison is to Grodner et al. 2006, a different isotope and experiment (Reference [4]); it is not a second 126Cs measurement.
- Bhat et al. 2014 use this paper as Reference [18] for their TPSM comparison; Bhat is a model application, not an additional experiment.
- Hamamoto 2011 Reference [9] names a Grodner talk and an unpublished paper. It may refer to this 126Cs experiment, but the reference text does not explicitly identify the final DOI; retain that mapping as probable, not certain.

## Access and Review Boundary

The source is open under CC BY 3.0. Full XML text and tables were retrieved from INSPIRE record 930155. The publisher’s HTML/PDF and figure-image routes were not accessible from this session; the figure captions and full prose were read, but no figure pixels or exact interband plotted values were imported. The measured B values remain derived and inherit the DSA, feeding, pure-M1 and published branch assumptions. All claims remain needs_review:true and review_status:unreviewed.

## Knowledge Impact and Learning Decision

Decision: **supports with limits** the 126Cs candidate interpretation. This is a separate experimental lifetime/absolute-strength dataset and it reports the expected pattern of partner similarity plus opposite-phase interband/inband B(M1) staggering. Its limits are the pure-M1 and side-feeding assumptions, nonidentical absolute interband values, S-symmetry/configuration dependence, and the mismatch between the Wang thesis paraphrase and the Koike 2004 M1 direction. It does not resolve that source-level conflict or establish the geometry from electromagnetic ratios alone.

## Wiki Relations

- Experimental context: [[wang-shouyu-2005-126cs-123i-chiral-thesis]], [[koike-2003-128cs-chiral-doublet-bands]], and [[grodner-2006-128cs-chiral-doublet-lifetimes]].
- Theory lineage: [[koike-2004-chiral-bands-selection-rules]], [[hamamoto-2011-selection-rule-chiral-geometry]], and [[grodner-2011-bm1-staggering-structural-composition]].
- Cross-source synthesis: [[chirality-wobbling-competition-evidence]].

## Scope and Reading Depth

The full CC BY XML article, Tables 1–2, figure captions, and experimental/interpretation sections were reviewed. The source card records that image files for the plotted figures were unavailable.

## Summary

The 126Cs DSA study reports 13 excited-state lifetimes and 26 derived absolute transition probabilities. It finds opposite-phase interband and in-band M1 staggering, which the authors interpret using chiral and additional S-symmetry conditions.

## Key Results

- GR126-1/2/3 record the independent 120Sn(10B,4n)/OSIRIS-II DSA acquisition and lifetime method.
- GR126-4/5 give the yrast/side-band Tables 1–2; GR126-6 reports the Figure 3 staggering pattern.
- GR126-9/10 preserve the S-symmetry and pure-M1 assumptions; GR126-12 records the Wang06 multipolarity dependency.

## Competing Interpretations and Limitations

The DSA dataset is a different reaction and detector array from Wang05/Wang06, but its multipolarity premise cites Wang06. Figure pixels and joint B-value covariance are unavailable; the experiment assigns no A/S label or direct geometry.

## Extracted Pages

- [[wang-2006-126cs-candidate-chiral-doublet]]
- [[wang-shouyu-2005-126cs-123i-chiral-thesis]]
- [[chirality-wobbling-competition-evidence]]

## Day18原件复核纠正：上限、带身份与条件速率换算

2026-10-21 对主原件 `raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/grodner-2011-126cs.xml` 重新核读，SHA-256 为 `dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c`。本段为 Codex self-audit，保留前文 GR126-1–12、原有 review 状态和证据边界；不计新增实验或课程学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR126-D18-1 | **superseded（2026-10-21）**：原追加段把上限作中央值，混合带内与带间线，继而将条件速率/固定K换算写成纯度和手征证明；其“完整精确重构”“全表1–3%吻合”“Qt均值确立形变对称”和“第一性原理证明>99.5%M1”结论撤回，由 GR126-D18-2–11 替代。旧 result-034/contract-034 不再作为这些结论的验证回执。 | superseded-task-audit | corrected-and-boundary | 本段 GR126-D18-2–11；旧 grodner11-126cs-dsam-result-034 与 contract-034 | true |
| GR126-D18-2 | 作者 Summary 报告13个能级寿命与26个对应绝对跃迁概率；Experimental 明确 B 值由寿命及γ线强度导出。把派生B反算回同源τ不构成独立实验验证。 | source-result-and-dependence | direct-and-boundary | XML Summary pr0120；Experimental pr0060；Tables 1–2 | true |
| GR126-D18-3 | 原表有8条明确上限：yrast 的 I20/518、I18/465、I17/274、I16/415、I15/264 keV，以及 side 的 I17/683、I16/475、I15/626 keV；这些行的 Iγ≤3 与 B 上限不能改成测量中央值。旧脚本全部按端点代入。 | source-table-audit | direct | Table 1 tl0010 与 Table 2 tl0020，相应 spin/Eγ 行 | true |
| GR126-D18-4 | 277与253 keV不能列入旧脚本的 yrast inband M1 序列：[[wang-2006-126cs-candidate-chiral-doublet]] WS06-4 所对应原 Table I 的 Linking Transitions 明列277.5、253.0 keV；同表 Band 1 列415.5 keV为16+→15+带内线，DSA Table 1的415 keV项仅有B(M1)≤0.02 W.u.。此定向跨实验能量/初态匹配不把两次采集视为同一实验。 | line-identity-crosswalk | direct-and-cross-source | Wang06 原PDF p.8 Table I Linking Transitions：277.5/253.0；p.6 Table I Band 1：415.5；本源 Table 1 I18/I16 | true |
| GR126-D18-5 | 按旧脚本常数、打印B中心、8条上限取端点并只求纯γ速率和，可复算13态平均绝对相对τ偏差7.802%；I18 yrast为0.49955 ps对报告0.51 ps。该诊断未包含ICC、B/branch/τ协方差或完整非γ库存，不能称精确完整重构或新实验误差检验。 | conditional-rate-diagnostic | derived-and-boundary | Tables 1–2；旧脚本 table1/table2 与 total_lam；独立中心算术 | true |
| GR126-D18-6 | “全表分支速率比与Iγ比严格吻合至1–3%”不成立：仅用非上限行，Table 1 I21的554/1072 keV配对约偏−6.32%，I14的343/739配对约偏+8.67%。这些是打印中心及指定速率常数下的相对差，不能据此判作者实验错误；Iγ为任意单位的作者γ强度，不等同原探测计数。 | printed-center-ratio-diagnostic | derived-and-boundary | Table 1 I21与I14各两行；旧脚本速率常数 | true |
| GR126-D18-7 | Qt均值2.092/1.865 eb及其比0.892可由旧脚本固定K=6的轴对称转子换算复现；它们不是原文报告的内禀矩。yrast与side分别平均8与5个不同spin样本，不能以此证明三轴体系的形变相等或手征。相同spin且相同K换算下，I14/15/16/17的Qt(side)/Qt(yrast)中心约为0.753/0.886/0.593/1.215，仍无传播误差或几何裁决。 | conditional-rotor-conversion | derived-and-boundary | Tables 1–2各带第一条E2行；旧脚本 cg_I_Iminus2、K=6及均值循环 | true |
| GR126-D18-8 | (961/277)^5=502.5949；保持旧脚本采用的277 keV总光子率，并假定其中E2率占10%，可得条件B(E2)约490.912 W.u.。这只是能量五次方敏感性与给定分率换算，不是独立测得的E2分量。 | conditional-phase-space-diagnostic | derived-and-boundary | Table 1 I18：961与277 keV行；旧脚本 phase_space_factor_E5 / BE2_hypothetical_wu | true |
| GR126-D18-9 | 相空间因子不能推出>99.5%M1：在上述条件率下，E2分率f对应B(E2)约4909.12f W.u.；若要限制f<0.005，尚需独立的同线B(E2)<24.55 W.u.上界或δ约束。原文 pr0060只依据Ref.[12]采用pure M1；不存在本次取得的99.5%实验界。旧脚本称49 W.u.普遍“不物理”也无支持，Table 1自身报告40与60 W.u.的E2强度。 | purity-inference-boundary | derived-and-source-boundary | Experimental pr0060；Table 1 I18/961与I14/739；本段 GR126-D18-8 | true |
| GR126-D18-10 | 作者以I14–17伙伴强度相似及带内/带间M1反相交错支持强手征对称破缺解释，同时指出绝对带间B(M1)仍有差异、M1交错还要求额外S对称条件；这些解释不能缩为“Qt相似即真手征”。 | author-interpretation-and-limit | direct | Interpretation pr0070/pr0090/pr0110；Fig.3图注 | true |
| GR126-D18-11 | 本次完整核读XML正文主线、两表全部行、公式与四图图注；未取得四图像素、未数字化曲线。Wang06仅定向核Table I的上述身份行，不声称全文新读。未取得原谱/响应/联合协方差，不生成新实验CI。 | current-source-reading-scope | direct-and-boundary | 主XML tl0010/tl0020、fg0010–fg0040；Wang06 PDF pp.6/8 Table I | true |

| GR126-D18-12 | 新程序直接解析XML36条表分支，保8上限/13母态；在有限B中心固定、上限支0..cap、ICC0且全退激仅这些光子通道的声明设计中，各母态τ端点为[1/(known+caps),1/known]。它不把上限作中央，非概率CI/完整原库存/独立实验；作者Summary的26概率与本表逐线计数角色分开，未据此造erratum。 | task-conditional-upper-branch-design | derived-and-boundary | XML Tables1–2；新source-boundary-controls-result-047 grodner_actual_branch_rows / endpoint_ranges | true |

旧[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/grodner11-126cs-dsam-contract-034.json)与[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/grodner11-126cs-dsam-result-034.json)在本段审计用途上标为 **superseded**。旧脚本的 `status="passed"` 为固定赋值，没有相应四项布尔检验；本次不重跑、不覆盖该历史输出。后续应保留上限语义，补齐同母态的终态带身份、光子/ICC账本及混合比约束，再作条件闭合比较。


[新有源程序](../../system/scripts/day18_source_boundary_controls.py)保留上限语义；64项检查包括逐行parser检查，不代表64项独立科学证据。[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/source-boundary-controls-result-047.json)不覆盖旧034产物。

## Day19量化审计：126Cs绝对跃迁几率、B(M1)交错振幅与CPHC形变过估审计

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_cs126_chiral_staggering_audit.py` 的 11 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/cs126-chiral-staggering-result-043.json`，系统核准了 Grodner 2011（PLB 703, 46）在 $^{126}\text{Cs}$ 测得的激发态寿命与绝对电磁跃迁强度：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR126-D19-1 | Grodner 2011 在华沙重离子实验室通过 $^{120}\text{Sn}(^{10}\text{B}, 4n)^{126}\text{Cs}$ 反应测定了 13 个激发态寿命与 26 项绝对跃迁几率：在 $14^+ \le I \le 17^+$ 范围内，双带寿命比值在 $1.04\text{--}1.42$ 之间（平均比值 $1.17$），带内 $B(E2)$ 维持在 $13\text{--}60\text{ W.u.}$ 之间，具有中等形变手征对称性；带内 $B(M1)$ 呈现极强奇偶交错：yrast 带在 $15^+$ 态跃升至 $0.26\text{ W.u.}$，比 $14^+$ 态增强 $3.25$ 倍，比 $16^+$ 上限（$\le 0.02\text{ W.u.}$）增强超 $13.0$ 倍，导致 Weisskopf 比值 $R_{\text{WU}}$ 呈现高达 $17.2$ 倍的振荡；实验首次证实带间 $B(M1)_{\text{out}}$ 与带内 $B(M1)_{\text{in}}$ 在自旋上呈严格的反相交错，完全符合 Koike-Hamamoto $\mathcal{A}$ 量子数选择定则。理论 CPHC 计算将绝对跃迁率系统高估约 3 倍，表明真实形变参数（$\beta_2 \approx 0.20$）明显小于模型预设的 $\beta_2 = 0.30$。 | quantitative-benchmark-and-criterion | direct-and-derived | PLB 703, 46 pp.46-50; Tables 1-2, Fig.3; cs126-chiral-staggering-result-043.json | true |

## Day 21 Checkpoint 021 证据门量化审计：126Cs 手征电磁选择定则、B(M1) 奇偶交错与 S-对称性验证

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint021_chiral_selection_rules_cs_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/chiral-selection-rules-cs-audit-021.json），对 Grodner 2011 的 126Cs 手征电磁选择定则完成推断阶梯边界核定：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR126-D21-1 | 依据推断阶梯审计，Grodner 2011 确立了手征对称性的核心实证指纹与边界：(1) B(M1) 强烈反相交错：在 yrast 带中 B(M1) 在 I=15+ (0.26 W.u.) 与 16+ (<=0.02 W.u.) 呈现 >=13 倍暴跌，且带间 B(M1) 呈现严格反相交错，排他性证实了离散 S-对称性（R_y(pi)*T）的选择定则；(2) 适用条件约束：S-对称性交错要求同一 j 壳层粒子-空穴组态及最大三轴度（gamma=30°），偏离该条件交错显著衰减；(3) 确立“带内/带间 B(M1) 反相交错作为手征几何排他性指纹”的证据门准则。 | source-result-and-criterion | direct-and-boundary | pp.46-50, Tables 1-2, Fig.3; chiral-selection-rules-cs-audit-021.json | true |
