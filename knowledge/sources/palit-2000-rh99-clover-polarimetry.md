---
type: source
title: "Palit2000：99Rh宇称、clover a/Q分层及标定对象"
aliases: [Palit2000 Rh99 clover calibration, Pramana54 347 polarization]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experiment-and-detector-method
reading_depth: deep-read
title_original: "Parity of the band head at 3710 keV in 99Rh using clover detector as compton polarimeter"
authors: [R. Palit, H. C. Jain, P. K. Joshi, S. Nagaraj, B. V. T. Rao, S. N. Chintalapudi, S. S. Ghugre]
journal: Pramana
year: 2000
volume: 54
issue: 3
pages: "347-354"
doi: "10.1007/s12043-000-0126-x"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "Publisher PDF Pramana54(3),347–354(2000)"
source_url: "https://link.springer.com/content/pdf/10.1007/s12043-000-0126-x.pdf"
raw_file: "raw/papers/gpt/day16-20261018/palit2000-rh99-polarimetry-16ac6571acce.pdf"
raw_sha256: "16ac6571accecd822c67cbdb79f8adeb72734ef3766f767d4f778af47bae1387"
raw_storage_status: publisher-staging-verified-raw-archive-deferred
nuclei: [99Rh, 101Pd, 24Mg, 76Kr, 78Kr, 80Sr, 81Sr, 82Sr]
reactions: []
experiments: [TIFR-clover-Compton-polarimetry]
models: [angular-distribution-polarization, local-empirical-Q-fit]
observables: [parity, linear-polarization, asymmetry, analyzing-sensitivity]
methods: [Compton-polarimetry, angular-distribution, calibration-provenance]
tags: [a-Q-separation, reference, convention, finite-geometry, covariance]
---

# 先区分几何a与偏振Q，再解释同跃迁的伴随观测

## Bibliographic Record

Palit等，Pramana54(3),347–354(2000)，DOI[10.1007/s12043-000-0126-x](https://doi.org/10.1007/s12043-000-0126-x)。Crossref题名/七作者/卷期页核，publisher实际HTTP200的8页PDF，SHA见frontmatter。当前原件在tmp/day16-palit2000/springer-pdf.pdf，未写raw/Bib。它是[[garg-2015-135pr-magnetic-rotation]] Ref32的精确方法源，不是Garg实际2015response或2019erratum。

## Scope and Reading Depth

本session完整读8页Sections1–4、致谢、全部13项reference，视觉核4图/Table1/Eq1–11。原图确认OCR丢失的负号：a2=−.16(.01)、C=−.000099(.000007)keV^-1、H4=−1/6。没有将OCR正数当原输入。未取得每一reference/calibrationpoint的原counts/门/拟合Cov；不声称重现δ曲线/误差面或Gargactualcalibration。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| P00-1 | 使用单clover在beam90°、邻接AB/CD为parallel、AD/BC为perp，两晶体能量和选fullenergy；Eu152同target/geometry给a=N∥unpol/N⊥unpol，122–1408keV约1.00(.03)。a不是Q。 | detector-count-and-normalization | direct | pp350–351 Eq10/11/Fig2 | true |
| P00-2 | plane-axis P由electricφ相对reactionplane定义；Δ的perp/parallel是Compton散射方向。P=Δ/Q，Q0=(α+1)/(α²+α+1)、α=Eγ/(mec²)；两个角/两个角色需同时保留。 | polarization-response-contract | direct | pp348–350 Eqs1/2/6–8；Fig1 | true |
| P00-3 | Q以knownKr/Sr及Rh/Pd的AD计算Pcal和实测Δ标定，并引Na24的1368作为cascade reference；Q实际范围386–1368keV。reportedlocalfit D=.446(.006)、C=−.000099(.000007)keV^-1。 | response-calibration-and-locality | direct | p351 calibrationparagraph；Fig3/Eq9 | true |
| P00-4 | 1117keV line在99Rh连接3710的23/2态到2593的21/2+；AD15/45/75/90°给a2=−.16(.01)、a4=.01(.01)，Δ=.05(.03)，作者得Pexp=.37(.21)。这些是同源观测/derivedP，不计三次实验。 | actual-target-and-companion | direct | p351 targetparagraph；Table1/Fig4 | true |
| P00-5 | Fig4同正P可与largeδ M1+E2和nearlypureE1+M2曲线相交；作者另用AD排largeδ，报告E1+M2 δ=.015(.055)，进而给3710负宇称。P的符号单独不完成这一步，完整Fphase/ADCov本run未重拟。 | author-inference-and-branch-condition | direct-attributed | pp352–353 Fig4/Discussion | true |
| P00-6 | 原式1117给Q0=.400033、Qfit=.134178，Δ/Q=.372639与报.37相容；只用roundedσΔ得到σP=.223584而报.21，fullCov/未舍入数未知，保留残差不报全误差预算重现。 | printed-input-calculation | actual-arithmetic | Eqs8/9；p351 target；本页结果 | true |
| P00-7 | C从keV^-1转MeV^-1应乘1000变−.099；正确重算Q一致。混用MeV能量和原keV^-1C会给Q≈.178371。线性fit在约4505keV过零，说明不能当域外通用response；不是实测高能零灵敏度。 | units-and-domain-failure | conditional-calculation-on-source-fit | Eq9/printedC；本页单位控制 | true |
| P00-8 | 未给Cov(C,D)。给定两个quotedmarginal且固定E，1117的σQ可能范围.000728–.005528，Cov0为.003943，仅此fit项；不代总responseσ，也不重复加到sourceP误差。 | uncertainty-readiness-and-bound | exact-propagation | Eq9/fitcoefficients；本页Cov公式 | true |
| P00-9 | Eq3对pureM1/E1有H2=1、H4=−1/6；用printedADcoeff得planePcal∓.215686。mixedδ/实际布居与误差仍需原合同，不能由这个pureprobe重测作者δ。 | conditional-pure-limit | original-and-arithmetic | pp348–349 Eqs3/4前段 | true |
| P00-10 | Eq5字面prefactor(E/E′)^2且文字E为入射、E′为散射，与标准KN的倒数不同；固定scatterangle的azimuthratio里共同prefactor可cancel，Eq8的Q0仍成立。finiteangle权重不同，但actualproducer未得，不据印刷式判Qfit或原数据错误。 | isolated-literal-formula-boundary | direct-visual-and-exact-algebra | p349 Eq5/定义；p350 Eq8 | true |
| P00-11 | Na24的1368校准称用4→2→0的correlation coefficients算P，但完整2756direction/tag/接受ledger未明确给出。无条件、未取向source的singlesP=0与有方向条件的P不同；不能擅给本实验P=1/6或宣判其校准坏。 | reference-companion-readiness | source-and-conditional-physics | p351 Na24calibrationparagraph | true |
| P00-12 | Table1的260.4/493.0Δ=−.053(.042)/−.078(.039)被作者用作M1对照；260.4在所报Q标定下限386之外，不能把fit外推P当已测该能量Q。 | control-and-range-boundary | direct | p352 Table1；abstract/Qcalibrationrange | true |
| P00-13 | Rh99负宇称后对p1/2,g9/2及h11/2相关组态仅是作者解释；作者仍要求lifetimes检验更大deformation。本页方法示范不把P/δ当已测collectivity或建立完整Rh99band证据。 | structure-interpretation-boundary | direct-author | p353 Discussion | true |

## 校准与实际采集分层

known-line校准涉及115MeV27Al+58Ni产生Kr/Sr，以及110MeV31P+74Ge产生Rh/Pd；同clover的Qfit、derivedP和Fig4δ曲线共享calibration/AD输入。Eu的a测几何偏置，polarizedreference再定Q，是两个测量层。每一reference的未舍入面积、门、背景、AD误差Cov及fitCov(C,D)未逐项给出，不能将曲线回代当独立验证。

Garg2015引用本method并不把这里的a≈1或C/D继承为其真实15clover运行值。Garg原文reported a≈.93(.06)、不同campaign/geometry/selection及其2019修订范围另核；本source不能补Garg或Matta的Q、P–R Cov和δbranch裁决。

## 原式重算与literal边界

1117keV的pointQ0=.400033、finitefit factor CE+D=.335417，得Q=.134178和P=.372639。σΔ/Q=.223584与作者.21的差.013584保留，未用freeCov或调系数强闭合。

`Var(Q)=Q0²[E²Var(C)+Var(D)+2E Cov(C,D)]`只为localfit项。原keV^-1/MeV^-1换算、Cov范围和域外负Q警示都不代替实际response。对pureprobe的H4负号及C/a2负号均来自原图，不从OCR补正号。

字面Eq5若用r=E′/E，与标准式的prefactor比为r^-4；在同一scatterangle比较两个azimuth时它cancel，所以原Eq8仍精确给Q0。若积分finiteangles，这个因子不能从积分拿出；没有producer时只隔离公式边界，不给作者实际实现定罪。

本run[原式程序](../../system/scripts/day16_palit2000_calibration_audit.py)actualexit0；[冻结合同/结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/palit2000-calibration-audit-result.json)。未digitize重拟Fig3/4，也未生成toycounts或新δ。

## Summary

这个真实primary连接了a的unpolarized校准、Q的polarizedreference、AD伴随观测和parity/mixing的条件判断。它支持联合观测，限制positiveΔ单值赋值与跨阵列数字迁移。

## Competing Interpretations and Limitations

- 作者用AD排除largeδ M1+E2后选E1+M2；本run没有完整phase/ADCov/response，保留“作者reported”而不独立授唯一性。
- Na24 reference tag与fullCov缺口不等于证明作者错误；其条件P不能从unconditionalsingles自行补齐。
- calibration范围/localC-D模型不外推所有能量；Table1的低能对照也不扩张Q实测域。
- 当前以方法页与Garg输入合同为canonical关联，不新建薄Rh99band/nucleus页：完整能级结构primaryRef8尚未重读，本文的可复用增量是观测/标定合同。

## Knowledge Impact and Learning Decision

`supports`真实jointAD/P方法；`limits`几何a替Q、跨campaign继承数值和无companion唯一δ；`revises`GargRef32的原件readiness，新增已读主源，仍不补Gargactualresponse/2019body。所有新claimsneeds_review。

## Extracted Pages

[[compton-polarimetry]]、[[linear-polarization-asymmetry]]、[[multipole-mixing-ratio]]、[[garg-2015-135pr-magnetic-rotation]]、[[135pr-mixing-branch-input-contract]]、[[high-spin-angular-polarization-mixing-ratio]]。
