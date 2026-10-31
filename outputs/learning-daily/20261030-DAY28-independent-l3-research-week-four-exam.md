---
type: output
graph-excluded: true
created: 2026-10-30
updated: 2026-10-31
---

# Day28：131Xe 低自旋伙伴带身份与δ分支的独立L3研究

## Run state

- run_id: `2026-10-30-day-28-01`
- prompt_run_id: `prompt-2026-10-30-day-28`
- day_index: 28
- session_id: `01a18c47-452f-7ca0-aa54-ab0de4d55ca3`
- continuation_session_id: `01a18c85-5ae9-7331-b5b9-bd9ba8082fdd`
- timezone: Asia/Shanghai
- overnight_until: `2026-10-31T15:00:00+08:00`
- closeout_window_ends_at: `2026-10-31T16:00:00+08:00`
- completed_day_indices: [28]
- partial_day_indices: [29]
- next_day_index: 29
- research_status: completed
- Day 28 card audit: complete
- Day 28 scorecard: complete
- Day 28 weekly REFLECT: complete
- Day 29 preview: uncredited

### Day 28 card completion audit

| Day28 deliverable | Status | Evidence/artifact | Evidence locator |
|---|---|---|---|
| L3 recall and problem selection | complete | `recall-001.md`, `recall-002.md`, daily report | `## Candidate pool and selection` |
| Source-to-claim-to-locator milestone | complete | `131xe-low-spin-partner-crosswalk.md`, `table-audit-001.json`, P-ADO profile | `C23-D28-1`; `BNK20-D28-1`; `Real-table Result` |
| Quantitative/design exercise | complete | strength derivation, BrIcc candidate audit, P-ADO profile, 882 response contract | `同母态两商的条件推导`; `官方BrIcc名义系数与ICC边界`; `两分支的条件分离` |
| Counter-evidence and falsifier | complete | 882 input contract, parity conversion findings, P-ADO null profile, 1979 access boundary | `ENSDF转换记录的语义边界`; `Real-table Result`; `source-access boundary` |
| Report, scorecard, weekly REFLECT and continuation | complete | this report, `continuation-011.md`, `verification-041.json`, session receipt | `### 第四次周考评分表`; `### Weekly REFLECT（第四周，持续更新）` |

Day28 已在 `2026-10-31T02:20:00+08:00` 完成正式内容审计，并在随后开放研究窗口于 `2026-10-31T15:47:50+08:00` 完成最终 closeout。[真实runner回执](20261030-DAY28-independent-l3-research-week-four-exam-run-01/run.json)为run-01目录；注入文本中的run-28目录仅作为不同的元数据标签保留，不另造runner或覆盖回执。原会话ID来自events的thread.started；原讨论命令为 `codex resume 01a18c47-452f-7ca0-aa54-ab0de4d55ca3 -C /workspace/wiki -s danger-full-access -a never`。中断后用户在fork续研，实际续研session另列于上方，其命令为 `codex resume 01a18c85-5ae9-7331-b5b9-bd9ba8082fdd -C /workspace/wiki -s danger-full-access -a never`；没有把fork冒写成runner原会话，也未重开Day28。启动status仅有live runner目录未跟踪，既有tracked工作树干净；已通过路径边界及H1预检，Bib哈希匹配，未改raw/PLAN/课程state。

## Candidate pool and selection

| 候选 | 当前信息增益/重叠 | 本轮决定 |
|---|---|---|
| 131Xe B1(a)/B5与2023 yrast/yrare映射；δ分支 | questions.md有明确未决项，两篇原件本地可核；可修正同数据重复计权和错误标签 | 唯一continuity槽位，active-L3 |
| 131Ce 六条link与三组同母态E2比值 | 既有project已完成此练习；本轮启动时复算约0.04634、0.06305、0.03946未产生新知识 | 不继续重复，不列为新成果 |
| 187Au 双根与偏振争议 | Day27已有专项资产，当前另开会与伙伴判据主线重叠 | 暂不启用novelty槽位 |
| 全库知识地图与资料路径审计 | 既定131Xe路线已达到有界饱和；全库索引和raw/output引用依赖能直接改变下一阶段研究选择与可复现性 | 增加一个治理/研究导航槽位；只生成索引与manifest，不移动原件 |
| 135Pr 共同响应分支审计 | 全库复习发现已有 Matta–Lv–Sensharma 三方证据和明确响应缺口，可形成下一篇方法/核结构论文蓝本；与131Xe对象身份主线不重叠 | 作为 novelty 研究设计槽位；不重新声称已完成统一raw重分析 |
| P-ADO 共享alignment null | Zobel 1983十行真实表格 profile 产生了可复核的跨reaction共享`σ/J` falsifier，区别于已有逐行/凸包/选择性协方差脚本 | 写入P-ADO research note；不把表格级`tau`当实验coverage或普适校准 |
| Day29研究设计答辩 | 当前问题仍有1983 AD原文、宇称版本差异与联合响应等路线 | 尚未打开，不预授分 |
| Day29研究设计答辩（无学分预习） | Day28当前问题局部证据饱和且距硬截止超过120分钟；可把882/宇称问题写成最小observable与belief-revision合同 | 已预习一张卡，不计课程学分，不开Day30 |

依据：[课程卡](../plans/2026-09-22-one-month-daily-task-matrix.md)、[apprenticeship](../plans/2026-09-22-one-month-codex-cli-apprenticeship.md)、[论文管线](../plans/2026-09-22-a130-triaxial-thesis-pipeline.md)、[[131xe-low-spin-partner-crosswalk]]。本轮先看过Wiki，因此[冻结回忆](20261030-DAY28-independent-l3-research-week-four-exam-run-01/recall-001.md)和[限定题002](20261030-DAY28-independent-l3-research-week-four-exam-run-01/recall-002.md)均按primed/delayed recall记录，不冒充陌生闭卷考试。关键复述：L3先绑定对象，再判断来源证据和竞争解释；停止一个来源不等于停止整个研究窗口。

## Sources and evidence

| 来源 | 本轮实读与精确locator | 分层、独立性与处理 |
|---|---|---|
| [[chakraborty-2023-131xe-wobbling-origin]] | 8页期刊正文/参考文献主线；视觉核printed064318-2 Fig.1、-3 Figs.2/3和Table I、-4 Figs.4/5/6、-7 Fig.11 | 原采集重分析；实验表、作者signature解释和TPRM分开。新增C23-D28-1至9保留needs_review，既有人审字段不变 |
| [[banik-2020-131xe-multiple-band-structures]] | 局部回读printed044306-4 Fig.3、-5/-6 Table I、-8/-9/-10放置与B1(a)/B5讨论 | 2023明确引用为Ref22的同一采集；新增BNK20-D28-1至3。高自旋B1(a)、B5分支与低自旋新链不同 |
| [[alwaleedi-2013-band-structures-131ce]] | 既有AW13-9、Eq.5.6/5.7方法入口 | 只借用标准同母态B比公式及δ假设，本轮不宣称重新精读该thesis或其原始方法文献 |
| Lönnroth等1983，Phys.Scr.27,228–240，DOI10.1088/0031-8949/27/4/002 | Crossref核书目；2023 Ref20及printed064318-4所引a2/a4 | OA流程返回oa_not_found；IOP HTTP200实际是CAPTCHA HTML，未获得直接原件，不能给它独立已核证据权重 |
| NNDC `131Xe Adopted Levels, Gammas`官方评估PDF | printed p.3 的1600.6 `17/2−`、794.6 `M1,E2`；printed p.4 的Jπ与BrIcc说明 | 加强负宇称评估谱系，但仍是评估副本，不替代1979/1983 primary，也不消除2020/2023版本冲突 |
| NNDC selected-dataset reference page | `1979IR01` Irving et al.，J.Phys.G 5,1595 (1979)，DOI10.1088/0305-4616/5/11/015；列出γ(θ)、线偏振、δ、B(E2)、B(M1)覆盖 | 闭合来源身份和实验覆盖描述；未恢复794.6-keV逐行primary表 |
| Irving 1979 DOI/IOP/Crossref access probe | DOI、IOP article、IOP PDF与Crossref API；`tmp/day28-131xe-recovery/irving-1979/probe.json` | Crossref只闭合题名/作者/卷页/页码；IOP三条路径均返回HTML，未取得正文/PDF，不增加794-keV逐线证据 |
| Irving 1979 IOP abstract | abstract 给出 `131Xe` 低能 `364.5`、`636.9 keV` 正宇称级及角分布/线偏振/mixing-ratio coverage | 只支持实验覆盖和低能级摘要事实；abstract 没有794-keV目标线，不能替代正文或目标线 primary |
| 官方ANU BrIcc `BrIccS v2.3 (9-Dec-2011)` | `Z=54,Eγ=794.6 keV`；FO/NH、E1/M1/E2/M2的αK/αTot回显；官方表单拒绝能量误差字段 | 理论候选集合，非实验事实；M1/E2凸包和EKC比较仍受误差口径、归一和协方差边界限制 |
| C23 arXiv源文件与模型约定worker | `131Xe.tex:265-275`、Fig.11、公开APS/arXiv/机构元数据访问回执 | Hamiltonian骨架、参数和端点映射闭合；E/M算符、g因子、淬灭和δ能量约定未公开，不能用派生商反推 |
| `137Ba` Mendeley 数据访问复核 | `https://data.mendeley.com/datasets/skhmjshxdj/1` landing HTTP 200但无v1 snapshot；public API为`dataset not found`，无数据文件 | 只更新可复现性/L4输入边界；不把公开论文图表或网页壳当作event/response/Cov数据 |
| Zobel 1983 真实表格 P-ADO null profile | 同一958.0-keV纯E2、十个projectile/beam-energy条件；共享`σ/J`、共同`rho`与`tau`的profile结果为`tau=1`无共同区间、95%参考域需`tau≈1.72` | 这是跨reaction共享alignment null的条件性falsifier，不是否定P-ADO、单行fit或feeding-aware模型；无event-level Cov/coverage |

两份原PDF SHA-256实际匹配source frontmatter：C23 `730db39eb9a5aecd3bbce1dce3cb9c32829eb2f4a2062ee31c59ddc4d52bd9ff`；BNK20 `21e7e1eed7a93ffc3c38f4580fcf93863d02c56e40ffc900b1634df14c7f34e6`。当前C23本地文件有期刊页脚/首页出版信息，修正了source“arXiv版本”的旧描述。[联网核身份回执](20261030-DAY28-independent-l3-research-week-four-exam-run-01/network-verification-001.json)记录Crossref两精确DOI、arXiv2311.09713和APS页面的真实访问；科学主张来自本地原件，网页标题/摘要不充当实验依据。web检索工具未返回可用结果，改用公开API与来源原页，未虚构搜索命中。

source-to-claim-to-locator地图及逐态表保存在 [[131xe-low-spin-partner-crosswalk]]。目前已闭合1046-keV低自旋节点及1862-keV暂定成员的局部对应；没有将全部B5或高自旋B1(a)重命名。1600.9-keV节点在2020为17/2+、794.8-keV线列E1，2023为17/2−；两文同一偏振中心值仍需版本解释。2791.8-keV23/2+和2792.1-keV21/2−的近能量不是身份同一证据。

checkpoint003整合全部worker产物：1983原件获取、强度识别性推导、宇称谱系、882响应合同、ENSDF字段语义和最终只读整合审查；并修正band页固定宇称元数据、882小根缺完整边界、交接叙述滞后及lint回执读取旧文件的问题。[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D28-001回到printed318 Eqs.3.29–3.30及printed319 Eq.3.39；这是本轮定向方法复核，不新称阅读全文。

parity worker取得DAE2018短文、Kaya2018及NNDC官方档案；[source manifest](20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/parity/source-manifest.json)保留哈希、真实URL、原件覆盖及失败端点。原PDF/档案暂存在tmp，未改raw、未建缺raw的source stub。[[131xe-1601-parity-version-boundary]]把这些材料保存为待正式摄入的版本线索，区别于已入库两原件。1983原件仍未取得，2018的其它角关联不能补成1055-keV原始AD；也不把独立再见794线当作独立测定其宇称。

## Theory/analysis exercise

[可复跑代码](20261030-DAY28-independent-l3-research-week-four-exam-run-01/audit_131xe.py)仅用标准库；[输入、控制与结果](20261030-DAY28-independent-l3-research-week-four-exam-run-01/table-audit-001.json)保存原PDF哈希、逐态标签和十条边。14项控制含哈希、有限性、物理极限、近能量异自旋/宇称拒绝、暂定标签保留和NaN拒绝；它们验证程序合同，不认证科学模式。

1. **光子份额非线性。** `fE2=δ²/(1+δ²)`；671的0.03(3)中心为0.08992%，δ±区间映射为[0,0.35871%]；882的0.09(8)中心为0.80349%，映射为[0.01000%,2.80882%]。区间函数像不等于新置信区间；小解中心值不能作全部成分的全局上限。放大Fig.4后实际读到δ1055=0.1(2)，正文称approximately zero；其中心份额0.99010%、区间函数像[0,8.25688%]。旧0.00(2)撤回，本轮初稿“没有数值误差”的漏读亦已纠正。模型δ=-0.69对应32.25391% E2，是模型输出，不能移作实验误差或“纯M1”认证。
2. **同母态比值。** 能量用MeV、κ=0.697，`R=κ Ec^5/Ed^3 × Id/Ic /(1+δd²)`。对1055.1/815.6、6.0(2)/1.0(1)，条件δ=0得1.28496；独立强度一阶σ=0.13545，固定δ=0且未知ρ的局部σ包络为[0.08566,0.17133]。纳入实际Fig.4小解δ=0.1(2)，得1.27224，独立强度与δ的一阶传播σ≈0.1433，可对账作者1.27(14)，仍不代表完整profile。对794.8/766.5、12.6(2)/≈1.8得约2.57109，分母无误差，不能重建作者2.54(4)的精确误差。共同τ可相消，不把ratio叫absolute B。
3. **印刷闭合。** 十条边残差−0.2至+0.8 keV；1055.1线+0.8、929.7线+0.5。Table I是拟合/采用数值且isomer来自舍入图，缺联合Σ。保留原数并提出原表/版本核验，不擅调节点或报告χ²。
4. **同母态两商的识别性。** 新增 [[131xe-same-parent-strength-identifiability]]：RE=(Ec/Ed)⁵rδ²/(1+δ²)、RM=κEc⁵/Ed³×r/(1+δ²)，条件中心值约0.0163964与1.27224，满足RE/C+RM/A=r。两个商共享r与δ，不能当作独立确认。worker的11项正向率/单位/极限/Jacobian控制已通过；它们认证代数，不认证实验Σ。固定能量且假定三个印刷边际独立的局部ρ≈−0.32668只是传播示范；0.14的舍入不能反推作者误差算法。
5. **模型能量约定。** Fig.11最右TPRM列出902/799-keV模型端点，对应1055.1/815.6-keV实验线；但`RM=B(M1;out)/B(E2;in)`与出带δ之间还隔着未知`RE=B(E2;out)/B(E2;in)`，不能由`RM=1.27`和`δ=-0.69`反推δ采用哪组Eγ。固定同一pair并明确`E_ref`后，8.7535、9.7933和Fig.11端点下约5.5352/6.0614是有效条件敏感性算术；`RM≈0.87051`是定义明确的hybrid sensitivity。它们不是作者真实预测或统计裁决；仍保留模型算符、有效电荷、g因子、淬灭和δ能量约定缺口。来源C23-D28-7及模型约定审计。
6. **882分支响应合同。** 新增 [[131xe-882-branch-response-contract]]，把881.8/880.1逐门峰形、角对、条件取向、偏振scatter-bin响应、共享校准和联合Σ列为必需输入；给出预测集合不交与nuisance剖面距离的充分条件。704.6只作条件性同母态取向参考，671/1055不得迁移裁决882。机器合同 `workers/882-contract/input-contract.json` 标记 `ready_for_joint_fit=false`，不生成根值或显著性。
7. **ICC候选集合。** 官方BrIcc查询已取得794.6-keV的FO/NH、E1/M1/E2/M2 K壳和总系数；名义M1/E2凸包仍受原始EKC误差口径、能量误差和共同协方差限制，不能借理论表替代原始primary或完成统计宇称裁决。
8. **ICC区间几何。** 在明确声明“仅作区间显示”的假设下，`EKC=0.0017(7)`给`[0.0010,0.0024]`，M1/E2名义凸包`[0.00234,0.00316]`的重叠为`[0.00234,0.00240]`；E1/M2与该临时带不重叠。该练习不提供置信度、σ或宇称裁决，完整边界已写入 [[131xe-1601-parity-version-boundary]]。

精确来源：C23-D28-2/3/4/5/6/7/8/9/10、BNK20-D28-1/2/3、AW13-9；BrIcc和模型worker机器回执见run目录。候选能差0.5-keV窗只作账本比较，没有充当实验置信门。

## Counter-evidence and missing companion observables

- 2020已报道B5局部成员，反对“2023整条链均为独立新采集”的误读；2023Table I部分量采用2020，不能按文献数平均。
- 2023 Fig.5负δ区的曲线与色带还有交点，反对RDCO单观测全局唯一性；另一解的精确根值、权重和与偏振联合相容性尚未获得。
- 2023作者明确yrast17/2−比值约为模型两倍，反对两个17/2−态均与TPRM精确吻合；yrast/yrare也不是可不经映射就当作favored/unfavored的同义词。
- 旧Day19两source的“黄金零对照”“所有M1>99.2%”“γ软必然导致进动退化”等断言已在原source行撤回，旧脚本与JSON作为历史过程保留。未进行未经核对的全库批量科学修改。
- 缺少的companion包括882独立偏振/AD、794.8-keV宇称版本说明、逐线全局δ profile、≈1.8强度误差、partner-resolved寿命及同母态E2 out/in。真实response、Σ与event/gate IDs缺失，不生成代理L4。
- 新反向检查：2020 Fig.4图注、Table I脚注k、B3讨论均使用795-keV E1，削弱“单行偶然排印”的解释；2023的766.5-keV线偏振栏空，其quadrupole与符合证据不独立证明electric性质。来源BNK20-D28-3、C23-D28-8。仍未裁定哪一宇称正确。

ENSDF反向检查也未闭合宇称：官方归档的794.6(2)-keV记录列`M1,E2`、`A2=-0.71(2)`、`A4=-0.09(4)`和`EKC=0.0017(7)`；`EKC`是评估文件中的实测K壳转换系数字段，`M1,E2`仍是非唯一标签，MR/DMR为空。官方BrIcc现已返回同能量FO/NH名义系数：αK(E1)=0.000932/0.000935、M1=0.00316、E2=0.00234、M2=0.00835/0.00833；纯M1/E2 αK凸包为[0.00234,0.00316]。但能量误差、原始EKC误差口径、电子/γ归一和理论协方差仍未闭合，不能转成统计宇称裁决。详见 [[131xe-1601-parity-version-boundary]]、[[tuli-2001-ensdf-format-manual]]、[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]]。

**可证伪条件。** Fig.5已足以否定“RDCO色带本身仅有一个δ交点”这一限定命题，不能由此宣布作者整套解释错误。要否定指定H1模型，须在身份/背景/响应受控条件下，使全部数据相容的δ分支与该模型逐跃迁预测域均不相交；若仍有大E2解可行，则先补偏振/AD，不直接认定wobbling。最小设计和失败条件已写入canonical project。

## Knowledge Impact and Learning Decision

**revises / limits。** 本轮修正了来源版本、整带同义化、671所属链、1055误差及旧排他断言。仍保留原作者偏好yrare signature partner、未见wobbling信号的有界结论；没有提出新的核素级模型预测，没有声称完整重分析已裁决模式。共同响应缺失是L4 readiness边界，不是停止全部L3研学的理由。

## Durable knowledge delta

canonical主交付为 `knowledge/projects/131xe-low-spin-partner-crosswalk.md` 的“逐态与逐边对应，禁止整带同义化”“小δ分支、光子份额与模型输出分层”“印刷表重算与误差合同”：本页保存可复用对象表、数值、协方差边界、反证与最小设计。两source补入atomic claims并撤回Day19旧行；questions/index新增可回访入口。所有事实在knowledge有长期副本，日报/JSON不作第二事实库。

checkpoint003补做限定周考题002，回答882小根、RE/RM识别性和794.8-keV版本冲突三个部分；该题是延迟回忆，不冒充陌生闭卷，不自动增加课程学分。既有研究札记和source锚点保持needs_review边界。

本次再写回 `knowledge/research-notes/131xe-882-branch-response-contract.md` 的“目标和输入边界”“两分支的条件分离”“Companion选择和不可迁移控制”。该页只保存可复用设计合同和失败条件，不把outputs中的机器合同当长期事实唯一副本。

本checkpoint还把官方BrIcc名义系数和C23公开模型约定边界写回 `knowledge/research-notes/131xe-1601-parity-version-boundary.md` 与 `knowledge/research-notes/131xe-same-parent-strength-identifiability.md`；BrIcc数值只形成理论候选集合，模型实现缺口只形成source boundary，不升级为宇称或模型统计裁决。

时间门回执 `time-gate-003.json` 记录了当前可访问路线的有界饱和、候选池重建、Day29恰一张无学分预习和继续开放至硬截止的决定；它不改变课程状态。

`day28-card-reaudit-precheck-003.json`显示五项Day28交付的artifact和evidence anchor均存在，但全部保持`pending-final-audit`，不提前触发card credit。

本次严格按时间门只预习Day29一张卡，新增 `knowledge/research-notes/131xe-day29-research-defense-preview.md`：保存794-keV电子/γ、882偏振/角分布、共享校准、negative controls、三种belief revision和失败条件；该页是无学分预习，不推进`next_day_index`。硬截止时正式 card audit 已将五项 Day28 交付全部标为 `complete`；此前 `pending-final-audit` 仅属于 closeout 前预审回执，不代表最终状态。

本轮按用户要求完成全库温故知新索引，新增 `knowledge/synthesis/wiki-full-library-map-20261030.md`，把1,019页知识、研究主线、五个论文候选和后续深读/浏览/索引分层集中到一个可检索入口；`knowledge/index.md`已增加入口。该页明确“论文候选是研究问题，不是已发表结果”，并保留source、raw、响应、协方差和人工审核边界。

本轮也完成只读工作区审计，未改名、移动、删除或覆盖任何原始材料。`outputs/literature-acquisition/20261030-workspace-audit/audit-summary.json`、`raw-papers-manifest.tsv`、`outputs-manifest.tsv`、`knowledge-artifact-references.tsv` 和 `source-raw-reconciliation.tsv` 分别记录raw/output文件快照、SHA-256、大小、扩展名、知识页引用关系和source→raw回链状态；它们是可回滚整理的基线，不是科学事实源。独立YAML parser得到393条哈希匹配、57条路径缺失、10条未声明哈希、6条路径存在但hash未验证、16条未设置raw slot和1个frontmatter解析错误；最新outputs快照为13,166个文件。这些是待治理元数据，不直接等同于科学证据缺失。

另生成 `outputs-cleanup-candidates.tsv`：45个`.pyc`、677个零字节过程文件和6个名称含`copy`的人工复核候选。失败回执、历史修复文件和`verification-*`快照仍按provenance保留，不按文件名批量清理。

本轮新增一条不重复的相邻核科学路线：对 `32S` 第一 `2_1+` 态早期比较源 Vermeer 1982 进行来源访问核验。Crossref DOI 元数据和 Elsevier PII 可复核，但无授权文本接口只返回最小元数据，未取得旧四极矩数值、符号约定、实验方法或独立性信息。因此新增 `knowledge/research-notes/32s-vermeer-1982-source-access-boundary.md`，并在 Mavela source 页增加 `DD-20261031-32S-29`；该结果是 source-access boundary，不改变 `32S` 科学结论。

全库温故知新还发现 `knowledge/projects/100sn-gamow-teller-independent-evidence.md` 的历史 `checkpoint138` 标题和“99.62%”措辞仍可能被误引用。本轮在该 project 页新增 `Day28 Claim-Safety Boundary`，把相空间对账降级为 task-derived sensitivity exercise，保留 Hinke/Lubos 的 independent decay-chain 证据和 `HK10-D21-R99-*`/`LB16-D21-R99-*` locator，不把条件算术升级为实验淬灭裁决。

另外完成 `knowledge/research-notes/partner-em-interval-loso-audit.md`：对 `135Nd`、`134Pr` 和 `106Ag` 的伙伴带 `B(E2)` 表做 lineage-aware、协方差无关的逐自旋留出审计。`135Nd` 和 `134Pr` 没有硬拒绝共同尺度，`106Ag` 因无逐行误差而不可执行；这是一项可复现的数据合同练习，不是新的手征判据。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/131xe-low-spin-partner-crosswalk.md",
      "summary": "固化2020/2023逐态对照、δ分支/份额、同母态比值与印刷残差、L3反证和L4最少输入；两source新增原件核验与旧断言撤回。",
      "anchor": "逐态与逐边对应，禁止整带同义化",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-1"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-2"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-3"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-4"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-5"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-6"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-7"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-8"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-9"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-10"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-1"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-2"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-3"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-D28-001"},
        {"path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md", "locator": "AW13-9"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/131xe-same-parent-strength-identifiability.md",
      "summary": "补齐同母态RE/RM分解、共享信息与协方差，并保留模型delta的能量约定情景。",
      "anchor": "同母态两商的条件推导",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-6"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-7"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-10"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-D28-001"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/131xe-1601-parity-version-boundary.md",
      "summary": "区分多处E1标签、无偏振quadrupole与宇称实测；补入官方BrIcc名义系数与模型约定的公开来源边界，外部评估转录仍留在待正式摄入层。",
      "anchor": "版本差异不能简化成单行笔误",
      "sources": [
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-3"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-8"}
        ,{"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-10"}
        ,{"path": "knowledge/sources/tuli-2001-ensdf-format-manual.md", "locator": "TU01-D28-1"}
        ,{"path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md", "locator": "KB08-2"}
      ]
    },
    {
      "knowledge": "knowledge/bands/131xe-negative-parity-yrast-13-2-sequence.md",
      "summary": "同步1601-keV节点的2020/2023宇称版本冲突与766.5-keV无偏振边界，保留原页面human-reviewed状态并将新增判断标为needs_review。",
      "anchor": "Day28 Evidence Boundary",
      "sources": [
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-2"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-3"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-2"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-8"}
      ]
    },
    {
      "knowledge": "knowledge/bands/131xe-negative-parity-yrare-sequence.md",
      "summary": "纠正1055-keV旧简化、保留882双根与同母态派生量共享输入边界。",
      "anchor": "Day28 Evidence Boundary",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-3"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-4"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-9"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/131xe-882-branch-response-contract.md",
      "summary": "把882双δ分支的真实响应输入、集合分离条件、704.6竞争退激参考和失败边界固化为L4 readiness合同。",
      "anchor": "两分支的条件分离",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-3"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-9"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-D23-001"},
        {"path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md", "locator": "KS70-2"},
        {"path": "knowledge/sources/krane-steffen-1970-cd110-mixing-ratios.md", "locator": "KS70-6"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/131xe-day29-research-defense-preview.md",
      "summary": "预习Day29研究设计答辩：把794-keV宇称和882双根写成最小observable、响应/协方差、negative control、三种belief revision和失败边界。",
      "anchor": "最小测量组合",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-2"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-8"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-9"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-2"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-3"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/135pr-mixing-branch-input-contract.md",
      "summary": "把135Pr的Matta–Lv–Sensharma争议整理为共同响应、协方差、falsifier和论文结构蓝本；不把公开图表审计升级为统一实验重分析。",
      "anchor": "Day28：可发表的共同响应分支审计蓝本",
      "sources": [
        {"path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md", "locator": "M15-D22-R095-1"},
        {"path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md", "locator": "L22-D22-R095-1"},
        {"path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md", "locator": "SH26-D22-R095-1"}
      ]
    },
    {
      "knowledge": "knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md",
      "summary": "把30天后尝试投稿落成四个有证据门、falsifier和最小新增输入的候选队列，不把候选写成已完成论文。",
      "anchor": "Candidate Queue",
      "sources": [
        {"path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md", "locator": "M15-D22-R095-1"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-1"},
        {"path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md", "locator": "GA13-1"}
      ]
    },
    {
      "knowledge": "knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md",
      "summary": "更新137Ba数据可访问性边界：landing壳恢复但snapshot/version/files和科学数据仍缺失，L4仍blocked-input-limited。",
      "anchor": "SO20-D28-1",
      "sources": [
        {"path": "knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md", "locator": "SO20-D28-1"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/pado-shared-alignment-null-profile.md",
      "summary": "以Zobel 1983十行真实表格建立共享sigma/J、共同rho和tau的P-ADO null profile；tau=1无共同区间，结论只针对跨reaction共享alignment假设。",
      "anchor": "Real-table Result",
      "sources": [
        {"path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md", "locator": "Z83-11"},
        {"path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md", "locator": "YA67-4"},
        {"path": "knowledge/sources/ionescu-1981-improved-angular-distribution-analysis-particle-xn.md", "locator": "IO81-21"}
      ]
    },
    {
      "knowledge": "knowledge/projects/sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction.md",
      "summary": "把P-ADO真实表格null profile接入现有项目的证据缺口，明确其反证对象是跨reaction共享alignment而非P-ADO本身。",
      "anchor": "Day28 added [[pado-shared-alignment-null-profile]]",
      "sources": [
        {"path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md", "locator": "Z83-11"},
        {"path": "knowledge/sources/ionescu-1981-improved-angular-distribution-analysis-particle-xn.md", "locator": "IO81-21"}
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "更新P-ADO开放问题，加入共享alignment null的真实表格反证和137Ba数据访问边界。",
      "anchor": "在用户的 P-ADO / NST mixing-ratio extraction 中",
      "sources": [
        {"path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md", "locator": "Z83-11"},
        {"path": "knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md", "locator": "SO20-D28-1"}
      ]
    },
    {
      "knowledge": "knowledge/synthesis/octupole-and-rare-electromagnetic-decay.md",
      "summary": "把137Ba Mendeley访问复核更新到八极/稀有衰变综合页，明确无event/response/Cov时不能做L4重析。",
      "anchor": "The source-dependence boundary is claim-specific",
      "sources": [
        {"path": "knowledge/sources/soderstrom-2020-137ba-competitive-gamma.md", "locator": "SO20-D28-1"}
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "细化131Xe低自旋小解与794.8-keV宇称版本差异的待核问题，不把局部闭合改成全问题resolved。",
      "anchor": "131Xe` 低自旋δ小解的全局唯一性与794.8-keV线的宇称版本差异如何闭合",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-2"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-2"}
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "建立Day28 L3对象与分支问题入口，标明旧零对照强断言已撤回。",
      "anchor": "Day28 当前L3：131Xe低自旋对象身份与δ分支",
      "sources": [
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-3"},
        {"path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md", "locator": "BNK20-D28-1"}
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "summary": "把全库复习入口接入现有知识健康面板，保持overview只做治理导航。",
      "anchor": "全库复习和研究选题入口",
      "sources": [
        {"path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md", "locator": "GA13-1"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-1"}
      ]
    },
    {
      "knowledge": "knowledge/synthesis/wiki-full-library-map-20261030.md",
      "summary": "建立全库温故知新地图、研究主线、论文候选和安全整理边界；课程学分与科学事实仍回到原始source。",
      "anchor": "2026-10-30 规模快照",
      "sources": [
        {"path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md", "locator": "GA13-1"},
        {"path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md", "locator": "C23-D28-1"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/32s-vermeer-1982-source-access-boundary.md",
      "summary": "记录 Vermeer 1982 `32S` 四极矩比较源的 DOI/PII 身份和无正文访问边界；未取得旧测量值，不裁决相容性。",
      "anchor": "## Evidence Boundary",
      "sources": [
        {"path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md", "locator": "DD-20261031-32S-29"}
      ]
    },
    {
      "knowledge": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
      "summary": "新增 Vermeer 1982 比较源访问边界的原子 claim；保留 `needs_review`，不把出版社元数据当科学结果。",
      "anchor": "DD-20261031-32S-29",
      "sources": [
        {"path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md", "locator": "DD-20261031-32S-29"}
      ]
    },
    {
      "knowledge": "knowledge/projects/100sn-gamow-teller-independent-evidence.md",
      "summary": "新增 Day28 Claim-Safety Boundary，降级历史相空间对账为条件敏感度练习，保留两条独立衰变链和原始 locator。",
      "anchor": "Day28 Claim-Safety Boundary",
      "sources": [
        {"path": "knowledge/sources/hinke-2010-100sn-decay-spectroscopy.md", "locator": "HK10-D21-R99-1"},
        {"path": "knowledge/sources/lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy.md", "locator": "LB16-D21-R99-1"}
      ]
    },
    {
      "knowledge": "knowledge/research-notes/partner-em-interval-loso-audit.md",
      "summary": "固化135Nd/134Pr/106Ag伙伴带B(E2)误差盒逐自旋留出结果；不拒绝共同尺度，不把中心值模式升级为手征判据。",
      "anchor": "## Provisional Reasoning",
      "sources": [
        {"path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md", "locator": "MU07-1"},
        {"path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md", "locator": "TO07-D24-002"},
        {"path": "knowledge/sources/rather-2014-ag106-transition-rates.md", "locator": "RA14-5"}
      ]
    }
  ]
}
```

## Open questions and belief revision

下一日优先级已交接至 `outputs/learning-daily/prompts/20261031-DAY29-research-design-defense.md`：不重复受阻的1983 IOP/CORE端点；优先追查794.8-keV宇称重指派说明、原始转换记录和同定义BrIcc系数，并按资源情况并行推进 `135Pr` response/Cov、`135Nd/134Pr` producer ledger 和八极 source-page/lineage 审计。若原件能闭合分支，更新指定claim与H1排序；若数据不足，保留两解/readiness边界。

对相邻的 `132Sn/N=82` 壳隙路线已做一次只读温故知新复核，现有页面已经把 `δ₂n`、`Δn(82)`、`E(2+)`、`B(E2)`、transfer spectroscopic factor 和单粒子间距分层；本轮没有发现新的、不重复且能改变判断的输入，结果记录在 `tmp/day28-132sn-shell-gap/verified-no-op.md`，不写 canonical 页面。

### 第四次周考评分表（primed开卷自审，阶段18/24）

0=未完成，1=能复述，2=有界正确但关键输入未核，3=原件与练习可复核，4=独立完整交叉验证。分数是当前产物自审，不是用户成绩、能力证书或课程学分。

| 维度 | 当前证据/未满足项 | 分数 |
|---|---|---|
| 理论与公式 | 完成同母态RE/RM推导、RB67积分率和模型Eγ边界；未回核全部原始方法文献 | 3/4 |
| 原件与身份 | 两PDF哈希、Fig/Table逐态核验，识别近能量异态和宇称版本差异 | 3/4 |
| 误差与响应 | 非线性区间映射、共享ρ/JΣJᵀ和882响应合同已形成；真实jointΣ未到位 | 3/4 |
| 事实/解释/模型分层 | 撤回模型δ当测量、γ软必然无wobbling等旧强句 | 3/4 |
| 反证与独立性 | 同采集依赖、宇称多版本、ENSDF字段边界和Fig.5双交点均已核查；1983原件未核 | 3/4 |
| 最小实验设计 | 完成882逐门/污染/偏振/校准/profiled separation合同；未获真实装置输入，不报beamtime | 3/4 |

### Weekly REFLECT（第四周，持续更新）

第四周的关键不是按现象标签背诵wobbling/chirality，而是让每个模式判断先经过对象身份、辐射成分和来源独立性。此次回读展示了两种常见放大：把同数据再分析当新独立确认，把低δ中心值与模型参数变成排他性机制证明。

本轮启动也暴露了过程不足：先读Wiki后才做回忆，不能再称闭卷；重复计算131Ce既有三组ratio没有增加判断信息。改进是先冻结primed回忆，再用图表追端点，并给程序拒绝近能量异量子态的控制。限定题002覆盖了“先验小根—派生量识别性—版本冲突”三段推理，但由于答案建立在同轮精读上，仍不当作陌生闭卷成绩。14项通过只认证计算合同，绝不升级为物理模式“全绿”。

后续自测必须补一项真正未提前看答案的限定题；继续核原始AD和偏振分支，不靠更多措辞或更多toy脚本抬高自评分。即使问题局部完成，也须重新核时钟、候选池和下一卡，遵守2026-10-31 15:00研究截止。

checkpoint003的推进集中在四个边界：RE/RM共享r和δ；795的宇称解释在多处出现而766级联没有偏振；882小根必须经共同响应剖面；ENSDF历史EKC和理论ICC不能在缺原始表/同定义系数时强行裁决。限定周考题002已完成，但仍按延迟回忆/primed自审处理，六行周考保持18/24，不以worker篇数增加分数。

## L0–L4 state

- L0/L1：主来源原件回核、关联与版本纠错已产生实际增量。
- L2：反向核查旧claim并定量拒绝越界误差/身份断言。
- L3：active；source-to-claim map、exercise、falsifier与最小prospectus已形成阶段资产。
- L4：事件级研究未启动；缺response、共同Σ、逐门计数/事件、880污染和未核原件。已形成882联合响应合同，但`ready_for_joint_fit=false`；出版表算术不冒称实验重分析。
- 科学review：新增claim均needs_review，保留既有review_status及C23-1至7字段；未设置human-reviewed。

## Verification and continuation

H1预检、boundary和EOL清理已实际完成：退出0、路径ok、Bib matched；清理0项。当前定量脚本退出0，11项独立强度控制、14项既有审计控制、882输入合同、P-ADO真实表格profile和ENSDF字段审计均通过。最终快照 `verification-041.json` 记录 writeback `valid=true`、boundary=0、diff=0；全库lint实测退出1：314 errors、433 warnings、5224 info，新增页面不产生error，剩余error来自继承基线。required lint失败阻止push，不修无关schema；Day28内容已完成，但发布状态诚实保留为 `final-not-pushed`。

writeback初次wrapper调用时将两个位置参数顺序写反，失败回执保存在 `verification-initial-call-order-failure-001.json`；已修正并实测 `verification-036.json` 为valid，映射本轮所有实际变化的knowledge页面。本轮新增全库索引、P-ADO研究和工作区审计；499个raw文件逐个登记，未移动任何文件。最近boundary/diff均退出0；科学检查与发布检查分别保留，不用局部通过掩盖全库失败。

最终开放研究回执为 `outputs/literature-acquisition/20261031-open-research-receipt.json`，状态为 `completed-final-not-pushed`；下一日 canonical 交接为 `outputs/learning-daily/prompts/20261031-DAY29-research-design-defense.md`，run 目录中的 `prompt-day29.md` 仅为 provenance copy。Day29 必须保持自身课程 credit，允许无上限自主派发 subagents、自动路由适用 skills，并在实际平台并发受限时启动新的 `/workspace/wiki` 内 Codex session；仍须遵守来源、raw、L4、lint 和 Git 安全边界。
