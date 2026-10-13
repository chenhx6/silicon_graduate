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

## Counter-evidence and missing companion observables

1. Klemme Fig.1同一line有距离相关shifted/unshifted分量，反驳“两个峰必是两条跃迁”；Table I的6g+从1.38到corrected1.63ps增加18.1%，显示finite stopping影响寿命。
2. Herzáň Fig.5(a)的quadruplet反驳“一个谱峰必是一条γ”；低能非观测的解释不能自动填成已测线。
3. rank-2是推导层反例，反驳width-only decomposition的充分性；它不声称Mavela真实nuisance就是这组值。
4. 必需packet：executed sorter/geometry/β inputs、ring/sector与γ-crystal切片、matched gates、energy calibration/response、joint covariance、stopping/feeding metadata。缺这些不能比较β20/24的实际影响或修订GOSIA/Q_S。

## Knowledge Impact and Learning Decision

`supports`：exact correction、逐emitter谱/yield身份、stopping与谱峰/跃迁区分。

`revises`：多角度width可诊断输入，却在已声明低速模型中不能独自分解三个nuisance；应先取得独立calibration。

`limits`：总谱窄峰、shared gate、energy closure、relative Iγ与模型曲线的结构推断。A≈130 chirality/wobbling/signature/configuration解释排序不变，未获得新绝对B矩阵。

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
| L2 | exact formula/covariance、geometry/gates、convention/decay、speed/calibration、aberration、displaced vertex、neutron cuts、photon recoil、Voigt与momentum stages均为可复算方法练习；未冒充测量。 |
| L3 | 诊断问题的竞争机制、反证、falsifier、数据包与停止条件完成；真实Mavela执行影响仍partial。 |
| L4 | experimental refit `not-ready`：缺事件、production code、ring spectra、response/covariance和feeding；模拟练习不作为新实验L4或absolute-strength研究。 |

## Verification and continuation

最新活动检查（2026-10-14T01:54:40.245714+08:00，距截止约785.3分钟）：累计writeback56items/22mappedpages。三份新增方法/primary source与two-distance、fixed-gate likelihood、event-mixing练习均已写回，参数/零核/积分/MC检查通过。lint exit0，0errors/110warnings（98citation-key、9未填充raw archives、3reaction-parser）；report/card/writeback/protected/diff通过，原窗口仍active。当前发布是checkpoint，不触发new credit或closeout。

持续检查（2026-10-14T01:00:40.490662+08:00，距截止约839.3分钟）：研究仍active。当前累计唯一writeback43items/19mapped pages；基于reopen snapshot的path/anchor/atomic locator、report/card coverage与PLAN/Bib hashes检查通过。Wiki lint exit0，0errors/104warnings（95citation-key、6reserved raw archive缺失、3reaction-parser）；不把missing archive写成已归档。四项本段新练习的conservation/limits/normalization/cut-contract检查通过，worktree diff检查通过。下一路线为held-out line/gate、joint-likelihood和calibration-transfer设计，未推进新课程卡。最终发布检查只在原窗口closeout执行。

第一段历史检查（后续窗口已重开）：boundary exit0（无error/warning）；Wiki lint最终 exit0，0 errors /92 warnings /1558 info。Warnings为89项既有citation-key缺失和3项reaction-parser边界；未猜测BibTeX key。第一次lint的4个错误仅为新method缺少Purpose/Inputs/Can/Cannot四小节，按模板/config补齐后同命令回归通过；失败记录保留。

report headings、唯一writeback（12items/8changed pages/0locator errors）、Day13 coverage与Day14 partial、PLAN/Bib保护检查均通过；git diff --check exit0。具体代码/MC结果和preflight记录可回到run-dir audit。提交前仍核对显式stage、cached diff、fresh fetch/ancestry/dry-run和非force push；真实结果只写run receipt，不把计划写成发布成功。

first-write boundary/preflight/EOL checks均成功，index初始为空。继承的Day6–9 run artifacts、system/log旧差异和daemon修改排除；raw/PLAN/受保护Bib只读，源PDF哈希一致。overview/QMD update按本次局部方法增量deferred；只读collection boundary已通过。

上一段历史收束时间为2026-10-13 17:51:03+08:00，早于原硬截止1268.94分钟；原deadline不改。原因、全候选池与Day14检查保存在research-closeout.json；它保留缺失输入和重复核验无新增判别能力的具体边界。本次用户已要求继续，正在检查其它独立方法/反证及高信息计算路线，不等待Mavela单次实验packet；讨论仍可用本页resume_command。

本轮续接文件：[continuation-prompt.md](20261013-DAY13-doppler-correction-recoil-velocity-run-01/continuation-prompt.md)。Formal Day14须新session，保持本次预习不计学分；最终发布和课程状态转换记录于run.json与scheduler event，精确hash只写任务回执。
