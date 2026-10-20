---
type: source
title: "Woodside2026：58Fe新Coulomb计数、相位多解与DSAM约束谱系"
aliases: [Woodside 2026 Fe58 anomalous collectivity, arxiv2603.17414v1]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: experiment-and-reanalysis
reading_depth: deep-read
title_original: "Resolving anomalous collectivity in the 4+1 to 2+1 transition of 58Fe"
authors: [J. A. Woodside, B. J. Coombes, A. E. Stuchbery, A. J. Mitchell, M. Reece, G. J. Lane, T. J. Gray, G. Pasqualato, L. J. McKie, N. J. Spinks]
journal: Physical Review C
year: 2026
volume: 113
issue: 4
pages: "044306"
doi: 10.1103/16y4-bggw
citation_key: ""
canonical_source: https://doi.org/10.1103/16y4-bggw
raw_file: raw/papers/2026_Woodside_Fe58_collectivity_Coulex_Dsam.pdf
raw_sha256: fddbd3b0de35b1b723c2bcb9959af4cf6c489a0d8e00f87e9126218acfec8d5a
nuclei: [56Fe, 58Fe, 60Fe]
reactions: [56Fe+197Au, 58Fe+197Au, 55Mn(alpha,p-gamma)58Fe]
methods: [Coulomb-excitation, Gosia, doppler-shift-attenuation-method, phase-convention]
models: [shell-model, GXPF1A]
tags: [58Fe, Coulomb-excitation, DSAM, stopping-power, matrix-elements, source-dependence]
---

# 58Fe：新采集与约束后B值要分别审计独立性

## Bibliographic Record

J. A. Woodside等，*Phys. Rev. C* **113**(4),044306(2026)，DOI[10.1103/16y4-bggw](https://doi.org/10.1103/16y4-bggw)。Crossref DOI/article-number已核。实际全文为[arxiv2603.17414v1](https://arxiv.org/abs/2603.17414v1)，上传2026-03-18、PDF dated19Mar2026。abs comments写14页，实际PDF15页，保留差异；VoR正文未读。

实际PDF为`tmp/day18-20261020/woodside58fe/woodside58fe-v1.pdf`，SHA256见frontmatter；raw_file是未写入归档槽，raw/Bib保护不变。官方源码包hash`5c98e7b5011491a50d97a04e1f6d7f78b3430d32c1a4485b97467a9ff29a47bd`，19成员为TeX/bib/README与图；不含实际Gosia job、逐photodiode数值yields/Σ或OCR重建的旧DSAM程序。

## Scope and Reading Depth

本独立Day18在SC26及实时metadata/abstract priming之后冻结本原件问题，完整原读15页含参考、13图、10表和4式；PDF2–13关键图表全部视觉核。原TeX仅定向复核lifetimes/constraint/fixedphase文字，不把注释掉的草稿当发表claim。八组TableVII的4→2中心、Fig8/9已印E2图及TableII四个归一yield另新复算；不是Gosia或旧DSAM fit重现。

未读Cavallaro1977/Bolotin1978/Kosyak1983、1981reference Coulomb、Stone2005或Orsay未发表工作的正文；其谱系和数值来自本文，后续需原件/官方对象。没有把未公开Gosia配置、旧计数或完整Σ补写成已取得。

## Summary

新220MeV56/58Fe Coulomb-excitation提供新的particle-γ计数，限制过去由DSAM/DBLS寿命得到的异常58Fe强度解释。Gosia结果仍依参考B、静态Q、bufferstates及重新分析后的DSAM寿命约束，尤其TableVI包含目标4+1态τ。故新采集独立与最终B完全独立是两个问题；本文结果/相位范围保留，未取得无此寿命约束的原fit，不能据摘要简写裁定全部独立性或反判实验无效。

## Experimental or Theoretical Setup

220MeV56/58Fe束入射718µg/cm²197Au，靶法线与束轴20°，CAESAR七HPGe（56Fe用六）/八Si photodiodes（56Fe排故障c）。Eu152作能标/效率；每HPGe-photodiode对作Doppler校正、粒子γprompt门与两侧random背景扣除，后因统计按particle detector合并γ探测器。新观测是TableII背景处理后的counts及修正yield。

Gosia用SRIM能量损失及BrIcc、2+1→0+1作归一reference；有fixedbuffer矩阵元、branch/δ/lifetime constraints、Qs(2+1)及假设Qs(4+1)=0。这里的Qs是**静态spectroscopic moment**，不是Jensen的sidefeeding Qs或band Qt。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| WO26-1 | 实际body为arxiv2603.17414v1十五页/13图10表4式，abs称14页，期刊metadataPRC113044306/DOI16y4-bggw；未读VoR。公开src19文件只有文稿/图，未得actualGosia/旧DSAMjob或原Σ。 | identity-version-and-input-scope | direct-metadata-and-original | PDF1–15；arxivabs；Crossref；officialsrc成员清单 | true |
| WO26-2 | 新Coulomb采集为220MeV56/58Fe+Au、CAESAR/photodiode/Eu152校准、prompt/random背景和逐pairDoppler修正；新counts独立于旧1978data。本文同时重分析旧DSAM，不能把后者也计新采集。 | direct-new-acquisition-and-lineage | direct-report | PDF2–4 SecII/TableI/Figs2–4；PDF8–12 SecIIIB | true |
| WO26-3 | TableII yield已修relativeefficiency及particle-γangularcorrelation成effective4π，再对同核2+1→0+1归一；56Fe4→2 counts7100/225000而yield.044，58Fe1680/50700而yield.054。yield非裸count比、absolutephotonperparent或绝对效率。 | observable-normalization-contract | direct-and-derived | PDF4 TableII及其前段 | true |
| WO26-4 | Gosia固定referenceRME为56Fe.327eb/58Fe.351eb，来自此前Coulomb/adopted2+1→0+1B；buffer另用adopted或re-evaluatedDSAM τ/branch/δ。Gosia本身仍使用SRIM，只是其能量积分角色不同于DSAM时间映射，不称无任何stopping输入。 | reference-and-model-input-dependence | direct-report | PDF4–5 SecIIIA/Eq1/TableIII；PDF6 TableIV | true |
| WO26-5 | TableVI明确将58Fe2+2 τ2.4(.5)和目标4+1 τ.66(.08)的re-evaluatedDSAM值纳Gosia minimization constraints，另含adopted2+1τ9.4(.3)。因此最终GosiaB与updatedDSAM τ的吻合不能无条件当完全独立验证；需actualweights/联合输入及去掉目标τ后的fit，当前未提供这些重放输入。 | explicit-shared-constraint-and-inference | direct-and-derived | PDF5 constraints段；PDF6 TableVI/caption；原TeX相同正文 | true |
| WO26-6 | 固定Qs(2+1)=−.19(.08)/−.27(.05)eb给强相关矩阵元方向；Fig7a未有清楚jointminimum。Qs(4+1)未测，作者用56Fe既有数据/模型比较选近0，再对两同位素都设0；不当58Fe独立测得Q4=0或完整自由fit。 | source-identifiability-and-cross-isotope-assumption | direct-and-boundary | PDF5–6 Eq2及其后四段；PDF7 Fig7 | true |
| WO26-7 | Fig8/9以固定一个到每态的E2符号选statephase，其余相对符号产生56Fe四/58Fe八组合；Eq3的三RME闭环P3可观测，单个statephase不是observable。TableVII/图10仅−++方案被作者95%规则排，七方案仍未唯一选定，不把minχ²方案当已测唯一phase。 | source-phase-multiplicity | direct-report | PDF7 Figs8–9/Eq3；PDF8 TableVII；PDF9 Fig10 | true |
| WO26-8 | TableVII58Fe4→2的B范围19–27W.u.（含作者排除方案），未排七方案为21–27；最大的27(3)低于旧adopted47(7)是作者条件fit下比较。其χ²绝对分位线/自由度与actualobjective未给完整输入，不能自换Δχ²cut或将8方案作Bayesian后验权重。 | reported-result-and-statistical-boundary | direct-and-boundary | PDF8 TableVII及其后段；PDF9 Fig10caption | true |
| WO26-9 | 旧Bolotin原raw已不存，但作者有logbook与OCR重建listing；先重现旧分析再逐态F和停止更新。SRIM电子stop与旧LSS约差2倍，初approx分别将Mn/Ta电子项乘.608/.515且核项不动；精确替表与该approx τ差通常末位一单位。不是整个生成元统一scale或本任务实际code执行。 | author-reported-old-data-reanalysis | direct-report-and-boundary | PDF8–10 SecIIIB/Fig11 | true |
| WO26-10 | TableVIII τ首误差是stat，第二误差“includes”stop估计（电子±5%/核±10%），不能把第二项又当pure-systematic与首项quadrature相加。目标态TableVIII为.66(3)(8)，TablesVI/IX用.66(8)，PDF10 prose另写.66(6)，保literal口径差，未读VoR不猜更正。 | uncertainty-budget-and-literal-boundary | direct-original | PDF6 TableVI；PDF10首段；PDF11 TableVIIIcaption/2077行；PDF12 TableIX | true |
| WO26-11 | 较长τ>1ps受停止/散射模型及小shift影响，作者建议适合ps的方法复测；氧化物vs金属可能解释Kosyak56/58差是conjecture。原Cavallaro缺proton gate/feeding的可能解释也非本次直接测得。 | author-counterevidence-and-conjecture | direct-report | PDF10 SecIVA；PDF12 TableIX后段 | true |
| WO26-12 | Fig13b/模型Eq4的三yrast点成簇而不定charge比斜率，作者仅称更靠近standardcharges；非唯一拟合universal有效电荷。Prose1.33与Fig13caption1.3保原，basis/interactions及64Fe等原文未读不外推。 | model-identifiability-and-transfer-boundary | direct-report | PDF12 Eq4；PDF13 Fig13/TableX/讨论 | true |
| WO26-13 | 对Fig8/9印出的实E2子图，新枚举得56Fe V7/E8/cycle-rank2有4个statephase类、每类64符号配置；58Fe V8/E10/rank3有8类、每类128配置，P3与same-pair E2/M1比都不受state rephasing影响。只核印图subset，不认证完整Gosia输入、未见弱支或新measuredδ/phase。 | task-exact-phase-graph-audit | derived-and-boundary | PDF7 Figs8–9/Eq3；新fe58phasecontract/result | true |
| WO26-14 | 新按Eq1/声明常规Weisskopfradius将TableVII八个4→2RME中心转W.u.，都在整数打印约.51W.u.内；TableII裸counts到yield的combinedrelativefactor约1.394/1.630/1.449/1.789，不能拆成单eff校准。Eq2静态Q给diagRME约−.250682/−.356232eb，statephase也不能翻该diag符号；非新Qt或CI。 | task-published-unit-and-normalization-audit | derived-and-boundary | PDF4 TableII；PDF5 Eq1；PDF6 Eq2；PDF8 TableVII；新20checks结果 | true |

## Analytical Reconstruction and Self-Audit

本次新[问题/合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/woodside58fe-input-contract-003.json)、[脚本](../../system/scripts/day18_fe58_phase_input_audit.py)与[20项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/woodside58fe-input-result-003.json)将新计数/相对yield、拟合RME、派生B及外部约束拆开。没有运行Gosia、假设原χ²项权重、删寿命项后宣称已重fit或从B倒推hiddenbranch。

实statephaseη_i=±1下M_ij→η_iη_j M_ij，closedcycle每顶点出现两次，故环乘积不变。Fig9以七条treeedges固定八态phase，剩三条chords为八类；这个自由度不等同同光子的M1/E2δ。后者两振幅随同statephase一起变，δ比不变。Diagonal M_ii也不随statephase变，所以静态Q符号不是任意gauge。

## Competing Interpretations and Limitations

新Coulombcounts是独立实验层，约束后的GosiaB具有旧reference/DSAM/buffer/Q依赖。当前证据不足以量化这些项各贡献多少，也不足以宣称新计数无信息或论文结论无效。真正独立的交叉检验需报告matchingyield/response/Σ和不借目标τ时的profile/相位范围。

源abstract“三次独立测量一致”与正文旧τ.34/.34/.54、近1σ才重叠的限定并列；不把独立采集等同独立stopping校准。Fig12时间图派生B仍依各τ与branch，不再增加测量。

## Knowledge Impact and Learning Decision

后续actualNNDC对象[[nndc-2010-fe58-reference-lifetime-lineage]] F58-2/3/4把reference再细分：811态half-life6.54ps明确由同1981Le02的B(E2)推得，mean9.435ps与本paper9.4ps对应；固定RME.351eb与adoptedmeanτ不能自动当两个独立新测量。静态Q也同primary，但实际jointB/QΣ未知。F58-8只是固定E/branch/ICC单primitive的依赖模型；actualGosia权重、去targetτprofile仍待input，不裁原fit发生重复计权。

`revises`[[stuchbery-2026-cr54-dsam-reevaluation]]对58Fe“独立Coulomb”二级简写：新采集可独立，最终强度的约束链须另审。`supports`[[lifetime-strength-audit-165tm-136nd]]按观测/fit/rate/geometry/解释分层；`limits`两方法同中心就算完全独立校验。与[[doppler-shift-attenuation-method]]互链，不能将58Fe百分数、Q4=0或八phase直接迁到165Tm/136Nd。

## Extracted Pages

- 方法：[[doppler-shift-attenuation-method]]，加入Coulomb新计数/DSAM约束的独立性区别。
- 研究审计：[[lifetime-strength-audit-165tm-136nd]]，加入完整独立性矩阵、phase/Q/δ合同与actualinput优先级。
- 来源对照：[[stuchbery-2026-cr54-dsam-reevaluation]]；索引：[[index]]。本轮不建仅复制参数的56/58Fe核素页。

## Human Review Triage

P0自审：WO26-5只记录明确constraint及其依赖，不据摘要或未知权重判circularinvalid；WO26-8/10保统计/误差口径；WO26-13只枚举印图subset。P1：fixedQ4跨同位素假设、参考B/τ的底层共同谱系、旧measurement原件未读。全部needs_review/sourceunreviewed，未设human-reviewed。

## Reproducibility and Evidence Gaps

本Day18 run保存PDF/src/Crossref指纹和actualscope，raw归档槽deferred。仍需逐photodiode/HPGe原yields与效率/AD/随机背景/Σ，Gosia版本/job/constraint权重与去目标τ结果，Q4/phase新观测，referenceB与adoptedτ的官方来源身份，以及旧logbook/listing/DSAM响应。当前只给原件依赖与条件代数审计，不给新实验B、δ、Q或CI。
