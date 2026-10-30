# BR85 §§1–2：参数、旋转基、交叉追踪与总能量合同

**048读区已完成：physicalPDF1–16全部连续主线与逐页fresh视觉，覆盖printed14–29的§1–2、Eqs1–26、Table1和Figs1–4。** 这是对046入口读区的实质推进，不是将先前参数表/机器命中扩大成全篇已读。其余69页原稿的应用和结论不在本worker阅读认证内。

这篇历史原件确实给出WK22Ref11所指κ/μ参数集及其计算语境；新增可维护信息是N_rot的近似定义、p/n独立列、参数选取范围、虚交叉处理和固定I总能量。它**没有**恢复2022GAMPN/ASYMO/PROBMO实际输入、ν编号、ε/λ零点、BCS方案或目标核拟合；crankedNilsson–Strutinsky也不是QTRproducer。同一Day24/133Ce附属研究，不新开课程/session、不授分。新claim均`needs_review:true`。

## 原件身份和实际读法

Tord Bengtsson and Ingemar Ragnarsson, *Rotational bands and particle-hole excitations at very high spin*, NPA436(1985)14–82，DOI10.1016/0375-9474(85)90541-X。046通过publisher取得的现有正文：

`tmp/day24-bengtsson1985-046/attachment-object-response.pdf`

69pages，4596459bytes，SHA256独立复算`605e785734279f1a7a6dfd234f1d3ff6b136f983b134ccf9d6b766f3b027d6b8`。Printed=physicalPDF+13。先读046report/receipt核清其当时只读PDF1/5/6/69；本轮不覆写该历史scope。首页received/revised为1984，出版身份仍1985。

本轮PDF1–16文本全部按顺序阅读，随后逐页看渲染图校公式/表/图；PDF12/Fig4另旋正核读。文本和图在`tmp/day24-bengtsson1985-methods-048/`；自动抽取本身不算阅读，本scope以实际已读页列出。不联网、不重新取body、不运行计算模型/未知程序/114；Python仅用于现有PDF读出、render、hash与JSON记录。未改canonical/raw/PLAN/Bib/Git/课程。

## 1. Hamiltonian和κ/μ：原列定义不能脱离实现

§2先写固定x轴推转h^ω=h−ωj_x（Eq1，PDF2/printed15）。§2.1.1（PDF5/18，Eqs3–7）采用变形振子、hexadecapole项、Nilsson修正和推转：

\[
h^\omega=h_{\rm ho}(\epsilon,\gamma)+2\hbar\omega_0\rho^2\epsilon_4V_4(\gamma)+V'-\omega j_x,
\]
\[
V'=-\kappa(N)\hbar\omega_0
\{2\mathbf l_t\!\cdot\!\mathbf s+\mu(N)[\mathbf l_t^2-\langle\mathbf l_t^2\rangle_N]\}.
\]

下标t为**stretched-coordinate orbital operator**；κ/μ是Nilsson无量纲参数，μ不是BCS化学势λ。表值需要连同该势、壳指标、ℏω0和坐标定义使用，不能只凭κ/μ引用就恢复单粒子绝对零点。

Eq5–6将V4写成Y40、Y42+Y4−2、Y44+Y4−4组合，取a40=(5cos²γ+1)/6、a42=−√30sin2γ/12、a44=√70sin²γ/12，使γ=−120°,−60°,0°,60°的轴对称性不被破坏。作者还明确别的ε4符号/轴约定可用。因此把别文同名ε4数字直接移入并不自动保持同一几何/势。

### Table1精确字面

PhysicalPDF6/printed19，caption为“parameters…used in this work”，表头第一列N_rot，随后分别是Protonsκ/μ与Neutronsκ/μ。已fresh视觉核全部九行：

|N_rot|protonκ|protonμ|neutronκ|neutronμ|
|---:|---:|---:|---:|---:|
|0|.120|.00|.120|.00|
|1|.120|.00|.120|.00|
|2|.105|.00|.105|.00|
|3|.090|.30|.090|.25|
|4|.065|.57|.070|.39|
|5|.060|.65|.062|.43|
|6|.054|.69|.062|.34|
|7|.054|.69|.062|.26|
|8|.054|.69|.062|.26|

PDF5末–PDF6首连续说明其选参目标：essentially reproduceRef25对rare-earth/actinide **valence orbitals**的fit；较轻区特别关注Z或N=8,20,28的single-particle gaps，并要求κ/μ随N平滑。作者称ground-state deformation/mass测试与其它Nilsson参数集精度相近，引用Ref26；这是一项作者测试声明，048未读Ref25/26或重跑该测试。原文没有在此指定“WK22的133Ce实际负宇称轨道18必采用表中某行且完全未修改”。

Figs2/3（PDF7–8，printed20–21）分别是这套参数的proton/neutron single-particle diagrams，纵轴e_i/(ℏω0)、横轴ε，取近似液滴谷ε4=ε²/6。实/虚线分别为正/负宇称；不是测得的Ce能级或WK22ε表单位说明。图用于辨认这套**理论**参数谱，不提供2022实际轨道header或零点。

## 2. N_rot究竟是什么：人为保留的近似壳标签

§2开头PDF4/17承认虚交叉清除有任意性，因重核能级密度高而增加一个保留量N_rot来减少此问题。§2.1.2（PDF6/19 Eqs8–10）先对crankedharmonic oscillator作变换，使其成为三个解耦振子，基写|n1n2n3Σ〉；Σ是沿crankingx轴的intrinsicspinprojection，Ω1=ωx，Ω2/Ω3依赖ωy、ωz与推转频率ω。

PDF9/22明确

\[
N_{\rm rot}=n_1+n_2+n_3.
\]

推转j_x耦合已经包含在旋转基内。完整势中V4、l_t·s、l_t²仍可耦合不同N_rot；作者以“reasonableω”“moderatedeformation”的小跨壳效应为理由**忽略这些off-shell矩阵元**，从而将N_rot作为保留量。因此它不是未截断Hamiltonian的额外严格守恒量，也不是Nilsson轨道νID、Ω、单个粒子数或qp计数。

Eq11实际矩阵构造还更具体：旋转基与非旋转|NljΩ〉基之间作变换，保留相同N_rot的旋转基块，并在非旋转求和中取**N=N′=N_rot**。这正是Table1表头N_rot与上文κ(N)/μ(N)的具体实现连接；不能只把N和N_rot当所有模型中无条件相同的量。表中p/n行须与这一近似Hamiltonian块一起解释。

§2.1.3（PDF9–10，22–23，Eqs12–17）不用简单数值本征矢排序来生成该变换，而以step operators和最低|000Σ〉的迭代展开建立波函数，避免简并时量子数指派困难。V_res有ΔN2耦合，N8幅至少需四次迭代；作者称本应用六次足够到计算机数值误差。048只核该实际算法与范围声明，不把“六次exact”当现代误差证明或2022截断收敛证书。

## 3. Pairing忽略：作者的近似、警告和可比对象

PDF1/14最后一段明确本计算忽略pairing，因此very-low-spin的**详细**理论–实验比较无意义；PDF2/15接着说何处pairing energy可忽略仍未充分理解，拟通过不同spin/massregion的比较研究。作者另外报告经验：即使最低spin，只有特殊情形yrastdeformation才显著受pairing影响。两句话不是矛盾：形变极小位置可能较稳健，不等具体低spin能谱/时钟/率已可忽略pairing。

PDF5/18 §2.1又明确其主要关注veryhighspin、pairing预期已减弱，以及同时处理大形变变化与pairing的巨大计算成本，故选择忽略并把许可性留给实验比较。这不是“达到某个普适spin后pairing严格为零”的结论，也不能替WK22已经含BCS的QTR删去λ/Δ或将BR85无pairing占据当WK22实际输入。

## 4. 虚交叉在ω、真实相互作用在I：两种问题不混用

PDF2/15–PDF4/17、Fig1/PDF3：相同量子数轨道随ω接近时，adiabatic本征支不交叉而在窄区间交换波函数，作者称virtualcrossing。真实两配置相互作用应在同一总I上讨论，未必对应同一ω。

由占据轨道计算（Eq2，PDF3/16）：

\[
I=I_{\rm sp}=\sum_{\rm occ}\langle j_x\rangle_i,
\qquad E_{\rm sp}=\sum_{\rm occ}e_i^\omega+\omega I_{\rm sp}.
\]

保留Fermi附近虚交叉时，低支在近constantω处出现I骤增，E_sp(I)近线性；激发支可能出现I下降甚至loop。Fig1的另一不同parity激发支可真正交叉并保较规则的二次能量行为。普通optimal-state法每ω只填最低轨道，再插值中间I，会把不同真实支的变化过度抹平，故作者仅认为其给grossbehavior。

§2.2.1（PDF11/24）给fixeddeformation上的Hellmann–Feynman关系

\[
de_i^\omega/d\omega=-\langle j_x\rangle_i.\tag{18}
\]

同页Eq19在一个简单two-level模型中给V<i²/(4J_c)会产生backbend，i为crossing单粒子alignment，J_c为kinematicalinertia。它是该方法说明中的有前提判据，不是用来给133Ce或135Nd填V的实验反演式、不是手征临界门。除去满足此条件的弱虚交叉可避免excited-band回弯计算困难；不代表所有实际弱相互作用物理上为零。

## 5. Diabatictracking的实际步骤和任意性

Fig4（PDF12/25，另旋正）固定ε=.16、γ15°、ε40，所有轨道N_rot5、signatureα+1/2，比较三种连接：a按non-crossingenergyorder；b按波函数overlap；c按−〈jx〉的能量切线。它是同一组计算点的追踪方式比较，不是三套实验。PDF13/26定义相邻频点overlapabs(〈φ_i(ω_n)|φ_j(ω_n+1)〉)²（Eq20）：>.9画实线，较小最大overlap用虚线，>.1的竞争overlap用点线。这些数是图/追踪阈值，**不是核波函数概率置信门或普适数值精度**。

强交互疑难区可在所涉轨道子空间删除coupling后rediagonalize（引Ref31）；本文主要采用只需e^ω与〈jx〉的简化追踪，不需保存全部wavefunctions。Eqs21–22（PDF13）向前、向后外推

\[
\widehat e_i(\omega+\Delta\omega)=e_i^\omega-\Delta\omega\langle j_x\rangle_i^\omega,
\quad
\widehat e_k(\omega)=e_k^{\omega+\Delta\omega}+\Delta\omega\langle j_x\rangle_k^{\omega+\Delta\omega}.
\]

双向差都在ΔjΔω内则连接，本文Δj=.6（PDF14/27）是由若干单粒子图研究选取的作者数值容差，不是拟合某实际bandmixingV。若相邻点落在最大相互作用处而无好连接，则搜跨两个ωstep；中间点用由两端e和jx决定的三次多项式插值，并调整使相互作用轨道的**能量和jx总和**不变。

最重要的作者限制在PDF14：此法目标是完全去掉弱交互，**“not fully correct”**，因为真实bands间总应有一些interaction；低ω某些h11/2 crossing尤其可疑。作者要求验证最终性质不强依赖可疑连接。因此“去交互diabatic支平滑”是有意近似，不等于实际证明混合为零，也不提供固定I的真实interaction或相干EM核。此程序可用于Woods–Saxon，不意味着它就是QTR本征态算符/输入producer。

## 6. Configuration、band、yrast：原作者有不同定义

§2.3，PDF14–15/27–28，Eq23：总parity为占据轨道parity之积；总signatureα为单粒子α的和mod2。evennucleusα0给evenI、α±1给oddI；oddnucleusα−1/2给3/2,7/2,11/2…，α+1/2给1/2,5/2,9/2…。分别保存parity/signature，得四条分支yrastline。

“Configuration”在此特指**各(N_rot,α)对称组中规定的占据数**，每组填一定数量较低轨道，parity由N_rot定；它是一个较粗分组。“Band”指去虚交叉后沿同一组tracked单粒子轨道建立的一串高spin态。**同一configuration可以含多个band**，本文给的是这些band中yrast部分，不是每个configuration唯一对应一个实验band号，也不是所有同signature近能级都应自动合并。

§2.4（PDF15/28）在givenconfiguration中追踪某ω下optimal或可由低能1p1h/2p2h到达的proton/neutronband；然后每一I取其中最低E_sp(I)。先固定occupationgroup/track再在其内取最低，不等于每ω全局重新填Fermi面；更不是coherent配置GCM或真实bandmixing对角化。

## 7. 总能量不等Routhian和单粒子和

PDF16/29，Eqs24–26：

\[
E_{\rm tot}(I)=E_{\rm sp}(I)-\langle E_{\rm sp}(I)\rangle_{
\rm Strutinsky}+E_{\rm rld}(I),
\]
\[
E_{\rm rld}(I)=E_{\rm surf}+E_{\rm Coul}
+\frac{\hbar^2I^2}{2J_{\rm rig}},
\qquad E_{\rm sh}(\omega=0)=\sum_i e_i-\left\langle\sum_i e_i\right\rangle.
\]

液滴surface/Coulomb参数外引Ref35，J_rig取sharpnuclearsurface、r0=1.2fm；每个configuration和每个I，在许多deformation点上分别极小化E_tot。公式用I²，不是本篇写I(I+1)的精确投影式。这个总能量已有shellcorrection与macroscopic参考，不能把Eq2的Σe^ω或某图的e_i直接认作同一能量零点。

作者说明Nilssonl²项会使Strutinsky平滑平均的dynamicalinertia约比J_rig大30%，重整化意在平均恢复rigidrotation；但N+1高l轨道是否过低仍须与实际highspinband比较且与参数fit纠缠。这是方法固有/定标边界，不由Table1“通用”就消失。

其off-shell/cutoff检查具体是**166Yb、ω=0、ε≲.5**：与多两壳并含跨壳耦合的E_sh比较，只见相对其它不确定度小的变化。作者因rotatingbasis预期误差对ω较不敏感，并指出heavy-superdeformedstates可能例外。048未复算，不能将此一例变成所有核、所有spin、所有ε或WK22九轨道space的数值收敛证书。

## 公式/图表覆盖索引

|原位置|本轮实际核读内容|
|---|---|
|PDF2–3/15–16 Eqs1–2,Fig1|cranking、占据和、virtual/real crossing与E(I)问题|
|PDF5/18 Eqs3–7|HO+ε4+Nilsson势、stretchedl、γ/ε4项|
|PDF6/19 Table1,Eqs8–10|p/nκμ、rotatingbasis、Ω/Σ/energy|
|PDF7–8/20–21 Figs2–3|两张参数理论s.p.diagram、轴和ε4谷、parityline|
|PDF9–10/22–23 Eqs11–17|N_rotblock与N=N′限制、step/iterative生成变换|
|PDF11–14/24–27 Eqs18–22,Fig4|exactfixed-fieldslope、conditionaltwo-levelbackbend、overlap/tangenttracking与容差/插值|
|PDF15–16/28–29 Eqs23–26|occupationgroups、band定义、signature、Strutinsky/rld总能量与限定cutoff检查|

## 对WK22Ref11：哪些现在关闭，哪些仍未关闭

|层|048真实推进|仍需保留的actual边界|
|---|---|---|
|参数谱系|原Table1的p/n列、N_rot行、κμ值及选参目标已明确；不是再依赖二级引用|WK22是否照用/改动哪些shell、实际νID/基/截断仍无card或header|
|空间/追踪|原近似N_rot与diabatic弱交互清除、configuration/band差别已读|这不是QTR九轨道混合或2022PROBMOsignedEM输出；不能沿平滑支反造完整相干态|
|pairing|本文nopairing的目标和警告完整|WK22有BCS，不能借此取消λ/Δ、blocking或选哪套方案|
|能量与零点|s.p.Routhian、lab s.p.sum、Strutinsky平均、rld和total能量分层|不能用本图e/(ℏω0)或shelllabel恢复WK22ε5–6MeV与λ50.6的共同零点；negativeλ未知仍未知|
|适用核和模式|历史veryhighspin方法有明确限制|未做135Nd替代fit，未产生133Ce3qpcrossing/τ/δ/g/shape实测或新手征判据|

本读区到PDF16结束；其后applications交由父任务其它既定读区。不自派新任务、不因方法已读就认证69页全文。最高信息下一步是父任务将方法与实际applications/限制合并，而不是再套一个无原始input的CNS/QTR数值job。
