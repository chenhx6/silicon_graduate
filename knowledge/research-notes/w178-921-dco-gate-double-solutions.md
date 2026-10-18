---
type: research-note
title: "178W 921-keV DCO：实测双候选、门角色与条件反演"
aliases: [178W 921 DCO double solutions, Day16 delta-double-solution-sheet]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [kramer-flecken-1989-use-dco-ratios, droste-1996-pdco-formalism, krane-steffen-1970-cd110-mixing-ratios, nndc-2009-178w-dco-reference-records, purry-1997-phd-w178-multiparticle-structure]
created_from: Day16 independent daily-learning run
promotion_target: dco-ratio
tags: [dco, mixing-ratio, phase-convention, gate-identity, provisional]
---

# 178W 921-keV DCO：实测双候选、门角色与条件反演

## Research Trigger

[[kramer-flecken-1989-use-dco-ratios]] KF89-15/16给出一项真实的双候选：3055-keV态发出的约921-keV线，结合两组DCO后作者仍报告小混合比与近纯四极两支，再以强度信息偏好小支。它补充[[dco-pdco-ambiguity-worksheet]]的D96作者模型和KS70 opening-angle coefficient例；三类输入不混并。

## Grounded Evidence

### delta-double-solution-sheet：先固定实测对象

| 项目 | 原件提供的身份/数值 | 边界 |
| --- | --- | --- |
| 实验 | 178W，80-MeV 18O、(18O,4n)，OSIRIS十二台Ge；DCO实际选六台 | KF89 printed337 Sec3/4；不补造靶核或event数 |
| target | 正文921 keV；Fig6具体标920.9 keV；起点约3055 keV，采用I=11，至I=10 | Fig7c/d固定spin方案；不由DCO新增宇称 |
| 角组 | θ1=90°、θ2=38°，φ=18°；对应的后向/方位对称组见Sec3 | φ是两束轴平面的夹角，不是polarization analyzer ψ |
| Fig7c | 921(G)–306：门是上游921，观测下游306；R=.66±.10 | 物理spin 11→10→8；306按pureE2作参考 |
| Fig7d | 921–169(G)：观测上游921，门是下游169；R=.47±.15 | 11→10→9；169不是pureE2，导入混合参数−1.9 |
| 作者两支 | δ1=.07±.10，或δ1>85 | printed338原图确认是δ，不自行改写为arctanδ>85°；不新赋置信度 |
| 强度companion | Iγ(1090)/Iγ(921)=1.2±.2；作者的pure-quadrupole预期2.3 | printed338末–339首；本方法文未给2.3的完整推导/误差 |
| 效率/归一 | 相对效率须校正；建议用近能量、已知spin/multipolarity的cascade标定 | KF89-4/9；逐能量pair效率、标定误差和实际normalizer未提供 |
| alignment/feeding | 作者用σ/I=.3，并假设35-ns isomer不强改该比 | 原件未写Gaussian指数；不是本任务的实测ρ或feeding重建 |
| response/Σ | 无原counts、背景ledger、finite geometry、DCOMAP producer和联合Cov | quoted errors不自动组成独立Gaussian likelihood |

KF89的γ1/γ2是gate/observed标签；D96的γ1/γ2是物理发射先后。对比必须先填写这两个角色栏。作者两组DCO是同一target的不同kernel，但不是两个独立实验。

### 将两行统一成同一target的方向比

定义共同目标比

\[
R_{t,g}=\frac{W(t@90^\circ,g@38^\circ)}{W(t@38^\circ,g@90^\circ)}.
\]

在相同corrected pair cells、cuts和normalization的假设下，Fig7c须取倒数，Fig7d不用：

\[
R_{921,306}=1/.66=1.5151515,\qquad
R_{921,169}=.47.
\]

第一行字面误差边界的像为`[1/.76,1/.56]=[1.3157895,1.7857143]`，非对称。小误差线性传播才给σ≈`.10/.66²=.2295684`。若原两比值有Cov，变换后的cross Cov乘`−1/.66²=−2.2956841`；不能默认改变量名后仍保留原协方差和误差对称性。这些是比值变换，不是增加一次测量，也不给区间置信水平。

## Assumptions

下面计算输入在数值之前冻结为`DAY16-KF89-W178-921-GATE-CROSSWALK-01`。它是明确的条件设计，**没有重测178W的δ，也没有重放DCOMAP**。

固定11→10→8和11→10→9、pointθ=90°/38°/φ18°；采用D96 Eq19的`p(M)∝exp[−M²/(2σ_std²)]`，首次选择σ_std/I=.3，不给daughter重置Gaussian；两步之间无其它去取向。效率因子在设计里设1，真实效率/finite response/feeding/Σ保持未知。

target坐标`d=a(E2)/a(M1)`按D96；同BM算符/state phases下才与KS70相同。169参考的−1.9在KF89没有完整operator定义，因此把它直接放入此坐标仅是**声明的诊断假设**，另固定+1.9作相位误用控制；这不是认证或重标定KF89的δ。若target是E1/M2，同一directional设计仍不能赋宇称，线偏振预测须重新说明电磁类型。

另在数值前冻结literal-HWHM解释`σ_std/I=.3/√(2ln2)`，仅诊断width用词歧义；不将二者任一当原producer已知参数，不扫描宽度去强配作者解。

## Provisional Reasoning

### 从正的响应矩阵求全体解

在实振幅、固定reference/ρ/response下，令v=(cosα,sinα)、d=tanα。两个计数格可写为正的二次型，`R=vᵀNv/(vᵀDv)`。D正定时其完整范围是(N,D)的两广义特征值之间；给定r后解`vᵀ(N−rD)v=0`，通常有两个projective根。α的±90°是同一个pure-quadrupole端点，不能用一个局部optimizer代替全部根。

上述std设计下，Fig7c统一target比的矩阵为（单位sr⁻²）

\[
N=\begin{pmatrix}.007979112410&-.002424705094\\-.002424705094&.008041434041\end{pmatrix},\quad
D=\begin{pmatrix}.004521547183&.002461011548\\.002461011548&.005132142260\end{pmatrix}.
\]

对其原始R=.66单行得到：

| 本任务D96坐标候选 | α/degree | R原行 | 同gate目标P，90°/38°/φ18° |
| --- | ---: | ---: | ---: |
| d=.091860035 | 5.24846274 | .66 | −.39845549 |
| d=46.26909199 | 88.76187627 | .66 | −.01992199 |

这不是作者`.07±.10 / >85`两支的更新值。两者分别属于条件点模型反演和原文分析；保持不同数据身份。两根P同号，故此例需要校准后的偏振**幅值和误差**，仅“magnetic/electric符号”不能挑根。

若再按声明把169的d设−1.9，并将两条quoted margins作为rectangle，α的交集仍分成`[−.399646°,10.371652°]`与`[83.372120°,86.818175°]`两段。它是自选模型下字面边界的preimage，无68%/95%含义，也没有复现作者的>85支。literal-HWHM诊断又给不同两段；错误地仅将169坐标翻成+1.9而不改kernel，在两个width选择下都无交集。后者展示误用约定的风险，不证明source的−1.9定义已认证。

### 相位表与失败控制

本session重新查看D96 printed519 Eq3–6/520 Eq7及KS70 printed727 Eq4/5/9–12。KS70 Eq4b的分数前确有**负号**，高倍原图与Eq9的正`√3/10`比例相互核对。设`C_L=k^L√[(L+1)/L]/(2L+1)!!`，则

\[
t_{KS}(EL)=C_L i^L\langle M(EL)\rangle,
\quad t_{KS}(ML)=-C_L i^{L-1}\langle M(ML)\rangle
=C_L i^{L+1}\langle M(ML)\rangle.
\]

在相同BM定义和单位下，D96 Eq5只多同一transition的共同positive因子，故`d_D96=δ_KS`。这个确认不扩张为所有paper的同名δ可互换。

| 检查对象 | 逐定义结论 | 原件locator |
| --- | --- | --- |
| 多极子顺序 | 本例是higher E2 / lower M1；generic KF89也有M2/E1，不能无条件叫E2份额 | KS70 Eq9；KF89 printed339的182例 |
| 发射/吸收 | KS70初态在右；Eq5所对照的Rose–Brink初态在左也仍指发射 | KS70 printed726 Eq3、727 Eq5文字 |
| operator与state phases | 共同state相位在同一transition比值内抵消；operator相对相位和归一要显式映射 | KS70 Eq4/5；D96 Eq5/7 |
| 第一/第二photon | KS70相同emission δ用于B(first)时干涉项负、A(second)时正 | KS70 Eq10/11 |
| 历史BR身份 | KS70 Eq12的BR是Biedenharn–Rose1953，γ1换号、γ2不换；不是Rose–Brink1967 | KS70 Eq12、printed734 Ref29/30 |
| 已归一RB坐标 | 旧原式桥`δ_KS=−δ_RB`及其√(2L+1)归一仍保留；不是裸T_RB比 | KS70-13；[[rose-brink-1967-phase-defined-angular-distributions]] RB67-6 |

相对坐标换号S=diag(1,−1)时，同时用`v′=Sv,N′=SNS,D′=SDS`，R全网格差0。只换v而不换kernel，本设计R最大差3.66；但pure dipole和pure quadrupole仍通过。这使“pure reference已校准，所以mixed interference也正确”的推断失败。

针对本次11/10高自旋，D96 generalized F和独立photon singles投影差`1.11×10⁻15`；完整Eq1/3/7 contraction与photon trace的24个比较最大差`1.22×10⁻17 sr⁻²`。这两路共享CG/Wigner primitives，不是两个独立程序或实验。第二gamma的rank≤4、第一gamma rank≤4，使可见initial rank≤8；这一裁剪来自triangle约束，不是随意删高rank。

### 未复现的原表保留为producer边界

原Table1十行的同几何std点模型检查中，10→8→7、L2/L2得到`.637341`，印值`.66`；9→8→8、L1/L2得到`1.188657`，印值`1.12`。同一实现的若干pure stretched行与印值相符。没有把这些偏差改表、扩大容差或调σ抹平；源的exact exponent、finite response、approximation和DCOMAP实现尚未恢复，原因未裁决。

完整tensor与trace相符只认证本任务声明的forward model内部一致；它不自动认证原producer。尤其不能拿本任务不包含作者>85支的rectangle交集去推翻原文选支。

后续已先冻结假设、再全文核[[bargholtz-1987-high-spin-gamma-gamma-directional-correlations]] BT87-4/5，按其infinite/finite-improvement形式检查这十行。两近似只有2/10和1/10落入.01半单位舍入，原四项差异均未被解释；不能据KF89 Ref6就归因为此近似。[[angular-correlation]]保存Eq10/Eq12核验和finite改进破坏stretched E2交换R=1的控制，故本问题转回实际producer/reference，停止在该固定近似网格继续调参数。

## Competing Explanations

### 新取得的评价参考与same-parent条件检验

[[nndc-2009-178w-dco-reference-records]] N178-2–9来自本session实际取得的三个200907 header官方对象。Dors的1979DO02对象给137.34/225.83及168.71/306.05的同母态AD，但MR栏空；1.5(.4)/.8(.3)是CC。RI注明125度，连写1.314按固定栏为1.3±1.4。18O的1989KR01对象只给920.9 D/(11)，adopted 11-/M1+E2不构成新独立赋值或完整δ。

这允许一个不拟合σ的必要条件检验。若同母态两线有共同postselection density和同层angular coefficients、target仅M1/E2、reference pureE2，定义s2=Q2,target/Q2,reference，则

\[
\frac{A_{2,t}}{A_{2,r}}=s_2\frac{v^T F_{2,t}v}{F_{2,r}(E2)},\qquad
v=(1,d)/\sqrt{1+d^2}.
\]

共同B2在非零reference时消去，不需Gaussian；也因此不能通过调σ来修复该条件包。原件未认证Q2比/共同选择/修正层，所以下面先固定**诊断假设s2=1**，不把它当仪器测量。

| 同母态pair | 评价A2 central比 | 全real d理论range | central条件根 |
| --- | ---: | --- | --- |
| 137.34 / 225.83，J9→8及9→7 | −2.1333333 | [−2.8877243,1.9877243] | d=−2.1662458或−.34224154 |
| 168.71 / 306.05，J10→9及10→8 | −3.5909091 | [−2.9272727,2.0000000] | 无real根 |

这是D96/KS共同BM坐标中的**条件反演**，不是重测137/169的δ，更没有给KF89的原−1.9约定认证。169 central比无根所需的positive s2必要下界为1.226708；这个由target数据推得的相容性条件不是独立Q校准。

反证必须保留误差层：169两quoted一倍边界的ratio像为[−4.611111,−2.884615]，已经与理论range相交，允许α约[−47.5861°,−36.9084°]；所以不能由central无根宣称数据不相容。137一倍边界给两段，二倍边界因经过fold而连成一段。所有rectangle/preimage均无置信水平，缺真实Cov时不叫1σ/2σ联合区间。

把旧平均−1.9仅作为未认证诊断坐标代入，137比预测−2.307269、169比−2.351212；后者又依赖Q/层/selection和原平均值精度。不得反求一个Q或alpha强配−1.9再声称校准独立。137有A4 target/reference，但reference误差边界到0、Cov未知；169 reference A4未列，更不能补0拼成唯一解。

新代码[day16_ensdf178_reference_audit.py](../../system/scripts/day16_ensdf178_reference_audit.py)核typed fields、parent/line identity、source F/photon矩阵和全范围/全根；输入identity为`DAY16-N178-SAME-PARENT-REFERENCE-01`，在数值前冻结。原δ平均、branching与response仍需1979primary；评价不是原文producer或新的独立测量。

### 921-keV K-shell对固定DCO点的检查

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D16-1–4重新核原件并提供两个新FO reference：Z74/E920.8的pureM1 alphaK=.00995(.00014)、pureE2=.00435(.00006)，actualweb v2.3(2011)，不是Yb数值迁移或新的实验。两次POST零重试；N6/N7 missing/398-keV warnings不影响已给K行，但不能把program total当完整total。旧人审source全部字节前缀保留，新section/claims仅self-audit。

按普通M1/E2的radiative份额加权，本页R=.66两个固定点的K预测为.00990314与.00435261。两理论marginal误差盒的像分别约[.00976381,.01004247]和[.00429258,.00441265]，都不与reported Kexp字面范围[.0056,.0078]相交。它是**固定模型点**的有边界反检验，没有传播原DCO的R/reference/ρ/response误差到整族branch families，不能变成实验排除或作者哪支错误。

名义theory+reported central Kexp的Eq5逆映射给fE2=.580357、abs(d)=1.176001及±两个sign；只以nominal theory映射quoted alpha边界得到abs(d)[.789423,1.865476]，无置信水平。这是条件算术，不是新测178W δ、原文globalfit或联合两实验重分析。ICC对sign不敏感，phase坐标翻号不能改变上述fractions/预测；不能用换号消除magnitude/校准条件差异。

原始electron/photon接受、门、峰分解、calibrator/normalization、共同Σ和数据版本仍需primary。KB08 Sec4.1.2还区分NP correction与DF的SC近似，动态penetration的核参数不是任意修正旋钮；本run没有调这些参数或宣称此跃迁存在异常转换。同一11→10的M1/E2模型不容E0；没有借额外成分强配数据。这个精确batch stop contract已满足，下一条高信息路线为producer原件/匹配response。

### Thematic REFLECT：原件、响应与companion的共同使用门

#### 后续primary使响应合同具体化

[[purry-1997-phd-w178-multiparticle-structure]]的实际Surrey1997PDF已经取得；P97-2/3/5原图确认921 K=.0067(.0011)、1090 K=.0031(.0005)，电子测量不是六台CAESAR的同一配置：1.5mg/cm²斜靶、SiLi磁透镜、单独simultaneousGe、beam后50–400ns，152Eu/internal lines与energy-dependent timing correction。不能继续笼统说“完全无primary/没有校准”；目前缺实际校准曲线、internal calibrator逐线、原peak/time/selection ledger及Σ。

P97-4的AD数据采用另一套prompt/early-delayed选择，只拟合`W0(1+a2P2)`。所以reported a2不能直接作为前面fullA2、不能无条件与delayedK共用ρ。实际47/97/148度三独立角的[1,P2,P4]设计满秩；但保存下来的只有truncatedfit系数，不提供原三个计数。若另**声明equal weights/point angles**，P4在[1,P2]的投影为(c0,c2)=(−.00954915,−.44481479)，使

\[
\widetilde a_2=\frac{A_2-.44481479A_4}{1-.00954915A_4}.
\]

实际weights/finiteangles未知，不能用此数值反解原A4或改原a2。正diagonal-weight下的slope可写成角对secant slopes的正加权平均，界约[−1.100076,.954230]，甚至不保证相同符号；固定geometry本身不恢复原fit。完整强度比43/34=1.264706及rho−1/0/+1局部误差尺度.16263/.11541/.01384也只作算术，不声称新branch或与KF89独立叠加。

P97-8为更直接的真实反证：290KICC及time/低能符合将旧约3525、I14、35ns方案修订为该态13-/T1/2<1ns，约30ns改归3654态。它说明新的matched observable可改变旧assignment和feeding历史，不证明本页点模型的δ已经重新确定。921依旧是3053→2132的11-→10-，不能把另一处spin修订误贴到它上面。

新[observable-ledger程序](../../system/scripts/day16_purry_observable_ledger.py)保存原PDF hash、表行、两个measurement ledger、actualgeometry设计和unknownweight边界。整份112页thesis只完成相关实验/分析/目标及summary定向阅读，source整体仍skimmed；1998paper未取得，按依赖谱系关联而不称其46页已读。该新增primary是本run的信息增益，不把此前公开路线失败抹去。

| 先前容易采用的判断 | 本组证据后的修正 | source/locator |
| --- | --- | --- |
| 同名921两组DCO可直接联合 | 一组gate=921、一组observed=921，先统一角色/倒数及Cov | KF89-15；printed338 Fig7c/d |
| pure校准通过即可核准mixed相位 | diagonal端点不检查off-diagonal，必须同步参数/核转换 | DR96-5、KS70-6；本任务F/fulltensor控制 |
| finite ordinary系数更精确便使joint比值更准确 | factorization仍是近似，可能失去exact交换R1 | BT87-4/6；Eq10/12和固定表检验 |
| 评价标签/邻近CC就是新的δ约束 | MR栏为空，CC可能来自默认平均；Kexp与total分开 | N178-5/6/12；KB08-D16-1 |
| 同母态reference自动消除所有响应问题 | 只在同层、同选择、已匹配Q比时消去B2；169central与误差盒给不同判断 | N178-3/4/10 |
| 再补一个observable便自动选择原两点 | 实际K配对后两固定点均不在所列一倍边界盒，必须重查联合条件 | N178-12；KB08-D16-4 |
| 多论文/多处理可累加独立实证 | 1979参考导入、1995/1997/1998组内复用、1999采集与2009评价各有谱系 | KF89-17；N178-2/7/11 |
| reportedKexp没有primary，只能停在评价 | thesis原装置/时间窗/校准类别和原表已核；仍需原曲线与event/fitΣ | P97-2/3/5/7 |
| 新的Purry a2可直接接旧全A2矩阵 | prompt/truncatedP2fit与delayedK的sample/estimator不同 | P97-4/10；原p23方法 |
| KF89采用I14说明该赋值无后续反证 | P97用290KICC及timing修订3525/3654的spin/35ns归属 | P97-8；KF89-20 |

决定supports逐对象证据链，revises自动选支与同标签合并，limits未核response/Cov下的唯一δ/Jpi/collective-mode结论。没有改变A≈130争议解释排序；本组结构信息的价值在于可迁移的实验判读合同。

- 实际小D/Q分量与近纯quadrupole分量仍是原文DCO允许候选；强度companion使作者偏好小支，没有给独立校准的唯一δ新测量。
- 模型/印表偏差可能来自输入、width/feeding、response、approximation或程序层；当前不归因为原文错误，也不把变动一个参数后凑中值当恢复原分析。
- 一个negative target P仍可能对应上表两根；改变E/M类型又改变偏振解释。应保留spin/parity/reference假设，而非给每个比值贴固定阈值。

## Verification Path

下一项有用输入是169-keV参考的原始角分布/强度与operator convention、DCOMAP定义及实际pair response。原件printed338把−1.9归给“Dors et al.[3]”，但printed339的Ref3为Gast et al.待发表、Dors1979为Ref2；先查该引文身份，不静默修正为已取到primary。

2026-10-18外部metadata已由Crossref与Semantic Scholar一致定位Dors六作者、*Nuclear Physics A*314(1),61–79(1979)，DOI[10.1016/0375-9474(79)90555-4](https://doi.org/10.1016/0375-9474(79)90555-4)，题名明确177Hf(α,3nγ)布居178W。metadata支持身份，不支持其δ算符定义/原误差。OA-only downloader与出版商public discovery未得PDF；Scholar一次timeout留证，不重试为新证据。TDM license不充当OA证明，raw归档未新增；尚未读取这篇19页primary。

能够分离上表候选的建议是**同一921 target、同一306 reference、同一角组/门/cuts**下的calibrated polarization amplitude，记录Q(921)、平行/垂直净计数、背景和与DCO共享事件Cov；不能借用182-keV的conversion结论或其它能量的P。实际Q/计数未提供，不报所需束流时间或显著性。

复算：[day16_kf89_w178_gate_audit.py](../../system/scripts/day16_kf89_w178_gate_audit.py)。输入及完整矩阵/全部根保存在`outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/`的`kf89-w178-921-input.json`与`kf89-w178-921-audit.json`；本页已保留可复用定义、输入、关键结果和限制，不以outputs作为唯一知识副本。

## Transfer Conditions

门角色的倒数和Cov Jacobian可迁移到同一corrected pair cells的重标记；实际换门、换angle groups或换normalizer需重新构造response。二次型反演要求固定reference、正的ρ和已声明的kernel；本例整数spin、real amplitudes、L≤2不自动认证半整数、高阶多极子或复杂去取向。

## Failure Conditions

分母为零/响应矩阵非正、把不同selection视为同一pair ledger、把KF89未定义的δ直接等同D96、把HWHM字样当已知std，都会破坏此计算合同。Table1未复现及>85作者支未重放是现存readiness boundary；没有通过改观测或调先验隐去它们。

## Falsification or Reverse Tests

纯极限检验不能发现S相对相位错配，故用mixed F投影与完整tensor作reverse check。对物理两候选，匹配的目标P幅值、独立reference或完整原producer可能改变其相容性；只有真实response/背景/Σ支持时才比较实验置信度。若新的matched模型同时覆盖两支，继续保留多解。

## Open Questions

169/137的−1.9原始定义和不确定度来自哪一份primary？2.3强度预期用了哪些K/矩阵元假设？Table1四项明显超过尾位舍入的差异属于何种输入或实现？实际isomer deorientation及两个DCO/强度的事件重叠如何进入联合Σ？这些缺口由后续研究跟踪，不作为默认用户待办。

## Human Review

本页没有发生人工审核。KF89来源页既有human-reviewed状态不覆盖本页或新KF89-15–18；所有新证据状态为Codex self-audit，未清除任何旧needs_review。

## Promotion or Rejection History

2026-10-18：创建为provisional research-note。原件中的实测摘要写入source KF89-15–18；本页的条件模型、分支preimage和反向检验不提升为实验δ、宇称或结构模式结论。

## Knowledge Impact and Learning Decision

`supports` DCO的多解性；`revises` 直接把921(G)与921 observed两行当同方向target比的做法；`limits` 仅偏振符号选根、pure reference认证全部相位，以及条件点模型冒充原producer。没有改变178W或A≈130的结构解释排序；experimental L4 refit仍not-ready。

## Sources

- [[kramer-flecken-1989-use-dco-ratios]] KF89-9/15/16/17/18：原式、实测两行、双候选、companion及谱系边界。
- [[droste-1996-pdco-formalism]] DR96-4/5：条件态、绝对振幅与generalized F；不以1996原印Eq4代替已勘误偏振系数。
- [[krane-steffen-1970-cd110-mixing-ratios]] KS70-5/6/7/13：单位、先后角色、BR身份和归一相位桥。
- [[nndc-2009-178w-dco-reference-records]] N178-2/3/4/5/6/7/8/9/10：评价系数、空MR/CC栏、RI角度/精度与same-parent条件包。
- [[purry-1997-phd-w178-multiparticle-structure]] P97-2/3/4/5/7/8/10：原电子测量合同、原K表、AD estimator、后续赋值反证及实际权重缺口。
