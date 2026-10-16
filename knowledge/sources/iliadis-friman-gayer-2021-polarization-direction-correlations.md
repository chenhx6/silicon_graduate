---
type: source
title: "Iliadis与Friman-Gayer 2021：偏振–方向关联、相位角色与测量几何"
aliases: [Iliadis Friman-Gayer 2021, IF21 polarization direction correlations]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: theory-method-review
reading_depth: deep-read
title_original: "Linear polarization–direction correlations in gamma-ray scattering experiments"
authors: [Christian Iliadis, Udo Friman-Gayer]
journal: European Physical Journal A
year: 2021
volume: 57
number: 6
article_number: 190
doi: "10.1140/epja/s10050-021-00472-1"
citation_key: IliadisFrimanGayer2021LPDir
citation_key_origin: agent-local-paper-label-pending-reference-manager
canonical_source: "doi:10.1140/epja/s10050-021-00472-1"
raw_file: "raw/papers/gpt/day15-20261016/iliadis-friman-gayer-2021-vor-4c0b226de8e5.pdf"
raw_sha256: "4c0b226de8e5356406122f7610d3d493a171487579b9b6cf879e8f993a30657f"
arxiv_version: "2104.00228v1 31-Mar-2021, separately acquired"
nuclei: [generic]
reactions: []
observables: [angular-correlation, analyzing-power, multipole-mixing-ratio]
methods: [linear-polarization-direction-correlation, detector-geometry-design]
tags: [phase-convention, nrf, polarization, angular-correlation, identifiability, source-criticism]
---

# IF21：初态已知仍须核相位、几何和多根

## Bibliographic Record

C. Iliadis与U. Friman-Gayer，*European Physical Journal A* **57**(6),190(2021)，DOI[10.1140/epja/s10050-021-00472-1](https://doi.org/10.1140/epja/s10050-021-00472-1)。Crossref exact DOI核作者、题名、卷/期/article190及2021年6月。

本session先从[arXiv](https://arxiv.org/pdf/2104.00228)取得**v1，31-Mar-2021**，raw为`raw/papers/gpt/day15-20261016/iliadis-friman-gayer-2021-arxiv2104.00228-58c0294f6b3d.pdf`、SHA-256 `58c0294f6b3d1ef6969484bf89dfc6248ea44b5a73b536ca6bf38aa048dfc756`。随后从[出版商PDF](https://link.springer.com/content/pdf/10.1140/epja/s10050-021-00472-1.pdf)取得VoR，39页/42,080,158bytes，hash见frontmatter。两个版本分开保存，不按同题名宣称逐字相同，也不将二者计独立证据。

## Scope and Reading Depth

- 在ALPACA README强priming后冻结回忆；v1完整读PDF1–18：Secs1–9、references、Appendix导言。主要公式、rank、worked example、unobserved propagation、图1–11、误差/geometry和局限均读，contact sheets视觉查主线。
- VoR定向核PDF1–6的definition/phase、p14 Fig10、p16 Eq30/31与局限；特别放大p3 Eq3–7、p5 Eq16–18及对RU09的批评。VoR未逐行通读39页。
- v1 Appendix仅选图：PDF20–23的pure/mixed与halfspin patterns、PDF28–31的unobserved和analyzing-power例；不称所有51图逐点数值复算。
- 本来源是理论/综述，作者图中Eq28/29数据为**hypothetical**。没有新的11B采集、RU09原事件、GEANT3 producer/实际Cov。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| IF21-1 | formalism假定target随机取向、各level isolated且Jπ确定，最低两multipoles截断；incidentbeam方向/偏振已定义并不消除这些条件。 | model-domain-definition | direct | VoRp2 Sec2；v1p2 | true |
| IF21-2 | W=WDD+WLP，WDD用An(1)An(2)，WLP用En(1)An(2)与P_n^2 cos2phi；En避免kappa系数的零CG分母。rank限于even n≤min(2J,2L1max,2L2max)，J为中间态。 | coefficient-and-rank-definition | direct | VoRp3 Eq2–7 footnote2；VoRp4 Eq9–11 | true |
| IF21-3 | 本文采用Biedenharn：intermediate J始终在RME右边，physical elastic给dB1=dB2；Eq18与未改Steffen系数体系的桥为dB1=−dS1、dB2=dS2。同号dS必须连同所用incoming系数修改一起核，不能只凭符号名互换。 | phase-role-definition | direct-and-use-boundary | VoRp5 Eq13–18 | true |
| IF21-4 | 作者明确批评Rusev2009/另一27Al工作写Steffen d1=d2，认为会改变W的大小而不仅δ符号。这是IF21作者的已发表判断；本任务未据此取得RU09代码或裁决所有modified-KSW实现。 | attributed-published-criticism | direct | VoRp5 Sec3 paragraphcitingRef21/22 | true |
| IF21-5 | IF21 beam沿x、E沿y、phi从z在yz投影计；不能同名替换beam-z/E-x探针角。本文A=(Wphi0−Wphi90)/sum，故本任务映射后RU09平行E减垂直E的不对称度为−A_IF。 | geometry-and-sign-crosswalk | direct-and-task-coordinate-map | VoRp2–3 Fig1/2；Eq26/27 | true |
| IF21-6 | 作者四detector基本几何在theta45/90、phi0/90取两个analyzingpowers；单个角的多根可能由第二角限制，但某些pure/mixed patterns相同，任意多角也不能保证唯一。图10/11为hypothetical数据与分支投影，非实验置信域。 | companion-observable-and-identifiability | direct | v1p10–15 Sec7 Fig9–11；p18 AppB | true |
| IF21-7 | finite acceptance一般以rank Qn(k)同时进入分子/分母，只有同detector/distance/shield等条件才可共用；不能把任意candidate/energy下几何效应概括成一个可移用常数C。 | response-transfer-boundary | direct | VoRp16 Eq30 andfollowingparagraph | true |
| IF21-8 | 不完美linearpolarization在作者无handedness模型下削弱asymmetry幅值，finite-source/selfabsorption/完整response仍需校正或radiation-transport，weakpatterns须likelihood和额外观测。 | beam-and-response-boundary | direct | VoRp16 Eq31；Secs8–9 | true |
| IF21-9 | 本任务独立实现Eq3–9并与保存的NRF photon trace比较，在选定3/2→3/2/5/2→3/2、固定real amplitude/pointgeometry网格差<9e−16，角平均=1。两路线共享CG/6j primitives，不是独立原作者程序或实验重分析。 | bounded-algebraic-crosscheck | task-calculation | VoRp3 Eq3–7；VoRp4 Eq9；本任务coefficientaudit | true |
| IF21-10 | 保留RU09印a/C作为有条件摘要输入时，一致Biedenharn physicalelastic模型在4443.93和8916.3各有4个实根，5019.08有2根；这不能直接替换发表δ或生成actualCI。未改Steffen同号的字面变体近原smallroots但未闭合−1.30，其producer/finite-response缺口保留。 | conditional-inversion-boundary | task-calculation-from-published-inputs | RU09TableI；VoRp5 Eq18；本任务rootmatrix | true |
| IF21-11 | 完整积分未观测中间gamma得到incoherent multipole sum与Cn传播，限制rank的是observed步骤和两中间spin而不是Lu本身；其δu符号不能由该marginal识别。 | unobserved-transfer-definition | direct | v1p8–9 Eq20–25；VoRcorrespondingSec6 | true |

## Summary

本综述给出NRF中偏振–方向关联的完整系数、相位角色、半整数spin多根及有区分力的观测几何。它对[[rusev-2009-multipole-mixing-ratios-11b]]提出了直接的相位批评，因此不能继续把“该实验无额外模型”解释为无convention/多根/response问题。

实验azimuthal a与用于反演的W模型是两层证据。保持物理振幅不变而全面变换坐标/系数不会产生新物理分支；只把两个同名delta设相同却不核operator roles会改变模型。[[polarized-photon-branch-audit]]保存本次独立的conditional roots与45° companion预测。

## Competing Interpretations and Limitations

- IF21对旧paper文字的批评与“RU09原程序实际上怎样实现”的问题分开。尚未取得该producer、unrounded response或完整Σ，不能将本任务的不同数值直接判为作者代码错误。
- [ALPACA固定README](https://github.com/u-eff-gee/alpaca/blob/f173c2d2e2fd855451e06446a2cfcce679c42d24/README.md) Sec4.ii指出，Zilges等后续NRF review以修改incoming系数方式保留同号KSW；此处只核了README的公开描述。其原review DOI`10.1016/j.ppnp.2021.103903`的footnote2尚未取得，2023 corrigendum DOI`10.1016/j.ppnp.2023.104059`目前也只metadata，内容未知，不推断勘误是否涉及相位。
- 该review的publisher PDF遭robot challenge；KUPS旧record404、精确query无目标全文，TUbiblio仅书目；公开API200只coredata、没有body（也未认证可用fulltext entitlement）。OpenAlex曾标bronze、API自报openaccessfalse，状态不等同实际正文到手。本任务未操作CAPTCHA、凭据或机构登录，也未把失败页面当原文。
- 这些边界要求保留“完整定义优先”的竞争解释，不能只引用一篇综述就宣布所有用同号KSW的实验都错误。

## Pinned Software Companion

公开[ALPACA](https://github.com/u-eff-gee/alpaca)固定commit `f173c2d2e2fd855451e06446a2cfcce679c42d24`。本次读取README、W_pol_dir/Ev/Av/F coefficients及相关header/test，7个target Git blobs均验证Git SHA-1与SHA-256，记录在本run。首轮raw host timeout后改用正式Gitblob API读取；未运行安装器、C++/Python外部代码，也没有copy GPL实现到本仓库。新的Python脚本独立实现的是发表的数学式。

codeREADME自述已与作者R实现和文献交叉测试，这是software作者声明，本session未重跑；它也不证明此公开commit就是2021图表或2009实验的exactproducer。代码/综述同理论谱系，不计独立实验采集。

## Reproducibility and Source Locators

[冻结系数核验输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-if21-coefficient-audit-input.json) SHA-256 `c0a46e572ed215c03608b2881765ba844937b57bb3e76940ebbeb3f2ebcd8af0`，[独立系数脚本](../../system/scripts/day16_if21_coefficient_audit.py)及[最终结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-if21-coefficient-audit.json)保存source/input/code hash、全grid与all-real-root endpoints。原RU09 firstcode/result和后续diagnostics都保留，没有调C/sign来只配smallroot。输出的W声明为角平均1的conditional density convention；没有把印刷归一式当作自动测试通过的证据。

## Extracted Pages

- [[polarized-photon-branch-audit]]：controlledinitialdensity、Biedenharn/KSW角色、独立系数/振幅与实际source多根分层。
- [[dco-pdco-ambiguity-worksheet]]、[[angular-correlation]]：下一角度应检查rank/condition/完整response，不套普适polarization唯一选解。
