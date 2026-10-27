# Tonev2007 原件再审计 098

结论：**本次已实际找到、复制并读取 26 页 VoR，文件身份、页数、字节数与 canonical SHA 一致；canonical 中多处定位和结论强度需要更正。** 原目录在本次 `ls` 时含 PDF，故起点“文件不存在”现在已不成立。未改 canonical、raw、PLAN、Bib、Git 或课程状态。

## 原件与获取链

- 本地原件：`tmp/day24-tonev2007-134pr-long-095/10.1103_PhysRevC.76.044313.pdf`；独占副本：`tmp/day24-tonev07-reaudit-098/Tonev_2007_PRC76_044313.pdf`。
- 1,527,111 bytes；SHA256 `822780157dadbeac4adfa3cd34b919b855a3911c497c229b2216fb7697f1b8aa`；26 页，印刷页 `044313-1` 至 `044313-26`；标题、DOI、作者和收稿/出版日均由 p1 核实。p1 页脚含 `044313(26)`，不是把预印本页数混入 VoR。
- 095 原目录仅找到 PDF，尚未找到其实际下载命令/HTTP 回执；**本地身份核验不自动认证“APS 官方直接链接取得”的原获取链**。旧 021 worker 的 harvest401/HALmetadata/机构403也不能否定后来得到的真实原件。
- 本次 APS 文章入口 `https://journals.aps.org/prc/abstract/10.1103/PhysRevC.76.044313` 请求 HTTP403 / Just a moment 验证页（5,577 bytes），保存响应与 manifest；未绕过验证、未请求任何凭据。故 SI 为本次入口未能核验，不能把空链接数组写成“该文无SI”。未重新下载已有全文。
- 原件文本逐页保存在独占 tmp；Table II pp12–14 已渲染并肉眼核对列身份，关键带内 E2 数值见本 worker `inband-e2-ledger.json`。此为 Codex self-audit，非 human-reviewed。

## Canonical 逐 claim 审核

| 原ID/事项 | 判定 | 实际原件定位和支持范围 |
|---|---|---|
| 身份、26页、bytes/SHA、反应 | 已核 | p1 abstract/页脚；p2 Sec II：119Sn(19F,4n)134Pr，RDDS87MeV、DSAM83MeV，IReS Vivitron / EUROBALL IV、内BGO、Cologne plunger。 |
| TO07-D24-001 / Table I pp9–11 | 表位置已核，完整性措辞过强 | 真正Table I 为 pp9–11，列为初末态、Eγ、实验/IBFFM/TQPTR Iγ、Pol、γmult。但有空实验格、`Seen`、仅理论行和未见线的上限；39.3keV来自Ref38且未被本实验观察（p8、p11注a）。不等于“全部跃迁都有实验强度和偏振”。 |
| TO07-D24-002 / Table II pp12–14 | 表位置已核，实验覆盖需界定 | 真正Table II pp12–14，确含τ、B(E2)、B(M1)及两模型列；大量态只有理论值，跨带ΔI1实验主要为M1上限而非分离测得E2/M1。p8给τ范围B1 I10–18、B2 I13–17；空格不是零。 |
| TO07-D24-003 / 多极性 | 核心已核；DCO/跨带E2定量部分缺失或过强 | p7 Sec III C（不是Sec II C pp6–8）给Compton方法；p8报告inbandΔI1 M1、E2 negligible，inband/interbandΔI2 E2，interbandΔI1 mixedM1+E2，**统计不足以定interband mixing ratios**。本文未给DCO数表，全文文本未检出DCO。不能将偏振定性指认改写为测得每条混合跃迁E2份额。 |
| TO07-D24-004 / 波函数/排除TQPTR | 几何解释已核，locator与“决定性排除”需改 | Discussion实际为**Sec V**，V A/B p11起；V C 几何算符与分布 pp17–18 Eqs6–13；V D TQPTR p18、Figs8–9；V E IBFFM pp18–22、Figs10–13。Figs6/7为能级比较（pp15/16），不是所称Figs7–9全部角动量分析。实际TQPTR虽EM失败却很好重现能谱/交叉，不能写模型所有表现被排除。 |
| TO07-D24-005 / IBFFM成功 | 主要EM趋势获支持；普遍成功需限定 | V F pp22–25，Fig15 p23、Fig16/17 p24与TableII：支持B1/B2 E2差异、形状涨落洗掉M1交错。但p23最低spin B1大E2不能重现；p23/25 crossingI15不能重现、能隙过大；p25的17_2→15_1 E2异常未复现，16_2→15_1 M1趋势也失败。p11还明确依据本次数据调过Hamiltonian与EM参数，非完全独立无调参预报。 |
| TO07-D24-006 / 作者结论 | 大意已核；节号/定论强度和漏掉的开放项需改 | **VI.CONCLUSIONS p25**（非SecV）：最终原话为study **suggests** weak fluctuation dominated chirality **combined with an intrinsic symmetry yet to be revealed**。p1 abstract确说weak chirality dominated by shape fluctuations；不能据此“彻底澄清物理实质”。 |
| TO07-D24-007 / 两套独立数据 | 同实验谱系已核；独立性断言未获原件支持 | p2直接说present in more detail results of experiments described in Ref20；p26 Ref20为Tonev2006，故2006/2007为同实验详述。本文未说其branch与PE06 Ref11统计独立，也未展示两套独立绝对B值的验证。不能把PE06和Tonev计作两次独立寿命/绝对E2测量。 |

## 实际数值：B(E2)范围与同spin比较

单位均为 e²b²，以下是 **ΔI=2 带内**实验列（Table II pp12–14），不是ΔI1的IBFFM理论E2列：

| 初态I | Band1→I−2 | Band2→I−2 | 中心值B1/B2（本任务算术，无CI） |
|---|---:|---:|---:|
|11|0.268(33)|未给实测|—|
|12|0.198(29)|未给实测|—|
|13|0.151(27)|未给实测|—|
|14|0.153(21)|0.039(19)|3.92|
|15|0.148(21)|0.089(20)|1.66|
|16|0.115(19)|0.050(18)|2.30|
|17|0.108(22)|0.047(17)|2.30|
|18|0.147(27)|未给实测|—|

因此 `.15–.25 / .05–.10` **不能作为全文精确实验包络或逐spin硬界**：B1含0.108、0.115、0.148和0.268，B2含0.039、0.047；带内B2只有I14–17这四个实测E2点。作者概括p23/25为约factor2，2006中2–3倍也只是趋势概括；不能把每一spin当固定比值。完整误差/共同归一协方差未给，故未构造显著性或CI。

需防止另一个列身份错误：p13的 `13_2→11_1=0.0030(5)` 是 **带间** E2；同页 `13_2→11_2` 只有模型值（IBFFM0.000、TQPTR0.160），没有该带内实测值。p24说理论最低点0.0002并不等于新增实测。原表存在一些排印/正文不一致（下述），不静默修原件。

## Wavefunction 和 static chirality 的边界

p17分析的是对几何标量算符本征基的投影分布，不是直接实验测得的β/γ概率。IBFFM的γ为等效三轴转子γeff，p14强调非static geometry，p18强调γ分布是effective γ的分布、β尺度依evib（拟合E2）而定。TQPTR的Figs8/9几何演示还采用特殊参数γ30°/axial、irrotational惯量比，而不是p11能谱比较用的微观惯量比1.52:3.55:1；两者不可混成一套被实验整体判死的参数。

p18：Figs8/9中左右手区域没有良好分离，作者称dynamic chirality为很慢的非谐振动；方向量子涨落即使轴对称也可给非零|σ|。p21：IBFFM与axialSU3比较中有利手征分量的平均增强小于20%；强σ0表示大振幅振动，不能用“存在非零σ”单独认证静态手征。

p21在IBFFM语境下认为两带不同形变、不相同σ分布不符良好分离左右手构型的偶/奇叠加。p2/25作者据所测EM与这两模型判断本核这对带未达到static limit；这是对指定134Pr bands、所测spin范围和模型映射的实质限制，**不是穷尽所有static-chirality模型或所有核素的排他证明**。p23还反驳PE06一项推理：小相互作用强度不必然意味着两带不同形状，TQPTR亦可给sharpcrossing；竞争解释没有被“彻底澄清”。

## 实验谱系与独立性

可建立的依赖图是：

`Tonev2006 PRL寿命/EM短报 ← 同一IReS RDDS/DSAM实验 → Tonev2007 PRC详述/branch/polarization/table`；PRC p2、p8支持，不能按发表两篇计两个采集。

PE06（既有真实原件末页本次重新读取）Ref9是Tonev AIP764p93与PRL96,052501，Ref11是Starosta等to-be-published。它的branch来源与Tonev详述在书目上不同，但PE06的寿命输入仍复用Tonev；PE06的Q比还是依两带混合假定的提取。**可说有不同的branch来源节点，不能说有两套独立τ/绝对B(E2)实验共同确认。** PRC自身没有交付Ref11最终全文身份或独立性声明。其Fig1还注明来自Ref26（Starosta AIP764p77），level-scheme图也不能自动计为全新独立能谱。

## 原件自身的不一致：保留而非替作者校正

- p8描述15_2的DSAMτ为0.897(47)，TableII p13及Tonev2006实际表为0.887(47)；应保留print discrepancy，数值账本采用明确的TableII，并暴露歧义。
- Fig15 p23图面middle标IBFFM、bottom标TQPTR，但caption把middle/bottom模型顺序反写；应以图面标签/TableII/正文核，不按caption一句交换模型。
- Fig15的TQPTR I15带指认已相对2006改动（p23 footnote1），14态近简并混合，带身份有约定性；2006/2007图不能作为未变更的独立模型复现。
- p25“E2理论值均inside experimental bars，except17_2→15_1”等概括与TableII部分具体列关系可能需逐线再核；本审计没有把该概括认证为所有表项都定量一致。

## 建议父任务的最小 canonical 修订

标题/summary改为“134Pr完整实验表与TQPTR/IBFFM比较：支持形状涨落下的动态手征解释及其未解交叉问题”；移除“确立/彻底澄清/决定性排除/两独立数据”的无条件断言。保留真实26页/SHA和正确表页；修正SecsV/VI、Figs8–13/15–17；以逐行E2账本代替固定范围；明示同2006实验谱系、interbandΔI1混合比未定、IBFFM失败项与intrinsic-symmetry未知。这里只给审计建议，未写入canonical。
