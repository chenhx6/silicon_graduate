---
type: method
title: γ 射线角关联分析
aliases: [angular correlation, gamma-ray angular correlation, particle-gamma angular correlation, gamma-gamma angular correlation]
created: 2026-07-09
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
method_type: gamma-ray-angular-correlation
tags: [multipolarity, alignment, attenuation, deorientation, pado-support]
---

# γ 射线角关联分析（Gamma-Ray Angular Correlation）

## Purpose

角关联分析（angular correlation）利用先前反应、粒子或 γ 辐射方向与后续 γ 射线方向之间的相关性，约束 nuclear alignment、transition multipolarity、mixing ratio 或退取向效应。

## Inputs and Assumptions

- Coincident particle-gamma or gamma-gamma directions with calibrated detector geometry.
- Known or hypothesized spin sequence, multipolarity and mixing-ratio values.
- A controlled description of initial alignment/orientation and any deorientation corrections.
- Separation of detector finite-solid-angle effects from nuclear alignment/deorientation effects.

## Source-Level Foundation

[[radeck-2012-deorientation-lifetime-98ru-rdds]] 在 inverse Coulomb excitation + RDDS 实验中拟合 distance-dependent particle-γ angular correlations，用未扰动的 Coulomb-excitation angular correlation 与实验相关函数之比提取 time-dependent attenuation factor `Gk(d)`。

## Boundary

- angular correlation 与 [[angular-distribution]] 都使用角度依赖强度，但前者保留两个事件或一个粒子-γ 方向之间的相关性；不能与普通 single-γ angular distribution 静默合并。
- [[kramer-flecken-1989-use-dco-ratios]] 展示了 DCO 是从 gamma-gamma angular correlation 压缩出来的一个 gate-与几何依赖比值，而不是脱离原始 correlation formalism 的普适常数。
- Radeck 2012 的 particle-γ angular correlation correction 属于 inverse Coulomb excitation / RDDS 语境，不是 fusion-evaporation P-ADO 的直接 `σ/I` 来源。
- detector finite-solid-angle factor `Qk` 与 nuclear alignment/deorientation factor `Gk` 是不同系统项。

## Relation to P-ADO

角关联可作为 alignment/deorientation 参数的独立约束或校正来源。它支持 P-ADO 的方法论动机：`δ` 提取不应把 alignment 或 attenuation response 当作无不确定度常数。

## What It Can Establish

Angular correlations can constrain spin sequence, multipolarity, mixing ratio, alignment and time-dependent deorientation when the coincidence geometry and reference response are controlled.

## What It Cannot Establish Alone

Angular correlations do not by themselves define a universal side-feeding Gaussian width or `sigma/I` prior. Their interpretation still depends on reaction mechanism, feeding history, detector response and model assumptions.

## 条件γγ响应：各向同性marginal仍可有角关联

Day14从shared-POL的common-selection边界回到完整符合响应，并接入无学分Day15 ADO预习。直接方法依据是 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-3：printed p.326 / PDF p.21，Eq.3.71–3.73将第一γ所准备的中间态布居张量与第二γ的辐射系数相乘；初态随机布居、确定宇称、不观测circular polarization是该式的条件。两个各向同性单γ marginals不意味着joint direction probability可分离。

### 从振幅到条件态的自设控制

只取无退取向的自设 `0→L→0` 两条pure electric跃迁，`L∈{1,2}`为photon rank。spin-zero endpoints宇称相同，中间态相对宇称为 `(-1)^L`；没有赋给任何实际核素。令 `d=2L+1`、`q1,q2=±1` 为photon helicities，`M` 为中间核态投影，`D`为photon方向旋转矩阵。两步CG和方向投影给

\[
S_{q_1q_2}(\hat n_1,\hat n_2)
=\sum_{M=-L}^{L}\frac{(-1)^{L-M}}{\sqrt{d}}
D^{L*}_{-M,q_1}(\hat n_1)D^{L*}_{M,q_2}(\hat n_2),\qquad
K_L=\frac{d^2}{4}\sum_{q_1q_2}|S_{q_1q_2}|^2.
\]

每条single-γ分布归一为1。第一γ方向确定、helicity未测时，中间态为 `ρ=A1 A1†/tr(A1 A1†)`；有限接受度gate是对这些未归一矩阵按响应加权再归一。完整均匀full-Ω积分恢复 `I/d`，有限门通常保留条件alignment/coherence。若gate位于后一步，使用joint effect/后选择计算，不能将选择解释为逆时间的核布居因果过程。

独立spin-matrix/Wigner振幅与Legendre路线核验，设 `x=hat n1·hat n2`：

\[
K_1(x)=\tfrac34(1+x^2)=1+\tfrac12P_2(x),\qquad
K_2(x)=\tfrac54(1-3x^2+4x^4)
=1+\tfrac5{14}P_2(x)+\tfrac87P_4(x).
\]

这是本任务的理论控制值，未写成Rose–Brink的实验数据。K对两方向对称、全角平均为1、非负；spin-density/effect计算也得到同一joint kernel。单γ的 `ω1=ω2=1` 仍不能把这些K替换成1。

### 组效率修正与full pair response

[[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-6/9的Eq2按单γ `ω1(θi)ω2(θj)` 和排除self-detector写response。一般符合净计数应先用已声明的joint kernel：

\[
I_g=F\sum_{i\in g}\sum_{j\ne i}
\varepsilon_i(\gamma_t)\varepsilon_j(\gamma_g)
\,K(\hat n_i,\hat n_j)\,G_{ij},
\]

其中 `Gij` 还可包含实际gate、时间/事件选择和pair acceptance。原Eq4的组效率/self-exclusion修正不自动包含任意K；定义上的 `f=R/intrinsic ratio` 可以吸收全部修正，却不能据此认证Eq4是任意级联的full response。这限制公式迁移，不否定Zheng原阵列已有参考线验证。

自设 `32°/58°/90°` 各4台、方位角0/90/180/270°、各组gate总效率均.04、target组总效率.04/.06/.05，explicit pair求和并排除i=j。singleγ均isotropic，分离组公式给R=1；pure E1 toy的full R=1，pure E2 toy的full R=.729470。前者是K2被该采样平衡，不能用其成功保证含K4目标也正确；这不是145Tb或JUROGAM的实际几何重放。

另取与target detectors不重叠的90°均匀方位ring gate，完全没有self-exclusion。32°/90°的conditional ratios仍为pure E1 `.760271`、pure E2 `.697063`，而singleγ分离式均给1。此例隔离出angular correlation，不把仪器自符合限制误当成全部物理相关。

### 极角、方位角和finite acceptance

仅让等权三极角的 `ΣP2/ΣP4=0` 不保证球面response张量全为零：每圈4个等距方位留下 `q=±4` harmonic。即使极角用精确 `31.7175°/58.2825°/90°`，本E2 toy仍随target φ变化；每圈8个等距方位、同样等权三极角可对本K2/K4 kernel精确消去这些方向项。实际效率、遮挡、门控权重、higher ranks和oriented初态需要重新检查，未当作原作者阵列设计意图。

若两探测器接受度是各自轴对称、均匀圆锥，半角为α、β，卷积给每个Legendre项乘 `Qk(α)Qk(β)`，其中

\[
Q_k(\alpha)=\frac{1}{1-\cos\alpha}\int_{\cos\alpha}^{1}P_k(u)\,du.
\]

独立cone quadrature与此式一致。在自设20°/35°半角和固定两中心方向，E2 point K=.594119变为finite-cone平均 `.940478`；finite response不只是一项总效率重标。`Qk` 是角接受度衰减，不能与核alignment/deorientation或Compton `Q_sens`混用。

复算：[day14_conditional_angular_response.py](../../system/scripts/day14_conditional_angular_response.py)，结果在 `outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-angular-response.json`。35项独立amplitude/Legendre、ρ/effect、积分、pair-exclusion、azimuth和finite-cone核验通过。知识页保存公式、输入、结果和限制，不将outputs用作唯一可复用副本。

### 接回Day14的必要观测

同名energy gate不保证各target-detector使用同一个gate effect，因为same-detector veto、pair/time cut或Compton选取可能改变 `Gij`。[[linear-polarization-asymmetry]]的pureE2 point outer set仍有其明确条件；本toy没有拟合shared R/A或解除393/394的顺序、宇称和multipolarity边界。应先取得真实逐pair response和matched-gate净计数，再核conditional population是否可共用。

最高信息检验是同一target/参考线的换门、方位分组和finite-response前向预测，同时保留shared-event covariance。一个低rank参考通过不能认证所有rank/mixing/spin的response；没有实测输入时不能报告实验显著性或把此反例升为新的核结构事实。

## 双γ排序的交换对称性

[[herzan-2015-193bi-spectroscopy]] HE15-9提供实际未定顺序的393.4/394.0-keV例子。下面只检验排序信息的条件，不把暂定的两个(E2)或Jπ提升为已确定输入。[[rose-brink-1967-phase-defined-angular-distributions]] RB67-3的Eq3.73以随机初态为条件；RB67-11的CG/helicity振幅是任务重构的依据。

### 随机初态与更强的maximal-coupling条件

静态级联的随机初态没有外部取向轴，helicity-summed joint intensity只能依赖 `hat n1·hat n2`，所以交换两方向仍相同。若两个排序假设只交换同rank纯跃迁的能量标签、保持spin sequence及共同response，这种γγ强度数据不给先后信息。这里不能把有取向初态默认为随机。

有一个更强的、无需随机初态的条件。取两个同rank、同E/M类型的纯stretched downward跃迁，`Ji=Jm+L`、`Jm=Jf+L`、`L≥1`。在一致的CG相位约定下，设 `Mi=Mf+μ1+μ2`、`Mm=Mf+μ2`，两个maximal-coupling系数之积为

\[
\begin{aligned}
&\langle J_mM_m,L\mu_1|J_iM_i\rangle
\langle J_fM_f,L\mu_2|J_mM_m\rangle\\
&=\sqrt{\frac{\binom{2J_f}{J_f+M_f}
\binom{2L}{L+\mu_1}\binom{2L}{L+\mu_2}}
{\binom{2J_i}{J_i+M_i}}}.
\end{aligned}
\]

中间态binomial约掉，剩余表达式对 `μ1↔μ2` 对称。因此完整两photon angular/helicity振幅满足 `S(q1,n1;q2,n2)=S(q2,n2;q1,n1)`；任意同一initialρ，包括有alignment或coherence的ρ，都保留此性质。若两个假设仅交换能量标签，任何共同的角度/偏振measurement与finite acceptance不能从相同的angular photon state创造顺序信息。这个结论针对declared angular model；不同时间、能量强度/寿命、旁路、intermediate interactions或更高/混合multipoles需另建模型。

### 独立数值与非stretched失败控制

自设pure E2 `19/2→15/2→11/2`，一条路线直接用maximal binomial，另一条路线在product-spin空间构造total `J²`、取highest M eigenvector并逐次lower，两个CG表一致。四个自设方向的16组pair中，full-amplitude exchange最大差 `4.48×10⁻16`；random、chosen Gaussian `σ/J=.3` 与chosen coherent initial state的intensity差均在浮点误差内。不能把这些数值当成实验精度。

改为自设 `19/2→17/2→13/2`、仍两条pure E2，第一条非stretched，maximal-coupling证明不再适用。random initial的intensity交换仍相同；chosen Gaussian initial在自设方位/点角下，两个排序的normalized point intensity为 `.879316/1.297627`。这是有取向非stretched例子的可能信息，不是对193Bi的预测或实测significance。

复算入口为 [day14_cascade_order_identifiability.py](../../system/scripts/day14_cascade_order_identifiability.py)，结果为 `outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/cascade-order-identifiability.json`。51项CG normalization、独立maximal/ladder、ρ/feeding与exchange/非stretched控制通过；没有将算法检查数视为独立实验。

### Feeding不是每层重新指定同一个Gaussian

第一γ未观测时，中间态的实际model population由channel给出 `ρm=Tr_ph(V1ρiV1†)`。在chosen diagonal initial下，`wm(Mm)=ΣMi,μ1 wi(Mi)|CG1|²`；random initial给random middle，但chosen Gaussian通常不等于中间态同一个 `σ/J` 的Gaussian。

上述两条toy链的exact feeding middle population与另行假设 `σ/J=.3` 的middle Gaussian，L1距离分别 `.076428/.143581`。这些是已声明toy下的概率距离，不是数据残差或真实feeding拟合。无条件每层重置Gaussian增加一个未经观测约束的输入，可能改变reference→target迁移。

### 判定与下一观测

本任务决定 `revises` “有取向便能用更精细角数据判同rank双线先后”的过宽预期。应先检验是否落在上述交换对称性；若是，优先独立中间态分支/能级、可分辨的时间信息或能证明该角模型条件失效的观测。HE15-9的未知order、shared R/A以及所有review flags保留；这项条件证明不判断真实双线是否满足pure/stretched、共同response或无中间演化条件。

## Sources

[[konigshofen-2001-mixing-ratios-130ba]] demonstrates a three-angle low-spin application: efficiency-corrected `W(180°)/W(90°)` and `W(55°)/W(90°)` ratios can yield a unique `δ` for 18 `130Ba` transitions when the spin/parity and pure-E2 reference assumptions hold. The unresolved `4+_3→3+_1` row remains an explicit multi-solution boundary.

[[falkoff-1948-polarization-correlation]] is a historical successive-γ polarization precursor: its `A` coefficient complements, but does not replace, directional-correlation coefficients and requires phase-convention mapping.

[[krane-1973-directional-correlations-oriented-states]] is the generalized DCO foundation, separating orientation parameters, radiation coefficients, finite geometry and multipole conventions from later compressed ratios.

- [[radeck-2012-deorientation-lifetime-98ru-rdds]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- [[kramer-flecken-1989-use-dco-ratios]]
- [[bargholtz-1987-high-spin-gamma-gamma-directional-correlations]]
- [[rose-brink-1967-phase-defined-angular-distributions]] RB67-3/11：方向相关的布居/响应与photon amplitudes；Day14 toy是任务重构。
- [[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-6/9：ADO组response的原定义和迁移边界。
- [[smith-2019-griffin-angular-correlation-analysis]] SG19-3/5/6/8/12：独立GRIFFIN实验的event-mixing归一、有限几何模板、校准Cov及新initial alignment迁移条件。

[[starosta-1999-pdco-experimental-test]] is a direct high-spin example of the compressed-observable boundary: `R_DCO` constrains the alignment/multipolarity space, while CLOVER polarization adds electric/magnetic sensitivity; the combined fit still leaves a 490-keV E2/M1-E2 branch under the paper's assumptions.

[[james-twin-butler-1974-angular-correlation-statistics]] adds the statistical gate: alignment/model variance enters the design matrix, effective degrees of freedom are `n−rank`, and `arctan δ` confidence contours must retain nonlinear/multibranch topology.


## 67Ga真实序列的门条件设计与single-marginal盲区

[[nndc-2005-67ga-selected-level-gamma-records]] N67-7报告958(E2)/554(E1)同DCO1.45(7)，却没有exactgates/angles/normalizer；N67-9记录primary未取得。以下从[[rose-brink-1967-phase-defined-angular-distributions]] RB67-3/11的CG/helicity/joint response构造**声明设计**，不是NORDBALL算法或原counts拟合。

### 固定设计与失败预测

冻结后固定pointθA40°/θB90°、φ0、两photon polarization未测、idealmatched-efficiency correction，定义R=W12(A,B)/W12(B,A)。状态取symmetric-diagonal、各|M|pair概率q≥0、Σq=1，purelimit只作模型。选择reallevelpaths的两条reference假设：

| 模型 | chosen starting→middle→final spin | target / reference假设 | allpositiveP的R区间 |
| --- | --- | --- | --- |
| A | 13/2→9/2→7/2 | E2 958 / E1 871，下方门 | [.413175911,2.551584550] |
| B | 9/2→9/2→5/2 | E1 554 / E2 1160，下方门 | [.811324495,1.103410944] |

Source没有说它用了这些gates。最初预计两hyp都可能R1.45，被固定模型B结果revises；角度没有调到强求相容。A有严格正population witness，B的每个pure-pair都a_j−1.45b_j<0，没有正q可给该比；它只排除这套**特定**nominalpure/point/reference/normalization模型，不能排除真实E1或source。首scratch probe曾漏deg2rad且numpybool JSON失败，未采用其数值，已在正式单位/归一检查前修正并保存边界。

一般R=(a·q)/(b·q)，本设计所有b_j>0，于是R=Σ[b_jq_j/(b·q)](a_j/b_j)，极值由pure-pairvertices给出。若另加unknowncommon scalar f、Rreported=fRideal，两个models的f允许区间相交为[1.314106959,1.787201064]。f1.45配两initialisotropic能给同reported1.45，只是未识别calibration的反例；从同targetratio得f不是独立测量，不能据此宣称算出了source f。真实array响应还可能energy/gate-dependent、nonseparable或有限接受度。

### 完全相同的单γ校准仍不确定joint gate比

在A中再**自选**精确calibration α2=α4=0。PureE2单γ只看rank≤4；γγ E2+E1 joint可读更高initialrank。用Charnes–Cooper变换y=q/(b·q)，在b·y=1、T2·y=T4·y=0、y≥0下min/max a·y。LP的primal/dual/reduced-cost残差小于1e−10，给数值核验的完整区间[.980174767,1.025136082]，不是interval-arithmetic证书或experimentalCI。

对应|M|按1/2、3/2、…、13/2排列：

| population | exact pair probabilities q | R |
| --- | --- | --- |
| min | (0,0,13/27,13/45,0,0,31/135) | .980174767 |
| max | (11/25,0,0,0,2/25,12/25,0) | 1.025136082 |

两组归一及T2/T4矩为零已按rational vertices精确核验。各混入5%uniformq后成为严格positive density，R仍为.981173438与1.023891199。更强的检查是：**两组的完整第一photon mode density都I5/5，第二都I3/3**，所以任何各自单photon测量都相同，joint directional gate ratio却不同。这不是只有几角处相似，也不是全initialstateisotropic；高阶initial信息在joint response中可见。

该结果补充[[magnetic-substate-population]]/RB67-26的referenceblindness：这次不需目标里有higher photon multipoles，普通E2+E1的joint analyzer就可能超出single-E2 calibration的population rank。它不否定properlyconditioned response模型；它阻止把两个singlemarginal或两个α输入自动等同完整γγ预测。

### target/reference互换与最小输入

若两个ratio真由**同一corrected pair cells/同events/同selection**互换target与reference，则R_T,R_G互为倒数，乘积1。两literal1.45乘积2.1025，不能被当作该假设下同一pair的两份独立约束；source实际可能是不同gate sums、normalizer或response，缺metadata时不判作者错。引用同对象也不认证同count ledger。

最低recoverable response记录需逐target给reference/全gate列表、level/line identity、pair角度与接受度、逐能量efficiency及background、normalization、event-ID重叠和joint covariance；新observable应给独立kernelrow，重复同joint ratio的变形不多一份信息。42项checks覆盖CG/isometry/binomial、units/axialrotation、physicalfeeding、sphere积分→singlemarginal、全部positivepopulation范围、LPwitness/infeasiblecase、scalar/readiness、互反及exactmoments/fullmarginal/strictPSD控制。代码[day14_dco67_gate_design.py](../../system/scripts/day14_dco67_gate_design.py)，完整kernels/duals/witnesses在本run dco67-gate-design.json。

决定revises预设两个模型都能fit1.45，supports先验证gate/normalization及population可观测空间，limits singleγ校准和裸ratio阈值用于联合纲图赋值；没有sourcegeometry、实测ρ/新multipolarity、实验显著性或L4重放。Day14继续，Day15仍partial无学分。

## 事件混合：效率归一之后仍有有限响应

[[smith-2019-griffin-angular-correlation-analysis]]实际读的是2018arXiv v1、2019期刊metadata另核。其SG19-5（PDF6 Fig2）在同一60Ni数据上给出与full模拟比较的χ²/NDF从7.96（pair数归一）、2.34（再加single-crystal效率）到1.02（event mixing）；三个处理共享事件，不能计三份独立实验。SG19-6（PDF7 Fig3）的已知66Zn0→2→0纯E2控制进一步显示：event-mixed数据仍不等于未卷积的物理correlation，需要匹配有限几何/材料响应。

沿SG19-3的Eq6–14，若同angle bin内pair的N_jk相同、混合参考Y=1、两能量/效率时间权重与cuts匹配，则

\[
\frac{w_i}{y_i}=\frac{\int N_i(\theta)W(\theta)d\theta}{\int N_i(\theta)d\theta}.
\]

还需W在接受区近常数，或N对称且W近线性，才等于中心角W；不能把分母归一当成完整去卷积。这里θ是两γ的opening angle，Zheng ADO的θ是相对束轴的极角，两者的核布居/响应输入不同。SG19-4给该研究mixing窗2–200μs、prompt<300ns，以及寿命≪mix间隔≪效率变化尺度；这些数不自动成为其它DAQ的参数。

SG19-7的正输入Z0/Z2/Z4模板可线性合成物理correlation，允许负线性系数；它们不是三类事件的probability mixture。完整模板保留bin响应；SG19-8的c2=beta a2、c4=gamma a4是进一步的代数近似，beta/gamma不等于核alignment、偏振Q(E)或ADO f。实际共享模拟/校准时，应检验Eq27省略的cross项是否为零。

原文各方法重用同一套数据（SG19-10），且若干cascade仍有多个Ji/δ候选（SG19-9）；更多opening-angle bins不保证spin唯一。新trigger、initial alignment、addback或angle regrouping先验验算条件见SG19-12，不能直接迁移GRIFFIN11cm的beta/gamma。v1 Table5精度、Table4/8的Gd a4符号与简化Q范围等差别保留SG19-13/14/15；VoR未取得，不用这些歧义数值重造实验Σ或新显著性。

下一项高信息问题是：同一interaction与多个partners配对时，mixed histogram的方差和prompt/mixed cross covariance如何随partner数变化？SG19-4只提供方法描述，没有给实际event-ID/完整Σ。需要以physical-event为单位保存重用关系或作block重采样，而非默认每个mixed pair都是新的独立衰变；本段未声称已求出GRIFFIN实际Cov。

Day15后续[[event-mixing-statistics]]已在明示的固定N、binary tags、逐row无放回算法下推导精确矩：增加K只消去配对噪声，一阶投影非退化时仍留1/N事件方差；平衡控制没有该主导项。独立small-N有理枚举与MC验证，ratio还需prompt/mixed cross Cov；均不是SG19实测Σ。SG19-16/17另把公开固定代码归档和NDA输入缺口分开，未将公开zip冒称full GEANT4重放。

## DCO双解与PDCO模式的条件选择

[[droste-1996-pdco-formalism]] DR96-4/5/6的5→4→2模型现由[[dco-pdco-ambiguity-worksheet]]独立复算：同R*的M1/E2两根、pureE1替代及第一/第二photon条件P分开保存；source近似−70°例不与本任务精确同R根混成一个点。一般选择更大预测分离的DIR-POL前，还要确认当前候选已排除同P2的pureM1/E1歧义，并取得matched Q/counts/Cov；没有普适的单observable唯一赋值。

该计算还以source广义F核对实现的相对multipole基底：pure limits可全部通过而混合干涉项坐标仍错；必须显式转换参数/系数。完整4π积分下游光子的singles边缘，与trace上游后带U的daughter density是不同运算，finite gate不能无条件替代它们。此为条件模型/文献复核，不认证其它source的delta符号或实际array response。

## 高自旋factorization的使用边界

[[bargholtz-1987-high-spin-gamma-gamma-directional-correlations]] BT87-4/5从exact generalized F在fixed小DeltaI/L、I→∞的极限得到ordinary A的factorization。printed517 Eq12写成

\[
W_\infty(\Omega_1,\Omega_2)
=\int d\Omega_s\,P(\Omega_s)w_1(\hat n_1\cdot\hat s)w_2(\hat n_2\cdot\hat s),\quad
w_i(x)=\sum_{k=0,2,4}\sqrt{2k+1}A_{k,i}P_k(x).
\]

I→∞使低阶辐射不会明显改变spin-axis，是这个共同轴乘积图像的条件。作者printed518的finite-spin improvement把ordinary A和initial B换成exact Eq2/3/B1，**仍保留factorized joint**；它不等于exact generalized-coefficient Eq1。有限B的形式矩代入不能自动作为已经测得、处处为正的classical spin-axis probability。

### 对实际方法表的有界反向检验

为查[[kramer-flecken-1989-use-dco-ratios]] printed334 Table1的producer边界，本任务固定90°/38°/φ18°、声明的`p(M)∝exp(−M²/(2(.3I)²))`，不调角度/σ或印值。无限spin采用相同固定width/I的连续cos-axis Gaussian极限；finite改进用exact ordinary F/B。十行印值的.01半单位舍入诊断分别通过exact6行、infinite2行、finite-improvement1行。四项exact未复现行如下，所有数都是本任务模型值，不是新的实测表：

| spin sequence / ranks | KF89印值 | exact | infinite | finite improvement |
| --- | ---: | ---: | ---: | ---: |
| 10→8→7 / 2,2 | .66 | .637341 | .646143 | .652439 |
| 10→8→8 / 2,1 | 1.07 | 1.029280 | 1.097269 | 1.051464 |
| 9→8→7 / 1,2 | .92 | .970704 | .908312 | .940620 |
| 9→8→8 / 1,2 | 1.12 | 1.188657 | 1.149485 | 1.219007 |

因此“KF89用了这种近似，故差异已解释”的假设未通过。部分行偏差变小并不恢复十行共同producer；KF89 Ref6引用BT87也不能证明实际用了哪套式/width/response。

### 检查近似是否保全exact不变量

本页既有maximal-CG证明表明，同rank纯stretched两步在共同ρ/response、无中间作用的条件下有完整photon交换对称。对于10→8→6的pureE2/E2，上述exact与infinite模型都给R=1；finite improvement却给`R=1.013742515`。原因可以从乘积式看到：infinite A只依赖相同DeltaI/L，两条w相同；finite ordinary A取不同自旋，w1与w2一般不相同，交换两个方向后的乘积不必相等。ordinary系数更精确没有恢复所有joint结构。

这限制近似的使用，不声称原作者在其Fig2条件下的比较错误。完整Eq10 harmonic contraction与Eq12轴积分按两阶quadrature核验到约3e−15，source Table1的五个无限spin A2/A4在印刷精度内；但两代数路径仍共享CG/Wigner primitives，不是独立producer。代码[day16_bt87_factorization_audit.py](../../system/scripts/day16_bt87_factorization_audit.py)，冻结input和audit JSON位于本日run目录，十行与控制条件在JSON保留。

Fig2的I20、M0、theta2=45°/phi相同控制下，本任务13点采样的finite改进最大absolute W误差约.0030/.0095/.0090/.0354/.0230（依次五个pure路径），不能说连续角度的全局上界。在接近angular node处，infinite式可给0而exact为小非零，relative误差约100%仍可有很小absolute W差；不把不同误差分母混成对源文的反证。

真正要解释RDCO或反演δ时，还须检查分子/分母误差和`dR/dδ`：小的W误差可能被近零分母、近pure端点或fold放大。应在目标observable、真实自旋/布居/response上核近似和不变量，不能只引用“spin约20就很好”。本检查没有真实178W响应/计数/Σ，不改变核结构模式或作者δ支。

### Exact有限B不是任意正的经典轴分布

从BT87 AppendixB EqB1的exact tensor与独立quadrupole对角元可核，整数J≥1、M=0时

\[
\frac{B_2}{\sqrt5}=-\sqrt{\frac{J(J+1)}{(2J-1)(2J+3)}}<-\frac12.
\]

若把finite B直接按无限spin Eq15当作正的unit-axis概率的Legendre矩，就要求`⟨P2(cosθs)⟩<−1/2`；但P2在实单位球面上的最小值就是−1/2，不可能。J20/M0的任务核验仍给约−.500447，而非严格经典下界。这个有限J量子修正不否定positive核density；它限制把finite moment substitution解释成实测的正经典P(Ωs)。Eq10的形式替换和真正的classical probability必须分开，不能据此采样伪布居或认证全部joint响应。


## 130Ba的两个opening-angle比值：何时确实能消去单比双解

[[konigshofen-2001-mixing-ratios-130ba]] KO01-6–11提供与beam-oriented DCO不同的独立实验：130Laβ+/EC后的offbeam130Ba，47million doubleγ events，180°/90°/55°是两gamma的openingangles。Fig2实例是1003.3keV的3+_1→2+_1，再经pureE2至0+_1；作者按Rose–Brink报告deltaRB=−4.5(.4)。TableI共40条跃迁，18行finiteδ；483.5keV的4+_3→3+_1仍未解。不能以abstract的18unique扩写成全表都唯一。

### 先分开作者计算、实验比值和本任务复算

正文A2=−.0321、A4=−.0778称为**calculated**。本任务固定unorientedρ=I/7、3→2→0、point响应、M1/E2 target、E2 reference；仅按已核normalized相位桥用d_D96=−deltaRB=+4.5，不拟合σ/响应或改原数据。直接photon trace与generalizedF两路得到

\[
A_2(d)=\frac{-.07142857143+.78246079644d-.20408163265d^2}{1+d^2},\qquad
A_4(d)=-.08163265306\frac{d^2}{1+d^2}.
\]

两路系数差<9e−16；d4.5给A2−.03214156/A4−.07779112，与作者四小数按±.00005舍入相容。这个换号结果依赖具体operator/state/归一映射；没有以sourceFig2符号相似反推转换，也不是原作者response代码。

从作者印刷**计算系数**生成的形状witness为R180=.90193794、R55=1.04387756，未当作图中实验横线的精确测量。仅R180时，本point模型有d≈.004919和4.498979两根，即RB坐标−.004919/−4.498979；对应R55≈.9677404/1.0438668。第二个形状比在此条件下能区分单比候选。

用A4中央值反解abs(d)≈4.50547，而A2中央值又略偏，这来自把两个四小数calculated值误当完全精确的联合输入。按实际尾位舍入同时作preimage后，d4.5相容。该窄舍入区间不是实验delta精度或CI；sourcequotedδ误差.4和图中测量band不能被这套计算值替换。

### 两个形状参数为何有用，统计又为何仍需Σ

若W(θ)=1+A2P2+A4P4，Ri=W(θi)/W(90°)，则两比给线性方程

\[
[P_2(\theta_i)-R_iP_2(90^\circ)]A_2+
[P_4(\theta_i)-R_iP_4(90^\circ)]A_4=R_i-1.
\]

在本witness两行矩阵det≈−1.46798，能恢复两个normalized coefficients。固定该spin/puregate下A4先约束d²/(1+d²)，A2的非零interference再约束sign；只要这些系数/响应未失去rank，确有额外functional信息。其它spin路径、puregate不成立、geometry/混合变化时需重做检验，不能保证全局Jπ唯一。

R180和R55共享W90。一般`Σ_R=JΣ_WJᵀ`；即使三角净yield真独立，其crossCov也有`R180 R55 Var(W90)/W90²`。actualevent重叠、background、efficiency和finite-response仍可增加cross项。原文的两个ratio functions不是两次独立实验，也不自动统计独立；本run没有原Σ，未算新的显著性/置信区间。

新[day16_ko01_three_angle_audit.py](../../system/scripts/day16_ko01_three_angle_audit.py)与本日冻结input保存全部roots、two-ratio inversion、相位/纯极限/舍入控制及Cov Jacobian。[[dco-pdco-ambiguity-worksheet]]的W178和D96例与本例各有数据/模型身份，不能把ratio数值迁移到beamDCO阈值。

### 核结构推断仍要自己的companion

KO01的2+_3→2+_1有91.7%radiativeM1、4+_3→4+_1有97.8%，但作者明确要求absoluteM1才能给unambiguous mixedsymmetry赋值。finiteδ/relativeM1不是absoluteB(M1)、波函数结构或γsoft模式的直接证明。TableI的1918.3keV3-到4+/2+两δ还属M2/E1，不能把genericδ²份额全叫E2。这些是真实实验使用门，与同一理论曲线的多种处理不增加独立证据。

## IPAC校准、额外OR门与共享衰减

[[eldridge-2018-gamma-band-mixing-ratios]] EL18-5/6/8的252Cf数据将64pairanglebins合成9个effectivebins；额外多门要求至少一个成立，可含fissionpartner，不能把OR读成AND或无条件source。一般W=1+G2A2P2+G4A4P4的G应区别于geometry Q和反应Gaussianρ。

其G2以pure4→2→0的A2ratio校准，再用同一phi/g模型给G4并按组平均；G4不是新增独立观测。更正a=Y/G的Jacobian须保留raw/G及calibration crossCov和各line共用G造成的相关；仅对角quotederrors无法重建完整Σ。Eq9对phi/g是偶函数，所以衰减本身不认证g符号；centralG2>1没有realphi，边界处理必须显式，不剪裁成1再声称精确fit。

EL18-7的真实104Mo大δ支跨同一pureE2点，EL18-9的部分打印更正未闭合则说明：publishedcorrected列/原producer/本任务重算是不同验证层。可用新增[projective脚本](../../system/scripts/day16_el18_projective_branch_audit.py)核所声明输入，但缺actual门/response/Σ时不替代原δ或形变结论。

## Genericproducer的输入误差与实验Σ

[[ekstrom-1993-delta101-angular-correlation-code]] D101-2/5/8的公开源码将每dataitem独立加入standardizedsquares，没有fullΣ/theorycomponenterror输入，DIPS另有F阈值和1000limit sentinel。输入uncertainty0可关闭A2/A4项或把δ固定；内部PURE名不自动是实际multipolepurity。用于来源论文的methodreference不证明实际producer/file/version/选择和误差口径一致。

D101-4还明确忽略mixed未观测跃迁的conversion-deorientation，SUK直接用δ²。若middlephoton被postselect与全部γ/ce未观测是不同条件，须回[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-3及[[internal-conversion-analysis]]处理totalweight；不能只因两个generic数学实现相符而抹掉sample条件。


## 混合比误差：profile、数据秩和临界表须分别核查

[[james-twin-butler-1974-angular-correlation-statistics]] JT74-5/6/7给θ=arctanδ的profile：固定θ后重新最小化其它参数得S_h，全局R=minS，单个参数的误差交点用S_h−R。原保守处方取增量max(1,R/ν·F)，ν=n−rank(design)，绝对阈值还要加R。它要求Gaussian及局部quadratic/linear-regression近似；不是对任意多解/nonlinear/physical-boundary都校准过的68% CI，也不同于多参数joint contour或ICC反演P(δ)分位区间。

原Table1/2与Fig.2明确：alignment估计是带误差的data，既改变S也改变n/rank；相关不自动等于精确秩亏。无独立alignment数据且δ/布居可补偿时，局部识别会退化；接近1的correlation或小奇异值不能单独决定整数rank，更不能从表行数直接给实验ν。正定已知Σ下可先白化design来核rank；未知/奇异Σ还须核有效支持，后一句是本任务统计延伸，不是原表提供的实验输入。

JT74 Sec.7.1/Fig.4中“忽略相关”的语境是取一个参数的marginal uncertainty同不依赖nuisance的理论比较；并非删去数据Cov或在profile时固定nuisance。检验δ1=Cδ2等joint假设，原文紧接着明确要Cov。原theory若不成立，S的分布也不再由该统计论保证，不能以更宽误差救回错误spin或response。

JT74-8/9与[[ekstrom-1993-delta101-angular-correlation-code]] D101-9另核原Table3/代码F表：JT74表数字的标准F上尾约.304–.308而非精确.32，代码则引用Gill1975、ν>16默认F=1。三者要分别记录；二者max结构相同不足以认证同一coverage。实际data/response/Σ和producer缺失时，不由这套方法另造EL18或W178的实验置信区间。


### pure M1附近的非二次profile与matched偏振

JT74-11是由原Fig.2路径出发的本任务推导，非新实验。对3→2的声明positive family p0=1−u、p±1=u/2、0<u<1，明确D96 nativeδ约定下a4=(6−5u)δ²/[7(1+δ²)]。纯M1时(a2,a4)对(δ,u)只rank1；profile未知u后，true-center距离首项为(6−5u0)²δ^4/(49Σ44)，不满足通常的δ二次近似。保留一般已知正定Σ与interior u时，局部λ=δ²≥0给半质量0+半χ1²的LR极限；ΔS=1在该点覆盖约84.13%，不能统称68%。这仅检验该条件族regularity，不把新阈值移植到真实DCO或其它混合比。

同density/gamma/方向下matched P90让(a2,P)的Jacobian determinant为2√30(4−u)/[5(24−u)]非零；已知非零Q的A=QP可增加局部信息。但Q自由时三参数(δ,u,Q)仍缺一rank，必须有独立且匹配的Q校准及其Cov；用同一A/P校Q后回代不增加该row。完整isotropy或Q=0是明确失败控制。局部fullrank也不证明global唯一解；原Fig2的δ相位/“equal population”口径未认证，所以未声称逐点复现原curve。完整方程与actual symbolic/trace controls见[[james-twin-butler-1974-angular-correlation-statistics]]的JT74-11。
