---
type: method
title: "γ-ray tracking array analysis"
aliases: [tracking array, gamma-ray tracking array, γ-ray tracking array, GRETINA, AGATA, tracking-array response function]
created: 2026-07-09
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
method_type: gamma-ray-tracking
tags: [gamma-ray-tracking, angular-distribution, angular-correlation, linear-polarization, pado-support]
---

# γ-Ray Tracking Array Analysis

## Purpose

γ-ray tracking arrays use segmented HPGe crystals and tracking algorithms to reconstruct gamma-ray interaction positions and directions. They enable continuous-angle angular correlations, angular distributions and linear-polarization measurements.

## Inputs and Assumptions

- Calibrated segmented HPGe interaction positions and tracking output.
- Energy-, angle- and configuration-matched response functions or event-mixing references.
- Control of clustering holes, tracking halos, finite detector population and Doppler/Lorentz effects when relevant.
- Separate modeling of detector response and nuclear alignment/population assumptions.

## Source-Level Foundation

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] states that tracking arrays such as AGATA and GRETINA can determine photon interaction points with high precision, so conventional detector solid-angle attenuation coefficients can often be close to unity. The same source emphasizes that angular-distribution extraction remains non-trivial because tracking, decomposition, detector tiling and clustering effects create response functions that differ from older ring-detector arrays.

## Key Method Boundary

Tracking arrays can reduce one classical detector-geometry correction, but they do not remove the need to model nuclear alignment, magnetic-substate population, deorientation or feeding history. In Lauritsen 2025, detector solid-angle attenuation and nuclear alignment attenuation are explicitly different uses of `alpha_k`.

## Longfellow 2026 Connection

Longfellow et al. demonstrate a GRETINA in-beam path that orders interaction points by energy, uses event-by-event Doppler correction, and applies the laboratory-frame Lorentz angle transformation before comparing angular distributions and polarization. Their result is a method characterization under stated conditions, not a claim that simple ordering is universally superior to full tracking. See [[lorentz-boost-correction]], [[doppler-correction]] and [[longfellow-2026-gretina-energy-ordering-polarization]].

## Project Relevance

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this page is only an instrumentation/method anchor. It supports the statement that a modern tracking-array formalism still contains explicit `Pm(J)` and `sigma/J` assumptions for in-beam angular distributions; it does not provide a universal `sigma/I` prior.

## What It Can Establish

Tracking arrays can provide continuous-angle angular correlations, angular distributions and linear-polarization observables. With proper response treatment, they can help constrain multipolarity, parity, mixing ratio and alignment assumptions.

## What It Cannot Establish Alone

Tracking-array data do not remove the need for a population/alignment model. They do not by themselves define a transferable `sigma/I` value, and response-function systematics can still affect extracted angular-distribution coefficients.

## Sources

- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]

## Recoil information and high-energy tracking boundary

[[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3的98Zr校正line从8.6(1)降到5.5(1)keV，支持photon first point与独立recoil vector/target vertex的共同重建。[[crespi-2013-agata-high-energy-doppler-response]] CR13-3在另一个15.1MeV实验中将segment122keV改为PSA119keV，作者将剩余floor归于未逐事件测得的12C速度向量。这两个独立例子不能转移数值，但限制“PSA位置精细化足以保证intrinsic resolution”的判断。

Crespi CR13-5/6又展示效率/背景tradeoff：在single15.1MeV、pair-production重要、低background情况下，add-back+PSA+1HitID约为其standard mgt tracking FEP的4倍；而source多γ的neutron-capture sum peak则由tracking抑制。不能将4倍推广到高multiplicity级联、其它能区或算法；fixed peak gate的line身份/centroid/width与efficiency要同时验证。原[[longfellow-2026-gretina-energy-ordering-polarization]]的GRETINA energy-ordering结果保留其setup-specific范围。

## Position validation and selection response

[[akkoyun-2012-agata-instrument-response]] AK12-1/2指出PSA位置依赖basis、noise/cross-talk和多hit，crystaltilt/targetpoint在tracking阶段进入；Fig39的positionFWHM随γenergy变化，不可用一个nominal5mm当所有point的σ。AK12-5的静止60CoComptonimage验证减少recoilnuisance，与beamDopplercheck互补，但PSA/sequence/calibration仍共享。

AK12-6的实际threeATCsource测试中，P/T从16.8%提高至53.9%，tracking/rawFEP保留84.5%；该效率ratio的分母是rawcrystalspectrum，不是所有发射γ。threshold、single-hit拒绝、energy/multiplicity、passivematerial和gate共同定义selection。图表/algorithmreplays与同一sourceacquisition是dependent，不把更干净谱当作更强结构证据。AK12-7的rawtrace/replay链提供更改PSA/geometry/selection后复核的方法；原event未取得，不声称已复算source性能。

## Neutron background and executed cut semantics

[[senyigit-2014-agata-neutron-rejection]] SY14-2/4的Ge-recoildeposits会在γenergy高能侧形成bumps；TOF-labelledγ不自动是目标核，附近材料真γ仍可留在g门。SY14-5/8的count-ratiodenominators与P/T分开，algorithm可能重组clusters，trackingefficiency不直接是binomialprobability。

SY14-6/7定位body/table/conclusion的gatepredicate与Co列label冲突。acceptORgood与rejectORbad不互为补集，sign/equality也不能随意改写；未取得productionmgt/publisherversion和eventreplay前，保留literalconditions和reportedtables，不推荐自动实施某个假定cut。sourceTables2/3/4为同次数据或model比较，重复图/表不新增独立证据。

## Tracking 参数的符号、单位与独立验证

[[crespi-2023-agata-tracking-performance]] C23-4/5 在pp.7–8明确区分OFT调参与实际PSA响应。不同位置出现同一个θ符号，不意味着同一物理量：

| 量 | 单位与对象 | 可用于哪一步 | 不能代替 |
|---|---|---|---|
| Doppler ∆θ/σθ | rad；photon对emitter vector的角误差 | energy Jacobian及joint covariance | OFT自由position参数或PSA的3D response。 |
| OFT名为σθ的自由参数 | cm；用于计算Compton scattered-energy uncertainty的average position parameter | FOM/selection与软件调优 | 一个独立measured angular σ或位置分辨率测量。 |
| PSA position FWHM/σ | mm；须声明energy、segment/depth、方向和分布 | first-IP几何、tracking和响应积分 | 所有能量/点位置的通用5mm。 |
| simulation smear S0 | cm；Eq.(4)按deposit energy缩放的Gaussian假设 | 指定simulation benchmark | 已测event-specific uncertainty。 |

source报告simulation/experimental OFT optimum从.24cm到.8cm、first-vertex weight从2到1；这是指定版本的数据调参context，不意味着PSA已测8mm FWHM，也不适用于其它code或2026版本。source用same-segment point merging、Gaussian smear和ideal/real geometry，现实response会改变FOM分布。

C23-1/2还指出有限Compton-electron轨迹、bound-electron momentum与two-interaction ordering ambiguity使正确/错误FOM重叠。提高PSA precision仍有价值，但最高FOM或最高deposit并不自动是无歧义truth；C23-11对2010 PSA+1HitID的Mγ1、低background与旧pair-production代码条件必须保留。原GRETINA Longfellow实验保持其自身已审核范围。

### Calibration transfer 的最小失败检查

[[soderstrom-2008-agata-position-design]] SD08-5/6 的two-distance idea需要common nuisance与真实first-IP geometry；[[doppler-correction]]保存了平方差推导、third-distance失败检查和negative-p²边界。Static Compton imaging（C23-14）减少recoil nuisance，却仍使用simplified ordering/simulated response，不能称为完全无模型的独立PSA truth。

独立particle vector、source image、held-out line/energy/location与geometry scan分别约束不同项。对同时更改PSA、FOM、threshold、材料和门的重放，应记录各阶段raw/selected spectra、FEP fraction、P-T、尾部和covariance；同一source的training/test split可检查统计过拟合，不能独自排除共享basis/coordinate/line-identity的系统误差。

Material background也可能满足近source方向：C23-6 的PRISMA steel-block例子说明真正scatter路径不能从target-only FOM假定中消失。C23-12的P/T升高附带17% efficiency loss、C23-13对neutron rejection的使用范围，都不能转化为本run已经测定的transfer correction。

C23-15明确把event-specific uncertainty与联合PSA/tracking改进列为尚未证明的建议；它提供可检验研究路线，需要真实packet与held-out验证，不作为既成性能结论。

## 联合接受率、event mixing 与同束轴各向异性

[[ljungvall-2020-agata-ganil-performance]] LG20-10/12 提供直接source-data比较：将uncorrelated **interaction points先混合、再tracking**，与tracking后再混两条独立γ所得normalizer不同。前者可保留两photon靠近时的clustering/PSA损失，后者只包含单photon响应的乘积，不能恢复joint acceptance `S12(n1,n2)`。此结论属于其highpeak/background source与指定OFT版本；同核beam events仍需另核验population/background/occupancy。

### Response-level 定量反例

[day13_event_mixing_acceptance.py](../../system/scripts/day13_event_mixing_acceptance.py)只构造full-sphere、positive smooth pair-acceptance模型，不重放OFT。令true角关联 `W(u)=1+.102P2(u)+.0091P4(u)`，系数参考LG20-11的theoretical source尺度，pair selection为明确自设函数。若normalizer只含single-response而漏掉pair selection，拟合得到a2≈−.165398、a4≈−.099697；matched joint normalizer恢复.102/.0091。256/512点积分收敛；相同knownsource系数不是本任务新测量或真实数据fit。

真实接受率为零的bins无法通过除法恢复；小normalizer也会放大误差。复用同一mixed histogram为多个gates归一化，会共享统计/cut/basis covariance，不能把它们当独立实验。应保存normalizer构建的输入stage、event pool、energy/PID/rate条件、same/different-event定义与重复使用范围。

### Independent events 仍可有共同 beam-axis shape

在另一个独立toy里，各事件photon相互独立，但单photon方向密度都为

$$q(\mathbf n)=\frac{1+A_2P_2(\mathbf n\cdot\hat z)}{4\pi}.$$

对两独立draws，用addition theorem积分绝对方向后，pair-angle cosine u密度为

$$g(u)=\frac12\left[1+\frac{A_2^2}{5}P_2(u)\right].$$

若自设A2=1，cross-event pair a2=.2，a4=0；方向quadrature给.200000000000014，50万pairs MC给.199326±.003239（这里±仅MC标准误）。这是共同束轴的marginal anisotropy产生的angle structure，不能说“不同event”就等于isotropic normalizer，也不能把它当same-cascade γγ quantum correlation。

另用isotropic目标shape去除以这个aligned normalizer，可得到spurious拟合a2≈−.190200、a4≈.018695；这是特意声明的另一个反例，未推导真实in-beam cascade必须如何归一化。实际beam correlation/population与response应联合处理，LG20-12的source→beam迁移限制不能省略。

### Raw/postPSA 与独立性边界

LG20-1 明确postPSA points只能重放后续event merging/tracking；重新跑PSA需要原traces和basis/calibration，不凭final tracked photons重建缺失IP。LG20-7/8/14的Doppler position estimate使用independent VAMOS vector和energy-dependent 1D IP FWHM模板，不把5.1mm平均值当所有角度/能量的σ。C23-7/12重复本篇source benchmark，不增加acquisition数；VD16同设施98Zr路线无runmanifest时也不默认独立。

## Detector frame 的 tracking 与 Doppler 处理顺序

[[ljungvall-2020-agata-ganil-performance]] LG20-1的processing chain和[[crespi-2023-agata-tracking-performance]] C23-1/8的Compton/Doppler式要求保留各阶段的frame。Detector中scattering的energy/angle与近似静止electron使用实验室frame；目标核的rest-photon energy则由已识别incoming photon的lab total energy、方向与emitter velocity反演。Ancillary vertex信息可先进入tracking，但不意味着先把所有detector deposits改成emitter-rest energies。

[day13_tracking_frame_order.py](../../system/scripts/day13_tracking_frame_order.py)构造free-electron two-hit fixture，incoming lab photon1000keV、true Compton cosθ=−.9。若先将每个deposit都乘同一个incoming inverse Doppler factor D，再配lab角/electron-rest式做FOM，会推得

$$\cos\theta_{wrong}=1-\frac{1-\cos\theta_{lab}}{D}.$$

自设emitterβ=.07且incoming沿速度方向，D=.932287，错误cos≈−1.038，落在physical范围之外；β=.3时≈−1.589。此时pre-scaled总能量仍数值等于正确incoming rest energy，**能量和正确不保证内部Compton classification也正确**。

若真正boost整个scattering的photon/electron four-vectors，electron在新frame中不再静止。Lorentz-invariant relation `pe·k=pe·k′+k·k′` 与four-momentum conservation继续满足；不能只缩放energy而保留electron-rest及lab-angle公式。代码的full boost/mass shell/invariant与β0顺序一致极限均通过，invariant residual<1.2×10⁻10keV²。

本fixture忽略bound-electron momentum、有限electron track、escape/材料与真实FOM；没有指控任何actualsource pipeline提前缩放。[[doppler-correction]]的hit-sum/first-point练习和这一frame检查检验不同条件：前者要求同一photon只用一个incoming direction，后者要求Compton tracking留在适用的detector frame。重放时应保存calibrated lab deposits、source/first-point metadata、tracked total与corrected rest energy的stage labels，避免只留最终窄谱。

## Particle ancillary 的 γ response 与 relative normalization

[[assie-2021-mugast-agata-vamos]] AS21-6/7 的source benchmark在41crystals/R182mm给1.4-MeVphotopeak效率4.9(1)%、邻晶add-back7.1(1)%；lowenergy P/T变差。Source/geometry/algorithm不同于LG20的29crystal配置，不能把比值当纯tracking改进。

MUGAST39crystals/R182mm与plunger35/R233mm的transparency比较先在1.4MeV归一，再讨论above200keV相似、100keV约10%差。这个shape comparison不保留absolute scale，不能证明所有gamma能量/角度的absolute attenuation均为零。AS21-1的target-holder shadow与AS21-13的forward mask/shutter说明real occupancy也需匹配。

Lightparticle/重离子信息能改善Doppler（AS21-8），addedmaterial/trigger和PID/clock仍改变被选gamma样本（AS21-2/9/10）。实际validation须同时保存raw/lab/rest能量、particle/beam/target metadata、FEP/P-T与joint efficiency/covariance，不从一个改善的峰宽推整套response完成。

## AGATA/EXOGAM 比较的 angular controls

[[lemasson-2023-agata-vamos-fission-history]] LS23-5/6 的98Zr1222.9-keV comparison明确区分EXOGAMall-rings15keV、backward-only7keV与AGATA100–170°的5keV；two spectra还归一same total counts。15/5含不同angularselection，7/5仍有array/config差，二者都不是matchedgeometry的purealgorithm factor或absoluteefficiency。

[[crespi-2023-agata-tracking-performance]] C23-10的1229.9打印值与本directreference的1222.9不同，继续保留原text与新locators；不把review省略的条件补写成原文完全一致。LS23-1/7的Exp1–4与VD16/LG20run绑定也需manifest，不能只同nuclide/facility合并数据。

[[ciemala-2019-20o-dsam-analysis-status]] CO19-10/11/12提供source simulation/current-photon/late-ion/response链的另一个例子。Code与data的相同tracking流程很有用，仍需要输入β/vertex/energyframe的stageidentity；modeltruth与late-measurement uncertainty不能在字段名“emittervelocity”下混合。
