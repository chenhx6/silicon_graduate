---
type: research-note
title: "129Ba365keV：现代数值归属、系数层与同母态参考边界"
aliases: [129Ba365 mixing reference boundary]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chakraborty-2024-possibility-wobbling-129ba, chakraborty-2024-ba129-365-mixing-ratio-arxiv-v3, nndc-2014-129ba-365-coefficient-records]
created_from: Day15 daily-learning uncredited Day16 preview
promotion_target: 129ba
tags: [a130, mixing-ratio, angular-distribution, calibration, provisional]
---

# 365keV：先更正作者数值，再核参考输入

## Research Trigger

[[chakraborty-2024-possibility-wobbling-129ba]]旧CH24-2将−.84至−.79误写成现代重分析采用区间。实际PRC p3将它作为历史回顾，本次χ² minimum为δ≈−2.0/80(4)%radiativeE2。CH24-7已明确supersede旧数值归属，原人审历史/claim flags保留；本页不给新的核结构赋值。

## Grounded Evidence

- CH24-7/8：PRC原5页的现代数值与旧A22/A44/P身份。
- [[chakraborty-2024-ba129-365-mixing-ratio-arxiv-v3]] C365-1–7：单页v3为2024-04-09，共享旧数据；不是另一场独立实验或已验证的PRC逐字preprint。
- [[nndc-2014-129ba-365-coefficient-records]] N129-2–9：365label的明确L/G/FL、AD1977/P1978/DCO1992谱系、defaultδ=.5的CC和错误reference-key边界。

## Assumptions

以下两练习都是L2 source-informed条件计算，非盲复现或actualL4。原始1977/1978的coefficient correction、布居、finitegeometry、polarimeter、gate与Cov未得。printederror只作nominal scale或literal margins，不视为jointconfidence。

## Provisional Reasoning

### 现代结果与历史结果分开

两2024文本均引用A22=−.70(.03)、A44=.16(.05)、P=.072(.068)，并从联合系数图/χ²报告δ≈−2.0(.2)。−.84至−.79来自旧作者AD/P区间交集的历史采用；不能把它拿来代表现代分析，亦不能把相同旧观测在preprint、PRC、ENSDF的重复出现计多份支持。

`f_E2=δ²/(1+δ²)`仅为radiative M1/E2子集：新quoted−2(.2)给中心.80、局部误差.032、字面端点.82877/.76415；作者80(4)%保留印值，不强行改成80(3)%。旧AD−.88(.09)给.436429/.050310，旧P−.58(.26)给.251721/.168872。它们不是absoluteB(E2)、母态totalbranch或三次独立实验。

P的central只约为1.06个quotederror scale，不能仅凭其正号选择branch。当前没有在primary核定P角度/符号/校准和与AD的共同误差，不做P–δ新反演。

### 明确chosen最大取向参考没有复现作者图线

为检查direct-radiation/reference层，先固定13/2−→11/2−、最低M1/E2、sameBM KS/D96坐标和**自选**p(M=±1/2)=1/2。它是物理可用的最大取向reference，不是source声称测得的布居，也不证明印刷A22/A44就是同层的W/constant coefficients。

此reference的single-gamma公式为

$$A_k(d)=\frac{a_k+2b_kd+c_kd^2}{1+d^2}.$$

| k | a_k | b_k | c_k |
| --- | ---: | ---: | ---: |
| 2 | −.3076923077 | 1.0204999355 | −.0439560440 |
| 4 | 0 | 0 | .5754245754 |

source-F与独立photon Legendre投影、12/16点积分一致到约4e−15，证明自选forward model内部相容。可是A2=−.70给d=−2.905240/−.205831，A4=.16给d=±.620603，**不等于作者图线/文字的−2/−.33/±1.3**。因此此reference不能直接替代其producer，未自由拟合sigma/alpha/C来强配−2。

额外选择printedmarginals和rho=−.8/0/+.8的二维Cov，rational score全部stationary points与pureE2 limit检查后，finiteglobalmin分别约−.167326/−.209613/−.244468，score8.34455/7.42022/6.52556。这些只说明错误的reference-to-data映射会改变反演，**均不是重新测得的129Ba δ**，不用于评价作者哪一根正确，也不生成experimentalCI。

缺口可能在布居/参考、finitegeometry、A22定义、相位、gate或producer等层。用目标δ反求所需alpha再称独立校准会循环；更高信息路线是找独立reference或primary correction recipe。

### 数据中确有一个同母态reference候选

N129记录中，母态643.6keV、13/2−的364.7keV至11/2−（FL278.81），另有461.6keV至9/2−（182.04），标E2。1977层paired coefficients分别为target A4=.16(.05)、reference A4=.08(.05)；同reference还有A2=.22(.02)及1978 POL=.44(.17)。这是真实可查的额外summary输入，不是为配作者δ造一个alpha。

但“同母态”不自动证明相同conditional density、coefficient layer或gate。原始polarization/gamma数据、purity和Q4未取得；E2标签也不等于已给M3等高阶的独立上限。下面只检验明确的条件包。

### 共享布居、纯E2参考下的rank4必要关系

若两线的observed coefficient同为`A4=rho4 F4 Q4`、共享母态postselection，target只M1/E2、reference纯E2，则M1/M1和M1/E2交叉项不能达到rank4，故

$$A_{4,t}=\frac{F_4(13/2\!\to\!11/2;E2)}
{F_4(13/2\!\to\!9/2;E2)}\,
\frac{d^2}{1+d^2}\,s_4 A_{4,r}
=-\frac83 f_{E2}s_4 A_{4,r},\qquad
s_4=Q_{4,t}/Q_{4,r}.$$

纯F4的数值为+.5253964397/−.1970236649；精确Racah factorial/Fraction证书给6j平方比64/9及相位，因此−8/3不是只由浮点猜出的分数。核rho4已消去，不需Gaussian布居。不同fixed人口/独立photon projection控制差<1.8e−15，不作为实际布居拟合。

若s4>0、fE2>0且rho4非零，两A4须异号。印刷mean均为正；一倍quotedmargin box内reference为.03–.13、target为.11–.21，无论正s4的大小都不满足这一条件。它是literal margin的逻辑相容性，不是joint1σ/数据错误证明。

再**选择**`s4=1`且`f_E2∈[0,1]`，二倍margin给reference−.02–.18，target.06–.26，但target可达上界仅.053333，尚未相交；只差约.00667，容易受额外几何/误差/舍入条件影响，不能夸成稳健排除。以两nominal独立sigma作profile distance的最小值6.873425，发生在允许边界fE2=1、reference_true=−.042740/target_true=.113973；不是actualfit、p值或新的δ。

这个检查的作用是指出**还要核哪些输入**：同层A4、samegate/postselection、referencepureE2、高阶/污染、Q4的能量/接受符号及jointΣ。未知这些时，不能从二个positive A4断言旧实验或作者物理错误，也不能宣布80%E2已被否定。

### 怎样独立检查Q4符号，而不重复旧cone练习

[[angular-distribution]]既有旋转响应定义`Q4(E)=<P4(cos beta)>_h`及uniformcone闭式，可直接给本案例一个新的geometry验收条件，不重跑旧35checks。要求h非负、归一且是可作scalarfolding的轴对称核；复杂jointgates/非轴对称响应不自动满足。

若h的全部角支持满足`beta_max < arccos(sqrt((15+2sqrt(30))/35)) = 30.555592°`，则P4在支持内严格为正，任意这样的positivekernel都给Q4>0。这个保守充分条件不依赖能量权重是否均匀；超过该半角只表示这个保证失效，不意味着Q4必为负。

**另在uniformsolidanglecone模型**，已有`Q4=c(1+c)(7c²−3)/8`，c=cos(beta_max)；对0≤beta<90°，Q4>0可放宽到beta<49.106605°。49.1°依赖uniform假设，不能拿它认证任意非均匀/有孔/不同selection响应。两个能量都独立满足适用的positive条件才支持s4>0；本任务没有Gizon实际openingangle/响应，仍未认证其s4符号或s4=1。

这把下一输入具体化为detector/sourceextent/angularsupport及energy/selection权重，而不是凭总效率或isotropysource自动当Q4已知。来源[[iliadis-friman-gayer-2021-polarization-direction-correlations]] IF21-7提供有限接受folding的框架；上面两角阈值是本任务从Legendre多项式的数学推论，非该文实测值或原Gizonarray参数。

## Competing Explanations

source coefficient层不同、条件ensemble不同、finitegeometry/response、未控highermultipoles/contamination或quotederror预算都可能破坏上述条件包。当前来源未决定其一。独立calibration问题与modernauthor的δreport、mode解释分别保留。

## Transfer Conditions

同母态reference取消rho的代数仅在相同时间/门postselection、相同coefficient定义和validateddetectorfolding下迁移；不要只凭同parent或“E2”标签跳过这些条件。maxalignment理论曲线也不是另一实验的nuclearalignment测量。

## Failure Conditions

将CC字段的defaultδ=.5当measuredδ；把现代δ误归成historical−.84..−.79；重复计preprint/PRC/评价；用目标root反推alpha作“独立”参考；把条件score当experimentalCI或wobbling证据，都会破坏本页合同。

## Falsification or Reverse Tests

优先取得1977Gi02原AD recipe和1978Gi04的P/参考角/校准；重核643.6的两branch是否同一postselection、coefficient定义、finiteQ和purity。若输入齐全，应联合四系数及P/实际Σ验证，保留全部δ根。若两个A4确同层且纯参考/Q4条件成立，需用其共同uncertainty/失败控制解释上述rank4相容性；不要先固定想要的δ。

## Open Questions

1. 原A22/A44如何从raw angular yields作布居/有限接受修正？modern图线是否明确给出其assumptions或code？
2. 461.6 reference的purity、gate和Q4能否独立认证？parentT643.6目前空白，不能借邻态时间推absoluteB。
3. 365/461的matched电子/γ或其它独立强度观测能增加哪一方向的信息？数据库CC采用假定δ，不能充当这个观测。
4. IF21引用的Bolotin1980 finite-angle实验（DOI10.1016/0029-554X(80)90884-8）及相邻DeBruijn–Lourens1980（DOI10.1016/0029-554X(80)90888-5）是以后可取的actualQ calibration候选；本次只有metadata/public-accessdiscovery，没有正文/数值，不当已读实验证据。

## Reproducibility

- [maxreference冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ba129-coefficient-input.json) SHA-256 `5fd2713b055ab00d7f4f08dd476a2c66371e3d33bfd1da4a08e4da539f9bc319`，[脚本](../../system/scripts/day16_ba129_coefficient_audit.py)/[结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ba129-coefficient-audit.json)；firstcode及source-curve mismatch记录保留，不调population去配文献root。
- [同母态参考冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ba129-same-parent-reference-input.json) SHA-256 `82a2b8bffe867717e01724dc25e554a36039345fdca16bcddc0b926d443e562c`，[脚本](../../system/scripts/day16_ba129_same_parent_reference.py)/[结果及exact证书](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ba129-same-parent-reference.json)。加入exactcertificate时一次函数定义顺序NameError无scienceoutput，已修正；输入/原数据未改。
- source原件/两个NNDCraw hashes各在source页；firstsourcepriming、versionhistory、accessfailures和旧review全prefix证明另存run。实际L4未开始。

## Sources

- [[chakraborty-2024-possibility-wobbling-129ba]] CH24-7–12。
- [[chakraborty-2024-ba129-365-mixing-ratio-arxiv-v3]] C365-1–7。
- [[nndc-2014-129ba-365-coefficient-records]] N129-1–9；同母态实际数据身份。
- [[droste-1996-pdco-formalism]] DR96-5和[[der-mateosian-sunyar-1974-attenuation-coefficients]] DA74-4/5：coefficient/取向层；本页−8/3为任务推导，非原paper报数。
- [[iliadis-friman-gayer-2021-polarization-direction-correlations]] IF21-7：Qn同时进入不同系数与实际接受的使用门；Legendre符号阈值为本页数学推论。

## Human Review

本页provisional/self-audited，没有human review。CH24旧粗略人审历史不扩到本页新推导；所有新source claim true。未得primary输入为研究边界，不自动变为用户待办。

## Promotion or Rejection History

- 2026-10-17：正式Day15完成后恰好Day16预习中建立。修正现代source数值归属；maxreference不匹配及同母态rank4条件包均保留，不推广为新的experimentalδ/模式结论。
