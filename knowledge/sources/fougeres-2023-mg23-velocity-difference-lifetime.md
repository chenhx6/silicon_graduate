---
type: source
title: "Fougères2023：23Mg速度差寿命、新质子份额与实际公开输入"
title_original: "Search for 22Na in novae supported by a novel method for measuring femtosecond nuclear lifetimes"
aliases: [Fougeres2023 Mg23 lifetime, F23 velocity difference]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
authors: [Chloé Fougères, François de Oliveira Santos, Jordi José, et al.]
year: 2023
journal: Nature Communications
volume: 14
pages: 4536
doi: 10.1038/s41467-023-40121-3
citation_key: ""
canonical_source: "Fougeres et al NC144536 publisher main7p SI8p Figshare22666537v1 Zenodo8044973"
source_url: https://www.nature.com/articles/s41467-023-40121-3
raw_file: raw/papers/day17-20261020/fougeres-2023-mg23-publisher.pdf
raw_sha256: 6652343310f238d7249654411a34713985bf4be73bd7e88d45cccd96158e0be7
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Mg, 22Na, 23Al]
reactions: [3He(24Mg,alpha)23Mg]
methods: [doppler-velocity-difference, lifetime, charged-particle-coincidence, gamma-tracking]
tags: [DSAM, lifetime-strength, proton-branching, covariance, public-data]
---

# 新寿命近旧值，分支输入显著改变强度链

## Bibliographic Record

Chloé Fougères等，*Nature Communications*14，4536(2023)，[DOI10.1038/s41467-023-40121-3](https://doi.org/10.1038/s41467-023-40121-3)。实际读取出版商正文PDF7页及Supplementary Information8页，出版5Sep2023；没有把预印本/会议文算独立采集。

正文SHA256`6652343310f238d7249654411a34713985bf4be73bd7e88d45cccd96158e0be7`，SI SHA256`56a513b755521f0f1f0043d0564a94f8552c51300401282df46cd9ae74be5fb9`。缓存`tmp/day17-fougeres2023/`，raw/Bib不改。[原件下载](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-main-download.json)、[SI下载](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-supplement-download.json)。

[Figshare22666537.v1](https://doi.org/10.6084/m9.figshare.22666537.v1)提供Source_Data.zip(375909bytes，MD5`269299f50431e8b03772efed1201e5d4`)，含两XLSX图数据，CC BY4.0。另取得本文引用[Zenodo8044973](https://doi.org/10.5281/zenodo.8044973)的EVASIONS v1.0.0，zip15494623bytes、MD5`ee3579b86bcdf8b7d6e16d598f6b4485`，34文件逐一对应[Git tag commit c6a4ff3](https://github.com/CFougeres/EVASIONScode/tree/c6a4ff3756724d6becd17414851bc8140d00a311)。当前main另有license删除提交，不代替论文冻结release；本轮按公开release证据读取，不改其许可或作者仓库。

## Scope and Reading Depth

声明J04/K16/Seattle/作者thesis强priming后冻结回忆；实际读正文7页全部主线/参考文献、Eq1–4、Fig1–3、Table1–2与SI8页全部/Fig1–4/Table1。全页视觉核。图数据先hash/CRC/白名单，再读main Fig2right全部37/25/37点及SI Fig1两grid；其余sheet仅结构/首行。代码目前读README、inputs、Makefile、main、CodeA和MC_sim，未完整审计/执行；公开ROOT只查schema，未读event数值。[actual scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-reading-scope.json)。

## Experimental or Method Setup

GANIL110.8(.4)MeV24Mg、3He约2×10¹⁷cm−2，植入约.1µm；5.0(.5)µmAu与20.0(.5)µmAu双箔，VAMOS++在0°测α、31晶AGATA在120–170°测γ。事件级α运动学给βreac、γ能量/角度反推βems，Δβ分布映射寿命；SPIDER300/640µm在10–25°测p。独立于J04/K16的采集，但依赖SRIM停止、跨能γ效率及reference结果。

## Summary

新测τ11(+7,−5)fs与旧10(3)相容；新测BRp=.68(.17)%与引用2020年的.65(.08)%接近，远小于旧条件链约3.7%。作者把新旧输入综合为τ10.2(2.6)fs/BRp.66(.07)%并假J7/2，推荐omega.24(+.11,−.04)meV。寿命近旧值不代表强度不变，分支、spin和共同来源必须逐项重审。原图数据和衍生事件已实际取得，但仍不等完整原实验fit/Cov闭合。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F23-1 | 实际publisher7页+SI8页完整主线/图表式已读，正文/SI/两XLSX/releasehash记录；GANIL本采集与J04/K16不同，评价和recommended组合不重复计独立实验。 | identity-reading-and-dependence | direct-original | main PDF1–7；SI1–8；reading-scope | true |
| F23-2 | GANIL110.8(.4)MeV/3He.1µm/5+20µmAu、VAMOS++α0–10°、31AGATA120–170°与SPIDER10–25°为实际setup，不迁用TRIUMF或Si-thesis response。 | actual-experimental-identity | direct | main PDF1–2；SI3 | true |
| F23-3 | βreac由αmomentum/两体运动学，βems由γR和角度反演，Δβ事件分布约exponential卷resolution；不是直接时钟计时或只把平均β当每个event。Eγ0与τ同时free，能量校准和response仍在推断链。 | observable-and-inference-chain | direct | main PDF2/Eqs1–4/PDF5 Fit；SI2 Fig1 | true |
| F23-4 | 作者以Ex选择减少topfeeding，称机制/角分布/角依赖eff不影响寿命；此为本选样/forwardmodel的适用主张，不扩展为任意finitegate或branch分析无角响应。branch MC仍假ℓ0p/isotropic、AGATA高能效率需simulation。 | author-scope-and-companion | direct-author-claim-and-boundary | main PDF2–3/PDF5 Branching；SI5 | true |
| F23-5 | 新τ为11(+7,−5)fs含stat/sys，约50%统计和26%系统；Table1列15/12/12/10/6.5/6/3.5/.3%，名义quadrature26.525对打印26保舍入/未取unrounded边界。20%stopping输入对应10%τ项，不可称零停止依赖。 | reported-lifetime-and-systematics | direct-and-arithmetic | main PDF3 Table1；exercise Table1 | true |
| F23-6 | 5292/3796控制报告4(+1,−3)/40(+6,−7)fs与评价5(2)/41(6)比较，检验有用但同模拟/校准、评价含旧测量；不把controlledagreement或低χ²ndf直接当所有系统误差/coverage证明。 | companion-and-shared-input | direct-and-boundary | main PDF2；SI2/5 | true |
| F23-7 | SI用Pearsonχ²拟合profiles、整体integral归一，τ/Eγ0 free；原完整fitrange/模板Cov/producer job未恢复。χ²ndf .4/.5→“errors conservative”是作者解释，不是本任务已证明的CI覆盖率。 | statistical-construction-and-readiness | direct-author-interpretation | main PDF5 Fit；SI2 Fig1 | true |
| F23-8 | SPIDER测BRp=.68(.17)%；pureAu背景减除后，先扣7855/8016/8163三个模拟高态，再限7770的τ/omega/BRp<.2%幅度，只拟关键峰。该branch不是完全无reference/无背景的直接p计数比。 | new-branch-and-conditional-subtraction | direct | main PDF3；SI3–5 Fig3 | true |
| F23-9 | BRp reference .65(.08)%来自Friedman2020；合并推荐.66(.07)%与τ10.2(2.6)是作者综合。旧J04 τ与新τ共享部分stopping知识但采集不同；2020body尚未读，不据转引认证其独立性/全误差。 | recommendation-versus-new-measurement | direct-and-source-readiness | main PDF3；Ref23；SIRef11 | true |
| F23-10 | J3/2、5/2、7/2仍被讨论，作者明确assume7/2，援IAS mixing缺失和shellmodeldecaypattern。新τ/branch并未直接独立测定J；其它J会改统计因子/BR响应，不能只改g就宣称完整替代实验fit。 | spin-assumption-and-model-boundary | direct | main PDF3 spinparagraph | true |
| F23-11 | 作者推荐omega=.24(+.11,−.04)meV；本任务固定推荐τ/BR/J中心得.241766、新测alone得.230930，旧τ10/BR.037得1.34016，展示分支输入主导变化。条件中心核不重建其非对称CI或新实验rate。 | actual-input-and-central-check | task-derivation | main PDF3；exercise conditional_rate_centers | true |
| F23-12 | 固定其它推荐数，仅g换J3/2/5/2给omega.120883/.181325meV，是条件灵敏度，不是候选自旋下matchingresponse已重拟合或新CI。 | conditional-spin-control | task-design | exercise conditional_rate_centers | true |
| F23-13 | 作者在negligibleE2假设下给B(M1)=.017(+.011,−.008)µN²，SM0.14为模型/有效g输入，不能把差异或“兼容typicalrms”认M1已唯一测定、band模式或δ约束。原B提取/联合branch细节仍需完整producer。 | reported-strength-and-model-boundary | direct-author-model | main PDF3 B(M1)paragraph | true |
| F23-14 | Figshare两XLSX为图源数据，不等全E710DAQ；mainFig2right三组37/25/37点，7785含fractionalcounts和1e−5点，误差平方近显示counts。此显示规则不证明原净谱是独立Poisson。 | actual-public-data-and-error-role | direct-numeric-data | article.xlsx figure 2 right F3:U39；exercise profiles | true |
| F23-15 | main7785显示区模型/测量总和364.47046/399.100046，直接全区Pearson123.956不等SIgridmin17.1982；Neyman因1e−5点放大。只表明缺matchingfitwindow/normalization/统计合同，不认实验错误或据此换χ²/重报τ。 | graph-replay-boundary | actual-data-crosscheck | article.xlsx figure 2 right K3:P27；SI figure1a；exercise profiles | true |
| F23-16 | SI Fig1a真实37×31grid最小在τ11.3fs/E7.33306MeV/χ²17.1982；Fig1b含τ.31875整31点χ²0，正值域最小3.94375/4.84006/16.4762。零切片原样保留，不当真实optimum或擅补缺值；需producer/grid填充定义。 | actual-grid-and-unfilled-domain-boundary | direct-numeric-data | supplementary.xlsx figure 1 (a)/(b) E2:G1180；exercise SI_grids | true |
| F23-17 | SourceData ZIP MD5/CRC及两workbookhash核；publishedCL列的角色仍需对应图/producer，不能把图误差/模板带与dataΣ混用。复现图源本身不增加独立实验。 | reproducibility-and-interpretation-boundary | direct-file-provenance | source-data-workbook-manifest；source_data-identity | true |
| F23-18 | Zenodo8044973 v1.0.0的34文件全与Git c6a4ff3 blob匹配，含作者标为experiment的409303-entry TreeMaster、AGATA/VAMOS/SPIDER字段，三个tree_results均空。这是已取得真实公开衍生event入口，不认证全DAQ/校准史或原paperjob。 | actual-public-producer-and-data-readiness | direct-archive-and-ROOT-schema | producer-source-manifest；public-root-schema；README | true |
| F23-19 | 发布默认inputs为τ5fs、γ7.333MeV、Ex7.785；main的width extraction分支/CodeA对应分支为空、旧fit段在comment中。当前release不提供可直接运行的完整原τ/Egrid fit脚本；尚未完整code/native核，不以“codeavailable”宣称原CI复现。 | actual-code-readiness-boundary | targeted-code | inputs.dat；src/main.cpp extract_width；CodeA_gamma.C | true |
| F23-20 | MESA/SHIVA ejecta、最大探测距离和未来γobservatories预测为作者模型，不是22Na天文检出或新核寿命数据；meanmassfraction与totalejectedmass不同，模型/figure数据与实验输入分列。 | model-result-and-scope | direct-author-model | main PDF4/Table2/Fig3；SI6–7 | true |
| F23-21 | 后续原34file/native核给真实409303-entry可读快照与publicrelease readiness边界：补lib后原build0，原loader数长/逗号解析及VAMOS scalar输出不回传，fitwidth分支未实现。仅限制publicrelease论文fit复现，不判实际paperproducer/τ/BR错或重算CI；原34hash保留。 | actual-public-producer-companion | native-and-input-audit | EV23-1/2/5/6/8/13/14 | true |
| F23-22 | 后续完整原读Friedman2020作者稿，.65(.08)%含新gas相对p强度及旧I866abs/旧gammafeed；本推荐Bp又合此值，推荐tau也合J04。因此两个omega≈.24不是两次完全独立强度确认，source/responsecounter价值与共享reference分开。 | actual-branch-primary-and-dependence | direct-original-companion | FR20-7/10/12/14/15 | true |
| F23-23 | 作者thesisChapter4完整原读补实测19(1)mmgap、responseσ/SNR与28Si benchmarknormalization/fit窗口；支持publicgeometry而限制backtoback简写的外推。longbenchmark不替本fsfitcoverage，未取得完整原job/Cov。 | same-study-primary-companion-and-scope | direct-thesis | F22-2/10/11/12/13/15 | true |
| F23-24 | 后续新实际ROOT接口查询直接从原XLSX重新取Fig2right key25点，与旧actualrows逐行相同；保持全部displaydomain、未扫描删bin/调门。新问题是统计/误差合同，不把同图重算计独立实验。 | actual-graph-new-interface-query | direct-source-data-and-native | figure2right K/L/O/P rows3–27；graph-root-result | true |
| F23-25 | 同25display值建indexedTH1D，仅求和载体：原model无Sumw2 fallback时autoUU/LL41.654553；显式zero模板variance时autoUW/LL110.195944。各合同均未恢复真实MCvariance/原job，LL不是新likelihood开关。 | actual-interface-contract-sensitivity | native-ROOT-on-graph-values | graph-root-result native_cases0/1；RCT26-2/3 | true |
| F23-26 | 同displaydomain归一α=399.100046/364.47046=1.095013423；fixedmodelPearson110.195944、Poissondeviance95.748411。重新把归一内容当sqrtvariance的fallback给UU43.206006；这是声明误差合同变化，不是只normalizer的物理效果。 | normalization-and-variance-contract | actual-graph-arithmetic-and-native | graph-root-result native_cases2/3 | true |
| F23-27 | 以假定原variance=M再actualTH1.Scale(α)，sumvariance=α²sumM=437.019908，强制UW保持原47.939784；auto换UW不等同一检验不变量失败。原模板error未知，此仅配套缩放控制，非MCstat估计。 | consistent-error-rescaling-control | native-on-actual-graph-values | graph-root-result native_case4 | true |
| F23-28 | 上述完整display合同均未复现SI17.1982，returnedp/ndf24及lowcountigood不解释为实验检验或两物理fit自由度。fractionaldisplay/1e−5点与未知MC/原mask阻止选择最接近的统计量冒原τfit/CI。 | original-fit-readiness-boundary | synthesis-with-actual-input | graph-root-result；F23-18/19；RCT26-5 | true |

## Analytical Reconstruction and Self-Audit

[来源前回忆](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-before-source.md)、[真实数据前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-before-source-data.md)、[练习合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2023_source_data_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-exercise-result.json)。两体β/γ Eq3–4点反演在声明角度/速度控制下闭合；没有认证α校准/SRIM/事件选择或新的τCI。

在仅p/γ通道和固定J7/2时，`omega=g(hbar/τ)BRp(1−BRp)`；必须把百分数转为概率，.66%是.0066，不是.66。推荐BR的名义逆方差平均(.68/.17与.65/.08)给.65544(.07239)%接近作者.66(.07)，但原共享Cov/系统处理未得；不借这个打印平均证明所有measurement独立。

## Competing Interpretations and Limitations

公开图数据与release事件显著改善readiness，却没有直接关闭原fitwindow、normalization、背景Cov、有限MC、系统项与recommended组合统计。全显示区χ²不闭合和零grid切片必须先查actualproducer，不能当原实验矛盾。后续代码审计只对原release实际路径负责，另名诊断/改模型必须分开，不修原input冒作者结果。

旧BR约3.7%与新.68%涉及不同β/γ与直接p分析；2020GADGET原件/identity/背景应另读才判断旧根本原因。新τ近旧值、低BR和假J7/2共同形成作者推荐强度；任一项不能单独认证唯一J、M1/E2或模式解释。

## Knowledge Impact and Learning Decision

`revises`沿用旧3.7%分支或以寿命相容推强度不变；`supports`独立事件级velocity差测量与真实公开data/producer核；`limits`作者“rate wellknown”、低χ²和codeavailability对完整联合CI的保证。新claim均needs_review，无human-reviewed；本session数据审计/中心算术不是新实验测量。当前仍Day17原窗口内Day18无学分知识预习。

## Extracted Pages

[[kirsebom-2016-23mg-dsam-lifetimes]]、[[saastamoinen-2011-thesis-al23-proton-response]]、[[nndc-2021-mg23-lifetime-strength-reference]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]。

## 原publicrelease后续：真实data可读，paperfit仍需版本桥

[[evasions-2023-public-release-native-readiness]] EV23-1–14已完整核主要source/native边界：原build补输出目录可成功，但loader输出/逗号解析与VAMOS scalar按值、fit分支未实现阻止完整paperfit复现。真实derivedevent查询409303条、maxtrack7、Si_dE>0的7933条只为输入/门descriptor，不是新BR或论文fit。保留本页F23-19当时partialcode状态，不把release问题直接归实验。

## Friedman2020原件补充：推荐组合的共享源

[[friedman-2020-gadget-al23-proton-branch]] FR20-1–16实际完整读作者稿，确认引用.65(.08)%并非全新绝对pγ重测。newgasratio配旧I866abs及gammafeed，再用J04tau给omega≈.24；本论文推荐组合复用这些输入，数值相近不增加两次独立omega确认。

## Chapter4实际输入：geometry与验证域

[[fougeres-2022-thesis-evasions-response-contract]] F22-1–15在本session完整读作者thesisChapter4(非全201页)，实测19(1)mmgap与responseσ/SNR定义比本paper简写更具体。28Si测试用独立归一/fit窗口且只验证其条件longlivedcase，不能移作本τ/Eγ0grid或zeroCov保证。

## 真实显示数据的ROOT统计合同查询

[新问题前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-graph-root-before.md)、[配套variance控制前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-graph-root-rescale-before.md)、[输入合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-graph-root-contract.json)、[程序](../../system/scripts/day17_fougeres2023_graph_root_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-graph-root-result.json)。

原XLSX全25点/作者displayerrors逐字节hash与旧表逐行对齐。TH1D横轴为点index，只是逐点和的接口载体，不推原bin边界。source没有modelerrors，fallback与zero均声明假设，不能称其中一种是原MC统计。source输入/curve未改，ROOT的低count/forcedUU告警保在[stderr](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-graph-root-stderr.txt)。无窗口搜索、原τ重fit或CI。

只改content而让GetBinError重新取sqrt，会改变effectiveMCstat；另actualScale一起缩variance的对照说明为什么normalizer与errorhistory要共同保存。该新native查询不提供额外独立实验或原paperfit吻合，不把某个结果接近图中χ²/ndf当作job已识别。
