# Day22：wobbling几何、声子与观测量

## Run state

- run_id: `2026-10-24-day-22-01`
- day_index: 22
- session_id: `01a16ccb-2ecb-7501-ae47-fb2d58c270da`
- timezone: Asia/Shanghai
- overnight_until: `2026-10-25T15:00:00+08:00`
- closeout_window_ends_at: `2026-10-25T16:00:00+08:00`
- completed_day_indices: []
- partial_day_indices: [22, 23]
- next_day_index: 22
- research_status: active
- formal_credit_applied: false

本页是checkpoint092重建的当前报告，不是最终session receipt。001–090旧叙述及119项结构写回存在重复/过强认证，历史保存在run内pre-correction-091、pre-correction-092和historical-writeback-through-091.json；历史不是已解决科学问题清单。091撤回19项无充分依据认证，092进一步以163Lu两篇原实验校准活跃观测页/概念页。结构检查不认证source truth。

## Session identity and inherited Day21 gate

原始runner回执截止、当前CODEX_THREAD_ID与事件身份一致，见[session identity](20261024-DAY22-wobbling-geometry-phonon-observables-run-01/session-identity-001.json)及[run.json](20261024-DAY22-wobbling-geometry-phonon-observables-run-01/run.json)。没有创建第二schedule session。Day21 final/card-credit回执只授[21]，分数18/24（各维3/4）；正式commit已在缓存origin/main祖先链。其H3文件是收束前fetch/ancestry/dry-run记录，不能直接替代最终push事件证据；正文尾部仍有active旧字样，与final receipt不一致。保留正式[21]学分，不据其复活过强科学结论。

## Candidate pool and selection

| 当前路线 | 信息增益 | 仍缺什么/下一步 |
|---|---|---|
| F14/H03几何与谐近似 | 原轴号、曲率/稳定性、非谐矩阵元限制可直接纠错 | 完整QTR/波函数没有重跑；勿用R≈I−j替代量子核芯分布 |
| 163Lu原实验（本轮主线） | 识别electric偏振选解与绝对寿命、双根相对B及Δn≈2退激的对象 | Ref.7 Schmitz1993寿命原文未得；F14 Ref.25字面书目落在165Tm，实际Lu数据来源待追踪 |
| 135Pr支持/反方 | 同一逐线观测向量能检验近简并＋强E2是否足够 | 旧正文δ/分母/独立性已有记录，仍需清理任务泛化与假数值 |
| 130Ba/136Nd两准粒子控制 | 原文M1占优仍支持TW，反驳任务自创通用E2硬门 | 新观测需超出模型单点定标；旧11倍DSAM表映射未成立 |
| Day23唯一允许预习 | 支持—反证—数据依赖与组态重指派问题 | 仅无学分预习，不正式计卡、不打开Day24 |

## Sources and evidence

| 来源 | 本轮实际覆盖与locator | 身份/独立性 |
|---|---|---|
| [[frauendorf-2014-transverse-wobbling]] | 既有全文记录；091定向核014322-6 Eqs.11–24及p.10 M1讨论并视觉核Eq.21 | 理论HFA与完整QTR不同；Pr实验数来自发表前通信，非新增采集 |
| [[hamamoto-2003-quantized-wobbling-excitations-alignments]] | 既有5页原件记录；091定向复核014319-4 Fig.4及结论 | 理论比较既有163Lu，允许非谐Δn≈2强度 |
| [[odegard-2001-evidence-wobbling-163lu]] | 092全文4页、视觉5868/5869，SHA 0ff38adfcbe031fb21c43b3bba290ca44a21898564bb78cf335fbb47b05ba379 | 152MeV Euroball IV采集；引用早期Qt不等于本篇测寿命 |
| [[jensen-2002-second-phonon-wobbling-163lu]] | 092全文4页、视觉Fig.1/Table I/Table II，SHA c6fd99c17c09763f742cbe36443f7039f21b3e28a5caa548748bdf0718630a8a | 新157MeV/6×10^9采集；仍依赖旧一声子δ/指认 |
| [[chen-2019-transverse-wobbling-even-even]] | 091全文5页、视觉Table I；R091条目 | 复用早期130Ba谱学＋CDFT/PRM，不新增实验 |
| [[lv-2022-transverse-wobbling-136nd]] | 091原件8页含自归档封面，视觉034302-4/5；R091条目 | 同既有JUROGAM批次，仅一条联合P–Rac；相对比/单点模型定标 |

全部新增原子条目needs_review: true；不设置human-reviewed、不改raw/PLAN/受保护Bib。其余旧追加未逐claim复核，不代表全文source claims一概无效。

## Theory/analysis exercise

在F14约定下，j平行/垂直最大惯量轴分别为longitudinal/transverse；数字轴号需跨文献映射。声子标签另要求检验所用谐近似/阶梯，不由两条带的几何或相似能量自动给出。完整模型拓扑、小角有效域与实测电磁量必须分开。

同一混合线的E2光子份额为δ²/(1+δ²)，与两条退激线的B(E2)out/B(E2)in是不同量。rM1还带μN²/(e²b²)单位。缺寿命不能报绝对W.u.；但同母态寿命抵消使相对比仍可检验模型。

## Four-column evidence exercise

| 候选带/原子出处 | Band energy | In/out strengths | Alignment | Polarization |
|---|---|---|---|---|
| 163Lu TSD2/TSD1；OD01-D22-001/002/003、OD01-D22-R092-1 | 分离250–300keV、随spin下降；九条连接线 | 平均δ=−3.10(+.36/−.44)，90.6(1.3)% E2；Table I在43/2→41/2给λ=.36(.04)；相对强度比较，不新增绝对寿命 | 相近i_x/J(2)，Fig.3参考25ω+45ω³；σ/I=.25(.02)是另一类磁子态宽度 | 源文以electric性质排除−.22根，未打印可引用的P正负/数值，不写“P<0基准” |
| 163Lu TSD3/TSD2；JE02-D22-001/002、JE02-D22-R092-1/2 | 新四条ΔI=1；另八条TSD3→TSD1 ΔI=2 | 476/627同母态λ=.14(.04)；rE2大根.51(.13)、小根.019(+.024/−.017)，无新增τ | TSD2/3相对i_x差约.1ℏ；Fig.4用62ℏ²/MeV刚性参考；支持family | 476统计不足未测偏振；作者用family/PRM支持大根，非实验排他选解 |
| 135Pr side/yrast；M15-D22-001至003、L22-D22-001至004 | 下降曲线仍可保留；新谱重组旧TW2网络 | Matta的813 rE2=.843(.032)与Lv的813.2/726 rE2=.12(.08)需各自输入/谱系；747/526=.7(+.7/−.5)是两带间支路 | QTR重取向是模型结果；不是i_x直接测进动锥 | 不同采集/分析有冲突；新联合P–Rac给小δ，不能称同一拟合面的两根 |
| 136Nd L3/L1；LV22-D22-R091-1/2 | Eq.4/Fig.4下降Ewob | 751 δ=−.48(+.13/−.14)，rE2=.36(.17)、rM1=.61(.29)，不是绝对B | 两准粒子刚性j=10是模型输入；参数按数据定标 | 仅751可分析，其余三条污染/弱；约19% E2仍被作者解释为两准粒子TW |
| 187Au band(2)/(1)；AU20-D22-R094-1、GU22-D22-R094-1/2/3 | 上升Ewobb可由两方不同结构解释 | 2020四线大δ及相对rE2最高约.7；2022两线小δ，数W.u.是外标估计 | PRM中部λ、QTR底部轨道是相互冲突的模型输入；无直接主轴j测量 | 2020未测links P；2022 P–Rac放开σ/I、借外部Q，误差较大 |
| 105Pd B/A；TI19-D22-R103-1/2/3 | Ewob降至29/2；≥33/2组态不同，升能差不直接判LW | 三线rE2=.66/.60/.34、rM1=.162/.089/.029为相对比，无新τ | CDFT β=.27/γ25°及ab惯量是模型/拟合；A/B高spin对齐组态分别处理 | DCO+负P支持大正δ；1034是g_eff模型定标点，非独立模型预测 |

## Counter-evidence and missing companion observables

135Pr说明早期E2-rich连接/下降Ewob的模式指认会受独立小δ观测挑战；强E2本身也不唯一决定声子。不能反向声称TiP唯一正确，更不能把所有M1占优候选判磁转动。两准粒子130Ba/136Nd的原文正是检验旧普适硬门的控制例。

## Citation-lineage countercheck

F14 p.10将163Lu弱M1数据指向Ref.25，但p.12书目为H.J.Jensen等NPA695,3(2001)。本次核本地48页原件首页/摘要，实际研究165Tm；本轮未读其全部48页。此为引用链身份疑点，非Fig.19数据错误证明。两个source已互链，实际Lu绝对B数据原始来源仍待查。

## Checkpoint092 quantitative reconstruction

脚本system/scripts/day22_lu163_relative_strength_audit.py核JE02原件SHA，以λ=.14、Eout=476、Ein=627及两δ中心重建rE2=.515407/.019344、rM1=.006282/.084648。首次对大rE2套仅输出末位±.005时失败（偏差.005407）；随后正确传播输入末位舍入得到相容box。这只检打印中央算术，不是实验jointCI、模型验证或新的绝对强度。

打印.51/.019≈26.84是替代选解敏感性，不是观测到的物理暴跌；.51/.21≈2.43还含不同带内分母尺度，不能独立等同于绝对两倍玻色子规则。JE02有限Δn≈2强度由非谐性解释；不能写成“无交叉线”或单据此排除所有wobbling。

## Checkpoint093：谐声子、完整拓扑与表示分层

本轮定向读Lawrie2020原件034306-6–11，核Eq.34/Table I及作者Summary；CF22定向核p.3–4、14/19–20、26，视觉核p.26；F24定向核p.14 Eq.26–27并视觉核。未把这些定向读取重称全文复读，未使用有勘误问题的CF22 Fig.15作新的高阶图像判定。

Lawrie以小角/声子式n量子化定义wobbling；CF22 Sec.4.6直接回应，称其TiP在本文术语下为非谐wobbling。定义差异不等于实验已统一：135Pr不同δ结果仍需实际响应/逐线比较。小角f失效、完整量子拓扑与实测强度是三个不同问题。

任务代数显示正曲率下f≥(2n+1)/I，共同正标度Ak不改f但改频率；按Lawrie Table I(vii)Lu打印输入，受限网格最小f1=.31599、f2=.52665。旧“横向Lu .10–.18因此充要有效”不应恢复。

SSS实际由均匀K振幅的局域态生成，其一维概率是密度矩阵有限Fourier和。旧045把它等同于某个Bogoliubov惯量压缩态的定义撤回；基底的窄角分辨不是新测核γ刚度。hfa-sss-controls-093.json的6项归一/正性/条件代数控制均通过；首次JSON序列化因NumPy bool失败，转换为原生bool后成功，这一技术修复不改变科学输入。

寿命路线仍开放：Hagemann2004书目已定位，未下载/读取新原件；缺失的绝对数据来源不靠review再引用补齐。继续Day22或恰好Day23无学分预习，不开Day24。

## Checkpoint094：187Au的P/δ身份错误与独立性纠正

Guo2022主文p.3的−.10(5)是旧测量polarization P；新Fig.3打印δ为−.26(+.16/−.15)、−.28(+.23/−.69)。旧任务把P当δ才产生约88倍的E2份额变化。按实际δ中央值，在保持相同光子分支/能量/分母的条件下，份额敏感性仅13.850/12.363；不同实验没有共同响应重拟合，不将其称实测物理塌缩。四项打印输入/错误诊断控制通过，见pr-au-branch-sensitivity-094.json；813同母态重建rE2=.118129、rM1=.397851接近Lv打印.12(.08)/.4(.3)，无新τ或绝对B。

SI六页实际方法区分a(E)本地标准源标定与Q(E)借同型探测器Zheng2013曲线，δ区间由穿过P–Rac误差矩形的全部σ/I曲线构成，不是公开完整joint-likelihood。αK面板把本文δ换算后与历史conversion比较；这不是本次新测第二套独立电子谱。数W.u.依赖外部100–200W.u.尺度，旧1.1e−4 e²b²无本文依据。

Sensharma2020的band(3)明确是signature partner，作者没有找到n≥2带。Guo独立数据未复现、把相似序列归188Pt，构成身份挑战；不能据此自动重写Sensharma原事件或声称二声子带已被证伪。两方PRM/QTR的Fermi位置、γ和模型空间不同，主轴角动量不是实测。项目/问题/概念页恢复开放争议，历史错误原文保存在pre-correction-094.json。

## Checkpoint095：135Pr逐线身份与条件χ²证据

实际视觉核Matta Table I、Lv Table1、SH26 Fig12；回读Matta/Lv主文物理段及Lv SI p1/4/5，SH26只定向PDF14–15。747的P+.04(+.08/−.13)配δ−.47；813的P−.03(+.05/−.12)配δ−.37。旧“+.04/−.37/3σ”混线认证撤回。Matta A不是Lv P，不能借别的阵列Q直接比较；747实验rE2/rM1为空，不读取QTR列作实测。

813同母态重建.11813/.39785说明Lv打印比值的算术来源；.843/.12=7.025为不同实验中央相对比，固定其它输入只换δ的份额因子约5.84。两者不同，不称物理或绝对B的7倍塌缩。

SH26原件Fig12在σ/I=.2下确实偏好大δ，作者认为多角度A2/A4可区分两局部极小；本任务保留这项条件支持证据。旧“σ/I自由后必等深”未经共同拟合，撤回。条件曲线也不自动等于完整profile或未知dof下的σ数。Matta p5与SH26 p15明确完整QTR允许j重取向，不能将HFA冻结等同完整实现；两派MoI/模型输入差异仍开放。

135Pr项目恢复开放，Day23预习的三模式方法页撤去统一δ/β/f/W.u./Δix硬门，保留可操作的逐量比较。SP/TiP/剪刀不是仅凭M1主导可作的排他分类。旧137Pr/108In黄金数值未在本次核验，移出活跃合同并保存pre-correction-095.json；原source既有事实不因此一概否定。

## Checkpoint096：A4的条件识别力与物理布居反例

定向核Yamazaki1967原扫描pp1–3及p19的三行（17/2→15/2），非重新通读23页。CG三角条件使rank4只剩E2²项，故已知非零C4=ρ4F4时，x=A4/C4可给|δ|=sqrt[x/(1−x)]；A2非零干涉可补符号。一个A2方程不保证恰有大模/小模各一，也不能断言角分布总须偏振才能选根。

保持取向未知则另有问题：用表中五位F系数、人工ρ2=−.02与ρ4=.02，δa=−1.4和δb=−.5640849给同A2、不同A4；将后一组ρ4改为.05486356，两组合法对称归一布居给全部同一角多项式。最小概率>.05；六项正性/张量/归一/多项式控制通过。它只是未知独立张量的存在性反例，不是Pr数据拟合、Gaussian族内等深证明或实验CI。

旧混合比观测页和高spin综合中的通用P正号、5%Q门、固定A4误差及“仅偏振可定解”认证已移出活跃部分，保存在pre-correction-096.json。此结果解释SH26条件AD信息与取向边界可同时成立，不抹去Lv新P–Rac的实际冲突。

## Checkpoint097：未核追加退出活跃知识与生成链

以baseline.json的启动SHA逐文件核对当前HEAD，全部被处理的tracked knowledge基线均一致，确认是本run修改而非用户遗留。48项恢复/定向修订见quarantined-knowledge-additions-097.json，内含修改前精确文本/哈希。未列入001–006或091–096实际原件审计的Day22“终审/充要/全区排除”追加回到启动基线；5个已纠正源页只移走旧未证preamble，保留R091+条目及原source事实/review。原问题队列保留开放，追加五个本轮已核问题；索引去掉88倍等错误描述。

114个未跟踪、run-owned的旧断言/生成/checkpoint脚本先完整归档到retired-producer-scripts-097.json，再逐文件移出system/scripts；这是可按原文恢复的历史代码，不作活跃生成器。保留6个已限定范围的模型/强度/表示控制脚本及既有day14 helper。没有递归删除、raw/PLAN/Bib修改或daemon动作；错误历史输出仍保留但不作为知识事实。

这一步没有新增核物理结果，也没有证实所有旧claim错误：它撤回的是未被本轮实际原件审计支持的认证与不安全生成链。它不把恢复后的旧review或source文字升级为本次新审核。后续研究优先补一条独立的磁转动/寿命对照或Lu绝对数据谱系，Day23仍仅无学分预习。

## Checkpoint098：独立磁转动原文与未闭合输入

Day23仅无学分预习：137Pr原件物理主线pp1–7及108In pp18–19/21–23提供独立比值与寿命链。137Pr B(M1)/B(E2)先升至37/2再降，作者解释3qp/5qp交叉；无绝对τ，不能认作绝对B(M1)下降或测剪刀角。108In TableV则有DSAM/branch/ICC导出的B(M1)：Band2 14−→16−为.911→.398；Band3 18+→19+从1.71升5.22，作者以alignment重开解释，模型高spin仍有偏差。旧7+→10+假轨迹撤回。

量化重建首次十组比值“全部3%内”假设失败。视觉重核TableI后确认43/2的507.2keV/5.7和972.1keV/1.1打印强度给24.0288，而打印B比18.5，末位舍入不能解释。原文仅说明弱E2取多门平均，缺逐门账本，暂不能判归因。不调输入强配；mr-ratio-first-nonclosure-098.json保留首次失败，后续文件明确中心未全复现。五项控制验证具体算术、保留不闭合与相对比不能确定绝对因子的正例，而不认证整实验或新CI。

## Checkpoint099：Lu寿命对象与同核SD–ND E2反例

定向读DO99 printed381–382、387–391，视觉核385Table1、387Eq1及388Eq2，另核OD01 printed5867的前身/新实验段。1999的SD2候选即OD01新152MeV EuroballIV建立九条links的前身；不能把旧未连状态误当2001仍未连。QSD=10.7(.7)b与QND=6.0(.5)b均引自Schmitz1993Ref2，并非DO99新τ或新SD2绝对B。原Schmitz全文仍未得。

DO99两态混合是2087/2198keV同21/2+ ND和SD1，而不是SD1/SD2。原打印分支经E^5修正给r1=.0402746、p=.0387153、r2=.00954208、QND/QSD=.486750；实对称两态H重建V=21.4136keV、各态排斥4.2974keV，与作者22(3)及约5keV相容。五项指定控制通过，没新CI或绝对B。Table1的697.1线有与相近SD线未分辨的脚注，不能将强度/一致性检验当独立干净分支；原门谱分离仍未知。

同核强E2脱带/相近能量态可由SD–ND混合解释，说明带外E2与近能量不能独立给声子标签；这是作者模型条件下的具体控制，不是新排他裁决。其Q比与引用寿命相容也不新增独立τ证据。

## Checkpoint100：TSD3同母态双带外E2比

视觉回核JE02 Fig1/TableI：45/2+ TSD3的1119.2→TSD1(41/2+)、476→TSD2(43/2+)与627→本带41/2+共母态。两个out/in相对比共627分母，故商可消去τ和带内B；打印.018/.51=.03529或.018/.019=.94737，直接λ/能量式给.03533/.94141。只是打印中心，不造jointCI；476δ和原多极赋值仍是输入。

此处与跨不同母态的.51/.21本质不同：前者是同母态双出口E2比较，后者含不同带内尺度。新比值显示大根下直接到TSD1的E2弱于邻带出口，小根下可比，但复用原计数/δ、不能当独立选根证据。有限Δn≈2与harmonic limit/非谐模型需一起比较，不自动否决所有wobbling。重用已核Lu比值脚本保存新增字段，未创建新实验或增加脚本数量。

## Checkpoint101：勘误图与RMS/SCS信息边界

CF22一页Publisher Erratum实际全文/原图核验：替换Fig15的行标Iν下标2是同spin第二态，不能当每行n=2；主文讨论的是selected n2/3。主文p16明确近等距能量可同时有B(E2)不按n的非谐行为，故图/谱/矩阵元分层仍必要。

采用原文D2允许的I4空间构造两组正、归一的人工混合态，三RMS平方均20/3，第四矩却为1408/15与1312/15，SCS图不同。单位立体角积分均1，六控制通过；不是同Hamiltonian本征态/Pr拟合，也不赋TW/LW/flip标签。Q按dΩ归一、源圆柱图P=Qsinθ；不同测度峰宽不能直接比。对实际模型应核可测能谱和跨spin矩阵元，不能把RMS或SCS图当实验直接几何。

## Checkpoint102：135Nd的带族、手征与继承统计量

MU07四页正文和TableI/Figs2–4回读保留原作者的手征支持解释，但撤回继承的过强排他语句。五个sqrt[B(E2)B/B(E2)A]中央比均值.935616、跨spin总体SD .010156，不是实验Qt置信区间；37/2→39/2中心E2降幅2.4615/2.6364，商1.0710，不是旧2.57/1.043。Qt与内禀形状仍需几何模型。M1为Fig2、E2为Fig3，有限图点相关/差分不构成全spin100%机制唯一检验；原文明确近失稳点非谐倾角可改变E2，RPA临界点与实测最近点亦有差异。

核chirality由time reversal关联左右手、space inversion不变，两带同宇称；旧“宇称隧穿”需改。寿命比接近1或B中共同τ抵消不指定实际Cov/相关系数/静态手征硬阈值。

LV21定向核setup/TableII/Summary：低spinD1/TiP1/TiP2单νh11/2家族不等MU07三准粒子A/B手征pair。同核不同组态不能互作否证。LV21和Lv2022Pr的152MeV、薄靶、JUROGAM39Ge及5.1×10^10事件相同，是共享campaign强候选；未有run/eventledger前不计两次全独立校准、也不称逐event完全相同。原Day21正式[21]/18分不变，修订的是科学推断范围。

## Checkpoint103：105Pd独立正常形变支持与校准点

实际回读Timár2019六页（五页main与第六页refs），视觉Fig2/TableI。其EUROBALLIV/DIAMANT与96Zr+13C采集独立于Pr争议；联合DCO/P支持991/1034/994大正δ=1.8/2.3/2.7，P为负，E2中央份额.764/.841/.879。作者明确DCO可有小δ而P不支持；这是实质支持证据，不能因其它核的反证全部抹掉，也不靠跨实验P符号定律。

三线rE2=.66/.60/.34、rM1=.162/.089/.029仍为相对量。C带1158/1159只能合并P且缺DCO，允许大小δ域；A/B与C约束不同。CDFT/PRM形变和惯量来自模型/能量拟合；额外g_eff×.36按1034δ定标，固定波函数/E2时M1×.1296、δ×2.778。定标点不作独立预测，其余同源派生量也不当额外实验。I≥33/2两带组态改变，后续能差上升不能单独判LW。

## Checkpoint104：IBFM例外、转引误差与整向量比较

定向核NOM22模型限制/电磁分解/TableII，非新11页全通读。反方作者保留105Pd实际实验冲突；127Xe低spinδ=−5.699/−4.901的模型例外来自近零M1及半填充敏感性，不能称全四核必M1主导或理论已证TiP。二手TableII的105Pd994rM1误差±.057与原TimárTableI±.016不符，比较须用原实验版本，未推作者程序实际用何数。

任务条件代数：固定状态/E2，整个M1算符（boson+fermion一起）乘η=.817/2.3=.355217，可使三个IBFMδ约2.047/2.300/2.396；rM1乘.126179而rE2仍.389/.236/.182。它不是作者重拟或只改某个奇粒子g，说明一个δ标度能改变比值而不修复整套E2/M1向量；不报新χ²/CI或理论排他结论。三canonical页写回，raw与原review范围不改。

## Checkpoint105：QRPA耦合、图量与原始数据路线

nature-downloader取得Ref67的CHORUS accepted稿（13PDF页含封面，SHA7204f8de…f5bc），实际读main12页主线并视觉核PDF11/12；tool把版本标publishedVersion，但封面明确accepted，保留人工版本纠正与默认APS许可，不称VoR/开放重用。SI按当前自动任务取正文，SI状态未核。公开缓存只读，未写raw或正式新增source；现有F24原件的targeted claim review及canonical方法同步，获取/范围回执在literature-acquisition。

Review p21 Fig35轴为绝对B(M1)out(μN²)，图注/文字却称rM1；accepted原稿Fig13也为绝对B，引用时必须锁定量。QRPA的LL耦合质子/中子轨道current的isovector scissors，改善频率和M1而E2仍偏低，不等同磁转动shears或通用g淬火。Review邻核164Yb转述与原稿162Yb/无直接1+谱、只比总M1系统学的限定不同；不把它改报成独立邻核实验验证。

原稿Ref17把Lu绝对量路线指向Görgen2004 PRC69,031301，Crossref题名已核。通用OA搜索未得、APS正文403/harvest401；SemanticScholar另定位LBNL/eScholarship仓储候选qt5fv6f0xv，正在核原件身份，尚未把候选当已读寿命数据。GoogleScholar超时及无命中arXiv结果保留，不是全局研究阻塞。

## Checkpoint106：零谐曲率与非零有限能隙

源F14冻结j形式的条件族`A=(3A0,A0,2A0),j=J/2,J=√I(I+1)`令HFA c2=0。保留正J3分支的四次项，领先临界算符为`2A0J p²+(A0/4)q⁴`；能隙尺度`A0J^(2/3)`。I10/20/40/80/160有限矩阵最低隙除该尺度为2.7120/2.7280/2.7347/2.7375/2.7386，趋近独立64/96基quarticGalerkin隙2.73931094。五控制通过，不是实际核拟合；j随I变化是渐近测试族，未加入完整QTR重取向/电磁算符。固定I最低隙也不直接等于实际跨spinEwob。

候选池已按实际clock刷新为candidate-pool-106.json：两个当前槽分别达到条件milestone或有局部访问缺口，下一条现有raw TPSM主文的Lu/Ta电磁/轴标签仍有高信息路线；Day23预习已核独立MR/SP/TiP比较，继续只无学分。Görgen2004完整正文尚未取得，403/401/仓储202空页/OSTI连接拒绝已汇总，不导入任何Qt数字，不把它当全局研究阻塞。当前10个active限定脚本，未提前收束/发布。

## Checkpoint107：TPSM的绝对/归一强度、K与轴变换

扩展现有25页TPSM raw的指定PDF7–9/13–18，视觉Fig8/9及相关段，不新称全25页通读。Fig8为绝对B、Fig9是out/in；两低带相近、高带/高spin有差异。F24 Fig37绿TSD3→TSD2为有限值、蓝TSD3→TSD1较弱，“n2→1suppressed”不能读为零/禁戒；须说明相对哪一谐标度和带内分母。未数字化逐点或擅改spin轴。

源文将量子化轴从long换到short，同时用γ′=−120°−γ等价扇区。任务qk=cos(γ−2πk/3)检验得q′=(q1,q3,q2)、二/三阶不变量不变；四控制通过。惯量、j、总角动量与跃迁张量须一致旋转，不能把坐标重标当TW→LW实际转向。K是投影基标签，最终三轴配置/K混合不保证某个K守恒；形变γ与Eulerγ也不同。没有TPSM原producer复跑或新shape测量。

## Checkpoint108：占据、交换与PES的磁性盲区

NOM22原Eq5/6、TableI与E2/M1算符定向核：127Xe输入v²=.4317，归一动力学/E2费米子prefactor为.1366、归一exchange权重4u²v²=.98134044。三项指定标量控制通过，系数本身不是B或实验占据；M1算符不带同一显式u²−v²因子，不能从半填充宣布M1普遍为零。该模型已有exchange项，原文说明其考虑boson为核子对，不支持“完全无费米交换”的笼统批评。

Majorana项在受限同质子/中子形变的PES上不给独立贡献、强度不能仅由PES映射确定，却可能影响M1。F24的TPSM/softcore比较则说明固定basisγ与effectiveγ涨落/交错不等价；作者引用的IBFM精确能量来自私人通信，未公开重放，不直接裁决新δ测量。γ-soft、能量拟合或算符截断都不单独成为跨核模式充要门。四canonical/source页同步。

## Checkpoint109：局部phonon代数与投影占据

通常spin约定下nK=I−m、b=J+/√(2I)满足精确[b,b†]=1−nK/I；有限矩阵tracecommutator=0，不能全空间等于单位阵。低占据仍可近似boson，不由全局有限性否认有效phonon。四项有限矩阵控制通过（最大误差1.18×10⁻14）。I13/2、45/2的b矩阵2→1/1→0平方比为1.8462、1.9556；这些是同一I的scaledJ练习，不是实际跨I E2二声子修正公式。nK不自动等于Bogoliubov后的nw，体固相位/对易号仍需映射。

107首次lint因R矩阵的双中括号被解析为wikilink而报2error，已改成圆括号表示并实际重跑lint；这是排版修复，不改轴变换结论。108–109的科学写回由最新一次实际检查合并核验，未伪称每个中间态都独立通过。下一检查继承225.8keV偏振设计的线身份/计数输入与P符号可判别性，仍为Day22观测量主题。

## Checkpoint110：225.8keV继承反证方案撤回

实际核已存在LV19 VoR缓存TableI p5并与raw arXiv p9对照；225.8/648.9同母态mixed线无δ，Iγ3.8/1.8/.79为以198.8线归一的相对量。旧δ225=.0389并非该实验测量，而依赖跨campaign未锁定成分的反演。旧设计代码只读未执行、未覆盖Day21run。

脚本把P写成(1−f)PpureM1+fPpureE2，遗漏相干干涉和方向强度分母；Q=.22、40.6selectedevents/h及lineyield亦无该设施/门/几何实际校准依据。T71原式实读/视觉表明混合线P需双线性Stokes/强度，而源文p=J0/J90还不是现代P。

即便暂沿旧未验证A0=−.08770/A1=.02885，N663仅使两均值相距约3个1/sqrtN；在已知a=1无背景的条件binomial方差下，A1距0只有.743σ。条件正号3σ约需10803selectedcounts，只是旧检验目标矛盾的诊断，不是新机时承诺。16.3/45.3h、P>0排除所有D6手征机制的认证撤回；只有指定Θ和nuisance预测集合外的实测观测才能反驳该版本。source/综合及provisional设计note同步收缩，旧文精确存pre-correction-110.json。Day21正式[21]/18分不变。

## Checkpoint111：计数层、倒数a约定与校准识别性

MI07现有raw定向实读/视觉printed714/716/718：a=Uperp/Uparallel，与另一Clover式用倒数才等价。5000photopeak按原rounded3%/25%约为150/1250selectedcounts，knowna=.12/Q=.14条件Poisson给σP=.308607，近原Outlook .3；不是新的SeGA实测CI、更不迁成225.8效率。实际a均值/误差含unit差异，未把其spread当target独立σ。

Miller式A=(x−ay)/(x+ay)，P=A/Q，对(x,y,a,Q)用完整Jacobian/Σ；independentrawPoisson的VarA与条件binomialFisher吻合。若a完全自由，目标两bin均值只识别a(1+QP)/(1−QP)；chosenwitness Q=.2、P±.3配不同正a/yield给同(954,940)均值。五项解析/有限差分/计数/正性控制通过，非actualClover校准域内歧义。新的pilot清单区分photopeak、selectedsignal、背景、a/Q/reference与模型Θ，没有给真实beamtime承诺。

## Checkpoint112：静态g的标量信息与测量迁移

本任务定义μ=gR R+gj j的一j+core量子控制，gI约束⟨I·j⟩并在gj≠gR时反演⟨R²⟩；gj=gR时无几何信息。精确CG²验证归一/磁矩期望/反演/奇异域；不同正R分布可有同⟨R²⟩=3、同chosen g=834/715。五控制通过，没有导入新核素g数据，Reff不是确定R量子数，标量不重建体固三维几何。

GR18现有raw定向读PDF3–5补测量边界：128Cs是两odd核子+core，不能套单j式；g=.59(1)为作者测量，近planar为PRM/CDFT解释，ps高spin态不能裸迁56ns带头TDPAD。原外场/频率校准桥未重放；Eq3 orientation算符字面仍需后续定义核验，不默默改rms/absolute。动态M1out的geff定标也不自动成为静态g算符的已验证校准。

## Checkpoint113：精确单侧计数检验的α与功效

仍仅诊断旧134的未验证A均值：a1known/无背景/fixedexclusiveN下，按单侧α=erfc(z/√2)/2找最小整数拒绝阈值。旧N663的3σ两均值检验功效.48666，N1841的5σ为.49188；若目标换为A1相对零的正号，N663功效.01101、N10803为.49886。五项binomial质量/阈值/功效控制通过。chosen较大样本1500/23000可给各目标>90%功效，但不称最小或真实beamtime方案；物理P/率/校准并未因此成立。

这是相同当前问题的有界统计完成，区分效应分离、型I错误和检验功效，不引入新卡/实验。12点多开启的staticg/GR18算符问题仍属当前slot；下一定向核signedtripleproduct、RMS与Gramproxy的不同定义并保留Ref14/producer缺口，不把数值近1当实验几何证明。

## Checkpoint114：三种orientation量与g信息边界

GR18现有raw PDF3–5/visual4 Eq3给出新的定义问题：字面signedχ期望与文中fixedk/R近1数值，需原方法/算符约定解释。usualindependentlabspins下χ=(i/4)[(jp+jn)²,(jn+R)²]，fixedjpn态signed期望必0。按源中两组指定耦合的任务CG控制，signed均0、RMS为.67918/.70817、Gram(pairmean)代理为.95786/.99963；三量不可混用。近1代理不证明作者实际算法，不静默改原Eq3或判原实验错误。

chosen共轭packet有同g=.502却相反signedχ≈±.4491，未声称真实核doublet/本征态。四项限定矩阵控制通过。初CGprobe漏abs(M)>J guard导致执行失败，补guard后同物理输入通过，记录保留。Ref14的真实metadata为NPA682,375–386,“Chirality in odd–odd triaxial nuclei”, DOI10.1016/S0375-9474(00)00663-1；正文OA未得，现有PRL86,971是另一文。此为开放operator问题，实测g与作者PRM解释层保持。

下一继续当前计数问题：在matched独立nullcalibration假设下，探索四原始计数的条件检验来消除a nuisance，而不承诺真实beamtime；该分析未打开新卡。90分钟线后只完成这些已开的g/计数分析和记录。

## Checkpoint115：独立matched-null四计数条件检验

延续已开计数分析，定义独立、无背景、互斥raw Poisson四cells；目标均值为(a ct(1+A),ct(1−A))，已知无偏振校准为(a cc,cc)。给定行总数和perp列总数，A=0下目标perp数服从hypergeometric；a和两个yield条件消去，alternative odds=(1+A)/(1−A)。这是假设shared response后的任务推导，不是SeGA事件重放。

chosen table(954,940;900,1000)、known Q=.2给P=.3、localσP=.16188、单侧exact conditional p=.034634；四倍chosen counts的p=.00011565，未把它当检验功效或真实预算。四count局部方差与full Poisson Fisher逆相符，六控制通过。若target a与calibration a不相同，即使P=0也能复现四个均值；统计显著不能验证物理匹配。真实背景拟合、重叠事件、非null reference、Q或a响应不确定度仍需共同likelihood，16.3/45.3h旧认证不恢复。

## Checkpoint116：完全伸展态的orientation极限控制

已开g/orientation分析补一个完全伸展乘积态：jp=jn=11/2、R=2、I=M=13，固定M空间一维，signedχ和RMSχ均0，而Gram(pair means)代理=.33234568。一般该代理的平方为(I+1)/[(jp+1)(jn+1)(R+1)]，有限值来自Casimir涨落。这个极限反例进一步说明三种定义不能互代，不是GR18实际9+态或原作者算法。116五限定控制通过；117另用Cartesian六项独立构造复核commutator（误差≤5.0e−14），并核伸展Gram解析式，共七控制通过。Ref14正文/producer未得，实验g与作者模型解释保持，问题仍开放。

上海13:30后只完成这两个已打开问题及其综合、回证和检查；不打开新来源/课程卡。Day22尚未正式授分，Day23仍仅partial，15:00才转formal closeout。

## Checkpoint118：同一计数模型的有限样本区间

完成当前四计数分析的检验/区间一致性：chosen表的单侧p=.034634，反演noncentral hypergeometric两尾的central95 P区间为[−.023264,.620768]，单侧95 lower=.027894。中央双侧含0与单侧拒绝不矛盾；不得把局部σ或p值混作同一置信定义。五项尾部/极端表/小margin枚举控制通过，与原六项模型控制一并保留。四Poisson cross-product estimator未误称conditional MLE。所有假设与计数仍为任务设定，未导入真实Q/背景/响应，也不生成新beamtime或机制排他认证。

## Checkpoint119：平方算符与Gram因子化的差额

完成当前orientation分析的代数收口：通常三个独立lab自旋中，χ²的精确表达需pairdot二阶、对称三乘积和量子反对易修正；平均内积的Gram行列式没有保留这些关联。以ħ=1推导后，与直接Cartesian三重积平方在当前三个chosen态比较，误差≤1.9e−12；总计八个限定控制通过。小spin探针曾因未装SymPy失败，改显式NumPy epsilon求和，无新增依赖或科学输入改变。

该式是任务数学推导，不声称GR18原作者采用何种算法；没有修订实验g，没有把同M复packet称真实时间反演核双态，也没有打开新来源或卡。Ref14正文/producer缺口继续保留。

## Checkpoint122：既有Lu原实验的缺测与条件上限回核

对OD01/JE02同SHA既有原件各四页作全文文本回读，并视觉核OD01p5869、JE02p2–4。共同母态和两个相对强度根均维持原记录。新增明确边界：OD01低能交替支路无法给有意义上限，不能补为零；JE02作者用来比较模型的rM1=.012上限属于选大δ的条件，小δ另给.083(.024)，不能将该上限独立用于选根或当绝对B。没有新采集、寿命、偏振或σ认证；既有两次采集/模型依赖仍分开。

## Knowledge Impact and Learning Decision

修订了OD01/JE02的旧任务认证和WOB-EXP-9–16，把错误的偏振符号、绝对B、全区唯一与模式排他改判从活跃概念/观测页移除。保留原作者支持解释及真实实验限制。更早数值/source追加仍待逐项检查，未宣称全库科学审核通过。

## Durable knowledge delta

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "anchor": "| F14-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
      "anchor": "| H03-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
          "locator": "H03-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
      "anchor": "| OD01-D22-R092-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "anchor": "| JE02-D22-R092-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
      "anchor": "| LV22-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
          "locator": "LV22-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
      "anchor": "| CH19-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
          "locator": "CH19-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md",
      "anchor": "| ZC91-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md",
          "locator": "ZC91-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/guo-2024-chiral-wobbler-74br.md",
      "anchor": "| GU24-D22-R091-1 |",
      "summary": "原件驱动的事实/模型范围与旧任务认证纠错；限该原子条目。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2024-chiral-wobbler-74br.md",
          "locator": "GU24-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## 必要检验、支持条件与反证",
      "summary": "按模型定义/小角域/实验支持分层，撤回跨核统一数值门。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
          "locator": "CH19-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/minimal-wobbling-identification-protocol.md",
      "anchor": "## 逐项程序",
      "summary": "将原子身份、选解、相对强度、模型/声子有效域分别检验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
          "locator": "LV22-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## HFA局部重建与失效域",
      "summary": "保留有原件的曲率与小角公式，不把有限模型对照当核素实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint091 可复核的算符与参考抵消",
      "summary": "FA仍有非零M1；公共Harris参考等频抵消，不虚报核素漂移。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint092 163Lu直接观测边界",
      "summary": "修正OD01偏振/寿命范围及JE02跨两声子退激。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R092-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/interband-e2-strengths.md",
      "anchor": "## Day22相对比值、绝对强度与声子归一（checkpoint092）",
      "summary": "重建相对B，揭示r21/r10不同带内分母；不推绝对W.u.。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-3"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/wobbling-motion.md",
      "anchor": "## Day22偶偶核追加裁决撤回（checkpoint092）",
      "summary": "撤回M1占优必否证及未绑定寿命表改判。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-transverse-wobbling-136nd.md",
          "locator": "LV22-D22-R091-1"
        },
        {
          "path": "knowledge/sources/chen-2019-transverse-wobbling-even-even.md",
          "locator": "CH19-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/transverse-wobbling.md",
      "anchor": "## Day22横向几何与声子有效域校准（checkpoint092）",
      "summary": "修正唯一基准、能量单调及HFA等同完整QTR的量词。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-003"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/longitudinal-wobbling.md",
      "anchor": "## Day22 checkpoint094：分类与可迁移边界",
      "summary": "不把特定费米面模型条件泛化为全部低spin核严格禁戒。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/wobbling-energy.md",
      "anchor": "## Day22能量解释边界校准（checkpoint092）",
      "summary": "保持派生能量对象和模型域，不由斜率唯一分类。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/experimental-wobbling-evidence-strength-map.md",
      "anchor": "| WOB-EXP-11 |",
      "summary": "重新校准高spin实验的多声子支持和偏振缺口，不作全区穷尽结论。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R092-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "anchor": "| F14-D22-R092-1 |",
      "summary": "定向原件核Fig.19所指Ref.25的字面身份疑点；不判数据错误或静默替换原引用。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R092-1"
        },
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "JT01-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
      "anchor": "| JT01-D22-R092-1 |",
      "summary": "首页/摘要身份核：165Tm的DSAM论文不直接提供163Lu TSD寿命，本轮不是全文重读。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2001-165tm-h9-2-configuration.md",
          "locator": "JT01-D22-R092-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
      "anchor": "| LAW20-D22-R093-1 |",
      "summary": "定向核作者冻结j、谐n规则和典型参数域，保留解释范围。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
      "anchor": "| CF22-D22-R093-1 |",
      "summary": "定向核Sec4.6对Lawrie的定义回应；非谐拓扑并非新独立实验。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R093-1 |",
      "summary": "核SSS真实有限Fourier定义，区别于Bogoliubov本征态压缩。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint093 定义、有效域与模型比较合同",
      "summary": "分开定义、谐近似有效域和完整模型观测预测，列出条件AMGM下界。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-squeezed-state-map.md",
      "anchor": "## Day22 SSS定义纠错（checkpoint093）",
      "summary": "修正旧045定义并给密度矩阵角表示归一核控制，非核素测量。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-coherent-state-map.md",
      "anchor": "## Day22 SCS相位、测度与模式边界（checkpoint093）",
      "summary": "区分体固符号与概率测度，撤回通用电磁硬门和模型图像实测化。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/wobbling-motion.md",
      "anchor": "## Day22 模式与谐近似的定义分歧（checkpoint093）",
      "summary": "并列两派定义，不把近似域判决直接替代实验模式裁决。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations.md",
      "anchor": "## Day22 thematic REFLECT：争议定义与观测合同校准（checkpoint093）",
      "summary": "三来源定义/有效域比较的专题反思；撤回旧全区终审并保留实验δ冲突与独立预测问题。",
      "sources": [
        {
          "path": "knowledge/sources/lawrie-2020-tilted-precession-wobbling.md",
          "locator": "LAW20-D22-R093-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R093-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
      "anchor": "| GU22-D22-R094-1 |",
      "summary": "新混合比、旧P身份、误差范围与继承错误校正。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-1"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-2"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
      "anchor": "| AU20-D22-R094-1 |",
      "summary": "支持实验的相对比、伴随SP身份与PRM输入范围。",
      "sources": [
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D22-R094-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/187au-longitudinal-wobbling-controversy.md",
      "anchor": "## Day22 checkpoint094：恢复开放争议与逐量对照",
      "summary": "撤回88倍/4σ及终审，保留源间独立性与共同响应缺口。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-2"
        },
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D22-R094-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/longitudinal-wobbling.md",
      "anchor": "## Day22 checkpoint094：分类与可迁移边界",
      "summary": "撤回普适费米面禁戒，回到具体模型及观测冲突。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-3"
        },
        {
          "path": "knowledge/sources/sensharma-2020-longitudinal-wobbling-187au.md",
          "locator": "AU20-D22-R094-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/experimental-wobbling-evidence-strength-map.md",
      "anchor": "## Checkpoint094：187Au独立性与强度纠错",
      "summary": "纠正P/δ、conversion与二声子身份依赖错误。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-1"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `187Au` 的376/462",
      "summary": "恢复真实未解决问题，撤回88倍与新4σ认证。",
      "sources": [
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-1"
        },
        {
          "path": "knowledge/sources/guo-2022-low-spin-wobbling-187au.md",
          "locator": "GU22-D22-R094-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
      "anchor": "| M15-D22-R095-1 |",
      "summary": "逐线A/δ与实验/模型列身份、完整QTR重取向边界。",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-1"
        },
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
      "anchor": "| L22-D22-R095-1 |",
      "summary": "逐线P/δ与同母态比值重建，不擅报3σ或物理塌缩。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-2"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
      "anchor": "| SH26-D22-R095-1 |",
      "summary": "保留固定σ/I条件χ²证据，撤回浮动必等深与最终TiP认证。",
      "sources": [
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/135pr-wobbling-controversy.md",
      "anchor": "## Day22 checkpoint095：撤回最终TiP裁决，恢复逐线争议",
      "summary": "重开实际response与模型差异问题。",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-2"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/signature-tip-shears-discrimination-contract.md",
      "anchor": "## 逐项比较程序",
      "summary": "撤回跨核硬门，预习改为逐量竞争解释比较。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-3"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/wobbling-vs-signature-partner.md",
      "anchor": "## Day22 checkpoint095：机制比较的适用边界",
      "summary": "撤回M1百分比到模式的唯一映射。",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-D22-R095-1"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `135Pr` 的独立P–Rac",
      "summary": "量身份和源间冲突保持开放，未形式终审。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
      "anchor": "| YA67-D22-R096-1 |",
      "summary": "A4条件识别推导及非负有限J布居歧义见证；非实测拟合。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "anchor": "## Day22 checkpoint096：A4能否选根取决于取向和响应",
      "summary": "撤回普适双根、偏振正号和精度硬门，给出有条件反演。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/high-spin-angular-polarization-mixing-ratio.md",
      "anchor": "## Day22 checkpoint096：A4能否选根取决于取向和响应",
      "summary": "已知取向和自由张量模型分开，保留SH26条件证据。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        },
        {
          "path": "knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md",
          "locator": "SH26-D22-R095-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "anchor": "## Day22 checkpoint096：A4能否选根取决于取向和响应",
      "summary": "为实数两成分单γ模型提供反演条件与正布居反例。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "- [ ] `A2/A4`、偏振及取向/响应",
      "summary": "收缩不可辨识性的量词，实际响应/Cov缺口仍开放。",
      "sources": [
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "#### 偏振和角分布的条件选解",
      "summary": "清除旧跨阵列精确吻合和普适正偏振定理，回到逐线与条件A4证据。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-D22-R095-1"
        },
        {
          "path": "knowledge/sources/yamazaki-1967-aligned-angular-coefficients.md",
          "locator": "YA67-D22-R096-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
      "anchor": "| AG07-D22-R098-1 |",
      "summary": "比值先升后降；43/2原打印强度与比值未闭合，模型/实验分层。",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-1"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
      "anchor": "| CHI01-D22-R098-1 |",
      "summary": "核实际寿命态与alignment上扬，撤回错spin轨迹。",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-1"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/signature-tip-shears-discrimination-contract.md",
      "anchor": "## Day22 checkpoint098：Day23无学分预习的独立磁转动对照",
      "summary": "独立ratio/absolute链对照，不迁寿命或固定硬门。",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-1"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/wobbling-vs-signature-partner.md",
      "anchor": "## Day22 checkpoint098：Day23无学分预习的独立磁转动对照",
      "summary": "保留MR组态变化处非单调与逐门输入缺口。",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-D22-R098-2"
        },
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
      "anchor": "| DO99-D22-R099-1 |",
      "summary": "Qt寿命谱系、SD–ND对象与未分辨线/新旧campaign边界。",
      "sources": [
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-1"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-2"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/interband-e2-strengths.md",
      "anchor": "## Day22 checkpoint099：163Lu的SD–ND E2对照",
      "summary": "同核相对E2/两态混合控制，避免外标Qt迁为SD2τ。",
      "sources": [
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-1"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-2"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## Day22 checkpoint099：163Lu的SD–ND E2对照",
      "summary": "为近能量与强E2非充分性增加有对象映射的SD–ND例。",
      "sources": [
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-1"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-2"
        },
        {
          "path": "knowledge/sources/domscheit-1999-triaxial-superdeformation-163lu.md",
          "locator": "DO99-D22-R099-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "anchor": "| JE02-D22-R100-1 |",
      "summary": "逐线共母态/分母映射与双带外E2比、依赖边界。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/interband-e2-strengths.md",
      "anchor": "## Day22 checkpoint100：同母态out/out能消去什么",
      "summary": "区分同母态消尺度和跨带不同归一的声子比较。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R100-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
      "anchor": "| CF22-D22-R101-1 |",
      "summary": "实际勘误图与RMS不重建SCS的正性条件控制。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-coherent-state-map.md",
      "anchor": "## Day22 checkpoint101：相同RMS可以对应不同SCS图",
      "summary": "三RMS/完整密度、测度与实验解释边界。",
      "sources": [
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-1"
        },
        {
          "path": "knowledge/sources/chen-2022-study-wobbling-spin-coherent-state-maps.md",
          "locator": "CF22-D22-R101-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "| MU07-D22-R102-1 |",
      "summary": "继承统计量/图号/手征对称性与模型临界边界纠正。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-1"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-2"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
      "anchor": "| LV21-D22-R102-1 |",
      "summary": "低spinTiP带族与三准粒子手征pair、campaign依赖分层。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-1"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint102：135Nd模式判别先绑定带族与统计量",
      "summary": "原支持解释保留，撤回Qt精密排他和同核跨组态否证。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D22-R102-1"
        },
        {
          "path": "knowledge/sources/lv-2021-tilted-precession-135nd.md",
          "locator": "LV21-D22-R102-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
      "anchor": "| TI19-D22-R103-1 |",
      "summary": "独立DCO/P支持、大δ/负P、相对强度与g_eff定标范围。",
      "sources": [
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-2"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/experimental-wobbling-evidence-strength-map.md",
      "anchor": "## Day22 checkpoint103：保留105Pd的独立支持链",
      "summary": "保留正常形变实质支持和C带/组态/定标限制。",
      "sources": [
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-2"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## 模型定标与独立检验点：105Pd控制",
      "summary": "区分g_eff幅度定标与额外可检验观测，不预先否决有调节模型。",
      "sources": [
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-2"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
      "anchor": "| NOM22-D22-R104-1 |",
      "summary": "保留IBFM实质预测、127Xe例外与二手表误差/校准边界。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-2"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations.md",
      "anchor": "## Day22 checkpoint104：竞争模型比较需保留完整观测向量",
      "summary": "整M1算符标度不修复E2向量；反方不作最终实验裁决。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-2"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "anchor": "## Day22 checkpoint104：竞争模型比较需保留完整观测向量",
      "summary": "δ比例、绝对强度与算符/数据版本校准分层。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-2"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R104-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R105-1 |",
      "summary": "Fig35绝对量/比值标签、LL模型与邻核转述限定。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## Day22 checkpoint105：wobbling–scissors耦合不同于磁转动分类",
      "summary": "isovector scissors与valence shears分层，不把M1淬火作唯一模式证明。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations.md",
      "anchor": "## Day22 checkpoint105：wobbling–scissors耦合不同于磁转动分类",
      "summary": "保留QRPA的E2缺陷、校准和转述差异，公开伴随未正式raw/source摄入。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R105-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
      "anchor": "| F14-D22-R106-1 |",
      "summary": "人工临界族的四次回复项/有限spin隙与渐近域，非核实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint106：HFA软化的有限spin四次势控制",
      "summary": "区分局部谐近似软化与完整有限谱、固定I与实测Ewob。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/wobbling-energy.md",
      "anchor": "## Day22 checkpoint106：谐频零不等于有限谱隙零",
      "summary": "五限定控制及完整模型/真实观测边界。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
      "anchor": "| SHJ24-D22-R107-1 |",
      "summary": "扩展Lu/Ta实读，绝对B/归一比、K与等价γ扇区分层。",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-1"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-2"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R107-1 |",
      "summary": "TPSM的suppressed须说明比较量，不误读为缺测/零。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R107-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## checkpoint107：K标签与等价γ扇区不是新物理模式",
      "summary": "轴置换不变量与完整输入一致变换，不把K/坐标当物理模式。",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-2"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-D22-R107-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
      "anchor": "| NOM22-D22-R108-1 |",
      "summary": "v²只是模型输入；exchange与PES不可识别Majorana方向分开。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-1"
        },
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2024-wobbling-review.md",
      "anchor": "| F24-D22-R108-1 |",
      "summary": "softcore/TPSM作者比较不变成普适softness禁戒或无Pauli断言。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R108-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/gamma-soft-vs-gamma-rigid-diagnostics.md",
      "anchor": "## Day22 checkpoint108：γ-soft不是模式禁止条件，PES不定标全部M1",
      "summary": "core交错、basis参数、PES约束与动态磁性残余项分层。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-2"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R108-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## Day22 checkpoint108：γ-soft不是模式禁止条件，PES不定标全部M1",
      "summary": "补充参数识别/交换处理边界，不用统一阈值裁模式。",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
          "locator": "NOM22-D22-R108-1"
        },
        {
          "path": "knowledge/sources/frauendorf-2024-wobbling-review.md",
          "locator": "F24-D22-R108-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/wobbling-motion.md",
      "anchor": "## Day22 checkpoint109：声子代数是局部近似，基占据不等声子标签",
      "summary": "明确finite-spin局部代数、nK/nw与真实E2阶梯的区别；任务条件练习。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
          "locator": "H03-D22-002"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## Day22 checkpoint109：声子代数是局部近似，基占据不等声子标签",
      "summary": "明确finite-spin局部代数、nK/nw与真实E2阶梯的区别；任务条件练习。",
      "sources": [
        {
          "path": "knowledge/sources/hamamoto-2003-quantized-wobbling-excitations-alignments.md",
          "locator": "H03-D22-002"
        },
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R106-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "| LV19-D22-R110-1 |",
      "summary": "核三线实际身份/缺δ，撤回未校准机时与Psign模式排他。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-2"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
      "anchor": "| T71-D22-R110-1 |",
      "summary": "混合线Stokes/强度含干涉，源p与现代P不可混。",
      "sources": [
        {
          "path": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
          "locator": "T71-D22-R110-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint110：撤回旧排他机时方案，保留可执行的输入清单",
      "summary": "provisional设计恢复共母态/响应/Θ/功效输入要求，旧128–141认证移历史。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        },
        {
          "path": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
          "locator": "T71-D22-R110-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/high-spin-angular-polarization-mixing-ratio.md",
      "anchor": "## Day22 checkpoint110：225.8keV设计不能由P正号直接裁模式",
      "summary": "区分假设分离和正号检验，不造新设施预算。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-2"
        },
        {
          "path": "knowledge/sources/taras-1971-phase-defined-polarization-formulas.md",
          "locator": "T71-D22-R110-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/miller-2007-sega-polarization.md",
      "anchor": "| MI07-D22-R111-1 |",
      "summary": "计数层/倒数a约定与已知校准方差、未知a识别边界。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint111：同一计数预算先区分样本与校准",
      "summary": "全Jacobian/Σ与target-only校准退化，不造实际阵列σ。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint111：pilot与双bin统计合同",
      "summary": "provisional设计把raw/selected/background/a/Q/Θ分层。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-geometry-phonon-observable-contract.md",
      "anchor": "## Day22 checkpoint112：静态g的独立标量约束与几何边界",
      "summary": "本任务定义的一j磁矩模型代数/CG控制，不是源论文新g数据或模式唯一反演。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D19-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/wobbling-criteria-card.md",
      "anchor": "## Day22 checkpoint112：静态g的独立标量约束与几何边界",
      "summary": "本任务定义的一j磁矩模型代数/CG控制，不是源论文新g数据或模式唯一反演。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        },
        {
          "path": "knowledge/sources/timar-2019-transverse-wobbling-105pd.md",
          "locator": "TI19-D22-R103-3"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint113：效应分离度不等检验功效",
      "summary": "旧未验证均值下的exactbinomial目标诊断，z/α/功效分开，不作核/设施预算。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint113：效应分离度不等检验功效",
      "summary": "旧未验证均值下的exactbinomial目标诊断，z/α/功效分开，不作核/设施预算。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R111-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "| GR18-D22-R114-1 |",
      "summary": "signedχ/RMS/Gram定义问题明确为条件待核，不改实验g或原式。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint114：g与三矢量几何需说明order parameter",
      "summary": "标量g/期望/方差/代理分开，条件packet不作核band证明。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "## Day22 checkpoint114：三矢量orientation定义待核",
      "summary": "Ref14metadata已核、body/producer未得，保留定向问题而非结案。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-1"
        },
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R114-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/miller-2007-sega-polarization.md",
      "anchor": "| MI07-D22-R115-1 |",
      "summary": "shareda/独立raw cells条件下的matched-null检验，非实际实验。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint115：独立matched-null四计数的条件检验",
      "summary": "四计数/校准匹配/条件统计边界，不作真实预算。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint115：独立matched-null四计数的条件检验",
      "summary": "四计数/校准匹配/条件统计边界，不作真实预算。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "| GR18-D22-R116-1 |",
      "summary": "完全伸展态signed/RMS零但Gram代理非零；保留作者定义问题。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R116-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint116：伸展态中的算符与代理差别",
      "summary": "非线性期望顺序不能互换；非核态/原论文算法认证。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R116-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/miller-2007-sega-polarization.md",
      "anchor": "| MI07-D22-R118-1 |",
      "summary": "同一chosen四cell模型的exact conditional区间/单侧与双侧标准，不作实际CI。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R118-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/compton-polarimetry.md",
      "anchor": "## Day22 checkpoint118：检验方向与区间尾部一致",
      "summary": "同一chosen四cell模型的exact conditional区间/单侧与双侧标准，不作实际CI。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R118-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day21-135nd-same-input-falsification-design.md",
      "anchor": "## Day22 checkpoint118：检验方向与区间尾部一致",
      "summary": "同一chosen四cell模型的exact conditional区间/单侧与双侧标准，不作实际CI。",
      "sources": [
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R118-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
      "anchor": "| GR18-D22-R119-1 |",
      "summary": "独立lab自旋平方三重积的任务精确关联式/定义边界，非原producer识别。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R119-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
      "anchor": "## Day22 checkpoint119：平均几何量遗漏哪些关联",
      "summary": "独立lab自旋平方三重积的任务精确关联式/定义边界，非原producer识别。",
      "sources": [
        {
          "path": "knowledge/sources/grodner-2018-128cs-chiral-g-factor.md",
          "locator": "GR18-D22-R119-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/antimagnetic-rotation.md",
      "anchor": "## checkpoint081追加认证撤回（checkpoint091）",
      "summary": "撤回缺原表和普适阈值的旧任务认证，108In只作实测强度来源边界对照。",
      "sources": [
        {
          "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
          "locator": "CHI01-D22-R098-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/flip-mode.md",
      "anchor": "## checkpoint077追加认证撤回（checkpoint091）",
      "summary": "撤回任意FM数值分区和未证物理认证，保留局部近似域。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "## Day22几何、声子与观测合同",
      "summary": "Day22已存在知识/来源导航，非新增科学证据。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2014-transverse-wobbling.md",
          "locator": "F14-D22-R091-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2018-comment-wobbling-stability.md",
      "anchor": "| FC18-1 |",
      "summary": "本run已读评论的理论范围/惯量排序与近似边界，非新实验。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2018-comment-wobbling-stability.md",
          "locator": "FC18-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tanabe-2018-reply-wobbling-stability.md",
      "anchor": "| TR18-1 |",
      "summary": "本run已读回复的理论判据/近似边界，非对2020/2022实验的回复。",
      "sources": [
        {
          "path": "knowledge/sources/tanabe-2018-reply-wobbling-stability.md",
          "locator": "TR18-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
      "anchor": "| OD01-D22-R122-1 |",
      "summary": "既有原件限定缺测、选根条件上限和真实响应输入，不作新数据/排他认证。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R122-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "anchor": "| JE02-D22-R122-1 |",
      "summary": "既有原件限定缺测、选根条件上限和真实响应输入，不作新数据/排他认证。",
      "sources": [
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R122-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/minimal-wobbling-identification-protocol.md",
      "anchor": "## Day22 checkpoint122：缺测、条件上限和实际响应",
      "summary": "既有原件限定缺测、选根条件上限和真实响应输入，不作新数据/排他认证。",
      "sources": [
        {
          "path": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
          "locator": "OD01-D22-R122-1"
        },
        {
          "path": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
          "locator": "JE02-D22-R122-1"
        },
        {
          "path": "knowledge/sources/miller-2007-sega-polarization.md",
          "locator": "MI07-D22-R115-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D22-R110-3"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. F14 Fig.19字面Ref.25与165Tm原件身份不匹配，不能用它认证Lu寿命，也不据此否定数据。Schmitz1993的Ref.7原始寿命与Qt：DOI/title已核，正文未得；不把它并作TSD2/3独立绝对寿命。后续逐带寿命来源仍待检索。
2. 135Pr/187Au共同响应、门、δ及Cov仍未重放；继续修复旧任务排他量词与不匹配的表/带身份。
3. 其余邻核的source补充尚未逐claim核，不由邻核S(4)或缺寿命直接裁决模式不存在。
4. Day23预习只讨论相同计数如何容纳组态重指派；需在正式Day23 run再审交付，不给本轮学分。

## L0–L4 state

L1/L2原件读取、概念和比值身份校准；L3竞争解释/模型有效域仍有边界；L4仅作来源明确的打印数值重建和解析控制，不重标原实验CI。候选池仍有高信息路线，未到研究截止，不以卡片覆盖或本检查点为结束理由。

## Agent self-audit triage

P0纠错：自设参数当实验、冻结j→M1零、两准粒子M1→剪刀、缺测→零、跨核/跨带寿命误配、全核区唯一和普适数值硬门已在091/092定位修订。早于这些修订的源页追加仍需核，不由一次检索或green lint认证。

P1：打印舍入与完整Cov不同；图示定性几何和参考扣除i_x不直接测j矢量；文献书目不提供实验数值。后续所有新增claims保持needs_review。

## Verification and continuation

required-checks-092.json记录上一检查点实际结构检查通过：lint零error、boundary通过、diff clean、21项原子引用有效，及4项打印输入舍入控制通过。它们不认证更早source追加或全库科学结论。required-checks-093.json记录本轮新增后的实际检查通过：lint零error、boundary通过、diff clean、29项原子引用有效及6项条件控制通过；非全库科学审核；094又完成187Au的直接原件和六页SI方法核验；095完成逐线及条件χ²纠错，096完成A4条件与物理布居反例，097隔离未核追加和旧生成脚本，098补独立磁转动原文对照并保留43/2未闭合，099核Lu寿命引用对象及SD–ND混合，100补TSD3同母态双出口，101核实际勘误及相同RMS的不同SCS反例，102修订135Nd带族和继承统计量，103补105Pd独立支持/定标边界，104核IBFM例外/转引/整向量，105核QRPA/图量并追实际Lu原数据，106完成有限临界四次势控制，107校准TPSM的强度/K/轴标签，108核占据/交换/PES磁性盲区，109核局部phonon代数，110撤回继承偏振排他/机时认证，111核计数层和校准识别性，112补staticg及113精确功效，114保留orientation定义边界，115/116完成两个既有分析，required-checks-116.json实际全项通过（102写回、lint零error、boundary/diff、六count及五orientation控制）；117独立算符控制见three-vector-orientation-controls-117.json。下一续接见next-continuation-117.md与run.json；15:00切换closeout，15–16完成正式Day22逐卡审计、末次检查、receipt、下一任务准备与H3显式提交/非force推送。当前未授分/提交/发布，不开Day24。

当前运行边界：run-local clock-events最后记录2026-10-24 22:18 monitor已停止（manual-attention-required），不把旧PID/心跳当作仍活跃研究证明。本轮同一thread的native goal continuation实际执行中，未重启daemon或创建新session；截止仍以原receipt的2026-10-25 15:00为准。
