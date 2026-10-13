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
sources: [mavela-2019-32s-quadrupole-moment-doppler-correction-thesis, klemme-1999-lifetimes-134nd-neighbors, vandebrouck-2016-vamos-dual-position-mwpc, crespi-2013-agata-high-energy-doppler-response, aladili-2009-agata-doppler-simulation, akkoyun-2012-agata-instrument-response, senyigit-2014-agata-neutron-rejection, tunl-2017-12c-level-widths, soderstrom-2008-agata-position-design, crespi-2023-agata-tracking-performance, ljungvall-2020-agata-ganil-performance, assie-2021-mugast-agata-vamos]
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

## Sources

具体atomiclocators列在EvidenceMatrix、contract与triage中；sourcepages均有URL/raw或public-copy fingerprint、阅读范围、claim kind与限制。详细公式及代码入口在 [[doppler-correction]]、[[tracking-array]]、[[gamma-gamma-coincidence]]；本页不能替原始文献事实源。

## Evolution Log

2026-10-14：从Day13的峰位/峰宽diagnostics扩展到velocitystage、independentconstraints、globalmodes、frame、linekernel和jointselection的cross-source契约。触发证据为VD16/CR13/LG20/AS21/SY14与声明的任务checks；先前仅固定geometry的width-only问题现加入可检验的观测杠杆与失败条件。Codex完成上述self-audit，owningmethods保留数学/参数；actualexperimentvalidation和未取得production身份继续partial，不提高A≈130mode排序。
