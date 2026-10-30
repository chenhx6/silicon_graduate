# Heyde–Wood2011：形状共存定义、E0组合约束与companion量词

结论：该综述支持以状态/结构不同的E2性质、构型与混合组成形状共存的证据链，**不支持把“必须E0+multistep Coulex”设为每个核/每个spin的普适门**。旧HW11-D21-1中186Pb的固定V50–100keV、28%基态变形成分、20–35%激发态杂质及“E0排他唯一识别”的归属，未从本篇受检原件找到支撑；应在原ID下明确撤回该认证，而非由124短注覆盖后仍保留active强claim。

本轮为Day24内Day25无学分preview的有界原件校准，不开Day26。不改canonical/raw/PLAN/Bib/Git、旧人审/撤回或课程状态；HW11-4既有`needs_review:false`保持。所有新源读取/数学解释为self-audit，`needs_review:true`。没有把综述所引实验当本轮独立primary。

## 原件、版本与真实覆盖

Kris Heyde and John L. Wood, *Shape coexistence in atomic nuclei*, RMP83,1467–1521(2011), DOI10.1103/RevModPhys.83.1467。

实际raw：`raw/papers/gpt/high-spin-20260920/review/2011_Heyde_Wood_Shape coexistence in atomic nuclei.pdf`；55页、3400392bytes；本轮SHA256 **660c376e493e638501bfc8596d4eda46f490becb811ba5f30259d6f78c652183**，匹配source。首页出版2011-11-30并印publisher error corrected2011-12-06，本轮不另猜更正内容。

PDF页+1466=printed页。本轮**不是55页全文重读**：

- 定向连续主线：PDF7–13/printed1473–1479（mean field/GCM、定义背景、Pb与Eq14）；PDF27–30/1493–1496（Kr triaxial/K歧义、pairing isomer与高spinSD）；PDF36–44/1502–1510（§III.C.1–7：fingerprints、0+解释、mixing TableVI和方法限制）。
- PDF1/1467摘要/内容表与引言另读；PDF3–5早期shell-model段只作背景与具体旧数字候选检索，不据此认证整篇模型介绍。
- 视觉核PDF1、8、10–13、27–30、36–41、43，重点Eq14、Figs5/6/8–13/38–41/47–50及TablesIV–VI的角色和缺项。未逐格重新转录所有review表值或55页全图。
- 对55页native text做限定数字/词组检索并保存上下文；文本提取/搜索范围不等于实际阅读55页。

## 一、原件定义不是一种“纯静态几何态”的测量标签

PDF1/printed1467摘要将核内“arrangements”描述为**一组能量本征态具有不同electric quadrupole properties（矩、transition rates）以及相对Fermi能的不同proton/neutron pair分布**。因此可用的定义校准是同一(N,Z)内不同结构家族的共存与混合；不是见两个mean-field minima便把它们等同两条已测刚性shape，也不是所有能量本征态都应具有一个永久未混合形状。

作者确有很强的2011综述立场：**PDF11/1477**原字面认为low-lying excited0+“It appears…without exception”关联shape coexistence。本报告忠实保留为**作者综述观点**，不反向编成“HW11证明低0+与共存无关”。同一页又明确excited0+结构仍open discussion；**PDF39–40/1505–1506 §III.C.3**详细讨论seniority、pair distributions、振动解释失效及多种必要待查信息。这不是一个针对任意核素的、单一观测的逻辑iff定理。

**multiple minima与mixing的层次：**PDF8/1474 Fig6/Eqs10–12说，投影能曲线上给定能量不能唯一指定mean-field state；要得到可和实验比较的谱，需要在projected states空间作GCM/Hill–Wheeler混合。PDF9/1475 Eq13与Fig7呈现g(q)的分布/平均形变。PDF10/1476 §II.C进一步称mean-field能面是semiclassical，需要恢复goodJ/N/Z并纳入混合。此论证限制的是**从intrinsic mean-field minima到lab谱**的映射，不把“每个shell-model实现必须另外显式做GCM”设为通用算法要求。

## 二、fingerprints有层级，不是强制同时交齐的一套仪器清单

**PDF36–38/1502–1504 §III.C.2连续段**实际分为direct、indirect和hints：

| 原件内容 | 支持与条件 | 不能偷换的量词 |
|---|---|---|
| 最佳direct deformation fingerprint是diagonal E2 matrix elements；该段谈multistep Coulex yield和实验难度 | 多步CoulEx可提供对角/非对角E2和相关不变量；这是强约束路线 | 不是“凡形状共存均必须multistep Coulex” |
| 下一类是B(E2)，可由寿命（Doppler/fast timing等）或CoulEx yields得到 | 同段明确B(E2)本身不区分static/dynamic deformation；低能强collective出口可能非常弱，需完整BR | 不把一条大B(E2)单独当刚性共存；也不将所有寿命技术排除成不够格 |
| leading indirect fingerprints是strong E0与particle-core coupling patterns | E0对不同mean-square charge radii的配置混合敏感；耦合patterns也需Fermi位置等条件 | **不是E0与Coulex两者皆必测**；不是强E0自动唯一给β/γ |
| hints包括isotope/isomer shift、masses/separation、pair occupancies/transfer等 | 结合已建立结构及systematics提供定位/构型线索 | 不把hint当最终shape标签，也不把缺某个hint当否定 |

PDF37/1503还说明：multistep Coulex可利用virtual coupling在multichannel yield fit提取不易直接见到的E2；lifetime route要得到某个collective B(E2)需观察相应弱branch。**这比较的是两种测量响应/信息来源，不是“所有共存必须两项都做”。**

同综述**PDF13/1479**列高K11−Pb isomer的quadrupole moments由level-mixing spectroscopy、TDPAD等方法表征，g为其它互补量。故即使PDF1502对其对角E2-Coulex段使用“require”，也不能把语法对象扩成所有shape/coexistence判定的普适实验必要条件。

## 三、two-level E0公式实际约束什么

**PDF13/printed1479**作者先称E0 components为不同mean-square charge radii配置混合的“model-independent signature”；这个积极证据措辞应保留，但不能扩大成β/γ与mixing各量的唯一反演。紧接的**Eq14**明确先假定two configurations，混合幅a与√(1−a²)，给

\[
\rho^2(E0)=\frac{Z^2}{R_0^4}\,a^2(1-a^2)
\left[\Delta\langle r^2\rangle\right]^2,
\quad R_0=r_0A^{1/3},\quad
\Delta\langle r^2\rangle=\langle r^2\rangle_1-\langle r^2\rangle_2.
\]

原件是**均方电荷半径差**，不是未经条件转换的“Δβ²”。同页作者说由energies与E0可估mixing matrix/unmixed energies；这种估计须连Eq14中的半径差输入/假定，而不是把未知半径差消失。**PDF40/1506**随后明确半径差有时可由isotope/isomer shifts得到，并列能量、B(M1)、B(E2)、ρ²(E0)、transfer data的组合。

以下为本任务的**条件代数**，不是另一个测量或HW11新拟合：若η=a²、实两态H的unmixed detuning为δ、off-diagonal V，则observed gap D满足

\[
D^2=\delta^2+4V^2,\qquad
\eta(1-\eta)=\frac{V^2}{D^2},
\]

\[
\rho^2(E0)=\frac{Z^2}{R_0^4}\frac{V^2}{D^2}
[\Delta\langle r^2\rangle]^2.
\]

因此即使有D和ρ²，仍只约束\|VΔ⟨r²⟩\|这一组合；不能分别唯一反演V、η、半径差、β或γ。η↔1−η的标签互换、符号/相位与多态空间还须额外信息。

Eq14对应的简单对角radius-operator图像也有范围：若在unmixed basis中存在不可忽略的off-diagonal E0 matrix element，混合后振幅还会含额外交叉项；多配置时更需full sum。把半径差换成Δβ²还要声明charge-density/deformation模型，不能由标量E0独立恢复三轴性或刚软。**E0未见/很小**也可能是mixing很小、半径差很小、灵敏度/branch限制等，不能据此普遍否定形状结构差别；这为该公式的逻辑边界，不是假定真实数据有其中哪一种原因。

“V=50–100keV必然强mixing”也不成立为一般代数：mixing取决于V与unmixed δ的比值，而不是V的绝对数值；没有δ/状态身份和模型空间不能定mixing fraction。

## 四、非0+、高spin及triaxial情况：不能用0+清单审所有体系

- **PDF13/1479 Eq14旁的odd-Pb讨论/Fig13**明确提到pairs of i13/2 states的E0 components，结合α-hindrance/coupling patterns解释配置混合。**PDF40/1506**更直接要求E0 mapping也应包括J≠0态之间的ΔJ=0 transitions。E0不是只供0+→0+的概念，odd-A/highspin问题也不能要求一定有同核0+ bandheads。
- **PDF12/1478 Fig11/12**将spherical high-J、deformed high-K isomers作为Pb形状共存的指示；Fig11caption甚至把“high-M”纠为“high-J”。此处不是低0+强度单独判定，母态/构型/核矩关联才是信息。
- **PDF29–30/1495–1496 §III.A.8**把highspin SD bands称为dramatic shape coexistence形式；指出绝对Ex/spin及draining links稀少，使其与lowspin框架统一困难。TableII是来自上游实验的SD Qt/寿命综述集合，非本轮新寿命。低spin成员可因dense mixing未被识别；不能用“未观察到0+或E0+Coulex不齐”一刀否决highspin共存候选。
- **PDF27/1493 Fig39与连续正文**的Kr例说明：由2+的spectroscopic Q转intrinsic Q需要K身份；第二2+可能为K=2，K混合显著影响对角E2。原文讨论74Kr的prolate K0/K2与oblate K0以及76Kr的强mixing解释，并强调triaxiality及Kumar–Cline不变量方法。这里的shape/sign解释具有K/混合条件，不是测一个Q号就唯一反演所有βγ。
- 一个triaxial/γ-soft collective family、几个K/声子激发或orientation双极小，不能只因“多态/多峰”就自动等同多个实验刚性shape。此句是本任务将上述结构层次用于三核矩阵的综合边界，不冒作HW11对手征的一条原句。

## 五、旧HW11-D21-1具体数值与量词的归属审核

| 旧认证片段 | 本轮实际原件支撑/检索结果 | 建议 |
|---|---|---|
|186Pb三0+：0/532/650keV|**可定位**：PDF12/1478 Fig12及PDF42/1508 TableVII有532、650(0+3)；这只给能级信息|可保为review所列数据，若论文使用需回上游primary；不推出固定mixing百分比 |
|“V~50–100keV作用下必定强mixing”|未定位该针对186Pb/普适强mixing门；**PDF41/1507 TableVI**实际列多核、不同拟合量的Vmix，从34到400keV均有；192/194Pb的51/52不是186Pb统一值|撤回普适门及该归属；不能把TableVI当同一核/统一测量CI |
|基态约28%变形、激发态20–35%异形杂质|55页native text归一检索未找到这组186Pb百分比；相关Pb连续段和所检模型/Figs6/7/12不提供这些百分比。**Fig13的boxed28是α-decay hindrance factor，非28%mixing fraction**；不声称它就是旧错误的来源|标为unsupported-as-attributed/withdrawn，待具体primary/model/locator才可恢复；负检索不等于证明任何文献都不存在这些数值 |
|ρ²(E0)是排他性物理指纹/唯一辨真实微观形变|Eq14给mixing×半径差的组合；§III.C.2将strongE0列indirect；§III.C.3明确多种数据联合|撤回排他/唯一量词，不抹去E0的真实约束力 |
|必须结合多步Coulex/对角Q才能共存或自洽反演|原文给强互补信息与不同技术路线，且非0/highspin/transfer/核矩例并存|改为按问题与可分辨预测选择互补约束；不能强制两个测量全齐 |

这是一项来源归属/量词审查，**不凭常识宣布所有旧数字物理上不可能**。本轮没有恢复D21旧脚本的自设inputs、没有运行009或任何114，也不以新脚本passed复活它们。

建议leader最小写回：

1. **HW11-D21-1原ID下**明确撤回上述无定位数字/排他硬门认证，保历史/flags；不要只靠别处124短注让active原句可被再次引用。
2. source **HW11-3**的“necessary-companion evidence set”宜改为review给出的互补direct/indirect/hints地图；AR-2中的普适“Require0+”也应限定到实际态/问题，odd/highspin不套0+门。
3. concept旧强段作为已撤回历史显式标出或用有locator的条件性正文替换，不复活50–100keV、ρE0唯一反演。
4. **HW11-4既有needs_review:false不改变。** 本轮提供meanfield→lab/GCM的限定locator，而非重新裁决原用户review。

## 六、对134Pr/135Nd/136Nd矩阵的可写回校准

三核矩阵可保“形状差异/配置改变/混合”竞争路线，但应按同一pair和spin段询问哪些observable真能区分预报。134Pr的解混合Q比是声明假设下的信息；135Nd/136Nd的PES βγ、RMS/3DTAC是模型；它们都不是HW11自动认证的实验多shape。E0、CoulEx E2、radii/Q、transfer或已有absoluteEM可按对象提供不同约束，缺某项降级对应推断，而非给所有核同一资格清单。综述列出的上游例子不增加三核实验独立票。

本轮知识影响为`calibrates-quantifiers-and-retracts-unlocated-certification`：保原源对E0/EM/transfer和形状共存的积极支持，撤回无法归属的百分比/绝对V门与唯一反演。

## 产物/检查

`source-reading.json`保存范围/hash；`claim-ledger.json`区分direct-review、作者观点、条件代数和withdrawal建议；`numeric-locator-search.json`在tmp保存搜索表达式与真实上下文；`artifact-manifest.json`存文件hash。

工具：rg/local PyMuPDF/hashlib、scoped连续原读与上述visual、55页native限定词检索；未联网/下载新来源、未数字化图求CI/新拟合、未修改raw/knowledge/Git。所有实验举例保持review→primary依赖。
