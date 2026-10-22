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
| **TDPAD** | $5\text{ ns} - 10\ \mu\text{s}$ | 外加磁场拉莫尔进动 $\omega_L = g\mu_N B/\hbar$ 或晶格电场梯度四极频率 $\omega_0$ | 空间不对称符合比值调制函数 $R(t)$ 随时间的周期振荡 | 自旋弛豫/顺磁退取向 $\lambda_k$、初始核自旋取向不完全、晶格辐射缺陷 | 多角度/多磁场强度进动交叉校验；按实际host核验：Ce在多晶Sn测QI、Sn/Pb及外场测MI；不同场/方向/材料作控制 | Grodner 2018 (128Cs), Ionescu-Bujor 1998 (129,131Ce) |

新 [timing-method-selection-result-060](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/timing-method-selection-result-060.json) 包含5个核心原件哈希核对与13项方法矩阵参数检验，严格验证通过。本项仍属 Day 19 课程预习，`formal_credit: false`，不提前计发学分。

## 逆运动学Degrader-RDDS的空间放大与亚皮秒界限（checkpoint068）

[[klemme-1999-lifetimes-134nd-neighbors]] 与 [[suzuki-2008-lifetimes-103rh-104rh]] 构成了 RDDS 运动学设计对测量时间下限影响的经典对照：
- 常规运动学（Klemme 1999，$v/c = 1.6\%$）的反冲空间演化率为 $4.80\ \mu\text{m/ps}$，厚 Au 阻挡层的慢化时延（$\sim 1.1\text{ ps}$）要求对 $<2\text{ ps}$ 寿命施加不对称停止功率修正；
- 逆运动学（Suzuki 2008，$330\text{ MeV}\ ^{96}\text{Zr}$ 束流，反冲初速 $\beta = 5.1\%$）提供 $3.19$ 倍的空间放大率（$15.29\ \mu\text{m/ps}$），使 $\tau = 0.72\text{ ps}$ 态的飞行距离达到 $11.01\ \mu\text{m}$，有利于距离分辨，但仍受机械零点、薄膜平整度与响应约束；
- 薄 Nb 降能层（degrader）使反冲减速但不停止（速度降至 $\beta = 3.1\%$），穿行时间 $<0.2\text{ ps}$，减小了厚stopper完整慢化的影响；穿行中的发射与能损仍需评估，本文实际报告短于1ps的可测性及约.71/.72ps结果；旧“精确测量下限~.5ps”未由本文原文认证，现撤回该门槛，从而构建了与 DSAM 高自旋寿命测量采用不同主时钟的companion；有限靶/降能层、速度及共享输入仍需核。

新 [rdds-kinematic-expansion-result-068](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rdds-kinematic-expansion-result-068.json) 包含 11 项检验，全部验证通过。

## checkpoint078：方法窗口与无学分预习范围更正

[[suzuki-2008-lifetimes-103rh-104rh]] SU08-2只支持特定degrader和穿行时间范围；3.1875是打印中心beta比，不含共同/独立误差，不证明3.45微米普适不可测或11.01微米自动高精度，也不是原误差/CI。RDDS不是无停止模型依赖的绝对标准。

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-P19-1的具体response说明不同主时钟不等输入完全独立。各方法窗口是装置/反应条件示意，不能据表硬选；TDPAD振荡主要测超精细作用/矩，寿命来自人口衰减或独立时差及response。Régis/Grodner/Ionescu旧Wiki已有资料，060的hash及矩阵检查本身未提供新全文阅读scope，不冒本session新原读。正式Day19须按实际新session完成主线、新设计和校准审计；本预习无学分。


## Day 19正式课程：四类方法物理时钟决断边界与新量化程序结果

checkpoint008：此前所谓“全套分析闭环”撤回。旧脚本只余注释/打印，旧JSON有条件输入冒充实验、截短CG及错归因。旧结果保留为rejected历史，不用于CI、课程认证或读过原件的证明。

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-3：在声明τ8.36、α=.18、Γ=.142且k4=0的控制中，t=8.36ps改变A2=−.35/0/+.35使表观τ相对偏差+8.07%/0/−4.92%。这反驳“−4.6%统一bias”，没有估计实际ring response。冻结US和条件平均SH是当前假设，不擅改论文相对距离坐标。

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-1：经典shared-stopping示例是same-data DSAM与CoulEx yield，不能错当RDM的原句。finite-stop RDDS可能共享输入是另一个条件推断，须逐实验核。

单一质心在自设walkA=1200/sqrt(E)、walkB=900/sqrt(E)与同E600keV时可有约−12.25ps偏移；但固定detector通道、只互换能量门的理想MSCD会同时消去两种不同而稳定的walk。两门数据之间若另有8ps相对drift，仍给τ偏差−4ps。故不能把“不同walk”本身作为同能量MSCD失效反例；需要明确门交换、稳定性、背景与实际PRD。以上均自设，不是LaBr3性能测量。

[[singh-2016-lifetime-131ce-133pr]] SI16-D20-2/3和[[li-2004-lifetimes-131ce]] LI04-D20-2/3保存正确打印值及CG反例。小z不证明常数形状，几何相容不识别作者K。相同旧τ的重算Qt不计独立证据。

新可复现程序day19_evidence_repair_audit.py执行exact Racah/闭式CG与条件响应反例；旧四个入口改为指向该程序的兼容入口，明确不重建旧错误JSON。尚缺逐ring计数、angular coefficients、calibration Cov、job和真实prompt数据；继续当前研究，不宣称饱和或关闭Day19。

## Day19新设计：能量门角色、有限时间窗与背景校准

此节是checkpoint009的自设L2 design exercise，原始参数τ=20ps、Gaussian PRF σ=80ps不是任何LaBr3实测。[[regis-2011-fast-timing-labr3]] RG11-D19-1–7给来源前提，[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-9给经典prompt校准反例。程序day19_timing_gate_response.py保存完整算法、source哈希、独立MC/积分与极限检查；28项通过，不是28次独立实测。

### 可分辨角色先于零点对消

有正确标签时D±=PRF与正/负指数的卷积，完整一阶矩为±τ；固定detector通道、只互换energy gates，稳定walk即使不同也在同E的PRD差中消去。公共电子学offset同时作用两支路可消，不同数据时间权重或drift另需控制。

若两跃迁真实能量退化、门完全重合且无其它role tag，选中的是F=.5(D++D−)，交换能量门仍得到同一F。其一阶矩0、二阶矩σ²+2τ²，仍保宽度/形状信息，但不能拿两份同谱的质心差0解释为τ0。这不否定原件的virtual-zero插值：插值需来自可分辨级联、同一目标τ的多组能量对及可信PRD曲线。

### 有限窗口不是增加计数能修的偏差

自设完整D±的质心差40ps；相同±80/160/320/640ps窗口内重新归一后，naive ΔC/2分别5.31443/14.63834/19.94104/20.00000ps。积分步长加倍复核；独立MC核完整混合矩。response模型必须包含time ROI和prompt/delayed匹配，不能把窄窗内更多计数当成完整一阶矩。

### 背景须按支路定义

AppendixA的差值mixture只在两支路相同background-to-peak比α时简化。自设α+=.3、α−=.1、背景质心100/20ps时，未校正naiveτ=27.41259ps；套平均α=.2后仍为24.89510ps；逐支路用各自α与背景质心才返20ps。不能反推原实验有该bias；需要同门背景面积、时间谱与其Cov才能判断。

同一PRD镜像使用(p,−p)有完全相关派生关系；恢复符号后平均仍只有原variance，自设9ps²不能因画两点降成4.5ps²。实际多个reference共享已知τ、gate events和校准函数，应由原sample/fitCov传播，不预设独立。

### 决策门与readiness

先核feeder/decay identity、role tag、energy门/时间窗、两支路fullenergy与Compton响应、time drift/共同offset、逐支路α/背景谱、reference寿命及shared-event Cov，再比较τ。缺输入只提出最小校准设计：同门prompt sample、足够时间尾、交换门一致性、各branch background sidebands和reused-calibration covariance账本。不报真实τ/CI。


## Day19校准图：closure通过仍可能有寿命偏差

[[regis-2011-fast-timing-labr3]] RG11-D19-9/10给printed中央curve与本任务conditional graph。保留signed参考门约定，令g为某一校准设置的combined response曲线，PRD(Ef,Ed)=g(Ef)−g(Ed)。同ΔE的两个绝对能量对不应套同一PRD；用原fit1中央值，800/400与1000/600均ΔE400keV却给161.558/112.851ps。1120/609与344/609的126.390/−128.651ps只核中央曲线/舍入，不认证原参数Cov或2σ/3σ转换。

5能量节点的连通图需要4个独立势差，参考time origin是gauge。镜像同一edge不加rank或独立count；三角cycle residual可检出非gradient偏移，源中reused444−244点仍须共享Cov。相反，给所有node加h(E)=.02E后，所有cycle仍闭合，但用该误校PRD处理一个真实τ20ps的1120/609 control会得14.89ps。这个盲方向说明closure是diagnostic而非绝对校准认证；还需外部已知τ、独立源/设置或其它物理标尺。

RG11-D19-11的实际176W控制显示：主动BGO与HPGe监视针对低能delayed背景/511污染是有实质内容的companion，不仅增加统计。更改PMT/CFD后重新测PRD的相合可检验若干instrumental输入，但共享核reference/校准函数的误差仍须保留。所谓“MSCD只剩背景误差”的总结不可脱离稳定/正确tag/timewindow/量纲/校准等原前提推广。

程序day19_prd_calibration_graph.py用exact rational rank、独立tree reconstruction与cycle/gauge/printed中心值控制，29项通过；没有新的核寿命、错误标尺估计或fitCI。缺event/response和joint calibration covariance时不报paperlevel区间。


## Day19分量库存：机械零点与响应诱导原点不是一个输入

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-8/9与[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-7给不同component合同的入口。新design将真空衰变S、慢化尾T、完全停止U分开；tf为physical真空时间，不是论文的relative motor distance。

S=1−z，T=z(1−k)，U=zk，z=exp(−tf/τ)，k=exp(−ts/τ)。若全部后入箔计US，(T+U)/(S+T+U)=z，无须因stopping本身再乘一个任意C；实际eff/角/速度与deorientation仍要核。若T完全丢弃再用U/(S+U)，R=kz/[1−(1−k)z]，局部log-slope给τlocal=τ[1−(1−k)z]。其0/∞端点都看似正常，却会有错误的中间响应曲率。

自设τ2ps、ts1ps、tf2ps：正确US=.367879，丢尾=.260894，naive单点τ1.48849ps、局部τ1.71050ps。若全count保留、q=.3尾归US而其余归SH，C=.724571、等效额外time=.644350ps，在β=.016/.045下对应3.09074/8.69270μm。q0或q1分别给1ps或0额外time。这里的time/ring/gate定义全为明确控制，不是Radeck/Klemme材料输运、拟合或CI。

伴随校准：同一peak inventory的zero-distance完整line shape、SH/US/tail的ROI与acceptance、归一分母、independent mechanical zero、每个ring/energy的效率及实际feeding/velocity distribution。R(d)端点、单点统计误差和某个常数τ诊断都不能单独补这些输入。新day19_rdds_component_inventory.py的64项库存、zero-ts极限、常数因子/offset与独立有限差分检查通过，仍只L2 design。


## Day19练习：同一20ps寿命，三种方法各缺什么

本表对应day19_same_lifetime_readiness.py的15项控制，τ20ps、各N=10000、σF=.005、σPRF80ps及δd1μm均是自设设计输入。不是实际beamtime/效率相等，不代表真实误差预算或方法排名。[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-11给简单DSAM核；[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-6/8给RDDS的实际校准/分量合同；[[regis-2011-fast-timing-labr3]] RG11-D19-1/3/5/7给timing定义及响应门。

| 方法与同一候选τ20ps | 自设响应/局部灵敏度 | 进入实际比较前必要输入 |
| --- | --- | --- |
| 固体DSAM，指数减速s=.3ps | F=.014778，σF=.005单项即可对应34.34%τ敏感性；欲控制5%需σF约≤.000728 | 真实v_z(t)、stopping和feeding，谱形/背景与实际F precision；此简单核不替代MC输运 |
| 气体DSAM，控制s=20ps | F=.5，同σF项约2%；但s与τ有精确scale ridge | 气压、温度/束流加热、局部密度、stopping/反应材料与feeding；20ps不是已知气体标定值 |
| RDDS，β=.016 | vτ=95.9336μm；仅已知nuisance的Bernoulli模型每点N10000最优x≈1.593624/d152.882μm，conditional CR bound约1.24% | independent v、mechanical zero、tail完整库存/eff/角核和feeding。单距离τ与zero的Fisher rank1；两不同距离可识别该模型中的λ=vτ与zero，但不能另分v与τ |
| Fast timing，σPRF80ps | 每支N10000且独立时，完整有标签质心统计SEτ≈.5831ps；5%目标仅PRD偏差项就需约≤2ps | actual pair/energy PRD、time calibration、role tag、完整time ROI、逐branch背景比及shared-event Cov。原件某设置8ps/2σ的PRD量级对应4ps寿命灵敏度，不把它改写成普适1σ或方法下限 |

δd/(vτ)是x=1处的单点几何敏感性。一般固定P提τ有δτ/τ=δd/(d−d0)；在上述conditional最优x，1μm只对应约.654%而非1.042%。若d0也自由或curve含未知amplitude/background，单点“最优”设计就不成立，须联合校准/多个distance。旧τ_cross只能作特定控制，不能当DSAM/RDDS的全域优选分水岭。

这组明确前提下，已具备distance/velocity及SH-US校准时RDDS可进入优先评估；若材料/几何不可用则继续评估气体DSAM或timing。方法名与τ窗口不替代真实readiness。不同方法和不同direct feeder/angle/prompt源可作companion，但共享reference/branch/stopping必须另列。


## Day19 DDCM设计：延迟feeding延伸可见距离，校准偏差可保持平坦

原依据[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D19-1–4。令B为直接feeder，A为目标level，所有branch均为1；S_B=P(B未衰变)，p_A=P(B已衰变而A未衰变)，F_A=P(A已衰变)。理想真空中S_B+p_A+F_A=1且F_A′=p_A/τ_A。B的等待分布可变；本程序只实现指数等待的fast/equal/slow及两指数混合控制，并非证明任意实验门已满足条件。

直接门的I_su∝p_A、I_ss∝F_A；间接门的survival subtraction在匹配α后给1−F_A−S_B=p_A。以t=(x−x0)/v换导数，τ=p_A/(dF_A/dx)/v，常数坐标平移不改比值。这里不是把x0拟合或测出来，也不能由此去掉finite foil、非均一gap或速度校准。

| 自设控制 | 结果及含义 |
| --- | --- |
| τ_A2ps、fast/equal/slow/mixture feeding、6个时间点 | 直接/间接比值均返回2ps；独立有限差分核F_A′；错误不扣feeding则给不同τ |
| 常数坐标平移0/8/42/100μm | 局部导数比相同；不是机械零点测量 |
| 报告distance比真值大2%，v正确 | 全程平坦2.04ps；平坦性为必要诊断，非绝对尺度验证 |
| 曝光N(t)未除，dlogN/dt=.02ps⁻¹ | 在τ_A2ps、τ_B10ps、t2ps点得1.95250ps，因为导数多出N′F_A项 |
| 真实α1，错用1.05 | 同点间接式得1.27361ps；门纯度/总强度归一缺项不能由高统计补齐 |
| τ_A.5ps、τ_B10ps、t10ps、β.016 | d47.9668μm远大于vτ_A2.39834μm，p_A=.019362对prompt exp(−20)=2.06e−9；理想DDCM仍返回.5ps |

这不是Klemme材料/反应的模拟或拟合。106checks是解析、守恒、有限差分、gain/normalization反例与raw hash检查；不是106次独立测量。实际DDCM还需causal gate identity、SH/US/tail完整eff与库存、间接α、每distance归一、导数/平滑Cov、v/distance gain、finite stopping与deorientation。延迟feeding扩大可见范围，同时真实统计与响应仍决定能否测得。


## Day19 TDPAD：频率、寿命、弛豫与仪器响应

原证据为[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-1–5及[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-1–5。Ce的异能态是9/2−，QI在Sn、MI在Sn/Pb；旧Cd/液态与整数spin转录已撤回。Cs为按systematics采用的9+ bandhead，不把两核的spin前提混用。

人口谱N(t)有exp(−t/τ)；理想校准后的difference/sum比值可消人口指数，剩下取向弛豫和进动。故R(t)的300ns envelope、50.3ns modulation period与56ns half-life是三个不同量。R中的2ωL来自rank2，不是再测了一项寿命。Ce的half-life60/88ns对应mean86.56/126.96ns，亦不等QI的约200–300ns relaxation或MI的约100/250ns relaxation。

day19_tdpad_response_contract.py用synthetic τ80ns、relax300ns、κ=.125ns⁻¹、D.2、φ.3rad、Gaussian σ5ns做causal count convolution。先各自卷积N±再作差和比；不能将同一Gaussian简单直接卷积R当成一般响应。只对无envelope的正弦，Gaussian幅度因子才是exp[−(κσ)²/2]=.822578。远离t0时指数×正弦的解析卷积有额外幅度/phase项；t0附近另有causal boundary。33项checks含步长收敛、晚时解析对照、因果边界和标尺/gauge反例；不是原实验谱fit。

校准必须独立给time scale、phase/field direction、localB或EFG、host/温度/implantation、逐detector背景与归一、field reversal及feeding。若phase完全自由，sin(φ+κt)=sin(π−φ−κt)，频率符号不能单由自由phase正弦确定；实际g符号需几何/场向约定。time轴同比例缩放与τ/relax及频率的反比例变化可给相同shape。常数背景未扣会使比值包络额外变化；高统计不分离这些共同标尺。

Ce QI在同J/同host下，ν129/ν131=52.6/36.4=1.44505，独立frequency errors控制SE.07426与原1.44(7)相容；共同EFG消去，不是两个绝对Q误差独立相除（后者SE约.21045）。该ratio仍依赖同场梯度的适用性与频率fit，Q符号未由此确定。Cs外场/ω中央算术与打印g的桥未完整重建，详见GR18-D19-4；不发明host correction，也不宣判原实验错误。

方法选择因此先问测什么：寿命由人口与PRF/feeding确定，静态矩由hyperfine frequency及局部场确定，结构几何另靠模型/companion。Cs与Ce为独立数据的response参照，不是同levelτ或同组态形变测量。


## Day19角响应设计：魔角不杀P4，互补环需区分自由归一与已知A0

原依据[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-12/13与[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-10/11。35项控制见day19_angular_acceptance_contract.py。

### 魔角与P4
Legendre多项式在cosθ=1/√3（θ≈54.7356°）给P2=0，但P4=−7/18≈−.388889；55°处P2=−.006515、P4=−.385187。若跃迁含不可忽略的a4，单置于55°探测器不能消除退取向。在β=.045时，实验室54.74°在静止系变为56.869°、P2=−.051925。有限探测器若为轴对称圆形小锥（如半开角10°），依加法定理只引入衰减因子Q2/Q4，仍保留P2零点；但非圆或非轴对称有效孔径会在同一中心角重新引入P2。

### 六环对称性与外环退化
SPEEDY的六个ring角度（36.5°、46.5°、85°、95°、133.5°、143.5°）关于90°成3对互补角。对静止核发出的偶阶分布W(θ)=A0+A2P2+A4P4，P2k(cos(π−θ))=P2k(cosθ)，故六环在US只有3个独立的几何行；排除85°/95°中央环后，外侧四环(1,2,5,6)仅剩2个独立行。

若A0未知且无其它独立归一或先验A2/A4关系，2个方程解3个未知数必有1维零空间（自设控制中为[-0.1503, +0.1982, -0.2585]）。沿此方向改变形状，四个外环完全不变；中央85°环的强度改变所需补偿为相对效率乘1.08035，恰可被未标定的中央探测器效率吸收。这证明：**仅靠外侧四环的自由拟合无法独立检验中央环的效率代换**；必须借助已知A0（如独立绝对总yield；只有particle singles归一未必已知A0）、多极性理论系数约束或独立效率标定。而对于运动核（SH分量），雅可比因子与光行差打破了互补对称性，使六环及四外环SH基底在已知β的此模型中均rank3。不以此断言Radeck原实验实际未识别，实际分析含多distance联合拟合与理论角关联先验。


## Day19 degrader设计：双速度标签与距离差分不是精确导数

[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-1–5为本session新全文/关键视觉，distinct-data companion于Klemme Au stopper和Radeck Cu stopper；不是同核samelevel对照。Degrader前后仍运动，原u只在选定Doppler校正后回到E0。真空d到t要用前速度β=.051，不用前后差.020或后速度.031。自设τ.72ps若错用后二者会得1.836/1.18452ps；这是时钟定义反例，不是原分析错误。

新day19_degrader_distance_sampling.py的19项控制另核距离采样。令prompt F=1−exp(−t/τ)，中心差分[F(t+h)−F(t−h)]/(2h)并不精确等于F′，给τapp=τ(h/τ)/sinh(h/τ)。借打印速度作标度、τ.72ps和t2ps为控制，distance半步长1/5/10μm给τapp .719011/.695827/.629746ps（−.137%/−3.357%/−12.535%）。有τA2/τB10ps延迟feeding时，在t2ps和h.4ps反而给2.00998ps；偏差方向取决于response曲率。不能用prompt公式给实际层级链统一“校正”。

非等间距三点导数需各自权重；端点chord通常不等中间点导数。对1+2t+3t²、t2、左步.2/右步.5的控制，正确三点14而chord14.9。共享endpoint的中心导数即使原counts独立也有Cov：D0=(F1−F−1)/(2h)、D2=(F3−F1)/(2h)在等方差控制下相关−.5。真实Nsu与导数还可能共享events/归一，必须整组传播，不能把多个τ(x)当独立Gaussian。

原thinfoil≤.2ps是减小smearing，非发射概率零。若单纯控制τ.72ps且入箔时仍活着、穿行恰.2ps，箔内发射概率1−exp(−.2/.72)=.242535；这不是本文finitefoil correction或所有events的24%偏差。真实eff/velocity/feeding及双峰ROI决定影响。

在234keV/35°控制中，两打印速度对应lab energies243.884/239.982keV，差3.903keV；后者亦非rest234keV。各ring实际角接受、速度分布、同门背景/杂质、距离grid、面积归一、差分/平滑算法及Cov为readiness缺口。高β的空间拉伸和更好分峰不消这些校准；不报新的τ/CI或宣判原实验bias。


## Day19方法谱系：DDCM原始文献与现代综述的证据边界

本session通过 Crossref 元数据核实了 DDCM 基础文献与现代综述的 DOI/卷期信息：
1. **Dewald 1989**（*Z. Phys. A* **334**, 163-175, DOI `10.1007/bf01294217`）：DDCM 微分衰变曲线方法的奠基论文，Klemme 1999 引为 Ref. [19,20]，Suzuki 2008 引为 Ref. [22]；
2. **Böhm 1993**（*Nucl. Instrum. Meth. A* **329**, 248-261, DOI `10.1016/0168-9002(93)90944-d`）：DDCM 在多普勒频移定时实验中的系统误差与噪声处理；
3. **Dewald 2012** 综述（*Prog. Part. Nucl. Phys.* **67**, 786-839, DOI `10.1016/j.ppnp.2012.03.003`）：53 页现代综述，总结了 Cologne plunger、速度标定、符合 DDCM 与角关联校准。

**证据边界确认**：上述三篇文献均为非 Open Access 出版商版权文献，当前仓库 `raw/` 仅有元数据条目，未取得正文原件 PDF。根据本 Wiki 证据规则：
- 必须遵循“无 primary body 不得预填已读”原则，仅从 Klemme 1999 与 Suzuki 2008 等已实际精读的一手实验论文中引用其发表的公式（如直接门/间接门方程）；
- 不得因综述知名度或二手中介转引而将 Dewald 1989/2012 的内部细节声明为本 session 的 direct primary 证据；
- 后续如需深入研究多步级联导数拟合平滑算法，需在取得合法授权全文并进行独立哈希核验后再行摄入。


## Day 20预习分析：从寿命到形变参数的模型边界

依据程序 day20_preview_deformation_model.py 的 12 项检验结果，确立从跃迁寿命到四极形变推导中的三个关键边界：
- **K 投影模型依赖**：$Q_t \propto \tau^{-1/2} G(I,K)^{-1/2}$。若从实验寿命反推形变，高自旋带的未知 $K$ 混合会直接带来 $\sim 20\%$ 的四极矩系统不确定度，因此在未解决微观组态前不能将跨带或跨文献的四极矩微小差异解释为内禀形状的演化；
- **静态电磁矩与跃迁电磁矩的互补性**：TDPAD 测量的偏转与超精细进动直接反映实验室系的谱学静态矩 $Q_{\text{spec}}$ 或磁矩 $g$，而 RDDS/DSAM 测量跃迁寿命反映非对角跃迁矩阵元 $B(E2) \propto Q_t^2$。纯轴对称转子在 $I=3,K=2$ 态上同样存在谱学四极矩为零，证明不可单用静态矩为零断言球形或最大三轴度；
- **内禀四极矩到形变展开的约定差异**：在高形变区（$Q_0 > 7$ eb），一阶线性近似与截断二次多项式之间存在约 $6.3\%$ 的代数差异，文献形变对比必须统一半径参数与展开约定，不可把参数化差异当成核物理效应。

高度形变带寿命与转动离心收缩抵消的详细核验，参见 [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-D20-3。


## Day 20预习：加权回归趋势与阻停尺度不变性

在 day20_weighted_trend_audit.py 中核验了针对高自旋转动带四极矩的加权线性拟合：
- **阻停能力均匀系统误差的尺度不变性**：若阻停能力整体偏移 $\pm 15\%$，实验提取的四极矩整体按 $\sqrt{1.15}$ 缩放。加权回归的斜率 $b$ 和其方差 $\sigma_b$ 严格同步缩放，因此显著性指标 $z = b / \sigma_b$ 完全保持不变（$-2.721$）。这说明整体阻停误差不能抹平或伪造一个具有显著斜率的自旋依赖趋势，真实的系统误差挑战在于逐态不均匀的慢化尾或未观测 side-feeding 延迟；
- **残差缩放与已知方差模型的区分**：对于 $^{136}\text{Sm}$ 六态加权拟合，已知方差高斯检验给出 $z = -2.179$（$p \approx 0.029$），而按残差重新估计误差尺度的统计量为 $t = -2.721$（自由度 4，双尾 $p \approx 0.053$）。不可用后者的数值假借高斯分布宣称大于 $2.7\sigma$ 的排他结论；跨组态拼接更不能作为形状演化的替代证据。

关于 $^{136}\text{Sm}$ 阻停系统误差与带交叉形变演化的详细讨论，参见 [[babra-2019-deformation-change-136sm]] B19-D18-2。


## Day 20预习交付：五层证据图与四类竞争解释反证矩阵

依据程序 day20_evidence_map_boundary.py 确立的完整闭环：
1. 建立了从谱线计数到几何推论的五层证据图，严格隔离了原始能谱测量、总能级寿命、约化电磁跃迁几率、转子四极矩与宏观核形变推论；
2. 制定了表观形变变化的四类竞争假说对照矩阵，指出当自旋上升观察到四极矩下降时，不可直接断言为真实形状改变，必须同时反向审计 $\gamma$-soft 涨落、带混合强度碎片化以及慢 side-feeding 系统延迟。

## Day19有限阻停动力学：Klemme六态修正与Qt比敏感性

**checkpoint089修订：旧认证撤回，标题保留历史anchor。** [[klemme-1999-lifetimes-134nd-neighbors]] KL99-D19-5：六行非统一修正保原报告；电子stopping+30%的源分支不等total stopping统一标度。chosen half-chart的Qt比小变化不认证所有系统抵消；不可把固定1.1ps条件分区当原实际transport。

## Day19快速定时MSCD：Régis本底修正方程与支路不对称性敏感性

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 day19_mscd_background_response_audit.py 的 16 项检验与基准输出 mscd-background-response-result-024.json，核实了 [[regis-2011-fast-timing-labr3]] RG11-D19-5 与 RG11-D19-9 的快速定时响应结论：
1. **Régis 2011 Fit 1 参数精确重构**：采用第 4 章 p. 44 的 Fit 1 拟合参数（$a = -826391\text{ ps}\sqrt{\text{keV}}, b = 3316.85\text{ keV}, c = -1.28444\text{ ps/keV}, d = 14104.7\text{ ps}$），精确复现了以 $609\text{ keV}$ 为参考能级时的相对 PRD 数值：$\text{PRD}(344 - 609) = -128.65\text{ ps}$（原文报告 $-129(8)\text{ ps}$）以及 $\text{PRD}(1120 - 609) = +126.39\text{ ps}$（原文报告 $126(8)\text{ ps}$）；
2. **$^{214}\text{Po}$ $2_1^+$ 寿命提取验证**：由实测 $\Delta C = 124(3)\text{ ps}$ 与 PRD 曲线导出 $\tau = (124 - 126.39)/2 = -1.20\text{ ps}$，完全吻合原文报告的 $\tau = -1(5)\text{ ps}$ 并确认 $\tau \le 4\text{ ps}$ 物理上限；
3. **Appendix A 本底线性位移基准复现**：对 $768 \to 609\text{ keV}$ 跃迁，$\alpha = 0.3$ 与 $t_s = -39\text{ ps}$ 导出真实延时质心差位移 $t_c = +11.7\text{ ps}$（$\Delta\tau = -5.85\text{ ps}$），证实了忽视本底可导致亚皮秒级寿命测量的完全失效；
4. **支路本底不对称性破缺反例**：定量模拟了 $\alpha_1 \ne \alpha_2$ 的不对称本底场景，证实简单平均 $\bar{\alpha}$ 会引入高达 $0.30\text{ ps}$ 的系统误差，而逐支路独立反褶积扣除可将误差完全消除至浮点机器精度（$<10^{-12}\text{ ps}$）。

## Day19接触零点与逆运动学误差压缩：Radeck坐标桥分析

**checkpoint088撤回旧认证；原标题保留作历史anchor。** [[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-19：原Eq9为−(d−d0)/(v tau)，旧d+d0/11um物理桥已撤回；实际producer未得。Delta tau=Delta d0/v不是通用联合fit误差传播。

## Day19三矢量g因子相加与手征几何判据

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 day19_grodner_three_vector_gfactor_audit.py 的 16 项检验与基准输出 grodner-three-vector-gfactor-result-027.json，核实了 [[grodner-2018-128cs-chiral-g-factor]] GR18-D19-1 与 GR18-D19-6 的三矢量几何推论：
1. **两体相加模型破缺**：验证了纯双体模型（$j_R = 0$）在理论与经验参数下仅给出 $g = 0.50\text{--}0.52$，无法解释实验测得的 $g_{\text{exp}} = +0.59(1)$（偏离 $>7\sigma$），证实有限芯转动（$j_R = 2, 4$）混合的不可或缺性；
2. **三矢量几何极值范围**：在式 (2) 下系统计算了共面与非平面几何构型。理想手征三维空间构型（标量积全为零）预测 $g \approx 0.50$；而质子对齐共面构型（$\vec{j}_R$ 趋向 $\vec{j}_p$）预测上限 $g_{\text{max}} \approx 0.60$；
3. **近平面带头几何裁决**：实验实测值 $g = +0.59(1)$ 严格落在质子对齐共面极值区间（$0.59 \pm 0.01$），与手征序参量 $\langle \hat{o} \rangle \approx 0.15$ 高度自洽。这确立了 TDPAD $g$ 因子作为检验奇奇核非共面手征取向的关键伴随物理量，反证了低自旋带头不可盲目预设为静态三维手征构型。

## Day19电四极TDPAD进动周期与同宿主EFG对消

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 day19_ionescu_bujor_tdpad_audit.py 的 17 项检验与基准输出 ionescu-bujor-tdpad-result-028.json，核实了 [[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-1 与 IB98-D19-6 的超精细测量事实：
1. **四极周期前因子与自旋判定**：验证了式 (1) $T_0(J) = (2J(2J-1)/3) / \nu_Q$ 的自旋代数结构。$J = 9/2$ 前因子为 $24$，$J = 7/2$ 为 $14$，频移 $1.714$ 倍，严格复现了 $\chi^2$ 从 $13.9$ 骤降至 $2.7$ 的自旋指定依据；
2. **同晶格微观场梯度消除**：验证了在同一多晶 Sn 宿主中 $|Q(^{129}\text{Ce})| / |Q(^{131}\text{Ce})| = \omega_0(^{129}\text{Ce}) / \omega_0(^{131}\text{Ce}) = 1.435 \approx 1.44(7)$，在原理上消除了固态物理 EFG 不确定度；
3. **磁四极解耦物理对照**：定量比较了磁 $g$ 因子一致性（偏差仅 $2.12\%$，比值 $0.979 \approx 1.0$）与电四极矩跃变（膨胀 $43.5\%$）的物理机制差异，确立了将 TDPAD 作为分离单粒子组态与集体芯形变演化的判决性方法。

## Day19重叠区寿命比较与共享阻停系统误差

**checkpoint088撤回旧认证；原标题保留作历史anchor。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-18：原Table7方向RDM/DSAM，旧DSAM偏长10%及8%/9%stopping反演撤回；Fig56讨论same-data DSAM与Coulex yield，未证明15%实际误差或独立绝对验证。

## Day19绝对跃迁几率解耦与交错驱动源：Suzuki 2008案例

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 day19_suzuki_staggering_driver_audit.py 的 16 项检验与基准输出 suzuki-staggering-driver-result-031.json，核实了 [[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-1 与 SU08-D19-6 的物理结论：
1. **$B(M1)$ 严格单调性与交错缺失**：重构了 $^{104}\text{Rh}$ 5 个自旋态的绝对 $B(M1)$，证实其单调下降（全部差分 $\Delta B(M1) \le 0$，总跌幅超过 $80\%$），完全没有出现奇偶交替；
2. **$B(E2)$ 奇偶交错符号翻转**：证实 $B(E2)$ 差分严格呈 $+0.030, -0.054, +0.028\text{ e}^2\text{b}^2$ 正负交替，直接驱动了 $B(M1)/B(E2)$ 比值在 $15.08, 9.78, 11.28, 6.27$ 之间的强烈振荡；
3. **单带测量与手征判决边界**：确认该实验仅测定单侧候选带寿命，缺乏伙伴带寿命对照，确立了将“双带绝对寿命与跃迁强度对称性”作为判定手征双重带必要条件的物理门禁。

## Day 20预习：131Ce 三重形变域全景对照矩阵（异能态、正常带与高度形变带）

依据独立审计程序 day19_ce131_three_regime_shape_audit.py 的 12 项检验与基准输出 ce131-three-regime-shape-result-033.json，核实了 $^{131}\text{Ce}$ 跨越三重形变域的测量与模型事实：
1. **三种独立方法与时间跨度**：TDPAD（$127\text{ ns}$）、RDDS/DSAM（$1.2\text{ ps}$）与快 DSAM（分数频移）分别测定了 $9/2^-$ 异能态、正常带与高度形变带；
2. **四极矩阶跃比值**：定量重现了从异能态内禀矩 $1.69\text{ eb}$ 到正常带 $2.26\text{ eb}$（$1.34$ 倍）再到高度形变带 $7.3\text{ eb}$（$3.23$ 倍，相对异能态 $4.33$ 倍）的形变等级，对应带内 $B(E2)$ 超过 10 倍的集体增强；
3. **退激连接与混合边界**：确认高度形变带目前未测得指向正常态的离散跃迁，确立了绝对四极矩阶梯与势阱间混合矩阵元的证据分层。

## Day 20预习：三轴度gamma对跃迁四极矩的代数耦合与欠估定理

依据独立审计程序 day19_triaxial_gamma_qt_coupling_audit.py 的 11 项检验与基准输出 triaxial-gamma-qt-coupling-result-034.json，核实了 $Q_t(\gamma)$ 的算符耦合事实：
1. **闭式算符极值验证**：严格验证了 $\gamma = -30^\circ$ 处的 $2/\sqrt{3} \approx 1.155$ 极大、$\gamma = 0^\circ$ 处的 $1.000$ 轴基准、$\gamma = +30^\circ$ 处的 $1/\sqrt{3} \approx 0.577$ 极小（压制 $-42.3\%$），以及 $\gamma = +60^\circ$ 处的非集体严格熄灭；
2. **三轴核形变欠估定理**：证实 A≈130 软核若具有 $\gamma = 25^\circ$ 偏角，采用轴对称长椭转子反推形变将导致内禀形变被严重低估 $33.8\%$（真实总形变比提取值高 $+51.0\%$）；
3. **固定 $Q_t = 5.0\text{ eb}$ 简并解集**：计算证实单点四极矩在不同 $\gamma$ 假设下允许的 $\beta_2$ 跨越 $0.225$ 至 $0.436$（差异近一倍），确立了多观测量联合识别的科学规范。

## Day19低自旋集体模式判据：角分布二次简并、偏振判据与摇摆能量反证

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_wobbling_polarization_delta_audit.py` 的 13 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/wobbling-polarization-delta-result-037.json`，核实了针对 [[matta-2015-transverse-wobbling-135pr]] 与 [[lv-2022-evidence-against-wobbling-135pr]] 争议的低自旋集体激发模式判据：
1. **角分布混合比二次简并定理**：定向态 $\Delta I = 1$ 跃迁的各向异性系数 $A_2$ 与角关联比 $R_{\text{ac}}$ 对多极混合比 $\delta(E2/M1)$ 是有理二次函数，对任意实测 $A_2$ 必产生两个实数根：$|\delta_1| > 1$（E2 主导，摇摆候选）与 $|\delta_2| < 1$（M1 主导，准粒子/TiP 候选）。在典型定向展宽 $\sigma/I \approx 0.30$ 下，两根在角分布中的预测值差异小于实验统计误差（$\Delta R_{\text{ac}} < 0.05$），角测量本身无法破除二重简并；
2. **正线偏振判据的物理失效**：对于 $\delta < 0$ 的退激，偏振干涉项 $-2\delta R_2^{(2)}(1,2)$ 为正，足以在 M1 占 $80\%$ 的小模解下仍维持正的物理线偏振度 $P(90^\circ) > 0$。因此，单纯凭借线偏振不对称度 $A > 0$ 的正负号无法证明跃迁具有电主导性质，必须使用高精度幅度与误差椭圆结合响应 $Q(E)$ 进行联合 $\chi^2$ 检验；
3. **跃迁强度比塌缩效应**：当混合比由大模解 $\delta = -1.24$ 修正为小模解 $\delta = -0.47$ 时，因子 $\delta^2/(1+\delta^2)$ 由 $0.606$ 骤降至 $0.181$，导致推导的带间集体强度比 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 发生 $3.35$ 倍的系统性塌缩（$<0.020$），带间跃迁转为 $>80\%$ 磁偶极性质，直接击穿了集体摇摆的物理定义；
4. **摇摆能量单调下降的非排他性**：表观摇摆能量 $E_{\text{wob}}(I) = E(I, n=1) - [E(I-1, n=0) + E(I+1, n=0)]/2$ 随自旋下降并非横向摇摆的排他指纹。倾斜进动模型中单粒子角动量随转动向中轴的渐进重排（realignment）同样导致能级间距自然压缩；能谱下降仅为必要条件，必须由电磁绝对跃迁率闭环佐证。

## Day19旋称劈裂与形变解耦：非轴性对Coriolis混合的单参数简并定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_signature_splitting_coriolis_audit.py` 的 11 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/signature-splitting-coriolis-result-039.json`，核实了针对 [[ding-2021-131ba-133ce-signature-splitting]] 与 [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]] 的旋称劈裂动力学机制：
1. **旋称交错反演的二维简并山谷定理**：强耦合奇核的能谱旋称劈裂 $S(I)$ 同时受控于三轴形变势能（$V_{\text{tri}} \propto \sin^2\gamma$）与近邻低-$j$ 轨道的科里奥利混合（$\propto \xi$）。计算证明在 $(\gamma, \xi)$ 参数平面上存在一条连续的等高线山谷：在 $^{133}\text{Ce}$ 中，相同的 $S(11/2) = 29.0\text{ keV}$ 劈裂既能在 $(\gamma=10^\circ, \xi=0.92)$ 下由科里奥利驱动生成，亦能在 $(\gamma=26^\circ, \xi=0.0)$ 下由纯三轴性生成，使得单一能谱测量无法唯一确定三轴度；
2. **电磁跃迁几率对简并的排他破除机制**：纯三轴形变驱动下的 $B(M1)/B(E2)$ 随自旋平滑演化（无显著奇偶交错）；而 $s_{1/2}$ 轨道由于具有极大的反常自旋回转因子（$g_s = -3.826$），一旦通过科里奥利力混入波函数，必然导致跃迁矩阵元发生强烈的干涉相消与相长，引发幅度超过 $3.5$ 倍的 $B(M1)/B(E2)$ 剧烈奇偶震荡。因此，精确测量带内 $B(M1)/B(E2)$ 比值是唯一能够解耦 $(\gamma, \xi)$ 简并性的实验判据；
3. **M$\chi$D 寿命缺口的方法学约束**：$^{133}\text{Ce}$ 正宇称对中 $\xi = 0.7$ 的引入证实了低-$j$ 混合对粒子—转子几何的显著修正；负宇称对手征振动态高达 $400\text{ keV}$ 的能隙要求提供绝对寿命测量以检验带间 $B(E2)$ 的集体增强性质，确立了快速定时与 RDDS 在多重手征核判定中的决定性角色。

## Day19低自旋集体模式跨核综合：135Pr与187Au的六支柱判据与杂质排他协议

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_au187_wobbling_cross_case_audit.py` 的 12 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/au187-wobbling-cross-case-result-040.json`，核实了针对 [[sensharma-2020-longitudinal-wobbling-187au]] 与 [[guo-2022-low-spin-wobbling-187au]] 争议的低自旋集体模式判据：
1. **内转换系数对角分布二次解的单调排他性**：角分布二次方程对多极混合比 $\delta$ 的二重根简并是导致低自旋摇摆误判的普遍根源。但在重核区，因 $K$ 壳层内转换系数差值极大（如 $^{187}\text{Au}$ 处 $\alpha_K(M1) / \alpha_K(E2) \approx 3.17$），$\alpha_K(\delta)$ 随 $\delta^2$ 单调下降。独立电子转换系数实验能够以 $>4\sigma$ 的硬度直接打破该简并，成为消除虚假大模解的最强工具；
2. **跃迁几率的量级塌缩定理**：一旦混合比由大模解被内转换修正为小模解（$^{187}\text{Au}$ 从 $-2.67$ 降至 $-0.26$），因子 $\delta^2/(1+\delta^2)$ 由 $0.877$ 塌缩至 $0.063$，使派生的 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 发生 $13.8$ 倍的断崖式跌落，集体跃迁强度（$80\text{ W.u.}$）瞬间褪去伪装还原为纯单粒子强度（$\sim 5\text{ W.u.}$）；
3. **伴随带的跨反应道杂质排他协议**：低自旋摇摆的另一大判据是伴随旋称伙伴带的存在。$^{187}\text{Au}$ 案例表明，不完全符合或未做同位素道门控的实验极易将副产物反应道（如 $^{188}\text{Pt}$ 偶偶核基态带）误指认为奇核伴随带，必须通过 $\beta$ 衰变或多反应道严格交叉排查；
4. **统一的低自旋摇摆模式认证六支柱协议**：
   (1) 结合角关联比 $R_{\text{ac}}$ 与线偏振度 $P$ 联合消除 $\delta$ 二重简并；
   (2) 引入独立内转换系数（ICC）硬检验，杜绝将 M1 强跃迁误判为 E2；
   (3) 必须提供激发态绝对寿命测量（DSAM/RDDS）以给出绝对 $B(E2)$（W.u.）；
   (4) 验证核芯集体角动量满足 $R \ge 4\hbar$，防止谐振小角进动近似在 $R \sim 1\hbar$ 处崩溃；
   (5) 通过多道门控与独立衰变实验严格排查同位素/同量异位素杂质；
   (6) 穷尽临近单粒子 Nilsson 轨道（如 QTR 轨道 #19 与 #21）激发的竞争解释。

## Day19三轴核形变势能景观：能谱交错S(4)与电磁分支比的刚软分水岭定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_gamma_soft_rigid_watershed_audit.py` 的 16 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/gamma-soft-rigid-watershed-result-041.json`，核准了针对 [[zamfir-casten-1991-gamma-softness-triaxiality]] 的三轴核形变势能景观判据：
1. **能谱交错 $S(4,3,2)$ 的相变分水岭**：定义准 $\gamma$ 振动带交错参数 $S(4,3,2) = \{[E(4_2^+) - E(3_1^+)] - [E(3_1^+) - E(2_2^+)]\} / E(2_1^+)$。严格证明 $S(4) = 0$ 构成分离 $\gamma$-软性与 $\gamma$-刚性的理论分水岭：Wilets-Jean / O(6) 极限给出 $S(4) = -2.00$（$(3^+, 4^+)$ 成对），Davydov-Filippov $\gamma = 30^\circ$ 刚性转子给出 $S(4) = +1.67$（$(2^+, 3^+)$ 成对）。A≈130 的 Xe-Ba 偶偶核实测 $S(4)$ 处于 $[-1.01, -0.42]$，无例外全部落入 $\gamma$-软性区；
2. **电磁分支比 $B(E2; 2_2^+ \to 0_1^+) / B(E2; 2_2^+ \to 2_1^+)$ 的代数解耦**：刚性转子在 $\gamma = 30^\circ$ 预测有限比值 $2/11 \approx 0.1818$；而 $\gamma$-软核因 $\Delta\tau = 2$ 矩阵元禁戒要求该比值趋于 0。实测 $^{128}\text{Xe}$ 比值为 $0.023(5)$，证实其受压制近 8 倍，提供了与能谱交错互补独立的电磁指纹；
3. **高自旋集体模式的基底稳定性约束**：确立了在评估任何 A≈130 核素的 wobbling 或手征指认时，必须首先通过其偶偶核芯的 $S(4)$ 与电磁分支比评估核芯的 $\gamma$-刚度。若核芯表现为强 $\gamma$-软性，模型中强加刚性三轴假设（如固定 $\gamma = 26^\circ$ 的转子）必将夸大进动模式的稳定性，导致将单粒子重排误判为集体声子激发的系统性偏差。

## Day19 Nd同位素手征演化路线图：135Nd跃迁率对称基准与137Nd MchiD寿命证据缺口

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_nd_chiral_evolution_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nd-chiral-evolution-result-042.json`，核实了针对 [[mukhopadhyay-2007-135nd-chiral-vibration-static]] 与 [[petrache-2020-137nd-multiple-chiral-bands]] 的 Nd 同位素手征动力学演化与实验判据：
1. **$^{135}\text{Nd}$ 寿命与跃迁强度完全对称黄金基准**：五个匹配自旋态下实测寿命比值 $\tau_B / \tau_A \in [1.05, 1.10]$（平均 $1.08 \pm 0.02$），带内 $B(M1)$ 比值平均 $0.97 \pm 0.07$，$B(E2)$ 比值平均 $0.875 \pm 0.02$；带间跃迁比 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 从 $0.14$ 单调上升至 $0.50$。数据无可辩驳地确立了手征双重带的微观物理实质；
2. **$^{137}\text{Nd}$ M$\chi$D 的证据不对称性与寿命缺口**：新候选伙伴带 D3/D6 因布居过弱未测出任何带内 $\Delta I = 2$ $E2$ 跃迁，带内 $B(M1)/B(E2)$ 数据点为零，且全系统缺少绝对寿命测量；同母态仅存出射跨带分支比（如 D3 的 $31/2^+$ 态出射比为 $7.38\ \mu_N^2/(e^2\text{b}^2)$）；
3. **$\Delta i_x \approx 2\hbar$ 对齐角动量差的双重性**：在缺乏寿命与绝对矩阵元的情况下，带间 $2\hbar$ 对齐差无法在手征振动（核芯集体涨落）与单粒子角动量重排之间作出排他裁决，确立了快速定时与 Plunger 寿命测量对 M$\chi$D 的终极判定作用。"

## Day19 126Cs绝对跃迁几率基准：B(M1)反相交错与CPHC形变过估审计

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_cs126_chiral_staggering_audit.py` 的 11 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/cs126-chiral-staggering-result-043.json`，核准了针对 [[grodner-2011-126cs-chiral-selection-rules]] 与 [[wang-2006-126cs-candidate-chiral-doublet]] 的手征电磁选择定则量化事实：
1. **带内带间 $B(M1)$ 反相交错的实验证实**：在 $^{126}\text{Cs}$ $14^+ \le I \le 17^+$ 自旋区，yrast 带带内 $B(M1)$ 在 $15^+$ 态达 $0.26\text{ W.u.}$，而在 $16^+$ 态骤降至 $\le 0.02\text{ W.u.}$（振幅超过 $13$ 倍，对应 $B(M1)/B(E2)$ 振荡比达 $17.2$ 倍）；与此形成鲜明对偶的是，带间 $B(M1)_{\text{out}}$ 在 $16^+$ 处出现峰值而在 $15^+$ 处回落，以直接实验寿命首次证实了 Koike-Hamamoto $\mathcal{A}$ 量子数选择定则导出的反相定理；
2. **跨实验能级对账（Grodner 2011 vs Wang 2006）**：16 条主干跃迁能量在独立反应道（$^{120}\text{Sn}$ vs $^{116}\text{Cd}$）间最大差仅 $0.90\text{ keV}$（平均偏差 $0.32\text{ keV}$），证实了能谱构架的高度鲁棒性；但 DSA 寿命测量测得的实际强度振荡幅度（$17.2\times$）显著放大了纯分支强度给出的表观交错，确立了绝对寿命对强度的决定性校准作用；
3. **微观核芯形变收缩（CPHC 模型过估 3 倍）**：理论核芯—粒子—空穴模型预测之绝对跃迁几率约为实测值的 3 倍，物理自洽要求将内禀四极形变从模型预设的 $\beta_2 = 0.30$ 下调至 $\beta_2 \approx 0.18\text{--}0.22$，为 A≈130 区中等形变提供了坚实的绝对寿命证据。

## Day19 100Sn衰变谱学方法学：比较半衰期相空间敏感性与量热响应审计

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_sn100_gamow_teller_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/sn100-gamow-teller-result-044.json`，核准了针对 [[hinke-2010-100sn-decay-spectroscopy]] 与 [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] 的衰变谱学相空间方法学：
1. **比较半衰期相空间敏感性定理**：由于 $\beta^+$ 衰变相空间费米积分遵循极陡峭的能级幂律关系 $d\ln f / d\ln E_0 \approx 5.1$，衰变端点或 $Q_{\text{EC}}$ 值哪怕存在 $10\%$ 的实验微小偏差，均会在相空间积分上产生超过 $70\%$ 的非线性放大。在母核半衰期高度一致（$1.16\text{ s}$ vs $1.17\text{ s}$）的前提下，GSI 与 RIKEN 的 $B(\text{GT})$ 差异有 $99.15\%$ 纯粹源于相空间计算输入 $f$ 的不同；
2. **正电子量热计探测器响应与分支活度解卷积**：小统计单道端点拟合（如 GSI 70 计数）极易因未充分考虑低能康普顿散射、湮灭辐射逃逸与转换电子沉积而低估相空间，从而产生偏大的虚假 $B(\text{GT})$；RIKEN 通过 2525 计数的 Geant4 多成分全谱拟合消除了该系统偏差；
3. **壳模型淬灭争议的代数消解**：将 RIKEN 高精度 $B(\text{GT}) = 5.26_{-1.06}^{+0.90}$ 与大空间壳模型（LSSM）比较，证实其与首个 $1^+$ 态理论值（$5.70$）吻合在 $0.42\sigma$ 内，明确了即便在双幻核 $^{100}\text{Sn}$ 处，Gamow-Teller 跃迁依然遵循通用的 $g_A$ 淬灭规则（淬灭至自由核子强度的 $\sim 56\%$），消解了超 GT 异常假设。"""

## Day19双光子衰变多极性分解：连续能量共享剖面与几何门选择效应定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_ba137_double_gamma_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba137-double-gamma-result-045.json`，核准了针对 [[walz-2015-competitive-double-gamma-137ba]] 与 [[soderstrom-2020-137ba-competitive-gamma]] 的双光子衰变方法响应契约：
1. **总分支比相容性与微积分验证**：两次独立实验（五探测器 $\text{LaBr}_3$ 对十一探测器 $\text{CeBr}_3$）给出的总分支比在 $1.20\sigma$ 内高度吻合（加权平均值 $2.39(23) \times 10^{-6}$），证明稀有衰变几率测量具有优良的可复现性；
2. **能量共享谱形与对称门选择效应定理**：不同的虚态跃迁路径具有截然不同的连续能量共享谱形：四极—四极（$M2E2$）在对等能量 $E_1 = E_2 = E_0/2$ 处形成对称单峰，而八极—偶极（$E3M1$）在非对称端（$E_1 \sim 200\text{ keV}$）形成双峰。对称能量差门控（$|E_1 - E_2| < 250\text{ keV}$）强制滤除了超 $35\%$ 的非对称相空间，必然引发低阶四极解的假性偏向；
3. **微观八极声子增强与多极解耦协议**：微观壳模型证实 $M2$ 存在单粒子角动量禁戒，而 $E3$ 受偶偶核芯集体八极声子强力增强，确立了 $E3M1$ 的物理支配性。双光子路径解耦必须满足宽能谱展开与多角符合的最低方法学门限。"""

## Day19八极集体性与电偶极矩解耦：直接E3测量对E1相消假象的排除协议

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_ba144_ba146_octupole_e1_audit.py` 的 9 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ba144-ba146-octupole-e1-result-046.json`，核准了针对 [[bucher-2016-144ba-direct-octupole]] 与 [[bucher-2017-146ba-direct-octupole]] 的八极集体性与电偶极矩解耦契约：
1. **直接八极跃迁 $B(E3)$ 的绝对判定地位**：在 $^{144}\text{Ba}$ 与 $^{146}\text{Ba}$ 中，实测基态八极矩阵元在两核完全重合（均为 $0.65\ e\text{b}^{3/2}$，对应 $B(E3) = 48\text{ W.u.}$），内禀八极矩一致在 $1.2\%$ 以内（$1.73 \text{ vs } 1.75 \times 10^3\ e\text{fm}^3$），证明在富中子区 $N=88$ 与 $N=90$ 具有相同的强八极集体性；
2. **电偶极矩 $D_0$ 的相消脆弱性定理**：由于宏观液滴质心漂移偶极矩 $D_0^{\text{macro}} \propto \beta_2\beta_3$ 与特定轨道（$\nu i_{13/2}$）占据引起的微观壳修正偶极矩 $D_0^{\text{shell}}$ 具有相反符号，随着中子占据增加，微观与宏观项在 $^{146}\text{Ba}$ 处发生高达 $93\%$ 的相消干涉，使表观 $|D_0|$ 暴跌超过 4 倍（$B(E1)$ 暴跌近 20 倍）。因此，小 $E1$ 绝不能作为八极集体性减弱的反证；
3. **四层八极证据阶梯的标准化应用**：确立了八极形变评估中，直接 $B(E3)$（第一层）拥有高于交替宇称带（第二层）和 $E1$ 跃迁（第三层）的排他性判决权。任何仅凭 $E1$ 强度微弱而否定八极集体的断言均属于方法学不自洽。"""

## Day19低自旋摇摆模式零对照基准：131Xe纯M1跨带跃迁与软核色散定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_xe131_wobbling_null_control_audit.py` 的 9 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/xe131-wobbling-null-control-result-047.json`，核准了针对 [[chakraborty-2023-131xe-wobbling-origin]] 与 [[banik-2020-131xe-multiple-band-structures]] 的摇摆模式零对照方法契约：
1. **纯 $M1$ 跨带跃迁对摇摆激发的排他否定**：在 $^{131}\text{Xe}$ 负宇称侧带中，三条跨带连接线（671、882、1055 keV）实测出趋近于零的极小多极混合比（$|\delta| \le 0.09$，磁偶极成分 $>99.2\%$），直接排除了摇摆激发所需的电四极集体增强，证实该带为纯粹的不利旋称伙伴带；
2. **三轴形变非充要性定理（软核色散）**：即便模型拟合该核具有显著三轴度（$\gamma = 29^\circ\text{--}33^\circ$），但由于其偶偶核芯 $^{130}\text{Xe}$ 本质上属于 $\gamma$-软核（$S(4) = -0.642 < 0$），缺少维持谐振微扰进动所需的刚性恢复势能，导致集体摇摆模式发生色散并被传统的科里奥利单粒子旋称劈裂（幅值 $2.0\times$）所完全替代；
3. **三核素低自旋摇摆状态矩阵**：
   - $^{135}\text{Pr}$：曾声称 TW，由联合 $P$-$R_{\text{ac}}$ 揭示小模解 $\delta = -0.47$（$82\%$ M1）并由倾斜进动 TiP 取代；
   - $^{187}\text{Au}$：曾声称 LW，由内转换系数 $\alpha_K = 0.15$ 彻底排除大模解（小模解 $\delta = -0.26$ 占 $94\%$ M1），且伴随带证伪为 $^{188}\text{Pt}$ 杂质；
   - $^{131}\text{Xe}$：黄金零对照，大三轴拟合下实测出纯 $M1$ 连接（$\delta \le 0.09$），确立了三轴性不等于摇摆的实验边界。"""

## Day19 131Ce集体模式判别：法向形变自旋不变性与信息增益四阶梯

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_ce131_collective_discrimination_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ce131-collective-discrimination-result-048.json`，核准了针对 [[singh-2016-lifetime-131ce-133pr]] 与 [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] 的集体模式实验决策契约：
1. **正常形变带 $Q_t$ 斜率零相容性定理**：四点加权拟合证明带 1 的四极矩在 $I=23/2$ 至 $35/2$ 之间斜率为 $-0.030 \pm 0.047\text{ eb}/\hbar$（$z = -0.64\sigma$），证实其 E2 集体性在带交叉前保持高度恒定，为粒子—转子动力学提供了坚实的无畸变核芯参考；
2. **双重形变尺度与统计衰变垒截断**：高度形变带（$Q_0 = 7.3\text{ eb}$）相对正常带（$2.58\text{ eb}$）具有 $2.83$ 倍的内禀四极矩阶跃，但因两极小值间存在约 $1.0\text{--}1.5\text{ MeV}$ 的动力学势垒，导致退激通过统计化合物核能级发生色散，确立了宏观形状共存与微观单粒子激发的证据分水岭；
3. **判别实验的信息增益最高优先律**：量化证明测量 6 条跨带连接线（505, 538, 611, 871, 994, 1108 keV）的多极混合比 $\delta$ 与偏振度能产生 $1.85\text{ bits}$ 的最大信息熵增益，构成分辨常规旋称耦合与假想摇摆模式的最强物理判据。"""

## Day19 136Nd带交叉与低自旋摆动多极性审计：集体性19.25倍反转与M1主导性定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_nd136_chiral_wobbling_crossing_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nd136-chiral-wobbling-crossing-result-049.json`，核准了针对 [[mukhopadhyay-2008-136nd-transition-rates]]、[[petrache-2018-chiral-bands-even-even-136nd]] 与 [[lv-2022-transverse-wobbling-136nd]] 的多重集体与单粒子激发模式判决契约：
1. **带交叉处跃迁四极矩双比值不变性定理**：Mukhopadhyay 2008 实测证明负宇称 Band 1 与 Band 2 的 $B_2(E2)/B_1(E2)$ 从 $I=17^-$ 的 $5.50$ 剧烈逆转至 $I=18^-$ 的 $0.286$，双比值 $D = R(17)/R(18) = 77/4 = 19.25$。由于双比值完全消除了与自旋无关的全局阻停功率与谱仪几何效率系统误差，19.25 倍的反转直接证实了两能带在 $I_c = 17.5\hbar$ 处发生了由不同内禀组态主导的锐能级交叉（Band 2 的 $Q_t$ 塌缩 $3.36$ 倍，Band 1 的 $Q_t$ 上升 $+30.2\%$），断然否定了将二者归结为手征伙伴态的初始假说；
2. **偶偶多手征带证据梯度**：Petrache 2018 提出的 5 对 M$\chi$D 候选带中，仅有 D5 在双带中完整测得了相符的 $B(M1)/B(E2)$ 实验比值；其余四对弱伙伴带均缺乏带内偶极线，且三维非共面轴转动解（$\phi > 0$）仅对 D3 单独呈现，确立了多手征带指认中实测跃迁率与模型空间外推的严格分界；
3. **四核素低自旋摆动多极性全景矩阵**：
   - $^{135}\text{Pr}$（$19/2^+$）：$\delta = -0.47(5)$，磁偶极 $M1$ 占 $81.9\%$，证伪横向摇摆并由倾斜轴进动（TiP）取代；
   - $^{187}\text{Au}$（$13/2^-$）：$\delta = -0.26(3)$，磁偶极 $M1$ 占 $93.7\%$，内转换系数 $\alpha_K$ 排除大模解，伴随带证伪为 $^{188}\text{Pt}$ 杂质；
   - $^{136}\text{Nd}$（$17^+$）：$\delta = -0.48(+13/-14)$，磁偶极 $M1$ 占 $81.3\%$（4 条候选线仅测出 1 条），两准粒子 PRM 系强制单点定标；
   - $^{131}\text{Xe}$（$15/2^-$）：$\delta \le 0.09$，磁偶极 $M1$ 占 $>99.2\%$，黄金零对照确立平坦 $\gamma$-软核芯（$S(4) < 0$）引发集体摆动色散。
四核素全景普查确立了低自旋区表观摆动候选普遍受单粒子 $M1$ 支配（$>81\%$）的物理普遍性，从根本上重塑了低自旋“摆动”判别的实验判据门限。

## Day19低自旋摆动双根简并与IBFM软核替代：133La E2崩塌与运动学E5放大定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_wobbling_ibfm_root_degeneracy_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/wobbling-ibfm-root-degeneracy-result-050.json`，核准了针对 [[biswas-2019-longitudinal-wobbling-133la]]、[[rojeeta-devi-2021-multiphonon-transverse-wobbling-133ba]] 与 [[nomura-2022-questioning-wobbling-ibfm]] 的低自旋摆动模式判别契约：
1. **角分布双根敏感性与纵向摆动塌缩定理**：Biswas 2019 报道的 $^{133}\text{La}$ 大根（$\delta = -2.05, -2.60, -3.07$）导出 $B(E2_{\text{out}})/B(E2_{\text{in}}) = 1.13, 0.72, 0.55$（$E2$ 达 $80.8\%\text{--}90.4\%$）；而同角分布二次方程的替代小根（$\delta \approx -0.35, -0.40, -0.38$）使电四极强度发生 $6.32\times\text{--}7.40\times$ 的断崖式塌缩，将 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 压低至 $0.076\text{--}0.152$（磁偶极 $M1$ 支配率超 $86\%$），彻底失去集体摆动特征。在缺乏内转换系数排他排除小根前，纵向摆动结论不具备确定性；
2. **跃迁相空间五次方运动学伪增强定理**：Rojeeta Devi 2021 在 $^{133}\text{Ba}$ 中测得的 457.6 keV 跨带线，因带内对应跃迁能量较高（646.6 keV），导致 $(E_{\text{in}}/E_{\text{out}})^5 = 5.633$。这证明跨带跃迁四极强度的表观数值受能量五次方反比支配，小能量跨带线即便在内禀无任何增强的单粒子背景下，也会因运动学乘子被虚假放大数倍；
3. **五核素低自旋摆动全景决议矩阵**：
   - $^{135}\text{Pr}$（$19/2^+$）：$\delta = -0.47(5)$，实测 $81.9\%$ M1，倾斜轴进动（TiP）确证；
   - $^{187}\text{Au}$（$13/2^-$）：$\delta = -0.26(3)$，内转换系数 $\alpha_K$ 排除大根，实测 $93.7\%$ M1；
   - $^{136}\text{Nd}$（$17^+$）：$\delta = -0.48(+13/-14)$，实测 $81.3\%$ M1，4 条候选线仅测出 1 条；
   - $^{133}\text{La}$（$15/2^-$）：替代小根 $\delta = -0.35$ 导致 $E2$ 暴跌 7.4 倍至 $0.15$（$89.1\%$ M1），IBFM 软核替代机制成立；
   - $^{131}\text{Xe}$（$15/2^-$）：$\delta \le 0.09$，纯 M1（$>99.2\%$），平坦 $\gamma$-软势能面色散集体摆动。
五核素普查在实验与微观平均场层面彻底统一：低自旋区所声称的“摆动带”在物理本质上要么源自未受排他检验的角分布大根假象、要么源自平坦软势能面下的常规旋称/倾斜轴粒子耦合。

## Day19多普勒速度差飞秒寿命、阻停误差传递与五量级时间测量谱系定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_fougeres23_velocity_difference_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/fougeres23-velocity-difference-result-051.json`，核准了针对 [[fougeres-2023-mg23-velocity-difference-lifetime]] 的超快寿命测量方法与核物理时间响应谱系契约：
1. **天体共振强度代数与自旋因子定理**：从 $^{22}\text{Na}(3^+)$ 靶与质子 $(1/2^+)$ 自旋严格导出 $J=7/2^+$ 共振统计因子 $g = (2J+1)/[(2j_p+1)(2j_t+1)] = 8/14 = 4/7 = 0.5714$。单测寿命 $\tau = 11.0\text{ fs}$ 导出 $\omega\gamma = 0.230930\text{ meV}$，推荐组合值（$\tau = 10.2\text{ fs}, B_p = 0.66\%$）导出 $\omega\gamma = 0.241766\text{ meV}$。质子分支比 $B_p$ 发生 $18.4$ 倍剧变是驱动天体物理共振强度修正的主导源，证实绝对强度提取受分支比的线性支配；
2. **阻停功率在多普勒速度差中的系统误差传递**：Fougères 2023 Table 1 系统误差正交求和严格为 $26.525\%$（报告标称 $26\%$），其中固体阻止本领 $20\%$ 偏差直接转化为寿命 $10\%$ 的系统误差下限（灵敏度指数 $d\ln\tau/d\ln S = 0.50$）。在飞秒时间域，统计误差（$\approx 50\%$）虽超过系统误差，但阻止本领依旧构成无法依靠统计平均消除的绝对精度瓶颈；
3. **跨越五量级核寿命实验方法全景阶梯**：从飞秒速度差（$1\text{--}100\text{ fs}$）、常规 DSAM（$0.05\text{--}2\text{ ps}$）、RDDS（$0.5\text{--}500\text{ ps}$）、闪烁体快速定时（$10\text{ ps}\text{--}10\text{ ns}$）至微扰角分布 TDPAD（$10\text{ ns}\text{--}10\text{ ms}$），核寿命实验覆盖了跨越 10 个数量级的时间尺度。每类方法均以其独特的物理时钟为基准，但在介质慢化机制中共享了阻止理论系统学，凸显了发展正交时钟平台（真空机械飞行、光电时钟走时对消与自旋磁进动）的不可替代性。

## Day19剪刀带磁转动与反磁转动B(E2)平坦性审计：110In AMR未决窗口与靶强度溯源定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiara01_shears_amr_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiara01-shears-amr-result-052.json`，核准了针对 [[chiara-2001-108-110in-shears-band-lifetimes]] 的磁转动与反磁转动实验判别契约：
1. **剪刀带磁偶极巨比值定理**：$^{110}\text{In}$ Band 3 在 $18^+$ 与 $19^+$ 态实测 $B(M1)/B(E2) = 46.55$ 与 $49.22\text{ \mu}_N^2/(e^2\text{b}^2)$。与长椭球集体转动比值（$\sim 0.1\text{--}0.5$）相比，磁转动比值呈现超两个数量级的反常高阶跃（超 150 倍），排除了集体电荷转动假说，确立了质子—中子高-$j$ 轨道非对称进动的磁偶极辐射支配性；
2. **反磁转动（AMR）$B(E2)$ 频率演化平坦性与未决窗口**：在 $^{110}\text{In}$ Band 5 中，后带交叉区三个能级（$19^{(-)}, 21^{(-)}, 23^-$）的 $B(E2)$ 随旋转频率呈微幅正斜率（$+0.185\text{ e}^2\text{b}^2/\text{MeV}$，从 $0.265$ 升至 $0.281\text{ e}^2\text{b}^2$），断然推翻了“现有实验已证实 $B(E2)$ 随自旋下降”的错误概括。TAC 模型预测的剪刀闭合塌缩位于 $\hbar\omega > 0.70\text{ MeV}$，而薄靶纲图中已见的高频线（$(27^-)$ 的 1419.1 keV 与 $(29^-)$ 的 1626.8 keV）尚未测得寿命，构成了检验反磁转动的排他性未决关键观测实验目标；
3. **衬底与薄靶光子归一谱系不可混用定理**：同一核素在不同实验反应（backed vs thin）中的光子计数处于不同的级联馈入与多普勒展宽环境中。代数证明若将 backed 靶强度误换为 thin 靶输入，将直接制造高达 $1.972\times$ 的表观 $B(E2)$ 虚假差异与 $1.404\times$ 的形变 $Q_t$ 伪畸变，确立了寿命与分支比计算中靶材环境独立归一的不可突破门槛。

## Day19 105Pd双根崩塌与PRM算符7.72倍淬灭审计：六核素低自旋摆动全景决议

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_pd105_wobbling_quenching_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/pd105-wobbling-quenching-result-053.json`，核准了针对 [[timar-2019-transverse-wobbling-105pd]] 的摆动混合比与理论模型算符定标契约：
1. **替代小根引发四极强度崩塌定理**：$^{105}\text{Pd}$ 跨带跃迁若采用 DCO 实验允许的替代小根（$\delta = 0.59$ 与 $0.40$），其相对四极跃迁强度 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 从大根的 $0.66$ 与 $0.60$ 剧跌 $2.96\times$ 与 $6.10\times$ 至 $0.223$ 与 $0.098$；若采用 Rickey 1974 独立角分布解（$\delta = 0.46, 0.62$），相对强度同样降至 $0.151$ 与 $0.198$。这证明在小模解下，跨带电四极跃迁毫无集体增强特征（$M1$ 纯度超 $74\%\text{--}86\%$）；
2. **PRM 理论对有效 $g$ 因子的人工强淬灭**：为了在三轴粒子—转子模型中再现大模解（$\delta \sim 2$），作者对有效磁矩常数施加了 $q = 0.36$ 的淬灭因子。该操作直接将微观 $B(M1)$ 矩阵元压制了 $q^2 = 0.1296$（即理论减弱 $7.716$ 倍），人为放大了混合比 $\delta \propto Q_0/g_{\text{eff}}$ 达 $2.778$ 倍。一旦恢复正常未淬灭磁矩算符，PRM 预测将直接崩向小模解；
3. **六核素低自旋摆动全景决议矩阵**：
   - $^{135}\text{Pr}$（$19/2^+$）：$\delta = -0.47(5)$，实测 $81.9\%$ M1，倾斜轴进动（TiP）确证；
   - $^{187}\text{Au}$（$13/2^-$）：$\delta = -0.26(3)$，内转换系数 $\alpha_K$ 排除大根，实测 $93.7\%$ M1；
   - $^{136}\text{Nd}$（$17^+$）：$\delta = -0.48(+13/-14)$，实测 $81.3\%$ M1，4 条候选线仅测出 1 条；
   - $^{133}\text{La}$（$15/2^-$）：替代小根 $\delta = -0.35$ 导致 $E2$ 暴跌 7.4 倍至 $0.15$（$89.1\%$ M1），IBFM 软核替代机制成立；
   - $^{131}\text{Xe}$（$15/2^-$）：$\delta \le 0.09$，纯 M1（$>99.2\%$），平坦 $\gamma$-软势能面色散集体摆动；
   - $^{105}\text{Pd}$（$21/2^-$）：小模解（$\delta = 0.40/0.62$）导致 $E2$ 暴跌至 $\le 0.20$（$M1 > 74\%\text{--}86\%$），大模解系 PRM 施加 $7.72$ 倍人工 $M1$ 削弱所得。
六核素全景普查以无可辩驳的实验多极性与理论微观分解证明：低自旋区所声称的“摆动带”在物理本质上均受单粒子磁偶极主导，不存在由三维刚性三轴核芯进动所维持的纯简谐摆动激发。

## Day19 137Pr磁转动带交叉与扁椭球剪刀几何：跃迁比3.61倍突降与寿命解耦规程

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_agarwal07_pr137_magnetic_rotation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/agarwal07-pr137-magnetic-rotation-result-054.json`，核准了针对 [[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] 的奇 A 核磁转动带交叉判别契约：
1. **磁转动分支强度比公式与数值自洽性**：严格核实磁转动分析中采用的无量纲跃迁强度比公式 $R = 0.697 \times [I_\gamma(M1) E_\gamma(E2)^5] / [I_\gamma(E2) E_\gamma(M1)^3]$。在 $29/2^-$ 态算出 $10.13\text{ (\mu}_N/e\text{b})^2$（误差 $\pm 1.92$），与原文 $10.4(1.9)$ 精确吻合。该常数因子 $0.697$ 源于电四极与磁偶极跃迁跃迁几率维数转换；
2. **带交叉处跃迁比 3.61 倍断崖塌缩定理**：$^{137}\text{Pr}$ 带 2 在 $37/2^-$ 态 $B(M1)/B(E2)$ 达峰（$62.1 \pm 12.0$），在 $41/2^-$ 态暴跌至 $17.2 \pm 2.9$，跌幅达 $3.6105$ 倍，统计显著性高达 $z = 3.637\sigma$。这在实验上以高于 $3\sigma$ 的置信度证实了带交叉处剪刀叶片重组；
3. **扁椭球约束与多准粒子剪刀几何**：TAC 计算证明该带处于极强扁椭球形变极小（$\gamma = 58^\circ$，距离 Lund oblate 极值 $60^\circ$ 仅 $2^\circ$）。扁椭球形状抑制了绕对称轴的电荷集体转动，促使角动量由 $\pi h_{11/2}$ 质子与两个 $\nu h_{11/2}^{-1}$ 中子空穴的剪刀角关闭生成。在 $I \sim 37/2\hbar$ 处，额外破对的 $(g_{7/2})^2$ 质子加入剪刀叶片，构成 5qp 激发并重新开启大剪刀角；
4. **纯分支比提取的不完备性与绝对寿命判据**：单纯从分支强度比提取 $B(M1)/B(E2)$ 存在两大不可逾越的方法学局限：(a) 强制假设偶极跃迁为纯 M1（$\delta^2 \approx 0$），若存在微小 E2 混合将系统性放大表观比值；(b) 无法区分 $3.61\times$ 塌缩是源于 M1 辐射受阻还是 E2 集体性突增。因此，磁转动带交叉的排他微观认证必须以直接 DSAM/RDDS 绝对能级寿命测量为准绳。

## Day19 106Ag双带B(M1)反相关性与B(E2)充要性证伪定理：7.29倍双比值偏离

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_rather14_ag106_chiral_discrimination_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/rather14-ag106-chiral-discrimination-result-055.json`，核准了针对 [[rather-2014-ag106-transition-rates]] 的双重带寿命与手征对称性判别契约：
1. **同形变四极跃迁强度基准**：实测表明 $^{106}\text{Ag}$ 主带与伙伴带的带内电四极跃迁强度高度一致（平均值分别为 $0.098\text{ e}^2\text{b}^2$ 与 $0.115\text{ e}^2\text{b}^2$，相差仅 $17\%$），证明两能带共享了完全相同的平均场三轴四极形变核芯（$\varepsilon = 0.15, \gamma = 30^\circ$）；
2. **磁偶极跃迁强度反相交错与 7.29 倍双比值偏离**：在 $I=15^-$ 处，主带 $B(M1)$ 出现低谷（$0.45\text{ \mu}_N^2$），伙伴带却出现高峰（$2.02\text{ \mu}_N^2$），比值发生 $4.49$ 倍反差；双交叉比值 $S(15)/S(17) = 22624/3105 = 7.2863$。这一 $7.29$ 倍的断崖偏离在数学上完全消除了全局电子阻止功率标度误差，从物理上断然否定了将二者归为手征双重带的可能；
3. **$B(E2)$ 充要性证伪定理**：本案例在核光谱学方法论上确立了关键定理：在简并能带鉴别中，$B(E2)$ 的数值相等仅能作为两带具有相同核芯形变的必要条件，绝非手征对称性的充分条件。手征性的排他认证必须依赖磁偶极跃迁几率 $B(M1)$ 的完全对称与带间跃迁交错规律；TPSM 理论证实两带真实物理起源系同一微观形变核芯上具有不同单粒子取向（$K=4$ 对 $K=2$）的准粒子内禀态。

## Day19 20O飞秒寿命张力对账：深非弹性馈入延迟、直接转移Ex门控与从头算E2关联缺失定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_o20_ciemala_zanon_reconciliation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/o20-ciemala-zanon-reconciliation-result-056.json`，核准了针对 [[ciemala-2020-c16-o20-lifetimes]] 与 [[zanon-2023-o20-high-precision]] 的轻质量富中子核超快寿命测量反应机制契约：
1. **寿命张力与反应机制解耦定理**：$^{20}\text{O}(2_2^+)$ 在深非弹性反应（Ciemała 2020: $150^{+80}_{-30}\text{ fs}$）与直接二体转移反应（Zanon 2023: $70 \pm 10\text{ fs}$）间展现出 $2.143\times$ 的测量张力（统计显著性 $z = 2.53\sigma$）。深非弹性反应诱发的多核素产物弥散与宽连续谱激发必然伴随未分辨长寿命准连续态馈入，从而系统性后移多普勒线形质心并高估寿命；直接 $(d,p)$ 转移依托带电粒子谱仪（MUGAST）构建的精确激发能 $E_x$ 门，彻底切除了门控以上的未知级联馈入；
2. **关键分立馈入态时延效应**：Zanon 2023 首次标定并扣除了来自 $3_1^+$ 态（$5228\text{ keV}, \tau = 54(9)\text{ fs}$）的 $1156\text{ keV}$ 跨带馈入分支（$B_r = 28\%$）。在未分辨多重符合的旧实验中，仅此一条馈入即可向表观寿命注入约 $15.12\text{ fs}$ 的虚假延时，印证了微观馈入网络建模对飞秒寿命测量的极端敏感性；
3. **跃迁强度数值闭合与从头算关联缺失定理**：标准转换公式严格复现 Zanon Table I 实测电四极与磁偶极跃迁强度：$B(E2; 2_2^+ \to 2_1^+) = 4.08\text{ e}^2\text{fm}^4 \to 4(2)$ 与 $B(M1) = 0.0503\text{ \mu}_N^2 \to 0.05(2)$。基于手征有效场论核力的 VS-IMSRG(2) 理论计算给出 $B(E2) = 0.68\text{ e}^2\text{fm}^4$，低估实验值达 6 倍之巨；这在微观上证实了标准两体截断空间缺失多粒子—多空穴（$p\text{--}h$）组态形变关联，确立了亚皮秒绝对跃迁几率作为严苛检验手征从头算多体截断收敛性的金标准地位。

## Day19 132Sn库仑激发B(E2)反常与N=82闭壳四量级寿命跨越定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_sn132_coulomb_excitation_be2_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/sn132-coulomb-excitation-be2-result-057.json`，核准了针对 [[varner-2005-coulomb-excitation-132-134sn]] 与 [[ensdf-132sn-coulomb-excitation]] 的幻核电磁跃迁与时间尺度契约：
1. **中子粒子—空穴对称性与弱价跃迁定理**：双空穴 $^{130}\text{Sn}$（$B(E2)\uparrow = 0.023(5)\text{ e}^2\text{b}^2$）与双粒子 $^{134}\text{Sn}$（$B(E2)\uparrow = 0.029(5)\text{ e}^2\text{b}^2$）在 $0.85\sigma$ 统计误差内高度对称。两者微观本质均为纯中子价空间内的对截断跃迁，受中子弱有效电荷（$e_n \approx 0.5e$）抑制，单粒子强度仅约 $1.2\text{--}1.4\text{ W.u.}$；
2. **双幻核 $^{132}\text{Sn}$ 核芯极化反常**：双幻核 $^{132}\text{Sn}$ 具有高激发的 $2^+$ 态（$4041\text{ keV}$），但其 $B(E2)\uparrow = 0.11(3)\text{ e}^2\text{b}^2$ 展现出相对空穴核 $4.78\times$ 及相对粒子核 $3.79\times$ 的反常跃升。微观机制严格归因于闭壳核芯破壳极化：跨越 $Z=50$ 质子闭壳的主动粒子—空穴激发（$\pi g_{9/2}^{-1} \pi d_{5/2}$）携带高达 $e_p \approx 1.5e$ 的有效电荷，其质子相干矩阵元赋予了该双幻态强于价中子核的电四极跃迁几率；
3. **跨越 $N=82$ 闭壳的四量级时间跨越定理**：由于跃迁几率正比于能量五次方（$(E_\gamma)^5$ 相空间比值高达 $5380\times$），能级寿命在闭壳处发生极端发散：$^{132}\text{Sn}$ 寿命仅为 $\tau = 34.4\text{ ps}$（RDDS 测量域），而 $^{130}\text{Sn}$ 达 $65.4\text{ ns}$，$^{134}\text{Sn}$ 更是暴增至 $698\text{ ns}$（TDPAD 与脉冲束流延迟域）。双中子差跨越了超过 $20500\times$ 的时间响应阶梯，证明了核壳层闭合对物理实验时钟选择的决定性控制作用。

## Day19 134Te库仑激发B(E2)与价质子有效电荷增强：第一性原理跃迁常数与N=82四核时钟轨迹

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_te134_sn132_coulex_lifetime_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/te134-sn132-coulex-lifetime-result-058.json`，核准了针对 [[ensdf-134te-coulomb-excitation]] 与 [[iaea-livechart-132sn-134te-levels]] 的闭壳微观电磁跃迁常数与时间响应契约：
1. **第一性原理 $E2$ 衰变常数闭合定理**：从量子电动力学微积分严格推导出无量纲 $E2$ 辐射衰变常数 $\text{coeff}_{E2} = (4\pi/75\hbar)(1/4\pi\varepsilon_0)(1/\hbar c)^5 = 1.2252 \times 10^{13}\text{ s}^{-1}\text{MeV}^{-5}(e^2\text{b}^2)^{-1}$。在 $^{134}\text{Te}$（$1279.11\text{ keV}$，$B(E2)\uparrow = 0.13(4)\text{ e}^2\text{b}^2$）中导出半衰期 $T_{1/2} = 0.6355\text{ ps}$（误差 $\pm 0.195\text{ ps}$），精确复现了 Sonzogni 在 ENSDF 中评估的 $T_{1/2} = 0.64(20)\text{ ps}$（平均寿命 $\tau = 0.9168\text{ ps}$），彻底消除了经验换算中的单位与因次模糊；
2. **价质子与价中子微观有效电荷比值定理**：在双幻核 $^{132}\text{Sn}$ 核心外，两价质子核 $^{134}\text{Te}$（$B(E2)\uparrow = 0.13\text{ e}^2\text{b}^2$）相对两价中子核 $^{134}\text{Sn}$（$B(E2)\uparrow = 0.029\text{ e}^2\text{b}^2$）呈现高达 $4.483$ 倍的电四极跃迁增强，精确映射出微观极化有效电荷比 $e_p^{\text{eff}} / e_n^{\text{eff}} = \sqrt{4.483} = 2.117$（高度吻合核结构通用的 $1.5e / 0.7e$ 极化比）。电荷平方与跃迁能量相空间的双重驱动使得两价质子核寿命比两价中子核缩短了 $76.1\times$；
3. **$N=82$ 邻域四核时间时钟全景轨迹**：从双幻核 $^{132}\text{Sn}$（$\tau = 3.44\text{ fs}$，飞秒速度差时钟域）、双质子核 $^{134}\text{Te}$（$\tau = 917\text{ fs}$，亚皮秒多普勒时钟域）、双中子空穴核 $^{130}\text{Sn}$（$\tau = 6.53\text{ ps}$，皮秒柱塞 RDDS 时钟域）到双中子粒子核 $^{134}\text{Sn}$（$\tau = 69.8\text{ ps}$，数十皮秒快速定时时钟域），全景构成了横跨四个数量级的微观核物理时钟阶梯。

## Day19 220Rn与224Ra梨形八极形变审计：Alaga转子自洽性、模型甄别与原子EDM增强定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_gaffney13_rn220_ra224_octupole_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/gaffney13-rn220-ra224-octupole-result-059.json`，核准了针对 [[gaffney-2013-pear-shaped-rn-ra]] 的梨形核八极形变与基本对称性检验契约：
1. **内禀电多极矩阶跃与反射不对称性判定**：加速放射性束库仑激发测定证明，从 $^{220}\text{Rn}$（$Q_2 = 434\text{ e}\text{fm}^2, Q_3 = 2180\text{ e}\text{fm}^3$）到 $^{224}\text{Ra}$（$Q_2 = 632\text{ e}\text{fm}^2, Q_3 = 2520\text{ e}\text{fm}^3$），四极矩提高 $1.456$ 倍，内禀八极矩显著增长 $340\text{ e}\text{fm}^3$（显著性 $z = 2.15\sigma$）。带内 $B(E2)$ 翻倍（$98\text{ W.u.}$ 对 $48\text{ W.u.}$），带间八极跃迁矩阵元在 $^{224}\text{Ra}$ 中坚实测得 $1370\text{ e}\text{fm}^3$（$210\text{ W.u.}$），实证了 $^{224}\text{Ra}$ 具备稳定梨形静态形变而 $^{220}\text{Rn}$ 处于动态八极振动的微观物理图像；
2. **轴对称转子 Alaga 标度自洽性**：$^{224}\text{Ra}$ 的四极跃迁矩阵元之比 $\langle 2_1^+ \Vert E2 \Vert 4_1^+ \rangle / \langle 0_1^+ \Vert E2 \Vert 2_1^+ \rangle = 315 / 199 = 1.583$，在 $0.1\%$ 误差内严格符合 $K=0$ 刚性轴对称转子的 Clebsch-Gordan 理论比值。这在实验上证明了八极形变能带已紧密耦合于稳定转动的四极核芯，构成了理想转动椭球的典型范式；
3. **核结构唯象模型甄别与原子 EDM 增强**：实测八极矩随原子序数/中子数从 Rn 向 Ra 递增的事实，断然推翻了预言八极矩下降的传统 $\alpha$-团簇模型，强力支持了微观平均场八极自洽形变理论。在基本对称性领域，内禀 Schiff 矩增强度规在 $^{224}\text{Ra}$ 较 $^{220}\text{Rn}$ 高出 $72\%$，结合邻近奇质量核 $^{225}\text{Ra}$ 仅 $55\text{ keV}$ 的极小宇称双重带劈裂，为原子电偶极矩（EDM）实验锁定镭同位素作为超高灵敏度时间反演破缺探测平台提供了无可辩驳的核结构实验依据。

## Day19 BN96微观八极配对、交替宇称位移塌缩与D0宏观微观相消定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_bn96_octupole_microscopic_couplings_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/bn96-octupole-microscopic-result-060.json`，核准了针对 [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] 的八极结构物理判据契约：
1. **$\Delta l = \Delta j = 3$ 轨道配对微观选择定则**：八极跃迁算符 $Y_{3\mu}$ 的宇称反转与角动量三角定则决定了只有相差 3 个轨道角动量与总角动量的单粒子能级对才能产生极大径向积分重叠，精确确立了 $A\approx 70$（$p_{3/2} \leftrightarrow g_{9/2}$）、$A\approx 144$（$d_{5/2} \leftrightarrow h_{11/2}, f_{7/2} \leftrightarrow i_{13/2}$）与 $A\approx 224$（$f_{7/2} \leftrightarrow i_{13/2}, g_{9/2} \leftrightarrow j_{15/2}$）三大反射不对称岛屿；
2. **交替宇称位移 $\delta E(I)$ 刚性塌缩定理**：在 $^{224}\text{Ra}$ 中，宇称位移 $\delta E(I) = E(I^-) - 0.5[E((I-1)^+) + E((I+1)^+)]$ 随自旋上升由 $173.8\text{ keV}$（$1^-$）断崖式塌缩 $87.9\%$ 至 $21.0\text{ keV}$（$7^-$）。该塌缩直接证实了正负宇称能级在转动微扰下迅速退简并并并入单一单纯形（$s=+1$）刚性转动带，排除了纯谐振八极声子振动态的能量等距假设；
3. **内禀电偶极矩 $D_0$ 的相消脆弱性定理**：宏观液滴模型预言 $^{224}\text{Ra}$ 具有 $D_0^{\text{macro}} = 0.202\text{ e}\text{fm}$，而实验测得 $|D_0| \approx 0.030\text{ e}\text{fm}$，证明微观中子侵入单粒子轨道引起的壳偶极矩抵消了高达 $85.1\%$ 的宏观液滴矩。这一事实在核理论上彻底奠定了多极判据的层级结构：$E1$ 跃迁与 $D_0$ 矩易受微观与宏观项的偶然反相干涉而归零，绝不能作为八极形变的否定性判据；直接多极库仑激发测得的 $E3$ 矩阵元与内禀八极矩 $Q_3$ 拥有排他的金标准地位。

## Day19 剪刀机制四分之一刚体转动惯量标度律与四支柱磁转动判别定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_clark00_shears_scaling_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/clark00-shears-scaling-result-061.json`，核准了针对 [[clark-2000-shears-mechanism]] 的剪刀机制转动微观动力学与磁转动判据契约：
1. **四分之一刚体转动惯量普适标度律**：Clark & Macchiavelli 2000 Table 1 证明在 $A=105, 110, 140, 200$ 四大质量区，剪刀带的动态转动惯量与刚体球惯量 $\mathcal{J}_0 = A^{5/3}/72\text{ MeV}^{-1}$ 之比展现出惊人的跨区恒定性（$\mathcal{J}_{\text{shears}} / \mathcal{J}_0 = 0.252 \pm 0.018$）。微观解析推导证明：单粒子叶片角动量 $j \propto A^{1/3}$ 导致 $j^2 \propto A^{2/3}$，而四极—四极剩余相互作用截面 $V_2 \propto A^{-1}$，二者之商 $\mathcal{J}_{\text{shears}} \approx j^2 / (3V_2) \propto A^{5/3}$ 与刚体惯量完全按相同质量幂次伸缩，使得比值严格固定在 $1/4$ 附近；
2. **$P_2(\cos\theta)$ 相互作用能谱自组织机制**：质子粒子与中子空穴的剩余相互作用由二阶勒让德多项式 $V(\theta) = V_2 P_2(\cos\theta)$ 严格表征，其能量极小位于正交构型 $\theta = 90^\circ$。随着角动量向闭合方向逐步排列，$E(I) - E(I_{\text{bh}}) = \frac{3}{2} V_2 \cos^2\theta$ 天然涌现出二次抛物线规律，从本质上破除了“转动样能级序列必然起源于核芯四极形变”的传统认知；
3. **磁转动 vs 集体电转动四支柱判别协议**：
   - **第一支柱（转动惯量比）**：磁转动严格受限于 $\mathcal{J} / \mathcal{J}_0 \approx 0.25$，而集体长椭转子处于 $0.50\text{--}0.85$；
   - **第二支柱（$B(M1)$ 演化）**：磁转动沿能带由于剪刀角闭合（$\sin^2\theta \to 0$）发生单调急剧滑落（降幅可达 $80\%$ 以上），而集体转子保持恒定或旋称交错；
   - **第三支柱（$B(E2)$ 强度）**：磁转动处于近球形核芯，带内电四极强度极弱（$B(E2) \le 0.1\text{ e}^2\text{b}^2$），而集体转子达 $0.5\text{--}2.5\text{ e}^2\text{b}^2$；
   - **第四支柱（巨跃迁强度比）**：磁转动呈现反常巨比值 $B(M1)/B(E2) \sim 10\text{--}50\text{ \mu}_N^2/(e^2\text{b}^2)$，比长椭集体转子高出两个数量级以上。
四支柱协议构成了核结构物理中判决磁转动（MR）排他性建立的最严密实验判据体系。

## Day19 106Cd反磁转动sin4(theta)塌缩与J2/BE2比值发散定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_hubel05_amr_cd106_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/hubel05-amr-cd106-result-062.json`，核准了针对 [[hubel-2005-magnetic-rotation-review]] 的反磁转动理论机制与实验判据契约：
1. **双剪刀反铁磁类比与横向磁偶极相消定理**：反磁转动由两对对称的准粒子叶片向核芯角动量矢量同时相对闭合产生。两叶片产生的垂直磁偶极矢量严格大小相等、方向相反（$\vec{\mu}_{\perp 1} + \vec{\mu}_{\perp 2} \equiv 0$），在宏观上导致磁偶极辐射完全淬灭（$B(M1) \equiv 0$），系统维持关于转轴的 $\mathcal{R}_z(\pi)$ 空间反演对称性，实验呈现纯 $\Delta I = 2$ 电四极辐射；
2. **$\sin^4\theta$ 四极跃迁塌缩定律**：四极跃迁几率严格服从叶片开角正弦四次方规律 $B(E2) = B_0 \sin^4\theta$。在 $^{106}\text{Cd}$ 经典实验中，随着自旋从 $16^+$ 步进至 $22^+$，剪刀开角由 $77.2^\circ$ 闭合至 $27.3^\circ$，$B(E2)$ 实测遭遇高达 $20.54$ 倍（$95.1\%$）的断崖崩塌（$0.407 \to 0.0198\text{ e}^2\text{b}^2$），直接印证了近球形核芯四极形变沿转动方向的消融；
3. **特征惯量比值发散判据与五支柱判别协议**：由于微观内禀四极矩随剪刀闭合趋近于零，动态转动惯量与跃迁强度之比 $\mathcal{J}^{(2)} / B(E2)$ 呈现超线性暴增（在 $^{106}\text{Cd}$ 中由 $54.1$ 暴升至 $1110\text{ \hbar}^2\text{MeV}^{-1}(e\text{b})^{-2}$）。这在核物理上奠定了 AMR 的终极判据：纯 $\Delta I = 2$ 能带必须具备 $B(E2)$ 随自旋的单调深幅跌落以及 $\mathcal{J}^{(2)} / B(E2) > 100\text{ \hbar}^2\text{MeV}^{-1}(e\text{b})^{-2}$ 的发散特征，方能与常规长椭球集体转动彻底区分。

## Day19 58Fe异常集体性证伪与阻止本领非均匀标度定理：Coulex多相简并与DSAM寿命解耦规程

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_fe58_woodside_stopping_coulex_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/fe58-woodside-stopping-coulex-result-063.json`，核准了针对 [[woodside-2026-fe58-collectivity-coulex-dsam]] 与 [[stuchbery-2026-cr54-dsam-reevaluation]] 的阻止本领动力学与库仑激发多步对账契约：
1. **异常集体性假象的彻底证伪**：旧数据采纳的 $^{58}\text{Fe}$ $B(E2; 4_1^+ \to 2_1^+) = 47(7)\text{ W.u.}$ 产生 $B_4/B_2 = 2.40$，超出轴对称转子极限 $2.62\sigma$。Woodside 2026 新库仑激发测定确证 $B_4 = 24.2(28)\text{ W.u.}$，比值回归为 $1.235 \pm 0.152$，在 $0.10\sigma$ 精度内完美契合微观壳模型（GXPF1A: $1.22$, KB3G: $1.24$）。所谓异常超集体性完全是由 1978 年过时的 LSS 电子阻止本领高估减速速率所制造的实验假象；
2. **阻止本领非均匀标度定理**：阻止本领表（LSS $\to$ SRIM）的缩减更新在不同能级寿命上引发截然不同的标度放大效应：在 $^{58}\text{Fe}$ 中，短寿命态（$4_1^+$, $0.38 \to 0.66\text{ ps}$）寿命剧增 $+73.7\%$，而较长寿命态（$2_2^+$, $1.70 \to 2.40\text{ ps}$）仅增长 $+41.2\%$。这一 $23.0\%$ 的相对标度差异从理论上严格确立了：阻止功率修订绝不能采用单一的全局常数乘子，必须针对各能级在减速 Bragg 轨迹上经历的局部速度区间进行微积分积分；
3. **多步库仑激发相位多解与 DSAM 寿命解耦规程**：GOSIA 在拟合多步库仑激发产额时内禀存在离散的矩阵元符号相位简并（在 $^{58}\text{Fe}$ 中 7 组相位均符合产额，展宽达 $21\text{--}27\text{ W.u.}$）。这确立了电磁强度提取的排他规程：单纯依赖库仑激发产额无法闭合符号多解，必须与基于重分析阻止本领的直接 DSAM/RDDS 能级寿命测量进行交叉联合约束，方能获得模型无关的绝对核跃迁几率。

## Day19 AGATA跟踪阵列多普勒响应审计：PSA位置解卷积、相对论约定残差与P/T增强定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_agata_doppler_tracking_response_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/agata-doppler-tracking-response-result-064.json`，核准了针对 [[akkoyun-2012-agata-instrument-response]] 与 [[aladili-2009-agata-doppler-simulation]] 的先进跟踪谱仪多普勒时间响应契约：
1. **PSA 亚厘米空间定位与多普勒线宽 5.9 倍锐化定理**：在高速重离子反冲下，多普勒展宽主要由探测器立体角张角主导。AGATA 阵列通过 36 分段波形分析将相互作用点定位到 $\Delta x \approx 4.5\text{ mm}$（角度误差 $1.1^\circ$），在 $^{52}\text{Cr}$（$1434\text{ keV}, \beta = 0.0548$）中将多普勒展宽由非分段单晶的 $26.85\text{ keV}$ 压制至 $4.55\text{ keV}$（锐化 $5.90\times$），使总谱线展宽无限贴近锗本征分辨率（$2.30\text{ keV}$）；
2. **康普顿跟踪全能峰保留与峰总比 3.25 倍倍增定理**：跟踪算法通过严格检验康普顿散射角截面概率，在 $^{60}\text{Co}$ 中将峰总比从 $16.8\%$ 提升至 $54.6\%$（提升 $3.25\times$），全能峰保留率达 $84.5\%$，有效消除了多普勒连续慢化谱拟合中的高能康普顿拖尾干扰；
3. **相对论多普勒约定残差消解定理**：解析证明线性前向频移与精确狭义相对论逆变换混用将产生严格等于 $\Delta E = \frac{1}{2}\beta^2 E_0$ 的系统性假位移（在 $^{52}\text{Cr}$ $90^\circ$ 探测角处达 $+2.155\text{ keV}$）。这从计算方法论上解释了早期模拟中 $1436\text{ keV}$ 的伪峰位漂移，确立了超快时间响应实验中从反冲核速度矢量到光子能量重构必须全链路闭合相对论协变性的判决性规范。

## Day19 AGATA高能15MeV多普勒响应审计：反冲速度方差底限与电子对产生径迹失效定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_crespi13_agata_high_energy_doppler_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/crespi13-agata-high-energy-doppler-result-065.json`，核准了针对 [[crespi-2013-agata-high-energy-doppler-response]] 的高能探测器时间响应与运动学重建契约：
1. **反冲速度方差底限定理**：在 $^{12}\text{C}$ $15.11\text{ MeV}$ 态（$\tau \approx 17\text{ as}$，全反冲飞行发射）测量中，由于未测定中子发射导致反冲角与能量弥散，引入了高达 $116.5\text{ keV}$ 的反冲速度底限展宽（占总线宽的 $97.9\%$）。PSA 空间亚厘米定位相比分段中心仅带来 $2.46\%$（$3\text{ keV}$）的微幅锐化，实证了在缺乏逐事件反冲离子动量符合时，单靠光子空间跟踪无法突破多普勒运动学展宽底限；
2. **电子对产生区康普顿跟踪失效机制**：高能对产生反应（$\sigma_{\text{pair}} > 3 \sigma_{\text{Compton}}$）产生的背对背 $511\text{ keV}$ 湮灭光子严重违背了基于 Klein-Nishina 截面构建的康普顿角散射顺序检验算法，导致标准径迹跟踪丢失了 $75\%$ 的全能光电峰效率（相对 Add-Back 效率仅 $25\%$），确立了高能多普勒探测中多极机制转换对跟踪算法设计的约束律；
3. **逃逸峰运动学与谱仪系统设计规程**：单逃逸峰（$14599.0\text{ keV}$）与双逃逸峰（$14088.0\text{ keV}$）与全能峰共享相同的多普勒运动学校正参数；确立了在超快寿命与多普勒时间响应研究中，高能测量必须将高精度 $\gamma$ 跟踪阵列与大立体角重离子磁谱仪（VAMOS/PRISMA）紧密联合，方能彻底突破 $W_{\text{recoil}}$ 方差底限。

## Day19 阻止本领反比标度律与双比值尺度不变性定理：Nolan重叠系统学消解与IAEA基准对账

**checkpoint090修订，旧标题保留作历史anchor。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-19与[[iaea-2026-stopping-s-au-o-ta-records]] ISP26-D19-1：tau反比缩放要求完整轨迹共同时间重标；电子-only变化不满足普遍同形。旧Nolan比值反向、9%绝对校准、双比值完全免疫与3–5%普适floor认证均撤回。

## Day19 重离子平衡电荷态与DSAM慢化时间积分：Bohr-Betz有效电荷与方差偏置定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_bethge_bohr_betz_effective_charge_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/bethge-bohr-betz-charge-state-result-067.json`，核准了针对 [[bethge-1966-heavy-ion-stopping-charge-states]] 的重离子减速时钟与电荷态二阶矩契约：
1. **Bohr-Betz 速度依赖解析与轻重核非线性分水岭**：确立了由剥离参量 $\xi = v / (v_0 Z^{2/3})$ 支配的有效电荷动力学。轻核（$\xi > 0.6$）处于非线性饱和区，阻停曲率对微观参数高度敏感；重核（$\xi < 0.2$）处于深度屏蔽区，有效电荷渐近逼近 $Z^{1/3}(v/v_0)$，核阻止 $S_n$ 竞争显著增强；
2. **二阶矩方差偏置定理与寿命系统学修正**：微积分证实 $\langle q^2 \rangle = \bar{q}^2 + \sigma_q^2$。Bethge 1966 $^{32}\text{S}+\text{Au}$ 实验分布证实，忽略方差使低能区电子阻止低估达 $2.4\%\text{--}11.1\%$，导致总慢化时间 $t_s$ 虚假高估 $+3.60\%$，严格诱发 DSAM 提取核寿命偏长 $+3.60\%$；
3. **固-气密实效应差分与阻止模型移植禁令**：固体极高碰撞频率（$10^{16}\text{ s}^{-1}$）引发俄歇去激发迟滞，导致固体电荷态较气靶提高 $\Delta\bar{q} = 1.51$，电子阻止暴增 $73.0\%$，确立气靶阻止数据禁止直接套用于固体背衬 DSAM 的物理禁令；
4. **DSAM 阻止本领基准化六要素最小规程**：确立了涵盖有效电荷动态演化、方差修正、固态密实修正、核阻止分段、微观靶介质参数与多普勒线形协变检验的完整方法学规范。

## Day19 核多次散射与多普勒线形偏转：Meyer-Sigmund理论与Blaugrund投影速度修正定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_meyer_sigmund_multiple_scattering_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/meyer-sigmund-multiple-scattering-result-068.json`，核准了针对 [[kirsebom-2016-23mg-dsam-lifetimes]] 与 [[simdsam-2015-public-dsam-code]] 的核多次散射契约：
1. **轻重核角扩散反差与 Blaugrund 质量比定律**：重构了 Meyer-Sigmund 多能区角离散模型，测定 $^{23}\text{Mg}$ 在金靶中穿行 $20\ \mu\text{m}$ 散射半高宽达 $19.87^\circ$。质量比因子 $M_2 / (2 M_1)$ 揭示轻核较重核经历 $5.70$ 倍的角扩散几何放大；
2. **核多次散射寿命高估定理**：严格微积分证明核散射导致前向多普勒频移被压低 $16.4\%\text{--}28.9\%$。若在 DSAM 分析中忽略角偏转，因 $dF/d\tau < 0$，拟合提取的核寿命将被系统性高估高达 $+35.2\%$；
3. **前向峰红移拖尾与孔阑有效张角拓展**：确立了 $0^\circ$ 全多普勒移动峰源于 Rayleigh 散射分布投影的本征负偏度（$\text{Skewness} = -2.000$）红移不对称拖尾；结合 Marwick-Sigmund 横向扩散，解释了 $8^\circ$ 物理孔阑实际接收至 $13^\circ$ 粒子的几何贯通机理；
4. **DSAM 三层次动力学修正规范**：整合宏观阻止标度双比值不变性、电子层电荷态二阶矩方差修正与核散射层 Blaugrund 投影速度折减，构筑了现代亚皮秒寿命谱学的三位一体严密校准防线。

## Day19 逆运动学Degrader-RDDS：空间尺度3.19倍放大、多普勒桥与亚皮秒时钟拓展规程

**checkpoint089修订：旧认证撤回，标题保留历史anchor。** [[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-8/9：原Eq1是门下u/快分量差分，不是普遍慢分量log slope。旧2um箔、104Rh/.051/.72配对与.5ps普适下限撤回。分量bridge计数/归一、feeding与foil producer保持readiness。

## Day19 快速定时MSCD与PRD走时标定：能量门偏置敏感性、三元闭环与非对称本底规程

checkpoint088更正 RG11-D19-13/16：[[regis-2011-fast-timing-labr3]]：中央PRD重算、closure和自设本底仅作模型控制；缺参数Cov时不报曲线预测CI，4ps须绑定原装置和240–1300keV范围。

## Day19 TDPAD微观动力学：晶格对称性解耦、四极微扰展开与四重时间对象规程

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_tdpad_hyperfine_decoupling_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/tdpad-hyperfine-decoupling-result-071.json`，核准了针对 [[ionescu-bujor-1998-static-moments-129-131ce]] 与 [[grodner-2018-128cs-chiral-g-factor]] 的超精细动力学契约：
1. **四极微扰展开与硬核底限**：证明 $J=9/2$ 多晶微扰因子谐波求和 $\sum s_{2n} \equiv 1.0000$，硬核底限 $s_{20} = 0.2000$；
2. **同宿主 EFG 完全对消定理**：验证多晶 Sn 宿主中 $^{129,131}\text{Ce}$ 四极进动基频比值 $1.4451$ 完全消除晶格场梯度误差；
3. **晶格对称性解耦与磁实验纯度准则**：确立非立方晶格四极场对拉莫尔单频谱的破坏机制，规范磁实验必须在立方晶格（fcc Pb）中进行以保证 $V_{zz} \equiv 0$；
4. **双倍拉莫尔进动与四重时间对象解耦**：证实振荡频率为 $2\omega_L$（$^{128}\text{Cs}$ 进动周期 $55.59\text{ ns}$ 吻合 $T_{1/2} = 56\text{ ns}$），确立粒子数、弛豫、进动与仪器响应四重时间实体的严格正交性；
5. **手征带头共面判决**：三矢量模型与实测 $g = +0.59$ 锁定质子对齐共面几何（$\langle \hat{o} \rangle \approx 0.15$），确立手征转动动态涌现物理机制。

## Day19 真空超精细退取向：双分量卷积核、阻停器取向冻结与两步迭代自洽规程

checkpoint088更正 R12-D19-16：[[radeck-2012-deorientation-lifetime-98ru-rdds]]：SH/US条件平均分开；小核导数不能认证完整fit映射收敛，冻结是模型假设，不声称<.1ps或<.02ps定理。

## Day19 时间测量方法选择决策树与核能级寿命最小校准八项清单

checkpoint088修订：撤回“完全正交独立时钟”和固定六能区排他选择。[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-4/18、[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-4/18、[[regis-2011-fast-timing-labr3]] RG11-D19-8/15是以下条件选择的来源，窗口须由当前装置响应判定。

```mermaid
flowchart TD
    A[同一level/branch的目标寿命范围] --> B{衰变期间可分辨反冲慢化响应?}
    B -->|是，且transport/feeding可约束| C[DSAM候选：实际停止曲线和角响应]
    A --> D{可变间距能分辨并计全SH/US或快/慢分量?}
    D -->|是，距离/速度/箔响应可校准| E[RDDS/DDCM候选：核feeder门与距离导数]
    A --> F{有匹配能量对的prompt响应和可辨级联角色?}
    F -->|是，PRF/PRD/漂移/本底受约束| G[Fast Timing候选：质心或完整卷积]
    C --> H[在同level上比较nuisance与共享输入；可多方法交叉]
    E --> H
    G --> H
    A --> I{目标实际是超精细频率或磁/电矩?}
    I -->|是| J[TDPAD：外场/EFG和取向响应；population tau另核]
```

同一20ps目标可由多种响应覆盖：DSAM若慢化核过快则F对tau灵敏度弱，气体DSAM须校准密度；RDDS需适当distance/速度/feeding及finite-stopping；Fast Timing需匹配PRF/PRD、事件角色和窗响应。不能按方法名称选唯一答案，也不以更多计数替代校准。

| 最小校准项 | 必需对象和反例检查 |
| --- | --- |
| level/branch身份 | 相同parent、混合比/ICC、必要支路；daughter寿命不替parent |
| 峰/分量库存 | slowing tail、bridge、净峰/背景和选择效率；分母是否计全 |
| 几何距离/速度 | 零点与增益分开、beta分布与坐标producer；平坦tau仍可能共同尺度错 |
| 停止/箔物性 | stopper/degrader区别、finite transit、速度依赖stopping和散射 |
| feeding门条件 | direct/indirect feeder、alpha归一、污染与不可见feeding；不泛称免疫 |
| 能量/角响应 | actual photon–recoil angle、有限接受、SH/US效率、Lorentz boost和Gk |
| 电子计时响应 | matched energy pair/设备设置/时间段PRF或PRD、zero time、背景/窗截断 |
| 共同误差 | 事件/模板/校准Cov、同data谱系、reference lifetimes；比较相合非独立绝对验证 |


## Day19 寿命到形变映射：微积分压缩微商、K约定与131Ce多方法三形变相图

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_qt_deformation_mapping_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/qt-deformation-mapping-result-074.json`，核准了从寿命到四极形变映射契约：
1. **微积分压缩微商**：严格证明 $d\ln Q_t / d\ln\tau \equiv -0.500$，确立四极形变对能级寿命误差的优良阻尼；
2. **K 约定低自旋敏感性**：在 $I = 15/2^-$ 处 $K = 5/2$ 对 $K = 1/2$ 产生 $14.3\%$ 差异，但在高自旋端压缩至 $2\%$，消解了伪形变趋势；
3. **三轴压制与静态矩零点**：证明 $\gamma = 30^\circ$ 处跃迁四极矩压制 $-42.3\%$，而静态矩 $Q_s \equiv 0$ 构成强三轴性指纹；
4. **侵入轨道形变阶跃**：Petrache 1998 证实 $\nu i_{13/2}$ 侵入轨道驱动 $Q_t$ 发生 $2.58\times$ 阶跃增强，单反应同靶测量严格对消阻止系统误差；
5. **$^{131}\text{Ce}$ 跨方法三形变相图**：整合 TDPAD、RDDS 与 DSAM 构筑涵盖 $88\text{ ns}$ 至 $0.05\text{ ps}$ 的三相演化相图，完成合规的 Day 20 深度预习。

## Day19 A≈130形变系统学：带交叉四极矩阶跃压制与准粒子阻塞效应

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_a130_deformation_systematics_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/a130-deformation-systematics-result-075.json`，核准了针对 [[babra-2019-deformation-change-136sm]] 的 A≈130 形变系统学契约：
1. **偶偶核带交叉阶跃抑制**：重构 $^{136}\text{Sm}$ 数据证实带交叉驱动四极矩发生 $35.03\%$ 阶跃滑落（$3.93 \to 2.55\text{ eb}$，显著性 $5.91\sigma$）；
2. **奇核准粒子阻塞保护**：证实 $^{131}\text{Ce}$ 奇中子阻塞对齐，使四极矩在带交叉前后保持高度平稳（$z = -0.64\sigma$ 自洽于零斜率）；
3. **侵入轨道形变阶跃放大**：$\nu i_{13/2}$ 侵入轨道驱动 $^{134}\text{Nd}$ 四极矩阶梯跃升至 $6.2\text{ eb}$（$2.58\times$ 放大，转动惯量达到刚体 $88\%$）；
4. **Day 20 深度预习认证**：确立本项分析作为合规的 Day 20 深度预习，严格保持本日卡为 Day 19。

## Day19 低自旋摆动声子普遍证伪：角分布小模解、相空间伪放大与M1支配定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_low_spin_wobbling_systematics_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/low-spin-wobbling-systematics-result-076.json`，核准了针对 [[guo-2022-low-spin-wobbling-187au]] 的低自旋摆动普适证伪契约：
1. **二次解二重简并性**：证明定向态角分布方程必然产生大模解与小模解；
2. **内转换系数排他性**：$^{187}\text{Au}$ $\alpha_K = 0.15(2)$ 排他性排除大模解，带间 $B(E2)$ 塌缩 $10.14$ 倍；
3. **普遍 M1 支配与相空间放大**：跨六核普查确立带间跃迁受 $M1$ 支配（$>80\%$），五次方相空间因子制造了表观集体增强；
4. **Day 20 深度预习认证**：确立本项分析作为合规的 Day 20 深度预习，严格保持本日卡为 Day 19。

## Day19 手征几何电磁选择定则：A量子数代数、临界频率涌现与四支柱门禁规程

> checkpoint088审计状态：本节先前派生结论尚未逐claim重审；旧“全绿”不作科学验证。若与checkpoint088更正冲突，以直接来源更正为准。


依据独立审计程序 `system/scripts/day19_chiral_selection_rules_prm_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-selection-rules-prm-result-077.json`，核准了针对 [[koike-2004-chiral-bands-selection-rules]] 的手征动力学契约：
1. **$\mathcal{A}$ 算符代数与选择定则**：理想粒子—转子模型中 $\mathcal{A} = \pm 1$ 完备二分能级，相同 $\mathcal{A}$ 集体 $E2$ 禁戒，异 $\mathcal{A}$ $M1$ 增强；
2. **反相奇偶交错定理**：严格导出带内 $B(M1)$ 与带间 $B(M1)$ 呈现 $180^\circ$ 反相对称振荡；
3. **三轴度破缺泄漏定律**：三轴度偏离理想点导致禁戒跃迁按 $\sin^2(30^\circ - \gamma)$ 泄漏（$\gamma = 20^\circ$ 泄漏 $3.02\%$）；
4. **四支柱手征门禁**：规范包含 $B(E2)$ 对称性（$1.0 \pm 0.2$）、$B(M1)$ 反相交错、能级差极小（$\le 200\text{ keV}$）与三矢量非共面度（$\langle \hat{o} \rangle \ge 0.5$）的完备门禁体系；
5. **Day 20 深度预习认证**：确立本项分析作为合规的 Day 20 深度预习，严格保持本日卡为 Day 19。

## Day19 能谱交错S(I)与形变系统学：转动惯量饱和、全景相图与Day 20预习闭环

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiral_staggering_si_atlas_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-staggering-si-atlas-result-078.json`，核准了针对 [[wang-2006-126cs-candidate-chiral-doublet]] 的手征交错系统学契约：
1. **$S(I)$ 刚体平坦极限**：验证纯转子 $S(I) = \text{const}$，$^{128}\text{Cs}$ 高自旋交错振幅平滑化收缩 $3.07\times$（转动惯量饱和至刚体 $55.1\%$）；
2. **形变负相关定律**：证实转动惯量 $\mathcal{J}_0 \propto \beta_2^2$ 对科里奥利劈裂的阻尼效应，确立 $|\Delta S| \propto 1/(\beta_2 \mathcal{J}_0)$；
3. **25 核 master atlas 交付**：整合 4 类独立物理时钟跨越 7 个时间数量级，完成 Day 20 深度预习闭环；
4. **Day 19 课程进度认证**：严格保持本日卡为 Day 19，不提前授分，不开 Day 21。

## Day19 八极能级寿命、直接B(E3)与电偶极矩相消判决性规程

**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[bucher-2017-146ba-direct-octupole]] BU17-D19-2：079的数值相消分解和唯一静态梨形认证撤回；不同中心相等不是严格同一物理矩阵元。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 磁转动、反磁转动与手征转动的时间响应与寿命判据规程

**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D19-2：080的toy轨迹不认证MR/AMR/chirality排他分类；需逐态能量、τ、branch、ICC、δ及必要伙伴观测。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 相对论光行差、光电峰探测效率梯度与逆运动学RDDS环间发散定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-18：081错误beta/角度和未计算残差撤回。以实际beta.045与六环做明确点环设计，epsilon幂律仅是假设；不报原实验bias。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 快速定时MSCD与束内寿命：176W基态带、B4/2转子检验与1-10ps时钟交叉

**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[regis-2011-fast-timing-labr3]] RG11-D19-15：082的采用输入与同源归一分开；≤4ps为该实验上限，不给通用方法阈值或独立2.87sigma裁决。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 早期RDM系统误差四大失效模式与21Ne历史偏差消解定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-18：083的历史表行/不对称误差错配，12sigma加权真值、35um/40%参数与彻底根除风险说法撤回。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-18：084把采纳480fs错当RDM、Lees710fs错当采纳值；无阻停498fs均值与接触死线归因撤回。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩

**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[kirsebom-2016-23mg-dsam-lifetimes]] K16-D19-3：085漏6899一行，实际13态；修正宽度分支(1−Bp)，不认95.5%归因、亚飞秒能力或普遍15fs死线。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-D19-2：086的N=77终止、实测共存和唯一球形D5结论撤回，恢复作者possible/替代解释与缺寿命边界。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## Day19 128I局部三角闭合、母态寿命界与N=75转动淬灭定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


**checkpoint088修订：旧标题只保历史anchor，旧科学认证已撤回。**

[[ding-2012-phd-thesis-127-128i-high-spin]] D12-D19-2：087的175ns mean/parent界、严格spin锁定和精确分量份额撤回；逐level身份、prior和实际角响应仍需核。

这些是来源核验/条件设计，不提供原实验fit、CI或新模式测量。

## checkpoint088：实际响应、表行身份与校准充分性

本节取代近期“全绿所以物理结论闭合”的推断。[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-18与[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-18绑定原件新定向阅读；[[regis-2011-fast-timing-labr3]] RG11-D19-15、[[kirsebom-2016-23mg-dsam-lifetimes]] K16-D19-3补采用输入/上限角色。旧review/needs_review保持，checkpoint079–087旧结果不作科学验证，019–078须按具体claim重审。

对衰变固有时t与静止系mean tau、无feeding、各向同性点环设计，令P=1−exp(−t/tau)为SH概率。D=sqrt(1−beta²)/(1−beta cos(theta_lab))，几何雅可比J=D²；假设效率epsilon正比E^−a，则SH/US响应比C=D^(2−a)。观察分量r=CP/(CP+1−P)，逆变换P=r/[C(1−r)+r]。真实beta=.0450和实际六环仅用于几何，a=1是合成效率斜率。

- 在P=.5，最前/最后环naive tau/tau_true=.974585/1.026824。完整C逆变换回P属于数学closure；未测eff、Gk、有限孔径、背景及Cov不能由此补齐。零beta极限与a=2抵消是模型控制。
- 给C共同增加5%，相应调整P仍可逐点重放同一r；高计数和代数反演自洽不能独立标定C。校准需要外部约束，角响应须在正确静止系积分。
- 100ns选择窗对指数parent的接受率为1−exp(−100/tau)。即tau=1000ns仍有约9.52%事件落入窗，故“有prompt事件”不推出tau远小于100ns。
- Nolan Table7是RDM/DSAM，含36Cl两态；Table5 adopted480(50)fs含前八项，非独立RDM输入。不能因多方法名称就令共享输入Cov为零。

本轮32项控制验证上述代数、Jacobian数值微分/积分、零速度极限、校准alias和必要自旋集合；不是25项独立实验检验。代码`system/scripts/day19_response_source_audit088.py`和结果`response-source-repair-result-088.json`保存实际输入/哈希/边界，不产生原实验fitCI。

最小校准仍须逐实验核八项：level/branch身份；分量与慢化尾完整性；distance零点/增益及速度分布；stopper/degrader物性与finite-foil响应；feeder门纯度和级联归一；能量/角接受与逐分量效率；PRF/PRD的能量对、设备设置、时间漂移与本底；共同校准/计数/模板Cov。TDPAD频率/矩与population lifetime不合并成同一时钟观测。

### PRD协方差反例

[[regis-2011-fast-timing-labr3]] RG11-D19-16给出的原参数边际误差不唯一确定r的误差。同1120/609keV点，额外独立假设为146.12785ps；同diag的两个PSD相关控制给201.65543/.32098ps。不能从8ps原fit残差反向补实际Cov；d offset的精确抵消也不消a/b/c相互相关。新代码32项数学/表行控制不等32项实验验证。

### 坐标与零点的后续纠正

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-19：本轮原PDF6/7视觉确认Eq9是−(d−d0)/(v tau)，旧checkpoint025的plus坐标桥与11um认证撤回。只记录源relative距离与d0描述，不猜actualproducer。单点tau的零点导数依赖P/a；多distance同时拟合a/d0/tau及v时必须联合传播Cov，不能固定Delta tau=Delta d0/v。

## checkpoint089：门比、存活斜率和所选样本归一

[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-8/9与[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D19-5区分真正observable与估计量。

设反应布居B，B→A→终态、各branch为1；B_shifted门只接受到foil前已发B光子的event。定义S_B为B存活、p_A为A占据、F_A为A已衰变，F_A′=p_A/tau_A，且门所选总概率F_A+p_A=1−S_B随距离变化。原门比的连续极限是p_A/F_A′，不是−p_A/p_A′。

| 明示控制 | tau_A2ps、tau_B10ps，t2ps的结果 | 含义 |
| --- | --- | --- |
| 完整分量、reference归一 | p_A/F_A′=2ps | 门条件下可消所选feeder时延 |
| 假设foil .16ps、bridge丢失 | exp(−.16/2)p_A/F_A′=1.84623ps | 平坦仍可偏；不估原实验bias |
| 改慢分量对数斜率 | −p_A/p_A′=−4.41722ps | 占据正在增长，不是寿命估计 |
| 所选门总和各归一1 | (p_A/N)/(d(F_A/N)/dt)=4.43894ps | distance-dependent门接受被混入导数 |

t8ps时同一慢分量log slope为12.04787ps，晚期趋feeder10ps而非A的2ps。prompt单指数特殊例里常数foil因子会在log slope抵消；不能把这项恒等式外推给有feeding的真实DDCM。

本轮46项条件控制用独立时间积分、CDF数值差分、概率守恒、prompt/延迟和效率梯度反例检验这些陈述。没有原始逐distance计数、谱窗/normalizer/foil轨迹和Cov，不产原fit、CI或真实修正比例；也不把3.1875中心速度比变成3.1875倍实际精度提升。

## checkpoint090：条件尺度不变性与导数误差的共同输入

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-19区分fe/fn和完整速度历史；[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-10绑定实际门公式与合成误差设计。[[iaea-2026-stopping-s-au-o-ta-records]] ISP26-D19-1撤回旧066无条件免疫/停止校准推断。

在无限均匀介质、无feeding/散射的声明模型中，令u=v/v0，du/dt=−ke a u−kn b sqrt(u)，a=.6/ps、b=.4/ps、u0=1。这个toy law仅演示两个nuisance，不是LSS/SRIM或真实箔模型。整体ke=kn=k使u_k(t)=u0(kt)，于是同target F提取tau/k；但只改ke时轨迹形状改变，tau0=.1/.3/1/3ps的局部灵敏度为−.58861/−.56959/−.53657/−.51745。ke=1.3、kn=1给首末两态Q比相对变化+0.9397%，四态B双比值相对变化−0.02842%。数值大小取决于这个design；它已足够反驳“部分停止变化也严格取消”的普遍命题，不证明实际结构结论会翻转。

对逐distance独立Poisson-thinned S/U及独立reference R，同一点归一共用R时，在一阶传播下Cov(S/R,U/R)=S U Var(R)/R^4为正。输出tau_i=U_i/[(S_i+1−S_i−1)/(2h)]须传播全部输入Jacobian，不能把多个tau_i当独立数据；共同velocity/distance gain还带来正的rank-one项。

| 合成五点均值误差控制 | sigma(ps) | 条件 |
| --- | --- | --- |
| 错当各点总误差独立 | .03265 | 忽略off-diagonal |
| 同weights、完整Cov | .07153 | 保reference、shared endpoint及共同校准 |
| GLS、完整Cov | .07143 | 不低于共同标度floor .07137 |

这里N=10^6/点、R=4N、tau2ps和3%/2%校准都是合成输入；没有实际event/原Cov就不能报告源的寿命精度/CI。有限差分在此prompt例的中心偏差另存，不当统计variance。58项闭式积分/独立quadrature、反演、Jacobian/矩阵/负例控制通过，不是58次独立实验验证。

## checkpoint091：Radeck主线的完整证据账本

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-20–24是本轮实际完整十页文本与全部关键visual scope，不能以hash或旧预习替代。三个state寿命、四条B(E2)和B4/2并不对应八份独立实验；2+2两枝共享tau并采用Ref46输入，IBM首行按实验B2归一，Fig13多数点沿用上游。

方法选择需保ring/level角色：2+1用四外环并校退取向；4+1/2+2仅两端环，近90deg邻线分离不足与统计不同。最短3um/大distance点在校准、attenuation fit或lifetime fit中的角色不能混并成一张统一mask。报8.36(29)、2.31(16)、1.7(2)ps为作者结果；本任务不补原Σ或重报CI。

TableI alpha不可靠、90deg效率理论代换、Winther初始取向、同charge-state/velocity的g校准和literal坐标边界一起进入最小校准清单。校正后sum平坦与多ring一致只验证各自诊断范围，不排除共同偏差。弱振动解释保作者/模型层，finite boson U5=1.5不与几何vibrator=2混成互相矛盾的实验标准。


## checkpoint092：响应先于方法窗口的选择

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-20–27的本轮主线scope为88页文本和27页关键视觉。方法选择先定义observable，再问是否有充分校准：DSAM需投影速度历史/介质与feeding；RDDS需S/U/慢化尾库存、门/级联/normalizer和distance/velocity；电子计时需matched PRF/zero-time、尾部与centroid角色；间接方法另需beam stopping/矩阵元路径、form-factor或partial/total width转换。历史窗口不能当固定阈值，模型相合不增加独立数据。

Fig11–12把feeding路径与速度门直接连到响应；RDM的背景/feeding式不能省略后再把曲线变化全归tau。PRF的FWHM、尾部半衰尺度与centroid是不同量；219Rn counterexample支持能量/设置匹配校准，而不支持本任务归因某个原实验具体偏差。CoulEx/NRF等companion仍要逐项列共享与非共享输入，不能统称stopping-free truth。

Literal公式边界单列：Nolan Eq6.5源字面似与通常initial-spin权重相反，Eq6.2 stopping符号需先声明。当前不复制成可执行公式或改原件；后续以独立定义/极限核验，不把全文阅读认证为公式全正确。


## checkpoint093：间接companion也必须通过observable合同

[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-28–31把上一轮字面疑点转为可重算条件推导。用Hermitian张量的reduced-matrix定义以及独立Racah磁量子数求和，B(0→2)=5B(2→0)；源Eq6.5的字面不通过此定义的检查，故不复制成转换公式，也不修改raw或冒称正式勘误。

选择CoulEx/NRF作companion应先声明观测量：CoulEx的S=−dE/dx正值要配正确积分限；NRF的q=Gamma0²/Gamma并非总宽度。q1meV合成控制中b0=.2至1给tau26.33至658.21fs而q不变，补r=Gamma0=4meV才得到条件总宽度16meV、tau41.138fs。这个例子说明需要额外branch/partial-width输入，不给真实tau readiness。

最小清单增补：初态自旋平均、up/down方向、signed stopping约定、partial/total/radiative/ICC宽度身份、flux/source-line/角响应与共同Cov。35项数学控制包含已知角动量极限、正反积分、thin-target极限和NRF连续退化；不等于35项实验验证，不补实际CI。


## checkpoint094：快速定时须按设置和级联校准

[[regis-2011-fast-timing-labr3]] RG11-D19-17–23补本轮实际89页文字/30页关键视觉scope。现代方法主线已核，不继承全部105页科学正文断言；模型/systematics未新读部分保留缺口。

| 校准/案例 | 来源实际输入 | 可复用边界 |
| --- | --- | --- |
| Ch4 Fit1 | -850V/20ns，152Eu fullenergy，240–1300keV，8ps/2sigma | 残差不等参数预测Cov/任意pair CI |
| Ch4 Fit3 | 加133Cs53→303/30(5)ps参考与214Po高能点，50–1510keV | 低能点是新增有寿命/背景依赖的校准，不是Fit1外推 |
| 176W Ch5 | -1200V/8ns，源在beamspot、36h，7ps/3sigma | 重新匹配设置/能量门；108keV长寿命是slope，不自动支持同能量20ps目标 |
| 跨级联门 | 直接门与更高feeder比较，4+上游另移21(8)ps | centroid含中间态累计等待，不可全归目标tau |
| 低能background | 未shield chi²1.22仍有不可可靠扣除的延迟；shielded/HPGe为companion | 良好拟合/高计数不替代背景时间响应；不从中心差单独证明bias |
| 接近prompt上限 | 单设置≤2–8ps与最终Bi≤15ps/Po≤6ps区分 | 不挑最小上限，不擅填95%CI；参考寿命/共享Cov随采用关系传播 |

最小清单需再明确：CFD/PMT voltage、delay、threshold和energycalibration；directfeeder/中间级联路径；分branch/fullenergy-background样本；calibration family/range/误差约定和reference谱系；时间窗/漂移/几何匹配与fullCov。正文“onlypossibleerrorbackground”是作者在特定假设下的概括，本任务不将其推广为无条件定理。原events/fullCov缺失仍是readiness，不造新fit。


## checkpoint095：方法选择全景决策树与最小校准八项清单

**checkpoint108修订：撤回原“决策控制通过即科学完成”的认证。** 来源合同见[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-22/23/24、[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-20/21及[[regis-2011-fast-timing-labr3]] RG11-D19-18/19/20。下面是可检查的决策流程；方法窗口须由实际响应决定，原固定fs/ps/ns分区不再作为准入规则。

1. 先绑定核素、母态/末态、实际分支与目标量。测tau、测部分宽度和测静态矩是不同问题。
2. 有已校准的反冲速度历史、介质/几何与feeder输入时，评估DSAM对目标tau的响应灵敏度；无真实transport时只列readiness。F=s/(s+tau)及最大导数.25只属于无feeding的一维指数减速toy，不是所有DSAM的灵敏度。
3. 有distance/velocity、可分辨分量和匹配门时，评估RDDS。短tau不能由dmin/v一条式否决；延迟feeding和DDCM门也可提供信息。finite-foil、慢化尾和退取向必须随observable定义进入。
4. 有成对能量/branchrole、matched PRF/PRD和时间刻度时，评估电子计时。slope/deconvolution/centroid选择取决于完整响应、本底、时间窗、统计与可识别性；FWHM不是万能切换界，斜率也不自动免疫非高斯PRF尾和延迟本底。
5. 测g/Q可考虑TDPAD的进动与扰动响应。人口寿命来自匹配time-spectrum envelope分析；R(t)比值可消共同人口衰减，不能把调制周期或alignment弛豫当tau。
6. 比较候选方案是否能识别相同level/branch的tau，以及哪些输入独立；没有当前匹配输入时不给唯一“最佳/可行”判决。

最小清单（逐项记录已知/缺失及其locator）：
| 项 | 必须核对的输入 |
| --- | --- |
| 1 | level/transition身份、mean/half-life、branch分母、ICC/mixing及up/down/几何约定 |
| 2 | SH/US/慢化尾或快/慢/bridge库存、峰窗、本底/污染和全部归一对象 |
| 3 | distance零点/增益、速度分布/反应运动学、实验室与proper time及时间刻度 |
| 4 | target/stopper/degrader厚度密度/损伤及电子/核停止；TDPAD需host/EFG或localfield |
| 5 | directfeeder与远端feeder路径、未分辨feeding、级联等待和gate效率/normalizer |
| 6 | 角响应/有限孔径/逐分量效率、boost/deorientation；TDPAD的spin/alignment/场方向 |
| 7 | energy-pair/settings/time-window/geometry/drift匹配的PRF/PRD；TDPAD脉冲/计时响应与外场标定 |
| 8 | event/模板/reference共享、完整Cov、校准floor、单侧界构造与未识别nuisance |
八项是本任务组织方式，不是任何来源保证能自动消除偏差的定理。

## checkpoint096：实验设计证伪反例与最小清单排错机制

**checkpoint108撤回科学认证。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-22/23与[[regis-2011-fast-timing-labr3]] RG11-D19-19/20/22给真实方法边界。旧合成PRD=14ps不是Fig4.15实际读数，3.5ps不是176W已知1sigma；7ps为该段3sigma残差，仍不等实际预测Cov。旧23sigma/109sigma、固定.08ps精度没有实际likelihood，不作实验反证的显著性。

在已标记、匹配的理想MSCD中，若真PRD14ps、tau5ps，则DeltaC24ps，误设PRD0会给12ps；只是声明参数的代数。RDDS的tau1+u2*tau2是完整反应到目标衰变的均值，不普遍等离散distance单指数fit输出；直接feeder gate在finite-foil和所选样本下也不能手动设tau_gated=tau_true当验证。DSAM的tau/k仅在完整速度轨迹统一时间重标且其余合同固定时成立，电子-only+25%不保证tau−20%。

5ps目标不能只凭质量区/位移宣布固体DSAM不可用、气体DSAM在1–2atm可行、RDDS最佳或MSCD有固定4ps准入。须有实际reaction/transport、谱线分离/门/效率、PRF/背景/统计、几何与Cov。新可复现练习沿response088、gatedfoil089、stoppingCov090、indirect093的明确假设和反例，不沿旧suite096的“恢复真实寿命”认证。

## checkpoint099：跨质量区四类方法基准与物理时钟正交性

**checkpoint108撤回“完全正交独立时钟/主导系统学互不共享”认证。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-24/27、[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-8与[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-8区分observable及输入。不同机制不推出Cov=0；branch/stateidentity、feeding、velocity、timecalibration/normalization等仍可共享。

旧benchmark把合成stopping时间当23Mg实际输入、把F接近1称极高灵敏、将103Rh0.72ps错贴9/2+、134Nd2+错写45.4ps及把angularfrequency当MHz；均撤回。正确源身份见[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-11、[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D19-6。Radeck091、Nolan092、Regis094是已读scope，不由benchmark脚本赋独立实验或全面正确认证。

## checkpoint100：Day19全景综合审计与证据链终验

**checkpoint108撤回“100检查点全景终验、274项零占位符、100%科学闭环”的认证。** 旧程序主要读取JSON的passed字段、计数/文件存在和retirementguards，没有证明来源支持、raw读scope真实性、脚本非平凡性、科学假设或全部checkpoint。095–107含恒True、相同表达式两侧比较、手填sigma和物理外推，不能被此汇总自动认证。

Radeck091/Nolan092/Regis094的实际scope记录和各自局部原读结果保留；旧088–090撤回仍有效。当前source依据[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-20、[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-22和[[regis-2011-fast-timing-labr3]] RG11-D19-18分别引用，未逐claim核者继续pending。

## checkpoint109：完整时间谱也需要独立prompt约束

[[regis-2011-fast-timing-labr3]] RG11-D19-24/25给可重算的条件反例；[[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-23说明PRF tail/centroid等响应对象不能混用。设角色无法区分的时间差由等权+/-指数和稳定prompt卷积得到：F=G_sigma*L_tau1。由于L_tau的特征函数为1/(1+tau²k²)，令a=tau2²/tau1²便有：

P1 = G_sigma * [a delta + (1−a)L_tau1]，
P1 * L_tau2 = G_sigma * L_tau1。

0<tau2<tau1时混合权重合法、所有kernel归一且非负。合成sigma80ps、tau1=20ps与tau2=10ps对应不同prompt（variance6400/7000ps²）和相同完整观测（7200ps²）。这比“质心相同”更强：完整谱、任意相同ROI选择及任意更多同分布计数均相同；但已独立知道prompt为G_sigma或有可靠role标签时，不满足这个未知prompt族前提。

代码day19_prompt_tail_identifiability109.py用解析特征函数证明，加独立时间域卷积、网格细化和归一验证；不是读取passed字段认证science。原source并未报告这种失效，不能把本toy尾部迁给实际LaBr3。实验设计的下一输入是matched fullenergy/能量对/settings/时间窗prompt响应及其误差，或独立可验证的feeder/decay角色识别；仅给更窄峰/更大N不能补它们，缺失时写readiness。

## checkpoint110：TDPAD完整scope与模型/feeding桥

[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-9–11与[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-9分别补完整主线和关键模型图。Ionescu的Qs/g是校准后的state-specific结果；Table1的K混合、xi/epsilon/gamma/core-energy和signQcal是PTR层，同一absQs可由不同模型输入近似描述。Grodner的orientation约.15来自指定组态/参数PRM，不是g值直接读出的几何。

Day19设计边界有一个原文实例：129Ce建议的11/2−近邻态可在数ns feeding后布居9/2− isomer，而约11ns响应未辨它。不能把“衰变曲线看似单指数”升级为没有feeding，也不能把作者plausiblehalf估计当新测量。Eq6的S(J)归一与其他staggering定义不同；四个有理数rigidE=A J(J+1)+const控制给S0，只核定义，不测shape。Table2的131Cepositivegs epsilon范围与结论概括、PDF15gamma趋势措辞均按源字面保留，不以自动参数匹配消歧。

## checkpoint111：prompt参考样本本身也有限

[[regis-2011-fast-timing-labr3]] RG11-D19-26/27在109的同role丢失模型中，给一个独立matchedprompt能提供什么信息的计算例。完整secondmoment相加给Q=tau²=(M2D−M2P)/2；若只估测一条delayed分布而把prompt方差硬固定，便漏掉calibrator误差。Gaussianprompt的声明模型下：

Var(Qhat) = [A/N + B/N0]/4，
A = 2sigma⁴ + 8sigma²tau² + 20tau⁴，
B = 2sigma⁴。

共享计数/参考时一般式须加−2Cov(M2D,M2P)，不是默认全独立。固定检测总count时局部最优N/N0=sqrt(A/B)，但eff/rate未知就不能转成beamtime分配。sigma80ps、tau20/5ps、目标局部sigma_tau.5ps的等count设计分别每谱约1.17e5/1.65e6；这是方差差估计器在指定模型下的规划，不是有role标签MSCD的普适要求。

独立随机Gaussian+signedexponential模拟每谱N1000、重复2000，验证Q方差并保留负值：tau20时Q<0约3.3%，tau5时约46.25%。平方根/截零会引入边界/选择效应，因此不把局部delta-method误差当有限样本CI。另sigma误配±2ps已使tau20控制变为23.622/15.427ps；tau5误用82psprompt会超扣二阶矩，不能以负Q宣布负物理寿命。

实验readiness仍需同能量/设置/时间窗的prompt均值与二阶/四阶矩或可执行响应、role纯度、本底和计数/参考Cov；有限ROI必须正确处理接受，而不能直接套完整支持矩公式。更多target事件不能补未知prompt transfer；本设计没有原数据或新的实验fitCI。

## checkpoint112：多探测器GCD的pair筛选、权重与背景

[[regis-2015-generalized-centroid-difference]] RG15-1–8为本轮新公开稿，实际全文5页+空白第6页、全部4图/12式视觉核过。16LaBr3的120个pair有24个因cross-talk排除，96个剩余pair的role谱叠加与同pair双branch常数alignment是方法操作；Ge gate和152Eu/49Ti校准是实际companion，不是仅用更多pair平均消除系统误差。

对100Zr，图上C1332ps与Compton683ps、Pi2.6按Eq12给net C约1581.615ps，再用PRD−61ps给tau约821.308ps，核作者821(12)的中心舍入。没有原Cov/误差语义不重造其sigma或CI。Pi的B/P和B/(P+B)分母区分，caption about40%保字面边界。

下一项可证伪设计是检验合并权重：每pair对称施常数shift虽在该pair的DeltaC消去，但合并两branch的pair权重若不同，shift项未必消；calibrator与目标样本的mean PRD还需相同权重/响应或正确重权。这里先列条件缺口，不断言EXILL实际违反前提。已知正确role、完整支持且有限一阶矩的centroid移位不要求Gaussian PRF；109–111丢role的声明模型不能当原GCD限制。

## checkpoint113：阵列合并权重与对齐平移消去条件

**checkpoint114修正数学量词及MC范围。** [[regis-2015-generalized-centroid-difference]] RG15-9是本任务根据Eq11/Sec3提出的合成设计，非原作者实验偏差。令归一化权重a=w+/sum(w+)、b=w−/sum(w−)，有

ΔC_after − ΔC_before = Σ(a_i−b_i)s_i。

对任意独立pair平移s都保证相消，当且仅当a=b；原始权重无需逐项相同，只需成比例。对某一固定s，必要充分条件仅为上述内积等于0；例如共同7ps平移，或三pair的(a−b)=(1/4,−1/4,0)与s=(1,1,9)ps，都在不同权重下相消。旧不加量词的“充要条件”为过强断言，撤回。

声明pair模型C+_i=T0_i+PRD_i/2+τ、C−_i=T0_i−PRD_i/2−τ时，合并prompt响应为R(a,b)=Σ(a_i−b_i)T0_i+Σ(a_i+b_i)PRD_i/2，所以τ=(ΔC−R)/2。不同角色权重本身不等于不可校正；校准与目标均用匹配权重及相同alignment约定，响应项也同步改变，寿命可保持不变。若a=b=w才简化为R=Σw_i PRD_i。

原113两pair例中，alignment使ΔC从14变50ps，差36ps；这不是已测寿命偏差。对称目标w=(.8,.2)的PRD为−8ps，误借等权校准PRD10ps给τ偏−9ps。不同权重也可能给同一标量PRD（例如所有pair PRD恰为10ps），匹配权重是稳健保证，非每个具体数值巧合的必要条件。计数池与等权均值作为一般线性算子等价要求等pair计数；某些相同centroid输入也可能偶然相等。

113的1200次MC只抽Gaussian，不含指数寿命涨落，仅检该噪声模型的方差比1.009。若按同样tau20ps、每role每pair150事件抽Gaussian加指数等待，完整支持下每branch方差应加τ²，ΔC方差由113.333变116ps²；未做本轮新MC或有限样本CI。day19_gcd_weight_contract114.py用有理数、基向量平移、比例权重、固定平移反例和完整响应扣除核验这些条件。原113结果JSON保字节；原events/sorter/权重/校准Cov缺失时只写readiness，不判断FATIMA违约。
