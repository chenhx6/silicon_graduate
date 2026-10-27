---
type: daily-learning
graph-excluded: true
created: 2026-10-26
updated: 2026-10-27
---

# Day24：手征伙伴带与133Ce附属分析（进行中）

## Run state

- run_id: 2026-10-26-day-24-01
- run_date: 2026-10-26
- day_index: 24
- session_id: 01a177ac-521f-7212-9312-ba967400db98
- resume_command: `codex resume 01a177ac-521f-7212-9312-ba967400db98 -C /workspace/wiki -s danger-full-access -a never`
- completed_day_indices: [24]
- partial_day_indices: [25]
- status: closeout-deliverables-complete (formal result in final-session-receipt-24.json)
- hard_deadline: 2026-10-27T15:00:00+08:00
- checkpoint_at: 2026-10-27T15:08:09.490712+08:00
- research_stopped_at: 2026-10-27T15:00:00+08:00（closeout提醒实际观察于15:01:38）
- next_day_index: 25（本卡验收目标；课程状态只在交付发布及原runner正式验收后推进）
- Day 24 card audit: complete
- closeout_event_id: `closeout`
- closeout_window: 2026-10-27 15:00–16:00 Asia/Shanghai

本run身份/截止来自实际`20261026-DAY24-chirality-vibration-static-partner-bands-run-01/run.json`，不是准备prompt的run-24。checkpoint001入口时原receipt尚未写入session字段，先以执行环境记录；本轮已核原run.json现在session_id与当前环境相同。未创建新session/run/deadline；本卡只计一次，课程状态由原runner验收及发布门控制。

先核Day23的四份实际receipt：`run.json` completed [23]/partial[24]；`card-credit-23.json` formal[23]、累计23/next24且no-double-credit；`final-session-receipt-23.json` completed；`task-publication-receipt-23.json` published、postcommit reconciliation passed。其SHA/路径列在本run 本地忽略的`session-receipt-001.json`，未根据准备文猜测。原15:00字段保留，显式override的effective deadline17:00只属于Day23；Day21/22信用、人审及撤回不动。

### Day 24 card completion audit

| Day24 matrix deliverable | Evidence/artifact及边界 | status |
|---|---|---|
| 回忆三根角动量、左右手与振动/静态区别 | 本run `recall-001.md`；[[frauendorf-meng-1997-tilted-rotation-chirality]] FM97-D24-001；[[135nd-chiral-partner-resolved-evidence-map]] 模型有效域及所用输入；Wiki primed非盲测 | complete |
| 三条指定主线原读 | [[nuclear-chirality]]；[[frauendorf-meng-1997-tilted-rotation-chirality]] FM97-D24-002；[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24-001；读源不等producer复现 | complete |
| 能量、B(M1)/B(E2)、geometry及g逐伙伴练习 | [[135nd-chiral-partner-resolved-evidence-map]] 伙伴带观测账本；MU07-D24-001；g保持unknown，实验派生B与模型几何分层，不补Cov | complete |
| crossing/configuration change/γ-softness/band mixing检查 | [[135nd-chiral-partner-resolved-evidence-map]] 四条竞争路线与可证伪输入；[[tonev-2007-134pr-dynamic-chirality]] TO07-D24-009及TO07-D24-010；未声称完成四套135Nd替代fit | complete |
| 实验/TAC-RPA/推断分层图与定量练习交付 | [[135nd-chiral-partner-resolved-evidence-map]] 近似阶次练习：等强来自什么；[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24-002；近似练习非实核拟合 | complete |

本卡交付完成不等于手征争议终结或真实L4输入齐备。Day25仅无学分preview，partial[25]；Day26未打开。133Ce作为重要持续研究补充，不以摄入/译稿或本卡完成宣告结项。

## Candidate pool and selection

015–017后的候选池已重建（candidate-pool-018.json）：Day24主槽的可得anchor/伙伴矩阵/有限量子与EM输出合同已到可供closeout审计的知识里程碑；实际normalizer/producer/完整核仍缺，已核入口不空转。133Ce当前所选独立静态矩槽在既有知识上verified-no-op，其余mask/582reference/实际λ输入仍被数据阻。北京时间2026-10-26T21:59:58.574368+08:00尚余1020.0分钟≥120，因此只进入下一未完成卡Day25的无学分preview：Petrache134Pr、Lv135Nd、136Nd primary的三核对照。先前未开preview的记录是历史，当前partial=[24,25]；Day24仍不先授分，Day25永不在本run列completed或越过next24，不开Day26。

|候选|输入/信息增益|本轮决定|
|---|---|---|
|主槽：135Nd原件与谐振/临界模型合同|FM97/MU07原件可读；已有预习缺一张清晰的正式owner map|优先完成；从预习实际缺口接续，不机械重做库存脚本|
|重要附属：133Ce共同采集/角响应|两论文描述可核，actual mask未交付；可解析finitegate条件|主卡高价值工作后执行一项有边界推导|
|133Ce582 out/out分母|现有ledger不能确认，817.7仅能差|deferred；不逆造线、不反复计算同一缺口|
|GAMPN/ASYMO/PROBMO实际输入|版本/header/λ零点/signedEM仍缺|deferred；不运行114隔离producer，不凭ħω重造input|
|Day25下一卡|已检查matrix；当前主卡仍有非谐量子化和独立实验反证路线|仅课程入口检查，未开科学preview；只准Day25无学分预习，不开Day26|

## Sources and evidence

069/073：[[nndc-2011-133ce-low-level-reference-records]]实际adopted/reaction/IAEA records，当前服务2011版本与不同fixedreaction值分开，073verified-no-op；新增评估不是新实验，IT/Cov/absoluteanchor循环/unplaced lines边界保留。071/074：[[butler-1975-la129-la131-rd-lifetimes]]真实4页RD primary，τ/feeding/velocity/La B/core定标/模型敏感性全图表核，PartII重复不计独立；075短审进行。

064/066/067/root068：[[gizon-1974-deformed-states-cerium-neodymium]]完整22p actualprimary，分工方法/135Ce、133Ce/δ、Nd/讨论并全图表核；root另复核Table4原图。GZ74-D24-001–016/WK22-44写回历史zero/observedline与edge、I55/partialalignment/roughδ/feeding、低1qp与高3qp边界。读取误OCR55°/年代和内部顺text误配强度均用原图纠正，未把错误数字写canonical。067正式报告待最终保存、070写回复审进行；069独立公开评估zero检索进行，不先写adopted值。

059/060/061：[[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]]真PartII25页分工完整原读，root全文text/关键visual，MTVII75-D24-001–015及WK22-43保存目标/邻芯定标、原表失配与Ce历史谱、PES推断限制。062另原读[[hamamoto-2011-selection-rule-chiral-geometry]]全12physical页，撤回旧D19-1过强充要/压制/实测γ认证，原行保audit062；063科学verified-no-op、历史引言措辞已改。064真Gizon1974 primary已取得，仅entry，尚不称全文；下一原读要核历史isomer/ground未定与反应/节点。

054/055/058：[[meyer-ter-vehn-1975-triaxial-rotor-particle-model]] 真30页PartI由方法/应用分工完整原读，root方法连续文本及关键visual；058独立source self-audit未发现必改项。MTV75-D24-001–012/WK22-42固化single-j等谱、共同零点、qp/qh近似、相对EM符号和shape/MoI联合敏感。057另取得真25页PartII，入口读非全读；059/060/061按A135、general/A190、discussion分区续学，未先写实验结论。

052：[[nolan-1983-ce130-high-spin-moment-inertia]] BR85Ref63真primary5页/4图，worker完整原读/visual，root全部text及2–4visual，再BR85p74 freshvisual。NO83-D24-001–007固化valleywidth Jband、samecampaign/differentselection/20%污染/原最高线顺序与自旋边界；primaryjustabove50与ε.25rigidreference52、BR85literaldiscrete45不同层。初稿“effectivemoment”泛称改为确切Jband，保更正过程不抹实际支持。Ref77仅metadata、body/campaign未核。

046/048/049/050：[[bengtsson-ragnarsson-1985-rotational-bands-particle-hole]]真69页原件，046仅entry；048方法1–16全部主线/freshvisual，04917–46全应用，root05047–69离散/130Ce/总结/参考，合并32图4表33式。root另methods关键文本/原Table1/2/3/Fig19及完整assigned11图/Table4视觉核。BR85-D24-001–014/WK22-41与三源REFLECT入蓝本/主map/matrix，原参数表与actualjob分开，引用实验不算本轮新采集。053短审methods无实质错，ω=0/ℏ²及very-lowspin措辞已修；051只O20/Ot/半径平方记号微调，source核心no-op。

043/044：[[leander-larsson-1975-potential-energy-surfaces-n-equals-z]]原件21页已分工主线/Appendix/全部Figs1–12及Tables1/2阅读，root原PDF4/7/10/19/20与判读段核，LL75-D24-001–012保存真实历史定义和局限。A2/A3是general angular CG-reduced，A8/A9却忽略γ且同ν对角QLike；不把任一个范围泛化成全三轴/径向库。原扫描Eq8第二系数与Fig12框残损不猜填。051正在短审新写回，不另算独立原实验。

032/036新用户原件：[[larsson-1978-nuclear-core-quasiparticle-coupling]]，35页/SHA108c29…d77eb；032读方法/附录PDF1–11/31–34，036读应用/总结11–31并核Figs3–10/Tables2–5，合并覆盖全部科学主线、Figs1–10/Tables1–5/Eqs1–22/A1–16。root方法全文及应用关键文本/视觉/参考核，非数值复现或逐篇重核所引实验。LLR78-D24-001–020分历史接口、定标/失败、任务算术及037方向推导。全文自动text与人工原读scope严格分开。

037独立review及root原A2回核使标准3j/Hermitian前提下方向代数闭合；M1/E2反向共同phase消、real ratio不额外翻号，B初态统计权重仍不同。037报告/receipt在容量瞬时失败前已保存，root实际读档后采用，不将model final错误当作未保存产物或另建run；未启动重复producer。038核六矩阵bar/index、BCS/惯量/real核及Table1算术无实质错误，仅把原between的literal范围改为favoured/unfavoured态之间。

031：[[chen-2018-four-j-shell-prm-136nd]]官方v1实际15页/6图/TableI/Eqs1–9已worker完整读，root全文文本主线/参考及PDF6/8/10视觉回核。CQ18-D25P-001–006保存量子good-I能力、D5六qp/参数、谱定标、EM输出和失败边界；实际Fig3只给带内M1/E2，无20+_D5C两E2的out/in。未以框架可算冒已发表prediction，thesis.21979未获得模型数值检验。030 Kuti103Rh既有source为verified-no-op，三核project仅新增MχD标签不自动证多shape的比较量词。

preview028/029：实际吕thesis的Ch4/Ch5/geometry/Table5.1有新可用输入。worker scoped读66–71/76–81/93–95/97/102–103及几何59–60/153–154；root方法文本/相关Table/关键视觉及Fig5.6旋转crop回核。TH19-D25P-001–005保存3母态14打印出口、373.7归一、名义39houses/四rings/active-mask未知与TDRclock区别，不冒164页全读/新独立campaign。029 HW Eq14同I scalar扩展由root读连续推导/代码并重跑exit0；capacity瞬时失败发生在已保存结果之后，续接只保存receipt，原过程与root验证分列。

preview025：[[heyde-wood-2011-shape-coexistence-review]]原55页Review本轮为明确scoped连续原读PDF7–13/27–30/36–44，worker17页visual；root关键文本及Eq14/fingerprints/TableVI visual（13/36/41），未冒55页重读。HW11-D25P-001–006校准定义、E0半径组合与direct/indirect/hints，原HW11-D21-1未定位百分比/固定V/唯一反演及必须E0+Coulex认证在原ID撤回；oldline/概念段完整保存withdrawal-audit-025.json。原HW11-4 needs_review:false保持，旧人审范围不动，原E0/EM积极约束不撤。

026重叠审查显示核心loop不变量/同四B反例已在[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-004/005及其末段，主结论verified-no-op而非新定理。只给022增加actualΔI2E2无M1/本边δ、其它ΔI1单边δ不普遍补E2loop的操作scope；未赋134Pr实际phase。027精确JYX bitstream一次授权HTTP1.1重试仍emptyreply/body0，原失败与partial状态保留，不从metadata填136Nd全表。

preview021–024：Tonev2007目标identity已核但body0（三新路后停），不建τ/B表。022仅PE06原空间数学扩展，root读script并重跑exit0；023独立审查修两项量词：LV19独立于MU07、不独立计同期PE18 campaign，clock允许jointfit/sharedCov、无clock降级限定本相对γ方法。thesis PDF66/印65的同experiment两核/commonTDRpool已有DD-20260910-136ND-01/02，root/workerfresh窄读visual，不冒重读164页。

024 MU08原6页/5图/两表/三式由worker全核，root读报告/既有canonical MU08-D18-5/6/7并核PE18图身份；旧负Band1/2→D4/D3的science判verified-no-op。新设计句只写三核project：旧EM挑战互为pair的两旧主带，不给后来D3-C/D4-C或正D5代寿命/反证。原source不为填delta改页，人审/撤回保持。

Day25无学分preview018–020：Lv2019原v1 10页/6图/TableI4页由worker全读/visual，root全文text/PDF2/3/5/7–9关键visual；Petrache2018原cover+六页正文由worker全文/六图，root主线/关键TableI及artifact身份；Petrache2006 VoR四页root全文/visual2–4。新增LV19-D25P-001–004、PE18-D25P-001–004、PE06-D25P-001/002，支撑[[chirality-shape-coexistence-companion-matrix]]三核逐family/companion矩阵。读本与共享dataset/模型输入分层，不把同论文副本算独立实验。

两个实质source纠正：PE18旧supplementary字段其实同正文reprint，原声称读到Bands1–3 δ/absoluteB补充表无实际文件支持，已在active source隔离并撤回；附本hash首段acb9错为实际cab9，修metadata不改raw。旧PE18-D19-2的D5/C简化配置不符原TableI，已修六qp原轨道内容，D5真实ratio支持保留。LV19同段589/649目标D2/D3冲突、D2 Ei2588.3与三条2558.3闭合条件也已回写，未静默改原表或否定总体正family。

checkpoint015/016：CH16官方archive两条路线transport-incomplete，完整主TeX member哈希一致；PartII完整official archive仅TeX+四图，root另安全逐regular member/hash核验、无执行。CH16-D24-013/WU18-D24-011只认证这个scopedreadiness，不宣称全网无producer。[[chen-2017-128cs-angular-momentum-projection-chirality]]既有raw本轮SHA d176ae…76c6相符，12页主线/4图/Eqs1–11由worker/root回读；root视觉PDF3–7覆盖四图/metric/角字典/EM比较。CH17-D24-001–008区分good-I/PNP、有限四κ/K空间、g=N^1/2f、coherent RME应有结构与未打印actualEMkernel，保GR06数据复用/高spin E2失败。

133Ce附属017为有依据verified-no-op：worker定向IB98关键原页/visual/hash，root核现有source IB98-D19-8/9及IB98-D20-R146-1/2，与既有162keV/9/2−/88ns/absQs.92(10)/g−.189(7)合同相符；不新增static/source科学更改、不搬数值到133Ce。相关clock/state ledger仅审计副本，知识仍在[[ionescu-bujor-1998-static-moments-129-131ce]]，不把outputs当新知识源。

checkpoint014：[[wu-2018-two-dimensional-collective-electromagnetic-transitions]]实际官方arXiv1809.04418v2，17页/4图/Eqs1–21；worker/root各读全文，root视觉PDF4–7/9–12覆盖4图/局部率/积分/输入及literal Eq2遗漏。276035bytes/SHA7d7c…93dcb，Crossref核PRC98,064302(2018)，九月v2与十二月VoR分开（VoR未核）。WU18-D24-001–010固化局部rate averaging/only-intraband、cranking/J角区别、PRM交错失败和未闭合mass版本；不认领实际作者producer或实核EM预测。

checkpoint010–013：OL02同一源参数的全局分支证书/阈quartic控制、CH13 metric三路synthetic组件已root读推导/代码并重跑exit0，详Theory。[[chen-2016-two-dimensional-collective-chiral-wobbling]]官方arXiv1609.06967v2实际30页/12图，worker全文/全部visual，root全文text主线及PDF4/6/8/14/16/19/21/24/25关键visual；body6543288bytes/SHA158efc…332be。Crossref核PRC94,044301，2016v2与2022typeset分开，VoR未核。CH16-D24-001–012保实际高频支持、低spin失败、改边界与极点/域输入边界。013独立review容量瞬时失败后原task续接保存，没有新run/session或降级编造结果。

checkpoint009：[[chen-2013-collective-hamiltonian-chiral-modes]]官方arXiv1212.2313v2实际16页全文主线由worker/root各读；root视觉PDF4–7/9–14覆盖8图和关键算符/质量/边界。SHA bef618…342a2c、HTTP200/987932bytes；Crossref/INSPIRE核身份，PDF1typeset2018与官方v2/2013出版年分别记录，未核VoR。CH13-D24-001–009新模型层进入主map；未运行作者producer，未给135Nd/133Ce补数字。

134Pr独立寿命路线核准Tonev2006 PRL96,052501，但actualbody0页/0图/0表。新APS401、HAL仅external APS、Padua OAI两标识idDoesNotExist，已停该端点。已有Petrache2006的Tonev Ref9/branch Ref11依赖原件定向核验与既有PE06-R45相同，无新science delta；不另造source表/B值或把旧summary计独立实验。

checkpoint006–008：A13两实际版本及AW13正宇称family/端点原件核验已进canonical，WK22-38分开formalism/参数/actualproducer引用。[[olbratowski-2002-critical-frequency-preprint]]原2002v1四页全文/Figs1–6/Eqs1–7由worker与root主线/visual双读，另独立review25项有界控制；官方arXiv历史/currentPDF验证没有新版本正文。2004四作者VoR、Larsson1978方法正文和Starosta2001所需定义正文仍未得，不用书目/摘要代正文。

A13-D24-001–004保8页accepted/5页reprint、带号/37.2keV零点及模型边界；779keV的A2/A0不确定度在两版本均为±.032，原Wiki的−.7312(32)已按双visual纠正为−(.7312±.032)，不改原reviewflags。AW13-D24-001–004保Band2寿命family与Band3 61.8keV头，表图端点和近能γ不强并。

checkpoint005：root逐页视觉Li2004原3页；独立worker读Singh2016原11页/全部关键visual，root抽PDF5 Table1；WK22worker相关连续段/图表与root抽Tables5.1/5.2。新增LI04-D24-001/002、SI16-D24-001/002、WK22-36/37，把既有131Ce寿命按节点/clock/类型接为133Ce方法合同；原用户flags保持。三个worker只写独占prefix；root统一写canonical。Qi09另经独立review验证原117控制范围、图框/裁切/graphicsstate，未发现需修正问题，非新实验认证。

checkpoint004：GR06原4页主线/visual PDF2–4全部六图；GR18原5页主线/visual PDF2/3/4的四图/两表/关键式。两raw SHA分别654527…1c9/c71ec5…fbf2核相符，未重拟DSAM/TDPAD或更改原g。新增GR06-D24-001/002、GR18-D24-001/002，保原signed/RMS/Gram、localfield与人审边界。

checkpoint003：[[qi-2009-135nd-particle-rotor-chirality]]原v1实际16页主线及五图回读，官方arXiv作者archive HTTP200；纯读paper.tex/fig5.eps，无TeX/PostScript执行。QI09-D24-001–003补半整数网格、同表示匹配及版本/有限模型窗口。该稿Ref21为AL11的v1，本轮AL11实际读v2，未混成同版本输入。

checkpoint002：[[almehed-2011-chiral-vibrations-a135]]公开arXivv2实际18页主线文本回读，fresh visual PDF3–18 contact sheet、PDF5/7/14/15/16单页深核。SHA `becba964421bb8860fa657865071df117622a492a2bbb2b23d661d235296f29b`；原件在既有tmp staging，raw归档槽不存在、未写raw、VoR未核。AL11-D24-001–005新增共同ω比较、有限窗口、mode/零模身份、BK/physicalE2及局部conditioning边界；邻核表值不补135Nd参数。

- [[frauendorf-meng-1997-tilted-rotation-chirality]]：期刊17页全文文本主线；fresh visual PDF2/3/5–10/12–16，覆盖Figs1–9及主要公式。raw SHA `9dc81b3147a786189dd0c2f31d79a56e9bb5d83e16fd0c8137bccaf2a43d81e2`。新增FM97-D24-001/002。原human-reviewed claims保持，本轮新增仍needs_review:true。
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]：原四页全文，fresh visual PDF2/3/4的TableI/Figs1–4/Eqs1–3与非谐讨论。SHA `9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425`。MU07-D24-001/002分开实验相近与谐振共同TAC曲线。
- Crossref两个DOI端点均HTTP200，题名/期刊/年份身份核到，记录在`external-metadata-001.json`。它们是元数据交叉核验，不是新实验或全文独立票。
- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] PDF54–61方法连续段及PDF59/61fresh visual；[[ding-2021-131ba-133ce-signature-splitting]]稿本PDF2定向回读、两raw哈希核到。WK22-35为finitegate数学边界；Ding既有正式版对照本轮不冒称重读全文。
- MU07同一实验的TableI/图/作者TeX和IAEA adopted不重复计票。2003纲图与2007DSAM有各自采集贡献，但共享assignment/branch的具体ledger仍缺。

## Theory/analysis exercise

099在当前Tonev2007原件内核对模型比较的单位/参数/选态合同：谱学Js:Ji:Jl=1.52:3.55:1（physicalPDF11），几何演示另为1:4:1/γ30°（physicalPDF17），IBFFM依当前数据调整H/EM参数；PDF23由曲率提出I>16超2qp空间并说明I14/I15赋名歧义。分别为模型输入、作者配置解释和定标依赖，不是实测几何或独立holdout。见TO07-D24-009/010及主map“134Pr原件对counter-model比较的控制”。

069 ENSDF line-level读取固定GS 0/1/2+/97(4)min与9/2−37.2(7)/5.1(3)h；reaction37.3(6)/4.9(4) held-fixed不平均。072原133Ce primary再确认τ76(3)ps→T1/2=52.7(2.1)ps转换，避免数据库T列冒meanτ。071 Butler E2率式条件算术qγ=.942/.980/.981/1.009只是缺BR/ICC诊断，不能重演actual producer；同文La τ与B正常值、core .33/.28定标、β/A2/3脚注冲突和Fig2 b4–7模型范围保留。

068真实印数ledger：Nd两核7个能级加法核对残差0，仅印数算术不当独立支持/统计检验。135Nd crossover Table560.3/正文560.5/图560.7保literal；135Ce两路径差1.1keV不强修。133Ce1163.6−170=993.6≈994、1163.6≈1164给1975注释数字出处；现代暂定offset37.2可闭合592.1/1200.8/608.7单节点边，但不扩wholeBand4。old817.3observedunassigned不与modern817.7energy-only混合。

062的真实source-input crosscheck：HM11 p4 gR.5与p9 Fig2caption55/130分开，固定h11/2投影所得exchange系数平方比78000.51/80.03只是算符系数，不是实际B或硬门。PartII原Table2一列率80%不补数、Table3b仅2/5理论δ在原字面范围，不给统计排除。Table5 La实测与模型比值保真实中央差异和定标依赖，不能迁Ce。

052按primary原W=8ℏ²/Jband^(2)与BR85名义比较尺度J52/45，root Fraction核对应W153.85/177.78keV、差23.93keV；这是source-formula尺度，不是重新提取的两个实测width、6channel即显著或resolution/CI。4keV/ch、raw背景与混合cascade合同保，未数字化误差条/curve重拟。

040仅实际四E2的joint log-response合同：R20/R21/D的J行(1,−1,0,0)/(0,0,1,−1)/(−1,1,1,−1)，真实共同normalizer/scale消，逐线gate/加性背景不消；共同幂律效率s下lnD系数−.117320938不能排一般系统学。root读script/run0；未造counts/Cov/CI。041将bareμ/标准M1、完整Q-like/球谐E2及full/reduced字段分类和条件比例列清，不对作者结果盲乘factor；3j核心复用RS88-18。042在明确dimensionful stretch下给五分量与dimensionless length²桥；含r_t²项不等物理E0，完整physical L仍给rank2，root符号脚本run0只核坐标恒等式，不恢复实际库。

032实际模型表练习：LLR78 Table1共享RME20=−100，γ4→ground4软/动态/刚芯127/102/70，ground4→2为−165/−164/−158。同Ii下软/刚B比分别3.29163265与1.09057042，root原Table1视觉/Fraction核；这说明用未定标EM补所选能谱的价值，不是133Ce/135Nd实验差或photoncount/功效。037的有限Hermitian/3j推导关闭一个方向数学点，actual2022单位/算符/phase仍独立未知，不再混成永远方向未核。

033在同一原表追加D5-C21+/7927.1的714.1(.18(4))、1060.7(.8(4))两E2，root新视觉核physicalPDF94/95与Fraction复算R21=.6146810196；R21/R20中心2.796692425无CI/显著性/模式判决。TH19-D25P-006–008将selected3-E2子集与完整库存、不同spin块、22+ Ei8355.1/8355.9的literal矛盾分开，不凑R22或physicalclosure。

035为六题源后理解校核，不是盲测/独立考试或新理论结果：三qp triad、finite static/左右奇量、五种阈值对象、τ差/B近合、sameI/commonω及四替代路线的实际证据层。已核MU07原PDF3/4关键段与现有source locators，当前canonical科学verified-no-op，不为回忆重复改源；独立短审结果另存workers/day24-understanding-review-035。

preview028实际源输入练习：D5-C20+/7543.0的611.4(.21(10))带内E2与1021.2(.6(1))跨D5-18+，root用Fraction复算(.6/.21)(611.4/1021.2)^5=.2197885667。此比消共同τ/373.7参考/E2常数、不需fulltotalBR；仍条件于端点/E2component/可比修正photonresponse，gate/Cov未知，不报CI、absoluteB或modeexclusion。14条出口完整保，不将672.5 mixed行当E2crossover，不把<.01当95%上限。

preview029：同Iπ Hermitian radius T作同U相似变换，与022不同Ii/If的forwardE2不同。含offdiag t后A=(WΔ+δx)/D+iy及mixed-radii差d=(δΔ−4Wx)/D，d²+4absA²=Δ²+4abst²；t0回HW Eq14。δ非零时可相消，δ0不任意相消；完整energy-basis H/T仍不唯一选physicalunmixed配置。无实际Z/R0/186Pb百分比/fit/CI，公式是任务推导不是原作者打印实现。

preview025条件代数：原Eq14为ρ²(E0)=Z²/R0⁴·η(1−η)(Δ⟨r²⟩)²；同实twolevel gap D有η(1−η)=V²/D²，故D和E0只定abs(VΔ⟨r²⟩)组合，半径/密度/多态假设不能省。V是否强mixing还依detuning。TableVI是多核/不同fit量的34–400keV资料，不是普适V门；186Pb532/650能级可定位，与未定位28%/20–35%混合百分比分开，不把review例子当三核新实验。

preview022：源混合矩阵R列(y,ny)，forward E2扩展Q=[[q1,q12],[q12,q2]]、M=RfᵀQRi；real symmetric q12是额外ansatz，不由Hermiticity强制forward两offdiag相同。q12=0的sourceα前向基线复17/18Table值；同parentτ消、scale/一致rephase保，原ratio相等捷径未必保。固定Q的Frobenius/det²/SVD不变，改变q12则值改变；仅两unsigned parentratio无列norm/loop sign，不能恢复SVD/绝对尺度。若mix独立已知+exactratio，可局部离散识别，不作普适连续退化论。全部连续推导/标签/单位/少量控制已进project，不fit新Q/V/CI或判alternative获胜。

Day25preview设计增量：三核matrix把134Pr的model-dependent解混合、135Nd正/负不同EM完整度、136Nd D5 ratio与D3模型几何逐family拆开；最小companion为state/component身份、双方clock+completeBR/ICC/normalizer、冻结输入的竞争预测及可分辨holdout。它是问题设计而非普适模式终判，少某项只降级相关结论，g/τ不成为一切模式必要充分硬门。PE06原2.0(4)与旧R45前向身份复算保持，无重fit新Q比CI；正在022允许off-diagonal E2的有界方法敏感性，未完成前不先认证。

checkpoint016：从投影态定义推Rfi=Σ f_f* Tfi f_i后平方，并说明用g需同步N^−1/2核变换；这是任务推导，源未交付actualEMkernel/参数/phase实现。K图折叠模方与azimuthal先K相干、后sumκ/积分ψ的图不同；不作所有密度都不含phase的普适断言。按标准全Euler范数推P带sinθdθdφ，图只示θ0–90/φ0–180、折叠倍数未给，不以flat图像归一。原Eq7 K0机械双计仅literalproducer边界，未判实际图错。

checkpoint014：原Eqs11–13/15–17为Bbar_i[X]=∫dτ abs(Ψ_i)² B_TAC[X](q)，先局部平方再按单态ρ平均，不含Ψf或跨I/sector kernel。与完整相干RME分开，也不同于将折叠均值角代入非线性B公式。局部θJ/φJ来自J向量，不在所有采样点等于ω的θ/φ。源参数i-axis局部ΔI2 E2限值5/(32π)≈.04973592e²b²只核图平台尺度；不重放集体曲线、不把角度单独当任意M1为零的充分条件。

checkpoint010：固定ω的R和固定I的H各有同球面精确二次能差证书；fixedI低I走反向D再A再aplanar，与原Fig4相符，不把fixedω最低R直接改名全I yrast。ωc零切向二阶曲率仍有正quartic代价，退化circle只在显式改惯量/zero gyro的不同模型出现。72项有界控制/root重跑通过，不叫RPA频率或实核阈值。

checkpoint011：正光滑有限B的Dirichlet合同下，x=∫√(B/B0)dφ使Pauli算符常质量；同φ的flat幅u=B^1/4ψ另有Q_B=(ℏ²/2)[B″/(4B²)−7B′²/(16B³)]。概率密度必须连测度；B、V和域都反射对称才推出本征奇量为0。synthetic B=1+.7φ²/V=18(φ²−.85²)²三路h²收敛，4095内点路间差≤4.12e−7而共同参考截断差约8.9e−6；16383点gap≈.195626391只属无量纲参考。packet两态相干互换、不等永久单手定态；large/singularB不普适推出硬墙。知识公式/误差对象已在主map，不只留worker报告。

checkpoint012/013：2DCH保质量交叉项、detB测度和周期域；1D对照也改periodic。正finite ph gaps/实tensor下Gram仅保证PSD，strict rank2需另检；有限gap极点φ响应为0。条件regular pole下θ-even w^−1/4单基可L²归一却有发散kineticform；actual端点/基组合/截断未得，不据此判作者谱错。源公式是否显式ℏ²与natural-unit约定另留literal，未自修input。

checkpoint009：CH13中Pauli一维算符与√B测度/B^−1/4基/盒壁配套；rotation域mass处方Ω=0不删除集体动能，故不等最终ΔE=0。对称B/V的非简并偶/奇φ态对φ奇量的期望为0、左右packet有限gap下相对phase演化，为标记清楚的本任务推断；不把unitary φ反射改成核空间宇称或真实核antiunitary C标签。原Fig8的PRM gap重开而1D不重开，直接限制高spin单调静态图像。另独立worker开展测度/坐标/离散收敛组件，结果未到前不先认证。

checkpoint007/008：OL02源参数在固定gyro/常惯量均匀转动合同下给ℏωc=.514639046MeV、连续Icrit=15.9538104ℏ；新planar分支另阈值1.282266726MeV。Fig6扣的是I²/(2𝒥m)，chiral经典水平线约−1.791583636MeV，不是Routhian或实验劈裂。独立给定ω/给定I约束曲率核验不冒实际RPA谱。A13 TableI头能与原图整数链在isomer参考下对应，+37.2仅条件ground转换；AW13整数/表图闭环22.3keV残差保留，不用舍入强闭。

checkpoint005：Li整数γ链在声明零点下作rounded-sum ledger，未冒精确Ex；Singh四present有限/三limits与Ref31/32旧列分开。133Ce蓝本新增三母态九observed边：832.0/1409.8/1809.1的τ必须绑定母态，不能借终态或131Ce。37.2在WK22为原边能差派生，817.7仍energy-only未观测；982.0是actualE2边，但原ratio reference producer仍未得。

checkpoint004：128Cs逐态companion表写入135Nd evidence map。GR06 yrast(18)+/.82ps/930→(16)+，与GR18采用9+、56ns half-life/g分列。条件clock练习（`cs128-clock-state-design-004.json`）：56/ln2=80.7909ns，mean比≈98525.5；只在假定高spin同参考omegaL时，两mean窗口的rank2相位≈10.0989和1.025e−4rad。它是设计尺度，不是高spin g/actualresponse/beamtime。

checkpoint003：`system/scripts/day24_qi09_projection_grid.py`识别690数据标记/36系列，K=.5… I的最大图坐标偏差.0669K；原PDF全部690颜色与顺序匹配、用三个图框anchor定affine后最大位置差.00250pt。117representation/rounding/轴交换控制通过；正K纵坐标和.9915–1.0041仅与声明绘图rounding模型的1相容，非新的物理概率CI或producer归一认证。

checkpoint002：[[135nd-chiral-partner-resolved-evidence-map]]新增same-I能隙与common-ω Routhian的Legendre关系/解析抛物线例、136Pm有限窗口原表和φ0 quadrupole Jacobian。脚本从实际PDF5解析55行、仅对30个φ0行反演；Cartesiantensor旋转微分、极限与原表identity共157控制通过，condition number2.712–6.678，最大微分残差1.34e−10。只核dimensionless局部坐标，无actualRPA求解、物理振幅/CI/阈值。

主卡：map写出F(q)=a+bq+cq²、v=ℏ/(2𝓜Ω)的谐振本征期望：F00=a+cv，F11=a+3cv，F10=b√v。线性截断给共同对角基线，二阶曲率可破等；Ω→0须检查小振幅失效。它说明近似阶次，未把内禀对角量当跨spin实验B或给actual135Nd临界参数。

附属：[[133ce-thesis-analysis-blueprint]]“有限all-detector门的接受度练习”推导真实联合响应积分与方位平均条件核。equalweight point-ring的G2/G4：8布局−1/8、−1/64；13布局−11/52、31/416，均非4π消去。`system/scripts/day24_finite_gate_acceptance.py`两路线/极限等32控制通过，输出`finite-gate-acceptance-001.json`。chosen positive kernel两ratio仅是synthetic示例，不是AD/DCO/Rac实测或原producer预测。

## Counter-evidence and missing companion observables

WU18的带内率有平滑趋势支持，但明确漏PRM M1/ΔI1 E2奇偶交错；source归因于I非good。背景中的interband E2规则未由该新计算检验，不能拿四sector相近带内曲线补跨sector cancellation或signedδ。周期继承明确，具体Ω惯量版本未明，低spin谱是否修复继续unknown。

CH13-D24-008是源内模型反例：高频second chiral vibration被1D方案遗漏；固定γ/单配置不能排除γ软度、crossing或组态混合。其same-ω谱不等same-I实测gap，源无新的τ/δ/g或完整EM率表。Tonev目标正文未得，缺口仅阻该原实验数值审计；主线仍有量子化/坐标和二维方法可推进，不是全日hard blocker。

FM97 Fig7抑制属于本模型；其134Pr高spin未见links同时有弱布居限制。MU07认可135Nd实验正支持，也承认带间E2低估、M1趋势差异、近transition TAC+RPA breakdown与非谐B差异；RPA含shape自由度不等实核γ刚性认证。

Map逐项给crossing、configuration change、γ-softness和bandmixing需哪些额外预报/holdout。尚缺两partner g、完整signed EM与projector、逐线parent/Jf/component/normalizer/Cov。133Ce尚缺actual run/mask/45°event/sorting/同门参考counts，Eq4.6“all”不能自动代替完整响应积分。不能把这些科学partial当用户待办或技术hard P0。

## Knowledge Impact and Learning Decision

preview018–020：`revises`PE18假SI/错误C配置的source记录；`limits`LV19局部端点/Ex表的直接唯一重建，保总体正宇称及负family绝对EM支持。`supports`按pair/segment/source设计companion，不把D5实验与D3几何拼接、或把不同采集/同一旧τ引用误当多独立实验。三核比较是Day25预习的可复用新综合，formalcredit0；不因这些错误撤销其它真实支持链。

014：`supports`集体概率对局部带内率的涨落修正；`limits`把“有wavefunction/B曲线”当成完整coherent跨带算符/phase。该方法分层也接回133Ce蓝本：不能代其实际GAMPN→PROBMO输入/EM合同，不宣称RS88/WK22也是rate-average，负parityλ/582reference等缺口继续保留。

010–013：`supports`固定模型全局变分与有限量子化的明确合同，`limits`固定ω/I混用、只按波函数图形/归一认证几何或求解域。CH16实际PRM高spin比较与晚期gap重开部分推进CH13遗漏坐标；低spin质量失败、假定1.10MeV Ω、改periodic边界及晚期LW解释一起保留，不称增维排他修复所有second-vibration。该方法链没有新增任何135Nd/133Ce实验。

checkpoint004：`supports`独立磁矩伴随量可补EM链，`limits`只按核名/反应名把不同spin/clock/run合并。GR18九条下游γ共同读取isomer，不能当九个level分别测g；Orsay/Stony与GR06数据采集不同，assignment/模型物理输入仍可共享。9+模型近planar不否定全带高spin，135Nd两partner g仍unknown。

checkpoint003：`supports`作者图的positive half-integer采样身份；旧“未得网格”缺口已缩小。`limits`原文P(K0)叙述到literal离散本征投影的外推；fold/bin/插值、相位/完整波函数仍缺。固定参数PRM的有限手征窗口保为模型支持，不把76keV当测量或能谱定标后的比较当独立无参预测。

checkpoint002三来源REFLECT：FM97固定shape模型、MU07本核实验和AL11邻核方法链分开；`limits`高spin无条件更静态/同I gap直接当RPA能量/最低ordinal固定模身份的推理；`supports`保留近谐可用域与本核EM正支持。AL1180%pairing和BK tensor不能覆盖MU07核素特定输入或实测charge shape。

`supports`135Nd已有实验手征支持，`limits`共同理论曲线和临界点的过强解释；`limits`finiteallgate的普适精确独立性外推。没有撤销其它核的真实支持链。Pr747 P+.04/δ−.47、813 P−.03/δ−.37、SH26 fixedσ/I=.2条件支持、Au band2原wobbling/band3原SP，以及Li2004/Singh2016等寿命边界沿用Day23校准，未作新数据认证。

## Durable knowledge delta

098原件纠错：Tonev2007源与companion保真实E2账本、模型失败及共享实验；WK22新增WK22-46修正412.4/767.7同母态；两concept/两project同步纠正超出原文的扩写。结构门不认证科学结论，直接原页证据见098三审计。

新增 `knowledge/sources/nndc-2011-133ce-low-level-reference-records.md` 评估记录页与 `knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md` primary页；前者把现代lowzero从Wiki派生升级为可追溯公开record但不冒新实验，后者将PartII La B追溯到真实RD τ/feeding/normalizer并保BR/ICC/Cov缺口。

新增 `knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md` GZ74-D24-001至016，并对133Ce蓝本/WK22/135Nd map/PartII源/index作具体写回：一个历史数字出处由unknown转可追溯，未指认光子线增加实际候选，582分母与整带身份仍missing，角响应/clock迁移边界可复用。

本段新增 `knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md`及实质修订 `knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md`，对应原子MTVII75-D24-001至015、HM11-D24-001至006，写回133Ce蓝本/WK22/135Nd map/Day25matrix/index；旧错误原行在审计保留，canonical给当前有效边界。

新增canonical `knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md`，并将PartI适用域写回133Ce蓝本、WK22、135Nd map及index；原子定位MTV75-D24-001至012分别列在唯一机器块。

052新增canonical `knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md`，并将BR85/133Ce/matrix的Jband对象、primaryassignment与二级概括分清。可复用input与判断不只存在workers。

050新增 `knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md` 原参数/追踪/跨核支持失败合同；蓝本“Ref11原参数与高spin实例”及三源REFLECT有长期可用方法增量，WK22-41不反推actual输入。

047新增canonical `knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md`，并把Ref23由“当时未读”更新为有页域的实际原读/仍缺完整三轴库，回到133Ce蓝本/LLR78/WK22与三核矩阵。输出不是唯一知识副本。

032/036/037实质增量在 `knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md`，以及 `knowledge/projects/133ce-thesis-analysis-blueprint.md` 的“1978原方法的新原件”、WK22-39和主伙伴图的四路线scope。历史body0/旧访问保留，实际方法原件取得不等actualproducer。036一条worker half-life宇称转录经root原图指出、局部放大更正为75Se1/2−；该错误未写入canonical，过程与更正receipt保留。

031新增canonical `knowledge/sources/chen-2018-four-j-shell-prm-136nd.md`及三核project的模型输出/holdout边界。原baseline额外检测的GU22/KU25/RS88三页来自外部已发布资料登记，不是本run科学增量；唯一block明确标作归属核验no-op，对账不改baseline/源页、不把未变外部文件列入本runstage。详情external-change-attribution-031.json。

新增canonical owner：`knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`，保存逐伙伴原打印表、层级矩阵、近似阶次和四条反证设计，回链FM97-D24-001/002、MU07-D24-001/002。`knowledge/projects/133ce-thesis-analysis-blueprint.md`保存finitegate推导、exact moments、假设及下一输入，回链WK22-35。来源原读覆盖和概念反链也作本轮实质更新；outputs不是唯一知识副本。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md",
      "anchor": "近似阶次练习：等强来自什么",
      "summary": "新增逐伙伴实验/模型/推断与四替代解释矩阵、harmonic阶次推导。 checkpoint002补same-I/commonω、有限窗口、模身份、BK/charge tensor、局部Jacobian及三来源REFLECT。 checkpoint003加作者投影网格/nativePDF匹配与模型版本边界。 checkpoint004加128Cs独立DSAM/TDPAD逐态、钟和采集对照。 checkpoint007/008加OL02经典/均场/RPA/量子/实验分层及扣参考能量身份。 checkpoint009加CH13集体量子化/有限gap/测度/边界及second-vibration失败。 010全局分支/阈quartic及改模型退化边界。 011连续metric/概率/packet及三路synthetic收敛，regular/singular域分开。 012/013二维原稿/周期边界/PRM支持和低spin失败、域边界。 014 EM PartII的single-density带内率/相干跨带核边界、交错失败与质量版本；不补实核输入。 015完整主TeX/partialarchive与actualproducer边界。 015完整author-package scoped清单。 016good-I有限space/metric/coherent核推导与几何信息边界，GR06非新实验。；新Larsson1978原件关闭历史方法body缺口，actual2022/实验迁移边界保持。；BR85原参数/追踪与130Ce实际模型比较原读，三源REFLECT保actualjob独立缺口。；054/055完整30页PartI原读并058短审通过：single-j/ph零点/配对/core/轴置换与signedEM合同；多轨道充分条件为任务推广，不填actualCe参数或δ。；PartII原25p比较的目标定标、历史Ce最低态失败、γsoftness/rms/fit与两极限边界。；HM11特殊选择规则不普适迁oddA，旧强认证撤回。；Gizon1974实际primary闭合994/1164数字出处，保历史zero与modern单node-edge候选/整带身份边界；old817.3unassigned不补现代817.7/582分母。；099续当前原件：微观/几何惯量合同、当前数据调参/赋名、I>16的2qp空间边界分开，不计135Nd新增实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-002"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-002"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-001"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-002"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-003"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-004"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-005"
        },
        {
          "path": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
          "locator": "QI09-D24-001"
        },
        {
          "path": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
          "locator": "QI09-D24-002"
        },
        {
          "path": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
          "locator": "QI09-D24-003"
        },
        {
          "path": "knowledge/sources/grodner-2006-128cs-chiral-doublet-lifetimes.md",
          "locator": "GR06-D24-001"
        },
        {
          "path": "knowledge/sources/grodner-2006-128cs-chiral-doublet-lifetimes.md",
          "locator": "GR06-D24-002"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D24-001"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D24-002"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-001"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-002"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-003"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-004"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-005"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-002"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-003"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-005"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-008"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-009"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-010"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-002"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-003"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-005"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-008"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-010"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-011"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-012"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-001"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-002"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-003"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-004"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-005"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-006"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-007"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-008"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-009"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-010"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-013"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-011"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-002"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-003"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-005"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-008"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-009"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-012"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-004"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-005"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-004"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-005"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-012"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-014"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-015"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-001"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-003"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-004"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-002"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-009"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-010"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-013"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-014"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-016"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-009"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-010"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
      "anchor": "Day24原件主线回读：模型范围与未见跃迁的条件",
      "summary": "新增原件主线/关键visual覆盖和模型迁移条件。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "Day24原件主线回读：谐振等强、配对输入与临界区",
      "summary": "拆开共同TAC曲线、RPA不改期望值、配对与非谐有效域。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/nuclear-chirality.md",
      "anchor": "Day24正式研究入口：伙伴分辨与模型有效域",
      "summary": "加入正式研究map导航和模型有效域边界。 增加OL02临界模型域与版本导航。 checkpoint009加CH13集体量子化/有限gap/测度/边界及second-vibration失败。 011连续metric/概率/packet及三路synthetic收敛，regular/singular域分开。 012/013二维原稿/周期边界/PRM支持和低spin失败、域边界。 014 EM PartII的single-density带内率/相干跨带核边界、交错失败与质量版本；不补实核输入。 016good-I有限space/metric/coherent核推导与几何信息边界，GR06非新实验。；098按原件纠错，未闭合输入/模型失败保留，095–097强认证撤回。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-001"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-008"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-010"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-011"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-001"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-003"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-006"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-006"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-003"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-004"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-005"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-006"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/133ce-thesis-analysis-blueprint.md",
      "anchor": "有限all-detector门的接受度练习",
      "summary": "新增有限门联合响应积分与两布局接受度moments的条件推导/32控制。 checkpoint005新逐态寿命参考、九observed边与迁移合同。 checkpoint006–008加A13带号/零点跨版本、AW13 Band2寿命family/表图矛盾与WK程序引文分层。 014 EM PartII的single-density带内率/相干跨带核边界、交错失败与质量版本；不补实核输入。 028真实thesis逐母态/relativeI输入与条件E2比；不补133Ce缺分母。；新Larsson1978原件关闭历史方法body缺口，actual2022/实验迁移边界保持。；041条件M1/E2/单位字典与042指定stretch五分量/physical L/length²恒等式固化，均非actualproducer结果。；Ref23后续实际原读状态已更新，历史未得记录保留，不把轴向对角公式当全库。；BR85原参数/追踪与130Ce实际模型比较原读，三源REFLECT保actualjob独立缺口。；052 Ref63 primary收紧continuum量/最高线/数值与shape推断，不倒填二级概括。；054/055完整30页PartI原读并058短审通过：single-j/ph零点/配对/core/轴置换与signedEM合同；多轨道充分条件为任务推广，不填actualCe参数或δ。；PartII原25p比较的目标定标、历史Ce最低态失败、γsoftness/rms/fit与两极限边界。；Gizon1974实际primary闭合994/1164数字出处，保历史zero与modern单node-edge候选/整带身份边界；old817.3unassigned不补现代817.7/582分母。；实际2011评估固定modern lowzero与寿命版本；Butler La primary关闭PartII Table5测量/取参谱系，不迁Ce。；1997 RDDS primary现提供真实133Ce τ和T1/2定义转换，逐态/branch/Cov边界保。；1998高spin DSAM primary现闭合四条τ/Qt与现代Band映射限制。；080逐态crosswalk确认832/1409.8/1809.1母态无τ，817.7 energy-only，582分母与旧unassigned线未绑定。；079补充1991Pa04精确书目与正文获取缺口，1998Joss独立primary已写；不以metadata替原文。；081新增独立SD primary节点，仍不填τ/Qt/582分母；SD/normal-triaxial/低spin观测链分开。；079新增Hauschild1996多带primary，补高spin配置候选/缺link证据，不新增寿命/582分母。；098按原件纠错，未闭合输入/模型失败保留，095–097强认证撤回。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-35"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-D24-001"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-D24-002"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-D24-001"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-D24-002"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-36"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-37"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-001"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-002"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-003"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-004"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-001"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-002"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-003"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-004"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-38"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-001"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-003"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-006"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-009"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-001"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-005"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-002"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-005"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-006"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-008"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-010"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-012"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-015"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-018"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-020"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-021"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-022"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-023"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-024"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-002"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-003"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-004"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-005"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-008"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-011"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-012"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-001"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-002"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-003"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-004"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-005"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-013"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-001"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-002"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-003"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-005"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-006"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-007"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-004"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-005"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-012"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-014"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-002"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-009"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-010"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-013"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-014"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-016"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-002"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-003"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-004"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-005"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-006"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-001"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-003"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-004"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-005"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-006"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-009"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-010"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-014"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-001"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-002"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-003"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-004"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-005"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-006"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-001"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-002"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-004"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-005"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-008"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-010"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-001"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-002"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-003"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-005"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-006"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-008"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-010"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-001"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-002"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-003"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-004"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-005"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-01"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-02"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-14"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-30"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-31"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-33"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-34"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-46"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
      "anchor": "WK22-35",
      "summary": "补原Eq4.6经验校准与finiteacceptance非4π的任务边界。 另增九边/derived节点与higher-spin coverage相对modelspace边界。 WK22-38分开程序、方法和参数参考；actualproducer未恢复。；新Larsson1978原件关闭历史方法body缺口，actual2022/实验迁移边界保持。；WK22-40保literal定义与已闭合条件归一/未识别actual字段。；Ref23后续实际原读状态已更新，历史未得记录保留，不把轴向对角公式当全库。；BR85原参数/追踪与130Ce实际模型比较原读，三源REFLECT保actualjob独立缺口。；054/055完整30页PartI原读并058短审通过：single-j/ph零点/配对/core/轴置换与signedEM合同；多轨道充分条件为任务推广，不填actualCe参数或δ。；PartII原25p比较的目标定标、历史Ce最低态失败、γsoftness/rms/fit与两极限边界。；Gizon1974实际primary闭合994/1164数字出处，保历史zero与modern单node-edge候选/整带身份边界；old817.3unassigned不补现代817.7/582分母。；实际2011评估固定modern lowzero与寿命版本；Butler La primary关闭PartII Table5测量/取参谱系，不迁Ce。；1997 RDDS primary现提供真实133Ce τ和T1/2定义转换，逐态/branch/Cov边界保。；1998高spin DSAM primary现闭合四条τ/Qt与现代Band映射限制。；098按原件纠错，未闭合输入/模型失败保留，095–097强认证撤回。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-35"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-36"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-37"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-38"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-006"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-010"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-39"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-40"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-021"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-022"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-003"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-004"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-001"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-002"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-41"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-004"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-005"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-012"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-014"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-002"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-009"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-010"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-013"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-014"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-016"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-002"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-003"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-004"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-005"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-006"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-001"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-003"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-004"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-005"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-006"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-009"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-010"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-014"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-001"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-002"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-003"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-004"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-005"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-006"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-001"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-002"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-004"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-005"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-008"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-010"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-46"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "Day24正式研究入口：135Nd逐伙伴实验",
      "summary": "增加新canonical项目的最小索引入口，模型/实验层级保持。 增加OL02临界模型域与版本导航。 checkpoint009加CH13集体量子化/有限gap/测度/边界及second-vibration失败。 012/013二维原稿/周期边界/PRM支持和低spin失败、域边界。 014 EM PartII的single-density带内率/相干跨带核边界、交错失败与质量版本；不补实核输入。 016good-I有限space/metric/coherent核推导与几何信息边界，GR06非新实验。 Day25preview三核matrix导航。；新Larsson1978原件关闭历史方法body缺口，actual2022/实验迁移边界保持。；Ref23后续实际原读状态已更新，历史未得记录保留，不把轴向对角公式当全库。；BR85原参数/追踪与130Ce实际模型比较原读，三源REFLECT保actualjob独立缺口。；052 Ref63 primary收紧continuum量/最高线/数值与shape推断，不倒填二级概括。；054/055完整30页PartI原读并058短审通过：single-j/ph零点/配对/core/轴置换与signedEM合同；多轨道充分条件为任务推广，不填actualCe参数或δ。；PartII原25p比较的目标定标、历史Ce最低态失败、γsoftness/rms/fit与两极限边界。；Gizon1974实际primary闭合994/1164数字出处，保历史zero与modern单node-edge候选/整带身份边界；old817.3unassigned不补现代817.7/582分母。；实际2011评估固定modern lowzero与寿命版本；Butler La primary关闭PartII Table5测量/取参谱系，不迁Ce。；1997 RDDS primary现提供真实133Ce τ和T1/2定义转换，逐态/branch/Cov边界保。；1998高spin DSAM primary现闭合四条τ/Qt与现代Band映射限制。；新增Tonev2006 134Pr寿命与手征检验原实验条目。；新增Tonev2007 134Pr长文条目。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-001"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-008"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-011"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-001"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-003"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-006"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-006"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-001"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-004"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-001"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-001"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-001"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-004"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-005"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-012"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-014"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-002"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-009"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-010"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-013"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-014"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-016"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-002"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-003"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-004"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-005"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-006"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-001"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-003"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-004"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-005"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-006"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-009"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-010"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-014"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-001"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-002"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-003"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-004"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-005"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-006"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-001"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-002"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-004"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-005"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-008"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-010"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-001"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
      "anchor": "Day24主线核验：共同转频、有限窗口与模身份",
      "summary": "原18页主线和关键visual回核，新增五项分层claim；publicstaging/raw归档边界保留。",
      "sources": [
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-001"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-002"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-003"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-004"
        },
        {
          "path": "knowledge/sources/almehed-2011-chiral-vibrations-a135.md",
          "locator": "AL11-D24-005"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
      "anchor": "Day24正式研究：作者投影网格与有限手征窗口",
      "summary": "官方作者archive与690marker匹配，缩小网格缺口并保producer/实验/版本边界。",
      "sources": [
        {
          "path": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
          "locator": "QI09-D24-001"
        },
        {
          "path": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
          "locator": "QI09-D24-002"
        },
        {
          "path": "knowledge/sources/qi-2009-135nd-particle-rotor-chirality.md",
          "locator": "QI09-D24-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2006-128cs-chiral-doublet-lifetimes.md",
      "anchor": "Day24独立伴随链：高spin DSAM与bandhead g逐态分开",
      "summary": "本轮原件逐态/run/clock核验与独立伴随设计，保response/model边界。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2006-128cs-chiral-doublet-lifetimes.md",
          "locator": "GR06-D24-001"
        },
        {
          "path": "knowledge/sources/grodner-2006-128cs-chiral-doublet-lifetimes.md",
          "locator": "GR06-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "Day24逐态companion核验：同isomer多γ与高spin寿命不是同一输入",
      "summary": "本轮原件逐态/run/clock核验与独立伴随设计，保response/model边界。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D24-001"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/li-2004-lifetimes-131ce.md",
      "anchor": "Day24：寿命逐态引用与133Ce迁移合同",
      "summary": "逐态/clock/限值及同寿命再转换谱系的原读核验，迁移方法不搬131Ce数值。",
      "sources": [
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-D24-001"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
      "anchor": "Day24：131Ce实际节点、clock与目标核迁移",
      "summary": "逐态/clock/限值及同寿命再转换谱系的原读核验，迁移方法不搬131Ce数值。",
      "sources": [
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-D24-001"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
      "anchor": "Day24 active source/version entry",
      "summary": "两版本身份/带族crosswalk/零点条件、779不确定度纠正与作者模型层分开。",
      "sources": [
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-001"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-002"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-003"
        },
        {
          "path": "knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md",
          "locator": "A13-D24-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
      "anchor": "Day24：正宇称寿命family映射与未闭合的表图端点",
      "summary": "正Band2寿命family桥、Band3低头与表图/近能γ未闭合项。",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-001"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-002"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-003"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-D24-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
      "anchor": "临界频率：给定gyro与惯量的均匀转动分岔",
      "summary": "新直接原稿source，全部四页与公式/图、版本、阈值/惯量/反证及量身份。 010全局分支/阈quartic及改模型退化边界。",
      "sources": [
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-001"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-002"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-003"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-004"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-005"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-006"
        },
        {
          "path": "knowledge/sources/olbratowski-2002-critical-frequency-preprint.md",
          "locator": "OL02-D24-007"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
      "anchor": "一维集体量子化补上有限隧穿，也保留其冻结自由度",
      "summary": "新直接source：16页v2主线、全部8图，模型/量子化/比较坐标和实际输出scope分层，未raw归档或认证VoR。 011连续metric/概率/packet及三路synthetic收敛，regular/singular域分开。 012/013二维原稿/周期边界/PRM支持和低spin失败、域边界。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-002"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-003"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-005"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-008"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2013-collective-hamiltonian-chiral-modes.md",
          "locator": "CH13-D24-010"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-011"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
      "anchor": "动态θ、交叉质量与高频再劈裂：补到哪一层",
      "summary": "新原方法v2 source，完整主线与关键visual，交叉质量/测度/域、改边界、实际benchmark/失败和条件Gram/pole分析分层。 014 EM PartII的single-density带内率/相干跨带核边界、交错失败与质量版本；不补实核输入。 015完整主TeX/partialarchive与actualproducer边界。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-002"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-003"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-005"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-008"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-010"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-011"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-012"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-001"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-003"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-006"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-009"
        },
        {
          "path": "knowledge/sources/chen-2016-two-dimensional-collective-chiral-wobbling.md",
          "locator": "CH16-D24-013"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
      "anchor": "集体取向涨落修正带内率，未给完整相干跨带振幅",
      "summary": "新直接PartII原v2 source：全文4图/局部率/概率积分、输入/有效角/好自旋/交错失败、only-intraband与literal遗漏分别记录。 015完整author-package scoped清单。 016good-I有限space/metric/coherent核推导与几何信息边界，GR06非新实验。",
      "sources": [
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-001"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-002"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-003"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-004"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-005"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-006"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-007"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-008"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-009"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-010"
        },
        {
          "path": "knowledge/sources/wu-2018-two-dimensional-collective-electromagnetic-transitions.md",
          "locator": "WU18-D24-011"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-006"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
      "anchor": "Day24正文回读：投影态、相干核与几何分布",
      "summary": "既有source原件增量深化并限定原configuration-mixing措辞，新增8项投影空间/metric/EM/phase/测度/输入与反证边界，原flags保持。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-001"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-002"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-003"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-004"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-005"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-006"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-007"
        },
        {
          "path": "knowledge/sources/chen-2017-128cs-angular-momentum-projection-chirality.md",
          "locator": "CH17-D24-008"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "Day24内Day25预习：两个family与局部端点边界",
      "summary": "同一原件新局部链接/能量歧义与两family数据/校准边界，保实际正支持。 023明确共享campaign与selectedevents/Cov未得；clock可jointfit。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-001"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-002"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-003"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-004"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-005"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "DD-20260910-136ND-01"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "DD-20260910-136ND-02"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
      "anchor": "Day24内Day25预习：实际reprint身份与D5组态更正",
      "summary": "纠正假SI/错hash与D5原TableC配置，保ratio/3D几何不同pair及未给absoluteEM范围。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-002"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-003"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
      "anchor": "Day24内Day25无学分预习：134Pr比较行",
      "summary": "原件scope/解混合假设、branch vs lifetime和shape解释的三核设计边界。 022非对角E2前向kernel/基变换不变量与ratio-identifiability，非fit。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-002"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/chirality-shape-coexistence-companion-matrix.md",
      "anchor": "不同核、不同pair的支持链不能拼成一条完整向量",
      "summary": "新Day25无学分逐family direct/author/model/alternative矩阵及companion缺项降级，非新实验/普适终判。 022非对角E2前向kernel/基变换不变量与ratio-identifiability，非fit。 023明确共享campaign与selectedevents/Cov未得；clock可jointfit。 024把旧negative互配EM挑战与新C/positiveD5的反证对象分开。 025按原件校准E0/shape定义/互补量词并撤回旧无定位强认证。 026已存loop合同verified-no-op，补ΔI2无M1δ的scope guard。 028真实thesis逐母态/relativeI输入与条件E2比；不补133Ce缺分母。 029同I scalar/radius Hermitian扩展与配置基前提，非新fit。；031给实际PRM输出边界和有限holdout合同；030复核既有103Rh知识为source verified-no-op，仅新增MχD不自动证明多shape的比较量词。；033补相邻21+实际条件E2比、selected子集/同spin块完整性及22+literal Ei歧义。；040补实际四线joint response/Jacobian与最小Cov合同，不报CI。；Ref23后续实际原读状态已更新，历史未得记录保留，不把轴向对角公式当全库。；BR85原参数/追踪与130Ce实际模型比较原读，三源REFLECT保actualjob独立缺口。；052 Ref63 primary收紧continuum量/最高线/数值与shape推断，不倒填二级概括。；PartII原25p比较的目标定标、历史Ce最低态失败、γsoftness/rms/fit与两极限边界。；090真实取得Tonev2006原实验5页，排除静态手征而兼容动态手征，PE06寿命谱系已闭合。；095引入Tonev2007 26页PRC长文基准，补充完整Table I偏振/强度与Table II跃迁几率。；098按原件纠错，未闭合输入/模型失败保留，095–097强认证撤回。；099续当前原件：微观/几何惯量合同、当前数据调参/赋名、I>16的2qp空间边界分开，不计135Nd新增实验。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-002"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-001"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-002"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-003"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-004"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-002"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-003"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-004"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-003"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-005"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "DD-20260910-136ND-01"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "DD-20260910-136ND-02"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-D18-5"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-D18-6"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-D18-7"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-001"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-002"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-003"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-004"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-005"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-006"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-D24P-004"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-D24P-005"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-001"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-002"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-003"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-004"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-005"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-007"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-004"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-006"
        },
        {
          "path": "knowledge/sources/kuti-2014-multiple-chiral-doublets-103rh.md",
          "locator": "KU14-13"
        },
        {
          "path": "knowledge/sources/kuti-2014-multiple-chiral-doublets-103rh.md",
          "locator": "KU14-D18-8"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-006"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-007"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-008"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-009"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-006"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-008"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-009"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-005"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-007"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-012"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-013"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-002"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-003"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-005"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-012"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-014"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-015"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-001"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-002"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-003"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-004"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-005"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-006"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-007"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-001"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-002"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-003"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-004"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-005"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-006"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-007"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-008"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-009"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-010"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/triaxial-shape-coexistence.md",
      "anchor": "Day24内Day25预习：逐伙伴比较的证据层",
      "summary": "新增三核竞争解释导航和实验/多极小/解混合分层。 025按原件校准E0/shape定义/互补量词并撤回旧无定位强认证。；098按原件纠错，未闭合输入/模型失败保留，095–097强认证撤回。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25P-002"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-003"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25P-004"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-001"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-002"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-003"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25P-004"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-001"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-002"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-003"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-004"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-005"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-006"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-003"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-004"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-005"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-006"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
      "anchor": "Day24内Day25预习：定义、E0与证据量词校准",
      "summary": "scoped原件校准及原ID撤回无定位百分比/固定V/排他与强制组合，补半径组合/非0高spin/综述立场范围，HW11-4原flag不变。 029同I scalar/radius Hermitian扩展与配置基前提，非新fit。",
      "sources": [
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-001"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-002"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-003"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-004"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-005"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-006"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-007"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
      "anchor": "Day24内Day25预习：真实D5母态、相对强度与方法输入",
      "summary": "scoped原件真实方法/几何与3parent14line库存、归一/unknown字段，实际sameparentE2中央条件比，非fullthesis重读/新campaign/absoluteB；原falseflags保持。；033补相邻21+实际条件E2比、selected子集/同spin块完整性及22+literal Ei歧义。；040补实际四线joint response/Jacobian与最小Cov合同，不报CI。",
      "sources": [
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-001"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-002"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-003"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-004"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-005"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-006"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-007"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-008"
        },
        {
          "path": "knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md",
          "locator": "TH19-D25P-009"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
      "summary": "新增实际15页v1精读：good-I四壳PRM的D5输入/真实支持与未发表目标两E2预测；不重放producer。",
      "anchor": "四壳量子PRM支持D5，目标两E2预测仍未交付",
      "sources": [
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-001"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-002"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-003"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-004"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-005"
        },
        {
          "path": "knowledge/sources/chen-2018-four-j-shell-prm-136nd.md",
          "locator": "CQ18-D25P-006"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
      "summary": "外部已发布提交bfdb7b3c的用户PDF获取登记，非本run科学写回；本run核验归属/历史原子边界为verified-no-op，当前文件等于HEAD，排除本run暂存清单。仅为不改原baseline的累计snapshot对账。",
      "anchor": "2026-10-26 用户补充原件：获取状态更新",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D23-024"
        }
      ],
      "note": "atomic locator是保留的既有科学/访问边界，不表示新增PDF已在本run科学读完；获取登记独立于原文结论。"
    },
    {
      "knowledge": "knowledge/sources/kumar-2025-review-magnetic-antimagnetic-rotational-structures.md",
      "summary": "外部已发布提交bfdb7b3c的用户PDF获取登记，非本run科学写回；本run核验归属/历史原子边界为verified-no-op，当前文件等于HEAD，排除本run暂存清单。仅为不改原baseline的累计snapshot对账。",
      "anchor": "2026-10-26 用户补充原件：获取状态更新",
      "sources": [
        {
          "path": "knowledge/sources/kumar-2025-review-magnetic-antimagnetic-rotational-structures.md",
          "locator": "KU25-D23-001"
        }
      ],
      "note": "atomic locator是保留的既有科学/访问边界，不表示新增PDF已在本run科学读完；获取登记独立于原文结论。"
    },
    {
      "knowledge": "knowledge/sources/ragnarsson-semmes-1988-particle-rotor-moments.md",
      "summary": "外部已发布提交bfdb7b3c的用户PDF获取登记，非本run科学写回；本run核验归属/历史原子边界为verified-no-op，当前文件等于HEAD，排除本run暂存清单。仅为不改原baseline的累计snapshot对账。",
      "anchor": "2026-10-26 用户补充原件：获取状态更新",
      "sources": [
        {
          "path": "knowledge/sources/ragnarsson-semmes-1988-particle-rotor-moments.md",
          "locator": "RS88-16"
        }
      ],
      "note": "atomic locator是保留的既有科学/访问边界，不表示新增PDF已在本run科学读完；获取登记独立于原文结论。"
    },
    {
      "knowledge": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
      "summary": "用户新原件方法/应用/附录已分工覆盖完整科学主线；恢复历史六矩阵/D2/BCS/signedEM/坐标合同，保实际定标与失败；Table1 B比与条件Hermitian方向代数单独标任务推导，未恢复2022job。；041条件M1/E2/单位字典与042指定stretch五分量/physical L/length²恒等式固化，均非actualproducer结果。；Ref23后续实际原读状态已更新，历史未得记录保留，不把轴向对角公式当全库。",
      "anchor": "历史方法矩阵元已可原读，2022实际job仍须另核",
      "sources": [
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-001"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-002"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-003"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-004"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-005"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-006"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-007"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-008"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-009"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-010"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-011"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-012"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-013"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-014"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-015"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-016"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-017"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-018"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-019"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-020"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-021"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-022"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-023"
        },
        {
          "path": "knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md",
          "locator": "LLR78-D24-024"
        },
        {
          "path": "knowledge/sources/ragnarsson-semmes-1988-particle-rotor-moments.md",
          "locator": "RS88-18"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-003"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-004"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-011"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
      "summary": "043方法/Appendix和044全主线图表拼合真实21页原读：历史dimensionless坐标/CG归一/轴向同态QLike及PES定标、static-to-lab与失败边界；不恢复actual2022或三轴完整库。",
      "anchor": "Ref23原件已读：轴向同态Q不等完整三轴跃迁库",
      "sources": [
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-001"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-002"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-003"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-004"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-005"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-006"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-007"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-008"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-009"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-010"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-011"
        },
        {
          "path": "knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md",
          "locator": "LL75-D24-012"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
      "summary": "046合法完整body后048/049/root050分工全69页/32图4表33式：原κμ/Nrot实现、虚交叉/组态追踪、continuum与resolved及130Ce/多核支持和失败；不是actualCe输入或EMproducer。；052 Ref63 primary收紧continuum量/最高线/数值与shape推断，不倒填二级概括。",
      "anchor": "原参数表已读，固定组态与实际能带仍须逐态辨认",
      "sources": [
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-001"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-002"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-003"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-004"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-005"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-006"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-007"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-008"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-009"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-010"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-011"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-012"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-013"
        },
        {
          "path": "knowledge/sources/bengtsson-ragnarsson-1985-rotational-bands-particle-hole.md",
          "locator": "BR85-D24-014"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-002"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-003"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-005"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-006"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
      "summary": "新增真实5页primary/四图原读：valleyJband而非Jeff、采集/选样/污染与最高线assignment/rigidreference分层；原W式名义尺度为任务算术不报实测宽度或CI。",
      "anchor": "实验谷宽约束J_band，不直接测得另一刚性形状",
      "sources": [
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-001"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-002"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-003"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-004"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-005"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-006"
        },
        {
          "path": "knowledge/sources/nolan-1983-ce130-high-spin-moment-inertia.md",
          "locator": "NO83-D24-007"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
      "anchor": "等谱映射有完整合同，不能只改γ与λ两个数字",
      "summary": "054/055完整30页PartI原读并058短审通过：single-j/ph零点/配对/core/轴置换与signedEM合同；多轨道充分条件为任务推广，不填actualCe参数或δ。",
      "sources": [
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-004"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-005"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-007"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-008"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-011"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-triaxial-rotor-particle-model.md",
          "locator": "MTV75-D24-012"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
      "anchor": "Day24 checkpoint062：选择规则的逻辑、输入和奇A迁移",
      "summary": "062原12p全部主线/table/captions/三fig核；修旧D19强认证并保原audit，063审查无必改。E2异A必要非充分、gR两job/系数非B、oddA规则未推导与真实实验谱系分清。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-001"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-002"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-003"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-004"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-005"
        },
        {
          "path": "knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md",
          "locator": "HM11-D24-006"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
      "anchor": "谱对三轴芯有偏好，不等于直接测得刚性",
      "summary": "057真25p后059/060/061分工全主线/图表，root全文text及关键visual；standard含目标定标、Ce9/2失败/历史零点、原表80与δ2/5、γsoft/rigid两极限和模型依赖保。；Gizon1974实际primary闭合994/1164数字出处，保历史zero与modern单node-edge候选/整带身份边界；old817.3unassigned不补现代817.7/582分母。；实际2011评估固定modern lowzero与寿命版本；Butler La primary关闭PartII Table5测量/取参谱系，不迁Ce。",
      "sources": [
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-001"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-002"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-003"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-004"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-005"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-006"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-007"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-008"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-009"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-010"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-011"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-012"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-013"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-014"
        },
        {
          "path": "knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md",
          "locator": "MTVII75-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-002"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-009"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-010"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-013"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-014"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-016"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-002"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-003"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-004"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-005"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-006"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-001"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-003"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-004"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-005"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-006"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-009"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-010"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-014"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
      "anchor": "原实验有实际边和时间信息，也有明确的未定身份",
      "summary": "064合法完整原件22页；066/067/root068分工全部科学主线/图表，实际I55/AD/feeding、四核低谱、历史ground-isomer未知、近线不等edge及模型解释边界，非actualproducer或现代高spin手征新测。；完整70条Table4光子ledger同步knowledge，不仅留worker输出；原表冲突/空白与未绑定现代边保。",
      "sources": [
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-001"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-002"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-003"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-004"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-005"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-006"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-007"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-008"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-009"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-010"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-011"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-012"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-013"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-014"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-015"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-016"
        },
        {
          "path": "knowledge/sources/gizon-1974-deformed-states-cerium-neodymium.md",
          "locator": "GZ74-D24-017"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
      "anchor": "服务当前返回的评估版本与历史实验身份分别保存",
      "summary": "069真实NNDC/IAEA同源评估记录，073无必改；GS/isomer/T/record版本、Cov/IT/anchor循环与unplaced peak边界已写。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-001"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-002"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-003"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-004"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-005"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-006"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-007"
        },
        {
          "path": "knowledge/sources/nndc-2011-133ce-low-level-reference-records.md",
          "locator": "N133CE11-D24-008"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
      "anchor": "原寿命支持条件三轴比较，邻偶核仍是定标输入",
      "summary": "071/074完整4p primary与视觉，τ/feeding/RD/normalizer、La B、脚注字典冲突、qγ条件算术和γ扫描边界已写；PartII重复不计独立。",
      "sources": [
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-001"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-002"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-003"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-004"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-005"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-006"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-007"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-008"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-009"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-010"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-011"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-012"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-013"
        },
        {
          "path": "knowledge/sources/butler-1975-la129-la131-rd-lifetimes.md",
          "locator": "BU75-D24-014"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
      "anchor": "133Ce寿命网络中的时钟、跃迁和模型边界",
      "summary": "072完整原读1997 APS 4页RDDS primary；τ/T1/2转换、RDDS拟合、逐态负/正宇称寿命、B假设和内部冲突写回，不迁现代未绑定母态。",
      "sources": [
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-001"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-002"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-003"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-004"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-005"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-006"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-007"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-008"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D24-009"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
      "anchor": "高自旋带的寿命和Qt提供独立时钟，也保留阻停与组态边界",
      "summary": "078完整4页APS Joss primary；Gammasphere DSAM/DBLS、四条高spin τ/Qt、TRS shape、sidefeeding和高spin identity/partner边界写回。",
      "sources": [
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-001"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-002"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-003"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-004"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-005"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-006"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-007"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-008"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-009"
        },
        {
          "path": "knowledge/sources/joss-1998-133ce-triaxial-band-lifetimes.md",
          "locator": "JO98-D24-010"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
      "anchor": "超形变带是真实观测节点，构型和形状仍需条件化",
      "summary": "081完整6页Hauschild primary；三条SD带、J(2)/alignment和PES/configuration条件，明确无τ/Qt/B/linking/DCO，与Joss/Gizon/Emediato分开但1995/1996同一Hauschild campaign。",
      "sources": [
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-001"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-002"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-003"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-004"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-005"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-006"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-007"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-008"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-009"
        },
        {
          "path": "knowledge/sources/hauschild-1995-133ce-superdeformed-bands.md",
          "locator": "HA95-D24-010"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
      "anchor": "三轴带和组态候选清楚，缺失link也清楚",
      "summary": "079完整7页Hauschild1996 primary；六带能级、alignment、tentative configs与DCO/link缺口写回，不升级3qp/静态shape/手征。",
      "sources": [
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-001"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-002"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-003"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-004"
        },
        {
          "path": "knowledge/sources/hauschild-1996-133ce-triaxial-bands.md",
          "locator": "HA96-D24-005"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
      "anchor": "134Pr所研究双带的静态极限受到限制，动态解释仍保持条件性",
      "summary": "090完整5页PRL Tonev原实验；Euroball IV RDDS/DSAM 14态寿命、带内B(E2) 2–3倍不对称、排除静态手征但兼容动态手征/形状涨落、以及与PE06 Ref.9/11谱系写回。；098按原件纠错，未闭合输入/模型失败保留，095–097强认证撤回。",
      "sources": [
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-001"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-002"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-003"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-004"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-005"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-006"
        },
        {
          "path": "knowledge/sources/tonev-2006-134pr-lifetime-chiral.md",
          "locator": "TO06-D24-007"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
      "anchor": "134Pr详细实验表与模型比较：形状涨落支持及未解交叉问题",
      "summary": "098核26页VoR/真实表图，保同实验、缺跨带δ、逐点E2及模型失败；更正095–097过强定论。；099续当前原件：微观/几何惯量合同、当前数据调参/赋名、I>16的2qp空间边界分开，不计135Nd新增实验。",
      "sources": [
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-001"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-002"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-003"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-004"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-005"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-006"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-007"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-008"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-009"
        },
        {
          "path": "knowledge/sources/tonev-2007-134pr-dynamic-chirality.md",
          "locator": "TO07-D24-010"
        }
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "summary": "按本次实际lint同步Day24治理快照，区分统计与科学证据；QMD刷新继续deferred。",
      "anchor": "Current Snapshot: 2026-10-27 Day24 closeout",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 134Pr的TQPTR能谱/交叉支持和EM失配、IBFFM主要EM支持与能隙/交叉失败，如何在同一数据/定标合同下比较？Tonev2007保留尚未揭示的内禀对称性，弱涨落主导手征仍属作者解释。2006/2007共享实验，不当独立重复。
2. 135Nd负pair原有绝对EM支持保留；完整态/算符核、normalizer/Cov及未定标替代预测仍缺。HM11的特殊odd-odd选择规则不能直接迁odd-A；异A只是特定E2非零的必要条件，非普适手征判据。
3. 133Ce六项附属问题有账本但未全部解决：582 out/out分母、actual代码/header/单位/负λ、run/mask/45°events、target母态寿命和3qp空间仍开放。14.1 keV不提供ωc，412.4/767.7均来自1445.8母态。下一输入必须改变判断，不以扩写已有summary充当研究。

## L0–L4 state

L0主来源回读、L1/L2证据分层和有界推导、L3逐伙伴图/反证设计进行中。有限接受度脚本是声明条件的数学组件，不是实核L4 response重分析。无独立用户数据、无实际fit/Cov/likelihood重放；不新增human-reviewed，不清needs_review。

## Verification and continuation

入口boundary/preflight均exit0；EOL清理0且无实质tracked继承dirty，继承未跟踪Day20/22/23文件已在`entry-audit-001.json`记录、全部保护。首次lint exit1：新project缺4个schema标题及index入口（5项）；已补齐，再运行最终检查，首次失败不隐去。最终lint exit0（errors0/warnings228/info4680）、boundary exit0、git diff --check exit0；原runner report/writeback/curriculum三门均valid。接受度脚本exit0/32控制通过。precommit EOL exit1只因6个本轮实质修改保留，unsafe/mixed0。228项warnings为继承citation/review等治理欠项，未掩盖或清除；详见`required-checks-001.json`。

续接：`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/next-continuation-001.md`。保留本session与原15:00截止；checkpoint不提前结束整段学习。当前问题仍有方法/反证高价值路线，不宣称schedule-level saturation；不授[24]、不开Day25正式卡。最终credit/final receipt/下一日准备只在对应原runner门执行。

Git稳定指针：main · Day24: map chiral partners and bound finite gate acceptance。本checkpoint采用显式manifest，实际hash/H3/远端结果只写`task-publication-receipt-001.json`；保护raw/PLAN/Bib和继承dirty。overview update deferred：这是首个增量checkpoint，最终formal closeout再按实际lint汇总；QMD刷新deferred，directread/rg可用。


### checkpoint002验证与继续状态

2026-10-26T18:46:31.527113+08:00，距原截止约1213.5分钟，continue-current。上一checkpoint publication receipt实际published/H3passed；本turn按最新continuation显式规定“mid-run不发布”，保存工作树，不stage/commit/push，统一正式closeout再发布。不是未获授权，不新建run/session、不给Day24学分，累计23/next24不变、Day25未打开。

本轮入口boundary exit0、EOL exit0；tensor脚本exit0/157controls。最终lint exit0（errors0/warnings228/info4685）、git diff --check exit0；原runner三门全valid，protected hashes不变、index空，记录required-checks-002.json，续接prompt为本run `next-continuation-002.md`。新增知识仅AL11source与135Ndmap，两页已入唯一writeback，既有8项累计映射保留。overview/QMD继续deferred。

下一候选池已按实际文件核重建（`candidate-pool-002.json`）：Qi2009公开v1暂存/hash存在，可核有限量子PRM的transient图像和投影概率表示；Grodner2006原四页/hash存在，可作独立DSAM/feeding链对照。Day25 matrix已检查，仅课程入口检查，未打开其科学preview，不列partial25；当前主问题仍有高价值路线。北京时间2026-10-26T18:51:00.089313+08:00距硬截止约1209.0分钟，本次仅交给原runner同session下一turn，不是Day收束或schedule-level饱和。


### checkpoint003继续状态

2026-10-26T19:13:45.209021+08:00，余1186.2分钟。用户显式farmer/go-on/all/auto续学已承接：同session原生goal实际active，Farmer ensure exit0仍为PID2698，dry-run actions=[]；无新监督实例、无新学习session、未杀现有服务。go-on以Git/handoff/run/environment多源恢复checkpoint002及中断的003。用户持续学习至原2026-10-27 15:00的要求覆盖局部收敛/默认5轮早停；fast未激活。

当前主线齐全但研究仍继续，未授Day24学分、Day25仅matrix入口检查未preview、不开Day26。本轮不stage/commit/push，保护已有worktree与raw/PLAN/Bib。原runner Python不在本次ps清单中，仅报告实际Codex同thread resume、nativegoal与Farmer状态，不冒称新启动daemon。

下一单位选独立伴随观测链：128Cs原DSAM伙伴寿命与bandhead g所对应的不同态/采集，保nucleus/state/clock/branch身份；优先有原件的GR06，不以同核名称合并τ/g向量。本轮fresh检查在required-checks-003.json，续接入口next-continuation-003.md。


### checkpoint004继续状态

2026-10-26T19:22:37.916008+08:00，余1177.4分钟。128Cs独立companion单位已主线/关键visual核验并固化source/map，clock仅条件算术。原15点继续研究，未授分、未开Day25知识preview，midrun不发布。003/004累计freshchecks已执行：lint0/errors0/warnings228/info4692、diff0、runner三门valid；117表示控制/AST通过，protectedhash不变、index空；实际结果在required-checks-004.json；source/知识对应现11项唯一block，未把outputs当唯一知识副本。

下一附属单位按用户既有要求：131Ce Li2004/Singh2016已有τ，准备按Ei/Jπ/branch/clock/采集谱系核其接入133Ce分析蓝本的条件，保两个核的数值和family分开。主卡已有高价值工作完成，附属不替代课程学分；不再空查133Ce mask/582分母。


### checkpoint005：并行证据整合及继续

2026-10-26T20:05:53.735911+08:00，余1134.1分钟；nativegoalactive，未进入closeout。用户新增持续subagent授权后使用team/dispatch三域只读shared evidence/独占outputprefix。Singh逐态、Qi独立representation审查、133Ce九边三任务均完成，root读报告并抽核原表；可复用内容已进source/133Ceblueprint，outputs只审计副本。

没有把worker完成当成Day完成，也没有按派发数计信息增益。原有主卡继续，partial[24]/累计23next24不动。当前新workers各自独立调查：Starosta2001原定义（未得body边界）、Larsson1978方法引用层（body0、WK22程序/参数引用新分层）、133Ce高spin原件的零点/编号crosswalk、2002criticalTAC原稿及AW13正序列映射；只在root原件抽核后吸收，不从中间消息授予科学认证。

本轮midrun不发布。所有全文提取/源PDF/整页图片等中间品最终不进发布manifest，canonical知识/必要审计脚本与小型结果按正式closeout精确清单处理。005freshchecks写required-checks-005.json；续接next-continuation-005.md。


### checkpoint008：原件整合与下一单位

2026-10-26T20:54:28.177459+08:00，余1085.5分钟，继续原Day24研究。006/007证据已root核并写入16个累计knowledge路径；008独立版本/公式审查未发现阻断性缺陷，但不扩大为HF/实验认证。用户许可持续subagents，worker只写独占prefix，root统一canonical。当前下一主单位为一维手征集体Hamiltonian的量子化/质量/测度/边界与高频失败；另一独立单位为134Pr两partner寿命反证。它们仍属Day24，Day25只有matrix入口检查。

本checkpoint保completed=[]、partial=[24]、累计23/next24，未做midrun暂存/提交/推送。新完整PDF/全文/整页图片最终不入publication manifest；raw/PLAN/Bib/继承dirty与人审撤回边界不变。最新检查将写required-checks-008.json；下一恢复提示next-continuation-008.md。旧005checks不认证其后改动。


### checkpoint009：量子化增量与fresh checks

2026-10-26T21:02:11.777548+08:00，余1077.8分钟，继续原Day24。CH13原件及新source/map/concept/index已整合，累计17条knowledge路径。008初次lint exit1：OL02缺Extracted Pages标题（1error/230warnings），已补；另发现本次插入公式含一个CR控制字符，已纠正为literal反斜线right并核无CR。此前runner008三门valid，不能替新页fresh检查；本次以required-checks-009.json为准并保留首次失败。

继续任务：011独立Pauli测度/坐标变换/谱收敛组件、010固定ω/I全局分支合同、012二维方法原件，三者由worker独占prefix，root核后写knowledge。原134Prbody0路线不反复撞端点。completed=[]partial=[24]、累计23next24，不提前授分；Day25仅matrix，midrun不发布。next-continuation-009.md给出可恢复入口。

009实际检查：lint exit0（SUMMARY pages=723 wikilinks=9675 hashes=352 errors=0 warnings=232 info=4721），git diff --check exit0，原runner report/writeback/curriculum三门valid；protected PLAN/Bib哈希与入口相同，index空。232warnings含原228及本轮两新source各自缺citation key/尚未raw归档的4项，未把新增warning伪称全继承；不修改raw/Bib消项。检查回执required-checks-009.json，未发布，继续研究。


### checkpoint013：主线方法链仍继续

2026-10-26T21:25:12.902241+08:00，余1054.8分钟。010–013已写canonical，累计18knowledge路径；原source actual_body路径/三个tmp PDF hash均本次重核相符。最新完成门仍009（lint0/errors0/warnings232、runner三门valid），这些门早于本轮新增，待下一fresh门不能沿用认证。所有新claimsneeds_review:true；未改原人审/withdrawals/raw/PLAN/Bib/课程状态，midrun不stage/commit/push。

下一高信息主单位为EM PartII：局部TAC率的概率平均是否等同跨I/sector相干矩阵元？实际body已由worker014取得，root核原式/模型有效域后才写知识。013的极点条件分析不扩成作者谱错，也不为复现未知producer继续造toy测试。当前仍有主线输入可读，未作schedule-level saturation。Day25仅课程入口检查，PE06定向既有依赖核验未形成该卡新交付；无Day25信用，不开Day26。续接next-continuation-013.md。


### checkpoint014：EM方法增量与恢复状态

2026-10-26T21:35:11.681482+08:00，余1044.8分钟，继续原Day24。新增WU18 source与主map/概念/index/133Ce方法迁移，累计19knowledge路径。013初次lint exit1（1error/234warnings）：project正文用双中括号写2×2矩阵，被识别为无效Wiki link；已改成逐分量数学记号。该字面/链接失败不隐去，diff与runner013三门当时valid；最新整体门待required-checks-014.json。

当前两个后续输入域：015查实际作者producer/grid/端点regularization；016核good-I角动量投影原模型如何保组态/几何/EM相干。二者仍服务Day24同一个伙伴证据问题，worker只写独占prefix，root核后单写canonical。user持续学习要求与原2026-10-27 15:00保持；不因source完成/检查点或代理轮数收束，midrun不发布、不授分。next-continuation-014.md可恢复。

014实际freshchecks：lint exit0（SUMMARY pages=725 wikilinks=9703 hashes=352 errors=0 warnings=236 info=4744）、boundary exit0、git diff --check exit0、原runner report/writeback/curriculum三门valid。19个changed knowledge路径全部映射；4个新source actualbody哈希相符、两组件AST/root实际重跑完成，PLAN/Bib入口hash不变、index空。236warnings为原228加4个新staging source各citation/raw两项，未伪称全继承，也不写raw/Bib消项；首次008/013失败保留在required-checks-014.json。当前仍研究中，未发布/未授分。


### checkpoint016/017与Day25预习门

2026-10-26T21:59:58.574368+08:00，距原截止1020.0分钟。015源包范围、016good-I原件/推导已root核并写canonical，20路径唯一writeback。017静态矩为既有source的verified-no-op，不强造page delta。最新已完成整体门014早于本增量，待fresh016checks；无本轮stage/commit/push，goal仍active。

按实际clock和已重建候选池启动恰好Day25 preview：root已查matrix及Lv source入口，018/019workers分别读135Nd/136Nd，root续Petrache134Pr原件；下一新知识只有partial25，不授该卡、不越过next_day_index24/累计23。Day24主卡仍等本run截止后的逐卡审计/receipt/发布门，不因局部达到deliverable而结束学习。next-continuation-016.md保恢复状态。


### checkpoint020：Day25无学分矩阵及原件更正

2026-10-26T22:18:12.191365+08:00，余1001.8分钟。018/019/020已root核并写canonical：三核比较/project+shapeconcept、LV19局部歧义、PE18假SI/配置纠正与PE06对照，累计25条knowledge路径，唯一writeback同步。最新完成016checks（lint0/errors0/warnings236、diff0、runner三门valid且partial[24,25]）早于后续preview修订，需fresh020验收。新claims仍needs_review:true、protected原件/PLAN/Bib/旧人审撤回与114隔离不变，midrun无发布。

下一有界输入：021Tonev2007长文exacttitle/DOI已核，但三新合法路线均无body（APS401/HALmetadata/Camerino403），0页/0表/0图；不创建伪sourceB表、不把引用关系当samecampaign。022在实际PE06两带空间允许off-diagonal E2，检何种矩阵不变量与可识别性；023独立审查三核matrix/共享采集边界。继续在Day25preview内，不开Day26、completed仍[]、partial[24,25]、累计23next24。next-continuation-020.md。

020实际freshchecks：初次lint1因newproject缺Current Hypotheses标题，已补内容并重跑exit0（SUMMARY pages=726 wikilinks=9731 hashes=352 errors=0 warnings=236 info=4764）；boundary0、git diff --check0、runner report/writeback/curriculum三门valid，25knowledge路径映射、protectedPLAN/Bibhash不变、index空。此前008/013失败及本次首次失败均留日志；midrun不发布、不授分，partial[24,25]仍仅知识预习。


### checkpoint024：kernel扩展与矩阵独立复核

2026-10-26T22:35:49.049721+08:00，余984.2分钟，继续Day24/恰好Day25preview。022数学与023谱系/量词修改已canonical，024既有science no-op但新pair-level transfer对照在project，累计25changed knowledge路径。最新020通过门早于本增量，待fresh024检查；partial[24,25]formalcredit0/next24保持。当前后续025校准shape概念/E0与companion量词，只读相应review连续段，不开Day26。当前各源/脚本完成是checkpoint，不是整日收束，仍goalactive/原15:00截止；midrun不stage/commit/push。next-continuation-024.md。

024实际freshchecks：lint0（SUMMARY pages=726 wikilinks=9735 hashes=352 errors=0 warnings=236 info=4766）、git diff --check0、runner report/writeback/curriculum三门valid，25changedknowledge映射。022脚本AST与root重跑exit0，PLAN/Bib入口hash相同、index空。236warnings照实保留，未改raw/Bib消项；midrun不发布，goal继续。


### checkpoint026：shape量词、重叠审查与实际输入续接

2026-10-26T23:01:24.719640+08:00，余958.6分钟，仍继续同Day24/恰好Day25preview，goalactive/Farmerstatusfresh running PID2698。025原件/withdrawal副本与026scope guard已canonical，累计26条knowledge路径唯一writeback；026核心为已存知识的verified-no-op，不按重复脚本计新信息。最新024通过门早于本增量，待fresh026lint/diff/runner。

027exactfullschemepaper仅metadata、实际body0，两路线+一次具体bitstream HTTP1.1运输重试全保，端点已停。转真实已有原件：028读吕thesis Ch4/5对应D5/C表而非继续网络失败，核哪些真实字段可补/哪些仍缺；029同I scalar E0算符的extra offdiag前提，区别022不同spin的E2forward块。source未给量保持unknown，不把worker编号当课程Day26/28/29；formalcredit仍[]/partial[24,25]/累计23next24。midrun不发布，next-continuation-026.md。

026实际freshchecks：lint0（SUMMARY pages=726 wikilinks=9739 hashes=352 errors=0 warnings=236 info=4772）、git diff --check0、runner report/writeback/curriculum三门valid，26changedknowledge全映射；HW11-4原needs_review:false保持、PLAN/Bib入口hash相同、index空。原records/withdrawal副本保留，236warnings如实，不改raw/Bib消项；仍研究中、无midrun发布/学分。


### checkpoint029：真实输入比值与同态scalar算符

2026-10-26T23:30:47.032977+08:00，距原截止929.2分钟，goalactive/同session仍研究中。028/029已root原表/方法/公式核并入source/project/133Ceblueprint，27changedknowledge路径唯一writeback；026最新门通过（error0/warn236、diff0、三门、26路径）早于本增量，待fresh029。旧DD-03与HW11-4 falseflags保、raw/PLAN/Bib未动，midrun不发布。

继续有限新问题：030 Kuti103Rh对MχD是否必为不同shape/config的比较控制（既有闭合则no-op）；031直接136Nd PRM原件核D5-C20+ inter/in E2可否作holdout，缺prediction不逆造图数。027具体bitstream运输失败已停，真实thesis不伪装那篇期刊。仍Day24+仅Day25preview/Day26课程闭，不按worker号启新卡，不先授分。next-continuation-029.md。


### checkpoint031：实际模型输出与外部改动归属

2026-10-26T23:46:38.324402+08:00，余913.4分钟，同goalactive/Farmer2698/原15:00截止，未收束。029首次runner writeback失效原因已查清：外部23:13提交bfdb7b3c更改三页获取登记，三页parent内容与本run原baseline完全相符、当前内容等于外部commit及HEAD。原baseline/失败029保存，新增归属回执并以明确外部no-op项做累计snapshot映射，不认领其科学delta、不stage原外部页。029 lint0/errors0/warnings236、diff0和其余两门valid仍为事实，不冒三门全过。

031新source及030比较边界已root核并写knowledge；28个本run changed知识路径＋3个外部已发布路径需fresh检查。032开始读外部新到真实Larsson1978原件，不再沿旧body0反复检索；033核相邻同parent真实E2，034独立看正式Day24科学缺口。仍completed[]partial[24,25]累计23next24，无新课程/学习session，无midrunstage/commit/push。检查结果另写required-checks-031.json；next-continuation-031.md保恢复。

031实际freshchecks：lint exit0（SUMMARY pages=727 wikilinks=9752 hashes=352 errors=0 warnings=238 info=4784）、git diff --check0、原baseline的report/writeback/curriculum三门valid，31changed路径=28run-owned+3外部归属对账。PLAN/Bib入口hash保持、index空；新增238warnings=原228+五个新staging source各citation/raw两项，未伪称全继承。required-checks-031.json保存，failed029不删除。科学仍partial/研究继续、无midrun发布。


### checkpoint038：新原件、理解校核与条件闭合

2026-10-27T00:12:46.197883+08:00，距原15点截止887.2分钟，已过本地午夜但run_date/session/deadline不改变。033相邻E2、034覆盖审查、035非盲测短答/两处措辞澄清、032/036原方法全主线及037方向代数已整合。032/036不是两个独立来源或实验；全PDF/全文/页图仍不入publicationmanifest。旧003/006的body0为历史，不被回填。

当前29个run-owned changed知识路径与3外部已发布获取登记的累计原baseline对账均需fresh038；最新完整门031早于后续增量，不能代替。旧HW11-4/DD03 falseflags与全部needs_review/撤回保持，raw/PLAN/Bib/114边界不动，未stage/commit/push。下一继续按原剩余时段重建候选池，优先实际可解析的模型/实验合同，而不重复旧missingnormalizer/582线空搜；Day25始终无学分preview，不开26。

038实际freshchecks：lint0（SUMMARY pages=728 wikilinks=9767 hashes=353 errors=0 warnings=239 info=4800）、git diff --check0、原baseline三门valid；32changed=29run-owned+3external、外部三页current hash未动、raw L78 hash相符、PLAN/Bib保、HW11-4/DD03原false保、index空。239warnings=原228+五staging页各2+LLR78 citation1，不改raw/Bib消项。required-checks-038.json保存；仍研究中、无midrun发布。


### checkpoint045：自动资源规则重申与新原件继续

2026-10-27T01:01:12.753022+08:00，余838.8分钟，继续原run/session/截止。用户明确纠正重复SI询问并重申“DAY每日学习不许问。默认能学尽学，应学就学，自行获取应该获取的文章、文件等等一切资源”。已实际写入system/memory.md、continuous-learning与literature-access流程、check.md和USER_GUIDE.md，跨日/session的默认正文+可用SI/必要资源自动获取，不再把通用skill的SI问题作为普通学习门。daily-resource-authorization-045.json为原话/范围回执；此前询问与agent-default下载过程保历史，不倒填为此前已有回复。

039实际获取：默认DOI PDF为1页preview，原manifest泛称downloaded未作全文认证；FULL XML给完整OCR/21页MAIN metadata，直链403一次保留后，用返回的exactattachmentEID走标准ObjectAPI取得21页/1736708B/SHA35ce50…562d。OA/Scholar失败入口和preview保，SIfetch_failed/CDP未启动不说SI全无；source-acquisition-039.json保存。043方法/Appendix与044PES主线原读中，尚未先建source/授科学阅读完成。

040/041/042的窄增量已knowledge，045规则为用户显式新增任务范围，五治理文件写前clean baseline已存；不触raw/PLAN/Bib/credentials或外部skill文件，midrun不stage/commit/push。最新已通过整体门038早于这些变更，待fresh045；formalcredit[]partial[24,25]累计23next24，不开26。next-continuation-045.md保新规则与学习恢复。

045首次检查：lint0/errors0/warnings239、diff0、runner三门valid，五治理文件规则可见、PLAN/Bib及外部三页保；但额外公式control-char扫描发现q±2第二个fraction处一个form-feed，故不保存accepted045。已改为literal反斜线frac并核无控制字符，首次失败留required-checks-045-initial.json，等待fresh门；不沿用旧检查认证修订。


### checkpoint047：Ref23整合与参数原文入口

2026-10-27T01:23:45.875483+08:00，余816.2分钟，继续原Day24。043/044真实21页主线/Appendix已写knowledge，累计33changed=30run-owned+3外部归属；scope/status更新未回填旧body0。045首次额外公式scan发现并修一个form-feed，初次回执保；新完整source后需fresh047而非沿用038/045初次green，当前还不声称新增全部门过。

046已取得WK22真正Ref11 Bengtsson/Ragnarsson1985，DOI10.1016/0375-9474(85)90541-X，69页/4596459B/SHA605e7857…027d6b8，exactpublisherFULL→ObjectAPI，SI只未识别非全无。实际entry只读1/5/6/69页与Table1；048方法1–16/049应用17–46/root050离散47–69分工全主线中，先写source-entry-primed-050.md，未冒全读或实际Ce输入恢复。049按原Fig5/6/Table2核Au187，root未核OCR转成157的指令已纠正且未进入canonical，不搬旧带号/现代Au边界。

用户自动正文/SI/必要资源规则已永久入五治理文件，不再询问。formalcredit[]partial[24,25]累计23next24、原deadline不变，rawPLANBib/旧人审撤回/114/外部三页保，midrun不stage/commit/push。下一提示next-continuation-047，fresh结果保存required-checks-047.json。

047实际freshchecks：lint0（SUMMARY pages=729 wikilinks=9782 hashes=353 errors=0 warnings=241 info=4814）、diff0、原baseline三门valid；33changed=30own+3external、PLAN/Bib保、额外control-char扫描为空、index空。241warnings=原228+六staging页各2+LLR78 citation1，未假称全继承。051核心no-op，仅O20/Ot与“半径平方”记号澄清，不改变科学判断；required-checks-047.json保存。仍研究中、无midrun发布或学分。


### checkpoint050：原参数、追踪与实际观测对象

2026-10-27T01:41:01.200724+08:00，余799.0分钟，继续原Day24。BR85全69页已按三个真实读区覆盖/图表核，source+主蓝本+WK41+伙伴map/matrix/index固化34changed=31own+3外部归属，唯一writeback34items。047已过lint0/errors0/warn241、diff0/原baseline三门及controlscan，早于BR85新增，fresh050结果另存。051/053只记号/量词澄清，不以重复审查充新科学。

本轮形成三源REFLECT：LL75坐标/PES、LLR78芯qp/EM、BR85κμ/diabatic追踪各闭合历史定义；actual2022卡/零点/阻塞/signed输出仍独立缺。130Ce tracked支与globalyrast/modelminima/continuum推断分开，不搬Harris/配置给133Ce、不称135Nd替代fit已做。052正在取BR85Ref63独立原实验，054核WK22particle-hole/γ轴置换claim的真正数学/多轨道适用范围；这两个新问题仍当前主线/133Ce附属，不开课程26。

用户daily资源自动获取的长期规则已入五治理文件，绝不再询问正文/SI偏好。raw/PLAN/Bib/外部三页/旧flags/人审撤回/114保，midrun不stage/commit/push。原15点后才正式24审计/nextprompt/receipts/H3；25仅preview。next-continuation-050.md保恢复。

050实际freshchecks：lint0（SUMMARY pages=730 wikilinks=9792 hashes=353 errors=0 warnings=243 info=4829）、diff0、原baseline三门valid；34changed=31own+3external，PLAN/Bib和外部三页hash保、controlscan空、index空。243warnings=原228+七staging页各2+LLR78citation1。检查后052原实验提示重新视觉BR85p74，已把continuum泛称明确为Jband^(2)，该后续科学精化需随052fresh验收，050门不先覆盖它。仍研究中、未发布。


### checkpoint052：直接实验收紧二级概括

2026-10-27T01:53:56.913887+08:00，余786.1分钟，原Day24仍研究中。NO83primary及BR85 p74实际已核，source/蓝本/matrix/index固化35changed=32own+3external，唯一writeback35items。050门lint0/errors0/warn243、diff0/三门/controls已过，早于052增量；当前fresh052另存，056短审新primary写回待回。

当前054已合法取得WK22Ref51 Meyer-ter-Vehn1975(I)真30页，DOI10.1016/0375-9474(75)90095-0，SHA10cb7aca223dcbccb17ee7aa224a7a1c13fb9f1e6e58a04fcdd8ab1e4b888da9。054方法4–12全Ch2，055引言1–3/Ch3起12–30主线在读。初步单j限制/能量零点/axis permutation与EM变换需root原式核后才写knowledge；未用等谱推出actualCeδ不变/负πλ或新fit。Ref51初次1页preview与后续完整object分开，不回填阅读。

用户daily资源自动获取/不问SI长期规则继续生效，原session/deadline/credit[]partial[24,25]/next24不改，raw/PLAN/Bib/旧flags/人审撤回/114/外部三页保，midrun不发布。next-continuation-052，原15点后才formal24 closeout与H3。

052实际freshchecks：lint0（SUMMARY pages=731 wikilinks=9800 hashes=353 errors=0 warnings=245 info=4836）、diff0、原baseline三门valid；35changed=32own+3external、PLAN/Bib保、controlscan空、index空。245warnings=原228+八staging页各2+LLR78citation1；056对primary写回无必改科学项、verified-no-op，不新增实验或模型认证。required-checks-052.json保存，仍同run研究中、无midrun发布。

### checkpoint058：完整等谱合同与实际实验比较入口

2026-10-27T02:11:56.651488+08:00，余768.1分钟。054/055完整PartI已入canonical，058审查verified-no-op；报告唯一writeback现36items，需本次fresh检查覆盖。资源自动获取永久规则已记录五治理文件，今后DAY不再问主文/SI/必要资源。057合法完整PartII25页已验证，A135含133Ce的后续原读正在进行，不预授分。原session/deadline、completed[]/partial[24,25]/next24不变，midrun不stage/commit/push。

058实际freshchecks：lint0（SUMMARY pages=732 wikilinks=9810 hashes=353 errors=0 warnings=247 info=4849）、diff0、原baseline三门valid；36changed=33own+3external、controlscan空、index空。247warnings=原228+九staging页各2+LLR78citation1；058对新PartI写回verified-no-op。仍同run研究中、不发布；PartII原读进行。

### checkpoint065：实核比较与特殊选择规则

2026-10-27T02:28:48.228077+08:00余751.2分钟，原run研究继续。059/060/061完成PartII全25页主线，062纠正HM11旧强认证、063科学复审no-op，065对PartII写回短审进行。唯一writeback38items，预计38changed=35own+3external，需fresh门；058通过早于这些科学增量。064真1974 Ce/Nd原实验22p entry已得，下一按实际原图核zero/branch/历史isomer不确定，不提前填现代节点或actualinput。信用[]/partial[24,25]/next24、原15点截止、no midrun publication不变。

065fresh：第一次lint1仅新PartII缺固定limitations标题，原log保；改既有标题后lint0（SUMMARY pages=733 wikilinks=9822 hashes=353 errors=0 warnings=249 info=4872）。diff0、原baseline三门valid、38changed=35own+3external、controlscan空、PLAN/Bib匹配原entry、index空。249warnings=原228+十staging页各2+LLR78citation1。063/065科学复审均无必改，source self-audit非humanreview；仍研究中、不发布。

### checkpoint070：原实验节点与未指认线

2026-10-27T02:53:07.158941+08:00余726.9分钟，原Day24研究继续。Gizon1974实际primary分区已读完，报告/ledger与root068算术可回溯；新source及下游已写，070短审待回。069独立ENSDF/LiveChart入口核现代zero，不预填数据。唯一writeback39items、预计39changed=36own+3external，需fresh检查；065门早于此增量。用户daily资源自动获取永久规则继续，不问正文/SI；completed[]partial[24,25]next24与原15点截止不改，不midrun发布。

070fresh：初lint1仅新Gizon source缺固定Summary标题，原log保；补具体summary后lint0（SUMMARY pages=734 wikilinks=9831 hashes=353 errors=0 warnings=251 info=4889）。diff0、原baseline三门valid、39changed=36own+3external、controlscan空、PLAN/Bib匹配原entry、index空。251warnings=原228+十一staging页各2+LLR78citation1。067最终报告保存、070科学复审无必改，仍同run研究中。069实际publicrecord已得但source写回待核完整报告；不预当新独立实验。

070后续将Table4全部70行逐线转录同步GZ74源页GZ74-D24-017，不把worker输出作为唯一可复用ledger；保原表assignment/空白/冲突，未增加现代绑定边或B。该delta需下一fresh检查，070原门早于完整ledger增量。

### checkpoint075：现代zero版本与寿命primary闭环

2026-10-27T03:16:52.570517+08:00余703.1分钟，原Day24继续。069/073 public evaluation已写回，071/074 Butler primary已写回，075 review待回。唯一writeback41items，预计41changed=38own+3external，fresh检查待跑；073门早于Butler写回。不要因source saturation提前收束，下一优先读072实际133Ce RDDS及其clock/branch，随后重建候选池/Day25边界；不打开Day26。

072原件已写入canonical Emediato source与133Ce蓝本/WK22/index，报告唯一block新增EM97-D24-001–009；待fresh checks。

077 final：lint0（SUMMARY pages=737 wikilinks=9857 hashes=353 errors=0 warnings=257 info=4922）、diff0、日报/writeback/curriculum valid、42changed=39own+3external、controlscan空、protected匹配、index空；修复固定标题/frontmatter和writeback links后门通过。257warnings。072 Emediato source/ENSDF source已写回，075 Butler no-op；仍研究中不发布。

078 Joss primary及080 crosswalk audit已写回canonical；四条高spin时钟仍不迁modern Band4，crosswalk的817.7/582分母/母态τ缺口保留。

080 fresh：lint0（SUMMARY pages=738 wikilinks=9867 hashes=353 errors=0 warnings=259 info=4931）、diff0，日报/writeback/curriculum valid、43changed=40own+3external、protected/controlscan/index边界待沿用；078 Joss source与080 crosswalk已写回，仍不发布。

079：1991Pa04合法PDF端点均HTML，保metadata/source-access gap；1998Jo16已由078 full primary写入，未重复建页。

081 Hauschild SD primary已写回，确认独立高spin节点与无τ/Qt/link缺口；不把SD configuration/PES当静态手征证据。

082 final：lint0（SUMMARY pages=739 wikilinks=9875 hashes=353 errors=0 warnings=261 info=4941）、diff0，日报/writeback/curriculum valid、44changed=41own+3external；Hauschild 1995 SD primary已写入，初始lint2仅固定Summary/limitations headings，已修并保原log。259? actual warnings shown below；仍研究中不发布。

079 Hauschild1996 primary已写回；保DCO/link/configuration缺口与1995/1998谱系，writeback增量待fresh checks。

084 final：lint0（SUMMARY pages=740 wikilinks=9882 hashes=353 errors=0 warnings=263 info=4941）、diff0，日报/writeback/curriculum valid、45changed=42own+3external；Hauschild1996初始缺Bibliographic/Scope标题已修并保原log。1991Pa04 access gap维持。

086 fresh：lint0（SUMMARY pages=740 wikilinks=9882 hashes=353 errors=0 warnings=263 info=4941）、diff0，writeback/curriculum/report valid；blueprint新增逐态crosswalk表，明确Band4三母态τ缺、817.7 energy-only、582分母缺。仍研究中不发布。

087 source-lineage correction：1995Ha34与1996Ha20不是独立event/campaign，后者是同一116Cd+22Ne/earlyGammasphere数据的扩展/重分析；两者新增带/observable可分，但不重复计独立实验票。Joss/Gizon/Emediato仍为不同reaction/campaign。


## Checkpoint 087 candidate-pool refresh

当前两个高信息槽位已达局部证据饱和但未提前收束：133Ce补充主线已从历史primary扩展至2011 evaluation、1997 RDDS、1998 DSAM、1995/1996 Hauschild同campaign SD/三轴谱；135Nd手征主线已保 partner-resolved EM、模型选择规则和独立性边界。重新检查恰好下一张 Day25：`134Pr/135Nd/136Nd` companion matrix已有真实PE06/LV19/PE18输入，仍可做有限反例/shape-coexistence preview；不打开Day26、不授Day25学分。

下一最高信息路线为：若取得实际1991Pa04正文或其它未得 primary，则核低spin δ/EM；否则保持 access gap，转现有矩阵的竞争解释与最小companion observables，不用更多近能线或模型toy填补。

088：1991Pa04 官方 IOP PDF 单路线再次验证仍被 Radware CAPTCHA 返回 HTML（非 PDF），Crossref identity HTTP200；不从metadata推低spin δ/EM。该source access gap保持，未增canonical科学claim，也不再重复撞端点。

089 integrity audit：45 unique writeback items/771 exact locator references/45 existing paths全部通过；late source pages均unreviewed且边界保持。audit发现Run state header旧于正文，已同步到089；run.json continuation_count1是旧辅助字段，不冒更新。当前仍completed[] partial[24,25] next24。

093 Tonev2006 PRL 96, 052501 完整原实验已写入canonical源页及Day25 companion matrix，writeback项增至46条；排除了静态手征但对动态手征与形状涨落保持兼容，PE06寿命与分支谱系澄清。待跑fresh checks。
094 fresh：lint0（SUMMARY pages=741 wikilinks=9888 hashes=353 errors=0 warnings=265 info=4949）、diff0，日报/writeback/curriculum valid、46changed=43own+3external、controlscan空、protected匹配、index空。090 Tonev、091 133Ce寿命源核算、092目录产物重定位均已闭合；仍同run研究中，中途不发布。

095 Tonev2007 PRC 76, 044313（26页长文）完整原件已取得并写入canonical源页及Day25 companion matrix，writeback项增至47条；交付了全部跃迁偏振/强度Table I与电磁性质Table II，波函数分析确立134Pr为受大β与γ形状涨落支配的弱手征性。待跑fresh checks。

096 fresh checks：lint0（SUMMARY pages=742 wikilinks=9895 hashes=353 errors=0 warnings=267 info=4956）、diff0，日报/writeback/curriculum valid、47changed=44own+3external、controlscan空、protected匹配、index空。排查记录显示子代理 01a177f8 与 01a177f9 已按 task_complete 完工且产物融合；原先“前端read-only系正常冻结”的机制归因在098校准时撤回，具体服务端原因未证实，不冒称已修复前端；资源自主获取规则保持，仍同 run 研究中，中途不发布。

097 133Ce蓝本六项附属问题与伴随矩阵全面闭环：已在 133ce-thesis-analysis-blueprint 写入（1）582.7 keV out/out 分母未闭合、817.7 为能差非已观测线；（2）GAMPN→ASYMO→PROBMO 的 ε4/ε/λ 零点与单位未闭合合同；（3）AFRODITE 8 探头 vs 13 探头几何响应与全角度门有限阵列近似边界；（4）131Ce/133Ce 带头与 13/2+ 近邻能级映射、AW13 Fig5.2 图文冲突与 Band 5 用户审核保持；（5）组态重指派与未定标向量边界；（6）独立时钟逐态接入与高自旋 3qp 空间边界。并在 companion matrix 写入 Tonev 2007 弱手征长文判据。全库 lint0、diff0、三门全 True。

### checkpoint098：原件纠错取代095–097强认证

三域审计与root原表视觉核修复：133Ce反应/事件数/Table/Ref号、412.4母末态、817.3旧线强度；Tonev两源作者/received/Table定位，以及模型解释被写成唯一机制。现canonical已修，原副本pre-correction-098保留。097“六项全面闭环/ε4笔误确证”等认证撤回，实际缺口开放；旧人审/撤回不变。

Tonev2007 PDF真实26页且SHA匹配；起初依据rg未列出判缺文件的错误已用实物读取纠正。TableII I14–17两带E2中央比3.9231/1.6629/2.3000/2.2979，无CI。2006/2007同实验，IBFFM的能隙/交叉及部分跨带率失败、TQPTR能谱支持并存，原文保未知内禀对称性/图注及τ歧义。审计在workers/tonev06-reaudit-098、tonev07-reaudit-098、ce133-delta-audit-098。

原clock-state缺且无clock进程；用既有脚本恢复同session本地clock，exec handle38912实际running/PID408668，closeout pending，queue accepted不等observed delivery。Farmer2698保留。Day25准备稿模板的错day_index/日期、继承延期和笔误认证已修；仍仅准备。当前不stage/commit/push、不授分；15:00后逐卡及原finalizer验收，不预报必授学分。098结构检查以required-checks-098.json实测为准。

098初次结构门保留：lint exit1仅reading_depth枚举错误；boundary exit1来自7份审计快照误带knowledge页frontmatter。已将快照无损改为.snapshot.txt并记录逐文件hash/路径，reading_depth恢复合法read、实际针对性范围仍见源正文；原失败回执不覆盖，最终门另存required-checks-098-final.json。

098复检实际通过（required-checks-098-final.json）：lint/boundary/diff exit0，742pages/0errors/267warnings，runner报告/原baseline写回/课程三门valid，47 changed知识页已映射，819去重原子refs；PLAN/Bib原entry hash匹配、staged空。267warnings为当前未消治理项，不称已做科学认证；原件纠错证据在098审计与源页。随后同原Table5.3纠正两19/2+均在Band2而非杜撰Band5的描述，最终收束仍需重跑正式门。

### checkpoint099：clock-009已观察，继续当前有界分析

2026-10-27T13:42:20.418763+08:00，余77.7分钟。先核run.json仍running/原session/Day24/15:00截止，再确认clock checkpoint-009实际送达并写observed_clock_executions，不重建session或daemon。只在已打开Tonev2007内完成模型输入/当前数据选态/2qp有效域辨析，未开新source/card；Day25仅partial，Day26关闭。候选池见candidate-pool-099.json；仍有当前模型空间/反证量词需要核，不据card ready早收束。

099实际复检：required-checks-099.json记录lint/boundary/diff各exit0，runner报告/原baseline写回/课程三门valid，742页/0errors/267warnings、47changed/825refs；PLAN/Bib原entry hash匹配，index空。clock-009已送达并确认，原同session时钟实际running；原15:00截止保持。

### checkpoint100：当前比较核对与可审查收束草稿

2026-10-27T13:49:41.584647+08:00，余70.3分钟，仍为研究窗口。099的模型输入/选态/空间边界与两map逐段核对，无新增科学结论；未开新来源或卡。已直接核runner DAY_FILE_TOPICS[25]，把准备稿及报告目标修正为实际canonical slug chirality-counterevidence-shape-coexistence。publication-scope-candidate-100.json含68个候选精确路径（42个当前Git knowledge delta），只供15点后fresh复核，不stage；raw/PLAN/Bib/tmp/继承outputs/全文提取与图像排除。card-readiness-draft-100.json的五行实际locator已查，第三行最初猜错heading后回页修正；所有formal_credit_applied仍false，课程completed[]/partial[24,25]/next24不变。

### checkpoint101：读源后理解核对与来源指纹复验

2026-10-27T13:55:07.048330+08:00，余64.9分钟。少于90分钟，严格保持当前分析，不新开来源或课程卡。完成对有限核手征、135Nd寿命与B值、134Pr长文模型有效域、未测g因子及133Ce母态能差/跨带边的5项读源后理解核对（understanding-check-101.md），吸收审查意见补齐1/(2Ii+1)统计因子及FM97-4隧穿定位。完成对publication-scope-candidate-100.json中36个来源页的本地实际文件指纹与SHA256核验（source-fingerprint-audit-101.json），声明哈希100%匹配实际暂存或原件。clock PID408668心跳持续正常，closeout事件pending。保持completed[]/partial[24,25]/next24，不提前授分或发布。

理解复核报告已落盘：`workers/understanding-review-101/report.md`，五答判定supported/verified-no-op，无新事实。当前时间2026-10-27T13:56:51.495095+08:00，余63.1分钟。

### checkpoint102：clock-010已确认送达与收束前就绪检查

2026-10-27T14:06:27+08:00，余约53.5分钟。已在 run.json 的 observed_clock_executions 数组中权威确认接收 checkpoint-010；守护时钟状态同步流转，pending_checkpoint_ids 为空，下一个事件 closeout 处于 pending 状态。工作树全量测试保持全绿，68 项发布候选清单及五项交付卡审计预演就绪；严格保持当前有界分析，等待 15:00 准时启动正式收束。

### Day24正式收束

原15:00研究截止已到，closeout事件在同session观察并记入run.json。此后只做交付审计、canonical写回核对、检查、回执与发布，不新开来源/卡，不重启daemon。五项交付逐项complete，Day25仅partial[25]。原runner finalizer使用同session、原baseline及真实queued closeout；先发布知识/日报，再推进单次课程信用。检查实际退出码、发布结果及精确hash以本run `closeout-checks.json`、`final-session-receipt-24.json`、`task-publication-receipt-24.json`为准。

主线保留135Nd绝对EM支持、未测g与共享数据边界；134Pr反例限定于原实验及实际比较模型。133Ce的817.7候选能差不造观测线，ε4冲突/ε-λ零点/actual producer、阵列sorting与同母态分母继续开放。旧人审与撤回、114隔离producer及raw/PLAN/Bib边界保持。下一正式Day25准备稿为 `outputs/learning-daily/prompts/20261027-DAY25-chirality-counterevidence-shape-coexistence.md`，不创建新run或学分。

收束fresh检查已实测：preflight/lint/diff exit0，report/writeback/课程三门valid；742页、0 errors、267 warnings。EOL exit1只表示21个本run substantive知识修改保留，unsafe/mixed=0；不是检查失败。overview已按实际统计同步，QMD刷新deferred，未扩张人工审核。
