---
type: learning-daily
graph-excluded: true
created: 2026-10-18
updated: 2026-10-19
---

# Day16：DCO/RDCO、混合比与符号约定

## Run state

- run_id: `2026-10-18-day-16-01`
- run_date: `2026-10-18`；timezone: `Asia/Shanghai`；day_index: `16`
- schedule_id: `wiki-daily-learning`；project_root: `/workspace/wiki`
- phase: `angular-correlation-polarization-and-mixing-ratio`
- session_id: `01a14ce6-425e-77c1-a127-2ac980bd76b5`
- resume_command: `codex resume 01a14ce6-425e-77c1-a127-2ac980bd76b5 -C /workspace/wiki -s danger-full-access -a never`
- original overnight_until: `2026-10-19T15:00:00+08:00`；15:00–16:00仅收束。
- status: `running`；用户明确恢复原研究窗口，Day16已获学分保留一次，研究持续到2026-10-19 15:00上海；前次提前收束记录保留为历史。
- completed_day_indices: [16]
- partial_day_indices: [17]
- Day 16 card audit: complete

原始回执为[run.json](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/run.json)，本次按用户指定固定日报路径保留文件名中的20261017；实际run_date与截止按runner注入的20261018回执，不从旧预备段落延长或缩短。课程已依据本session独立交付与实际publication005对账为next17/count16，只计Day16一次。Day15 partial16、旧分数、旧程序检查不计本session学分；13:00上海按原时间门开始恰好Day17知识预习，只列partial17，不正式计17，未打开Day18。首个科学checkpoint时尚未授分；随后已正式计16一次，用户恢复后原run/goal继续active。

启动已核README/index/profile/PLAN/active handoff、学习workflow、三份计划与矩阵Day16。入口工作树存在旧Day8/9/13/14/15回执、log和daemon脚本修改；[entry-baseline.json](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/entry-baseline.json)保存完整状态、620份knowledge快照与保护文件hash。首写前boundary exit0；EOL清理在首批回执/回忆写入之后、科学写入之前执行，恢复0份、index为空，明确这一执行顺序，不伪称所有H1步骤均在第一次输出写入前完成。

### 用户恢复原研究窗口

2026-10-18T16:31:18.642920+08:00，用户明确要求持续学习至次日下午15:00前。同run/session重新开放研究，原deadline不变；课程next17/count16与completed16/partial17保持，不重复授分。前次局部证据饱和不足以结束整段窗口，此后检查新的高价值primary路线，不以重复toy填时段。恢复baseline、primed假设冻结和原学分状态见本run的reopened-baseline-001.json及reopened-source-before-freeze-001.json。

### 主动回忆与本session独立交付

[冻结回答](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/active-recall-frozen.md)在`2026-10-18T10:48:08.995961+08:00`冻结；[时间/hash回执](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/active-recall-freeze.json)给SHA-256 `472fe5d580944117ff5bd57606ddd5c3509c0fdb0b54af60ccc9914dbc19c523`。已暴露prompt中的Day15索引、交接和课程卡，明确primed，不称盲测。此后才打开本日source/raw和旧详细worksheet。

回忆正确保留了gate/target、实δ双根、pure-limit盲区、Cov和matched P/Q边界；当时尚未知道本日178W两组数据的实际角色，也没有从记忆认定KS70与D96应同号。之后的原图/定量核验补上这些具体内容，不用旧预习成绩代替本session验收。

### Day 16 card completion audit

| 课程交付 | 本session实际证据、artifact与locator；适用边界保留 | 状态 |
| --- | --- | --- |
| 来源前主动回忆/priming冻结 | [冻结回答与时间hash](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/active-recall-freeze.json)，新session16；不是盲测、不用Day15旧分数 | complete |
| 主来源完整主线/关键原件 | [source-reading-audit](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/source-reading-audit-001.json)：D96 518–525 Eq1–21/Figs，KS70 724–734 Eq3–19/三表；KF89/BT87及独立KO01原件实际覆盖 | complete |
| 明确数据身份的delta-double-solution-sheet | [178W知识单](../../knowledge/research-notes/w178-921-dco-gate-double-solutions.md)；KF89-15/16/17/18、printed338 Fig7c/d，冻结input与新allroots audit；actualdata/authorbranch/conditionalmodel分层 | complete |
| 两相位约定与pure/错误控制 | DR96-5、KS70-5/6/7/13；原图Eq4b负号/先后B-A角色/BR与RB身份；新F/fulltensor、同步S变换/pure端点盲区核验见kf89-w178-921-audit.json | complete |
| 反证、matchedcompanion与sourceindependence | P97-2/3/5/8，实际primary电子装置/50–400ns与K表、290KICC/timing后续修订；N178-12与KB08-D16-4，缺actualΣ/response时不新测δ；KO01-11未解支保留 | complete |
| 理论/定量练习与来源后复述 | 角色倒数/CovJacobian、两相位变换、actualfull-rank/approximationinvariants、KO01独立双ratio；[口试复述](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/day16-post-source-oral-recall.md)不造盲测成绩 | complete |
| canonical写回/报告/检查/续接/显式发布 | 本session科学001–004均实际H3/Gitee发布，唯一writeback按entrysnapshot验证；[verification008](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-checkpoint-008.json)lint/boundary/diff0；当前续接与准备的下一正式Day17prompt存在；预习/收束余项继续按同门发布 | complete |

正式学分只属于16；表中完成依据是本session已完成并发布的Day16交付，非Day15partial16。Day17仅知识预习，既不列completed，也不跨过它推进课程。课程已按science publication005与真实检查对账为next17/count16；最终精确hash和远端结果只记run receipt。

## Candidate pool and selection

恢复窗口当前选择仍为GRETINA source/偏振response的continuity问题，Riley2021是必要companion原件；没有新增第二novelty或课程卡。它纠正“仓库公开七quad例就是主体论文数据”的预期，并提供新的物理反证与可核表格。更多MC/终态URL重试不能替原producer或统计ledger；研究窗尚有>11h，下一候选将从实际校准分母/选择/原数据缺口重建，保持partial17、不开18。

| 候选 | 与近期知识重叠/信息增益 | 当前决定 |
| --- | --- | --- |
| 178W921真实DCO两支、921(G)与921 observed角色 | 既有KF89有定义/一般限制，但未保存此数据点的双支和两个门；可查原件并作新反向检验 | continuity主问题 |
| D96/KS70共同BM算符、state ordering与干涉 | Day15已预习，因此本日必须重新核原件，不能只复述旧bridge | 必修约定核查，与实测门角色整合 |
| KF89原表point结果与producer差异 | 新计算暴露部分纯跃迁表值未复现；查exact/high-spin approximation有潜在信息增益 | 下一条当前问题路线，暂不归因 |
| Dors1979的169/137参考输入 | 原文Dors[3]/Refs2/3冲突；可独立追准确身份、定义和误差 | 当前追源，未因缺全文停止其它路线 |
| 135Pr/129Ba真实response/Σ | 核心影响高，但Day15已记录缺口；重复toy或原样重试终态失败不增加信息 | 保留候选，需新可用primary/数据才提升 |
| Day17 P/A/Q与真实polarimeter response | 13:00上海按timegate开启唯一下一卡知识preview，SG98actual表/响应已核 | 仅partial17；其原producer/fit-calibrationCov仍缺，正式17需新session独立逐卡 |

本轮初始continuity为W178/相位，novelty后来选独立130Ba三角度实验；仍只是一项continuity与一项novelty问题。后续恰好Day17知识preview单列，不授正式学分。最新checkpoint时钟为2026-10-18T12:00:09+08:00，距原硬截止约1619.85分钟；原截止不改，当前K-shell/primary路线仍有信息增益，继续研究。

## Sources and evidence

### Checkpoint027：60Ni/60Co官方reference与原引用链

新增canonical [[nndc-2013-ni60-co60-reference-records]] N60-1–11（[文件](../../knowledge/sources/nndc-2013-ni60-co60-reference-records.md)）；NNDC60028001/002精确对象/hash、β−完整140行与Adopted定向阅读范围已记录。MR−.0025(22)误差为.0022；Adopted→β−→1980Kr05是共享谱系，不计两次独立实验。NSR正式接口/Crossref核原题名、作者、NIM169573–576、DOI10.1016/0029-554X(80)90959-3；低温Co60/Feγ角分布的评价/metadata与原正文分开。publisher403/API仅coredata、HAL0/ADS拒绝/Scholar超时保留，不补原operator/phase或Cov。

[固定列/反冲/共享误差结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ni60-reference-audit-result.json)：实际SDK质量、同对象Ex→restEγ扣recoil、两对象差异/RI归一和理论CC分层；conditional pointP差的δ-onlyσ=.0008203509，对比错误独立.0023719382。不是实验P/CI或新的δ测量。

[实际SDK分支读取](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ni60-RDM-pair-consistency-corrected-result.json)：Ig(1+CC)总分支归一，pair .9983894029与同模型100k99840/99845相容。初gamma-only归一试算已invalidated、未入canonical数值；source/模型相容性不认证真实Q、历史producer或primaryphase。脚本编译/执行实际0，原输入不变。


### Co60 point-reference conditional Stokes：相同极限与轴平均

UG24-30–34及[canonical benchmark](../../knowledge/research-notes/co60-gate-role-response-benchmark.md)保存新joint两光子密度模型、先冻结的源/轴/相位/门假设和失败控制。pureE2 4→2→0在理想point gate且不观测reference helicity时，first/last P_parallel在90°同为1/6；actual小M3输入给.1652824009/.1643540933，不把角色不同概括成physicalP必不同。

native/RB同步转换、pure上极限globalphase、W两角色一致、Rz/独立intermediate-density核≤8.89×10^-16；130个fulljointPSD/Hermitian/trace和12个referenceplane spin2控制通过。v1只构造AA†并核reduced态，v2补显式fulljoint检查/轴旋转，未改原level输入；结果均保留。

纯模型闭式P=(1−x²)(4−x²)/(24+3x²+x⁴)、P60=45/397，局部W加权P平均19/189而共同目标轴的无gate reference积分恢复无偏振。freeelectronKN单点ψ90°即使同P也因E不同给contrast.064118/.057773；所有这些都是条件设计/推导，非关闭polarizedEM的MC photonStokes、arrayQ、实验P或δCI。

### Co60目标／门与native角关联控制（本批100k已实际通过）

[canonical Co60 benchmark](../../knowledge/research-notes/co60-gate-role-response-benchmark.md)及UG24-19–27新增原例完整主线、actual十二quad/noPOL、native correlation开关、Ni1173 E2/M3 δ配置与source/target/gate矩阵。两组1000 run/native0；完整truth pairs999/994、rawdetector pairs7/4，缺失占位1/6被显式排除，不从微小样本拟Q或精确angular W。

两条独立角动量代数路线对实际mixed输入给a2=.1005293099/a4=.00940581308，native/RB配套转换、pureE2极限与官方F/F3 contraction核到1.48×10^-15。48静态矩阵units/index核，数值差非PSA分辨率。backflag actual1k每晶体/prefix/eventwide103/123/166与78/89/126，源bank倒序改变48/35个history的prefix标签；未映射原论文producer，不重算实验back fraction。

各100000 history/新seed/分母/门/momentCov已冻并通过run/native/angle分析；source完整pairs99840/99845，a2=.105902±.007183/.006829±.007092，a4=.007674±.009631/.008455±.009514，预定mixed/iso0的条件2D比较相容。detector rawpairs507/549、比值SE.135–.245，非精确W或Q（UG24-28/29）。2017 companion仅metadata，正文访问边界具体保留，不计新科学证据。formal16一次/partial17，不打开18。

### Riley2021原件主线：有效响应与Q迁移的边界

新canonical [Riley2021](../../knowledge/sources/riley-2021-ucgretina-energy-response.md) R21-1–18：实际arxiv2104.09986v1全26页主线/参考索引、12图逐一视读、两表和Eq1核。读取前[riley2021-response-before](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/riley2021-response-before.md)已冻并说明公开code/Eu2012/Morse/MC priming，绝非盲测。Crossref/实际PDF身份匹配，VoR body未取得。

原件全阵列为NSCL12quad，公开2012七quad与当前11.4.2/7quad MC分别保留。作者的I/II有效层tuple按同组flood数据不同能区取值；低能效率/continuum没有被一组参数同时解释，quoted stat interval不代表真实被动层精度。fullmodel邻接/后方材料修复最小模型的低能continuum，polarimetry/tracking仍需现实segmentation/partial charge collection。

actualasolid两shape/usePassive/parser/doc核得coax1.5/back2.5/outer.9mm，恰等Table2 II；文件hash不动，不据此认证原12quad或exactproducer。R21 continuum target1172/1173、LaBr gate1332；L25-30 target1333/gate1173，保留γ角色区别。I53/58及3548/3549、Fig7/8(d)caption与实际轴、backfraction归一producer缺口均如实留source。

### G411源模拟checkpoint023：记录兼容与实际源框

新source [G411重放](../../knowledge/sources/ucgretina-2024-geant4-11-source-replay.md) UG24-1–17保存固定publicsha02e5a924/724blob、actual11.4.2与官方headers逐字节对照、原truth双失败及source-only记录副本。原1000decay程序exit0却1000num全0；仅process名兼容后仍26zero-E槽。另名denseappend只记录实际callback，原source不改、beta/boost未认证。

同种子γ/decay各1000history的183/349条有效CRYS逐位不变，decoder exit0。新的实际导航反证是：原decay preinitialize源框下Eu152从Target出发且无有效POLYETHYLENE；只移源框到initialize后，从euTape出发。新几何1000decay为367条CRYS/287探测history，decoder0；不作paired显著性或历史response认证。原六个GeomMgt1001及decay PART102按精确warning块保留，不当全几何已闭合。

[源响应note](../../knowledge/research-notes/gretina-eu152-source-response-replay.md)保存event分母/有效字段/几何与实验Q的分层、fixedN和compound-Poisson有限MC矩阵推导。各100000history/新种子/四区/无smearing或fit已前置冻结并实际通过run/native/history检查。γ/decay分别20431/32976条CRYS，四区counts为(2364,555,0,0)/(3611,850,3,0)，高区结果仅限该模型（UG24-15–17）。此为partial17，不另授卡，不开18。

### NSCL公开Eu152实际ROOT与sorting/decoder

新增[公开data source](../../knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md) UE12-1–11。EuREADME/Fit/macros、三sorting主线完整读，GRUT固定2020对象只读Build/Sort/GetIP目标链。两ROOT的blob/SHA/ROOTmagic及读后hash实际核，PyROOT6.40.04读所有keys、egam及角hist descriptor；原ROOT/raw不改。它们是2012七quad source/background processedhist，非Morse六quad或L26十二quad/FMA的数据。metadata2013保存时间不当科学采集日期。


### UCGretina公开代码与Geant4原函数

[代码source](../../knowledge/sources/ucgretina-2021-polarized-emission-code.md) UC21-1–9：实际GitHub官方tree/blob/SHA固定2026与2021对象，ITDecay436行/Reaction主线、编译门与runtime flags已读；Geant4v10.7.4关键原函数、tensorcopy/MP编码/Stokes轴/KN项定向读。不是全788文件精读或Riley2021论文全文。源码/生成binary只在tmp；SDK为实际11.4.2，旧函数抽取只改class名并依赖该SDK数学服务，不冒称原10.7.4 runtime。


### A=25官方当前对象与2009存档

新增[官方source](../../knowledge/sources/nndc-2025-a25-mixing-reference-records.md) N25-1–10。九个当前对象与旧200908 Adopted子对象均实际核hash/字段；完整读Na BeO142行、Na/MgXUNDL23/25行、MgNRF15行，其余仅定向header/target/MR/reference，不称整188页评价精读。NaXUNDL官方PDF一页已视觉核；2009从官方archive真实目录取得，不再原样重试publisher403。当前评价base202508/cut31-May-2025、期刊2025-10，与202602XUNDL/19-Jan-2026编译分开。XUNDL来自同2026Lo01，不计独立实验。


| 来源/链接 | 本session实际覆盖 | evidence与独立性 |
| --- | --- | --- |
| [D96](../../knowledge/sources/droste-1996-pdco-formalism.md) | 8页全文主线；原图printed519/520/521/524及geometry/σ/结论；DR96-4/5/6 | formalism/作者模型，不是新实验；FORTRAN未得 |
| [KS70](../../knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md) | 11页全文主线；原图Eq3/4/5/9–12、Fig4/TableI–III/Fig5 | 110Cd Ge(Li)实验与定义；25个correlations不是25个独立实验 |
| [KF89](../../knowledge/sources/kramer-flecken-1989-use-dco-ratios.md) | 7页全文主线；原图定义/Table1/Fig6/7/8、实测两行和References | 178W OSIRIS实验；两门、强度比和处理共享数据，reference另导入旧文 |
| [BT87](../../knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md) | 8页完整主线和Eq7/10/12、Fig2/Table1原图 | 高自旋近似/方法验证，与KF89引用有理论谱系，非独立实验 |
| [NNDC178W](../../knowledge/sources/nndc-2009-178w-dco-reference-records.md) | 四个官方选定对象/固定栏与所选AD/Kexp记录 | 评价转述旧采集，不计新实验；raw归档/Bib缺口保留 |
| [KB08](../../knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md) | 13页正文主线+AppendixA/selected W row与实际两次新FO查询 | 理论数据与reported Kexp分层；旧人审prefix完整保留，新claims true |
| [Purry1997](../../knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md) | Surrey112页实际PDF；定向实验/分析主线、原表、目标与反证/summary | primary；与1998paper/评价重复数值按依赖，wholethesis仅skimmed |
| [KO01](../../knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md) | 3页全文主线/原图/TableI40行标签与Fig2例 | 独立offbeam130Ba实验；两个ratios并非两次独立实验，calculatedcoefs不当实测 |
| [SG98](../../knowledge/sources/schmid-1998-gammasphere-polarization.md) | 16页完整主线/原式/三表；44页版仅定向table定位 | 恰好Day17无学分知识preview；版本/同data处理不是独立experiment，fullCov缺口保留 |
| Dors1979 | Crossref核六作者、NPA314(1)61–79、DOI10.1016/0375-9474(79)90555-4；全文未取得 | 元数据可定位177Hf(α,3nγ)，不据题名补写δ定义或当新增实证 |

四份实际raw的SHA-256分别与source页匹配；KF89存大写hex，首个提取器因case-sensitive比较退出1，归一hex大小写后确认同一hash，raw未改。渲染与OCR均在`tmp/day16-source-reading/`；无raw/PLAN/Bib写入。Crossref题名/作者/年份/卷页是外部元数据核对，不替代原件数值和locator。

实测摘要新写KF89-15–18，均needs_review:true。原KF89 page human-reviewed及所有旧claim flags保留；这次self-audit不冒充人审。

## Theory/analysis exercise

### 两光子joint density、pure闭式与参考面spin2

[新joint代码](../../system/scripts/day16_co60_conditional_stokes.py)先构造A(λ1,λ2,Mi)再对unpolarized Mi和reference helicity求迹，未交换物理级联顺序。IQUV的Q_J是光子密度分量，polarimeterQ(E)另定义。native−.0025→RB+.0025连operator相位配套后结果0差；pureM3幅度±global号不影响observable。

[闭式核验](../../system/scripts/day16_co60_closedform.py)实际0，对x=cosθγγ：W=5(24+3x²+x⁴)/126，Q_J=5(1−x²)(4−x²)/126，P=Q_J/W。13角/两角色与joint到3.34×10^-16；∫Wdx=2、P90=1/6。盲平均局部P得19/189，正确commonaxes全reference方向积分Q/U/V≤1.75×10^-16；同target固定轴的reference面旋转满足Q_J+iU_J∝e^(2iφ)。这是“先投影轴/再平均”必要性的明确反例，不能据此否定有既定reactionplane的原paper加权式。

### 60Co整级联相位、实际计数与控制图

[理论脚本](../../system/scripts/day16_co60_cascade_theory.py)与[官方F3收缩](../../system/scripts/day16_co60_g4f3_crosscheck.py)实际exit0，native/RB同步变换和pureE2控制闭合≤1.48×10^-15。actualnative-δ−.0025给a2.1005293099/a4.00940581308；这是固定level配置，不是本日实验δ。

[rawgate/moment脚本](../../system/scripts/day16_co60_gate_audit.py)和[backflag控制](../../system/scripts/day16_co60_backflag_audit.py)处理真实模拟文件；缺失/未唯一γ对排除、固定N与conditional pair N分开，zero支持保留undefined。两组100k最终source moment与预定模型/iso0相容（条件Gaussian D².6023/1.7086），不能反推微小M3相位唯一值或全producer正确。

[控制图SVG](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/co60-control-figure/co60-control.svg)／[PDF](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/co60-control-figure/co60-control.pdf)／[source CSV](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/co60-control-figure/co60-control.source-data.csv)：发射端与detectorresponse两类证据分别显示。Python workflow/backend持久在repo tmp，180×86mm、600dpiPNG、最小字7pt；alignment/font/collision/visual检查通过。初legend布局与static-export语法被QA发现已修，失败trace保留；source final仅WARN有PNG无TIFF（研究笔记合同，无submissionraster声明）。

### Riley2021实际表格、输入参数与Compton机制核验

[response crosscheck](../../system/scripts/day16_riley2021_response_crosscheck.py)在冻结typed原表/版本/hash/单位后实际exit0：Table1 inclusive21×21×13=5733与原文相符，36能量对应nominal206388个网格组合而非独立实验；Table2 II/I的coax/back/outer比为.5/1.25/2.25。当前asolid9/21行经format/parser/usePassive核，coax1.5/back2.5/outer.9mm对应II数值，未改输入去追旧fit。

free stationary electron的Eback=Eγ/(1+2Eγ/m_ec²)给1172/1173keV时209.769/209.801keV、electron edge962.231/963.199keV；背散射差.032keV远小于Fig11的4keV bin，只作约210keV结构/邻接材料机制核验，没有digitize图counts、重拟χ²/CI或标Q。结果[exercise-result](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/riley2021-response-exercise-result.json)，canonical R21-11/18与UG24-18。

### 真实可执行源模型的有限MC设计

1000history实际统计控制已先过：两个低区S1/S2为γ27/5、decay38/14；H12为0/3，fixedN总数crossCov为−.135135/+2.470470counts²。双路线矩阵PSD、hist/history求和和读后hash通过。两高区零观测的95%界约.00299125只约束模型history-hit概率，不是实验source-free或平均singles上限（UG24-13/14）。

[canonical统计合同](../../knowledge/research-notes/gretina-eu152-source-response-replay.md)从完整history的晶体singles向量c_e定义S、H，推得fixedN总数Cov=N/(N−1)(H−SS^T/N)，与Poisson化history数时H分开。未探测history保留在N内；四个事前半开能区为120–128/1404–1412/1540–1800/1800–3000keV。它是新设计/推导，不能迁为无TTree实验ROOT的Σ或误称fullfitCov。100k实际矩阵PSD、双算法残差≤1.41×10^-11counts²、hist/history求和与读后hash均过。低区fixedN Cov12=−13.120331/+7.306573counts²；Poisson化history数时H12=0/38，不能混用条件化。

### 实际源/背景比例与共享归一Cov

[ROOT合同](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-eu152-input-freeze.json)及[actualaudit](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-eu152-public-data-audit.json)在前置窗口合同后执行exit0。egam均8000×1keV bins、整数非负、Sumw2N0，源11249812/背景1731654条entries；1800–3000 rebin4得13836/30293=.456739181，finite独立Poisson背景假设下σa=.00468656，对照把B当exact则.00388296。1540–3000另得.492627908，不能按相同窗口/独立点处理。

[真实ROI Cov](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-eu152-ROI-cov-audit.json)在source前置ROI冻结后计算：两grossROI Y/B=1299473/50784与276090/1244，共同a使crossCov≈1387.571counts²、ρ=.00225767，matrix正定。它们不是Gaussian净峰或已测eventΣ；仅示范真实hist输入下的条件误差传播。

原InBeam selector299–315抽取编译，[32无序排列16fail](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-point-selection-audit.json)后没有立刻归因paper：追到[GRUT实际反证](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/grutinizer-point-order-counterevidence.json)，normalBuildFrom→SortInts保证decompE降序、descendingdistinct原控制全过。只保留ties/reader版本缺口。


### 完整finite IQUV设计的前置合同与验证

[代数前置冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-full-finite-design-freeze.json)固定Q+iU=−2tau_plusminus*及fullq d_(q,m)；[12新PSD全值冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-full-finite-design-input-freeze.json)早于执行。另名[设计结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-full-finite-design-final-result.json)实际exit0：18cases/540points全IQUV对独立trace最大差4.56e−15，Rz3.34e−16、同步native/RB系数变换残差0；δ0与purelowerexact、δ1e6与upper差≤1.05e−6，nonPSD拒绝不clip。trueIzero的设计残差2.89e−15在预定1e−14数值门下normalizedNone，独立traceexact0；门不是探测阈值。原source/binary和literal失败不改。


### 有限H、同tensor角采样核与evenκ U控制

[finite-product-first-result](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-finite-product-first-result.json)实际exit0，解析H与原非零分母乘积差≤2.00e−15，但六个一般PSD案例最初并未整体闭合；原结果保留。随后[同tensor角核比较](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-angle-kernel-comparison.json)抽取actualoldLegendre编译，核Pnorm=dκ0及dκ0=(−1)^κd0κ；同pol samplerI与photontrace≤1.34e−15，原IT Stokes归一核在nonaxial可差.48–.74。按恒等式作诊断收缩后I/Q/V闭合，U仍反号，不称完整修复。

[evenκ独立隔离](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-even-kappa-U-audit.json)直接运行原literalpureM1 1→0、态[i,0,1]/sqrt2（只有q0/2），CG比均finite；16calls I/Q/V匹配而U反号，最大合同残差6.67e−16。θ45°行原U−.942809、Jones+.942809；固定G4消费端/511keV90°点KN模型给K45/K135为4.38415/.228094，不是实测counts或Q。实际old/sdk d_k00(−1)均1，先前poleNaN猜测未观察；trueI=0控制则normalizedundefined。


### 实际Stokes内核执行与phase身份纠正

[冻结v2](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-core-audit-v2-freeze.json)、[core结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-core-audit-v2.json)、[独立oracle](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-core-validation-v2.json)来自两份实际编译脚本，最终exit0。字面168calls中pureE2/低spinM1共48finite，mixed/highrank共120 P1/P2 NaN，norm均finitepositive。实际CG分子/分母/F在mixed k0及dipole k4都为0；独立photontrace均有限物理，finitepure差≤1.11e−15、norm差≤7.78e−16。同1→1 MP3与MP304 δ0的purelimit一过一败，norm同为1.65。

初次ctypes加载TLS失败发生在physics执行前，命令级preload后运行0；不改系统/原输入。首轮Na−.85误作native但命名为RBbranch，本run已显式纠正并保留原记录；[实际F/R桥](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-g4-rb-phase-crosscheck.json)最大误差1.56e−15，正确native是0/+.85。v2同σ/J=.56、θ90°的理论P1=.340288/.017054，仅条件forward，不是实测P或新A0fit。


### A=25真实字段、参考谱系与条件加权重放

[冻结v2](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/a25-reference-input-v2-freeze.json)在数值执行前保存十对象/hash和field-flag合同；[实际审计](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/a25-reference-audit.json)由system/scripts/day16_a25_reference_audit.py执行exit0。旧2009三个MR依次−.189(.012)/−.13(.03)/−.02(.03)，按已核单emitter KS/RB合同转换后与L26旧reference逐项闭合。2025的1612四分量独立误差条件重放给−.206805±.013098，与采用−.207(.013)相容；1793重放−.13±.012792，采用误差.02尚未由该简单公式闭合，保留原值及未知evaluator程序。

Na1041在Adopted、FSU和XUNDL三层的Ei/Ef/Egamma、MR空栏与comment、A2/POL、不同array/beamenergy分别保存。3970 MR(F)追到1972Ke13覆盖默认1975Bu14；失败控制拒绝空MR数值化0、忽略flag归primary和将XUNDL3971静默改成3970。level-gap残差及M=25u recoil仅标尺度，未强配能量/置信度，未分析寿命或B值。


新输入[kf89-w178-921-input.json](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/kf89-w178-921-input.json)在数值前冻结（identity `DAY16-KF89-W178-921-GATE-CROSSWALK-01`；SHA-256 `d686f653ee6a67d20beba402c7f679a00674cb4e500a446b2cb927c86e6e0690`）。[新脚本](../../system/scripts/day16_kf89_w178_gate_audit.py)和[结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/kf89-w178-921-audit.json)属于本session；底层CG/Wigner/photon primitives复用Day15代码，明确依赖。

统一target后的R921,306=1.5151515，字面边界像[1.3157895,1.7857143]；与另一R的cross Cov需乘−2.2956841。条件std-Gaussian/point设计中，原`.66`单行给d=.0918600或46.2691；同gate目标P分别−.3984555/−.0199220，均为负。它们不替换作者`.07±.10/>85`。

用二次型的generalized eigenvalues检查完整R范围，用projective α=atan d求全部根，不用单optimizer选支。两quoted-margin rectangle在声明ref d=−1.9时仍留下两段；不称置信区间。literal-HWHM和仅改reference符号均按冻结配置作为诊断，未调σ/参考去强求作者支。

本session原图确认KS70 Eq4b前有负号，结合Eq9的正√3/10比例，核D96/KS70同BM条件下d相同。first B与second A的干涉符号、历史Biedenharn–Rose与Rose–Brink身份、裸T比与normalized δ逐项保留。S同时变换参数和kernels使R差0；只改参数时mixed R最大差3.66而pure仍过。新spin11→10的F/photons差1.11e−15，完整D96 tensor/trace24个比较差≤1.22e−17 sr⁻²；共享基础函数，不算独立实验或producer。

### 后续：高自旋factorization没有解释原表差异

来源前[BT87假设冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bt87-before-source-recall.json)明确已受摘要/Ref6 priming；随后完整读printed513–520八页，核Eq1–16/Table1/Fig2/AppendixA-B。新[固定输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bt87-factorization-input.json)和[计算结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bt87-factorization-audit.json)由[新脚本](../../system/scripts/day16_bt87_factorization_audit.py)产生。没有改σ/角度/印表或拟合reference。

[BT87来源](../../knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md) BT87-4：finite improvement只把ordinary A/B换exact，joint仍factorized。Eq10 harmonic contraction与Eq12轴积分差1.78e−15，两个quadrature差2.89e−15；无限spin五个A2/A4印值校验通过。KF89十行的舍入相容计数为exact6/10、infinite2/10、finite improvement1/10，原四项差异均未由这些近似解决。有限改进还将10→8→6/E2-E2的exact R1变成1.0137425；不是所有ordinary系数改进都保全joint交换不变量。[angular-correlation知识页](../../knowledge/methods/angular-correlation.md)保存公式、数值及限制。

Fig2条件的13个角采样显示I20 finite改进absolute W误差较小，不能称全角误差上界；angular node附近infinite W0对exact小非零会给100%relative误差，不据此反驳源的absolute W比较。另从exact B2与独立quadrupole式核J20/M0的形式轴矩−.500447027，越过正经典unit-axis分布的P2下界−.5；finite moment substitution不能被当作实测正经典P(Ωs)。决定limits最初“用近似解释原表差异”的假设，停止这套固定网格的参数尝试，转回primary/producer与NNDC谱系输入。

### 后续：官方178W评价对象与同母态参考

通过普通ENSDF首页session初始化后取得[四对象manifest](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/n178-public-objects-manifest.json)：178074001/004/006/005，均200907 header、2008cutoff，检索日不当新实验年份。004/006分别回指1989KR01/1979DO02，005混收1998Pu01/1999Cu02，adopted E/RI默认来自13C数据。

[canonical source](../../knowledge/sources/nndc-2009-178w-dco-reference-records.md)保留原行/field空白和scope：18O102行与alpha223行主线读完；adopted1434行及13C1028行只核header/global rules/所选parent-gamma。未通读216页NDS或取得Dors/Purry完整primary。原始快照在repo tmp；保持raw不变，新增raw归档槽位未填充、Bib key无唯一命中，两项缺口不能当论文ready。

[冻结v1](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/n178-reference-input.json)先于数值；[v1结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/n178-reference-audit.json)与[新脚本](../../system/scripts/day16_ensdf178_reference_audit.py)核MR/CC/RI固定栏和parent identity。137.34/225.83的同母态A2 central比在声明same-layer、pureE2 reference、s2=Q2t/Q2r=1条件下给d=−2.16625或−.342242。169/306 central比−3.59091超全δ范围[−2.92727,2]，但一倍quoted边界的ratio像已相交；不能由central无根称源数据矛盾。未调σ或Q强配旧平均−1.9，也不叫新MR/置信区间。

更重要的新companion是N178-12：同一921-keV目标的explicit alphaKexp=.0067(.0011)，同母态1090参考为.0031(.0005)，来自1998Pu01缺省层；[独立冻结v2](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/n178-reference-input-v2.json)和[v2 typed audit](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/n178-reference-audit-v2.json)核K-shell实验标记、空MR及实际母态。它们不是total CC .009(.004)/.00380；还缺primary的electron/photon calibration、门/峰分解、Q/efficiency/Σ与匹配理论K系数。1998Pu01已由官方Refs/Crossref定位Purry等NPA632,229–274(1998)，DOI10.1016/S0375-9474(97)00654-4，目前元数据不当46页已读。

原169附近另有来自18-母态的168.0，和10-母态168.3共享literal A2=−.67且均无error；原峰分解未核，不能计两次独立校准。alpha对象RI125度以及1089.7的1.3±1.4 fixed-field precision同样保留，拒绝把邻近CC数读成δ或把不同反应RI平均成新branch。

### 后续：真实K-shell companion的匹配理论与认识修正

[来源前回忆](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/w178-kicc-before-source-recall.md)与[时间/hash](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/w178-kicc-recall-freeze.json)在重开KB08 raw之前冻结，明确受旧Yb查询/ENSDF数值priming。随后重读KB08 printed202–214完整主线、AppendixA215、定向TableB1 printed223/W184及Eq1/5/20/24、Table2；不是宣称重新逐格读全部AppendixB。原PDF hash匹配，旧humanreview source的全字节前缀保存并核hash，新KB08-D16-1–4只为Codex self-audit。

[冻结query input](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bricc-w178-query-input.json)限定Z74/E920.8、FO pureM1/E2各一POST，零自动retry、nominal energy、无A178-specific radius计算。[query receipt](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bricc-w178-query-receipt.json)与[offline capture](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bricc-w178-captured.json)分开：HTTP200之后核program v2.3(2011)/Z/element/E/multipole/FO echo、全rows、N6/N7 empty及398keV warnings。K系数M1=.00995(.00014)、E2=.00435(.00006)是新理论输入，不是实际K测量或旧Yb平移；K有效不代表programTot完整。raw网页留repo tmp、关键数值/hash已canonical。

[可运行三阶段程序](../../system/scripts/day16_bricc_w178_reference.py)与[结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bricc-w178-conditional-comparison.json)给本任务两个固定R根的nominal K预测.00990314/.00435261，理论quoted误差盒的像均不与reported[.0056,.0078]相交。它没有自动选择一根，也未传播R/ρ/reference/response误差至整族DCO分支。普通FO/M1E2的central算术逆映射abs(d)=1.176001、fE2=.580357，仍±两sign；quoted alpha边界名义像abs(d)[.789423,1.865476]无置信水平、不是新测δ或联合fit。

决定revises“额外observable会自动在现有两点中选一个”的预期，limits仅靠phase换号修复magnitude差异。新必要输入为原electron/photon校准、门/分峰/normalization/Σ以及该普通模型的适用条件；没有自由调sigma、efficiency或penetration参数强配。源Sec4.1.2的NP/SC/核参数条件和Table2误差定义保留。其后已成功取得Purry1997thesis（见下一段），1998paper仍未取得；两者严格分开，currentbatch不再任意开更多能量/modelquery。

### 后续：已取得Purry1997 primary，原K测量与真实反证

OpenAIRE定向thesis检索返回Surrey公开delivery，nature-downloader实际下载[112页PDF身份/覆盖回执](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/purry-thesis-identity-and-coverage.json)：Christopher Stephen Purry、Surrey、May1997、3,748,295bytes，hash b8ee1308d4871c1514d0ed54b3d523104da143bb346088a24eb008d97fc96753。原title页、wrapper/2017reproduction与原日期分开；旧epubs文件名只作discovery，不冒称同一hash。原PDF只在repo tmp、raw槽未归档。

[新primary source](../../knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md)实际定向读Ch1、Ch3printed12–24完整实验/分析、Ch4intro/所选表行和printed49–54/summary95–97；wholethesis仍skimmed，不冒充完整112页精读。P97-2/3/5的原图确认K=.0067(.0011)/.0031(.0005)、独立SiLi磁透镜+单Ge、1.5mg/cm²斜靶、beam后50–400ns、152Eu/internal lines和timeenergycorrection。此后不能继续说完全无primary/完全无校准；实际efficiencycurve/internalcalibrator逐线/peakledger/Cov仍缺。

P97-4原AD采用另一prompt/earlydelayedselection、拟合W0(1+a2P2)；它不直接等于fullA2，也不自动与delayedK共用ρ。[冻结estimator input](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/purry-estimator-input.json)、[target ledger](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/purry-thesis-target-input.json)、[程序](../../system/scripts/day16_purry_observable_ledger.py)/[核验](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/purry-observable-ledger-audit.json)核实际47/97/148三角full设计秩3；equalweight point诊断c0=−.00954915/c2=−.44481479，reported a2=(A2+c2A4)/(1+c0A4)。实际weights未知，不能用此反解原A4；任意positive diagonalweights的c2界跨零[−1.100076,.954230]，原geometry本身不恢复estimator。

P97-8是比条件toy更直接的反证：作者用290KICC=.027(+.004/−.007)、prompttiming和68/61低能符合，把旧3525态I14/35ns改为13-/T1/2<1ns，30±1ns改归3654态。旧KF89历史结论保留，新KF89-20链接此后续原件；不能仅凭原abstractestablished14忽略修订，也不能把另一态spin改变误贴到921的11→10路径或量化原δ变化。原producer/response不足仍有真实适用边界。

### 后续：130Ba独立三角度实验的真实选支条件

W178当前primary/producer路线到达输入边界后，[candidate-refresh-004](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-004.json)选择一个仍属Day16的novelty问题；Day17科学预习尚未开始。来源前[primed recall冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ko01-recall-freeze.json)后，完整读KO01三页/所有Fig1–3/TableI关键列，原hash匹配。实际offbeamβ实验与此前W178采集独立，puregate/phase等理论定义仍共享谱系。

[TableI typed scope](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ko01-table-scope.json)核40条跃迁、18行finiteδ，并非“全表只有18行”或所有都unique；483.5keV未解/星号无误差保留，负宇称末两行是E1/M2。原KO01-1–5 flags不变，新6–11为selfaudit。

[冻结input](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ko01-three-angle-input.json)/[新程序](../../system/scripts/day16_ko01_three_angle_audit.py)/[结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ko01-three-angle-audit.json)复算Fig2的3→2→0 pureE2gate，normalized相位桥d_D96=−δRB=4.5给A2−.03214156/A4−.07779112，与作者calculated−.0321/−.0778按尾位舍入相容；两计算路径差<9e−16。印刷coefs构造的shapewitness R180=.90193794单独仍给d≈.004919/4.498979，R55预测约.9677404/1.0438668；第二比可在这个固定模型下挑branch。

两R可线性恢复normalized A2/A4，rank4约束magnitude、rank2interference选sign；但两者共享W90，原Σ未知。图中横线没有数值表/likelihood，computedwitness/舍入preimage不是experimentalmeasuredcounts或新δCI。这个真实成功例不抹去4+_3→3+_1失败例，也不令relativeM1自动成为absoluteB或mixedsymmetry证明。canonical angular-correlation保存公式、输入、全根、Cov条件和核结构companion缺口。

### 恰好Day17知识预习：P/A/Q与真实Compton响应（无学分）

[time gate](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/day17-preview-time-gate.json)在上海13:00按原day19/15:00截止刷新，仍约1559分钟；重建current候选/复核matrix17后，只开启恰好下一卡知识preview。保持day_index16，partial[16,17]，不正式计17、不打开18。来源前[回忆/hash](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/day17-preview-recall-freeze.json)说明Day15/ST99/本run priming，不称独立盲测。

完整读Schmid1998 published16页主线与Figs1–15/Table1–3、rawhash匹配；新SG98-4–12与[compton方法页](../../knowledge/methods/compton-polarimetry.md)保存PAQ分层。twofold定义A=(etaC−S)/(sqrteta(C+S))，C包括sideADCzero所代表的另一侧photopeak；eta=Su/Cu、Q=Acal/Pcal不等于genericclover的同名校正。Fig9eta示例threshold130、Fig10Q/197Pb样本threshold60，迁移需matchedselection。F中的epsilon此处为photopeak，传统polarimeter为coincidence，高背景不能只比裸F。

[实际Table3冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/day17-sg98-table-input.json)与[新代码](../../system/scripts/day16_sg98_polarimetry_preview.py)/[核验](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/day17-sg98-table-audit.json)使用197Pb七行C/S/fiterrors/eta；432行C30934(402)、S4449(125)、eta.163(.003)得A=.0415282，不能代成(C−S)/(C+S)=.7485或balanceddenominator=.06250再沿原Q。source A/P/curve共享依赖，不重复计实证。

actualfiterrors条件传播的432 σA诊断.00980、etaerror敏感性.00611；sqrt(area)Poisson仅.00508。sourceerrors来自多peak/backgroundfit，fullC/S/eta/Q Cov未得；不能把这些diagnostics称完整实验budget。knowneta/无背景固定n时VarA=[1+(eta−1)A/sqrteta−A²]/n是声明二项层的恒等式，nearA0才回F近似，不填造counts。

printingclosure保存失败：294行按原eta.061/C16622/S1226得−.048106，未在C/S整数、eta/A最后位box内复现−.045。所需eta.0617505属于target反推，未当独立标定/未改输入；它仍在原quoted .061±.001内，A差远小于.019，不是实验证据矛盾。[44页alternate边界](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/day17-sg98-alternate-table-boundary.json)仅targeted搜索/图像定位、未找到可独立核的该表；不假称本次完整重读44页或用其修表。

source原197Pb正link/负inband pattern对E1/负宇称的支持保留为作者解释；过高幅值、带内散布及AD形状反查支持其高背景拟峰系统边界。约36%是specificpurehighspindipole/maximumalignment比较，不是通用physicalP上限。缺的是matchedeta/Q、actualpeak/cut/efficiency/Σ，不能以更多同data处理或任意Q插值取代。该preview不计正式Day17、不给其day-index前进。

### 用户恢复后的新追源与1505-keV相关网络

恢复时间、primed冻结和baseline见[恢复回忆](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/reopened-source-before-freeze-001.json)与[KS70网络冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/reopened-ks70-network-freeze.json)。新DNB SRU记录核Jül-Spez458完整身份；两页目录实得并原图确认DCO Sec3.2从printed46开始，正文未得。Canonical [KF89-21](../../knowledge/sources/kramer-flecken-1989-use-dco-ratios.md)和[W178追源单](../../knowledge/research-notes/w178-921-dco-gate-double-solutions.md)保留URL/hash/目录与正文边界，访问发现记录001–005不当科学证据。

重新原图核KS70 TableI/II/Fig5、Eq10/11/17，冻结[15transitions/31cells/4direct输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ks70-network-reference-input.json)，[新程序](../../system/scripts/day16_ks70_network_reference_audit.py)与[结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ks70-network-reference-audit.json)回链[KS70-14至18](../../knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md)。31个target/gatecell按无向gamma对为26对；作者25correlations的countdefinition未知，不擅改或计独立实验。764/658和707/658各有3条图示路径，缺branch/selectionweights时不能任选一条U链。

真实1505分别在3→2→0与5→3→2中作first/second。TableII单A22留下δ−3.45050/−.483082两支，上游reference的A22预测−.08660/−.20632对照实测−.184(.024)有区分力；四项TableII marginalboxes交约[−.495802,−.454731]，明确非CI或新δ。TableI四项同条件无一倍margin共同交，direct/indirect1505/658中央差−.068；缺实际response/Σ，不宣称原实验矛盾或用summary−.55(.10)重复拟合。[canonical双解计算单](../../knowledge/methods/dco-pdco-ambiguity-worksheet.md)保存二次型、物理角色、pure/rank4与多path边界。

[first-run failure](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ks70-network-first-run-failure.json)保留在任何inverse前因图示energyclosure0.11keV守卫失败；放大确认源标签最大残差.5keV，最终保留源两层energy/residual，不篡改值/补uncertainty。新photon/F只核代数和同坐标，复用底层不算独立producer。支持matchedreference/多rank，限制总体“consistent”摘要与精确单fit混同。研究继续，原deadline与仅16学分不变。

### 固定ALPACA代码对象：独立实现与观测对象边界

[代码前冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-before-code-freeze.json)后取得固定2023commit的113blob源码，核GPL/1.0.5、selected公式/接口/CMake；并将匹配的GSLdevheaders仅解到tmp，系统无安装/配置改动。完整reproducibility见[canonical代码source](../../knowledge/sources/alpaca-2023-v105-angular-correlation-code.md) AC23-1至6。配置/build/所选8项ctest均实际exit0，113源blob运行后保持原hash；不把wholepackage标全读/全测。

[冻结numeric输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-comparison-input.json)先固定first/last dB=−dKS/+dKS和16pi²/32pi²；新[harness](../../system/scripts/day16_alpaca_code_crosscheck.py)通过实际C++/GSL既有CABI，与自写photontrace的1505两角色、实际单路764–687–818/中间全marginal、两个polarizedcontrol最大差1.12e−15；错first混合相位W最大差.6608114而pure仍通过。此为**独立数学实现**，同formalism，不增独立实验，也不使缺失的DCOMAP/RU09producer或response/Σ到手。

[首Python包装失败](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-first-wrapper-failure.json)保留undefined evaluate_angular_correlation_rotated；未改upstream source，改从实际导出的create/evaluate/free CABI执行，不声称Python/rotation全部ready。[最终结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/alpaca-comparison-result.json)另核API对象切换：填first EM会启用pol-dir，theta135示例Wdir=.89954143而pol两轴=.92027694/.87880592、平均回dir；仅90度检查会漏此例差别。新知识已写[双解方法单](../../knowledge/methods/dco-pdco-ambiguity-worksheet.md)与IF21/KS70反链。

### 官方ENSDF原相位章：完全未观测转换与MR字段

[来源前冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ensdf-phase-before-freeze.json)后，从NNDC官方首页取得两份不同manual：[Martin1987原phase章](../../knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md)实际完整九页PDF132–140、章内1–9；[Tuli2001格式](../../knowledge/sources/tuli-2001-ensdf-format-manual.md)仅定向GammaRecord/V.9–14，whole112页skimmed。MA87-1/2/5给first/last相位、原NRFδ1=−δ2直接locator，保留RB术语/算符归一边界；TU01-1说明unsignedMR符号未知，不能被普通float自动认正，DMR也保留代数不对称范围。rawarchive/Bib缺口仍显式，不称186页整本精读。

MA87-3原Eq9新增有意义的sample条件：完全未观测mixedbranch用Delta²=δgamma²(1+alpha_Lprime)/(1+alpha_L)而非总沿radiativeδ²；观测electron则另用shellratio和particleparameters。按[新冻结168.71输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/w178-unobserved-ic-input.json)各1POST/0retry，KB08-D16-5给nominalW74FO totalM1=1.073(.015)/E2=.553(.008)、所有列明shell数值/无warnings。旧920.8/Kquery不重跑、不代total。Ref21 Anicin1972只取得metadata，无body，未借chapter转述假称原读。

[新程序](../../system/scripts/day16_unobserved_conversion_audit.py)与[结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/w178-unobserved-ic-audit.json)：声明middle168.71radiativeδ=−1.9后qgamma3.61→qtot2.70445，fE2 .78308→.73005；10→9的U2 .938216→.941382、U4 .799604→.809779。没有测得的新endpointgate 11→10→9→7设计中，两个旧first候选的R变化约+.152%/+.110%；不是原两DCO测量重放或差异解释。q/c精确缩放还能保持所有Uk，故paritysensitivity不保证自由q下唯一parity。

新知识已回写[internal-conversion-analysis](../../knowledge/methods/internal-conversion-analysis.md)/[deorientation](../../knowledge/concepts/deorientation.md)/[multipole-mixing-ratio](../../knowledge/observables/multipole-mixing-ratio.md)、双解单与NRF边界，source见MA87-3/4、KB08-D16-5、N178-4；电子/γselection、response/Σ与operator假设逐项保留。首JSONnumpybool序列化failure已记，未修改输入或网络重试。研究继续至原deadline，不因本条完成结束。

### RZ17实际参数：概率测度、卷积与大delta尾部

[primed来源前冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rz17-before-source-freeze.json)后完整重读原三页/Eqs7–17/Table1/Figs1–3，[Table1输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rz17-pdf-measure-input.json)在数值前冻结。原RZ17人审page/7claims全字节prefix保留；[source新RZ17-8至12](../../knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md)明确原作者结果/本任务measure/未得RooFitrecipe分层。首hashguard多写c失败已动态对照source hash核相符，未改raw。

实际M2/E3/K示例三alpha为8.8(3.1)/14.49(.21)/.227(.004)。本任务显式independentGaussian+physicaldomainpushforward，Z=.9636292、mean.924387；Eq17图解交点[.451541,1.282363]复现source图解，但equaltailed16/84 [.509370,1.271456]与mean左右各.34 [.615665,1.670067]不同。原所报.92^(+.42/−.37)不被改写。[完整结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rz17-pdf-measure-audit.json)含GH/GL收敛、独立ratio解析式与800000MC，mean相合不能认证全interval/producer或truecoverage。

Literal普通positivePi卷积mean2.55349，在theoryerror→0时也会多平移2delta0；Eq14缺实际centering/FFT/supportrecipe，未将此failure归给实际RooFit。Declaredpushforward尾p~.083207/d³：mean有限、secondmoment无限，flatdelta likelihood又不能在0∞归一。新[canonical概率方法](../../knowledge/methods/icc-mixing-probability-domain.md)与[ICC方法](../../knowledge/methods/internal-conversion-analysis.md)保存proof、同数据sharedCov与物理域边界，不生成新实验δ。

### EL18独立裂变样本：大delta的连通分支与共享IPAC校准

[来源前primed冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/el18-before-source-freeze.json)后完整重读11页/Eqs1–9/四表/11图，[EL18-5至11](../../knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md)保存64→17→9bin、多extra门OR、Goodin/Daniel谱系、samephi/G4非独立校准及实际printingboundary。既有四claim/review保留，不称同37条来自37independent实验。

[冻结104Mo行](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/el18-projective-branch-input.json)绑定Table2 3gamma+→2+→0+/extra556/200*/478/331*；能量行未给不补。原δ50^(+∞/−27)和bracketed−.15(.02)均保留，negative<-159亦allowed。[新计算](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/el18-projective-branch-audit.json)的printedA2central根−.151126/+55.7172不改成source50；一倍字面矩形允许大正/大负并经pureE2点连接，非jointCI/原DELTA区间重放。[canonical双解单](../../knowledge/methods/dco-pdco-ambiguity-worksheet.md)已固化。

另原图核106Mo2gamma→2的raw/corrected同印−.18/.27而groupG=.78/.6：中央相除−.230769/.45、lastdigitbox不交，保留未闭合；110RuTablebound−41/正文−46同样不擅改。共享G/raw校正Cov未知，g符号不能从evenphi衰减单独得到；代数constantE2/M1穿零说明δsigntrend不是唯一shape证明，而非实际替代模型。[angular-correlation](../../knowledge/methods/angular-correlation.md)与source保存这些实际控制和限制。下一原DELTA/producer说明仍值得追，研究继续原deadline。

### DELTA1.01公开producer：实际Fortran执行与输出合同

官方IAEA目录challenge、旧NNDC404后，从实际PyNECMake发现DELTA文件，取得namedtag0.7.8与develop相同207603byte/hash副本；sourceheaderv1.01/1993。GitremoteHEAD未得，内容hash固定而不伪报commit。[canonical DELTA source](../../knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md) D101-1至8区分公开mirror/当前内容与2018actualproducer，原license/source/binary都只repo tmp、不redistribute/sourceinstall。

[五组card预冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta-code-execution-input.json)后GNUFortran13.3未改sourcecompileexit0/五caseexit0；104MoA2only2度实际根约−.151/55.9、1度约−.151/55.8，不改成论文50。DIPS的SIGMA是absoluteχ²threshold且poorfit用F规则；+1000为没找到scan内crossing的sentinel，不能当有限实验error。内部PURE也能表示fixednonzeroδ，非physicallypure标签。

knownpurecontrol的exactgridχ²0，但三点插值报告.199；[预冻结数值followup](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta-pure-followup-input.json)只改step/range，1度报告.012、已知pure点local.1度printed0，未改源码。两followupexit0。[完整offline审计](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta101-output-audit.json)核printedgridcoefficients到F9.3精度，明确firstpureminimumtest失败、processexit不代科学通过；actualEL18response/Σ/2018binary仍缺。source还直接注明忽略Anicin混合conversion退取向，印证前面的sample合同。[双解单](../../knowledge/methods/dco-pdco-ambiguity-worksheet.md)/[角关联](../../knowledge/methods/angular-correlation.md)已固化。

### 104Mo官方旧对象：targetidentity与标签不能替分支选根

Goodin2010指定机构403/目录未得准确thesis题名，OpenAlex的fullname/ORCIDlink也只发现用途，未写进primary身份。Krane1973已核DOI/卷页但APS/OSU/ADS无body；OpenAIRE把1973deformed与1974spherical两个DOI合一，已拆为metadata边界不作同一文/erratum。上述访问不添加新科学模型。

[三个104Mo官方对象](../../knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md) N104-1至7实际取得：Cf201行/Cm96行全部主线，adopted325行定向所选parent/gamma/global。base200709/cutMar2007、ERR2007与Q2012分层，未含2018EL18。adopted1028.35/3+/B给836.3/M1/MR空；Cf1027.9/835.5和Cm1028.0/835.8是不同energy层，结构候选不等于已复原EL18未列energy的actualgate。

[冻结输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/mo104-crosswalk-input.json)/[crosswalk结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/mo104-crosswalk-audit.json)核MR空、旧globalM来自CmDCO但该对象无targetR/gate/angles；旧M1标签不填δ0，也不单靠版本裁决EL18大E2支。reference192层/T1/2 .97(.08)→mean1.3994(.1154)只核EL18calibrationinput，不开Day18。Cm对象T还引自Cfplungerprimary，数据集标题不当独立采集。知识已同步EL18/双解单和source，不新测δ/τ或补旧DCO。

### 恰好Day17预习延续：91Ru真实门、偏振符号与校准误差

先冻结[primed回忆](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-preview-before-source.md)及hash，后沿[Zheng2013 source](../../knowledge/sources/zheng-2013-linear-polarization-91ru.md)的原11页全文主线、两表/八图/Eqs.(1)–(9)重新阅读。正文044328-n=PDF第n+1页；本run正式16/partial17不变。Table I十一项、Fig.2三组真实峰面积及Table II九项身份[冻结输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-calibration-input.json)，原PDF hash已核，未改raw。

Z13-6/8：Fig.2的497门三比值复算.500726/.964256/.953129；仅声明独立拟峰面积时σ为.01531/.01771/.01740，未恢复全Cov。R_eff=1.79是效率曲线常数比例，在两光子乘积中相消，不能再乘入R。898.5在Table II用了974门，R=1.01(.01)，不是Fig.2的同一观测。919.8 nonstretched E1与615.8 stretched M1连A=−.07(.01)都相同；DCO/spin/geometry共同区分，负A不能独判M1。436 doublet按parent/child隔离，绝对Jπ仍保留作者基态假设。

Z13-7/9/10/11：[实际程序](../../system/scripts/day16_z13_calibration_audit.py)与[11行结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-calibration-audit.json)显示全部P/Q中央值在末位舍入下相容；若括号σ均属同一Q=A/P的一阶marginal标准差，316/586/823/974/1054不满足任意合法Cov的局部必要界。宽松允许所有中央值及σ各末位±半位后，只有316/586/974/1054仍稳健排除这套条件包，823降级。源误差定义/producer未得，不改原表或判实验错。声明独立Q加权拟合得p0=.38616115、p1=7.39668×10^-5、χ²=9.98029；原.39(.02)/.00006(.00003)/标签11保留，未称精确复现。Q由同校准A/P得到，A/Qfit回代有共同输入，不是独立P验证。

`supports`联合判据，`limits`单独符号和误差独立假设；canonical为source新增Z13-6–11、[Compton方法](../../knowledge/methods/compton-polarimetry.md)的“EXOGAM已知E2校准：比值误差与回代依赖”、[偏振方法](../../knowledge/methods/linear-polarization-asymmetry.md)的真实nonstretched E1反例。缺逐线polarization gate/净counts/背景、A2/A4与a/Q的实际联合Cov；Table II只列DCO门，未擅自等同选样。没有新实验δ/Jπ/显著性，没有正式17或Day18。Z13-12另定向核arXiv v1的两表/Eqs/Fig.5，Table I十一行token均相同，upper435.9的A在v1为.17(.07)、期刊为.17(.05)，[版本核验](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-arxiv-table-crosscheck.json)保留；未混σ或增计独立实验。

### 1368-keV响应比较延续：FOM不是Q的同义词

Z13-13、原正文044328-5的1368比较句/等式(8)–(9)，另核arxiv v1 p.10同句：[冻结点输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-fom-input.json)与[代码式/结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-fom-point-audit.json)。表中pure-E2 calibration点止于1264；印刷curve外推1368得Q=.1600783，文字另报.135(.005)，中央差保留。未知p0/p1相关已使curve一阶σ在.00713–.02070间，另缺cross-Cov/选样，未判显著冲突或替换原Q。原F比4.4在同响应假设下分成Q²比1.244792及条件epsilon比3.534727；反推epsilon不是独立效率测量，没有F误差不制造新beamtime收益。复用结论已写入同一canonical source及Compton方法，仍partial17。

### 104Mo续追：官方NSR与更早XUNDL对象

[Gu96前回忆](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gu96-before-source.md)后，DOI题名和官方NSR key1996GU04已核。期刊body仍403/401/无OA，未虚构“已读Gu96”。但NSR列出200207的[104042007 XUNDL-1](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gu96-xundl-download.json)，本session读110行全部主线并[冻/核固定栏](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/mo104-xundl-audit.json)：27 level/55 gamma，L1028.0的467.4/835.8两支M/MR/DMR空，全文无DCO/gate/angle字段。原注释显式混入2002Sm10的252Cf寿命，且T不确定度纯统计；不把对象标题当另一Cm采集/完整Σ，不开展Day18。canonical[N104-8](../../knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md)保存原行/hash/版本及独立性边界。首次旧NSR URL误给Gu02只返通用frontend，未使用那篇数据；按原Gu04纠正后才获得真实官方record，访问过程保留。

### JT74原9页：F临界值与profile误差的出处

本session明确已受旧Wiki/DELTA/EL18 priming，先[冻结回忆](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-before-source.md)，后沿[JT74原件](../../knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md)完整105–113主线，视觉三表/六图；Crossref DOI、作者、年卷页核实，raw hash不变。JT74-5/6/7/10：固定atanδ后须profile其它参数，区分增量Ecrit与绝对R+Ecrit，ν=n−rank且alignment估计进入data；参数相关不自动等于秩亏。Sec7.1的“忽略相关”是单参数marginal同独立于nuisance理论的比较语境，随后的jointδ约束明确要Cov，不能用短句删Σ。

[冻结真实Table3/actual代码输入](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-statistics-input.json)后，[程序](../../system/scripts/day16_jt74_statistics_audit.py)/[结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-statistics-audit.json)核全部12项：原表标32%上尾，但按标准F实际约.30405–.30807；末位±.005仍不覆盖.32。Student-t密度积分及ν1/2闭式与F库最大差1.45×10^-15，保留数学对应未闭合，不猜原表/勘误原因。另抽相同hash代码的未改F unit实际GNU Fortran编译/运行exit0，DELTA引Gill1975的表与JT74不同（ν1 3.38对3.69），ν>16默认1，不能把结构同max当同一coverage。新JT74-5–10、D101-9与方法页写回，未给新实验δ/CI或宣称EL18实际producer已认证。

### 同一JT74问题的有界推导：纯M1点的regularity失败控制

不是实验新数据：先[冻结问题/priming](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-nonregular-before-analysis.md)与helperhash，再按原Fig2的3→2 spin path**声明**p0=1−u、p±1=u/2正density族，未认证原caption的group口径/δ phase，故不称原curve重放。[SymPy独立CG/Wigner-d程序](../../system/scripts/day16_jt74_nonregular_profile.py)与已核photon trace在mixed/pure/角度上最大差1.78×10^-15；[完整exact结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-nonregular-profile.json)给pureM1的AD Jacobian rank1、profile首项δ^4。对known正定Σ/interior u的声明高统计局部模型，LR为半质量0+半χ1²，ΔS=1在该点覆盖.84134475；只作regularity失败控制，不给真实DCO新CI。

同transition/density/选择的P90幅度可补局部rank，但未知Q会加一个nuisance使三参数仍rank2；独立matching Qcal才到rank3。Q=0/完整isotropy为失败控制；全局branch/实验Cov仍未解决。JT74-11及canonical angular-correlation/worksheet保存条件/公式/代码，不把数值当作者原结论。初次缺SymPy exit1，PyPI1.14.0及依赖隔离装repo tmp后actual analysis exit0，旧helper/raw不变，第三方包不发布。

### 恰好Day17预习延续：GRETINA真实双支、calibration谱系与约定

先[冻结primed回忆/旧人审prefix](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-preview-before-freeze.json)，后沿L26原10页全文/三表七图/Eqs1–19阅读；Fig1的β=.048/.046/.044由视觉补出（text提取遗漏），[8行原表冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-primary-input.json)保留multipole顺序/pureE2特殊0与RB ratio单位。新[L26-17–26](../../knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md)另列needs_review，整个旧1–16/humanprefix不改。

真实25Na1041 AD=.20(.02)/.00(.04)，作者δRB≈0/−.85；两支A0pred+.021(.007)/+.002，实测+.043(.008)，故符号同正不能选支。作者的0偏好有σ/Q条件，第二支误差/联合Cov缺失，未新拟合δ或给新CI。p7 positive E1/M2 ΔJ0例句与Table3 negative直接冲突，exact source-model检查支持Table3；旧L26-15须连新L26-19读，不由旧humanflag掩盖冲突。

合法取得并读完[Morse2022 UNC13页authorpreprint](../../knowledge/sources/morse-2022-gretina-polarization-sensitivity.md)，全部12图/两表视觉核，VoR公开API只有metadata。M22-5确认也用A0=Q Pbar/2；6quad tracking与当前12quad energyorder不同。Eq19参数实为tuned模拟GRETA500–2000四点fit，未误称多能实测。σ100≈7mm并非测量，作者同时保留P90模拟约.85/实验约1的companion失败。定向L25 source校准另明Q=.016/.048=.33及1173 coincidence reference，newL25-30/旧全prefix保持。

[事前双source合同](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gretina-replay-contract.json)、[程序](../../system/scripts/day16_gretina_convention_audit.py)/[完整结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gretina-convention-audit.json)：Racah/RB与D96 native emission的δnative=−δRB使mixed/pure AD/P最大差3.89×10^-16，错误同号达1.5336；Pi纯/混合工作桥与Q半因子转换保留定义范围，不冒称作者intent。A2zero仍可有Pfinite，I90zero则Pundefined。Morse印刷AD中央给P90=1.003776/极小negative pabs2，但physical边界与literal误差盒相容，不夹值/不当负布居测量。Ft≤.1 Q虽增，F仅余.25且implied效率.0974，未在缺Cov时新算误差或beamtime。source能量/β/quadcenter的twohit排序条件是design，不是误排序率。

Canonical [25Na ledger](../../knowledge/research-notes/gretina-25na1041-polarization-response-contract.md)与三source/方法页保存全部复用内容、角色/单位及独立性。Alikhani2012 body仍未得，未据两篇转述认证其原式；source MD tool provider unavailable/attemptedfalse与closed目录边界保留。所有新增均self-audit/needs_review，仍只formal16/partial17。

### 同一response问题延续：公开Fig4平均未按字面闭合

[事前问题/priming](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-averaging-before-analysis.md)、[218点原coverage/axis冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-coverage-vector-input.json)及[模型合同](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-coverage-averaging-contract.json)先于均值计算。原PDF5无embedded raster；从vector取黑C218点/红P2908点，按原0/π、y0/1 ticks及affinematrix映射，未为目标约.35/.53调curve/axis/δ。初stroke-style查询空是parser未读stroke属性/transform，不是原图无数据；后按实际attributes解析。redcutline自动隔离未闭合，门用sourcecaption/text的1.40–1.75，未反推选择。

[实际程序](../../system/scripts/day16_gretina_coverage_average.py)/[完整结果](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-coverage-average-audit.json)使两个积分坐标/16或32Gauss/overallCscale控制差≤1.12×10^-16。按图中红P×黑C literal平均为.377923/.543870，source正文为about.35/.53，保留未闭合；approx没有声明末位/CI精度，不能由图示kernel不足就判实验错。原Table1sigma=.55的publishedmodel同红curve RMS差9.81×10^-5；direct印刷a2/a4模型RMS .003295，两模型事前固定，未调参数。

声明factorized point-response下，direct AD模型的sourcecoverage平均.381428/.547017，event平均.362301/.546949；publishedsigma模型event均值.358972/.543766。改变平均必须同时处理校准Q和calibrator/target的weighting-ratio，不固定Q去强配A0。C若是theta-bin counts，额外乘sin会改成另一对象；joint〈SigmaP〉与分别平均之积及fit统计Cov也须区分。±.01 pagept registration只作数值敏感性，9个negative-C corner拒绝而非clip，非experimentalerror。

图中sourcecut质量约.19669、声明event模型约.16288不是实际polarimetry counts；观测振幅比1.5714的break-even fraction .40496只适用固定角形状的共同scale、knownresponse/无背景uniformξ模型，不给实际delta误差/切门最优。新增L26-27–29/Compton方法/案例note保存artifact与边界，35items不变，仍formal16一次/partial17。

## Counter-evidence and missing companion observables

Co60当前finiteMC的source开关通过不解决Q：507/549detectorpairs相对10bin仍宽误差。R21/LaBr gate与本rawGRETINA双门不同；backprefix实际对照也未映射原实验producer。Weisshaar2017 body各合法入口的具体失败/credentials_missing已记录，不询问/改密钥，也不从元数据补科学缺口。

R21-8/12–17的独立反证/边界：极小单晶quoted stat interval明确不反映真实层精度；I/II reuse同flood数据，改变fit范围不新增实验。能谱photopeak与门控continuum的companion不能代偏振harmonic/Q；1173target/1332gate也不能当L25反向角色的同reference。原raw计数、backfractionproducer/联合Cov及χ²grid未得，保留readiness，不补写新的实验CI。

### 实际能谱不替Compton校准

UE12-3/8/9表明两ROOT无TTree/实际Comptonξ，labθφ不是散射平面ξ；MC模板与fullfitCov未取得，p0中央接近不认证整response。README run022/1540/p2p3fixed与实际宏run020/1800/release的字面差别保留。sourceprimary一γ/event与radioactive一decay/event分母不同，不能将两种simulation当独立Q验证。selector的normal降序反证限制原担忧；actualtie率/原binary仍缺。


### 软件pureE2反证与整阵列producer缺口

UC21-8的Morse实际p0=.52/p±1=.24、2→0 pureE2控制通过，不能由mixed/highrank代码失败宣判原标定错误；公开实现与论文的exactbinary/macro/Geant4data/geometry/后处理仍未认证。必需companion为PSD photontrace、强度/purelimit及matching jointresponse；更多同代码helper执行不是独立实验。经验Q半因子须连同KN joint harmonic和平均定义重标，不能固定Q删半因子。


### 官方转录不能代替独立偏振companion

N25-4/5/10给三项实际边界：POL=.043(.008)是A0而非P；官方PDF靶厚度1.152µg/cm²与L26 Sec3的1.152mg/cm²相差1000；MgXUNDL G3971与当前Adopted3970.3不按nearest-keV闭合。旧M1标签/同paper XUNDL δcomment不增加选支证据；FSU35MeV的A2=.28(.09)也不能无matching布居/response/Cov直接与55MeV联合。1041两候选的A0预测仍同号，实际jointresponse与另一支误差仍缺。


最直接反例是一个已知pure参考也无法验证混合项相位：两纯端点通过，错误换号仍改R。另一个反例是本点模型部分Table1不吻合（例如.637341对印值.66；1.188657对1.12），且两比值rectangle没有复现作者>85支；原因未裁决，不能报告原文错误或实验新δ。

作者的强度比1.2±.2相对预期2.3只支持其branch偏好；模型预期和Cov缺失，不能变成独立、无假设的排除。182-keV E1/ICC结论不是921-keV target的独立companion。下一有判别力测量需同921/306、90°/38°/φ18°及matched cuts的P幅值、Q921、净计数/背景、与DCO共同事件Cov；没有这些输入不计算实验显著性或束流时间。

## Knowledge Impact and Learning Decision

pointgate本批 `limits`仅以角色不同就推physicalP不同的强断言：pureE2存在相同P极限；`supports`原门/轴/相位/能量response合同仍必须匹配。局部标量平均与全局密度平均的反例加强Pbar的适用条件，未靠旧Q改变均值追数据。

本批R21 `supports`多observable约束有效能谱响应；`revises`同仓库代码例等同原论文配置的预期；`limits`把参数一致/能谱吻合/极小stat interval提升为真实层测量或Q认证。原DCO/δ多解与same-transition companion边界保持。

### publicsource batch的判断

`supports`实际background/计数单位/共享归一Cov合同；`revises`无序selector反例可代表normalproducer偏差的初始担忧，上游降序是真实反证。`limits`将另config的processed energy/labanglehist当当前P/Q或matchingresponse；两源码/数据版本和多种处理不增加独立实验。


### 完整finite设计的作用范围

`supports`所声明singleemitter/realδ/fullq/Jones合同下的有限IQUV模型；`revises`“尚无一般PSD闭合设计”的readiness边界。`limits`把该模型通过称为原UCGretina/Morse exactproducer验证、独立实验或新的1041 branchfit；原literal失败、先前general失配和原pureE2反证都保留。


### 一般tensor结果的修订

`revises`只消除0/0便足以验证general Stokes的初始设想：实际还需同tensor angle kernel与分析轴消费端核验。`supports`公共CG的解析有限化与pure/PSD/truezeroI分层；`limits`把代码控制直接推广为Morse标定错误、通用patch或新的实验δ。原κ0/pureE2反证保留。


### 软件来源的判断更新

`revises`public tensor→Stokes入口尚缺的状态；`supports`同一observable的phase/pure/PSD/强度门；`limits`从pure2→0校准直接外推任意mixed/highrank emitter。来源实现的可重复条件失败不等于原论文或全Geant4失败，producer/arrayresponse/实验jointCov仍notready。


### A=25版本核验的更新判断

`revises`target Ei/Ef与Firestone旧参考未直接核的缺口，`supports`L26旧reference在完整相位桥下的引用一致性，`limits`POL当P、空MR当0和默认primary覆盖字段flag。当前/旧评价共享旧数据且Cov未知，不把版本差异称独立实验冲突；Na1041未获得新的唯一δ或实验CI。


`supports` DCO多解与phase/response合同；`revises` 不分gate角色直接联合同名R的做法；`limits` 偏振符号挑根和pure reference认证全部相位。没有新Jπ、B值、wobbling/chirality结论；178W条件计算不外推A≈130。本轮按当前池/唯一Day17预习持续重查公开来源和必要输入；各问题保留原始response/producer/Σ及未得正文边界，当前原研究窗口继续，不由同一模型重复或标签复用补成确定结论。

## Durable knowledge delta

本批新增[Ni60官方reference源页](../../knowledge/sources/nndc-2013-ni60-co60-reference-records.md)及[Co60笔记](../../knowledge/research-notes/co60-gate-role-response-benchmark.md)的“评价reference、共同δ误差与实际分支权重”锚点；N60-3/9/11分别支持MR误差/依赖、共享误差分量及actualSDK内部控制。原phase正文缺口仍保留；outputs仅为执行证据。

UG24-30–34、Co60 benchmark与Compton方法页写入joint模型/明确pureE2角色相同极限、actual小M3差别、KN单点能量依赖、130fullPSD/12spin2控制及19/189标量平均反例；知识层有完整公式、定义、边界及代码回链，非只outputs数字。

Co60 UG24-28/29及benchmark新增各100k实际moment/conditionalCov/图像和detector统计边界；source/选择/相位与counter例已在knowledge正文，不只outputs图/receipt。

新增canonical [co60-gate-role-response-benchmark](../../knowledge/research-notes/co60-gate-role-response-benchmark.md)，UG24新增19–27：静态源码/1k/native/coordinate、actual missing-pair与backflag控制和joint-cascade phase/theory。angular-correlation/Compton/index/Eu152note同步选择对象与readiness，不只留run输出。

新增canonical [Riley2021 source](../../knowledge/sources/riley-2021-ucgretina-energy-response.md) R21-1–18，保存完整主线、12图/表/Eq1、data与model/CI/能区限制。UG24新增18 actualasolid对应II数值；Eu152note/Compton/index/UE12/UC21关联原件并保持不同数据/版本身份。重算5733点与Compton背散射、source参数crosswalk均有knowledge副本。

新增canonical [G411 source](../../knowledge/sources/ucgretina-2024-geant4-11-source-replay.md) UG24-1–17和[Eu152 response note](../../knowledge/research-notes/gretina-eu152-source-response-replay.md)，保存actualbuild/nativeABI、truth失败与有限修正、同种子core对照、Target/euTape导航反证和finite-MC推导。Compton方法、原UE12关联与index同步；这些可复用结果有knowledge正文副本，不只在outputs。

### 实际公开校准数据与sorting合同的durable增量

新增canonical [ucgretina-2012-eu152-public-calibration-data](../../knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md) UE12-1–11，保存ROOT身份/actualcounts、两background窗口、共享ROI Cov、event分母、truthsorting与upstream反证。[Compton方法](../../knowledge/methods/compton-polarimetry.md)、[1041ledger](../../knowledge/research-notes/gretina-25na1041-polarization-response-contract.md)及index同步“真实可用hist与matchingresponse之间仍缺哪层”，不只留outputs。


### 从literal边界到另名finite模型的durable增量

UC21source新增UC21-14–16与fullq/Jones公式、12新PSD范围/纯端点/数值zero门；Compton方法及1041ledger同步数学模型readiness与真实response缺口。system/scripts/day16_ucgretina_full_finite_design.py为可复现设计，原实验δ、globalQ或全array认证仍未取得；新增科学知识的canonical副本在knowledge而非仅outputs。


### 有限系数与Stokes消费端的新durable增量

[UC21source](../../knowledge/sources/ucgretina-2021-polarized-emission-code.md)新增UC21-10–13、H公式/六PSD输入/核差及U隔离边界；[Compton方法](../../knowledge/methods/compton-polarimetry.md)和[1041 ledger](../../knowledge/research-notes/gretina-25na1041-polarization-response-contract.md)保存“有限数值式≠完整偏振producer”和真实zeroI门。三个新科学审计脚本使用冻结新合同，原source/binary/hash与旧失败保留；可复用内容不只在outputs。


### 公开tensor→Stokes的可复用代码边界

新增canonical [ucgretina-2021-polarized-emission-code](../../knowledge/sources/ucgretina-2021-polarized-emission-code.md) UC21-1–9；[Compton方法](../../knowledge/methods/compton-polarimetry.md)保存编译/运行门、零CG比值/purelimit和Q归一条件；[1041 ledger](../../knowledge/research-notes/gretina-25na1041-polarization-response-contract.md)保存正确native分支与readiness，Morse/sourceindex加可恢复入口。原source/review flags、raw/PLAN/Bib不变；只有Day16下partial17知识，没有新增课程信用。


### A=25可复用身份与版本矩阵

新增canonical [nndc-2025-a25-mixing-reference-records](../../knowledge/sources/nndc-2025-a25-mixing-reference-records.md) N25-1–10，重写[1041 ledger](../../knowledge/research-notes/gretina-25na1041-polarization-response-contract.md)中的缺口并补官方identity/旧新MR矩阵；[multipole-mixing-ratio](../../knowledge/observables/multipole-mixing-ratio.md)与[Compton方法](../../knowledge/methods/compton-polarimetry.md)保存phase→version→field-provenance/POL语义顺序，索引加入口。原humanreview prefix/flags、raw/PLAN/Bib均保留；本日继续仅partial17，无新课程学分。


canonical [178W知识单](../../knowledge/research-notes/w178-921-dco-gate-double-solutions.md)保存实测身份表、作者双候选、role reciprocal/Cov Jacobian、矩阵/新两根、phase交叉表、未复现结果和下一companion。KF89 source新增15–18；dco-ratio与旧worksheet有反链，index有最小导航。程序与outputs输入/结果用于复算，本节不是唯一知识副本。新增GRETINA cal/branch ledger与Morse primary也已写入knowledge，见本节机器映射。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/research-notes/w178-921-dco-gate-double-solutions.md",
      "summary": "新建178W921实测双支计算单，保留门角色、倒数与Cov、条件矩阵全根、相位控制及producer边界。 恢复批次新增：DCOMAP原件的新定位：Jül-Spez458。",
      "anchor": "delta-double-solution-sheet：先固定实测对象",
      "sources": [
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-15"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-16"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-17"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-18"
        },
        {
          "path": "knowledge/sources/droste-1996-pdco-formalism.md",
          "locator": "DR96-5"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-6"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-13"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-6"
        },
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-6"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-3"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-4"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-5"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-10"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-12"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-2"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-4"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-2"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-3"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-4"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-5"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-8"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-10"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-21"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
      "summary": "本session重新核7页主线，新增四项实测双候选、强度prior、参考编号冲突和response边界；旧review不动。 恢复批次新增：1988原学位论文的目录取证与未读边界。",
      "anchor": "2026-10-18独立Day16复核：921-keV实测双候选",
      "sources": [
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-15"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-19"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-6"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-20"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-21"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/dco-ratio.md",
      "summary": "加入同一target在两数据行中的gate角色及非对称倒数误差实例。",
      "anchor": "同一target在两组数据中的gate角色",
      "sources": [
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/dco-pdco-ambiguity-worksheet.md",
      "summary": "将本session178W新交付与Day15预习分开，增加canonical反链。 恢复批次新增：同一mixed跃迁的上游与下游参考：1505-keV真实表值。 新增固定ALPACA独立实现/观测对象边界。 新增原ENSDF章/total-decay和MR字段边界。 新增EL18独立裂变样本projectivebranch/校准边界。 新增公开DELTAactualrun/误差与数值failure边界。 新增104Mo评价时层/target身份及标签使用边界。 补误差阈值自身的来源/适用域审计。 增加源Fig2动机的positive-density exact Jacobian/四次profile及条件LR边界；matched P与独立Q校准的rank要求。 用真实AD/P案例补matched reference角色，不造R_DCO数据。",
      "anchor": "独立正式Day16的新实测对象",
      "sources": [
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-15"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-15"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-16"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-17"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-2"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-3"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-5"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-6"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-3"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-6"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-7"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-8"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-9"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-10"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-5"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-6"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-7"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-8"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-2"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-3"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-5"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-9"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-9"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-11"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-18"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-21"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-24"
        },
        {
          "path": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
          "locator": "L25-30"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "最小索引新增178W921计算单导航，不添加独立科学结论。 新增固定ALPACA独立实现/观测对象边界。 新增原ENSDF章/total-decay和MR字段边界。 加入ICC概率物理域方法入口。 新增公开DELTAactualrun/误差与数值failure边界。 新增104Mo评价时层/target身份及标签使用边界。 加入Morse新primary与25Na1041 durable ledger导航。 加入A25官方对象/历史版本入口。 新增UCGretina固定公开代码入口。 加实际Eu152 sourcecalibration数据入口。 G411新批补入truth/geometry实际控制与历史源response边界。 Riley2021原件已另读并核当前模型/原论文响应迁移边界。 Co60 gate/source与选择对象控制和原producer缺口已关联。 补Ni60官方reference/共同δ误差与actualSDK总分支归一，保留primaryphase缺口。",
      "anchor": "w178-921-dco-gate-double-solutions",
      "sources": [
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-15"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-1"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-1"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-11"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-1"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-1"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-1"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-18"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-10"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-1"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-13"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-21"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-27"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
      "summary": "完整核8页原件，区分exact、infinite与finite improvement；固定原表诊断未解释差异，保留同rank交换不变量限制。",
      "anchor": "2026-10-18独立Day16实际覆盖与决定",
      "sources": [
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-4"
        },
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-5"
        },
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-6"
        },
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "summary": "保存高自旋factorization公式、十行反向检验和finite系数替换失去exact交换R=1的条件控制，分开absolute/relative误差。 同页保存独立130Ba真实三角度实验的两个shape信息与shared-denominator门。 新增EL18独立裂变样本projectivebranch/校准边界。 新增公开DELTAactualrun/误差与数值failure边界。 新增profile/数据秩/Cov语境与临界表分层，不能认证未匹配实验CI。 增加源Fig2动机的positive-density exact Jacobian/四次profile及条件LR边界；matched P与独立Q校准的rank要求。 Co60 gate/source与选择对象控制和原producer缺口已关联。",
      "anchor": "高自旋factorization的使用边界",
      "sources": [
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-4"
        },
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-6"
        },
        {
          "path": "knowledge/sources/kramer-flecken-1989-use-dco-ratios.md",
          "locator": "KF89-11"
        },
        {
          "path": "knowledge/sources/bargholtz-1987-high-spin-gamma-gamma-directional-correlations.md",
          "locator": "BT87-7"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-7"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-8"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-9"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-10"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-11"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-5"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-6"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-8"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-9"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-2"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-4"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-5"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-8"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-5"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-6"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-7"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-8"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-9"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-9"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-21"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
      "summary": "保存四个2009 ENSDF选定对象的hash、MR/CC固定栏、同母态AD、RI角度/弱线精度、三反应谱系及实际921 K-shell companion；raw archive/Bib key缺口显式保留。",
      "anchor": "178W评价记录：参考行里没有已给出的signed δ",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-1"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-2"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-3"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-4"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-5"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-6"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-7"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-8"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-9"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-10"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-11"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-12"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
      "summary": "精确保留既有人审全字节前缀；追加KB08原式默认/SC/误差边界、两次Z74 FO理论查询和K-companion固定点检查，均新Codex-only claims。 新增原ENSDF章/total-decay和MR字段边界。",
      "anchor": "2026-10-18 W178 K-shell理论输入与使用边界",
      "sources": [
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-1"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-2"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-3"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-4"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/internal-conversion-analysis.md",
      "summary": "保存实际W178 Kexp与shell匹配理论、两固定DCO点均在literal box外的反向检验；名义abs(delta)映射不当实验新测量。 新增原ENSDF章/total-decay和MR字段边界。 新增RZ17实际参数的概率测度/producer和尾部边界。",
      "anchor": "178W 921-keV：真实K-shell companion不能自动替两个DCO点选支",
      "sources": [
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-4"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-12"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-3"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-4"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D16-5"
        },
        {
          "path": "knowledge/sources/nndc-2009-178w-dco-reference-records.md",
          "locator": "N178-4"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-9"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-11"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
      "summary": "Surrey1997实际112页primary按定向scope读实验/分析/原表/目标/后续赋值反证，核electron装置50–400ns/K表与truncateda2；整体仍skimmed、raw归档/Bib缺口公开。",
      "anchor": "Purry 1997：先核实际测量，再使用K-shell companion",
      "sources": [
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-1"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-2"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-3"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-4"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-5"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-6"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-7"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-8"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-9"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "从Purry原P2-only estimator和实际三极角导出omittedP4的投影/正weight界，保留原weights未知，不重造测量A4。",
      "anchor": "原文a2拟合系数与完整A2不是同一个自动可移植对象",
      "sources": [
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-4"
        },
        {
          "path": "knowledge/sources/purry-1997-phd-w178-multiparticle-structure.md",
          "locator": "P97-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
      "summary": "本session完整核3页原图，TableI40行/18finiteδ与未解/星号范围分开；1003例按原phase/计算coefs作有界双比复算，不重造实验counts/CI。",
      "anchor": "2026-10-18独立Day16原件重核",
      "sources": [
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-6"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-7"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-8"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-9"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-10"
        },
        {
          "path": "knowledge/sources/konigshofen-2001-mixing-ratios-130ba.md",
          "locator": "KO01-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
      "summary": "Day16内恰好Day17无学分预习重读16页主线，核twofoldA/zerochannel/threshold、实际Table3峰面积与294打印closure失败及fullCov/高背景界，旧flags保留。",
      "anchor": "2026-10-18 Day16内恰好Day17知识预习：实际覆盖",
      "sources": [
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-4"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-5"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-6"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-7"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-8"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-9"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-10"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-11"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "summary": "保存PAQ分层、双分段actual432计数公式/derivatives、fiterrors与理想Poisson层区别、printingfailure和matchedeta/Q/fullCov门。 新增EXOGAM比值误差的任意Cov必要界及原表条件不闭合；回代不是独立P验证。 补1368文字Q与外推curve的未闭合、FOM因子化与同response身份条件。 新增GRETINA normalization/真实cut tradeoff与不同reference/Q谱系。 新增C(theta)测度/Jacobian、平均产品与经验Q重标的条件设计，实际jointkernel未恢复。 补XUNDL POL=A0与target/单位转录边界。 保存实际Stokes禁戒比值/pure反证及KN/Q归一合同。 补有限H解析消CG、actualsame-tensor dκ0/d0κ与literalevenκ U控制/消费端及真zeroI边界。 补另名fullq/Jones finiteIQUV设计、事前冻结12PSD/540点与rotation/pure/zero/nonPSD域控制，不认证原实验producer。 新增实际public能谱/共享Cov/event单位与sorting/decoder反证、P/Q readiness。 G411新批补入truth/geometry实际控制与历史源response边界。 Riley2021原件已另读并核当前模型/原论文响应迁移边界。 Co60 gate/source与选择对象控制和原producer缺口已关联。 新joint pointgate相位/firstlast/pure/KN/共同轴平均控制与闭式已写，非实验或arrayQ。 补Ni60官方reference/共同δ误差与actualSDK总分支归一，保留primaryphase缺口。",
      "anchor": "Gammasphere双分段的P/A/Q与actual峰面积",
      "sources": [
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-4"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-5"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-6"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-7"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-9"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-10"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-11"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-12"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-7"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-9"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-10"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-11"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-13"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-5"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-6"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-8"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-9"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-11"
        },
        {
          "path": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
          "locator": "L25-30"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-24"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-27"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-28"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-29"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-4"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-5"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-12"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-13"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-14"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-15"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-16"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-2"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-4"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-6"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-10"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-5"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-7"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-14"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-21"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-27"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-30"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-31"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-32"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-33"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-34"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-3"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-9"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "summary": "区分GammasphereA与genericclover计数式，链接实际data/eta/Q共同校准与sourcebound，不扩展sourceparity结论。 新增同一A/σ的nonstretched E1与stretched M1真实反例，保留DCO门/能级/选样身份。 新增真实同号A0双支、source例句/Table3冲突与needs-review边界。",
      "anchor": "双分段Gammasphere的A须随定义携带Q",
      "sources": [
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-4"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-6"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-9"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-6"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-8"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-18"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
      "summary": "用户恢复批次新增：Day16恢复批次：完整相关网络与1505-keV参考角色；actual source与条件计算分层。 新增固定ALPACA独立实现/观测对象边界。",
      "anchor": "Day16恢复批次：完整相关网络与1505-keV参考角色",
      "sources": [
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-14"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-15"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-16"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-17"
        },
        {
          "path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md",
          "locator": "KS70-18"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
      "summary": "新增固定公开C++程序的actual执行/phase/observable边界；ALPACA固定公开代码对象：先辨认算的是什么",
      "anchor": "ALPACA固定公开代码对象：先辨认算的是什么",
      "sources": [
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-1"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-2"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-3"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-4"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-5"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/iliadis-friman-gayer-2021-polarization-direction-correlations.md",
      "summary": "新增固定公开C++程序的actual执行/phase/observable边界；2026-10-18 Day16恢复：固定C++实现实际执行",
      "anchor": "2026-10-18 Day16恢复：固定C++实现实际执行",
      "sources": [
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-4"
        },
        {
          "path": "knowledge/sources/alpaca-2023-v105-angular-correlation-code.md",
          "locator": "AC23-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
      "summary": "新增ENSDF原相位/format与total-decay条件权重；Martin 1987：相位定义与完全未观测跃迁",
      "anchor": "Martin 1987：相位定义与完全未观测跃迁",
      "sources": [
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-1"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-2"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-3"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-4"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-5"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
      "summary": "新增ENSDF原相位/format与total-decay条件权重；Tuli 2001：不能把MR省略符号读成已知正号",
      "anchor": "Tuli 2001：不能把MR省略符号读成已知正号",
      "sources": [
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-1"
        },
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-2"
        },
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/deorientation.md",
      "summary": "新增ENSDF原相位/format与total-decay条件权重；未观测γ与全部衰变的条件权重",
      "anchor": "未观测γ与全部衰变的条件权重",
      "sources": [
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "summary": "新增ENSDF原相位/format与total-decay条件权重；Radiative、电子与总衰变权重：同符号不等于同对象 新增RZ17实际参数的概率测度/producer和尾部边界。 新增先相位后版本及字段参考flag的真实A25案例。",
      "anchor": "Radiative、电子与总衰变权重：同符号不等于同对象",
      "sources": [
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-3"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-4"
        },
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-1"
        },
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-2"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-8"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-12"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-6"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/polarized-photon-branch-audit.md",
      "summary": "新增ENSDF原相位/format与total-decay条件权重；ENSDF原1987相位章与固定程序执行：新直接来源",
      "anchor": "ENSDF原1987相位章与固定程序执行：新直接来源",
      "sources": [
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-2"
        },
        {
          "path": "knowledge/sources/martin-1987-ensdf-mixing-ratio-phase-conventions.md",
          "locator": "MA87-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
      "summary": "实际RZ17参数的测度/变量变换/卷积与尾部自审；保留作者结果和review。",
      "anchor": "2026-10-18原式复核：P(delta)的测度与卷积配方边界",
      "sources": [
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-8"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-9"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-10"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-11"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/icc-mixing-probability-domain.md",
      "summary": "实际RZ17参数的测度/变量变换/卷积与尾部自审；保留作者结果和review。",
      "anchor": "ICC反演混合比：先定义概率对象",
      "sources": [
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-8"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-9"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-11"
        },
        {
          "path": "knowledge/sources/rezynkina-2017-graphical-extraction-multipole-mixing-ratios.md",
          "locator": "RZ17-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
      "summary": "EL18实际104Mo分支/共享G校准/打印重放边界，原δ/review保持。 新增公开DELTAactualrun/误差与数值failure边界。 新增104Mo评价时层/target身份及标签使用边界。",
      "anchor": "2026-10-18 Day16独立复读：projective分支与共享衰减",
      "sources": [
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-5"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-6"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-7"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-8"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-9"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-10"
        },
        {
          "path": "knowledge/sources/eldridge-2018-gamma-band-mixing-ratios.md",
          "locator": "EL18-11"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-1"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-5"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-7"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-1"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-2"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-3"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-4"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
      "summary": "固定内容的公开DELTA实际执行和phase/error/limit/pure数值边界。 实际抽未改F unit编译/运行，Gill表与JT74表不同、finiteν/default边界。",
      "anchor": "DELTA1.01：generic producer与实际实验分析要分开",
      "sources": [
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-1"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-2"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-3"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-4"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-5"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-6"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-7"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-8"
        },
        {
          "path": "knowledge/sources/ekstrom-1993-delta101-angular-correlation-code.md",
          "locator": "D101-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
      "summary": "实际104Mo对象target/ref/空MR/旧标签与评价时层、companion谱系核验。 新增官方NSR/2002XUNDL110行：混合谱系、target空M/MR/缺DCO与纯统计T注释；不当primary正文。",
      "anchor": "104Mo：旧评价标签不替后来混合比分支选根",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-1"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-2"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-3"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-4"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-5"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-6"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-7"
        },
        {
          "path": "knowledge/sources/nndc-2007-mo104-selected-gamma-reference-records.md",
          "locator": "N104-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
      "summary": "本session原11页主线/两表八图重核；真实DCO门/峰面积、nonstretched E1负偏振、Q误差条件边界与共享校准回代，恰好partial17不授学分。 补1368文字Q与外推curve的未闭合、FOM因子化与同response身份条件。",
      "anchor": "DAY16延续：EXOGAM原表、门身份与校准误差边界",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-6"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-7"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-8"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-9"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-10"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-11"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-12"
        },
        {
          "path": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
          "locator": "Z13-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
      "summary": "原9页三表六图重读；profile/F处方、rank与Cov语境、真实Table3概率核验及实际DELTA F unit对照，纠正旧摘要笼统correlation措辞。 增加源Fig2动机的positive-density exact Jacobian/四次profile及条件LR边界；matched P与独立Q校准的rank要求。",
      "anchor": "DAY16原文重核：profile阈值、F表与相关性的语境",
      "sources": [
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-5"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-6"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-7"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-8"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-9"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-10"
        },
        {
          "path": "knowledge/sources/james-twin-butler-1974-angular-correlation-statistics.md",
          "locator": "JT74-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
      "anchor": "Morse2022：实测标定与模拟曲线分开",
      "summary": "新取得并读完UNC13页authorpreprint；6quad实测/角门/Q半因子、四cut与tuning反证/GRETA模型范围，真实表与physical-domain复算。 加公开code反链，保留pureE2反证和exactproducer缺口。",
      "sources": [
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-1"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-2"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-3"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-4"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-5"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-6"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-7"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-8"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-9"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-10"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
      "anchor": "DAY16无学分预习增量：数据身份与新约定自审",
      "summary": "完整10页三表七图重核，8行实测/作者分支与符号冲突、RB/native单emitter桥、Pi/Q/排序合同；旧人审fullprefix不动。 新增公开Fig4矢量积分、literalprose未闭合及source/event平均/Q一致迁移条件；不判实验错误。",
      "sources": [
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-17"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-18"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-19"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-20"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-21"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-22"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-23"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-24"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-25"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-26"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-27"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-28"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-29"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
      "anchor": "DAY16必要companion：Q的观测与参考角色",
      "summary": "定向Sec5/参考校准的实际Q定义和1173-gated1333对象；保持整个旧humanreview prefix与1–29 flags。",
      "sources": [
        {
          "path": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
          "locator": "L25-30"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/gretina-25na1041-polarization-response-contract.md",
      "anchor": "25Na1041：同号偏振如何参与分支判别",
      "summary": "真实AD/偏振双候选与matched response/calibration谱系，明确无RDCO与无新实验CI；保存phase/pure/physical/选择失败控制。 补22Ne参考图平均边界，不迁sourceC到1041或据cut图给实际最优/新CI。 官方Ei/Ef和2009/2025 MR版本已直接补齐，不增加独立δ证据。 补publiccore边界、正确native分支及初始identity纠错。 补有限H解析消CG、actualsame-tensor dκ0/d0κ与literalevenκ U控制/消费端及真zeroI边界。 补另名fullq/Jones finiteIQUV设计、事前冻结12PSD/540点与rotation/pure/zero/nonPSD域控制，不认证原实验producer。 保存真实publicsource仍不matching1041response及selector担忧收窄。",
      "sources": [
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-18"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-19"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-21"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-23"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-24"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-25"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-26"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-4"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-8"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-9"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-10"
        },
        {
          "path": "knowledge/sources/morse-2022-gretina-polarization-sensitivity.md",
          "locator": "M22-11"
        },
        {
          "path": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
          "locator": "L25-30"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-27"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-28"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-29"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-2"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-3"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-4"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-6"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-7"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-12"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-13"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-14"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-15"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-16"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
      "anchor": "A=25：评价字段与原实验的观测对象",
      "summary": "新增十对象身份、旧新MR/phase/fieldprimary矩阵、XUNDL POL和单位转录边界与条件加权重放；不是新实验。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-1"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-2"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-3"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-4"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-5"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-6"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-7"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-8"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-9"
        },
        {
          "path": "knowledge/sources/nndc-2025-a25-mixing-reference-records.md",
          "locator": "N25-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
      "anchor": "UCGretina：发射代数、软件实现与阵列响应分开",
      "summary": "固定公开2021/2026 Stokes代码和Geant4原函数，实际core/独立trace/phase/purelimit核验；保存mixed高rank浮点失败、反证与producer边界。 补有限H解析消CG、actualsame-tensor dκ0/d0κ与literalevenκ U控制/消费端及真zeroI边界。 补另名fullq/Jones finiteIQUV设计、事前冻结12PSD/540点与rotation/pure/zero/nonPSD域控制，不认证原实验producer。 Riley2021原件已另读并核当前模型/原论文响应迁移边界。",
      "sources": [
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-2"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-4"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-6"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-12"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-13"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-14"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-15"
        },
        {
          "path": "knowledge/sources/ucgretina-2021-polarized-emission-code.md",
          "locator": "UC21-16"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
      "anchor": "Eu152公开能谱：实际数据能支持哪一层校准",
      "summary": "真实ROOT源/背景counts和window/Cov传播，sourceevent分母及truthsorting、GRUT降序counterevidence；不代原ComptonQ/arrayresponse。 G411新批补入truth/geometry实际控制与历史源response边界。 Riley2021原件已另读并核当前模型/原论文响应迁移边界。",
      "sources": [
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-2"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-4"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-6"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-10"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
      "summary": "新建固定G411源能谱软件source，核原truth双失败/source-only追加、nativeABI、同种子有效core不变和源框顺序实际导航边界。 新1000history统计控制核跨区Cov正负、PSD/双算法与zero-hit概率界。 各100k实际运行/四区/有限Σ及三个高区history的能量闭合已写回，未做实验Q/δ/旧fit。 Riley2021原件已另读并核当前模型/原论文响应迁移边界。 Co60例native开关/几何/混合/1k/坐标/missing与prefixback、F3双路线已记录。 两组100k实际source moment/cov与detectorstatistics通过，控制图/CSV/PDF及QA已交付；不拟Q或实验δ。 新joint pointgate相位/firstlast/pure/KN/共同轴平均控制与闭式已写，非实验或arrayQ。 补Ni60官方reference/共同δ误差与actualSDK总分支归一，保留primaryphase缺口。",
      "anchor": "G411源模拟：程序退出、有效记录和实验响应分别核验",
      "sources": [
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-2"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-4"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-6"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-12"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-13"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-14"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-15"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-16"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-17"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-18"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-19"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-20"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-21"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-22"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-23"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-24"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-25"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-26"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-27"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-28"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-29"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-30"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-31"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-32"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-33"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-34"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-3"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-9"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/gretina-eu152-source-response-replay.md",
      "summary": "新建source-response合同，保存已执行模型边界及fixedN/compound-Poisson有限MC推导，未报未完成100k结果。 新1000history统计控制核跨区Cov正负、PSD/双算法与zero-hit概率界。 各100k实际运行/四区/有限Σ及三个高区history的能量闭合已写回，未做实验Q/δ/旧fit。 Riley2021原件已另读并核当前模型/原论文响应迁移边界。 Co60 gate/source与选择对象控制和原producer缺口已关联。",
      "anchor": "source-calibration可复用关口",
      "sources": [
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-1"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-2"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-4"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-5"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-6"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-7"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-8"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-9"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-10"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-11"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-12"
        },
        {
          "path": "knowledge/sources/ucgretina-2012-eu152-public-calibration-data.md",
          "locator": "UE12-3"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-13"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-14"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-15"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-16"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-17"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-1"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-7"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-13"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-14"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-18"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-21"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
      "summary": "新建Riley2021 arxivv1实际全主线/12图/两表/Eq1 source，核12quad身份、有效层/模型CI、低能与continuum反证、5733点/Compton机制及Q迁移边界。",
      "anchor": "能谱匹配的有效参数与偏振响应需要分别验证",
      "sources": [
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-1"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-2"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-3"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-4"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-5"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-6"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-7"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-8"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-9"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-10"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-11"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-12"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-13"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-14"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-15"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-16"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-17"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-18"
        },
        {
          "path": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
          "locator": "L25-30"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/co60-gate-role-response-benchmark.md",
      "summary": "新建Co60同源不同target/gate/响应对象表、实际小样本门/缺失/坐标/backflag控制、声明混合级联相位与有限MC设计；100k实际结果已写回。 两组100k实际source moment/cov与detectorstatistics通过，控制图/CSV/PDF及QA已交付；不拟Q或实验δ。 新joint pointgate相位/firstlast/pure/KN/共同轴平均控制与闭式已写，非实验或arrayQ。 补Ni60官方reference/共同δ误差与actualSDK总分支归一，保留primaryphase缺口。",
      "anchor": "同一个60Co源需要分别保存γ角色和响应对象",
      "sources": [
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-19"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-20"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-21"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-22"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-23"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-24"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-25"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-26"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-27"
        },
        {
          "path": "knowledge/sources/riley-2021-ucgretina-energy-response.md",
          "locator": "R21-5"
        },
        {
          "path": "knowledge/sources/lauritsen-2025-gamma-angular-formalism-tracking-arrays.md",
          "locator": "L25-30"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-28"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-29"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-30"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-31"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-32"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-33"
        },
        {
          "path": "knowledge/sources/ucgretina-2024-geant4-11-source-replay.md",
          "locator": "UG24-34"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-3"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-9"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
      "summary": "新增2013Ni60/Co60两官方对象的固定列/版本/共同MR/RI/CC谱系、静止反冲、条件误差与actualSDK分支审计；原phase正文未取得。",
      "anchor": "评价输入与实际观测要分开",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-1"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-2"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-3"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-4"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-5"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-6"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-7"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-8"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-9"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-10"
        },
        {
          "path": "knowledge/sources/nndc-2013-ni60-co60-reference-records.md",
          "locator": "N60-11"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

### 下一有界问题仍是同一Stokes合同

有限H与κ指标问题已有直接来源/同输入比较；U在明确Jones/G4轴下的literal偶κ控制也已隔离。后续若构建有限general表达式，须从这些式子推导、另名保存并做PSDrho与完整IQUV/rotation/purelimit验证，不能只flipU让残差过或修改原externalcode。完整arrayproducer/response/experimentalCov继续缺失。


### 由实际code结果产生的下一问题

原实现的0/0×F需在数学上先消去CG，再作为独立设计实现验证，不能静默patch原源、把NaN置0或用pure控制掩盖。一般κ/coherence、轴极限和source/target selection仍未覆盖；这些属于当前Stokes/Compton预习路线，须先冻结新合同再开展，不能凭当前168calls当全部范围通过。


### A=25剩余高信息缺口

已解决旧2009三reference数字与当前target身份；未解决FSU原paper角分组35/145与评价概述45/135的原始口径、实际alignment/feeding/fitCov，以及L26所用Q/联合response。下一有界路线为已定位2015Vo12的合法primary与其同跃迁AD论证；先冻结问题，不能把metadata当正文或重复无信息失败访问。


GRETINA新增belief revision：Pbar并非脱离selection/kernel的通用一个数；Q本来按特定平均/归一校准，改变target平均而固定旧Q不能当响应修正。Fig4 literal曲线积分未闭合prose about值，下一须核实际≥2hit/θψ/source normalization/未舍入producer，而非调坐标或sigma追目标。当前publiccurve可复算不等于rawresponse恢复，作者1041选支保留adopted-response条件。精确target Ei/Ef与knownδ reference谱系尚可用官方数据再核。

新增Z13问题：Table I括号σ的实际定义、原a/Q/AD联合Cov及未舍入producer；同校准回代不独立。

新增当前问题：RZ17实际RooFit居中/physicaldomain/区间recipe；EL18groupG与106Mo更正列、unroundedΣ/DELTA版本；Goodin2010是否同events及何处被修订。公开DELTAgeneric程序已取到且实际运行，仍不能以同名程序回答这些actualproducer问题。各canonical source/method保留精确locator与下一输入，不把它们转为默认用户待办。

Dors[3]身份冲突已经定位到准确DOI，尚待全文给169/137的约定与误差。DCOMAP/width/finite response/feeding与Table1差异未决；两R与强度的Cov未得。原先“加P符号便能选两支”的直觉被本次同号例限制；更高信息输入是matched P幅值校准。缺口由Codex跟踪，不转为默认用户审核任务。

## L0–L4 state

L0为三篇主线/原图回核；L1/L2为新证据单和反向验证；L3调查已由用户恢复至原15:00截止，169参考定义/producer与新原件缺口保持开放。尚未进行experimental L4 refit；已有条件设计不冒充实际数据分析，也未取得完整input/response/Σ。新增真实可执行的source-only MC与history统计子任务，版本/输入/单位/模型Cov/失败检查均存档；它不补齐experimental L4 refit的原事件、matching偏振response与联合Σ。未新增人审或修改旧needs_review。

## Verification and continuation

### Conditional Stokes checkpoint026验收

[verification-reopened-020](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-020.json)report/card/唯一writeback42/42通过，boundary/diff/lint实际exit0、0errors172warnings（128citation-key、41raw槽、3reaction-parser）；L26/L25人审prefix、PLAN/Bib保护通过。newjoint/closedform actual0，source代码/输入未换成实验事实，原图QA及025的格式暂存纠正证据保留。

原硬截止仍2026-10-19 15:00上海，freshclock/receipt候选门显示尚有约9h+，goalactive继续。下一Ni60 officialreference的Adopted与long-Co60beta两个精确文本对象HTTP200已得，physics rows尚未读；不混异构态、不把下载metadata预写成MR结果。内容指针main / `Trace DAY16 conditional calibration polarization and averaging`，actualhash/push只publication026/runreceipt。

### Co60 checkpoint025验收与继续门

暂存纠正留档：首次gitadd因通用PDFignore返回1，生成SVG行尾空格/CSV CRLF亦被cached check发现；随后在确认门未过前误触发的本地提交从未push。已将exporter改为SVG行尾清理/CSV LF、仅显式纳入一份生成图PDF并补HEAD日志＋ownentry，原data cells和PNG像素逐位不变；在同一未发布提交上amend一次并重跑完整门。初失败与最终证据见publication-025-stage-and-format-correction及最终verification/H3，不改变ignore规则或纳入raw论文。

[verification-reopened-019](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-019.json)actualreport/card/唯一writeback42changed/42items通过，boundary/diff/lint均exit0、0errors172warnings（128citation-key、41raw槽、3reaction-parser）。L26/L25人审prefix/PLAN/Bib保护与原724file/binary hash通过。figure另有source/font/collision/alignment/visual QA：退出0、min7pt，source仅“PNG无TIFF”warning按research-note合同保留，非submissionraster认证。

原截止仍2026-10-19 15:00上海，freshclock约04:34尚余625min，goalactive继续，completed16仅一次/partial17。下一point-reference first/last conditionalStokes问题已冻结回忆，不预设pureE2对称性；不从关闭polarizedEM的MC反推P/Q、不重试2017终态入口。本批内容指针main / `Validate DAY16 Co60 gate roles and source angular correlation`，精确hash/actualpush只publication025/runreceipt。

### Riley2021 checkpoint024验收

[verification-reopened-018](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-018.json)实际report/card/唯一writeback通过：41changed/41items；boundary/diff/lint均exit0，0errors172warnings（128citation-key、41raw槽、3reaction-parser）。原L26/L25人审prefix和PLAN/Bib hash保持。paper26页/12图及typedtable/parser/Compton交叉核验均有实际artifact，保留新primary为arxivv1、原fit/producer/Cov未复现的边界。

publication023已actualGitee/HEADorigin核准；本批内容指针main / `Read DAY16 primary energy response and calibration boundaries`，精确hash/实际push仅后续publication024/runreceipt。03:15上海仍距原15:00约705min，goalactive，继续原校准分母/选择companion候选；本checkpoint不结束窗口、不给Day17正式学分。

### Source-MC checkpoint023实际检查与后续原件

各100000history的run、native/GEB和history统计脚本实际exit0；8000bins/四区/history求和、PSD、独立NumPy Cov与输入hash检查通过。原724blobs fresh复核无mismatch。原truth失败、源框顺序差别、warning和beta边界未被通过结果覆盖。[verification-reopened-017](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-017.json)实际report/card/唯一writeback通过（40changed/40items），boundary/diff/lint均exit0、0errors/170warnings（127citation-key、40raw槽、3reaction-parser）。PLAN/Bib与L26/L25旧人审prefix保护通过。初汇总wrapper误把textlint当JSON的exit1已修正并留档，原required检查本身均0。

下一continuity companion为Riley2021 DOI10.1016/j.nima.2021.165305：回忆已冻，Crossref/arXiv200且实际PDF26页/identity核准，当前仅首身份页已读，12figures/全文主线尚待核。没有把摘要/metadata作新的scientific claim。仍按原2026-10-19 15:00上海截止继续，goalactive，formal16只计一次/partial17。


### Public-data checkpoint022验收与下一response输入门

[verification-reopened-016](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-016.json)实际report/card/writebackvalid（38 changed knowledge pages/38 items），boundary/lint/diff均exit0；lint0errors168warnings（126key/39raw/3parser）。原ROOT读后hash、L26/L25旧humanprefix、PLAN/Bib保持。首次数字矩阵doublebracket被lint当wikilink，已只改表示法、原失败/initialverification保留，未改科学数字追检查。

本批实际rawcount/条件Cov/selector/upstream反证均有artifact；没有Compton事件/MC模板/fullfit/Q重建。SDK11.4.2/ROOT存在，UCGretina/grutinizer binary不存在；下一先读固定geant4.11 branch的真实build/geometry/source依赖，判断能否在repo tmp构建有版本限定的source能谱MC。前置primed回忆/输入门已冻于ucgretina-source-response-build-before.md/hash；若缺依赖或matching input如实notready，不造MC或调geometry强配。原19日15:00上海deadline/goalactive、formal16一次partial17不变。


### Fullfinite checkpoint021检查与候选池重建

[verification-reopened-015](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-015.json)实际report/card/writebackvalid，37 changed pages/37 items；required boundary/lint/diff均0，lint0errors166warnings(125key38raw3parser)。完整设计原540点/PSDrho控制通过，清单里native–RB同步变换控制曾首脚本未执行，已保留首脚本snapshot006/结果并补实际control残差0，最终结果另存未覆旧。原source/binary、人审prefix/PLAN/Bib保持。

[新timegate/pool](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-reopened-014.json)于00:59上海核剩840.8分钟，Day17卡154–161重新读取，formal16/partial17不变。单emitter代数局部饱和后不继续堆toy；已冻结真实公开sorting/source-calibration入口的primed回忆，下一核actualUCG例的ROOT/sorting是否真有P/A/Q所需同对象数据，缺则写精确readiness，不裸迁几何。原15:00截止/goalactive保持。


### 有限H与一般tensor checkpoint020验收

[verification-reopened-014](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-014.json)实际report/card/writeback通过（仍37 changed knowledge pages/37 items），boundary/lint/diff均exit0；0errors/166warnings（125key/38raw/3parser）。新脚本finiteH、samepol-oldLegendre及originalevenκ U均exit0，初一般bridge失配保留；未把脚本0当generalvalidated。L26/L25旧humanprefix、PLAN/Bib保持。

00:44上海仍距原15:00约856分钟，goal保持active。下一完整finite tensor/Jones推导已在ucgretina-full-finite-design-before.md/hash冻结，尚未新执行；先保留既有source/counterevidence，再按合同对新PSD态核全IQUV。Geant4说明网页404/DNS失败有实际记录，未据此编造manual文字；现有证据来自固定代码和数学定义。原run/学分/partial17及截止不变。


### UCGretina checkpoint019检查与续接

[verification-reopened-013](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-013.json)实际report/card/writeback通过，37 changed knowledge pages/37 items；boundary/lint/diff均exit0。Lint 0errors/166warnings＝125 citation-key、38 raw槽、3 reaction-parser。新source首次缺title_original、批量替换误伤一处N25 wikilink都已由检查发现并修复，初日志保留ucgretina-first-lint.json；未改输入追检查。TLS与Na坐标首轮错误也明确留档，v2物理/phase核验才写canonical。原L26/L25人审prefix与PLAN/Bib保护通过。

00:18上海仍距原15:00约882分钟，goal active，formal16仅一次next17/count16、partial17。下一有限表达式/一般κ问题已[冻结](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ucgretina-regularized-before-freeze.json)，继续当前Stokes路线，不以代码checkpoint结束学习窗。FSU2015目前primarybody未得，合法metadata/机构目录/search失败与无关身份拒绝均留档；不把它们当原文。

### A=25 checkpoint018检查与持续窗口

[verification-reopened-012](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-012.json)实际report/card/writeback通过，36 changed knowledge pages/36 items，唯一writeback；boundary/lint/diff均exit0。Lint为0errors/164warnings（124 citation-key、37 raw槽、3 reaction-parser），新source未改raw/Bib，warning明确保留。初次缺两个source固定标题、表格竖线解析和末尾空行已纠正，原失败见a25-first-execution.json；未改科学输入追过检查。L26/L25人审prefix、PLAN/Bib hash保持。

上海23:45仍距原次日15:00约915分钟，goal active/pursuing，本checkpoint不是整窗停止。2015Vo12原文前回忆已冻并明示priming；publisher accepted403/harvest401、Scholar timeout与泛匹配arXiv身份拒绝均有记录。只沿合法新入口继续，不把失败当正文或原样重试终态；next17/count16保持，partial17不授正式信用。

### 历史提前收束时间门与候选池（已由用户恢复）

[最终候选/clock审计](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-007-closeout.json)记录科学研究停于 **2026-10-18T13:36:07+08:00**，距原研究硬截止仍 **1523.88 min**。截止不是停止原因，也未被改写。已再次查原receipt与matrixDay17，重建W178/相位continuity、独立130Ba novelty及恰好Day17preview候选池；新NRF公开路线仍无body，源/数据缺口构成本轮继续高价值判断的边界。

剩余输入具体为actualDCOMAP及Dorsreference定义、Purry逐line校准曲线/peak-gate ledger/联合Σ、SG98 unroundedproducer/perdetectorfit-calibrationCov，以及NRF2022footnote2/2023corrigendumbody。更多同toy重跑、adopted标签、自由调σ/η/Q或终态访问重试不能替代这些输入。这是已重建当前池内的停止判断，不宣称世界上全部合法来源穷尽；下一真实input可重新触发具体claim研究。

KS70追加twoangle问题因旧KS70-12已经覆盖而verified-no-op；NRF追加公开检索没有产生新科学claim。[NRF去重审计](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/nrf-route-dedup-audit.json)承认去重前重复GET两旧机构页，零增益、后续停止；未重复旧terminalPDF/XML，也未由metadata猜勘误内容。新增science均已canonical；这些访问回执只是过程证据。

### 实际检查与交付

- [verification008](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-checkpoint-008.json)：16 changed知识页/16writeback items有效；boundary/diff/lint exit0，0errors/150warnings（117 citation-key missing、30 raw missing、3 reaction parser）。新source的archive/Bib槽缺口保留；不冒称raw已归档或paperready。原件/temporaryprimary hash、PLAN/Bib与KB08人审prefix核通过。
- 首轮6个research-note栏目、后来N178缺ExtractedPages的lint exit1都已修复并留原回执；SG98 294printingclosure仍是**隔离的科学边界**，不伪报7行全复现。代码initial snapshot的精确hash/replay见[initial-code-replay-proof](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/initial-code-replay-proof.json)，不改变物理输入。
- 科学publication001–004实际fetch/ancestry/dry-run/non-forcepush均成功、各自originHEAD匹配；新preview/收束修改使用精确manifest继续同一门。actualhash/最终remoteoutcome只记run receipt，不写在所属commit正文；当前分支/主题稳定指针见handoff与最终回执。
- QMD status exit0：562indexed/2459vectors、349orphanchunks、38pending，外部cache更新deferred；直接原件/知识检查不冒称新页已被旧索引收录。Farmer watcher PID42019实际运行，无Git角色；没有新daemon/session/hosttask或GUI Scheduled。
- [下一正式Day17prompt](prompts/20261019-DAY17-linear-polarization-paq-compton.md)只准备2026-10-19的独立run，未启动、未授学分。[本日续接](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/continuation-current.md)与[run.json](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/run.json)保存session/resume。原runner成功退出未观察，使用manual reconciliation，不伪造normalrunner/clock/scheduler事件。

[final-verification.json](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/final-verification.json)已实际验证报告/card/writeback有效（只completed16/partial17）、preflight/boundary/lint/diff均exit0、0errors/150warnings；8份mappedoriginalraw与3份共享helper的freshhash另核通过。发布与课程最终结果只在run.json按实际命令更新；课程只计Day16一次、保留partial17，不开Day18。此前科学收束后的closeout-only现已被用户恢复指令覆盖；当前继续研究至原截止。

最终科学发布已成功（main / `Finalize DAY16 evidence and uncredited Day17 polarimetry preview`）；课程与完成回执稳定指针main / `Complete DAY16 card and reconcile course state`。正式coverage为completed[16]/partial[17]、next17/count16，normalrunnerexit未观察，不伪造退出码。下一正式17仅有准备prompt，未启动。


### 恢复checkpoint007（研究继续）

2026-10-18 16:47上海，fresh boundary/lint/diff均exit0，0errors/150warnings；[恢复验收](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-001.json)通过report/逐卡/唯一writeback与保护状态，累计17changed/17items，本批4页知识变化。稳定指针main / `Extend DAY16 with Cd110 reference-role and network audits`，exacthash/actualpush只回执。此为checkpoint，goal/window仍active至原2026-10-19 15:00，下一ALPACA code-object新路线已冻结问题但未执行。


### 恢复checkpoint008（研究继续）

2026-10-18T17:06:46.396253+08:00：actual ALPACA C++/GSL及selectedtests/CABI已核，required boundary/lint/diff均0，0errors/152warnings；[验收002](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-002.json)通过19changed/19items和单卡coverage。稳定指针main / `Validate DAY16 phases with the pinned ALPACA C++ implementation`，actualhash/H3/push只回执。Goal/window继续active，当前转官方ENSDF原manual相位说明，不重计Day16或开启Day18。


### 恢复checkpoint009（研究继续）

2026-10-18T17:32:44.322159+08:00：累计24changed/24writeback，原phase章和168.71conditionalexercise已canonical。Boundary/diff/lint-fixed实际exit0，0errors/156warnings；首Tuli缺required限制栏目lint1已修并保留。[verification003](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-003.json)通过单卡coverage/writeback/hash/KB08旧prefix保护。稳定指针main / `Separate DAY16 phase conventions and unobserved decay channels`，实际hash/remote只回执。下一继续RZ17变量变换/概率域，goal/windowactive原15:00，不重计卡。


### 恢复checkpoint010（研究继续）

2026-10-18T17:49:31.347570+08:00：actual RZ17/Table1 probabilitymeasure/tail exercise已canonical；累计26changed/26items，boundary/diff0，method栏目缺项造成的首次lint1已补齐、fixed lint实际0/0errors156warnings。验收004保留initialexit/history纠正。[候选刷新](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-reopened-004.json)在原截止前仍约1272min，下一独立EL18实测branch/Gk问题已冻结/开读，window/goal继续active。稳定指针main / `Audit DAY16 ICC probability measures and pure-limit tails`，exacthash/actualH3/push只回执，不重计Day16或开Day18。


### 恢复checkpoint011（研究继续）

2026-10-18T18:05:06.303600+08:00：EL18实际branch/G校准/printing边界已canonical；[验收005](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-005.json)通过27changed/27items、单卡coverage、actualboundary/lint/diff0，0errors156warnings。稳定指针main / `Trace DAY16 projective mixing branches and shared IPAC calibration`，exacthash/actualH3/push只回执。继续官方DELTA原程序route，window/goal保持active至原15:00，不重计卡。


### 恢复checkpoint012（研究继续）

2026-10-18T18:30:38.431770+08:00：DELTAactualpubliccode/execution/数值failure已canonical，[verification006](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-006.json)通过28changed/28items、singlecard、actualboundary/lint/diff0，0errors158warnings、继承dirty保护。稳定指针main / `Validate DAY16 DELTA source contracts and interpolation controls`，actualhash/H3/push只回执。下一Goodin机构primary路线继续，原deadline/goalactive不变，无重复学分。


### 恢复checkpoint013（研究继续）

2026-10-18T19:02:26.083951+08:00：N104实际reference/object时层已canonical，验收007通过29changed/29items与singlecreditcoverage；actualboundary/diff0、lint-first缺Scope已修后0/0errors160warnings。稳定指针main / `Trace DAY16 Mo104 reference identities across evaluated data`，exacthash/actualH3/push只receipt。继续EL18引Daniel2007原方法/ORA可访问原件路线，不以metadata补原文，goal/window保持active至原15:00。

### 恢复checkpoint014（研究继续）

[verification-reopened-008](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-008.json)实际boundary/lint/diff均exit0，report/card/writeback通过，30 changed knowledge页/30 writeback items；lint为0 errors、160 warnings（122 citation key、35 raw归档槽、3 reaction parser）。Z13旧正文/claim flags除updated日期外完整保留，原PDF/PLAN/Bib/protected hashes未变。arxiv表初次逐行text检查因871换行exit1，改按完整行段后11项通过，输入未改；失败在版本核验回执保留。

[最新时间门/候选池](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-reopened-009.json)余1172.5分钟，原次日15:00截止不变。下一Gu96 primary前回忆已冻，追104Mo旧DCO/reference与谱系；本checkpoint继续原goal，不重授16或正式17。续接[continuation-current.md](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/continuation-current.md)已更新；发布稳定指针main / `Audit DAY16 EXOGAM gate identities and calibration uncertainties`，实际hash及结果仅回执。

### 恢复checkpoint015（研究继续）

[verification-reopened-009](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-009.json)实际boundary/lint/diff均exit0，report/card/writeback通过，31 changed knowledge页/31 items；lint0errors160warnings（122key/35raw/3parser）。新source/code/method旧flags及raw/protected保留，JT74只修旧摘要correlation措辞，旧claim flags未动。F unit compile/run0、非regular符号/trace/physical/response失败控制通过；缺SymPy首exit1及isolated安装/analysis0的过程回执保留。

[刷新候选池010](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-reopened-010.json)余1126.49min，原deadline不改；JT74/Mo104当下边界已核，继续恰好Day17的L26 GRETINA response知识preview。source-before及完整旧人审prefix已冻结，raw hash已核，仅前两页已读，未做新claim；后续完整主线再判。正式16只计一次，partial17不授学分，未开18。更新[续接](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/continuation-current.md)，稳定发布指针main / `Trace DAY16 profile thresholds and conditional identifiability`，实际hash/结果仅receipt。

### 恢复checkpoint016（研究继续）

[verification-reopened-010](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-010.json)最终boundary/lint/diff均exit0、report/card/writeback通过，35 changed knowledge页/35 items；lint0errors162warnings（123key/36raw/3parser）。首次新research-note缺schema及M22缺ExtractedPages共17error、writeback缺directsource link均已修，保留初exit1/false日志；fixed actual0/true。两旧human source全prefix bytehash通过，protected raw/PLAN/Bib不变。代码首symbolic == guard exit1，component simplification后0；新增parity标签/pure-contract控制后再跑0，frozeninputs/旧helpers不变。

[timegate/pool011](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-reopened-011.json)余1028.48min，继续原goal。下一L26Fig4公开C(theta)平均问题先冻回忆/边界；PDF5的vectorSVG已提取，尚未digitize/计算，不称rawresponse或新P/Q测量。prepared17 prompt补完整priming，未启动session/授学分。沿用[续接](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/continuation-current.md)和原deadline；稳定发布指针main / `Audit DAY16 GRETINA calibration conventions and branch evidence`，实际hash/结果仅receipt。

### 恢复checkpoint017（研究继续）

[verification-reopened-011](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-011.json)实际boundary/lint/diff均exit0，report/card/writeback通过；35 changed knowledge页/35 items，lint0errors162warnings（123key/36raw/3parser）。旧两source人审prefix逐字节/protected hash保持，source/coverage/script哈希与numericcontrols通过。图形axis不是拟合误差，literalapprox未闭合与jointkernel/实际Qcov缺口保持，不造新实验结果。

[timegate/pool012](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/candidate-refresh-reopened-012.json)余966.38min，检查恰好下一卡后继续同案例official25Na/25Mg targetreferenceidentity。source-before回忆已冻，NNDC lists实际2025-08ENSDF与2026-02postcutoffXUNDL发现，未授独立实验/课程credit；selecteddata下载后按实际scope/原字段审计。prepared17prompt补Fig4priming，未启动session。沿用[续接](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/continuation-current.md)/原deadline；发布稳定指针main / `Trace DAY16 polarization averaging and calibration transfer`，actualhash/H3/结果仅receipt。


### Checkpoint027实际验收与持续研究

[verification-reopened-021](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/verification-reopened-021.json)实际通过report/card/唯一writeback（43 changed knowledge pages/43 items）、新script/inputhash、旧人审prefix/PLAN/Bib保护；boundary/lint/diff各exit0。Lint为0errors174warnings：129citation-key、42raw归档槽、3reaction-parser。SDKhelper编译/执行0、原输入不变；共同δ误差仍只为模型分量。

CSU真实REST已由其官方hashedconfig修正主机，exacttitle查询200/0对象，区别于UI同host/server404；没有取得1980正文。发布稳定指针main / `Audit DAY16 Ni60 reference uncertainties and source branches`，actualhash/H3/push仅publication027/runreceipt。当前06:02上海距原15:00仍约538分钟，goalactive/学分16一次partial17保持；继续有价值新来源或matching response输入，不以本checkpoint收束。
