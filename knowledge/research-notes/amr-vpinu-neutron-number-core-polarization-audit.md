---
type: research-note
title: "AMR的Vπν、中子数与核芯极化：同中子数Cd/Pd比较和条件微观推导"
aliases: [AMR Vpinu neutron number core polarization, Cd Pd same N interaction audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full, zhang-2013-105106cd-pnc-superfluidity, zhang-2019-104pd-pnc-antimagnetic-rotation, kumar-2023-amr-review, qiao-2025-pd-systematic-amr-metadata, pohl-1996-107108pd-highspin-metadata, juutinen-1994-109111cd-107pd-highspin-metadata]
created_from: Day26 delegated AMR Vpinu and neutron-number research
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, quadrupole-interaction, core-polarization, neutron-number, 106Cd, 104Pd, 110Cd, Pd]
---

# AMR的Vπν、中子数与核芯极化

## Research Trigger

106Cd和104Pd均为N=58，质子相对Z=50闭壳层分别少2和4个，是否意味着104Pd的四极粒子–空穴相互作用Vπν更强？中子数从106Cd的58增至110Cd的62，或102Pd的56增至108Pd的62，是否通过h11/2费米面上移使剪刀闭合变慢、核芯惯量增大？本页将这些直观猜想拆成文献已给的参数、可求导的有效模型与尚待微观计算的机制。

**本轮直接原件结论：不能声称104Pd已测出比106Cd更大的Vπν。** Rather2014直接沿用Cd的Vπν=1.2 MeV，并采用有效两空穴构型；Roy2011同样把106、108、110Cd均取1.2 MeV。PNC四空穴模型与此不同，不能靠“多两空穴”把唯象参数乘二。中子费米面随N上升只是待自洽核验的起点，h11/2占据、自旋对齐和核芯响应须分别计算。

## Grounded Evidence

| 核/问题 | 原件定位 | 原文结果或输入 | 证据性质与边界 |
|---|---|---|---|
| 106、108、110Cd的Vπν | [[roy-2011-cd110-systematics-antimagnetic]] printed324–326 Eqs3–6、Fig3及结论 | 三核均用Vπν=1.2 MeV；Vππ约0.15–0.20 MeV | 沿该模型用I(ω)系统学约束/沿用的有效参数，非裸TBME直接测量 |
| 108Cd到110Cd的构型 | Roy printed324–326 | 108：jν=16、n=8、ℑ=0；106：有效jν=18；110：jν=10、n=4、ℑ=19.5 ℏ²/MeV，因alignment不支持g7/2额外对齐 | 活跃中子构型改变；N增加不等于jν单调增加 |
| 同N的104Pd/106Cd | [[rather-2014-104pd-antimagnetic-arxiv-full]] PDF pp4–6 Eqs4–9及结论 | 104Pd沿用Vπν=1.2、Vππ=0.2 MeV；有效πg9/2⁻²⊗ν[h11/2²(g7/2/d5/2)²]，jν=16、n=8；ℑ=5、ℑrot=17 ℏ²/MeV | 作者把104Pd/106Cd当邻近系统迁移参数；没有独立的四空穴Vπν拟合 |
| 104Pd微观空穴 | [[zhang-2019-104pd-pnc-antimagnetic-rotation]] PDF pp5–7 Figs4–7 | πg9/2有四个部分空穴；约0.4 MeV中子ν1/2−[550]占据由约0.4突增至2；gd占据下降；质子空穴随后重排 | PNC-CSM结果；价空间相对100Sn计数，与半经典有效两空穴不同 |
| 106Cd中子交叉 | [[zhang-2013-105106cd-pnc-superfluidity]] PDF pp7–10 | 约0.3 MeV的g7/2→h11/2占据改变；配对影响交叉；高频需形变调整 | 模型结果；不是只随静态N变化的简单填壳 |
| 102–108Pd证据覆盖 | [[kumar-2023-amr-review]] Table3 pp78–80；[[pohl-1996-107108pd-highspin-metadata]] | 102Pd为混合集体/可能AMR；104Pd有DSAM；本综述未列106/108Pd AMR | 不能建立整条偶偶Pd AMR参数序列；高自旋谱学存在不等于AMR寿命存在 |

## Provisional Reasoning

### 1. 首先区分三种“相互作用强度”

微观两体矩阵元vJ、有效四极耦合κπν和半经典剪刀能量中的Vπν不是同一个量。可用一个明确约定的模型写为

$$H_{Q}=-\kappa_{\pi\nu}\,\hat Q_\pi\!\cdot\!\hat Q_\nu.$$

Q的单位若为长度平方，则κ为MeV/长度四次方；采用无量纲归一的Q时κ才是MeV。将给定多体态的转动密度、占据和配对平均后，才能把角依赖投影成

$$E_{\pi\nu}(\theta)=E_0+V_2P_2(\cos\theta)+V_4P_4(\cos\theta)+\cdots.$$

把V2称作有效Vπν是一个模型约定。它已经折入活跃核子数、轨道四极矩、角动量耦合及核芯极化，不能再无条件乘以质子–中子对数。Roy/Rather把每侧粒子–空穴项写为Vπν P2/2，两侧相加为Vπν P2；n主要控制粒子–空穴与空穴–空穴项的相对归一。将n=8机械替换为“8个1.2 MeV相加”会重复计数。

半经典Vπν的正号对应该约定下粒子–空穴的正交极小、排斥角项；裸κ的符号、空穴变换符号与具体轨道矩阵元不能从这一正号直接反推。适合比较的对象应是同一构型空间中的角势曲率，而非不同作者符号相同的参数名。

### 2. 同N并不固定中子波函数；四空穴也不自动把力矩加倍

Z从48变46会同时改变质子配对、形变势面、质子–中子平均场和中子Nilsson谱。即便N=58，h11/2与gd占据、交叉频率和转动密度仍可不同。Roy用106Cd的有效jν=18，而Rather对104Pd取jν=16；这已说明“同N就固定中子刃长”的前提不成立。二者都是有效合矢量输入，不应当作同一量子态的自旋测量。

若四个空穴在某个受控经典极限下分成两组完全相同的对称刃，每组对同一中子密度贡献vP2，则总角势可成为2vP2，其粒子–空穴力矩幅值为

$$|\tau_{\pi\nu}|=\left|-\partial_\theta E_{\pi\nu}\right|=3V_2|\sin\theta\cos\theta|.$$

**这里乘二只对固定单刃矩阵元、相同相位/角度且忽略反对称与配对的反事实模型成立。** 真正g9/2⁻⁴波函数必须反对称化；低频PNC非对角配对贡献使四支独立刃分解不唯一。同一j壳两空穴的最大J为8、四空穴为12，最大角动量只增长50%，已经反驳“空穴数加倍→所有响应加倍”的普适推论。

一个可精确枚举的反向例是：在完整g9/2壳中移走时间反演配对的±m，构造反对称轴向Slater空穴态，取公共径向/约化系数外的q=3m²−j(j+1)。两空穴移走±9/2时，Qhole=−72；四空穴移走±9/2和±7/2时为−96，幅度比4/3；若移走±9/2和±1/2，反而为−24，幅度比1/3。这些都是时间偶轴向四极控制态，**不是AMR推转态或实际Pd占据**，却严格说明相同单j壳中“更多空穴”不能单独决定总四极源的大小。固定中子Q与耦合时，相应P2系数也不会按空穴数自动加倍。程序枚举全部5种两空穴与10种四空穴配对选择。

PNC104Pd中四个部分空穴会改变质子Q张量与可用对齐空间，也可增强、削弱或重新分配角势的P2与P4分量。要给出Vπν比值，应在同一EDF/PNC方案固定同一形变与角约束，计算E(θ)、减去相同定义的核芯和配对能，再拟合Legendre系数及误差；当前文献没有交付这样的106Cd/104Pd配对抽取。

### 3. 核芯极化如何重整化四极力矩

可复用的条件推导取核芯四极坐标qc、正定刚度矩阵C及外源Qπ、Qν：

$$E_c={1\over2}q_c^{\mathsf T}Cq_c-q_c^{\mathsf T}(F_\pi Q_\pi+F_\nu Q_\nu).$$

令∂E/∂qc=0，得到

$$q_c=C^{-1}(F_\pi Q_\pi+F_\nu Q_\nu),$$

$$\Delta E_c=-{1\over2}(F_\pi Q_\pi+F_\nu Q_\nu)^{\mathsf T}C^{-1}(F_\pi Q_\pi+F_\nu Q_\nu).$$

交叉项为

$$\Delta E_{\pi\nu}^{\rm induced}=-Q_\pi^{\mathsf T}F_\pi^{\mathsf T}C^{-1}F_\nu Q_\nu.$$

它给出“更多空穴改变核芯极化”的具体含义：Qπ与核芯柔度C⁻¹共同控制诱导耦合。若四极势面变软且相关投影同相，诱导项可增强；若轨道贡献抵消、配对增强或形变变硬，结果可能相反。核芯接近软模、C不再正定时，该静态消元失效，必须显式保留集体坐标。这是自建二次响应模型，不是已经对Cd/Pd求得的数值。

此外，核芯转动惯量是对时间奇Coriolis场的响应，四极柔度是对时间偶形变场的响应。它们在自洽理论中相关，但**Q柔软或空穴更多，不构成ℑcore必增的定理**。E2有效电荷和磁矩g因子也各自具有不同极化通道。

### 4. 剪刀“闭合快慢”必须标明自变量

取c=cosθ、jh固定，Roy型约定为

$$I_{\rm sh}=j_\nu+2j_hc,$$

$$V_{\rm sh}=V_{\pi\nu}P_2(c)-{V_{\pi\pi}\over n}[P_2(2c^2-1)-1],$$

$$\omega_{\rm sh}={1.5V_{\pi\nu}\over j_h}c-{6V_{\pi\pi}\over nj_h}(2c^2-1)c,$$

$$I=j_\nu+2j_hc+\mathcal J_c\omega_{\rm sh}(c).$$

其中I的数值以ℏ计、ωsh以MeV/ℏ计、ℑc以ℏ²/MeV计；代码采用ℏ=1的数值单位。Vπν是角势能标度，不是耗散阻尼或真实时间演化速率。

- **相对频率ωsh**：正稳定分支有dc/dωsh=1/(dωsh/dc)。较大Vπν意味着相同闭合角需要较高频率，因而按频率扫描闭合较慢。
- **相对自旋I**：若ℑc=0，则c=(I−jν)/(2jh)，Vπν完全从B(E2)随I的轨迹消失。只改变Vπν不能改变固定刃长的B(E2)(I)。
- **有核芯时**：令

$$D\equiv{dI\over dc}=2j_h+\mathcal J_c\left[{1.5V_{\pi\nu}\over j_h}-{6V_{\pi\pi}\over nj_h}(6c^2-1)\right].$$

当D>0，且固定B0、B/B0=(1−c²)²，

$${dc\over dI}=D^{-1},\qquad {d(B/B_0)\over dI}=-{4c(1-c^2)\over D}.$$

所以较大的正核芯响应使相同角度处的下降更慢；这需要参数固定、稳定分支和固定Qeff。Qeff随I变化时还多一项(dB0/dI)(1−c²)²，足以改变平台或塌缩形状。

ωsh是有效模型的内部频率。Rather还定义物理比较频率ω=ωrot−ωsh，并引入ℑrot。因此dI/dωsh不能直接标成实测J(2)；ℑ=5和ℑrot=17也不能相互替换。

### 5. 受控算例：能说明敏感性，不能替代同位素拟合

程序固定jh=4.5、Vππ=0.15 MeV、n=4，在c=0.5比较：

| Vπν / MeV | ℑc / ℏ²MeV⁻¹ | ωsh / MeV | D | dc/dI | d(B/B0)/dI |
|---:|---:|---:|---:|---:|---:|
| 1.2 | 0 | 0.2125 | 9.0000 | 0.11111 | −0.16667 |
| 1.2 | 5 | 0.2125 | 10.8750 | 0.09195 | −0.13793 |
| 1.2 | 19.5 | 0.2125 | 16.3125 | 0.06130 | −0.09195 |
| 2.4 | 19.5 | 0.4125 | 24.1125 | 0.04147 | −0.06221 |

最后一行是“假设V加倍”的控制场景，**不是104Pd的实测/拟合参数，也不是四空穴的物理上界**。ℑc=0时两种V的B(I)完全相同；ℑc非零时二者会通过核芯竞争改变闭合轨迹。这揭示了V、ℑc、jν和Qeff之间的不可辨识性：单凭B(E2)下降斜率不能单独抽出Vπν。

### 6. 随N增加：h11/2费米面图像要保留三个修正

**第一，N不能直接映射为h11/2粒子数。** 50–82壳同时含g7/2、d5/2、d3/2、s1/2和h11/2；配对、形变与Coriolis项使这些轨道混合。104Pd PNC在同一N=58的核中，频率约0.4 MeV就出现ν1/2−[550]占据突跳，说明转动驱动的占据重组本身可大于两相邻同位素的平滑填壳效应。106Cd的交叉机制也涉及gd→h11/2转移。

**第二，四极贡献随占据可以相消。** 对单一j壳，选定量子轴后角向对角四极矩有

$$q_{20}(j,m)\propto3m^2-j(j+1),\qquad\sum_{m=-j}^{j}q_{20}(j,m)=0.$$

h11/2的角因子从|m|=1/2的−35到|m|=11/2的55，完整壳的迹为零。公因子中的径向矩阵元、角动量约化系数和有效电荷另行指定；此式不能直接给实际形变符号。它说明不同m/Ω的填充可增强或抵消Qν，高半壳的空穴图像与低半壳的粒子图像会重新组织角势。**不能把此单j算式标成“106Cd到110Cd已经跨越h11/2半满”**，因为实际占据未核验，旋转轴m也不等于固定Nilsson Ω。

**第三，惯量由准粒子能谱和配对共同控制。** 在一个明确约定的BCS线性响应近似中，

$$\mathcal J_{\rm IB}=2\sum_{\mu<\nu}{|\langle\mu|J_x|\nu\rangle|^2(u_\mu v_\nu-u_\nu v_\mu)^2\over E_\mu+E_\nu},$$

指标求和与Kramers简并因子须在具体实现中一致。这是条件示意，并未替代Thouless–Valatin自洽响应。费米面附近小分母、Jx矩阵元与配对的变化可使惯量上升；闭壳接近、阻塞、残余相互作用与形变变化也可削弱响应。因此只说“中子更多→配对弱→ℑc更大”缺乏普适依据。

Cd链已有具体反例：Roy对N=58的106Cd取有效jν=18，对N=60的108Cd取16，对N=62的110Cd取10，同时把110Cd的ℑc取19.5。这里的额外中子没有增加活跃剪刀刃的合自旋；解释来自不同对齐构型与核芯分担。Vπν反而保持1.2 MeV。该模型支持配置重组与角动量分担的变化，不支持已经测定Vπν随N单调衰减或增强。

### 7. 102Pd到108Pd：目前可提出方案，不能给缺失的数值趋势

Pd链N=56、58、60、62的同一“AMR参数序列”尚未建立。102Pd综述条目为混合集体/可能AMR，104Pd有DSAM与PNC，106/108Pd在本综述AMR表中缺项；Pohl1996的108Pd高自旋谱学原件入口已保存，但正文/寿命未读。Qiao2025题名研究的是103、105、107、109Pd，不能补作偶偶102–108Pd的数据链。

可执行的下一步是对四核统一选择EDF或PNC空间，沿同一频率/总自旋约束计算：n(h11/2)、各Ω占据、配对能、Q20/Q22、Jπ/Jν、局部势面刚度、时间奇响应及E(θ)的V2/V4；再用104Pd直接B(E2)校准唯一共享的算符约定，并对其它核保留预测与缺项。这样才能判断h11/2填充究竟增强剪刀力矩、转向核芯转动，还是首先发生构型交叉。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-vpinu-neutron-evolution-20261029/`。

- `amr_vpinu_neutron_model.py`：标准库条件模型，明确ωsh、力矩、闭合斜率和单j四极迹。
- `vpinu_torque_grid.csv`：48个V/θ点；V加倍只在控制模型中使粒子–空穴力矩加倍。
- `core_closure_sensitivity.csv`：24个几何点，分别扫描V与ℑc。
- `same_N_106Cd_104Pd_scaling.csv`：同一jν控制下的V加倍反事实，不标为实际Cd/Pd拟合。
- `cd_neutron_evolution_proxy.csv`：Roy风格的jν、n与核芯参数描述；不是从B(E2)重新拟合的同位素结果。
- `h11_2_quadrupole_substates.csv`：12个m态的角四极因子，满壳迹严格为0。
- `g9_2_hole_quadrupole_controls.csv`：15种反对称配对空穴控制态；四空穴/两空穴的四极源比可为4/3或1/3，不是普适2。
- `model_summary.json`、`provenance.json`：方程、假设、输入身份和来源阅读定位。

## Assumptions

角势截断P2、固定对称刃、固定Qeff、固定构型与核芯响应；二次极化核芯的刚度正定；单j四极因子只示角向结构。任何条件模型均不冒充EDF或PNC自洽计算，不把实际DSAM线形重新拟合写成已完成。

## Competing Explanations

空穴计数、配对阻塞、形变软化、gd/h11/2转移、普通核芯转动、带交叉和寿命系统误差都能影响B(E2)轨迹。Vπν、ℑc、jν和Qeff相互补偿时，同一B(E2)(I)可有多种参数解释；实验必须联合I(ω)、Qt、绝对寿命和构型观测。

## Transfer Conditions

可迁移的是模型归一化审计、力矩求导、核芯消元和满壳四极迹；不可迁移的是1.2 MeV、19.5、5或17的具体数值、某个N对应的h11/2占据或半满位置，以及同一模型的有效两空穴直接视为四空穴量子态。

## Failure Conditions

把104Pd的Vπν写成2.4 MeV测量值；把四空穴响应普适加倍；把ωsh当作真实时间速率或未经转换的实验ω；把ℑ与ℑrot混用；把N增加当作h11/2单壳逐级填充，均使本页推论失效。

## Falsification or Reverse Tests

在ℑc=0时改变Vπν，应保持B(I)不变而改变ωsh(I)；固定四刃数、改变Qeff(I)，应可改写B的下降；在同N同EDF下冻结占据后再松开配对与核芯形变，分别计算V2的变化，以区分裸矩阵元、占据和极化贡献。若四空穴比两空穴的受控角势没有加倍，即否定简单对数比例。

## Open Questions

是否能取得统一EDF的106Cd/104Pd角约束E(θ)并抽取带协方差的V2/V4？110Cd的g7/2未对齐能否由同一PNC参数给出？106/108Pd是否有可支撑AMR的独立绝对寿命？原始线形/模型代码能否解决Roy/Rather的有效刃与Pauli修正端点映射？

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[rather-2014-104pd-antimagnetic-arxiv-full]]
- [[zhang-2013-105106cd-pnc-superfluidity]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[kumar-2023-amr-review]]
- [[amr-cd-isotopes-quantum-termination-odda-signature-audit]]
- [[amr-pd-four-hole-geometry-evolution-audit]]
- [[amr-j2-dynamic-inertia-endpoint-audit]]
- [[qiao-2025-pd-systematic-amr-metadata]]
- [[pohl-1996-107108pd-highspin-metadata]]
- [[juutinen-1994-109111cd-107pd-highspin-metadata]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`。既有撤回、人审和课程信用边界不变。

## Review Status

直接原件的Vπν参数和104Pd两种模型空间已核；条件算例已生成；完整同位素链的自洽占据、极化与时间奇响应仍未计算。

## Promotion or Rejection History

2026-10-29：拒绝“104Pd四空穴已使Vπν加倍”与“N上升保证ℑcore单调增加”的预设；建立可复算条件推导和后续微观观测量合同。

## Continuation Handoff

优先寻找/执行共享EDF的104Pd/106Cd角约束路径；同时取得106/108Pd原始高自旋与寿命正文。先统一V、Jcore与频率约定，再讨论跨同位素数值趋势。
