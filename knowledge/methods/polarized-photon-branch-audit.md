---
type: method
title: "偏振光子散射的混合比分支核验"
aliases: [NRF branch audit, polarized photon mixing branches]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
method_type: polarized-photon-angular-correlation
tags: [nrf, mixing-ratio, phase-convention, polarization, conditional-inversion]
---

# 偏振光子散射：已知初始偏振仍可能多解

## Purpose

以[[rusev-2009-multipole-mixing-ratios-11b]]的实际不对称度和[[iliadis-friman-gayer-2021-polarization-direction-correlations]]的显式系数定义，区分已知入射beam density、phase/role选择、detector响应和最终混合比分支。它与[[dco-pdco-ambiguity-worksheet]]互补，但这里是NRF absorption–emission，不能直接套两个先后发射gamma的同名delta规则。

这是来源后的L2/设计练习，不是RU09 events/GEANT3重放、重新评价11B δ或新核素结构图。

## Inputs and Assumptions

RU09 TableI给ground-state三线：4443.93keV，a=.026(.019)；5019.08keV，a=.200(.016)；8916.3keV，a=.215(.020)。ground为3/2−，excited分别5/2−、3/2−、5/2−。原C为.950/.941/.950，来自作者10MeV GEANT3；beam P_gamma只说nearly100%，本计算**选择exact1**作nominal近似，无P/C实际不确定度或Cov。

最低M1/E2、real amplitudes、isolated states、unpolarized target ground、point detectors；不拟合Gaussian sigma、P、C或更高阶。原beam与装置存在finite acceptance/能量响应，不能因此给新δ置信域。Rusev的a是**入射束偏振下散射方向不对称**，不是clover Compton A或emitted-gamma物理P。

原仪器epsilon_h/epsilon_v=1.011(.010)，a使用Ah/th与Av/tv及该效率比。不能把raw水平/垂直峰面积直接相除；其校准/beam/GEANT/branches在多线间共享，未给完整Sigma。

## phase roles与有向几何

IF21 Eq13–18采用Biedenharn：中间J始终在RME右边，elastic同一pair给dB1=dB2；与其所说的**未改系数**Steffen坐标桥为dB1=−dS1、dB2=dS2。源于算符和state顺序的转换须连同coefficients一起做；它不是把一个物理候选翻成另一支。

IF21 VoRp5明确批评RU09按Steffen文字写d1=d2，认为影响W大小。这是综述作者判断。本次还核到ALPACA公开README提及另一个modified-KSW约定：改变incoming coefficients可让elastic两步同号。对应2022 review脚注正文尚未取得，2023 corrigendum也只得metadata，**不能据此裁决RU09实际producer使用了哪套公式**。同号delta不是单独充分的error标记，必须得到完整定义。

IF21 beam沿x/E沿y，phi从z轴的yz投影量起；探针用beam-z/E-x和标准azimuth。proper rotation给phi_probe=pi/2−phi_IF。因此RU09的平行E减垂直E不对称为−A_IF；不能忽略这个几何差再只翻δ符号。

## 两条代数路线及原始失败记录

第一条保留的NRF probe使用已验证doubled-spin CG/Wigner photon operators：吸收由同photon-mode emission算符的Hermitian conjugate构造，ground density为I/(2Jg+1)，emission helicities取trace。原native到RB基底用既有(-1)^L，不为RU09调号。每个scattering amplitude是`C0+δC1+δ²C2`，W为quartic；共同(1+δ²)^−2在ratio中抵消。

这个probe的internal polynomial/direct、纯极限及Jexc=1/2各向同性控制通过，但首轮不匹配RU09的全部mixed曲线；5/2路径给4实根，原文讨论two roots并举−1.30。完整firstcode/result/input已保存，没有挑一根配表或改C。固定delta_in=0、相反internaldelta或丢rank4的后续诊断均明确是**不同模型/后验scope controls**，也没有闭合全部source结果，不作actual作者实现归因。

第二条独立实现IF21的Eq3–9：An是F11+2dF12+d²F22；En含electric/magnetic phase及rank因子，避免CG分母0/0。与原trace在选定ground3/2、Jexc3/2和5/2、五个real d及斜向几何网格比较，max差8.89e−16；数值角平均1。两路径共享CG/6j基础函数，因此是独立代数收缩，不是两份独立实验或原作者程序。

它验证了首probe与**IF21物理elastic/Biedenharn模型**相容，不意味着首probe是RU09 Eq3/producer的逐字重放。原冻结input的同名KS约定假定没有回写，后来解释在这里明确分层。

## 保留所有实根的条件反演

在IF21一致模型中使用原印a/C做摘要反演，所有central实根如下；不是对实验δ的替代推荐，也未以物理可接受性丢根。

| input line / a | dB=dS,em 的所有central实根 |
| --- | --- |
| 4443.93 / .026 | −2.914493569；−.512675420；+.173061902；+2.138866947 |
| 5019.08 / .200 | −.053879697；+.575312969 |
| 8916.3 / .215 | −7.104080121；−.389283148；−.000544798；+3.105891689 |

每根由quartic全根求解并代回ratio核验；印a±sigma的全部根也在artifact，不将这些endpoint images当jointCI。published beamP/C uncertainty、finite-response、background、multi-lineCov均缺，所以没有完整statistical reanalysis。

按IF21 Eq18作“未改Steffen却同号”的字面变体，即在B系数中dB1=−dB2，4443的小根.15824164、5019的小根−.03643268接近原表.158/−.036；但8916仍未得到原文大根−1.30。physical一致模型在−1.30给a≈−.41786，字面变体约+.36810，均非原观测+.215。这个不闭合保留为**unrounded source implementation/定义/response的复现边界**，不是证明哪一种作者代码错误，也不能把source原δ改成上述conditional roots。

RU09自己按大E2成分“unusually large”选择较小|δ|，−1.30对应radiative E2≈.62825（约63%），是作者物理先验选择；其a没有独立唯一选枝。即使采用其选根，后续branching-transition δ2也继承选定δ1和同response，不能算新的独立ground-state验证。

## 真正能区分这些候选的下一观测

对**上述consistent point model**，在theta45°的理想RU09 parallel−perp预测为：

| line | 对应上表各central根的 ideal a45 |
| --- | --- |
| 4443.93 | −.47384435；−.01354296；+.01321306；−.34497584 |
| 5019.08 | +.09852351；+.04554228 |
| 8916.3 | −.48332245；+.04431638；+.10161676；−.36006462 |

theta90数据在每行刻意相同，45°增加了不同direction的约束；但4443两个小模根的45°差只有约.02676，actualresponse/误差未给，不能保证实验可分。这里没有把source的C90=.950移用C45；须按IF21 Eq30在各rank/各detector实际fold response，考虑共同P、efficiency和背景Cov，或做验证过的transport simulation。

一个新的强度“合理性”论证与一项matched45°或独立幅度observable不是同层证据。也并非任何更多角都保证唯一：IF21的某些pure-dipole/pure-quadrupole完整patterns相同，额外同类detectors不能增加rank；出射偏振或其它独立observable可能更合适。

## What It Can Establish

说明knownbeam density无需fusionevaporation Gaussian模型仍不自动消除phase、formalism、finitegeometry、多根和physical-prior依赖。给出由实际发表摘要输入驱动、定义完整、可复算的conditional根及下一角预测；将未闭合source重放与已核数学分开。

## What It Cannot Establish Alone

不能以本模型改变RU09发表δ、原source旧人审、11B Jπ或结构解释；不能在无producer/events/beam/response/Σ时提供actual confidence或判作者代码错误。原文“model-independent”针对其无需额外反应取向模型的语境，不能扩张为无物理假设或唯一性证明。

## Reproducibility

- [原冻结RU09输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-rusev09-elastic-input.json) SHA-256 `507029204a85b75d93d37dda9d319f8b36ecea16185fa7594509ac478cf21d59`；[原trace脚本](../../system/scripts/day16_rusev09_elastic_branches.py)、[firstresult](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-rusev09-elastic-first.json)和firstcode snapshot保留。
- [IF21核验输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-if21-coefficient-audit-input.json) SHA-256 `c0a46e572ed215c03608b2881765ba844937b57bb3e76940ebbeb3f2ebcd8af0`；[系数脚本](../../system/scripts/day16_if21_coefficient_audit.py)/[最终全grid与roots](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-if21-coefficient-audit.json)。来源前冻结都是primed，不冒称盲复现或正式Day16成绩。
- ALPACA仅固定commit/Gitblob read，没有build、执行或复制GPL程序；KSW1973只定向核相关role/normalization页，没有通读56页。它们不替代直接paper或RU09 actualproducer。

## Sources

- [[rusev-2009-multipole-mixing-ratios-11b]] RU09-8–14；actualasymmetry/控制/作者选根与数据依赖。
- [[iliadis-friman-gayer-2021-polarization-direction-correlations]] IF21-1–11；完整显式definition、publishedcriticism、geometry、rank与response。
- [[krane-steffen-1970-cd110-mixing-ratios]]与[[rose-brink-1967-phase-defined-angular-distributions]]：本run先前核过的operator/state桥，不能仅由符号名推另一NRF角色关系。
