---
type: source
title: "Garg et al. 2015 - Negative-parity high-spin states and possible magnetic rotation in 135Pr"
aliases: [Garg 2015 135Pr magnetic rotation]
created: 2026-09-21
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: experiment-and-TAC
reading_depth: deep-read
title_original: "Negative-parity high-spin states and a possible magnetic rotation band in 135Pr"
authors: [Ritika Garg, S. Kumar, Mansi Saxena, Savi Goyal, Davinder Siwal, Sunil Kalkal, S. Verma, R. Singh, S. C. Pancholi, R. Palit, Deepika Choudhury, S. S. Ghugre, G. Mukherjee, R. Kumar, R. P. Singh, S. Muralithar, R. K. Bhowmik, S. Mandal]
journal: "Physical Review C"
year: 2015
volume: 92
pages: "054325"
doi: "10.1103/PhysRevC.92.054325"
citation_key: Garg_2015
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Garg et al., Phys. Rev. C 92, 054325 (2015)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf"
raw_sha256: "c74e7c12614cf405861c639194e132f3096d5f46d22062b0164fa166282b9e88"
nuclei: [135Pr]
reactions: [123Sb-16O-4n]
experiments: [INGA, RDCO, IPDCO]
models: [tilted-axis-cranking, 3qp-5qp-configuration]
observables: [negative-parity-band, M1-E2, signature, crossing, polarization, DCO]
methods: [gamma-gamma-coincidence, DCO, linear-polarization]
tags: [135Pr, magnetic-rotation, TAC, high-spin, M1-E2]
---

# Negative-parity high-spin states and possible magnetic rotation in `135Pr`

## Bibliographic Record

- R. Garg *et al.*, *Phys. Rev. C* **92**, 054325 (2015), DOI `10.1103/PhysRevC.92.054325`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf`。

## Scope and Reading Depth

- PDF pp.054325-1–9 fully read: `123Sb(16O,4n)` experiment, INGA matrices, level scheme, RDCO/IPDCO, Table I, alignments/crossing plots, TAC 3qp/5qp comparison and conclusion.
- Not covered: raw events and later lifetime measurements.

## Key Results

- About `3×10^8` triple-and-higher γ coincidences were recorded with 15 INGA clovers. A negative-parity `ΔI=1` band with new crossover E2 transitions was established; RDCO/IPDCO assigned M1/E2 and E2 character for many links (PDF pp.1–4, Table I, Fig.1).
- The band shows strong M1 transitions, small/medium E2 crossovers and a crossing in alignment/energy behavior. TAC calculations use a 3qp `πh11/2⊗νh11/2^-2` configuration for the lower band and a 5qp `πh11/2(g7/2)^2⊗νh11/2^-2` configuration above the crossing (PDF pp.5–9, Figs.4–6).
- The authors call the band a possible magnetic-rotation band. Relative `B(M1)/B(E2)` ratios are already reported; lifetimes and absolute strengths remain missing for this band (PDF pp.6–8, Figs.5/7 and conclusion).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA15-1 | `135Pr` negative-parity high-spin band has M1-dominated ΔI=1 links and new E2 crossovers. | experiment-result | direct | PDF pp.1–4, Table I | true |
| GA15-2 | TAC 3qp/5qp configurations reproduce the crossing/energy systematics and motivate a possible magnetic-rotation interpretation. | model-interpretation | mixed | PDF pp.5–9 | true |
| GA15-3 | Without lifetimes/absolute strengths, the magnetic-rotation label remains possible rather than established. | limitation | direct | PDF pp.8–9 | false |

## Summary

Garg *et al.* provide an A≈130 high-spin magnetic-rotation candidate with multipolarity/polarization-asymmetry evidence, relative strength ratios and TAC configuration comparison. The authors identify future lifetimes as helpful for confirming the MR interpretation; this paper does not report the band's absolute strengths.

## Competing Interpretations and Limitations

- Strong M1/weak E2 patterns can also reflect signature/configuration mixing or core rotation; TAC fits are not unique.
- The 3qp→5qp crossing and possible MR identity depend on configuration assignments and alignment reference.
- No DSAM/RDDS lifetimes or absolute transition probabilities are provided in this source; a magnetic-rotation claim should not be upgraded beyond candidate level.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GA15-AR-1 | Assignment chain | Coincidence scheme → RDCO/IPDCO/δ → M1/E2 links and negative-parity band identity. | PDF pp.2–4, Table I | self-checking |
| GA15-AR-2 | MR chain | Alignment/crossing + M1/E2 pattern → TAC 3qp/5qp comparison → possible MR ranking. | PDF pp.5–9 | self-checking |
| GA15-AR-3 | Missing discriminator | Lifetimes would supply absolute B(M1) and B(E2); relative B(M1)/B(E2) is already reported. This is a limitation of the present source, not a universal MR rule. | PDF pp.6–8, Figs.5/7 and conclusion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[magnetic-rotation]], [[tilted-axis-cranking]], [[multipole-mixing-ratio]], [[linear-polarization-asymmetry]] and the A≈130 magnetic-rotation candidate map.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `GA15-P0-1`: Retain “possible magnetic rotation” wording and missing-lifetime boundary; do not promote a TAC-supported candidate to established MR.

## Extracted Pages

- Concepts/methods: [[magnetic-rotation]], [[tilted-axis-cranking]], [[multipole-mixing-ratio]], [[linear-polarization-asymmetry]]。


### Day16 原表与采集身份复核

2026-10-19 本session完整重读9页Sections I–IV/全部references，视觉核Table I及Figs.1–8。以下数字明确是2015 original版本：Crossref和INSPIRE已核有同篇2019勘误 DOI [10.1103/PhysRevC.100.069901](https://doi.org/10.1103/PhysRevC.100.069901)，但本run未取得勘误正文。不能把旧Table I写成已核最新更正值，更不能从Lv二手描述猜改了哪些计数/系数。失败访问和2019body readiness另存；原2015 PDF/hash、旧claims/review不改。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GA15-4 | 本实验为IUAC NewDelhi的82MeV123Sb(16O,4n)，800µg/cm²靶/Au backing10mg/cm²，15clovers距25cm；32/57/90/123/148°各3/2/4/2/4，约3×10^8 fold≥3。不是Matta的80MeV TIFR/INGA采集。共同反应/INGA名称不证明同一事件或所有nuisance独立。 | actual-acquisition-identity | direct | 054325-1 SecII | true |
| GA15-5 | 原RDCO是I_target148(gate90)/I_target90(gate148)。TableI的上标Q/D只标gate为quadrupole/dipole，未逐target列exactgate全表。原经验约1/.4及.8/2依本角组/gate，不能作普适阈值。 | DCO-role-and-gate-contract | direct | 054325-3 Eq1/前后；TableIcaption | true |
| GA15-6 | 原Δ=(aN⊥−N∥)/(aN⊥+N∥)，a=N∥unpol/N⊥unpol由target位置Eu152 singles取得，reported约.93(.06)。polarizedtarget来自90°clover与allarray gate矩阵。a是仪器几何不对称修正，不是Compton Q(E)或已经测得P。 | calibration-and-observable-layer | direct | 054325-3 Eq2；054325-4 Eq3/后段 | true |
| GA15-7 | original TableI747.5的RDCO=.25(.01)Q、Δ=−.05(.03)，813.3为.22(.02)Q、−.20(.08)，作者标M1+E2但本paper未给两线有符号δ数值。755.3只列DCO=.46(.04)Q，无Δ；不能扩张成第三条已测P。 | historical-original-target-values | direct-original2015 | 054325-2 TableI/对应Ei1478.2/2204.4/3000.4 | true |
| GA15-8 | 相同transition身份需spin/path：747.5是17/2−→15/2−、813.3是21/2−→19/2−；对应Matta747.0/812.8及Lv747.3/813.2是带版本的能标别名。不同R/Δ/P/response不合并成一个likelihood。 | versioned-transition-crosswalk | original-and-cross-source-identity | TableI；M15-4/5；L22-4 | true |
| GA15-9 | 2019erratum的题名/作者/原文关系已由Crossref、INSPIRE material=erratum核；APS401/403、contenthostDNS、直接arXiv0及MCP无有效全文，当前只metadata。不能由2015负Δ或XUNDL复制旧值推断勘误内容或最新物理结论。 | correction-readiness | externally-verified-metadata-only | DOI10.1103/PhysRevC.100.069901 | true |
| GA15-10 | 固定old2015计数比时，r=N∥/N⊥=a0(1−Δ)/(1+Δ)，a*=λa0给Δ*=[Δλ+Δ+λ−1]/[Δλ−Δ+λ+1]。747/813的central sign-zero a*分别1.027895/1.395。这只是旧表条件响应，不是恢复raw或实际勘误。 | conditional-calibration-transform | exact-algebra-and-old-rounded-input | Eq2；本页固定计数推导 | true |
| GA15-11 | 若附加单一globalλ/同旧counts且要求两target正、六条原M1标签线仍负，central需λ>1.5又λ<1.061856，无解。M1标签本身来自同观测，不是独立反证；这个小合同不排energy/gate-dependent修正、误差区间或原erratum真实处理。 | bounded-design-failure-control | actual-conditional-computation | TableI selected14rows；本页globalλ条件 | true |
| GA15-12 | 固定counts有∂Δ/∂ln a=(1−Δ²)/2；若把reported.06视共同σa，747/813单项σΔ约.03218/.03097，且跨线相关。quotedΔ是否已含该项/Cov未得，不能再次相加或拿两campaign差值直接作显著性。 | conditional-shared-calibration-Cov | derivative-and-propagation | Eq2/3；本页导数 | true |
| GA15-13 | Fig2的844 doublegate位于feeding以上，正文明确其谱不见某些sidebandfeeding；Fig3星号为污染线。这些coincidence图的gates不是已提供全部逐线polarizationgate/净counts ledger。 | companion-and-selection-boundary | direct | 054325-4/5 Figs2/3；054325-6 Band1 | true |
| GA15-14 | 本文Fig5/7展示derived B(M1)/B(E2)比，但无本实验寿命/absolute B(M1)，crossing之后又缺crossover而不能判其比值趋势。保留possibleMR及TAC模型层，不把强度比当绝对collectivity或新δ判决。 | strength-and-model-layer-boundary | direct | 054325-7/8；Figs5/7；Conclusion | true |

本run的计算仅用14个原TableI selected rows、originala≈.93及明确的fixed-counts条件；没有生成rawcounts或用freeα、Q去追Matta/Lv分支。单个globala修正的central sign要求失败说明response必须按实际对象恢复，不能据此认定2019作者错误，也不能替energy/gate-dependent处理写结论。新源[[nndc-2008-135pr-selected-mixing-records]]展示GargXUNDL-3仍为2015编译、旧Δ无MR，和Lv的P字段/2026的δ不同层。

`supports`A≈130真实reference/gate/data-identity审计；`limits`旧Δ当最新值、a当Q及跨campaign裸比较；`revises`project中“Garg original尚未单独核”的入口状态，只补实际已完成原读。未读erratum/rawresponse/Σ的缺口保持。原GA15-1–3 flags不变，新claims全needs_review。

[旧表条件程序](../../system/scripts/day16_garg2015_calibration_audit.py)actualexit0；[固定输入/结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/garg2015-calibration-audit-result.json)。参考[[135pr-mixing-branch-input-contract]]、[[135pr-wobbling-controversy]]、[[compton-polarimetry]]与[[dco-ratio]]。


### Ref32 actualprimary续接

[[palit-2000-rh99-clover-polarimetry]] P00-1–12实际原读补齐本文Ref32的方法入口：Eu a与polarizedreference Q的两层校准。原source单clovera≈1、C/D来自其特定数据/能区；本文a≈.93(.06)及未知Q/Cov仍独立保存，不以引用链搬入数值或替代2019勘误。

## Day25内Day26无学分preview：比值趋势与模型条件

checkpoint005独立代理回核PDF7–8；此处是既有原件定向核，不新增独立采集。GA15-3既有人审及GA15-9勘误body未得边界保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA15-D25P-A005-01 | 作者报告本带B(M1)/B(E2)上升至约35/2，非本档案曾要求的普适陡降；候选MR解释结合TAC配置与谱学。等长刚性双叶且忽略core的下降抛物线仅条件算例，不是该带实际拟合或身份硬门。 | direct-trend-and-model-domain | direct-original-plus-explicit-boundary | PDF7 Fig6 discussion | true |
| GA15-D25P-A005-02 | 结论称未来寿命可能有帮助，未规定只能薄靶反冲或必须few-W.u.加单调陡降才可确立。绝对B缺失须按本篇范围表述，旧相对B比不是不存在。 | author-limitation-and-nonuniversal-design | direct-original | PDF8 conclusion | true |

正式Day26仍未授分；此校准仅纠正已存在preview，不开下一张卡。数学模型不能凭比值演化代替本带时钟。

## Day26原件复核：带头、交叉与强度比的数据覆盖

本次重读PDF1–8主线，视觉核PDF7 Figs7/8；原2015文件/哈希不变，2019勘误正文仍未取得。以下仅认证2015原文的报告范围，不把旧表当最新更正值。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GA15-D26-001 | Table I给3530.0-keV态27/2−，149.5-keV线27/2−→25/2(−)；正文取约3531/150。此处是带低端身份，不是5qp交叉点。 | experimental-report-and-identity | direct-original2015 | printed054325-2 Table I; -7 Band3 | true |
| GA15-D26-002 | 作者给135Pr交叉ℏω≈0.37 MeV、I≈33/2−，并与137Pr约0.42 MeV、35/2−比较；3qp/5qp归属来自TAC。 | author-report-and-model-interpretation | direct-original2015 | printed054325-7/8 Figs5/6/8 | true |
| GA15-D26-003 | 作者报告比值升至约35/2−；交叉后crossover未见，因此明确说不能由B(M1)/B(E2)解释该交叉。旧“17/2到25/2从24.5降到8.0、27/2反弹到35/2的22.0”无本原件支持，撤回该轨迹。 | source-correction-and-coverage | direct-original2015 | printed054325-7 Fig7 and text; -8 first paragraph | true |
| GA15-D26-004 | 同母态强度比可在响应/分支与多极性假设下得到而不需绝对寿命；其变化不唯一给出B(M1)自身变化。本文缺绝对B，不能称比值不存在。 | observable-layer-boundary | direct-report-and-general-inference | Figs5/7; Table I; conclusion | true |

`revises` [[magnetic-rotation]] 的Day25伪数列；`supports` 按配置与数据覆盖限制单调性；综合见 [[octupole-mr-amr-evidence-gradient]]。不把本次纠错扩展成对其它MR核素或2019勘误的判决。

## Current correction source

The 2019 correction is recorded in [[garg-2019-135pr-polarization-erratum]]. For current multipolarity use, replace the old 813.3-keV `−0.20(8)` with `+0.04(3)` and the old 747.5-keV `−0.05(3)` with `+0.03(3)`; both are `M1+E2`. The erratum does not add absolute lifetimes or absolute B(M1), so the candidate MR interpretation remains bounded by the original source limitations.
