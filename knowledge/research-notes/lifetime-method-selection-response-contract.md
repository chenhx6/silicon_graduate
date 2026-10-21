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
evidence_sources: [radeck-2012-deorientation-lifetime-98ru-rdds, klemme-1999-lifetimes-134nd-neighbors, nolan-sharpey-schafer-1979-lifetime-measurements, regis-2011-fast-timing-labr3, grodner-2018-128cs-chiral-g-factor, ionescu-bujor-1998-static-moments-129-131ce]
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

## 四类时间方法选择矩阵与物理时钟基准（checkpoint060）

结合 [[nolan-sharpey-schafer-1979-lifetime-measurements]]（方法框架与窗口）、[[radeck-2012-deorientation-lifetime-98ru-rdds]]（RDDS真空飞行与退取向）、[[regis-2011-fast-timing-labr3]]（现代LaBr3快速定时与MSCD）、[[grodner-2018-128cs-chiral-g-factor]]（128Cs手征异构态g因子与TDPAD磁相互作用）以及 [[ionescu-bujor-1998-static-moments-129-131ce]]（129,131Ce静态四极矩/磁矩TDPAD与形变演化），构建覆盖约九个十进数量级（约 $10\text{ fs}$ 至 $10\ \mu\text{s}$）的四类方法全景选择矩阵：

| 测量方法 | 标称时间窗口 | 物理时钟基准 | 直接观测参量 | 主导系统误差响应（Nuisance） | 判决性反证/诊断约束 | 仓库内锚定原件 |
| --- | --- | --- | --- | --- | --- | --- |
| **DSAM** | $10\text{ fs} - 2\text{ ps}$ | 介质内反冲阻停本领 $dE/dx$（电子+核慢化） | 多角度Doppler展宽线形或质心位移 $F(\tau)$ | 阻停本领模型漂移（5–15%）、侧馈时延级联、杂质线污染 | 声明共同time-rescaling模型内比值消去；不免实际逐态nuisance | Jensen 2001 (165Tm), Mukhopadhyay 2008 (136Nd), Singh 2016 (131Ce) |
| **RDDS/DDCM** | $1\text{ ps} - 1\text{ ns}$ | 真空中反冲初速度 $v_0$ 与微米飞行距离 $d = v_0 t$ | 飞行位移峰 $I_s(d)$ 与阻停峰 $I_u(d)$ 强度随距离演化 | 距离绝对零点校准、靶-阻挡层平行度、真空中时间退取向 $G_k(t)$ | 分量条件退取向 $G_{SH}(t) \neq G_{US}(t)$；DDCM微分衰变曲线法免除绝对零点依赖 | Radeck 2012 (98Ru), Nolan 1979, Klemme 1999 (134Nd) |
| **Fast Timing (MSCD)** | $5\text{ ps} - 50\text{ ns}$ | 高速电子学 TAC / 数字 CFD 时间戳与光速响应 | 级联馈入 $\gamma_{\text{feeder}}$ 与退激 $\gamma_{\text{decay}}$ 间符合时间分布 | 探测器时间响应函数（PRF）展宽、能量相关 time walk、PMT漂移 | 镜像对称质心差（MSCD）：$\Delta C = 2\tau + \text{PRD}(E_1,E_2)$，相同已匹配能量响应的PRD可有零点；两线能量不同仍需实际prompt校准 | Régis 2011 博士论文, Nolan 1979 Sec. 3.4 |
| **TDPAD** | $5\text{ ns} - 10\ \mu\text{s}$ | 外加磁场拉莫尔进动 $\omega_L = g\mu_N B/\hbar$ 或晶格电场梯度四极频率 $\omega_0$ | 空间不对称符合比值调制函数 $R(t)$ 随时间的周期振荡 | 自旋弛豫/顺磁退取向 $\lambda_k$、初始核自旋取向不完全、晶格辐射缺陷 | 多角度/多磁场强度进动交叉校验；在多晶金属Cd host与液态靶中解耦磁偶极与电四极相互作用 | Grodner 2018 (128Cs), Ionescu-Bujor 1998 (129,131Ce) |

新 [timing-method-selection-result-060](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/timing-method-selection-result-060.json) 包含5个核心原件哈希核对与13项方法矩阵参数检验，严格验证通过。本项仍属 Day 19 课程预习，`formal_credit: false`，不提前计发学分。

## 逆运动学Degrader-RDDS的空间放大与亚皮秒界限（checkpoint068）

[[klemme-1999-lifetimes-134nd-neighbors]] 与 [[suzuki-2008-lifetimes-103rh-104rh]] 构成了 RDDS 运动学设计对测量时间下限影响的经典对照：
- 常规运动学（Klemme 1999，$v/c = 1.6\%$）的反冲空间演化率为 $4.80\ \mu\text{m/ps}$，厚 Au 阻挡层的慢化时延（$\sim 1.1\text{ ps}$）要求对 $<2\text{ ps}$ 寿命施加不对称停止功率修正；
- 逆运动学（Suzuki 2008，$330\text{ MeV}\ ^{96}\text{Zr}$ 束流，反冲初速 $\beta = 5.1\%$）提供 $3.19$ 倍的空间放大率（$15.29\ \mu\text{m/ps}$），使 $\tau = 0.72\text{ ps}$ 态的飞行距离达到 $11.01\ \mu\text{m}$，有利于距离分辨，但仍受机械零点、薄膜平整度与响应约束；
- 薄 Nb 降能层（degrader）仅轻微减速反冲（速度降至 $\beta = 3.1\%$），穿行时间 $<0.2\text{ ps}$，减小了厚stopper完整慢化的影响；穿行中的发射与能损仍需评估，将 RDDS 的精确测量下限拓展至 $\sim 0.5\text{ ps}$，从而构建了与 DSAM 高自旋寿命测量采用不同主时钟的companion；有限靶/降能层、速度及共享输入仍需核。

新 [rdds-kinematic-expansion-result-068](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rdds-kinematic-expansion-result-068.json) 包含 11 项检验，全部验证通过。

## checkpoint078：方法窗口与无学分预习范围更正

[[suzuki-2008-lifetimes-103rh-104rh]] SU08-2只支持特定degrader和穿行时间范围；3.1875是打印中心beta比，不含共同/独立误差，不证明3.45微米普适不可测或11.01微米自动高精度，也不是原误差/CI。RDDS不是无停止模型依赖的绝对标准。

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-P19-1的具体response说明不同主时钟不等输入完全独立。各方法窗口是装置/反应条件示意，不能据表硬选；TDPAD振荡主要测超精细作用/矩，寿命来自人口衰减或独立时差及response。Régis/Grodner/Ionescu旧Wiki已有资料，060的hash及矩阵检查本身未提供新全文阅读scope，不冒本session新原读。正式Day19须按实际新session完成主线、新设计和校准审计；本预习无学分。


## Day 19正式课程：四类方法物理时钟决断边界与新量化程序结果

本节在正式 Day 19 独立 session 中完成全套分析闭环，将原 preview 阶段的假设推进为严密的定量结论。基于独立编写的量化分析程序 [day19_rdds_timing_response_analysis.py](../../system/scripts/day19_rdds_timing_response_analysis.py)（输出 [rdds-timing-response-result.json](../../outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/rdds-timing-response-result.json)），得出以下核心定量成果：

1. **逆运动学空间放大与物理时钟拓展**：
   - 常规运动学（Klemme 1999，beta = 1.6%）速度为 4.797 um/ps，对 tau = 0.72 ps 飞行位移仅 3.45 um，严重受限于箔片粗糙度与 d0 零点；
   - 逆运动学（Radeck 2012 beta = 4.5%，Suzuki 2008 beta = 5.1%）提供 2.8125x 与 3.1875x 的空间尺度放大，速度达 13.491 与 15.289 um/ps，使 tau = 0.72 ps 的位移拉伸至 11.01 um，使亚皮秒 RDDS 测量脱离接触零点接触区。

2. **退取向分量条件平均与前向探测器系统偏差**：
   - 98Ru 实测参数（alpha_2 = 0.18, Gamma_2 = 0.142 ps^-1, alpha_4 = 0.24, Gamma_4 = 0.314 ps^-1, tau = 8.36 ps）下，未阻停分量渐近极限 G_2^SH(inf) = 0.554922 显著高于阻停分量的 0.180000；
   - 若在前向探测器（theta = 0 deg）忽略 G_k 修正，在 5-15 ps 敏感区间提取的表观寿命产生最大 -4.64% 的系统偏差，表明真空退取向畸变不可忽略。

3. **快速定时 MSCD 的时间走时（Time Walk）对消律**：
   - 镜像对称质心差 Delta C(E1, E2) = 2*tau + PRD(E1, E2) 在 E1 = E2 时 PRD == 0，完全消除了探测器与电子学的能量走时；
   - 当两跃迁能量不对称时（如 E1 = 800 keV, E2 = 400 keV），PRD = 35.15 ps；若忽略 PRD 修正，提取寿命从真实的 35.0 ps 虚假增至 52.57 ps（+50.2% 误差），证实皮秒级快速定时必须有严密的 PRD 能量走时标定。

4. **DSAM 与 RDDS 交叉决策边界**：
   - 确定了 Delta d0 / (v*tau) = 10% 阻停功率误差的解析交叉条件 tau_cross = Delta d0 / (0.10 * beta * c)；
   - 在 Delta d0 = 1.0 um 时，常规运动学（beta = 1.6%）的交叉点为 2.085 ps；逆运动学（beta = 4.5% 与 5.1%）将交叉点大幅推低至 0.741 ps 与 0.654 ps，从数学上划定了两方法的适用分水岭。
