---
type: learning-daily
graph-excluded: true
created: 2026-10-18
updated: 2026-10-18
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

原始回执为[run.json](20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/run.json)，本次按用户指定固定日报路径保留文件名中的20261017；实际run_date与截止按runner注入的20261018回执，不从旧预备段落延长或缩短。课程已依据本session独立交付与实际publication005对账为next17/count16，只计Day16一次。Day15 partial16、旧分数、旧程序检查不计本session学分；13:00上海按原时间门开始恰好Day17知识预习，只列partial17，不正式计17，未打开Day18。首个科学checkpoint已发布到Gitee，原run/goal继续active，学分仍未授予。

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

## Counter-evidence and missing companion observables

最直接反例是一个已知pure参考也无法验证混合项相位：两纯端点通过，错误换号仍改R。另一个反例是本点模型部分Table1不吻合（例如.637341对印值.66；1.188657对1.12），且两比值rectangle没有复现作者>85支；原因未裁决，不能报告原文错误或实验新δ。

作者的强度比1.2±.2相对预期2.3只支持其branch偏好；模型预期和Cov缺失，不能变成独立、无假设的排除。182-keV E1/ICC结论不是921-keV target的独立companion。下一有判别力测量需同921/306、90°/38°/φ18°及matched cuts的P幅值、Q921、净计数/背景、与DCO共同事件Cov；没有这些输入不计算实验显著性或束流时间。

## Knowledge Impact and Learning Decision

`supports` DCO多解与phase/response合同；`revises` 不分gate角色直接联合同名R的做法；`limits` 偏振符号挑根和pure reference认证全部相位。没有新Jπ、B值、wobbling/chirality结论；178W条件计算不外推A≈130。本轮已按当前池/唯一Day17预习重查公开来源和必要输入；在原始response/producer/Σ及特定未得正文边界收束，不由同一模型重复或标签复用补成确定结论。

## Durable knowledge delta

canonical [178W知识单](../../knowledge/research-notes/w178-921-dco-gate-double-solutions.md)保存实测身份表、作者双候选、role reciprocal/Cov Jacobian、矩阵/新两根、phase交叉表、未复现结果和下一companion。KF89 source新增15–18；dco-ratio与旧worksheet有反链，index有最小导航。程序与outputs输入/结果用于复算，本节不是唯一知识副本。

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
      "summary": "将本session178W新交付与Day15预习分开，增加canonical反链。 恢复批次新增：同一mixed跃迁的上游与下游参考：1505-keV真实表值。 新增固定ALPACA独立实现/观测对象边界。 新增原ENSDF章/total-decay和MR字段边界。",
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
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "最小索引新增178W921计算单导航，不添加独立科学结论。 新增固定ALPACA独立实现/观测对象边界。 新增原ENSDF章/total-decay和MR字段边界。 加入ICC概率物理域方法入口。",
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
      "summary": "保存高自旋factorization公式、十行反向检验和finite系数替换失去exact交换R=1的条件控制，分开absolute/relative误差。 同页保存独立130Ba真实三角度实验的两个shape信息与shared-denominator门。",
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
      "summary": "保存PAQ分层、双分段actual432计数公式/derivatives、fiterrors与理想Poisson层区别、printingfailure和matchedeta/Q/fullCov门。",
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
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "summary": "区分GammasphereA与genericclover计数式，链接实际data/eta/Q共同校准与sourcebound，不扩展sourceparity结论。",
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
      "summary": "新增ENSDF原相位/format与total-decay条件权重；Radiative、电子与总衰变权重：同符号不等于同对象 新增RZ17实际参数的概率测度/producer和尾部边界。",
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
    }
  ]
}
```

## Open questions and belief revision

Dors[3]身份冲突已经定位到准确DOI，尚待全文给169/137的约定与误差。DCOMAP/width/finite response/feeding与Table1差异未决；两R与强度的Cov未得。原先“加P符号便能选两支”的直觉被本次同号例限制；更高信息输入是matched P幅值校准。缺口由Codex跟踪，不转为默认用户审核任务。

## L0–L4 state

L0为三篇主线/原图回核；L1/L2为新证据单和反向验证；L3调查已由用户恢复至原15:00截止，169参考定义/producer与新原件缺口保持开放。尚未进行experimental L4 refit；已有条件设计不冒充实际数据分析，也未取得完整input/response/Σ。未新增人审或修改旧needs_review。

## Verification and continuation

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
