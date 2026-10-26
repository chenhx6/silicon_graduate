# 131Ce与133Ce：能带、可观测量和分析流程的限定综合

本报告响应“将133Ce硕士论文作为与131Ce学位论文同样重要的长期分析蓝本”的要求。比较的基本单位是各自原件的带头、Jπ、具体跃迁和组态解释，不能先把两个核的Band1/2/3/4当作同一物理对象。本轮仅完成可追溯比较与操作蓝本，不宣称用户独立数据已分析、全文翻译已完成或集体模式已裁决。

完整字段、unknown和定位见[comparison_matrix.json](comparison_matrix.json)；实际操作见[blueprint_checklist.md](blueprint_checklist.md)；下一日只作附属研究的候选见[next_day_supplement_questions.md](next_day_supplement_questions.md)。本任务不改变Day23主体、课程卡/学分和当前effective17:00收束边界。

## 1. 三条必须先纠正的预设

1. **Band3不是同一个“基态带”。** Alwaleedi2013的131Ce Band3被作者指定为61.8keV的低激发1/2+带，并可能为νs1/2[400]1/2+；Wakudyanaye2022的133Ce Band3才建于1/2+基态。没有直接测定两者相同的s1/2/d3/2混合系数。
2. **两核并不都拥有同口径的ix/ωc。** 131Ce论文有Harris reference、实验alignment/Routhian和Table5.1 crossing；133Ce论文主要研究低spin能量/S/QTR和EM，当前没有相配套的实验ix、Band1/4 crossing数值。模型长轴Rl≈2ħ不是实验cranking ix，更不能把131Ce的ωc借来填133Ce。
3. **不能说131Ce全核“没有寿命”。** AW13这批Bands1–7分析缺完整partner/link-specific τ、measuredδ/P及absolute strength network；Wiki已保存Li2004/Singh2016的独立DSAM/RDDS寿命和Ionescu-Bujor1998的静态矩证据。它们各有带/态/方法身份，不能自动补齐AW13 Band4↔Band1的全部分支。

## 2. 来源与采集身份

|来源|核/反应|原件与本轮锚点|分析特点|
|---|---|---|---|
|AW13，Alwaleedi2013博士论文|131Ce，N=73；100Mo(36S,5n)，165MeV|97页；PDF=印刷+4；PDF56/58–59/67–73/79–90相关页|101-Ge Gammasphere；fold≥7约3×10⁹事件，展开为四重符合/4D hypercube，4DG8R；强度归一508keV线|
|WK22，Wakudyanaye2022硕士论文|133Ce，N=75；125Te(12C,4n)，57MeV|130页；PDF=印刷+11；PDF61–71、77–115相关页|AFRODITE数据，论文具体run写13clovers=1@45°+8@90°+4@135°；γγ/γγγ、AD/RAD及QTR；强度归一170.2keV|
|Ding2021已存在直接来源|131Ba(GALILEO)与133Ce(AFRODITE)|原PDF2，实验/两点Rac方法本轮直接回读|GALILEO为131Ba辅助方法，不是131Ce采集；与WK22正宇称研究同源/重用，不增加独立133Ce实验票|

**设备谱系冲突必须保留：**Ding2021 PDF2把133Ce AFRODITE写成8clovers=4@90°+4@135°，而WK22 PDF61写13clovers；WK22 Ch4通用介绍亦写8并提后来17。不能凭共享event总数判定哪一处代表具体angular-analysis detector mask。后续实际重拟必须拿run geometry/live mask/angle grouping；本报告分别引用各原文，不挑一值暗改另一文。

原件hash由本轮脚本重算并保存在JSON：AW13 b50c22877418de560f06002588bb46d34f5ba670c6880e30a89d1509c79ad8c1；WK22 48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080。Ding是现有原件的针对性方法补核，未扩展检索新来源。

## 3. 逐带结构对照

### 3.1 负宇称νh11/2 yrast族

|字段|131Ce AW13-Band1|133Ce WK22-Band1|
|---|---|---|
|带头/基线|9/2−及11/2−signature序列；作者转载9/2−异能态80ns、161keV退到7/2+|9/2−；Table5.1由207.4−170.2给37.2keV中央值|
|组态层|νh11/2[514]9/2−，e/f；alignment后e/f⊗EF|主要轨道18≈νh11/2[514]9/2−，九轨道QTR与单轨道FA比较|
|ix|作者给第一次gain约9ħ@ω≈.3、第二次可能约5ħ@.6；初始ix未在本轮图上精确取数|没有相配套的实验ix数表；Rl/K/Ω是另一类模型量|
|ωc|Table5.1：α=−1/2为.329、α=+1/2为.367MeV/ħ；caption“accurate±.002MeV”不是新构造CL|unknown；不从bandhead、能量近简并或Harris模型参数推造|
|S(I)|作者描述低spin增大、I≈13ħ后下降、I≈25ħ又增大，并用core polarization解释|九轨道QTR较好描述Band1 S，但9/2、11/2能序有失败；不据S唯一确定γ|

131Ce的Harris reference是130Ce S-band，J0=17.0ħ²/MeV、J1=25.8ħ⁴/MeV³（AW13 Eq5.1–5.3/PDF79）。133Ce正宇称QTR的10.4/35.7及负宇称10/25是另一套模型惯量，不是相同实验reference，也不允许直接合并ix曲线。核素差两个中子、pairing/blocking及Fermi位置不同；相同Nilsson标签只提供候选组态连续性。

### 3.2 负宇称非yrast族

|字段|131Ce AW13-Band4|133Ce WK22-Band4|
|---|---|---|
|带头|15/2−；PDF85/p81正文报Ex=972keV|13/2−，832.0keV，Table5.2|
|作者解释|可能γ振动耦合νh11/2[514]9/2−，Table5.3写γ⊗e/f|九轨道QTR中主要同轨道18、额外约2ħ长轴芯转动的TiP解释|
|实验links|Band4→1有538.3、611.1 M1/E2及994.3、1108 E2；反向有504.9 M1/E2、871.2 E2|624.6、608.7、582.7、464.4等mixed与794.8、993.4、982.0等E2网络|
|ix/ωc|Band4不在Fig5.3数值alignment系列或Table5.1 crossing表中，保持unknown|相同缺口；不拿模型Rl当ix或从其它带补ωc|
|电磁限制|R为angular-intensity ratio，非measuredδ；δ=0用于部分band比值；无完整Band1/4 τ/δ矩阵|三条连接δ和两类relative-B比存在，但原producer/Cov、582 out/out身份及表–图尺度冲突未闭合|

AW13正文的972keV只是本任务保留的作者字面带头值，尚未以完整adopted-energy/零点/互链表独立闭合，不用它作跨核精确head-spacing结论。最稳健的比较是各自的head spin、parity及具体连接线。两个“Band4”不同的head spin与解释，不意味着它们是同一个声子模式，也不应将γ vibration、TiP、signature partner和wobbling互换命名。

### 3.3 正宇称νg7/2候选族

131Ce AW13-Band2由作者归于νg7/2[404]7/2+、a/b两signature，Table4.5/4.6包含带内E2和255.8、285.1、344.9、410.1等M1/E2线，现工作延伸到63/2+。作者给初始alignment约1ħ、首次约9ħ gain@.3MeV/ħ，并用πh11/2 EF crossing解释；Table5.1两signature的ωc均.316MeV/ħ。第二次约2ħ gain@.6被提为可能AB，需更多数据。该表Band2 parity单元打印负号，与Fig4.1、Tables4.5/4.6及§5.2.2正宇称冲突，保留而不采用错误单元裁决parity。

133Ce WK22-Band2建于7/2+，Table5.3正文整数340keV，337.8线从678.1退到7/2+给340.3keV中央闭合。其带内337.8、355.3、426.4、392.8、451.4 mixed序列及693.1、781.8、819.3、844.4等E2形成强耦合候选。19/2+有2733.4与2739.5两行，不能因相同spin合并或任择其一计算高端S。

WK22的QTR主轨道20主要为g7/2[404]7/2+，相邻s1/2/d3/2的K=1/2混合与Coriolis、γ共同影响S；χ=.7时较大γ≈20°才恢复显著S。**这说明S对模型多项输入敏感，不表示本实验独立测得low-j混合系数或γ刚性。** Table6.3的9/2+主振幅打印平方和>1及ε4=.1/.01、ε表单位/λF零点等缺口必须保留。

AW13没有同口径的low-j QTR波函数扫描，WK22也没有本任务所需的实验ix/ωc表。因此可迁移的是“对g7/2 strong-coupling候选同时检验S、mixing、EM及crossing”，不能声称已完成两核low-j Coriolis admixture的定量比较。Band2的S幅度没有在本轮做曲线精确数字化，保持unknown；Ding对Ta/Re的十倍幅度比较也不能变成131Ce对133Ce的十倍结论。

### 3.4 低j正宇称Band3族与近简并

131Ce AW13-Band3：1/2+，Ex=61.8keV，作者仅给“possible νs1/2[400]1/2+”解释；Table4.4提供338.1、509.9、623.4、743.3keV的E2序列。本轮没有从完整共同零点重建Band3全部absolute energies，不能填其与Band2近简并点/ωc；也不把候选νs1/2解释改成已测s/d混合。

133Ce WK22-Band3：1/2+基态，Table5.4列3/2+134.2、5/2+318.3、7/2+570.4、9/2+815.9、11/2+1201.4、13/2+1445.8、15/2+1932.9、17/2+2171.9keV。Band3 13/2+@1445.8与Band2 13/2+@1459.9相差14.1keV；该母态的412.4keV mixed线到Band2 11/2+@1033.4，767.7keV E2到Band2 9/2+@678.1。这里有可定位的same-spin近邻与跨带链接，但不是已测混合矩阵元/avoided-crossing gap。

Table5.3/5.4的assigned能量在11/2时E2−E3=−168.0keV，13/2时+14.1，15/2时−80.2。仅能说source-local两序列的同spin能量相对排序变化，不能据三点插值出旋转频率交叉、反推相互作用强度或宣称两条unperturbed组态真正相交。该例很适合作为后续“同spin配对不等于同带/同模式”的身份练习。

## 4. 同定义的少量S(I)中央值对照

AW13 Eq5.5/PDF82与WK22 Eq2.37/PDF35为同一四能量算符。令dI=E(I)−E(I−1)，则S(I)=dI−[d(I−1)+d(I+1)]/2。本轮只选表中明确带内M1/E2相邻三线，逐项列在JSON，不用谱图的模糊标签反推全套adopted levels。

|带族/共同spin|131Ce selected-path S（keV）|133Ce selected-path S（keV）|
|---|---:|---:|
|Band1，13/2|180.80|182.10|
|Band1，15/2|−237.80|−216.15|
|Band1，17/2|320.50|277.30|
|Band4，19/2|65.20|49.60|
|Band4，21/2|17.15|100.55|

它们是本任务透明选择的局部路径算术，不是两篇论文各自发表的S点清单，也不是全网络唯一能级重建。未有原energy Cov，故不加实验误差条、显著性或γ反演；冗余E2/M1边有打印差异时应先做closure，再给最终adopted S。

**新发现的source identity边界：**AW13 Figure5.2/PDF83 caption写“negative-parity band4”，而前后§5.2.1连续讨论Band1和同一fig。不能把整张曲线既计为Band1又计为Band4；本表回到明确的source gamma rows，避开caption身份认证。S是能量的线性派生量，拟合E之后再把S当独立数据会重复计权。

## 5. 方法迁移与能判别的东西

- 608.3/608.7近双峰说明：单门出现209/399不能唯一认证它们与608.3直跃迁同路径。必须用门响应、互符合和独立第二/第三门分离分支，不能把anti-coincidence中的低统计缺峰强行置零。详细步骤在checklist。
- AD、DCO、Rac是不同选门角度/响应的observable。stretched dipole/quadrupole是多极阶及spin change分类，不是单靠角比测出electric/magnetic。mixed M1+E2应保留δ全部允许根和取向/有限几何/feeding条件。
- out/in与out/out必须逐母态、终带及reference绑定；同parentτ相消不等于能删除efficiency、conversion或共同归一Cov。131Ce Eq5.6假定δ=0不能当成 measuredδ，133Ce三线δ与两比同源不能计三票。
- 本次thesis网络缺绝对τ/完整absolute BR时只有相对B约束；但131Ce已有独立寿命/静态矩来源，需按state/branch/experiment映射后才可用。DSAM/RDDS可增加独立绝对强度信息，其feeding/stopping/geometry/背景模型及所有缺测分支仍须核；它们不是任何collective-mode标签的普适充分最终判据。
- QTR输入、reduced-ME归一、whole-M1缩放、固定轨道与经典freeze等已开控制可继续支撑分析训练，但不能用“缺原代码”把所有可算量都拒绝，也不能用一个toy控制冒实际作者job。

## 6. 本轮完成与真正未完成

完成的是四family比较矩阵、五个selected local S并列表、Band3近邻定位与可执行分析清单；未关闭的是133Ce ix/ωc、131Ce Band3全能级/近简并、完整δ/τ/branch Cov、所有模型实际input及高spin跨带mapping。下一日附属研究优先选actual ledger闭合，并限制每次主卡完成前只开一个小问题，不因本项目重要就替代下一日主线。

本worker未读用户独立原event/私有拟合，也没有修改source、人审、raw或Git。父代理负责把经过边界校准的可复用增量写回knowledge，并决定下一日prompt调度；这里不擅自发布或授分。
