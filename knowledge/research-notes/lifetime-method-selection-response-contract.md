---
type: research-note
title: "寿命方法选择：时间响应、分量条件与最小校准"
aliases: [lifetime method selection response contract]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day18-uncredited-Day19-preview
evidence_sources: [radeck-2012-deorientation-lifetime-98ru-rdds, klemme-1999-lifetimes-134nd-neighbors, nolan-sharpey-schafer-1979-lifetime-measurements]
tags: [lifetime, RDDS, DSAM, deorientation, calibration, response]
---

# 寿命方法选择：先定义时间响应，再比较精度

## Research Trigger

正式Day18在主线和新DSAM审计后，按原2026-10-21 15:00上海deadline的实时≥120分钟门，开始恰好下一Day19知识预习。先冻结承认强priming的回忆；不授19、不新建session/调度、不打开再下一卡。当前已完成Radeck十页原读、Nolan选段/电子计时段与分量响应exercise，方法选择表和最小校准清单见末两节。Nolan本次是定向核验，不是新完整88页阅读；现代fast-timing/TDPAD primary、actualproducer与Cov仍缺。

## Grounded Evidence

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-P19-1–10是本session新完整原读十页/13图3表9编号式，旧人审prefix/12旧flags原字节保留，新claims待审。[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D18-1–4此前定向companion已核finite-stopping，不能把它再计一项独立新实验。

| 实际对象 | 在Radeck中的角色 | 不能代替的输入 |
| --- | --- | --- |
| 六ring、particleγ触发、相对distance谱 | Radeck2012采集的SH/US强度，stopper tail并入US | Winther初始alignment/相对eff/绝对距离零点 |
| normalized SH+US vs distance | Fig5/9的deorientation诊断与校正检查 | 不是在所有角度/实验下保证alignment不变的充分检验 |
| P=SH/(SH+US) | lifetimefit的比值，公共particle归一与solidangle因子消 | SH/US能量eff、boost、退取向response不消 |
| GUS、GSH | 同一角数据提取的component-conditioned attenuation | 不当两个独立原实验或仅由一个积分G唯一决定 |
| 90°eff calibration | 最短距离用理论角关联代替缺失calibration、加sys | 不是独立实测eff；不能由收敛两步认证实际Cov/coverage |
| τ、B(E2)、B4/2、IBM比较 | 观测→模型/responsefit→branch转换→解释 | 不按输出列增加独立证据；IBMcharge匹配2+输入不独立验证该输入 |

## Assumptions

新解析chart明确取physical elapsed time t≥0、Gk(t)=αk+(1−αk)exp(−Γkt)、指数核寿命、stopper内取向冻结；α/Γ/τ用源中心。这个chart说明时间条件平均，不认证原相对distance坐标或实际fitproducer。没有实际Acoul、完整jointΣ、逐ring计数或distance/efficiency校准账本，不给新τ/g/CI。

## Provisional Reasoning

对到达stopper时刻t，US的取向核为GUS(t)=G(t)。SH只包含到达前衰变，须以条件密度exp(−u/τ)/[τ(1−exp(−t/τ))]在0≤u≤t平均，因此

\[
G_{SH}(t)=\alpha+\frac{1-\alpha}{1+\Gamma\tau}
\frac{1-e^{-(\Gamma+1/\tau)t}}{1-e^{-t/\tau}},\quad
\alpha\le G_{US}(t)\le G_{SH}(t)\le1.
\]

t→0两者趋1；t→∞时US趋α，而SH趋α+(1−α)/(1+Γτ)，不会趋同一α。用源τ8.36ps/两rank参数得SH极限.554922/.449653，US.18/.24。这个差异就是同一个退取向过程在不同衰变选择下的结果；不是新实验确认了两个不同超精细场。

[新合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/radeck-kernel-input-contract-007.json)、[程序](../../system/scripts/day19_radeck_component_kernel.py)/[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/radeck-kernel-result-007.json)核raw hash和正时间有界关系。字面d3−d0正8的Eq9会给P≈−.045333，故实际坐标桥是必要输入；没有因此改符号、猜erratum或重报τbias。A0(d)=0与正Fig7角强度也保为literal边界。若另假定d3为绝对零点起飞，t=.222387ps、G2US=.974510只是条件数值，不能当真实最短距离alignment或eff偏差测量。

## Competing Explanations

同一个SH/US强度变化可以含寿命、时间退取向、能量效率、boost、距离零点或污染。Radeck的多角关联与两个分量信息帮助区分其中几项，但缺失90°eff被理论补归一，同data的迭代与校正后平坦性不能作为全输入独立的证明。Klemme的distance恒定性也仍保finite-stopping；方法名不同不等所有nuisance正交。

## Transfer Conditions

相同level/branch身份、速度/材料与电子charge-state演化、samegate角接受、component定义、时间/距离零点、实际效率和联合Cov须匹配。Γ=|g|/C只给幅度；同元素C迁移另要同v/c/charge equilibrium等原条件，不能由符号字母把C当任意核的独立校准。

## Failure Conditions

stopper中取向未冻结、未见feeding、宽速度/acceptance与alignment相关、缺失relativeeff被未知模型替代、distance零点/符号没有producer证据，都使简化kernel不足。finite-stopping时US含慢化尾，不是每个US光子的发射速度精确为零。

## Falsification or Reverse Tests

取得匹配的efficiency calibration和distanceproducer后，检查各ring独立P(d)、SH/US角分布与去除理论归一的敏感性；若共模型无法同时解释分量与角度，应扩response而非强行缩小τ误差。需要实际计数/Σ才能定量判断该检验对原τ的影响。

## Evidence Gaps

Nolan1979本preview已核方法框架/电子计时选段，方法选择表和最小校准清单已形成；本次未完整重读88页，也未取得现代fast-timing/TDPAD primary或原producer。Radeck原Wintherjob、distance零点、逐ringcounts、实际eff/attenuation/lifetime联合Cov均未得。不能只凭文中“model independent”简写或两步迭代称已复现实验。

## Reproducibility

Day19-preview回忆time/session/hash先于本preview打开Radeck/Nolan；sourceprefix长度/hash与raw hash冻结，原人审字节不变。原件十页文本和PDF2–9视觉核、参数合同和脚本结果在同一Day18 run目录；无新session/正式19学分。旧阅读和本回忆均强priming，不报盲测分数。

## Human Review

旧Radeck人审段只保历史，不把本新段或脚本升为human-reviewed。新claim与研究推断均待审；当前缺口由Codex追踪，不自动成为用户待办。

## Knowledge Impact and Learning Decision

`supports`以component-conditioned response选择寿命方法；`revises`一个积分退取向因子可直接校两个分量、校正后平坦性即全独立验证的假设；`limits`从相同τ/B/模型列计独立证据。已用Nolan方法框架补方法选择表和最小校准清单；正式Day19仍需独立session承认本priming并完成新交付。

## Open Questions

- Nolan1979 的方法范围、现代 fast-timing 响应和 Radeck 的 component kernel 能否在同一 source-grounded decision tree 中严格对齐？
- Radeck 的实际 Winther–de Boer angular-correlation input、逐 ring efficiency 和 distance-zero producer 能否取得，以检验 Eq. 9 的字面边界是否只是排版/坐标约定？
- 对 Ag106，是否存在同 level、同 reaction 的 RDDS 或 fast timing 数据，能把 Rather 的 DSAM stopping/feeding nuisance 与 observed rate contrast 分离？

## Promotion or Rejection History

- 2026-10-20 Day18 内无学分 Day19 preview：Radeck 原件完成新读，canonical note 保持 `ai-draft`、`unreviewed`；当时Nolan定向阅读与方法选择清单待补；后续已完成相关预习知识，正式Day19 card仍未开始。
- 当前 note 只固化 component-conditioned response、校准缺口和可复现条件 exercise；不提升为正式 Day19 课程交付，不把旧 priming 或本 preview 兑换课程学分。

## Nolan方法框架：选择方法前先列主导响应

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-P19-1–8是本session针对PDF3/6–7/10–12/19–23/78–81的原文核验，旧source全文读取状态与所有旧flags不改。综述把DSAM的主导依赖放在stopping/velocity/feeding，把RDM的主导依赖放在flight-distance与短寿命端的distance calibration；它还给出约1–20ps重叠区和“相合可能共享错误stopping”的直接反例。

因此当前方法选择决策树是条件性的：

| 条件 | 首选响应 | 必查校准 | 主要失败模式 |
| --- | --- | --- | --- |
| line-shape可解析、recoil stopping可建模 | DSAM | velocity、电子/核 stopping、feeding/side-feed、角/能量响应 | stopping model或feeding profile主导τ |
| shifted/unshifted随距离可分、plunger距离可精确标定 | RDDS/DDCM | distance zero、ring efficiency、deorientation、finite stopper、feeding gate | 短τ距离标定或分量/角关联response |
| prompt时差明显、fast detector response可校准 | 电子计时（1979框架） | prompt curve、walk、background、gate/feeding | PRF/能量门不匹配；未得实际producer/Σ |
| alignment/hyperfine随flight time改变 | component/deorientation kernel | angular correlations、charge-state/velocity、同元素C迁移条件 | 把US冻结、SH平均或理论补eff当无偏 |

这张表是本任务的bounded synthesis，不把“方法窗口”写成硬阈值。下一步若正式开启Day19，必须为每行补实际source locator和至少一个同data counterinput；当前不打开Day20。


## 电子计时：PRF先于寿命拟合

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-P19-9–12补PDF48–52。电子计时的关键输入不是“时间戳”这个名称，而是production zero-time、decay detector、prompt response function (PRF)、energy/walk/geometry dependence和prompt/delayed同门校准。slope需寿命长于PRF尾，centroid可处理远小于FWHM的差，但越接近PRF响应越需要同时测PRF、按能量/门校正并追踪系统误差。

Day19 preview的最小方法选择清单现为：

1. 先识别直接观测：DSAM的F/lineshape、RDDS的SH/US-distance、timing的delayed−prompt time distribution。
2. 列出主时钟与 nuisance：stopping/feeding；distance/velocity/deorientation；PRF/zero-time/walk/background。
3. 找同data counterinput：above-gate/side-feed or alternate stopping；rings/distances or angular correlations；prompt calibration and energy-matched gates。
4. 只有响应合同、branch/ICC/mixing和joint covariance齐全时，才把τ转为B/Qt并比较结构；方法结果相合仍须检查共享反应、模型和强度输入。

本预习已覆盖矩阵要求的Radeck/Nolan主线、bounded exercise、response counterexample、decision tree和minimal calibration list，但仍只算Day19无学分preview；正式19需新session重新逐卡承认priming并补实际source/producer边界。
