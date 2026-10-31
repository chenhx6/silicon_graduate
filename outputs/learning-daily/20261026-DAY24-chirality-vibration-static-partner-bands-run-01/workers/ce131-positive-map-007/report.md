# 131Ce正宇称节点与Li2004寿命family：AW13 Band2 / Band3

本轮为Day24有界原件self-audit，新增判断`needs_review: true`。只写指定worker/tmp；未改canonical、raw、PLAN、Bib、用户review flags、Git、session或课程学分。Band5 Table5.3的高spin两分量`e⊗AEFG`既有人审不重新解释或更改。

## 先校正带号

**AW13 Band1是负宇称νh11/2；g7/2正宇称是AW13 Band2。** 原派发的“Band1/g7/2”经回原文发现错配，root已确认以原论文编号为准，未写入canonical。证据：PDF58/printed54 §4.3.1 Band1；PDF82/printed78 §5.2.1 Band1；PDF86/printed82 §5.2.2 Band2；Tables4.5–4.6(PDF72–73/printed68–69)。因此本轮正序列跨文对接为 **Li正宇称family ↔ AW13 Band2**，AW13 Band3为另一独立的低激发正宇称结构。

AW13 Band3的**1/2+带头Ex=61.8keV**由PDF86/printed82 §5.2.2直接报告，νs1/2[400]1/2+只是作者的possible interpretation。133Ce论文的同号Band3为ground是既有跨核控制；这里不把131Ce的61.8重设0，不搬133Ce的寿命、混合系数或其它输入。

## 原件与实际读取覆盖

- AW13：`raw/theses/degree dissertation/Band structures of 131Ce.pdf`，97页；本轮SHA=`b50c22877418de560f06002588bb46d34f5ba670c6880e30a89d1509c79ad8c1`，匹配source。正文此段PDF页=printed页+4。
- Li04：`raw/papers/2004_Lifetimes of Excited Levels in 131Ce.pdf`，3页；SHA=`100a06fc1bb6d7061a153552529c9245f123248f213a93f022b202af97dcdcc5`，匹配source。PDF2/3对应printed462/463。
- 实际读AW13相关连续主线：PDF55–59的Ch4引言、实验/编号和正负宇称分段；PDF66 Band3/5文字；PDF79–86的§5.1–5.2.2相关解释。定向读Tables4.4–4.7及Fig4.11说明。其它相邻谱页的提取用于核caption，不冒称全论文重新精读或全图逐点数字化。
- 实际视觉：AW13 PDF57 Fig4.1整图及三张低能级放大裁图，PDF70 Table4.4，PDF72/73 Tables4.5/4.6，PDF76 Table4.7（仅低spin链接，不改highspin配置），PDF77 Fig4.11，PDF80 Fig5.1，PDF83 Fig5.2，PDF86 Band2/3主线。Li PDF2 Fig1及Fig2、PDF3 Table1和相关段落fresh视觉核。没有在本worker重读Li PDF1或声称新全文三页阅读。

## Li正链可绑定的AW13节点/边

下表是**source-scoped、高可信但provisional的family crosswalk**：同核、同π、同母末态spin、连续五条级联及g7/2解释共同支持。它不表示γ能量精确相等、两次采集同一数据、旧τ已由AW13重测，或每个出口的branch/ICC已齐。

| Li04 PDF2 Fig1 | Ji→Jf | AW13对应行 | Li−AW keV | 寿命能挂到什么对象 |
|---|---|---|---:|---|
| 257 keV | 9/2+→7/2+ | **255.8**，Table4.6 PDF73/printed69 | 1.2 | 只作级联/ground锚；Li Table1没有9/2+寿命行，不能补τ |
| 610 | 13/2+→9/2+ | **607.7**，Table4.5 PDF72/printed68 | 2.3 | Li的13/2+母态τ=1.46(56)ps，匹配AW13-B2-13/2+ family |
| 725 | 17/2+→13/2+ | **723.7**，同上 | 1.3 | Li的17/2+母态τ=1.32(10)ps；Li Fig2b实际展示该线形 |
| 796 | 21/2+→17/2+ | **793.6**，同上 | 2.4 | Li的21/2+母态τ=.60(26)ps |
| 649 | 25/2+→21/2+ | **647.4**，同上 | 1.6 | Li的25/2+只给τ<2.19ps，**effective、未作feeding correction**；不是有限meanτ |

Li finite/limit数值取其PDF3/printed463 Table1，既有LI04-1–4用户flags保持。本轮只核目标身份，不再次审核/更改旧人审范围。原Table1的Qt与τ是旧Li派生/测量链，不重算或合并；它们不是AW13采集的新结果。

**不能绑定：**上述τ不能挂到AW13负Band1、Band3、Band5的同spin正宇称态、整条Band2所有其它spin，或133Ce任何态。Li没有这些目标的逐态τ。多条独立邻线和拓扑提供family对应，但无双方Eγ误差/校准联立资料，不以1–3keV差异宣称统计相容、实际同一线精确值或“新版本修正旧版本”。两组能量分别保留。

### 零点与路径能量

Table4.5/4.6没有Ex列。以7/2+ ground=0作明确声明的选定路径：

| 节点 | Li Fig1整数能量和 keV | AW Table4.5/4.6指定路径和 keV |
|---|---:|---:|
| 9/2+ | 257 | 255.8 |
| 13/2+ | 867 | 863.5 |
| 17/2+ | 1592 | 1587.2 |
| 21/2+ | 2388 | 2380.8 |
| 25/2+ | 3037 | 3028.2 |

这些是**selected-path sums**，不是论文已给的adopted Ex或带Cov拟合。不能把一个来源的母态Ex和另一个来源的Eγ拼成“精确节点”。AW13另一signature的Table4.5 E2选路可得到11/2+=542.2、15/2+=1209.8、19/2+=1973.2、23/2+=2756.6、27/2+=3265.7keV；该路仅保自身定义，不强制与下述冲突dipole表全局闭合。

## Band3节点/边与743-keV归属缺口

AW13 Fig4.1(PDF57/printed53)和Fig4.11(PDF77/printed73)支持低能正宇称Band3的图示边；Table4.4(PDF70/printed66)有338.1(7/2+→3/2+)、509.9(11/2+→7/2+)、623.4(15/2+→11/2+)三条明确主链E2。图还给72(3/2+→1/2+)、212(5/2+→3/2+)、284(5/2+→1/2+)、125(7/2+→5/2+)；这些低线没有Table4.4对应精确行。

保留两层：1/2+的61.8keV为直接正文；其它节点若算Ex，应标条件加和。沿61.8+rounded72再接338.1/509.9/623.4得3/2+≈133.8、7/2+≈471.9、11/2+≈981.8、15/2+≈1605.2keV。5/2+由61.8+rounded284得≈345.8keV；另一条到7/2+的125路径给≈470.8，与前一路差1.1keV。没有精确低线/误差，不选某一路认证精确Ex。

**743.3不能仅凭Table4.4的“Band3 quadrupoles”分组自动建一个adopted Band3 19/2+节点。** 该行印19/2+→15/2+、Iγ=6.2(.5)。Fig4.1却只明确画Band3主链至15/2+，并画Band5的19/2+经约743-keV箭头馈入Band3的15/2+；Table4.7(PDF76/printed72)另列743.4、19/2+→15/2+、Iγ=20.1(.9)。两行强度不同，**也不能静默把743.3与743.4并成同一条重复link**。目前保留：Table4.4原行的末态带身份/是否另有未画的Band3 19/2+为unresolved；Table4.7+Fig4.1支持的743.4作为Band5→Band3独立行。Ledger不造一个已确认Band3 19/2+，也不宣称物理上不存在这个态。

Fig4.1还有Band5→Band3的677-keV连接；Table4.7给677.4、17/2+→15/2+。§4.3.2 Band3(PDF59/printed55)及Band5(PDF66/printed62)文字都提677/743与两带关联。913.2另有末态问题：Table4.7字面21/2+→17/2+，图上913箭头似落在Band3 15/2+共同level线；不凭图表任挑一边，不用它锚定Ex或生成新的精确Band3节点。

**同spin控制：**AW13 Band2的19/2+与Band5的19/2+必须是不同source-scoped节点，后者有独立333.1-keV退激和743.4-keV跨带出口（Table4.7），前者有763.4-keV带内出口（Table4.5）。Table4.4另一个未解19/2+行保持自己的candidate身份，不能因spin或近同γ合并。

## 其它必须保留的原件冲突

1. **Table4.6低spin dipoles：**PDF73/printed69字面344.9为13/2+→11/2+、410.1为15/2+→13/2+。Fig4.1放大图却将rounded345连接15/2+→13/2+、410连接21/2+→19/2+，并另画321(13/2+→11/2+)、378(17/2+→15/2+)、384(19/2+→17/2+)。保留原表行和图行，不自改spin。仅使用表中11→9的285.1和13→11的344.9相加，已与E2行607.7相差22.3keV；这不是一个可用“整数舍入”解释的精确图闭合。它只说明当前打印graph身份/数值未闭合，不证明哪行错或实际测量出错。Li对接绕开这些冲突行，不用整表盲拟合adopted Ex或S。
2. **Table5.1的Band2 parity：**PDF79/printed75原单元为负，Fig4.1、Tables4.5/4.6、PDF86正宇称正文相反；继续保留既有内部冲突，不改原记录。
3. **Fig5.2 caption vs正文：**PDF83/printed79图注写negative-parity Band4；紧邻PDF82/printed78 §5.2.1的Band1正文两次用此图论述Band1。本轮视觉重核，冲突未解，不把一图计为两条独立测量。它也不是正Band2或Band3的S数据。Fig5.1(PDF80/printed76)是Bands1/2/5/7的Routhian图，不能用其相对Routhian零点替代Ex ground零点。
4. Band5 Table5.3 highspin两分量既有人审完全保持；本轮看低spin节点/连接不重开其配置映射。

## 匹配合同、影响和剩余输入

知识影响为`refines-and-limits`：可以把Li的四个正宇称寿命对象与AW13 Band2特定母末态family连接，避免“131Ce全核无寿命”或“AW13 Band3可用Li正τ”的误写。仍需每个实际branch的全出口、ICC、时间定义、feeding、共同Cov和跨publication身份，才能组合绝对B或执行same-input模型比较。AW13自身没有新τ；Li正负宇称不是同宇称伙伴对；本轮也没有恢复133Ce任何τ。

新增主要缺口是source table/figure的明确节点冲突。没有用无依据全局重新标号、插值、自归一或多表平均关闭它们。今后若有原作者adopted level table、旧Refs47–50或逐门谱，可优先核743.3/743.4和Table4.6母末态；当前不因这些缺口把其它已经清楚的E2 family crosswalk全部丢弃。

## 产物与命令检查

- `node-edge-crosswalk.json`：Band2的37条Table4.5/4.6原字面边、两signature的条件路径节点、Band3低节点与边、独立743.3未解行、Band5低spin链接、5条Li crosswalk。此JSON不替代原表，也不包含新的adopted Ex fit。
- `checks.json`：两raw SHA、37行/5条crosswalk计数、π/spin步长、逐来源能量差、未硬造B3 19/2节点和22.3keV图闭合残差；这些只认证转录/算术，不认证实验CI或配置。
- `artifact-manifest.json`：本worker与tmp产物列表/hash。
- tmp保存raw检查、定向PDF页文本、视觉图及Fig4.1放大裁图。未下载外部来源。

命令：`git status --short --untracked-files=no`识别并保留共享已有修改；Python hashlib/PyMuPDF核原件SHA/页数、定向提取render；`view_image`视觉检查上述原页；JSON解析与恒等式/计数检查。未做作者模型、用户数据、统计拟合或Git写入。
