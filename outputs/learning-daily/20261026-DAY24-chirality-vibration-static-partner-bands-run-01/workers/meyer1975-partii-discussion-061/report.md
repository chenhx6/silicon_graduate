# 061：PartII如何由谱学讨论PES，以及结论为何仍是定性

**原文支持的是：指定single-j/芯参数模型下，多个odd-A谱对γ有相当一致的偏好；它没有把这些拟合γ直接测成γ波函数宽度、PES曲率或严格刚性。** 作者在讨论开头说把rigid shape照字面理解会是naive，在结尾明确“no quantitative conclusion can be drawn”。这些不是本任务追加的保守措辞。

## 文件、primed recall与实际scope

J. Meyer-ter-Vehn, *Collective model description of transitional odd-A nuclei (II). Comparison with unique parity states of nuclei in the A=135 and A=190 mass regions*, NPA249(1975)141–165，DOI `10.1016/0375-9474(75)90096-2`。已有真body：`tmp/day24-meyer1975-partii-entry-057/attachment-object-response.pdf`，本轮pdfinfo/hash确认**25页1368683bytes**，SHA `fd1ba7f9280e8bafd86bbec06ec18e8a7089f93e84306829a4be897d9dd8439d`。physicalPDF页+140=printed页。本单元没有新下载/网络或复制raw。

读原件前先写`primed-recall.md`，明示已有PartI的方法知识，预期不算PartII事实。本轮**连续精读PDF20–25/printed160–165**，即§4主体/PES、§5结论及全部44条references；为接完整§4开头与具体限制，另定向读**PDF1–2和PDF18–19**（前后context，不冒全文）。这十页均text+fresh整页视觉；全文text仅用于定位coexistence/limits，不算全部25页阅读。主scope视觉：**Fig10、Tables6–7**；必要context又核**Figs8–9**及PDF18–19相邻段。没有独立复核前面Tables1–5/Figs1–7或所有引用primary。

## 先核预期：哪些成立，哪些需要修正

- “用谱学而非直接密度测量推形状”成立，但本文不主张直接对odd-A谱作不受限best fit：PDF2说忽略项使这种best fit目前不适当，优先从邻偶核定参数；“essentially parameter-free”是这个条件下的作者用语，不是模型没有经验输入/选择。
- “rigid成功不直接测刚性”被原文明确支持。PDF19–20开头承认soft/fluctuating shapes，讨论只给qualitative answer。
- 预期需要查shape coexistence，结果是：摘要“coexistence”实际指**ΔI=2与ΔI=1 band structures同时出现**，并以同一三轴shape asymmetry解释；不是宣称观测到同核两个不同shape。Fig10也只是四种PES类型示意，不能改成某核两个well的实测证据。

## Fig10：是解释框架，没有本篇新算的逐核PES

PDF20/160图注明确“Schematic potential-energy surfaces for different types of nuclei”。四类分别是harmonic vibrator、深prolate minimum、γ valley型soft PES、triaxial区域有clear minimum的PES。作者假定低激发collective motion由quadrupole自由度主导，然后用这些图讨论softness；不是由这四幅示意反演出目标核PES，更不是计算了Ce的collective mass或波函数。

PDF21先说既有A190/A135的microscopic PES（Refs33–35）没有明显triaxial minima，**随页脚又保Ref36的近期例外**：N=76、56≤Z≤66一些triaxial minima较明显。不能把正文概括剪成“所有microscopic PES都无三轴min”。本轮只是读到该转引，未原读Refs33–36，也不将其当新的136Nd实验或本篇PES。

## Table6：排的是完全γ独立极限，不是所有γ软度

PDF21/161用Wilets–Jean（Ref37）的**complete γ-independent**极限作检验：2₂⁺与4₁⁺、3₁⁺与4₂⁺应同时degenerate。源说该极限不依β势的具体形状；应限所引collective model，不扩大成任意γ-dependent kinetic/mass条件下只要V平就有同样谱。

原表两个量是

\[
r_1=E(2_2^+)/E(4_1^+),\qquad
r_2={E(4_2^+)-E(2_2^+)\over E(3_1^+)-E(2_2^+)}.
\]

| 情形 | r1 | r2 | 原表身份 |
|---|---:|---:|---|
|complete γ-soft|1|1|理论极限|
|rigid triaxial rotor γ22.2°|1|2.73|另一理论点|
|190Os|1.02|2.01|所引实验Ref13|
|124Xe|.96|1.47|所引实验Ref42|

作者据此说complete softness不符，同时明确**rigid-triaxial limit也未达到**，解释成波函数既非sharp localized也非均匀铺满γ valley、可能有有限spread。该spread判断是**作者在这两个model limits之间的解释**，不是本表测出了σγ或唯一PES。表无joint errors/原能级输入，本轮不加显著性、CI或以比值距离给γ分布宽度；两比同用E2₂还共享输入，不是两份独立实验。

Refs38–39的anharmonic-vibrator低能fit得到“empirical PES”也只是被本文引用的模型反演，不是直接测得的potential或本轮独立复算。

## Table7：dynamic rms与effective fitγ要分开

PDF22/162引用Ref33的calculated PES及βγ动力学，给state-dependent rms量；同时列本文选定的standard β/γ。

| 列/态 | βrms | γrms(deg) |
|---|---:|---:|
|186Os，0₁⁺|.223|23.2|
|186Os，2₁⁺|.230|21.1|
|186Os，4₁⁺|.239|19.6|
|186Os，2₂⁺|.226|33.4|
|196Pt，0₁⁺|.154|36.2|
|196Pt，2₁⁺|.168|38.9|
|196Pt，4₁⁺|.181|40.5|
|196Pt，2₂⁺|.173|31.2|

本文standard列为**186Os β.23/γ16°**及原header明确的**196Hg β.13/γ37°**。右侧dynamic列是196Pt，standard列是196Hg；**不擅修成同核，不将二者作严格同核精度对照**。表中rms是Ref33的计算输出，standardγ是本模型参数；没有原动态波函数/定义，不能把二者等同、相减成实测shape fluctuation或把fitγ当rms/width。

作者认为very soft PES会让各odd-A态及相邻芯的effectiveγ大变，但Au的h11/2与Tl的h9/2谱都指向约37°，与Hg芯在约±2°内一致，因此不愿只归于odd-particle stabilization，倾向Hg芯本身比所引PES更不软、可能有triaxial minimum。其后明确说Os、Pt和A135的证据**弱于Hg**。

这些是作者通过指定谱模型作的排他程度有限的推论。**±2°不是实验统计CI、不是波函数σγ、不是PES谷宽。** PDF23结论195Au/137Nd再说“within ±2° or so”，PDF24立刻限定仍不能作quantitative conclusion；两句需同存。

PDF22进一步明确真正定量需odd particle耦合parameterized anharmonic vibrator或至少β固定/γ可动的soft vibrator，fit experiment；**作者当时没有这种计算结果**。PDF23又说已有spherical particle–phonon研究主要non-unique parity，不能直接比本unique-parity family；Alaga三粒子/空穴cluster+phonon比较还待数据/计算，本文未完成替代路线胜负。

## 模型的pairing、单j与“高spin”范围

必要context PDF1–2/141–142直说固定βγ只是近似，低激发family指**约2Δ以下**；涉及较高I不等模型已覆盖3qp破对。遗漏项包括β/γ波动（整体压缩谱/改EM）、Coriolis attenuation、odd particle改变core参数、pair blocking、其它j壳及3或更多qp混合。非unique-parity同宇称多个j近Fermi的系统mixed-j比较未做；因此不把本篇模型稳定γ结论泛给所有Ce组态。

对实际133Ce，PDF18–19 §3.2.4/Fig9提供**源内失败例**：triaxial β.22/γ23°比轴向β.19/γ0°整体谱好，但最低9/2仍未下降够；作者没有加ad hoc Coriolis attenuation，因为会模糊模型物理，也说selfconsistent惯量的处理如何推广到三转轴仍open。这不是“triaxial计算完全再现Ce”。Fig9打印的\(\widetilde\lambda_F=1.0\)、Δ1MeV、相对11/2参考等也不填WK22 actual negative-parity λ/header。本单元没有重审所有Fig9能量/transition行，只核该failure及caption/参数范围。

PDF18上半137Nd也保不相容：某些高激发level/branch不符合h11/2模型，作者提出f7/2或h9/2替代并要求更多实验。这是依据energy+decay network作有限assignment推断，不是测定配置，也不是给实际135Nd三qp解释。未造任意“spin超过I0失效”的数值界限。

## source independence与可执行crosscheck

PartII是PartI同一作者/同一模型的应用，不是独立实验。odd-A spectra取已有heavy-ion/β-decay资料，邻偶芯数据又用于参数；同一图中多态与同一源的后续report不可按独立实验计数。Table6两核的实验来源分别Ref13/42，Table7 rms为Ref33计算；Gneuss/Greiner与Habs empirical PES、Refs33–36 microscopic PES和本作者interpretation需分层。PDF24明确187Ir数据含发表前Grenoble–Swierk通讯并经许可使用，不能把本文理论paper标新独立采集。

可行的下一真实crosscheck（本轮**未执行**，不假造输入）：

1. 回Ref13/42或匹配评估记录，核190Os/124Xe四个Table6 endpoint能量/assignment、版本及error/correlation，再复算r1/r2；检验的是complete Wilets–Jean极限，不直接推出rigidity或唯一PES。
2. 回Ref33取得同核dynamic Hamiltonian/metric与γrms定义；明确Table7的196Pt/196Hg差异及fitγ口径后，才比较same-nucleus E2、静态Q、collective wavefunction分布。本文表不能补波函数或势曲率。
3. 固定同一data/β/λ/惯量与算符，实际做rigid-core对βγ-dynamic core的联合held-out EM/energy比较；作者尚未做这一quantitative alternative，当前无producer/数据不声称路线已完成。
4. 对本133Ce负谱先回Fig9引用的Refs26–27（NPA2221974p557与Nashville1974proceedingsp154）固定9/2及11/2等能量基准和links，再连接现代数据；不由图中的模型λ或拟合γ替代WK22执行字段。

所有计划只列可取的真实对象，没有新下载、fit、假counts/δ/τ或模型CI。

## belief revision与写回建议

supports：PartII实际把多个odd-A谱和邻偶芯放到同一个可解释模型比较，并给有限γ稳定性的线索；不是只有参数名。limits：模型好谱不能照字面认rigid，Table6既非complete soft也非rigid极限，Table7不把rms与fit当同量，定量dynamic-core测试仍未完成。revises：任何“同谱定γ±2°即测得刚性/谷宽”“摘要coexistence就是两shape”“所有microscopic PES都无triaxial minimum”的读法需收回。

可复用事实及原子候选在`claim-ledger.json`，由root按证据类型写回knowledge；本worker不改canonical/raw/PLAN/Bib/Git/信用/session。仍sameDay24＋恰好Day25未计分预习，不开下一课程卡。
