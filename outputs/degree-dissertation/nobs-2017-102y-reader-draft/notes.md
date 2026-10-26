# Nobs 2017 学位论文深读：102Y 自旋宇称指认的条件证据链

状态：独占临时研究草稿；Codex source self-audit，非 human-reviewed。Day23 补充阅读，不改变 Day23 signature/wobbling/TiP/MR/AMR 主线、课程卡或学分。全文索引不等于全文翻译，关键图视觉核验不等于所有图数字化。

来源：Chantal Rebecca Nobs，*Spin and parity assignment for the ground and isomeric states in 102Y*，University of Brighton，题名页 June 2017、作者声明26/06/2017，PDF metadata creation January 2018；不得用PDF生成日取代学位年份。原PDF138页，SHA256 `acb846d63e4a8cc61491d6f5ba04a4858bf3efd3e98bb9152b50383987b76a57`。PDF19=印刷p1，之后固定PDF=印刷+18。原件始终只读。

## 实际阅读账本

已按顺序读PDF1–138的原生可提取文本：题名/摘要、目录/图表清单、致谢/声明、正文全9章和完整参考文献；正文读的是文字及可提取表格内容，不是只跑关键词。全部文本已读不表示所有图/公式已视觉核对、所有背景事实已外部验证或全文已译。段落合并是page-local fragment，跨页/内嵌数学可能截断；完整native blocks另保留。PDF图片中的符号与数值以视觉记录为准。

视觉已查看16张整页contact-sheet原图：PDF54、57、59、60、64、83、107、109、111、113、114、117、119、123、125、129；并放大核PDF125 Fig8.8。细小数值未逐一数字化。其它122页尚未作逐页视觉审读，其科学图的文字图注已读，不能标成全图核准。

|章节|实际文本阅读页（印刷；PDF）|论证功能与关键locator|尚存边界|
|---|---|---|---|
|前置|i–xvii；PDF2–18，题名PDF1|摘要提出5−/0−与100keV，目录确认9章、69图15表|摘要省略条件，不能单独作指认依据|
|1 Introduction|1–3；PDF19–21|p2说明IGISOL两实验、RIKEN两路径；作者未参加RIKEN实验|setup信息来自共享实验及同事/既有来源|
|2 Theoretical Background|4–22；PDF22–40|p16–18 E2能量经验与寿命/B(E2)两类β2比较；p19 Cheal I=2/3歧义；p20–21 Table2.2旧两路径|背景/经验关系非新实验；R4/2、Grodzins不能独自定形；源中有记号/背景疑点|
|3 Experimental Details at IGISOL|23–37；PDF41–55|p30–32未分辨；p33 tape/几何；p34–36能量/效率校准；p37数字25ns|首轮效率源外置≠implant point；两轮DAQ、计数率、tape周期不同|
|4 IGISOL Data Analysis and Results|38–53；PDF56–71|p41/Fig4.3不明确趋势；p46/Table4.1+Eq4.1模板混合；p47/650ns；p49/Table4.2和门谱|没有纯态分离；共同152归一、历史模板依赖；82:18与后文78:22冲突|
|5 Experimental Details at RIBF|54–57；PDF72–75|345MeV/u U+Be；WAS3ABi5 DSSSD、EURICA84HPGe；p56–57效率/addback/100µsDAQ|同一2013数据重分析，作者非在场；Fig5.3 caption relative/y轴absolute不一致|
|6 RIBF Data Analysis and Results|58–78；PDF76–96|p58两run组/PID；p61 1.5s/晚窗；p63–65短窗扣谱与Table6.1；p68±300ns；p73–78 Y支路|两路径统计/喂入不同；短窗非严格纯Y；γ-γ随机未扣；无新AD/P/δ/Q/τ|
|7 BCS Calculations|79–93；PDF97–111|p81 pairing；p86仅prolate；p87 μ调参；p88–89邻核经验校正；p90–91 GM；p92–93 W.u.估计|非参数自由预测；残余pn相互作用未含；300keV不是拟合/测量；Table7.3单位疑点|
|8 Discussion|94–109；PDF112–127|p96–98双1059/283与764放置；p100 Jπ继承；p103–105条件5−/0−+X；p107 inherited logft；p108选择规则|同位素谱学加模型辅助；不是直接Jπ测量；内部ratio/交叉引用错误须保留|
|9 Concluding Remarks|110–113；PDF128–131|p111未分离与路径结论；p112 prolate条件和laser冲突；PI-ICR outlook|p111 high/low路径写反，与Ch6/8相抵触；未来精度不是本实验性能|
|References|114–120；PDF132–138|完整83条元数据已读；Refs8/9/37/68–78谱系|未外取83篇原件；同文献重引不增加独立证据|

## 主要实证链

### 1. 先观察两个population pattern，再作Jπ模型辅助解释

Hill1991（Ref8）TRISTAN主要由102Sr→102Y→102Zr观察low-spin-like pattern；Shizuma1983（Ref9）JOSEF直接102Y decay主要high-spin-like pattern。旧high-spin列不是“单纯另一个纯态实测模板”：Table4.1/6.1 caption明确由TRISTAN与JOSEF合并推得。Nobs取得新的IGISOL/RIKEN数据对比，但旧列彼此依赖，不应数成多份独立high-spin determination。

IGISOL首轮Ramsey频率扫描未出现可分离双峰（印刷p30–32、38–42，Figs3.8/3.10/4.1/4.3）。Fig4.1两条Gaussian是示意可能位置；caption写superimposed to indicate a possible position，不能改写成双峰拟合证据。p41明确强度随频率变化的大误差使结论不明确。作者从未分辨宽度与历史population推得E_x<100keV；原文未提供覆盖率/CL、检测能力全模型或可复现上限拟合。故可写“作者据未分辨提出约100keV上限”，不能写“95%CI或直接精密质量差测量”。

IGISOL次轮仅净化阱，约10ions/s，保留混合样本（p32/43），Table4.1强度相对152keV归一。Eq4.1 I_meas=a I_ls+(1−a)I_hs，p47说明对159、326、579、1059、1090五线求a再平均；列中a=0.22、0.27、0.09、0.11、0.22的中央均值0.182。该操作是共享归一模板混合系数，没有给出完整Cov、权重或population-recovery效率；不能无条件等同绝对产生截面/原始态数比。p46写18:82，p94/97/109写22:78；保留并列，不择一抹平。

RIKEN把同一2013实验的两run组分开：criterion1选102Sr（451754 implants），criterion2选102Y（2130924 implants），p58。Table6.1（p65；PDF83）主要差异：326keV为8(1)与48(3)，1059为30(3)与13(2)，1211为37(3)与8(2)，全部相对152keV=100。此直接观测支持两条population pattern，不能单凭相对强度唯一倒推出β母态Jπ或集体模式。

### 2. 校准、时间窗和扣谱是观测定义的一部分

IGISOL能量用152Eu+133Ba的16线80–1408keV作线性channel-energy calibration（p34–35）。首轮源置β探测器外、距Ge约1cm，次轮源才位于implant point（p35–36，Figs3.15/3.16）。几何不匹配导致首轮相对效率的系统边界，论文未给完整几何修正/Cov。tape周期首轮60s、次轮10s；β/Ge几何和Ge数也不同（p33）。首轮analog 11µs master window及β>150keV、β<4000keV、γ>10keV（p37）；次轮triggerless timestamp25ns（p37），βγ上限1.5µs且sorting software不能设下限（p43），γγ650ns（p47）。这些门不能挪到其它阵列。

RIKEN能量源152Eu、效率源152Eu+133Ba；紧密HPGe addback需两晶体各沉积>120keV、105ns（p56）；每implant/β trigger的γDAQ窗100µs（p57）。ion–β选≤1.5s，减2–3.5s晚窗（p61/Fig6.4）。criterion1有102Y150keV与102Zr152keV重叠，于≤20ms谱（减2–2.02s）按244keV归一后扣除Y成分（p63–64/Fig6.5）。20ms降低而非数学上消除Y→Zr二次β的概率；paper称“only Y”是其工作近似。未提供早/晚窗的完整链式Bateman/异能态acceptance、共享归一Cov与残余Zr污染的数值上界，不能自行补零。

RIKENγγ正文p68先说±300ns，随后写<300ns；对称矩阵，随机太少未扣。未提供原event、runlists、gate widths、efficiency coefficients、peak fits和Cov，不能从论文完整重现γ强度CI。Fig5.3 y轴Absolute Efficiency(%)而caption称relative，故绝对效率解释须另核原calibration。

### 3. 不同门下1059keV线不能自动是同一条transition

p96–97/102给两种解释：旧实验statistics不足；或者102Zr有两条近同能1059keV线，分别落到152与478keV层，其population随β母态改变。IGISOL与RIKEN criterion2看到1059–326 coincidence，遂把1059.5置1538→478。criterion1未见该coincidence，正文预计约3counts的弱峰需要更多statistics；这不构成双线唯一证明。Durell1995 Ref78的248Cm spontaneous-fission图（本论文Fig8.3 p99/PDF117）支持1538→478支路；当前仅视觉读的是论文重印图，尚未独立外取Durell原件。

283keV在IGISOL见152/326 coincidence，未见1059 coincidence；p97根据1821–1538能差、与579强度及Ge效率（1059约3.6%、326约7.6%）支持放置1821→1538。该放置还有Durell图支持，不能伪称本数据直接看到283–1059 coincidence。764keV见152/326/579 coincidence，支持1242→478；p102 singles I1090/I764=11(3)，gated=7(3)近似相容。p98却写I764/I1090=11(3)，与Table4.1和p102是反比冲突；中文忠实保留原句并在注记说明，不暗改原文。

### 4. 5−与0−如何得到，以及不能声称什么

模型链：Jain1995 Ref68原用于mass180的blocked BCS代码→pairing改用N=63/A~100区Ref69的Gp/Gn（p81，Eq7.5）→只取prolate（p86），ε2=.3→κp=.065、μp=.32、κn=.07、μn=.39；μp原.57不收敛降到.32（p87）→在101Y/101Sr/103Zr以已知轨道能量经验校正，Table7.2/7.3→102Y低组态ν5/2[532]⊗π5/2[422]给K=5−/0−候选→GM Eq7.13因两者Ω=Λ+1/2，取5−较低（p90–91）→高多极低能0−→5−γ衰变受抑，0−可能β-decay isomer（p93/103）。

这不是angular correlation、linear polarization、conversion-electron multiplicity或直接g-factor测量给出的独立Jπ。全文native-text中未出现angular correlation/polarization/mixing ratio/logft字符串（logft在Fig8.8图像中）；检查方法就是核正文实验分析章节而非以关键词无命中作为“缺测”唯一证据。论文没有报告本研究AD/P/DCO/δ；没有新拟合的absoluteβfeeding/Qβ/logft或状态分离寿命。寿命300/360ms来自Ref37，Weisskopfγ寿命是计算。

模型只画prolate，不等于实验排除了oblate。p86形状动机是相邻偶偶100Sr/102Sr/102Zr/104Zr的Skalski模型β2=.35/.36/.36/.37；odd–odd102Y的形状仍是类比与假设。p112作者承认与Cheal2007 laser tentative I=2,3不一致；当前未取得Cheal原件，不裁决谁对。

Table7.4的双态共同BCS能量不包含残余pn splitting，p90说明可达几百keV。默认双态间隔300keV（p93/103/105）是illustrative，p105明确承认若真300keV不应难分辨，最终Fig8.7以0−能量X代替，作者置X<100keV。0−γ半衰期3.26×10^12s来自该300keV/Weisskopf设定；不能当实际测量或移植为其它核异能态寿命。

102Y激发态1+部分由Hill1986 Ref37继承（p105），Fig8.8（p107/PDF125原图）在1689.57、1347.92、497.80、243.85keV旁列1+，左侧Iβ依次17、21、5.7、35及logft4.5、4.5、5.3、4.5。这些图内数字在native提取中缺失，已视觉补记；它们属于重印旧方案，不是Nobs重测logft、完整feedings或uncertainty。对应新Fig8.7按未知X整体偏移，不能把旧绝对能量与新ground0混成同一零点。

p108 Eq8.1列allowed/1st/2nd forbidden的ΔI/Δπ，作者解释5−母态主要allowed到negative-parity states，0−主要first-forbidden到positive-parity states。这是给定Jπ后的相容性解释，βhalf-life还依赖Q、分支matrix elements；仅300/360ms相近不能唯一验证Jπ。不要把摘要中“has been shown”升级为无模型实验排他认证。

## 原文内部问题与未裁决项

1. p46 vs p94/109：18:82与22:78两套IGISOL混合比例；Table4.1五a均值对应前者。未建立原peak/Cov重拟合，不发布单一精确population。
2. p111（PDF129）结论把直接Y→Zr写成低spin、Sr→Y→Zr写成高spin；与Table6.1、p100、p112的相反归属冲突。已原页视觉确认，不能沿用孤立结论段。
3. p98 I764/I1090=11(3)反比冲突，p102为I1090/I764=11(3)。Table4.1 3/33支持小于1的前者；属于source typo候选，不是暗改后的新原始值。
4. p64 Fig6.6(a)/(b)在连续正文中两次互换；caption与p65实图(a)为Sr、(b)为Y，按caption/table标识并保留冲突。
5. p20/p30 ground/isomer half-life写300/360ms；p61/p108 low/high写300/360ms，而模型ground=high。只能把low300/high360注明为继承值，并单列ground/isomer映射冲突；当前不做新寿命判定。
6. Table7.3（p89）原页列“Change in quasiparticle energy (keV)”但数值±0.1–0.9，与Table7.2需数百keV的改变尺度不一致。可能单位或代码内部量不同，当前没有input/code，不能自行改成MeV。
7. Fig7.2 caption ε4=ε2²/6用于proton，Eq7.10b却对N,Z≤50规定ε4=0，需原代码input确认；不宣称完全复现BCS。
8. Eq7.9b印ω_z²=ω_0(1−2ε2/3)，与频率量纲疑点；保留原式，未用它数值模拟。
9. p93“0+→0−无γ因此IC更可能”的概括不能拿来当一般E0规则；E0本身不能改变宇称，此段缺通道/相互作用说明，当前不采纳其IC断言作为事实。
10. p6 HO累计44/92、Nilsson符号K[NnzΩ]与后文Kπ[NnzΛ]、Eq2.6系数/单位等背景需教科书独立核验；本任务不依其作新推导。
11. p105 Fig8.7箭宽指Table4.1但Y intensity实际在Table6.3；p106声称看到喂入209的transition与Ch6低statistics措辞等也需逐线核，不升级所有放置。

## 与Day23主线的可迁移方法边界

可迁移的是证据结构：先核population/transition identity，再检验Jπ与电磁矩阵元；保留不同feedings、相同Eγ双线、resolution/no-observation、归一与校准依赖；把邻核校正与本核新观测分开。signature partner、wobbling、TiP、MR/AMR每个假说都应预测同一组逐线观测，能谱相似或计算能级排序不能替代AD/P/δ/τ/绝对B等缺失量。

本论文不测Day23的wobbling phonons、TiP转轴、shears geometry、MR/AMR B(M1)/B(E2)随spin变化；GM doublet的平行/反平行intrinsic coupling不是signature partner、chiral doublet或wobbling phonon。102Y的低能β-isomer不可直接给A≈130带的lifetime、δ、g、Q、efficiency、alignment或spin赋值。W.u.计算与阻碍解释不冒充实验transition rate。

## 十条最有价值的原子化claim

|ID|可用措辞|证据层|精确locator|
|---|---|---|---|
|NOBS-01|首轮Ramsey扫描未干净分离两态，强度随频率的变化在误差下不明确|实验结果/作者评价|p41/PDF59，S0101–S0102；Fig4.3 p42/PDF60|
|NOBS-02|首轮效率源在β-detector外，次轮才置implant point|实验校准|p35–36/PDF53–54，S0088/S0090；Figs3.15/3.16|
|NOBS-03|IGISOL混合系数以旧low/high模板Eq4.1逐线求a再平均|作者分析/依赖|p46–47/PDF64–65，Table4.1、Eq4.1、S0112/S0113；82:18/78:22冲突另列|
|NOBS-04|RIKEN两个选择路径的326keV相对强度分别8(1)和48(3)，152归一100|直接报告表值|p65/PDF83，Table6.1；Fig6.6 caption定义(a)Sr/(b)Y|
|NOBS-05|Sr路径用≤20ms、244keV归一谱扣除Y成分，以处理150/152keV重叠|数据处理|p63–64/PDF81–82，S0141/S0142；Fig6.5|
|NOBS-06|1059keV放置保留低statistics与两条近等能transition解释|竞争解释|p96–97/PDF114–115，S0223/S0224；p102/PDF120 S0234|
|NOBS-07|BCS质子μ因不收敛从.57改.32，再按邻核能级校正|模型/校准|p87–89/PDF105–107，S0195–S0200；Tables7.2/7.3|
|NOBS-08|ν5/2[532]⊗π5/2[422]给5−/0−候选，GM规则取5−较低|模型辅助Jπ|p89–91/PDF107–109，Table7.4、Eq7.13、S0205–S0207|
|NOBS-09|300keV双态split为default，最终改未知X<100keV，非测得300keV|作者模型/实验约束解释|p93/PDF111 S0215；p105/PDF123 S0238、Fig8.7|
|NOBS-10|Fig8.8的1+及logft4.5/5.3属于继承Hill1986方案，不是Nobs新logft测量|旧图重印/来源谱系|p105/PDF123 S0239；Fig8.8 p107/PDF125，放大图已核，Ref37 p116/PDF134|

## 尚缺输入与下一步

不需要用户立刻补交材料。若要重分析而非源读，需要两IGISOL与RIKEN逐run event/peak积分、效率原源数据及其几何、时间窗/随机归一、共同152/244归一Cov、BCS原码/input/修正单位、纯态质量差/状态分离测量、Hill1986/1991、Shizuma1983、Cheal2007和Durell1995直接原件。当前十claim可按其边界写入由主代理管理的knowledge；这里未改任何science/review状态。


可复用证据链已写入canonical：[Nobs source](../../../knowledge/sources/nobs-2017-spin-parity-102y-thesis.md)，本reader不作为第二事实源。
