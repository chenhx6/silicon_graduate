---
type: research-note
title: "A≈60：绝对E2、条件形状混合与高自旋取向的连接边界"
aliases: [A60 collectivity and orientation transfer, G26 A60 foundations]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [doctoral-r1-g26-crider-2016-68ni-shape-coexistence, doctoral-r1-g26-starosta-2007-64ge-rdm-e2, ding-2025-chiral-rotation-a60-residual-interactions, campaign-g04-idoko-2025-69ga-highspin, poves-2020-limits-assigning-nuclear-shape]
created_from: "G26研读；总控原件Table/Fig复核后重建"
promotion_target: ""
tags: [a60, shape-coexistence, gamma-softness, two-state-mixing, e0, doctoral-foundations]
---

# 轻质量区并不是一个统一的“软核芯”

## Research Trigger

64Ge和68Ni分别提供非谐集体描述与构型混合的重要实验入口。
它们与高自旋取向候选之间可以比较机制，不能用一个核的低自旋测量代替另一个核的核芯输入。
本页主要推进两份实验原件的理解；Ding/69Ga高自旋资料沿用既有source边界，
不在这里重新虚构一套Co/Ni组态、角度或实验窗口。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 64Ge两态寿命τ=3.3(5)、8⁺⁴₋₂ps；向下B(E2)为410(60)、620(210)、1.5(5)e²fm⁴ | [[doctoral-r1-g26-starosta-2007-64ge-rdm-e2]]，PDF3 Table I及其左右正文 | 本文RDM与采用分支/能级信息的联合抽取；总控核原表 | τ为平均寿命，三条B依次2₁→0₁、2₂→2₁、2₂→0₁；不是独立的三次寿命实验 |
| 同表GXPF1A预测跨带B=14，Qs(2₁)=−18.6、Qs(2₂)=+18.5efm² | 同上，Table I的th.列 | 模型，ep=1.5e/en=0.5e，pf空间16空穴 | 不是测得的静态矩；弱跨带预测明显偏大，不能只报道吻合项 |
| 68Ni首次观测430keV弱分支，BR=0.12(3)%；0₃半衰期0.57(5)ns | [[doctoral-r1-g26-crider-2016-68ni-shape-coexistence]]，PDF2/printed109、PDF4 Table1/Fig3 | 两项相关但不同实验；总控回读PDF2–5 | 寿命实验用像素快塑闪+LaBr3/SeGA，分支实验另用GeDSSD+SeGA |
| B(2₁→0₁)=52.5(84)、B(2₁→0₂)=147(46)e²fm⁴；ρ²(E0)=0.0076(4) | 同上，PDF3–4，Table1、Fig3 | 本次分支结合既有2₁寿命；E0/0₂半衰期采用Ref10 | 不把采用量算作本篇新测；0₂能量1604keV，非旧草稿的1770keV |
| cos²θ=0.74(7)、半径差0.17(2)fm²、内禀\|Q₀\|=93(5)efm² | 同上，PDF3/printed110两态模型段 | 作者条件模型抽取 | 混合、半径差和轴向Q₀不是三项独立直接观测；符号未由该绝对值决定 |

64Ge原件SHA为`715a4c8ada9a6e4bcc2be1df8c845e680d81b6f0c4f91bf70931fe7b10592ad8`；
Crider原件为`923ce537b505cecd49cdf75901bdd1be76896da0326ce29e8b049f10143d4b28`。
读取范围按对应source；总控本轮独立核64Ge PDF2–3与Crider PDF2–5。

## Provisional Reasoning

### 1. 先看怎样测到绝对量

Starosta实验利用单中子敲出和中能RDM，62Zn作为检验：提取τ=4.2(7)ps，
与引用值4.2(3)ps一致。64Ge的2₂→2₁喂居约30%，在寿命拟合中处理；
约40%的观测激发来自减速箔反应，也进入该实验的线形计算。
这些比例属于该设置，不能变成其它RDM实验的默认修正。
主靶在原文是500μm natC，减速箔为250μm93Nb，不能误写成9Be反应靶。

Crider对68Ni的0₃→2₁的478keV线作时间谱拟合；对430keV弱线的分支测量
来自另一次能识别0₂退激信号的实验。原文还用68Zn短寿命态检验prompt响应、
以70Ni已知6⁺寿命作一致性检查。短寿命采用值与本篇新测结果必须区分。

### 2. 两态模型到底假设了什么

以下为条件推导，非实验恒等式。假设0⁺空间用正交基\(|s\rangle,|d\rangle\)近似，
\(\epsilon_d>\epsilon_s\)，相位选\(V>0\)，
\[
H=\begin{pmatrix}\epsilon_s&V\\V&\epsilon_d\end{pmatrix},\quad
|L\rangle=\cos\theta|s\rangle-\sin\theta|d\rangle,\quad
|U\rangle=\sin\theta|s\rangle+\cos\theta|d\rangle.
\]
于是\(\tan2\theta=2V/(\epsilon_d-\epsilon_s)\)，
\(\Delta E=\sqrt{(\epsilon_d-\epsilon_s)^2+4V^2}\)。
再假设2₁主要连到d基矢、到s的未混合E2可忽略，则
\[
\frac{B(E2;2_1\to L)}{B(E2;2_1\to U)}=\tan^2\theta.
\]
代入52.5/147的中心值得\(\cos^2\theta\simeq0.737\)，与作者0.74(7)一致。
误差依赖共享寿命/分支；本页没有恢复完整Cov，不另造更精确误差。
如果2₁本身明显混合或交叉E2不小，这个抽取需扩展。

用\(F=\sum_pr_p^2\)（单位fm²），定义\(\rho(E0)=\langle L|F|U\rangle/R_0^2\)。
在未混合F交叉项可忽略时，
\[
\rho^2(E0)=\frac{Z^2}{R_0^4}\sin^2\theta\cos^2\theta
[\Delta\langle r^2\rangle]^2.
\]
单体算符并不在任意构型基底自动对角；这里的忽略是模型假设。
原文按此得到半径差0.17(2)fm²。
强E0同时涉及混合与半径差，不能单独读为“形变很大”或“势垒很低”。
轴向、锐面及小形变展开还可连接半径差和β²差，但那是另一步模型映射。
0⁺谱学静态Qs恒为零，不能直接测其“正负Qs”。

### 3. 哪些解释仍在竞争

64Ge实测能量/强度与GXPF1A及非谐集体图像有多项相容之处，
作者讨论大振幅四极运动和反号Qs；但Qs在此是理论预言，且弱跨带强度未被定量再现。
它不证明所有N=Z核势面都平坦，也不确定全部γ概率分布。

68Ni中不同0⁺与组态的关联受模型空间影响：Crider PDF3–4明确比较是否允许
质子跨Z=28激发；0₃能量及半衰期对模型有区分力。
实测0₃半衰期0.57(5)ns，而文中引用A3DA与LNPS预测分别108ns和1.5ns，
说明再现能级不等于解释所有EM。该预测比较为2016原文记录，不认证2026全部模型现状。
基态“球形”不能理解为无四极涨落；[[poves-2020-limits-assigning-nuclear-shape]]
用同一核说明内禀形状局域程度需另看高阶矩，不能从闭壳名称断定。

## Assumptions

- 两态截断、2₁组态和未混合E2/E0交叉项都是假设；ρ²上限不独立证明所有混合很弱。
- 所有跃迁方向、平均寿命τ与半衰期t₁/₂按原文保留。
- 内禀Q与β不是探测器直接读数；实验室0⁺密度与内禀分布分开。
- 此处核心原读是两个低自旋实验；高自旋机制回[[ding-2025-chiral-rotation-a60-residual-interactions]]
  和[[campaign-g04-idoko-2025-69ga-highspin]]的已有核查，不借本页添精确参数。

## Competing Explanations

离散构型混合、连续β–γ波动、有效算符及模型空间截断可以影响相同E2/E0信息。
高自旋能谱近简并还可能响应残余相互作用而非取向几何相同变化。
不同核与不同态不共用一个“轻核软芯”参数；低自旋实验不直接裁决另一核的手征性。

## Transfer Conditions

跨区迁移应对齐组态、自旋、探针、有效相互作用及电荷/质量映射。
稳定Qₜ只支持特定转子表示下带内E2幅度稳定，不能唯一证明势阱不变；
Qₜ下降也可能涉及混合、顺排或实验系统误差，需共同模型比较。
高阶形状矩与角分布的关系按[[doctoral-r1-t03-shape-invariants-and-softness-20261108]]处理，
不能仅从q₂/q₃或幅度方差直接给无权γ方差。

## Failure Conditions

两态不再支配、未混合交叉项不小、态身份/跃迁方向错误、共享Cov缺失却报高显著性，
或把低自旋结论外推整区，均须扩展模型或撤回相应抽取。

## Falsification or Reverse Tests

在共同模型中预测未拟合的2⁺对角矩、其它带间绝对E2及E0，而不只复算拟合比值。
64Ge两个Qs的符号是可检验的具体模型输出，反号不是所有非谐振子的普适定理。
68Ni还可比较允许/限制质子跨壳空间对0₃寿命的预言；不以单个Qs符号独立指认整个0⁺形状。

## Open Questions

- **idea：** 跨区比较残余质中耦合相对集体能标的大小，能否解释取向谱与能谱不同敏感性？
  assumption为同一可比有效相互作用/算符空间；不能预设简单A⁻¹或A⁻¹ᐟ³径向稀释定律。
  prediction由共同输入模型先给，竞争解释为占据、惯量与核芯极化；
  若只匹配能谱而留出EM区分不了，则保留不可识别。
- **idea：** 同一组态的跨壳重排是否同时改变E0混合与可允许八极轨道的可用性？
  必须独立检查宇称、Δj三角条件和占据。E0强度本身不能预言E3；
  p₁/₂–g₉/₂单粒子rank3因Δj=4禁止。
  竞争解释为标量混合与八极相干依赖不同矩阵元；
  需同一Hamiltonian预测E0、E2、E3后比较未拟合分支，无相关时结束该路线。
- 本轮未穷尽所有轻核与后续实验，以上仅为文献启发的候选，不宣称新模式或全球新颖。

## Human Review

- Review scope: G26研读与总控原件复核/重写，未发生用户逐项审阅。
- Decision: provisional；科学使用依据直接证据及条件。
- Complete unresolved P0/P1 inventory: 未发现原件身份P0；P1为完整Cov、
  扩展组态混合与高自旋共同模型尚未完成，不自动转为用户待办。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 总控核表重建 | worker draft | provisional | 更正0₂能量/装置、移除未核高自旋数字与普适软度判据，保持实测/模型/采用量的依赖 | doctoral-nuclear-structure-foundations |
