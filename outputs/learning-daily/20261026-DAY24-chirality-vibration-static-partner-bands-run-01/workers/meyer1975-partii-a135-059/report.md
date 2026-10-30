# 059：PartII 的 A≈135 实验比较、133Ce 节点与模型反例

**本分区physicalPDF14–19 / printed154–159已逐页文字精读，并视觉核Tables4–5、Figs7–9及正文。** `primed-recall.md`在本轮assignedbody前写，明确057已读14/16/18/19等预暴露，非盲测。本文原件25页，直接body`tmp/day24-meyer1975-partii-entry-057/attachment-object-response.pdf`，1368683B，SHA256`fd1ba7f9280e8bafd86bbec06ec18e8a7089f93e84306829a4be897d9dd8439d`，本轮重核匹配。不是本agent独立全25页读完，也不是作者数值复现。

本篇J.Meyer-ter-Vehn1975,*NPA249*141–165,DOI10.1016/0375-9474(75)90096-2，WK22 Ref52；PartI另Ref51。新增fact应由父任务写回knowledge，本worker不修改canonical/raw/Git/course/session，无网络/producer/旧114或subagent。单纯实际印数算术见`source-central-crosscheck.json`，不是新toy。

## 新增最小结论

- 133Ce Fig9确是低lying νh11/2 single-j hole-family历史比较，N75的135Nd/133Ce/131Ba只在§3.2.4作谱相似性并列；本分区没有为135Nd/131Ba各画完整nodes或给它们逐核EM数值。它不是现代3qp手征同组态或partner-resolvedEM证据。
- Fig9三列都以自己的11/2态为0；**实验9/2是−170keV，三轴模型+18、轴对称+37**。三轴例β.22/γ23°，轴对称β.19/γ0°，同tildeλF1.0/Δ1MeV；比较并非仅改变γ。最低9/2排序/能量偏差未闭合，作者没有采用adhocCoriolisattenuation。
- 实验谱与模型谱的某些近合不等已识别每个modelstate：135Pr branching不够逐态认同；137Nd额外negativeparity组在h11/2模型中的branching不符，作者提出f7/2/可能h9/2替代；这些反例不能删。
- Table5为转引Ref29的129/131La B(E2)，本模型电四极尺度由adjacenteven B(E2)定标，理论±.02仅γ不确定度，非完整模型误差。实验的两个favoredbranch强度比稍小于1，而所印三轴中央比约1.14/1.16；保近似支持和真实中央差异，不作缺Cov的显著性。

## 实际逐页/图表范围

| physical / printed | 本轮实际读取与视觉核 |
|---|---|
|14/154|187Ir(h11/2)尾段反例、§3.2开头、Table4全部12rows/headers/缺字段；原印`N>82`与表N74–78相冲突，视觉确认为原页字样，不替原文改字|
|15/155|A135 softness/prolate叙述、Fig7全部experiment/两modelcolumns与caption|
|16/156|证据核素清单、135Pr comparison与branching限制、129/131La E2判据定义与实验来源|
|17/157|Table5所有数值/脚注、higher-transition未验证预期、137Nd comparison至跨页|
|18/158|Fig8完整、额外137Ndlevels/branching失败、§3.2.4 133Ce及Coriolis偏差|
|19/159|Fig9完整及4500px crop、core-inertiaopenquestion、§4第一段“rigidshape不应literal”限制|

必要定义定向回看PartII **PDF7 Fig2caption**、**PDF8 Fig3caption**（仅caption文字，非额外整页科学认证）：能量相对basicstate，Q/μ为calculatedbasicstate moments；Fig3线型强度为理论B(E2)/B(M1)加已知experimentalEγ算rate。Fig8明确沿用这些定义；不把Q1.5eb/μ−.9n.m.或箭头当直接测量。另定向原读WK22PDF66–67 Tables5.1–5.2供低node/edgecrosswalk，不重读全文；引用实验Refs21–32等未独立新读。

## Table4：邻偶核标度、缺字段与原文不一致

Table4 caption指Ref13。以下为原表所印energies(keV)与**derived**β、γ(Δγ)、`βA^(2/3)`，不是本文新测或各odd核directshape。空格保空，不拿相邻γ补填：

| even core | E2₁ | E4₁ | E2₂ | β | γ(Δγ)° | βA^(2/3) |
|---|---:|---:|---:|---:|---:|---:|
|128Xe|443|1033|970|.213|23(3)|5.4|
|130Xe|536|1204|1122|.190|23(4)|4.9|
|132Xe|668|1440|1298|.169|24(6)|4.4|
|130Ba|357|902|908|.231|22(2)|5.9|
|132Ba|465|1128|1032|.203|24(3)|5.3|
|134Ba|605|1401|1168|.177|25(5)|4.6|
|132Ce|325|858|—|.240|—|6.2|
|134Ce|409|1049|966|.210|23(2)|5.5|
|136Ce|553|1316|1093|.182|25(5)|4.8|
|134Nd|294|789|—|.256|—|6.7|
|136Nd|374|974|—|.223|—|5.9|
|138Nd|521|1250|1014|.185|26(4)|4.9|

PDF14开头实际印“Z>50 and N>82”，但Table4各row为N74/76/78，PDF19§4又说50<Z,N<82；这是源内部适用区文字不一致。本任务保留而不将其错误范围当后续核素筛选。PDF15作者自己承认even-A spacings服从rigidtriaxialrotor较A190差，可能因更大β/γsoftness；γ约20–30°较恒定与β随质量变是模型提取/解释，不能当γ刚性测量。排除oblate的作者论证还引evenBa quadrupolemomentsRef21，本轮未独立核该实验。

## 模型参数与实验谱系：逐核不能用邻核标签补齐

| 对象 | 本分区实验来源/能级族 | 本分区实际模型与限制 |
|---|---|---|
|135Pr|Ref25，兼high/lowspin、负宇称h11/2protonfamily；Fig7 basic11/2位于absolute358keV，图中记0(+358)|triaxβ.21/γ23° vsaxialβ.18/γ0°，tildeλF.6/Δ1MeV。7/2、9/2、11/2第二/第三态群位置更支持三轴，但branching不足逐个identify；不把nearbyenergy当对应态已核|
|129/131La|Ref29的favored15/2→11/2、19/2→15/2寿命导出B(E2)转引；能谱另多源|Table5 b6.8/6.4、γ22±2/23±2°、tildeλF.5、Δ1MeV。b来自adjacentevenB(E2)均值；与Table4energyderived b不是同一输入，不静默替换|
|137Nd|Refs26heavyion+28βdecay合并negativeparity谱；basic11/2图记0(+520)|Fig8 h11/2hole，β.20/γ26°、tildeλF.60、Δ1MeV；γ标准值来自138Nd。Q1.5eb/μ−.9n.m.为模型basicstate值。extra组难认，保f7/2/可能h9/2替代|
|133Ce|Ref26；Fig9 lownegativeparityfamily，见下nodes|β.22/γ23° vsβ.19/γ0°，tildeλF1/Δ1MeV；9/2仍偏高，未加Coriolisattenuation；未给133CeabsoluteB/M1/δ表|
|135Nd|Ref26的h11/2neutronhole yrastfamilies；并在135Prβfeeding中出现9/2−parent|与133Ce/131Ba“almostidenticalnegativeparityspectra”为作者系统学描述；本分区无135Nd独立node/参数/EM表，不从137Nd代填|
|131Ba|Ref27所引h11/2neutronholeyrastfamily/N75比较|没有独立画图或逐态EM表，不能把133Ce模型参数或129/131La寿命挪给它|

Ref26为J.Gizon,A.Gizon,M.R.Maier,R.M.Diamond,F.S.Stephens,*NPA222*(1974)557；同一个源被用于Nd与Ce多个核，转引页不等多个完全独立实验campaign。Ref27为Gizon/Gizon/Horen,Nashville1974conferencevol1p154；Ref28为NowickiKFK2017(1974)；Ref29为Butler,Meyer-ter-Vehn,Ward,Bertschat,Colombani,Diamond,Stephens,*PLB56*(1975)453。这些书目来自057已读PDF25refs，本轮没有取得其reaction/run/response/Cov或后续修订，故**实验谱系与依赖可定位，campaign独立性尚未认证**。PartII是模型比较文，不能把它再投一份独立实验票。

PDF16 particle/hole类比文字给Auγ约37°、La/Prγ约23°，并两处实际都印λF>εh11/2；本分区不从这段自动补signedλ或修不等号。PartI的完整duality和零点合同另存canonical，当前tildeλ并非可直接与WK22 MeVλ比较的actualinput。

## Fig9 133Ce：三列、节点与最低9/2反证

三列分别按basic11/2重置0。下表experimentrelative与triaxmodel为原图印数；rightaxialcolumn没有重复spin标签，对应值按连线读，不再当额外experimentallevels。顶部2454旁spinglyph扫描残损似23/2或22/2，本任务保`needs_review`，不凭odd-A数学预期自动改印字：

| historical node | experiment relative keV | triax model keV | axial connected value keV | triax−experiment |
|---|---:|---:|---:|---:|
|9/2−|−170|18|37|+188|
|11/2−|0|0|0|0(anchor)|
|13/2−|385|351|323|−34|
|favored15/2−|620|628|741|+8|
|17/2−|1136|1153|1356|+17|
|19/2−|1380|1420|1900|+40|
|21/2−|2027|2228|2847|+201|
|experimental23/2− / modeltopglyphuncertain|2336|2454|3434|+118(仅数值，不认证glyph)|

另有experimentdashed994线、左侧另注1164但未在本caption解释，其连线往triaxunfavored15/2−1103/axial1868；向下箭头到13/2385。**不把左注1164直接当9/2reference的absoluteEx已证**，也不把994线的spin/branching按model标签反填experiment。图内只少量arrow不是完整branching/transitiondata。

最低9/2的反证是levelordering：experiment相对11/2低170，model反而高18/37。作者明说Fermienergypenetration可下拉但不够，I<j的Coriolisdistortedbands惯常用adhocattenuation，此处因要保模型物理图像没有使用；Ring/Mangselfconsistentcoreinertia解释怎样纳入三轴rotor仍open。本图真实支持三轴例对部分谱的改善，同时保最低态失败，不能称全谱拟合精确或模型已解决该基态。

## 与 WK22/A13 低family的有限 crosswalk

这一步只作source印数的带头/零点及实际边候选：取WK22 **11/2−207.4keV**为offsetanchor `S=207.4`，将Fig9实验relative加S。它不校正历史能量，不把现代Ex变为旧图直接测量。WK22PDF66 Table5.1当前原读，9/2modern37.2为207.4−170.2或592.1−554.9的**派生**decimal，不是新独立能级表行。

| Jπ | historical+S | WK22 node | difference keV | 可用状态 |
|---|---:|---:|---:|---|
|9/2−|37.4|37.2 derived|+.2|带头近合；不写精确identity|
|11/2−|207.4|207.4|0|人工anchor，不计独立support|
|13/2−|592.4|592.1|+.3|lowfamilycandidate|
|15/2−|827.4|827.1|+.3|lowfamilycandidate|
|17/2−|1343.4|1344.7|−1.3|保差值；不称同精度相等|
|19/2−|1587.4|1590.3|−2.9|保差值，需oldprimary/calibration/version|
|21/2−|2234.4|2201.1|+33.3|大差，不自动merge|
|23/2−|2543.4|2486.6|+56.8|大差，不自动merge|

逐边而非只spin：old385−0=385，对WK384.7；620−385=235，对WK235.0；620−0=620，对WK619.7，支持最低family候选。随后1136−620=516对WK517.6、1136−385=751对WK752.6；1380−1136=244对WK245.6，不消除差值。高spinold2027−1380=647对WK610.8、2336−2027=309对WK285.5，不能靠一个offset修复；不能因此单方面改任何旧或新实验。

old994→385的arrow给609keV；加S的1201.4节点靠WK22Table5.2的1200.8，且后者有实际608.7→592.1边。这可保存为**单node/edgeprovisionalcandidate**，但old994实验线无清晰独立Jπ标注且没有WK22的832.0head，不认证wholeBand4身份/原文已见整条newband，更不移任何δ/强度。A13低negativeBand4与WK22Band1已有canonicalfamilycrosswalk可引用，不在本任务重做；其Gammasphere采集和1974Ref26实际事件是否独立仍需各sourceexperiment，不能按年份分票。

## E2、M1、δ：Table5可读强度，不能代 Ce 实验

Table5全表 `B(E2)↓ [e²b²]`：

| transition / quantity |129La experiment|triax theory|axial theory|131La experiment|triax theory|axial theory|
|---|---:|---:|---:|---:|---:|---:|
|15/2−→11/2−|.42±.02 (269keV)|.37±.02|.50|.34±.02 (336keV)|.32±.02|.45|
|19/2−→15/2−|.38±.06 (475keV)|.42±.02|.52|.33±.03 (533keV)|.37±.02|.47|
|adjacenteven average2+→0+|.33±.05|calibration|—|.28±.07|calibration|—|

脚注：129La用`b=βA^(2/3)=6.8,γ22±2°,tildeλF.5,Δ1MeV`；131La用`b6.4,γ23±2°,tildeλF.5,Δ1MeV`。b由adjacentevencoreB(E2)average确定；**表的theoreticalerrors仅dueγexpuncertainty**，不是包含b/λ/Δ/模型缺项/实验共同systematic的fullerrorband。不能把coreaverage既作calibration又当独立预测成功；odd-A寿命可提供不同观测，但共享response/Cov未交，不称完全统计独立。

PDF16 ratio `R=B(E2;(j+2)→j)/B(E2;2+→0+)_av`随γ的模型例约1.5(0°)、1.2(20°)、.9(25°)，另略依b/λ；Table5中央实验R为129La1.2727、131La1.2143，符合作者“around1.2”的量级而非用它反演唯一γ。中央higher/first实验比.38/.42=.90476与.33/.34=.97059；所印triaxmodel比.42/.37=1.13514和.37/.32=1.15625。原文说“veryclose”/支持triaxial并称weakcouplingrigidcore约1.4、harmoniccore2.0较差；本任务保中央比不完全同trend，**不在缺相关误差下给排除σ或模型likelihood**。所谓γ22°“确认至约±3°”是该模型/该calibration与所引实验的作者解释，不是现代γ-distribution宽度。

next23/2→19/2相对19/2→15/2的ratio在γ>20°快速升、30–40°可>2是**未验证模型预测**，PDF17明确openquestion；不能给Ce或La填一个已测高spinB。135Pr作者不报告不足以认态的branching数值；137Nd有理论78%branching反例，Fig8箭头由theoreticalB(E2)/B(M1)+knownexperimentalEγ造intensity，不是fullyholdoutEMprediction。**本分区没有133Ce/135Nd/131Ba的absoluteB(M1)、signedδ、τ数值或matchedpartnerEMvector**；Fig8 Q/μ更非本核新测moment。

## 137Nd与135Pr的反证与真实支持并存

135Pr Fig7实验11/2basic0(+358)、7/2~185、15/2~373、9/2~441、13/2~593、19/2~1033，以及827/856/931等tentativeJ群；threecolumn参数如前。作者以γ23°model有合适第二/第三7/2/9/2/11/2群、γ0°过高支持shapeasymmetry，但branching不够逐个identify。某些额外model低spin态未在βfeeding中populated的解释依135Nd9/2−parent/logft<7，不是实验已排除这些态或source给了完整EMmatrix。135Pr历史图不映射现代wobblingbandnames。

137Nd Fig8实验mainfamily11/20(+520)，9/2457、13/2580、15/2669、17/21375、19/21552、21/22300、23/22561；对应model主支约0/428/533/740/1373/1735/2653/2921，能量差非处处很小。作者标准γ26°来自138Nd，13/2与15/2closegap偏向稍更大γ。额外855relative（文中absolute1374）若认model7/2，应78%强衰basic11/2而非主要向9/2；另认5/2又能量不符；1380relative（absolute1899）组的next-neighborbranching也与h11/2model候选的preferredbands不合。作者因此说notlikelyh11/2、可能f7/2/再h9/2，需moredata。**11/2basic图0(+520)与855+520=1375而文字1374相差1keV**也保历史打印/rounding，不静默统一绝对能量。

PDF14的187Ir尾段给独立模型限制：experimentalyraststaggering在参数容差内不能获得；7/2band相对11/2偏高与15/2yrast偏低，改善两点需γ朝相反方向，即便各在±2°内也不能同一个γ同时修复。作者推Ptcore可能更γsoft。接PDF19§4开头承认rigidshape不应literal、存在softfluctuations证据；后续完整PESdiscussion另由父任务分区读，不把本例fit说成γrigid实测。

## 原子 claim ledger

`claim_kind`与`needs_review`对本单元自审，不设置human-reviewed；全部实验事实为本模型文转引，除明确标任务算术外不当新测。

| ID | 原子陈述 | kind / locator | evidence/反证与边界 |
|---|---|---|---|
|P2A135-001|PDF14实印N>82，而Table4为N74–78、PDF19写50<Z,N<82|literal-source-inconsistency /14,19|保原字，不改核素或先验范围|
|002|Table4部分Ce/Nd E2₂/γ缺失|literal-derived-parameter-table /14 Table4|不靠相邻γ补值；β/γ非directshape|
|003|135Nd/133Ce/131Ba为N75 h11/2holefamily系统学比较|author-systematics /16,18|只Ce画Fig9，非现代3qp/partneridentity|
|004|Fig9三列11/2各归0，exp9/2−170、triax18、axial37|direct-figure-literal /19 Fig9|最低9/2ordering不合，triax残差188|
|005|Fig9 β.22γ23对β.19γ0，同tildeλ1/Δ1|model-input /19 Fig9|非γ单参数holdout，非WKactual卡|
|006|Ce最低9/2仍过高、未作Coriolisattenuation|explicit-model-failure /18–19|三轴图部分改善不消该反证|
|007|lowCe节点offset207.4后近合但高spin差33.3/56.8|task-source-number-crosswalk /19+WK22PDF66|人工anchor不计验证；逐edge/历史版本需primary|
|008|old994→385边609与WK608.7成单node/edge候选|provisional-source-crosswalk /19+WK22PDF67|oldJ未清、832head缺，非wholeBand4identity|
|009|Table5实验B来自Ref29；b由evenB平均定标|calibration-data-dependency /16–17 Table5|coreinput不又作independentholdout；rawCov未得|
|010|Table5理论±.02只含γ不确定度|literal-error-scope /17 caption|非fullmodelCI或设施精度|
|011|Lahigher/first实验<1、printedtriaxtheory>1|task-central-ratio /17 Table5|保真实中央差；无Cov不报排除|
|012|La23/2higherE2的>2比值是openprediction|unobserved-model-prediction /17|不给Ce新absoluteB|
|013|135Prbranching不足逐态recognition|explicit-identity-limit /16 Fig7|nearenergy支持asymmetry不认证one-to-one|
|014|137Ndextra组h11/2branching失败，提出f7/2/h9/2|model-alternative /17–18 Fig8|未读新primary，不自动更新assignment|
|015|Fig8Q/μ是计算、modelintensity用已知Eγ|operator-observable-provenance /18 caption+PDF7/8caption定义|不是newmoment/M1/δmeasurement或fullyindependentprediction|
|016|sameRef26多核转引与sameRef29多量不等独立experimentvotes|source-lineage /16–18+refslocator25|campaign/response独立性unknown|
|017|187Ir两个偏差需要相反γ修正|explicit-counterexample /14|不以单γ±2°叙事掩盖失败|
|018|rigidshape不应literal，softness仍应讨论|author-validity-boundary /15,19|不能fitenergy→measuredrigidity|

每项推荐claim `needs_review:true`（source-self-audited，不是humanreview）。关键模型数值/节点/ratio均可在原图表与JSON重算；不生成测试/玩具以追求delta。

## 未解与停止

本分区已完整可复核。未解的是Fig9最高modelspin残损字、994旁1164注义、historicalRef26/27primary的完整节点/反应/后续更新、1380/855绝对零点1keV打印差、跨campaign/derivedB共同Cov及现代Ce实际signedEM/input。可以确定旧Fig9最低family有方法比较价值，不能在这些缺口前合并全highspinband/修历史源或填2022λ/Δ/producer。父任务其它分区完成后才宣告PartII全篇；本任务不打开新课。
