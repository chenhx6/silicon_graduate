---
type: source
title: "Construction and use of a three Ge(Li) Compton polarimeter"
aliases: ["Butler 1973 three GeLi polarimeter", "Three-Ge(Li) Compton polarimeter"]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "CONSTRUCTION AND USE OF A THREE Ge(Li) COMPTON POLARIMETER"
authors: ["P. A. Butler", "P. E. Carr", "L. L. Gadeken", "A. N. James", "P. J. Nolan", "J. F. Sharpey-Schafer", "P. J. Twin", "D. A. Viggars"]
journal: "Nuclear Instruments and Methods"
year: 1973
volume: 108
pages: "497-502"
doi: "10.1016/0029-554X(73)90530-2"
citation_key: Butler_1973
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Butler, P. A. et al. Construction and use of a three Ge(Li) Compton polarimeter. Nucl. Instrum. Methods 108, 497-502 (1973)."
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1973_Butler et al_Construction and use of a three Ge(Li) Compton polarimeter.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1973_Butler et al_Construction and use of a three Ge(Li) Compton polarimeter.pdf"
raw_sha256: "1d19589bd41fb0b28230a3cb76cf8c240fc5f7899b1bd50a1c288bcfb8a3e7c2"
nuclei: ["33S", "56Fe", "24Mg", "28Si", "12C", "26Al"]
reactions: ["30Si(α,n)33S"]
observables: ["linear-polarization", "polarization-asymmetry", "polarimeter-sensitivity", "peak-to-background", "figure-of-merit"]
methods: ["compton-polarimetry", "linear-polarization-asymmetry", "angular-distribution"]
tags: [three-GeLi, Compton-polarimeter, detector-calibration, 33S, spin-parity-assignment]
---

# Construction and use of a three Ge(Li) Compton polarimeter

## Bibliographic Record

- 作者：P. A. Butler 等。
- 期刊：*Nuclear Instruments and Methods* 108, 497-502 (1973)。DOI：`10.1016/0029-554X(73)90530-2`。
- 原始文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1973_Butler et al_Construction and use of a three Ge(Li) Compton polarimeter.pdf`；SHA-256：`1d19589bd41fb0b28230a3cb76cf8c240fc5f7899b1bd50a1c288bcfb8a3e7c2`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.497-502 全文；three-Ge(Li) apparatus、P/A/Q definitions、Compton/gamma gates、calibration Table 1、Q(E) interpolation、`33S` 4868-keV spin ambiguity application、Figs.1-6 和总结均已阅读。
- Not covered: 原始 event tapes、electronics response simulation 和引用论文全文。
- Coverage caveats: 1973 detector response is geometry/energy/threshold-specific；`33S` assignment is conditional on population and multipolarity assumptions explicitly described by the authors。

## Paper Question and Scientific Motivation

- 论文构建三 Ge(Li) Compton polarimeter，测定 `0.4-4.4 MeV` γ 线性偏振，并示范其如何解决 `33S` 4868-keV level 的 `7/2−` vs `11/2−` spin ambiguity（摘要；PDF pp.497,501）。

## Method and Design Logic

- 50 cm³ coaxial Ge(Li) 作为 scatterer，35/61 cm³ 两个 coaxial Ge(Li) 作为 `Q=0°/90°` absorbers；scatterer axis 与 beam 垂直，lead shielding 减少 direct radiation（PDF pp.497-498）。
- 原Eq1定义plane-axis P；Eq3的efficiency-corrected `A=(a(E)N⊥−N∥)/(a(E)N⊥+N∥)`，Eq4为`P=A/Q(E)`。旧Wiki额外`1−αA`分母不在原文，已纠正；source前冻结回忆的旧错保留追溯（printed497）。
- Compton kinematic `cos θ` gates 与 511-keV pair-production veto 减少背景；calibration 用已知 E2/E1 transitions 的 angular distributions 和 polarization（PDF pp.498-500，Table 1）。

## Key Evidence and Reasoning Chain

1. `cos θ` gates 把 `56Fe` 847-keV peak-to-background 从约 3 提升至 5，并在 `33S` 841-keV complex spectrum 把 improvement factor 从 4 提升至 7；pair-production veto 进一步改善高能数据（PDF pp.498-499）。
2. Table 1 calibration 给出 Q 约 `0.44` at 847 keV、`0.274` at 1368 keV、`0.235` at 1779 keV、`0.09` at 4430 keV 等，显示 sensitivity 随能量下降（PDF p.500）。
3. 拟合得到 `Q(E)≈0.84 Q′(E)`，其中 Q′ 是点散射/点探测器 Klein-Nishina estimate；finite detector size 造成约 16% 整体 sensitivity reduction（PDF p.501，式 (5)）。
4. 对 `30Si(α,n)33S` 4868-keV level，angular distribution 给出 `a2≈0.41`、`a4≈−0.27`，单独只能支持 `7/2` 或 `11/2`；偏振测得 `P(90°)=0.56±0.15`，与 χ² 和 pure-E2 constraint 联合后选择 `11/2−`（PDF pp.501-502，Fig.6）。

## Summary

三 Ge(Li) polarimeter 以独立 scatterer/absorber geometry 兼顾 energy resolution、Compton sensitivity 和 background rejection。作者通过已知偏振线标定 Q(E)，再用 `33S` 4868-keV level 演示 polarization 与 angular distribution 联合解决 spin ambiguity。该来源为现代 clover/segmented polarimeter 提供历史 detector-response baseline，尤其展示 kinematic gate、pair veto 和 calibration dependence。

## Experimental or Theoretical Setup

- Detector: 50 cm³ scatterer + 35/61 cm³ absorbers, absorber directions 0° and 90° relative to polarization plane。
- Calibration transitions: `56Fe`, `24Mg`, `28Si`, `12C`, `26Al`, `33S` known E2/E1 cases。
- Application: `30Si(α,n)33S`, `Eα=9.8 MeV`, 4868-keV level。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B73-1 | 三 Ge(Li) polarimeter 的 P/A/Q formalism 与 relative absorber efficiency correction 已建立。 | method-definition | direct | PDF pp.497-500，式 (1)-(3) | false |
| B73-2 | Kinematic `cosθ` gates 和 511-keV veto 显著改善 peak-to-background，尤其在复杂高能谱中。 | detector-result | direct | PDF pp.498-499，Figs.2-3 | false |
| B73-3 | Q(E) 从约 `0.44` at 847 keV 降到约 `0.09` at 4430 keV，且 `Q≈0.84Q′`。 | calibration-result | direct | PDF pp.500-501，Table 1，Fig.5 | false |
| B73-4 | `33S` 4868-keV level 的 polarization `P=0.56±0.15` 与 angular distribution 联合支持 `11/2−` assignment。 | experimental-criterion | direct | PDF pp.501-502，Fig.6 | true |

## Nuclear Structure Information

- 该来源主要是方法；`33S` 仅作为 spin-assignment demonstration，不能单独替代原始 spectroscopy source。
- 4868-keV state 的最终 assignment 依赖 population/substate and pure-E2 assumptions；本页保留 conditional language。

## Authors' Interpretation

- 三晶体 polarimeter 的高 resolution 和 Compton background control 使其适合复杂 high-spin spectra；polarization 能补足 angular-distribution spin ambiguity。

## Model Results

- 不适用；Q(E) interpolation 是 detector response calibration，不是 nuclear structure model。

## Competing Interpretations and Limitations

- `33S` assignment 对 population of first two magnetic substates and E2 assumption 敏感；不同 reaction alignment 可能改变 inference。
- Q(E) depends on detector volumes, scatter angle, absorber geometry, threshold and efficiency; no universal Q.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-B73-1 | Core reconstruction | 本文把 detector calibration、background gating 和 polarization/spin inference 连接起来，强调 response-first 分析。 | PDF pp.497-502 | self-checking |
| AR-B73-2 | Assumptions and dependencies | 依赖 known-P calibration, relative efficiency `a(E)`, reaction alignment, angular-distribution coefficients and multipolarity constraint. | PDF pp.499-502 | self-checking |
| AR-B73-3 | Transfer conditions | P/A/Q/gate logic transfers; Q values and 33S inference do not transfer without matched calibration. | PDF pp.497-502 | provisional |
| AR-B73-4 | Failure conditions | Background, pair production, finite detector response or unresolved substate population can change P and spin assignment. | PDF pp.498-502 | active-L3 |
| AR-B73-5 | Reverse/falsification test | Repeat 33S-like combined χ² with alternate substate populations, no-polarization branch and independent Q calibration lines. | PDF pp.501-502 | candidate-L3 |
| AR-B73-6 | Research-question decision | Historical calibration source for P/A/Q and combined spin assignment; no L4. | PDF pp.497-502 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki already has Compton P/A/Q and detector-response boundaries; this source adds three-crystal geometry, cosθ gating, pair veto and a concrete joint spin-assignment case.
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: It supports response-first linear-polarization analysis and shows why angular distribution alone can leave spin ambiguity.
- Persistence decision: update [[compton-polarimetry]] and [[linear-polarization-asymmetry]] source lists。
- Review state: `unreviewed`; method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[compton-polarimetry]] | Historical three-Ge(Li) scatterer/absorber calibration and background controls. |
| methodological-bridge | [[spin-parity-assignment]] | Joint angular-distribution/polarization χ² resolves a conditional spin ambiguity. |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | Adds early detector-response lineage to modern clover/tracking sources. |

## Human Review Triage

### P0

- B73-P0-1：`33S` `11/2−` assignment is conditional on reaction population and pure-E2 assumptions; do not state as unconditional without the source boundary。

### P1

- B73-P1-1：Q(E) and background-improvement ratios are detector-specific calibration values。

### P2/P3

- DOI and pages are aligned from PDF PII; no nucleus page created。

## Extracted Pages

- Nuclei: no standalone `33S` page。
- Bands: no band page。
- Concepts: Compton response, polarization calibration, spin ambiguity。
- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[spin-parity-assignment]]。

## Non-source Notes and Follow-up

- Next: compare B73 with Simpson HS-008 and Garcia-Raffi HS-009 in the detector-method project; continue HS-013.


## Day17原件自审：先效率修正，再以Q换算P

本session先冻primed回忆再完整原读6页/6图/表1/5式/16refs，hash1d19589bd41fb0b28230a3cb76cf8c240fc5f7899b1bd50a1c288bcfb8a3e7c2/578497bytes不变。旧B73-1–4行/falsefalsefalsetrueflags与reviewunreviewed保持，新增自审全needs_review；原法P/A/Q一般关系保，不把旧formula错说成作者非线性修正。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B73-D17-1 | 原P定义为电矢量在beam–γ平面内减normal的比，ComptonA为perp scatter减parallel scatter；不同detector先Eq3 A=(aNperp−Nparallel)/(aNperp+Nparallel)，再Eq4 P=A/Q。旧Wiki多出的1−alphaA分母不在原式，已修叙述；核alpha、effa、Q不能混。 | formalism-transcription correction | direct | p.497, Eqs1–4 | true |
| B73-D17-2 | a(E)由无偏振56Co(.8–3.5MeV)/66Ga(2–4.5MeV)测相对absorbereff，约1、accuracy1%；Eq3方向为a=Nu_parallel/Nu_perp。它是geometry/efficiency校准，不是polarimeterQ或已知P校准的同一量，实际Cov未给。 | independent-relative-efficiency input | direct and algebra | p.500 Sec2.3 | true |
| B73-D17-3 | scatterer50cm³、horizontal35cm³/vertical61cm³、axesvertical关系/7.5cmPb；2MeV平均ξ85°，Qprime却定义pointξ90°。实际4000/1000ADC校gain/zero后sum成5000channels，N由sumtotalpeak面积取，不是任意rawscatterADC或SG98twofoldcounts。 | geometry and actual-count observable | direct | pp.497–499 Sec2.2 | true |
| B73-D17-4 | cosξgate从actualscatter/absorberE筛物理几何域，另vetoabsorber511keV；source报告peakheight/background相对singles的Fe3/5、56Cosource8/13、33S4/7等对象不同。不是absoluteP/B=3/5，也非已测countretention/efficiency/FOM。 | gate-and-denominator distinction | direct | pp.498–499, Fig2 and Sec2.2 | true |
| B73-D17-5 | 4430单逃逸/全能面积比.6→.4、加两门称sensitivity在.8/4.4MeV升20/50%；无原gateacceptance/eventcounts，不由此补实验F或跨threshold迁移。 | detector-result and transfer-boundary | direct | p.499 Sec2.2 | true |
| B73-D17-6 | Table1七点P由AD+knownEM/近threshold布居计算，A同时测；p,p'用scatterersinglesmonitor，alpha,n用suitablespin1/2level作monitor，共归一/参考依赖。P列是predictedP，不是七个独立实测P去独立验证Q。 | calibration-provenance | direct | p.500 Table1 and Sec2.3 | true |
| B73-D17-7 | Table1的33SE1为Ex2935/Eg967；Fig3的2935-keV线是同Ex的groundbranch且P约−.6。不能把Ex2935当Table1校准γ能量，或同母态便转用另一支P/Q。 | parent-versus-photon-role boundary | direct | p.499 Fig3; p.500 Table1 33S E1 row | true |
| B73-D17-8 | 原Qfit=Qprime(CE+B)，E用MeV，C=0±.005MeV^-1、B=.84±.04；Qprime取pointKNξ90，B/C共Cov未给。C0仅令nominalQ/Qprime恒定，不令Q常量，±.04不是所有校准点独立error或整曲线CI。 | response-fit contract | direct | p.501 Eq5 and Fig5 | true |
| B73-D17-9 | 新七行A/印P重算Qcentral .44/.273737/.235417/.090909/.575758/.365854/.135802，与印Q小舍入差保；对应pointQprime的Q/Qprime约.775–.895，不重fit/删点强配B=.84，原Cov与unroundedinput未知。 | Codex actual-table arithmetic | derived | p.500 Table1 | true |
| B73-D17-10 | 将印a2/a4按已归一pureE2 point90公式作诊断，24Mg/12C给1.00672/1.05104，33S2971给.76938而印P.81。未取得原finiteangle/constraint/fitrecipe，保不闭合、不clipP/替authorP重标Q；不判原实验错误。 | point-transfer failure-control | derived conditional | p.500 Table1; p.501 Fig5 | true |
| B73-D17-11 | design-only Nperp6000/Nparallel4000/a1.01/Qfixed.44给A=.204771/P=.465389；原式Jacobian/finiteDifference/null/labelswap/scale核通过。自设Poisson独立counts与a1%时sigmaA_count=.009778、a=.004790、合=.010889，非原B73实验误差或CI。 | Codex count-error design | derived not measured | p.497 Eq3 | true |
| B73-D17-12 | Q=A/P的实际local传播需Cov(A,P)，而AD/P/Q同calibrationchain；新七行只列conditionaldiagonal及任意PSD二元Cov界，不从印σ反推实际Cov或claim重复实验。 | shared-calibration covariance-boundary | derived from source contract | p.500 Sec2.3 and Table1 | true |
| B73-D17-13 | 33S4868用Ea9.8、1933γ到2935(7/2−)，P.56±.15与AD只在假定仅absM1/2、3/2且11/2假设由lifetime排M3/pureE2、RBδ号/.1%CL合同下选11/2−。不是Psign独断spin或任意正population已排7/2；7/2→7/2的δ是E2/M1，11/2→7/2的δ是M3/E2，后一pureE2 δ0不可叫pureM1。Refs12/13/15当时tobepublished，body未取。 | inference and necessary-companion boundary | direct-author | pp.501–502 Sec2.4, Fig6 and references | true |
| B73-D17-14 | 本文无1977Ni实际job/门/硬件校准确认，WA77引用此装置只建立方法谱系；两文actualComptoncounts、完整response/Σ仍缺，不迁Q/a/33Sassignment或由此认证现代clovertracking。 | source-independence and readiness | synthesis from actual scopes | p.497 apparatus; p.500 calibration | true |

[七行原表/设计输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/butler1973-calibration-contract.json)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/butler1973-calibration-result.json)，script `system/scripts/day17_butler1973_response_audit.py`。Selfchosencounts与Poisson/a独立假设不替真实峰fit/背景subtraction/Cov。

令D=aNperp+Nparallel，则∇A=(2aNparallel/D²,−2aNperp/D²,2NperpNparallel/D²)，Var_localA=gᵀΣg。这里a误差为同校准跨γ共享量，若与N或Q共有输入须保交叉项；不是再引一个source未有的alpha分母。三GeLi的correctedcountasymmetry与clover相似字式不保证计数observable、门、geometry或Q可互换。

本次`revises`Wiki公式错、`limits`把predictedP当独立实验/把Ex当Eg及印表系数裸迁point；新旧sourceflags保持。关联[[wadsworth-1977-61ni-levels]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]与[[polarimetry-shared-calibration-count-design]]。
