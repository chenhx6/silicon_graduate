# 052：130Ce 的 Nolan1983 原实验使 BR85 的离散谱/连续谱比较可以分层

**新原件全文与全部图已读，非旧source重复或no-op。** 本单元完成Crossref精确身份、库内重叠搜索、授权publisher API获取、完整5页/hash/首末核、PDF1–5全文和Figs1–4及唯一未编号displayed relation视觉审核。保持同一Day24；不授分、不改canonical/raw/Git/course/session、不运行producer/旧114。

## 身份、资源与覆盖

BR85 Ref63精确对应P.J.Nolan, R.Aryaeinejad, A.H.Nelson, D.J.G.Love, D.M.Todd, P.J.Twin, **“The moment of inertia of 130Ce above spin 30ℏ”**, *Physics Letters B*128(5)(1983)285–289，DOI`10.1016/0370-2693(83)90261-7`，PII0370269383902617。Crossref search后exact DOI endpoint200，六作者/题名/刊物卷页匹配；PDF刊头日期1September1983，received2March1983不混作出版日期。

Wiki定向检索未见该原件source或已读receipt；现有Nolan1979 lifetime review、BR85引用层、其它Ce寿命source均非本实验原件。raw文件名/文本Bib索引没有找到相同body，故不是已核全文后的重复下载。本轮没有递归扫描所有PDF正文；阴性搜索限已述范围。

本地body：`tmp/day24-nolan1983-ce130-companion-052/attachment-object-response.pdf`，**5页、307863B、SHA256`9085414a3cf1daafdeb3e7b685ea9bc6fdbfa44ee91f2e484c5eda353af6f927`**。%PDF/pdfinfo有效，首physicalPDF1 printed285和末PDF5 printed289均视觉核，页数与285–289含首尾匹配，不是首页预览。

获取沿合法已配置Elsevier API：FULL XML→实际`1-s2.0-0370269383902617-main.pdf` EID→标准Object API，两次HTTP200，没有失败重撞、OA/browserfallback或猜PDF URL。FULL XML53912B，SHA`f1077f0fa0869489fe500b69d4a1b0c1f385aa6d34208a3fe39eb74b8380e161`。helper以`--si`执行；publisherCredentials仅私有配置读取/headers传送，不输出或改凭据。XML附带si1–si4.gif经metadata核为`ALTIMG`、`abstract-attachment=true`、13–14pixel高的inline图，**不是仅凭si字样当补充资料**；inventory未识别真实SI。不宣称所有publisher入口绝无SI。所有下载仅tmp，未摄入raw。

另将BR85 Ref77分开核到**“Electromagnetic Transitions in 130Ce”**, *Physica Scripta*T5(1983)153–156，DOI`10.1088/0031-8949/1983/t5/028`。Crossref exact200，作者名单比Ref63更长（含P.J.Smith、Garrett/Hagemann/Herskind），**本轮只有metadata，未取得/读Ref77正文**。本primary Ref4仅列Nolan et al. NordicConference/Phys.Scr.(1983),tobepublished，与其相容，但还不能认证两文每个run/计数重叠程度。不能把它们同作者/同核当独立campaign或同一份数据已证。

## 实验记录与selection依赖：不是两个独立campaign的52/45测量

PDF1/printed285直接报告本次`100Mo(34S,4n)130Ce`，Daresbury Tandem150MeV34S；三层97.3%enriched100Mo thinfoils，总约1.5mg/cm²、对beam约15MeV能损。TESSA1含5个escape-suppressed Ge spectrometers(ESS)，7个BGO sum-energy/multiplicitydetectors、约50%4π立体角。**>50million events**每个含ESSγγ coincidence加sumenergy/multiplicity。给出的662/1332keV处63%/52%是**photopeak/total ratio**，不是absolute fullenergyefficiency；≤1350keV的photopeak-photopeak eventfraction>25%。这些响应信息不恢复完整efficiencycurve、angularresponse、background或rawcounts。

| 对象 | 直接selection/处理 | 与其它对象的依赖 |
|---|---|---|
|Fig1a yrast谱|5ESS加和，至少5BGO；与16+至22+ yrasttransitions符合；.5keV/channel|同本campaign；bandgate影响feeding集合，不是species-completeunbiasedsample|
|Fig1b isomer谱|同BGO条件；与isomer14−至20−若干transitions符合；.5keV/channel|同campaign但不同gates，不是第二独立实验|
|Fig1c/d bumps|分别将a/b压到1000channels、2keV/channel|同一谱重bin，不能把compressedbump作为新增独立证据|
|Figs2–3 correlationcuts|同presentdata，γγ且≥5BGO；512×512matrix、4keV/channel；沿gradient−1穿valleycuts；Fig2每100keV平均，Fig3区宽另列|未说明也用了Fig1特定bandgates；**不能把rawcorrelation自动归属同一条resolvedband**。cuts互相共享matrix，非独立campaign|
|Fig4 currentdiscrete点|yrast/isomer的discretetransitions用`Jband2=ΔI/Δω`|仍同本campaign与levelassignment；两band不是独立instrumentcalibration|
|Fig4 currentvalley点|presentcorrelationvalleywidth反演，附estimateduncertainty|与上述rawmatrix同源；高ω不是逐线resolvedbandextension|
|Fig4外部NaI点|Ref10 Bialkowski1981 `124Te(12C,6n)130Ce`、NaI(Tl)γγcorrelation|**不同反应/既有实验**；原件未本轮读，只能称本primary转述generallyagree，不恢复共同Cov|
|更早isomer20−|本primary引Ref4的`117Sn+16O`数据|另一反应的既有来源；不是当前MoS事件。Ref77可能相关但body未核，保持分开|

PDF4/288以discreteproducts估计：≥5BGO selection下`129Ce+129La`合计约20%，其它产品更小。作者结论是structures **most likely**为130Ce，但其它可能性不能完全排除；不能把≥5BGO门误写成纯130Ce鉴别。这个污染估计也非每个Eγcut逐点20%背景可直接相减。

PDF3/287作者因photopeak-photopeakratio较高、rawdata里旋转特征清楚，**没有减uncorrelatedbackground**。这不是background等于0、实验不存在systematic或已做完整responseunfolding；本轮没有rawmatrix/脚本/逐cutwidth/Cov，不报告新的confidenceinterval或复现实验惯量。

## 离散谱最高spin：原文有明确assignment边界

PDF1–2/285–286新yrastlines`1242,1285,1311,1327keV`互相及所有lowerbandmembers符合。90°相对forward/backward强度与ΔJ2相容；1242明确assign为26+衰变。**其它三条顺序难定**，三线集中40keV内提示backbend/upbend起始；其它>850keV新线还不能放入scheme。按ΔJ2连续延伸可作到32+的最高spin账，但本文没有给这三线各自28/30/32的唯一拓扑/不确定度；不要把BR85摘要式“resolved32+”升级成原件逐线order已核。

isomerband以Jπ7−为基，先前117Sn+16O达20−，本次明确写延至**28−或possibly30−**（1322keVline）。28−及以下的coincidences/intensities，尤其所有ΔJ1decays提供assignment支持；30−并非同等级确定。PDF2说isomerabove-yrastenergy在J20为630keV、J28为190keV，这是same-I跨**相反parity**带能量接近，不能作sameparitychiralpartner或不同形状直接证明。

Fig1实际显示lowertransition标签和高线支持，未附完整能级表/全部angularratios/uncertainties；本轮不从图恢复缺失误差、绝对B、τ或未经原文定位的全部levelenergies。

## 连续谱量精确为 Jband^(2)，不是Jeff E2总计数

PDF3/287直接displayedrelation：

\[
W=\frac{8\hbar^2}{\mathcal J^{(2)}_{\rm band}},
\qquad \mathcal J^{(2)}_{\rm band}=\Delta I/\Delta\omega
\quad\text{（后式PDF4为discrete extraction）}.
\]

W是图上valleywidth，`Eγ1−Eγ2`坐标与cuts定义须保，不能随便改成perpendicular几何长度再沿用同一8因子。本文明写`Jband2`，由γγcorrelation相邻transition间隔相关性反演；**不是**BR85§6.2按全部E2数目给的Jeff2。BR85若在回述中宽称continuumeffective，应补这个primary对象，不能把52搬成另一Jeff定义的同数值。

PDF3–4/Figs2–3旋转valley至约Eγ1.6MeV（abstract等价至ℏω.8），fillings在1040–1080、1190–1220、1280–1320keV；它们与compressedbump及约1300三yrastlines覆盖类似Eγ区，是同campaign的关联现象，不是每个cut已识别一对bands。Fig3其余cuts1080–1120、1140–1170、1240–1270、1400–1440keV用于比较；Fig2中心1100/1200/1300/1400/1500，每100keV平均。变窄ridge可能提示band惯量散布小，作者主动说**更多数据才能确认**。

PDF4/Fig4给：(ℏω)²约.4MeV²以下discretevalues，yrast/isomer相互相容；之上presentvalleyvalues约constant **justabove50 ℏ²/MeV**。图中rigidbodyreference **52**对应假设`ε2=.25`，本primary正文没有以精确数字另列“discrete45”。BR85的“continuum52对discrete45”是其比较/概括，不能由本篇构造(52−45)显著性、逐band共同systematic已消除或独立的Δshape测量。Fig4有valleypoint的estimatederrors，但无数表/完整Cov，本文也未给每点 uncertaintyprovenance；本轮不digitize后报精确difference。

原文一处写到(ℏω)²约.4“MeV”，邻句与图轴均MeV²；按平方频率对象保单位，不为该排字处创造物理含义。ℏω≈.6与sqrt(.4)≈.63只是文中近似门，不是普适I阈值或Harris参数。

## 作者解释、替代解释与BR85并排

PDF4模型前提明确：**assumeprolateε2=.25**，Ref11 R.Bengtsson/S.Frauendorf1979 crankedshellmodel，pairinggap1.2MeV。预计νi13/2对在ℏω.6产生约10ℏalignment；νh11/2对在.5约6ℏ；首crossing在.32阻塞其它某些crossings。νh11/2 [5237/2] alignment强pairingdependent，减少pairing使其难见；i13/2的predictedproperties较少依pairing。isomerbasicconfiguration文中为`h11/2⊗g7/2`并称h11/2被block（引Ref4），本轮不补原件未在该句明确的particletype或改成WK22配置。

作者根据yrast/isomergates都有bump、h11/2被block的论证说**consistentwithνi13/2alignment**，不是直接测出i13/2occupation或唯一crossing。替代解释被作者写出：即使无backbend，reactionfeeding经少量statisticaltransitions直接进bands也可造bump；bumpEγ对应J22–28，低于expectedentry36–42而且1.6MeVcorrelation表明别处feeding，这些是作者偏向crossing的支持。**有无backbend仍须全部相关discretetransitions，本次未能观测齐**，不能删除这一原文结论。

原实验作者认为ℏω>.6的constantJband2提示shape没有majorchange（如变spherical或很不同deformation）；“equalrigidbodyvalue”依赖ε2.25reference与响应假设，**不直接证明γrigid、staticshape或实测constantε2**。BR85§8.4则在另一no-pairingCNS模型内比较ε.20–.25trackedbranch与ε.35min，并以52/45推可能moredeformedcascade。两者是不同模型/conditionalinference，均不能替代缺失resolvedhigherbandtransitions。primary没有观测/label一条ε.35band，也没有测τ或给CeHarris输入。

| BR85所用层 | 本primary真正支持 | 应保的额外边界 |
|---|---|---|
|离散32+/30−范围|新yrast三高线支持连续ΔJ2高spinextension；isomer确认至28−，30−possible|yrast高三线order难定；BR85更简写不是primary更强assignment|
|higherω惯量约52|rawcorrelationwidth推Jband2 justabove50，与ε2.25rigidreference52相容|非Jeff计数、非特定resolvedband、20%其它核污染不可全排|
|离散约45对continuum约52|Fig4discrete与valley在不同ω/selection的比较对象可见|primary无literal45表值；同campaign共享counts/instrument，缺Cov不能给显著性|
|crossing/highj解释|bump/valleyfillings+pairing/blockedconfig支持i13/2解释|feedingalternative、有无backbend需尚缺的discretelines|
|moredeformedcascade|不是本primary直接测量结果|BR85模型推断；primary作者反而以constantJ2说无majorchange，两者不合并成实测shape|

## 全部图与响应核对范围

- Fig1 physicalPDF2/printed286：四panel完整视觉核，bandgates、≥5BGO、.5/2keV/channel、lowerlabels与yrast新lines/isomer1322均核；c/d仅重bin。
- Figs2–3 PDF3/287：rawγγ≥5BGO的allcuts、W示意与Eγ1−Eγ2坐标完整核。没有把峰形/valleyfillings写成净backgroundsubtractedcounts。
- Fig4 PDF4/288：yrast×、isomer实点、currentvalley实方块与外部Bialkowski空点区分，currentestimatederrorbars与52reference完整核；未数值digitize。
- PDF5/289 refs全文视觉核。Ref3 priorh11protonbackbend/Ref4formerisomerexperiment/Ref10NaI/Ref11model分别保来源；本轮未独立读它们body。

## 最小写回与真正下一缺口

父任务可将本篇作为BR85 Ref63的primarycompanion新增source，并把三项主增量写回：**Jband2而非Jeff2；MoS同campaign不同selection+products污染边界；28−/possible30−与yrast高线order边界**。再保主文的pairingmodel/feedingalternative、rigidreference而非直接shape测量，避免把BR85的52/45概括当已独立精确差。

Ref77正文仍是具体缺口，可核其117Sn+16O/其他campaign、discreteassignment是否进一步定序与30−、lifetime/EM内容及它与Ref63的数据依赖。需要精确response重放则还缺currentrawmatrix、gates/efficiency/background/widthfit/Cov；这不是向用户索资源的要求，也不以toy补。本文已足以关闭Ref63sourceidentity与本轮primaryquestion，不因未得rawcounts而拒绝原文可支持的结论。

停止原因：原件5页与全部图/关键公式已直接核完，有明确新增证据；没有等待或再询问资源，不重跑旧玩具，不将130Ce的数值/τ/模式标签迁给133Ce。
