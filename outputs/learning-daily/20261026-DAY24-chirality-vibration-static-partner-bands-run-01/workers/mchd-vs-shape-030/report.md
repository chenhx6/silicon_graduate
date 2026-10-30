# 103Rh原件控制：MχD标签不必等于不同shape/configuration共存

**科学处理：verified-no-op。** 本轮目标已由既有Kuti source的atomic claims和Day18校准完整覆盖；fresh原读未发现需要改该source的新科学事实或转录错误，不为新增而造physics。给三核矩阵可复用的一条比较边界见文末。

本轮仅Day24中Day25无学分preview，不开Day26。没有改canonical/raw/PLAN/Bib/Git、旧review/withdrawal，也未运行未知代码/114。

## 原件与真实覆盖

I. Kuti et al., *Multiple Chiral Doublet Bands of Identical Configuration in103Rh*, PRL113,032501(2014)，DOI10.1103/PhysRevLett.113.032501。

实际raw：`raw/papers/2014_Kuti et al_Multiple Chiral Doublet Bands of Identical Configuration in Rh 103.pdf`；5页、494614bytes；SHA256 **ef327ad2d7b55a71b72c356bb2789f107b1e1d464daa59c181bec44abf88a0b2**，匹配canonical。PDFn=printed032501-n。本轮5页全文主线及references已读，全部5页fresh视觉，覆盖Figs1–4、DCO/归属逻辑、CDFT/TAC/PRM输入与不利结果；本Letter无逐态τ/absoluteB表。本轮未新读Suzuki、Ref19/32或其它引文正文，无新paper/下载。

## 逐pair账本：不能跨宇称借clock或branch

| 本文pair | π与实测支持 | 配置/形状/动力学解释 | τ/absoluteEM边界 | 已有atomicID/原件locator |
|---|---|---|---|---|
| Bands1/2 | 正；此前已提出的pair，本篇Fig1/4给能量与B(M1)/B(E2)比较 | πg9/2^−1⊗νh11/2²；正PRM β.29、γ20°、J0=23；J0按谱趋势调；作者承接旧PRM的vibration→nearstatic→vibration解释 | 本篇未给寿命分离的双方绝对B表；Suzuki所测正“Band3”与这里1/2的精确编号crosswalk未在本轮恢复 | KU14-8/12；KU14-D18-3/4/7；PDF2/4，Fig1/4 |
| Bands3/4 | 负；新4与旧3扩展、links/DCO、约300keV同spin差、相似B比/alignments | 同effective πg9/2^−1⊗νh11/2g7/2配置的第一双重带；负PRM共同β.26、γ20°、J0=25、ξ.85 | 本篇没有3/4的DSAM/RDDS τ与分离absoluteB；不能用正pair寿命补 | KU14-2–7/10/13/16；KU14-D18-2/3/7；PDF2–4 Figs1–4 |
| Bands6/5（原文此顺序） | 负；新5与旧6扩展，约100keV同spin差、相似B比/alignments | **同一个负配置/同套PRM输入**的第三、第四本征带，组成第二/“excited”doublet；不是另换一个shape输入 | 同样无双方τ/absoluteB；计算5/6能量偏高约200keV、.45MeV alignment jump未重现；不能借其它pair补 | KU14-7/13–16；KU14-D18-8/9/10；PDF3–5/Figs3–4 |

DCO给quadrupole/dipole分类，负π还依赖PDF1末–PDF2的E2/M1 electromagnetic-character假定，不把DCO独立升级为电/磁完全测量（KU14-3/4）。Bands4与6的能量排序会随spin互换；“yrast/excited”是作者据alignments/ratios作的pair分组，不代表每个spin始终严格四态能序（KU14-7、D18-10；PDF3左栏）。

## 原件真正说的same-configuration与distinct-shape层次

**直接作者/模型陈述：**PDF1右栏明确将本例与此前133Ce/107Ag的“每对有distinct configuration”场景对比，提出检验同配置第三、第四带。PDF4右栏直接说：以一个负πg9/2^−1⊗νh11/2g7/2有效配置和J0=25、ξ=.85计算的**四个最低本征带形成两对**；PDF4末–PDF5总结将它们解释成同配置的yrast/excited chiral doublets。这正是标题中的限定含义，既有KU14-13/16已记录。

**不能误配CDFT两个minima：**PDF3右栏的configuration-fixed CDFT确列两个负候选：πg9/2^−1⊗νh11/2d5/2，β.27/γ18.7°；及含g7/2占据的候选，β.26/γ14.5°。但作者接着在TAC中因low-j强混合仅固定high-j配置、其余占据随自洽最低态，并将g7/2贡献约化为effective valence g7/2¹，随后用**同一**negative PRM配置描述3–6。不能把前述两个静态CDFT候选各分配给两个实验负pair，再把它称为本文已实证的distinct-shape MχD。

**形变差是模型结果：**ground β.25/γ20° γ-soft、正候选β.29/γ11°、负候选βγ和转动中β减/γ增均是CDFT/TAC输出（KU14-9/10；PDF3）。正/负PRM分别取β.29/.26而γ都20°（D18-7；PDF3末–PDF4首）。它们不是实验E0、Q或completeE2-invariant形状测量。本文未给一个两负pair的独立“不同shape”实验检验，也未证明真实多体波函数全部成分完全相同；same **effective** configuration归属依赖该模型映射。

## 不能省去的不利结果与实验谱系

- PDF4右栏：5/6计算能量比实验高约200keV，作者用“might”归因single-j PRM未充分含复杂关联；不是已测定唯一误差来源（KU14-13、D18-8）。
- PDF5首段/Fig3：5/6在ℏω≈.45MeV的alignment sharp increase未重现，作者称might与frozen core有关（KU14-14、D18-9）。
- PDF4左栏：正pair B比的实测随spin下降慢于计算，归于frozen-rotor近似；negativepair ratio的细节交错支持是模型/作者解释，不是所有绝对M1/E2矩阵元已逐态吻合（KU14-12/15）。
- 这些差异没有抹掉四条负带、links、同spin差、相似ratios/alignments的真实实验信息；也不能单独据此宣布same-config解释已排他错误。
- 本文部分band结构引用旧Ref19/32，并作新扩展/新band分析。本轮没读那些旧原始采集manifest，不另认证2014事件池与旧文完全独立；更不将CDFT/TAC/PRM三种比较重复计实验票。
- 原KU14-D18-1–11的跨宇称/Suzuki错误数据撤回完全保留。正“Band3”的寿命既不能因同编号挂到负Band3，也不能未经早期纲图核对就强配正1或2；本轮没有重算或平均那些τ/B。

## 已闭合的atomicID与唯一三核matrix边界

可直接引用已有source，而无需新建Kuti claim：

- **KU14-13、KU14-16**：同一有效配置的四PRM带→两doublets，以及依赖模型配置映射。
- **KU14-7、KU14-D18-10**：4/6能序互换，pair标签不能机械按每spin能序。
- **KU14-D18-2/3/7**：负3–6缺本文absolute τ/B；正负宇称crosswalk与实际PRM形变。
- **KU14-D18-8/9**：200keV和alignment不利结果。

**建议写入三核矩阵的一条新边界（综合，不是新实测）：**

> MχD表示同一核内多对手征候选/模型结构，标签和pair数本身不必意味着不同shape或不同effectiveconfiguration共存。103Rh在Kuti2014中提供同effectiveconfiguration、共同PRM形状输入上的yrast与exciteddoublets解释，说明应逐pair核其配置/shape证据，不能由“MχD”自动升级为实验三轴shape coexistence；同配置标签也不反向证明真实态没有shape变化或混合。

适用于134Pr/135Nd/136Nd矩阵的是这个量词控制，不是给它们搬103Rh参数、寿命、shape或模式胜负。原source已完整提供事实与限制，所以本worker对canonical的科学处理为**verified-no-op**；若leader写matrix，只需以已有atomicIDs承接上面这一条综合边界。

## 产物与检查

`reading-and-noop.json`保存真实原读范围/hash/atomicIDs；`pair-ledger.json`区分三个pair及无τ字段；`artifact-manifest.json`保存产物hash。tmp有5页text/render及raw check。

工具仅rg、local PyMuPDF/hashlib、view_image、JSON检查及read-only git status。无模型运行、数字化图/拟合CI、跨论文寿命借用、canonical写入或旧producer运行。
