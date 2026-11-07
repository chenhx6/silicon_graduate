---
type: synthesis
title: "同核异能态机制、弱衰变与超重合成：跨核区可迁移条件"
aliases: [同核异能态与衰变系统学, isomer-and-decay-systematics, weak-decay-and-superheavy]
created: 2026-11-06
updated: 2026-11-07
status: active
review_status: unreviewed
confidence: medium
scope: isomers-beta-decay-superheavy-synthesis
sources: [book-jain-nuclear-isomers, paper-walker-dracoulis-1999-energy-traps, paper-dracoulis-2016-metastable-states-heavy-nuclei, paper-walker-podolyak-2020-100-years-isomers, hayes-2005-k-conservation-178hf, dracoulis-2013-192os-isomers-gamma-soft, book-suhonen-from-nucleons-to-nucleus, zagrebaev-2001-superheavy-synthesis-survival]
tags: [isomers, seniority, k-isomer, gamow-teller, superheavy-nuclei, cross-region, astromer]
---

# 同核异能态、弱衰变与合成动力学

## Agent active summary

本轮以五份新提供综述/专著、应用论文及Hayes博士论文原件补充三项主线：
异能态是衰变网络的瓶颈，不能只凭寿命指定机制；单j半满壳相消有明确对称性条件；
冷异能态稳定性与热复合核形成/存活/布居截面是不同问题。
已完成一个有界精确单j L4，数值与认识变化见
[[seniority-mid-shell-cross-region-model-test-20261107]]。
逐文件学习、暂定新课题与实际阅读范围见[[isomer-six-region-transfer-research]]。

## Question and Scope

### 从衰变通道判断机制

电磁支路满足λγ(XL)=CXL Eγ^(2L+1) B(XL)；总寿命还包括该支路内转换、
其它电磁支路、β/EC、α、粒子发射和裂变等可能过程。
需要能级顺序、允许的末态、矩阵元和竞争宽度，不能只由高自旋或质量区判断。
综述提供机制框架，具体能级和寿命仍回到原始实验。

| 机制 | 实际被抑制的因素 | 迁移成立条件 | 失效、混合与反例 |
|---|---|---|---|
| 自旋陷阱/能谱瓶颈 | 可及末态的自旋、能量和跃迁矩阵元使快通道受抑 | 局部多重态排列、低Eγ或较高多极性等共同形成瓶颈 | 不要求统一ΔI≥3；低能E2也可能延长寿命；组态/形状混合可并存 |
| seniority/粒子—空穴选择 | 特定价空间和态对的偶秩一体矩阵元抑制 | 明确价核芯、粒子/空穴占据、seniority或相关离散对称性及算符 | 多轨道、不同seniority/粒子—空穴signature、有效算符和组态混合改变结论；不能把任何弱E2都归因半满壳 |
| K阻碍 | 近轴对称描述下，初末态K分布与多极性不匹配 | K是有用近似量子数，ΔK与支路XL可指定；用分γ寿命提取阻碍 | 三轴/γ涨落、Coriolis顺排、偶然态混合、末态混合和相干相消均可影响；一个fν不能唯一反演γ |
| 形状陷阱 | 不同集体构型之间的重叠与势垒穿越受抑 | 相关形状坐标、集体质量、组态及隧穿通道共同形成亚稳态 | 第二极小本身不保证长寿命；配对、形状混合、γ衰变/转换和裂变通道可能改变结论 |
| 极低跃迁能/原子环境 | 很低Eγ及电子通道改变总衰变率 | 实际核能隙、多极性和可用电子态/光场必须匹配 | 229Th不同电荷/晶体环境寿命不能直接互换；不应硬套高K或seniority机制 |

机制可叠加，并不是互斥四分类。原页将137Ba的低能E2例子放进“必须ΔI≥3”的定义，
在逻辑上即不一致；本页撤回该门槛，不据此重新指定137Ba组态。

## Synthesis

### seniority相消及精确检验

对单一j轨道中的相同核子、纯seniority v态，偶秩L>0的一体算符有
\[
\langle j^n vJ_f\Vert T^{(L)}\Vert j^n vJ_i\rangle
=\frac{\Omega-n}{\Omega-v}
\langle j^v vJ_f\Vert T^{(L)}\Vert j^v vJ_i\rangle,
\qquad \Omega=\frac{2j+1}{2}.
\]
在这一适用域且分母非零时，n=Ω的同v E2矩阵元相消。
这是矩阵元的有符号关系；B值是其平方。奇秩算符、Δv≠0、一般多轨道空间
或所有真实异能态不服从这条相同公式。
原书入口：[[book-jain-nuclear-isomers]] Ch.3，印刷pp.41–43、Eqs.(3.15),(3.20–3.21)。

本轮用12个磁子态的真实费米Slater基、旋转标量配对Hamiltonian与一体E2算符，
计算j=11/2、v=2的10→8跃迁。没有把解析比例当作数值输入。
纯配对极限中同v的10与8态简并，本计算检验矩阵元，不提供非零γ能量或异能态寿命。

| n | 2 | 4 | 6 | 8 | 10 |
|---|---:|---:|---:|---:|---:|
| 纯配对B(E2;n)/B(E2;2) | 1 | 0.25 | 数值舍入内为0 | 0.25 | 1 |

加入确定性的J=2对关联后，n=4/8强度改变，而被跟踪n=6态之间仍相消。
计算显式检查了其共同粒子—空穴signature及E2在该变换下的奇性。
因此修正原先过宽的直觉：**非配对混合并不必然解除半满壳相消**，
要检查被混合态和Hamiltonian真正保留/破坏的对称性。
结果是无经验拟合的有限模型，不能给真实核的剩余B(E2)、半衰期或有效电荷。

跨区迁移应先做壳计数：130Sn相对N=82有两中子空穴，
210Po相对Z=82有两个质子；它们不是单h11/2六空穴半满壳的通用例子。
“具有seniority相关异能态”与“恰好因精确半满壳相消”必须分开。
真实Sn还涉及d3/2、s1/2等多轨道与有效算符，不能从质量数直接读出n。

还有一个纯代数的跨区限制：n−v必须为偶数。对g9/2，Ω=5，
精确半满n=5不可能属于v=2偶粒子链；其n=4/6在单j理想极限只能到
相对n=2强度1/9的近半满抑制。对h11/2，Ω=6则允许n=6、v=2的精确节点。
因此相同“seniority异能态”名称下，是否存在该态对的精确零点也会随壳简并度改变；
这是模型适用性的推论，不是任何指定真实核的强度预报。

## Counter-evidence

### 第二轮：真正解除节点与真实核的反向约束

[[seniority-node-three-body-breaking-round2-20261107]]构造归一的J=27/2三费米子通道，
V3=ΣB†B为纯三体、旋转不变且破坏中壳粒子—空穴对称性。
所跟踪10→8的B在小λ以λ²起始，而全部单j标量两体通道满足
C_n†P_J(2Ω−n)C_n−P_J(n)=(2J+1)(1−n/Ω)I，在n=Ω处保PH。
这限定了该单轨道、同种核子模型中的体数结论，不等于真实核必须以基本3N解除节点。

若纯配对基线的两态简并，三体扰动又使Eγ∝λ，则无量纲Eγ⁵B代理以λ⁷起始。
若先由保PH两体项形成有限能隙，B仍可被保护而为0；随后三体解除时代理则以λ²起始。
矩阵元与相空间必须同时检查，两种幂都不提供物理单位的寿命。

真实核对照见[[sn136-seniority-anomaly-and-three-body-identifiability-round2-20261107]]：
136Sn相对132Sn的f7/2四粒子是理想中壳计数，但实际多轨道两体计算可给
B(E2)从14.5到22.0e²fm⁴、与24(4)的实验值相容。因此非零B不是显式三体的唯一证据；
需联合其它末态、算符及谱来比较解释。

### K异能态与三轴动力学

用同一支路的辐射时间定义
\[
F_W=\frac{T_{\gamma,\rm partial}}{T_W},\quad
f_\nu=F_W^{1/\nu},\quad\nu=|\Delta K|-L>0.
\]
若btotal含光子和转换电子，Tγ,partial=Ttotal(1+α)/btotal；
若给的是辐射分支概率，不再乘一次ICC。
混合多极性要分别提取相应分强度，不能把总寿命代入所有支路。
见[[reduced-hindrance-factor]]的约定。

Hayes2005的安全能量库仑激发研究，说明低K带可随旋转顺排混入高K成分，
高K带自身在同一自旋区仍较纯（PDF pp.279–281）。
所以“混合发生在异能态自身”“异常低fν必定是静态三轴”都不是普适结论。

192Os提供另一个约束：10−态可以长寿命而具有约5–11的支路fν，
12+/20+的低能跃迁与顺排又给不同寿命机制。
同一核素的不同组态不能共用一个形状标签
（[[dracoulis-2013-192os-isomers-gamma-soft]]，Table1、Figs.3–5）。
2012年191/193Ir作者提出spin trapping与三轴组态共存，
本轮该篇仅取得首页，解释和数值细节保留访问边界。
第二轮[[os192-branch-rates-and-shape-identifiability-round2-20261107]]进一步给出：
两E2的约220倍强度比对应光子率比0.217、含原表转换系数的总跃迁率比0.806，
并非220倍的衰变流。共同τ可消去，未知协方差、暂定指定和表文差异仍须保存。

## Evidence Matrix

### 六区比较合同

| 核区 | 值得联结的物理 | 迁移时必须保留的限制 |
|---|---|---|
| A≈60 | 跨壳排列、形状共存与能谱瓶颈；高自旋组态可能不同于低能价空间 | pf壳多轨道混合不能直接套h11/2单j定理；需要具体能谱和跃迁 |
| A≈80 | g9/2组态、三轴/八极关联及低能连接；时间窗可分离不同feeding | 低能未见线、转换和不同带号可能改变网络；手征与寿命并非一一对应 |
| A≈100 | 93mMo能谱陷阱与触发跃迁；105Pd集体取向运动及核芯响应 | NEEC还需原子空穴和电子能谱；核结构相似不能直接迁移百分比耗散率 |
| A≈130 | Sn邻区seniority与壳演化、Ba/Ce多准粒子态和软核耦合 | 明确粒子/空穴、有效价空间及同v/异v；不能以区域平均γ或固定fν决定异能态 |
| A≈160及稀土延伸 | 高K、阻塞配对、Coriolis和强形变/三轴激发 | 稀土高K实例不能反推整个核区必轴对称；同态多分支和末态混合是关键 |
| A≈190 | Os/Ir组态依赖形状、顺排与高多极性；Tl多准粒子候选 | 同核不同形状、强度重分配与γ软性可以共存；寿命长不是静态γ的反证 |

超重核与229Th等在六区之外，仍是本任务开放探索的重要比较对象；
六区是坐标，不是知识收录边界。

## 5. 弱衰变：Ikeda恒等式与gA淬灭分开

令O−=Σσ τ−作用为n→p，O+为逆过程，S±是**裸自旋—同位旋算符**
对完整末态集合的总强度。闭合与对易关系给
\[
S_- -S_+=\langle i|[O_+,O_-]|i\rangle=3(N-Z).
\]
精确约定和推导入口是[[book-suhonen-from-nucleons-to-nucleus]]
印刷pp.541–545，Eqs.(17.63–17.74)。
截断空间缺失自旋—轨道伙伴、有限实验能窗、组态关联和反应提取假设都会影响
实际获得的强度，不能把实验缺失百分比直接等同自由核子gA的改变。

若在特定模型中定义Oeff=qO，那么这个**有效算符**的总差为q²3(N−Z)，
不意味着原来的裸算符恒等式失效。两体流与多体关联等可能共同贡献，
需要相同Hamiltonian、算符和模型空间的比较；不存在对所有核素、跃迁秩和
β衰变/双β过程通用的0.5–0.6强度或gA,eff=1.0定律。
高自旋异能态的β衰变还可能属于禁戒跃迁，不能一律用allowed GT描述。

## 6. 从实验室异能态到星体中的独立物种

能级寿命长不自动意味着天体反应网络中要保留独立异能态。
经中间能级的光激发/退激、电子环境、核反应与温度演化决定是否热化。
只有在交换足够快时，才可用
\[
\frac{n_m}{n_g}=\frac{2J_m+1}{2J_g+1}\exp[-(E_m-E_g)/(k_BT)]
\]
及热平均衰变率；否则要解耦合态布居网络，比较交换、β/EC、俘获和环境变化时标。
不能只从一个能隙给出确定的冻结温度或r过程丰度变化。
综述框架见[[isomer-review-learning-and-transfer-20261107]]；
132Sn周围的直接论文及质量不确定度研究见
[[isomer-shell-evolution-astrophysics-and-superheavy-transfer-20261107]]。

129Pd的中子衰变异能态在Yuan2016中是预测；是否在2026已得到验证需要额外检索。
其可行性依赖Sn、母/子态能量、角动量/宇称和离心势垒；
质量不确定度可以改变通道，但“Sn增加200 keV必然关闭一个约380 keV的Q值”并不成立。
即使中子发射能量允许，也需与γ分支和产生布居比较。

## Model Dependence

### 超重核稳定性、截面与布居

完全熔合蒸发剩余核的一种阶段分解为
\[
\sigma_{\rm ER}(E_{\rm cm})\simeq
\frac{\pi\hbar^2}{2\mu E_{\rm cm}}
\sum_J(2J+1)T_J P_{\rm CN}(E,J)W_{\rm ER}(E^*,J).
\]
T控制接触/俘获，PCN描述相对于准裂变的复合核形成，WER描述到指定剩余核的级联。
这是带输入和阶段分离假设的反应框架，不是三个无参数常数。
[[zagrebaev-2001-superheavy-synthesis-survival]]原文Eq.(1)明确给出近似性质。

对指定xn支路，较一般的写法是对级联能量/自旋路径取平均：
\[
W_{xn}=\left\langle\prod_{k=1}^{x}
\frac{\Gamma_{n,k}}{\Gamma_{{\rm tot},k}}
P_{\rm terminal}\right\rangle_{\rm cascade},\qquad
\Gamma_{\rm tot}=\Gamma_n+\Gamma_f+\Gamma_\gamma+\Gamma_p+\Gamma_\alpha+\cdots .
\]
只在其它宽度可忽略时用Γn/(Γn+Γf)，再在Γn≪Γf时才近似Γn/Γf。
原文Eq.(10–11)还有中子能量积分和终末γ冷却。
壳修正、温度、配对、惯量、裂变路径和角动量均带模型不确定度。
原页“所有宏观势垒为零”、固定Γf/Γn与固定生存率数值没有成立的普适性；
原source中不存在的Fig.12/Table1 locator已隔离撤回。

Xu2004的高自旋稳定性计算和Herzberg2006的254No异能态谱学属于不同证据层。
冷高K组态可能改变裂变势垒或重叠，不能由此直接计算热复合核ER截面；
反过来，也不能一概断言高K对所有生产路线绝无作用。
要预测异能态专属截面，还需入口自旋分布、级联feeding、K/组态演化与探测时间窗。
转移与熔合路线可比较，但没有反应动力学/产额模型时不设任意“增益倍数”门槛。

## 8. 耗散与核钟：结构相似不等于应用率可迁移

93mMo的2018 NEEC报告、2021评论/答复与2022隔离束实验应保留为证据演化链。
2022原文以低γ背景条件给P≈2×10−5上限，其构造包含效率、时间门、死时间与ICC，
不是“268 keV窗口零计数”；也没有给本任务可照搬的99%覆盖概率认证。
它对先前百分比效应提出强反证，但不排除预测远低于灵敏度的NEEC过程。
这条线的可复用研究方法是把产生、输运、停止和探测分离并设置背景/伴随线控制，
而不是将一个核的耗散比例迁移到另一个核。

核钟方面，229Th与45Sc的能隙、多极性、电子/晶体环境和耦合方式不同。
小核能隙、辐射衰变可见、激光激发、与原子钟比频、闭环锁定及不确定度预算
是不同的实验里程碑，不能由“发现异能态”一步跳到“可工作的高精度钟”。
详见[[nuclear-clock-isomer-learning-and-transfer-20261107]]；最新结论按实际取得的2026原件定位。

## Limitations and Missing Evidence

### 自审与开放问题

P0：保留原件、哈希和实际范围；未把模型/摘要或重复版本计为实验复测。
P1：真实多轨道seniority破缺、K混合的两端、绝对弱衰变算符、热化网络与
超重核级联输入仍需逐问题核验。已完成的单j模型验证不填补这些数据缺口。
下一步优先选择能区分机制的多观测量对象，而不是再做一遍统一现象分类。

## Sources

- [[book-jain-nuclear-isomers]]
- [[paper-walker-dracoulis-1999-energy-traps]]
- [[paper-dracoulis-2016-metastable-states-heavy-nuclei]]
- [[paper-walker-podolyak-2020-100-years-isomers]]
- [[hayes-2005-k-conservation-178hf]]
- [[dracoulis-2013-192os-isomers-gamma-soft]]
- [[book-suhonen-from-nucleons-to-nucleus]]
- [[zagrebaev-2001-superheavy-synthesis-survival]]
