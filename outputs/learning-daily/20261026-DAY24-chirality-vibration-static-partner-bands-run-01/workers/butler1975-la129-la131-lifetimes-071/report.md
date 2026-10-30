# 071：Butler1975 La 寿命 primary 与 PartII Table5 的数据／定标依赖

**完整4页全文、Figs1–2、Table1及公式／脚注／参考已直接原读和逐页视觉核。** `primed-recall.md`在打开正文前写，明确已有PartII Table5预暴露，非盲测。原件提供真正新的RD寿命实验依据；PartII转引同一组B(E2)不再计另一份实验或独立理论票。

## 身份、获取和重叠

P.A.Butler,J.Meyer-ter-Vehn,D.Ward,H.Bertschat,P.Colombani,R.M.Diamond,F.S.Stephens，**“Triaxial shapes in light La nuclei”**, *Physics Letters B*56(5)(1975)453–456，DOI`10.1016/0370-2693(75)90410-4`。Crossref bibliographicsearch后exactDOI200匹配七作者/题名/卷页；PDF刊头26May1975、received11April1975，日期分开。

定向Wiki/source/blueprint与raw文件名搜索未见同一primary；PartII已有Table5转引，Nolan/别的Butler1975引用为其它源，不构成该正文已读。阴性结果不称全库全部PDF内容搜索穷尽。

直接body：`tmp/day24-butler1975-la129-la131-lifetimes-071/attachment-object-response.pdf`，**4页、268368B、SHA256`231b6f427ac9bdd15688bf373959d2dff63dd7e694ee2dbb9b12cc0186ba8e0a`**；%PDF/pdfinfo/首453末456和身份均核。合法配置ElsevierFULLXML→实际`1-s2.0-0370269375904104-main.pdf`→Object API，两次200无失败/OAfallback；XML43836B，SHA`fb4c59cf6d3b5c9917c593a03e27bdff25ca0facf5811ac18d13c0f0cfd28cd9`。helper按`--si`运行；inventory中的si1.gif为ALTIMG/abstractattachment/11×35px，不冒作SI；仅记未识别真实SI，非全局绝无SI。凭据仅私有module/HTTPheaders，未打印或改写；全部资源仅tmp，raw未摄入。

## 实测响应：recoil-distance、校正与联合馈入拟合

PDF1/453明确采用**recoil-distance**，不是DSAM，也没有本篇宣称DDCM无feeding法。LBL88inchcyclotron的反应与靶为：

| 对象 | reaction/beam | target |
|---|---|---|
|129La|119Sn(14N,4n)，67MeV|Sn selfsupportingfoil .75mg/cm²|
|130Ce|118Sn(16O,4n)，82MeV|Sn selfsupportingfoil .75mg/cm²|
|131La|116Cd(19F,4n)，72MeV|enrichedCd .6mg/cm² onNi .2mg/cm²|

Ni是所述**靶backing**，不能补写成paper已给plungerstopper材质。planarGe置0°。各最低yrasttransition分别积分stopped`Is`与moving`Im`，画`Is/(Is+Im)`对plungersetting；Fig1为131La，15/2→11/2用上方0–400µm尺度，19/2→15/2及23/2→19/2用下方0–100µm尺度，**两横轴不能误作同一距离刻度**。曲线点不是公开rawhistograms或新可直接拟合count集合。

PDF1末–2首：131La15/2→11/2在最大距离（flight400和1600ps）仍见**14% stoppedcomponent**，作者主要归因直接进入15/2的sidefeeding；Fig1已作此分量修正。本文未给逐distance原始峰面积/这项修正的完整公式与Cov，不能把图当未修正纯指数，也不把14%当每个核/每条线普适sidefeedingfraction。

平均recoilvelocity由stopped/movingcentroidshift得，并修正Ge finite-solid-angle：129La`.0087c`、130Ce`.0103c`、131La`.0105c`。targetthickness与recoilcone造成明显projectedvelocityspread，作者说显式纳入后与averagevelocity法结果没有显著差别；这是其数据/范围内的检验声明，不是所有plunger实验可忽velocitydistribution的定理。距离零点、stopperresponse、效率／峰面积共同systematics的完整manifest没有随本文公布。

PDF2–3：每核同时least-squares拟合15/2与19/2（even2+/4+对应）两decaycurves；19/2以上feeding用**两个或更多自由寿命的levels**近似，由23/2→19/2curve形状和所有curve共同origin部分约束；当cascade相对强度随spin明显下降，也加入来自其它levels的feeding。故`τ15,τ19,feeding,origin`不是天然独立估计，未知jointCov不能由四个单误差反推。τ栏是寿命记号，不能当T1/2再加/除ln2。

## Table1 的 measurement → B 链与所引 core 数据

Table1原表 `B(E2)↓ [e²b²]`，a=presentresults。以下新La数据直接对应各**母态寿命**，不是同一band平均：

| nucleus / transition | EγkeV | τps | experimental B(E2) | theory strongK1/2 / K11/2 | weak | aligned γ0 / γexp |
|---|---:|---:|---:|---:|---:|---:|
|129La15/2−→11/2−|269|130±6|.42±.02|.53/.07|.33|.50/.37(γ22°)|
|129La19/2−→15/2−|475|8.7±1.3|.38±.06|.55/.22|—|.52/.42(γ22°)|
|131La15/2−→11/2−|336|55±2|.34±.02|.49/.06|.30|.45/.32(γ23°)|
|131La19/2−→15/2−|533|5.8±.6|.33±.03|.50/.20|—|.47/.37(γ23°)|

原文把这些downwardtransitions作为E2比较，先前level/decoupledconfiguration见Refs1/2；**没有逐支branchingratio、ICC数值／采用表或conversion代码、完整出口sum、逐支pureE2validation表**，也没有列寿命→B的实际转换程序。因此能保原reportedB，但不能声称本轮仅凭τ/Eγ已精确重现全部B或缺省每个transition的totalbranch=1/ICC=0。空weakhigher项不以1.4/2.0随手补入。

| core/comparison | 原表Eγ/τ/B | 测量来源与角色 |
|---|---|---|
|128Ba2+→0+|279keV，140±30ps，.33±.07|Ref6 Kutschera等PRC5(1972)1658；129La邻coreinput|
|130Ce2+→0+|254keV；prior225±19ps[4]，present211±9ps[a]；该rowB.33±.02|本文另反应测core，且与Ref4 DehnhardtNPA225(1974)1比较；不能将同row重复τ自动当两个独立B数|
|130Ba2+→0+|357keV；未列τ，B.24±.08|Ref7 Towsley/Cook/Cline/Horoshko,JPSJSuppl34(1973)442；131La邻coreinput|
|132Ce2+→0+|325keV，68±10ps，.32±.05|Ref4；131La邻coreinput|
|106,108Cdcoregroup|原表633keV，B.082±.006，未列τ|Ref5 HäusserPLB52(1974)329；groupentry，不给两个核各造同一精确γ|
|107Cd15/2−→11/2−|515keV，23.5±1.5ps，B.095±.006|同Ref5转引对照，不是本文新Cd采集|

原文称130Ce present/Ref4τ“excellentagreement”，本文唯一有其它τmeasurement可比较的本次对象；该比较确有价值，但Ref4原件未在本轮独立读取，也不从相容中心值推全套RDresponse无偏。La与本次130Ce是不同reactionevents，却共用实验方法/装置标度并进入corecalibration；两者不可叫相同eventvector，也不当完全无共同systematics。

## 真正可做的原表算术，而非补 BR/ICC

`source-central-crosscheck.json`只使用已印数。标准近似E2单位式可写成

\[
B(E2)[e^2b^2]\simeq\frac{0.0816\,q_\gamma}{E_\gamma[\mathrm{MeV}]^5\,\tau[\mathrm{ps}]},
\qquad q_\gamma=\frac{b_{\rm total}}{1+\alpha_{\rm IC}}
\]

（选定pureE2transition，τ用mean-life convention）。这只是一般辐射率关系；**不是本文交付的actualconversionproducer**。若人为取qγ1，四条B中央依次约`.44564,.38788,.34644,.32706`，而原表`.42,.38,.34,.33`；反算所需组合qγ约`.94246,.97967,.98140,1.00899`。这些是**条件一致性诊断**，不能当测得的BR/ICC、不能假设b1再报α；最后central略>1在所印精度/误差/近似常数下不支持程序错或物理违例。本文未给实际采用的α/b，故精确conversion链保持open，不从差额创造系统误差。

129La邻evenB无权中央均值`(.33+.33)/2=.33`；131La为`(.24+.32)/2=.28`，解释PartII Table5两个normalizer的中央来源。误差不是本轮naive独立quadrature认证，原引用与当前coremeasurement的jointCov没有交；PartII的.05/.07误差不能据这四个单误差自行推定。PrimaryTable1 weak131La15/2行实际写`.30`，不因centralaverage.28就静默改该模型预测。

107Cd实际中央ratio `.095/.082=1.15854`、triax`.096/.082=1.17073`、axial`.12/.082=1.46341`，可复核正文所引`1.16±.11 /1.17 /1.46`尺度，非重拟Cd或把quoted±.11当本轮传播结果。La的higher/first实验中央`.38/.42=.90476`、`.33/.34=.97059`；printedtriaxmodel为`1.13514/1.15625`，保实际中央差异，不在缺Cov/完整feedingbudget下算排除σ。

## core normalizer、参数和真正的 held-out 结构

Table1脚注给129La尺度数**6.8**、131La**6.4**，由coreB(E2)导出；λF`(e1+e2)/2`由h11/2Nilssonlevels估计，Δ1MeV由odd-evenmassdifferences。γ22°/23°不是直接由Laτ独立测出：PDF3说来自130Ba2+/2+′/4+的energyratios及更重Ba系统学[2]。Thus odd-A寿命是不同观测类型的模型检验，但模型绝对尺度和γ有外部实验定标；不能把coreinput再计一次预测成功，不能以同作者PartII/PRL模型再加两张独立理论票。

**原印参数字典有不一致**：PDF2 Table1脚注实际排成`β/A^(2/3)=6.8,6.4,4.0`；PDF3 Fig2caption及PDF4正文却写`βA^(2/3)`，并给其范围4–7。已视觉核两处，不照OCR静默纠正除号，也不采用literaldivision造β输入；与PartI/PartII本模型b乘积字典比较前应标这项排印边界。它不妨碍原表B/τ读取，却限制从该脚注直接复制actual参数。

Fig2纵轴是`B(E2)/[(5/(16π))Q0²]`，不是直接e²b²；Q0按caption以Z/β/A尺度定义。曲线的normalized值对b4–7、e1≤λF≤e2范围约5%稳定是作者**该模型参数敏感性**声明，不是实验overall5%uncertainty或普适模型精度。primaryTable1模型数值没有±.02errorbars，PartII后来Table5的theory±.02来自其γuncertainty处方，不能写成primary已给fulltheoryCI。

实验的fourLaB在此用于测试triaxialmodel，不能再拿相同B作为另一后续“未用EMholdout”；后续23/2→19/2或27/2→23/2的不同γ响应曲线则是本模型**预测**，不是本文新测这些B。Fig1有23/2→19/2decaycurve用于feeding约束，不表示其lifetime/B已作为独立reportedresult；Table1只报15/2/19/2。

## 源内物理图像、模型比较与反证范围

PDF3在轴合同下解释11/2、15/2、19/2的I偏向**intrinsic2-axis**，以增core–particleoverlap；该2轴在γ60°为oblateaxis，3轴在γ0为prolateaxis。classicalapprox为

\[
B(E2)_{\rm class}\simeq\frac5{16\pi}[Q^{(2)}_{22}]^2,
\quad Q^{(2)}_{22}=Q_0\sin(\gamma-60^\circ)/\sqrt2.
\]

随着γ→60，该轴周围趋对称使此分量趋0；15/2/19/2exactcurve在γ10–35°接近classical。γ>35°附近rotation-aligned15/2与11/2[505]Nilssonband的15/2发生crossing，解释35–45°B的oscillation；这是**随模型参数γ扫描的levelcrossing**，不是La实测随spin发生某一bandcrossing。I>19/2时core惯量偏好的1轴占优，higherE2可峰在γ30°。不把这些axis labels变为现代chirality/wobbling模式判门或γrigidity测量。

作者称triaxial值接近实验、weakfirst值系统偏低；对higher/first，**缺core4+→2+精确实验**使更全面weakcoupling比较困难。只有再假设simple rotationalcore/vibrationalcore才给约1.4/2.0，与实验近1比不合。不能把这两条额外core假设的失败扩成所有weakcoupling或所有softcore理论被排除。strongcouplingK1/2/K11/2、axialaligned、triaxialaligned为Table1所列特定模型，不是模型全集的formalcomparison。

作者对Laγ值和unfavoredstates的总体判断是**triaxialmodelinterpretation**，不是直接成像或测得γ分布。sameMeyer参与experimentalprimary与后来的PartII说明理论/数据谱系相连，**不取消本RD实验的新信息**，但其重复表格、同normalizer或sameprediction不可叠为independentvotes。La129/131新测τ也不能移给Ce133或替其同母态clock/branch。

## 原子 claim ledger

| ID | 单一陈述 | kind / locator | 边界 |
|---|---|---|---|
|BU75-001|本文新测La129/131母态15/2/19/2τ|direct-derived-experiment /1–2,Table1|RDresponse推断，非rawtime直接读数|
|002|三反应/不同beam/target及0°planarGe|direct-setup /1|sameapparatus不等sameeventvector；Ni不是已给stopper|
|003|131La14%longdistance stopped由sidefeeding修正|direct-analysis-assumption /1–2 Fig1|非全核/全线普适fraction|
|004|平均v经finiteGe solidangle校正，vspread显式检查|direct-calibration /2|只属该实验稳定性声明|
|005|同时fit两curve，上馈≥2freeτlevels及commonorigin约束|direct-fit-contract /2–3|τ/feeding/zero有相关性，非independent单指数|
|006|四Laτ/B及误差原值与PartII转引匹配|direct-table /2|B无逐branchICCconversionmanifest，不宣称复现|
|007|本文130Ceτ211±9对先前225±19|new-core-measurement-plus-reference /2–3|core用作calibration；未新读Ref4body|
|008|adjacentcoreBcentralaverage给.33/.28|task-source-arithmetic /2|不补Cov/误差，不改weakmodel.30|
|009|β尺度来自coreB、λ从Nilsson、Δ从mass|model-calibration /2footnotes|非WK22actualinput/全freeprediction|
|010|γ22/23从evenenergies/systematics|model-calibration /3|不是独立Laτ测γprofile|
|011|β/A^(2/3)脚注与βA^(2/3)图注不一致|literal-source-dictionary /2–4|不静默复制参数或指控整体计算错|
|012|Table1theory无errorbars，Fig2约5%限归一模型范围|literal-error-scope /2–4|不是experiment5%或fulltheoryCI|
|013|E2formula反算q只条件一致性|task-source-central-check /2+standardradiationformula|非测BR/ICC/新CI；q≈1偏差不认证错误|
|014|weakhigher比1.4/2须额外coremodel，actualcore4→2欠精确|explicit-author-limit /3|不排所有weak/softmodels|
|015|Fig2>35°crossing是γparameterscan|model-output /3 Fig2|非实验bandidentity/crossingω|
|016|higherBcurve预测未测；23→19curve已用于feeding|prediction-vs-calibration /1–3|不把feedingcurve当新reportedBholdout|
|017|107Cdratio引用值可由表central复得|source-reference-plus-arithmetic /2,4|不是本文新Cdmeasurement|
|018|PartII重复Table5与本文同数据/理论链|source-dependency /2,4refs+PartIITable5|保实验价值、不重复计票|

每条建议needs_review:true、source-self-audited，非human-reviewed。全文本、全部visual和原表算术足以支持这些限域claims；没有新modelproducer、rawdatafit或统计测试。

## 未解与停止

本单元4页完整阅读已达停止条件。实际未交逐branchBR/ICC、plungerstopper/zero完整响应、原counts/feedingfit/Cov、归一core引用的具体误差依赖与β脚注字典修订；未独立读Refs3–7的全文，本文不构成那些来源已核。它关闭PartII Table5的primaryτ与RD/feeding/calibration来源，不能关闭Ce133自身τ/BR/582reference或actual2022input，更不给手征/进动/静态三轴一量判门。
