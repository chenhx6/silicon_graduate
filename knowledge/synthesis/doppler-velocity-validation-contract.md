---
type: synthesis
title: "Doppler correction 的速度信息与最小验证契约"
aliases: [Doppler velocity validation contract, 反冲校正验证契约]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
scope: doppler-recoil-vector-response-validation
confidence: medium
sources: [mavela-2019-32s-quadrupole-moment-doppler-correction-thesis, klemme-1999-lifetimes-134nd-neighbors, vandebrouck-2016-vamos-dual-position-mwpc, crespi-2013-agata-high-energy-doppler-response, aladili-2009-agata-doppler-simulation, akkoyun-2012-agata-instrument-response, senyigit-2014-agata-neutron-rejection, tunl-2017-12c-level-widths, soderstrom-2008-agata-position-design, crespi-2023-agata-tracking-performance, ljungvall-2020-agata-ganil-performance, assie-2021-mugast-agata-vamos, lemasson-2023-agata-vamos-fission-history, ciemala-2019-20o-dsam-analysis-status, ziliani-2019-agata-calibration-controls, ciemala-2020-c16-o20-lifetimes, zanon-2023-o20-high-precision, ciemala-2021-deep-inelastic-lifetime-method, baker-cousins-1984-histogram-fits, nptool-2019-reaction-velocity-code-object]
tags: [doppler-correction, velocity-information, calibration, covariance, evidence-contract]
---

# Doppler 速度信息的最小验证契约

## Question and Scope

怎样证明某条校正γ的energy/line shape/selected intensity能用于后续level或strength分析？本页给出跨source的方法契约，详细公式与可运行检验在 [[doppler-correction]] 与 [[tracking-array]]。契约不是本run已经通过的实际实验validation，也不判定wobbling/chirality/shape或新的absoluteB。

## Evidence Matrix

### 实际观测、解释与模型各自支持什么

| Source与locator | 原报告 / 模型对象 | 支持的判断 | 不能由此补齐 |
|---|---|---|---|
| [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-27/28 | Exact式与总校正谱、不同emitter yield输入。 | γ–projectile angle与速度stage必须声明。 | executed sorter/ring covariance、printed9%/7%差异的真实执行影响。 |
| [[klemme-1999-lifetimes-134nd-neighbors]] KL99-4/18 | 同跃迁随distance出现shifted/unshifted分量；finite stopping correction。 | 双峰或宽线可包含速度历史。 | 将两分量直接当两新levels、以单初始β消除stopping/feeding。 |
| [[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3 | same-data98Zr width8.6→5.5keV。 | independent particle vector/vertex信息可以改善Doppler。 | 所有energy/位置的PSAσ、全covariance或实验独立重复。 |
| [[crespi-2013-agata-high-energy-doppler-response]] CR13-2/3 | 同谱meanvector优化，PSA/segment119/122keV。 | firstpoint改善仍受未测eventvector限制。 | 把最窄same-line fit当独立speed测量或移植ordering最优。 |
| [[ljungvall-2020-agata-ganil-performance]] LG20-7/8/14 | VAMOSvector与simulated energy-dependent IP response对接；平均position5.1mm。 | measured vector与matched response/template可约束position。 | 一点平均FWHM代每eventσ、未知响应/selection/target history。 |
| [[assie-2021-mugast-agata-vamos]] AS21-17/8/9/10 | lightparticle two-body10.2→7.1keV；integerPID/rigidity/pathTOF，Au-backing边界。 | 除heavytrack之外，light-ejectile也提供recoil信息。 | wrongchannel/PID、unknownbeam/target/loss或γ之前的feeding recoil。 |
| [[senyigit-2014-agata-neutron-rejection]] SY14-2/4/6/9 | detector-neutron bumps、γTOF与cut-stage/predicate冲突。 | origin identity与execution stage影响γ候选。 | γTOFtag自动属于target、只用threshold摘要重现productioncuts。 |
| [[tunl-2017-12c-level-widths]] T12C-1/2/3 | evaluated total/partialwidths与分母。 | levelΓ、γpartial、line gap/photon frame是不同输入。 | 把观测keVFWHM当naturalΓ或将评价编译算另一velocity实验。 |

表中数字是各source的report，不是本任务重新测量；authors对floor/finite-stopping/target的解释、原simulation和任务条件推导分开保留。实际measurement、model-template interpolation与一般物理公式不得合成“直接实验验证”一句话。

## Synthesis

### 输入—过程—检查—失败条件

| 检查对象 | 最小输入 | 独立或互补检查 | 会推翻当前解释的结果 |
|---|---|---|---|
| photon/level identity | raw/各emitter-corrected谱，PID/channel、γγ/particle gates、background与line locators。 | 停止distance/time、互斥branch/feeding和material line控制。 | 两components有不同coincidence identity，或同一line随stopping改变，原single-level解需重审。 |
| velocity与emission stage | particle vectors/TOF/rigidity或light完整momentum，beam/target/loss、A/q与γhistory。 | measured independent particle、known-rest line/非共平面directions、two-body closure。 | knownbeam/missingmass与forcedentry不相容，或alternatevector/PID仍同样符合。 |
| coordinate/frame | vertex、γfirst-IP、particle/beam axes、长度/角单位与执行transform。 | rotation/origin consistency、promptvertex、零nuisance roundtrip。 | 同一frame的transform不保持相对angle，或lab Compton被restenergy预缩放后破坏。 |
| covariance与precision | 直接raw-inputΣ或明确derived-coordinate转换，σ/FWHM及fit窗口。 | FD/MC/极限、held-outgeometry/energy、matched静止response。 | 方差预算依赖重复计入θ误差、zeroJacobian被当全误差零、mixture tails与simpleGaussian不相容。 |
| selected shape/intensity | cuts/FOM/threshold执行stage、unselected/selectedcounts、ε/rate、normalizer。 | fixedgate scan、conditional likelihood与joint pair-response，held-out tests。 | 最窄peak仅由truncation造成，normalizer遗漏pairloss，或samecounts可由不同ε/Z/N0解释。 |
| inference到τ/B/结构 | 以上身份/response通过，再有feeding/stopping、branch/ICC/δ、lifetime/绝对normalization。 | 同母态闭合及独立companion observables。 | 缺beam/current、branch/response或data packet时，narrowpeak不能补出absolute strength。 |

这是一组可检验设计，不声明已拿到实际packet。[[akkoyun-2012-agata-instrument-response]] AK12-7与LG20-1强调rawtraces和postPSA points的replay范围不同；最终tracked谱不能重新提供缺失PSA输入。[[soderstrom-2008-agata-position-design]] SD08-5/6的two-distance思路也须保留commonbaseline/真实first-IP geometry，原printedEq.(4.4)不静默替换。

## 最容易误用的量

| 容易合并的对象 | 正确保留的区别 |
|---|---|
| beam / postreaction / γemitter / terminal residue β | 按真实emissions/material crossings定义各stage；源particlevector的独立性与阶段要同时检查。 |
| scalarβ / completevector | knownspeed和两coplanarprojections可有globalmirrors；localfullrank不保证唯一。 |
| naturalΓ / Gaussianσ / fittedFWHM / mixturehalfheight | Lorentz无finitevariance；kernel/fit/窗口与不同width对象各自定义。 |
| OFT σθ / angularσθ / IP FWHM | C23-4、LG20-2中前者单位cm；后两者为rad或mm并需energy/depth/geometry条件。 |
| correct peakenergy / correct trackingselection | 改变detector-lab Compton inputs可破坏FOM，即便energy和随后被校正正确。 |
| independent events / isotropic normalizer | Commonbeam-axis marginal shape仍可造成cross-event angle structure（LG20-12），且tracking后混合遗漏joint response。 |
| normalizedtransparency / absoluteefficiency / P-T | AS21-7的1.4MeV归一比较丢掉absolutescale；P-T升高可伴FEP loss（AK12-6、LG20-4）。 |

这些方法反例都在 [[doppler-correction]] / [[tracking-array]] 中用声明的参数、代码与analytic/MC/invariant检验保存。成功运行toy只验证指定模型和数值，不验证某实验的productionidentity/response。

## Independence and Shared Data

- Originalarticle、thesis、review、表/图/不同gate及same-event algorithm replay要标source lineage。C23重述CR13/SY14/LG20/AS21，不增加acquisition数。
- VD16与LG20同设施/98Zr数据无runmanifest时不默认独立；source/beam/geometry的互补检查仍可能共享PSA/basis/calibration。
- Held-out events可以检查随机过拟合，共有coordinate/gain/line identity的systematic可能一起通过。需要held-out line/energy/geometry或independentparticle输入来增加不同约束。
- Derived宽度/分支、up/downrate、混合eventnormalizer及多个normalizedgates共享输入；没有covariance不制造独立errorbar或提高显著性。

## Knowledge Impact and Learning Decision

`supports` 多种recoil/vertex/γresponse观测的互补性；`revises` 窄峰、PID/TOF或局部fit可单独证明完整velocity/response的判断；`limits` 从method benchmark直接进入absoluteB/collective-mode结论。

Readiness：source/locator与有边界L2/L3方法审计可做；本run实验L4仍缺productionevents/code/calibration、target/backing/history、response/normalization与jointcovariance。这个缺口由研究者持续追踪，不自动转成用户上传或审核待办。

### 统计与速度分析之后的判定表

| 被检验的充分性说法 | 现有证据支持的判定 | 实际分析还须怎样区分 |
|---|---|---|
| 精确Lorentz变换且correctedpeak窄，就验证了全部速度 | 变换可正确而reference粒子/stage、输入producer、角度或history仍不同；宽度与局部rank有已声明的非唯一反例。 | 独立state-conditioned kinematics、frame/epoch/caller binding及不同角度/line controls。 |
| 采用正确Poisson统计量就得到正确τ/E区间 | 只有forwardfamily/domain/nuisance/selection正确时才适用；已声明模型的错误入口β、boundaries和不可识别极限改变coverage。 | 原counts/edges/rebin、全nuisance与model alternatives、joint/profile定义和完整pseudoexperiments。 |
| 多角度、共用背景或多个replay可以直接相加独立信息 | 必须按eventmarks/总数设计/sharedoff/templatebank记录依赖；联合粗分区可改善summary，不增加raw事件。 | eventIDs/weights/overlap与on/off/MC的实际观测关系。 |
| 长line晚速度匹配就独立验证入口history | Source支持aftertargetreference校准，tuning幅度不等σβ；finitehistory、objective/window、vertex和parent/residue frame另有条件。 | 外部anchors/τ及Σ、实际拟合窗口/response、速度stage、entry/depth/stopping数据。 |
| 这些验证已解释20O两次τ差异或建立A≈130结构结论 | 没有。Primary实验与model值、任务counterexamples分层；150/70fs差异原因、目标核mode排序与absoluteB均未裁决。 | 取得可复现experimentalpacket后检验竞争解释，保持transition-bound τ/branch/δ与source谱系。 |

判定表汇总本页已有BC84-1/2/4/5/9、CM21-15/16/17/22、ZA23-2/7/10和其他source语境；它是synthesis，不增加实验复测。可复用的新认识是验证须分成observable/caller、physicalhistory/response、统计观测模型和decision/coverage各条证据链。合成closure只改变对“充分性”的判断，不确定actualpipeline发生同样失败，也不把十个练习计成十份独立证据。

## Open Questions

真实packet如何记录independentparticle与PSA共享vertex/angle covariance？是否有跨geometry/energy且保留unselectedstages的replay可验证transfer？在正确channel/feeding身份下，哪些centroid/line-shape/selection变化仍需要真实velocity history？这些问题服务 [[a130-thesis-evidence-matrix]]，不提高当前mode证据等级。

## Counter-evidence

KL99-18的same-transition停止分量、SY14-2/4的detector-origin线、CR13-3的velocityfloor、LG20-10的jointresponse和AS21-11的absolute normalization缺口分别限制不同推断。它们不是同一种失败，也不能互相移植nuisance数值。Expected-but-absent的companion只有在matched sensitivity/acceptance下才构成反证。

## Model Dependence

Exact Lorentz/four-momentum公式依frame/particle identity与适用的free/constantvelocity模型；Gaussian Jacobian/quadrature、Lorentz mass-profile、proper-time/geometry、response mixture与fixed selection likelihood各有独立假设。Knownspeed的globalmirrors、wrongentry/PID modes等任务counterexamples只否定所声明的充分性，不判actualsource发生了相应错误。原SD08 printedformula、AA09sourcecode和Mavela执行版本等缺口都保留。

## Confidence Notes

本页medium表示有多个source和经过相称self-audit的方法边界；不代表实验L4、source原始review状态或structure信心水平。表中的reportnumbers有directlocator，transfer/validation设计是synthesis/our-inference；未接受user科学裁决，不记human-reviewed。

## Limitations and Missing Evidence

所有新publiccopy保留URL/version/hash与未归档raw边界。Actualproductionevents、basis/code、reactiondepth/backing、line/entrypoint、PID/confusion、response/normalization与jointcovariance没有完整取得；publishedsource的例图/宽度和toychecks不补出这些输入。正式paperclaim需回原文与对应review/citation状态。

## Agent self-audit triage

P0: none identified。未建立新的structure/absolute-strength结论；sourceidentity与raw缺口、targetlabel/printed/version冲突已隔离，未把其作为确定输入。

| ID / priority | 实际判断与依据 | Source locator / 任务inference | 重要性、后续核验目的与不核验风险 | 结果 |
|---|---|---|---|---|
| DVV-P1-1 | 实测width改善、model interpolation、作者floor解释和方法契约分别列。 | VD16-3、CR13-2/3、LG20-7/8/14、AS21-8；contract为synthesis。 | 后续声称velocity/position校准时回matchedraw/conditions；否则把same-line fit或template当独立truth。 | self-audit complete within stated scope；actual packet仍缺。 |
| DVV-P1-2 | Variance/Γ/FWHM、derivedθ与rawΣ、globalmodes、selectionnormalizer的条件显式。 | C23-4/8/15、SD08-5/6、LG20-10/12、SY14-6/9及canonical method exercises。 | 复用定量公式时核单位、frame、kernel、executionstage；否则可能重复误差、误用normalizer或把localfit当唯一解。 | 条件公式/验证已核，unreviewed不升为human。 |
| DVV-P1-3 | Source/review和同run多gate共享数据；missingpacket不补absoluteB。 | AS21-17/11/12、AK12-7、LG20-1、T12C-2/3；lineage table与readiness。 | 正式科研使用需核normalization/response/dataidentity，防止重复证据计数或超出数据支持。 | 保留需要数据才能完成的边界，不制造用户待办。 |

P2/P3：导航/anchor关系按本run writeback检查；不改变source/claim review flags或课程学分。

## History-specific update

[[lemasson-2023-agata-vamos-fission-history]] LS23-5/6/8/11细化angularcomparison、post-degrader U/S与FPdelayedhistory；[[ciemala-2019-20o-dsam-analysis-status]] CO19-3/6/9/13明确sharedRF/energy/PID校准、jointτ/Eγ和preliminaryno-final-result。它们补充上述contract，不把方法benchmark、modelpredictions或historyselection变成新测量/absoluteB。

## 20O 独立实验对照的验证路线

[[ciemala-2020-c16-o20-lifetimes]] CI20-1/2/3/5/6/7/8 与 [[zanon-2023-o20-high-precision]] ZA23-1/2/3/5/7/9/10支持一个具体L3 comparison：20O2+2两次独立采集的总τ150fs/70fs有数值张力，作者并未完全解释来源。旧实验初速度迭代重建、新实验particle-assisted初速度和Ex selection为不同nuisance约束；同样需要stopping、transport、response、restenergy/τ jointfit与feeding leak检查。

验证顺序：先统一total/partialτ与confidence定义，再定位input/correction/emission/exit velocities；核entry/gate/feeding，随后以独立energyanchor、held-outline/angle及多个transport条件做jointprofile。2023SI的1156keV3+1→2+2 branch28%不等目标samplefeedfraction；长2+1line的Au-loss correction说明其benchmark convention，不能自动替所有short-state production fields。

反证要求：若已量化的Ex迁移/feeding上界不足以产生差异，feeding候选被削弱；若测得entryvelocity与旧重建在共同条件/Σ内一致，初velocity候选被削弱；若restenergy/response constraints变化仍稳定保留差异，则不能让它们无限吸收τ。上述为本任务design，不是已经完成的实验反证。

`our-inference`：2394.6±1.0与2396.1(.2)keV的能量区别、τ–Eγ covariance可能影响两τ比较，原χ²/template未得，不判因果。3+分支strength的USDBδ输入以及旧partial190fs与新total70fs的区别须延续到所有结构/模型比较。L4experimentalrefit仍not-ready，不pool、不报精准Gaussianσ。

## 方法version、cumulative lifetime 与不重复的校验

[[ciemala-2021-deep-inelastic-lifetime-method]]的preprintCM21-4和正式CM21-14/15直接对照：正式版formula/label一致、reference为aftertargetvelocity，并写DC材料pathcorrection/T按Zfine-tune。初速度展开使用100targetlayers、2MeVTKEL、acceptedangle/TOFresponse；它补齐source方法定义，production参数/Σ与代码仍未得。不同版本只是一条同2017data的方法链，不计新independentexperiment。

CM21-17/18的final80%totalerror和cumulativelifetime说明使“给出τ就是纯态寿命且误差可直接Gaussianpool”不成立。作者从absencefeedingγ解释negligible的范围保留，需要detectorε/threshold/population才变成严格f上界。ZA23新1156feeder与Ex门控制提供另一约束；reactionpopulation不同，不能把其branch或漏门率移植给2017样本。

CM21-16的Mgenergyanchor由PARISNaI neutronactivation/24Naβdecay产生，不能标成Eu本体branch；sourcegating/energyorigin与per-sourceactivitynormalization仍不同。CM21-20的articleCC-BY4.0与AGATAdataownership分开；ZA23-15的注册license/embargodate虽已核实，GANILlanding网络失败，未取得events文件清单，不臆测权限拒绝或宣称L4 ready。

## 统计定义不能由峰图补齐

[[baker-cousins-1984-histogram-fits]] BC84-1/2/3/4/5/6/7/9支持将bin积分、Poisson或fixedN、统计量/normalization与point/interval/GOF分开。ZA23-10的Neyman/observed10规则和CM21-17的final80%totalerrors保留其source定义；不能自动换成统一Gaussianσ、保证unbiasedτ/E或从χ²minimum alone宣称validatedhistory。

自设uniformrate反例/regularGaussian区域已写[[doppler-correction]]并有脚本/MC：allbins≥10仍有Neymanratebias，joint68%/τprojection约87%不同。这些只约束过强method假设，不证明sourceτ方向/显著性或转换它的errors。需要rawcounts/background/bin/template/Σ与confidenceconstruction才能做actualrefit；samepipeline输出的几种fitstatistic不是独立实验。

## Entry history 的可解析竞争者

CM21-18与ZA23-2/3/5/7所需的feeding/entry边界在[[doppler-correction]]“同一发射等待分布不唯一对应目标态寿命”有一项任务反例：τl<τeff、上态τeff、直接r=τl/τeff和feeding1−r使目标γproperwaiting恰为Expτeff。共同transport/response下，同一目标γ多角/全shape也不区分两个固有τ；这不是source已报告的feeder参数。

所需反证是独立entry/feeder信息，或证明共同K假设失效的recoil/multiplicity/trigger响应。自设120/60fs/50%与600kMC/analyticclosure仅证明有限模型的非唯一性，未解释真实150/70fs。来源已知54fs上态/28%branch不等该构造；knownentryhistory可排除竞争者，actualL4仍需packet。

## 共同K的物理边界也要量化

目标态/upperphotonrecoil、transport、alignment/角关联或selection改变时，共同K的exactfeeding反例条件不成立。[[doppler-correction]]的cascade-recoil练习用自设two-bodymassproxy/constantflight及isotropic角分布检验这一边界；A20/gap1MeV使50%feed/σ2keV模型的σ变2.000689keV，未知Gaussianresponse可吸收多数差异。Model的KL/MC非实际τdiscrepancy/实验precision，不能从“物理上打破理想恒等式”跳到“source已可辨识feeding”；独立tag/entry和响应约束仍须核。

## Depth prior 与末速度各自约束什么

CM21-6/7/19/21提供sourceTKEL/靶depth/TOF和实际倾斜geometry，ZA23-2则有particle-assistedentry约束。[[doppler-correction]]的自设equal-effective-S/collinear极限使相同末能量不区分三depthprior，错uniformprior可偏移toyτ/E；fullshape残余KL或不同S/path可反证错prior。ActualCM21geometry不满足其共线假设，故不能用toy证明该实验bias。

必要packet是state-conditioned exitdata、reaction/TKEL/depthprior的版本/依据、materials/path/response与covariance，以及独立entry或geometry/stoppingcontrastcontrols。多份同末速度的重放/fit不构成新的independententrymeasurement；反之，可靠physicalprior也是有效输入，应按来源/范围明确而不统称“未测就无法使用”。

## Code object、caller与测量binding

[[nptool-2019-reaction-velocity-code-object]] NP19-1–12只证明固定2019publicobject的单位/producer/getter/mass/frame；GitLab当前代码与experimentcaller未取得。ZA23-2的particle-assistedentry有measuredlightinput基础，仍须beam/mass/vertex/energycorrection/φ和实际operator binding。

GetVelocity/TOF/Bρ等同input派生字段，不因值相符增加independentmeasurement。Reaction4vector/Nucleus缓存和Mass含Exc须一致或明确不同估计器；physicaldomain与branch/radian/totalMeV不能由framework名保证。Sanity数值是任务counterfactual，不推断source发生mass/unitsbug。Read-only对象审计可提高L3contract，不能替actualL4dataset/code/Σ。

## Histogram 输入与独立性

BC84-2 的 bin 积分定义已在 [[doppler-correction]]“有限能量 bin：积分、边界与重分 bin”作合成检验。正确连续核仍可因中点近似给不同 τ/E；精确积分恢复自设真值，而粗 bin 的局部信息量降低。相同事件的不同 binning 是依赖检查，不能叠加为独立实验或额外统计量。

必要输入包括完整 bin edges、rebin 规则、固定 ROI、条件或 extended normalization、原始 on/off 计数、共用背景与有限模板的来源/协方差。上述局部 Fisher 数值不重算 ZA23/CI20/CM21 区间；缺少这些输入时，实际实验重拟合仍 not-ready。

[[doppler-correction]]“共用背景观测如何连接 bin 与角度组”给出本任务的 on/off 推导和独立计数检验：共享一个背景归一化观测可产生 rank-one 交叉项，扣除后的 bin 不是独立 Poisson。共同误差在差分中也可抵消，因此须按实际估计器和观测关系传播。局部 joint-Poisson/GLS 等价不证明有限样本区间 coverage；背景 shape、transfer 与原实验共享事件仍需单独核验。

同页“有限模板与共同模拟事件的协方差”区分单模板误差和共用事件的模板差误差。必要 packet 还包括 generated/selected counts、权重、参数 bank 的共同 event IDs/seeds、归一化约束及 data/MC 依赖。共同随机数可使差值稳定，却不增加独立事件数；leading 1/N covariance、局部 score 投影和 ensemble 检查也不替代实际寿命 coverage。

同页“自适应 bin 边界也是观测的一部分”进一步要求保留细 bin 计数与选择算法。若边界由同一数据选择，忽略其参数依赖可改变观测模型；“输出均≥10”不是这个问题的充分控制。该两 bin 反例有明确合并规则，未取得的 ZA23 production rebin 不能由它替代。

同页“共享事件、总计数设计与重放的信息”进一步区分 Poisson thinning、fixed-N 约束和重叠 gates。确定性 replay 的统计量相关；不同粗分区联合可恢复部分分辨信息，因此不能把“非独立”扩大为“任何粗 summary 联合都无收益”。必要输入是 raw-event/共同样本身份、ROI、映射和 event marks，真实多光子/背景 covariance 另核。

同页“非线性 τ/E 区域：有限计数、边界与不可识别极限”将局部 covariance 与 region coverage 分开检验。自设20fs边界、无减速寿命零信息、fixed-N nonlinear fits均有明确 domain、seed/hash、optimizer失败和恢复记录；这些不是源论文的 nuisance 或区间。必要 packet 还需实际参数 domain、可识别性和完整算法的 coverage 检查。

“速度 nuisance：正确统计量仍须正确的 forward model”与其同数据semantic audit说明，错固定入口β可影响 E0和τ，但联合真值、τ profile和joint-region投影必须分开。独立Gaussianβ观测的正确family closure不证明实际velocity tag无偏/独立、stage正确或全部physicalnuisance已知。

CM21-15/16/22的longline调整是after-target T/velocity；0.4%/0.7%是tuning幅度，不是σβ。“长寿命校准线：有限 history 与估计量选择”的条件练习进一步要求保存control τ、reference energy/Σ、拟合objective/窗口、response和stage。整线mean、densitymode和actualfittedpeakcenter不同，late-velocitycontrol不自动成为独立entry/depthmeasurement。

这项calibrator self-audit还检查固定相对角度和reference对象的边界：另行隔离的displacement与free-singleγ parent/daughterframe例子说明，mode也可受vertex影响，另一个速度reference给另一个observable。选择exit/residue reference用于historyfit可以成立，但模型/数据须绑定相同observable；不能把独立fixture的残差相加成source correction。

## Sources

新增 [[ziliani-2019-agata-calibration-controls]] ZL19-2/4/6/7/8/9实际time/energy/historycontrols；与CO19同data。Calibrationwidth、energyanchorprecision、actualcentroidΣ、independentvelocity与absolutephotonintensity仍分开，完整predicate/config/Σ未取得。

具体atomiclocators列在EvidenceMatrix、contract与triage中；sourcepages均有URL/raw或public-copy fingerprint、阅读范围、claim kind与限制。详细公式及代码入口在 [[doppler-correction]]、[[tracking-array]]、[[gamma-gamma-coincidence]]；本页不能替原始文献事实源。

## Evolution Log

2026-10-14：从Day13的峰位/峰宽diagnostics扩展到velocitystage、independentconstraints、globalmodes、frame、linekernel和jointselection的cross-source契约。触发证据为VD16/CR13/LG20/AS21/SY14与声明的任务checks；先前仅固定geometry的width-only问题现加入可检验的观测杠杆与失败条件。Codex完成上述self-audit，owningmethods保留数学/参数；actualexperimentvalidation和未取得production身份继续partial，不提高A≈130mode排序。
