---
aliases: []
review_status: "unreviewed"
reasoning_status: "provisional"
evidence_sources: ["polarization-delta-collection-20261119-source"]
created_from: "User-requested literature acquisition and learning design; scope-specific provenance, not completed full-text learning"
tags: ["spectroscopy", "literature-evidence"]
type: research-note
title: "线偏振与E2/M1混合比原文收集表"
created: 2026-11-19
updated: 2026-11-19
status: active
---

# 线偏振与E2/M1原文收集表

首轮调查的历史方法比较见 [[pdm-p-joint-broad-survey-20261119]]；
本页和最终原文数据快照保留随后扩大后的测量用途与范围。

## Scope

用户本轮唯一任务是收集Nuclide、Data、References，不做PDM计算，不按PDM是否能处理来筛核。不限制年代和核素，保持E2/M1范围。
同跃迁P/偏振观测量与δ一并保存；P仅作校验的条目如实标明，不能误算为P共同拟合。γγ条件偏振、低温取向及入射束偏振均保留原文对象和级联。
同文多个核素、同一跃迁不同δ分支、引用前人值和不同方法估计均不等于独立实验；缺失量不补零，图示不估读。
总索引与证据边界：[[polarization-delta-collection-20261119-source]]。

## Nuclide

|核素|文献|原文方法|P用途|σ/I报道|数值|原文处理|位置|
|---|---|---|---|---|---|---|---|
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|NRF（核共振荧光），利用HIγS线偏振单能γ射线束照射硼靶，测量散射γ射线的偏振分析能力A(θ=90°)与角分布强度比R=W(135°,90°)/[W(90°,180°)+W(90°,90°)]，并通过贝叶斯后验概率密度提取E2/M1混合比δ；同时修正相位定义错误对Rusev et al. (2009)实测偏振不对称度a=-A(90°)进行蒙特卡洛重分析|联合拟合|不采用该参数（NRF共振荧光实验直接从基态光吸收激发，不存在粒子在束布居的高斯自旋投影分布参数sigma/I）||不适用|Sec. II, Sec. IV, Tab. II, Tab. III, App. B|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|线偏振光子束NRF；用散射方位不对称a提取δ；Table I另列引用文献δ。|入射束偏振/方位角分析|不采用高斯σ/I；光子吸收–退激角关联。||原文使用自旋序列的角分布和固角修正C(θ)。|Table I p.3；Eq.(2) p.2；正文p.4|
|18F|[[polarization-delta-collection-20261119-source#R002\|R002]]|16O(3He, pγ)18F反应，E(3He)=2.95 MeV；在θγ=90°使用单平面Ge(Li)偏振仪测定线偏振P，并用40 cm³ Ge(Li)测定γ角分布（偏振仪晶体具体尺寸60 mm×35 mm×6.5 mm在给出页面中未见）|数值校验|未采用/未报告高斯sigma/I参数。偏振度P直接由实测角分布系数a2、a4与混合比δ按Rose-Brink公式计算，未用高斯分布参数化取向（原文无“阈值附近出射质子l=0使反冲核取向”表述）||未参数化sigma/I；E2/M1 δ明确标注cited_original（源自Ref.10与Ref.5），不能算成新独立实验|Table 2, p. 316-317|
|22Ne|[[polarization-delta-collection-20261119-source#R031\|R031]]|in-beam angular distribution and Compton polarimetry; delta fixed to literature value from Olivier et al. (1993) [41]|数值校验|reported as sigma/Ji|0.33(7)|fitted with delta fixed to literature|Table 1, Table 2, Page 5, 7|
|25Al|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|利用24Mg(p,γ)25Al共振态在90度测量康普顿线偏振度P，结合文献角分布解出的双分支x计算理论P并对比排除|定量选支|不适用高斯σ/I；共振态布居。|不适用|0+靶质子俘获共振，m=±1/2布居；不同于重离子高斯σ/I分析。|Table I, p. 667; Section 5, pp. 668-669|
|25Mg|[[polarization-delta-collection-20261119-source#R031\|R031]]|in-beam angular distribution and Compton polarimetry; delta fixed to literature values from Firestone (2009) [40]|数值校验|reported as sigma/Ji|0.59(3) (1612 keV), 0.58(4) (1793 keV)|fitted with delta fixed to literature|Table 1, Table 2, Page 5, 7|
|25Na|[[polarization-delta-collection-20261119-source#R031\|R031]]|in-beam angular distribution and Compton polarimetry in fusion-evaporation reaction|定量选支|reported as sigma/Ji|0.56(7)|fitted along with delta in Eq. (2)|Table 1, Table 2, Page 4-7|
|31P|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|利用30Si(p,γ)31P共振态在90度测量8.04 MeV跃迁线偏振度P，与文献角分布两分支x计算的P对比|定量选支|不适用高斯σ/I；共振态布居。|不适用|0+靶质子俘获共振，m=±1/2布居；不同于重离子高斯σ/I分析。|Table I, p. 667; Section 5, p. 669|
|33Cl|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|利用32S(p,γ)33Cl共振态在90度测量2.85 MeV跃迁线偏振度P，结合文献角分布确定自旋为5/2+并排除3/2+混合比分支|定量选支|不适用高斯σ/I；共振态布居。|不适用|0+靶质子俘获共振，m=±1/2布居；不同于重离子高斯σ/I分析。|Table I, p. 667; Section 5, p. 669|
|34Cl|[[polarization-delta-collection-20261119-source#R049\|R049]]|RDCO + IPDCO|定量选支|报告了高斯自旋对准参数σ/J = 0.3|0.3|fixed|Table I, Sec. II, Sec. III A|
|35Cl|[[polarization-delta-collection-20261119-source#R007\|R007]]|35Cl(p,p'γ)35Cl反应，Ep=5.11 MeV，使用NaI(Tl)康普顿线偏振计结合Ge(Li)测定部分未分辨的3.00 MeV与3.16 MeV γ射线的线偏振度（Ω=90°与0°计数比N及偏振参数p）|数值校验|未报告高斯分布参数sigma/I（采用共振反应与Compton偏振计测量解析，未拟合高斯磁亚态分布模型）||未采用|Table 1, p. 11-12|
|36Cl|[[polarization-delta-collection-20261119-source#R018\|R018]]|35Cl(n, γ), thermal neutron capture; coincident primary-secondary γ-γ directional correlation and linear polarization correlation using Compton polarimeter at 90°|联合拟合|不采用该参数；热中子俘获经单一2+共振俘获态退激，采用Ferguson (1965) γγ级联方向与偏振关联理论，不适用且不使用高斯磁子步截断参数σ/I||不采用该参数|Table 1, p. 671; Abstract, p. 668; text, p. 670-671|
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|RDCO + RADO + IPDCO|数值校验|报告|σ/J = 0.3|固定|Table I, Sec. II, Sec. III|
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|RDCO + RADO + IPDCO|仅性质校验|已报告数值|0.3|fixed|Table I, p. 5; Sec. II, pp. 2-3|
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|38Ar(α, nγ)41Ca 在线反应，测量角分布与90°康普顿散射线偏振度P(90°)，联合拟合确定Jπ与δ|联合拟合|未采用高斯分布参数sigma/I；初始态取向由统计复合核模型计算磁亚态布居||采用统计复合核模型计算初始态磁亚态布居，拟合中赋予50%（或0.1）误差进行联合极小化|Table 1, Section 2, Section 3|
|45Ti|[[polarization-delta-collection-20261119-source#R020\|R020]]|42Ca(alpha,n)45Ti反应，Ge(Li)测量单gamma角分布与平面型Ge(Li)测量线偏振P|数值校验|原文给出高斯磁子态宽度sigma并自由拟合，未直接采用高斯sigma/I参数化|1.39|自由拟合|Table 2, page 262-263; Section 3.1.2, page 266|
|46Ti|[[polarization-delta-collection-20261119-source#R019\|R019]]|46Ti(p,p'γ)反应，在Ep=5.489和5.508 MeV共振激发，单平面Ge(Li)偏振仪测90°线偏振不对称度A(90°)，配合Ge(Li)角分布|2073 keV联合拟合；2346 keV仅性质校验|不采用该参数。实验在孤立复合核共振态布居，形式体系直接使用Legendre展开系数ak及PW(90°)关联，未报告亦不采用高斯分布sigma/I||not_used|Table 2, Fig. 5, Fig. 8, pp. 276-282|
|47Ti|[[polarization-delta-collection-20261119-source#R020\|R020]]|44Ca(alpha,n)47Ti反应，Ge(Li)测量单gamma角分布与平面型Ge(Li)测量线偏振P|数值校验|原文给出高斯磁子态宽度sigma并自由拟合，未直接采用高斯sigma/I参数化|1.5|自由拟合|Table 4, page 267; Section 3.2, page 270|
|51Cr|[[polarization-delta-collection-20261119-source#R020\|R020]]|48Ti(alpha,n)51Cr反应，Ge(Li)测量单gamma角分布与平面型Ge(Li)测量线偏振P|数值校验|原文给出高斯磁子态宽度sigma并自由拟合，未直接采用高斯sigma/I参数化|1.49, 1.53|自由拟合|Table 9, page 280-281; Section 3.4, page 278-285|
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|50Ti(α, n)53Cr*(γ)反应，Eα=14.2 MeV。测量单γ射线角分布W(θ)及90°线偏振P(90°)。|定量选支|已报告数值|1.07-1.76|拟合自由参数（角分布分析中假设初态磁子态Mi呈高斯分布，磁子态分布宽度σ(Mi)与自旋Ji、混合比δ作为自由参数同时由角分布最小二乘法拟合确定Q^2_min）|Table 1, Section 2, Section 3, Section 4, Fig. 4|
|55Fe|[[polarization-delta-collection-20261119-source#R035\|R035]]|低温核取向（nuclear polarization at low temperatures in cerium-magnesium nitrate crystals）与线偏振测量|定量选支|该实验为低温核取向实验（通过铈镁硝酸盐晶体绝热去磁至约0.003 K低温），不采用束流在束反应的高斯自旋分布截断参数sigma/I，而是采用取向参数Bn描述极化态。||不采用该参数|Table 1, Table 2, Fig. 7, Fig. 10, Page 264, Page 272-276|
|56Fe|[[polarization-delta-collection-20261119-source#R009\|R009]]|低温核取向(NO)结合康普顿散射线偏振计|定量选支|不采用高斯sigma/I参数；基于Tolhoek与Cox的核取向参数fk(I, beta0)，由3.25 MeV纯E2跃迁定出1/T*=250下参考取向参数beta0 = 0.62±0.07(理论计算取0.60)||不适用|Table 2, Table 3, Table 5, Section 5, 6, 7 (p. 71-85)|
|57Ni|[[polarization-delta-collection-20261119-source#R006\|R006]]|γγ DCO + 康普顿散射线偏振不对称度定性校验 (δ源自文献[5] cited_original)|仅性质校验|不采用该参数；实验采用γγ符合DCO比值分析，未引入高斯取向模型参量sigma/I||none|Table 1, Fig. 4, text p. 379 [cited_original: Rudolph1999_EPJA4]|
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|角分布/中子–γ角关联与实测P综合限制δ和自旋；采用布居约束。|联合约束|未给σ/I；使用其他布居约束。||符合分析假定m=±1/2；单谱用统计模型限制布居，不等同高斯σ/I固定。|Section 2.2, Section 2.3, Table 1, Figs. 3-7|
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|角分布系数＋P联合拟合，并加入复合核模型取向约束。|联合约束|未给σ/I；使用其他布居参数。|未给σ/I|δ与布居参数β、x联合拟合；模型给出取向约束。|p. 36, Section 2; Table 3, pp. 40-41; Table 4, p. 42|
|65Cu|[[polarization-delta-collection-20261119-source#R005\|R005]]|65Cu(γ,γ')共振荧光散射，结合Ge(Li)角分布与NaI(Tl)康普顿散射偏振仪不对称比测量|定量选支|不采用该参数；该实验为光核共振荧光弹性散射(γ,γ')，初态取向由吸收步几何自旋耦合确定，不采用重离子在束高斯sigma/I模型||不采用该参数|p. 78-80, Fig. 2|
|67Ge|[[polarization-delta-collection-20261119-source#R024\|R024]]|在束γ谱学(57Fe(12C,2nγ)67Ge)，Ge(Li)测量角分布，三晶体康普顿散射计测量线偏振P(90°)|仅性质校验|未报告||未说明拟合中高斯布居参数sigma/I的具体取值或处理方式|Table 2, Section 3.5, Fig. 8|
|72Se|[[polarization-delta-collection-20261119-source#SE22\|SE22]]|ANGCOR计算响应，P–DCO联合χ²拟合。|联合拟合|明确给出σ/j=0.3。|0.3|由本实验E1跃迁标定后固定。|Table I、II；方法p.7；Fig.7、p.8。|
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|70Ge(alpha, n)在束gamma谱学，8角度角分布与康普顿散射线偏振度P_exp联合拟合|联合拟合|报告了磁子能级分布宽度sigma，在卡方极小化中与混合比delta同时变动拟合；图3单独给出了430.5 keV跃迁的sigma拟合值，但表1未单独列出各跃迁的sigma数值|430.5 keV给出sigma=1.8(+0.5,-0.6)，其余跃迁未单独列出具体数值|自由拟合/小区间内变动|p.142-143 Sect. 2.1, Eq. (4), Fig. 3, Table 1|
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|P与ADO理论响应联合比较提取δ。|联合约束|所查正文及SI未报告σ/I数值。||未报告σ/I数值及最终处理，不据此判为固定。|正文pp.2–3 Fig.3；SI pp.1–2 Table I|
|79Kr|[[polarization-delta-collection-20261119-source#R027\|R027]]|在束γ谱学：单γ角分布测量与康普顿平板Ge(Li)探测器线偏振测量；δ由单γ角分布结合角分布衰减修正提取，实测Pexp用于与由A2/A4/δ导出的Pad进行数值对比校验|数值校验|正文未报告数值||未报告高斯sigma/I参数或数值；Table 1注脚e说明在提取δ时考虑了角分布衰减(taking into account the attenuation of the angular distribution)|Table 1, Table 2, p.553-557|
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|实测P与RDCO理论曲线联合比较提取δ（包括ΔI=0与1）。|联合约束|所查正文未报告σ/I数值。||未报告|Table 1, Fig. 2, text on p. 3-4|
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|在束γ谱学，80Se(α,3n)81Kr反应，测量单γ角分布与平面Ge探测器线偏振P_exp，由角分布系数提取多极混合比δ，并与理论偏振度P_ad进行数值对比校验多极性及宇称|数值校验|原文未给出高斯分布参数sigma或sigma/I的具体数值，仅在Table 2注c中说明考虑了角分布衰减(attenuation)||未给出具体参数，仅说明Table 2混合比计算时考虑了角分布衰减|Table 1, Table 2, p. 209-212|
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|in-beam gamma-ray spectroscopy: angular distributions and linear polarization via 82Se(alpha, 2n) reaction|数值校验|attenuation coefficients alpha2 = 0.55 and alpha4 = 0.15 used for alignment normalization; Gaussian sigma/I not used/reported||fixed attenuation coefficients alpha2 = 0.55 and alpha4 = 0.15 adopted from systematics and statistical model calculations|Table 1, Table 2, Section 2.1|
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|γγ(θ)方向关联与γγ(90° LP)线偏振-方向关联|定量选支|不采用该参数（放射性衰变γγ级联关联测量，不涉及反应在束高斯自旋截止参数sigma/I）||不适用|Table 1, Table 2, Table 3, Section 2, Section 3|
|105Pd|[[polarization-delta-collection-20261119-source#T19\|T19]]|DCO给出δ候选，定量P–DCO比较选择分支；不是同时自由拟合。|定量选支|正文未给σ/I数值；标定取向衰减系数。|未报告具体sigma/I数值|用1100-keV E2与1331-keV E1标定不完全取向衰减系数；未报告σ/I参数化。|第2页、第3页、第5页Table I及第3页Fig. 2|
|111Cd|[[polarization-delta-collection-20261119-source#R003\|R003]]|γγ方向偏振关联 (γ-γ linear polarization correlation)|定量选支|不采用该参数 (111In放射性衰变布居γγ关联，不涉及在束高斯布居参数sigma/I)||不采用该参数|p.51-53, Section 3, Section 4, Fig. 2, Fig. 3|
|112In|[[polarization-delta-collection-20261119-source#R025\|R025]]|112Cd(p,nγ)112In在束反应，测量γ射线角分布与90°康普顿散射线偏振Pexp，结合统计复合核模型(Hauser-Feshbach)提取与检验自旋宇称及混合比|数值校验|不采用高斯平滑对齐参量sigma/I；统计张量由Hauser-Feshbach统计复合核理论程序结合DWUCK4光学势透射系数直接计算||not_used|Table 2, p. 499 (PDF page 7); Section 2.4, 2.5, 3.2, Fig. 4i|
|116Sn|[[polarization-delta-collection-20261119-source#R032\|R032]]|114Cd(α,2n)116Sn反应，E(α)=34 MeV，在束γ射线谱学，利用INGA三叶草探测器阵列测量γγ符合、DCO比值(RDCO)与线偏振不对称度(asym)|仅性质校验|报告了σ/J = 0.37|0.37|固定/输入值（与文献中同类α束流实验一致，作为ANGCOR程序输入参数计算理论RDCO曲线）|Table 1, Section 3, Section 4.2|
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|in-beam γ-ray spectroscopy (JuroGam 3 + MARA), prompt γ-γ-γ coincidences, directional correlations (RDCO, Rac), angular distribution (a2, a4), and linear polarization asymmetry (Ap)|未说明|正文未报告数值||not_reported|Table I, pages 15-19|
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|在束γ谱学(重离子聚变蒸发反应)，JUROGAM 3阵列测量DCO比值、角关联各向异性Rac、角分布系数a2/a4以及Clover探测器线偏振不对称度AP|未说明|正文未报告数值||未报告|Table II|
|122Te|[[polarization-delta-collection-20261119-source#R010\|R010]]|γγ direction-polarization correlation|定量选支|不采用该参数。本实验为Sb-122放射性衰变γγ方向-偏振关联测量，中间态核取向由前级跃迁退布居确定，不涉及在束核反应的高斯自旋截面分布参数sigma/I||不采用该参数|Section 3, p. 501; Fig. 4, p. 499|
|125Sb|[[polarization-delta-collection-20261119-source#R023\|R023]]|γγ方向关联与γγ线偏振-方向关联测量(γ-γ(90° LP))|数值校验|不采用该参数；实验为放射性衰变(125Sn衰变)γγ级联方向关联与偏振关联，不涉及在束核反应高斯自旋取向sigma/I参数||不适用|Table 2, Table 3, p.373-379|
|125Te|[[polarization-delta-collection-20261119-source#R012\|R012]]|低温核取向(NO)结合康普顿线偏振计与方向各向异性测量|联合拟合|不采用该参数；低温核取向实验直接测定统计张量与角分布系数乘积ρ2A2=-0.3638±0.0025与ρ4A4=-0.0024±0.0029，并给出温度T=7 mK及去取向参数U2、U4范围||不采用高斯sigma/I参数化（低温核取向体系，由热力学玻尔兹曼分布及去取向系数描述，实验直接测定ρ2A2与ρ4A4）|p.225-226, Section 4, Fig. 6|
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|in-beam γ-spectroscopy, 122Te(α, n) and 123Te(α, 2n); γ-angular distribution, γ-linear polarization (POLALI), γγ-DCO|数值校验|未在数据表中逐跃迁报告具体σ数值；正文和图4、图5说明采用高斯磁子态分布，σ作为自由参数与δ同时变动以最小化χ2||varied / fitted|Table 3, Table 4, Section 2.3, pages 80-84, 96-97|
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|DCO确定δ候选及误差；定量P选择483-keV大δ分支。|定量选支/性质校验|所获正文及SI未给σ/I数值。||正文采用ANGCOR；SI未补充σ/I数值或处理说明。|Page 3, Table 1; Page 3, Fig. 3|
|129Ba|[[polarization-delta-collection-20261119-source#R047\|R047]]|重新拟合既有角分布；引用Gizon1978实测P作一致性对照，不是新P实验。|数值校验（转引既有P）|未报告 (重分析理论角分布曲线，未给出高斯分布sigma/I参数的具体数值)||未说明|p. 3, Fig. 2, Fig. 3|
|131Xe|[[polarization-delta-collection-20261119-source#R045\|R045]]|在束γ谱学，130Te(4He, 3nγ)反应，利用7台Clover探测器组成的INGA阵列测量RDCO与线偏振不对称度asym|仅性质校验|未报告||未说明|Table I, Fig. 4, Fig. 5, Sec. III pp. 3-4|
|132Ce|[[polarization-delta-collection-20261119-source#R037\|R037]]|在束γ谱学（EUROGAM II阵列，100Mo(36S,4nγ)反应，E=155 MeV）。通过非对称几何HPGe同轴探测器对的γγ方向关联函数W(θ1, θ2, Δϕ)经GCORR程序拟合提取E2/M1多极混合比δ；利用24台四叶草Clover探测器作为康普顿偏振仪测量线偏振度P以校验/确认跃迁的多极性特征（电/磁性质校验）。|仅性质校验|不采用该参数（文中使用GCORR程序直接拟合EUROGAM II非对称探测器几何关联函数W(θ1, θ2, Δϕ)与重合计数，未采用或报告一维高斯取向参量σ/I）。||不采用该参数|Table 2, Table 4, Fig. 3, Fig. 4, Sec. 3.2, p. 180, 184-187|
|132Xe|[[polarization-delta-collection-20261119-source#R039\|R039]]|γγ方向-偏振关联 (directional-polarization correlation using EXILL clover polarimeters)|联合拟合|不采用高斯sigma/I参数；未取向初态裂变产物132I的β-衰变，由级联首光子取向参数Bk(γ1)定量描述中间态取向|||Table 1, Table 5, Figure 9(a), Section 4|
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|R_DCO与偏振不对称度asym(配Q校准)二维等高线图联合拟合提取δ|联合拟合|所查正文未给σ/I数值。||未报告|PLB 823 (2021) 136756, Page 2-4, Table 1, Table 2, Fig. 4|
|133Cs|[[polarization-delta-collection-20261119-source#R039\|R039]]|γγ方向-偏振关联 (directional-polarization correlation using EXILL clover polarimeters)|定量选支|不采用高斯sigma/I参数；133Ba放射源衰变，未取向初态，由级联首光子取向参数Bk(γ1)定量描述中间态取向|||Table 1, Table 5, Section 4|
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|RDCO与Polarization联合轮廓线拟合，辅以角分布拟合对比|联合约束|已报告|0.3|假定固定|p.3 σ/I假定及联合方法；Table 1；Fig.4(g–i)|
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|在束γ谱学，重离子融合蒸发反应100Mo(40Ar, 5n)135Nd，JUROGAM II探测器阵列测定角分布、RDCO比值与Clover探测器线偏振不对称度AP|仅性质校验|正文未报告数值||未报告高斯sigma/I或自旋取向参数|Table I, Table II, Figs. 5, 6|
|135Pr|[[polarization-delta-collection-20261119-source#L22\|L22]]|P–Rac联合求中心值，再沿观测误差边界扫描求区间。|联合约束|说明了求解方式，未列最终σ/I数值。|未列最终值|中心值与δ联合求解；扫描响应曲线传播误差。|主文Table 1/Fig.2；补充材料pp.1、4–5。|
|135Pr|[[polarization-delta-collection-20261119-source#R051\|R051]]|在束γ射线角分布 + 康普顿散射线偏振不对称度测量|仅性质校验|正文未报告数值||未报告|Table I, Fig. 2, Fig. 3, text pp. 3-4|
|136Nd|[[polarization-delta-collection-20261119-source#ND22\|ND22]]|P–Rac响应曲线与实验点联合提取。|联合约束|主文未明确给出σ/I数值。|未给出|主文未具体交代取向处理，引用既有方法。|主文Sec.II–III、Fig.3；实验方法Ref.[38]。|
|144Nd|[[polarization-delta-collection-20261119-source#R011\|R011]]|低温取向＋线偏振；原文仅确定\|δ\|，未选择符号。|联合约束|不采用高斯sigma/I参数。实验为绝热去磁低温取向核系统，由有效自旋哈密顿量计算对齐参数f2=0.348、f4=0.033，结合热中子俘获去取向因子G2=35/36、G4=343/432及级联衰变级数nu进行角各向异性和偏振分析||不采用该参数|PDF p.1 Synopsis, p.9 Table IV, p.10-13 Fig. 6, p.17 Table VI|
|145Ba|[[polarization-delta-collection-20261119-source#R030\|R030]]|EUROGAM Phase II三叶草（Clover）探测器阵列测量248Cm自发裂变符合γ射线，结合三重角关联DCO1与Clover康普顿散射线偏振关联Pexp，联合确定基态带ΔI=1 M1/E2跃迁的混合比δ|联合拟合|不采用该参数。248Cm自发裂变未测裂变碎片方向，初态磁子能级视为均匀无规布居（uniform/random magnetic substate population），不使用高斯取向参数sigma/I||不采用该参数|Table 9, Table 8b, Table 6b, Table 6c, Section 3, Section 4.2|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|RDCO–P联合χ²拟合；另报告DCO法及二法平均δ。|联合拟合|报告σ/j≈0.35。|0.35|以纯E1实测DCO标定σ/j≈0.35，后续计算采用该值。|PDF page 4, 6; Table I, Fig. 5-10|
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|γγ方向-偏振关联 (directional-polarization correlation using EXILL clover polarimeters)|数值校验|不采用高斯sigma/I参数；152Eu源EC+β+衰变，未取向初态，由级联首光子取向参数Bk(γ1)定量描述中间态取向|||Table 4, Table 6, Table 7, Section 5.1|
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|在束γ-γ符合DCO方向关联与Clover探测器IPDCO线偏振不对称度测量|仅性质校验|原文明确报告采用自旋取向参数σ/J = 0.3，由前期文献[26-29]指导并经BRICC检验确定|σ/J=0.3|fixed|Table I, Section II A, Section II B|
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|in-beam gamma-ray spectroscopy, R_DCO and Clover Compton linear polarization (P)|联合拟合|正文未报告数值||原文使用ANGCOR程序计算理论RDCO与P轮廓，未报告所采用的高斯自旋取向参数sigma/I|PDF page 8, Table 1; PDF pages 6-7, Section 3|
|163Lu|[[polarization-delta-collection-20261119-source#R052\|R052]]|DCO + 角分布 + Clover探测器线偏振测量|仅性质校验|已报告数值|0.25±0.02|对同自旋区强E2跃迁拟合得到平均值0.25±0.02，无明显自旋依赖|Page 5867-5869, Table I|
|166Er|[[polarization-delta-collection-20261119-source#R036\|R036]]|低温核取向(Nd-ethyl-sulphate中166mHo超精细结构取向) + 康普顿散射线偏振测量|仅性质校验|低温核取向实验，不采用高斯分布参数sigma/I；取向度由超精细结构参数A/k及玻尔兹曼布居决定，完全取向极限下计算取向参数fk(I)|||p. 675, 678, 680-681, 684|
|172Yb|[[polarization-delta-collection-20261119-source#R014\|R014]]|γγ方向关联与γγ线偏振关联 (liquid source, 172Lu decay)|数值校验|不采用该参数；实验为放射性衰变γγ关联测量（液体源），取向由首跃迁辐射决定，不涉及重离子在束反应的高斯自旋分布截断参量sigma/I||不采用该参数|Abstract; Sect.3, p.73; Sect.4, p.75; Sect.6, p.78-80; Fig.13, Fig.14, Fig.15|
|177Ta|[[polarization-delta-collection-20261119-source#R008\|R008]]|in-beam (α,2nγ), Compton linear polarimeter + angular distribution|联合拟合|正文未报告数值||不采用高斯分布参数sigma/I；角分布直接拟合得到ρkAk，在与偏振不对称度B联立求H2(12)时统计张量ρk相互对消|Page 423-426, Section 3.2, Fig. 6, Fig. 8|
|181Ta|[[polarization-delta-collection-20261119-source#R013\|R013]]|γγ方向关联与γγ线偏振关联联合测量 (Compton scattering summing polarimeter + NaI(Tl) detectors, 181Hf radioactive decay)|联合拟合|不采用该参数 (本工作为181Hf放射性衰变γγ级联关联实验，中间态取向由第一级跃迁及环境扰动因子Gk决定，且在方向关联与线偏振关联的比值联立方程中完全对消，不涉及在束高斯布居sigma/I参数)||不采用该参数|Page 65, Abstract; Pages 70-78, Sections 5-8, Tables 2, 3, Fig. 6|
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|P + RDCO联合分析|联合约束|所查正文未给σ/I数值。||未报告|Fig. 1, Fig. 2|
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|在束γ谱学，RDCO与线偏振度P联合测量|联合拟合|正文未报告数值||未报告|Table 1, Fig. 4, text on pp. 2-3|
|187Au|[[polarization-delta-collection-20261119-source#G22\|G22]]|P–Rac联合允许区间：逐取向计算曲线，合并允许解。|联合约束|有不同取值曲线；不指定最终单值。|例：0.2、0.3（图示）|扫描不同σ/I并合并区间；图示数值不是扫描边界。|主文Fig.3、p.3；补充材料pp.1–4/Fig.2。|
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|in-beam γ-ray spectroscopy, Compton polarimeter (clover detectors) + DCO|联合拟合|已报告数值|0.3|fixed|Table 1; Section 2.1, 2.2, Pages 2-4|
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|192Ir衰变γγ角关联和γ–线偏振γ条件关联；原文分别报告角关联、偏振和综合δ。|联合约束|不采用高斯σ/I；放射性衰变级联。||通过级联角关联条件取向，不是重离子高斯布居分析。|Table 2 p.172；正文p.175；Figs.4–5|
|192Pt|[[polarization-delta-collection-20261119-source#R004\|R004]]|Low-temperature nuclear orientation (SPIN facility at T=15 mK, B=0.8 T) combined with Compton polarimeter linear polarization measurement|联合拟合|不采用高斯sigma/I参数；实验为超低温稀释制冷机铁基质核取向(T=15(1) mK, B_ext=0.8 T)，由超精细相互作用玻尔兹曼分布与标准核取向Bk系数描述||不采用该参数|Table 1, Page 42|
|194Pt|[[polarization-delta-collection-20261119-source#R016\|R016]]|γγ方向关联 + γ线偏振γγ方向关联校验 (NaI + Ge(Li) summing polarimeter, 194Au放射性衰变)|数值校验|不采用该参数 (194Au放射性衰变γγ角关联，中间态2+寿命约50 ps，无在束高斯对准分布参量sigma/I)||不适用|Table 1, Table 2, p.261-262|
|196Pt|[[polarization-delta-collection-20261119-source#R016\|R016]]|γγ方向关联 + γ线偏振γγ方向关联校验 (NaI + Ge(Li) summing polarimeter, 196Au放射性衰变)|数值校验|不采用该参数 (196Au放射性衰变γγ角关联，中间态2+寿命约50 ps，无在束高斯对准分布参量sigma/I)||不适用|Table 1, Table 2, p.261-262|
|211Bi|[[polarization-delta-collection-20261119-source#R015\|R015]]|γγ方向关联与康普顿散射线偏振关联测量|定量选支|不采用该参数（放射性衰变γγ级联关联实验，中间态取向由初级跃迁角分布及角动量耦合决定，不涉及在束高斯布居参数sigma/I）||不适用|Table 1 (p. 590), Section 4 (p. 592-594), Section 5 (p. 594-598)|
|215Po|[[polarization-delta-collection-20261119-source#R017\|R017]]|α-γ线偏振关联测量（Compton polarimeter）、α-γ及γ-γ方向关联测量、橙型谱仪内转换电子谱测量|定量选支|不采用该参数（放射性α衰变体系，取向由α分波混合L描述，非束流高斯σ/I）||不适用|p.456-470, Section 2, 3, Table 1-4, Fig. 1, 10, 11|

## Original Data

数值列与完整字段保存在机器可读文件；下表同步原文事实以供知识检索。误差为作者给出的正绝对偏移，未给中心的区间不造中心；无穷边界与原文分支状态保留。
|核素|文献|Eγ keV|Jiπ→Jfπ|δ原文|P原文|偏振观测量|角输入|取向参数|门/级联|原文位置|其他原文输入|
|---|---|---|---|---|---|---|---|---|---|---|---|
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|2895.3|3/2-→1/2-|−1.39+0.18−0.22||-0.37(5)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|2895.3|3/2-→1/2-|−0.08+0.06−0.08||-0.37(5)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4444.03|5/2-→3/2-|−2.90+0.13−0.18||+0.026(19)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4444.03|5/2-→3/2-|−0.511+0.011−0.017||+0.026(19)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4444.03|5/2-→3/2-|+0.172 ± 0.020||+0.026(19)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4444.03|5/2-→3/2-|+2.13 ± 0.06||+0.026(19)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4474.5|5/2-→5/2-|+0.72 ± 0.40|入射束≥99%|+0.25 ± 0.06|0.32 ± 0.03|||Tab. II, Sec. IV B, Fig. 7||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4474.5|5/2-→5/2-|< −2.1||-0.19(7)||||Tab. III, App. B, 原文被排除分支||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4474.5|5/2-→5/2-|−0.72+0.16−0.24||-0.19(7)||||Tab. III, App. B, 原文被排除分支||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4474.5|5/2-→5/2-|−0.08 ± 0.14||-0.19(7)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|4474.5|5/2-→5/2-|+1.7 ± 0.7||-0.19(7)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|5018.98|3/2-→3/2-|−0.055 ± 0.023||+0.200(16)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|8916.59|5/2-→3/2-|-0.023 ± 0.009|入射束≥99%|-0.23 ± 0.01|0.63 ± 0.01|||Tab. II, Sec. IV A, Fig. 6||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|8916.67|5/2-→3/2-|−6.7+0.9−1.8||+0.215(20)||||Tab. III, App. B, 原文被排除分支||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|8916.67|5/2-→3/2-|−0.387 ± 0.019||+0.215(20)||||Tab. III, App. B, 原文被排除分支||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|8916.67|5/2-→3/2-|−0.001 ± 0.028||+0.215(20)||||Tab. III, App. B||
|11B|[[polarization-delta-collection-20261119-source#R044\|R044]]|8916.67|5/2-→3/2-|+3.06+0.28−0.19||+0.215(20)||||Tab. III, App. B, 原文被排除分支||
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|2895.21|3/2-→1/2-|-0.19 (+0.10,-0.17)|入射束Pγ：nearly100%|a=-0.37(5)（散射方位不对称）||||Table I δd（本实验）p.3；Eq.(2) p.2；p.4|C(90°)=0.969；εh/εv=1.011(10)（Eq.1–2, pp.2,4）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|2895.21|3/2-→1/2-|-0.05(20)|入射束Pγ：nearly100%|a=-0.37(5)（散射方位不对称）||||Table I δe（转引文献值，Krane–Steffen约定）, p.3|C(90°)=0.969；εh/εv=1.011(10)（本实验入射/探测设置）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|4443.93|5/2-→3/2-|+0.158 (+0.025,-0.021)|入射束Pγ：nearly100%|a=0.026(19)（散射方位不对称）||||Table I δd（本实验）p.3；Eq.(2) p.2；p.4|C(90°)=0.95；εh/εv=1.011(10)（Eq.1–2, pp.2,4）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|4443.93|5/2-→3/2-|+0.19(3)|入射束Pγ：nearly100%|a=0.026(19)（散射方位不对称）||||Table I δe（转引文献值，Krane–Steffen约定）, p.3|C(90°)=0.95；εh/εv=1.011(10)（本实验入射/探测设置）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|4474.3|5/2-→5/2-|-0.061 (+0.025,-0.022)|入射束Pγ：nearly100%|a=-0.188(7)（散射方位不对称）||||Table I δd（本实验）p.3；Eq.(2) p.2；p.4|C(90°)=0.982；εh/εv=1.011(10)（Eq.1–2, pp.2,4）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|5019.08|3/2-→3/2-|-0.036 (+0.013,-0.013)|入射束Pγ：nearly100%|a=0.200(16)（散射方位不对称）||||Table I δd（本实验）p.3；Eq.(2) p.2；p.4|C(90°)=0.941；εh/εv=1.011(10)（Eq.1–2, pp.2,4）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|5019.08|3/2-→3/2-|-0.03 ± 0.05|入射束Pγ：nearly100%|a=0.200(16)（散射方位不对称）||||Table I δe（转引文献值，Krane–Steffen约定）, p.3|C(90°)=0.941；εh/εv=1.011(10)（本实验入射/探测设置）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|8916.3|5/2-→3/2-|0.000 (+0.014,-0.014)|入射束Pγ：nearly100%|a=0.215(20)（散射方位不对称）||||Table I δd（本实验）p.3；Eq.(2) p.2；p.4|C(90°)=0.95；εh/εv=1.011(10)（Eq.1–2, pp.2,4）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|8916.3|5/2-→3/2-|-0.11 ± 0.04|入射束Pγ：nearly100%|a=0.215(20)（散射方位不对称）||||Table I δe（转引文献值，Krane–Steffen约定）, p.3|C(90°)=0.95；εh/εv=1.011(10)（本实验入射/探测设置）|
|11B|[[polarization-delta-collection-20261119-source#R048\|R048]]|8916.3|5/2-→3/2-|-1.30|入射束Pγ：nearly100%|a=0.215(20)（散射方位不对称）||||正文p.4（另一分支；作者采用较小绝对值根）|C(90°)=0.95；εh/εv=1.011(10)|
|18F|[[polarization-delta-collection-20261119-source#R002\|R002]]|1587.0|2+→3+|+0.9±0.6|+23±46%||a2=-0.53±0.03; a4=-0.06±0.06|||Table 2 (footnote e cites Ref. 5)||
|18F|[[polarization-delta-collection-20261119-source#R002\|R002]]|1702.0|1+→1+|+0.50±0.06|0±20%||a2=-0.32±0.07; a4=-0.05±0.11|||Table 2 (footnote c cites Ref. 10)||
|18F|[[polarization-delta-collection-20261119-source#R002\|R002]]|1702.0|1+→1+|+2.0±0.3|0±20%||a2=-0.32±0.07; a4=-0.05±0.11|||Table 2 (footnote c cites Ref. 10)||
|18F|[[polarization-delta-collection-20261119-source#R002\|R002]]|2524.0|2+→1+|+3.0±1.0|-15±30%||a2=0.10±0.06; a4=0.19±0.07|||Table 2 (footnote e cites Ref. 5)||
|22Ne|[[polarization-delta-collection-20261119-source#R031\|R031]]|2166.0|4+→4+|-0.04(3)||A0_fit=+0.030(7)|a2=0.39(5); a4=-0.05(6)|0.33(7)||Table 1, Table 2, Page 5, 7||
|25Al|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|2240.0|3/2+→1/2+|x = 0.06 ± 0.06|0.71 ± 0.17||-0.4 ± 0.1|||Table I, p. 667; Section 5, p. 668||
|25Al|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|2240.0|3/2+→1/2+|x = -2.2 ± 0.5|0.71 ± 0.17||-0.4 ± 0.1|||Table I p.667；p.668（原文P排除的大\|x\|分支）||
|25Al|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|2690.0|3/2+→5/2+|x = 0.35 ± 0.10|0.11 ± 0.14||-0.5 ± 0.1|||Table I, p. 667; Section 5, p. 668||
|25Al|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|2690.0|3/2+→5/2+|x = 11 ± 6|0.11 ± 0.14||-0.5 ± 0.1|||Table I p.667；p.668（原文P排除的大x分支）||
|25Mg|[[polarization-delta-collection-20261119-source#R031\|R031]]|1612.0|7/2+→5/2+|0.189(12)||A0_fit=-0.011(3)|a2=-0.29(1); a4=-0.05(5)|0.59(3)||Table 1, Table 2, Page 5, 7||
|25Mg|[[polarization-delta-collection-20261119-source#R031\|R031]]|1793.0|9/2+→7/2+|0.13(3)||A0_fit=-0.012(3)|a2=-0.23(2); a4=-0.04(5)|0.58(4)||Table 1, Table 2, Page 5, 7||
|25Na|[[polarization-delta-collection-20261119-source#R031\|R031]]|1041.0|9/2+→9/2+|0.0(2)||A0_fit=+0.043(8)|a2=0.20(2); a4=0.00(4)|0.56(7)||Table 1, Table 2, Page 5, 7||
|25Na|[[polarization-delta-collection-20261119-source#R031\|R031]]|1041.0|9/2+→9/2+|-0.85||A0_fit=+0.043(8)|a2=0.20(2); a4=0.00(4)|||Table 1, Page 4-7, 原文被排除分支||
|31P|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|8040.0|3/2+→1/2+|x = 0.06 ± 0.02|-0.38 ± 0.18||-0.37 ± 0.03|||Table I p.667；p.669（原文P不支持的小x分支）||
|31P|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|8040.0|3/2+→1/2+|x = -2.2 ± 0.2|-0.38 ± 0.18||-0.37 ± 0.03|||Table I, p. 667; Section 5, p. 669||
|33Cl|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|2850.0|5/2+→3/2+|x = -0.09 ± 0.03|0.55 ± 0.22|||||Table I, p. 667; Section 5, p. 669||
|33Cl|[[polarization-delta-collection-20261119-source#SU59\|SU59]]|2850.0|3/2+→3/2+|x = -1.4 ± 0.6|0.55 ± 0.22|||||Table I p.667；p.669（被排除的3/2+自旋/x分支）||
|34Cl|[[polarization-delta-collection-20261119-source#R049\|R049]]|1112.0|6-→5-|0.36(6)||-0.03(1)|1.92(17); 1.92(17)|σ/J = 0.3|1256|Table I, Sec. III A (高δ分支>1被实测IPDCO排除)||
|34Cl|[[polarization-delta-collection-20261119-source#R049\|R049]]|2035.0|3+→3+|-0.4(1)||0.04(1)|0.51(8); 0.51(8)|σ/J = 0.3|491|Table I, Sec. III A||
|34Cl|[[polarization-delta-collection-20261119-source#R049\|R049]]|2229.0|4+→3+|0.4(1)||-0.09(3)|0.90(9); 0.90(9)|σ/J = 0.3|491|Table I, Sec. III A (高δ分支>1被实测IPDCO排除)||
|34Cl|[[polarization-delta-collection-20261119-source#R049\|R049]]|2840.0|6+→7+|-0.3(1)||-0.02(1)|0.83(12); 0.83(12)|σ/J = 0.3|491|Table I, Sec. III A||
|35Cl|[[polarization-delta-collection-20261119-source#R007\|R007]]|3000.0|→|-0.02 <= δ <= 0.09|0.37 <= p <= 0.58|0.88 ± 0.03||||Table 1, p. 12||
|35Cl|[[polarization-delta-collection-20261119-source#R007\|R007]]|3160.0|→|-0.31 <= δ <= -0.21|0.09 <= p <= 0.46|0.82 ± 0.06||||Table 1, p. 12||
|36Cl|[[polarization-delta-collection-20261119-source#R018\|R018]]|790.0|3+→2+|-1.1 ± 0.4|-0.07 ± 0.02||A2 = +0.044 ± 0.004; A4 = +0.016 ± 0.006; R = -0.244 ± 0.027||coincident primary γ-ray (C -> 0.79 MeV)|Table 1, p. 671; Abstract, p. 668; p. 670||
|36Cl|[[polarization-delta-collection-20261119-source#R018\|R018]]|1170.0|1+→2+|0.32 ± 0.06|-0.11 ± 0.06||A2 = +0.037 ± 0.002; A4 = +0.001 ± 0.002; R = +0.45 ± 0.06||coincident primary γ-ray (C -> 1.17 MeV)|Table 1, p. 671; Abstract, p. 668; p. 670||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|323.0(6)|15/2+→13/2+|0.08(3)||-0.07(1)|0.52(3); 0.79(4); 0.52(3)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|521(1)|11/2-→9/2-|0.02(2)||-0.10(2)|0.42(3); 0.68(9); 0.42(3)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|598.2(7)|17/2+→15/2+|0.01(2)||-0.05(1)|0.46(3); 0.76(4); 0.46(3)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|746(2)|11/2-→9/2-|-0.04(7)||-0.08(3)|0.39(8); 0.57(12); 0.39(8)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|779(2)|(13/2-)→11/2-|-0.07+0.09-0.11||-0.07(4)|0.37(9); 0.48(8); 0.37(9)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|936.8(6)|13/2+→11/2+|0.15+0.02-0.03||-0.05(1)|0.64(4); 0.91(4); 0.64(4)|σ/J = 0.3|2217|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|1166(1)|9/2-→11/2-|-0.14(8)||-0.07(2)|0.61(8); 0.61(8)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|1573.8(8)|9/2-→7/2-|0.47+0.10-0.09||-0.09(1)|0.93(13); 1.56(13); 0.93(13)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|1912(2)|11/2-→11/2-|-0.38+0.30-0.25||0.05(2)|0.72(16); 0.90(16); 0.72(16)|σ/J = 0.3|1611|Table I, p. 044310-5||
|37Ar|[[polarization-delta-collection-20261119-source#R040\|R040]]|2019(3)|19/2+→17/2+|-0.01+0.09-0.11||-0.02(1)|0.86(18); 0.93(17); 0.86(18)|σ/J = 0.3|681|Table I, p. 044310-5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|335.5|6+1→7+1|+0.01(2)||-0.04(7)|0.92(9); 0.93(7); 0.92(9)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|519.3|7+2→6+2|-0.19+0.10-0.13||-0.11(9)|0.57(11); 0.55(9); 0.57(11)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|558.7|9-1→8-2|+0.03(6)||-0.11(7)|0.84(8); 0.88(8); 0.84(8)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|810.4|6+2→7+1|+0.06+0.10-0.11||-0.10(8)|0.89(16); 0.99(13); 0.89(16)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|891.0|5-1→4-1|+0.14+0.12-0.10||-0.07(1)|0.63(4); 0.91(5); 0.63(4)|σ/J = 0.3|1651.5|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|916.6|8+2→8+1|-0.20(37)||+0.14(9)|1.42(25); 1.32(21); 1.42(25)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|1079.7|9-1→8-1|-0.17+0.10-0.13||-0.17(9)|0.6(1); 0.71(9); 0.6(1)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|1244.8|10-2→10-1|-0.27+0.30-0.34||+0.03(5)|2.06(23); 1.67(18); 2.06(23)|σ/J = 0.3|1351.2|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|1329.2|7+2→7+1|-0.28(35)||+0.15(8)|1.35(24); 1.15(19); 1.35(24)|σ/J = 0.3|891|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|1579.8|10-2→9-1|-0.05(8)||-0.10(9)|0.77(11); 1.07(11); 0.77(11)|σ/J = 0.3|2269.2|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|1767.4|11-1→10-1|-0.64(24)||-0.14(6)|0.51(13); 0.42(6); 0.51(13)|σ/J = 0.3|1351.2|Table I, p. 5||
|40K|[[polarization-delta-collection-20261119-source#R046\|R046]]|1822.9|8+1→7+1|-0.01(6)||-0.08(2)|0.79(9); 0.87(9); 0.79(9)|σ/J = 0.3|891|Table I, p. 5||
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|168.0|11/2+→9/2+|Fig. 3|P(90°) = -0.24 ± 0.06||a2 = -0.33 ± 0.01; a4 = 0.00 ± 0.01|||Table 1, Section 3.2, Fig. 3||
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|718.0|9/2-→7/2-|0.19 +0.09 -0.05|P(90°) = -0.33 ± 0.13||a2 = -0.17 ± 0.05; a4 = 0.49 ± 0.26|||Table 1, Section 3.3||
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|2576.0|5/2-→7/2-|1.48 ± 0.11|P(90°) = -0.69 ± 0.07||a2 = 0.30 ± 0.01; a4 = 0.00 ± 0.01|||Table 1, Section 3.1||
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|2576.0|5/2-→7/2-|0.36 ± 0.08|P(90°) = -0.69 ± 0.07||a2 = 0.30 ± 0.01; a4 = 0.00 ± 0.01|||Table 1, Section 3.1||
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|3677.0|9/2-→7/2-|1.28 ± 0.02|P(90°) = 0.32 ± 0.08||a2 = -1.06 ± 0.01; a4 = 0.34 ± 0.01|||Table 1, Section 3.3, Fig. 4||
|41Ca|[[polarization-delta-collection-20261119-source#R038\|R038]]|4343.0|9/2-→7/2-|Fig. 5|P(90°) = 0.25 ± 0.31||a2 = 0.25 ± 0.02; a4 = 0.34 ± 0.02|||Table 1, Section 3.4, Fig. 5||
|45Ti|[[polarization-delta-collection-20261119-source#R020\|R020]]|1353.6|9/2-→7/2-|+0.51 +0.18/-0.08|-0.3 +0.3||a2=-0.827+-0.028; a4=+0.002+-0.046|||Table 2, page 262||
|46Ti|[[polarization-delta-collection-20261119-source#R019\|R019]]|2073.0|2+→2+|- 3.1 ± 0.9|Fig. 5|3.2 ± 1.1 %|a2 = 0.445 ± 0.016; a4 = -0.016 ± 0.020|||Table 2, Fig. 5, p. 276, 278||
|46Ti|[[polarization-delta-collection-20261119-source#R019\|R019]]|2346.0|2+→2+|- 0.10 ± 0.14|Fig. 8|-1.0 ± 1.6 %|a2 = 0.188 ± 0.018; a4 = 0.012 ± 0.023; Fig. 8|||Table 2, Fig. 8, p. 276, 282||
|47Ti|[[polarization-delta-collection-20261119-source#R020\|R020]]|821.5|17/2-→15/2-|-0.03+-0.03|-0.3 +0.5||a2=-0.219+-0.007; a4=+0.014+-0.008|||Table 4, page 267||
|51Cr|[[polarization-delta-collection-20261119-source#R020\|R020]]|905.3|13/2-→11/2-|+0.07+-0.02|-0.4 -0.1||a2=-0.383+-0.006; a4=-0.005+-0.011|||Table 9, page 281||
|51Cr|[[polarization-delta-collection-20261119-source#R020\|R020]]|1164.6|9/2-→7/2-|+0.17 +0.02/-0.01|-0.4 -0.1||a2=-0.503+-0.006; a4=-0.001+-0.009|||Table 9, page 280||
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|530.2|7/2-→5/2-|+0.07±0.03|-0.45 -- -0.25||a2=-0.298±0.013; a4=-0.019±0.017|sigma=1.50||Table 1||
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|593.8|11/2-→9/2-|+0.11±0.04|-0.20 -- +0.20||a2=-0.384±0.010; a4=-0.062±0.014|sigma=1.76||Table 1||
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|696.4|9/2-→7/2-|+0.17±0.03|-0.15 -- +0.15||a2=-0.462±0.009; a4=+0.009±0.011|sigma=1.67||Table 1||
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|766.0|13/2-→11/2-|+0.14±0.05|-1.30 -- -0.33||a2=-0.501±0.010; a4=+0.015±0.014|sigma=1.62||Table 1||
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|1006.3|5/2-→3/2-|-0.36±0.02|-0.69 -- -0.34||a2=+0.128±0.008; a4=+0.002±0.008|sigma=1.60||Table 1||
|53Cr|[[polarization-delta-collection-20261119-source#R021\|R021]]|1006.3|3/2-→3/2-|-4.7±0.8|-0.69 -- -0.34||a2=+0.128±0.008; a4=+0.002±0.008|sigma=1.07||Table 1, 原文被排除分支||
|55Fe|[[polarization-delta-collection-20261119-source#R035\|R035]]|935.0|5/2-→3/2-|+0.36±0.11|P_L（原文计算）=+0.21±0.02|实测P_L Q_L：Fig.10|0.15|||Page 264, Page 276||
|55Fe|[[polarization-delta-collection-20261119-source#R035\|R035]]|935.0|5/2-→3/2-|+0.37±0.07|P_L（原文计算）=+0.21±0.02|实测P_L Q_L：Fig.10|0.15|||Table 1||
|55Fe|[[polarization-delta-collection-20261119-source#R035\|R035]]|935.0|5/2-→3/2-|+15±6|P_L（原文计算）=-0.02±0.02|实测P_L Q_L：Fig.10|0.15|||Table 1 (原文被排除分支)；原文被排除的大δ备选根||
|55Fe|[[polarization-delta-collection-20261119-source#R035\|R035]]|1410.0|5/2-→3/2-|+0.7±0.1|P_L（原文计算）=+0.14±0.02|实测P_L Q_L：Fig.10|0.22|||Table 2 (原文被排除分支)；备选M1/E2自旋假设，原文最后判定该γ为纯E2||
|55Fe|[[polarization-delta-collection-20261119-source#R035\|R035]]|1410.0|5/2-→3/2-|+3.0±0.5|P_L（原文计算）=+0.02±0.02|实测P_L Q_L：Fig.10|0.22|||Table 2 (原文被排除分支)；备选M1/E2自旋假设，原文最后判定该γ为纯E2||
|56Fe|[[polarization-delta-collection-20261119-source#R009\|R009]]|1750.0|3+→4+|-0.03|+0.075±0.027|||||Table 3, Table 5, Section 7.2 (p. 77, 83, 85)||
|56Fe|[[polarization-delta-collection-20261119-source#R009\|R009]]|1750.0|5+→4+|+0.04|+0.075±0.027|||||Section 7.2, Section 8, Table 3 (p. 77, 83, 85) (次选未完全排除分支)||
|56Fe|[[polarization-delta-collection-20261119-source#R009\|R009]]|2020.0|4+→4+|+5 <= δ <= +15||||||Table 5, Section 7.2, Section 6.2 (p. 77, 82, 85)||
|56Fe|[[polarization-delta-collection-20261119-source#R009\|R009]]|2020.0|4+→4+|+1.0±0.3||||||Section 7.2, p. 82 (原文被排除分支)||
|56Fe|[[polarization-delta-collection-20261119-source#R009\|R009]]|2609.0|3+→2+|\|δ\| < 0.04|+0.15±0.04|||||Table 3, Table 5, Section 7.2 (p. 77, 82-83, 85)||
|57Ni|[[polarization-delta-collection-20261119-source#R006\|R006]]|1075.0|→|-1.4(8)||Fig. 4(b), (c)|1.03(10); 1.03(10)||2577|Table 1, Fig. 4, p. 379 [cited_original: Rudolph1999_EPJA4]||
|57Ni|[[polarization-delta-collection-20261119-source#R006\|R006]]|1100.0|→|+0.94(18 13)||Fig. 4(b), (c)|0.44(5); 0.44(5)||2577|Table 1, Fig. 4, p. 379 [cited_original: Rudolph1999_EPJA4]||
|57Ni|[[polarization-delta-collection-20261119-source#R006\|R006]]|1136.0|→|-0.15(9)||Fig. 4(b), (c)|0.80(8); 0.80(8)||2577|Table 1, Fig. 4, p. 379 [cited_original: Rudolph1999_EPJA4]||
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|842.0|5/2-→5/2-|-1.19 <= delta <= -0.36|0.01+-0.11|||||Table 1, Section 3.2, Fig. 4b||
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|909.0|5/2-→3/2-|+0.20 (+0.16, -0.03)|-0.15+-0.04||||neutron coincidence|Table 1 p.370；Fig.4(a)及正文p.373||
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|949.0|7/2-→5/2-|-2.5+-0.5|-0.22+-0.05|||||Table 1, Section 3.3, Fig. 5a||
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|1544.0|3/2-→5/2-|-0.18 <= delta <= 0.18|0.49+-0.19|||||Table 1, Section 3.4, Fig. 6b||
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|1611.0|3/2-→3/2-|0.18 <= delta <= 2.75|0.05+-0.20|||||Table 1, Section 3.4, Fig. 6a||
|61Ni|[[polarization-delta-collection-20261119-source#W75\|W75]]|1953.0|5/2-→5/2-|0.03+-0.16|-0.65+-0.27|||||Table 1, Section 3.5, Fig. 7||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|533.2|9/2-→7/2-|-0.02 ± 0.03|-0.39 ± 0.07||-0.18 ± 0.01; -0.03 ± 0.02|||Table 3, p.41||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|792.6|9/2-→7/2-|-0.97 ± 0.18|-0.62 ± 0.12||0.57 ± 0.02; 0.06 ± 0.02|||Table 3, p.41||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|816.7|3/2-→1/2-|-0.23 ± 0.07|-0.12 ± 0.07||-0.01 ± 0.01; 0.0 ± 0.01|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|841|5/2-→5/2-|-1.83 ± 0.2|-0.17 ± 0.06||0.15 ± 0.01; 0.02 ± 0.02|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|908.3|5/2-→3/2-|0.18 ± 0.05|-0.15 ± 0.03||-0.28 ± 0.01; -0.02 ± 0.01|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|947.6|7/2-→5/2-|-2.46 ± 0.15|-0.10 ± 0.03||0.47 ± 0.01; 0.13 ± 0.01|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|972.5|9/2-→7/2-|0.7 ± 0.23|0.03 ± 0.12||-0.79 ± 0.02; 0.06 ± 0.03|||Table 3, p.41||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1064.6|5/2-→5/2-|-0.14 ± 0.12|0.16 ± 0.08||0.21 ± 0.01; 0.0 ± 0.01|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1131.9|5/2-→3/2-|0.47 ± 0.09|-0.03 ± 0.04||-0.44 ± 0.01; 0.01 ± 0.01|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1387.2|7/2-→5/2-|-2.7 ± 0.4|-0.05 ± 0.17||0.44 ± 0.02; 0.15 ± 0.03|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1541.7|5/2-→5/2-|0.07 ± 0.05|0.35 ± 0.10||0.16 ± 0.01; 0.0 ± 0.02|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1609.4|5/2-→3/2-|0.33 ± 0.14|-0.05 ± 0.10||-0.4 ± 0.01; 0.01 ± 0.02|||Table 3, p.40||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1950.6|7/2-→5/2-|0.02 (+0.07, −0.02)|-0.4 ± 0.1||-0.26 ± 0.02; -0.03 ± 0.02|||Table 3, p.41||
|61Ni|[[polarization-delta-collection-20261119-source#W77\|W77]]|1997.3|5/2-→3/2-|0.27 ± 0.06|-0.24 ± 0.11||-0.43 ± 0.01; 0.02 ± 0.02|||Table 3, p.41||
|65Cu|[[polarization-delta-collection-20261119-source#R005\|R005]]|8484.0|3/2-→3/2-|0.61±0.01||K=1.10±0.02|A22=0.38±0.04; A44<0.04|||p. 79, Fig. 2||
|65Cu|[[polarization-delta-collection-20261119-source#R005\|R005]]|8484.0|3/2-→3/2-|-0.14±0.02||K=1.10±0.02|A22=0.38±0.04; A44<0.04|||p. 79 (原文被排除分支)||
|67Ge|[[polarization-delta-collection-20261119-source#R024\|R024]]|419.45|(21/2)-→(19/2)-|0.02±0.03|-0.21±0.16||a2=-0.212±0.022; a4=0.004±0.022|||Table 2, Section 3.5, Fig. 8||
|72Se|[[polarization-delta-collection-20261119-source#SE22\|SE22]]|454.5|2+→2+|-5 ± 3||0.058(39)|RDCO=0.82(15); Rθ=1.73(22); 1.73(22); 0.82(15)|σ/j=0.3|RDCO/Rθ: 976.7|Table I, p. 5; Section II.B, pp. 7–8; Fig. 7, p. 8; Section IV.A, p. 8||
|72Se|[[polarization-delta-collection-20261119-source#SE22\|SE22]]|1136.1|2+→2+|-0.1 ± 0.24||0.127(89)|RDCO=1.12(18); Rθ=1.87(22); 1.87(22); 1.12(18)||RDCO/Rθ: 862.0|Table I, p. 5; Section IV.B, p. 9||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|279.4|7/2+→7/2+|0.3 +0.4 -0.2|0.0(4)||A2=-0.03(4); A4=-0.01(5)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|295.4|7/2+→9/2+|-0.16 +0.03 -0.01|-0.22(2)||A2=0.04(1); A4=0.03(1)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|299.3|9/2-→7/2-|-0.21 +0.03 -0.01|-0.16(3)||A2=-0.51(2); A4=0.03(2)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|344.0|9/2+→7/2+|-0.35 +0.04 -0.05|-0.06(4)||A2=-0.73(2); A4=0.12(2)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|354.3|7/2-→5/2-|-0.38 +0.03 -0.01|-0.05(1)||A2=-0.60(2); A4=0.03(2)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|373.1|13/2-→11/2-|-0.17 +0.05 -0.06|-0.2(1)||A2=-0.53(3); A4=0.03(4)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|382.3|7/2+→5/2+|0.8 +0.1 -0.1|-0.00(5)||A2=0.26(4); A4=-0.10(5)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|430.5|17/2-→15/2-|-0.16 +0.03 -0.04|-0.19(5)||A2=-0.55(2); A4=0.08(3)|sigma=1.8 +0.5 -0.6||Table 1, Fig. 3||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|450.0|15/2-→13/2-|-0.24 +0.04 -0.05|-0.11(4)||A2=-0.58(1); A4=0.08(1)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|472.8|→|-0.08 +0.08 -0.20|-0.2(2)||A2=-0.29(5); A4=0.07(6)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|532.2|7/2+→5/2+|-1.1 +0.2 -0.2|0.18(4)||A2=-0.73(1); A4=0.09(1)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|551.8|9/2-→9/2-|0.0 +0.3 -0.3|0.3(1)||A2=0.21(6); A4=-0.10(7)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|601.9|13/2+→13/2+|1.1 +0.2 -0.1|-0.11(4)||A2=0.28(1)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|629.8|13/2+→11/2+|0.2 +0.1 -0.1|-0.1(3)||A2=0.2(1); A4=0.1(1)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|639.3|9/2+→9/2+|0.04 +0.03 -0.03|0.59(2)||A2=0.35(1); A4=0.02(2)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|658.7|5/2-→3/2-|-0.35 +0.08 -0.09|-0.08(7)||A2=-0.53(2); A4=0.09(2)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|665.2|(19/2-)→17/2-|-0.4 +0.1 -0.1|0.0(1)||A2=-0.34(7); A4=0.02(8)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|765.0|5/2-→3/2-|-0.6 +0.2 -0.3|0.02(7)||A2=-0.34(3); A4=0.10(4)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|796.4|(9/2+)→7/2+|-0.40 +0.09 -0.14|-0.03(7)||A2=-0.53(2); A4=0.04(3)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|850.6|9/2-→7/2-|-0.3 +0.2 -0.3|-0.1(2)||A2=-0.49(7); A4=0.06(9)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|891.4|15/2+→13/2+|-0.27 +0.03 -0.05|-0.10(4)||A2=-0.80(2)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|942.7|11/2+→9/2+|2.2 +0.2 -0.1|-0.32(3)||A2=0.51(3); A4=0.29(3)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|999.6|11/2+→9/2+|-0.07 +0.01 -0.03|-0.26(4)||A2=-0.36(3); A4=0.07(4)|||Table 1||
|73Se|[[polarization-delta-collection-20261119-source#R001\|R001]]|1078.3|→9/2-|0.06 +0.05 -0.06|-0.3(1)||A2=-0.13(4); A4=0.09(5)|||Table 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|314.9|8+→7+|0.00+0.05−0.06|-0.31(0.07)||0.84(0.09); 0.84(0.09)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|347.5|9+→8+|−0.22+0.04−0.04|-0.11(0.03)||0.72(0.05); 0.72(0.05)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|367.4|7+→6+|-0.02+0.06−0.06|-0.30(0.09)||0.83(0.09); 0.83(0.09)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|405.9|6+→6+|−0.7+0.2−0.2|0.28(0.10)||1.04(0.07); 1.04(0.07)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|407.6|11+→10+|−0.11+0.05−0.05|-0.17(0.09)||0.79(0.05); 0.79(0.05)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|428.9|4+→4+|0.0+0.2−0.2|0.54(0.12)||1.21(0.09); 1.21(0.09)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|483.1|11+→10+|-0.01+0.07−0.08|-0.32(0.17)||0.83(0.07); 0.83(0.07)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|486.1|10+→9+|−0.5+0.1−0.1|0.05(0.05)||0.54(0.06); 0.54(0.06)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|497.4|9+→8+|0.03+0.05−0.05|-0.35(0.21)||0.87(0.10); 0.87(0.10)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|527.2|8+→7+|−0.63+0.08−0.10|0.09(0.03)||0.54(0.03); 0.54(0.03)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|600.3|6+→5+|−0.5+0.1−0.1|0.06(0.09)||0.55(0.03); 0.55(0.03)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|661.2|9+→8+|0.22+0.09−0.08|-0.50(0.14)||1.09(0.10); 1.09(0.10)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|697.8|12+→11+|−0.15+0.06−0.07|-0.14(0.11)||0.72(0.07); 0.72(0.07)|||SI Table I, p. 1||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|815.3|8+→7+|−1.1+0.3−0.4|0.19(0.19)||0.46(0.03); 0.46(0.03)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|959.5|10+→9+|−0.7+0.1−0.2|0.08(0.06)||0.49(0.03); 0.49(0.03)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|1155.6|9+→8+|3.1+1.8−0.9|-0.11(0.36)||1.16(0.15); 1.16(0.15)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|1239.5|12+→11+|−0.08+0.05−0.06|-0.22(0.09)||0.77(0.05); 0.77(0.05)|||SI Table I, p. 2||
|74Br|[[polarization-delta-collection-20261119-source#G24\|G24]]|1266.8|10+→9+|8+3−2|-0.07(0.20)||0.92(0.05); 0.92(0.05)|||SI Table I, p. 2||
|79Kr|[[polarization-delta-collection-20261119-source#R027\|R027]]|747.8|11/2+→9/2+|-0.55(7)|0.23(11)||A2=-0.83(2); A4=-0.13(11)|||Table 1, Table 2 [78Se(α, 3n)]||
|79Kr|[[polarization-delta-collection-20261119-source#R027\|R027]]|747.8|11/2+→9/2+|-0.55(7)|0.03(6)|||||Table 1, Table 2 [77Se(α, 2n)]||
|79Kr|[[polarization-delta-collection-20261119-source#R027\|R027]]|889.9|11/2+→9/2+|0.18(4)|0.06(17)||A2=0.03(6); A4=0.02(19)|||Table 1, Table 2 [78Se(α, 3n)]||
|79Kr|[[polarization-delta-collection-20261119-source#R027\|R027]]|889.9|11/2+→9/2+|0.18(4)|0.21(9)|||||Table 1, Table 2 [77Se(α, 2n)]||
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|671.8|3+→2+|+0.52+0.05-0.05|-0.55(20)||1.20(10); 1.08(12); 1.08(12); 1.20(10)||E2 gates|Table 1, p.4; Fig.2||
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|783.5|2+→2+|-1.57+0.11-0.11|+0.18(3)||0.35(1); 0.46(3); 0.46(3); 0.35(1)||E2 gates|Table 1, p.4; Fig.2||
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|793.5|4+→4+|-0.66+0.08-0.08|+0.35(4)||0.61(2); 1.18(18); 1.18(18); 0.61(2)||E2 gates|Table 1, p.4; Fig.2||
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|895.2|2+→2+|+0.06+0.03-0.03|+0.11(7)||1.47(6); 1.18(11); 1.18(11); 1.47(6)||E2 gates|Table 1, p.4||
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|1455.3|3+→2+|+0.12+0.03-0.04|-0.40(17)||0.53(3); 0.62(6); 0.62(6); 0.53(3)||E2 gates|Table 1, p.4; Fig.2||
|80Se|[[polarization-delta-collection-20261119-source#B26\|B26]]|1678.7|2+→2+|+0.18+0.06-0.06|+0.07(4)||1.69(11); 1.25(10); 1.25(10); 1.69(11)||E2 gates|Table 1, p.4||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|166.1|17/2-→15/2-|= -0.05|-0.25(6)||A2=-0.34(2); A4=-0.05(3)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|231.2|21/2+→21/2+|-0.05(5)|0.8(3)||A2=0.37(4); A4=0.01(7)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|233.5|19/2-→17/2-|-0.08(5)|-0.4(3)||A2=-0.40(5); A4=0.08(9)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|294.5|17/2-→15/2-||-0.4(2)||A2=-0.29(2); A4=-0.01(4)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|308.2|(17/2-)→(15/2-)|-0.07(4)|-0.43(15)||A2=-0.35(2); A4=-0.05(5)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|362.0|19/2-→17/2-|-0.08(3)|-0.19(3)||A2=-0.42(3); A4=-0.03(6)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|367.5|15/2-→13/2-|-0.09(3)|-0.27(5)||A2=-0.40(2); A4=-0.02(6)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|428.8|21/2-→19/2-|(-0.1)|-0.19(5)||A2=-0.34(4); A4=0.03(7)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|515.1|25/2+→23/2+|-0.10(4)|-0.40(11)||A2=-0.49(9)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|564.3|23/2+→21/2+|-0.10(3)|-0.18(13)||A2=-0.44(4); A4=0.08(8)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|575.3|27/2+→25/2+|-0.10(4)|-0.19(19)||A2=-0.50(5); A4=-0.02(8)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|608.7|23/2-→21/2-|-0.20(6)|0.01(19)||A2=-0.61(8)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|673.6|13/2+→11/2+|0.5(3)|0.02(10)||A2=-0.91(3); A4=0.01(6)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|823.9|11/2+→9/2+|= -0.7|-0.11(11)||A2=-0.66(4); A4=0.10(6)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|884.4|11/2+→9/2+|-0.4(1)|0.12(8)||A2=-0.89(5); A4=0.03(7)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|1017.5|15/2+→13/2+|= -0.8|(0.2)||A2=-0.31(4); A4=-0.01(4)|||Table 1, Table 2||
|81Kr|[[polarization-delta-collection-20261119-source#R026\|R026]]|1059.7|19/2+→17/2+|= -0.2|0.4(3)||A2=-0.50(5); A4=-0.03(6)|||Table 1, Table 2||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|180.1|7_2^-→7_1^-|-0.12 (8)|0.3 (3)||A2=0.28(3); A4=-0.01(4)|||Table 1, Table 2 (plate-shaped detector)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|244.5|7_2^-→6_1^-|0.07 (3)|-0.5 (1)||A2=-0.11(2); A4=0.00(3)|||Table 1, Table 2 (plate-shaped detector)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|367.6|6_1^-→5_2^-|0.24 (6)|-0.38 (4)||A2=0.11(1); A4=0.02(2)|||Table 1, Table 2 (plate-shaped detector)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|367.6|6_1^-→5_2^-|0.24 (6)|-0.45 (25)||A2=0.11(1); A4=0.02(2)|||Table 1, Table 2 (two detectors)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|556.6|8_1^-→7_2^-|0.17 (4)|-0.33 (10)||A2=0.03(1); A4=0.02(3)|||Table 1, Table 2 (plate-shaped detector)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|556.6|8_1^-→7_2^-|0.17 (4)|-0.33 (7)||A2=0.03(1); A4=0.02(3)|||Table 1, Table 2 (two detectors)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|943.2|5_1^+→4_2^+|0.4 (1)|-0.32 (20)||A2=0.27(8); A4=-0.02(9)|||Table 1, Table 2 (plate-shaped detector)||
|84Kr|[[polarization-delta-collection-20261119-source#R028\|R028]]|943.2|5_1^+→4_2^+|0.4 (1)|-0.44 (25)||A2=0.27(8); A4=-0.02(9)|||Table 1, Table 2 (two detectors)||
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|582.0|1/2+→3/2+|+0.266 +0.052 -0.040||beta = 0.958 +/- 0.006|A22 = -0.306 +/- 0.010; A44 = -0.008 +/- 0.012||204|Table 1, Table 2, Table 3||
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|582.0|1/2+→3/2+|+1.00 +0.08 -0.09||beta = 0.958 +/- 0.006|A22 = -0.306 +/- 0.010; A44 = -0.008 +/- 0.012||204|Table 1, Table 2 (原文被排除分支)||
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|616.0|3/2+→3/2+|-2.00 +/- 0.22||beta = 0.981 +/- 0.043|A22 = 0.248 +/- 0.017; A44 = -0.010 +/- 0.018||204|Table 1, Table 2, Table 3||
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|616.0|3/2+→3/2+|-0.215 +/- 0.045||beta = 0.981 +/- 0.043|A22 = 0.248 +/- 0.017; A44 = -0.010 +/- 0.018||204|Table 1, Table 2 (原文被排除分支)||
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|835.0|1/2+→3/2+|0.038 +/- 0.019||beta = 0.936 +/- 0.012|A22 = -0.200 +/- 0.007; A44 = -0.003 +/- 0.010||204|Table 1, Table 2, Table 3||
|95Mo|[[polarization-delta-collection-20261119-source#R022\|R022]]|835.0|1/2+→3/2+|1.59 +/- 0.06||beta = 0.936 +/- 0.012|A22 = -0.200 +/- 0.007; A44 = -0.003 +/- 0.010||204|Table 1, Table 2 (原文被排除分支)||
|105Pd|[[polarization-delta-collection-20261119-source#T19\|T19]]|991.0|17/2-→15/2-|1.8(5)|Fig. 2||Fig. 2; Fig. 2||stretched E2|Page 2, 3, Table I, Fig. 2||
|105Pd|[[polarization-delta-collection-20261119-source#T19\|T19]]|991.0|17/2-→15/2-|0.59(20)|Fig. 2||Fig. 2; Fig. 2||stretched E2|p.3 Fig.2（原文DCO小根，P不支持）||
|105Pd|[[polarization-delta-collection-20261119-source#T19\|T19]]|994.0|25/2-→23/2-|2.7(6)|Fig. 2||Fig. 2; Fig. 2||stretched E2|Page 2, 3, Table I, Fig. 2||
|105Pd|[[polarization-delta-collection-20261119-source#T19\|T19]]|1034.0|21/2-→19/2-|2.3(3)|Fig. 2||Fig. 2; Fig. 2||stretched E2|Page 2, 3, Table I, Fig. 2||
|105Pd|[[polarization-delta-collection-20261119-source#T19\|T19]]|1034.0|21/2-→19/2-|0.40(6)|Fig. 2||Fig. 2; Fig. 2||stretched E2|p.3 Fig.2（原文DCO小根，P不支持）||
|111Cd|[[polarization-delta-collection-20261119-source#R003\|R003]]|171.0|7/2+→5/2+|+0.145|γ(245): Fig. 2|A=12.8%|||171 (polarized photon: 245 keV, cascade: 171-245 keV)|p.51 Abstract; p.52 Section 4, Fig. 2||
|111Cd|[[polarization-delta-collection-20261119-source#R003\|R003]]|171.0|7/2+→5/2+|-0.145|γ(245): Fig. 2|A=12.8%|||171 (polarized photon: 245 keV, cascade: 171-245 keV)|p.52 Section 4 (原文被排除分支)||
|112In|[[polarization-delta-collection-20261119-source#R025\|R025]]|1062.98|2+→1+|-0.16±0.05|-0.315(74)||A2=-0.036(14); A4=0.023(19)|||Table 2, p. 499||
|116Sn|[[polarization-delta-collection-20261119-source#R032\|R032]]|931.8|2+→2+|1.70+0.96-1.3||0.06(0.13)|1.00(0.17); 1.00(0.17)|0.37|1293.8|Table 1||
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|182.9|(8-)→(7-)|0.10(35)||-0.03(2)|a2=-0.15(9); a4=0.31(17); 0.91(5); 1.2(2)f|||Table I, page 16||
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|236.4|(8+)→(7+)|0.00(15)||-0.02(1)|a2=-0.22(5); a4=0.08(10); 0.82(3); 1.11(7)f|||Table I, page 16||
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|265.5|(9-)→(8-)|0.00(20)||-0.2(1)|a2=-0.18(2); a4=0.10(2); 0.9(1); 1.0(2)f|||Table I, page 16||
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|274.6|(9+)→(8+)|0.10(10)||-0.07(2)|a2=-0.11(18); a4=0.06(34); 0.85(4); 1.11(9)f|||Table I, page 16||
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|288.3|(10-)→(9-)|0.10(20)||-0.3(2)|a2=-0.00(30); a4=0.11(57); 0.74(8); 1.0(2)f|||Table I, page 16||
|118Cs|[[polarization-delta-collection-20261119-source#R043\|R043]]|307.0|(10+)→(9+)|0.10(25)||-0.02(1)|a2=-0.12(6); a4=0.23(11); 0.89(5); 0.97(9)f|||Table I, page 16||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|205.3|(23/2+)→(21/2+)|-0.35(25)||-0.13(13)|a2=-0.78(24); a4=0.14(44); 0.8(2)|||Table II, page 18||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|207.1|21/2+→19/2+|0.10(10)||-0.01(1)|a2=-0.12(3); a4=0.02(4); 1.0(3); 1.0(3)|||Table II, page 20||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|208.7|5/2+→3/2+|0.10(20)||-0.001(1)|a2=-0.29(4); a4=0.24(7); 0.80(9)|||Table II, page 17||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|238.6|11/2+→9/2+|-0.05(30)||-0.04(1)|a2=-0.33(13); a4=0.18(25); 1.02(5); 1.02(5)|||Table II, page 18||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|268.6|13/2+→11/2+|-0.05(25)||-0.04(1)|a2=-0.32(14); a4=0.16(27); 1.04(5); 1.04(5)|||Table II, page 18||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|292.2|15/2+→13/2+|0.40(10)||-0.05(5)|a2=-0.27(6); a4=-0.01(5); 0.8(2)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|296.5|15/2+→13/2+|0.00(20)||-0.02(1)|a2=-0.28(13); a4=0.19(25); 1.06(5); 1.06(5)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|299.8|25/2+→23/2+|-0.15(40)||-0.05(4)|a2=-0.53(52); a4=-0.24(96); 0.9(3); 0.9(3)|||Table II, page 20||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|302.6|17/2+→15/2+|0.00(10)||-0.03(3)|a2=-0.22(5); a4=0.01(9); 1.0(2); 1.0(2)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|314.0|19/2+→17/2+|0.00(20)||-0.05(3)|a2=-0.27(3); a4=-0.10(6); 1.0(1); 1.0(1)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|315.2|(15/2-)→(13/2-)|0.10(15)||-0.06(2)|a2=-0.14(14); a4=0.08(27); 1.2(2); 1.2(2)|||Table II, page 16||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|320.8|17/2+→15/2+|0.10(25)||-0.08(2)|a2=-0.26(14); a4=0.13(27); 1.04(5); 1.04(5)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|327.0|21/2+→19/2+|0.00(10)||-0.05(4)|a2=-0.23(6); a4=-0.09(12); 1.1(3); 1.1(3)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|332.7|27/2+→25/2+|0.00(10)||-0.10(5)|a2=-0.23(8); a4=-0.09(16); 1.0(3); 1.0(3)|||Table II, page 20||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|341.9|19/2+→17/2+|0.00(10)||-0.07(2)|a2=-0.28(14); a4=0.08(26); 1.06(6); 1.06(6)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|345.1|(17/2-)→(15/2-)|0.10(10)||-0.10(4)|a2=-0.06(11); a4=0.08(21); 1.2(2); 1.2(2)|||Table II, page 16||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|357.7|21/2+→19/2+|-0.05(20)||-0.04(2)|a2=-0.20(17); a4=0.10(32); 1.04(7); 1.04(7)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|369.4|23/2+→21/2+|-0.05(20)||-0.03(3)|a2=-0.33(18); a4=0.09(35); 0.78(9)|||Table II, page 19||
|119Cs|[[polarization-delta-collection-20261119-source#R042\|R042]]|389.9|(21/2-)→(19/2-)|0.10(20)||-0.06(4)|a2=-0.09(14); a4=0.21(27); 1.0(2); 1.0(2)|||Table II, page 16||
|122Te|[[polarization-delta-collection-20261119-source#R010\|R010]]|690.0|2+→2+|+0.8||Fig. 4|||560|Section 3, p. 501; Fig. 4, p. 499||
|122Te|[[polarization-delta-collection-20261119-source#R010\|R010]]|690.0|2+→2+|-0.05||Fig. 4|||560|Section 3, p. 501, 原文被排除分支||
|125Sb|[[polarization-delta-collection-20261119-source#R023\|R023]]|332.0|5/2+→7/2+|-0.29+0.08-0.09||β=0.985±0.021|A22=0.042±0.015; A44=-0.009±0.020||1087|Table 2, Table 3, p.376, p.378||
|125Sb|[[polarization-delta-collection-20261119-source#R023\|R023]]|332.0|5/2+→7/2+|-2.26+0.41-0.51||β=0.985±0.021|A22=0.042±0.015; A44=-0.009±0.020||1087|Table 2, Table 3, p.376, p.378||
|125Sb|[[polarization-delta-collection-20261119-source#R023\|R023]]|332.0|5/2+→7/2+|-0.29+0.08-0.09||β=1.00±0.02|A22=-0.021±0.008; A44=-0.005±0.013||470 (intermediate 1087)|Table 2, Table 3, p.376, p.378||
|125Sb|[[polarization-delta-collection-20261119-source#R023\|R023]]|332.0|5/2+→7/2+|-2.26+0.41-0.51||β=1.00±0.02|A22=-0.021±0.008; A44=-0.005±0.013||470 (intermediate 1087)|Table 2, Table 3, p.376, p.378||
|125Sb|[[polarization-delta-collection-20261119-source#R023\|R023]]|1067.0|9/2+→7/2+|-0.86±0.18||β=1.01±0.03|A22=0.199±0.022; A44=-0.001±0.032||823|Table 2, Table 3, p.377||
|125Te|[[polarization-delta-collection-20261119-source#R012\|R012]]|176.0|9/2-→11/2-|-0.63+0.16-0.65|0.395±0.034||ρ2A2=-0.3638±0.0025; ρ4A4=-0.0024±0.0029|||Section 4, p.225-226, Fig. 6||
|125Te|[[polarization-delta-collection-20261119-source#R012\|R012]]|176.0|9/2-→11/2-|-0.95+0.48-0.33|0.395±0.034||ρ2A2=-0.3638±0.0025; ρ4A4=-0.0024±0.0029|||Section 4, p.225-226, Fig. 6||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|223.6|5/2+→3/2+|(3.6+3.7/-1.9)|-0.01(7)||A2/A0=0.20(1); A4/A0=-0.01(1)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|257.8|7/2+→7/2+|-0.18+0.37/-0.15|0.52(23)||A2/A0=0.23(4); A4/A0=-0.02(7)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|277.6|9/2+→7/2+|-0.26+0.06/-0.09|-0.08(4)||A2/A0=-0.53(2); A4/A0=0.04(2)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|300.9|9/2+→7/2+|(-3.76±0.12)|0.14(2)||A2/A0=-0.32(1); A4/A0=0.14(1)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|408.6|11/2+→11/2+|0.29+0.25/-0.23|0.28(7)||A2/A0=0.30(4); A4/A0=-0.11(6)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|416.7|15/2-→13/2-|-1.5±0.5|0.18(6)||A2/A0=-0.46(3); A4/A0=0.12(5)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|422.3|9/2+→9/2+|-0.13+0.20/-0.12|0.77(19)||A2/A0=0.35(4); A4/A0=-0.13(6)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|426.4|13/2-→11/2-|-0.42+0.05/-0.07|0.01(1)||A2/A0=-0.86(6); A4/A0=0.08(1)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|445.5|7/2+→7/2+|0.38+0.13/-0.12|0.23(5)||A2/A0=0.29(2); A4/A0=0.01(3)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|540.1|3/2+→1/2+|-0.03+0.07/-0.13|-0.08(2)||A2/A0=-0.18(1); A4/A0=0.02(1)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|573.3|15/2-→13/2-|(-1.4±0.1)(AD)|-0.13(5)||A2/A0=-0.83(2); A4/A0=0.15(2)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|573.3|15/2-→13/2-|-0.6+0.1/-0.2(Corr)|-0.13(5)||Table 4: 45-90-90=2959(65), 90-45-90=1235(42), 90-90-180=1134(85), 45-225-0=1087(53), 45-135-0=1200(39)||484.3|Table 3, Table 4, page 96-97||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|618.5|19/2-→17/2-|-0.9±0.3|-0.17(44)||A2/A0=0.16(2); A4/A0=0.04(3)|||Table 3, page 97||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|690.7|5/2+→3/2+|0.13±0.03|-0.48(13)||A2/A0=-0.11(2); A4/A0=0.16(4)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|711.1|3/2+→1/2+|(0.07+0.07/-0.20)|-0.15(4)||A2/A0=-0.15(1); A4/A0=0.02(2)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|870.2|(7/2)→(5/2)|(14+33/-11)|0.07(11)||A2/A0=0.27(5); A4/A0=0.01(8)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1105.4|5/2+→3/2+|-0.05+0.08/-0.15|-0.23(8)||A2/A0=-0.20(3); A4/A0=-0.05(5)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1202.6|7/2+→5/2+|-0.6+0.3/-0.5|0.05(4)||A2/A0=-0.36(3); A4/A0=0.05(4)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1264.7|19/2-→17/2-|-2.3+0.1/-0.2 b|0.08(11)||A2/A0=-0.75(2); A4/A0=0.30(3)|||Table 3, page 97||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1264.7|19/2-→17/2-|-9+6/-7 c|0.08(11)||A2/A0=-0.75(2); A4/A0=0.30(3)|||Table 3, page 97||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1292.8|(7/2+)→5/2+|-0.24+0.17/-0.53|-0.17(12)||A2/A0=-0.44(7); A4/A0=-0.09(12)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1304.2|5/2+→3/2+|(-2.7±0.4)|0.05(7)||A2/A0=-0.43(5); A4/A0=0.28(8)|||Table 3, page 96||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1490.0|13/2-→13/2-|0.9+0.2/-0.3|0.10(15)||A2/A0=0.42(8); A4/A0=-0.33(11)|||Table 3, page 97||
|125Xe|[[polarization-delta-collection-20261119-source#R029\|R029]]|1562.8|9/2+→7/2+|-5.7+2.4/-3.3|0.06(18)||A2/A0=-0.20(6); A4/A0=0.14(9)|||Table 3, page 97||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|483.0|13/2-→11/2-|-2.1+0.2-0.2|0.23(13)|+0.058(32)|0.303(21); 0.303(21)||RDCO门：674 keV（SI Table1）|Table 1, Page 3; Text Page 3; Fig. 3；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|483.0|13/2-→11/2-|-0.29+0.03-0.04|0.23(13)|+0.058(32)|0.303(21); 0.303(21)||RDCO门：674 keV（SI Table1）|p.3 Fig.3及正文（DCO小根，原文P支持大根）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|577|15/2-→13/2-|-1.7+0.2-0.3||+0.051(37)|0.245(28); 0.245(28)||RDCO门：735 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|638|19/2-→17/2-|-2.4+0.9-0.7||+0.068(115)|0.311(66); 0.311(66)||RDCO门：674 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|639|17/2-→15/2-|-2.2+0.2-0.1||+0.008(36)|0.304(15); 0.304(15)||RDCO门：777 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|651|13/2-→11/2-|+0.15+0.05-0.05||-0.012(137)|0.717(69); 0.717(69)||RDCO门：744 keV（SI Table1）|Table 1, Page 3; Text Page 3; Fig. 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|735|21/2-→19/2-|-2.4+0.1-0.1||+0.031(25)|0.313(10); 0.313(10)||RDCO门：681 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|800|25/2-→23/2-|-2.9+0.7-0.5||+0.074(61)|0.352(41); 0.352(41)||RDCO门：804 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|876|17/2-→15/2-|+0.26+0.10-0.10||-0.114(132)|0.849(132); 0.849(132)||RDCO门：519 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|127Xe|[[polarization-delta-collection-20261119-source#C20\|C20]]|884|29/2-→27/2-|-3.1+1.9-1.1||+0.048(82)|0.366(88); 0.366(88)||RDCO门：890 keV（SI Table1）|Table 1, Page 3；原文RDCO法（非P联合拟合值）；SI Table1 p.2||
|129Ba|[[polarization-delta-collection-20261119-source#R047\|R047]]|365.0|13/2-→11/2-|−0.84 ⩽ δ ⩽ −0.79|0.072(68)||A22 = −0.70(3); A44 = 0.16(5)|||p. 3；转引Gizon1978输入，δ结果类别按原文位置区分||
|129Ba|[[polarization-delta-collection-20261119-source#R047\|R047]]|365.0|13/2-→11/2-|≈ −2.0|0.072(68)||A22 = −0.70(3); A44 = 0.16(5)|||p. 3, Fig. 3；转引Gizon1978输入，δ结果类别按原文位置区分||
|129Ba|[[polarization-delta-collection-20261119-source#R047\|R047]]|365.0|13/2-→11/2-|≈ −2.0(2)|0.072(68)||A22 = −0.70(3); A44 = 0.16(5)|||p. 3, Fig. 2；转引Gizon1978输入，δ结果类别按原文位置区分||
|129Ba|[[polarization-delta-collection-20261119-source#R047\|R047]]|365.0|13/2-→11/2-|≈ −0.33(3)|0.072(68)||A22 = −0.70(3); A44 = 0.16(5)|||p. 3, Fig. 2, 原文被排除分支；转引Gizon1978输入，δ结果类别按原文位置区分||
|131Xe|[[polarization-delta-collection-20261119-source#R045\|R045]]|670.6|13/2-→11/2-|0.03(3)||-0.03(5)|0.57(4); 0.57(4)||stretched E2 gates|Table I, Fig. 5, Sec. III p. 4||
|131Xe|[[polarization-delta-collection-20261119-source#R045\|R045]]|1055.1|17/2-→15/2-|0.1(2)||+0.02(5)|a2=-0.49(4); a4=0.03(6); 0.54(3); 0.54(3)||stretched E2 gates|Table I, Fig. 4, Sec. III pp. 3-4||
|132Ce|[[polarization-delta-collection-20261119-source#R037\|R037]]|197.5|(15-)→(14-)|-0.088^{+0.012}_{-0.013}|-0.31(15)||0.40(2); 0.40(2)||gated by ground-state band members of 132Ce|Table 2, Table 4, Fig. 3(b), Fig. 4, p. 180, 186-187||
|132Ce|[[polarization-delta-collection-20261119-source#R037\|R037]]|282.0|(16-)→(15-)|-0.042^{+0.008}_{-0.009}|-0.01(4)||0.49(2); 0.49(2)||gated by ground-state band members of 132Ce|Table 2, Table 4, Fig. 3(b), Fig. 4, p. 180, 186-187||
|132Ce|[[polarization-delta-collection-20261119-source#R037\|R037]]|351.7|(17-)→(16-)|-0.122^{+0.016}_{-0.016}|0.03(5)||0.33(3); 0.33(3)||gated by ground-state band members of 132Ce|Table 2, Table 4, Fig. 4, p. 180, 187||
|132Ce|[[polarization-delta-collection-20261119-source#R037\|R037]]|412.4|(18-)→(17-)|-0.076^{+0.026}_{-0.027}|-0.35(9)||0.42(2); 0.42(2)||gated by ground-state band members of 132Ce|Table 2, Table 4, Fig. 4, p. 180, 187||
|132Xe|[[polarization-delta-collection-20261119-source#R039\|R039]]|630.2|2+→2+|+4.2(4)|0.12(5)||a2=−0.223(12); a4=0.284(25)||667.7|Table 1, Table 5, Figure 9(a), Section 4||
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|457.6|19/2-→17/2-|-1.90 ± 0.15||0.033(32)|0.25(2); 0.25(2)||680.4|Page 4, Table 1 & Table 2|Q≈0.3（500 keV）；原文p.3写asym=P/Q|
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|613.2|13/2-→11/2-|-1.40 ± 0.10||0.030(31)|0.18(1); 0.18(1)||641.9|Page 4, Table 1 & Table 2; Fig. 4(c)|Q≈0.3（500 keV）；原文p.3写asym=P/Q|
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|626.8|15/2-→13/2-|-1.50 ± 0.11||0.037(29)|0.18(1); 0.18(1)||641.9|Page 4, Table 1 & Table 2; Fig. 4(d)|Q≈0.3（500 keV）；原文p.3写asym=P/Q|
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|743.4|17/2-→15/2-|-2.10 ± 0.19||0.041(46)|0.25(2); 0.25(2)||680.4|Page 4, Table 1 & Table 2|Q≈0.3（500 keV）；原文p.3写asym=P/Q|
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|812.0|21/2-→19/2-|-1.95 ± 0.16||0.024(22)|0.24(2); 0.24(2)||680.4|Page 4, Table 1 & Table 2|Q≈0.3（500 keV）；原文p.3写asym=P/Q|
|133Ba|[[polarization-delta-collection-20261119-source#D21\|D21]]|1067.0|17/2-→15/2-|-0.15 ± 0.02||-0.050(42)|0.37(3); 0.37(3)||889.8（Table1脚注c）|Page 4, Table 1 & Table 2; Fig. 4(e)|Q≈0.3（500 keV）；原文p.3写asym=P/Q|
|133Cs|[[polarization-delta-collection-20261119-source#R039\|R039]]|81.0|5/2+→7/2+|−0.178(12)|P(356.0)=+0.082(36)||a2=0.051(7); a4=−0.013(14)||81.0 (POL=356.0)|Table 1, Table 5, Section 4; 级联356.0-81.0 keV, 被偏振光子356.0 keV||
|133Cs|[[polarization-delta-collection-20261119-source#R039\|R039]]|81.0|5/2+→7/2+|+0.158(5)|P(356.0)=+0.082(36)||a2=0.051(7); a4=−0.013(14)||81.0 (POL=356.0)|Table 5, Section 4; cited_original [15]; 级联356.0-81.0 keV, 被偏振光子356.0 keV; 原文被排除分支||
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|758|17/2-→15/2-|-1.96 (+0.5, -1.12)|Fig.4||-0.69 ± 0.05; 0.19 ± 0.09||445|Fig.2（原文角分布法）；P数据见Fig.4||
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|874|21/2-→19/2-|-2.24 (+0.62, -0.95)|Fig.4||-0.68 ± 0.06; 0.21 ± 0.09||445|Fig.2（原文角分布法）；P数据见Fig.4||
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|982|25/2-→23/2-|-2.9 (+0.6, -1.5)|Fig.4||-0.55 ± 0.06; 0.18 ± 0.10||445|Fig.2（原文角分布法）；P数据见Fig.4||
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|758.0|17/2-→15/2-|-2.05+0.39-0.30|Fig. 4(g)||Fig. 4(g); Fig. 4(g)|0.3|445|Table 1, Fig. 4||
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|874.0|21/2-→19/2-|-2.60+0.46-0.47|Fig. 4(h)||Fig. 4(h); Fig. 4(h)|0.3|445|Table 1, Fig. 4||
|133La|[[polarization-delta-collection-20261119-source#Biswas2019\|Biswas2019]]|982.0|25/2-→23/2-|-3.07+0.47-0.65|Fig. 4(i)||Fig. 4(i); Fig. 4(i)|0.3|445|Table 1, Fig. 4||
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|410.2|15/2-→13/2-|-0.21(5)||-0.070(18)|0.88(10); 0.88(10)||518|Table I, Table II, Fig. 6(d)||
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|518.1|13/2-→11/2-|-0.11(5)||-0.024(10)|0.69(8); 0.69(8)||694|Table I, Table II, Fig. 6(a)||
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|518.3|17/2-→15/2-|-0.26(8)||-0.14(8)|1.05(13)||717|Table I, Table II, Page 7-8||
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|566.0|19/2-→17/2-|-0.33(9)||-0.081(72)|0.54(17)|||Table I, Table II||
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|566.8|15/2-→13/2-|-0.48(14)||-0.019(6)|0.36(6); 0.36(6)||709|Table I, Table II, Fig. 6(c)||
|135Nd|[[polarization-delta-collection-20261119-source#R041\|R041]]|618.3|17/2-→15/2-|-0.32(5)||-0.012(4)|0.83(10); 0.83(10)||594|Table I, Table II, Fig. 6(b)||
|135Pr|[[polarization-delta-collection-20261119-source#L22\|L22]]|450.2|19/2-→17/2-|-0.31 (+0.1, −0.13)|-0.07(+0.09,-0.10)|-0.017(+0.022,-0.023)|0.49(4); 0.49(4)||P: 747|PLB 824 (2022) 136840 Table 1 (p. 3), Fig. 2(f); Supp Mat Table 1 (p. 5)||
|135Pr|[[polarization-delta-collection-20261119-source#L22\|L22]]|747.3|17/2-→15/2-|-0.47 (+0.09, −0.22)|0.04(+0.08,-0.13)|0.006(+0.012,-0.019)|0.37(4); 0.37(4)||P: 450|PLB 824 (2022) 136840 Table 1 (p. 3), Fig. 2(b); Supp Mat Table 1 (p. 5)||
|135Pr|[[polarization-delta-collection-20261119-source#L22\|L22]]|813.2|21/2-→19/2-|-0.37 (+0.1, −0.14)|-0.03(+0.05,-0.12)|-0.004(+0.007,-0.016)|0.48(6); 0.48(6)||P: 796|PLB 824 (2022) 136840 Table 1 (p. 3), Fig. 2(d); Supp Mat Table 1 (p. 5)||
|135Pr|[[polarization-delta-collection-20261119-source#R051\|R051]]|593.9|13/2-→11/2-|-0.16 ± 0.04||Fig. 3||||Table I, Fig. 2, Fig. 3||
|135Pr|[[polarization-delta-collection-20261119-source#R051\|R051]]|747.0|17/2-→15/2-|-1.24 ± 0.13||0.047 ± 0.012||||Table I, Fig. 2, Fig. 3||
|135Pr|[[polarization-delta-collection-20261119-source#R051\|R051]]|812.8|21/2-→19/2-|-1.54 ± 0.09||0.054 ± 0.034||||Table I, Fig. 2, Fig. 3||
|136Nd|[[polarization-delta-collection-20261119-source#ND22\|ND22]]|751|17+→16+|-0.48 (+0.13, −0.14)|0.02 (+0.04, −0.05)|0.03 (+0.06, −0.07)|0.55(5)||P: 989|PRC105,034302, 主文pp.3–4; Fig.3||
|144Nd|[[polarization-delta-collection-20261119-source#R011\|R011]]|864.0|2+→2+|\|δ\| = 0.63 ± 0.15|-0.23 ± 0.07|N_perp/N_parallel = 0.85 ± 0.04|W(0°) - 1 = +0.077 ± 0.013|||PDF p.9 Table IV, p.13 Fig. 6, p.17 Table VI|Q=0.34±0.04（Table IV）|
|145Ba|[[polarization-delta-collection-20261119-source#R030\|R030]]|112.5|7/2-→5/2-|0.13 +0.07 -0.06|P(350.0 \| 112.5) = P(350.0)=-0.05(4)||DCO1=0.79(3)||Cascade: 350.0 P - 112.5|Table 9, Table 8b, Table 6c||
|145Ba|[[polarization-delta-collection-20261119-source#R030\|R030]]|164.5|9/2-→7/2-|-2.25 +0.97 -1.77|P(364.3 \| 164.5) = P(364.3)=-0.21(8)||DCO1=1.03(9)||Cascade: 364.3 P - 164.5|Table 9, Table 8b, Table 6b||
|145Ba|[[polarization-delta-collection-20261119-source#R030\|R030]]|164.5|9/2-→7/2-|-0.31 +0.24 -0.27|P(364.3 \| 164.5) = P(364.3)=-0.21(8)||DCO1=1.03(9)||Cascade: 364.3 P - 164.5|Table 9, Table 8b, Table 6b||
|145Ba|[[polarization-delta-collection-20261119-source#R030\|R030]]|185.4|11/2-→9/2-|0.18 +0.10 -0.07|P(276.9 \| 185.4) = P(276.9)=+0.10(5)||DCO1=0.97(15)||Cascade: 185.4 - 276.9 P|Table 9, Table 8b, Table 6b||
|145Ba|[[polarization-delta-collection-20261119-source#R030\|R030]]|185.4|11/2-→9/2-|3.24 +0.99 -0.60|P(276.9 \| 185.4) = P(276.9)=+0.10(5)||DCO1=0.97(15)||Cascade: 185.4 - 276.9 P|Table 9, Table 8b, Table 6b||
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|415.0|13/2-→11/2-|-3.3+9-14||0.038(35)|0.44(7); 0.44(7)|0.35||Table I, Fig. 5, Page 4, 6；原文RDCO法（非P联合拟合值）|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|415.0|13/2-→11/2-|-0.12+8-10||0.038(35)|0.44(7); 0.44(7)|0.35||Fig. 5, Page 6；原文RDCO法（非P联合拟合值）|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|537.9|17/2-→15/2-|-6.2+25-88||0.024(15)|0.54(9); 0.54(9)|0.35||Table I, Fig. 7, Page 4, 6；原文RDCO法（非P联合拟合值）|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|537.9|17/2-→15/2-|-0.04+9-10||0.024(15)|0.54(9); 0.54(9)|0.35||Fig. 7, Page 6；原文RDCO法（非P联合拟合值）|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|554.5|13/2-→15/2-|-0.08+10-9||-0.079(28)|0.68(10); 0.68(10)|0.35||Table I, Fig. 9, Page 4, 6；原文RDCO法（非P联合拟合值）|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|415.0|13/2-→11/2-|-3.3 (+1.3, -3.0)||0.038(35)|0.44(7); 0.44(7)|0.35||Table I δc；Fig.6（P–DCO）, pp.4,6|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|415.0|13/2-→11/2-|-3.3 (+1.5, -3.3)||0.038(35)|0.44(7); 0.44(7)|σ/j≈0.35||Table I δav（作者二法平均）, p.4|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|537.9|17/2-→15/2-|-6.3 (+3.3, -8.8)||0.024(15)|0.54(9); 0.54(9)|0.35||Table I δc；Fig.8（P–DCO）, pp.4,7|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|537.9|17/2-→15/2-|-6.3 (+4.1, -8.8)||0.024(15)|0.54(9); 0.54(9)|σ/j≈0.35||Table I δav（作者二法平均）, p.4|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|554.5|13/2-→15/2-|-0.10 (+0.02, -0.11)||-0.079(28)|0.68(10); 0.68(10)|0.35||Table I δc；Fig.10（P–DCO）, pp.4,8|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|151Eu|[[polarization-delta-collection-20261119-source#M23\|M23]]|554.5|13/2-→15/2-|-0.09 (+0.11, -0.14)||-0.079(28)|0.68(10); 0.68(10)|σ/j≈0.35||Table I δav（作者二法平均）, p.4|Q=Q0[a+bEγ]；a=0.626(125)，b=-3.22(23)×10^-4 keV^-1；几何不对称a(Eγ)=1.03(7)（原文p.5）|
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|656.5|4+→4+|2.2(−7, +35)|+0.01(2)||a2=−0.186(29); a4=0.110(60)||244.7|Table 6, Table 7, Section 5.1; 级联656.5-244.7 keV||
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|688.7|2+→2+|12(−3, +5)|+0.16(8)||a2=−0.137(18); a4=0.305(36)||121.8|Table 6, Table 7, Section 5.1; 级联688.7-121.8 keV||
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|867.4|3+→4+|−6.9(7)|−0.14(3)||a2=0.137(11); a4=−0.204(26)||244.7|Table 6, Table 7, Section 5.1; 级联867.4-244.7 keV||
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|964.1|2+→2+|−8.5(9)|−0.03(3)||a2=0.012(11); a4=0.290(22)||121.8|Table 6, Table 7, Section 5.1; 级联964.1-121.8 keV||
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|1005.3|4+→4+|−4.1(5)|−0.16(8)||a2=−0.032(11); a4=0.140(22)||244.7|Table 6, Table 7, Section 5.1; 级联1005.3-244.7 keV||
|152Sm|[[polarization-delta-collection-20261119-source#R039\|R039]]|1112.1|3+→2+|−11(−3, +2)|−0.26(3)|A=−0.033(3)|a2=−0.267(9); a4=−0.075(19)||121.8|Table 4, Table 6, Table 7, Section 5.1; 级联1112.1-121.8 keV||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|305.0|49/2(+)→47/2(+)|0.11+0.11-0.05||-0.15(1)|1.38(8); 1.38(8)|σ/J=0.3|913[E2]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|335.0|65/2-→63/2-|0.10(3)||-0.03(3)|1.39(6); 1.39(6)|σ/J=0.3|913[E2]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|343.0|71/2-→69/2-|0.19+0.09-0.08||-0.07(3)|1.24(3); 1.24(3)|σ/J=0.3|761[E2]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|389.0|69/2-→67/2-|0.17+0.11-0.08||-0.02(3)|1.27(4); 1.27(4)|σ/J=0.3|466[E2]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|455.0|45/2+→43/2+|0.33(3)||0.09(2)|1.07(3); 1.07(3)|σ/J=0.3|913[E2]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|497.0|51/2(+)→49/2(+)|0.3(5)||-0.01(5)|0.79(4); 0.79(4)|σ/J=0.3|637[M1]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|637.0|47/2(+)→45/2+|0.08+0.12-0.09||-0.17(8)|1.43(1); 1.43(1)|σ/J=0.3|913[E2]|Table I||
|153Ho|[[polarization-delta-collection-20261119-source#R050\|R050]]|1126.0|69/2-→67/2-|0.17||-0.11(1)|1.02(4); 1.02(4)|σ/J=0.3|1001[E1]|Table I||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|140.8|11+→10+|2.35+0.71-0.54|-0.35(21)|-0.14(8)|1.05(3); 1.05(3)|||Table 1, Fig. 5(b)||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|154.5|10+→9+|1.67+0.59-0.58|-0.45(8)|-0.18(3)|1.15(4); 1.15(4)|||Table 1||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|199.2|12-→11-|2.22+1.37-0.80|-0.25(13)|-0.09(5)|1.11(7); 1.11(7)|||Table 1||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|204.7|15-→14-|3.52+3.37-1.26|0.14(15)|0.05(6)|1.05(6); 1.05(6)|||Table 1||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|229.7|14+→13+|2.86+2.31-1.10|0.31(27)|0.12(10)|1.05(6); 1.05(6)|||Table 1||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|244.6|14-→13-|1.59+0.45-0.55|-0.39(11)|-0.14(4)|1.13(3); 1.13(3)|||Table 1, Fig. 5(a)||
|154Tb|[[polarization-delta-collection-20261119-source#R033\|R033]]|270.5|16-→15-|2.31+0.67-0.52|-0.21(13)|-0.07(4)|1.06(3); 1.06(3)|||Table 1||
|163Lu|[[polarization-delta-collection-20261119-source#R052\|R052]]||43/2+（计算代表值）→41/2+（计算代表值）|-3.10+0.36-0.44||||0.25±0.02|TSD1 (21/2 - 45/2 hbar)|Page 5867-5869, Table I；原文合并带间跃迁分析，计算采用代表自旋||
|163Lu|[[polarization-delta-collection-20261119-source#R052\|R052]]||43/2+（计算代表值）→41/2+（计算代表值）|-0.22+0.05-0.03||||0.25±0.02|TSD1 (21/2 - 45/2 hbar)|Page 5868 (原文被排除分支)；原文合并带间跃迁分析，计算采用代表自旋||
|166Er|[[polarization-delta-collection-20261119-source#R036\|R036]]|817.0|6-→5-|between about 30 and 100|+0.36 (+0.10, -0.13)|N_perp/N_parallel = 1.32 +- 0.09||||p. 675, 678, 681, 684||
|172Yb|[[polarization-delta-collection-20261119-source#R014\|R014]]|1094.0|3+→2+|+3.2±0.2|P(90°)=0.77±0.04||A22=-0.41±0.01; A44=-0.042±0.012||79|Abstract; Sect.3 p.73; Sect.4 p.75; Sect.6 p.78-80; Fig.13, Fig.15||
|177Ta|[[polarization-delta-collection-20261119-source#R008\|R008]]|311.0|21/2-→19/2-|0.29+0.11-0.06||B=0.063±0.031|ρ2A2=0.048±0.007; ρ4A4=-0.006±0.011|||Page 423-424, Section 3.2; Fig. 8 (结合内转换系数限制的最终推荐值)||
|177Ta|[[polarization-delta-collection-20261119-source#R008\|R008]]|311.0|21/2-→19/2-|0.29+0.36-0.06||B=0.063±0.031|ρ2A2=0.048±0.007; ρ4A4=-0.006±0.011|||Page 423, Section 3.2; Fig. 8 (偏振与角分布联合测定分支一)||
|177Ta|[[polarization-delta-collection-20261119-source#R008\|R008]]|311.0|21/2-→19/2-|10.2+2.6-5.6||B=0.063±0.031|ρ2A2=0.048±0.007; ρ4A4=-0.006±0.011|||Page 423, Section 3.2; Fig. 8 (偏振与角分布联合测定分支二，原文被内转换系数排除分支)||
|181Ta|[[polarization-delta-collection-20261119-source#R013\|R013]]|482.0|5/2+→7/2+|7.2+1.8-1.5||k=1.061±0.028 (HCl), k=1.129±0.029 (HF)|A22=-0.091±0.004 (HCl), A22=-0.236±0.006 (HF); A44=-0.011±0.006 (HCl), A44=-0.037±0.010 (HF)||133+137|Page 65, Abstract; Page 71, Table 2; Page 73, Section 6; Page 77, Section 7||
|181Ta|[[polarization-delta-collection-20261119-source#R013\|R013]]|482.0|5/2+→7/2+|7.3+1.7-1.5||k=1.061±0.028 (HCl), k=1.129±0.029 (HF); 476 keV校正因数1.05|A22=-0.096±0.004 (HCl), A22=-0.249±0.006 (HF); A44=-0.011±0.006 (HCl), A44=-0.039±0.006 (HF)||133+137|Page 78, Section 8, Table 3||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|262.0|11/2-→9/2-|-0.12(2)|Fig. 2(a)||Fig. 2(a); Fig. 2(a)|||Fig. 2(a)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|347.0|19/2+→17/2+|0.02(10)|Fig. 2(f)||Fig. 2(f); Fig. 2(f)|||Fig. 2(f)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|368.0|15/2-→13/2-|-0.08(3)|Fig. 2(b)||Fig. 2(b); Fig. 2(b)|||Fig. 2(b)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|457.0|19/2-→17/2-|-0.08(5)|Fig. 2(c)||Fig. 2(c); Fig. 2(c)|||Fig. 2(c)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|495.0|27/2-→25/2-|-2.9(7)|Fig. 2(e)||Fig. 2(e); Fig. 2(e)||502|Fig. 2(e)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|498.0|23/2-→21/2-|-2.9(9)|Fig. 2(d)||Fig. 2(d); Fig. 2(d)|||Fig. 2(d)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|588.0|23/2+→21/2+|-3.1(13)|Fig.2(j)||Fig.2(j); Fig.2(j)||283; 428+283|p.3 Fig.2(j)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|648.0|27/2+→25/2+|-3.2(13)|Fig.2(g)||Fig.2(g); Fig.2(g)|||p.3 Fig.2(g)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|701.0|31/2+→29/2+|-3.5(15)|Fig.2(h)||Fig.2(h); Fig.2(h)|||p.3 Fig.2(h)||
|183Au|[[polarization-delta-collection-20261119-source#N20\|N20]]|751.0|35/2+→33/2+|-3.9(19)|Fig.2(i)||Fig.2(i); Fig.2(i)|||p.3 Fig.2(i)||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|292.3(1)|11/2-→9/2-|-0.03(3)|-0.34(12)|-0.13(4)|0.68(2); 0.68(2)|||Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|395.2(1)|15/2-→13/2-|-0.05(4)|-0.31(10)|-0.11(3)|0.67(3); 0.67(3)|||Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|485.4(2)|19/2-→17/2-|-0.06(6)|-0.34(16)|-0.12(7)|0.66(4); 0.66(4)|||Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|555.6(1)|23/2-→21/2-|-0.07(6)|-0.30(15)|-0.09(6)|0.65(5); 0.65(5)|||Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|554.9(2)|15/2-→13/2-|-3.2(5)|0.19(10)|0.06(4)|0.74(5); 0.74(5)||264|Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|592.4(1)|19/2-→17/2-|-2.6(4)|0.16(13)|0.07(7)|0.49(3); 0.49(3)|||Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|610.7(2)|23/2-→21/2-|-2.4(6)|0.14(11)|0.06(5)|0.48(5); 0.48(5)|||Table 1||
|185Au|[[polarization-delta-collection-20261119-source#R034\|R034]]|518.1(2)|31/2-→29/2-|-3.4(6)|0.21(15)|0.07(6)|0.53(5); 0.53(5)||323, 409, 548|Table 1||
|187Au|[[polarization-delta-collection-20261119-source#G22\|G22]]|376|11/2-→9/2-|-0.26 (+0.11, −0.15)|Fig.3(a)||Fig.3(a); Fig.3(a)||316,319,400,417,471,565,625|PLB 828 (2022) 137010, p. 3 Fig. 3(a); Supplement p. 3 Fig. 2||
|187Au|[[polarization-delta-collection-20261119-source#G22\|G22]]|462|15/2-→13/2-|-0.28 (+0.23, −0.69)|Fig.3(b)||Fig.3(b); Fig.3(b)||316,400; 313（峰左侧）|PLB 828 (2022) 137010, p. 3 Fig. 3(b)||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|274.3|31/2+→29/2+|≈0.4|-1.0(7)||1.00(17); 1.00(17)|0.3|stretched E2|Table 1, Section 2.2 Page 4||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|310.9|33/2+→31/2+|≈0.4|-0.48(36)||0.74(12); 0.74(12)|0.3|stretched E2|Table 1, Section 2.2 Page 4||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|334.7|27/2-→25/2-|≈0.25|-0.41(8)||0.79(8); 0.79(8)|0.3|stretched E2|Table 1, Section 2.2 Page 3||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|463.5|17/2+→15/2+|<0|0.11(21)||0.38(9); 0.38(9)|0.3|stretched E2|Table 1, Section 2.2 Page 3-4||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|515.6|21/2+→19/2+|<0|-0.11(21)||0.36(10); 0.36(10)|0.3|stretched E2|Table 1, Section 2.2 Page 3-4||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|707.8|19/2+→17/2+|<0|0.19(44)||0.26(9); 0.26(9)|0.3|stretched E2|Table 1, Section 2.2 Page 3-4||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|847.4|23/2+→21/2+|<0|-0.02(14)||0.19(4); 0.19(4)|0.3|stretched E2|Table 1, Section 2.2 Page 3-4||
|187Pt|[[polarization-delta-collection-20261119-source#R053\|R053]]|928.9|27/2+→25/2+|<0|0.03(15)||0.22(3); 0.22(3)|0.3|stretched E2|Table 1, Section 2.2 Page 3-4||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|+(10 +2.0/-1.2)|||A22=-0.148±0.013; A44=+0.292±0.020||2(296)2(316)0|Table 2 δ(transition), p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|-(6.2 +∞/-1.7)|P(300–300级联)=-0.020±0.024||||300–300 keV unresolved group|Table 2 δ from polarization, p.172；正文p.175||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|-8.6±2.2|||||2(296)2(316)0|Table 2 δa（综合值）, p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|+9.98 (+0.02/-0.04)|||A22=+0.029±0.013; A44=+0.002±0.020||3(308)2(296)0|Table 2, p.172；脚注b：级联次序改变对应符号改变||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|2.6 to 10|||A22=+0.010±0.013; A44=-0.031±0.020||3(308)2-2(316)0|Table 2, p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|≤-7|||A22=-0.012±0.017; A44=+0.046±0.023||4(589)2(296)2|Table 2, p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|296|2+→2+|-9.0 to -11.0||||||正文p.175 summary（保留原文区间顺序）||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|308|3+→2+|-(7.3 +1.0/-0.8)|||A22=-0.094±0.015; A44=-0.023±0.020||3(308)2(612)0|Table 2 δ(transition), p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|308|3+→2+|-12±0.6|||||3(308)2(612)0|Table 2 δa（综合值）, p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|308|3+→2+|-6.5 to -8.3||||||正文p.175 summary（保留原文区间顺序）||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|604|3+→2+|+2.1 (+0.3/-0.2)|||A22=-0.480±0.016; A44=+0.34±2.23||3(604)2(316)0|Table 2 δ(transition), p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|604|3+→2+|2.4 (+6/-1.6)|P(600–300级联)=-0.129±0.042||||600–300 keV unresolved group|Table 2 δ from polarization, p.172；正文p.175||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|604|3+→2+|1.9±0.4|||||3(604)2(316)0|Table 2 δa（综合值）, p.172||
|192Pt|[[polarization-delta-collection-20261119-source#PT68\|PT68]]|604|3+→2+|+1.9 to +2.4||||||正文p.175 summary||
|192Pt|[[polarization-delta-collection-20261119-source#R004\|R004]]|296.0|2+→2+|15(4)|0.05(4)||A22=0.009(5); A44=0.033(5)|||Table 1, Page 42||
|192Pt|[[polarization-delta-collection-20261119-source#R004\|R004]]|308.0|3+→2+|7.6(1)|0.03(1)||A22=-0.364(6); A44=0.155(6)|||Table 1, Page 42||
|192Pt|[[polarization-delta-collection-20261119-source#R004\|R004]]|604.0|3+→2+|-1.4(1)|-0.27(4)||A22=0.939(12); A44=0.165(14)|||Table 1, Page 42||
|194Pt|[[polarization-delta-collection-20261119-source#R016\|R016]]|294.0|2'+→2+|-(30^{+39}_{-11})|0.034±0.046||A22=-0.101±0.014; A44=0.323±0.022||328|Table 1, Table 2||
|196Pt|[[polarization-delta-collection-20261119-source#R016\|R016]]|333.0|2'+→2+|+4.03±0.12|0.067±0.031||A22=0.113±0.005; A44=0.315±0.010||356|Table 1, Table 2||
|211Bi|[[polarization-delta-collection-20261119-source#R015\|R015]]|405.0|7/2-→9/2-|-0.65 to -2.6|0.066±0.040|k=0.941±0.036|A22=-0.085±0.007; A44=-0.005±0.009||405-427 complex|Table 1, Section 4 (p. 594), Section 5 (p. 598)||
|211Bi|[[polarization-delta-collection-20261119-source#R015\|R015]]|427.0|7/2-→7/2-|0 to 0.175|0.066±0.040|k=0.941±0.036|A22=-0.085±0.007; A44=-0.005±0.009||405-427 complex|Table 1, Section 4 (p. 594), Section 5 (p. 598)||
|215Po|[[polarization-delta-collection-20261119-source#R017\|R017]]|271.2|7/2+→9/2+|sign of δ_γ(271) = +, δ^2_exp = 14.6 +4.9 -2.8|B2 = 0.029 ± 0.011, B4 = 0.0147 ± 0.0042|Fig. 1|A2 = -0.060 ± 0.020; A4 = -0.157 ± 0.020||α(271 keV level)|Table 3, Table 4, p.457, 461, 466||

## Research Trigger

User-requested collection or learning-design question; the original scope and historical stage are retained below.

## Grounded Evidence

Evidence anchors: [[polarization-delta-collection-20261119-source]]. Original locators and actual coverage are recorded in those sources and the tables below.

## Provisional Reasoning

The original discussion below is a scope-bounded data/method comparison or learning design, not a new experimental result or certified field-wide prevalence estimate.

## Assumptions

Bibliographic identity, version and reading coverage must be checked separately; filenames and page counts do not establish independent works or completed reading.

## Competing Explanations

Different reported values can arise from different experiments, conventions or analysis conditions; repeated publication of one experiment is not independent support. No new physical alternative is invented merely to fill this section.

## Transfer Conditions

Reuse only with the original measurement object, geometry/gates, calibration, definitions and uncertainty treatment. Learning-design recommendations remain recommendations, not physical claims.

## Failure Conditions

Missing originals, illegible figures, unresolved version/identity or absent numerical covariance constrain reuse; do not silently fill gaps or claim a full reproduction.

## Falsification or Reverse Tests

Return any material numerical or methodological discrepancy to its source locator; revise the interpretation if the original contradicts the extraction or proposed classification.

## Open Questions

Outstanding scientific or acquisition boundaries are listed in the original discussion below or the linked sources. Historical download requests are superseded by the user closing acquisition.

## Human Review

No new human-reviewed event is asserted. The user closing downloads or accepting a table format does not certify every scientific claim.

## Promotion or Rejection History

2026-11-19: normalized provenance and schema for baseline publication; retained provisional status and original numerical content. No automatic promotion of physical conclusions.
