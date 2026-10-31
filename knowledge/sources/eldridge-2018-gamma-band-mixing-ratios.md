---
type: source
title: "Eldridge et al. 2018 - E2/M1 mixing ratios from gamma-vibrational bands"
aliases: [Eldridge 2018 gamma-band mixing ratios]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "E2/M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational bands of 102,104,106,108Mo, 108,110,112Ru, and 112,114,116Pd"
authors: [J. M. Eldridge, B. Fenker, J. H. Hamilton, C. Goodin, C. J. Zachary, E. Wang, A. V. Ramayya, A. V. Daniel, G. M. Ter-Akopian, Yu. Ts. Oganessian, Yu. X. Luo, J. O. Rasmussen, S. J. Zhu]
journal: "European Physical Journal A"
year: 2018
citation_key: eldridge_2018_E2
volume: 54
pages: "15"
doi: "10.1140/epja/i2018-12426-5"
canonical_source: "Eldridge et al., Eur. Phys. J. A 54, 15 (2018)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf"
raw_sha256: "a244b7e49fb513f057119bce603c0790a5cf381bd7a909f9c2996d033e1439b7"
nuclei: [102Mo, 104Mo, 106Mo, 108Mo, 108Ru, 110Ru, 112Ru, 112Pd, 114Pd, 116Pd]
reactions: [252Cf-fission]
experiments: [Gammasphere, IPAC]
models: [gamma-vibrational-band, Greiner-proton-neutron-deformation]
observables: [E2-M1-mixing-ratio, g-factor, attenuation, gamma-band]
methods: [integral-perturbed-angular-correlation, gamma-gamma-angular-correlation]
tags: [gamma-band, mixing-ratio, IPAC, Mo, Ru, Pd, gamma-softness]
---

# E2/M1 mixing ratios from γ-vibrational bands

## Bibliographic Record

- J. M. Eldridge *et al.*, *Eur. Phys. J. A* **54**, 15 (2018), DOI `10.1140/epja/i2018-12426-5`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/振动/2018_Eldridge et al_E2M1 mixing ratios in transitions from the gamma vibrational bands to the ground state rotational b 1.pdf`。

## Scope and Reading Depth

- PDF pp.1–11 fully read: Krane–Steffen δ definition/convention, Greiner comparison, Gammasphere `252Cf` IPAC setup, attenuation/g-factor extraction, Tables 1–4, Figs.1–11, contamination controls and conclusions.
- Not covered: raw event files, the Goodin thesis and later evaluated level schemes.

## Key Results

- A `62 μCi 252Cf` source inside Gammasphere produced `5.7×10^11` triple-and-higher coincidences with 101 working HPGe detectors and 64 pair angles. IPAC angular correlations were fit with `W(θ)=1+G2A2P2+G4A4P4` (PDF pp.1–3, Eq.7).
- Ground-band `2+` g factors and attenuation factors were measured first. Average `G2,G4` were `0.78(6),0.6(2)` for `104–108Mo` and `0.85(6),0.7(2)` for `108–112Ru`; `102Mo` and Pd cases used near-unity corrections (PDF pp.3–4, Table 1).
- Across 37 γ-band→ground-band transitions in Mo, Ru and Pd, 30 (≈81%) are pure/near-pure E2 (`|δ|≥3`) within 1.5σ in `(A2,A4)` space, and all are compatible with pure/near-pure E2 within 3σ. Multiple δ branches, including `±∞` pure-E2 limits and very large opposite-sign solutions, are retained when the oval intersects the uncertainty region (PDF pp.4–9, Tables 2–4, Figs.4–10).
- The `102Mo` 1244.9-keV level is confirmed as a `3+γ` state from the unique angular-correlation oval. The sign trend of `δ(E2/M1)` changes around `110Ru`, supporting Krane's predicted shape transition, while Greiner's proton/neutron-deformation theory systematically underpredicts magnitudes and does not predict sign changes (PDF pp.3–10, Fig.11).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EL18-1 | γ-band→ground-band transitions in ten Mo/Ru/Pd isotopes are predominantly E2, with 37 measured δ values and explicit multi-branch uncertainty. | experiment-result | direct | PDF pp.4–9, Tables 2–4 | true |
| EL18-2 | The δ sign trend changes near `110Ru`, consistent with a model-predicted shape transition but not a direct γ-rigidity proof. | systematics-interpretation | mixed | PDF pp.9–10, Fig.11 | true |
| EL18-3 | IPAC attenuation/g-factor corrections are necessary and isotope/feeding dependent. | method-result | direct | PDF pp.2–4, Table 1 | false |
| EL18-4 | Greiner's model underpredicts δ magnitudes and cannot reproduce sign changes in this dataset. | experiment-model-conflict | mixed | PDF pp.9–10, Fig.11 | true |

## Summary

Eldridge *et al.* provide a large, cross-isotope γ-band mixing-ratio data set. The direct result is predominantly E2 decay from γ bands to ground bands; the shape-transition interpretation is a systematics/model layer, and IPAC ovals preserve branch ambiguity rather than forcing a single δ solution.

## Competing Interpretations and Limitations

- δ uncertainty is expressed in `(A2,A4)` space; a finite error oval may wrap around `δ=±∞`, allowing both signs or pure-E2 limits. A single numerical central value can hide this topology.
- IPAC depends on attenuation `Gk`, g factors, lifetimes, hyperfine fields and contamination/gates. Similar energies in fission partners required extra gates and can bias coefficients if not controlled.
- The Krane shape-transition comparison and Greiner theory are interpretations; a sign change in δ is not a standalone measurement of γ softness/rigidity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| EL18-AR-1 | IPAC chain | Detector-pair angular bins → `A2/A4` → attenuation correction from `g`/lifetimes → δ oval intersection. | PDF Eqs.5–9, Tables 1–4 | self-checking |
| EL18-AR-2 | Branch topology | Parameterized `A2,A4` oval can have two or unbounded δ branches; retain all within stated σ. | PDF pp.4–9, Tables 2–4 | self-checking |
| EL18-AR-3 | Shape transfer | δ sign/magnitude trend → model shape comparison only after common Krane convention and attenuation controls. | PDF pp.9–10, Fig.11 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-correlation]], [[gamma-soft-deformation]], [[gamma-band-energy-staggering]] and cross-isotope A≈130/neighbor shape diagnostics.
- New reusable rule: report δ as a branch set in `(A2,A4)` space; do not collapse `±∞` or opposite-sign solutions without a physical or independent constraint.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `EL18-P0-1`: Preserve IPAC attenuation/g-factor and δ-oval branch boundaries; the `110Ru` shape-transition interpretation is not a direct standalone observable.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-correlation]], [[gamma-soft-deformation]], [[gamma-band-energy-staggering]]。

## 2026-10-18 Day16独立复读：projective分支与共享衰减

先冻结primed预期，核原raw hash并完整重读11页主线、Eqs1–9/四表/11图及references，放大Tables1–4、Figs1/3/4/5/11与contamination段。当前metadata题名/13作者/EPJA54 article15与Crossref相符；source旧claims/review状态保持。本批只对明确选定104Mo行及一项correctioncontrol做计算，不声称37行都重拟合、全raw/DELTA producer已恢复。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| EL18-5 | 实际64pairanglebins先合17，再按cosθ对称合9；最多10个额外gate要求至少一个成立，是OR而非十门AND。额外门可来自本核或fissionpartner；这些selection/response不由单行spin序列自动恢复。 | experimental-selection-and-estimator | direct | PDF2–3 Sec2；Table2–4星号脚注 | true |
| EL18-6 | G2来自各核pure4→2→0的A2/理论值，G4由同phi模型计算后再组平均；104–108Mo用.78(.06)/.6(.2)，108–112Ru用.85(.06)/.7(.2)。这不是两个独立校准实验。Eq9对phi/g是偶函数，单凭IPAC衰减只给模，不在本任务补sign；G2>1中央无realphi需边界处理。 | shared-calibration-and-domain | direct-and-derived | PDF3 Eqs6/8/9；PDF4 Table1/text | true |
| EL18-7 | Table2的104Mo3gamma+→2+→0+、extra556/200*/478/331*，rawA2/A4=−.146(.009)/−.07(.01)、corrected=−.19(.02)/−.12(.04)，报δ50^(+∞/−27)及bracketed−.15(.02)。PDF6明确大支还允许δ<−159，不能把50上界∞当只正号。该表行没列targetenergy，本任务不补能量身份。 | measured-branch-and-reference | direct | PDF5 Table2 104Mo3gamma row；PDF6 firstparagraph | true |
| EL18-8 | 方括号是某一理论A2或A4距离本坐标实测超过1.5σ而仍在3σ；正文通常只用A2定δ，少数双系数行有dagger。quotedδ误差位于A2/A4空间，不是δ轴Gaussian误差；未给完整Cov/DELTA配置时不称已恢复jointellipse/CI。 | uncertainty-and-branch-selection | direct | PDF3 results/lastparagraph；PDF4 Sec3.2；PDF5–7 Tablecaptions/footnotes | true |
| EL18-9 | 原图Table2的106Mo2gamma→2行raw/corrected均印−.18(.02)/.27(.08)，但正文称同组按G=.78/.6更正；central相除应−.230769/.45，按最后打印位的centralroundingbox也无交。Table3 110Ru3gamma→2负branchbound印−41、PDF8正文印−46；保留原差，不凭此改数据或判实际程序错误。 | printed-response-and-replay-boundary | direct-and-task-printing-audit | PDF5 Table2 106Mo firstrow；PDF4 correctionrule；PDF6 Table3；PDF8 lastparagraph | true |
| EL18-10 | 作者Fig11/讨论把跨±∞的signtrend与Krane1973shapechange比较；该同transitionE2/M1ratio符号不是静态Q的直接读数，pure点可由M1穿零产生符号变化。任务固定E2/M1小振幅反例只限制逻辑唯一性，非实际Mo/Ru/Pd的替代核模型或新shape结论。 | author-interpretation-and-inference-boundary | direct-and-task-algebra | PDF2 Eq1/signparagraph；PDF9 Discussion；PDF10 Fig11 | true |
| EL18-11 | 论文以Goodin2010thesis为待纠正的前结果/方法，引用Daniel2007及Luo2001装置；本批独立于W178/130Ba采集，但EL18/thesis/同252Cf程序处理不能计成多次独立实验，精确共享events还需原metadata。 | source-lineage-and-independence | direct-and-audit-boundary | PDF1 Intro/2 Sec2/3 method；PDF11 Refs2/7/10 | true |

### 104Mo真实表行与projective区间

[冻结输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/el18-projective-branch-input.json)身份`DAY16-EL18-MO104-PROJECTIVE-BRANCH-01`，KS70发射约定与既有D96 bridge相同，3→2→0/pureE2reference用已核二次型。作者表列δ50对应(A2,A4)≈(−.188386,−.081600)，δ−.15给(−.189134,−.001796)；微小A2差与source三位理论列−.189/−.188不强求exact打印重放，unrounded inputs未给。

若**只用printedcorrectedcentralA2=−.19**，全部实根为−.15112555和+55.71718211；不把第二根改成50后宣称source重放。以两个printedmargins的一倍**矩形**作条件域，得到δ≤−132.0316或δ≥23.0837，且经±∞连接为同一projectivebranch；小负根在此盒外，三倍盒则又允许−.23136到−.07433。该字面盒不是原fullCov或作者区间，也不替代原文的negativebound−159；来源数字保持。它展示`atanδ=±90°`对应同一pureE2坐标，不能平均两个δ轴端点或截成两个独立实验。

对选择/衰减，centralraw/G给−.18717949/−.11666667，与所印corrected相容。若额外**假设raw2/raw4/G2/G4独立**，局部error为.0184513/.0423099，只是diagnostic；实际G4由共享G2/phi模型来而且组平均，Σ未知不能以这个对角传播充当原errorbudget。相同G2=.78对应单phi .4122761、G4(phi)=.5809215、dG4/dG2≈1.218408；组平均G4=.6不必须恰等于函数作用在平均G2，未据此判source不一致。

Eq9的G2/G4范围分别[1/5,1]、[1/9,1]，偶函数只给|phi|。Table1 102MoG2=1.03(.08)、114Pd1.06(.04)的central没realphi，source仍列g或∞error；本任务不剪裁成1、重拟g、借此声称作者数值程序错误或把正printedg当独立sign测量。

### 使用边界和决定

新[程序](../../system/scripts/day16_el18_projective_branch_audit.py)/[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/el18-projective-branch-audit.json)保存central所有根、projectivejoins、correctionJacobian、lastdigitfailure和samephi/Gsign控制。未取得原paircounts/9binledger/finiteacceptance、raw-background/附加门、actualΣ和DELTA输入recipe，因此只做L2表/定义核验，不是experimentalrefit。

`supports`δ区间需保留pure点与small/large多根；`limits`37行独立显著性、±∞符号趋势直接证明shape、或G2/G4独立校准。`revises`以表中central数值“看起来符合”便认定原程序闭合的做法。[[dco-pdco-ambiguity-worksheet]]补本例；[[angular-correlation]]补共享衰减/ORgate与观测对象。下一可复用高信息输入为NNDC DELTA原程序/说明和Goodin/实际校准ledger，不是自由调G/δ强配表。

## 公开DELTA副本已实际运行，原2018producer仍未认证

[[ekstrom-1993-delta101-angular-correlation-code]] D101-1至8给一个PyNE namedtag0.7.8保存的1993v1.01源码内容对象，已未改编译/执行。它按所声明printed104Moinput给两根，且揭示独立data/有限grid/抛物线/poorfit阈值与1000sentinel；这些事实不认证本篇实际用同hash或同unroundedinput。原2度purecontrol的插值失败/细步长恢复也保留，不把processexit0当实验分析正确性。

此新层使“generic DELTA源码不可得”的边界得到限定推进，而actualEL18paircounts/9binresponse/groupG与Σ/inputrecipe继续开放；未改原50/negativebound或source人审/flags。

## 104Mo的旧评价identity与反证层

[[nndc-2007-mo104-selected-gamma-reference-records]] N104-1至7实际取三个官方对象。2007base的adopted3+/gamma-bandparent1028.35给836.3/M1/MR空，Cf1027.9给835.5、Cm1028.0给835.8且M/MR空；可为本篇104Mo3gamma→2+表行提供结构候选，但本篇未给targetenergy/原peakledger，不把这些数无记录代入其actualgate。旧adoptedM1与本篇大E2支是需追来源的冲突信号，不由版本先后或空MR擅裁决。

adoptedglobalM说来自CmDCO，但96行Cm对象无actualtargetR/gate/angles，不能当独立δ0；相同.97ns half-life换成1.40ns mean与本篇calibration相容，却不是另一份新测量。N104-6/7保留不同array配置/同组paper、Cm标题下引Cfplungertime的谱系。currentonline仍2007base，不宣称已采用本篇2018结果。
