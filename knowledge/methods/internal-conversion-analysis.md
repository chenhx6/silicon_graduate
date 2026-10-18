---
type: method
title: 内转换系数分析
aliases: [internal conversion analysis, internal conversion coefficient analysis, ICC analysis, ICE gamma ratio method]
created: 2026-07-12
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
method_type: conversion-coefficient-analysis
tags: [internal-conversion, mixing-ratio, multipolarity, gamma-spectroscopy]
---

# 内转换系数分析（Internal Conversion Coefficient Analysis）

## Purpose

利用实验内转换系数与理论 ICC 表比较，约束跃迁多极性和 multipole mixing ratio `delta`。

## Inputs and Assumptions

- measured electron-to-gamma or X-ray-to-gamma intensity ratios;
- atomic number、transition energy、候选 multipolarities；
- theoretical ICC source，例如 BrIcc；
- 对 mixed transitions 的 `delta` 约定与不确定度。

## Core Relation

对 mixed `(pi L + pi' L')` transitions，ICC 使用

`alpha = [alpha(pi L) + delta^2 alpha(pi' L')] / (1 + delta^2)`.

因此 ICC 对 `delta` 的符号本身不敏感，只对 `delta^2` 敏感。

## Practical Routes

- 直接测量 electron/gamma intensity ratio；
- 当 ICE 数据不完整时，用 X-ray/gamma ratio 与 fluorescence yield 间接求得特定壳层 `alpha`；
- 用 BrIcc 之类的理论表和不确定度处理来比较纯多极与混合多极情形。

## Relation to Mixing-Ratio Extraction

[[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]] 展示了如何把 measured `alpha_exp` 与 pure-multipole theoretical ICC uncertainties 一起传播到 `delta`，并说明最终 `P(delta)` 一般不是 Gaussian。

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] 给出 BrIcc 的 mixed-transition ICC 公式、`delta`/transition-energy uncertainty 传播，以及插值与 vacancy-treatment 的边界。

## What It Can Establish

ICC 可以为 multipolarity、spin/parity assignment 和 `delta` 提供独立于角分布 alignment 假设的约束，尤其适合和角分布、DCO、偏振联合使用。

## What It Cannot Establish Alone

- theoretical ICC table、atomic-vacancy treatment、energy interpolation 和 multipolarity 输入都会影响结果；
- 单个 `alpha` 值反演出的 `delta` 置信区间可能非对称；
- 当实验 `alpha` 误差较大时，简单反演可能偏置 `delta` 中心值；
- 对非唯一 multipolarity 标签（如 `D/Q/O`）不能假装已经得到唯一 ICC 结论。

## 164Yb固定候选：明确壳层、效率与E0的输入门

[[nndc-2018-164yb-pdco-reference-records]] N164-4/6/10区别了489.8理论KC/CC与647实验EKC上限。新的匹配reference由[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D15-1–4给出：官方Z70/E489.8 FO-only pure M1/E2各一次，actualweb v2.3(2011)，K=.0363(5)/.01475(21)，L-tot=.00536(8)/.00314(5)，programTot=.0432(6)/.0188(3)。N6/N7空白/警告保留，不认证完整total。Z-only查询不等于A164核尺寸重算；2008表的reference A为173。

固定[[starosta-1999-pdco-experimental-test]] mixed点atanδ=−21°，radiative wM=.871572/wE=.128428，于是K=.0335323855、L=.0050748908、programTot=.0400663669。K相对pureE2的比为2.273382；不把这些数强贴到原文未核定义的alpha_κ，也不称新测量或整族δ区间。energy.1keV、δ误差及actualtheoryCov未输入；quoted pure-component errors的rho−1/0/+1只给敏感性，不再独立叠加.3% interpolation。

### angle-integrated ICC与所测electron/gamma比

对归一角分布W_s,e和W_gamma及各自接受R，定义`A_s=∫R_s W_s,e dOmega`、`A_gamma=∫R_gamma W_gamma dOmega`。无背景且同transition/event-selection时，计数均值比为

$$\frac{\mu_{s,e}}{\mu_\gamma}=
\frac{\epsilon_s A_s}{\epsilon_\gamma A_\gamma}\,\alpha_s
\equiv\kappa_s\alpha_s.$$

这是定义层forward relation。若电子/γ有joint gates或共享postselection，A还要用相同conditional response；不能拿γ-array的single-gamma efficiency或ADO修正代替electron接受。不同candidate的alignment/mixing若改变W，κ也可能不同。实验alpha独立于核alignment的说法，前提是有限接受已适当校正或积分，不是任何electron/gamma raw ratio都无alignment依赖。

只有这个ratio且κ自由时，`(alpha, kappa)→(c alpha,kappa/c)`给相同likelihood；增加计数不能解这种识别缺口。必须给独立效率/角响应/reference及其与背景、electron/gamma gates的Cov。电子K kinetic reference428.4677keV来自2008binding，实际energy-loss/响应仍需实验核定。

### 一个显式chosen的固定点计数设计

只为设计，假定κ=.5已知、背景为0、两个fixed alpha不带误差，electron与γ是Poisson thinning。条件于两类总探测n，电子数为binomial，`p=κalpha/(1+κalpha)`；source yield这个共同nuisance消去。不是实际数据，也不包含unknownselection、deadtime、calibration、E0或wholeδfamily。

以**自选**expected twice logLR目标9，`E[2logLR]=2n D_Bern(p_true||p_other)`，得

| fixed truth | p_e | 所需chosen n | expected electrons | expected gammas |
| --- | ---: | ---: | ---: | ---: |
| pureE2 K=.01475 | .00732101 | 1378 | 10.0883 | 1367.912 |
| mixed point K=.0335324 | .01648972 | 1056 | 17.4131 | 1038.587 |

目标9不是3sigma或已验证power。此精确fixed模型中，仅用LR>1偏好正确点的概率分别约.94878/.93060，并非指定type-I error下的power；少量electrons不能靠Asimov数值保证实际判别。若κ自由，pureE2 κ=.5与mixed κ=.2199366的**完整条件分布完全相同**。两个候选各自profile同样的对称fractionalκ区间，半宽约.389011时区间开始重叠；这是chosen nuisance域的代数阈值，非实验允许systematic。

### E0与两壳rank：怎样的下一观测有区分力

16+→14+候选的同一branch不容E0，14+→14+候选则选择规则允许；489.8<1022keV无E0 pair。按KB08 Eq7/11，在相同FO/reference、忽略其它修正的固定mixed点，`alphaK_obs=baseK+xK(E0)`且xK≥0，故E0不能把.0335324降到pureE2 .01475。该条件lower bound不覆盖任意δ、高阶/penetration、unknownelectron接受或未识别同能峰。高侧electron excess可来自E0/不同fractions/response，不能独证E0或唯一δ；ICC仍不给δ sign。

若用两个明确shell并得到calibrated angle-integrated ratios，令w为M1辐射分数、x=rho²(E0)/T_gamma（单位s），则

$$\alpha_s=e_s+(m_s-e_s)w+\Omega_s(E0)x,\qquad s=K,L.$$

在只保留M1/E2/E0且Omega已独立给定的模型，系数矩阵两列`(m−e)`与Omega不共线才有局部full rank；还须w∈[0,1]、x≥0及jointerrors。只有K一条约束通常不能分w与E0；只有tau而totalbranch/其它decays未知也不补rank。下段随后补了nominal匹配Omega，但其Cov、actualshellresponse或完整branch仍缺，**未声称两壳方案已经可识别实际164Yb**。E0表不给统一Datheor，不能从ICC1.4%替造。

可复算入口：[冻结查询v2](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-z70-489p8-query-input-v2.json) hash `5a4deef640bd8177002fc24c929641f7ee29300b9b1a4eb1ae1a03acc2858a9c`；[官方响应与完整rows快照](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-z70-captured-coefficients.json)；[设计输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-n164-icc-design-input.json) hash `af3cd646844951f40081a2342fb2ad120441ba14af3635bd8550aeb481f1b3dd`；[计算脚本](../../system/scripts/day16_bricc_n164_icc_design.py)/[结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-n164-icc-design.json)。query只两POST，无自动retry；全部数值与rate/response/统计假设已在canonical页保存。此fixedpoint/设计stop contract已满足，无新L4或spin裁决。

### 新E0 K/L1参考：中心满秩但病态

为真正核上述rank条件，随后冻结一个独立有界续问，另作**1POST/0retry** E0查询（不重跑前两点）。[KB08 source](../sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md) KB08-D15-5实际返回BeOmg而非ICC FO：OmegaK=5.595E10、L1=8.284E9、L2=1.616E8s^-1，programTot6.440E10、K/Tot=.8688。无reportederror/其它shell，不称completeTotal；不能把E0电子因子混成普通ICC或借ICC1.4%。这仍是模型reference，与actualE0 strength无关。

取z=OmegaK x后，名义K/L1模型为

$$\begin{pmatrix}r_K-.01475\\r_{L1}-.00186\end{pmatrix}
=\underbrace{\begin{pmatrix}.02155&1\\.00309&.1480607685\end{pmatrix}}_{A}
\begin{pmatrix}w\\z\end{pmatrix},\qquad
A^{-1}\simeq\begin{pmatrix}1470.1759&-9929.5437\\-30.68229&213.98167\end{pmatrix}.$$

参数w与z均无量纲；列**分别归一**后，两列sine=.00457610，夹角.262192°、2norm条件数437.0513。列归一去掉仅由Omega单位或选参尺度造成的条件数，但它仍不是按actualmeasurementΣ白化的信息矩阵，不能直接转实验参数误差。

在source fixed−21°、z0的名义点，rK=.0335323855、rL1=.0045531588。postlookup以**自选**L1相对+1%、K不变只展示局部导数尺度，w下降.4521079至.4194645、z升.00974293；这不是实际测量、误差预算、独立holdout或新δ拟合。

另一个postlookup scope控制：保留L1/Omega中心，将M1_K降至.0358209924、E2_K升至.0149511832，两者均在各quoted marginal的约.9580倍内，A的det≈0。它证明仅有这些marginals不能认证full-rank稳定性；未证明真正atomic共同Cov或系统变化允许这个方向，也未把这些括号当置信域/严格theorybound。来源fullrank中心与此marginalbox控制分开。

当前下一观测不能只说“补L1即可”。需先取得calibratedshellresponse、joint计数/背景/calibrationΣ，验证reference uncertainty的相关结构，再选择能提供独立direction的shell或matched photon interference观测，并检验condition。既有DCO/PDCO的取向和gate约束不能丢掉。actual164Yb并无这些电子数据，ordinaryICC/Ωscope已满足stop contract，不再自由query更多能量或参数以充窗口。

[E0冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-e0-shell-rank-input.json) hash `0082add7f6e8821a4fc05a639f47af915c85d1a0492e82f337450e2056f9a723`，[原HTTP回执](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-e0-query-receipt.json)、[离线计算脚本](../../system/scripts/day16_bricc_e0_shell_rank.py)/[完整结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-bricc-e0-shell-rank.json)。mainline原件和query有scope，不重放作者代码、不重算A164电子波函数或实际L4。

## 178W 921-keV：真实K-shell companion不能自动替两个DCO点选支

[[nndc-2009-178w-dco-reference-records]] N178-12实际列同一约921-keV branch的alphaKexp=.0067(.0011)，来自1998Pu01缺省层；同母态1090为.0031(.0005)，但原calibrator/效率/角接受/门/Cov未取得。它与adopted CC total .009(.004)是不同对象；adopted多极标签不能再作为该K数据的独立确认。

新[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D16-1–4核原Eq5/20、SC模型边界与**两次**Z74/E920.8 nominalFO查询，actualweb v2.3(2011)：pureM1 alphaK=.00995(.00014)，pureE2=.00435(.00006)。K有数值不代表N6/N7也有，raw警告398keV/unknown保留；没有用programTot .01188/.00533代K或重新插值total。2008表mass参考W184，当前Z-onlybackend未给A/datafile hash，不称A178波函数重算。

在[[w178-921-dco-gate-double-solutions]]的**固定点设计**中，R=.66两D96坐标根约.09186/46.2691分别给

| 固定模型点 | radiative E2份额 | nominal alphaK | 与reported literal[.0056,.0078]的关系 |
| --- | ---: | ---: | --- |
| d=.0918600 | .00836766 | .00990314 | 两pure理论marginal误差盒传播后仍无交集 |
| d=46.2691 | .99953311 | .00435261 | 同上，无交集 |

它没有选中一根。两点不代表全部DCO允许branch families，且没有原response/Σ，所以不能把这张表变成实验排除。普通混合公式的名义中央映射为fE2=.580357、abs(d)=1.176001，两sign都给同ICC；这是条件计算，不是新实验delta或原文联合fit。quoted alpha边界的名义theory像abs(d)[.789423,1.865476]无置信水平。

理论component errors可有共同Cov；给定quoted尺度时Var(alpha)=wM²sM²+wE²sE²+2rho wMwE sM sE，只列rho−1/0/+1敏感性，不把它当actual covariance。Table2的1.4%已经含interpolation，不再独立加.3%；物理gamma .1keV和原calibration误差未完整传播。

判定`revises`“补一个reported ICC即可自动选原DCO根”，`limits` phase换号作为修复magnitude差异的办法；继续查same-transition matched response及原producer。J11→10条件下不容E0；没有借未知额外成分或任意核penetration参数强配，DF的SC近似与NP校正式也不能无定义叠加。程序[day16_bricc_w178_reference.py](../../system/scripts/day16_bricc_w178_reference.py)的三阶段、冻结input/hash、actualrows/coverage与oldcode snapshot均在本日run-dir，关键知识已在本页与source保存。

随后取得的[[purry-1997-phd-w178-multiparticle-structure]] P97-2/3/5原图确认这些Kexp数值，并将原测量合同具体化：独立SiLi磁透镜/单Ge、beam后50–400ns的matched spectra，152Eu/internal lines与energy-dependent timing correction。不是完全未校准，也不是与prompt angular distribution相同sample；缺的是原efficiency/angle/peakledger、calibrator逐线与Σ。论文P97-8用290KICC和符合timing修订旧3525/35ns方案，说明实际companion可以改变assignment；本页固定921两点仍只是条件检查，不重做原实验。

## Sources

- [[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]]
- [[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]]
- [[nndc-2018-164yb-pdco-reference-records]] N164-4/6/10/13；实际参考记录的同量/独立性边界。
- [[starosta-1999-pdco-experimental-test]] ST99-2/12；fixed−21°point及独立转换需求。

## 完全未观测跃迁：用总衰变权重而非自动沿用光子δ²

[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-3/4区分三个对象。定义radiativeq=δgamma²=Tγ(Lprime)/Tγ(L)，purecomponent totalICC为alpha_L/alpha_Lprime，则所有该branch衰变均未被区分时

$$q_{\rm tot}=q\frac{1+\alpha_{L'}}{1+\alpha_L},\qquad U_k^{\rm all}=\frac{U_k(L)+q_{\rm tot}U_k(L')}{1+q_{\rm tot}}.$$

若额外要求middleγ且对方向全积分、两multipole的探测选择按声明条件相同，权重回q，得到Ugamma；若完全未观测电子/γ，则用qtot。若只选i-shell电子，deltacei=sqrt(alpha_i(Lprime)/alpha_i(L))*deltagamma，还要在观测electron角式使用particleparametersb_k；不能将alphaK替代Eq9的totalalpha。branch、multiplicity、电子/γveto/threshold或方向cut会改变真实条件权重，以上不自动代表实际DAQ。

由两比值直接推得

$$U_k^{\rm all}-U_k^\gamma=\frac{q(c-1)[U_k(L')-U_k(L)]}{(1+q)(1+cq)},\quad c=\frac{1+\alpha_{L'}}{1+\alpha_L}.$$

因此alpha相等/均0、δ=0或pureLprime极限给相同传播；middleδ反号始终不变。转换率不同可以产生宇称敏感性，但若radiativeq自由，任意cB>0可用qB=qA*cA/cB得到完全相同所有Uk；**单靠totaltransfer也不唯一确定parity或radiativeδ**，仍需独立radiativemixing/ICC/responsecompanion。

### W178168.71：来源身份明确的条件设计

[[nndc-2009-178w-dco-reference-records]] N178-4绑定历史2133.93(10−)→1965.20(9−)/168.71keV；旧KF89 nominalδ=−1.9的operator归属未认证，本例显式**选择它作为radiativeE2/M1坐标**，不能把选择升级成实测定义。[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D16-5的新nominalFO total为M1 1.073(.015)/E2 .553(.008)，故c=.749155813、qgamma3.61、qtot2.70445248，radiativeE2fraction.78308026对totaldecay.73005458；abs(Delta)=1.64452196是effectiveweightcoordinate，不是新测δ。middlebranch辐射率份额约.60031279仅为该二成分设计。

| rank | U_M1 / U_E2 | U_gamma | U_all-decay |
| --- | --- | --- | --- |
| 0 | 1 / 1 | 1 | 1 |
| 2 | .984962119 / .925267445 | .938216398 | .941381749 |
| 4 | .949871380 / .757978172 | .799603597 | .809778866 |

独立GSL6j与CG channelpureU差≤4.45e−16，trace/U0/limits与identity均核。用名义11→10→9→7、首921/末225.83pureE2、point90/38/phi18、fixedstdGaussian.3和旧两个firstδ候选作**另一个没有实测endpointRDCO的设计**：按显式R=W(first90,last38)/W(first38,last90)，小候选Rgamma1.48134383→Rall1.48360244（相对+.15247%），大候选1.49070324→1.49234834（+.11036%）。不可将此两值套到原921(G)–306/.66或169门/.47；原168middle并不是那两项测量的未观测对象。未据此解释历史偏差、改δ或选branch。

给定puretotalquotedmarginals，c的字面box[.739942529,.758503401]无CI；实际theoryCov未知，局部rho−1/0/+1分别给sc≈.00927995/.00665418/.00156167，未再叠加interpolation，能量.05keV/原responseΣ未传播。[冻结input](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/w178-unobserved-ic-input.json)和[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/w178-unobserved-ic-audit.json)、[原创程序](../../system/scripts/day16_unobserved_conversion_audit.py)保留query/hash/normalization/role；首JSONnumpybool序列化失败不改physics输入、已留回执。
