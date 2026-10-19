---
type: output
graph-excluded: true
created: 2026-10-19
updated: 2026-10-19
---

# Day17：线偏振、P/A/Q与Compton响应

## Run state

- run_id: `2026-10-19-day-17-01`
- run_date: `2026-10-19`；timezone: `Asia/Shanghai`；day_index: `17`
- session_id: `01a1532e-0f21-7903-9bf6-8a9cc9ee9e17`
- phase: `angular-correlation-polarization-and-mixing-ratio`
- schedule_id: `wiki-daily-learning`；Docker-local，非GUI Scheduled对象。
- hard_deadline: `2026-10-20T15:00:00+08:00`；15:00–16:00仅收束。
- status: `running / substantive checkpoint`；原生goal为active，未提前关闭研究窗口。
- completed_day_indices: [17]
- partial_day_indices: [18]
- Day 17 card audit: complete
- 启动课程文件为next17/count16；正式17只在本卡验收/发布后对账一次，原整日研究窗口继续；Day16预习、旧程序检查与旧分数不兑换正式17。本session只允许正式17，最多无学分partial18，不开19；现按时间门仅预习18，未授18/未开19。

实际runner回执位于[run.json](20261019-DAY17-linear-polarization-paq-compton-run-01/run.json)，其run-01/session与原deadline覆盖准备prompt的run-17/output_dir示例。`events.jsonl`实际thread.started与CODEX_THREAD_ID相符。用户打断后明确要求farmer/go-on/all/auto继续；后来暂停并恢复goal，仍是同一session，不新建daemon/session或调度。现已从canonical scheduler的16:06 manual-waiter-interrupted及原PID缺失核实原waiter/runner中断；当前研究通过同session用户恢复的nativegoal继续，正常runnerexit code仍未观察。已append-only补同session索引，见[session-index](20261019-DAY17-linear-polarization-paq-compton-run-01/session-index-observed-004.json)，未启动新session/调度器。

### Day 17 card completion audit

| 课程交付 | 本session实际证据/artifact与locator | 状态 |
| --- | --- | --- |
| 来源前主动回忆及priming声明 | [active-recall-before-sources.md](20261019-DAY17-linear-polarization-paq-compton-run-01/active-recall-before-sources.md)与[freeze](20261019-DAY17-linear-polarization-paq-compton-run-01/active-recall-freeze.json)，2026-10-19 16:04:24上海、session/hash；不是盲测 | complete |
| ST99原件主线与关键图/表/式 | [[../../knowledge/sources/starosta-1999-pdco-experimental-test]]末段actualreadscope；printed16–26、Figs1–7、Table1–4、Eq1–7及脚注；ST99-14 | complete |
| SG98原件主线与关键图/表/式 | [[../../knowledge/sources/schmid-1998-gammasphere-polarization]]末段actualreadscope；printed95–110、Figs1–15、Tables1–3、Eq1–19；SG98-13/14 | complete |
| P/A/Q分层与新计数/误差练习 | [[../../knowledge/research-notes/polarimetry-shared-calibration-count-design]]“P/A/Q分层与原件输入”及“声明设计的计数与定量结果”；[newresult](20261019-DAY17-linear-polarization-paq-compton-run-01/paq-shared-calibration-result.json) | complete |
| 反证、必要companion和独立校准输入 | ST99-2/7/13/14；SG98-5/8/9/12/13/14；新note中holdout支路、共同Σ和改分母反例 | complete |
| 本日报、唯一writeback与checks | 当前二十四页canonical已变更；17主线检查/发布001–006已通过，唯一writeback/同sessioncontinuation/receipt与[Day18准备prompt](prompts/20261020-DAY18-dsam-lifetime-strength.md)存在；当前卡验收另记verification015，整日研究仍持续 | complete |

Day17课程交付与逐卡证据已经齐备；表只授17，18为无学分preview。课程卡完成不结束原研究窗口：nativegoal/run持续active，课程状态只在当前验收/实际发布后对账一次，整日收束仍待原deadline。

## Candidate pool and selection

按README/index/profile/memory/activehandoff/PLAN、三份课程计划、continuous-learning/autonomous/reflect规则和最近八次日报的候选部分重建；见[candidate-pool-001.json](20261019-DAY17-linear-polarization-paq-compton-run-01/candidate-pool-001.json)。日报只提供运行历史，不作为新的科学事实源。

| 槽位/候选 | 信息增益、覆盖与当前决定 |
| --- | --- |
| continuity：两原件的P/A/Q、共享a/η与Q依赖 | 当前课程强制主线；实际计数定义和cross-Cov可改变P幅度/误差，先核原件再作新联合设计，已产生canonical增量 |
| 同一问题下一步：detector合并权重 | ST99以18台合并a≈1、SG98以12台合并C/S；reference/target的不同权重是否破坏迁移仍有高信息增益，继续研究 |
| 实际P/δ重拟合 | 原events、producer、matching response、fit/calibrationΣ未得；不以更多toy替输入 |
| SG98 294-keV printingclosure | 旧边界仍在，无新producer/unrounded输入；不调η、不复跑旧JSON计新交付 |
| non-overlapping novelty | 当前未强行占槽；Day16强priming来源不自动算novelty，不以篇数判饱和 |
| Day18 | 当前continuity仍有有价值路线，未打开；如后续按时间门局部饱和才看恰好下一卡，无学分 |

Day8–16近期覆盖含选律/相位、寿命与分支、双带电磁、反应与符合、Doppler、谱学身份、ADO/DCO和大量偏振预习。按课程重读ST99/SG98属于有记录的课程重叠，不声称来源未暴露或实验独立。

## Sources and evidence

### checkpoint038：真实公开25图点的新接口问题

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-24–28/[[root-2026-chi2test-option-contract]] RCT26-14从原XLSX全25点逐行核旧表，新增actualROOT/interface/errorhistory查询。仍同源同数据，不当新独立实验或旧Pearson重跑授分。


### checkpoint037：原AppendixA.2实际背景门

[[fougeres-2022-thesis-evasions-response-contract]] F22-48–53完整A.2/PDF168/printed165及FigA.2视觉核；额外A.3文本输出已如实记录scope，非整个附录读。源给真实三30keV窗，但没有逐bin/Cov。


### checkpoint036：ROOT统计API与inactive示例

[[root-2026-chi2test-option-contract]] RCT26-1–13新联网双版本固定commit/blob；Chi2Test/Chi2TestX主线全读并native原表达式核。publicLL示例L42–141实际inactive，未认证paper调用；[[evasions-2023-public-release-native-readiness]] EV23-16补具体边界。


### checkpoint035：Ch6同数据三方法与失败companion

[[fougeres-2022-thesis-evasions-response-contract]] F22-31–47，完整PDF105–126/printed102–123、17图9表4式文本/视觉核；同data组合、targetshift与BRfitdomain明确，spin未定。原ROOTstatistic/job/Σ缺口继续保。


### checkpoint034：Ch5原事件重建与拒绝门

[[fougeres-2022-thesis-evasions-response-contract]] F22-16–30完整读PDF87–103/printed84–100、15图3表11式，文本与视觉均核。关键是DCT/VAMOS合成角及7333/Si6879相交区域实际拒绝条件；numericmask/job/Σ仍缺，不能由derivedtree认证原fit。


### checkpoint033：作者thesisChapter4新primary

[[fougeres-2022-thesis-evasions-response-contract]] F22-1–15，HAL201页只完整读Ch4/PDF74–86、图4.1–4.8/Table4.1/Eq4.1–4.3及front/TOC；HAL再生日期不当新实验。


### checkpoint032：官方exact23AlEC新对象

[[nndc-2021-mg23-lifetime-strength-reference]] M23-17–26：23012026,23MG/202101共299行全文新读/hash核。官方本身对absoluteI451推导/γidentification保caution，NR空/纲图不完整，不当primarybody/新实验。


### checkpoint031：gamma源链三份机构原报告

[[tamu-2006-2007-al23-gamma-reference-reports]] TA07-1–12，实际selectedI5–10与I27–28共8页完整主线/图refs视觉核；205页年报其它未读，PRC/thesisbody未取。source发现与TLS失败/readiness留档，不从metadata补science。


### checkpoint030：Friedman2020完整上游primary

[[friedman-2020-gadget-al23-proton-branch]] FR20-1–16，OSTI封面+作者稿8页/4图/2表实际全读和视觉核；arxivv2正文归一文本仅首页日期不同，非VoR/独立采集。newgasratio与旧absolute/gammafeed分列。


### checkpoint029：真实publicrelease主要路径/native

[[evasions-2023-public-release-native-readiness]] EV23-1–14主要source/headers/Backupextraction/doc/activeSRIMheader实际核。原34文件hash保，nativecopy只加lib输出目录/另名client；现有ROOT6.40，不冒paperexactjob。


### checkpoint028：新GANIL原件/实际公开数据

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-1–20，publisher7页/SI8页全主线/式图表实际读，Figshare375909byteZIP/两XLSX与Zenodo34文件逐hash/CRC/Gitblob核。actualTreeMaster409303entries，仅schema未读event值，不宣称原DAQ/fullfitCov。


### checkpoint027：真实ROOT5.22代码输入

[[root-2008-v522-background-error-contract]] R522-1–11：v5-22-00 tag→a365d2fa4cdc4fea91420c400280dc9fc7c64214，公开tree/blob/hash核；TH1/TSpectrum/TArrayD相关方法实际读。原thesis只指5.22，不认证exactpatch/job。


### checkpoint026：实际作者thesis与原期刊边界

[[saastamoinen-2011-thesis-al23-proton-response]] SA11-1–14，实际JYX112页作者primary，只定向4.2/5.3/AppendixA与refs，不称全文或期刊reprint。PRC83045808body当前未得；原计数/analysis/Σ未得。


### checkpoint025：2010Letter实际原读与正式erratum边界

[[sallaska-2010-na22-letter-version-contract]] S10-1–10，v2四页完整主线/一式一表两图；v1定向source/text/table/figure比较非独立盲读。正式erratum DOI已核，body当前未得，不从关联metadata/标题补科学。


### checkpoint024：Sallaska2011实际20页主线

[[sallaska-2011-na22-absolute-resonance-strength]] S11-1–20，实际arxiv1009.3925v2二十页/18图/6表/7式全读及视觉核；sourcehash/date-today/版本分开。2010报告/erratum只识别引用，body未得，不能算新采集。


### checkpoint023：23Mg官方五对象与2013获取边界

新canonical [[nndc-2021-mg23-lifetime-strength-reference]]，M23-1–15；四reaction557行全部、Adopted630行仅L1–48/330–465实际读。原2013body仍未得，完整readiness已落盘；不把评价转述冒作primary。原15点窗口继续，17学分只一次、18仅partial。


| 来源与identity | 本session实际覆盖/locator | 证据分层与独立性 |
| --- | --- | --- |
| [[../../knowledge/sources/starosta-1999-pdco-experimental-test]]；DOI10.1016/S0168-9002(98)01220-0 | 原11页printed16–26主线与全部图像；printed17 Eq1/2、footnote1，printed18 Eq3/4，printed19 Eq5/6/Table1，printed21 integrated，printed23–25三表，printed26 ακ | 原164Yb采集与NORDBALL单clovercalibration分开；reference P来自上游AD/GOSIA，四组P/integrated/RDCO不是独立实验；旧10⁻5/脚注纠正不作新发现 |
| [[../../knowledge/sources/schmid-1998-gammasphere-polarization]]；DOI10.1016/S0168-9002(98)00624-X | 原16页printed95–110主线与全部图像；Eq13–18、Fig8 zero、Fig9/10 threshold、Fig12 level scheme、Table3与Fig13–15 | 三reference的A/P/Q同链派生；197Pb是另一应用数据；44页alternate本session未打开，原same-study版本不计独立实验 |
| 两DOI的Crossref exact请求 | 本次实际HTTP200，分别11/12作者、1999/1998、423/417和16–26/95–110；[progress-001](20261019-DAY17-linear-polarization-paq-compton-run-01/progress-001.json) | 仅校身份，非物理正文/独立实验 |

两原件实际SHA-256分别为`883fdd7b08831efefe25f5df610e84b95bb1acbcd7b8e7f684b1a1b31bf8030b`、`66502edb2f0ff2d09321d3b388767ea98736b83865b90f128fdd1e46921b2a2c`，与source元数据一致。raw只读；启动boundary/preflight均exit0，受保护Bib基线matched。

本轮新增ST99-14/15是共享校准/合并响应合同；SG98-13/14/15是改分母、效率字典与合并权重边界。公开GRS26-1–10另按软件对象分层。新claims全needs_review，原25条ST99/SG98 claim行和flags逐字核相同，未设human-reviewed。

### 实际公开producer的证据推进

[[../../knowledge/sources/grsisort-2026-compton-polarimetry-code]] GRS26-1–10：固定GRSISort commit6bd3c617cf212158da80918594ba9623fb4137c2、targeted GRSIData54dfb1d244593a48820142ee20232a12cc959d50；七份primary selected文件完整读，API/build targeted读，Gitblob/SHA256核验。原样选定函数body在声明hit/settings/sink和真实ROOT6.40.04中编译0/run0，未做完整build或实验重放。

实际组件观察：newAnalyze不消费secondF（两次均P=.04439854；声明pureE2 oracle=.16662554）；normalizedratio的null点报σ0而明确独立bin设计localσ=.134164；ROOT相邻inclusive分组重叠边界bin；同historymultiset改变跨eventhit index时mixed0/0/1而prompt1/1/1。GRSIData的AddHit/GetHit/FixCrossTalk targeted路径没有自动能量排序来解除该局部条件，但真实DAQ/eventpack影响未恢复。默认CMake含Lean而不含newAnalyze、Lean的secondF消费正确，是必须保留的反证；不将这些局部代码结果判成原实验或整个GRSISort失效。

[pinned manifest](20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-pinned-download.json)、[component input](20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-component-input.json)、[actual result](20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-component-result.json)、[script](../../system/scripts/day17_grsisort_component_audit.py)保存边界。当前tree没有ROOT文件且未得实际配套data/Σ，不宣称全部合法数据入口穷尽；source raw归档槽deferred，原件真实缓存repo tmp/固定URL可重取。

### 新anchor完整主线已核：实际GRIFFIN校准

[[../../knowledge/sources/garnsworthy-2019-griffin-facility]] GF19-1–14：本session来源前回忆另冻后，完整读36页arxiv1809.07183v2、Figs1–28/Tables1–8/Eq1–12，所有页面视觉核，PDF18/22/23/24另核Table7/关键式/校准曲线。DOI10.1016/j.nima.2018.11.115、104作者/NIMA918/9–29/2019由Crossref精确title核；actualbody仍是2018v2而非声称已读VoR。原hash b257eb66cf822ef9c8e476125ac8d00979df340b5567baa62f72ca4ff4ef16ed；raw归档deferred、无Bib唯一key，原件repo tmp可复取。

实际calibration采用.5QPcos2ξ、1332-keV nominalP90=1/6与Q=.240(.012)，16clover；其它570/1173/1771点为.390(.024)/.258(.012)/.201(.045)。cloverpair90°与crystalΘ68–113°、Θ/ϑ/ξ、Fig18同data分组、Fig20的1064scatter/570gate与反向角色分开。当前2026code不认证当年producer，paper Q也不裸迁其它角组/array（GF19-6–12）。[[../../knowledge/experiments/triumf-griffin-compton-source-calibration]]保存实际输入账本。

作者关于减少clover数不改变Q属于其校准条件，不把它与本run自由weights模型误称实测冲突。Fig19绿色band/其它Q点、207Bi两支与同known-P参考均有共享依赖；未得rawevents/实际fitΣ，experimentalL4仍not-ready。既有source25claim/review边界不因新primary清除。

## Theory/analysis exercise

### checkpoint038：实际图点的统计与配套variance

[程序](../../system/scripts/day17_fougeres2023_graph_root_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-graph-root-result.json)：fallbackautoUU41.654553、zero-template UW110.195944；α1.095013423同域归一后fixeddeviance95.748411。原variance=M再actualScale使α²variance/forcedUW47.939784一致；不声称该variance是原MCstats。全点/无windowsearch，原SI17.1982未复现、不选近数值冒原fit。


### checkpoint037：真实三窗的精确符号合同

[程序](../../system/scripts/day17_fougeres2022_a2_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-a2-exercise-result.json)仅标准库Fraction：D=S−(L+U)/2的完整Cov与Poisson特例分开，constant/linear背景消、quadratic残余−b2h³。真实h30keV不提供actualb2/CI或信号side泄漏。初无sympy失败exit1已保，未装包/改原source。


### checkpoint036：实际接口/原表达式native

[程序](../../system/scripts/day17_root_chi2_ll_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/root-chi2-ll-exercise-result.json)：LL=无LL；同designcounts错误buffer改变autoUU6.199134→UW8.783184，原manual6.410432少o0项6，positiveo/s0应∞但原finite；highendpoint排bin不同。明确声明design组件、低counts警告及inactivecaller，不外推实验τ/CI。


### checkpoint035：实际τ/Γ表与条件Cov

[程序](../../system/scripts/day17_fougeres2022_ch6_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch6-exercise-result.json)核Table6.4/6.7/6.9、hbar/tau及Eq6.2：声明对称化算9.9455fs；固定weights在ρ>.4623125时σ大于min政策，非实验CI修订。DCLM打印9.5fs/60meV中心不闭合保原，final9.9/66量级闭合；BR.68(.06)与F23.68(.17)版本分开。


### checkpoint034：实际22门、loss印刷式与Doppler交叉

[程序](../../system/scripts/day17_fougeres2022_ch5_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-result.json)对真实Table5.1与Eqs5.5/5.8/5.11核验。keyalpha门与另六行相交，非污染份额；Eq5.8映射随厚度改变，非ExCI；厚靶loss字面与图不闭合不猜修。单β.077交叉θDS144.6878°只解释污染重叠，非labtheta拒绝门。


### checkpoint033：实际geometry与输入量级

[程序](../../system/scripts/day17_fougeres2022_ch4_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-result.json)核19mm=19000µm、原SRIM表正确逗号/energyunitlookup.63074MeV对thesis.662保残差，.28‰×6750=1.89keV。固定β/propermean路径控制仅解释量级，不冒实验τ/CI。


### checkpoint032：字段与两种lab角色

[程序](../../system/scripts/day17_mg23_al23ec_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-al23ec-exercise-result.json)核NRblank、ΣEC_TI87.7483(缺额不填branch)、母态TI/γroles；βp emittedlab→totalCM乘r而capturebeam→CM除r，源两行中心近闭。共同I451scale条件相消不补relativeinventory/原Σ。


### checkpoint031：r/Bp/时间label实际算术

[程序](../../system/scripts/day17_tamu_report_ratio_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/tamu2006-2007-report-exercise-result.json)核r=.080→Bp.074074；mean10/J7/2给omega2.5797近报2.6，literalhalf10给1.7881，保label边界不修原文。三γ比normalize近S11旧3.1/80.8/16.2，却不补absolute3.95或新CI。


### checkpoint030：新ratio/旧reference的量化角色

[程序](../../system/scripts/day17_friedman2020_branch_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-exercise-result.json)核perβp.02583对报.0257、报p/g给daughter.006464；新branch/旧τ/J中心omega.24289，τ12endpoint不当原>.16 jointCL。两ratio共sys/rho敏感性仅条件，不重报CI；旧gamma打印inventory对新through-state3.95不强配。


### checkpoint029：原函数native与实际eventquery

[复算脚本](../../system/scripts/day17_evasions_release_native_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-exercise-result.json)freshcopy复现make2→补lib后0、原noanalysisreturn1，loaderstatus1但callerN保持sentinel/逗号首E999/Se0、VAMOSbeta不回传。真实data409303/maxtrack7/7933Si_dE>0核。没有运行未初始化fullMC、修source或新τ/BR/CI。


### checkpoint028：新branch和真实图数据交叉核

[程序](../../system/scripts/day17_fougeres2023_source_data_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-exercise-result.json)核新τ11/BR.0068中心omega.23093、推荐10.2/.0066给.24177；假J不作测定。Table1名义quadrature26.525对原26保边界。actualFig2right全区Pearson不等SIgridmin，SIfigure1b有31点零切片；不拿显示数据强造原fit/CI。


### checkpoint027：原方法组件与匹配Jacobian

[复算程序](../../system/scripts/day17_root522_background_contract.py)/[实际结果](20261019-DAY17-linear-polarization-paq-compton-run-01/root522-exercise-result.json)用原Smooth/Background表达式另名组件+当前ROOT6.40helpers。声明21bin：storedSmootherror不改，Background非零content/零stored errors，无bufferfallbacksqrtcontent。另四bin estimated a=Dk/Bk的matchingvariance0，固定aAdd式75.7778；非原hist/原CI。


### checkpoint026：perβ与daughterbranch分开

[程序](../../system/scripts/day17_saastamoinen2011_thesis_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/saastamoinen2011-thesis-exercise-result.json)核真实Table5.4和Fig5.7：perβp.13856%不同于daughterBp.0377358；固定旧τ/J给Γp2.484/Γγ63.337/omega1.366meV，非新测量/CI。十二行共同I451-only Cov给总贡献.0281个百分点，非fullfitCov。J3/2仍允许L2，仅此不裁决spin。


### checkpoint025：Lab/CM波长条件桥

[程序](../../system/scripts/day17_sallaska2010_frame_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2010-frame-exercise-result.json)锁两版source/TableI/Eq1/rateEPS。NRλCM²=r²λLab²，CM窄峰积分加lab能量Jacobian给λLab²r³，原Letter写λLab²r；质量数r²≈1.092975。正式勘误/原producer未得，不给9.3%实验重标或称历史冲突解释。


### checkpoint024：实际partial误差预算

[程序](../../system/scripts/day17_sallaska2011_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-exercise-result.json)按TableIII finitepartials、TableI系统和允许upperlinear加法，近复213/288/610打印总误差；454为20.903对原22未闭合。213尾10%total给total/observed1.111而非1.10。NT与capture共用eff时条件比η1275/ηH、共同scale消去，非实际Cov/CI已恢复。


### checkpoint023：固定输入的两通道约束

[新程序](../../system/scripts/day17_mg23_reference_contract.py)/[实际结果](20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-reference-exercise-result.json)核五hash与九upper/两finite转换、branch归一Jacobian及omega=g(hbar/τ)Bp(1−Bp)。固定τ10fs/omega5.7meV：J3/2无实根，J5/2与7/2各两根；tau允许上界8.248/12.372/16.497fs。没有新spin排除/Bp测量或jointCI。


完整公式、假设与数据在[[../../knowledge/research-notes/polarimetry-shared-calibration-count-design]]；可运行[day17_paq_shared_calibration.py](../../system/scripts/day17_paq_shared_calibration.py)，输入[paq-design-input.json](20261019-DAY17-linear-polarization-paq-compton-run-01/paq-design-input.json)，结果[newresult](20261019-DAY17-linear-polarization-paq-compton-run-01/paq-shared-calibration-result.json)。这是新声明的设计计数，不是ST99/SG98实测数据。

clover用A=(aN⊥−N∥)/(aN⊥+N∥)；SG98用A=(ηC−S)/(√η(C+S))且C含sideADCzero。各推自己的Jacobian，联合primitive六counts和独立P_ref传播P_t=P_ref A_t/A_ref，保留Cov(A_t,Q)。另一路条件binomial Fisher和各120000次Poisson设计MC验证同一统计模型，不计独立实验。

| 新设计 | U；reference；target（各两类别均值） | A_t；Q；P_t±localσ | 若错当A_t/Q独立的σ |
| --- | --- | --- | --- |
| clover | 500000/500000；55000/45000、P_ref=.5±.01；53000/47000 | .06；.2；.300±.0194486 | .0201951 |
| SG98 | 1000000/160000；101600/14400、P_ref=.8±.012；100600/15400 | .015；.05；.300±.0627474 | .0646613 |

共同η不自动完全消去；比值中只取消√η，剩余敏感性为C_t/(ηC_t−S_t)−C_r/(ηC_r−S_r)的局部log导数。若改成B=(ηC−S)/(ηC+S)，则B=(1+η)QP/[2√η+(η−1)QP]，一般非线性；此设计沿旧Q得到P=.441961，即使以同一参考重标一点也仅.291999而非真值.300000。符号、数值和适用条件都在canonical，未修改source实验结果。

脚本首次用两个interpreter均缺SymPy（actualexit1），保留[first-execution-failure.json](20261019-DAY17-linear-polarization-paq-compton-run-01/first-execution-failure.json)；随后用已有repo内依赖缓存的per-command PYTHONPATH执行exit0。未安装全局包、未改系统配置；新代码/input/hash、依赖版本与首次成功/补充代数核验结果均保留，不称首次即成功。freeze的时间说明如实区分来源前回忆与执行后查看结果前封存的inputhash。

### 合并权重的新精确结果

[分析前freeze](20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-freeze.json)、[Rational输入](20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-input.json)、[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-result.json)和[脚本](../../system/scripts/day17_paq_array_weight_contract.py)来自本session下一有界问题，非旧MC重跑。

在共同物理P与明确perpendicular基线权重下，clover合并A=kP/(1+λP)，λ=−Cov_w(a,Q)/(2〈a〉)；所以matched null不自动给单一线性Q。原a范围加声明0≤Q_j≤1、匹配weights时，单参考非线性P绝对偏差的保守界为10/391≈.0255754；不匹配weights的无偏振A条件域为[−1/34,3/98]。在这些额外前提下，仅权重变化不能从P=0产生原centralA=.120，但不构成实验误差预算或δ分支裁决（ST99-15）。

SG98在各台totalphotopeak对P不变、匹配weights时仍严格线性；合并η=(1−c0)/c0，c0=Σv/(1+η_j)，不是η算术均值。不同targetweights可同时产生offset和新斜率，单Q不能消offset。新design targetP=.3在错误迁移时可得到apparentP≈2.24579，逐台正确forward model回到.3；这揭示合同失效，不clip、不冒称原197Pb偏差（SG98-15）。本代数局部已闭合，下一转实际producer/逐台ledger readiness，不再堆同toy。

### 原样完整Q(E)程序与极限核验

GRS26-11/12的[完整程序结果](20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-q-energy-result.json)与[脚本](../../system/scripts/day17_grsisort_q_energy_audit.py)记录compile/run均0。原plot在fixed1332/Q=.2509下以(E,1332)调用ScaleQ，100/3000keV输出.111820/.445044；按函数自身calibration→target字典正向(1332,E)为.562967/.141449。旧Lean正向调用保留为反证，不将plot问题扩为历史实验Q错误。

原程序uniformθ KN-sensitivity平均与另一个明确声明的KN×dΩ模型不同；低能解析极限分别√2−1与1/2，point90为1。独立积分核通过，但都缺真实geometry/threshold/多散射/Σ；不能拿某个半因子裸换经验Q或把理想平均当detector response。

### 默认Lean完整source的输入格式正负控制

GRS26-13的[输入前合同](20261019-DAY17-linear-polarization-paq-compton-run-01/lean-schema-before.md)、[实际结果](20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-lean-schema-result.json)、[程序](../../system/scripts/day17_grsisort_lean_schema_audit.py)记录完整旧Lean source仅附batch entry运行。相同设计TH2D均值、不同keys：newhelper格式actualexit139、四目标graphs缺失；legacy格式actualexit0并输出171/19/10/101点。原fit amplitude约.199523/.199614只说明声明cos2均值fixture的程序行为，不是实验P/Q/CI。输出文件存在或检查器exit0均不代消费成功，原失败未抹去。

### 原primary摘要与当前kernel的受限核算

[冻结输入](20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-primary-calibration-input.json)、[程序](../../system/scripts/day17_griffin_primary_calibration_replay.py)、[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-primary-calibration-result.json)保存published四Q和actualcurrentScaleQ执行，不能称原Fig19 producer重放。源.240锚点给570/1173/1771条件预测.378202/.259795/.198649，差+.011798/−.001795/+.002351；只传播anchorσ的curve Cov=.012² ssᵀ，不用缺失measurementCov造新χ²/CI。

源nominalA0=.5×.240×1/6=.020，σ=.001仅Q项。Table7的A245ε122/[16(1+α121)]打印中央值给10204.872，独立area/eff-only localσ121.016；明确末位rounding盒10183.221–10226.535包含源10201。省ICC则21991.5。这里给实际photon/total分母反证，不恢复完整原Σ或制造新计数实验。

### 实际坐标表与native position的受限核验

[原表输入](20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-geometry-table-input.json)、[原样ROOT geometry脚本](../../system/scripts/day17_griffin_geometry_contract.py)与[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-geometry-result.json)固定身份不拟合：GetPosition含45mm代表interactiondepth；Table2两距离128位置/256方向与native均在.05°打印盒内，最大差.04192°，另名front-control可差7.7406°。这不是测量actualdepth/实验response。

Table8仍**partial**：源113.4/152.3/160.2(重数64/64/128)与当前native113.5/153.3/161.2未全匹配；首次全表match假设失败和原输入保留。独立原Table2打印中心最近后两角差约.958/.943°，在两表同几何点前提下超.25°保守rounding外界。不同基点/历史producer/未舍入版本未解，不能称实验矛盾或sourceerratum。另定向v1原33页的identity/Table2/Table8及两页图像，相关印刷条目与v2相同；未整读v1或计独立实证。Publisher默认TDM200仅metadata、FULL401，VoR body未得（GF19-18）。Ref38 Smith原PDF3/Table1/caption及PDF4定向核也含相同三行/脚注，仅确认共享角表谱系、不计独立证据（SG19-18），旧17claim/flags保持。clover90°的点几何110/145mm crystalΘ域约67.456–112.544/71.431–108.569°，不认证原paper literalcut/Q（GF19-15–17、GRS26-14）。

### 207Pb官方reference的实际输入与派生概率

[[../../knowledge/sources/nndc-2011-pb207-bi207-polarization-reference]] N207-1–13：本session来源前回忆另冻，官方201102 Adopted/207Bi EC两text实际hash/字段核；完整EC154行及Adopted相关lowlevels/近能母态/comments定向读，未称整1488行/147页评价fullread。1064MR显式+.02(.01)、570MR空，Adopted理论CC与EC实测汇总分开。原P/N/E格式三页视觉核（TU01-5/6/7），NR/BR/NB=1使EC RI成为per100parent photon，source EC字段还含.0380(.0022)%β+，不把“无β”简写当严格零或据此宣告实际偏差。N207-13同时给反向限制：β+直接到1633level的预算约−257.856keV、到569level约805.803keV，whole-source小branch不等于选中1064/570cascade污染；upper.806s不等已发两γ的间隔。

[真实冻结输入](20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-reference-audit-input.json)、[程序](../../system/scripts/day17_pb207_reference_audit.py)、[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-reference-audit-result.json)显示源RI570=(100−.131)/(1+α)派生关系：声明独立bypass/α时，RI≈97.74787、σ≈.02877，totalσ保留Cov为.002、错当RI/α独立为.04152；均是条件诊断，非原Σ/CI恢复。selectedcascade双光子发射名义概率≈.72918，非marginalsingles乘积.72824或detectorε。MR的upperfraction≈.00039984、interferencecoefficient≈.039984，不是实际P误差界。

NSR正确endpoint核1976Av01为Avignone/Girard PRC13,2067–2070、DOI10.1103/PhysRevC.13.2067；APSlanding403/官方harvest401，primarybody未得，无phase/fitΣ推测。初NNDC/NSR请求home/404均识别并留档，不以HTTP200或downloaderwrapper0声称得到正文。当前仍Day17continuity，Day18仅看card、未预习/授分。

## Counter-evidence and missing companion observables

### checkpoint032：官方caution也须按层使用

M23-18/19/20/21/22/25/26：RI100不等absolute100%，43.3%来源程序不清/两条1.53comment不闭合保原样；TI4.89不是FR20throughγ3.95。共有乘法scale可能在比值消，不据caution全盘否定/认证branch。原3.95表/fullCov仍未取得。


### checkpoint031：后续run不是一律同event

TA07-2/3/4/11/12：2005与2006Sep/Nov数据/计数期/BGO及高能标定分开；新run仍共享设施/校准知识。三报告相对比不等absoluteγfeed，精确3.95/原Σ未闭，原PRCbody与thesis未得不冒已读。


### checkpoint030：低背景也有模型，推荐也会共享输入

FR20-3/4/5/6/7/10/14：gas减少β背景仍有exponential/linear选择、wall/beam/eff校正和583/595doublet。newratio仍用旧I866abs/γfeed；F23推荐再复用，不把两篇.24当独立强度确认。原counts/producer/fitCov及gamma原件仍缺。


### checkpoint028：新measurement与推荐组合分开

F23-4/7/8/9/10/15/16：assume7/2、邻态/背景/ℓ0模拟和γ高能eff仍需合同；χ²ndf低非自动coverage证明。newbranch.68%对旧约3.7%更新关键，原Friedman2020/全producer参数/fitwindow/normalization/Σ待核。publishedrelease widthfit分支为空/旧fit注释，不能codeavailable就称论文CI已复现。


### checkpoint027：不是所有API都会传播分析误差

R522-2/3/4/5/11实际反证“每步自动传播”保证；原16%/2%/13%仍按作者报告。原patch/script/返回对象使用/数据与fullCov缺，不据zero-buffer组件宣称实际fit误差错或重报Bp/τCI。


### checkpoint026：背景与自旋解释仍是输入

SA11-8/9/10/11/12：30keVFWHM不能排16keV近IAS小贡献；作者7/2偏好还含势垒/IMME动力学，gamma/τ来自不同旧源。ROOT5.22平滑/scale/Add误差传播主张待真实code核；不把净计数Poisson或Sumw2buffer当完整Σ。


### checkpoint024：完整积分与停止输入范围

S11-2/8/9/11/12/13/14：有限强度完整积分减少absolute-stopping依赖；弱模板/能量损失/有限尾仍需响应。in-situ活动度不能独自跟踪被照靶NT；5732的213/209placement不同，610partial含旧branch。Fig12caption门角色与图13/TableIII相反、TableV upper/lower分位文字与数值不闭合保留；不修raw或宣称实验矛盾。原点数据/全Cov/producer仍缺。


### checkpoint023：Adopted没有消除自旋和弱支问题

M23-4/8/9/10：Adopted3/2+,5/2+与fusion7/2(+)并列，capture有另一γ和新omega；7852/5138缺失只为评价者转述的未确认沟通。M23-12散射对象不覆盖7785，不能补Γp。靶厚160vs40、原2011/2013body与原jointΣ仍缺。


- ST99-2：490-keV的P/RDCO仍保留E2与ΔI0 M1/E2；正号不保证唯一δ/Jπ。ST99-12的ακ是作者理论预测而非已测ICC，不能拿它闭合分支。
- SG98-5/8：zerochannel是另一侧confined，Fig9 130keV与Fig10/Pb 60keV不能混用。源Table3误差来自DAMM拟峰，不能覆盖为√面积。
- SG98-9/12：432线正A和带内负A是直接观测层；E1/M1/negativeparity是作者附条件解释，shears为结构解释。高背景散布/AD companion限制精确P提取；约36%只属于原条件，不是通用P界。
- SG98-10：294打印中央值未闭合仍保留；actualη在quoted误差内，不是实验矛盾，不调η强配。
- 必要独立校准输入：未参与Q拟合、已知P且energy/threshold/gate/arrayweights可核验的holdout支路；另需U/r/t真实峰与background/event-overlap Σ。用同reference回代自己不是独立验证。
- SG98-14：Eq13称N为source发射数，而Eq18称Ni为incident；要有接受角/曝光归一字典。photopeak/coincidence、本征/绝对/relativeNaI/条件效率不能混为同一ε；高背景下裸F不是可靠仪器排名。

## Knowledge Impact and Learning Decision

`supports`直接从原始计数表达P/A/Q、共同校准和可复算Σ；`revises`“改分母再标一条线即可继续用线性Q”的预期；`limits`从同参考回代、偏振号或裸F取得独立验证。没有新增实验P/Q/δ/Jπ/模式，也没有解释原294印刷差或490剩余分支。

本session的数学交叉核验为同一design的内部证据；两原件不同采集可以比较合同，但不能组合成一个新的实际计数实验。任何真实反演仍需matchingresponse/完整Σ。

### 207Pb双门角色的新条件核

新canonical [[../../knowledge/research-notes/pb207-gated-polarization-reference]]以实际N207-2/3输入作本session独立练习；非重跑旧Co60结果。[新合同](20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-stokes-contract.json)/[新程序](../../system/scripts/day17_pb207_conditional_stokes.py)/[实际结果](20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-stokes-result.json)给pureM4/E2的P1064(90°)=−24/101与P570(90°)=183/505，共享W=1+(221/1001)P2−(18/1001)P4；角色互换不只换能量。native±.02的pointP分别约−.25015/−.22522与.37420/.35012，小E5强度并不保证同阶P精度。原primaryphase未知，未将评价正号指定native或重标paperQ。

直接光子迹与独立exactCG/阶乘d最大差8.88×10⁻16，独立F/F3三rank符号残差0；PSD/nativeRB/EMduality及directfullsphere4controls通过。68–113°均匀cos接受仅是声明设计，pure平均−.21603/.34124不是实际GRIFFINP；unobservedgate共同轴Stokes0与eventplane标量平均分开。N207-14/15为新derivedmodel claims，非官方测量。

Hutter2002只metadata/来源前回忆，未得body；publisher无candidate、downloadercredentials_missing、OpenAlex/Semantic无OA、机构验证页/403、Scholar/Googletimeout及Bingofftopic留[boundary](20261019-DAY17-linear-polarization-paq-compton-run-01/hutter2002-body-boundary.json)。不算阅读credit，不绕过访问限制或从题名补高能结果。

### 恰好Day18无学分知识预习：lifetime-strength-audit

[候选池/时间门007](20261019-DAY17-linear-polarization-paq-compton-run-01/candidate-pool-007.json)在上海19:56、距原deadline约1144min确认当前PAQ理论局部闭合且primary/events/response/Σ仍输入受限；检查下一卡后选择恰好18，无19。先冻结承认旧DSAM/Day9/13priming的[回忆](20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-before-sources.md)/[sessionhash](20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-recall-freeze.json)，再开source/raw；不是盲测。

[[../../knowledge/sources/jensen-2001-165tm-h9-2-configuration]]原48页PDF/hash核匹配，本session只定向读DSAM PDF21–25/printed23–27与必要实验、matchingTable1/2/6/mixing/结论context，不冒称新48页全文；J01-6–10保存belowgates、三步/5fs、stopping5%原句和同标尺依赖。[[../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates]]本session六页全文主线/五图/两表/三式与关键视觉核，MU08-15–17区分fulltailgate、five-step/2fs/globalfit与candidategeometry。旧claim/reviewflags保持，原raw未改。[实际scope](20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-reading-scope.json)/[identity](20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-original-identity.json)/Crossref保存对象与日期层。

新[[../../knowledge/research-notes/lifetime-strength-audit-165tm-136nd]]和[输入](20261019-DAY17-linear-polarization-paq-compton-run-01/day18-lifetime-strength-contract.json)/[程序](../../system/scripts/day17_day18_lifetime_strength_audit.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/day18-lifetime-strength-result.json)对Jensen十一行作声明pγ1/ICC0/fixedK1/2的τ→B→Qt，最大central差1.772%、额外nearestdecimalbox全部有交集；不反解ICC/branch或称原表错。MU08九组B/Qt与候选G=CG(I I2−2|I−2 I−2)²=(2I−3)/(2I+1)的额外打印box相容；fixedK0给约1.58倍不同Qt，**数值匹配不等于作者实际公式已认证**。LKH82仅PDF3/printed121 Eq2.2/2.3原图复核，现代常数不称原文直接数字。

反证：fulltailbelowgate仅免去截快tail的一类selectionbias，不消sidefeeding；5%与最高15%预算不同、未给Σ不拼独立Gaussian；B/Qt/其它band标尺同链派生不计独立测量。实际lineshape/events/response/feeding/Σ仍缺，没有新L4τ/B/Qt或实验CI。今日formal17不变，partial18仅知识预习，课程next17/count16暂保持，最终也只允许17信用。

### Sun2023原primary：仍为恰好Day18知识preview

[[../../knowledge/sources/sun-2023-bayesian-dsam-31s]]实际原读arxiv2203.10336v2/9Nov2022十页、五图一表三式及reference；关键图/公式/表视觉核，[scope](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-reading-scope.json)明确不是已得2023VoR/SI。官方src仅maintex/六EPS，publisherFULL401/discovery无candidate，未补actualcounts/训练网格/GPstate/后验样本；原版本/共享数据依赖分开。来源前primed回忆先冻，全文不是从review赞许替代。

SUN23-6–10：positiveτprior、Eγ/bkg/sp的restrictiveGaussian与A2uniform/A4zero、Gaussianbinlikelihood和PCA/GP/MCMC是实际分析合同；作者明确nuisancepriors强烈影响posterior。Eq3只印quadraticexp，若Σ随参数变完整Gaussian还需normalizer；actualtailoredcode未得，不称作者代码错。公开MADAI固定2015commit仅上游待核对象，首两个Model/GPModel文件与README已原读、原样component执行尚待，不能冒称paperproducer。

SUN23-10/11：有限值来自16/50/84quantile，四上限来自90thquantile；6390的4156线低统计、作者说无finiteconstraint，20fs/Γ>33meV/strengthlowerlimit是条件影响链，非第五项正式90%bound。下一actualSI/likelihood/prior尾部输入才有信息，不能把chainstep数当独立认证。

[新rate合同](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-rate-contract.json)/[程序](../../system/scripts/day17_sun2023_rate_boundary.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-rate-result.json)用真实reportedτ1.120(.180)ps与**USDB模型**E2partial6.9ps：τM1≈1.337024ps，固定model的local尺度.256516ps，现代单位/rounded1248给B(M1)≈.021883µN²、RME≈.295858µN。模型E2centralrate占约16.232%，不因dominantM1就删除；这不是新测δ、原posterior或completeCI。20fs仅条件单位核≈32.9106meV，未认证6390统计上限。可复用链已补[[../../knowledge/research-notes/lifetime-strength-audit-165tm-136nd]]与DSAM方法；原reviewWC23flags保持。

正式17已在007实际发布后仅一次对账为next18/count17；见[creditreceipt](20261019-DAY17-linear-polarization-paq-compton-run-01/card-credit-007.json)。**run/nativegoal仍active至原研究截止**，此段只18无学分方法preview，不启动formal18/不打开19。

### MADAI公开核：原样组件与两API反证

[[../../knowledge/sources/madai-2015-distribution-sampling-likelihood]]固定2015commit9f9ee0da、所选tree/Gitblob/SHA256和actualreadscope，fullprojectCMake先因缺Boost头/iostreams exit1，未改系统；随后以实际Eigen3.3.7编译**原样四个source文件**与声明fixture，编译/运行actualexit0。不是fullGP/MCMC或paperproducer复现。[合同](20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-contract.json)/[原fixture](20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-fixture.cpp)/[新程序](../../system/scripts/day17_madai_likelihood_component.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/madai-likelihood-result.json)保存初只ordinary组件版本与后来两API补核，不覆盖首次记录。

MDA15-2–4：同residual1、totalvariance1→4，原quadratic的logratio+.375(比1.45499)，完整Gaussian的variableΣnormalizer后−.318147(比.727496)，排序反转；fixedΣ只改mean时normalizer是常数，不影响relativefit，是必要反证。MDA15-5/6的实际flag/consumer查证：base/defaultappcovflagfalse可由settings打开；ordinary的自给log_likelihood分支**不在另一API中**，公开MH下一步调用另一API。nativecustomfixture返回−.818147/−.0836706，不能仅凭ordinaryescape就认证完整MCMC。

原样uniformprior正控制和刻意negativeCov失败域控制分列，behaviourchecks通过只验证观测行为，非Gaussian统计合同/原实验“全通过”。[[../../knowledge/sources/sun-2023-bayesian-dsam-31s]] SUN23-16明确actualtailoredpapercommit/config/Σ/data仍缺，不从2015publickernel归因其CI错误。此段仍恰好无学分18方法preview，不给新学分或打开19。

### 新publisherSI输入：同一Sun方法companion

新的公开CDN精确PII入口HTTP200取得五页SI（非此前arxivmaintex，非已得2023VoRmainbody），[hash/identity](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-si-cdn-attempt.json)、[primed全读前冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-before-full-si-freeze.json)、[完整五页十三图/全部视觉scope](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-si-reading-scope.json)均保存。SUN23-17–22已canonical；原008“SI未得”保留为当时状态，不把source后续获得说成原URL成功。

SI补35keV implanted3He/25µmAu/6×10^17cm−2、实际GRIFFIN单clover/GRSISortunpacking角色和六个αgatecenters；同hardware名称仍不补ComptonQ或Bayesiantailoredproducer。Fig13可直接看6390posterior，但未给90th数值/训练support/config或draws，不升级20fs为90%limit、不把图轴认hardcut。Fig9/12明确1/2+3076/5156仍列A2，是下一物理对象/帧/phenomenologicalresponse的高信息问题，当前不判fit错。主文/SI/同data/posterior图均不重复计实验或授18信用。

### 新SI spin-half对象的必要物理域与反例

[[../../knowledge/research-notes/spinhalf-angular-nuisance-response-contract]]承认旧CG/Jones/本次全文priming后先冻[新问题](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-spinhalf-before-analysis.md)/[hash](20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-spinhalf-freeze.json)；YA67原PDF1 Eq1/2与视觉定向核，不冒称重新23页。根据SI Fig9/12的Ji1/2前提作[新合同](20261019-DAY17-linear-polarization-paq-compton-run-01/spinhalf-angular-contract.json)/[新程序](../../system/scripts/day17_sun2023_spinhalf_angular_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/spinhalf-angular-result.json)，不是只复用旧检查数。

isolatedparityconservingEM、末态全求迹、核restframe下，spin1/2的裸核I=1、linearQ/U=0，但orientation可有circularV；四组symbolicδ CG效应矩阵为I2/0，新旋转光子迹相合；两者共享SymPyCG后端/既有d helper，不计完全独立程序或实验。必要反例同样保留：后续γgate的1/2→3/2→1/2 pureM1/M1 jointW=1+¼P2；Ji3/2rank2控制1−½P2；声明boostβ=.1 labJacobian的a2≈.0200862不是Sun实际速度/A2。因此实际paperA2究竟是rest发射项还是lab/response现象自由度未定前，不能机械置零、称已测alignment或推τbias。物理域/linear-vs-circular与frame/gate限制已写linearpolarization/DSAM方法，正式17只一次，18仅知识preview。

### 实验反证原件：15O的finiteτ转upperlimit

[timegate/candidate011](20261019-DAY17-linear-polarization-paq-compton-run-01/candidate-pool-011.json)重建后仍在原窗口，明确只恰好18无学分methodpreview；Galinski2014原body未得，[terminalboundary](20261019-DAY17-linear-polarization-paq-compton-run-01/galinski2014-body-boundary.json)保留。另选实际可得的独立DSAMcounterprimary [[../../knowledge/sources/schuermann-2008-15o-6792-dsam]]，[primed回忆](20261019-DAY17-linear-polarization-paq-compton-run-01/schuermann2008-before-body-freeze.json)先冻再开source，实际arxiv0804.1934v1七页/9图/2表/2式完整原读、PDF1–6所有mainfigures视觉核。[identity/scope](20261019-DAY17-linear-polarization-paq-compton-run-01/schuermann2008-reading-scope.json)和Crossref核2008身份；PDFdated2018与官方tex date today仅版本/编译边界，不造2018新实验。

SCH08-3–10：同Ge密角/gain监控、五线共享a/b/primaryF限制后，6792与6172 F=.99(.01)、τ<.77fs；作者同时说旧data点不矛盾而旧finite结论未获支持。Eq1的P=.987是GEANT4有限Ge尺寸Doppler修正，**不是线偏振P**；reference实际为6129keV的angle-dependenttail/background，不能当无误差stoppedline。5181companion共享本run系统误差，TableII的两个14N点复用Bister旧F作conversioncheck，不计新实验。

[真实TableI/II新合同](20261019-DAY17-linear-polarization-paq-compton-run-01/schuermann2008-attenuation-contract.json)/[程序](../../system/scripts/day17_schuermann2008_attenuation_audit.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/schuermann2008-attenuation-result.json)给P×F=.97713；错省P使apparentF低.01287，只是条件映射非原作者错误/τbias。额外独立SD假设下6792旧新F contrast≈1.897，与把旧central固定/只用新scale的≈6是不同问题；未复现作者>5σ的profiletest，也不据此否定其判断。τ<.77fs的ℏ/τ≈.85482eV与authorΓγ>.85数值相合但radiativeinventory/1σlimit语义分列，不升级90%CI。

源Eq2的SRIMprojectedvelocity/6thpoly原coefficients、centroidΣ和GEANT4P误差未得，不发明F(τ)fit。新知识写入DSAM/lifetimeaudit/原P-A-Qnote，原scope/frame问题不靠重复toy填补，formal17仍一次、18无学分、未开19。

### Jensen剩余主线：实际带混合与Qt标尺链

[重建候选/时间门012](20261019-DAY17-linear-polarization-paq-compton-run-01/candidate-pool-012.json)选择现成matchingDay18原件中本session尚未通读的剩余主线；不是新课卡。[新问题priming冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-fullmainline-freeze.json)承认历史fullingest及本session早期DSAM/表格暴露，随后完成48页主线、19图/8表角色/Eq1–9，[actualscope](20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-fullmainline-reading-scope.json)将密Table1/7/8overview与selectedrows核分开，不冒每格独立重建。原J01-1–10/flags保持，新11–18已canonical。

[实际Table1/5/6/7/8新合同](20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-bandmixing-contract.json)/[程序](../../system/scripts/day17_jensen_bandmixing_reference_chain.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-bandmixing-result.json)：M1rate37.25/.80和原Eq4/5给α²≈.0166274/β²≈.9833726、|V|≈1.764615keV、Q541/Q523≈1.164763；sinθ主值14.818°会错配原rate，namedbasis下选165.182°，它不是光子δ或signedV测量。Table5六model eigenpairs仅必要printingclosure，不cert原VMIfit。

Qt四输出=(A,B,rplusB,A/rminus)，两个来自DSAM、另两个依mixing；共享标尺不会在给每输出独立误差时自动保留。独立primitiveSD只是额外design，得到Q523/Q541尺度.0668847而原Table6.87(.10)保持，不反解actualCov/概率或叠已计5%。新matchedN96 observed/modelTm–Er双差44keV、Tm–Yb48keV只centraldiagnostic，不把100keV总模型残差全叫新pninteraction；Tmgain>5.3保持limit非点。

主线counter：band4spin/两bandδ多解及无3↔4link保持；Qt跨spin近constant有模型支持不等逐spin实测，E1绝对强度沿用同Qt/mixing链不计独立验证。Octupoleb未fit、examples残差与body/caption单位边界保留，较大Qt不能单独闭合crossing物理。Jensen/Lifetimeaudit/Qt/DSAM页持久化新解释与artifact，仍恰好18无学分、formal17仅一次/未开19。

### 官方31S：MRcompanion、原双根和同源寿命字段

[[../../knowledge/sources/nndc-2022-s31-mixing-lifetime-reference]]由本session[primed回忆冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-reference-before-freeze.json)后selected官方对象取得，actual[identity/hash/payload](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-selected-downloads.json)和[readingscope](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-reference-reading-scope.json)保存。Adopted913行仅targetedcontexts，reaction71行全读，不冒整评价全文；headerJun2022cut/Novrecordupdate不等包揽所有laterexperiment。

S31-2–5：1248同母态MR显式+.35(.02)回1970Moss α–γ，另+5.3(.4)根仍在comment，smallroot偏好含RUL/旧寿命条件，非角数据独断唯一δ。1971Engmann的meanτ720(180)fs与T1/2.50(.12)ps同源，转换约.72135/.17312ps不增加第三次测量。2010Do03两个detector预算再按额外quadrature/ln2转换，与Sun打印1.2+1.5−1.1和3.2±7.0ps大致相合；不把同paper两detector/不同单位当独立实验或恢复actualΣ。NSR两primary准确title/DOI已核，body/phase/fit未得。

[新合同](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-mixing-contract.json)/[程序](../../system/scripts/day17_s31_mixing_reference_contract.py)/[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-mixing-result.json)以fixedSunmean1.12ps作γ-only诊断：smallMR的fE2=.109131、τM1=1.2572ps、BM1≈.0232725，而USDBτE2=6.9ps对应fE2=.162319、rate-equivalent|δ|≈.440195、BM1≈.021883；不将差/.02当model排除显著性或nativephase已桥接。largealternate也保留条件结果，不用newτ再做RUL选根。理论CC/IPC组件printingclosure非独立ICC测量，不迁给其它δ。

S31-6/7另核3076/5156的1/2+premise，并保留4971附近channel-dependent可能双态；这补identity而非SunactualA2/响应模块。原BM1W(W.u.)栏也不裸比SunµN²。newsource/Sun/lifetimeaudit/DSAM/spinhalfnote均已canonical；没有新实验τ/δ/B或CI，formal17只一次、18无学分/未开19。

### exactXUNDL：同Sun论文编译及未给6390寿命

官方XUNDL目录新对象31016069,31S经[新beforebody冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-xundl-before-body-freeze.json)、[exactpayload/hash](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-xundl-selected-download.json)、[45行完整原读scope](20261019-DAY17-linear-polarization-paq-compton-run-01/s31-xundl-reading-scope.json)核为202401/27Dec2023compiled、explicitunevaluated2023Su03/PLB839137801。同目录两个XUNDL-11不按suffix选identity。

S31-12–15：其T字段转写两finite/四upperlimit，comments存原meanτ；6390T空，仅两个γ，支持当前结果地位的边界，不添第五项20fs/90%寿命。nominal250ln2=173.2868fs与compiled172等末位不完全闭合保留，不补原unroundedquantile/roundingrule、不改源结果。3435两γ62(12)/38(11)同Sunbranchsummary，不能与oldAdopted83/100归一直接混；unequalquotederrors不强推严格normalizedCov。新对象不是独立experiment/data或已得VoRbody，原prior/GP/config仍未得，canonicalS31/Sun页已持久化。

### Day18无学分预习：独立电子阻止数据的覆盖

[新source](../../knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md) ISP26-1–9从IAEA官网/实际CSV取得新输入；[来源前冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-data-before-freeze.json)、[actualscope](20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-reading-scope.json)与[可复算结果](20261019-DAY17-linear-polarization-paq-compton-run-01/stopping-coverage-result.json)保存新读范围、版本/hash和失败，非旧练习换学分。

官方电子截面满足−dE/dx=nS，核阻止已扣除/可忽略；两pair单独下载CSV与全库selected行相等，392行中只有63实验行，另329是SRIM2013模型。S/Au六组均32S，Wr1979仅.0168/.0251MeV/u两低能点；O/Ta没有15O，最低16O点.1167807MeV/u。Ep.318MeV与15u质量近似起点.001424MeV/u，即使用声明总γ能量8MeV宽松三角界，最低实验点仍高约46.55倍。这是能区诊断，不是原速度历史或新τ。

同位素匹配插值比只描述当前模型关系：Fs1976约.977–1.044，Wr1979约1.002–1.027，Bt1966约.962–1.928；不裁决原实验/模型或直接形成先验。初版跨17/18O到16O比值已剔除、原对象留档。单位核Wr .58MeV/(mg/cm²)=189.701×10⁻¹⁵eV cm²/atom，无density假设。literalerror不认证1σ/点间独立，Fs/Wr共享部分作者，SRIM训练谱系也未得。

`supports`下一原实验输入路线；`limits`用当前SRIM2013替Sun Geant4/database或SchürmannSRIM2006的v(t)cosψ；`revises`按元素/点数认匹配和独立性。Wardprimary403/OpenAlex无OA与schema403保留，N/Ta targeted仅14N编译点没有恢复Bister15N原输入。canonical method/auditledger/source/index已同步；formal17一次、18仍partial、未开19。

### Day18无学分预习：Bt1966原实验的计量来源

[Bethge1966 source](../../knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md) B66-1–10实际原读五页/六图/四式，原件从MPG公开档案唯一成员取得，ZIP CRC/hash核通过；[回执](20261019-DAY17-linear-polarization-paq-compton-run-01/bethge1966-archive-member-receipt.json)只读约5.64MB ranges，未下载/验整个50GB档案。publisher202空响应与原迁移页面非PDF保留，未冒称body。Bister1977精确DOI/metadata、APS403/harvest401/OpenAlex无OA/Scholar无PDF保留，其body与15N/Ta输入仍未得。

B66-3/5：原法要入/出阻止近似相同、局部弱能变；作者direct值整体高于charge-derived，明确归因于N0束电荷计量，S误差25%。两个方法有共用装置/上游质子阻止与模型，不是两个独立现代校准。Fig3的O半经验线与S的charge均值连接不是同一role，S当时缺同类比较；新primary解释旧编译比值的限制，不从当前SRIM比值裁决实验。

B66-9/10的[新符号练习](20261019-DAY17-linear-polarization-paq-compton-run-01/bethge1966-exercise-result.json)：固定localK/正geometryg时Seff=(KSi+gSo)/(K+g)，单bin对(t,−Kt/g)方向不辨识；N0共同scale可给条件rank1Cov，但25%未被赋为该scaleσ。Eq4要二阶电荷矩，不能取meancharge平方。首次python缺SymPy退出1已留，复用repo既有依赖后通过，非新独立软件/实验。

Fig3初目视跨断轴标记的疑似10倍差被高分辨率反证并保存，没称勘误；literal归一与IAEA16行/符号/核扣除完整桥仍partial。`supports`有源系统误差/companion，`revises`逐行独立σ假设，`limits`表到实际DSAM速度投影/先验。canonical source/IAEA/method/auditledger/index已同步，不给18信用、不重复17。

### Day18无学分预习：实际Geant4停止本领组件

[新source](../../knowledge/sources/geant4-2026-ion-stopping-component-contract.md) GSI26-1–10核公开v11.4.2实际callpath与已存在SDK11.4.2/G4EMLOW8.8；[source前冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-before-freeze.json)、[actualscope](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-code-scope.json)、[native完整回执](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-component-result.json)与[比较](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-comparison-summary.json)保存新输入。源码定向读非全Geant4/手册，reading_depth skimmed；初错误模块404/tree403保留，git ls-remote核实际tag/commit，未认证安装binary逐位同源或Sunprivateproducer。

三配置actual MODEL分别Bragg/LindhardSorensen/ParamICRU73，option4非空name才选external；.025低表边界/平方根外推、E/A与protonscaledenergy、electroncut/productioncut/nuclear开关分开。按63真实编译行各自同位素/纯NISTAu/Ta查询，另3诊断点不是实验。Wr编译/组件比standard约.922–.935、option4约.496–.546、external约.498–.548；无数据训练独立性/联合Σ/actualSun配置，不从此给sp新prior或实验错判。

首次fixture在未建modeltable时SIGSEGV−11；gdb/原kernel BuildPhysicsTables路径定位client少RunInitialization，修后原三个配置都0，未改SDK。另nativeexternal低能15O点首次total.0144161、重复.1501867，所有原始查询保留。仅加diagnostics的源码副本重现：首次rangebuild使chargeSquareRatio6.14324→64，末尾比值约.0959881；[严格context/hash重放](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-param-trace-replay.json)一致。初缺patch工具也留档、改用Python严格匹配，无系统安装。它是声明API/组件问题，不归因Sun真实posterior/transport/CI。

`supports`把停止模型落到可查的实际组件；`revises`以版本名唯一指定curve及把首次查询当稳定物理量；`limits`当前模型对原实验反演的替代。新source/IAEA/method/auditledger/index已canonical。formal17一次、18仍partial/无学分、未研究19，原窗口继续。

### Day18无学分预习：native AlongStep两步反证控制

GSI26-11–15的新[来源前/设计冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-design-freeze.json)先要求不能预填API迁移；随后读native callpath并运行[真实native控制](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-native-result.json)。纯NISTTa/15O21.354261keV、seed13579、nuclear/fluctuationoff、external/option4各.1/1nm，每event只前2steps后人为kill；不是完整slowing/实际DSAMresponse。四配置exit0，step由StepLimiter定，pre−post−deposit残差<10⁻¹⁶MeV。

[步骤摘要](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-native-summary.json)显示external两步长首event首step/次event对应deposit均.09598809169，option4均1。只插diagnostics的副本与原native步骤逐值同；.1nm未触发range，qtrace已见首次15000MeV过渡cache在localq²6.14324之后设64，末尾比值压低首步能损。它扩展此前API1nm的range路径解释，不能将range当全部首次状态问题的唯一来源。

[严格重放](20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-replay.json)重新编译native/两个diagnostic副本，步骤和trace一致，未patch SDK/publicsource。原stepcharge字段未当effectiveq²；只有声明模型与人为边界，未估Sun原τ/CI或任意实验bias。source/method/auditledger已canonical；`supports`native适用域控制，`revises`过宽或过窄的软件归因，`limits`局部step到真实response迁移。正式17一次、18无学分，不研究19。

### Day18无学分预习：alpha gate与vertex运动学合同

SUN23-27–31重核原PDF2 Fig1/3SecIII、官方tex183–199/210与SI Fig2；直接确定E为1mmSi残余沉积、DeltaE为87µmSi能损，而实际gate表达式是E/DeltaE+E/校正量仍未得。[冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/sun-alpha-gate-before-freeze.json)、[actualscope](20261019-DAY17-linear-polarization-paq-compton-run-01/sun-alpha-gate-targeted-scope.json)、[合同](20261019-DAY17-linear-polarization-paq-compton-run-01/sun-alpha-kinematic-contract.json)、[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/sun-alpha-kinematic-result.json)保存source/SDK质量/声明无损模型分层。

固定vertexbeam128MeV、targetrest/sourceQ5.533、无所有target/Si损失、theta0–13°，七态全部positivephysicalroots保留。2234高rootalpha49.4806–52.2116MeV，不含printed47±1；差值只否定“沉积gate直接等无损vertex”假设，不是实测loss、实验矛盾或原fit重做。SDK自洽Q5.53329137仅敏感性控制，高root差至多.000578MeV，不能用mass最后位强配gate。actualSDK masslookup在无particledefinition时可用AME12fallback，不认原Sun配置/新质量评价（GSI26-16）。

4动量与CM/Lab控制通过；2234 fixedangle dEx/dTalpha约−.5552至−.5554，2MeVvertex窗映约1.1104–1.1108MeVEx，支持源“约1MeV”的量级而非认证actualsorter/σ。角接受、前靶beamloss、出靶/Si/deadlayer和calibrationCov仍需实际producer。canonical Sun/GSI/method/auditledger已同步，formal17once/18无学分、不研究19。

### Day18无学分预习：23Mg原方法与公开SimDSAM

[Kirsebom source](../../knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md) K16-1–16实际原读arxiv1508.07188v1十三页/21图/2表/4式，全页视觉核；源码date-today解释PDF2018日期，journal2016与v12015分开，VoR未得。原TableII13行4finite/9limits已canonical，Ref25等PDF裁切字段不补metadata，6236/7444不造图号。作者7787<12fs/95%仍兼容争议双方，Bp前文±.07/结论±.007/19%内部差异保留。

该原实验明确alpha先出Au，约4MeV损失后才连接vertex与测量；nominal8°接受因束斑/散射扩展，100/500µmSi与Sun87/1000µm不同。Eq4 He contribution/swelling同时出现，peakdensity部分.55944不是总S或新σ；fixedBp/J/τ12重放omega_gamma1.11680meV并非新joint95%界。Fig21几何Ω乘积约1.01479也不消除宽门背景/角分布代价。[原式练习](20261019-DAY17-linear-polarization-paq-compton-run-01/kirsebom2016-exercise-result.json)与全部打印输入保持。

[SimDSAM source](../../knowledge/sources/simdsam-2015-public-dsam-code.md) SD15-1–15核实际2015code/2021READMEpin、52blob/hash/579892bytes，公开data为表/模型响应，不含原ROOTanal/experimentalhistograms/fitCov。defaultGEANT表、R1mm、效率最近能量bin/角度cubic等与正文示例不同，不能裸认paperexactjob或Sunproducer。

[原表达式组件](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-native-component-result.json)及[独立重编译重放](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-native-component-replay.json)实际0，初std::decay类名冲突仅语法适配/保源hash，原missingreturn和unusedZ14缺表警告保留。native径向矩.331814符合r=UR而非uniform-area .5；原gamma/v固定时间轨迹不满足properclock区间，xOutput与末步位置不同。alpha32MeV控制measuredtotal31.9864/internalresidual27.9898区分active总能与单E残余；public表peakmix/pure约.603–.612非Sun新40%误差。没有改原physics、构建原posterior或重拟合实验τ/CI。

`supports`实际公开输入可推进组件与原方法核验；`revises`代码可取得即原实验完全可复现、变量同名即响应相同；`limits`同设施/共享Forster/SRIM与新SDK问题的迁移。原代码MC使用导出表，不能直接套GSI26 runtime首状态问题。canonical两新source、Sun/method/auditledger/index已同步；formal17once，18仍无学分，不研究19课程卡。

### Day18无学分预习：Forster真实Mg/Au输入的反证

ISP26-14–17核实际Mg/Au pair/wholeCSV与exactFs1976ref CSV的十行逐字段相等：全24Mg/.2–3.2MeV/u、质量阻止单位、literalerror4。新[冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/forster1976-before-freeze.json)、[真实CSV](20261019-DAY17-linear-polarization-paq-compton-run-01/forster1976-Mg-Au-frozen.csv)、[原reader回执](20261019-DAY17-linear-polarization-paq-compton-run-01/forster1976-public-table-component-result.json)与[对照](20261019-DAY17-linear-polarization-paq-compton-run-01/forster1976-input-comparison-result.json)保存真实输入/模型角色；不是新独立标定。

ρ19.30把1.6MeV/u质量阻止4.37转为8.4341MeV/µm，支持K16 about8.5；sourcebeta .059–.065的质量数proxy约1.626–1.974MeV/u。整十点compiled/GEANT约.800–1.064、compiled/PASS约.699–.903，不能只拟一constant scale；邻近1.6/2.0点GEANT比1.01817/1.00624，限制“default表身份不同就证明论文/代码数值矛盾”的过强解释（K16-17/SD15-16）。没有σtest/拟scale/原Cov或24Mg→23Mg混合靶完整transfer。

Forsterprimary尝试仍body未得：OpenAlexclosed/noPDF、合法OAonly downloader status oa_not_found、NRC exactquery无结果；manifest的TDMlicense→confirmed_oa标签不认证body或授权，按实际0downloads记录。初CLI误用--doi exit1未发正文请求，改actual--dois后完成发现流程，不重试终态URL/从metadata补方法。canonical IAEA/K16/SD15/auditledger/index已同步，[reader重放](20261019-DAY17-linear-polarization-paq-compton-run-01/forster1976-reader-replay.json)compile/run0、52hash保持。

`supports`source约8.5的实际输入量级；`revises`仅凭模型label差就判数值冲突；`limits`literal4%对jointΣ/实验CI的保证。formal17once/18无学分，不研究19课程卡，原窗口继续。

### Day18无学分预习：有界MODEL joint packet及材料原源readiness

SD15-17–21/K16-18按[冻结设计](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-freeze.json)只运行原eventmain的64detected事件/array10000/新tmp目录，[显式卡](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-MODEL-job.CARD)保其余defaultphysics/table。产生[MODEL CSV](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-MODEL-joint.csv)与原ROOT，[schema](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-schema.json)核64行EPART/EGAMMA Float_t/keV，ASCII另含observedangles。不是原实验events或新拟合数据。

新目录严格重放同一physics/RNG，ASCII逐字相同、ROOT分支逐值相同；[实际strictreplay](20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-strict-replay.json)compile/run0、52hash保持。诊断EQa GetEntries/全bins=6820，default积分5427；64/6820=.00938416仅是截断proposal域/normalizedeff模型条件接受比，不认实验absoluteefficiency。info积分15是τpayload而非15事件。此case无角数组wrap/20k剪角，不能外推其他job。

原missingreturn/unusedZ14缺表和libunuran.so.16 Load失败都保留；源Unuran只有Load而无API调用，本次仍完成64条输出，但exit0不认证全部依赖/物理/原paperfit。oldclock/radius/输入边界不被重放成功清除，不增加history代原experimentalROOT/ROOTanal/Σ。

K16-19准确追到Alexander1981物性原源DOI10.1016/0022-3115(81)90217-8、JNuclearMaterials96,51–56。当前[readiness](20261019-DAY17-linear-polarization-paq-compton-run-01/alexander1981-primary-readiness-boundary.json)只有metadata，OpenAlexclosed/NRC无结果/OAonly0body；题名含DSAM不作A的独立性/循环性事实推断。实际calibrator寿命/停止输入/误差/适用温度dose仍需body。公开refs/releases/DataCite exactDOI审计（SD15-22）只回同master/noassets/既有arxivpaper，没有新实验包；未声称所有合法路线穷尽或联系作者。canonical SD15/K16/method/auditledger已更新；`supports`producer格式readiness，`limits`MODEL到实验/物性的迁移，formal17once/18无学分/no19课程。

### Day18无学分预习：独立Jenkins fractional-Doppler与混合来源TableI

[J04 source](../../knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md) J04-1–14实际原读arxiv astro-ph/0312404v1四页/一表/一图两panel及两insets，全页视觉核；源码date-today解释PDF2018，不增实验/版本。[冻结](20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-before-freeze.json)、[scope](20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-reading-scope.json)、[练习输入](20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-exercise-contract.json)与[结果](20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2004-exercise-result.json)保持source与条件推导。

22MeV12C/薄C/Gammasphere采集独立于K16，七角centroids→fractionalshift→modelτ，feedingdirect是假设。TableI τ10(3)为本次，omega_gamma1.8(.7)adoptedAngulo；其余表项也混新γ/旧direct/spectroscopicfactor输入（原s_l命名保留）与模型估计，不当九个新强度测量。附近态用不同branch-gates辨认，100列是观测/归一角色，非完整inventory已精确闭合。

原Q7579.6(1.4)及23/22近似回算九Ep中心均.05keV内，独立quadrature名义errors不完全闭合；commonQ-only2.14223keV²外积是显式条件，不是actualΣ。τ10给总宽65.8212meV，固定J/adoptedomega/仅两通道有Bp互补根.05040/.94960，展示branchcompanion必要，不是新Bp/CI。实际58/42两γ在声明3MeV理想step下visible.58/totalfactor1.724，不能重放作者含energy/yield/response的保守4meV界或自行给CL。

J04原文说finite-recoil已校，而K16二级评论旧Ex似未校，需photon/gap/currentfinalenergy/详细文桥，不能自动加修正改raw。DCO all-axis/90vs32/37校准.9/1.7不可迁ST99/SG98，E2标签不只允许DeltaJ2，作者Jπ判断还含transfer/mirror/stretched条件。原centroid/stopmodel/feeding/Σ及2004/2013谱系未齐，下一详细文核依赖。canonical J04/K16/methods/auditledger/index已同步；`supports`独立寿命链，`revises`混读新τ/旧强度，`limits`裸ratio/τ到唯一Jπ/Γgamma。formal17once/18partial，无19课程。

## Durable knowledge delta

本批新增[thesis源](../../knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md)F22-16–30及[lifetimeledger](../../knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md)“Ch5原选择合同：粒子门、合成角与污染拒绝”：原PID/合成角/contaminationcut/observable合同与真实22行可重放输入，canonical保存而非仅outputs。


新增[作者Ch4源](../../knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md)F22-2/6/10/11/12/15；EVASIONS/F23及lifetimeledger明确19mm反证和response/benchmark域，科学beliefrevision写入knowledge而非仅outputs。


canonical [官方Mg23源](../../knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md)“新23AlEC对象：编译也未认证absoluteγ参考”新增M23-17–26；lifetimeledger及method同步NR/字段/参考警示/共同尺度矩阵。


新增[TAMU报告源](../../knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md)TA07-3/4/6/7/8/9/12和[[lifetime-strength-audit-165tm-136nd]]“γ参考谱系：真实后续采集与绝对分母仍有边界”，保存真实run/相对比/单位/缺失输入矩阵。


新增[GADGET上游原件](../../knowledge/sources/friedman-2020-gadget-al23-proton-branch.md)FR20-7/8/10/11/12/14/15与[[lifetime-strength-audit-165tm-136nd]]“Friedman2020：独立相对强度与共享绝对输入”，保存新采集/旧归一/推荐组合矩阵及实际算术边界。


新增[EVASIONS原release源](../../knowledge/sources/evasions-2023-public-release-native-readiness.md)EV23-2/5/6/8/13/14和[[lifetime-strength-audit-165tm-136nd]]“publicrelease与原paperproducer分开审计”，持久保存真实数据/原失败/版本边界，outputs非唯一知识副本。


新增[新GANIL源](../../knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md)F23-5/8/9/10/11/15/16/18和[[lifetime-strength-audit-165tm-136nd]]“Fougères2023：新τ不变，branch更新改变omega”；保存新branch矩阵、实际图数据边界及公开event/producer可执行入口。


新增[ROOT5.22源](../../knowledge/sources/root-2008-v522-background-error-contract.md)R522-2/3/5/8/10/11；canonical [[polarimetry-shared-calibration-count-design]]“真实工具合同补充：平滑与匹配不自动进入Cov”和lifetimeledger同步实际反证/统计合同。


新增[作者thesis源](../../knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md) SA11-5/6/7/9/11/12/14及[[lifetime-strength-audit-165tm-136nd]]“低能质子companion：两层分母与作者自旋解释”；真实分母表、来源矩阵、条件复算和新可证伪ROOT输入均canonical。


新增[2010版本源](../../knowledge/sources/sallaska-2010-na22-letter-version-contract.md)S10-1/2/3/4/9和[[lifetime-strength-audit-165tm-136nd]]“短报/详细文的frame与同源版本”；可复用frame关系/同源矩阵/缺失输入均canonical。


新增[直接capture原件](../../knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md) S11-2/8/9/11/16/17及[[lifetime-strength-audit-165tm-136nd]]“直接capture强度：停止功率与归一分别检查”，保存可重用停止角色/NT/eff矩阵及实际partial预算。


新增canonical [23Mg官方源](../../knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md)与[[lifetime-strength-audit-165tm-136nd]]“23Mg官方匹配：先列自旋和分支，再谈寿命换强度”；M23-4/5/8/9/13/14提供可复用输入矩阵/条件计算。outputs不作唯一知识副本。


本轮十二个knowledge页面实际变更。新canonical [[../../knowledge/research-notes/polarimetry-shared-calibration-count-design]]保存P/A/Q表、两Jacobian、共同校准比值/误差、新计数/Fisher/MC、非线性反例和holdout设计；ST99-14及SG98-13/14给精确source锚点。两method页新增使用门、index提供入口；另新增[[../../knowledge/sources/grsisort-2026-compton-polarimetry-code]]保存public代码；[[../../knowledge/sources/garnsworthy-2019-griffin-facility]]与[[../../knowledge/experiments/triumf-griffin-compton-source-calibration]]保存实际paper/calibration证据。outputs不是唯一知识副本。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/research-notes/polarimetry-shared-calibration-count-design.md",
      "summary": "保存Day17新P/A/Q分层、联合计数/误差设计、改分母非线性与效率归一边界；均为附条件推导。 新增逐探测器合并、权重迁移、条件界与Rational反例。 增加公开producer/实际组件与版本反证入口。 增加原样完整ScalePlot的能量role与平均kernel核验。 新原件实际Q与版本/数据依赖已加入。 207Pb真实reference/归一依赖与readiness已补。",
      "anchor": "共同校准如何进入参考比值",
      "sources": [
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-14"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-13"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-14"
        },
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-15"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-15"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-7"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-11"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-12"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-12"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-3"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-6"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-5"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
      "summary": "本session完整主线/图表原件复核及共享a/reference/target依赖边界，原claim flags保持。",
      "anchor": "2026-10-19 Day17独立session的实际复核",
      "sources": [
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-14"
        },
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
      "summary": "本session完整原件复核，新增改分母非线性与发射/入射效率字典；原294等边界保持。",
      "anchor": "2026-10-19 Day17独立session的实际复核",
      "sources": [
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-13"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-14"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "summary": "新增共享校准传播与reference独立验证门。 增加公开producer/实际组件与版本反证入口。 新原件实际Q与版本/数据依赖已加入。 补真实.9/1.7 sourcegate与spin/E2条件，不迁linearP。",
      "anchor": "同参考校准的计数与误差门",
      "sources": [
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-14"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-13"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-7"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-12"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-23"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-24"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-1"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-2"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-3"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-4"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-5"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-6"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-7"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-8"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-9"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-10"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-11"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-12"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-13"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "summary": "新增primitive计数/响应归一与效率分母使用边界。 新增逐探测器合并、权重迁移、条件界与Rational反例。 增加公开producer/实际组件与版本反证入口。 增加原样完整ScalePlot的能量role与平均kernel核验。 保存默认Lean完整source的ROOTschema正负控制，未得实际data。 新原件实际Q与版本/数据依赖已加入。 补原表/native点身份、双距离角门与Table8 partial边界。 207Pb真实reference/归一依赖与readiness已补。",
      "anchor": "共同校准与估计量归一的联合设计",
      "sources": [
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-14"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-14"
        },
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-15"
        },
        {
          "path": "knowledge/sources/schmid-1998-gammasphere-polarization.md",
          "locator": "SG98-15"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-7"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-11"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-12"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-13"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-12"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-15"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-16"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-17"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-3"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "加入Day17新研究笔记导航；这里只是治理入口，物理主张仍回source/note。 增加公开producer/实际组件与版本反证入口。 新原件实际Q与版本/数据依赖已加入。 207Pb真实reference/归一依赖与readiness已补。 索引新的官方停止本领证据。 索引新读Bt1966原实验。 索引新的离子阻止组件合同。 索引23Mg原方法与公开代码页。 补真实ForsterMgAu十点/单位/reader对照与约2%邻点反证，保原body/Σ/job缺口。 索引描述纳入Mg/Au。 索引新的独立fractional-Doppler source。",
      "anchor": "polarimetry-shared-calibration-count-design",
      "sources": [
        {
          "path": "knowledge/sources/starosta-1999-pdco-experimental-test.md",
          "locator": "ST99-14"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-7"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-12"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-3"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-6"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-7"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-11"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-13"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-3"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-4"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-6"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-23"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-24"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-5"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-8"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-10"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-11"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-3"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-5"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-9"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-11"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-1"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-2"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-3"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-4"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-5"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-6"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-7"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-8"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-1"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-2"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-3"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-4"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-5"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-6"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-7"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-8"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-1"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-2"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-3"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-4"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-5"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-6"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-7"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-8"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-9"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-1"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-2"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-3"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-4"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-5"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-6"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-7"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-8"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-9"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-11"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-12"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-13"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-14"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-15"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-1"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-2"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-3"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-4"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-5"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-6"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-7"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-8"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-9"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-10"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-11"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-12"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-13"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-14"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-14"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-16"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-17"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-16"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-1"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-2"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-3"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-4"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-5"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-6"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-7"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-8"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-9"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-10"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-11"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-12"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-13"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
      "summary": "固定公开GRSISort/GRSIData、完整selected原件读取及原样ROOT组件；保留Lean默认目标反证和无真实data/Σ边界。 增加原样完整ScalePlot的能量role与平均kernel核验。 保存默认Lean完整source的ROOTschema正负控制，未得实际data。 新原件实际Q与版本/数据依赖已加入。 补原表/native点身份、双距离角门与Table8 partial边界。",
      "anchor": "条件组件的实际数值与反证",
      "sources": [
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-3"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-5"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-6"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-7"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-8"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-10"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-11"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-12"
        },
        {
          "path": "knowledge/sources/grsisort-2026-compton-polarimetry-code.md",
          "locator": "GRS26-13"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-12"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-15"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-16"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
      "summary": "本session完整读36页arxivv2/图表式，核原Q/角组/half-factor/重复数据、配置与计数分母，保存实际摘要重算与currentcode比较边界。 补原表/native点身份、双距离角门与Table8 partial边界。 定向v1角表/公开VoR无body访问边界。 共享Smith角表谱系已定向核，非独立实证。 207Pb真实reference/归一依赖与readiness已补。",
      "anchor": "本任务的量化、核验与认识修订",
      "sources": [
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-6"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-9"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-13"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-14"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-15"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-16"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-17"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-18"
        },
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-18"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-3"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/experiments/triumf-griffin-compton-source-calibration.md",
      "summary": "保存实际GRIFFIN source-calibration ledger、参考/target/gate、reportedQ和响应/Σ readiness；不新造实验。 补原表/native点身份、双距离角门与Table8 partial边界。 207Pb真实reference/归一依赖与readiness已补。",
      "anchor": "GRIFFIN源偏振标定的可复用输入账本",
      "sources": [
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-6"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-8"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-9"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-10"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-12"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-15"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-16"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-17"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-3"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
      "summary": "仅定向原PDF3/Table1/caption/Sec2与PDF4核共享角表/response合同，旧17claim行与flags不改，不重授全文credit。",
      "anchor": "Day17定向角表与response合同复核",
      "sources": [
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-18"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
      "summary": "两selectedENSDF对象实际字段/母态/MR/ICC/归一/β+及source谱系核验；派生Cov/photonpair练习明确为条件，不造P/CI。 记录Q行2012更新而header201102的row-version边界。 以Q/level预算约束whole-sourceβ+不能直接移作选中cascade污染。",
      "anchor": "原计数定义的受限练习",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-3"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-5"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-6"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-7"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-9"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-10"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-11"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-12"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
      "summary": "仅新增N/EC三页原manual文本/图像定向核，定义NR/BR/NB与IB/IE/TI，旧4claims/flags保持。 补parentE/QP身份边界。",
      "anchor": "Day17源参考的N/E字段定向应用",
      "sources": [
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-5"
        },
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-6"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-5"
        },
        {
          "path": "knowledge/sources/tuli-2001-ensdf-format-manual.md",
          "locator": "TU01-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/pb207-gated-polarization-reference.md",
      "summary": "以本session官方13/2→5/2→1/2实际输入导出双门角色I/Q_J/P，exactCG与独立F/F3/directsphere控制；下支pure与nativephase/实际接受缺口明确，不重拟实验Q。",
      "anchor": "交换门角色不能只交换能量",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-14"
        },
        {
          "path": "knowledge/sources/nndc-2011-pb207-bi207-polarization-reference.md",
          "locator": "N207-15"
        },
        {
          "path": "knowledge/sources/garnsworthy-2019-griffin-facility.md",
          "locator": "GF19-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
      "summary": "本session先DSAM定向，后新问题冻结并完成48页主线/19图8表/9式角色核；actualbandmixing链/同标尺/模型baseline与E1单位边界，新11–18自审，旧1–10行/flags保持。",
      "anchor": "2026-10-19 Day17内无学分Day18定向自审",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-6"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-7"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-8"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-9"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-10"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-11"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-12"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-13"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-14"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-15"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-16"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-17"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
      "summary": "六页主线/五图两表三式原读；movinggatefulltail/globalfit边界及九行候选Qt几何，原14+CORRclaims/flags保持。",
      "anchor": "2026-10-19 Day17内无学分Day18重新原读",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-15"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-16"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "summary": "新lifetime-strength-audit把实际spectra、条件fitτ、rate/B/Qtgeometry与形变解释分层；只是无学分18preview。 补实际63实验行与方法模型、低能区和独立性清单。 补原实验计量/模型比较和独立性边界。 补实际停止模型配置与native failure checks，非原实验反演。 补native两步反证、transitioncache与range路径区分，保留实际实验response/Σ边界。 补alpha门残余/沉积/vertex合同、源Q条件运动学与gate-Jacobian边界。 补actualprimary/实际publicproducer输入与countercontrols，不造实验CI。 补真实ForsterMgAu十点/单位/reader对照与约2%邻点反证，保原body/Σ/job缺口。 补有界MODEL64联合packet/schema/6820proposal与strictreplay，保原data/Cov和A-primary缺口。 补actual独立primary的混合输入/共享Q/阈值与Γ分支练习。",
      "anchor": "B到Qt要另给几何",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-7"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-8"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-10"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-15"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-16"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-17"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-7"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-11"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-13"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-3"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-4"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-6"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-5"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-8"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-10"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-11"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-11"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-12"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-13"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-14"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-15"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-16"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-17"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-18"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-3"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-5"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-9"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-11"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-1"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-2"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-3"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-4"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-5"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-6"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-7"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-8"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-1"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-2"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-3"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-4"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-5"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-6"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-7"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-8"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-1"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-2"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-3"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-4"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-5"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-6"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-7"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-8"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-9"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-11"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-12"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-13"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-14"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-15"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-27"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-28"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-29"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-30"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-31"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-16"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-1"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-2"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-3"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-4"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-5"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-6"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-7"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-8"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-9"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-11"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-12"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-13"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-14"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-15"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-1"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-2"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-3"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-4"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-5"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-6"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-7"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-8"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-9"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-10"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-11"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-12"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-13"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-14"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-14"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-16"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-17"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-18"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-20"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-21"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-18"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-22"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-1"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-2"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-3"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-4"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-5"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-6"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-7"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-8"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-9"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-10"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-11"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-12"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-13"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "summary": "区分两source的三步/五步、5fs/2fs与stopping预算；fulltailgate不消feeding。 补DSAM电子阻止到投影响应的matchinginput边界。 补局部入/出路径与共同N0归一边界。 补模型/能量/cut/历史与实际电子量合同。 补native两步反证、transitioncache与range路径区分，保留实际实验response/Σ边界。 补alpha门残余/沉积/vertex合同、源Q条件运动学与gate-Jacobian边界。 补mixture/energy/properclock/software与实际response的分层门。 补有界MODEL64联合packet/schema/6820proposal与strictreplay，保原data/Cov和A-primary缺口。 补centroid/model/feeding链、总τ到branch/强度的必要合同。",
      "anchor": "fulltailbelowgate只控制一类selectionbias",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-15"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-16"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-6"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-7"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-8"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-7"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-11"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-13"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-3"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-4"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-6"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-17"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-20"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-21"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-22"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-23"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-24"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-5"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-8"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-10"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-11"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-11"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-12"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-13"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-14"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-15"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-16"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-17"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-18"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-3"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-5"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-9"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-11"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-1"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-2"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-3"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-4"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-5"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-6"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-7"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-8"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-1"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-2"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-3"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-4"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-5"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-6"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-7"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-8"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-1"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-2"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-3"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-4"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-5"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-6"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-7"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-8"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-9"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-11"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-12"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-13"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-14"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-15"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-27"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-28"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-29"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-30"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-31"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-16"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-1"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-2"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-3"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-4"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-5"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-6"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-7"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-8"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-9"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-11"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-12"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-13"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-14"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-15"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-1"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-2"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-3"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-4"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-5"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-6"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-7"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-8"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-9"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-10"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-11"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-12"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-13"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-14"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-15"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-18"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-20"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-21"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-18"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-22"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-1"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-2"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-3"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-4"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-5"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-6"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-7"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-8"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-9"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-10"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-11"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-12"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-13"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/transition-quadrupole-moment.md",
      "summary": "固定K和候选stretchedaxisCG是不同几何；9行算术匹配不唯一认证producer/内禀轴。",
      "anchor": "固定K与候选stretched-axis几何",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-17"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-11"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-12"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-13"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-14"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-15"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-16"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-17"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "J01-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
      "summary": "原读2022v2十页/5图1表3式，actualprior/likelihood/GP与quantile、6390conditional应用及USDB辅助M1提取分层；未得SI/actualinput/paperproducer。 补alpha门残余/沉积/vertex合同、源Q条件运动学与gate-Jacobian边界。 补真实同设施companion与Sunproducer/gate迁移界限。",
      "anchor": "Bayesian DSAM首先要问likelihood与prior合同",
      "sources": [
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-6"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-7"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-9"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-10"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-11"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-12"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-13"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-15"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-3"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-4"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-6"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-17"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-20"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-21"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-22"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-23"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-24"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-3"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-5"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-9"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-11"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-12"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-13"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-14"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-15"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-27"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-28"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-29"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-30"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-31"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-16"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-1"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-2"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-3"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-4"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-5"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-6"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-7"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-8"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-9"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-11"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-12"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-13"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-14"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-15"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-1"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-2"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-3"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-4"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-5"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-6"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-7"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-8"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-9"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-10"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-11"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-12"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-13"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-14"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/wang-2023-experimental-studies-nuclear-chirality-china.md",
      "summary": "保留旧reviewscope/claimflags，把当时未摄入Sun的历史边界回链现在原读primary；不升原review为独立验证。",
      "anchor": "2026-10-19 primary follow-up boundary",
      "sources": [
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-9"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
      "summary": "固定2015publickernel四文件实际原样编译/两API执行，variableCov/normalizer、fixedCov与custom分支callpath反证，原fullprojectBoost失败/初版本保留，不代Sunpaperproducer。",
      "anchor": "MADAI公开likelihood核与paperproducer是两个对象",
      "sources": [
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-2"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-3"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-4"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-5"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-6"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-7"
        },
        {
          "path": "knowledge/sources/madai-2015-distribution-sampling-likelihood.md",
          "locator": "MDA15-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/spinhalf-angular-nuisance-response-contract.md",
      "summary": "实际SI spin1/2前提引出核rest singles域证明；arbitrarypositiveρ可linearP0/circular非0，后续γgate与boost反例限定A2解释，不判原fit错或造CI。",
      "anchor": "不能省略末态求迹条件",
      "sources": [
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-23"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-24"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-13"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
      "summary": "实际arxivv1七页/9图2表2式完整原读；同Ge密角/共几何与gain、P有限尺寸F分母、finite-to-limit反证、同数据再分析/统计对象和上限width边界；不造原MC/Σ。",
      "anchor": "15O6792：数据点相容不等于寿命提取结论相同",
      "sources": [
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-3"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-4"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-5"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-6"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-7"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-8"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-9"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-10"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-11"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-12"
        },
        {
          "path": "knowledge/sources/schuermann-2008-15o-6792-dsam.md",
          "locator": "SCH08-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
      "summary": "实际官方Adopted定向/旧reaction71行全读，1248MR双根/RUL选根、半衰期/mean同源、1/2身份与channel双态及model-rate对照；未得oldprimarybody/phase/actualCov。",
      "anchor": "31S1248：官方MR输入有真实来源，也有选根条件",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-1"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-2"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-3"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-4"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-5"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-6"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-7"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-8"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-9"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-10"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-11"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-12"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-13"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-14"
        },
        {
          "path": "knowledge/sources/nndc-2022-s31-mixing-lifetime-reference.md",
          "locator": "S31-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
      "summary": "新增官方selected电子阻止数据、同位素/能区/误差与模型边界。 补新primary读取状态与原计量误差解释，保持旧未读历史。 补同位素匹配组件对照，不称新独立数据或prior。 补真实ForsterMgAu十点/单位/reader对照与约2%邻点反证，保原body/Σ/job缺口。",
      "anchor": "电子阻止数据能约束什么，尚缺什么",
      "sources": [
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-1"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-2"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-3"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-4"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-5"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-6"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-7"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-8"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-1"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-2"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-3"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-4"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-5"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-6"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-7"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-8"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-1"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-2"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-3"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-4"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-5"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-6"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-7"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-8"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-9"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-10"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-14"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-16"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-17"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
      "summary": "新读Bt1966原五页/六图/四式，束流系统/方法合同/局部推导与未闭合图表桥分开。",
      "anchor": "从原实验看阻止表的误差与对象",
      "sources": [
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-1"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-2"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-3"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-4"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-5"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-6"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-7"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-8"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-9"
        },
        {
          "path": "knowledge/sources/bethge-1966-heavy-ion-stopping-charge-states.md",
          "locator": "B66-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
      "summary": "新增真实SDK组件/模型/表/API与首次范围构建诊断，保留producer/实验边界。 补native两步反证、transitioncache与range路径区分，保留实际实验response/Σ边界。 补alpha门残余/沉积/vertex合同、源Q条件运动学与gate-Jacobian边界。",
      "anchor": "同一个Geant4版本也须记录实际模型与查询合同",
      "sources": [
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-1"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-2"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-3"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-4"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-5"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-6"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-7"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-8"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-9"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-10"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-11"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-12"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-13"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-14"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-15"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-27"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-28"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-29"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-30"
        },
        {
          "path": "knowledge/sources/sun-2023-bayesian-dsam-31s.md",
          "locator": "SUN23-31"
        },
        {
          "path": "knowledge/sources/geant4-2026-ion-stopping-component-contract.md",
          "locator": "GSI26-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
      "summary": "新增23Mg原13页主线与响应/植入靶/alpha门/limit及条件强度练习。 补真实ForsterMgAu十点/单位/reader对照与约2%邻点反证，保原body/Σ/job缺口。 补有界MODEL64联合packet/schema/6820proposal与strictreplay，保原data/Cov和A-primary缺口。 补独立J04原source与K16转引/energy定义边界。",
      "anchor": "先传播粒子到探测器，再解释能量门",
      "sources": [
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-1"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-2"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-3"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-4"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-5"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-6"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-7"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-8"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-9"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-11"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-12"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-13"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-14"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-15"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-1"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-2"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-3"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-4"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-5"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-6"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-7"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-8"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-9"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-10"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-11"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-12"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-13"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-14"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-14"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-16"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-17"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-18"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-20"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-21"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-18"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-22"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-1"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-2"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-3"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-4"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-5"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-6"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-7"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-8"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-9"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-10"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-11"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-12"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-13"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/simdsam-2015-public-dsam-code.md",
      "summary": "新增真实2015代码/52blob/data与原表达式native控制及exactjob边界。 补真实ForsterMgAu十点/单位/reader对照与约2%邻点反证，保原body/Σ/job缺口。 补有界MODEL64联合packet/schema/6820proposal与strictreplay，保原data/Cov和A-primary缺口。",
      "anchor": "公开程序的行为与原实验job分别核对",
      "sources": [
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-1"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-2"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-3"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-4"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-5"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-6"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-7"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-8"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-9"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-10"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-11"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-12"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-13"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-14"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-15"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-1"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-2"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-3"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-4"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-5"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-6"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-7"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-8"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-9"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-10"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-11"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-12"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-13"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-14"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-14"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-15"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-16"
        },
        {
          "path": "knowledge/sources/iaea-2026-stopping-s-au-o-ta-records.md",
          "locator": "ISP26-17"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-16"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-17"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-18"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-20"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-21"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-18"
        },
        {
          "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
          "locator": "K16-19"
        },
        {
          "path": "knowledge/sources/simdsam-2015-public-dsam-code.md",
          "locator": "SD15-22"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
      "summary": "新增独立J04原件/真实TableI、fractional-Doppler与adopted强度/阈值/条件Σ分层。",
      "anchor": "一张表中的新能谱、新寿命和旧强度不是同一类证据",
      "sources": [
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-1"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-2"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-3"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-4"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-5"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-6"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-7"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-8"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-9"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-10"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-11"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-12"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-13"
        },
        {
          "path": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
          "locator": "J04-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
      "anchor": "自旋和分支是寿命换强度的实际输入",
      "summary": "新增五对象官方匹配与half/mean、分支、条件强度约束。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-1"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-4"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-5"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-8"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jenkins-2004-23mg-fractional-doppler-rate.md",
      "anchor": "官方后续：保留不同自旋与未决身份",
      "summary": "保留官方不同spin及未确认身份/采集边界。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-2"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-4"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
      "anchor": "官方字段补充：上限同源，自旋仍需条件化",
      "summary": "核同源half/mean，不由编译固定原J7/2。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-4"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-5"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "23Mg官方匹配：先列自旋和分支，再谈寿命换强度",
      "summary": "加入spin/branch/omega输入矩阵及条件两通道多根/无根边界。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-4"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-8"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-9"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-13"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "用总寿命推共振强度时的额外输入",
      "summary": "总宽到强度需要spin与分支，不把central no-root当排除。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-13"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "DCO的EM字符可能已借寿命先验",
      "summary": "记录RUL/寿命共享输入与DCO字符边界。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-3"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[nndc-2021-mg23-lifetime-strength-reference]]",
      "summary": "新增canonical source入口。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
      "anchor": "完整积分减少一项依赖，绝对归一仍需要证据",
      "summary": "新增原20页完整主线、实际预算重构与共享校准条件。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-1"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-2"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-8"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-16"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
      "anchor": "2011原件补充：强度输入有实际归一合同",
      "summary": "补新primary并保留先前compiled-only时点。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-13"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-14"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
      "anchor": "直接capture原件：避免绝对stopping的范围",
      "summary": "补寿命换强度的真实companion与stop/共享边界。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-2"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-9"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-12"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "直接capture强度：停止功率与归一分别检查",
      "summary": "写入完整积分/有限窗/NT/eff和实际误差预算矩阵。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-2"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-8"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-11"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-16"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "独立capture companion的“无绝对停止”也有条件",
      "summary": "停止功率角色按具体推断分开。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-2"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-8"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-9"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "名义magic angle与共同效率的companion边界",
      "summary": "保留P4/有限接受与效率比Cov。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-4"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-5"
        },
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[sallaska-2011-na22-absolute-resonance-strength]]",
      "summary": "新增直接capture source入口。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
          "locator": "S11-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
      "anchor": "版本相同表值不能代替分析程序或勘误正文",
      "summary": "原读四页短报/版本差异和frame条件推导。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-1"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-2"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-3"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-4"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sallaska-2011-na22-absolute-resonance-strength.md",
      "anchor": "Letter版本补充：frame定义需要实际程序桥",
      "summary": "补实际同源短报/公式frame边界。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-2"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-3"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-4"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "短报/详细文的frame与同源版本",
      "summary": "同源证据/NR关系/正式erratum缺口分开。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-1"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-3"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-4"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-5"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "寿命companion的frame合同",
      "summary": "公式推导与actualproducer修正分开。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-3"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-4"
        },
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[sallaska-2010-na22-letter-version-contract]]",
      "summary": "新增短报版本source入口。",
      "sources": [
        {
          "path": "knowledge/sources/sallaska-2010-na22-letter-version-contract.md",
          "locator": "S10-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
      "anchor": "每次β衰变的质子强度与激发态的质子份额不同",
      "summary": "新增作者thesis定向数据/响应/归一与条件重构。",
      "sources": [
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-1"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-5"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-6"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-7"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-9"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
      "anchor": "作者thesis中的Bp分母与自旋条件",
      "summary": "补真实Bp分母和来源依赖，不造新CI。",
      "sources": [
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-5"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-6"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-9"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "低能质子companion：两层分母与作者自旋解释",
      "summary": "增加matchedbranch/相邻IAS/背景与同源矩阵。",
      "sources": [
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-5"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-6"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-7"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-8"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-9"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "共享归一与净计数：低p伴随观测的实际例子",
      "summary": "记录归一Cov与工具误差待核边界。",
      "sources": [
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-11"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-12"
        },
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[saastamoinen-2011-thesis-al23-proton-response]]",
      "summary": "新增定向thesis源入口。",
      "sources": [
        {
          "path": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
          "locator": "SA11-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/root-2008-v522-background-error-contract.md",
      "anchor": "自动处理对角误差不等于传播完整分析协方差",
      "summary": "新增真实旧API/hash、组件与归一Jacobian审计。",
      "sources": [
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-1"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-2"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-3"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-5"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-8"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
      "anchor": "ROOT5.22公开API反证：内容改变不代表误差闭合",
      "summary": "收窄原自动传播保证，不改作者结果/原claims。",
      "sources": [
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-2"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-3"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-8"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "实际ROOT5.22：自动误差传播的范围收窄",
      "summary": "记录actualcode/producer边界/归一Cov。",
      "sources": [
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-2"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-3"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-5"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-10"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "平滑后的背景不是新增Poisson计数",
      "summary": "计数误差分层与estimatedscale合同。",
      "sources": [
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-2"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-3"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-5"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/polarimetry-shared-calibration-count-design.md",
      "anchor": "真实工具合同补充：平滑与匹配不自动进入Cov",
      "summary": "给Day17 design增加实际工具反证/使用门。",
      "sources": [
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-2"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-3"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-5"
        },
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[root-2008-v522-background-error-contract]]",
      "summary": "新增actualcode source入口。",
      "sources": [
        {
          "path": "knowledge/sources/root-2008-v522-background-error-contract.md",
          "locator": "R522-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
      "anchor": "新寿命近旧值，分支输入显著改变强度链",
      "summary": "新增新primary/真实数据/producer身份及图数据复算边界。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-1"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-5"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-8"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-10"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-11"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-15"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
      "anchor": "新GANIL输入：τ相容，BRp已另测",
      "summary": "新独立寿命/branch和推荐组合分列，不改旧claims。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-5"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-8"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-9"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
      "anchor": "历史Bp不是当前唯一输入",
      "summary": "更新旧branch使用门，保历史分母。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-8"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-9"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-10"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "Fougères2023：新τ不变，branch更新改变omega",
      "summary": "写新输入矩阵/实际图数据不闭合和L4入口。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-5"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-8"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-9"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-10"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-11"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-15"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-16"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "事件级速度差也保留停止和联合能量输入",
      "summary": "方法与剩余response/cov合同分开。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-3"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-4"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-5"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[fougeres-2023-mg23-velocity-difference-lifetime]]",
      "summary": "新增新原件与真实数据入口。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
      "anchor": "公开事件已取得，原版发布程序尚不能代替论文fit",
      "summary": "新增原release实际build/原函数/真实eventquery与readiness边界。",
      "sources": [
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-1"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-2"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-5"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-6"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-8"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-13"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
      "anchor": "原publicrelease后续：真实data可读，paperfit仍需版本桥",
      "summary": "补actualproducer核，不把release故障外推paper实验。",
      "sources": [
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-5"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-6"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-8"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "publicrelease与原paperproducer分开审计",
      "summary": "保存L4实际输入/失败与fullCInot-ready矩阵。",
      "sources": [
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-2"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-4"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-5"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-6"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-8"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-13"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "已公开producer仍需原输入和调用合同",
      "summary": "build/return/table/physicsfit分层。",
      "sources": [
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-5"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-6"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-8"
        },
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[evasions-2023-public-release-native-readiness]]",
      "summary": "新增原release/native审计source。",
      "sources": [
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
      "anchor": "新相对强度与旧绝对参考共同给出daughter分支",
      "summary": "新增完整原件/真实分母与共享误差复算。",
      "sources": [
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-1"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-7"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-10"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-11"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-12"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
      "anchor": "Friedman2020原件补充：推荐组合的共享源",
      "summary": "核BR上游primary和推荐组合共享，不计独立omega。",
      "sources": [
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-10"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-12"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/saastamoinen-2011-thesis-al23-proton-response.md",
      "anchor": "新gasratio仍选择性采用旧高能参考",
      "summary": "低p疑虑与旧reference有效性逐字段分开。",
      "sources": [
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-9"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-10"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "Friedman2020：独立相对强度与共享绝对输入",
      "summary": "更新来源矩阵/两ratioCov/下界endpoint角色。",
      "sources": [
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-7"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-8"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-10"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-11"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-12"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-14"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "新采集与独立校准不是同一件事",
      "summary": "实际共享reference/近独立stat使用门。",
      "sources": [
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-7"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-8"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-10"
        },
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[friedman-2020-gadget-al23-proton-branch]]",
      "summary": "新增GADGET独立采集/旧reference源入口。",
      "sources": [
        {
          "path": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
          "locator": "FR20-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
      "anchor": "后续采集与同一source链的重复引用需要分别记录",
      "summary": "新增机构三报告原8页/真实run谱系与分母边界。",
      "sources": [
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-1"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-3"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-4"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-6"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-8"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-9"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/friedman-2020-gadget-al23-proton-branch.md",
      "anchor": "γ参考源链的机构原报告补充",
      "summary": "保absolute3.95未闭边界，核后续新采集。",
      "sources": [
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-3"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-4"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-6"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "γ参考谱系：真实后续采集与绝对分母仍有边界",
      "summary": "保存run矩阵/r与Bp/时间label条件复算。",
      "sources": [
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-3"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-4"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-7"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-8"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-9"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "Compton屏蔽和reference版本：原报告的使用门",
      "summary": "屏蔽/新event/共享标定与相对绝对角色分开。",
      "sources": [
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-3"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-4"
        },
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[tamu-2006-2007-al23-gamma-reference-reports]]",
      "summary": "新增原报告source入口。",
      "sources": [
        {
          "path": "knowledge/sources/tamu-2006-2007-al23-gamma-reference-reports.md",
          "locator": "TA07-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
      "anchor": "新23AlEC对象：编译也未认证absoluteγ参考",
      "summary": "新增299行exact对象/NR/absolute参考caution/能量角色与共同scale。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-17"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-18"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-19"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-21"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-24"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-25"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-26"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "官方23AlEC：NR空与绝对参考警示",
      "summary": "更新真实官方归一/比值相消/3.95未闭矩阵。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-18"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-19"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-21"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-24"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-25"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-26"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "anchor": "参考警示要追到比值中的共同尺度",
      "summary": "参考争议与比值Cov逐层分开。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-18"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-19"
        },
        {
          "path": "knowledge/sources/nndc-2021-mg23-lifetime-strength-reference.md",
          "locator": "M23-25"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
      "anchor": "作者输入说明修订几何疑点，却不认证完整paperjob",
      "summary": "新增作者Ch4完整13页/真实geometry/σ/SNR/验证域与算术。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-1"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-2"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-6"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-10"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-11"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-12"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-15"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-16"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-18"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-20"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-21"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-24"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-25"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-26"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-27"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-29"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-30"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-31"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-32"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-34"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-36"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-38"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-40"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-41"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-42"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-43"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-44"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-46"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-47"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
      "anchor": "作者thesis反证：19mm不是已证几何故障",
      "summary": "primary反证支持公开geometry，原native问题另保。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-2"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
      "anchor": "Chapter4实际输入：geometry与验证域",
      "summary": "增加同研究primary实际输入/使用门。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-2"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-10"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-11"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-12"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "作者Chapter4修订geometry疑点与response范围",
      "summary": "写实质beliefrevision与benchmarkdomain矩阵。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-2"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-5"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-6"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-10"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-11"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-12"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "同作者primary也能修订代码审计的解释",
      "summary": "nativefault与装置description分开核。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-2"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-10"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-12"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[fougeres-2022-thesis-evasions-response-contract]]",
      "summary": "新增thesisCh4 source入口。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "summary": "新增Ch5原PID/粒子门、合成角、污染拒绝及β/Δβ身份合同；缺原mask/job/Cov不新fit。",
      "anchor": "Ch5原选择合同：粒子门、合成角与污染拒绝",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-18"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-20"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-24"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-25"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-29"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-30"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "Ch6同数据组合：minσ与未知协方差",
      "summary": "写回同data三方法/minσ的条件反证、真实BRfitdomain/先验及版本差与失败spincompanion。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-36"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-40"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-41"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-43"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-44"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-46"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-47"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/root-2026-chi2test-option-contract.md",
      "anchor": "统计量由实际接口、误差状态与分析域共同定义",
      "summary": "固定双ROOT/sourceblob/native与原表达式，建立实际统计API/zero/bin/errorstate边界。",
      "sources": [
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-1"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-2"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-3"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-4"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-5"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-6"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-7"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-8"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-9"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-10"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-11"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-12"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
      "anchor": "统计API与inactive示例的边界",
      "summary": "保持旧inactive结论并补新实际API/原表达式。",
      "sources": [
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-8"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-9"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-11"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "ROOT接口与inactive示例：不能由LL名字指定统计量",
      "summary": "整合同数据寿命统计的API、inactivecallpath与原job缺口。",
      "sources": [
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-2"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-3"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-5"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-8"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-9"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-10"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-11"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "直方图比较的接口名不能替代统计合同",
      "summary": "增加直方图统计合同使用门。",
      "sources": [
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-2"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-3"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-4"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-5"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-8"
        },
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "ROOT统计API入口",
      "summary": "新固定版本source入口索引。",
      "sources": [
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
      "anchor": "统计API与inactive示例的边界",
      "summary": "新增EV23-16，旧rows/review保持。",
      "sources": [
        {
          "path": "knowledge/sources/evasions-2023-public-release-native-readiness.md",
          "locator": "EV23-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
      "anchor": "A.2真实三窗的背景算符",
      "summary": "新增F22-48–53：真实三窗/误差算符与曲率、signalleakage/原job边界。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-48"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-49"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-50"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-51"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-52"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-53"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "A.2实际三窗：扣背景谱的误差合同",
      "summary": "整合原A.2实际背景窗口与不将扣后谱当Poisson的使用门。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-48"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-49"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-50"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-51"
        },
        {
          "path": "knowledge/sources/fougeres-2022-thesis-evasions-response-contract.md",
          "locator": "F22-53"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
      "anchor": "真实显示数据的ROOT统计合同查询",
      "summary": "新增F23-24–28，真实原图25点与actualROOT/statistic/errorhistory合同和一致缩放，原fit仍未鉴定。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-24"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-25"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-26"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-27"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-28"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/root-2026-chi2test-option-contract.md",
      "anchor": "统计量由实际接口、误差状态与分析域共同定义",
      "summary": "新增RCT26-14原公开图数据companion，非独立实验。",
      "sources": [
        {
          "path": "knowledge/sources/root-2026-chi2test-option-contract.md",
          "locator": "RCT26-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/lifetime-strength-audit-165tm-136nd.md",
      "anchor": "真实25图点：统计合同查询仍未识别原fit",
      "summary": "保存全25点各统计合同对照与normalizer/errorhistory配套缩放边界。",
      "sources": [
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-24"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-25"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-26"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-27"
        },
        {
          "path": "knowledge/sources/fougeres-2023-mg23-velocity-difference-lifetime.md",
          "locator": "F23-28"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

### checkpoint033：geometry解释已修订

F22-2/15给实测19(1)mm支持publicinput，先前back-to-back字面对照不得计为已证geometry错；EV23-10旧row保历史、追加反证。原loader/scalar问题独立，Ch4σ/SNR和longbenchmark窗口还不能关闭F23fsfit/Σ。下一高信息是事件重建与fit章节，未读不预填。


合并权重的代数条件已由新Rational推导/直接逐台求和闭合，见canonical新段；原ST99/SG98实际逐台ledger仍缺。下一高信息路线转公开sorting/producer：检查其是否保留原始hit类别、逐detector几何/门、背景与response，和能否构造匹配参考/target的真实输入；泛用代码不能自动视为原1998/1999 producer。

完整U/r/t/逐台权重/fit-Cov、P_ref的AD/GOSIA不确定度、逐门响应/producer仍缺。若取得matched holdout失败或target-weight不同的实测ledger，将触发Q迁移和δ幅度判断修订；当前没有这样的观测，不裁决原实验。

## L0–L4 state

### checkpoint029：L4实际输入进展与fullfit边界

真实公开derivedevent/停止表/主要producer已取得并做native检查，属于已执行L4输入/组件审计；完整paperfit因release参数输出/格式/fit分支不齐仍not-ready。科学partial不当实验失败；下一输入必须改实际fit合同或补独立companion，不用更多toy/history填缺。


L1原件学习、L2源与方法写回已实质推进；当前L3为校准/response可识别性、最小独立检查设计与实际producer/primary readiness。原样软件组件为限定版本的实际代码执行，非实验L4。声明MC只是数理验证，不是actual experimental L4 fit；真实events/response/Σ未齐，实验重分析not-ready。日计划授权保持有效，不将缺口自动转为用户待办或额外启动请求。

## Verification and continuation

启动boundary和automationpreflight actualexit0；首次lint因新研究笔记缺11个必需heading为exit1，随后补齐并以JSON格式重跑的[lint-001](20261019-DAY17-linear-polarization-paq-compton-run-01/lint-001.json)为exit0、0errors190warnings（137citationkey/50rawslot/3reactionparser）。source旧25claim行/flags实际逐字核相同，raw/PLAN/Bib和继承dirty保留。`git diff --check`当前actualexit0。[verification-002](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-002.json)已实际核report/coverage/唯一writeback六页、boundary/lint/diff均通过，PLAN/Bib/recall与原25claim保护通过；H3与实际push另记本runpublication，未把内容检查当远端发布成功。

原研究窗口仍持续；当前[continuation-current.md](20261019-DAY17-linear-polarization-paq-compton-run-01/continuation-current.md)继续同一session的array-weight问题，不以本检查点终止整日。首检查点main / `Establish DAY17 polarization calibration evidence and count design`已actualH3/Gitee push，精确hash只[publication-001](20261019-DAY17-linear-polarization-paq-compton-run-01/publication-001.json)。新增producer/array/Q(E)本批的验证与发布见后续回执。原生goal仅在原窗口收束与所有交付/验证/发布完成后才标complete；Farmer PID42019确认存活，无pending恢复事件，不承担学习调度或Git。

Resume：`codex resume 01a1532e-0f21-7903-9bf6-8a9cc9ee9e17 -C /workspace/wiki -s danger-full-access -a never`。本轮正文/候选/续接尽量中文；QMD/overview批量刷新deferred。

### checkpoint002实际验收

[verification-005](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-005.json)实际report/唯一writeback七页/partial17 coverage/preflight/boundary/lint/diff通过，均actualexit0，0errors192warnings＝138key/51rawslot/3reactionparser。原25claim/review/PLAN/Bib/recall保护和四script/结果hash通过；新增rawslot/key仅为public软件归档/Bib边界，来源identity/cachehash已核。当前仍在原研究窗口，非Day17整日完成。

本批稳定指针main / `Audit DAY17 pooled polarimeter response and public producer contracts`；精确hash及实际H3/push只本runpublication-002，原已发布001继续有效。

### checkpoint003实际验收与下一anchor

[verification-006](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-006.json)实际report/coverage/唯一writeback七页/boundary/lint/diff通过，均exit0、0errors192warnings；nativeLean的已记录负例exit139与正例exit0是研究结果，未隐藏为全过。002 main / `Audit DAY17 pooled polarimeter response and public producer contracts`已actualH3/push；003稳定指针main / `Verify DAY17 native consumer schema and stage GRIFFIN primary`，actualhash/push仅publication-003。

下一anchor arxiv1809.07183v2已通过nature-academic-search定位和nature-downloader OA取得36页原件，hash/路径见[downloadreceipt](20261019-DAY17-linear-polarization-paq-compton-run-01/griffin-facility-download.json)，source前回忆另冻。当前只读首identity页与关键词定位，主线/图表/公式尚未读；不将检索或扫描的数字当新科学证据。研究仍active/partial17，继续完整原件，原deadline不变。

### checkpoint004实际验收与持续窗口

[verification-010](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-010.json)实际report/唯一writeback十页/partial17覆盖/boundary/lint/diff均通过、actualexit0，0errors195warnings（139key/52rawslot/4reactionparser；新source-calibration reaction字段对fusion parser不适用，显式保留warning）。旧ST99/SG98/Smith42条claim行与review状态、PLAN/Bib实际保护通过。Table8科学复现仍partial、原值/initialfailure不改；版本/数据边界见source，不从绿灯声称原实验或完整表成功。

003 main / `Verify DAY17 native consumer schema and stage GRIFFIN primary`已actualH3/Gitee push。本批004稳定指针main / `Ground DAY17 GRIFFIN calibration in primary evidence and geometry checks`，actualhash/H3/push只publication-004。研究仍由同session activegoal继续，原20日15点截止不变；局部来源/表核查完成不是整日结束。

### checkpoint005官方reference验收

官方207Pb两对象/P–N–E格式scope与1976primaryaccess边界见本run对应receipt；[verification-012](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-012.json)为本批当前验收。稳定指针main / `Audit DAY17 official Pb207 reference and normalization covariance`，精确hash与actualH3/push只publication-005。report/唯一writeback十二页、partial17coverage、boundary/lint/diff均须actual通过才发布；本checkpoint不授卡或结束原窗口。下一Hutter2002目前仅metadata，不算已读原件。

### checkpoint006条件参考与访问边界

[verification-013](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-013.json)实际report/唯一writeback十三页/partial17coverage/boundary/lint/diff通过，均exit0、0errors197warnings；新note初lint缺七schemaheading为exit1，修正并保留initialreceipt。旧N20713行/TU017行与reviewflags保持。新高L/半整数条件核、独立F/F3残差0和spherecontrols不代实验CI。

1977Ku09已核NSR/Crossref identity为Kumar等PRC15,1852、DOI10.1103/PhysRevC.15.1852；正文下载因CDP不可达为do_not_auto_retry，未读原扰动/phase/fit。1976/1977两对象新增OSTI查询connecttimeout，均未取得body，不原样重试。稳定指针main / `Derive DAY17 Pb207 gated Stokes with explicit phase and response limits`，精确hash/actualH3/push只publication-006。原研究窗与课程状态保持active/partial17，不因本批局部闭合结束。

### checkpoint007逐卡完成与持续窗口

[verification-015](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-015.json)实际report/coverage/唯一writeback18changed与19mapped(另含未改LKH82source)、boundary/lint/diff全部exit0，0errors197warnings；旧J01五行/MU08十九匹配行与review保持。014初contract验收的双partial和直接source链接缺口、初schema缺Assumptions均保留；现在17实际卡交付齐且001–006已发布、[Day18准备prompt](prompts/20261020-DAY18-dsam-lifetime-strength.md)存在，按证据完成17卡、只18partial，未放宽解析器或授18。

本批稳定指针main / `Complete DAY17 card and preserve uncredited DSAM preview`，actualhash/H3/push与仅一次课程对账只本runreceipt。**原研究窗口/nativegoal继续active**，不以完成课程卡结束整日。下一Sun2023已合法下载arxiv2203.10336v2/9Nov2022十页（不是2023VoR），当前仅PDF1/abstract/introstart；完整主线、方法/图式和actual公开input核验待续，不能把二级review或download当primary方法验证。

### checkpoint008 primary与一次学分对账

007已实际H3/Gitee push，之后[card-credit-007](20261019-DAY17-linear-polarization-paq-compton-run-01/card-credit-007.json)才把course从next17/count16推进到next18/count17，且append-only保存同session索引；只formal17，18preview无学分，原runner正常exit未观察，不伪造成功收束。research/nativegoal仍active。

[verification-016](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-016.json)实际report/唯一writeback20changed/21mapped/coverage/boundary/lint/diff均exit0，0errors199warnings＝141key54raw4parser；旧WC23十四claim/review/PLAN/Bib保持。初newsource缺rawhash已修且真实failure保留，reservedrawslot仍缺不写raw。稳定指针main / `Ingest Bayesian DSAM primary and audit model-assisted strengths`，actualhash/H3/push只publication008。下一actualMADAIcomponent/配置待核；源码已读部分不冒称编译通过或paperexactproducer，原15:00窗口不结束。

### checkpoint009原样软件与正式SI验收

008已实际H3/Gitee push；新[verification-018](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-018.json)实际report/21changed/22mapped唯一writeback/coverage/boundary/lint/diff均exit0，0errors201warnings＝142key55raw4parser；原Sun十五行/review/PLAN/Bib保持。原fullprojectBoost依赖失败exit1隔离为readiness，原样四文件两API组件的compile/run0与scientificcounterexample都保留，未将observedbehaviourchecks称Gaussian合同通过或原实验CI错误。

正式版主文的新imageAPI400/ScienceDirect403不当body，当前仍2022v2+publisherSI；只有SI新入口成功/已读。稳定指针main / `Audit MADAI likelihood paths and read official DSAM supplement`，actualhash/H3/push仅publication009。研究/nativegoal仍active至原15:00窗口，formal17仅一次/18无学分/未开19；下一SI的spin1/2–A2对象仅待限定核验。

### checkpoint010物理域与下一原方法输入

[verification-020](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-020.json)实际report/22changed/24mapped唯一writeback（含未改LKH82/YA67）/coverage/boundary/lint/diff全部exit0，0errors201warnings；原Sun二十二行/review及PLAN/Bib保持。新的restframe/末态gate/boost控制只给物理合同，不识别SunprivateA2模块或产生原τ/CI。符号与旋转迹共享SymPyCG后端/既有d helper，不计完全独立软件或实验。

Fry2018机构检索429验证页、OpenAlex无关结果均未接受为body；下一Galinski2014准确DOI已核为15O旧fsDSAMmethod，来源前回忆已冻，当前只metadata/下载尝试，不预填实际frame/prior。稳定指针main / `Separate spin-half emission from gated and lab angular response`，actualhash/H3/push仅publication010。正式17仅一次、18无学分/未开19，原研究窗口/nativegoal持续active。

### checkpoint011实验反证与原表算术验收

010已actualH3/Gitee push；[verification-022](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-022.json)实际report/23changed/25mapped唯一writeback/coverage/boundary/lint/diff全部exit0，0errors203warnings＝143key56raw4parser；原Sunsource自010逐字未变、PLAN/Bib保持。Schürmann actualsevenpages/Fig1–9/TableI–II/Eq1–2读毕，newF/P/统计对象算术不称原datafit。Galinskibody终态未得、Fry机构challenge边界保留，不当科学证据。

下一Bertone2001旧原实验准确DOI10.1103/PhysRevLett.87.152501只metadata与beforebodyfreeze，publiccandidate发现不等PDF已取；其body读取以actualreceipt为准，不能从2008转引补原实验细节。稳定指针main / `Read DSAM experimental counter-evidence and audit attenuation contracts`，actualhash/H3/push仅publication011；formal17只一次、18无学分/未开19，原研究窗口/nativegoal仍active。

### checkpoint012 Jensen完整主线与依赖矩阵验收

011已actualH3/Gitee push；[verification-024](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-024.json)实际report/23changed/25mapped唯一writeback/coverage/boundary/lint/diff全部exit0，0errors203warnings。原J01十行/所有review及PLAN/Bib保持，扩展本sessionmainline不重写历史targetedscope。新组态mixing/四Qtreference/同Nmodelbaseline算术只支持限定合同，未恢复原VMI/DCO/DSAMfit/Σ或新CI。Bertone精确OSTI索引请求最终connecttimeout，body仍未得；未将新失败冒称原科学反证。

稳定指针main / `Audit full Tm165 band-mixing and quadrupole-reference dependencies`，actualhash/H3/push仅publication012。formal17已一次/course18count17，18仍无学分知识preview，未开19；原研究窗口/nativegoal继续，下一用新的actualinput或source合同推进，不堆同代数/终态URL。

### checkpoint013官方MRcompanion与同文XUNDL验收

012已actualH3/Gitee push；[verification-027](20261019-DAY17-linear-polarization-paq-compton-run-01/verification-027.json)实际report/24changed/26mapped唯一writeback/coverage/boundary/lint/diff全部exit0，0errors205warnings＝144key57raw4parser，原Sun二十四行/review与PLAN/Bib保持。初newsourcegenericcanonicalURL重复及缺title_original的schemafailure已修并留initialreceipt，没改科学输入或raw。

原记录/本计算的half-life/mean/δ双根/RUL和model-rate层分列；XUNDL是同2023Su03的unevaluatedcompilation，6390T空不造第五项寿命，nominalprintingresidual不指认实验错。下一Moss1970exactDOI/NSRmetadata和beforebodyfreeze已留，Caltecholdpath404/新API无匹配/OpenAlex无publicPDF候选，不当primarybody；合法download尝试结果以actualreceipt为准。稳定指针main / `Verify S31 mixing references and same-paper lifetime compilation`，actualhash/H3/push仅publication013。formal17一次/course18count17、18preview无学分/未开19，原研究window/nativegoal仍active。


### checkpoint014停止本领输入验收

IAEA新source/四页canonical、真实CSV/单位/能区练习及scope已持久化；currentSRIM不当actualpaperproducer、literalerror不造prior或实验CI。verification028记录report/25changed27mapped/coverage/boundary/lint/diff实际exit；lint当前0error207warnings。初index缺链已修/initial留档。matrix18定位命令意外多显示19标题/条目，未读取19来源或做分析/授卡，见correctionreceipt；后续避免相邻卡context。稳定指针main / `Audit experimental stopping coverage for DSAM response inputs`，实际hash/H3/push只publication014。原研究window/goalactive、formal17一次/partial18不变。


### checkpoint015原实验计量验收

B66实际primary与公式/图role/counterevidence、真实PDF/hash/CRC/range与初failure已存；report唯一writeback26changed/28mapped，formal17once/partial18不变。verification029保存实际report/coverage/knowledge/boundary/lint/diff/protected/oldreviewchecks；当前lint0error209warnings。稳定指针main / `Read original heavy-ion stopping and charge-state systematics`，actualhash/H3/push只publication015。原研究window/nativegoal仍active，下一实际Geant4stopping对象/模型选择须新freeze与input，不把component认证成Sunproducer。


### checkpoint016 native停止组件验收

GSI26实际targetedcode/原表/nativecomponent/firstquerytrace及失败记录canonical；代码source保持skimmed，不冒称全原读或Sunproducer。唯一writeback27changed/29mapped，formal17once/partial18不变。verification030保存report/coverage/knowledge/boundary/lint/diff/protected/oldISPclaimchecks实际exit；当前0error211warnings，漏Summary的initiallint已修/留档。稳定指针main / `Audit native Geant4 ion stopping models and query initialization`，actualhash/H3/push仅publication016。原研究window/nativegoalactive，下一只核observedAPI路径能否迁到实际AlongStep合同，不无输入外推原实验bias。


### checkpoint017 native控制与claim索引验收

GSI26-11–15实际source/native/diagnostic/strictreplay已canonical；无原producer/experiment偏差外推。初lint虽然0，但新增claim与表header间空行令工具漏索引，本次连表保全部row文本/flags并显式核15GSI/13ISP。verification031记录report/27changed29mapped/coverage/boundary/lint/diff/protected/review及nativecontrols实际exit，当前0error211warnings。stablemain / `Bound native ion stopping state effects with controlled steps`，actualhash/H3/push仅publication017。原窗口/goalactive，formal17once/18partial不变；下一先核Sunαgate测量能量与vertex/后靶损失合同。


### checkpoint018 alpha gate合同验收

Source/SDK/条件vertex/Jacobian与actualgate缺口已canonical。旧26SUN/15GSIrows/flags保持；新SUN27–31最初插在NuclearStructure段未被claimheader索引，本次已只移动完整rows、显式核31SUN/16GSI，初lint0不当完整claimcoverage。verification032保存report/27changed29mapped/coverage/boundary/lint/diff/protected/review实际exit，0error211warnings。stablemain / `Separate detected alpha gates from vertex recoil kinematics`，actualhash/H3/push只publication018。原研究window/goalactive、formal17once/partial18不变，下一同设施Kirsebom2016需新freeze/实际body后才判迁移。


### checkpoint019 K16/SimDSAM验收（编号不是Day19卡）

K16完整原读/publicsource与原表达式nativecontrol/重放、52hash/失败/警告已canonical；未重fit实验τ/CI。唯一writeback29changed31mapped，旧Sun31rows/flags保持，新增SUN32与16K16/15SD15indexed且true；verification033记录report/coverage/boundary/lint/diff/protected/native实际exit，0error215warnings。K16exercise freeze初sessionID手误已保原/按runreceipt改执行元数据，时间/questionhash不变。stablemain / `Read original Mg23 DSAM and audit the public SimDSAM producer`，actualhash/H3/push仅publication019。原window/goalactive，formal17once/18partial不变，下一真实ForsterMgAu数据与primary核查，不研究19课程卡。


### checkpoint020真实输入反证验收

Forster compiled真实十点/units与原reader两tablemode/strictreplay已canonical，近邻约2%相容性限制过强的label冲突判断；原body/Σ/job缺口保持。旧ISP13/K16_16/SD15_15rows/flags保持，新ISP14–17/K16-17/SD15-16indexed true。verification034记录report/29changed31mapped/coverage/boundary/lint/diff/protected/native实际exit，0error215warnings。stablemain / `Cross-check real MgAu stopping inputs against public model tables`，actualhash/H3/push仅publication020。原window/goalactive，formal17once/18partial不变；下一有界MODEL joint packet先冻设计，不冒原实验data/τfit。


### checkpoint021 MODEL接口/readiness验收（不是新课程卡）

原eventmain64MODELpacket/schema/条件6820分母/RNG/新目录strictreplay与52hash已canonical，物理/依赖警告及原experimentaldata/job/Cov缺口保持；A-primary只metadata。旧K16_17/SD15_16rowsflags保持，新K16-18/19及SD15-17–22 true且indexed。verification035记录report/29changed31mapped/coverage/boundary/lint/diff/protected/packet实际exit，0error215warnings。stablemain / `Record bounded MODEL alpha gamma packet and producer readiness`，actualhash/H3/push仅publication021。原window/goalactive、formal17once/18partial不变；下一独立Jenkinsprimary需actualbody/新artifact，不再增加MODELhistory填缺口。


### checkpoint021 Git门失败与补偿修复

暂存check发现derivedMODEL CSV的CRLF与卡comment尾空格；在确认失败前已启动本地内容commit，是本session流程失误，尚未push。原runtime卡/ROOT/ASCII/52source均不改，只规范公开analysis副本行尾；48cardtokens/64CSV解析行逐项相同，初失败与原始卡文本/hash在publication-021-preflight-failure-and-correction.json保存。不重写历史，以 `Normalize MODEL packet delivery without changing physics data` 补偿提交，重跑current/cumulative/staged checks及H3通过后才推送。格式命令最后print变量名误用的exit1也保留，写入与hash复查独立确认。没有因此改变物理结果、needs_review或课程状态。


### checkpoint022独立J04与input谱系验收

J04四页/表图/源tex与真实TableI/条件ΓQthreshold练习canonical；不以newτ/adoptedω作两个新独立测量。旧K16_19rows/flags保持，新14J04/K16-20indexed true；verification036记录report/30changed32mapped/coverage/boundary/lint/diff/protected/exercise实际exit，0error217warnings，initialindex错误已修/留档。stablemain / `Audit independent Mg23 fractional Doppler and adopted strength inputs`，actualhash/H3/push仅publication022。021格式失误已非rewrite补偿、累计门0后actualpush，物理data/原runtime卡不改；本段commit增加guard避免失败门后提交。原window/goalactive、formal17once/18partial不变；下一J13actualbody/数据依赖桥继续，不从metadata补。

### checkpoint023官方Mg23输入验收

verification037记录本批实际report/coverage/writeback/boundary/lint/diff及旧claim/review保护；完成检查后才按显式manifest023/commitguard/H3发布。当前预习不授18，不结束原研究窗口。

### checkpoint024原件/误差预算验收

verification038核report/唯一writeback/course/boundary/lint/diff与旧claims/review；通过后manifest024/commitguard/H3显式发布。原窗口继续，正式17只一次、18无学分、不研究19课程卡。

### checkpoint025版本/条件推导验收

verification039为report/coverage/唯一writeback/boundary/lint/diff/旧claim与review门；实际通过后manifest025/commitguard/H3。当前仍同原研究窗口，不授18、不重复17、不开19。

### checkpoint026作者thesis/分母验收

verification040核报告/coverage/唯一writeback/boundary/lint/diff/protected/旧rowsreview；通过后manifest026/commitguard/H3发布。仍同原窗口，formal17once、18partial，不授18/no19。

### checkpoint027actualAPI/组件验收

verification041核report/course/唯一writeback/boundary/lint/diff与旧claim/review/保护；通过后manifest027/commitguard/H3。初decode/NumPybool失败已留档；发布fixture仅注释/尾空格规范且tokens不变，原源字节不改。同原窗口继续，formal17once/18partial/no19。

### checkpoint028新原件/实际数据验收

verification042核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected及实际numericartifact；通过后manifest028/commitguard/H3。缺uproot初失败已记录并用既有PyROOT6.40 schema读取，不安装依赖/不改raw。原窗口继续，formal17once/18partial/no19。

### checkpoint029原版native/实际输入验收

verification043核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected与原34hash/nativeartifact；通过后manifest029/commitguard/H3。原release问题已隔离，不改raw/原data或paper结论。同原窗口继续，formal17once/18partial/no19。

### checkpoint030原件/共享归一验收

verification044核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected及真实artifact；通过后manifest030/commitguard/H3。初一页版本比较脚本语法失败已修/留档，不改科学输入；原窗口继续，formal17once/18partial/no19。

### checkpoint031原报告/源链验收

verification045核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected/artifact；通过后manifest031/commitguard/H3。科学边界保partial，原窗口继续，formal17once/18partial/no19。

### checkpoint032official对象/字段验收

verification046核report/course/唯一writeback/boundary/lint/diff/旧16M23rowsreview/保护与artifact。通过后manifest032/commitguard/H3；原source未修，未造实验CI，formal17once/18partial/no19。

### checkpoint033thesis输入/反证验收

verification047核report/course/唯一writeback/boundary/lint/diff/旧rowsreview/protected/artifact；通过后manifest033/commitguard/H3。原source/数据未改、未新fitCI，formal17once/18partial/no19。

### checkpoint034原选择合同验收

verification048核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected与真实22行artifact；通过后manifest034/commitguard/H3发布。仍同原窗口/goalactive，formal17只一次/partial18，不授18/不开19。

048初diffcheck抓到continuation末端多空行(exit2)，保initial-failure.json；只规范EOF后重跑，不改科学输入/结果。

### checkpoint035同数据统计合同验收

verification049核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected与新实际artifact；通过后manifest035/commitguard/H3发布。formal17once/18partial/no19，原window继续，未重报实验CI。

### checkpoint036实际API验收

verification050核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected及native/sourcehash；通过后manifest036/commitguard/H3。ROOT低count/forcedUUwarnings有意保，非coverage验证；原windowactive、formal17once/18partial/no19。

050实际boundary/lint/diff均exit0；lint0errors/239warnings(4reactionparse/161citationkey/74rawmissing)，41changed/43mapped；旧claims/review/protected与native检查通过，warnings未清除。

036cachedcheck因新stderr末端空行exit2，commitguard在commit前拒绝，未生成失败提交。保initialfailure与原tmpstderr，只规范交付文本EOF、warnings内容/科学源/结果不改，再通过cached门才提交。

### checkpoint037原背景算符验收

verification051核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected及实际门/精确有理数artifact。通过后manifest037/commitguard/H3；原windowactive、formal17once/18partial/no19，原τ/BR/CI未重报。

### checkpoint038真实图数据/native验收

verification052核report/course/唯一writeback/boundary/lint/diff/旧claimsreview/protected及新真实data/nativeartifact。通过后manifest038/commitguard/H3，原window/goalactive、formal17once/partial18/no19，无新原paperfit/CI。
