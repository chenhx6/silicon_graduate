---
type: learning-daily
graph-excluded: true
created: 2026-10-13
updated: 2026-10-14
---

# Day 13 — Doppler correction、反冲与速度信息

## Run state

- run_id: `2026-10-13-day-13-01`
- run_date: `2026-10-13`；timezone: `Asia/Shanghai`；day_index: `13`
- phase: `gamma-spectroscopy-and-level-schemes`；schedule_id: `wiki-daily-learning`
- completed_day_indices: [13]
- partial_day_indices: [14]
- Day 13 card audit: complete
- 已发布卡学分：内容发布门通过后推进为`next_day_index=14 / completed_day_count=13`；正式Day14入口为`outputs/learning-daily/prompts/20261014-DAY14-week-two-spectrum-to-level-scheme-exam.md`。
- 入口状态：`next_day_index=13 / completed_day_count=12`，与矩阵一致；Day 11/12 不重跑。
- session_id: `01a13489-64ba-7930-9a2c-291375d95ad0`（本次新 session，与上轮不同）。
- resume_command: `codex resume 01a13489-64ba-7930-9a2c-291375d95ad0 -C /workspace/wiki -s danger-full-access -a never`
- 研究硬截止：`2026-10-14T15:00:00+08:00`；下一调度：`2026-10-14T16:00:00+08:00`。
- 执行路线：用户在同一 interactive session 中明确继续；未观察到 foreground daily runner，故以真实人工续接/检查回执对账，不伪造 runner exit code。
- 使用技能：`farmer`、`go-on`、`all`、`auto`；`debug`仅用于method schema错误修复。保留原任务、模型与文件现场；farmer 的 ensure 启动成功，dry-run 无恢复 action。auto 的原生 goal 创建成功；不增加未请求的 token budget。
- 2026-10-13 21:06 起，用户要求持续学习，原 session/截止不变；状态为 active-Day13。既有卡学分保留，不重复推进 next14/count13。上一段17:51提前收束仅记历史，后续已恢复更广的 Day13 方法问题。
- 本次课程交付完整；实验重拟合仍 not-ready，见下面的数据边界。Day 14 只有知识预习，没有该卡 completion audit、正式周考学分或课程跨越。

- 时钟 checkpoint-001 已于 `2026-10-14T12:00:52.124160+08:00` 在原 session 实际接收并记入 observed_clock_executions；余 179.1 分钟，继续当前 DAY13 分析。原 clock supervisor 11:51 退出，farmer 已观察到会话 running；按提醒保持 daemon 不重启，用会话内 clock tool 判断截止。

- 最终研究收束：`2026-10-14T15:04:21.971452+08:00` 观察到原15:00截止，之后仅做closeout；当前DAY13分析与source/model/independence/readiness审核完整，课程保持next14/count13。发布稳定指针：main / `Finalize DAY13 statistical and velocity validation contracts`，精确结果见run receipt。

- 最终内容已发布：main / `Finalize DAY13 statistical and velocity validation contracts`；fresh fetch/ancestry/dry-run/HEAD:main push均exit0，manifest与提交、远端HEAD、handoff指针核对通过（2026-10-14T15:15:14.362374+08:00）。完成回执另以main / `Record DAY13 completion after published closeout`保存；课程state原值已对账，无重复计卡。

### Day 13 card completion audit

| Day-matrix deliverable | Evidence locator / artifact | Status |
|---|---|---|
| 来源前回忆：shift、velocity、angle、stopping、event correction | [recall-record.md](20261013-DAY13-doppler-correction-recoil-velocity-run-01/recall-record.md)，保存于本轮原文读取前；明确标作上轮预习后的 primed recall。 | complete |
| Doppler 方法、Mavela thesis 与一个 in-beam source 主线核验 | [Doppler method](../../knowledge/methods/doppler-correction.md)；[Mavela](../../knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md) DD-20261013-32S-27/28，Eqs.(4.5)/(4.6)、Fig.4.17；[Klemme](../../knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md) KL99-2/4/18，十页主线及 Fig.1/Table I–II。 | complete |
| 给定能量、β、角度的重算及速度误差传播 | [复算代码](../../system/scripts/day13_doppler_diagnostics.py)、[结果 JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/doppler-exercise.json)；exact inversion、Jacobian、covariance、有限差分和固定 seed MC。 | complete |
| 区分真实宽化、未完全校正、停止与近邻跃迁，含反证和必要伴随观测 | [诊断表](../../knowledge/methods/doppler-correction.md)；KL99-18 同跃迁的距离相关两分量；[Herzáň](../../knowledge/sources/herzan-2015-193bi-spectroscopy.md) HE15-5 的四线峰；低速 width-only rank-2 反例明确标为任务推导。 | complete |
| 一页 Doppler correction 诊断表，保留 locator | [Doppler correction 诊断表：峰位、峰宽与停止](../../knowledge/methods/doppler-correction.md)，八行症状/伴随检查/反证/locator；同步 [A≈130 thesis matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md) 的 Doppler-to-level/strength contract。 | complete |

## Candidate pool and selection

本轮延续问题为“校正后的峰能否验证速度/方向，并分开停止和多条跃迁”；主来源是必读的 Mavela `32S` thesis。独立 in-beam 对照选择 Klemme `134Nd` coincidence-RDDS：它将速度历史保留为寿命信息，直接检验“校正之后就不需 stopping”的说法。Longfellow 的已审核 GRETINA 方法仅作 first-interaction/角度与能量转换分离的支持性核验。唯一下一日预习选择 Herzáň `193Bi`，用原图和表把谱峰身份接到能级放置。

| 候选 | 本轮处理及信息增益 | 剩余判别输入 |
|---|---|---|
| Mavela β20/24、9%/7%与 S3 printed transform | 复核 printed input 和精确式；修正 `196Pt` 冲突句的 locator；不把排印列表等同执行版。 | production sorter hash、target/coordinate metadata、ring/sector spectra。 |
| β/角度/response 的峰宽识别 | 精确协方差传播及低速 rank-2 多解，改变对 angle-width diagnostics 的充分性判断。 | 至少一项独立 calibration，实际 joint covariance 和 response。 |
| Klemme stopping 与近邻线 | 全文主线、Fig.1和 Table I/II 回读；相同跃迁随 stopper distance 改变分量。 | 原始 distance/feeding/response 包才能重拟合。 |
| GRETINA frame/first-point | raw Eq.(18) 支持能量反演；最高能量点的排序是本装置的方法选择。 | 不移植阵列 response 或 sorting performance。 |
| Day 14 唯一知识预习 | Fig.2/Table I 三层重建、共用门和 quadruplet 反例；Table II 的 X/linking 与弱线缺失边界。 | 正式 Day 14 自己的来源前回忆、周考、weekly REFLECT 与逐卡验收。 |

开始快照为17:12、距原截止1307分钟；17:33刷新后1286分钟，按 AGENTS/continuous-learning 的新规则只预习 Day14，不按旧 advance wording 给学分。最终研究候选池在17:51:03刷新，剩1268.94分钟，见 [research-closeout.json](20261013-DAY13-doppler-correction-recoil-velocity-run-01/research-closeout.json)。

**历史收束决定（后被用户持续学习指令撤销）：**这次提前收束不是因为两个来源读完：已重新检查生产数据、独立 calibration、stopping 对照、tracking frame、下一张卡与具体可复算路径。当前诊断问题和唯一预习的可得证据已固化；仍会改变判断的输入是缺失的 acquisition/code/response 包，官方库新核验也没有这些附件。其它一般来源不能代替本次执行身份。未打开 Day15 的科学来源或课程；未解决输入列为 readiness boundary，不列成用户待办。

## Sources and evidence

| 来源与指纹 | 本轮实际覆盖 / locator | 独立性与证据层 |
|---|---|---|
| Mavela 2019；local raw SHA-256 `4c656a983a0502eaef7c551dfaf6e13539ce472f8e76aea6299ad09cfc112ccf`，94页 | 摘要/动机、CE/reorientation 理论主线、setup、calibration/gates、Doppler/GOSIA、discussion/conclusion；关键图式和代码视觉核验 PDF file pp.41,51,53,56,70,74。DD-20261013-32S-27/28；DD-20261013-32S-25 locator 改为 PDF p.41 / printed p.32。 | 一个实验；PDF、本文知识页和 UWC copy不是独立复测。Q_S/GOSIA extraction、作者 intrinsic-shape interpretation 与本任务 diagnostics 分层。 |
| Klemme 1999；SHA-256 `2a6dfcdac12de9dbf61b2a63c274aed8e286249a3dd28d1a2c6c5a46f1c00604`，10页 | introduction lifetime conflict→GASP/plunger/DDCM→finite stopping→Tables I–IV/IBM/TRS/ASYR limits→conclusion；视觉 Fig.1/2、Table I；KL99-18 补足 same-line distance反例。 | 独立于 Mavela；多 rings/gates/邻核仍属同次 acquisition，Table II branching 为另一次薄靶数据依赖；模型几何不是直接实测。 |
| Longfellow 2026；SHA-256 `fb3b4f5e4dce6a436bb569b64af1914c6b673561374d7867a3d906aef7090df1` | 支持性 raw p.3 Eq.(18)、first-interaction/ordering 段、p.7 summary；L26-8。 | 独立方法实验；原 human-reviewed/claim flags 保持不变，本轮未改 source。 |
| Herzáň 2015；SHA-256 `f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea`，20页 | 仅本次 Day14 预习：reaction/tagging→bands/isomers/SD→interpretation/conclusion 主线；重点视觉 Table I p.3、Fig.2 p.8、Fig.5 p.10，及 Table II p.15 / negative evidence p.19；HE15-4–7。 | 独立 A≈190 实验；图、表、同门投影不是多份独立实验。Jπ/multipolarity 为联合赋值，configuration/SD 是受约束解释。 |

外部核验：Crossref `10.1103/PhysRevC.60.034301` 的作者/题名/年/期刊与 raw 一致，属于身份核验。UWC [item API](https://uwcscholar.uwc.ac.za/server/api/core/items/459d5ba1-daee-4bc9-b3f7-974e342e8e9a) 与 [bundle inventory](https://uwcscholar.uwc.ac.za/server/api/core/items/459d5ba1-daee-4bc9-b3f7-974e342e8e9a/bundles?size=100) 本次均HTTP200，分别列 thesis PDF、LICENSE、TEXT、THUMBNAIL，没有独立执行 sorter、event/yield/ring spectrum/calibration 附件。没有将 metadata 或搜索结果当作物理证据，也没有下载或改动 raw。

Mavela 的 Eq.(4.5)/(4.6) 与 inverse/Jacobian相容，Fig.4.17的2230.57-keV peak聚拢是真实图示；它未给角分辨centroids、完整 covariance 或执行版列表。Sec.4.4从 uncorrected target 与 projectile-corrected spectra取不同 yield，不证明 target β=0。printed β20 异常、β24候选、S3 transform 和9%/7%文本边界均保留。

## Theory/analysis exercise

设 θ 为 lab photon direction 对发射核速度的夹角，`E_lab=E0/[γ(1−β cosθ)]`，`E0=E_lab γ(1−β cosθ)`。对 x=(E_lab,β,θ) 用 `σ²=JΣJᵀ`；θ以 rad 输入，σβ与σθ若相关必须保留cross term。精确 Jacobian 和推导保存在 [Doppler method](../../knowledge/methods/doppler-correction.md)；来源基式是 Mavela Eq.(4.6)，传播结果是本任务推导。

自设 `E0=1000 keV, β=0.07, σE_lab=1 keV, σβ=0.002, σθ=2°`：

| θ | E_lab (keV) | independent σE0 (keV) |
|---:|---:|---:|
| 35° | 1058.226372 | 2.377966 |
| 90° | 997.546991 | 2.644848 |
| 145° | 943.449018 | 2.395211 |

三行精确反演均为1000 keV。90°的 β 一阶低速项消失，但 exact derivative 仍有相对论项，角度项较大。忽略 γ 会共同偏低2.453009 keV。35°相同 marginal σ 下，把ρβθ从−0.8改到+0.8使σ由3.0748变为1.3620 keV；未给 covariance 不能声称完整误差预算。

代码实测：forward/inverse最大误差 `1.14×10⁻13 keV`，有限差分相对误差 `2.44×10⁻9`，九种 covariance 的固定seed MC σ与一阶式最大差 `0.171%`；程序退出0。新模拟只验证方法与假设，不构成实验重拟合。

低速反例为 `V(θ)=A+B cos²θ+C sin²θ`。由于cos²+sin²=1，设计矩阵rank2；`(A,B,C)=(1,4,5.9705014)` 和 `(2,3,4.9705014) keV²` 给七个角度完全相同 variance。这直接限制“仅多角度峰宽就能唯一分解response/β/angle”的说法。独立calibration才能解除至少一项歧义。

停止toy用自设指数 slowing/emission law，无feeding、β_i=0.016、τ=t_s=1.1ps。固定初始β校正后的exact MC mean residual在35°/90°/145°为−6.502/+0.085/+6.615keV。Klemme只报告约1.1ps Au stopping time，没有报告本toy law或τ；两者不能等同。

### Day 14 uncredited knowledge preview

[来源前回忆](20261013-DAY13-doppler-correction-recoil-velocity-run-01/day14-preview-recall.md) 明确为已读source概要后的 primed recall，raw图/表在之后打开。正式Day14仍要重新做回忆和周考。

[Level-scheme method](../../knowledge/methods/level-scheme-reconstruction.md)保存Herzáň Fig.2/Table I的1228(17/2+)→929(15/2+)→605(13/2+)子图。299.2、323.4列M1，直接622.4分支列E2；`299.2+323.4−622.4=0.2 keV`。拟合误差独立时σ=0.1732keV；再假设caption的0.3keV增量各线独立时σ=0.5477keV。没有joint covariance，后者只是练习。三整数level energies为圆整值。

622.4分支与299.2+323.4级联互斥；共用下方门又未必能拆出同带299.8/299.2近邻。HE15-5的323-keV quadruplet是直接反例。HE15-6保留SD带的X与tentative link，HE15-7保留未见低能线及conversion/x-ray解释，不补写“已测”跃迁。

| 预习自检维度（0–4；primed，非正式周考） | 分数 | 本次证据与仍需练习 |
|---|---:|---|
| 理论/公式 | 3 | exact transform/Jacobian与energy closure已复算；不能替代完整响应积分。 |
| 谱/纲图/门 | 3 | 三层branch和四线峰已核；未持有真实多门矩阵重拟合。 |
| 误差/feeding/background | 3 | covariance与rank反例；实际feeding/response未知。 |
| 事实/解释/模型分层 | 4 | 图表、assignment、X/linking与模型解释明确分开。 |
| 竞争解释/反证 | 3 | stopping、quadruplet与未见低能γ的反例；灵敏度未重算。 |
| 研究问题/最小设计 | 3 | β/geometry/calibration和互斥branch controls已提出；事件包未取得。 |

本轮自检19/24，不是Day14正式成绩。预习REFLECT：峰、跃迁、能级和configuration不能合并成一个证据对象；energy closure与多投影会共享事件/标定；negative evidence必须带detection/branch/ICC条件。正式Day14宜优先检验这些边界并形成自己的weekly产物，而不是照抄预习分数。


### 持续 Day13：独立 vector/vertex 对照与 selection exercise

用户21:06要求后重开同一session。已读[[vandebrouck-2016-vamos-dual-position-mwpc]]公开8页preprint主线及p6 Table1/p7 Fig5：98Zr1222.9-keV line从8.6(1)到5.5(1)keV。已读[[crespi-2013-agata-high-energy-doppler-response]]10页preprint主线及p8 Table2：15.1-MeV line的PSA/segment/crystal为119/122/>160keV，average β为同一谱优化而非独立event velocity。新全文仅存tmp，source记录remoteURL、SHA和未填充raw槽位；保持raw目录不变。

[geometry/gate code](../../system/scripts/day13_doppler_geometry_gates.py)和[exercise](20261013-DAY13-doppler-correction-recoil-velocity-run-01/geometry-gate-exercise.json)新增有声明假设的two-plane correlation、finite-bin二阶bias和fixed-gate migration。MC/Jacobian最大相对差0.185%，quadrature64/128、zeroβ和exact-event-inverse检验通过；source-inspiredρ≈−0.973不是作者measured covariance。true angle ratio1.30的synthetic fixed gate可读成1.381（不同width）或1.1945（额外βbias0.002），不当作实验alignment。推导、参数、数值和thematic REFLECT已全部固化到Doppler/tracking方法页。

当前下一路线：reaction/target能损与angular straggling、emission-history造成的velocity/vertex差异、first-point排序与selection covariance；继续Day13，Day14保持已有partial、无Day15。


### 持续Day13：发射tail、近似约定与hit顺序

[[aladili-2009-agata-doppler-simulation]]47页全文主线/关键图已核（AA09-2/4/5/7/8）；它是simulation/design，非独立实测。其平均flight≫target的criterion支持主要靶外发射，不排除指数tail。在constantβ/uniform0.5μm reactiondepth/sourceτ的明确toy下，Cr/Arinsidefraction约1.49%/2.41%。Eq6.8的1.15×10⁻5m=16.5μm打印冲突保留。

[convention/decay code](../../system/scripts/day13_doppler_conventions_decay.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/convention-decay-exercise.json)验证exact-exact与linear-linear roundtrip；linearforward+exactinverse在1434keV/β.0548/90°给+2.158keV。其与source图mean约1436仅量级相容，provisionalcase在[[doppler-forward-inverse-convention-check]]，缺sortpax/MGT不能宣称作者代码错。

Compton two-hit toy满足scattering energy关系：sum后用真实firstpoint得1000keV；逐deposit用自己的径向角得1004.537keV；最高deposit当first得1005.766keV。它限制energyordering的普遍性，同时保留Crespi/Longfellow在指定setup的实际表现。新结果固化到Doppler方法；MC/analytic概率最大relative差0.593%，thin-target/zero-nuisance/共同factor求和检验通过。仍持续Day13，下一步检查meanβ自校准与hold-outline/angle验证、emissionposition/particle-budget影响。


### 持续Day13：速度stage、TOF与centroid自校准

[reconstruction/calibration code](../../system/scripts/day13_recoil_speed_calibration.py)与[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/recoil-speed-calibration-exercise.json)已验证kinetic derivative/TOFcovariance及β-gain-offset一阶rank2、exactweakcurvature。sourceinput与自设measurement分开：Klemme28Si+110Pdnominalbeamβ.09755/boost.01987不可直接代替reportedmean.016；Mavela/S3particleenergy须明确scattering/loss/emissionstage；VD16timeσ不能脱离pathlength推出σβ。syntheticβ.07与.0701可以通过gain/offset改变拟合五角centroid至max residual.002577keV；sourceindependentcalibration可能排除alternative，因此不宣称Crespi实际β有歧义。方法页已保存所有units/assumptions。

Recchia2009/Söderström2011metadata身份已确认，但publisher、HAL只有metadata、GSI connecttimeout，暂不从二手摘要生成新实验claim。正在读公开AGATAoverview的直接commissioning与response主线以补充比较边界；该instrumentoverview引用其它实验不当成新独立acquisition。课程仍next14/count13，回执running，未给额外学分。


### 持续Day13：staticposition与algorithm-response验证

[[akkoyun-2012-agata-instrument-response]]的41页主线和Sec9–11关键证据已核（AK12-1–7），原preprintfig39/40与thresholdparagraph视觉核验。static60CoComptonimage约5mmFWHM减少beamkinematics依赖，但PSA/sequence/calibration仍共享。sourceactual3ATCtest的rawP/T16.8%、tracked53.9%、FEPcountpreservation84.5%区分两种指标，不能当absoluteγefficiency。fullarray/algorithm比较与thresholdloss为simulation语境；citedRecchia/Söderström原文仍未取得，不用overview重复计实验。

关键reusable结果和最小validationmatrix已写回tracking/Doppler方法。raw仍不变；新source保留publicURL/version/SHA与未填充rawarchive边界。当前选择继续研究energycorrection与angularframe/acceptance：窄化peak不消除photonaberration或energy-dependentlabresponse。dayindex13不变，Day14仍partial，未开Day15卡。


### 持续Day13：energy与angle/acceptance变换

复核L26-2/3/8原Eq2/18。[angular-acceptance code](../../system/scripts/day13_doppler_aberration_acceptance.py)与[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/aberration-acceptance-exercise.json)将restisotropicphotonboost到lab，energy校正仍将allphotons恢复1000keV；finiteangle的per-solid-anglecounts不flat。β.07时145/90densityratio0.894825，加入明确自设ε(E_lab)后0.935502。maxMCbinrelative差1.69%，whole-sphere/Jacobian/static/energyinverse检查通过。

boostaxis、labbeam/quantizationaxis、angularaberration与energycorrection分别声明；realarraygeometry/response/feeding/covariance不在toy内，没有新δ/alignment测量。新推导写回Lorentzconcept和Doppler方法，Longfellowhuman-reviewedsource和其claimflags未改。学习仍active，下一路eventdisplacedvertex/lifetime/feeding选择，不开Day15卡。


### 持续Day13：delayedvertex/feeding的conditionalresponse

[displacedvertex code](../../system/scripts/day13_doppler_displaced_vertex.py)与[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/displaced-vertex-feeding-exercise.json)将sourceAA09-1/4的远发射点条件推进为明确toy：恒定knownβ仍因错误targetvertex有同号low-energyresidual；detectedtimes须按angularJacobian/projectedarea/distance²加权。β.3/R150mm/τl2ps在90°的mean为−.3765keV，另有τf20ps时为−4.0838keV；actualnuclear参数/response未代入。

idealproper-time10psgate在同一τl2ps下接受direct.993262/feeding.326826，需与actualtimestamp/flightpath/response区分。48/96点quadraturemean差≤2.2×10⁻12keV、MC/CDF/Erlang2/static检查通过。line-tail为nonGaussian，σ不冒充FWHM。推导、参数、numerics与独立promptvertex/held-outtime-gatefalsifier已全部写回Doppler方法；无新实验lifetime/B。学习继续。


### 持续Day13：探测器中子宽线与 cut-contract 反证

[[senyigit-2014-agata-neutron-rejection]]已读公开15页preprint及核心tables/figures；Crossrefjournalyear为2014，2013仅preprint/online年。Ge-recoilvisibledeposit叠加γ造成约40keVhigh-sidebumps，γTOFgate仍有其它material真γ；27Al2211-keVpeak的reportedFWHM15keV与paper引用τ26.6fs所给naturalΓscale2.47×10⁻5keV是不同物理量（SY14-2/3/4）。

[neutron/width/selection code](../../system/scripts/day13_neutron_width_selection.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/neutron-width-selection-exercise.json)核验natural-widthunits、straight-flightTOF和Table4nestedpercent分母；57%再28%中心值合69.04%，不相加。SY14-6/7保留body/table/conclusion的谓词及Co列差异，未选择actualproductioncut。若固定same-cluster/energy/peakcount的post-filter前提成立，Table2literalORaccept含E1>30进而含E1>45，联合Co1332loss应≤单项3.9%，但报告18.5%；此条件反证说明summary不足以复现cuts，非actualcodebug结论。

IAEALiveChart12C/27Al两官方host返回403challengeHTML，未当CSV或level核验；TUNL首条guess路径404，正在从官方index找真实入口。τ/Γ使用sourceinput边界，未补写12Cnaturalwidth。学习保持active、deadline不改、课程next14/count13不再推进。

### 持续 Day13：评价宽度、branch 分母与 photon recoil

[[tunl-2017-12c-level-widths]]读取范围是官方在线 Tables 12.13/12.14 的选定记录、footnotes及2020修订 companion 的身份与对应行；没有把257页评价全文算作已读。Table13 p3给15.110-MeV态 total Γ=43.6(1.0)eV；Table14 p1给ground γ partial 38.5(.8)eV、total γ 41.8(1.1)eV。以 total Γ 得中央 mean life15.10as；ground γ占γ子集与all-decay的中央比约.921/.883，分母不同。派生宽度共享输入、joint covariance未给，不制造独立ratio误差。

[photon-recoil code](../../system/scripts/day13_photon_recoil_width.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/photon-recoil-width-exercise.json)检查自由两体衰变的四动量与母/子frame反演。mass-number近似A12、gap15.110MeV给母系photon15.099801MeV与recoil10.198843keV；用紧接γ后的子核速度反演，得到另一frame且高20.411473keV。此差在理想四矢量算术中不依赖lab角度/boost。A52、gap1.434MeV的frame差仅约.0424keV，不能单独解释旧simulation约2-keV问题；后续未测γ/particles还会改变terminal-residue stage。

这些推导同步到Doppler、level-scheme、Crespi follow-up与provisional note。source保留online获取版本/hash与未归档raw边界，圆整15.1-MeV标签不构成实际sorting错误证据。当前仍research-active，下一步检查Lorentz/Gaussian convolution与finite gate，课程学分不变。

### 持续 Day13：Voigt 线型与门内强度

[线型代码](../../system/scripts/day13_voigt_gate_response.py)与[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/voigt-gate-response-exercise.json)验证归一化、独立卷积和零核极限。自设Lorentz/Gaussian FWHM各20keV，真实Voigt FWHM32.751907keV，平方和28.284271低13.64%。用相同真实FWHM W比较 `±W` 门，Voigt/Gaussian接受.798321/.981468；相同峰宽不等于相同门内fraction。

TUNL .0436-keV natural Γ加到仅作对照的119-keV Gaussian，FWHM119.023221keV。这个尺度检查限制天然宽度主导，却没有从Crespi观测谱中分解Gaussian响应。理想Lorentz没有有限variance，不能把Γ当σ代入先前Jacobian误差预算。公式、有限窗/物理阈值条件与必要实验输入全部写回[[doppler-correction]]；本例没有新增真实line fit或absolute yield。

### 持续 Day13：missing momentum 与阶段约束

[阶段代码](../../system/scripts/day13_missing_momentum_stages.py)与[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/missing-momentum-stages-exercise.json)区分两种条件。先蒸发neutron、后发射目标γ时，错用compound平均boost留下recoil分散；自设Tn2MeV、gap1MeV、A130给σ.292439keV，正确emitter vector反演消除此项。固定能量/各向同性才给box profile与简化sqrt(n) law，未重跑AA09 evaporation chain。

另一条件反例固定observed photon、terminal residue及initial invariant mass，却允许未知中间态和晚neutron方向；可得不同earlier-parent velocity/rest-photon energy。它不声称Klemme或VAMOS的低位束缚γ有晚neutron。已知中间态、完整particle测量和material-loss packet能增加约束。AA09-9新增原Fig2.2/6.12与Sec5.3 locator，stage diagram与所有数学边界已写回Doppler方法。

### 持续 Day13：两距离标定与 tracking 参数单位

原Recchia2009/Söderström2011文章的Crossref身份已核验，但institutional route仍只有metadata、403/timeout或CSIC的受限占位PDF，未新增其直接实验claim。已取得并阅读全文[[soderstrom-2008-agata-position-design]]10页与[[crespi-2023-agata-tracking-performance]]43页；综述重复的CR13/SY14/Recchia数据不计独立acquisition。原SD08 Eq4.4的未平方宽度/距离差经视觉核对保留，未声称production code错误。

[two-distance code](../../system/scripts/day13_two_distance_resolution.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/two-distance-resolution-exercise.json)另行声明W²=B²+(kp/R)²；true first-IP距离与共同B/k/p才支持平方差反演。自设front40/140mm、IP在front后30mm，误用front使p5mm估成2.71694mm。若近geometry baseline改变，两点仍零残差拟合，却在第三distance失败；小杠杆/误差还可产生负p²，不能clamp成已测p0。covariance MC和Jacobian核验通过，所有条件写回Doppler方法。

C23-4的OFT自由参数σθ单位cm，不能当Doppler rad角误差或直接PSA FWHM。C23-8原Eq7独立匹配精确Jacobian，速度一阶零敏感角cosθ=β，90°只是低β近似。static imaging共享PSA/order/model，联合PSA/tracking改进仍为作者未证实建议。raw全保持不变，新public copy/hash/未填充槽位明示，研究继续active。

### 持续 Day13：selection normalizer 与 held-out 检查

[gated-likelihood code](../../system/scripts/day13_gated_likelihood.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/gated-likelihood-exercise.json)对自设Gaussian μ1.2/σ2keV实施fixed±2keV门。naive Gaussian得到μ.342411/σ1.050582keV，含parameter-dependent selection normalizer恢复1.203206/2.005365；known-total-trials再提供acceptance约束，但只有toy具备这个输入。无门极限、积分/MC和近Z1的tail数值检查通过。

rate依N0×ε×Z，selected count或normalized shape不能独自给absolute yield/所有response参数。same-source test split检查随机过拟合，却共享gain/basis/geometry的systematic；held-out line/energy/location、independent particle或third geometry才约束不同项。所有公式、数据边界和必要packet写回Doppler方法，未诊断actual source fit错误。学习仍active，下一步检查partial particle geometry与vector可识别性，不开新日卡。

### 持续 Day13：GANIL primary 与 joint event-mixing response

[[ljungvall-2020-agata-ganil-performance]]public copy33页主线已读。六detector Doppler-position估计使用VAMOS vector、relative speed输入、Geant4 target/acceptance和energy-dependent one-dimensional IP FWHM law，得到平均5.1mm但作者保留1mm估计误差及detector spread的统计解释。原events/basis/code仍未取得，C23重复该source benchmark不新增独立实验。公开copy的2020 arXiv标头、2022submission footer/build metadata，以及body/conclusion before-core width2.93/3.08keV打印差均明示，未静默合并版本或更正原数据。

[event-mixing code](../../system/scripts/day13_event_mixing_acceptance.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/event-mixing-acceptance-exercise.json)构造声明的positive joint-acceptance fixture，遗漏pair-response使true a2=.102拟合成−.165398，matched joint normalizer恢复原值；不是实际OFT重放。另独立common-beam-axis photons的pair-angle a2=A2²/5，A2自设1时quadrature .2、MC .199326±.003239；独立event不等于isotropic normalizer。

原LG20 Fig18直接比较mix-before/aftertracking，LG20-12明确source→beam迁移条件。公式、toy假设、zeroacceptance和normalizer covariance全部同步tracking/coincidence/Doppler页。研究持续active，未给额外day credit，下一路线是partial vector可识别性、heterogeneous response和量化判别设计。

### 持续 Day13：global vector 多解与 Cartesian covariance

[vector-global exercise](20261013-DAY13-doppler-correction-recoil-velocity-run-01/vector-identifiability-exercise.json)由[code](../../system/scripts/day13_vector_identifiability.py)构造knownβ/knownrest-energy/commonvector的两mirror directions。两nonparallel coplanar photon constraints均精确符合，两个local Jacobians都rank2；所有coplanar directions仍不能判别mirror，新增noncoplanar方向预测energy差2.793137keV。是不同calibration emitters的声明fixture，不冒充actual finite-mass cascade或CR13 fit歧义。

[Cartesian code](../../system/scripts/day13_vector_position_jacobian.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/vector-position-jacobian-exercise.json)从(E_lab,b components,emissionvertex,first-IP)推导10-input Jacobian/Σ，避免derivedθ误差重复叠加。有限差分、radial零项、scalar equivalence、β0与commonframe invariance/physical target shift区别通过；MC σ相对差最大.0954%。全部数学、参数与边界写回Doppler方法，尚无actualsourcejointΣ，学习继续active。

### 持续 Day13：heterogeneous IP response 的平均规则

[response-mixture code](../../system/scripts/day13_heterogeneous_response.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/heterogeneous-response-exercise.json)以LG20 Eq4作声明模板，actual source范围/参数未重拟合。自设two-deposit groups及geometry得mixture half-height FWHM7.484993keV、same-variance Gaussian宽9.706038、先平均p再平方的宽8.903350。要平均conditional variance，且总体mixture不再单Gaussian；相同FWHM/σ不保证相同gate fraction。

known per-event σ及common centroid下的weighted estimator提高toy精度，group offset或错误σ则破坏前提；没有因此升级C23的未证明tracking建议。积分、Gaussian极限及MC通过，公式/参数/covariance/fit-window边界固化Doppler方法。顺带将T12C的Ex单位写为15.110MeV±3keV，避免MeV中心值/keV不确定度文字歧义，不改source数值或raw。

### 持续 Day13：tracking 与 Doppler 的 frame 次序

[frame-order code](../../system/scripts/day13_tracking_frame_order.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/tracking-frame-order-exercise.json)构造真实kinematic一致的free-electron two-hit fixture。先把所有deposit乘incoming Doppler D，虽然总能量仍correct，却破坏保持lab angle/静止electron假设的Compton test；β.07例true cos−.9会错读成−1.038。完整boost同时变换electron/photon四矢量则守恒，β0回到相同顺序。

该反证检验处理frame与stage，未重放实际OFT/GRETINA或指控来源code。LG20 chain/C23 Compton/Doppler原locator、公式与boundary已写回tracking方法。原谱窄化不能独自证明selection/ordering无误，下一步继续精度与observability设计，仍active-Day13。

### 持续 Day13：retarded arrival time 与 energy factor

[retarded-time code](../../system/scripts/day13_retarded_arrival_time.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/retarded-arrival-time-exercise.json)核验a(t)=γt+[R(t)−R0]/c，da/dt等于instantaneous Doppler inverse factor，独立photonboost×numeric derivative恢复E0。自设β.3/properτ10ps/R150mm，35/90/145°detectedarrivalmean约7.98/10.46/12.92ps，10ps门接受约.714/.616/.539；另加自设1000psjitter后接近.501/.500/.499。

proper τ、lab emission γτ与conditioned arrival history分别记录；理想time gate不等actualtimestamp或已测寿命。积分/MC/static/far/boost检查通过，完整formula及start/path/walk/stopping/feeding边界写回Doppler方法。本段持续active，后续精度/near-zero sensitivity与自然宽度frame映射，未新开课程卡。

### 持续 Day13：zero-sensitivity curvature 与 narrow-width recoil

[curvature code](../../system/scripts/day13_zero_sensitivity_curvature.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/zero-sensitivity-curvature-exercise.json)在cosθ=β0构造first-derivative0的三组例题。仍有quadratic误差；fixedlab/uncertaininverse与trueβspread/fixedinverse的residual符号相反，不能混为独立项。exactMC/二阶FD/zero-noise核验通过，所有参数自设，不识别实际tail。

既有[photon-recoil code](../../system/scripts/day13_photon_recoil_width.py)与[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/photon-recoil-width-exercise.json)新增mass-energy derivatives检查；在narrow independent Lorentz模型下，Γph与Γlevel由two-body slopes联系，heavy recoil-neglected才近似Γi+Γf。A12/gap15.110的mass-number例题将43.6eV映为43.541182eV，约.0588eV小于源1eV uncertainty；未改评价数据或拟合真实photon谱。canonical公式/限域均写回Doppler方法，研究继续active。

### 持续 Day13：MUGAST primary、light recoil 与 integer PID

[[assie-2021-mugast-agata-vamos]]公开13页全文与Fig17/18/式已核。实际19O(d,p)20O的1.673-MeVline从meanbeamβ.126校正FWHM10.2keV，改为lightparticle measuredmomentum/two-body重建后7.1keV；共享同acquisition，未从总差反解single nuisance或制造显著性。该run有Au backing、source未完成一种target-loss监测，16Ocommissioning又缺absolutebeam normalization，均保留。

[rigidity/PID code](../../system/scripts/day13_rigidity_pid_covariance.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/rigidity-pid-covariance-exercise.json)自设L7m/A20/q8/β.126/relative designσ.002，path/rigidityρ−.8/0/+.8给flightσ.698/.520/.233ns；source.2%resolution没有明示σ/FWHM，未拿toy复现800ps。alternateintegerlabels有不同β，但未赋actualmis-ID概率；knownreaction/independentline/PIDpacket可排除这些模式。

Source1.4MeV归一的differentgeometry transparency比较不是absoluteresponse；三subsystem tag也非三个独立实验。Source target CH2/d-channel及51/57-keVprinted间隔差有locator，未改raw或补猜actualmanifest。所有重要方法/反证/locator同步Doppler/tracking/coincidence/index，学习持续active，不新开课程卡。

### 持续 Day13：exact reaction、feeding stage 与 inverse 多解

[two-body/entrypoint code](../../system/scripts/day13_two_body_entrypoint.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/two-body-entrypoint-exercise.json)锁定synthetic19u/Q5.4MeV质量体系，逐reaction/γ mass shell和四动量守恒。Observedlowerγ不自动确定reactionentry；强制wronglower entrymass，允许beamT自由时有10.73376/66.21207MeV两解，均被本例known152MeV排除。实际sourceAS21-12提供独立particleEx×gamma entrypoint语境，未虚构actualbranch。

第一轮singlebracket求根失败已保存[first-attempt](20261013-DAY13-doppler-correction-recoil-velocity-run-01/two-body-entrypoint-first-attempt.json)；非单调masscurve的解析minimum定位后两root分别bracket，原命令回归通过。SelfchosenΣ的γσ预测/MC.059621/.059667keV不含target/PSA/history，不解释实测7.1keV。Method记录所有条件/失败/反证，研究仍active，下一步整合minimal validation contract与继续高信息来源路线。

### 持续 Day13：minimal validation contract 与 self-audit

新增[[doppler-velocity-validation-contract]]作为简明canonical入口；EvidenceMatrix把实际width/PSAmodel/作者floor解释分列，contract逐项给identity、velocitystage、frame、Σ、selection和下游τ/B的最小输入/失败条件，详细数学保留methods。DVV-P1-1/2/3完成Codexself-audit，sourceunreviewed/未归档raw、production/response/covariance缺口仍明示，不升humanreview或结构信心。

这是活动阶段的知识整理，不是全窗口closeout。课程仍next14/count13、Day14只有既有partial。下一高信息路线为AGATA/VAMOS prompt/delayed/degrader的速度stage与98Zr数据谱系，需读直接sources，继续按原15:00硬截止研究。

### 持续 Day13：fission/degrader 与20O status的直接source对照

[[lemasson-2023-agata-vamos-fission-history]]12页全文/Table1/Fig6已核；98Zr1222.9line的EXOGAM15(all)/7(back)与AGATA5keV角覆盖不同，spectra又按totalcounts归一；原C23简述不扩写为matchedgeometry纯算法factor3。Post-degrader vd reference让U恢复而S保留低能angleband；U仍moving，FPdelayed又是stoppedstage，数据来自不同Exp1–4/refs。

[degrader code](../../system/scripts/day13_degrader_reference_history.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/degrader-reference-history-exercise.json)用声明的β/lossclock/idealcap/σ1keV，gap.470mm directτ3.8的afterfraction.02867、feeder7.5后.30572；conditionalenergygate又变样本。Sourceτ仅设scale，未fitRDDS。Delaysurvival[code](../../system/scripts/day13_delayed_survival_selection.py)/[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/delayed-survival-selection-exercise.json)的properclock/stopwindow/velocityMC也通过，原窗口capability不是executedgate，未提取新isomerlife/ε。

[[ciemala-2019-20o-dsam-analysis-status]]官方10页全文与calibration/Fig8核验；实际18O+Ta深度非弹性data不是MUGAST19Otransfer。Source报告RFdrift与energy/PID共同校准，longlineτ10.5ps为参考、NN320/NN+NNN200fs为模型，below~300fs是初步解释，jointτ/Eγfit仍待进行。Forward/currentβ与targetexit处理及outputvelocitylabels保留executionstage边界，未指控sourcecode错误。

Ref11 PLB135939 identity查核为17C，仅metadata候选、不用作20O backingprimary。所有importantcontrasts/formulas/falsifiers已写canonicalmethods/synthesis/sources，研究继续active，后续量化τ/Eγ辨识设计与sourcecalibrationroute，不开新课程卡。

### 持续 Day13：τ/Eγ designinformation 的模型条件

[lifetime-energy design code](../../system/scripts/day13_lifetime_energy_design.py)、[JSON](20261013-DAY13-doppler-correction-recoil-velocity-run-01/lifetime-energy-design-exercise.json)以声明slowing/σ/threepointangles生成normalizedprofiles。在τsynt.20ps条件下，τalt.32ps改E0可让三centroid残差≤.167keV；fullshape另给最小conditionalKL.02843494/photon。Expected2NKL依自设exactmodels/counts，不是sourceχ²/CL或NNNforce比较。

归一化/timequadrature/independentMC/no-loss/largeτ/identicalKL极限通过。实际CO19 jointτ/Efit仍未在2019报告给出，stopping/feeding/response/Σ不全，未借toy量化actualτ。新Ref11 bibliographyclaimAS21-18及所有design参数/边界已canonical写回，learningactive，后续check/publish与直接calibration来源，不开新课程卡。

### 持续 Day13：direct calibration 与 reference covariance

[[ziliani-2019-agata-calibration-controls]]官方7页全文/TableI/Fig4核验，sameJuly2017data与CO19互引。GGPtimestampsreplay对齐、tightpromptgate提高P/B>2且photopeakcounts损失<4%；corecal用Eu/AmBe及2–3MeV背景Pb/Mganchors，14A/11C借segmentsenergy恢复。TableI是resolution%未explicitσ/FWHM；2754.007Mg背景线不能当Eu-decaybranch算ε。

DirectRef8明确18O1938.2(2)短τprinted26.5(29)fs、1981.93(9)长τ2.80(7)ps；不同history的近energycontrols辅助排共有calibration趋势，sameexperiment不算独立两数据。Source仍preliminary，不补final20Oτ。Commonenergyreference也不会因31crystals按√31消失；简单Σ示例已canonical，数字自设不等TableIaccuracy。所有事实/locator/transfer条件同步methods/source/synthesis/index，研究active。

## Counter-evidence and missing companion observables

1. Klemme Fig.1同一line有距离相关shifted/unshifted分量，反驳“两个峰必是两条跃迁”；Table I的6g+从1.38到corrected1.63ps增加18.1%，显示finite stopping影响寿命。
2. Herzáň Fig.5(a)的quadruplet反驳“一个谱峰必是一条γ”；低能非观测的解释不能自动填成已测线。
3. rank-2是推导层反例，反驳width-only decomposition的充分性；它不声称Mavela真实nuisance就是这组值。
4. 必需packet：executed sorter/geometry/β inputs、ring/sector与γ-crystal切片、matched gates、energy calibration/response、joint covariance、stopping/feeding metadata。缺这些不能比较β20/24的实际影响或修订GOSIA/Q_S。

## Knowledge Impact and Learning Decision

`supports`：exact correction、逐emitter谱/yield身份、stopping与谱峰/跃迁区分。

`revises`：多角度width可诊断输入，却在已声明低速模型中不能独自分解三个nuisance；应先取得独立calibration。

`limits`：总谱窄峰、shared gate、energy closure、relative Iγ与模型曲线的结构推断。A≈130 chirality/wobbling/signature/configuration解释排序不变，未获得新绝对B矩阵。

最终方法判定固定在 [[doppler-velocity-validation-contract]]“统计与速度分析之后的判定表”。`revises`：精确变换/正确countstatistic/窄region并不是完整物理模型验证；bin积分、观测selection、shareddata、velocityreference/history与region语义须分别闭合。`supports`：独立且stage正确的particle/control、完整on/off/template输入及model-awareclosure是有效判别路径。`limits`：本轮selfchosenmodels不裁决source发生何种bias、不解释真实20Oτ差异，不增加A≈130绝对strength/mode证据。

[来源后复述](20261013-DAY13-doppler-correction-recoil-velocity-run-01/day13-post-study-recall.md)的12项答案已回链canonicalowner；self-audit不是盲测/humanreview/Day14周考。十项当前分析的参数、units/frames、seed/datahash/依赖与limits见[可复现manifest](20261013-DAY13-doppler-correction-recoil-velocity-run-01/statistical-velocity-analysis-manifest.json)和对应代码/结果。来源事实、作者解释、模型输出与任务推断仍按原记录分层。



### 20O 两次独立测量：primary 与 supplement 审计

持续路线截至2026-10-14 07:48 Shanghai仍active，不计新卡。来源前primed recall见run-dir `oxygen-final-source-before-recall.md`；两primary七页全文及2023四页SI已经读过，Fig.3(old)/SI Fig.5的τ–Eγ面和表注视觉核验。Raw保留未填充，publicURL/version与三份PDF哈希均写入source；SI自公开authorarchive读取，不执行source。

| 层级 | 本段核实内容 | Canonical locator |
|---|---|---|
| 实验/分析报告 | 2020 totalτ150(+80/−30)fs、E2394.6±1keV、branch79(5)%、partialτ190fs；16C是E条件结果。 | [[ciemala-2020-c16-o20-lifetimes]] CI20-3/5/6/8 |
| 实验/分析报告 | 2023 totalτ70(10)fs/90%70(14)、3+54(9)/90%54(12)；质子给state-entry速度/Ex，SI新1156feeder BR28%。 | [[zanon-2023-o20-high-precision]] ZA23-1/2/3/4/5 |
| 作者解释 | 差异原因未完全理解，initialvelocitymodel或unobservedsidefeeding候选；作者“cancelled”强措辞不视为本任务证明。 | ZA23-7/8 |
| 模型输出 | NN+3N/VS-IMSRG/USDB强度/τ是模型；3+分量用USDBδ.13/.019，未知experimentalδ。 | CI20-9/10; ZA23-6/12/13 |
| 本任务推断 | 各velocitystage、Ex迁移、response/stopping、τ–Eγ需共同验证；能量最佳值差的影响只是待检验候选。 | [[doppler-correction]]“20O 两次独立寿命测量的速度与馈入对照”; [[doppler-velocity-validation-contract]]同例 |

反证/必要观测已在canonical表逐项列明：gateleakage上界与1156taggedγ、state-conditioned entry/exit分布和Σ、independentstopping/targetthickness、held-out角度/能量以及实际τ–Eγ数值面。19Olongline的extendedχ²valley、16C的energycondition与未知3+δ均反驳“任一Dopplerfit都给精确τ或纯实验B”的过强结论。2019/2020同data互依赖，2023是独立采集；装置原理/外部stopping库共享不等已经知道数值crosscovariance。

设计练习：两入口模型 `f=P3×.28×A3/(P2×A2+P3×.28×A3)`，等population/acceptance仅得f=.21875，meanproperwaiting约81.81fs；不是reportedf或fittedτ。70+54f的simplecascade即使f=1仅到124fs，显示该单支路不能单凭BR.28就断言造成旧150fs；不是排除真实2020全部sidefeeding。已写回方法页，后续将计算gate迁移/线形/统计辨识性。

Long20Ocontrol的Au-loss correction与data/simE/FWHM为具体response检查；其vectorconvention不自动覆盖每个shortline。SI的Neymanχ²、≥10eventsrebin及jointΔχ²2.3/4.6完整保留，不假设精确Gaussiancoverage。无raw事件/χ²grid/生产模板，L4仍not-ready，不pool或给差异的精准σ。

下一高信息route已做primedsource-before recall：Ciemała方法篇DOI10.1140/epja/s10050-021-00451-6、公开arXiv2012.05180v1；本段尚未读取其body，不预写方法新结论。


### 方法正式版本、feeding/Ex设计与数据入口续核

沿用phys-model处理有界模型，source前回忆在`deep-inelastic-method-source-before-recall.md`，version控制回忆在`cm21-version-control-recall.md`，模型设计前回忆在`entry-gate-feeding-design-recall.md`。[[ciemala-2021-deep-inelastic-lifetime-method]]公开v1与publisherfinal各17页读完，identity/hashes/版本已隔离。

新的直接反证：v1 p.7 Eq1 lab分子标签冲突，在publisherp.6已由consistent measuredEγ/correctedEγ0及乘D消除；当前arXiv仍旧hash。正式版aftertargetvelocity含DC-loss/path和Z-dependentTfine-tuning；fulltarget/yellow与first10layers/green也替代v1midtarget/green。不能说所有版本都有公式错误或因v1label判生产τ错误。精确90°γexit/γem仍有transverse项，与finiteangle应共同考虑，illustrative四向量/零极限检查通过。

Publisher pp.12–14还明确totalerrors的statistical/stopping/background/ionvelocitysystematic贡献及80%CL；v1叫1σ。Publisher称cumulativelifetime含可能feeding、以未见populatingγ解释其cases贡献可忽略。逐versionconfidence/负证据需要保留；2023有新1156feeder不自动给2017reaction的布居或f。Canonical方法/synthesis已经修订，sourceauthorinterpretation与任务判断分开。

Gate/feeding数值设计采用自设ExGaussianσ、P3/P2、gate、properβhistory与response，无真实events/Exresolution/Austopping。P3/P2=10时σ.25/.5/.75MeV给f.000314/.180708/.466922；σ.5下gatecenter−.1/0/+.1给.124381/.180708/.255055。f=.5、两步70+54fs条件模型的prephoton mean97fs，错设no-feeding fixedE fit96.71fs，profileE fit94.05fs/E+.768keV，KL.009687/photon；其它f表与公式同步写 [[doppler-correction]]。这是expectedshape projection而非实际χ²/CL；600k独立MC、解析survival/equalτ、quad128/256与no-loss/f0验证通过。

DataCite核实e775s DOI与2020collection/2025embargo结束/CCBYNC metadata；印刷URI格式异常保留，registryAu20mg/cm²/intensity2e5为designfields，不能替main24.4/4e5。PubliclandingHTTPS ConnectionError、HTTP ConnectTimeout，未读取events清单；失败来自网络，未声称权限拒绝。CM21final的articleCCBY4与AGATAdataownership亦分开。Actualevent/code/χ²/template/Σ仍缺，L4refit not-ready。

原窗口研究仍active，本段source/method/practice完成不触发新学分或收束；下一候选为有条件计数/fitstatistic与RF/TOF alias、TKEL反演closure，仍限DAY13。


### RFphase/rigidity 的离散反例

来源/设计前回忆`rf-tof-alias-design-recall.md`，selfchosenconstantflight/mass=A u/path/phase-noise等模型`day13_rf_tof_alias_design.py`与run-dirJSON已通过。构造(19,8)β.1/(20,6)β.071426的flight254.968470/356.968470ns，102nsperiod下phase均50.968470ns且Bρ相同。条件于truebranchβσ.00041345（500kMC.00041354），全局alias仍成立；自设independentETOTσ2MeV分开89.161/47.704MeV后排除错误支。Toy1375.80keV/150°错分支校正偏−34.6456keV，非reportedoffset。

Canonical公式、表、适用/反证已写[[doppler-correction]]“RF周期编号与连续速度精度的不同信息”：只有periodindex丢失才适用；sourceactualunwrap未知，absoluteclock/q/energy或可靠knownγhold-out能排除alias。C(M)21提供RF/aftertarget定义、AS21提供conditionalintegerPID，不能说source确实只保phase或已经错k，也不能把同PIDrigidityspeed当独立clock。


### 计数原报告与jointregion设计续核

来源前回忆见`lineshape-statistic-source-before-recall.md`；先独立完成uniformrate/Gaussianregion推导和MC，再打开Baker–Cousins原报告。Crossref/INSPIRE核题名/作者/1984publication与UCLAHEP83-3/KEKSCAN83-11-266；沿KEKpubliclocator取得22页July1983/acceptedOct1983报告，封面/pp.8/12公式视觉核验。FNAL猜测候选403且未验身份，未被写成来源；actualreporthash/URL/覆盖范围在[[baker-cousins-1984-histogram-fits]]，raw保留未填充。

SourceBC84-1/2/3/4/5/6/7/9分开pointestimate/interval/GOF、binintegral、Neyman/Pearson/Poissondeviance、Poissonrate/conditionalmultinomial与freeoverallscale保证area的条件。本文作者本身提醒finiteN/ML/WLS bias与MC验证；任务没有把ML描述为万能无偏。

自设32同meanPoissonbins、200k重复：μ50/100/200的Neymanmean49.011/99.018/199.037，Poissonmean49.9997/99.9970/200.0100。全模拟observedminimum17/50/132，均≥10，证明该计数阈值本身不保证rateestimator无偏；无真实τ/E数据，不估source寿命bias方向。Scoreclosedform/PoissonMC范围检查通过。

另一regularGaussiancontrol（στ10fs/σE.4keV/ρ−.8，均自设，不视作sourceΣ）：Δq2.3 joint概率68.336%，τ轴projection87.063%；忽略covarianceoffdiagonal的MCjoint71.742%。1MMC核analyticjoint/projectedCDF及energyprofileidentity。SourceCM21/ZA23/CI20的quotedintervals不由该toy重标或Gaussianpool；trueτerror需actualstatistic/template/Σ/confidenceconstruction。

这些meanbias、χ²field、normalization与validationpacket已经同步写[[doppler-correction]]与validation-contract；script`day13_count_statistic_regions.py`、outputJSON均标synthetic。Source方法全文和局部quantdesign完成只算checkpoint，原researchwindow仍active；下一高信息route是TKELbasis/depth/response的inverseclosure，未启动其它日卡。


### Entry history 的exactfeeding反例

在后续复杂TKEL/depthclosure之前，先解决更直接的可解析entryhistory问题；设计前回忆exact-feeding-entry-history-recall.md。模型完全自设：effective tau120fs可由固有lower tau60fs、upper tau120fs、direct/feeding各.5产生相同全properwaiting density。Density/Laplace/allr端点、normalization/firsttwo moments与600k独立MC均通过；共同自设transport/response三角energyprofile差1.4e-17。不是sourceevents、realKS/p-value或tau差异归因。

Canonical公式/条件/反证已写[[doppler-correction]]与validation-contract：只有共同K、未观测feeder/无recoil/statechange等声明条件下成立；particleEx directentry、feeder gamma/upper tau/布居与实际multiplicity/response可排除或打破。已知ZA2354fs上态/.28branch不等本构造。单target gamma fit即使精确，也须与cumulative/固有tau区别一并传到strength链。

来源/模型/任务推断分开，next14/count13不变；原窗口仍active。下一candidate TKEL/depth/responseinverseclosure仍未做，不把这项解析完成当schedulelevel结束。


### Cascade recoil 的限定检验

设计前回忆cascade-recoil-degeneracy-check-recall.md，constant-flight/massproxy/isotropicupper+target两γ练习已执行；exactfeeding的新物理边界明确包括upper recoil、state-dependentalignment/角关联、selection。Boost/mass-shell/角normalization/analyticmoments/600kMC及limits通过。

自设A20/gap1MeV/Eγ2396.1keV，feed-only recoilσ.07425keV，50%mix+σ2keV后2.000689keV；fixedresponseKL1.187e−7/photon，未知mean/σ时KL<1e−12数值未分辨。任一expected2N×KL都只是chosenmodel/count的designmetric，无realχ²/CL或sourceprecision声明。代码特意用parentreference遗漏kick，不代表实际VAMOS已采用该reference；foiltransport/cascade角关联未模拟。

推导/参数/表/反证同步到[[doppler-correction]]与validation-contract。Upper photon/independententrytag、真正responseΣ仍是必要伴随条件；不从理论上理想退化被打破就断言真实数据能区分。原window仍active；下一TKEL/depthclosure尚pending，不计新卡。


### Depth/exitvelocity 的特殊极限closure

设计前回忆tkel-depth-response-recall.md；generic20u/共线foil4um/beam100/channel4MeV/constantS2.5、三depthprior、trueτ80fs的selfmodel已执行。三prior均final86MeV/β.09575459，初分布/γhistory不同；wronguniform fixedE τ80/42.59/172.82fs，profileE τ80/40.05/190.73fs（uniform/front/back），残余KL非零可被完整shape/control反证。Uniform一个optimizerstart nonsuccess已留flag，另两恢复truth，不隐去数值失败。

properclock与路径积分、500k/每prior独立MC、归一化/quad和long/no-loss通过。SourceCM21-21正式targettilt45degree/θφaperture新atomiclocator与已有100layer/TKEL/stop一并写回，实际geometry并不满足toy共线条件。仅说明measurement/prior/independententry的关系，不估真实sourcebias，不解释150/70，L4refit仍not-ready。

知识与表同步[[doppler-correction]]/validation-contract/sourcecard；原window仍active、next14/count13不变。重建候选池后，下一高信息route可转particle-assistedkinematics的publicsoftwareobject/units/stage，以及有限bin/background/templateΣ；已完成物理toys不重复。


### Particle-assisted kinematics 的历史publiccodeobject审计

来源前回忆nptool-code-object-source-before-recall.md。公开GithubREADME核实迁向GitLab，后继API ConnectionError/page timeout，故只审2019NPTool.2.dev pinnedobject；source/mainheader/selectedNucleus/units/constants/license均按Gitblob+SHA256验证，thirdpartysource未build/execute。Canonical [[nptool-2019-reaction-velocity-code-object]]明示readscope/commit与sourcepaperexecutionunknown，raw仍保留未填充。

直接代码证据：输入light动能MeV/角rad、beamtotalT、beam+z/targetrest/planey0；P4=Ptotal−P3，Ex相对配置Mass。Reaction4vector和Nucleus对象更新不同；NucleusMass含Ex，SetEnergyImpulse从E与对象Mass重算scalarβ，TOF为inverse-speed s/m、velocitycm/ns、Bρ默认Q=Z。Actualcaller/φrotation/mass/beamvertex/energycorrection/stage不能由库名保证，getter互相转换不新增independentclock。

自设20u/Ex4.071/trueβ.126的mass-shellsanity，错误groundMass重算β.127695、chosen2396.1keV/150°校正偏+3.695keV；正确mass与P/E一致。mass19u下8AMeV须total152，两个单位选择的nominalbeamβ.130223/.030057；β.1的derivedper-lengthT与D8m转换266.851ns。Genericendothermic5MeV/T10的labtotalEhelper通过而invariantthreshold55.0067未过，限定helper/branch/domain需核。全部是physicalcounterfactual，不是源代码执行或真实e775/150-70差异诊断。

公式、producer/schema/单位表和数值已同步knowledge，source/author/code-model/任务推断分层。CM21 source table原14–21row被空行隔断的格式已经合并，所有已核claim现在纳入机器governance检查；事实/状态未升级human-reviewed。Next14/count13不变，研究仍active；下一有限bin/背景与templateΣroute有高信息工作，未formal打开其它日卡。

### 持续 DAY13：有限 bin 的积分与信息损失

[设计前回忆](20261013-DAY13-doppler-correction-recoil-velocity-run-01/finite-bin-covariance-design-recall.md)为已读 BC84 后的 primed recall。BC84-2 原报告 pp.4–5 Eq.(1) 的 bin 积分定义已再次核对；[代码](../../system/scripts/day13_finite_bin_lineshape.py)和[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/finite-bin-lineshape-exercise.json)使用既有合成 entry/feeding 核，不使用原论文事件或模板。

自设 τ70 fs、E0=2396.1 keV、σ2 keV。中点式在0.5/5/10/20-keV bin 下分别拟合70.015/71.145/77.015/80.317 fs；20-keV bin 移半宽后为72.882 fs。各精确积分拟合恢复70 fs，最大误差6.4×10⁻7 fs。此结果只限制本模型的中点近似，未判断实际 ZA23 的 rebin 或寿命偏差。所有内容同步至 [[doppler-correction]]“有限能量 bin：积分、边界与重分 bin”。

对齐细到粗 bin 的概率可加性差<1.2×10⁻16，非均匀 bin 的独立积分差<6.7×10⁻16；无减速 Gaussian、正尾数值稳定、ROI 分母与 bin 细化通过。另600k独立事件生成验证 bin 概率，最大标准化差2.46。三角度每组自设10000光子的局部 Fisher 检查显示粗化信息损失为正半定，τ局部 SE从0.476增至0.559 fs；这些不是实际拟合区间或 coverage。首次导入函数名错误在分析前修复，记录在[验证尝试](20261013-DAY13-doppler-correction-recoil-velocity-run-01/finite-bin-validation-attempts.json)。

有限模板原始方法候选 Barlow–Beeston1993 的 Crossref/INSPIRE 身份已核；FNAL指定报告路径403，nature-downloader以 `--open-access --no-si` 的有界正文检索返回 oa_not_found，OpenAlex无仓储全文，Scholar失败、CDS响应不是JSON。未读全文，不新增其直接claim；保留 acquisition/provenance于tmp。auto授权内选正文，不扩展机构登录或索取凭据。下一步是本任务自行推导与验证共享背景/模板协方差，仍在原DAY13窗口。

### 持续 DAY13：共享 off 计数的协方差

[共享背景代码](../../system/scripts/day13_shared_background_covariance.py)和[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/shared-background-covariance-exercise.json)为任务推导，自设两个独立 on 流、一个共用 off 计数和严格已知背景 shape。BC84-4/5 仅提供 counting-model 方法背景，未把它写成来源的具体 sideband 实现。

完整 covariance 中出现 `(B/r)QQᵀ`。在真值处 profile 背景的联合 Poisson Fisher 与完整 C 的局部 GLS 等价，参数 covariance 差<5.3×10⁻18。自设每组 signal10000/background4000、r0.25时，对角权重估计器报告τ SE0.857fs，其真实传播SE1.460fs；正确局部GLS为1.223fs。120k独立on/off重复验证方差，最大relative差0.338%；约2.22%扣除后bin为负。无非线性数据拟合或实际区间修正。

反证控制明确共同误差对差分可抵消、对和可增强；忽略相关项没有普遍方向。独立背景观测、未知q/r或on事件重叠需不同模型。推导/条件/数表同步至 [[doppler-correction]]“共用背景观测如何连接 bin 与角度组”及 [[doppler-velocity-validation-contract]]，下一步继续有限模板和共用模拟事件的协方差；研究窗口与课程状态不变。

### 持续 DAY13：有限模板和共用模拟事件

[代码](../../system/scripts/day13_finite_template_covariance.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/finite-template-covariance-exercise.json)用合成 proper-time/feeding/response 核做 normalized weighted templates。Leading 1/N ratio-estimator covariance、参数点共用事件的交叉项与差值 covariance 为本任务推导；BC84-2/9仅作方法背景，未归给尚未读到全文的 Barlow–Beeston。

自设70/72fs两点、每份2000模拟事件时，共用随机数的模板差 covariance trace约为独立bank的0.10816，8000组ensemble为0.10866。单模板主bin p0.187031仍有SE0.008675；samehypothesis重放差为零不证明单模板无误差。独立Ndata10000的固定lifetime-score投影，NMC2000时计入模板噪声的SD比只算data为2.48148；此值不是τSE或sourceinterval修正。

800k独立pilot加8000组templates验证四种covariance，Frobeniusrelative差3.4–4.1%；归一化零方向、fixed-selected-N无权重、samehypothesis和无限模板极限通过。Generated/selected、weights、共同eventIDs/seeds和data/MC依赖明确分开。公式、数值、反证与必要packet同步至 [[doppler-correction]]“有限模板与共同模拟事件的协方差”及validation synthesis。

当前bounded analysis还包含已选的adaptive observed bin边界与event-overlap/Poisson-vs-fixedN契约；继续完成这些统计/响应问题。实际20O事件/code/response仍缺，course next14/count13不重计，13:30后不打开新source/card。

### 持续 DAY13：adaptive bin 的完整观测模型

[代码](../../system/scripts/day13_adaptive_bin_observation.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/adaptive-bin-observation-exercise.json)为独立fixed40-photon小直方图的自设合并规则：两bin都≥10时保留，否则合并。忽略边界选择的抽象p估计在true.25时大样本极限.2982966；所有输出bin仍≥10。完整likelihood保留合并事件概率，在期望数据上恢复.25。

64组/8000重复的naive mean.298259、完整观测mean.249663；后者不宣称有限N精确无偏或有intervalcoverage。独立pilot控制mean.249975，对称p=.5时本例naive偏差为零。1061种实际integer summaries的优化/粗网格对照、normalization和controls通过。SourceZA23-10只是rebin≥10报告，实际algorithm未知；本例不拟合τ或断言sourcebias。

公式/分母/数表/反证与rawfinecounts/algorithm需求同步至 [[doppler-correction]]“自适应 bin 边界也是观测的一部分”及validation synthesis。下一当前子问题是shared event的Poisson/fixedN covariance与重放信息边界。

### 持续 DAY13：共享事件与粗投影联合

[代码](../../system/scripts/day13_event_overlap_information.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/event-overlap-information-exercise.json)区分fixedN/Poisson event marks与重叠门。自设10000事件，两门cross covariance约718.335/521.239count²，150k计数MC核验relative差0.478%/0.289%；互斥单光子bin仅Poisson情形可独立thinning。

同批photons用βref .08/.10的deterministic replay，两粗投影各29bins，联合57bins。联合分区可恢复少量summary分辨信息，τ局部SE .825051fs；错当两投影独立给.589322fs。它们没有增加raw事件；重复总count的differencevariance0、sumvariance40000，而independent近似20000。公式、表与raw身份/ROI/映射边界同步 [[doppler-correction]]“共享事件、总计数设计与重放的信息”及validation synthesis。

这轮 finite-bin/background/template 子问题已有解析、独立MC和反证；接下来检验同一合成核的有限计数非线性τ/E likelihood区域覆盖，局部Fisher/leadingΣ尚不能替代该检查。保持DAY13原截止，actualsourceinterval不重标。

### 持续 DAY13：非线性 τ/E likelihood 区域覆盖

[代码](../../system/scripts/day13_nonlinear_interval_closure.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/nonlinear-interval-closure-exercise.json)对同一slowing核的无馈入模型做五场景×2000个计数实验。Fixed selected counts、5-keV bin、response/pointangles严格已知，τ20–250fs domain为自设控制，不是sourceprior。

用χ²2的68.3%阈值，τ70fs内部点在每角度25/1000计数时覆盖.676/.695；τ20fs下界时.7995/.781；无减速、τ不可识别时.861。下界局部halfχ²1+halfχ²2和无减速χ²1的相应概率.7767/.8704，与finitecount/MC误差分开记录，未重标source区间。

Analyticgradient、原核binprobability、128/256quadrature与noloss验证通过。少量optimizer起点失败完整保留，边界1000counts场景11次Powell恢复；所有experiment最终有数值核验，不按失败丢样本。各counts数组的seed/顺序/dtype/shape/hash可再生。公式/数表/limits/读iness同步 [[doppler-correction]]“非线性 τ/E 区域：有限计数、边界与不可识别极限”及validation synthesis。

已选的同一forward/statistics问题继续检验wrongfixedentryβ与independentnoisyvelocityconstraint，13:30后只完成此当前分析，无新source/card，原hardcutoff15:00不改。

### 持续 DAY13：入口速度 nuisance 与区间语义

[速度nuisance代码](../../system/scripts/day13_velocity_nuisance_interval.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/velocity-nuisance-interval-exercise.json)延续同一无馈入核。Trueentryβ.126、错固定.125时，期望fit给τ71.4267fs/E0shift−2.01353keV；这不解释真实20O150/70fs差异。加入独立无偏Gaussianβtag（自设σ.001）并profileentryβ后，2000重复的68.3%jointτ/E覆盖在每角度25/1000counts为.6885/.702，错固定时.129/0of2000。梯度、quadrature和Schurprofile检查通过，优化失败起点未丢实验。

[同数据semantic audit](../../system/scripts/day13_velocity_region_semantics.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/velocity-region-semantics-exercise.json)核对counts/βhash，重复的不是独立证据。低N错固定β的τ一参数profile覆盖.6815、jointpair.129、jointτ投影.872；高N对应.482、0of2000、.693。正确nuisance高N为.6805/.702/.871，三种定义明确分开。0of2000的MC95%双侧exactbinomial上界.001843，不写成真实coverage严格零。公式/表/反证与stage/independence/Σ需求同步 [[doppler-correction]]“速度 nuisance：正确统计量仍须正确的 forward model”。

### 持续 DAY13：长寿命控制线与晚速度校准

既有CM21正式PDFp7/Fig9已回读并视觉核验，publicbytes SHA06255eba…仍与先前versionreceipt相同；source新增CM21-22。0.4%/0.7%是oxygen/carbon aftertarget T/velocity的tuning幅度，不是σβ或independententryresolution，actualmean/mode/peakfitobjective/window/Σ未在该段规定。未打开新来源或课程卡。

[long-control代码](../../system/scripts/day13_long_control_velocity_estimator.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/long-control-velocity-estimator-exercise.json)只借controlenergy/τ尺度；chosenpropercrossing.13ps、β.10→.09、labσ1keV/pointangles/无feeding非实际CM21transport。150°下1375.80/1.27ps的exit-reference整线mean/mode残差约−.60097/−.009845keV；3853.170/12.4ps约−.17757/−.000356keV。不同估计量不能自动互换为sourcepeakcenter，更不以此解释source调参幅度或τ差异。

各700k独立proper/noiseMC验证mean，quadrature/finite-historylateβ恢复/longτ/equal-speed通过。Mode用analyticdensityscore细化并核粗grid，旧bounded初估也保留，避免relativeenergytolerance影响小shift。图中的“latecontrol”仍需明确τ/外部anchorΣ、ROI/背景/response、objective和velocitystage；正确historyinversion也使用了trajectoryprior。内容同步 [[doppler-correction]]“长寿命校准线：有限 history 与估计量选择”及validation synthesis。

### 当前校准分析的适用性审核与 thesis 连接

[适用性代码](../../system/scripts/day13_calibration_applicability_audit.py)、[结果](20261013-DAY13-doppler-correction-recoil-velocity-run-01/calibration-applicability-audit-exercise.json)复用已验证的位移/反冲关系，隔离固定角度、母/子frame条件。Chosenconstantlateβ.09/R150mm/150°下，3853.170keV/12.4ps的错误targetvertex mean/mode残差约−.17836/−.17409keV；原固定角度mean/mode比较因此只说明其自身history模型，不能泛称mode消除全部偏差。正确knownvertex信号反演为零。

另选free-singleγ/A19或A13 massproxy，givenparent-restphotons1375.80/3853.170keV，daughterframe分别高.10695/1.22626keV。Fourmomentum、inverse、geometryquadrature/static/far limits通过；不同fixture不相加、不转作sourcecalibration修正，实际transport/caller未知。内容同步 [[doppler-correction]]“固定角度与母/子frame是这个例题的边界”。

[[a130-thesis-evidence-matrix]]新增fit-validity row，将这些方法边界接到τ/branches/δ→absolute-strength契约；不是新的A≈130实验。[[questions]]只保留一个去重后的actualpacket问题，缺输入由本任务readiness跟踪，不形成用户待办。当前卡学分/唯一Day14partial保持不变，未打开新source/card。

## Durable knowledge delta

原已发布段落的canonical落点为八个 `knowledge/` 页面；持续段落新增source/tracking方法映射于同一block：Doppler诊断/推导、level-scheme方法、三份source、A≈130 evidence contract、开放问题locator及index。`outputs/`的JSON/回忆/评分/候选池只作执行与验收记录，不能取代这些证据页。新科学claims仍为unreviewed/needs_review；未升级为human-reviewed。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Doppler correction 诊断表：峰位、峰宽与停止",
      "summary": "固定症状、伴随检查、反证与locator；分开emitter、angle/velocity、stopping和多线。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-28"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "精确 Jacobian 与协方差练习",
      "summary": "新增自设三角度重算、相关误差、有限差分和MC验证；非实验测值。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "低速峰宽多解：角覆盖本身不足以分离三个 nuisance",
      "summary": "写回rank2反例和独立calibration解除歧义的条件。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "停止历史 toy 的边界与符号检验",
      "summary": "以明确自设的law显示初始β校正后残差；不把1.1ps尺度当实测停止曲线。",
      "sources": [
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-4"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
      "anchor": "DD-20261013-32S-27",
      "summary": "补exact transform和emitter-specific counts事实并修正196Pt句的实际p41/p32 locator。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-28"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-25"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
      "anchor": "KL99-18",
      "summary": "补同跃迁距离相关两分量和TableI/TableII finite-stopping区别。",
      "sources": [
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
      "anchor": "HE15-4",
      "summary": "固化三线属性、复合峰、tentative SD X/link和低能非观测的作者解释。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-6"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "193Bi Band 1 三层实例",
      "summary": "新增图表子图、逐线证据层、energy closure/covariance和同母态branch边界。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "门条件、反证与可以重排纲图的观察",
      "summary": "保留复合峰、弱线缺失、未知X和可证伪的重排条件。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-6"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "Doppler-to-level/strength evidence contract",
      "summary": "连接Doppler/line identity到A130强度与模式证据门，不改变模式排序。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "PDF p.41/印刷 p.32",
      "summary": "修正target-conflict问题定位，保留production数据缺口。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-25"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[level-scheme-reconstruction]]",
      "summary": "登记新方法页和Doppler诊断入口。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
      "anchor": "VD16-3",
      "summary": "公开preprint全文/原表核验，保留真实raw未归档和same-data处理边界；直接vector/vertex改善独立方法证据。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-1"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-2"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
      "anchor": "CR13-3",
      "summary": "公开高能AGATA实验，区分meanβ优化、缺逐事件速度floor和tracking/FEP tradeoff。",
      "sources": [
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-2"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-5"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Recoil vector、共同 vertex 与校正门的响应",
      "summary": "新增vector梯度、two-plane correlated vertex/angle、finite-bin bias和fixed-gate数值推导；非实验结果。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-1"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-2"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Recoil information and high-energy tracking boundary",
      "summary": "补共同vector/vertex信息及high-energy/multiplicity-specific ordering边界。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-5"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[vandebrouck-2016-vamos-dual-position-mwpc]]",
      "summary": "新source/owning method reciprocal入口。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
      "anchor": "AA09-4",
      "summary": "全文simulation主线、target/lifetime/velocity-spread、printed单位和约定边界；全部非实验新测量。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-2"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-3"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-4"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-5"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-7"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "发射位置、forward/inverse 约定与 first-interaction 顺序",
      "summary": "新增mean-flight→tail概率、约定roundtrip和正确incomingdirection下addback反例，代码可重算，非原数据replay。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-4"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-8"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/doppler-forward-inverse-convention-check.md",
      "anchor": "Provisional Reasoning",
      "summary": "保存source1434/1436的bounded counterfactual及code-falsifier；provisional不当source错误结论。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-8"
        },
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "angle/ring 的 corrected peak gate 是否具有已验证的selection efficiency",
      "summary": "新gate-response/trajectory-covariance问题与所需实际输入。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-2"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[aladili-2009-agata-doppler-simulation]]",
      "summary": "新增simulation源与provisional note入口。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-4"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "速度信息的 stage 与独立校准",
      "summary": "新增kinetic/TOF/path协方差、beam/compound/emission stage区分与centroid beta/gain/offset的弱识别性练习，非sourceβ实测。",
      "sources": [
        {
          "path": "knowledge/sources/mavela-2019-32s-quadrupole-moment-doppler-correction-thesis.md",
          "locator": "DD-20261013-32S-27"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-17"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-2"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
      "anchor": "AK12-5",
      "summary": "AGATAoverview主线和原fig/table核验；staticimaging、energy-dependentPSA、threshold/efficiency及same-source依赖，原primary访问边界。",
      "sources": [
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-1"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-2"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-3"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-4"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-5"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-6"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Position validation and selection response",
      "summary": "区分static/beamvalidation的nuisance、P/T与FEPpreservation及algorithm/thresholdresponse。",
      "sources": [
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-1"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-4"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-5"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "分层验证的最小矩阵",
      "summary": "跨source设计energy/staticposition/particle/movingline/selection各层控制，不假装独立实测校准已完成。",
      "sources": [
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-1"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-5"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-6"
        },
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[akkoyun-2012-agata-instrument-response]]",
      "summary": "登记source和owningmethods入口。",
      "sources": [
        {
          "path": "knowledge/sources/akkoyun-2012-agata-instrument-response.md",
          "locator": "AK12-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/lorentz-boost-correction.md",
      "anchor": "Energy-corrected events retain a laboratory angular response",
      "summary": "finite-angleper-photoncounts归一化/Jacobian/energy response练习；保留boostaxis与quantizationaxis条件。",
      "sources": [
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-2"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-3"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Energy gate 恢复后，angular acceptance 仍在实验室 frame",
      "summary": "energy-restgate与lab angular/energy response不可合并，实验条件和模型界限分开。",
      "sources": [
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-2"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-3"
        },
        {
          "path": "knowledge/sources/longfellow-2026-gretina-energy-ordering-polarization.md",
          "locator": "L26-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Delayed emission vertex 与 feeding 的条件响应",
      "summary": "新constant-speed/几何加权emissionvertex模型、feeding/time-gateCDF、one-sidedtail与falsifier；未当实验τ或B。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-1"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-4"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-4"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
      "anchor": "SY14-6",
      "summary": "15页preprint主线/原fig/tables核验：detector-origin宽化、TOF非targetidentity、nestedcount分母、正文/结论predicate与列label边界；exec-code未核。",
      "sources": [
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-2"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-3"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-4"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-5"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-7"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-8"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Detector-origin 宽线、natural width 与 cut 语义",
      "summary": "naturalΓ/motion/recoildeposit分层、TOFscale、DeMorgan/monotonicity与nestedratios练习，不改sourcecut。",
      "sources": [
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-2"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-3"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-4"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-5"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Neutron background and executed cut semantics",
      "summary": "actualexecutionstage、TOF/sourceidentity与count-response定义。",
      "sources": [
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-4"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-5"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/gamma-gamma-coincidence.md",
      "anchor": "Gate predicates and spectral-origin control",
      "summary": "门逻辑必须说明accept/reject与referenceobject，backgroundline不自动归target。",
      "sources": [
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-4"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-5"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[senyigit-2014-agata-neutron-rejection]]",
      "summary": "登记2013preprint/2014journal的source及method入口。",
      "sources": [
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-2"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/tunl-2017-12c-level-widths.md",
      "anchor": "T12C-1",
      "summary": "核验在线评价选定宽度/分支及2020 companion版本；read仅声明数据记录范围，raw保留位置未填充。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-2"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-3"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-4"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-5"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-6"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Photon recoil：level gap、母核 frame 与子核 frame",
      "summary": "固定total/partial Γ分母与自由核two-body公式；母/子frame不同，四动量练习不冒充实际event重建。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-2"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-3"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-4"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "Level gap and gamma-energy precision",
      "summary": "精确level gap与母系rest γ能量比较需要recoil/frame输入；保留mass-number近似与圆整边界。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
      "anchor": "T12C-1",
      "summary": "用有版本的评价数据约束天然宽度尺度和分支分母，不裁决该实验真实calibration。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-2"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/doppler-forward-inverse-convention-check.md",
      "anchor": "photonrecoil是另一个frame候选",
      "summary": "A52 photonrecoil/frame差远小于约2-keV counterfactual；不把另一frame或圆整line label当代码错误证据。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Lorentz natural line 与 Gaussian response 的卷积",
      "summary": "归一Voigt与finite-gate练习；限定Gaussian variance和Lorentz Γ的不同运算，保留synthetic与source-width尺度边界。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-4"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-6"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Missing momentum 与发射前后的速度阶段",
      "summary": "区分neutron-before-gamma的recoil spread和conditional late-particle未知stage；明确真正measured emitter vector可消除此前蒸发nuisance。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-2"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-9"
        },
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
      "anchor": "AA09-9",
      "summary": "回读particle/γ阶段示意及CM/lab neutron histogram；保留source artificial γ不能证明真实cascade时序的边界。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/soderstrom-2008-agata-position-design.md",
      "anchor": "SD08-5",
      "summary": "全文会议稿与原Eq4.4视觉核验，保留preliminary/model及geometry transfer边界；不把未平方打印式静默替换。",
      "sources": [
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-1"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-2"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-3"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-4"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-5"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-6"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
      "anchor": "C23-4",
      "summary": "全文review原方法/响应/limitations；OFT σθ为cm调参量，exact Jacobian与independence approximation、historical benchmark不新增acquisition。",
      "sources": [
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-1"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-3"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-4"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-5"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-6"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-7"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-8"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-9"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-10"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-11"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-12"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-13"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-14"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "两距离 position 标定：消去哪一项，留下哪些假设",
      "summary": "声明Gaussian/common-baseline模型后用平方差；first-IP距离、shared covariance、held-out geometry及负p²边界数值核验。",
      "sources": [
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-3"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-5"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-6"
        },
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "cosθ=β",
      "summary": "用direct review Eq7核验速度Jacobian零点及忽略correlation的适用条件；不是整体最优角。",
      "sources": [
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Tracking 参数的符号、单位与独立验证",
      "summary": "区分OFT cm parameter、Doppler rad和PSA/FWHM；保留physical order ambiguity与held-out transfer需要。",
      "sources": [
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-1"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-4"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-5"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-6"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-11"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-12"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-14"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "soderstrom-2008-agata-position-design",
      "summary": "添加两份方法source导航，原paper inaccessible与review依赖边界保留。",
      "sources": [
        {
          "path": "knowledge/sources/soderstrom-2008-agata-position-design.md",
          "locator": "SD08-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "门选择后的 likelihood 与未参与优化的验证",
      "summary": "固定selection的conditional normalizer与known-trials likelihood例题；shape/rate区别、test split共享systematic及真正held-out transfer条件。",
      "sources": [
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-4"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-5"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-12"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-5"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-8"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
      "anchor": "LG20-7",
      "summary": "GANIL primary全文、Dopplerposition/response/normalizer原图及copy-date/打印值差；保留event/code/rawpacket缺口。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-1"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-2"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-3"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-4"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-5"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-6"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-7"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-8"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-9"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-10"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-11"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-12"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-13"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-14"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "GANIL 的直接 Doppler-position 对照",
      "summary": "independent VAMOS vector、energy-dependent 1D IP FWHM与Gaussian interpolation的source适用条件，不能移植平均5.1mm。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-7"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-8"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-9"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "联合接受率、event mixing 与同束轴各向异性",
      "summary": "mix before/aftertracking区别与声明toy；independent common-axis draws的pair a2=A2²/5已quadrature/MC核验。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-1"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-7"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-8"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-10"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-11"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-12"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/gamma-gamma-coincidence.md",
      "anchor": "Joint pair acceptance 与 event mixing stage",
      "summary": "coincidence normalization需joint pair-response和mix stage；source/in-beam与zeroacceptance/covariance边界。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-10"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-11"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
      "anchor": "Direct GANIL follow-up",
      "summary": "续读Ref25 primary，source/review仍同实验谱系，原2011 Ref24仍未得全文。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-3"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-4"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-10"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-12"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "ljungvall-2020-agata-ganil-performance",
      "summary": "补primary GANIL source导航和copy版本边界。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "已知 speed 不等于唯一的 velocity vector",
      "summary": "两projection/knownspeed的global mirror counterexample，localrank2不足以排全局多解；noncoplanar constraint与source几何/阶段边界。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-1"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-8"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Cartesian 输入的完整 Jacobian：避免重复计入角误差",
      "summary": "从E/b/vertex/first-IP raw inputs推导full Jacobian/Σ；radial零项、β0/共同frame invariance与physical target movement区别。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-1"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-8"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Energy-dependent IP response：平均 variance 与混合谱",
      "summary": "用声明的IP energy-response模板核验平均variance/mixture FWHM/gate；known σ权重centroid的条件与实际tracking未证明边界。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-8"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-14"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Detector frame 的 tracking 与 Doppler 处理顺序",
      "summary": "自由electron Compton/boost例题验证lab tracking与rest incoming photon correction的frame次序；总能量correct不等于prescaled FOM合适，不指控actualsource。",
      "sources": [
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-1"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-1"
        },
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "到达时间的 retardation 与 Doppler factor",
      "summary": "proper/lab emission/arrival对象不同，geometry时间导数与energyinverse同factor；conditionalgate与自设计时response的极限/MC/boost核验。",
      "sources": [
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-4"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "一阶速度敏感度为零时的二阶边界",
      "summary": "zero first derivative仍有quadratic传播，区分inverse estimator error与actual emitter spread两种fixture；非Gaussian/no actualtail claim。",
      "sources": [
        {
          "path": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
          "locator": "C23-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Narrow level width 到 photon width 的反冲映射",
      "summary": "free two-body mass slopes与narrow independent Lorentz width映射；q→1近似、unit/precision/covariance边界，不改evaluatedΓ。",
      "sources": [
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
      "anchor": "AS21-8",
      "summary": "primary13页与原Fig17/18/式核验：lightparticle recoil、conditionalPID/TOF、target/normalization/material与printedboundaries。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-1"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-2"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-3"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-4"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-5"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-6"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-7"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-9"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-10"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-11"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-12"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-13"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-14"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-15"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-16"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Light-ejectile 两体反冲与 conditional rigidity velocity",
      "summary": "actual10.2→7.1keV方法证据及four-momentum输入；rigiditycontinuous covariance与integerPID模式的有界练习。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-4"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-9"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-10"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-12"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-14"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-16"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Particle ancillary 的 γ response 与 relative normalization",
      "summary": "differentgeometry/crystal sourceefficiency与normalizedtransparency不等absolutescale；particle/trigger/material伴随response需匹配。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-1"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-2"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-6"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-7"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/gamma-gamma-coincidence.md",
      "anchor": "AS21-2/11/12",
      "summary": "particle/gamma/heavytag是同event互补，entrypoint/feeding和absolutebeam normalization边界不同。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-2"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-11"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "assie-2021-mugast-agata-vamos",
      "summary": "新增direct light-ejectile/rigidity source导航，保留two-body与PID/target/readiness条件。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Exact two-body 与反应 entrypoint 的可证伪例题",
      "summary": "synthetic mass-consistent二体/feedingγ重建；knownbeam排wrongentrymass，非单调inverse的两root与首轮failure/修复保留，不宣称actualsourcefit。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-3"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "DVV-P1-1",
      "summary": "新增简明evidence/validation契约，区分source报告/解释/model/任务inference，保留falsifiers、共享数据与self-audit/readiness。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-10"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "doppler-velocity-validation-contract",
      "summary": "增加cross-source calibration/velocity contract导航，详细数学仍归owningmethods。",
      "sources": [
        {
          "path": "knowledge/sources/vandebrouck-2016-vamos-dual-position-mwpc.md",
          "locator": "VD16-3"
        },
        {
          "path": "knowledge/sources/crespi-2013-agata-high-energy-doppler-response.md",
          "locator": "CR13-3"
        },
        {
          "path": "knowledge/sources/ljungvall-2020-agata-ganil-performance.md",
          "locator": "LG20-10"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-8"
        },
        {
          "path": "knowledge/sources/klemme-1999-lifetimes-134nd-neighbors.md",
          "locator": "KL99-18"
        },
        {
          "path": "knowledge/sources/senyigit-2014-agata-neutron-rejection.md",
          "locator": "SY14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
      "anchor": "LS23-8",
      "summary": "12页fissionreview/Table1/角覆盖/delayed/degrader原图核验；sourcelevel/model/printed/lineage边界。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-1"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-2"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-3"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-4"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-5"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-6"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-7"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-8"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-9"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-10"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-11"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-12"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-13"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-14"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
      "anchor": "CO19-9",
      "summary": "10页官方progressreport：RF/energy/PID与stage，jointτ/Eγ拟合未完成、模型数值非measuredτ，branchlabel冲突保留。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-1"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-2"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-3"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-4"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-5"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-6"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-7"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-8"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-9"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-10"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-11"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-12"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-13"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Post-degrader reference 保留的 velocity-history 信息",
      "summary": "proper-clock/finitefoil/feeding与postreference例题，sourceU moving≠β0；保留energy-onlyhistory与真实loss/Σ边界。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-8"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Focal-plane delayed 样本的 survival 与速度选择",
      "summary": "survival/stopwindow/halfmean转换与velocityselectionMC；isomeralive不是ion detectionefficiency，actualgates/branch/ε未给。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-3"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-11"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "20O progress report 的 RF 与 lifetime–energy contract",
      "summary": "sharedcalibration、unknownEγ/τ联合设计及no-finalfit；sourceemission/exit字段须verification，不宣称sourcecode错。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-1"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-3"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-6"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-9"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-10"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-12"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "AGATA/EXOGAM 比较的 angular controls",
      "summary": "15all/7back vs5的条件与normalizedcountsscale；source/modeldata stage不同。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-5"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-6"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-7"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-11"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/gamma-gamma-coincidence.md",
      "anchor": "LS23-11/12",
      "summary": "PD在不同emitterstage，survival/window/ε与same-event依赖决定negativeevidence。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-11"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/crespi-2023-agata-tracking-performance.md",
      "anchor": "Fission benchmark angular-control follow-up",
      "summary": "详细reference限制原1229.9/15vs5简述，保留originaltext/version，不加independentacquisition。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-5"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-6"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "History-specific update",
      "summary": "补angularcontrol、postreference/FP、sharedRF和preliminaryfit边界，未改actualstructure/strength/readiness。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-8"
        },
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-11"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-3"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "ciemala-2019-20o-dsam-analysis-status",
      "summary": "两新source导航：publicstudyversion/history与未归档raw边界。",
      "sources": [
        {
          "path": "knowledge/sources/lemasson-2023-agata-vamos-fission-history.md",
          "locator": "LS23-8"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Unknown Eγ 与 lifetime：centroid 和 full shape 的信息不同",
      "summary": "声明synthetic τ/Eγ模型的mean vs fullprofile/KL设计；shape核验/MC/limits，不测sourceτ、不把expectedmetrics当CL/forces证据。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-1"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-9"
        },
        {
          "path": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
          "locator": "CO19-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
      "anchor": "Reference-route identity follow-up",
      "summary": "Ref11 bibliographicroute确认为17C，metadataonly不用于20Ohistory；source接续选择已更正。",
      "sources": [
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
      "anchor": "ZL19-8",
      "summary": "7页directtime/energy/historycontrols、TableI/Fig4核验；sameJuly2017data、percentagewidth/origin/νlifetime层级。",
      "sources": [
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-1"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-2"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-3"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-4"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-5"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-6"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-7"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-8"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-9"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Direct calibration controls 与 history 控制的边界",
      "summary": "静止energyanchors、18Oshort/longcontrol与sharedreferencecovariance；不强制physicalshortshift归零、不用tablewidth当centroidσ。",
      "sources": [
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-2"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-4"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-6"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-7"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-8"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/tracking-array.md",
      "anchor": "Time replay、core recovery 与响应类型",
      "summary": "GGPtimestamps、badcoresegments及response层分开，sourcecountloss不是absoluteε，same data非indrep。",
      "sources": [
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-1"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-2"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-4"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-5"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-6"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
      "anchor": "2026-10-14directRef8续读",
      "summary": "actualRef8提供1938.2short/1981.93long与标定流程，不补finalτ或βstagecode。",
      "sources": [
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-1"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-2"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-4"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-8"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "新增 [[ziliani-2019-agata-calibration-controls]]",
      "summary": "实际校准controls补contract，commonreference/time与energyorigin继续分层。",
      "sources": [
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-2"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-4"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-6"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-7"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-8"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "ziliani-2019-agata-calibration-controls",
      "summary": "directcalibrationsource导航与same-dataset初步分析边界。",
      "sources": [
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-1"
        },
        {
          "path": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
          "locator": "ZL19-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
      "anchor": "Summary",
      "summary": "公开2020primary的total/partialτ、jointenergy与16C条件结果；初/发射/末速度和同2017lineage保留。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-1"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-2"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-3"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-5"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-7"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-8"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-9"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zanon-2023-o20-high-precision.md",
      "anchor": "Summary",
      "summary": "独立2023实验main/SI、particle入口/Exfeeding、jointCL与unknown3+δ的strength边界。",
      "sources": [
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-1"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-4"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-6"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-8"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-11"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-12"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "20O 两次独立寿命测量的速度与馈入对照",
      "summary": "150fs与70fs的具体竞争解释/必要观测/反证，不pool或归因；total/partial与二维CL分开。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-2"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-3"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-5"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-7"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Feeding branch 与目标样本 fraction",
      "summary": "任务两入口公式/meanbound：branch.28不等f，70+54f非真实fittedτ，不排除旧实验全部feeding。",
      "sources": [
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-4"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "寿命到strength的条件链",
      "summary": "τ/branch/δ与sharedcovariance、3+USDBδ模型输入需随B比较保留。",
      "sources": [
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-6"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-11"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "20O 独立实验对照的验证路线",
      "summary": "stage/gate/response/jointprofile的可反驳验证设计和L4缺口，能量差解释仍taskhypothesis。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-3"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "ciemala-2020-c16-o20-lifetimes",
      "summary": "两primary入口导航及独立性/模型依赖边界。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-8"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2019-20o-dsam-analysis-status.md",
      "anchor": "后续独立version",
      "summary": "2019report与同实验2020final结果分时，独立2023transfer另列，不改2019publishedhistory。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-1"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-3"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ziliani-2019-agata-calibration-controls.md",
      "anchor": "同data的后续结果",
      "summary": "2019calibrations与2020finalτ相同lineage，无新增独立实验。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-1"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-5"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-6"
        },
        {
          "path": "knowledge/sources/ciemala-2020-c16-o20-lifetimes.md",
          "locator": "CI20-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
      "anchor": "Summary",
      "summary": "两version各17页的method/labels/stages/CL/cumulative与dataownership；publisher消除v1标签冲突，不判执行错。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-4"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-5"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-6"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-7"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-8"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-9"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-10"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-11"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-12"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-13"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-16"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-19"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-20"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "TKEL 展开、速度tuning与90°的适用条件",
      "summary": "TKEL/depth/TOF/longlinetuning与acceptedangle，不把sameanchor当独立velocity检查。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-1"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-2"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-3"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-5"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-6"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-7"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-9"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-11"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "印刷公式与生产执行边界",
      "summary": "v1/正式版明确version：正式inverse/aftertarget定义一致，源代码仍缺，80%total/cumulative不转成统一1σ。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-4"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-8"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-9"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "90°只是低速一阶的shift控制",
      "summary": "exactγexit/γem/transverse与finiteangle边界；自设scalar/fourvector counterfactual数值已核。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-12"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/doppler-forward-inverse-convention-check.md",
      "anchor": "新的文档case",
      "summary": "保留v1label而用publisher定义反证正式文档错误候选；不改变AA09未知执行假设。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-4"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Ex门泄漏与错设单寿命拟合：受限设计练习",
      "summary": "自设gate/kernel/feedingdensity/pointangle条件化、wrongmodelτ/E与KL结果；MC/quad/limits通过，非experimentfit。",
      "sources": [
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-4"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "方法version、cumulative lifetime 与不重复的校验",
      "summary": "source定义缺口缩小；逐versionCL、cumulative/feeding negativeevidence与article/dataaccess边界。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-16"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-19"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-20"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zanon-2023-o20-high-precision.md",
      "anchor": "DataCite正式注册已通过",
      "summary": "DOI/公共metadata已核，landingHTTPS/HTTPnetwork失败；registrydesignfields与mainactualparams分开。",
      "sources": [
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-14"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "ciemala-2021-deep-inelastic-lifetime-method",
      "summary": "methodprimary/version与sensitivity/source权限导航。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-20"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "RF周期编号与连续速度精度的不同信息",
      "summary": "selfchosenphase-only/A-q alias两解闭合、local precision不能裁离散k，independentenergy/absoluteclock反证，非真实VAMOS误判。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-1"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-9"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
      "anchor": "Summary",
      "summary": "KEK/UCLA原报告22页、公式/scale/point/interval/GOF/finiteNconditions核验，非publisher六页或新实验。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-3"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-6"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-7"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-8"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "均匀Poissonrate的可解析反例",
      "summary": "自设32bins/200kMC，allobserved≥10仍Neymanharmonicrate偏差，不移植为真实τ偏差或ML万能。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-3"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-10"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "二参数区域、投影和profile的不同覆盖",
      "summary": "自设相关Gaussian/1MMC、χ²2CDF和projectedτCDF，σ/CI的定义不可与原source互换。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-7"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Overall normalization与计数信息",
      "summary": "bin积分、Poisson总rate vsconditionalmultinomial/freeoverallscalearea条件与背景prior boundary。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-6"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "统计定义不能由峰图补齐",
      "summary": "point/interval/GOF/sourceconfidence与rawbin/background/templateΣ/closurepacket，counttoys非L4refit。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-3"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-6"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-7"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-17"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "baker-cousins-1984-histogram-fits",
      "summary": "直接statisticalmethodsource与source/finiteN版本边界导航。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-3"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-6"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "同一发射等待分布不唯一对应目标态寿命",
      "summary": "自设120/60fs direct/feeding fractions的full-density/Laplace恒等式；同K下gamma shape非唯一tau，独立entry/feeder反证及recoil/selection限制。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Entry history 的可解析竞争者",
      "summary": "数学counterexample把cumulative/target tau与必要伴随信息具体化，不移植source54fs/branch.28或推断150/70因果。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-3"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "Cascade recoil 对共同响应假设的限定",
      "summary": "exacttwo-body/boost/角条件权重与自设cascade recoilwidth；profileGaussianresponse吸收多数学理差异，未作真实foilτfit。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "共同K的物理边界也要量化",
      "summary": "physicalbreaking与actualidentifiability不同，commonK含alignment/anglecorrelation/response，需要independenttag/entry/Σ。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-14"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-18"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-5"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-1"
        },
        {
          "path": "knowledge/sources/tunl-2017-12c-level-widths.md",
          "locator": "T12C-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "等有效停止率下，末速度缺少反应深度信息",
      "summary": "自设equal-S/共线/三prior的exitblindness、properclock、错priorτ/E与MC/quadclosure；实际倾斜/contrast/entry可排除极限。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-6"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-7"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-19"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-21"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
      "anchor": "CM21-21",
      "summary": "正式版targettilt45和VAMOSθ/φ接受字段，限定toy不可反写actualgeometry。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-21"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Depth prior 与末速度各自约束什么",
      "summary": "measuredexit vsphysicalprior/独立entry，sameexitfit不新增独立input；actualsourcegeometry/Σ仍必要。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-6"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-7"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-19"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-21"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
      "anchor": "Summary",
      "summary": "固定历史源码对象/hash/单位/frame/gettercontract；Github迁站与network边界，不attest论文执行。",
      "sources": [
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-1"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-2"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-3"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-4"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-5"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-6"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-7"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-8"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-9"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-10"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-11"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "固定代码对象的velocity字段：输入、状态和单位",
      "summary": "beam/light/data/prior到P4的依赖、container/cache/mass、derivedTOF/velocity、caller frame与stage归属。",
      "sources": [
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-1"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-2"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-3"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-4"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-5"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-6"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-7"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-8"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-9"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-10"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-11"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-12"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/assie-2021-mugast-agata-vamos.md",
          "locator": "AS21-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "质量状态与invariantβ的quant sanity",
      "summary": "自设on-shellP/mass不匹配3.695keV、MeV/per-A/pathunits和invariantthreshold；不是第三方执行或sourcebias。",
      "sources": [
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-2"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-6"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-7"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-8"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Code object、caller与测量binding",
      "summary": "固定对象audit与actualcaller/dataset不同；sameinput派生字段非independent测量，L4仍需binding/Σ。",
      "sources": [
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-2"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-3"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-4"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-5"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-6"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-7"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-8"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-10"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-12"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "nptool-2019-reaction-velocity-code-object",
      "summary": "历史codeobject导航、byte/stage与current/experimentversion边界。",
      "sources": [
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-1"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-2"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-7"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "有限能量 bin：积分、边界与重分 bin",
      "summary": "合成Gaussian混合的精确bin积分、中点近似和边界/ROI敏感性；所有数值为任务模型，未重拟合source。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "正确积分也不能恢复粗 bin 丢失的信息",
      "summary": "对齐rebin可加性、条件Fisher信息损失、独立事件MC和Gaussian极限；局部误差不是sourcecoverage。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "保存bin边界/rebin/ROI/条件分母及原on-off/template数据契约；同事件重分bin非独立证据。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "共用背景观测如何连接 bin 与角度组",
      "summary": "任务推导共享on-off背景covariance，保存负bin、独立性和unknownshape/exposure边界，非source实现。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "联合 on/off 信息与局部误差传播",
      "summary": "局部jointPoisson/GLS等价和naive估计器sandwich variance；120k计数MC和无限off极限通过，非intervalcoverage。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "忽略相关项不保证同一方向的偏差",
      "summary": "共同误差在difference/sum中抵消或增强的解析反例；不将忽略Σ的影响方向普遍化。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "追加共享off/事件overlap/transfer/q与实际计数packet要求，保持experimentalL4notready。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "有限模板与共同模拟事件的协方差",
      "summary": "任务推导normalizedweightedtemplate的leading1/N协方差与generated/selected分母；归一化零方向不是独立bin。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "参数扫描点共用随机数时的交叉项",
      "summary": "共用模拟事件使模板点相关，可降低差值噪声但不使单模板误差消失或增加独立样本数。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "模板误差进入数据比较的条件",
      "summary": "独立data/MC的scoreprojection噪声与templateN敏感性，8000组ensemble和limits通过；非τinterval修正。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "追加finiteMC权重/入选数/共同eventID和dataMCbinding；保留actualL4notready。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "自适应 bin 边界也是观测的一部分",
      "summary": "数据选择边界携带参数信息；fixed40-photon合并反例、完整likelihood、独立pilot/对称controls，非sourcealgorithm或τbias。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "追加finecounts/rebin选择算法与complete-observation要求；每bin≥10不能替代统计验证。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "共享事件、总计数设计与重放的信息",
      "summary": "Poisson/fixedN event-mark covariance及overlap/disjoint控制，150kMC验证，非sourcegateimplementation。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "同一事件的不同粗投影可细化观测",
      "summary": "同一raw事件的two-referencehist相关，联合分区可恢复coarse信息但不能当独立data；jointprob/Fisher/总countvariance通过。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "补充eventmarks、Poisson/fixedN/thinning与replayraw身份和summary信息边界。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/gamma-gamma-coincidence.md",
      "anchor": "门重叠与投影计数的 covariance",
      "summary": "链接canonicalDoppler eventmark推导；Poisson/fixedN、multiplicity/overlap/权重和replay分区关系，非sourceproduction评价。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "非线性 τ/E 区域：有限计数、边界与不可识别极限",
      "summary": "同一核的fixedN nonlinear regionclosure，internal/boundary/noloss与optimizer失败/恢复、counts身份；非sourceinterval校准。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "补充参数domain/identifiability/joint-profile/fullalgorithmcoverage，与局部Σ和actualsourceerrors分层。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "速度 nuisance：正确统计量仍须正确的 forward model",
      "summary": "独立beta nuisance与错fixedentry模型对照，jointτEcoverage有限N closure及SE/原source界限。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "联合真值、τ profile 与联合区域投影",
      "summary": "对同一hasheddata区分pair/profile/projection和0/R的MC区间；复算非独立证据。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-1"
        },
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
      "anchor": "CM21-22",
      "summary": "正式Fig9核0.4%/0.7%aftertargetvelocitytuning幅度、σ/stage/estimator边界，非新数据独立验证。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "长寿命校准线：有限 history 与估计量选择",
      "summary": "source-inspiredmean/mode与有限history的条件calibration，700kMC/score-root/limits，不归作source算法或bias。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-16"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "加入velocitynuisance/独立tag/semanticregion与latecontrol objective/window/stage契约。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-correction.md",
      "anchor": "固定角度与母/子frame是这个例题的边界",
      "summary": "当前longcontrol条件自审：不同fixture隔离vertex/frame边界，非sourcebias或新独立证据。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-7"
        },
        {
          "path": "knowledge/sources/aladili-2009-agata-doppler-simulation.md",
          "locator": "AA09-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "Histogram 输入与独立性",
      "summary": "增补calibratorvertex/refparticle/state/epoch与observablebinding，晚reference用于historyfit须模型一致。",
      "sources": [
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-15"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        },
        {
          "path": "knowledge/sources/nptool-2019-reaction-velocity-code-object.md",
          "locator": "NP19-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "Doppler-fit validity before lifetime/strength interpretation",
      "summary": "将bin/likelihood/Σ/velocity/parentframe/source-lineage契约连接A130 τ与strength，不给实验结构新结论。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "实际 Doppler τ/E 分析能否提供完整",
      "summary": "去重跟踪actualpacket的原counts/stage/校准/Σ/coverage缺口，不用模型解释20O差异。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-2"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/doppler-velocity-validation-contract.md",
      "anchor": "统计与速度分析之后的判定表",
      "summary": "汇总observable/producer/physicalhistory/统计观测/coverage的充分性边界与actualpacket；toys不裁决20O原因或A130mode。",
      "sources": [
        {
          "path": "knowledge/sources/baker-cousins-1984-histogram-fits.md",
          "locator": "BC84-5"
        },
        {
          "path": "knowledge/sources/ciemala-2021-deep-inelastic-lifetime-method.md",
          "locator": "CM21-22"
        },
        {
          "path": "knowledge/sources/zanon-2023-o20-high-precision.md",
          "locator": "ZA23-7"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- Mavela实际执行β表/坐标与打印列表是否相同？新的bundle库存仍不含执行与逐环数据；继续保留开放问题，未更改PDF或猜测正确数值。
- independent calibration能约束width分解中的哪项？rank2限制的是已写明的低速/小独立误差模型，真实角度相关response与non-Gaussian tails要另建响应。
- level identity何时需要拆峰或重排？对子图的closure、coincidence、spin/parity或同母态branch条件出现可靠冲突时重审；先排除随机/feeding/response问题。
- 本次 belief revision和最小数据设计均已写回方法页；没有把输入缺口转成人工审核清单。

## L0–L4 state

| 等级 | 状态 / readiness |
|---|---|
| L0 | 已读source的身份、locator/原图核验完成；新public source的raw槽位未归档，URL/version/tmp-byte hashes明示；保留文本与执行版边界。 |
| L1 | source↔method、thesis contract、index反链完成；不同实验/不同emitter的适用条件保留。 |
| L2 | 来源方法与自设 exercise 分层完成；新增 finite-bin/ROI、共享背景、weighted templates、adaptive edges和event-overlap的公式/seed/单位/误差/反证可复算，未冒充测量。 |
| L3 | 诊断矩阵与20O独立实验/方法version比较已写回；正式CM21反证v1label外推，feeding/τ–E差异原因未裁决，真实Mavela执行影响仍partial。 |
| L4 | 合成分析有明确输入/代码/hash/seed、竞争模型与失败检查，其结论限于声明的模型；experimental refit `not-ready`：缺事件、production code、ring spectra、response/covariance和feeding，未生成新实验τ或absolute strengths。 |

## Verification and continuation

最终收束检查：155items/32mappedpaths的唯一writeback、完整Day13audit/Day14partial、十项新分析和原source/model边界已核；lint23为0errors/128warnings（107citationkey、18reservedraw、3reactionparser）。AST/代码与data/dependencyhash、PLAN/Bib、无raw/PLANdiff、state next14/count13、sourceCM21publishedhash、singleblock和diffchecks通过。显式46-filemanifest排除继承Day6–9/daemon/旧log及tmp。H3、commitfilemanifest和handoff reconciliation的实际结果只写run.json/reopened-publication-h3-012.json，失败时保留本地commit，不更改凭据或Git配置。



边界self-audit：本次恢复时矩阵 `sed116–140` 意外带出Day15标题/一行回忆任务文本，已记录于run.scope_self_audit。没有选择、开展或计入Day15学习，也没有新开其来源；后续只处理Day13既有分析/收束。此记录不把意外文本显示写成Day15知识交付。



最新活动检查（2026-10-14T11:43:08.379833+08:00，余196.9分钟）：126items/32mappedpaths（31owningpages）。Depth/exit/clock/MC/quad与pinned2019NPTool object source/units/mass/state/context sanity均通过；Gitblob/SHA、successornetworkfailure/未build/rawbound已记录。CM21 fragmentedtable修复后21claims均machineparsed。Lint0errors/128warnings（107citationkeys、18rawslots、3parser）、boundary/report/card/writeback/protected/state/diff通过。原window仍active至15:00，不推进课程；下一有限bin/背景/templateΣ，不开formal14/15。

最新活动检查（2026-10-14T09:39:59.057803+08:00，余320.0分钟）：118items/31mappedpaths，exactfeeding全density/Laplace/600kMC及cascade recoil的mass-shell/两boost/角moments/600kMC/limits通过。Tag分母明确pre-angular/unit4π；commonK须含alignment/角关联，recoil模型constantflight不作foilτ重拟合。Lint0errors/126warnings，boundary/report/card/writeback/protected/state/diff通过。原run/goal仍active至15:00，下一TKEL/depth/responseclosure仍pending，不开formal14/15。

最新活动检查（2026-10-14T08:56:32.257106+08:00，余363.5分钟）：writeback114items/31mappedpaths（30owningpages）。RFphase/A-q构造与count/Gaussianregion练习独立MC/score/limits/closure通过；BC原报告22页identity/hash/关键式已核。Lint0errors/126warnings（106citationkeys、17rawslots、3parser），boundary/report/card/writeback/protected/diff通过。上一段Gitee初推送128断线，freshH3 retry成功并核远端，真实failure保留；本段仍active，不计新卡，下一TKEL/depth/responseclosure。

最新活动检查（2026-10-14T08:17:58.740041+08:00，余402.0分钟）：累计writeback107items/30mappedpaths（29owningpages），三新source、publisher/currentarXiv与SI均核identity/hash、raw仍未填充。Entrygate/feedshape的MC/quad/limits/四optimizerstarts及exact90/fourvector checks通过；lint0errors/124warnings（105citationkeys、16rawslots、3parser）。Boundary/report/card/writeback/PLAN-Bib保护/diff通过。DataCite已核、landing网络失败，没有eventaccess声明。研究仍active，不重复课程推进；下一route统计量/RF-TOF/TKELclosure。

最新活动检查（2026-10-14T07:40:42.094171+08:00，剩约439.3分钟）：writeback89items/27mappedpages；ZL19校准与18O短/长寿命control已写回。lint0errors/118warnings（102citationkeys、13未填充rawslots、3reaction-parser）；report/card/writeback/protected/publiccopy/boundary通过。原研究窗口仍active；下一route为Ciemała2020与Zanon2023的独立20O寿命测量、supplement和velocity/feeding/τ–Eγ audit，不新增课程学分。

最新活动检查（2026-10-14T05:57:51.878940+08:00，剩约542.1分钟）：writeback83items/26mappedpages。LS23/CO19两新fullsources、不同angularcontrols/postdegrader/FP/RF/jointτ-Eγ的source层级核验完成；three newstage/survival/design exercises通过。Wiki lint0errors/116warnings（101citation-key、12rawslots未填充、3reaction-parser）；report/card/writeback/protected/boundary/diff通过。Ref11身份误候选已排除，未把17Cmetadata当20O证据。原窗口仍active，下一route S.Ziliani2019 APB50p625的directcalibration，以及sourceχ²/velocity-stage数据契约。

最新活动检查（2026-10-14T03:53:11.627863+08:00，剩约666.8分钟）：writeback71items/24mappedpages。10份publicsource和validation-contract综合已具locator/self-audit与source/models/任务推断边界；retarded-time、zero-sensitivity、rigidity/PID、two-body/entrypoint及narrowwidth extension均通过。Two-body首轮single-root失败保留，两root恢复后原命令回归通过。lint0errors/112warnings（99citation-key、10未填充rawslots、3reaction-parser）；新综合inboundlink已补齐。boundary/report/card/protected/diff通过，原run仍active。下一route primary20O backing/emissionhistory与AGATA/VAMOS prompt/delayed/degrader谱系，course不再推进。

最新活动检查（2026-10-14T02:26:50.727152+08:00，剩余约753.2分钟）：writeback60items/22mappedpages；vector-global、CartesianΣ、heterogeneous response与tracking-frame四个新增练习通过解析/finite-difference/MC/守恒/极限核验。boundary、diff、report/card/protected通过，lint0errors/110warnings；已实读milestone仍next14/count13，不重复计卡。下一route为retarded arrival time/energy与速度关系，研究仍active。

最新活动检查（2026-10-14T01:54:40.245714+08:00，距截止约785.3分钟）：累计writeback56items/22mappedpages。三份新增方法/primary source与two-distance、fixed-gate likelihood、event-mixing练习均已写回，参数/零核/积分/MC检查通过。lint exit0，0errors/110warnings（98citation-key、9未填充raw archives、3reaction-parser）；report/card/writeback/protected/diff通过，原窗口仍active。当前发布是checkpoint，不触发new credit或closeout。

持续检查（2026-10-14T01:00:40.490662+08:00，距截止约839.3分钟）：研究仍active。当前累计唯一writeback43items/19mapped pages；基于reopen snapshot的path/anchor/atomic locator、report/card coverage与PLAN/Bib hashes检查通过。Wiki lint exit0，0errors/104warnings（95citation-key、6reserved raw archive缺失、3reaction-parser）；不把missing archive写成已归档。四项本段新练习的conservation/limits/normalization/cut-contract检查通过，worktree diff检查通过。下一路线为held-out line/gate、joint-likelihood和calibration-transfer设计，未推进新课程卡。最终发布检查只在原窗口closeout执行。

第一段历史检查（后续窗口已重开）：boundary exit0（无error/warning）；Wiki lint最终 exit0，0 errors /92 warnings /1558 info。Warnings为89项既有citation-key缺失和3项reaction-parser边界；未猜测BibTeX key。第一次lint的4个错误仅为新method缺少Purpose/Inputs/Can/Cannot四小节，按模板/config补齐后同命令回归通过；失败记录保留。

report headings、唯一writeback（12items/8changed pages/0locator errors）、Day13 coverage与Day14 partial、PLAN/Bib保护检查均通过；git diff --check exit0。具体代码/MC结果和preflight记录可回到run-dir audit。提交前仍核对显式stage、cached diff、fresh fetch/ancestry/dry-run和非force push；真实结果只写run receipt，不把计划写成发布成功。

first-write boundary/preflight/EOL checks均成功，index初始为空。继承的Day6–9 run artifacts、system/log旧差异和daemon修改排除；raw/PLAN/受保护Bib只读，源PDF哈希一致。overview/QMD update按本次局部方法增量deferred；只读collection boundary已通过。

上一段历史收束时间为2026-10-13 17:51:03+08:00，早于原硬截止1268.94分钟；原deadline不改。原因、全候选池与Day14检查保存在research-closeout.json；它保留缺失输入和重复核验无新增判别能力的具体边界。本次用户已要求继续，正在检查其它独立方法/反证及高信息计算路线，不等待Mavela单次实验packet；讨论仍可用本页resume_command。

本轮续接文件：[continuation-prompt.md](20261013-DAY13-doppler-correction-recoil-velocity-run-01/continuation-prompt.md)。Formal Day14须新session，保持本次预习不计学分；最终发布和课程状态转换记录于run.json与scheduler event，精确hash只写任务回执。
