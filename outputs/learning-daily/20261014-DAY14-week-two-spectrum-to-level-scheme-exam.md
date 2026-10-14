---
type: learning-report
graph-excluded: true
created: 2026-10-14
updated: 2026-10-15
---

# DAY14 第二次周考：从谱到能级纲图

## Run state

- run_id: `2026-10-14-day-14-02`
- run_date: `2026-10-14`；timezone: `Asia/Shanghai`
- day_index: 14；phase: `gamma-spectroscopy-and-level-schemes`
- schedule_id: `wiki-daily-learning`；run_kind: `substantive / weekly-learning`
- session_id: `01a13a0e-e8bd-7251-b970-f6975679e281`
- resume_command: `codex resume 01a13a0e-e8bd-7251-b970-f6975679e281 -C /workspace/wiki -s danger-full-access -a never`
- overnight_until: `2026-10-15T15:00:00+08:00`；15:00–16:00仅收束。
- research_status: active；本报告是内容checkpoint，不是整段时窗完成。
- completed_day_indices: [14]
- partial_day_indices: [15]
- Day 14 card audit: complete
- Day 14 scorecard: complete
- Day 14 weekly REFLECT: complete
- course_credit: 尚未推进；需report/writeback/checks/continuation/publication通过后才计Day14，持续研究不重复计卡。

本次session身份由run-02 `events.jsonl` 的thread.started与原生goal threadId交叉确认；补记receipt和scheduler事件。run-01是此前已取消的另一session，不接管、不自动重启。恢复任务使用用户已给出的持续学习、写入与Gitee授权，Farmer只监督allowlisted瞬时错误，没有Git角色。已有Day6–9/Day13回执、旧log与daemon修改保留。

### Day 14 card completion audit

| 课程交付 | 本次artifact与精确evidence locator | 状态 |
| --- | --- | --- |
| 来源前画三层级联、门条件与DCO/偏振/寿命位置 | [冻结回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/active-recall-before-sources.md)，三层图和六条原答；保存后才打开source/raw，明确primed | complete |
| 沿全文主线核验一图一表 | [[herzan-2015-193bi-spectroscopy]] HE15-4/8，PDF p.3与p.7 Table I / p.8 Figure2；本文pp.1–20主线回读，关键图表视觉核验 | complete |
| 重建子纲图并逐线分级 | [[level-scheme-reconstruction]] “Day14 五能级七跃迁逐边审计”，七条E/C/M/J证据；HE15-4、HE15-8 | complete |
| 理论/定量练习 | [fixture](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-fixture.json)与[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-analysis.json)，35项检查；HE15-4/8/9/10/12 | complete |
| 可能重排纲图的反证与必要伴随观测 | HE15-9，PDF p.7 Table I footnote f；HE15-5 p.10 Fig.5；方法页“标定、寿命与伴随观测的逐项契约” | complete |
| 实验判据矩阵、六维评分和weekly REFLECT | 本文对应三节；[周度回执](../learning-weekly/20261014-week-two-spectrum-to-level-scheme-reflect.md)；canonical方法页“第二周证据链的可复用认识修正” | complete |

## Candidate pool and selection

连续性问题是“能量闭合和共同门能否唯一指定跃迁身份、顺序与Jπ”。Day14课程明确指定Herzáň或Ding；选择Herzáň193Bi既便于正式复核昨日预习，又与近期A≈130/C/O Doppler工作的核素及采集不同。正式卡要求覆盖同一source，所以这是记录在案的cooldown exception，不能继承Day13预习19/24或其学分。

| 候选 / coverage | 信息增益与选择 | 当前边界 |
| --- | --- | --- |
| 193Bi一图一表、Band1五level七边 | continuity selected；将单三层closure扩为相关cycle审计，查到319.8-keV表尾行 | 没有逐对事件/Σ，不重新评价实验能级精度 |
| 393.4/394.0双线顺序与shared R/A | 同一continuity问题的直接反证；能量和和允许ΔI均不解除未定顺序 | 需要独立endpoint、branch、time或tag |
| a(E)/Q(E)、isomer assignment与parent lifetime | 同一证据链必要companion；明确source实际DCO定义及条件性spin | 无原counts，反事实不重估作者误差或δ |
| SD floating X、1836-keV tentative link与46/87-keV非观测 | 检查原论文结论边界；保留model/作者解释 | 无confirmed link/absolute strengths，不能确定X或形变 |
| Ding127/128I再做同类闭合 | deferred；近期已作反应/谱系，当前未定双线更能检验方法 | 不是用重复来源充填novelty |
| Day15 ADO知识预习 | 当前shared-POL必要域已固化，转向相邻卡的geometry/gate修正与误差可识别性 | partial15；不计卡，实际matched-gate/response/covariance仍缺 |

最近学习覆盖：Day8选律/δ约定，Day9寿命/branch→strength，Day10双带电磁指纹与谱系，Day11–12反应布居/符合背景，Day13 Doppler/速度/停止/统计，均以既有日报与canonical知识页定位。当前不把这些日报用作新的实验来源，也不从数量推学习饱和。另一个非重叠novelty问题未强行选择。

### Active recall 与 priming

来源前答案完整保存在[冻结回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/active-recall-before-sources.md)。已读运行prompt/handoff中的昨日预习摘要，所以明确为primed recall；未凭记忆填Herzáň具体能量、R/A或误差。原答正确指出共同门、相对能量自由度、阵列特定DCO、P/A/Q分离和parent lifetime，但尚未写出三个cycle的相关性或本文未定双线表注，这些由正式读图/表后补足。

## Sources and evidence

| 来源 / 身份 | 本轮实际覆盖与locator | 证据分层与独立性 |
| --- | --- | --- |
| Herzáň et al., PRC92,044310(2015), DOI[10.1103/PhysRevC.92.044310](https://doi.org/10.1103/PhysRevC.92.044310)；citation key `Herz__2015`；raw SHA256 `f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea`，20页 | pp.1–2动机/setup/tagging；pp.3–7全部Table I；pp.8–9 Figure2；pp.10–15各带/isomer/SD；pp.16–20组态、systematics、结论、引用。视觉核p.3/7/8/10/15 | 一次JYFL193Bi acquisition；Table I/Figure2/Figure5是dependent图表/投影；153-ns bandhead引用Ref7，非本次七线parent的新τ |
| 外部结构化Crossref核验 | [metadata回执](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/crossref-herzan-metadata.json)，作者/题名/2015/卷92/DOI一致 | 元数据核验，不是独立实验；返回pages为空，文章号由PDF核验 |
| Canonical source与方法 | [[herzan-2015-193bi-spectroscopy]] HE15-4–14；[[level-scheme-reconstruction]]新增逐边、cycle、topology、companion sections | 实验测量、联合赋值、作者解释、模型和任务推导分开；旧needs_review全保留 |
| Zheng2002原扫描全文；DOI留空，身份由期刊页眉与rawhash核验 | [[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-1/6/7/8；PDF pp.1–5，重点p.2 Eq1–5、p.3 Fig1/效率、p.4 Fig2/Ref3 | Day15无学分预习；f的计算偏离与实验标准误差分开；Ref3 DOI [10.1007/s100500170001](https://doi.org/10.1007/s100500170001)仅metadata，2002文依赖对应145Tb实验 |
| Rose–Brink1967方法依赖局部复核 | [[rose-brink-1967-phase-defined-angular-distributions]] RB67-11，printed316/PDF11 Eq3.24/25；RB67-4，printed320/PDF15 Eq3.40/41的既有直接核验；本段视觉回核printed326/PDF21 Eq3.69–3.73 | formalism，非193Bi新数据；初态polarization、photon helicity、detector sensitivity与ENSDF Q分别定义 |
| Zobel1983，DOI [10.1016/0167-5087(83)90649-X](https://doi.org/10.1016/0167-5087(83)90649-X)，citation key zobel_1983_Energyprojectile | [[zobel-1983-energy-projectile-alignment]] Z83-11/12/13/14；六页printed389–394全部视觉主线，Eq1–3、Table1、Fig1–5/refs；rawhash/metadata回执在本run | 67Ga published fit coefficients；新分析为Codex self-audit，原Jul08人审/旧flags保留；Ref4 purity/structure和Ref5方法依赖不能重复计采集 |

主要定位：HE15-8是Table I p.3/p.7及Figure2 p.8；HE15-9是p.7 footnote f；HE15-10是p.7 a定义及p.10 Figures3/4；HE15-11是p.13条件性29/2+赋值与p.14 conversion；HE15-12是p.10 Ref7寿命与p.3相对强度；HE15-13是p.19 conversion/SD解释。源页保存每条claim的locator，不用搜索片段当证据。

## Theory/analysis exercise

七边的中心值闭合为`+0.2,+0.4,+0.3 keV`。D的rank4、三个cycle、绝对offset nullspace均由代码核验。独立0.1-keV拟合误差下条件χ²=6.666667；自设将caption约0.3 keV按quadrature加上、并令各线独立后，χ²=0.666667，dof3。后者cycle Σ为`0.1×(3,1,0; 1,3,1; 0,1,3) keV²`，不是三个可相乘的独立检验。

独立whitened least squares与cycle-space χ²相等；共享gain取消、共享加性offset保留；换row顺序结果不变；刻意错移一条crossover的失败检查能检出不相容。393/394换序演示同时保留upper=2045.5 keV，但intermediate差0.6 keV；这些不是修改后的实验能级。SD链rank13/14说明未知X仍为自由度。

依原文a(E)重算：a(323.4)=1.0955364，A=−0.012对应条件N⊥/N∥=0.8911476；错误令a=1会得−0.0575589。不是新偏振测量，未从公开表反推原始counts。三个same-parent photon-intensity ratio为2.132231、1.921569、1.157407；没有τ/ICC/δ/branch completeness，均不转换成absolute B或total branch。

执行命令：

```bash
python3 system/scripts/day14_level_scheme_audit.py --fixture outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-fixture.json --output outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-analysis.json
```

实际exit0，35/35检查通过。核心公式、数值与适用边界的canonical副本在[[level-scheme-reconstruction]]，run-dir保存输入转录、代码结果与哈希回执。

### 实验判据矩阵

| 命题层级 | 本次可用观测 | 可支持范围 | 仍需信息 / 失败条件 |
| --- | --- | --- | --- |
| emitter/line identity | reaction、RITU/GREAT tag、Figure5 matched gates | 作者归属的193Bi谱线 | random/target污染、quadruplet、299.2/299.8response必须控制 |
| placement/order | γγ/γγγ、Figure2、Table I、energy sums | source-level七边子图 | 双线order、共享祖先门与共用calibration不能只靠closure裁决 |
| multipolarity | setup-specific Rexp和校正a(E)后的A | 支持作者M1/E2赋值 | δ、高阶、alignment、gate/response；shared-doublet值不识别每一line |
| Jπ | multipolarity加可信anchor、conversion与parallel path | 有条件沿图传播 | HE15-11明确依赖Band1；不凭RDCO或偏振单独量出absolute spin |
| τ/absolute strength | 本文isomer时间与conversion；先前153-ns引用 | 对对应isomer建立更强链 | 不能把bandheadτ赋给七边parent；需各parent τ、全branches、ICC、δ |
| configuration/shape/mode | alignment/ratio/systematics、作者semi-empirical模型 | 受约束解释和candidate | SD absolute strengths与confirmed link仍缺；没有新的A≈130模式判定 |

### Continuity checkpoint：conditional gate 与复合峰

正式周考发布后继续同一问题；[计算前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/gate-design-before-analysis.md)与[37-check设计结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-gate-design.json)保留顺序。代码 `system/scripts/day14_conditional_gate_design.py` 实际exit0、37/37；64状态枚举与5×10⁶-event独立MC的mean/second moment最大z≈2.18。b/h/效率/σ/parent数量全为自设、无IC/feeding/angular correlation的限制模型，不是193Bi数据。

已知纯A=622直接支与B=323级联门的conditional系数时，两门可解除同response两强度参数的rank1退化；A门效率→0、b→1或比例污染则失败。若只保留两张合并峰总面积且b未知，存在连续physical等价族；完整可分的joint energy spectra并不只有这两个信息。shared-event双γ在B门下产生positive covariance，固定N与Poisson parent flow的Σ不同，不能把每个line/gate都当独立Poisson。

HE15-13低能γ的设计例（N=5000、ε=.01、branch=1）给46/87-keV零计数概率0.826/0.0268；没有实际flow/efficiency/背景，这不是sourceupper limit。完整公式/数值/边界已canonical写回[[level-scheme-reconstruction]] “互斥分支门、复合峰与shared-event计数”。

### Day15 无学分ADO计算与误差图

来源前primed回忆见[预习原答](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-preview-before-sources.md)。Zheng2002扫描件5页已视觉读完；Z02-6明确ε为组效率之和，1/N来自self-exclusion。仅两角计数和target效率比不能识别f，还需独立本征参考或gate response；原式方向为R_ADO=(ω1S/ω1L)f。

全部自设：5000/4800计数、效率比.80±.016、额外参考1.34±.04给R_ADO=1.302083、f=.971704、独立假设σf=.040057。改变自设efficiency/reference相关系数−.8/0/+.8，σf为.026508/.040057/.050065；不是原实验误差。均匀组内response f=.974006；保持同组总效率但使两个能量效率相关地不均匀时，explicit pair-sum f=.772081。原文5.2%/3.2%是calculated最大偏离，不是完整实验uncertainty。

脚本 `system/scripts/day15_ado_preview_worksheet.py` 实际exit0，28项检查通过。[完整计算](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-ado-preview-worksheet.json)与[误差图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-ado-input-uncertainty.svg)经PNG视觉核验。等权32/58/90的P2抵消与理想31.7175/58.2825/90的P2/P4同时抵消是任务推导，未当作者的设计意图。38 hardware pairs与44 ordered energy assignments不同，不能直接推出独立统计精度。

条件接回Day14：若只靠几何乘法f恢复旧common-selection point model的shared mean，需要f≥1.488716，对应self-exclusion必要η≥.32828；145Tb均匀4台组的4/3上界不能移植到JUROGAM或作为实验排除。完整定义、推导、数值和反例已写入[[angular-distribution]]“ADO计算单：额外输入、self-exclusion与误差”；同时按RB67-4修正旧method中初态polarized必需奇K的过强表述。Day15只列partial15，不建formal audit或计学分。

### 条件γγ响应：分离式的可检验边界

[本段来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-correlation-before-source-recall.md)明确priming；随后核RB rawhash并视觉读printed326/PDF21 Eq3.69–3.73和Zheng printed910/PDF2 Eq1–5。RB67-3保留random initial、definite parity与helicity-unobserved条件；Z02-9记录原Eq2乘积而不替作者声称角关联已消除。

自设0→L→0、两条pure-electric photon rank L∈{1,2}，spin-matrix/CG/helicity与独立Legendre展开给K1=1+½P2、K2=1+(5/14)P2+(8/7)P4；singleγ均isotropic，joint仍有correlation。完整均匀gate恢复I/(2L+1)，有限gate有conditional density；这不是193Bi或145Tb的新level/spin。

自设32/58/90°各4台、四方位、每组gate效率.04，explicit pair加self-exclusion：E1的R=1，E2的R=.729470，分离组式都给1。无self-exclusion的disjoint 90°ring gate也给E1/E2条件比.760271/.697063，隔离了角关联贡献。只让三极角ΣP2/P4=0仍留q=±4方位harmonic；每圈8方位才对本toy消去K2/K4。自设20°/35°finite cones把某个E2 point K=.594119变为.940478，与Qk卷积和独立quadrature一致。

代码 `system/scripts/day14_conditional_angular_response.py` 实际exit0，[35项结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-angular-response.json)通过；它与第一组纲图35-check是不同exercise。完整公式、density/effect、参数、数值及边界已固化到[[angular-correlation]]“条件γγ响应：各向同性marginal仍可有角关联”，接回ADO及level scheme方法。结论为limits单γfactorization的充分性、supports逐pair matched-response核验，不给shared393/394新E2/M2/Jπ结论。

### 近邻双线排序：对称性先于增加角数据

[计算前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/order-correlation-before-calculation.md)保留了“有取向可能增加信息”的初始预期及priming。general-spin结果使预期收紧：静态random-initial intensity只依赖两方向夹角，交换不变；两个同rank/同E-M类型pure stretched downward transitions还有更强的maximal-CG对称性，中间binomial抵消，full amplitude对photon交换对称，任意同一initialρ也不能从角度/偏振数据判能量标签先后。

自设pure E2 19/2→15/2→11/2：binomial与独立total-J²/highest-state/lowering构造相同，full-amplitude swap最大差4.48×10⁻16，random/Gaussian/coherent三种initial的角强度差均在浮点误差内。非stretched控制19/2→17/2→13/2在random initial仍对称，但chosen Gaussian、chosen方位/点角下两个ordered intensities为.879316/1.297627。都不是193Bi的spin/数据预测。

脚本 `system/scripts/day14_cascade_order_identifiability.py` 实际exit0，[51-check结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/cascade-order-identifiability.json)通过；删除了一个无信息的response同值检查，最终数为51。exact unobserved feeding middle与每层另行设同σ/J=.3的Gaussian，L1距离为.076428/.143581，说明该重置是额外输入，不是原cascade channel自动给出的结果。

完整proof与边界在[[angular-correlation]]“双γ排序的交换对称性”，接回[[level-scheme-reconstruction]]“近邻双线排序的角关联可识别性”；source premises为RB67-3/11，HE15-9仅是实际未定order的动机。决定revises观测选择：先检验交换对称性，若在其条件内，优先middle branch/独立level/time或能证明模型条件失效的观测；不默认更精细DCO/POL能判先后。实际weak-line Q/(E2)/π、shared R/A与review flags保留，未做排序fit或significance。

### Day15无学分实测对照：67Ga条件迁移

[来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-before-source-recall.md)先于source打开；近期fingerprint仅见本run的候选提示，Ionescu1981已有Oct12使用而暂缓重复。选择非重叠novelty问题“同parent取向/参考条件迁移”，核素与data context为67Ga，与continuity的193Bi双线身份/顺序分开。主线沿Zobel全部六页、图表/公式/setup/误差/结论核完；Crossref HTTP200 exact DOI/title/207(3)/389–394/1983，rawhash匹配，未用搜索snippet当证据。

Z83-11的958.0-keV同parent Table1完整十行已upright视觉转录：[fixture](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-958-table-fixture.json)。它们是published LS fit estimates，表误差为statistical，delta采用0；alpha9MeV该列空白未填零，其他parent的30行按matched-parent问题未选，raw40行保存。alpha22−11.3MeV的Δalpha2/4为−.299/−.588，若quotederrors按std且独立，差量误差.051624/.125176；C48−32为−.037/−.182及.049679/.144045，未报实验显著性。

作者p393明确alpha2/alpha4 statistical dependence和error ellipse（Z83-12），数值Cov未提供。源码区分GF的peak-profile Gaussian与nuclear-population Gaussian；本任务自定义s为std、half-integer complete reference |M|=1/2。Stevens/独立CG tensor一致；alpha2-only条件s/J .127046/.365043不是作者实测sigma/I或jointfit。11.3MeV residual的chosenrho −.8/0/+.8给sigma_r .197717/.148564/.071067，只是敏感性；没有原Cov/response不作Gaussian排除概率。

自设两Gaussian width .12/.38、weight .45混合给alpha=(.797082,.564819)，与同alpha2的singleGaussian alpha4差.089121，未拟合Fig3的direct fraction。另以mass-number CM64/68、扣caption4MeV阈值幅度及3.0317MeVparent重构Fig3六lower ticks，最大差.004182MeV；它是坐标cross-check，不认证作者精确mass/targetloss或反应Q符号。

脚本 `system/scripts/day14_zobel83_alignment_worksheet.py` 实际exit0，38项通过；[结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-alignment-worksheet.json)、[SVG图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-alpha-data-model.svg)和CSV/source-data可复核。沿用Python并应用nature-figure：singlepanel alignment not applicable，glyph/collision/source audits均exit0，minfont8pt、collision0fail0warn，PNG视觉通过；源码3export/width warnings按Wiki140×110mm/vector图+400dpi预览逐项复核。详情见[图QA](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-figure-qa.md)。

决定supports条件/feeding-aware reference transfer，limits统一sigma/I和两误差的joint检验；Z83-9的same-energy/same-target还涉及effective beam/targetloss。全数值、模型、约定、反证和边界canonical写在[[angular-distribution]]“Zobel1983：同parent反应条件与Gaussian诊断”；Z83 source新11–14为needs_review:true，旧human metadata及1–10 flags保留，未扩原Jul08审核范围。Day15仍partial、不计卡；实际数据摘要可用，原events/fitCov/完整response仍缺，L4 replay not-ready。

### Angular-fit Cov：knowngeometry与两个errors仍不唯一

[计算前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/angular-covariance-before-calculation.md)标明priming与本source已全文读。Z83-15的C四angles同时采、alpha两组三angles加fixedmonitor是knownsetup；raw intensities/efficiencies/monitor/实际GF covariance仍未给。

本任务选三parameter beta0+beta2P2+beta4P4再归一，以sourcealpha11.3 fit point(.973,.803)、F=1为local Jacobian点（Cgeometry也固定此点以隔离geometry，不称C组actualmean）。任务pureE2 max coefficients为40/91、−216/1001；equal absolute variance下两geometry的rho为+.504879/−.631222。未知F的Jacobian、QR、直接F/alpha Fisher与profiledSchur结果一致；把F当已知会改变Cov。

同alpha六angles、same point，两个chosen positive diagonal variance examples保持marginalsigmas .037/.090，rho仍为−.963993/−.142543。两者是可行噪声示例，未认证globalbounds或恢复sourceGF。全局multiplicative mode在normalizedalpha一阶取消，但chosen2%第一run monitor-mode会改变矩阵；实际monitor error未知。

代码 `system/scripts/day14_angular_fit_covariance_design.py` 实际exit0，[26项结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/angular-fit-covariance-design.json)通过。完整X/J/GLS/Fisher/Schur、矩阵/variance/条件写在[[angular-distribution]]“角采样与归一化下的Cov可识别性”，Z83-15为新needs_review:true。决定limits从marginalerrors+geometry反推actualjoint判断，supports保存fitparameterization/weights/shared-normalization；没有实验significance、新sigma/I或新line assignment，Day15仍partial。

## Counter-evidence and missing companion observables

HE15-9的实际未定双线是核心反例：energy sum、共享R/A和假设的ΔI=2均不足以裁决order。若一条线出现可独立定位的旁路或延迟顺序，应重审中间level；source仍保留括号Jπ与(E2)。HE15-5的quadruplet限制“一个峰是一条γ”的简化；干净622.4直接分支门与323.4级联门的299-keVcomponent差异可能迫使拆峰，但必须控制622/626门纯度、feeding、response和random。

必要companion分类：confirmed SD link与endpoint为expected-but-not-established；46/87-keV低能γ为not observed、原因仍是作者解释；缺事件/Σ的重拟合为blocked-needs-event-level data。αtot=261/12.82与87.4-keV x ray会降低γ灵敏度，不能把未见峰直接写成路径不存在。Table I/Figure2/Figure5和多角度数据共享采集，互补不等于独立复测。

## Knowledge Impact and Learning Decision

- **supports：** 一图一表的逐边source-level纲图和DCO/偏振/转换联合证据链。
- **limits：** 三个closure视作独立测试、shared-doublet R/A视作逐线性质、bandheadτ视作parentτ、relative intensity视作absolute strength的捷径。
- **revises：** 对下一项信息的选择从“再算能量和”转为定位未定endpoint、测试独立anchor与取得parent-resolved电磁输入。
- 193Bi与A≈130的configuration/mode排序均未改变。无新增human-review事件，source/page review状态不提升。

## Day 14 scorecard

这是本session正式任务产物的六维Codex self-assessment，受Day13预习priming影响，不能称为独立盲考能力或把19/24当基线实验。0=未做，1=复述，2=条件应用，3=有source和可复算反例，4=能沿证据链指出并测试判决边界。

| 维度 | 分数（0–4） | 本次可核验证据与短板 |
| --- | ---: | --- |
| 理论 | 3 | incidence/cycle/GLS、offset/gain区别与独立解法；未完整重推γγ角关联formalism |
| 判图 | 4 | 原图/全部续表逐边七线，查到319.8表尾行及393/394未定顺序；保留X |
| 误差 | 3 | caption额外误差、cycle相关、Σ敏感性与失败控制；真实joint response/calibration缺失 |
| 证据分层 | 4 | 直接峰量、联合placement/Jπ、作者形状解释、模型与counterfactual明确分开 |
| 反证 | 4 | 原论文doublet、quadruplet、branch互斥和弱线非观测边界均有locator |
| 可证伪问题 | 3 | 可定位branch/time/tag和parentτ设计；没有事件级数据验证实际检出功效 |

合计21/24。仍需补强的是真实gating/response功效、完整calibration covariance及角关联前向模型；不通过加分隐藏这些短板。

## Day 14 weekly REFLECT

本周从选律、B定义、双带指纹、反应与门控、Doppler和统计走到逐边纲图。最应修正的习惯是把“每一步相容”累加为“结构唯一”：HE15-9给出真实未定顺序，HE15-11显式依赖Band1，HE15-12阻止借用bandheadτ，均要求定位尚未识别的自由度。

后续判断：先验证line/parent/branch identity，再讨论δ和绝对strength；对共享数据的角度/偏振、图/表、calibration和model projection保留依赖；把最小测量对准不同候选预测会分开的observable。canonical认识修正已写入[[level-scheme-reconstruction]]，周度回执只记录学习状态。当前证据支持方法层面的修订，没有支持新的wobbling/chirality/shape裁决。

## Durable knowledge delta

本run实际修改十一份knowledge Markdown，超出昨日预习的增量为七边逐条证据、相关cycle/标定nullspace、未定doublet shared-quantity边界和parent-lifetime契约。canonical知识路径：

- [Herzáň source](../../knowledge/sources/herzan-2015-193bi-spectroscopy.md)：HE15-8–14及正式来源主线/triage。
- [level-scheme method](../../knowledge/methods/level-scheme-reconstruction.md)：五能级七边、GLS/反例和必要companion。
- [A≈130 thesis matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)：方法对照行，不冒充A≈130新实验。
- [NNDC193Bi evaluation](../../knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md)：公开对象的版本、RI/精度、weak-line/Q与条件CC；不是独立实验。
- [知识索引](../../knowledge/index.md)：新增评价source导航。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
      "summary": "核验七边中的表尾行、未定双线与共享角度/偏振、实际标定、条件性isomer赋值及parent寿命来源；原flags保留。；原p7/p9的352.3图表spin差异重新视觉核验。",
      "anchor": "Day14 正式逐边复核与来源边界",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-10"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-12"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-13"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-14"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "固化五level七边逐条E/C/M/J审计、三个相关cycle与带假设35-check重算；不替换作者能级。",
      "anchor": "Day14 五能级七跃迁逐边审计",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "保留actual a(E)/Q(E)、bandhead与parent寿命、conditional intensity和SD低能companion的区别；weekly认识修正同步canonical页。",
      "anchor": "标定、寿命与伴随观测的逐项契约",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-10"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-12"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "增加spectrum-to-level correlated-closure方法对照行和active说明；193Bi不当作A≈130模式独立证据。",
      "anchor": "Day14 spectrum-to-level identity and correlated closure",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-2"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "37-check纯分支gate/unknown-branch/shared-count/low-energy nonobservation设计；全部自设条件，不作为actual193Bi counts或branch fit。",
      "anchor": "互斥分支门、复合峰与shared-event计数",
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
          "locator": "HE15-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
      "summary": "新增官方选定ENSDF对象的version/hash/locators、七边精度和RI、weak-line Q/352冲突、BrIcc计算与153-ns依赖；非新独立实验。",
      "anchor": "193Bi：评价对象与原实验的分层",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-1"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-2"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-3"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-4"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-6"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-7"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-8"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-9"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "真实evaluation crosswalk与79-check；明确整数/调整精度、Q≠E2、352.3 triangle冲突、parent conditional photon/totalbranch区别。",
      "anchor": "原图、评价精度与赋值冲突的crosswalk",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-3"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-4"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-6"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-7"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-8"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "新增193Bi官方评价来源导航，注明共享2015He27与CC/model边界。",
      "anchor": "nndc-2017-193bi-level-scheme-evaluation",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "summary": "70-check sharedA凸组合、nearbycalibration、pureE2取向/联合R/A必要域和selection失败条件；不做line/M2/Jpi赋值。",
      "anchor": "未分峰偏振的联合命题与选择条件",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-10"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "将joint POL条件约束、orientation/geometry/selection与spin-parity边界接回level-scheme evidence chain。明确同名energy gate未必有共同target-independent effect。",
      "anchor": "Shared POL 对joint命题的条件约束",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
      "summary": "原扫描全文再核，新增组效率/self-exclusion定义、calculated偏离与数据谱系边界；不清review flags。追加Z02-9 Eq2/full-joint迁移边界；不替作者声称correlation已消除。",
      "anchor": "Day15 无学分预习：定义、归一与原始阅读",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-7"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-8"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "固化28-check ADO自设练习、f额外输入、逐台response反例、uncertainty/covariance和有条件Day14几何桥；仅partial15。接回35-check conditional γγ response。",
      "anchor": "ADO计算单：额外输入、self-exclusion与误差",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-1"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-7"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-9"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "修正polarized初态必需奇K的过强表述，保留definite-parity/helicity-summed与w(-M)=w(M)两项条件及detector/nuclear attenuation区别。",
      "anchor": "初末态宇称确定且不测 γ 偏振",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
      "summary": "局部视觉回核printed326/PDF21 Eq3.69–3.73，保留parity/helicity/random-initial条件和任务toy分层；不重复全42页阅读或清review。接入51-check最大耦合交换对称性，明确为任务推导。",
      "anchor": "Day14 条件γγ响应的局部回核",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "summary": "35-check conditional γγ toy：isotropic marginals不保证factorization，K1/K2、ρ/effect、pair/self-exclusion、azimuth cancellation与finite cones；未做真实谱重放。",
      "anchor": "条件γγ响应：各向同性marginal仍可有角关联",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "summary": "51-check general-spin、binomial/total-J²-ladder、任意initialρ的same-rank stretched full-amplitude对称性及非stretched失败控制；feeding同σ/J不是自动输出。",
      "anchor": "双γ排序的交换对称性",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "将exchange symmetry接回实际未定双线的下一观测选择；不改变weak-line赋值或宣称actual模型条件成立。",
      "anchor": "近邻双线排序的角关联可识别性",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
      "summary": "六页主线/metadata/raw核验，新增Table1 selected means、statCov边界、Ref4/5依赖与Fig3坐标核算，原Human/旧flags保留、新11–14 true。新增Z83-15实际angles/two-run normalization，原旧人审不扩。",
      "anchor": "Day14无学分预习：同parent条件迁移与统计边界",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-13"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-14"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-8"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-9"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "十个published同parent alpha pairs、38-check CG/Stevens/条件Gaussian/std/inversion/Cov sensitivity/mixture/CMticks、SVG及图QA写回；不作experimental significance或统一sigma/I。",
      "anchor": "Zobel1983：同parent反应条件与Gaussian诊断",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-13"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-14"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-8"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "26-check knowngeometry/GLS/Jacobian/Fisher/Schur/same-marginalpositivevariance/global-vs-run-mode设计，rho示例不当actualGF；完整公式/矩阵/输入边界固化。",
      "anchor": "角采样与归一化下的Cov可识别性",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-15"
        }
      ]
    }
  ]
}
```

### Day15预习的canonical增量

- [Zheng2002 source](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md)：Z02-6/7/8，原式组效率、calculated deviation和Ref3谱系。
- [角分布方法](../../knowledge/methods/angular-distribution.md)：ADO计算单与group/individual response、额外输入、covariance、条件桥，以及RB67-4的even-K条件修正。

### 条件响应的canonical增量

- [角关联方法](../../knowledge/methods/angular-correlation.md)：conditional density、K1/K2、pair/azimuth/finite-cone反例与matched-response输入。
- [RB1967 source](../../knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md)：局部原图/公式条件复核，RB67-3/11；[Zheng source](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md)新增Z02-9迁移边界。

### 67Ga条件迁移的canonical增量

- [Zobel1983 source](../../knowledge/sources/zobel-1983-energy-projectile-alignment.md)：新Z83-11–14、原表/误差/依赖/mainline scope；原人审不扩展。
- [角分布方法](../../knowledge/methods/angular-distribution.md)：10行原表数据、条件Gaussian模型/标准差s约定、unknownCov、mixture与Fig3坐标核算及图。

### Ref7 原始寿命依赖的有界外部核验

本段保存了[原文前依赖回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nieminen-before-source-recall.md)，以nature-academic-search/nature-downloader做一个DOI pack。Crossref确认Nieminen2004题名、作者、卷69/DOI；arXiv初查询400，简化query0结果；OpenAlex exact DOI closed，OA downloader exit0但下载0、oa_not_found；APS前缀502、直接HTTPS403 HTML，JYX候选API超时，Scholar工具超时。详见[access recap](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nieminen-access-recap.json)。自动confirmed_oa标签未采信：APS default license不代表OA，且同manifest的Unpaywall为false；candidate URL不等于PDF已取。

未新增Nieminenprimary source页或猜测其寿命方法/数据谱系；153-ns仍为HE15-12的外部bandhead引用，canonical source页已固化此边界。保持研究active，转向公开193Bi evaluation做版本/locator/依赖审计，不将评估当独立复测。

### NNDC193Bi evaluation：实际数据crosswalk与weak-line反证

[评估来源前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/evaluation-before-source-recall.md)先于数据打开。旧NNDC接口404、IAEA403后，解析NNDC实际form取得193083001/193083004两个官方ENSDF对象（827/819行，201709；ADOPTED有2019ERR）。SHA/version/POST参数与精确locators固化到[[nndc-2017-193bi-level-scheme-evaluation]]；raw保持不变，文本临时保存，raw槽仅reserved/unpopulated。NDS381页论文未全读，实际范围为selected data-object audit。

代码 `system/scripts/day14_ensdf_crosswalk.py` 实际exit0，79/79 identity/column/RI/weak-line/SD/条件branch检查通过。五level为605.53(18)、928.93(21)、1228.13(21)、1555.30(25)、1875.1(3)keV；原七γ中心值一致，reaction RI为原表0.1倍，selected adopted母态又重标强线100。N193-2/3明确采用2015He27并least-squares/quadrature处理；它验证评价规则，未给jointΣ，也不是独立复测。

最实质的反证：N193-5的393/394只列Q，明确shared negativePOL与placement-implied(E2)不一致，order未established；N193-6的352.3 multipolarity留空，评论原Table I(13/2−)→(11/2−)/M1与Figure2在1610的15/2−冲突。已视觉回看PDF p.9与p.7，新增primarysource HE15-15；若Figure2 ΔI=2，M1被single-photon triangle排除，但不能据此选出最终spin。原source的tentative标签与needs_review不清除。

N193-7取得的是pure-multipole BrIcc/Frozen-Orbitals CC，更新“ICC完全缺失”的边界：计算值有了，δ/branch completeness/parentτ仍未给。在两已报告channel的条件模型中，三母态的M1photon fractions为0.5142/0.5276/0.4416，含conversion的M1conditional branches为0.7543/0.7206/0.6138，不是实测totalbranch或absoluteB。N193-8把bandhead153-ns引用定位到604.7γ(t)/2004Ni06，compiler flight/intensity摘要不替代Ni04完整方法。N193-9保留14个X表达式与unplaced1836candidate。

Canonical知识已写回source、method及thesis matrix；[[level-scheme-reconstruction]]保存完整matrix、公式、normalization和赋值冲突。最高信息路线仍是解除这些具体未定约束，不以重复query或更多校准位数判结构。

### Checkpoint001送达后：shared POL 与joint hypothesis

同session实际收到clockcheckpoint001并在run.json.observed_clock_executions保存clock_event_id/same_session_id/observed_at；原queued20:56时间与实际ack22:04分开，不新建session/daemon。Run仍running、day14、原次日15:00截止；不因卡完成停止。

[计算前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-polarization-before-calculation.md)先于本段model。重核RB原图printed316/PDF11 Eq3.24与polarization/WE paragraph，rawhash一致；不是重读全部42页。`system/scripts/day14_shared_polarization_limits.py` 70项均通过，独立vector-gradient与Wigner/helicity kernels一致、convexcount恒等式、isotropy/normalization、LP必要域与核CG案例验证。

共享A按校正counts正权重混合，negative mean不能指定哪条line磁性，但可限制joint positivity；a(E)在.6keV的近邻差仅使floor约−1.484×10⁻5。若固定rawratio而仅重标a将mean推到0，需要增加16.45%；这不是sourcecalibration错误或新significance。

PureE2在合法取向下可negative P；在本段common selection/轴对称/point response/fixed Q_sens下，同时施加Rexp≈1.26后，pureE2 outer set的A为+.03325到+.09507，mean−.076位于外侧。2×printed-error box无解、3×有解都是sensitivity ranges，不是joint CI。分别改变有效选择能匹配两个单变量，hypothetical M2也能在松弛CG模型中匹配joint mean，但需opposite parity，未给任何line的新M2/Jπ。

[必要域图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-E2-response-region.svg)经PNG视觉检查，标签/边界可读；[完整结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-polarization-limits.json)。Canonical落点为[[linear-polarization-asymmetry]]“未分峰偏振的联合命题与选择条件”及[[level-scheme-reconstruction]]“Shared POL 对joint命题的条件约束”。Actual beam/gate/geometry/Σ仍缺，NDS的Q及所有review flags保留。

## Open questions and belief revision

1. 哪个旁路、time/tag或独立spin anchor能裁决393/394的顺序？重复同一能量和不能裁决。
2. 真实response/净计数能否分别识别299.2/299.8、622/626和323 quadruplet？现有绘图不能补出逐门Σ。
3. 哪些parent τ/branch/ICC/δ输入足以把七条线的相对量接到absolute strengths？153-ns引用不能挪用。
4. 1836-keV候选link的endpoint、强度与false-link控制能否闭合X？当前保持未confirmed。
5. 哪些reference/feeding观测足以约束target conditional population？逐层重设同σ/J可能带入额外prior；需原始实测对照。
6. 对实际393/394是否存在同rank pure stretched/共同response的交换对称条件？若成立，角数据本身不提供order；若不成立，需先定位失效的具体premise。

这些是Codex后续研究路线，不自动转成用户待办。认识修订发生在方法充分性上，未改变结构模式排序。

## L0–L4 state

- L0：anchor原文20页主线、Figure2/Table I及表注、校准/isomer/SD已正式复核；另Zobel1983六页主线/图表/公式/统计边界视觉核验。
- L1/L2：source/method/matrix互链、35项有条件表格/反例练习、六维周考和认识修正已固化。
- L3：line identity/ordering的有界判别问题active；当前最高信息路线是conditional gate与branch/time设计，不把counterfactual当实验。
- L4：真实event-level重分析not-ready；缺事件、response、joint covariance、执行sorter/门接受度及相关parent τ/δ。其缺失不终止其它有价值学习路线。

## Verification and continuation

首次写科学内容前boundary exit0、无error/warning；H1 preflight exit0，protected Bib基线匹配；EOL清理exit0、未触碰substantive/staged内容。raw PDF哈希与source一致，原raw/PLAN/Bib保持只读。定量脚本实际exit0，35/35。

本checkpoint实际验收：report/card/writeback均valid；wiki_lint --fail-on error exit0，0 errors/128 warnings（107既有citation key、18既有未填raw槽、3reaction parser）；git diff --check exit0；protected PLAN/Bib哈希与raw全树size/mtime均匹配基线。第一次lint exit1因inline矩阵被识别成wikilink，已改为无歧义的行列记法并回归。Gitee实际结果仅run receipt；本段内容通过验收后按显式manifest发布。恢复提示已保存[continuation-prompt](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/continuation-prompt.md)。本报告不是研究收束声明；研究截止保持原receipt，不因卡片或一个来源完成提前结束。

当前快照 2026-10-14T19:35:55.416781+08:00，距原截止1164.1分钟；下一日prompt已准备入口、未创建新session/未计Day15。QMD/overview本次deferred，未扩大维护范围。下一步：刷新clock/候选池，完成同一问题的conditional gate、composite-response与最小branch/time设计；若当前问题局部饱和，再查恰好下一张Day15作无学分预习。任何正式Day15学分留待其独立日run，Day16不打开。

### Checkpoint 002 实测与续接

2026-10-14T21:26:21.851052+08:00；距原截止1053.6分钟，research/goal仍active。35/37/79检查三段均exit0；本段lint exit0（0errors/129warnings：107citation key、19raw slot、3reaction parser），新slot为未归档的公开NNDC对象；首次新source缺Summary/Extracted Pages已补齐并回归。report/card/writeback8items/5pages与protected/rawmetadata通过；diff验收随后同batch记录。

本段知识增量是conditional gate/shared-count/低能γ功效与实际NNDCversion/assignment/ICC crosswalk，未给新spin、absoluteB或mode结论。Checkpoint001已Gitee发布，当前批次稳定subject为 `Audit DAY14 evaluated assignments and conditional branch gates`；exacthash/actualpush仅runreceipt。Clockcheckpoint001只验证queued，未冒称delivery。下一高信息currentroute：shared negativePOL能约束哪种joint(E2,E2)命题及其calibration/weight/geometry边界；之后刷新候选池，若饱和再读恰好Day15无学分预习。Day15未计卡，Day16未打开。

### Candidate-pool refresh：恰好Day15无学分预习

当前sharedPOL模型/反例已固化，仍有决定性缺口为实际matchedgate/acceptance/Σ而不是更多同公式重算。下一未完成cardDay15的ADO/角分布/几何修正是剩余高信息route，已在打开source前保存preview recall，标明priming；这里只列partial15，不计Day15、不创建formal audit、不越过Day15或打开Day16。下一核Zheng2002原定义和公开角度/效率练习，保持今天day14。


### Checkpoint003 实测与继续

2026-10-15 00:02 Asia/Shanghai快照距原截止897.4分钟，仍继续同run/session。本批次70/28项分析均通过；report/card/writeback重验valid，唯一writeback13items/8份本run修改知识页。wiki_lint --fail-on error实际exit0、0errors/129warnings（107citation key、19未归档raw槽、3reaction parser）；git diff --check实际exit0；AST、原review flags、raw/PLAN/Bib核验通过。writeback初次失败因method只写RB claim而未直接链接source；已补RB与Herzáň回链并回归。EOL exit1仅保留4项本run substantive knowledge edits，unsafe/mixed0。

本批次稳定指针 main / `Bound DAY14 shared polarization and ADO response assumptions`；精确hash与实际Gitee结果记录在runreceipt。恢复点[checkpoint003](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-003.md)及continuation已存在。正式21/24不变，Day15仅partial预习；下一current route为conditional γγ joint response、matched gate与finite acceptance，实际193Bi事件重拟合仍not-ready。

暂存门首次发现Matplotlib SVG尾空格，未commit；已在两份export函数去尾空格、固定SVG hash salt并去掉动态date，重执行70/28检查均exit0，数值保持。之后重新验cached diff。


### Checkpoint004 实测与继续

2026-10-15 00:35 Asia/Shanghai，距原截止865.0分钟；research仍active。conditional-response脚本35/35、exit0；report/card/writeback15items/10份本run修改知识页valid。wiki_lint --fail-on error exit0、0errors/129warnings（107citation key、19raw slots、3reaction parser）；git diff --check exit0；AST/protected/raw metadata及原review flags通过。原source仅局部回核所用公式，不重复宣称新全文阅读。

上批次已Gitee发布；本批次稳定指针 main / `Derive DAY14 conditional gamma coincidence response`，实际H3/hash仅receipt。恢复见[checkpoint004](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-004.md)和continuation。下一current为general-spin近邻双线排序可识别性，计算前回忆已保存；不计Day15、不停止整段时窗。


### Checkpoint005 实测与候选池重建

2026-10-15 01:09 Asia/Shanghai，距原截止830.7分钟，仍有substantive window。order脚本实际exit0、51项通过；report/card/writeback17items/10份本run修改知识页valid。wiki_lint --fail-on error exit0、0errors/129warnings（107citekey、19raw槽、3parser）；git diff --check exit0；AST/protected/raw metadata/旧review flags通过。

本批次稳定指针 main / `Test DAY14 doublet angular-order identifiability`，实际publication/hash仅runreceipt。当前模型定理局部饱和但没有结束时窗；近期fingerprint显示Ionescu1981已在10月12日Day11/12使用，暂缓重复，Zobel1983尚未见recent daily/weekly记录。下一Day15无学分知识预习候选为experimental alignment/reference transfer，仍需source-before recall、raw/metadata及主线验证。恢复见[checkpoint005](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-005.md)。


### Checkpoint006 实测与持续研究

2026-10-15 02:57 Asia/Shanghai，距原截止722.0分钟。38项worksheet/图throughpipeline实际exit0，report/card/writeback19items/11份本run修改知识页valid；wiki_lint --fail-on error exit0、0errors/129warnings（107citekey、19rawslots、3parser）；git diff --check exit0；AST/protected/rawmetadata/继承Review及new11–14 true通过。

Figure源/glyph/collision audits均exit0，最小8pt、collision0fail0warn，singlepanel对齐not applicable、PNG视觉通过；源3个export/width warnings已按140×110mm Wiki/vector/400dpi合同逐项核。原文Pubfit、作者解释与自设模型保持分层。原人审不扩到新增claim；正式21/24与partial15保持。

本批稳定指针 main / `Audit DAY14 empirical alignment and covariance limits`；actualH3/hash仅runreceipt。恢复点[checkpoint006](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-006.md)。下一bounded route是angular-fit geometry/normalization怎样影响Cov以及两个marginalerrors不能唯一指定哪些joint判断；需先冻结预测并声明chosen design，不能补出作者GF矩阵。研究未收束，不因一篇source或图完成结束时窗。


### Checkpoint007 实测与继续

2026-10-15 04:19 Asia/Shanghai，距原截止640.9分钟；researchactive。26-check covariance-design实际exit0，report/card/writeback20items/11份本run修改知识页valid；wiki_lint --fail-on error exit0、0errors/129warnings（107citekey、19rawslots、3parser）；git diff --check exit0；AST/protected/rawmetadata/继承Review及new11–15true通过。

本批稳定指针 main / `Demonstrate DAY14 angular covariance identifiability limits`，actualpublication/hash仅receipt。恢复见[checkpoint007](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-007.md)；下一核remaining Day15 coefficient conventions及必要统计source，先查overlap，不重复同prototype换值充填，不计Day15、不打开下一卡。
