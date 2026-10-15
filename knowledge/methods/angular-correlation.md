---
type: method
title: γ 射线角关联分析
aliases: [angular correlation, gamma-ray angular correlation, particle-gamma angular correlation, gamma-gamma angular correlation]
created: 2026-07-09
updated: 2026-10-15
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
