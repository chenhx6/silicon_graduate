# 049：Bengtsson–Ragnarsson1985 连续谱、固定组态和终止带应用的证据合同

本单元已直接读physicalPDF17–46（printed30–59）全部文字，视觉核范围内全部Figs5–21、Tables2–3与Eqs27–32。精确范围为§3全部、§4及4.1–4.3全部、§5全部、§6/6.1/6.2全部、§7引言/7.1/7.2全部、§7.3在PDF46的开头（跨PDF47部分由root续读）。不是整篇69页已独立全读。先写`source-entry-primed.md`再开本轮assignedbody；046已看PDF1/5/6，不声称盲测。

原件身份：T.Bengtsson/I.Ragnarsson1985, *NPA436*14–82, DOI10.1016/0375-9474(85)90541-X。直接body为`tmp/day24-bengtsson1985-046/attachment-object-response.pdf`，69页，4596459B，SHA256`605e785734279f1a7a6dfd234f1d3ff6b136f983b134ccf9d6b766f3b027d6b8`。本轮文本/renders只在`tmp/day24-bengtsson1985-continuum-applications-049/`，没有联网、producer、未知附件或旧114，无canonical/raw/Git/course/session修改；同一Day24，不开Day26。

## 本轮真正关闭的应用层问题

1. `J^(2)_eff`、`J^(2)_yrast`和`J^(2)_band`来自不同的transition集合/实验对象；unresolved bump或correlation valley不能被升级为已解析的同I双带。本文用明确公式和Te/Pd/Ba/Xe例分开这些层。
2. “fixed configuration”在本文按`N_rot`和signature的**组别占据数**定义；同组内实际轨道仍可更换，故固定组态内仍可有band crossings/backbends。只固定π/α的yrast envelope又是另一条路径。不能把保持一个粗组态标签误作保持一条相干band wavefunction。
3. alignment/crossing既不必伴大shape change，也不必带来较小J^(2)。变化取决于**填入与挖空两轨道的响应差**、形变与total-energy竞争。Au约40的多粒子alignment未出大shape跃迁，Ba例反而增加J^(2)。
4. 原文实质保留了失败/限制：Au noncollective cascade终止spin理论较实验高；c3有较大interpolationerrors；Te Fig18不同插值曲线不重合；Pd是邻核平均、相对band能依赖j-shell位置，理论15–24与引用约26仍有差别；Xe minimum-based最优与惯量支持的collective路径不能合成唯一已证形状。

这些是CNS高spin no-pairing应用的source-grounded合同/作者判断，不是2022 PROBMO复现，也不是本任务新实验或新拟合。本文187Au历史组态c1/c2/ph1等不等于现代GU22 Band2/3；不迁移现代δ或模式标签，不因此逆转用户既有Au校准。

## 方程与连续谱的观测对象

PDF17/printed30 Eqs27–28：

\[
J^{(1)}=I\left(\frac{dE}{dI}\right)^{-1}=I/\omega,
\qquad
J^{(2)}=\left(\frac{d^2E}{dI^2}\right)^{-1}
=\frac{dI}{d\omega}=J^{(1)}+\omega\frac{dJ^{(1)}}{d\omega}.
\]

这是本文I/ω单位约定，数值惯量以ℏ²/MeV给出；不能混入另一paper的finite-spin prescription。within one rotational band定义`Jband`；对many bands/cascades平均可定义所有deexciting E2贡献的`Jeff`，而`Jyrast`仅允许yrast states。作者说`Jeff^(2)`可由unresolved spectra取得，`Jyrast^(2)`需要resolved spectra；correlation valley宽度敏感于同一band相邻transition能的间距，从而约束`Jband^(2)`。valley fillings可有许多近同能transitions/backbends的贡献，不给逐条line pairing。

PDF26/printed39 Eq29与PDF46/printed59 Eq32：

\[
J^{(2)}_{\mathrm{orb}(i)}=\frac{d\langle j_x\rangle_i}{d\omega},
\qquad
\Delta J^{(2)}_{\rm band}=J^{(2)}_{\mathrm{orb}(k)}-J^{(2)}_{\mathrm{orb}(i)}
\quad(i\to k\ \mathrm{particle\! -\! hole\ excitation}).
\]

Eq32用本例相对稳定形变下的轨道响应作估计，本文再与详细band计算核；不自动纳入任意large shape change、pairing或混合。

PDF40/printed53 Eqs30–31，N(Eγ)为能量低于Eγ的stretched-E2 transition数：

\[
J^{(1)}_{\rm eff}(E_\gamma)=4N(E_\gamma)/E_\gamma,
\qquad
J^{(2)}_{\rm eff}(E_\gamma)=4\frac{N(E_\gamma+\Delta E/2)-N(E_\gamma-\Delta E/2)}{\Delta E}.
\]

PDF41/54回述Ref16：theoretical Jeff取四条π/α cascades的平均，并smear近似实验resolution；引用rare-earth Jeff上升与计算very-deformed shape的上升相关。这是模型/实验间的相关解释，smearing、transition集合和cascade平均的依赖必须保留。`Jeff≫Jband`可反映band结构rapid change、不同band近同能transitions计入Jeff；不能把二者数值相等与否变成单一几何形状判据。

本任务推导提醒（非原文新增模型）：由Eq28看，J^(2)是E(I)二阶导的**倒数**。Fig6/14/16/19还减去了`a I(I+1)`参考，读曲率必须加回参考的2a，不能将图上残差曲率倒数当absolute惯量；负残差曲率也不自动表示negative physical J^(2)。作者图注提供的曲率示例以其完整convention为准。

## 187Au：形状/旋转轴/组态与crossing不能混为一层

§4 PDF17–30/30–43的核是**187Au,Z79,N108**（Fig5/6/Table2直接视觉核），不是157Au。低spin shape coexistence与high-spin两cascade是作者引Refs43–45的历史实验/particle-rotor语境，本轮未独立读原实验；与现代GU22命名无自动对应。

PDF19/32：低spin odd-particle轨道不同可伴different equilibrium shape；positive-parity d/s或h11/2一侧较小near-oblate/triaxial，lowesth9/2偏larger prolate，作者以[5411/2]的slope解释。最低i13/2 [6601/2] strong-prolate激发组态作者明确说当时**no experimental verification**。π−/α+1/2 surface存在positiveγ collective与γ约−75至−120°、ε约.10–.20的small-collectivity minima，可存至约I50；低spin collective侧ε约.20，随spin缓增。particle-rotor不区分60°sector，而cranking下γ<−60°关联绕smaller axis旋转；这一sector/axis差不能当作新形状的直接实验测量，更不能把γ符号单独当chiral handedness。

Table2 physicalPDF21/printed34明确固定各p/n的`N_rot,α`组占据，且分别给p/n及totalπ/α；不是全ν轨道固定。图7在I32.5+将c1/c2/c3/c4/ph3各自单min的smooth surface与全部(+,+1/2)组态竞争的surface并列，作者认为前者插值更可靠。相应fixed-coarse-config内仍有不同single-particle orbitals穿Fermi surface，故§4.1开头就说**这些fixed configurations的backbend仍对应其内的band crossing**。

Table2的逐组占据字面可回原页；本轮读取了全表并保其schema，未将c1–ph4重新命名为现代实验bands。核心对照为c1（p:2h9/2+1i13/2，n:10i13/2）；c2/c2′（p:2i13/2+1h9/2，n:9i13/2，差第九n的signature）；c3再占一Nrot7neutron；c4为更strongly-deformed配置；ph1–ph4是另一小collectivity侧。这个shell描述是原文近似j归属，仍以Table2的shell/signature计数为严格标签。

PDF23–27/36–40主线：Fig9在`ε=.24,γ15°,ε4=.05`展示p/n routhians，横轴有Strutinsky renormalization；只有deformation合适时作者才期望其crossingω与Fig8 backbend一一对应。c1在I27/40的crossings分别对应firstg9/2(α+)和firsti11/2(α−) neutron；c2′约ℏω.4、c2约.5MeV的firstg9/2填充不同；c2′第二约I45、ΔE1.2MeV由h11/2p挖空、secondh9/2p填入。c3的Nrot7填充增大deformation并改变crossings，I约40是本应backbend但**插值算成upbend**的明确例；h9/2/h11/2 p crossing频率随shape很强，在I30–50 equilibrium不靠mesh时误差较大。这是输入/网格与assignment交叉检查的直接source警示，不是新实验backbend。

同一模型在I约40有νj15/2、νi11/2、πh9/2近同时alignment，使E(I)的上升变缓，但insert显示无drastic shape change：ε/γ逐渐增加，I15–20约γ10–15°，I60约25°。c4 strong-deformation `ε≈.47,γ≈0°`约I60成yrast；I40时约高1.5MeV。两min间barrier不高，但作者因组态很不同推测互衰变受hindrance；**未计算或测得decay rate**。大I60难观测是作者1985展望，不是当前可达spin断言。

collective c1/c2/c3的典型`Jband^(2)≈40`，`J^(1)≈80`（I20–40，后更大）；strongc4的`J^(1)≈J^(2)≈115`接rigid value。高度aligned routhian近直线可带来大spin而orbitalJ2小；别把大total I/ω等同大dI/dω。小collectivity侧（Fig10 `ε=.179,γ−101.6°,ε4=.045`）Δℏω约.5MeV只增数单位spin，Fig6b大曲率对应smallJ2；Fig11 `ε=.113,γ−120°`的slopingFermi surface展示pure-ph与slightlycollective j-shell填充。fully-aligned prolate终止态的例Iπ31.5−、41.5+、45.5−；正文后页在比较gamma-vibrational I±2时又举41.5−/39.5−，本任务不静默将这两个独立原字面合并为同一标签。基于纯cranking这里只找到fullyaligned态关联的I−2而非完整I±2；不把此限制写成实验中禁止I+2或已识别gamma振动。

PDF29末–30首/42–43还以所引Ref49的couplingscheme解释prolateph：维持ε/ω近常数时rotation可补偿quadrupole破坏sphericaldegeneracy。Z79可看作Z82三holes，N108相对由i13/2/h9/2/f7/2组成的“N114core”有6–8holes。所引quasishell-energy图在`ω/ω0=.75ε`、ε约.11使p79/n108各有约2–3MeV gain、合4–6MeV；本文slopingFermisurfaces又倾向`.6ε`。这些是特定core、shape和approximateoccupation的模型解释，不是可迁给Ce的core定义或实验shell-energy测量。

§4.3 PDF30/43对照保持差异：Ref45“oblate”cascade只见至I30–35，prolate至50–55；模型noncollective侧预计至40–45，作者称minor difference，仍保偏高。邻186Hg至I20两带只称qualitative，忽略pairing使quantitative比较排除。作者提出两个coupling schemes的total decay time和g-factor可能不同：collective侧p spin低ω已15–20并维持至I40–50，小collectivity侧p spin在I<30约5–7、I30–50约10–12。**这些是可检验预期/作者解释，不是本文新τ或g测量，也不提供现代Au band身份。**

## 158Yb/158Er：signature近简并可由终止组态产生

§5 PDF30末–36上/43–49：在no-pairing、deformation不过大、近j-shell归属有效时，固定部分填充给maximal spin；valenceparticles终止偏oblate，valenceholes可prolate。20Ne d5/2²p+d5/2²n最大8是概念例，不把pure-j近似当所有mixedNilsson态严格定理。

Figs12–15给158Yb以及158Er终止路径。158Yb`π[(d5/2)^−1(h11/2)^6d3/2]ν[(f7/2h9/2)^4(i13/2)^2]`一signature终止47+，另signature可到48+；158Er相关终止53−。本文模型显示shape向γ60°/ε约.1–.12发展，spin接近上限时每spin能量代价可变小，残差E(I)发生负曲率；40–50若干终止态比低spin smoothtrend低1–1.5MeV。Ref52/53引用158Yb约700–800keV几乎恒定yrastcascade，作者以一个I36终止、约yrast上100keV的candidate比较；不是本模型已复现每条resolvedline或唯一assignment。

最高d5/2轨道两个signature在沿途几乎degenerate，onehole产生的两bands可一路little-signature-splitting至终止。Fig14终止47+/48+的例具有同配置但d5/2hole signature不同；不是sameI chiral pair，也不是能量近简并即staticchirality。Ref54所引Yb M1 bump仅**tentatively observed**，本文说这种band可能负责是speculation，不能升级为测得M1 strength pattern。

Fig15按人工构造路径联合变ε/γ/ε4/ω：先静态prolate到ε.17，再固定shape加ω到.05ω0，然后随γ走向oblate并增ω，最后γ60°下ω/ω0=.64ε趋回spherical。它是用于解释终止/degeneracy的single-particle路径，非实验时间轨迹；shell-effect比较引用Ref49，非独立数据验证。Fig14 I60的`ε=.39,γ26°`stronglydeformed与pure-ph竞争也是模型，不与Fig12某一终止branch合成同条band。

## 118Te：E2 bump可支持集体分量，但未解析四条cascade

§6.1 PDF36–40/49–53将Ref55的输入I约30→55、unfolded γbump>1.2、upperedge约2.3MeV且mainlyE2作为实验现象。作者模型为I≤约30多oblate/ph、30–45 collective、≥45 collective与pureph混合；这解释bump的作者论证不是观测到每条图16band。作者现算显式含microscopicε4，而Ref57只计其liquid-drop作用，κμ也不同；averageyrast behaviour相似不能冒作两个完全独立参数预测或证明精细band鲁棒。

Fig16 I20–60能量减`.011I(I+1)`，π/α四条yrast的每个spin及可成yrast的band；I40最favoured(−,1)约低其它.5MeV，shape约`.24,8°,.03`，与Fig17只“nearby”的`.253,−3.4°,.011`不可当完全同一shape。p52/n66 gaps与n从Nrot5向4 deexcite构成作者的favouredconfiguration解释。Fig18画同一(−,1) yrastcascade与延拓`πh11/2²νh11/2⁵`，I33–45不同插值带来的不重合直接用作计算uncertainty示例。延拓该band不表示实验继续观测到。

模型的I40附近collectivebands普遍ε.23–.24、γ0–10°、πh11/2²及νh11/2⁴–⁶。近pure p state`g9/2^−2 g7/2² h11/2²`上限Ip24；neutron主成分的上限22/26，使bands约最多45–50。作者强调即使能量代价升高，当前bands也**无真实朝pure-ph γ60°终止的趋势**；本例“spin-capacity近上限”不自动等同observedtermination。到约I50占firstνi13/2，shape向`.30,30°`，backbends把ΔE维持2.2–2.3以下；图中51+→49+约1.85MeV、53+→51+约2.2MeV是**计算跃迁**。作者称可自然解释1.2–2.3MeV bump，同时明确更高spin离散谱与γγcorrelation会是severe tests，不能说这些检验已完成。

I35–45模型J1从约50→40、Jband2约其半且随spin小降，与一个bump上边缘的观测同源比较不计多份独立约束。§6.2随后定义Jeff正是为避免把bump直接作single-bandmoment。

## 106Pd：邻核平均与二阶导敏感性

§7.1 PDF41–43/54–56，原件图19/20为**106Pd,Z46,N60**；引用Ref58实验是它及若干邻核结果。valley至(ℏω)²约.8MeV²（ΔE约1.8）：.1–.3区Jband2约20→35，.4降至约23，.6回35，更高约26。第一升与已观测低spin firstbackbend前惯量变化关联。不能将上述width反演数值当已逐条解析106Pd同Ibandpair。

模型πg9/2四holes给Ip12；νh11/2计数1/2/3的favouredalignedneutronstates分别最大16−、22+、25−/26−，与p合成总终止34+、37−/38−near-yrast。高spin跨Z50的p excitations驱正γ；Fig19标h11/2p与g9/2→g7/2 crossing在I30–36。图注明确nearπg9/2⁶ bandtermination的irregularities**not numerically significant**，不得物理解读波动。

I≈20作者才说no-pairing calculation“might become realistic”，不是通用阈值。模型νh11/2²dominantband J2约27，接近终止时≥30；I>30接νh11/2³再到πh11/2¹branch。后者J2约15–24，引用最高spin约26；作者只称generalagreement，不抹掉差异。PDF43末明确两边大uncertainty：实验many-nucleiaverage；theory relativebandenergies强依赖各j-shell准确位置；withinband较stable仍因J2为secondderivative对small rotationalvariation敏感。它直接限制由一条数值惯量回推唯一shape/configuration。

## 128Ba/122Xe：同粗标签可以隐藏g9/2holes差别

§7.2 PDF44–46/57–59 引Refs59/60：128Ba的Jband2约40ℏ²/MeV在ℏω>.45，至最高约.62略增；122Xe在.45–.65约25。作者以γsoftness和不同shape讨论，但保模型张力：**该参数集算122Xe多数yrast在noncollectiveoblateaxis**，同时有near-yrast/triaxial`.25,30–40°`及prolate`.29,0°`minima。粗标签均约`πh11/2^(1,2)νh11/2^(4,5,6)`，细看triaxial无πg9/2holes、prolate有twoholes。作者依据measuredJ2比较倾向I20–30为triaxial无holes configurations；不是实验直接测得零holes，更不能把三个minima混成已知同一态。prolatebands在ℏω>.7因alignment趋完成J2下降；该解释与Te小J2现象相容仍为modelcomparison。

128Ba ε≤.27的collectivebands算J2≤35，不能解释quoted40；largerprolate ε≈.34 branch算I>40成yrast，在I24仅高.4MeV。Fig21代表形状为`.33,1°,.058`，**不把正文近似.34静默改写成图的.33或反向**。pZ56与nN70/72附近低density，πh11/2²/³、νi13/2⁰/¹/²为所研究groups。占据/挖空轨道的curvature是关键，不能说“高j填入使J2必降”。

Table3 physical46/59在ℏω=.6MeV给neutronJorb2（ℏ²/MeV）：

| orbital | signature α | Jorb2 |
|---|---:|---:|
|[541 1/2]|+1/2|2.0|
|[541 1/2]|−1/2|1.5|
|[523 7/2]|+1/2|−4.5|
|[523 7/2]|−1/2|−2.0|
|[660 1/2]|+1/2|0.5|

最后一行OCR漏掉，但视觉清楚是**0.5**，正文只说i13/2“essentiallyzero”，不能抄成literal0。在本shape/ω条件下，[5237/2]+→[6601/2]+ Eq32为0.5−(−4.5)=+5，这个仅为原表两项减法不是本任务新模型。类似p[4201/2]挖空至thirdh11/2也可增加J2。详细band计算给`πh11/2²νh9/2²`约35、`πh11/2³νh9/2²`约38、`πh11/2³ν[(h9/2)²i13/2]`约40；作者称reasonableagreement，非3个新的独立实验点。最后对130Ce的largedeformation/highj→J2increase作预期，并引Ref63说largeJ2被见；§8.4具体discretespectrum另由root读，本单元未抢先认证。

§7.3本单元只读physical46结尾：valleywidth之外fillings/disappearance也含信息，manynear-same-Eγtransitions可fillvalley，后句跨页。没有将PDF47下文或整节判据记为已读。

## 全部范围图表的视觉审核索引

| 图表 | physical / printed | 内容与应保的读取合同 |
|---|---|---|
|Fig5|18/31|187Au π−α+1/2 surfaces，I4.5→54.5；1MeV contours/dotglobalmin，两个couplingsminima可至约50；不是实验shapemap|
|Fig6a/b|20/33|同核collective与small/no-collectivitybranches，减`.0056I(I+1)`；b圈为γ−120°prolateterminatingstates；c/ph标签按Table2|
|Table2|21/34|p/n各`Nrot,α`组计数，totalπ/α；粗固定config不是每轨道固定；c1/c2/c2′/c3/c4/ph1–4都为模型|
|Fig7|22/35|I32.5+ c1–4/ph3 fixedsurfaces与(+,+1/2)总surface，min值5.3/5.6/6.3/7.9/4.7MeV，combined4.7；不据well数数实验bands|
|Fig8|23/36|Au I vsΔE，π/α组人为纵移20ℏ；仅(+,+1/2)c1–4纵轴absolute有效，不能从图的高ordinate误报I100|
|Fig9|24/37|Au routhians `.24,15°,.05`；Strutinskyrenormalizedω、p/nspin与Nrot/signature标注，合适shape条件的一一crossing对应|
|Fig10|28/41|Au `.179,−101.6°,.045` routhians及ph占据；非Fig9同shape|
|Fig11|29/42|Au `.113,−120°` ei vsmi/slopingFermisurfaces；实线pureph、虚线slightlycollective，非实验levelscheme|
|Fig12|32/45|158Yb fixedterminating config I15→47+ surfaces；α=−1到47，α0换d5/2holeprojection到48+|
|Fig13|33/46|158Yb47+/158Er53− shapetrajectories，Ip21/20；另Fig15的构造path；非timecourse|
|Fig14|34/47|158Yb energy减`.0086I(I+1)`；36+(及42+)candidate、45−/47+/48+termination、I60largeshape/ph竞争；caption保candidate措辞|
|Fig15|35/48|人工jointε/γ/ε4/ω path，沿程d5/2hole两signature近degenerate；末ω/ω0=.64ε，不能据此认证chirality|
|Fig16|37/50|118Te四π/αyrastenvelopes及可成yrastbands，减`.011I(I+1)`，圈alignedγ60°；不是bump已分出这些bands|
|Fig17|38/51|Te nearbyshape `.253,−3.4°,.011` routhians；ω0处asymptoticlabels，不与I40min完全同shape|
|Fig18|39/52|Te(−,1)yrast与fixedcollective延拓，I33–45两条因插值不同不重合；~I50另branch两yrasttransitions|
|Fig19|42/55|106Pd E减`.0013I(I+1)`；不画(+1)highbands、圈aligned；πg9/2⁶termination处irregularity不具numeric意义|
|Fig20|43/56|同Pd shape每4ℏ；37−/38−相似轨迹仅画一个signature；缺线非证明无partner|
|Fig21|45/58|Ba区 `.33,1°,.058` p/nrouthians、IpZ56/InN72，N70/72gaps；图与Table3同conditionalcontext|
|Table3|46/59|五行Jorb2原值已完整抄表，上文；不能把0.5略写为0后又精确算差|

范围内numberedequations只有27–32，均已视觉核并在上文保定义；所有图表均已逐页检查，未pixel-digitize每个曲线点或把未给errorbars的modelcurve补成数据集。引用实验数值只是本文转述，本轮没有独立读取Refs38–63等原件；来源依赖而非新增独立证据。

## 133Ce/Day24 可用的最小增量与未关闭项

可迁移的研究合同：先区分resolvedband、yrastenvelope、all-E2cascadeaverage、correlationvalley和quotedcentroid/bump；保π/α、Nrot/signature计数与具体轨道/holes；crossing同时查shape与single-particleω轴renormalization；报告mesh/interpolation、pairing忽略与secondderivative敏感性；g/τ等预测须独立观测才算新约束。同一γ/energy/proximity可有aligned、terminating、differentholes等替代机制，不能单靠近简并或粗组态断定chiral/vibrational/staticpartner。

未关闭：WK22 actualκμ选择、basis/blockedstate/BCS、producer版本、ε/λ共同零点、coherentsignedRME、现代bands身份与实验Cov；本篇不因引用链就解决这些。128Ba/122Xe/130Ce历史高spin应用能提供比较逻辑，却不把N=Z轻核参数或这里heavy/A130数值直接移至odd133Ce。root后续PDF47–69及048methods可补完整source；本单元已覆盖所分配全部主线，不独立宣告全篇完成。

停止原因：指定30页、全图表/方程已读核，source身份无新增问题；进一步离散130Ce或methods属于父任务分工，保持下一读区边界，不用toy/test制造增量。
