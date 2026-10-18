---
type: method
title: DCO与PDCO双解：点响应与相位坐标
aliases: [delta-double-solution-sheet, DCO PDCO ambiguity worksheet, D96 point-response ambiguity]
created: 2026-10-17
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
method_type: gamma-gamma-directional-correlation
tags: [dco, pdco, mixing-ratio, phase-convention, conditional-response]
---

# DCO与PDCO双解：点响应与相位坐标

## Purpose

沿[[droste-1996-pdco-formalism]] DR96-4/5/6独立复算5→4→2模型，并以[[krane-steffen-1970-cd110-mixing-ratios]]实际818–658 corrected coefficients作另一项受限反演。这是L2理论/表值/设计练习，**不是raw RDCO重放、作者FORTRAN运行或新核素赋值**。下文从两篇原式核同BM定义的桥，区分实现坐标、文献约定和真正物理双根；不凭同名符号或近似数值认证任意文献的全局转换。

## Inputs and Assumptions

source模型在Fig7（printed524）指定`I0/I1/I2=5/4/2、sigma/I0=.3`，Eq19给有限Gaussian `p(M0) proportional exp(−M0²/(2sigma²))`；所以本例sigma=1.5，不另给daughter重设Gaussian。第二条gamma2为4→2的pureE2。比较gamma1的pureE1（改变宇称的假设）及M1/E2（不改宇称）；不是把不同电磁类型混入同一个有确定宇称的振幅。

使用point detectors、无feeding/未观测中间跃迁/外场去取向；没有finite acceptance、FEP效率、polarimeter Q(E)、background或实际Cov。所有初始ρ、geometry和spin对候选固定；实际变动这些nuisance可能增加多解。

本计算单先**自己定义**

\[
R^*=W_{00}(\gamma_1:0^\circ,\gamma_2:90^\circ)
/W_{00}(\gamma_1:90^\circ,\gamma_2:0^\circ).
\]

source Fig7也说DCO用0/90°。随后独立回核[[kramer-flecken-1989-use-dco-ratios]] printed334，旧Wiki实验式的倒置由KF89-9更正：其W第一角是门角、第二角是待测角，gamma标签不自动是物理发射先后。按物理先后a、b，本R*对应KF的(obs=a,gate=b,theta1=0,theta2=90)，也对应(obs=b,gate=a,theta1=90,theta2=0)；单独交换一套角标签或obs/gate则给1/R*。D96图注未列全部gate/ordered-detector标签，不只凭约.4反推唯一标签解释。KF的low-spin/width边界又说明D96的I0=5、sigma/I0=.3是作者模型输入，不是实际低spin alignment测量。

PDCO取两光子theta=90°、phi=180°，与source phi=0按其90°平面对称关系对应并经计算核验；phi=180使用两个相反方向，避免将同一point detector当成两个不同台。角度外部用degree，Wigner函数内部显式转radian。

输入身份`DAY16-PREVIEW-D96-5-4-2-POINT-MODEL-01`，冻结JSON SHA-256 `9cf693c7416634e007601cfeeb13b632f086681a17e7c12ba134494e526efa7d`。冻结时已经读过D96文字和图中近似数，属于primed复算，不是盲复现。

## 从振幅到条件态的最小模型

冻结probe实现选Condon–Shortley CG、`D*=exp(+i mu phi)d(theta)`及`d^1_(0,+1)=+sin(theta)/sqrt2`：

\[
T_{\lambda,M_fM_i}^{TL}(\Omega)=
\sqrt{\frac{2L+1}{8\pi}}
\langle I_fM_f,L\mu|I_iM_i\rangle D^{L*}_{\mu\lambda}(\phi,\theta,0)\eta_T(\lambda),
\quad \mu=M_i-M_f,
\quad \eta_E=1,\ \eta_M=\lambda.
\]

photon1/2算符串联后，对未观测final spin和helicity取trace；polarization analyzer则取`[-exp(i psi)T_+ + exp(−i psi)T_-]/sqrt2`。psi=0表示电场在emission plane内，故`P=(W_psi0−W_psi90)/(W_psi0+W_psi90)`。各multipole全角/helicity积分的channel为identity；normalized mixed amplitudes的总概率为1。联合density单位为每sr²，R和P无量纲；不是仪器测得的asymmetry A。

### Pure checks不足以核混合相位

首个scratch因没有SymPy而未产生数值，随后改用同一Condon–Shortley约定的有理Racah CG和Wigner有限和，未改冻结physics。pureE1的singles/PDCO基准通过；但同名正负混合参数与source例不符，保留[首轮probe回执](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-point-probe-receipt.json)，没有直接翻符号后宣布成功。

独立从DR96-5（printed519 Eq3、printed520 Eq7）计算F：9j通过两种四角动量耦合基底的六CG重叠求得，另由photon kernel角分布作Legendre投影。source-native定义`d=a(E2)/a(M1)`、基底顺序(M1,E2)时，本例

\[
F_0=I,\qquad
F_2=\begin{pmatrix}.2943920289&-.9309493363\\-.9309493363&0\end{pmatrix},\quad
F_4=\begin{pmatrix}0&0\\0&.5665577237\end{pmatrix}.
\]

冻结probe与source的F相差`S=diag(1,−1)`的相对基底变换；必须用`delta_probe=−d`。保留冻结probe定义，把变换显式作用于坐标，不改原输入。source Eq5的M1/E2两项都含i²，不能仅由此断定整个geometrical basis的相位也相同。完整Eq3/7含CG、9j、初末态顺序和相位，才给这里的对应。

不同d的normalized angular coefficients经两条计算路径最大差`6.7e−16`；不转换时某项差可到1.6352。pure multipoles的对角项在两坐标中一致，所以仅靠pure reference不能检验混合干涉项的实现。这个内部基底对应**不是**对其它文献delta定义的自动换号规则。


### D96与KS70共享BM定义下的桥

KS70 printed727 Eq4b的magnetic显式负号不可漏掉。记其发射RME为t_KS（不是去取向U_lambda），electric项是`C_L i^L M(EL)`，magnetic项是`−C_L i^(L−1)M(ML)=C_L i^(L+1)M(ML)`。同BM算符/state phases/units和同一transition下，D96 Eq5因此满足

\[
a_{D96}(TL)=\sqrt{8\pi k/(2I_i+1)}\,t_{KS}(TL),\qquad
d_{D96}=\delta_{KS}\quad(\hbox{同一gamma的E2/M1}).
\]

共同positive normalization只在同gamma的multipole ratio内抵消；不同gamma的absolute rates有各自E/spin因子。不能把`delta_probe=−d_source`误说成“KS70 delta=−D96 delta”。两文共享BM理论定义，桥相容不是新增独立实验。

KS70 Eq10的B(first photon)有负线性干涉项，Eq11的A(second photon)有正干涉项。Eq12的BR是**Biedenharn–Rose1953**：gamma1处delta_KS=−delta_BR，gamma2处=+delta_BR；Eq5的**Rose–Brink1967**是另一份state-order/operator-normalization映射。initial-left在这里仍指发射notation，不仅凭bra/ket位置改叫实际吸收。裸T_RB比还需sqrt(2L+1)归一，不能直接同名替换。

### Rose–Brink归一化坐标的闭合

本run针对[[rose-brink-1967-phase-defined-angular-distributions]] RB67-6的printed319/PDF14 Eq3.39及KS70 printed727/PDF4 Eq5作定向原图复核；RB67-6已有的a_RB定义与observable中的E2/M1符号链获确认，没有新的人审或新实验。

令`a_RB(TL)=<Ii||T_L||If>/sqrt(2L+1)`，则KS70 Eq5逐L给

\[
t_{KS}(TL)=(-1)^{I_i-I_f+L}\sqrt{\frac{2I_i+1}{2\pi}}\,a_{RB}(TL).
\]

放大KS70 Eq5确认共同因子是2Ii+1（初态），不是2If+1；本段首份未发布草稿的下标误读已修正。与D96桥相乘后得到`a_D96(TL)=(-1)^(Ii−If+L) 2sqrt(k) a_RB(TL)`，其平方和回到RB67 Eq3.29的`Gamma_gamma=4k sum|a_RB|²`。这是absolute normalization的反向检查，非新增实验。

同一transition的spin normalization和共同state phase抵消。因此

\[
\frac{t_{KS}(T'L')}{t_{KS}(TL)}=(-1)^{L'-L}\frac{a_{RB}(T'L')}{a_{RB}(TL)}.
\]

对本页相邻E2/M1坐标：`d_D96=delta_KS=−delta_RB`；冻结probe的相对坐标`delta_probe=−d_D96`于是数值等于delta_RB，但这是逐定义闭合后的结果，不能由两个相似符号猜测。高阶与低阶相差偶数时该L-phase为正；不把这里的E2/M1符号链无条件套到任意两算符。

从KS70实际系数方程代换`delta_KS=−delta_RB`，RB形式的A22线性项变为正，A44及所有delta平方份额不变。原两根`−1.426985941/−.194000621`只是在RB坐标中写成`+1.426985941/+.194000621`，并未增加物理候选。若只改delta符号而不改几何/干涉项，预测会变；只核width或pure limits检测不到此错误。精确裸T比还差sqrt(5/3)，不能再把它当已归一delta。

| 同一E2/M1物理振幅的坐标 | 对d_D96的关系 | 角色限制 |
| --- | --- | --- |
| D96 Eq3/5 | d_D96 | 当前source BM定义 |
| KS70 Eq4/9 | +d_D96 | 同BM算符、同transition |
| RB67 Eq3.39 | −d_D96 | normalized interaction RME；初态在左仍是emission |
| Biedenharn–Rose1953 γ1 | −d_D96 | KS70 Eq12第一条populating gamma |
| Biedenharn–Rose1953 γ2 | +d_D96 | KS70 Eq12第二条radiating gamma |
| 本任务冻结probe | −d_D96 | 固定implementation basis，不是另一实验约定 |

此表的source/坐标桥与候选多解分开保存；同一transition的符号重写不是统计独立证据。source边界见KS70-13及RB67-6，原审核状态保持。

## 精确同R双根与近似source点分开

从上述模型的pure dipole预测固定`R*=.4062005480`，这是主动构造的逆问题witness，未伪装成观测数据。在M1/E2假设下，R是两个quadratic forms的比；同R约束给source振幅坐标的两根

\[
d=0,\quad d=-3.1952146985,
\qquad \arctan d=0^\circ,\ -72.6215491^\circ.
\]

不同first E/M性质还允许pureE1有同样的directional R。这里初末态parity是竞争假设的一部分，不能只把一张M1/E2表的d套给E1。

| 候选/身份 | R* | gamma1 singles P | POL-DIR：测gamma1 P | DIR-POL：测gamma2 P |
| --- | ---: | ---: | ---: | ---: |
| pureE1，改变宇称 | .406200548 | .343428707 | .560408130 | .560408130 |
| M1/E2的d=0，pureM1 | .406200548 | −.343428707 | −.560408130 | .560408130 |
| M1/E2的精确同R第二根d=−3.195214698 | .406200548 | .269005901 | .384948788 | .208820728 |
| source的−70°近似示例，d=−tan70° | .362034032 | .273255004 | .437181265 | .173582689 |

最后一行不与前三行混成一个精确同R点。source DR96-6写R约.4，给−70°时的P约.27/.44/.17；独立计算与其印刷精度相符，但source没有给统计误差。不能将source近似示例的P值移到本任务精确根−72.62°上，也不能由.406和.362的差在无sigma_R时判实验允许/排除。

## 必要观测与失败控制

实际164Yb reference的后续核验见[[st99-pdco-calibration-table-replay]]与[[nndc-2018-164yb-pdco-reference-records]]。N164-6的647实测EKC上限是ST99原已使用的prior；N164-4的489 KC/CC为采用E2的BrIcc，不是新增转换测量。目标T1/2及其derived BE2也不能循环选δ，302未知ICC/branch Cov要保留。这给“补一个独立观测”设定了具体数据身份门，而不是只再取一个adopted标签。

只有R时，M1/E2两根都容许；测gamma1的P符号可区分pureM1与mixed根，但引入未知初态宇称后，pureE1和mixed仍可能都给positive P。若当前候选已限定为E1/mixed，测已知gamma2(E2)在两种上游选择下的条件P，在本模型给更大分离（.5604对.2088）；这来自条件daughter density，不是gamma2的多极性改变。

DIR-POL不能单独区分pureE1和pureM1，因为第一条未测偏振时两者在此几何给同一条件density。实际需要同一transition/cuts下的DCO、第一条/第二条polarization及可比较的alignment/response；不能称某一个新增observable普适唯一赋值。没有Q(E)、selected counts、background/Cov时，不算实际significance或所需束流时间。

以下验证均为本任务模型控制，不是独立实验：

- source F0归一、CG/Wigner相位及generalized F与direct photon kernel的混合项对应；mixed失配的首轮数值留证。
- angular/helicity channel identity在6×12与12×24 quadrature下最大偏差`6.8e−15`；正交linear analyzer两结果之和回到unpolarized W。
- 完全isotropic初态给R*=1、singles P=0；back-to-back条件P也为0，但把phi改90°，本例pureM1条件P=.103448276，说明无alignment不要求所有PDCO为零（printed523的一般边界）。
- 对未观测gamma1作完整trace后生成的daughter tensor，与source Eq13–15的`B_lambda(I0) U_lambda(gamma1)`吻合；没有重设daughter Gaussian。source模型中的完整4π积分与有限角门分别保存。
- phi0/180、pure limits和同R两根的observable关系按声明geometry核验；source-native/implementation的坐标改变不应改变同一个物理预测。


## KS70已校正818–658点的受限双根

第二项输入身份`DAY16-PREVIEW-KS70-818-658-TABLEII-01`、SHA-256 `a195a5d0a44433b4148f5a54bc069a5654dc7a916880c1d4992e5d06c7992673`。KS70-10的direct TableII给`A22=.375±.050、A44=.180±.050`；indirect TableI的658门818行给`.481±.082、.155±.112`。这些是**已background/finite-geometry修正的gamma-gamma opening-angle coefficients**，不是beam-oriented DCO的detector-swapped ratio或raw counts。

Fig5的spin path是`2+(1475.7)→2+(657.7)→0+(0)`，target818.0keV、gate657.7（nominal658）pureE2；parent为110mAg，文中253day是历史source值。此处初态无取向rho=I/5。第一条按M1/E2截断，第二条2+→0+的pureE2由spin/parity选律固定；不把本页固定spin model当新的Jpi测量。

在同KS emission convention下，direct photon kernel与独立generalizedF乘积均得

\[
A_{22}(\delta)=\frac{1/4-(\sqrt{105}/14)\delta-(15/196)\delta^2}{1+\delta^2},\qquad
A_{44}(\delta)=\frac{16}{49}\frac{\delta^2}{1+\delta^2}.
\]

两路径最大差`5.6e−16`。A22是二维Rayleigh quotient，其全实delta范围`[−.313994805,.487464193]`；超出range的central datum不能硬造实根。

仅由TableII central A22得到两个实根，**不是重提取原文25-correlation global fit**：

| KS坐标central根 | atan(delta)/degree | 预测A44 | 与原A44=.180±.050的关系 |
| --- | ---: | ---: | --- |
| −1.426985941 | −54.9780834 | .218987942 | 在所列边际±范围内 |
| −.194000621 | −10.9790360 | .011843635 | 不在该字面范围内 |

A44增加functional information，但它与A22来自共同fit/background/geometry，**不是统计独立的重复证据**。把quoted margins作为rectangle，A22的atan preimage为`[−59.7373,−49.1895]`与`[−16.7676,−6.2199]`；再和A44字面范围相交只余`[−57.0632,−49.1895]`。这些是选定rectangle的preimage，没有置信水平，不称68%/95%CI或显著性排除。

TableI central A22在near-maximum处给另两个central根约`−.78498/−.52782`；quoted上沿超出physical maximum不等于数据错误，只表明fold附近的反演非线性。TableIII global delta=`−1.20±.15`给本模型预测`A22=.417256551、A44=.192706591`，来自共同network的summary不能再当独立输入和TableI/II相乘。

[反演脚本](../../system/scripts/day16_ks70_convention_inversion.py)、[冻结系数](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ks70-818-inversion-input.json)、[preimages/单位结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ks70-convention-inversion.json)、[系数图](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ks70-inverse.svg)保留两配置全部输入。图的bands是quoted marginal ranges，points是模型根，无joint confidence fit。

### 单位列、源精度与共同数据

KS70 Eq9在electron-mass natural units给`delta=(sqrt3/10)k Delta_BM`。本任务用声明的rounded单位常数得到`delta≈.83473 E_gamma(MeV) Delta_(eb/muN)`，不是1970 exact constant-set重建。TableIII15行中8个finite mixed rows做单位核算，7个pureE2限值保留∞；没有将∞强作finite data。所有central列和Fig5的radiative M1百分比在印刷精度下相容。

误差列另有精度边界：把全部尾零当significant digit的严格诊断在620.2keV的`.50→.95`误差转换不闭合。放大原件确认此印值，未改数据/容差；尾零排版、unrounded estimates和作者rounding recipe未给。保留该诊断，不宣称8行的全部误差已精确重现。delta、BM moments与M1百分比共享同一fit，不增独立测量。

`1/(1+delta²)`只属于radiative M1/E2子集，不是整个核态总衰变分支。2+→2+还可能有E0 conversion，E0不进入此single-gamma模型；本页不推出absolute B、总寿命或E0排除。


## 勘误公式与有向分析轴的独立核验

[[droste-1996-pdco-formalism]] DR96-8/9和[[starosta-1999-pdco-experimental-test]] ST99-8支撑本段。不是再跑5→4→2双根：本次冻结两个新chosen路径3→2→0（E2 gate）与2→1→0（M1 gate），正的对称布居分别为(1,2,4,6,4,2,1)/20和(1,3,5,3,1)/13；比较pureM1/E1/E2及native d=+.3/−.3/+1.7、四个点几何和in/perp/oblique分析轴。它们均是模型输入，非测量。

第一条代数路线逐项实现Eq1、Eq3/4、Eq7/8及B张量；第二条直接合成photon operators后trace。两者共享已验证CG/Wigner基础函数，不能称两份完全独立程序。Eq8的H含CG比，数值上与Eq7的相同CG先解析约消，避免合法零项出现0/0；rank<2的polarization d元素严格为零。

本probe采用Dstar和Jones组合`[-exp(+i psi_probe)Tplus+exp(−i psi_probe)Tminus]/sqrt2`。其强度交叉项是`−Re[exp(2i psi_probe)Tplus Tminus*]`；与Eq1的有向分析轴坐标对应时，显式用`psi_probe=−psi_Eq1`，native振幅仍按既有`(-1)^L`映射。这个implementation map不认证实际detector的全局handedness。

初次numeric结果中DCO和psi0/90已经匹配，但oblique分析轴最大差.00182560；因为`sin(2psi)=0`，只测in/perp平面看不出上述方向映射。保留原结果与code snapshot，识别映射后未改冻结physical inputs。整个网格都是source-informed检查，不是blind或独立holdout。

最终勘误公式与direct trace最大差`1.04084×10^-17 sr^-2`，总角积分两阶均为1（差<2.2×10^-15），互补分析轴之和差<6.1×10^-18、反射对称差<3.5×10^-18。**原印T磁相位在pure项也通过**，但mixed最大差.00142805；例如chosen2→1→0、d=1.7、90/90/phi180，corrected/direct P=.16164223，原印式P=.80047168。原式勘误、analyzer坐标与真正delta双根须分别检验，pure limits或两个轴平面的通过都不充分。

复算入口：[脚本](../../system/scripts/day16_d96_eq4_erratum_audit.py)、[冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-d96-eq4-audit-input.json)（SHA-256 `95fd2ebfb8e20eb006ad7bde1e4bb4d8969389b65bffa936d978f8fec54d685d`）、[最终结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-d96-eq4-audit.json)、[首轮numeric结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-d96-eq4-audit-first.json)、[坐标定位](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-d96-eq4-coordinate-diagnostic.json)。更早一次rank0非法投影调用在生成numeric前失败，局部zero guard修复；未改旧helper或physics。范围仅integer、real、L≤2、DCO/一个polarimeter；无实际array response/events/Cov或作者FORTRAN，不外推135Pr或PPCO。stop contract已满足，不再调此网格参数。

## Thematic REFLECT：比值、响应与参数的使用门

2026-10-17实验对照：[[st99-pdco-calibration-table-replay]]以实际164Yb来源保存Q/a/geometry、五点NDF和非唯一候选。[[starosta-1999-pdco-experimental-test]] ST99-8还明确更正D96 Eq4磁相位为Tprime而非T（DR96-8）；本页早前用Eq3/7与独立Jones/RB路径得到的实现坐标映射不是该印刷勘误。原式逐字实现、振幅基底转换、真实物理双解是三个不同检查。

本组来源改变的是判读合同，不是某核已确定的结构模式。可复用的认识修正为：

| 先前容易混用的量/假设 | 本组来源给出的更严格判断 | 证据与可触发修正的下一输入 |
| --- | --- | --- |
| 两角计数和效率即可识别f | 只给R；还需独立本征比或gate/geometry，并分开source分离近似与fulljoint | [[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-6/9；实际pair response/参考 |
| event mixing或single-gamma校准等于完整response | 匹配效率权重后仍有有限角卷积；固定公开code不等于完整replay | [[smith-2019-griffin-angular-correlation-analysis]] SG19-3/6/17；actualgeometry/recipe/data |
| pure limits通过就核准了所有相位 | diagonal项可一致而mixed interference基底仍错；需sourceoperator/F及明确转换 | DR96-5、KS70-5/6；mixed reference或逐定义映射 |
| 一个central coefficient、一个P符号足以选解 | 固定模型仍有两根，额外形状/测量mode能改候选排序；真实confidence还需jointCov | KS70-10、DR96-6；matchedA44/P1/P2/Q/counts/Σ |
| source被人审后不会再有转写错误 | 原件证明旧实验DCO分式倒置；新KF89-9优先，原review历史不扩至新更正 | [[kramer-flecken-1989-use-dco-ratios]] KF89-9；保留原件和review范围 |
| 表的delta、moments、M1percent是多份独立实证 | 它们是相同fit/定义的派生列，不重复计数 | KS70-5、SG19-10；保存event/calibration依赖 |

停止本层实际实验反演的输入缺口是original event/selection、geometry/response、背景与normalized-coefficient Cov。知识预习与条件计算仍可继续，但不能以这些练习给实际Jpi、delta confidence或collective-mode裁决。当前优先补的是会改变候选排序的独立约束与完整input identity，而不是再测一个同counts的ratio变形。

## What It Can Establish

独立正式Day16的新实测对象见[[w178-921-dco-gate-double-solutions]]：KF89-15/16的178W921两组gate角色、作者两候选和强度companion，与本页Day15预习计算分开。新高自旋point反演和完整D96 tensor核验是本session交付；未恢复DCOMAP/response/Cov时不把其根替换作者支，也不将旧预习重记为新学分。

提供一个可复算的理论双解、精确/近似数据身份交叉表，以及source F/实现基底的相位核对；说明为何pure reference、一个directional ratio或一个polarity符号不够。可用于设计能改变候选排序的下一测量和代码验证。

## What It Cannot Establish Alone

本计算单没有raw RDCO counts、production response或完整Cov，不能给测量的delta置信区间、唯一Jpi、模式或B值；已有的是source模型与已校正angular coefficients。Ref1的分式/标签已原件更正，同BM定义下D96/KS70桥已核，不等于任意paper全部约定已认证。没有作者FORTRAN，不外推half-integer、高rank、其它sigma/feeding/array；整数5/4/2和2/2/0只在本文条件下验证。

## Sources

- [[droste-1996-pdco-formalism]] DR96-4：完整边缘/未观测feeding U；DR96-5：a(TL)、alpha、CG/9j/phase；DR96-6：Fig7/正文的作者模型和geometry；DR96-7：FORTRAN未取得的边界。
- [[krane-steffen-1970-cd110-mixing-ratios]] KS70-5/6/7/10/11：BM/RME/角色、actual coefficients和source precision。
- [[kramer-flecken-1989-use-dco-ratios]] KF89-9/10/11/13/14：原件分式与标签、同L/width/mixed-pair迁移边界。
- [[angular-correlation]]与[[multipole-mixing-ratio]]：本页为条件方法练习，不替换其通用定义；跨文献算符/状态顺序仍须原文映射。
- [脚本](../../system/scripts/day16_pdco_ambiguity_preview.py)、[冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-pdco-point-model-input.json)、[完整模型与控制](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-pdco-ambiguity-preview.json)、[F基底核对](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-d96-derived-phase-map.json)。参数、证明、数据表和边界已在本页保存，不只留在outputs。
