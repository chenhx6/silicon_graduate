# 028：真实 thesis 能补 D5/D5-C 逐线输入，但不是总 BR 或绝对 B 表

**信息增量成立。** 实际 thesis Table5.1 提供 PE18 短文未逐线列出的 **Eγ、母态Ei、Ji/Jfπ、效率修正相对Iγ、部分RDCO/Rac及multipolarity**。本轮为三个实际母态整理了14条出射线。**这些行没有给 signedδ、ICC、每次总衰变分支、τ 或 absoluteB**；不能把行内相对强度重新归一就称 totalBR。D5双方 B(M1)/B(E2) 的真实支持保留，旧“假SI中有δ/absoluteB表”的说法不恢复。

## 原件、目录与实际 scope

Bingfeng Lv, *Chirality in the136Nd and135Nd nuclei*, Université Paris-Saclay thesis,2019，NNT2019SACLS353。现有body：`raw/theses/degree dissertation/吕冰峰.pdf`，164页/6844285bytes，SHA256 **84e8b934fda9a97ea79527a8b1456f40e534bc67be847d61b1a1219002d85749**；封面原标识 `https://theses.hal.science/tel-02347000`。本轮**零网络调用**，未改raw。

目录定位 physicalPDF6–8 后，当前实际读：

- **连续方法章：physicalPDF66–71 = printed65–70，Chapter4全部**；不是164页全读。
- **连续dipole段：physicalPDF76–81 = printed75–80，§5.1.3及Figs5.6–5.11**；开头页面含上一节结尾，保留真实连续范围。
- **Table5.1标题和全部D5/D5-C行：physicalPDF85、93–95，printed84、92–94；完整footnotes physicalPDF97/printed96。** 没有审计整张表其它所有bands。
- **比例解释：physicalPDF102–103/printed101–102，Fig5.18及相邻连续段**；保D5较强、四弱partner无自己的比值。
- **定向几何：physicalPDF59–60/printed58–59，§3.4；physicalPDF153–154/printed149–150，AppendixA/TableA.1。** 另少量标题/临近表页用来定位，不冒称其它章全文精读。
- 新视觉核方法PDF66/68/69/71、schemePDF77、门谱PDF81、表PDF93–95/97、ratioPDF102，以及探测器PDF59–60/153–154。原source已覆盖的全文阅读不自动转成本轮覆盖。

`receipt.json`详列scope；本单元没有寿命/强度拟合、未知代码/114或作者producer执行。

## 实际方法输入：哪些能落地，哪些仍缺

| 字段 | 原文实际给出 | 不应扩大为 |
|---|---|---|
|campaign|JYFL152MeV40Ar+100Mo(xn)，约14pnA、约一周allocatedbeamtime，0.5mg/cm²自支撑靶；135/136Nd同一研究采集，5.1×10^10fold≥3promptcoincidences，约4000Gb/2000files（PDF66）|独立于PE18/LV19的第二次测量；每个核或每条线的selectedeventcount |
|eventclock|TDR100MHz、10ns时间戳（PDF66）|高spinD5母态的ps寿命或τ测量 |
|energy/efficiency|152Eu/133Ba能量标定；ENCAL二次多项式；EFFIT形式与A6.2/B1.8/C0/D5.5/E.6/F0/G20的效率拟合参数（PDF67–68）|每个detector/每个run的校准表、完整uncertainty/Cov、原始净计数 |
|Doppler/addback|统一β=.0245能量校正（PDF68）；同clover200nsaddbackwindow（PDF60）|DSAM stopping-time分析；与MU08厚靶时钟相同 |
|RDCO|157.6° 对75.5°+104.5°≈90°的asymmetric矩阵；explicitEq4.8及Tablefootnotese/f gateclass（PDF69–70/97）|每条Iγ的exactgate相同，或仅凭DCO可定parity/δ |
|Rac|133.6°+157.6° 对75.5°+104.5°，两矩阵同all-angleenergygates，按组效率归一；typicaldipole≈.8/quadrupole≈1.4（PDF70–71）|直接δ拟合、对任意线响应已标定或消除了feeding/背景 |
|polarization|PDF71明确RDCO/Rac不能独立定parity，电/磁需polarization并引Ref96|本D5表每条线都有P、Q(E)、δ或相干M1/E2分量 |
|Iγ|Tablefootnoteb：已效率修正，**对373.7keV归一**，来自totalprojection+gatedspectra组合（PDF97）；GSB2+→0+373.7行I=100（PDF85）|每次leveldecay的absolutephotonprobability或totalBR；全部出射/IC闭合 |

与DD-20260910-136ND-01/02关系：共同campaign/谱学总框架原已收录，本轮新增的是**具体可追溯的方法参数、D5母态逐线库存及保留unknown字段**。这是同一源/采集的深挖，不是独立重复确认。PE18原“假SI”是另一个reprint的身份错误；thesis是真实独立文档，但数据仍有血缘依赖。

## 39 detector 的正确分组和 active-count 边界

§3.4直接写 **24clover+15tapered=39个detector houses**，四个polar rings：

| θ | 类型/nominal数量 |
|---|---|
|75.5°|12clovers|
|104.5°|12clovers|
|133.6°|10tapered|
|157.6°|5tapered|

AppendixA另列每个detector的azimuthφ，φ0为竖直向上、从upstream观看顺时针增大（PDF153–154）。所以 **39不是39个polar-anglegroups，更不等本次具体run/line活跃detector mask**。未给每个run的disabledcrystal/deadtime/selectivecuts记录，不能补actualactivecounts或把效率参考值作本条线计数率。

一个原件局部边界：TableA.1在PDF154把75.5°/φ135°那行又标为**Q14**，前面φ45°已有Q14，而Q17未另列。保留字面重复，不擅改ID；**不据此断言只有38个active探测器或某个通道失效**。几何表不是active-mask日志。

## 三个真实母态的出射线账本

所有Iγ均是上述373.7-reference的relativeintensity。表中“e/f”仅说明DCO的stretchedquadrupole/dipolegateclass，**不是Iγ具体门谱的唯一producer标识**。统一unknown字段：δ、ICC、totalBR、per-parentphotonprobability、τ、absoluteB和exactIγgate；JSON以null保留。

### D5，Ei6521.8keV，18+

| EγkeV | Iγ | 原mult. | Ji→Jf | 原角比 | Locator |
|---|---|---|---|---|---|
|283.8|2.5(4)|M1/E2|18+→17+|RDCO=.84(15),f|PDF93/printed92|
|515.6|.35(10)|E2|18+→16+|RDCO=.92(33),e|PDF93|
|579.8|1.01(8)|M1/E2|18+→17+|RDCO=1.22(18),f|PDF94/printed93|
|764.6|1.9(2)|E2|18+→16+|RDCO=2.16(29),f|PDF94|
|826.9|2.7(3)|E2|18+→16+|RDCO=2.15(30),f|PDF94|
|951.8|.16(2)|E2|18+→16+|Rac=1.31(22)|PDF94|
|1330.5|**<.01**|E2|18+→16+|—|PDF94|

283.8、515.6分别接D5的6238.0/6006.2母态序列；其它daughter需保具体level/family绑定，不能把所有E2都叫带内crossover。764.6的条件daughter能量5757.2与该表γ-band16+节点相合，但不据算术把其它未定family强行填满。<.01是原印relativeI上限，原文未给其coverage/检测阈值合同；不擅作95%CI或absolutebranch上限。

### D5-C，Ei7543.0keV，20+

| EγkeV | Iγ | 原mult. | Ji→Jf | 原角比 | endpoint范围 |
|---|---|---|---|---|---|
|330.0|.42(9)|M1|20+→19+|Rac=.69(15)|到D5-C7213.0；PDF94|
|611.4|.21(10)|E2|20+→18+|—|scheme候选带内；Ei−Eγ=6931.6为条件daughter能量；PDF94|
|1021.2|.6(1)|E2|20+→18+|Rac=1.42(21)|到D5的6521.8；PDF95/printed94|

这三I之和不是1、也不应被改成1；相对光子强度库存与totalBR是不同量。它们可支持后续同parent、同component且响应匹配后的条件比，但当前不产生绝对B或已测τ。

### D5-C，Ei7927.1keV，21+

| EγkeV | Iγ | 原mult. | Ji→Jf | 原角比 | endpoint |
|---|---|---|---|---|---|
|384.1|.6(1)|M1/E2|21+→20+|Rac=.71(13)|D5-C7543.0；PDF94|
|672.5|.5(2)|M1/E2|21+→20+|RDCO=1.45(48),f|D57254.6；PDF94|
|714.1|.18(4)|E2|21+→19+|Rac=1.33(40)|D5-C7213.0；PDF94|
|1060.7|.8(4)|E2|21+→19+|—|D56866.4；PDF95|

daughterenergies在JSON中明确标为**Ei−Eγ的条件计算**，非本轮新测量。源Fig5.6和表level支持这些family绑定；模式M1/E2不等已给δ。一次line可以同时有DCO与relativeI，其背景/门差异和Cov仍未知。

## 真正补了什么，仍没有补什么

| 可用程度 | 本轮落点 |
|---|---|
|**已补具体输入**|D5/D5-C逐线Eγ/Ei/Jπ/Iγ、部分角比/赋值、D5spectralgates、373.7归一参考、DCO/Rac分角定义、名义几何、EFFIT与β/addback参数|
|**可缩小的研究问题**|可明确哪条带内线/跨带线共母态，哪些mixedcomponent需要δ，哪些daughter未知；可给后续原分析/同门producer请求具体对象|
|**未补**|signedδ、ICC、totaldecaybranch、漏枝/非γ完整性、每条Iγexactgate/背景/response/Cov、同runactive-mask、D5/Cτ或absoluteB|
|**真实支持保持**|PDF80/102作者说D5与D5-C强度足以提双方B(M1)/B(E2)且相近；Fig5.18实际画双方ratios。更细表让relativeEM检验可追溯，不撤去这一正支持|
|**不恢复**|旧reprint被误认SI的δ/absoluteB表；用10nsTDR当τ、用oldMU08负带τ给positiveD5、按relativeI或相同eventcount认证same-selectedproducer|

Fig5.11的确给D5门谱：对230/284/345/388/463-keV组合的doublegates求和（PDF81）。但Tablefootnote说Iγ由totalprojection与gatedspectra组合取得，**没有逐行声明本账本14线都来自Fig5.11的同一门/背景/响应**。图的gate信息不能自动补进每行exactgate字段。

## 建议新增的atomic草稿

这些是对DD-136ND-01/02的细化，均needs_review:true；不改原flags、人审或学分。

1. **TH19-D25P-001**：Table5.1的D5/D5-C实际逐线输入覆盖Eγ/Ei/Jπ/相对Iγ/部分DCO-Rac/mode，footnoteb按373.7归一且混合totalprojection/gatedspectra；未给这些态的δ/ICC/τ/absoluteB。Locator：physicalPDF93–95/97，printed92–94/96。
2. **TH19-D25P-002**：三个母态6521.8(18+,D5)、7543.0(20+,D5-C)、7927.1(21+,D5-C)的14条出射线可作父态库存，不能由Iγ重归一认证totalBR或同gate。Locator：同表及`d5-parent-line-ledger.json`。
3. **TH19-D25P-003**：39是24clovers+15tapered的名义detectorhouses，分四polar rings；AppendixA给azimuths，不给runactive-mask。表中重复Q14应保literal，不推activecount。Locator：PDF59–60/153–154，printed58–59/149–150。
4. **TH19-D25P-004**：Ch4补actualprocessing参数与100MHz10nsTDR，但后者是eventtimestamp，不是D5/C寿命；与PE18/LV19同campaign，非新增独立采集。Locator：PDF66–71、Fig5.11/footnoteb及既有DD-136ND-01。

## 完成状态

本单元按**明确scoped方法/表段**完成；不是164页全文或Table5.1所有bands闭合。它提供真实信息增量，PE18假SI和PRC98,044304的body0/transport失败历史仍各自保持，不用thesis冒充已取得那篇期刊正文。只写assignedworker与tmp；canonical/raw/PLAN/Bib/Git、session/课程信用不变。仍sameDay24run＋恰好Day25preview，未开Day26、未运行114。


## 实际可算的同母态 E2 比：缺 τ 不等于所有 EM 都不可计算

按 root 后续指示，对 **D5-C 20+、Ei7543.0keV** 的两条实际 E2 行建立单一有界对照：611.4-keV、Iγ=.21(10) 为 scheme 中带内20+→18+候选；1021.2-keV、Iγ=.6(1) 到 D5 18+ 的6521.8keV态。两行分别在physicalPDF94/95，均印E2；共同归一参考在PDF97。

在**同母态、同XL=E2、端点赋值正确、相对Iγ代表经匹配响应的无偏photon强度**条件下，

`B_out(E2)/B_in(E2)=(.6/.21)*(611.4/1021.2)^5 = 0.2197885667`。

相对光子强度商为2.8571428571，能量五次方因子为0.0769259984。**共同τ、全局强度参考和E2率常数消去，因此此条件比不需要τ或全parent总BR。** 原报告“未补absoluteB”不应被理解成“没有任何可计算EM约束”。

但是，两个Iγ来自totalprojection/gatedspectra的组合，具体门/背景/feeding/效率响应是否匹配和jointCov仍未给。这里不给CI、不把quotederrors当独立、不给absoluteB/δ/phase、不作模式排他。无需先把14行归一成totalBR。完整输入和条件见`same-parent-e2-ratio.json`；其它21+出射线继续全部保留，不为形成比而删行。
