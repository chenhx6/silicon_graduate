---
type: source
title: "Chakraborty et al. 2024 - Exploring the possibility of wobbling motion in 129Ba"
aliases: [Chakraborty 2024 129Ba wobbling possibility]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article-reanalysis
reading_depth: deep-read
title_original: "Exploring the possibility of wobbling motion in 129Ba"
authors: [S. Chakraborty, S. Bhattacharyya, G. Mukherjee, C. Majumder]
journal: Physical Review C
year: 2024
volume: 110
pages: 024324
doi: 10.1103/PhysRevC.110.024324
canonical_source: https://doi.org/10.1103/PhysRevC.110.024324
citation_key: chakraborty_2024_Exploringpossibility
raw_file: "raw/papers/2024_Chakraborty et al_Exploring the possibility of wobbling motion in Ba 129.pdf"
raw_sha256: D5729DE577067F8AFEAB771AFB51328989772C68962A938D553BCCB50F0C0808
nuclei: [129ba]
reactions: []
experiments: []
models: [triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, wobbling-energy, signature-splitting]
methods: [angular-distribution, dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, reanalysis, wobbling-possibility, longitudinal-wobbling, a130]
---

# Exploring the possibility of wobbling motion in `129Ba`

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

PRC 110, 024324 (2024), DOI `10.1103/PhysRevC.110.024324`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, reanalysis of published angular-distribution/polarization coefficients, band reassignment, TPRM/QTR calculations and explicit limitations.
- Not covered: original raw spectra/data or independent reanalysis of the 1977/1992 source papers.
- Coverage caveats: no new experiment is reported; the conclusions inherit uncertainties and incomplete transition coverage from older datasets.

## Paper Question and Scientific Motivation

- Author-explicit motivation: reassess legacy `129Ba` band data to determine whether band 3 may be a wobbling excitation rather than only a signature/TiP-like structure (PDF pp.1-2).

## Method and Design Logic

- Reanalyse published angular-distribution, DCO and polarization coefficients; revise band roles; compare energy staggering/E_wob with `127Xe`; use TPRM/QTR calculations while explicitly requesting new data (PDF pp.2-4, Figs.2-7).

## Key Evidence and Reasoning Chain

- Legacy 365-keV coefficient overlap → substantial E2 admixture; incomplete other links → weak electromagnetic closure; energy/model analogy → “likely/possibility” wobbling, not observation.

## Summary

This paper explores, rather than claims definitive observation of, wobbling in `129Ba`. It reassigns the yrast `13/2−` sequence as a likely first-wobbling-phonon band and calls for new measurements before an unequivocal conclusion.

## Experimental or Theoretical Setup

No new dataset. The analysis revisits results from `120Sn(12C,3nγ)129Ba` at 52 MeV and `116Cd(18O,5nγ)129Ba` at 86 MeV, including angular distributions, DCO and limited polarization.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH24-1 | Reanalysis of the 605-keV band-2→band-1 link gives a low mixing ratio and supports band 2 as unfavoured signature partner. | author-interpretation | indirect | PDF pp.2-3, Figs.2-4 | true |
| CH24-2 | Published 365-keV angular-distribution and polarization values overlap at adopted `-0.84≤δ≤-0.79`, indicating a substantial E2 admixture for band 3→1. | experimental-criterion | indirect | PDF p.3 | true |
| CH24-3 | Other relevant links lack sufficient angular/polarization information; some DCO ratios are only suggestive. | experimental-fact | direct | PDF p.3 | true |
| CH24-4 | Similar energy staggering to `127Xe` and increasing `E_wob` are used to support a longitudinal-wobbling possibility. | author-interpretation | contextual | PDF pp.3-4, Figs.5 and 7 | true |
| CH24-5 | TPRM reproduces bands 1/2 as signatures and QTR/FA reproduces band 3 energy trend with longitudinal coupling. | model-result | direct | PDF pp.3-4, Figs.5-7 | true |
| CH24-6 | Authors conclude band 3 is likely first-phonon wobbling, but explicitly require further angular-distribution/correlation and polarization measurements for unequivocal establishment. | author-interpretation | indirect | PDF p.4, Summary | true |

## Nuclear Structure Information

Bands 1/2 are treated as signature partners and band 3 as a possible first-wobbling-phonon sequence. No new spectra or raw-event reanalysis are supplied.

## Authors' Interpretation

The authors deliberately retain possibility/likely wording and state that new angular/polarization measurements are required for unequivocal establishment.

## Model Results

TPRM describes signature bands and QTR/frozen-alignment calculations reproduce the proposed band-3 trend. The model comparison inherits old-data and cross-nucleus assumptions.

## Competing Interpretations and Limitations

Signature partner, TiP and wobbling are discussed. The article argues TiP E2 fractions are smaller than the adopted 365-keV value, but this is a cross-case model/experiment comparison, not a direct exclusion. Old data and incomplete links keep the conclusion at “possibility/likely.”

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| CH24-AR-1 | Core reconstruction | This is a reinterpretation of legacy observables plus model calculations; no new direct experiment is added and the conclusion remains possibility/likely. | Key Results and Competing Interpretations above | unreviewed |
| CH24-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| CH24-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| CH24-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| CH24-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| CH24-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: This is a reinterpretation of legacy observables plus model calculations; no new direct experiment is added and the conclusion remains possibility/likely.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[longitudinal-wobbling]] | Provisional `129Ba` candidate based on reanalysed legacy data. |
| competing-interpretation | [[tilted-precession-bands]] | TiP is discussed but not tested with a nucleus-specific common-input analysis. |
| limits | [[multipole-mixing-ratio]] | Demonstrates how old angular-distribution branches affect a modern reassignment. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `CH24-2`, 365-keV link, PDF p.3 — Evidence: adopted δ=-0.84 to -0.79 comes from overlap of legacy angular-distribution/polarization results. Agent inference: the modern reassignment depends on old coefficients and branch conventions. User check: original datasets, signs and uncertainty overlap. Risk: revised δ would change the key E2 argument.

### P1

- `CH24-4`/`CH24-6`, Figs.5-7 — Evidence: energy analogy and models support “possibility/likely,” while other links remain incomplete. Agent inference: no new experiment establishes wobbling. User check: preserve possibility/likely wording and assess TiP comparison. Risk: upgrading to observation would exceed the source.

### P2/P3

- P1: legacy band identity and TPRM/QTR assumptions. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[129ba]]
- Concepts: [[longitudinal-wobbling]]
- Methods: [[angular-distribution]], [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

Do not upgrade “possibility/likely” to “observation.”

## 2026-10-17当前使用更正：现代重分析不是历史采用区间

**数值引用以本节CH24-7为准；旧CH24-2把历史采用值误归给本篇现代分析。**本次对照原5页PDF，hash `d5729de577067f8afeab771afb51328989772c68962a938d553bccb50f0c0808`匹配；完整重读主线、references，并视觉核Fig1–7及关键p3文字。旧human review record、CH24-1–6的true标记及全部原正文保留为历史；新内容为Codex self-audit，不在人审范围内。

printed024324-3左栏先回顾Gizon旧工作：AD区间−.97至−.79、P区间−.84至−.31、历史采用−.84至−.79。紧接着正文与p2 Figs2/3给**本篇重分析**的χ² minimum δ≈−2.0，radiative E2 contribution80(4)%。旧CH24-2所写“Published...overlap at adopted−.84≤δ≤−.79”不能当本篇新的数值结果，不能继续以这个历史值计算现代E2分数。

本次又取得同第一作者的[单页arXiv v3](https://arxiv.org/abs/2108.05313v3)，版本日期2024-04-09，题名为“On the multipole mixing ratio of the365keV gamma-transition in129Ba”。它也用同Gizon摘要给δ≈−2.0(2)。两文本有共享实验输入/论证，不构成两场独立采集；未声明单作者preprint就是四作者PRC的逐字VoR。arXiv早期2021日期和v2 withdrawal历史不应套成v3正文年份/内容。

两现代文本都没有在当前页提供完整可重放的primary coefficient-correction/布居/finitegeometry/Σ输入。本任务的明确chosen最大取向reference内部F/photon计算一致，但未重现其black curves；原件1977/1978的coeff层尚未取得，不以自由调sigma/alpha/C来配作者−2.0。故“作者报告80%”与“本任务已独立重算真实实验δ=−2.0”必须区分。

单页v3的独立source identity见[[chakraborty-2024-ba129-365-mixing-ratio-arxiv-v3]]，选定评价对象见[[nndc-2014-129ba-365-coefficient-records]]；它们的locator和数据依赖不合并成一份新实验。

具体数据谱系、条件计算边界和新source identity见[[ba129-365-mixing-reference-boundary]]。本次只更正数值归属及可复现性合同；作者对wobbling仍是possibility/likely，并要求新数据。高E2 fraction本身不使TiP/其它解释在所有configuration中自动被排除。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CH24-7 | 本篇现代365keV重分析给δ≈−2.0、80(4)%radiativeE2；−.84至−.79是该段回顾的历史采用值。旧CH24-2归属错误由本行supersede，原review/flag不变。 | numerical-attribution-correction | direct-and-self-audit | printed024324-3 leftcolumn paragraphs1–3；printed024324-2 Figs2/3 | true |
| CH24-8 | 重分析输入A22=−.70(.03)、A44=.16(.05)、P=.072(.068)引自Gizon旧数据；Fig2/3/4和本篇/单页v3的派生比较不增加实验独立性。 | data-lineage-and-summary | direct | printed024324-3 quotedobservables；printed024324-5 Refs26/27 | true |
| CH24-9 | 521/671仅A22、缺A44，作者明确不能提供completeinformation；其小DCO/大负A22只是mixedδ/E2提示，不能各自作为完整δ测量。 | missing-companion-boundary | direct | printed024324-3 paragraphfollowingmodern365fit；Fig4 | true |
| CH24-10 | TPRM的ε2=.22/γ=33.5°用于bands1/2；QTR/FA与J3>J1,J2支持作者的longitudinal解释，不是γ发射alignmentσ或独立的E2混合比测量。 | model-parameter-layer-boundary | direct | printed024324-4 Fig6/7 discussion | true |
| CH24-11 | 同δ=-2.0±.2的fraction换算给中心.80、局部sigma.032，端点.82877/.76415；作者80(4)%保留印值，非新的测量或完整CI。旧AD−.88(.09)给.43643/约.05031，为另一历史派生值。 | radiative-fraction-definition-check | task-calculation-from-source | printed024324-3 modernδ/fractionparagraph；本任务fractionworksheet | true |
| CH24-12 | 自设maxalignmentM±1/2单gamma参考在13/2→11/2的F/photon投影控制通过，但其A2/A4根不重现本篇图线；本篇未给完整producer/原coeff-correction层，不能据此判作者错误或调α后宣称已重放实验。 | bounded-reproduction-readiness | task-calculation-and-source-scope | printed024324-2 Figs2/3；printed024324-3；本任务referenceboundary | true |
| CH24-13 | 从公开评价取同母态461.6 E2参考作独立条件control时，rank4 spinratio为−8/3；实际positiveA4摘要不能在未核samepostselection/coeff/purity/geometry前被强行当source的共同rho校准。它限制本次replay readiness，不否定作者80%或证明实验错误。 | companion-reference-readiness | task-calculation-and-evaluated-premises | Fig1的同母态branches；N129L643.6/G364.7/G461.6；本任务rank4proof | true |

## Day18 checkpoint053修订：现代重分析多极根敏感性与偏振统计边界

原CH24-claims保持；旧CH24-D18-1降格为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH24-D18-1 | **superseded**：旧关于“边缘显著性偏振下挑选大解的唯象重解释”降格，由CH24-D18-14/15分层记录作者对历史数据的重分析与多极根敏感性。 | task-correction | superseded-interpretation | 本段D18-14/15；旧chakraborty24-129ba-wobbling-result-025 | true |
| CH24-D18-14 | 本文对Byrne 1986/Gizon 1977历史365 keV数据进行现代chi2极小拟合，报告大解delta ~ -2.0(2)（80% E2）为最佳拟合解，并将其与历史采用解delta in [-0.84, -0.79]（~40% E2）和反事实小解delta ~ -0.33(3)（~9.8% E2）对比，展现了不同根对应的多极成分差异。 | source-result-and-method | direct | PDF p.3 Figs. 2-3；Sec. III | true |
| CH24-D18-15 | 历史线偏振测量值P = 0.072(68)相比于零的偏离为Z = 1.06sigma；作者据此提出大解在正偏振方向具有吻合性，并结合TPRM计算讨论纵向摆动可能性，明确要求未来高精度绝对测量予以检验。 | author-interpretation-boundary | direct-and-boundary | PDF p.3 Fig. 3；Sec. IV | true |
| CH24-D21-1 | **superseded（checkpoint042）**：旧大根由模型偏好主观挑选之断言与既有 CH24-D18-14/15 更正冲突；现代作者报告 chi2 最佳解，缺原 producer/Σ不能重裁。历史采用区间中点不是新测 -0.815(25)；P/sigmaP 对零的显著性不是两根判别。脚本衰变率漏 e²/(4πε0) 单位因子，b=.65 与1–500 ps任设，绝对B及摆动阈值撤回。 原review/needs_review保持；旧passed不认证来源、实验或CI。 | task-correction | superseded-scientific-certification | checkpoint042撤回记录 | true |

## Day 21 checkpoint038 修订状态

旧段落的逐字快照保存在本run的 superseded-042/chakraborty-2024-possibility-wobbling-129ba.txt。其科学认证撤回：旧大根由模型偏好主观挑选之断言与既有 CH24-D18-14/15 更正冲突；现代作者报告 chi2 最佳解，缺原 producer/Σ不能重裁。历史采用区间中点不是新测 -0.815(25)；P/sigmaP 对零的显著性不是两根判别。脚本衰变率漏 e²/(4πε0) 单位因子，b=.65 与1–500 ps任设，绝对B及摆动阈值撤回。


## Day21 checkpoint046：现代拟合归属与E2率的单位修复

冻结已primed回忆后，本轮新读PRC全部5页文字，视觉核PDF pp.2–4 Figs.1–7/χ²图及结论；同时定向核LKH82 printed p.121 Eqs.2.1–2.6原页。raw SHA256与页码见本run `e2-unit-scope-046.json`。原page-level human-reviewed是2026-07-25历史审核，本节属于新的Codex自审；不改变原record、review_status或claim needs_review。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH24-D21-R46-1 | 本文现代AD联合轮廓/χ²报告δ≈−2.0与80(4)%E2；−.84至−.79为历史采用区间。本文说A22单独允许约−2.0或−.33，而A22/A44联合在报告不确定度内支持大模解；本轮没有重建black curves、联合Σ或原producer，不能改称作者仅按模型偏好挑根。 | author-fit-and-reproduction-boundary | direct-original | printed 024324-3 left-column modern-fit paragraph | true |
| CH24-D21-R46-2 | p.3明确521/671缺A44，不能给complete information；p.4结论likely并要求新AD/correlation/polarization。p.3与135Nd TiP的E2份额比较是跨核解释，不能当129Ba全部TiP构型的排他实验检验。 | missing-companions-and-interpretation | direct-original | printed 024324-3 paragraph after modern-fit result | true |
| CH24-D21-R46-3 | 本文重用Byrne1992/Gizon1977/1978数据，未在本次核读的5页中给365keV绝对寿命/光子branch/完整拟合Cov。因此δ²/(1+δ²)的radiative份额不能单独变成绝对B(E2)；旧任设b=.65与τ=1–500ps范围不能冒充实验误差域。 | rate-identifiability-boundary | source-scope-and-task-inference | printed 024324-5 Refs.25–27 | true |

### 原率公式到现代单位：仅作方法复算

依据[[lange-kumar-hamilton-1982-multipole-admixtures]]的LKH82-1及printed p.121 Eq.2.2，统一SI时对电多极率显式加入1/(4πε0)。NIST 2022 CODATA常数在线表 https://physics.nist.gov/cuu/Constants/Table/allascii.txt 于本轮实际HTTP200获取，快照/hash见本run `nist-constants-046.txt`、`nist-retrieval-046.json`。使用exact h/e/c及所列ε0，推得E2系数约1.22519×10^9 s⁻¹ MeV⁻⁵/(e²fm⁴)；独立以αℏc的核单位路线一致。这里系数是本任务由原定义与常数换算，不是本文印出的新实验数值。

对于M1/E2光子截断，定义f_E2=δ²/(1+δ²)、q_line_gamma为每次母态衰变在此线发一个光子的绝对概率，τ为母态平均寿命，则B(E2)[e²b²]≈0.0816202 q_line_gamma f_E2/(τ[ps] Eγ[MeV]^5)。若输入为含内转换的total branch，且该pair仅M1/E2与相应IC，才可用q=b_total/(1+α_mix)；相对γ强度不能直接代q，半衰期亦不能直接代mean τ。旧038代码省略了e²在高斯单位下的energy×length因子，且使用任设branch/τ；其B/W.u.数值与模式阈值保持撤回。

程序`system/scripts/day21_checkpoint046_e2_units.py`只检两套单位路线与b²/fm⁴转换；实际129Ba B输出为null。可同时按比例缩放允许的M1/E2部分率而保持δ不变，故仅凭δ不识别绝对尺度。没有建立真实寿命域时，500倍只是自设扫描跨度，不能叫实验不确定度或据此排除wobbling。下一高信息输入是同母态寿命、绝对分支/IC与matching响应/共同Cov；其它核的绝对B不能借来补空。
