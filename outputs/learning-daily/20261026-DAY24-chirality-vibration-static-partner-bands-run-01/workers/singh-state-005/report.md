# Singh2016：131Ce逐态寿命台账与133Ce输入迁移合同

状态：本 worker 对原件的限定 self-audit；`needs_review: true`，不改变 canonical source 的 review 状态。仅写本 worker 目录，未创建 run/session/credit、未修改 raw、PLAN、Bib、canonical 页或 Git 暂存/提交/远端。可复用内容由主代理审核后写回知识层。

## 原件、读取范围与定位约定

原件：R. P. Singh et al., *Pramana – J. Phys.* **87**, 7 (2016), DOI 10.1007/s12043-016-1218-6。这里 **7 是文章编号，不是7页**。本地 PDF 有11页，1202741 bytes；本轮重新计算 SHA-256 为 `95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30`，与 source 页相符。

本轮实际阅读：11页逐页提取文本并读正文/参考文献；视觉查看 PDF3–10 的页面图，覆盖 Figures1–12、Tables1–2、Eqs1–5；另以4倍图查看 Fig1。PDF页与印刷页均为 “Page n of 11”（文章编号7另列），下文 `PDF5/printed5` 即同页。不是只查关键词或继承 Day20 的阅读认证。Table2/133Pr仅为全文主线和方法对照阅读，不在本轮逐态数值提取范围。

本轮以 source 页 Day20 更正为校准入口，并独立回原表：正确的 present 27/2− mean τ 是 **1.25(+0.41/−0.25) ps**；旧1.24值不复活。Day20关于 Eq1中央换算、K混合、Cov及旧ref转换残差的未闭合边界保持，本轮不通过重算强行闭合。

## 131Ce Table1 present 台账

Table1只印初态Ji；下表末态由 PDF3/printed3 Fig1 的箭头和 PDF5 Eq1 的 I→I−2共同确定。各行均负宇称，不能只凭相同 spin 或 “yrast” 跨论文配对。

| Ji→Jf | Eγ keV | Ex_i keV（条件加和） | present mean τ ps | present Qt eb | 方法及原件定位 |
|---|---:|---:|---|---|---|
| 15/2−→11/2− | 510 | 810 | 9.6(+1.9/−3.8) | 2.93(+.60/−.30) | RDDS/plunger；PDF3 Fig3a，PDF5 Table1 |
| 19/2−→15/2− | 642 | 1452 | <7.31 | >1.90 | RDDS/plunger；PDF3 Fig3b，PDF5 Table1 |
| 23/2−→19/2− | 750 | 2202 | >1.3 | <2.85 | DSAM停止时间下界；PDF4末段–PDF5首段、Table1；另有 plunger 约3 ps上界（不在Table1） |
| 27/2−→23/2− | 827 | 3029 | 1.25(+.41/−.25) | 2.26(+.37/−.23) | DSAM；PDF4 Fig4a,b，PDF5 Table1 |
| 31/2−→27/2− | 892 | 3921 | .51(+.05/−.05) | 2.66(+.13/−.12) | DSAM；§2.3高spin分析与Table1归属；Fig4未单列此线 |
| 35/2−→31/2− | 922 | 4843 | .60(+.11/−.10) | 2.43(+.22/−.20) | DSAM；PDF4 Fig4c,d，PDF5 Table1 |
| 39/2−→35/2− | 962 | 5805 | <.54 | >2.29 | 高spin DSAM归属为章节级推定；PDF2 §2.1/PDF4 §2.3和Table1，无962线专门诊断/限值构造图 |

4个有限 mean τ、3个单侧限值，与 PDF10/printed10 §7 Summary 的计数一致。限值不得改造成中央值、零值或正态误差点。23/2−是最清楚的例子：750 keV在最小plunger距离全移位（PDF3），DSAM无明显随角度变化的线形（PDF4），正文给停止时间下界1.3 ps及plunger约3 ps上界（PDF5）；不能据此宣称一个具有完整联合置信度的[1.3,3]区间。

**Ex口径：**原表没有Ex列。PDF3 Fig1以7/2+基态为0，9/2−经162 keV到基态，11/2−经138 keV到9/2−，然后依次510/642/750/827/892/922/962 keV。故本轮只给 `Ex(7/2+)=0` 下的**印刷整数γ能量加和**：9/2−=162、11/2−=300，以及上表810…5805 keV。这不是原表已测精确Ex，未给相关能量误差，不能把整数加和用于亚keV精度或替代评估能级。该Fig1本身据Refs11/21采用，并非本工作重测全能级方案。图中的基态10.3 min与9/2− 88 ns均为标注的 **T1/2**，不能当作 present mean τ或side-feeding寿命塞入Table1。

## 本次提取对feeding和误差的依赖

| 状态/对象 | Table1印刷参数 | 角色与locator |
|---|---|---|
| 15/2− | τSF=1.0(+.1/−.2) ps，QSF为破折号 | 附加cascade feeding；PDF3右栏至PDF4首段。低spin Bateman拟合使用 present DSAM确定的23/2−以上四极矩作约束，故技术不同不意味着拟合输出完全独立 |
| 27/2− | τSF=.73(+.15/−.12) ps，QSF为破折号 | 27/2−附加cascade，兼有四级转动侧馈模型；PDF4右栏及Table1 |
| 31/2− | QSF=5.79(+.24/−.28) eb，τSF为破折号 | 侧馈拟合参数，不是yrast Qt；PDF4 §2.3、Table1 |
| 35/2− | QSF=5.01(+1.44/−.77) eb，τSF为破折号 | 同上 |
| 19/2−、23/2−、39/2− | 两列均破折号 | 未给逐行参数，不是零feeding或已证无feeding |

PDF2–3：131Ce用119Sn(16O,4n)131Ce，plunger 86 MeV与厚靶DSAM 90 MeV为不同采集。plunger用162-keV门（9/2−→7/2+），避开138-keV门受181Ta 137-keV污染；300-ns符合时间窗用于接收大部分88-ns异构态退激；510与511-keV正电子湮灭峰干扰使singles未用于寿命拟合。符合统计不足以用直接feeding shifted-component门做DDCM，因此采用 LIFETIME 的归一unshifted强度 Bateman拟合。

PDF4–5：DSAM将510/642/750-keV下方门谱相加；`LINESHAPE`模拟5000条recoil histories、.002-ps步长。四级转动侧馈惯量取30 MeV⁻¹ ħ²，feeding强度来自98°数据及旧Ref29。Ziegler与shell-corrected Northcliffe–Schilling两种停止方案给出的结果取平均，quoted error取两者较大者，并设τ最小10%误差。plunger和DSAM误差分析均用MINOS，正文给参数χ²增1的误差定义；PDF5另给侧馈参数68%窗口。**没有完整跨态Cov或各限值的likelihood**；不能把这些误差处方当成已经证明的独立Gaussian样本，也不能将平均两种stopping当成两个独立实验。

## Ref31/32比较列：旧τ与依赖的Qt

PDF5/printed5 Table1 caption明确说：旧Refs31/32的寿命与“using eq.(1)”提取的Qt一同列作比较。PDF11 Ref31=T. Klemme et al., PRC60,034301(1999)，Ref32=G.-S. Li et al., CPL21,461(2004)。本 worker只直接核了Singh的原始转载和归属；**未在此worker重新打开Klemme或Li原PDF**，不能把该表的归属核对写成已独立核完原始旧论文。

| 旧来源列 | Ji−，Eγ keV | 转载mean τ ps | Singh比较列Qt eb | 计权身份 |
|---|---|---|---|---|
| Ref31 | 15/2，510 | 7.53(37) | 3.24(8) | 旧τ；本表依Eq1转换Qt |
| Ref32 | 19/2，642 | >4 | <2.5 | 旧下界→Qt上界 |
| Ref32 | 23/2，750 | 1.44(54) | 2.72(51) | 旧τ；依赖转换 |
| Ref32 | 27/2，827 | 1.23(23) | 2.28(21) | Li旧τ，**不是present1.25**，也不是第三次测量 |
| Ref32 | 31/2，892 | <1.04 | >2.03 | 旧上界→Qt下界 |

其它旧列破折号均不造值。Figure5（PDF6）circles为present，star为Ref31，diamond为Ref32；图中的全部点不能作2016新数据。引用链应为 `旧采集→旧τ→Singh再转换Qt→Fig5`；同一τ的多个转载或派生不能重复计权。当前实验与Li旧实验的独立采集身份由来源页已有记录承接；不能据此假定跨实验所有共同系统误差为零。

Qt转换边界：PDF5 Eq1以Eγ MeV、Qt eb、T s⁻¹，系数1.224×10¹²；PDF6首段明确Table1采用K=1/2。Qt是转子模型下的派生量，非直接测得的静态四极矩。PDF5 Eq2–3讨论mixed-K，未给每行真实branch/ICC/exact producer。不能从 τ/Qt 的中央值残差恢复实际branch或擅自改表。PDF9 Eq4以prolate、无hexadecapole条件转换β；Eq5需要γ/轴约定，−80°来自TRS输入再检验相容性，而不是单个Qt独立量出γ或刚性。

## 133Ce蓝本可用的输入迁移合同（方法层）

| 输入层 | 目标核必须另有的字段/证据 | 从本文可借鉴的检查 | 必须保持unknown的情况 |
|---|---|---|---|
| 状态/边身份 | source/run、目标核、原作者band标签、Jiπ/Jfπ、Ex零点与误差、Eγ、门/级联支持 | 先逐态逐边，保持同一母态与末态，不按band编号合并 | 133Ce与131Ce同号band、同spin或同orbital不能自动映射；τ不存在或不属于目标parent就不填 |
| 时间定义和观测对象 | mean τ或T1/2、finite/upper/lower、置信定义、direct/feeding clock、采集谱系 | Table1的mean τ与Fig1的采用half-life分栏 | limit只知方向而无likelihood时不补中央值/CI；邻核τ不作为prior或替代观测 |
| 直接响应 | 目标实验beam/target/backing/stopping、速度、距离/角组/门、污染峰、拟合谱和实际feeding | RDDS与DSAM互补选法；核对shared constraints和门下级联 | 不搬1.20%c、30MeV⁻¹ħ²、τSF/QSF、5000条history、停止方案或10%处方到133Ce作为已验证精度 |
| 部分率→绝对B | 同parent全出口、photon vs conversion-corrected强度、BR/ICC、E/M混合δ所有根、τ与共同Cov | mean τ→总率；用本态的photon branch和多极份额取部分γ率后才转B | 只有相对强度比可消同parentτ；不同parent不能消，未知branch/ICC不补1/0；不得用131Ceτ或Qt把133Ce相对比“绝对化” |
| Qt/模型 | 目标核旋转式/单位、K或波函数混合、β/γ/轴、转动/电磁算符、参数版本 | 分开实测率、派生Qt、模型形状与我们的推断 | 不搬131Ce Qt/β/γ、TRS minima或同一band号；Qt不自动定静态Q或γ刚性 |
| 来源依赖 | 原测量ID、转载ID、转换ID、图重绘ID；共享normalization/feeding约束 | ref31/32的same-τ→different-Qt链显式列出 | 同一数据的论文/学位论文/新转换不能视为独立测量；未有Cov不假定零 |

可直接接入蓝本的是“先身份→时间/限值→方法/feeding→部分率/单位→模型→谱系”的空字段合同。**本worker不向133Ce表填任何131Ce数值τ/Qt，也不假定131Ce某band编号等于133Ce同号band。** 133Ce现有同parent相对B比只在该母态身份和光子强度定义齐全时保留τ消去；新增绝对量要有133Ce该态自己的寿命与完整出口。

对Day24主问题的边界：此文主要为单条νh11/2 yrast寿命和πh11/2核对照。PDF9明确另一个接近15ħ变yrast的带因统计不足**未测到寿命**；Table1不提供一个手征伙伴对的完整逐态绝对B矩阵。γ-soft背景或作者TRS解释不认证chiral vibration/static chirality，也不能填补另一条候选带的寿命。

## 可复核产物与命令检查

- `raw-check.json`：本轮raw路径、bytes、11页和SHA匹配。
- `pdf-page-01.txt`…`pdf-page-11.txt`：本轮从同raw生成的逐页文本；不替代原件。
- `pdf-page-03.png`…`pdf-page-10.png`、`fig1-detail.png`：实际视觉查看的页面/局部图。
- `ce131-table1-state-ledger.json`：7 present rows、5 comparison rows，区分finite/limit与null，保留逐行method attribution和派生Ex口径。
- `ledger-checks.json`：SHA、4 finite/3 limit计数、ΔI2/负宇称、整数能量边闭合；这些是转录/算术控制，**不是实验认证**。
- `verify_ledger.py`：可重复只读检查现有raw与本ledger；命令为 `python3 <本目录>/verify_ledger.py`。

执行过的工具：`pdfinfo <raw>`（11页、未加密）；Python `hashlib.sha256`、`pymupdf.open`逐页文本与render；`view_image`实际查看上述页面；`git status --short --branch`仅识别继承dirty，不修改；JSON与能量恒等式控制。无外部检索、无旧原件复核、无实验events重分析、无统计趋势重拟合。

缺口已经隔离：精确Ex/误差、全branch/ICC、各限值likelihood、joint Cov、actual producer/fit参数、旧原件跨核对和跨文band ID均未被补造。任务范围限定为原件提取与方法迁移，没有等待缺输入或扩大到新采集/新课程。
