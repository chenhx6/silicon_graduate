---
type: research-note
title: "偏振计数的共同几何校准与参考线比值设计"
aliases: [shared geometry calibration in polarimetry, P A Q count design]
created: 2026-10-19
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: daily-learning-Day17-L3-design
evidence_sources: [starosta-1999-pdco-experimental-test, schmid-1998-gammasphere-polarization, garnsworthy-2019-griffin-facility]
promotion_target: ""
tags: [polarimetry, calibration, covariance, experimental-design]
---

# 偏振计数的共同几何校准与参考线比值设计

## Research Trigger

[[starosta-1999-pdco-experimental-test]] 原 printed18 Eq3/4（ST99-14）定义 clover 的散射计数不对称度和无偏振几何校准；[[schmid-1998-gammasphere-polarization]] printed100 Eq13、printed101 Eq15/16（SG98-4/13）给双分段的另一种估计量。两文均由已知偏振参考的 A/P 标定 Q，均未提供可恢复全部共同校准依赖的原始计数与 Σ。这里保存可复用的联合计数设计和一个改分母反例；这是本任务推导，不是两篇论文直接报告的新实验结果。

关键问题是：同一个无偏振样本校准 a 或 η 后，同时用于参考 A_r 与目标 A_t，怎样计算 P_t 的误差？只分别列 σ_A 与 σ_Q 不足以回答。该问题直接影响 matching-reference 的 δ/EM 判据，值得持久化，但尚未验证任一实际实验的完整统计模型。

## Grounded Evidence

### P/A/Q分层与原件输入

| 层 | Clover：ST99实际定义 | Gammasphere双分段：SG98实际定义 | 需要另行测量或核验的输入 |
| --- | --- | --- | --- |
| physical P | 电场在反应面内减面外的强度差/和，printed17 Eq1 | J0−J90 的差/和，printed99 Eq5 | 指定自旋、布居、方向、gate、纯度与相位；不是 Compton 散射计数本身 |
| measured A | (aN⊥−N∥)/(aN⊥+N∥)，printed18 Eq3 | (ηC−S)/(√η(C+S))，printed101 Eq15 | 原始/拟峰计数、背景与事件复用；C须含两侧confined及side-ADC-zero |
| null response | a=U∥/U⊥，printed18 Eq4 | η=Su/Cu，printed101 Eq15后定义 | 同能量、阈值、门和arrayweights的无偏振样本；null不能单独确定Q |
| polarimeter Q | Q=A_r/P_r；原NORDBALL单clover向EUROGAM移用有边界 | Q=A_r/P_r；三pureE2参考的P来自AD/Eq6 | 已知P_r及其误差/响应；几何、阈值与参考选择必须匹配 |
| angular Q_k | 与上述标量Q不等同 | 与上述标量Q不等同 | 角关联有限立体角的逐rank response，不由polarimeterQ补齐 |
| F与ε | 单次接受计数或绝对效率的分母需声明 | Eq18用photopeak ε，传统Eq11用coincidence ε | 曝光/入射或发射光子、deadtime和背景；裸F不提供beamtime排名 |

ST99 Table1 的 Ba参考P由上游AD而来，Cd/Sn CE参考P由GOSIA而来；这些不是本篇独立直接测到的P。SG98同一calibration的A/P/Q三列不是三个独立实验。ST99的10⁻5指数/脚注勘误和SG98的294-keV印刷closure边界仍按原source保留，本设计没有修复它们。

## 跨装置observable-response合同矩阵（Day17整合）

这张矩阵把本session已读原件与当前canonical claim逐行对照，初版十行后续加入Bass1972。JO95等部分条目继承旧日原读/priming，本次只核其已有atomic页，并不重称新实验或全文阅读。所有下列核偏振P、计数、Q都按各行对象定义；“相似差和式”不等sameevent。原needs_review/human前缀不因矩阵晋升。

| 原件与locator | 实际计数/定义 | 相对零点或效率输入 | P与分析能力输入 | 效率/merit与不可裸迁条件 |
|---|---|---|---|---|
| [[ewan-1969-single-geli-polarimeter]] EW69-D17-1/2/11 | 单planar晶体转两orientation的fullpeak；Qraw=2A | 16cm下两orientation角接受校正，非两个absorber | Qcorr=2A/P，通常A/P=Qcorr/2；印r可为(1+p)/(1−p)，不是boundedp | 全能峰photoelectric稀释未知；oldP>1failure解释已撤回，原作者命名/body仍边界 |
| [[twin-1970-polarization-angular-correlation-40k]] TW70-D17-1–4 | GeLi+2NaI的sumpeak；ψ82是Compton角，θ为emission | θ0null校analyzereff | R另finitegeometry算/Ar1460检查；R.21(.02)归2231keV | Eq中的核Qk非R；不同角/几何、null与knownP不能互换 |
| [[butler-1973-three-geli-compton-polarimeter]] B73-D17-1/2/3/6 | sumfullpeak N；A=(aN⊥−N∥)/(aN⊥+N∥) | unpolarized56Co/66Ga给a≈1、1%accuracy | 原P=A/Q，无额外alphaA；P由knownEM/AD预测、A同测 | independenta层不使P/A/Q同链独立；parentEx2935不等Eg967 |
| [[logan-1974-generalized-polarimeter-merit]] L74-D17-1–7 | N=T−B，两orientation各t；目标σA/A | Eq2等价独立VarB=B，不是任意fitΣ | 线性knownQ，Table977 ε任意1.6/1.0、S1.3/.2 | M backgroundfree=εQ²/[2(1−Q²P²)]；εincidentfullE/time2t，P0relative目标不定义 |
| [[jones-1995-clover-compton-calibration]] JO95-5/6/7 | Cloveradjacentcrystalcount；A/a在两配置测 | 0°Clover定a、90°测A，addback作ADmonitor | coaxialAD/STAG/finiteangle推P；Q′(B+CE)，C0±.003/MeV | 原F=Q²Nsum为countF；相对NaI效率不是N或absoluteε，thresholdscan共享事件 |
| [[garciaraffi-1995-nonorthogonal-compton-polarimeter]] GR95-D17-1–9 | 效率归一两count，pointQ3=0；0/60 A=QP/(1−QP/3) | unpol只校offset/eff比 | extendedalpha沿point为作者假设；未知Q1/Q2需两knownP或actualchannelresponse | Fig3同POLmodifiedMC非实验；MsmallP含4f/(1+f)²，不迁finiteP/含背景time |
| [[schmid-1998-gammasphere-polarization]] SG98-4/5/7/8/14 | C含两侧confined含sideADCzero，S为shared；A=(ηC−S)/(√η(C+S)) | η=Su/Cu，必须samecut/arrayweights | pureE2AD给P再A/P校Q，Eq13前提确保linear | 双分段ε为photopeak，传统ε为coinc；Fig9eta130门不移Fig10/Pb60门，294closure不调η强配 |
| [[starosta-1999-pdco-experimental-test]] ST99-6/7/9/13/14 | CloverA与四groupPDCO/RDCO复用主采集 | individuala与poola及target权重需匹配 | Q外采NORDBALL移EUROGAM有域；7(2)×10^-5/keV；known647路径取alignment非独立prior | integratedP不是第六独立点、Q不补jointresponse；旧D96勘误保持，490两candidate未独断 |
| [[schlitt-1994-sectored-compton-polarimeter]] SC94-D17-1–8 | corefullE＋outersector两hit/另两veto给H/V | unpolCoa=.9899(.0052) | Pd622tag/512probe、actualP98%不同nominal1；部分AD/P共B73 | εrelative=(H+V)/Nscorepeak，F用absoluteεcoinc@25cm；150门4438Q7.93非总述未标门9.5 |
| [[vonderwerth-1995-compton-polarimeters]] VW95-D17-2/4/5/6/9 | POLALI有Es/E′/knownrole；MINIPOLAsector只timing＋共同E，orderunknown | unpolarizedRa校groupa，两geometry/pairgroups另列 | Q=Aexp/Ptheor；apertureΔφ拟Q非独立验证，近287/288需Ge产品身份 | εc=(Nsum/2Ns)ε_abs_single；新algorithm不补actual未记录E，crosstalk/损伤有原run域 |
| [[bass-1972-two-crystal-compton-polarimeter]] BA72-D17-1/2/5/6 | N=nco/(nco+nanti)，两旋转fraction再构Qsource；R是分析能力 | 同采集co/anti和四rotations平衡，仍有geometry/gain/cuts域 | Pref来自AD或双Compton，Rσ仅stat而未含Prefσ | source相对merit=R sqrt(Nbar)，不能将fraction换odds或以Nbar作absoluteε |



### 三种“能消零点”的信息仍不同

无偏振源或axisymmetry下θ0null可以约束探测效率比/offset；它本身不给knownnonzeroP下的分析能力。KnownEM/AD/γγtag提供的是另一层P标尺，但这个标尺也有sameparent、门、有限接受、核布居与phase依赖。若A/P/Q由同一calibrationchain派生，增加表列数不能增加独立实验。

有界偏振度p与强度比r的精确转换也不是新的物理信息。EW69的可行ratio解释修订了本session的错误failure判断；保持数学字典与历史作者意图取证分开。SG98改分母产生非线性、GR95真实nonorthogonal分母、B73误转额外项，是三个不同对象，不能因为字式相近便互相取消或移用。

### 哪个新输入最可能改变当前判断

| 待补实际输入 | 直接改变的判断 | 现有材料为什么不能替 |
|---|---|---|
| 同energy/门/threshold/arrayweights的unpolarizedledger | 零点和a/η迁移是否有效 | source名或pool a≈1不认证targetgateweights |
| reference的核P合同及AD/tag/response联合Cov | Q是否有独立标尺，targetP误差与calibration是否共享 | “knownE2”只给多极性，未必给制备取向/finitegeometry或δ/Jπ唯一性 |
| actualtarget/reference C/S或N⊥/N∥的净面积、背景model与共享Σ | P/δ分支显著性是否能量化 | √area不是一般peakfiterror；marginal表列不能恢复fullCov |
| 两不同knownP或逐channelStokesresponse（当alpha未独立固定） | 非线性响应Q1/Q2是否可辨 | null+一个非零P只约束一个组合，不能证明extendedpointalpha |
| 同source曝光/absoluteε/接受角与事件唯一性 | F/merit能否转成时间、能否跨仪器比较 | relativeNaI、conditionalcoinc及countF不是同分母，sharedcuts不是independent点 |
| 实际readout/ordering/threshold/完整producer与runstate | 公共数据是否足以重放所需选择 | 公开算法不能补未记录segmentenergy、原modifiedtransport或neutrondamage状态 |

这里的nextinput不是用户待办；在本日授权范围内有公开producer/data时继续寻找，没有时保readiness而不造实验CI。Psign与Jπ/δ/形变的裁决仍需samecascade的spin/AD/DCO/寿命/转换系数等companion；多测一项correlation也可能像TW70的770–1159一样不增辨别信息。

### 130Cs：把通用响应合同应用到四条实际link

[[simons-2005-130cs-chiral-structures]] SIM05-D17-1–12的本session原件复核，把A≈130的结构指认接回具体测量链；不是从通用矩阵推一个新的核指认。原13页完整text/关键visual核读，旧摘要是priming，旧flags保持。printed543 Eq3给P=A/Q，Q引用printed552 Ref17 [[jones-1995-clover-compton-calibration]]；本文未印本campaign实际Q曲线/阈值/a/逐晶体权重/原峰面积/Σ。JO95-4/6/7的标定recipe有域，不能凭器件同族补成这些输入。Eq3不显式a不等于实际a=1或证明遗漏处理。

| 初态到末态（Fig1/Table身份） | γ keV | D gate RDCO | Q gate RDCO | physical P（原列） | 原mult |
|---|---|---|---|---|---|
| A3380 16+ → B3083 15+ | 297.1(.6) | .62(.05) | 1.0(.1) | −.15(.10) | M1/E2 |
| B1507 11+ → A960 10+ | 546.7(.2) | .9(.3) | 空 | −.2(.1) | M1/E2 |
| B1908 12+ → A1313 11+ | 596.1(.3) | 1.0(.1) | 空 | −.1(.1) | M1/E2 |
| B2630 14+ → A2019 13+ | 609.2(.5) | 1.0(.4) | 空 | −.2(.1) | M1/E2 |

D/Q在这里是Table的门类型，不是两个polarimeterQ。四中心/所印sigma绝对比1.5/2/1/2仅描述误差规模；sharedQ/事件/gate/背景Σ未知，不能相乘独立概率或造jointsignCI。作者以DCO、P、levelmap及bandA prior解释sameparity和共同unique-parity配置（printed545），后者不是单由Psign得到；chirality另依赖Fig4–7/模型且无absoluteB。

同母态两photon支路、δ=E2/M1时，若原相对强度确可用作积分photonbranch，则

\[
R_{M1}=\frac{B(M1)_{\rm in}}{B(M1)_{\rm out}}
=\frac{I_{\rm in}}{I_{\rm out}}
\left(\frac{E_{\rm out}}{E_{\rm in}}\right)^3
\frac{1+\delta_{\rm out}^{2}}{1+\delta_{\rm in}^{2}}.
\]

这里共同parent寿命/任意公共强度归一取消；没有额外乘totalICC，因为I是photon分支代理、M1 component由1/(1+δ²)分配。若拿totaltransition intensity则须先回到photon，若I带门/各向异性接受差也须先补响应，不能无条件采用。原Table caption说relative151，但I151=53.4(16)/I408.86=100(3)（SIM05-D17-8）如实保，公共尺度差不影响以下中央比，却不能替代实际efficiency recipe。

| 同parent | Ein/Iout keV | 条件δin=δout=0的R中央值 | 原边界 |
|---|---|---|---|
| A12（Ei1603） | 289.7/96.0 | 1.9740946 | out原括号mult，不能升pureM1 |
| A14（Ei2446） | 426.2/165.9 | 0.45703433 | 两原mult均M1/E2，δ未知 |
| A16（Ei3380） | 465.6/297.1 | 0.29446027 | 两原mult均M1/E2，δ未知 |
| A18（Ei4322） | 449.8/286.7 | 0.52330541 | out原括号mult，不能升pureM1 |
| B12（Ei1908） | 401.0/596.1 | 0.79415548 | 两原mult均M1/E2，δ未知 |
| B15（Ei3083） | 453.0/636.0 | 32.840177 | out原括号mult，不能升pureM1 |
| B16（Ei3561） | 478.4/646.0 | 1.2031224 | 两原mult均M1/E2，δ未知 |

这些七行是原Table的中央代数控制，不称作者Fig6全部数值/producer复现；Fig6 A15/A17的lowerlimit仍是lowerlimit，未填成对称点。附artifact还在固定E下对两强度marginalσ给任意相关系数的local范围：R|σin/Iin−σout/Iout|到R(σin/Iin+σout/Iout)，不是实际CI。δ未知时相同P符号不取消(1+δout²)/(1+δin²)，故“同parity支持”不能升级“pureM1 strength已无模型确定”。

本次决定`supports`原四link/配置谱系，`limits`仅用负P与表列ratio的强断言。B带无同样staggering、模型幅度过强、缺partner寿命/absoluteB仍是必要companion。原数据与Bhat2014再比较是同一Euroball谱系；Jones1995是独立reference采集，但引入它不使四link标定误差相互独立。最高信息输入是本campaign逐link gates/netpeak/background/Q/a及联合Σ，未得时不重做实验δ/P/模式裁决。

复算入口`system/scripts/day17_simons2005_link_audit.py`；输入/结果为本run `simons2005-link-contract.json` / `simons2005-link-result.json`。长期科学内容在本节与SIM05 atomic页，outputs只保存本次复算轨迹。

## Provisional Reasoning

### 两个估计量的Jacobian

令 clover 的 x=N⊥、y=N∥、D=ax+y：

\[
\partial_x A=\frac{2ay}{D^2},\qquad
\partial_y A=-\frac{2ax}{D^2},\qquad
\partial_a A=\frac{2xy}{D^2}.
\]

SG98令 n=C+S：

\[
\partial_C A=\frac{(1+\eta)S}{\sqrt\eta n^2},\quad
\partial_S A=-\frac{(1+\eta)C}{\sqrt\eta n^2},\quad
\partial_\eta A=\frac{\eta C+S}{2\eta^{3/2}n}.
\]

对任意真实Σ，先用gᵀΣg传播。以下数字只用事先声明的独立Poisson原始类别计数和独立P_r局部误差；不把源Table3的拟峰误差改成√面积。ST99与SG98的两个分母不同，不能共用一套导数。

## 共同校准如何进入参考比值

只有在同一可适用的Q及匹配物理P下，才能写

\[
Q=\frac{A_r(h)}{P_r},\qquad
P_t=P_r\frac{A_t(h)}{A_r(h)},\quad h=a\ \text{或}\ \eta.
\]

对SG98，参考/目标使用同一η时，√η相消：

\[
P_t=P_r\frac{(\eta C_t-S_t)(C_r+S_r)}
{(\eta C_r-S_r)(C_t+S_t)}.
\]

在A_t/A_r非零的局部区域，

\[
\partial_\eta\log(P_t/P_r)=
\frac{C_t}{\eta C_t-S_t}-\frac{C_r}{\eta C_r-S_r}.
\]

因此共同η误差既不是自动完全抵消，也不是两个独立标定误差；只有额外的相同计数比条件才局部抵消。目标A_t=0时用未除A_t的Jacobian，不套对数式。

等价的A_t/Q传播是

\[
\operatorname{Var}(P_t)=\frac{\operatorname{Var}(A_t)}{Q^2}
+\frac{A_t^2\operatorname{Var}(Q)}{Q^4}
-\frac{2A_t\operatorname{Cov}(A_t,Q)}{Q^3}.
\]

这里Cov(A_t,Q)即使target与reference采集独立也可能因共享U校准而非零。其符号和影响依实际设计；以下正Cov例不证明省略它总会保守，也不补出真实实验Σ。A_r除以它自己回代P_r是恒等式，不能当独立验证。

## 声明设计的计数与定量结果

表中为本session新声明的Poisson均值，非源实验counts；每行内先后类别按表头，P_r也为设计值，不假称一条实际reference。

| 设计 | 无偏振U两类别 | 参考r两类别/P_r | 目标t两类别 | h；A_r；A_t；Q |
| --- | --- | --- | --- | --- |
| clover：⊥、∥ | 500000、500000 | 55000、45000；.5±.01 | 53000、47000 | 1；.10；.06；.20 |
| SG98：C、S | 1000000、160000 | 101600、14400；.8±.012 | 100600、15400 | .16；.04；.015；.05 |

原始六counts/P_r的联合Jacobian给出：

| 设计 | P_t及联合local σ | 错把A_t、Q独立的σ | 新120000次Poisson设计MC的σ |
| --- | --- | --- | --- |
| clover | .300000±.0194486 | .0201951 | .0195646 |
| SG98 | .300000±.0627474 | .0646613 | .0634302 |

clover的variance分量依target/reference/U/P_r为.00024910/.00008910/.00000404814/.000036；SG98依次为.00333887931/.00044340517/.00013469828/.00002025。数字是chosen设计的一阶传播，不是实验confidence interval或detector排名；两个设计的counts/参考P并不等价。

独立推导的条件binomial likelihood使用

\[
p_\perp(A,a)=\frac{1+A}{a(1-A)+1+A},\qquad
p_C(A,\eta)=\frac{1+\sqrt\eta A}{1+\eta},
\]

对参数(log h,log Q,P_t,P_r)构造Fisher矩阵，外加独立P_r约束。其逆矩阵P_t分量与原始计数delta variance一致；它是同一设计的另一数学核验，不是新独立实验。MC有限样本平均轻微比值bias分别为.01483σ/.01248σ，未证明有限样本比值无偏。零/近零A_r、负净峰和有背景问题需要真实likelihood，不能靠本地Gaussian式裁剪。

## 改分母后重标一条线仍会失败

若把SG98改成

\[
B=\frac{\eta C-S}{\eta C+S},
\]

根据原式与C+S守恒，有

\[
B=\frac{(1+\eta)A}{2\sqrt\eta+(\eta-1)A}
=\frac{(1+\eta)QP}{2\sqrt\eta+(\eta-1)QP}.
\]

除η=1或只取局部小A极限，这不是一个与P无关的常数乘P。所以上面的SG98设计用旧Q会得到P_t=.441961；即使用B_r/P_r重新标一条reference，仍得到.291999而非设计真值.300000。这是响应合同被改变的明确反例，不是SG98实验结果失效或新Q校准。

在承认这个非线性forward model后可以用B反演P；问题在于沿用线性A=QP。未来若以新的估计量分析实验，必须同时更新完整forward response和误差模型，不能仅更换分母/参考一点。

## 效率分母、必要companion和失败条件

SG98-14的原文字典需带到任何F比较：printed100 Eq13将N写成source总发射光子，而printed101 Eq18邻文将N_i称incident photons，ε写成photopeak efficiency。必须显式提供N_emitted→N_incident的几何接受/照射定义，或声明incident指整个装置的归一；本文未给可替用户恢复该字典的独立N ledger。不能混用每次入射晶体的本征效率、每发射光子的绝对效率、相对NaI效率和选中photopeak条件概率。纯粹把分母改名不改变观测counts，但改变了F比较的意义。

最小独立校准输入是一条**没有参与Q拟合的、已知P的检查支路**，其方向、布居/门、能量/阈值、background与arrayselection均有可追溯匹配；如P不是直接测量而来自AD/GOSIA，须另带相应误差和模型边界。增加一条同Q拟合内参考的回代点不足以填此缺口。

另需原始U、r、t峰/背景和event-overlap ledger：共享拟合、插值η(E)、多个参考能量的共同参数、P_r的AD校准依赖、gate/finiteacceptance变化均可破坏当前独立Poisson假设。原SG98 Fig9为130keV threshold而Fig10/Pb为60keV；ST99单clover79°校准不是任意EUROGAM/gate的完整响应。这些都必须回原数据，而不是从设计MC估计实际systematics。

反证一是ST99-2的490-keV E2/M1-E2仍多解，说明P/DCO并不保证唯一Jπ；反证二是SG98-9/12的高背景P散布和ADcompanion，说明更多acceptedcounts不自动提高真实结论可信度。P/A号不能独断δ、宇称或shears/wobbling解释。

## Assumptions

定量练习限定单一能量、匹配的阈值/geometry/gates/arrayselection和可共用的线性Q。六primitive类别计数独立Poisson、无背景和事件复用；P_ref具有独立的局部Gaussian误差。这些是设计假设，不是原两篇实验已经满足的已知事实。

## Competing Explanations

真实P变化、未分峰/背景拟合、逐探测器权重变化、阈值/geometry变化和共同校准可造成不同A。当前设计仅隔离最后一项和估计量归一；未用它排除其它解释，也未解释实际294-keV或490-keV未决项。

## Transfer Conditions

迁移前提供明确物理P坐标/自旋与参考身份，及同对象energy/threshold/gate/geometry/arrayweights。若能量不同，Q(E)、a(E)/η(E)插值的共同参数/Σ必须显式提供；不能仅同仪器名称便采用本设计一个Q。

## Failure Conditions

近零参考A、负净峰、未给background/event-overlap Σ、偏振相关总接受度或不同参考/target选择，都会使当前比值与误差近似失去保证。√η取消不认证剩余η取消；不对物理区间外估计作clip或擅加伪计数。

## Falsification or Reverse Tests

完整primitive Jacobian与条件binomial Fisher给同一local variance，MC核有限样本sigma/bias；改分母的非线性公式给明确反例。真正实验验证必须另留未参与Q拟合的known-P支路；与同reference恒等回代不同。

## Open Questions

当前缺真实逐detector/gate的U、reference、target净峰/背景ledger与Σ，以及Q/P_ref/AD的共同依赖。合并detector的a/η/Q迁移条件已在下方新段以原合同和Rational设计明确；实际逐台/gate ledger仍缺，下一核公开producer输入，不用更多同模型MC代替它。

## Human Review

本页为Codex self-audit，未发生用户科学审核；`review_status: unreviewed`。本session的继续/自动执行授权不等于逐claim确认。

## Promotion or Rejection History

- 2026-10-19：从Day17原件阅读与新联合计数设计创建；保持provisional。未晋升为任一实际实验结论，未改原source review flags。

## 可复算与self-audit

输入[paq-design-input.json](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/paq-design-input.json)、[脚本](../../system/scripts/day17_paq_shared_calibration.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/paq-shared-calibration-result.json)保存设计参数、原件hash、全Jacobian/Σ、Fisher和MC。命令：

```bash
PYTHONPATH=/workspace/wiki/tmp/day16-jt74/python-deps python3 system/scripts/day17_paq_shared_calibration.py
```

依赖NumPy/SymPy；该路径是现有repo内依赖缓存，未修改系统配置。首次两个interpreter均缺SymPy的实际失败见同run的`first-execution-failure.json`；不能称首次执行即成功。缓存可重建，核心公式/输入/代码已在持久层；脚本不重放Day16的旧检查。

P1 self-audit：`supports`直接从primitive counts保留共同校准；`revises`只要重标一点就可随便更换A归一的直觉；`limits`F或√count对高背景实际P精度的保证。新分析均为`our-inference`/声明模型、`source_independence: multiple-dependent`、`needs_review: true`；没有新增实验δ/Jπ/P/Q或human-review。晋升待实际matching-response/Σ输入。

## 探测器合并：匹配零点仍不保证一个线性Q

ST99-7/15原printed21/Fig2给所选18台单台a∈[.95,1.05]、合并a∈[.99,1.01]且取a=1；SG98-4/15原Eq13和printed106给12台C/S合并。下面是分析前另冻问题后完成的**声明response模型**，没有原逐台illumination、Q或Σ，不能当原阵列发生偏差的证据。共同物理P（同一偏振坐标、兼容方向和gate）是额外假设；一般array的P_j不同须逐台forward model，不适用以下单P缩写。

### Clover：原始垂直效率权重下的精确合并

取X_j=ℓ_j e⊥,j(1+Q_jP)、Y_j=ℓ_j e∥,j(1−Q_jP)，a_j=e∥,j/e⊥,j。定义w_j∝ℓ_j e⊥,j，归一Σw_j=1；它是**无偏振perpendicular基线权重**，不是总accepted counts或γ强度Iγ。令ā=〈a〉、q̄=〈Q〉、c=Cov_w(a,Q)。若U、reference和target均匹配这个w，合并U给a_U=ā，直接合并原始计数再校正得到

\[
A_{\rm pool}(P)=\frac{kP}{1+\lambda P},\qquad
k=\bar Q+\frac{c}{2\bar a},\qquad
\lambda=-\frac{c}{2\bar a}.
\]

即使A_pool(0)=0，也不保证A_pool/P为常数。若各a相同、各Q相同，或恰好c=0，则恢复线性；这是可检验的充分条件，不是原论文已测c=0。用单一P_r标Q_r=A_pool(P_r)/P_r后，

\[
\widehat P_t=P_t\frac{1+\lambda P_r}{1+\lambda P_t}.
\]

在共同w、a与Q的范围及单P假设成立时，Cauchy–Schwarz与有界变量方差给出Grüss界：c的绝对值不超过(a_max−a_min)(Q_max−Q_min)/4。**额外取0≤Q_j≤1、ā≥.99**，源a范围条件下λ绝对值≤5/396≈.0126263；对P_t、P_r∈[−1,1]且参考非零/response非零，单参考非线性引起的P绝对偏差≤10/391≈.0255754。这是保守数学界，不是实验systematic σ、置信区间或完整calibration预算；若权重不匹配，该界不约束总偏差。

若target为P=0但w_t与U不同，其a_eff仍只是a_j的凸平均，原a_U∈[.99,1.01]和a_eff∈[.95,1.05]给

\[
-1/34\ \le A_{\rm false}(0)=\frac{a_U-a_{\rm eff}}{a_U+a_{\rm eff}}\le3/98.
\]

因此在这些**无背景/同a范围/同选择**前提下，单纯权重迁移不能从P=0生成ST99 printed21的A中央值+.120；它不排其它systematics，不计算实验概率，也不选490-keV的δ分支。

新两台design取a=(.95,1.05)、Q=(.10,.30)、w_U=w_r=(.5,.5)，有ā=1、c=.005、k=.2025、λ=−.0025。P_r=.8、P_t=.3时，matching-w的一点标定给P̂=.2996247；若仅target改w_t=(.9,.1)，P̂=.2792313；此选择的无偏振target也会给A=.0204082，沿Q_r得apparentP=.1005795。数字不是原18台的数据或实际偏差估计。

### SG98：photopeak权重下的线性与offset

每台依Eq13取总photopeak均值n_j对P不变，v_j=n_j/Σn_j；

\[
\frac{C_j}{n_j}=\frac{1+\sqrt{\eta_j}Q_jP}{1+\eta_j},\qquad
S_j=n_j-C_j.
\]

令c0(v)=Σv_j/(1+η_j)、d(v)=Σv_j√η_jQ_j/(1+η_j)。匹配U权重v_u时η_U=[1−c0(v_u)]/c0(v_u)，**不是**η_j的算术平均。用这个η_U处理target，

\[
A_t(P)=\frac{(1+\eta_U)c0(v_t)-1}{\sqrt{\eta_U}}
+\frac{(1+\eta_U)d(v_t)}{\sqrt{\eta_U}}P.
\]

若v_t=v_u，则offset为0且响应严格线性；若权重变，offset通常不为0，同时斜率也变。只校Q不能消除offset。不同物理P_j、偏振相关totalacceptance或不同threshold需要完整response，不能从该式自动认证。

新design取η=(.09,.25)、Q=(.04,.06)、v_u=v_r=(.5,.5)，有η_U=77/468≈.1645299而算术均值为.17，Q_eff≈.0502551。匹配v时reference P_r=.8与target P_t=.3准确回到.3；target改v_t=(.8,.2)则P̂≈2.24579，P=0也给apparentP≈2.01258。所有逐台类别均非负；这些越界估计揭示错误迁移的设计反例，不能clip成物理P=1或称源197Pb结果失效。

### 本问题的核验、复用与停止边界

[array-weight-input.json](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-input.json)、[exact script](../../system/scripts/day17_paq_array_weight_contract.py)、[result](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/array-weight-result.json)保存Rational输入、直接逐台求和与闭式恒等式、P∈{−1,−.5,0,.3,.8,1}的正计数/逐台校正恢复控制。没有额外MC或实际事件；新分析与先前计数MC不计作独立实验。

此代数局部已解决“合并null接近1是否足够”的问题。真正提高原实验判断信息的下一输入是逐detector/gate的基线权重、参考/target共同坐标及Q_j/η_j、背景/Σ/producer。取得这些输入前，不继续扫同一toy或把条件上界当实测校正；可转向实际公开sorting/producer的readiness核验。

### 实际公开producer的后续输入门

[[grsisort-2026-compton-polarimetry-code]] GRS26-1–10已按固定commit/双hash核所选原件并执行原样组件。取得了Compton双hit/第三γ、ξ/θ、10-history mixed和归一consumer的实际路径，但没有真实ROOT/TTree、逐detector reference/targetledger与Σ。源newAnalyze/默认Lean并非同一path；已复现的index/secondF/normalizederror/bin边界需按该版本限定，不外推原ST99/SG98。

当前缺口已从“是否有公开producer”收窄为“能否取得matching actualdata/执行版本和统计结构”。下一个有信息增益的动作是检验对应构建路径、实际settings与输入basis或合法公开数据入口；不是再用合并权重toy取代真实证据。

### Q(E)角色与接受权重不能被一个同能量点认证

GRS26-11/12追加核原样完整ScalePlot程序：原函数calibration→target角色与plot循环传参反向；1332→1332的回代会掩盖反转，旧Lean正向调用是版本反证。源码均匀θ的单次Σ平均与KN×dΩ加权也不同；E→0分别√2−1和1/2、point90为1。该数学/程序结果说明Q必须连同role、平均kernel与经验半因子定义保存，不将一个理想平均或代码comment Q=.2509认成matching实验response。

### 原装置校准对当前推理的约束

[[garnsworthy-2019-griffin-facility]] GF19-6–14在完整原件后提供实际Q(.240±.012 at1332)、明确.5QPcos2ξ/90°cloverpair与68–113°crystal角组、三其它能量检查和同207Bi双角色。[[triumf-griffin-compton-source-calibration]]是测量/来源ledger；本note的sharedCov/array反例仍是声明模型，不能称paper实际失败。

源数据对当前generic正向ScaleQ作条件比较给570/1173/1771约.378202/.259795/.198649；源reported为.390/.258/.201，anchor共同误差的rank1项需保留，但actualcrossCov/fitΣ不足以报新置信度。Table7的ICC/summing真实摘要重算另显示photon/total分母的重要性；这些新summary-check不增加独立实验数或替代rawresponse。

### 官方207Pb参考的派生归一与概率门

[[nndc-2011-pb207-bi207-polarization-reference]] N207-1–11用真实selected官方对象核1064/570 roles：MR+.02(.01)/blank不同，EC photonRI/experimentalICC与Adopted theoreticalICC不同。RI570=(100−.131)/(1+α570)直接暴露RI–α依赖；在明确独立bypass/α的设计极限，totalσ的α项抵消而不是重复相加。条件pair emission≈.72918不等marginalRI乘积或detectorε，MR强度份额.0004也不等实际P误差界。这一来源相邻的真实输入审计收紧calibration readiness，原primaryphase/完整Σ仍缺，未造新实验P或CI。

### 另一种P不能混入本表

[[schuermann-2008-15o-6792-dsam]] SCH08-5的P=.987是有限Ge尺寸的Doppler修正，乘在β0Fcosθ前；它不是本表physicallinearP、a/η或ComptonQ。SCH08-11的actualcenter映射P×F=.97713只检验其F分母，不能当polarimetry校准或从DSAM曲线给γ的linearP。

## 真实工具合同补充：平滑与匹配不自动进入Cov

[[root-2008-v522-background-error-contract]] R522-2/3/5/10是本note计数设计的实际软件反证：ROOT5.22 Smooth只改content，Background未写估计误差，Add按固定系数diagonal合并。声明matching a=Dk/Bk给不同jointCov；原Compton/Si实验脚本未得时不把本design或工具名升级为实验置信区间。


## 三GeLi原计数式与独立校准层

[[butler-1973-three-geli-compton-polarimeter]] B73-D17-1/2/6/11/12把a相对absorbereff、A校正sumpeakarea、P核光子planeaxis、Q=A/P分层固定。旧Wiki额外1−alphaA分母是转录错已纠；source原Eq4只P=A/Q。新design6000/4000、a1.01的Jacobian/误差保自设Poisson及a独立条件；实际B73counts/背景fit与跨线Cov未取得，不能用印a1%或Qcurve方差当实验jointΣ。

Table1七个Q都是AD预测P和同测A派生；unpolarized56Co/66Ga的a才是另一相对effinput，且仍需samegeometry/selection。Ex2935/Eg967别与同母态groundγ2935混用；nominalpointP>1不clip，不以失配强改authorP/Q。


## 独立装置的null与分析能力分层

[[twin-1970-polarization-angular-correlation-40k]] TW70-D17-1–5的θ0null只relativeeff，R为另一有限geometry/knownAr1460检查；Comptonψ82不能当emissionθ。原R.21(.02)归2231γ，1.5MeV只有验证对象。与B73不同独立dataset仍共理论祖先；pointKN82/90结果不替actualresponse或跨装置factor，原counts/共同Cov未得。


## 单晶峰面积与平均分母

[[ewan-1969-single-geli-polarimeter]] EW69-D17-1/2/3/7明确samecrystal旋转的peakcount差除average与常用差除sum有2倍；correctedQ和rawQ/P不同列。表四点映成A/P .0785/.052/.063/.032仅同合同，不当新校准测量；833A=−.017不是P，knownQ833/Σ未得。先核分母和orientationobservable，再讨论效率或敏感度比较。


## 非正交sum与校准可识别性

[[garciaraffi-1995-nonorthogonal-compton-polarimeter]] GR95-D17-1/2/6/8的normalizedpointQ3=0，而P相关sum留下非线性；原φ0/60 alpha−1/3。一般两channelcos2kernels若不共knowngeometryfactor，Q1/Q2需两个独立knownP斜率信息；unpolarizednull只校offset/eff、一knownP仅一约束。原extended沿pointalpha为作者假设，actualresponse/Σ未取得，不用新point例认证CLUSTER。

原M=4f/(1+f)² εQ²为smallP/忽背景，finiteA Eq14和P符号相关；simplepair3/2merit不是所有P/实际sensitivity优化保证。与[[butler-1973-three-geli-compton-polarimeter]]原正交P=A/Q和[[ewan-1969-single-geli-polarimeter]]average分母2倍约定是三个不同合同。


## Sectored校准的core、tag和merit分母

[[schlitt-1994-sectored-compton-polarimeter]] SC94-D17-1/2/3/7/8的H/V是带另两sector否决的选择，Nscorephotopeak作relativecoinceff分母；F另用absolutecoinceff。512是622tag后的probe，不可移source singlesP；TableP98%与nominalP1保recipe缺口，1368/C的AD/P还共B73标尺。实际count/Σ/absolutecoreeff未知，不拿旧25%造绝对F或把NRFsign当任意Jπ判据。


### 强度比解释的belief revision

[[ewan-1969-single-geli-polarimeter]] EW69-D17-11/12精确恒等式rEW=(1+p)/(1−p)将>1的原式映回boundeddegree；已撤回旧formulafailure解释、保历史快照/冻结与原书章缺口。rawQ2A/corrected2A/P的计数归一桥不受影响；未将r当degree用于counts/P/Q误差或新实验校准。


## 背景估计的方差属于计数合同

[[logan-1974-generalized-polarimeter-merit]] L74-D17-1/2/3/7/9的sourceEq2可独立推为VarN=N+2B；若背景估计方差ηB应改N+(1+η)B并保orientation/sharedCov，不能只把N当Poisson或把source2/S当所有fit通用项。source每orientationt与arbitraryε只给条件merit，σA/A相对精度/P0边界、fullQ/a calibration须另核；不造actualnoise/CI。


## actual读出与calibrator身份优先

[[vonderwerth-1995-compton-polarimeters]] VW95-D17-2/4/5/6/9/10说明MINIPOLAsector只timing、共同totalE；知道两segmenthit不等能重建Es/E′和ordering。POLALI实际knownroles+70–110gate与a/Rasource校准另列，Q/P核标尺不混。69Ge287.2与70Ge288.0calibrator不同，近E不是独立身份匹配；source半sumabsoluteε合同保，actualcounts/Σ缺不造门retention/CI。


## 同一次partition的分子与分母

[[bass-1972-two-crystal-compton-polarimeter]] BA72-D17-1/5/8/9：N=C/(C+A)而非C/A，Cov(C,C+A)=VarC；在独立primitivePoisson设计下σfraction为binomial尺度，实际peakfit/rotation/sharedPref仍需fullΣ。原statonlyR不含Pref误差，阈值扫描共源/共事件，不能将每行Rσ视独立或以原Nbar回造counts。

### SeGA2007：a的倒数约定与5000全峰计数

[[miller-2007-sega-polarization]] MI07-D17-1–13原6页713–718本session完整原读。4quadrant×8slice侧入射，本run实际6个37°/9个90°的15unit与standardFig2的8+10不同；249Cf约1µCi、Si400µm/11cm及Pt2mil是本source几何。245Cm388.3同parent的333和388支均E1却有相反a2/P，说明Psign还取决于branch/取向，不能只把E1固定成一种sign。

#### a小是原几何，不是偏振小

MI07 Eq5/6定义

\[
a_{\rm MI}=U_\perp/U_\parallel,\qquad
A=\frac{x-a_{\rm MI}y}{x+a_{\rm MI}y},\quad x=N_\perp,\ y=N_\parallel.
\]

本页前ST99的a=Uparallel/Uperp等于1/a_MI；表达式可同义转换，但不能把同一个a数值直接放过去。原weightedaverage a333=.126(.007)/a388=.128(.007)，sample unitstd .009，σ多来自detector差异（printed716）。这既不是offset，也不表示physicalP；sidegeometry/选择的parallel/perp约占总峰25%/3%，所以极不平衡。roundedfraction ratio .12和原a约.127不强调为同一精确值；每unit用实际a，poolweights变化需重核。

#### 5000是总峰，不是5000个选中事件

用作者rounded fractions的**明确设计**：Npeak=5000，P=0，Q=.14，knowna=.03/.25=.12。则期望x=150/y=1250（非原actualcounts），有

\[
\partial_x A=\frac{2ay}{(x+ay)^2},\quad
\partial_y A=-\frac{2ax}{(x+ay)^2},\quad
\partial_a A=-\frac{2xy}{(x+ay)^2}.
\]

独立primitivePoisson或声明exclusivefixedN/noBG的同阶Jacobian均给null处

\[
\sigma_P^2=\frac1{4Q^2}\left(\frac1x+\frac1y\right),
\quad\sigma_P=.3086067.
\]

它支持原Outlook约.3的计数量级；若误把5000作为两类sum或只用1/(Q√Npeak)，会丢掉实际接受/不平衡代价。此设计暂忽a/Q/背景/峰fit误差，不认证真实CI。若**另行假定**.007是独立σa，仅这项localσP=.208333；但source说unitspread占主要成分，实际sameunit/commoncalibration与事件依赖未知，不能将这个设计σ直接和统计项相加后称作者误差。

#### 效率、F与共享资料

Eq14的εc=(Nparallel+Nperp)/(2Ntot) εphoto是两方向**平均**。singleεphoto=.00212、rounded25%/3%给εc=.0002968，FM=.14²εc=5.81728×10^-6；用原εc=.000299则5.8604×10^-6，近原5.9×10^-6。不是整15array ε，不是两类sum裸.28，也不是另一篇中相对NaI或coincidencetag效率。

原Table1的POLALI/Clover/Gammasphere Q外推至约350、absoluteeff从图估；FM中央值可按Eq13核，误差仅源可用Quncert，作者加eff估计后认为整体约30%。不是新同beamtime比较，低statcost或scope不同不由同列FM消除；这项标准FM也不替完整实际峰fit/不平衡计数的likelihood。

#### AD给的P还需实际接受合同

Nd/Ns=fDS εalpha Wav（Eq9–12）可消同Ge效率，不能消α选择/finiteangle/共singles误差。原a2(388)=+.17(.01)、a2(333)=−.29(.02)；E1 Eq8为

\[
P(\theta)=\frac{-3a_2\sin^2\theta}{2+2a_2-3a_2\sin^2\theta}.
\]

barepoint37°/90°分别给388 −.085702/−.278689、333 +.181602/+.379913，不能宣称已重放原四group finiteangleP。printed716列388 −.267(.007)/−.13(.02)，333 +.24(.02)/+.37(.02)，并称forward/back respectively；388的文字顺序与point角序尤不闭。source还说约1% finiteangle uncertainty已平均修正，但未给完整gamma/alpha接受与producer；这里不交换原marker、不从effectiveangle反校几何或改Q。

若**声明**共同E1的integratedStokes模型、将正权响应对unpolarized几何平均，则S=〈sin²θ〉，

\[
\bar P=\frac{-3a_2 S}{2+2a_2-3a_2 S},\qquad
S=\frac{2\bar P(1+a_2)}{3a_2(\bar P-1)}.
\]

原四P按打印顺序给S=.966897/.527850（388）、.515426/.958584（333），均0–1；小/大S可两能量成近组，但这仅诊断所需响应moment，不认证实际ringlabels、37°有限接受、无权P平均或源producer。5000count练习也不依赖将这些P重标。

原四group relativeA在claimed Qrel=.18下的summary标准化残差约−1.065/.113/−.080/.835，未重拟合逐unit数据。Qrel/同source AD/a/两branch共享事件与方法谱系，不能把四group当四独立Q实验或虚构Σ。highestinput仍actualunit/gates/threshold/ordering、净峰/背景/接受与jointfitCov；higherenergy/inbeam/数字tracking在原文是下一测量/改善，无31/33Mg新parity结果。

复算`system/scripts/day17_miller2007_count_audit.py`，本run `miller2007-count-contract.json` / `miller2007-count-result.json`。决定`supports`source计数量级与sidegeometry可行性，`limits`跨约定/energy/array/merit迁移，没有新的实验P/Q/δ/CI。
