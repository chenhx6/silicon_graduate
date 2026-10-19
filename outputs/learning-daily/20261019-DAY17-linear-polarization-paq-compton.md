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
| 本日报、唯一writeback与checks | 当前十八页canonical已变更；17主线检查/发布001–006已通过，唯一writeback/同sessioncontinuation/receipt与[Day18准备prompt](prompts/20261020-DAY18-dsam-lifetime-strength.md)存在；当前卡验收另记verification015，整日研究仍持续 | complete |

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

## Durable knowledge delta

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
      "summary": "新增共享校准传播与reference独立验证门。 增加公开producer/实际组件与版本反证入口。 新原件实际Q与版本/数据依赖已加入。",
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
      "summary": "加入Day17新研究笔记导航；这里只是治理入口，物理主张仍回source/note。 增加公开producer/实际组件与版本反证入口。 新原件实际Q与版本/数据依赖已加入。 207Pb真实reference/归一依赖与readiness已补。",
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
      "summary": "本sessionDSAM/必要context定向原读；三步5fs/实际belowgates/stopping预算、同源Qt标尺与11行条件换算，旧五claim/flags保持。",
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
      "summary": "新lifetime-strength-audit把实际spectra、条件fitτ、rate/B/Qtgeometry与形变解释分层；只是无学分18preview。",
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
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "summary": "区分两source的三步/五步、5fs/2fs与stopping预算；fulltailgate不消feeding。",
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
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

合并权重的代数条件已由新Rational推导/直接逐台求和闭合，见canonical新段；原ST99/SG98实际逐台ledger仍缺。下一高信息路线转公开sorting/producer：检查其是否保留原始hit类别、逐detector几何/门、背景与response，和能否构造匹配参考/target的真实输入；泛用代码不能自动视为原1998/1999 producer。

完整U/r/t/逐台权重/fit-Cov、P_ref的AD/GOSIA不确定度、逐门响应/producer仍缺。若取得matched holdout失败或target-weight不同的实测ledger，将触发Q迁移和δ幅度判断修订；当前没有这样的观测，不裁决原实验。

## L0–L4 state

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
