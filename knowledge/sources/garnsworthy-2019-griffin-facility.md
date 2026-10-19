---
type: source
title: "Garnsworthy等2019：GRIFFIN装置、实际偏振标定与响应边界"
title_original: "The GRIFFIN Facility for Decay-Spectroscopy Studies at TRIUMF-ISAC"
aliases: [Garnsworthy 2019 GRIFFIN facility, GRIFFIN 1809.07183]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: instrument-paper-and-calibration
reading_depth: deep-read
authors: [A. B. Garnsworthy, C. E. Svensson, M. Bowry, R. Dunlop, A. D. MacLean, B. Olaizola, J. K. Smith, et al.]
year: 2019
journal: "Nuclear Instruments and Methods in Physics Research A"
volume: 918
pages: "9-29"
doi: "10.1016/j.nima.2018.11.115"
arxiv: "1809.07183v2"
data_version: "arXiv v2 dated 2018-12-06; PDF footer 2018-12-10; VoR metadata2019"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "Garnsworthy et al., NIM A918,9-29(2019); actual body arxiv1809.07183v2"
source_url: "https://arxiv.org/pdf/1809.07183v2"
raw_file: "raw/papers/gpt/day17/garnsworthy-2019-griffin-facility-arxiv-v2.pdf"
raw_sha256: "b257eb66cf822ef9c8e476125ac8d00979df340b5567baa62f72ca4ff4ef16ed"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [60Ni, 207Pb, 56Fe, 66Zn, 198Tl]
reactions: []
experiments: [triumf-griffin-compton-source-calibration]
models: [Klein-Nishina-response, GEANT4]
observables: [linear-polarization, quality-factor, angular-correlation, detection-efficiency]
methods: [Compton-polarimetry, event-mixing, gamma-gamma-angular-correlation]
tags: [GRIFFIN, clover, polarization, source-calibration, response]
---

# GRIFFIN：实际标定、角度角色与软件版本分开

## Bibliographic Record

Crossref按精确title实际HTTP200核DOI、104作者、*NIM A*918、9–29、2019年2月；arXiv元数据和实际PDF identity相符。正文证据来自36页[arXiv1809.07183v2](https://arxiv.org/pdf/1809.07183v2)，侧栏日期2018-12-06、PDFfooter2018-12-10；没有把它说成已取得期刊VoR或已逐字比较版本。OA原文下载由nature-downloader的单个确定arXiv URL完成，未触及认证/host/globalconfig。

原件真实缓存在repo `tmp/day17-griffin-facility/PDFs/`，SHA-256如frontmatter，raw归档槽未填；[downloadreceipt](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-facility-download.json)保留URL/hash/bytes/36页。Bib中未匹配到唯一key，未改用户Bib。本文与2013/2014同名早期介绍、[[smith-2019-griffin-angular-correlation-analysis]]以及当前[[grsisort-2026-compton-polarimetry-code]]是不同对象，不依名称认定同一experiment/producer。

## Scope and Reading Depth

本session另冻明确承认旧Co60/GRSISort和metadata priming的来源前回忆；完整读36页Sections1–7及reference list，核Figs1–28、Tables1–8、Eq1–12的主线和相关误差/limitations。所有页面图像均检查，PDF18/22/23/24另以高分辨率核Table7、Eq5/6、实际Q数据与Fig18–20；Table2几何和Fig15 caption也已检查。没有逐篇打开67条引文，也未把其它fast-timing章节当Day18正式卡或新实验重分析。

本文原数据包含装置校准与多种示例；本任务仅以可追溯摘要/图表作L2重算和L3 response合同，不恢复其TTree、逐门峰/fitΣ或当年producer。后续未取得的Ref40 Alikhani2012正文不以本篇引用冒充直接已读。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GF19-1 | 装置16个clover、64晶体；11cm高效率与14.5cm优化peak-to-total是不同配置。PACES需要移除一个clover；Fig15效率实际caption为60晶体/15clover，不能把所有benchmark都当同一16clover/抑制选择。 | instrument-configuration-boundary | direct | PDF3 Fig1；PDF9 Table1；PDF14 Sec3.7；PDF20 Fig15 | true |
| GF19-2 | cross-talk以E′1=E1+α12E2、E′2=E2+α21E1建模；例子用1332±15keV sum-gated点拟合得α12=.0024、α21=−.0092，跨pair可异号，不能仅以一项全局scale代逐pair correction。 | calibration-model-and-observation | direct | PDF15–16 Sec4.1.1/Fig10/11/Eq1/2 | true |
| GF19-3 | summing empirical方法利用所述γγ角关联关于90°的对称及近似同晶体响应，用180°符合估0°summing；它不是对任意particle/gate/array的无条件恒等。Table7的photon概率还需1/(1+α121)，不能把total decay当光子。 | counting-normalization-and-conditions | direct-and-self-audit | PDF17–18 Sec4.1.3/Table6/7 | true |
| GF19-4 | PACES/ZDS、11cm、无Delrin的Fig15配置在1MeV给singles10.06(11)%、clover-addback14.20(16)%；60Co activity约1%用于absolute normalization并作summing修正。它们不是Q或Compton选中事件效率。 | efficiency-denominator-boundary | direct | PDF19 Sec4.1.4；PDF20 Fig15 | true |
| GF19-5 | 作者以64²=4096含self的ordered crystal pairs计52组Θ差，Table8保留两类几何的86.2/93.8重复近值；66Zn0→2→0的1333.1/1039.2示例需finitegeometry，引用Smith方法。该验证不自动认证偏振响应或当前软件。 | angular-response-and-lineage | direct | PDF19–22 Sec4.1.5/Table8/Fig17；PDF34 Ref38 | true |
| GF19-6 | Eq5以polarized/unpolarized Compton分布比定义A_CE；Θ为两γ方向夹角、ϑ为Compton散射极角、ξ为两个平面夹角。Eq6实用定义A(ξ)=.5 Q(E)Pγ(Θ)cos2ξ，不能套成ST99/SG98的同一个计数A或同一个Q。 | observable-and-coordinate-definition | direct | PDF22 Sec4.1.6 Eq5/6 | true |
| GF19-7 | 偏振事件为同clover两晶体Compton＋另一clover第三γ；无偏振参考来自event mixing。作者称49个独特ξ，并对cloverpair施90°选择，对应其晶体Θ约68–113°。ξ角组数量不能直接替Table8的Θ权重或任意新版geometry census。 | event-and-angle-selection-contract | direct-and-self-audit | PDF22–23 Sec4.1.6 | true |
| GF19-8 | source采用60Co cascade中1332-keV E2的nominal P90=1/6标定16clover Q(1332)=.240(.012)。Fig18a/b是同一数据的未分组/8个选择分组，不增独立实验；部分稀疏角组合被排除。 | actual-calibration-and-dependence | direct | PDF23 Sec4.1.6/Fig18 | true |
| GF19-9 | source其它能量报告Q570=.390(.024)/207Pb、Q1173=.258(.012)/60Ni、Q1771=.201(.045)/56Fe，与从1332按Ref40缩放的Fig19曲线比较。原始calibration/gate/fitCov及曲线跨能量Σ未给，不能以三点独立χ²作实验显著性认证。 | reported-validation-and-readiness | direct-and-self-audit | PDF23 Sec4.1.6；PDF24 Fig19 | true |
| GF19-10 | Fig20a观察1064-keV M4(+E5)散射、门570；Fig20b反过来观察570-keV E2、门1064，折叠关于90°。它与570-keV Q检查复用207Bi源/cascade，γ的emitter为207Pb；两个角色不裸交换，不算两份独立证明。 | reference-role-and-source-independence | direct-and-self-audit | PDF23–24 Sec4.1.6/Fig20 | true |
| GF19-11 | 作者称所研究校准中减少clover数不改变Q但降低统计；它属于该测量条件，不能推出任意target/gate权重迁移无偏。其近两倍sensitivity优势亦有具体quasi-continuous/经典法比较对象。 | author-report-and-transfer-boundary | direct-and-self-audit | PDF22–23 Sec4.1.6 | true |
| GF19-12 | 论文说明实际实验每次约1–15TB/2–10天且另复制保存；本轮未取得真实event/矩阵、实际producer版本或完整Σ。当前2026 GRSISort source/默认Q备注不认证本篇2018/2019的执行路径，局部代码问题也不裁决论文数据。 | data-and-producer-boundary | direct-and-self-audit | PDF8 Sec2.7；PDF22–24 calibration scope；GRS26-6/10/13 | true |
| GF19-13 | 本任务把原四点与当前fixed generic ScaleQ正向角色作条件比较，570/1173/1771预测约.378202/.259795/.198649；不称重放原Fig19 producer。共同1332误差产生rank1曲线Cov，缺实际measurement crossCov时不报新CI/χ²显著性。 | bounded-summary-code-comparison | task-calculation-from-direct-source | PDF23 reportedQ；PDF24 Fig19；griffin-primary-calibration-result | true |
| GF19-14 | Table7字面中央参数给summing≈10204.872、仅独立area/efficiency传播σ≈121.016；打印half-last-digit盒约10183.221–10226.535包含源10201。未舍入/实际Cov未得，不称全errorbudget恢复；漏ICC则21991.5，放大2.155。 | bounded-published-table-replay | task-calculation-from-direct-source | PDF18 Table7与邻式；griffin-primary-calibration-result table7 | true |
| GF19-15 | 固定GRSIData原GetPosition带45mm interaction-depth、26mm transverseoffset，原样ROOT执行的110/145两距离128个位置/256方向均在Table2±.05°内，最大差.04192°；另名减45mm front控制可差7.7406°。相合只核该坐标合同，不认证真实相互作用深度或原producer，原front-face措辞仍需字典。 | coordinate-definition-and-replay | actual-pinned-code-and-source-table | PDF9 Sec3.2/PDF11 Table2；TGriffin.cxx329–360；griffin-geometry-result | true |
| GF19-16 | Table8保持52个角/重数类合4096；当前native110mm同样52类，但印113.4/152.3/160.2分别对不上native113.5/153.3/161.2。独立Table2打印中心的最近角距后两行约.958/.943°，超过明示同几何假设下.25°保守舍入外界。保留partial/原表，不认sourceerratum或实验失效。 | bounded-table-consistency-boundary | direct-source-and-task-calculation | PDF21 Table8/PDF11 Table2；griffin-geometry-result table8_comparison | true |
| GF19-17 | 共同nativeclover-axis90°的64个orderedcloverpairs，在110mm晶体点Θ约67.456–112.544°、145mm约71.431–108.569°；只是给定点geometry的census。本文source约68–113°与当前helper默认145mm需分别记录，不能默认为已复现原calibration切选或从角计数算Q。 | angle-role-distance-and-acceptance-boundary | source-and-conditional-geometry | PDF23 Sec4.1.6；Helper.hh10/76；griffin-geometry-result census | true |
| GF19-18 | 另获arxivv1原33页但仅定向identity、PDF10 Table2与PDF21 Table8/图像；涉及113.4/152.3/160.2及caption的条目与v2相同，不计独立实验。Publisher发现无PDFcandidate，公开TDM默认200仅metadata、FULL401，仍未取得VoR body，不能称出版商角表已核或更正。 | version-and-access-boundary | direct-targeted-version-and-access | arxiv1809.07183v1 PDF10/21；griffin-v1-targeted-version；public TDM attempts | true |

## Summary

这份完整装置论文提供当前public code之外的实际校准锚点、三能量检查和明确的θ/ϑ/ξ/half-factor合同。作者直接报告的Q/计数曲线、nominal P参考输入、模型缩放和当前任务推断分别保留。[[triumf-griffin-compton-source-calibration]]集中保存可复用的measurement ledger/输入缺口；[[compton-polarimetry]]与[[polarization-sensitivity]]中的Q使用仍需带具体response定义。

## 本任务的量化、核验与认识修订

[输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-primary-calibration-input.json)、[程序](../../system/scripts/day17_griffin_primary_calibration_replay.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-primary-calibration-result.json)保留publishedsummary、PDF/code/script/hash和actual C++ ScaleQ执行。原源参考式给A0=.5×.240×(1/6)=.020，σA0=.001仅来自Qσ；从同A/Q回代不能独立验证P90。

当前固定generic代码的正向能量角色给下表；它不是认证原Fig19算法/geometry的actualproducer。

| E/keV | 源reportedQ(σ) | 当前kernel×源.240的条件值 | 源值减条件值 |
| --- | --- | --- | --- |
| 570 | .390(.024) | .37820235 | +.01179765 |
| 1173 | .258(.012) | .25979461 | −.00179461 |
| 1332 | .240(.012) | .24000000 | 0，标定回代 |
| 1771 | .201(.045) | .19864887 | +.00235113 |

若只传播独立anchor的σ=.012、缩放因子s_i固定，则曲线Cov_ij=.012² s_i s_j，三validation点共用rank1分量；这是声明的条件敏感性，不是实际Σ。1173与1332同60Co source family、570与Fig20同207Bi cascade、Q本身由A/nominalP推得的依赖必须另核。没有统计显著性、new Q拟合或新P/δ。

Table7的formula为A245 ε122/[16(1+α121)]。按打印值得10204.872、源10201，末位rounding盒相容；σ121.016只在area/efficiency独立且α固定等条件下接近打印121，不证明真实calibration Cov已得。它说明photon/total-decay分母在实际count calibration中的影响，不以更多toy消除原输入缺口。

## Competing Interpretations and Limitations

### 坐标点定义与Table8复现的未决项

[分析前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-geometry-before.md)、[typed Table2/8](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-geometry-table-input.json)、[原样geometry执行](../../system/scripts/day17_griffin_geometry_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-geometry-result.json)固定paper crystal1–4→native0–3、detector1–16身份，未拟合旋转、置换或深度。source Table2按三ring模板的64行/两距离录入，与所有打印方向核对；native的静态array和GetPosition body原样抽取，ROOT6.40.04编译/run0。

两距离128个native位置的θ/φ共256项均在打印±.05°内；这一结果把“距离相同但基点不同”的问题收紧：source表的方向与native的most-likely interaction point一致，而不是本任务另定义的减45mm front-face控制。原文Sec3.2及caption使用front-face中心措辞，但实际physical crystal面、代表相互作用点和producer字典没有由这种数字相合完全恢复，不能称测到了深度45mm。

Table8先前“全打印表匹配”的初代码假设已被实际Counter对比否决，失败snapshot/分类记录保留，原科学输入不改。源113.4(64)、152.3(64)、160.2(128)三个角类与当前native末位/1°差别已高分辨原图再核；两组86.2/93.8的不同geometry也未合并，native近86两值相隔.00920835°，没有认证caption“same to four decimal places”。

为区分新旧producer和打印内在条件，另从**原Table2打印中心本身**求所有4096pairangles。每方向沿θ后φ的误差路径上界为.05+.05=.1°，pair角误差由球面三角不等式≤.2°；加Table8自身±.05°，给.25°保守外界。在“两表指同一几何点”的附加前提下，152.3/160.2最近Table2中央角仍距.957736/.943429°，超过该界；113.4未由此界排除。不同点定义、未舍入历史输入/producer或源打印版本尚未核，故只立复现边界，不给sourceerratum、实验角度修正或新的P/Q结论。

原程序的compile/run与结构/身份检查可通过，同时scientific_replay_status仍为partial；没有把检查绿灯等同于Table8完整复现。下一真实输入是historicalgeometry/producer与unrounded Table2/8角色，而非自由调cp/id或改角表追通过。

为核版本，另合法取得arxivv1（33页，SHA-256 `fb2be20c273bc258d895e074231d61baaef37fa5f423e5f147a2a942b1b924c3`），实际只读identity、PDF10的完整Table2和PDF21 Table8/caption及两页高分辨图像。相关角/重数/脚注与v2相同；没有把v1整篇标为read或增加实验独立性。[版本回执](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-v1-targeted-version.json)保留范围。

出版商accessdiscovery的landing200没有PDFcandidate；Crossref公开TDM默认view返回200却只有22个XML elements/metadata、无body/table，不能当全文。显式FULLview为401，未重试该权限终态或修改凭据，VoR仍未取得；因此本页未对出版商版本作角表结论。arxiv两个版本相同只收窄版本差异路线，不消除geometrypoint/实际producer边界。

Ref38的[[smith-2019-griffin-angular-correlation-analysis]]原28页v1本session只定向重核PDF3 Table1/caption/Sec2（高分辨原图）与PDF4 Table2/数据与kernel合同，原hash仍`0390bdbb6b78f035d1d49abd4ecf863a684f3a8eb3ba6c537cfbd8fb6e352f33`；相同三行/脚注在那里也有（SG19-18）。这是共享geometry表谱系，不是独立实验纠错。该source旧17条claims/flags保留，未把本次targeted范围说成28页新的fullread；旧公开simulation归档NDA缺口仍限制历史producer重放。

- P90=1/6是source采用的已知参考输入，不是本篇从已校Q又独立测到的P。finitegeometry/gates与empiricalQ一起构成合同，不能固定Q只改P平均或删.5。
- Q=.240(.012)与当前代码comment的.2509不相同；源版本、采集、选择和Cov未绑定，不能仅比数值判统计冲突或历史producer错误。
- Fig18选择8bins、舍稀疏角、Fig20折叠和Fig19多能比较的rawcounts/fitSigma未取得。对现在代码进行设计fixture测试，不能恢复这些原始分析。
- 所读正文无真实event/response公开文件清单；这只是本次readiness，未宣称全部合法入口穷尽。Ref40/旧实验引用不因本篇summary就算直接核验。
- 15clover效率、16clover偏振标定、11/14.5cm、PACES/SCEPTAR/absorber与suppression必须逐项核。当前完整读其它fast-timing/未来polarized-beam章节仅作主线理解，不额外计课程信用或将预期设备说成2018已测性能。

## Analytical Reconstruction and Self-Audit

| 项目 | 判断与依据 | 状态 |
| --- | --- | --- |
| 原件身份/版本 | DOI/Crossref metadata104作者与arxivv2/PDFhash；VoR未逐字比较 | self-audited |
| 实测与model输入 | Q由known-P calibration，能量曲线按Ref40缩放；源P/Q/A不独立 | self-audited |
| 当前代码对照 | 明确2026 pin与2018采集未绑定；Lean/newAnalyzer不同path | remains-open |
| 实验L4 | 无event/actualresponse/完整Σ/producer，保持not-ready | remains-open |

## Knowledge Impact and Learning Decision

`supports`实际参考/角组/half-factor与response链；`revises`仅有代码comment就已有实验Q的认识；`limits`同数据分组、回代或新版函数对旧测量的“独立验证”。本篇各校准/应用例子按数据来源分层，与Smith角关联或Alikhani方法引用不重复计独立实验。Codex self-audit，新claims全needs_review，无human-review事件。

## Human Review Triage

P1：论文级采用具体Q/符号/δ或跨阵列迁移前，核matching reference/门/θ/threshold、原fit/Σ与producer。当前是完整研究学习，不把未取得的输入自动派给用户审核。

## Extracted Pages

- [[triumf-griffin-compton-source-calibration]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]、[[detection-efficiency]]；与[[smith-2019-griffin-angular-correlation-analysis]]、[[grsisort-2026-compton-polarimetry-code]]保持方法/版本谱系。
