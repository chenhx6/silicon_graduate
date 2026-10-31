# Day25 preview：MU08 旧负带 EM 挑战的真实对象

**结论：MU08 的绝对 EM 差异直接挑战的是 2008 年 Band1 与 Band2 互为同一 chiral pair 的解释。** 已核低 spin 谱系为 **Band1→2018 D4，Band2→2018 D3，均负宇称**。它没有测量后来新弱带 D4-C/D3-C 的 τ，也不涉及正宇称 D5 的 τ；因此不能直接否定 D4/D4-C、D3/D3-C 或 D5/D5-C 新配对。旧实验本身精确而有信息，作者也明确保留各配置上未来可能观察到 chiral vibration 的路径。

本轮重核与既有 MU08-D18-5/6/7、PE18-D20-R146 边界一致，判作 **verified no-op for existing scientific claims**。新增交付只是 pair-resolved 的 Day25 比较行和同母态 ledger；不制造新实验 delta、不恢复已撤回的 positive D1/D2 桥接或普适排除。

## 身份、原件与阅读

S. Mukhopadhyay et al., *Electromagnetic transition rates in high-spin bands in136Nd*, **PRC78,034311(2008)**，DOI **10.1103/PhysRevC.78.034311**，实际 PDF 标 published17September2008。

原件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf`；6页、171233bytes，SHA256 **ea77d7d033051369d19aad2f82a542e91e262eb490d518b246f7f04c2d0dcd2c**。官方 DOI/PDF入口 `https://journals.aps.org/prc/pdf/10.1103/PhysRevC.78.034311`；本轮直接读已有 raw，没有联网重复获取。

阅读：全文6页、全部Figs1–5/TablesI–II/Eqs1–3；关键PDF2–5全部视觉核查。另只定向读 PE18 canonical **PDF3 Fig1** 做级联指纹核对，其SHA256 **d2615fc0d95428b06c056eb8946afa2f62940ce58d79c1fc1cc3f50e19c73ef3**；不冒称新读完整PE18。`active-recall.md`在本轮body前冻结，明确受Wiki priming、不评分。没有运行114、作者程序、旧反演或新的寿命fit。

## Run / family / parent / branch / clock 分开

| 对象 | 原件可确认的合同 | Locator |
|---|---|---|
|采集记录|ATLAS175MeV40Ar+100Mo(4n)；1.14mg/cm²富集靶，17.9mg/cm²Pb backing；约2.5×10^9 fold≥5事件，100个Gammasphere Compton-suppressed HPGe|034311-1|
|Run身份边界|论文没有提供可核的原run/event UUID；这里用paper+beam/target/campaign描述，不把新阅读或不同发表年份计新采集|全文scope|
|Family|原Band1/Band2是两条negative-parity序列；相连且I≈17附近最近接近/交叉。不是2018positive D1/D2|034311-1/2Fig1|
|Parent|TablesI–II覆盖各带I15−–19−，共10个母态；TableI共26条打印分支，按Ex/Jπ绑定|034311-3TableI；-4TableII|
|Branch|本文自己提取branch，称旧Refs17/18无该信息；各母态打印中心归一为1，但未明确photon/total-transition/IC分母|034311-3TableI及左栏|
|Clock|DSAM line shape是在靶/背衬减速时采样的level lifetime；不是TDPAD长寿命异能态或另一campaign的时钟|034311-1–3|
|Fit合同|BLUE分角双门；门在目标以下，未停止峰每ring覆盖完整stopped+shifted；LINESHAPE5000 recoil histories、0.002ps步长、SRIM电子阻停；五步side-feeding且Qs可变，逐级加入至globalfit|034311-2/3Fig2|
|误差/成分|quoted errors不含可达15%的stopping systematic；ΔI1绝对B(M1)提取假设pure M1，不等测得δ=0；τ/branch/Cov/ICC未完整公开|034311-3；-4TableIIcaption；-5Fig4caption|

175MeV的其它核/发表是否共享同一event pool，不能仅由共同beam/setup与引用自动认证；本文对象是4n的136Nd。与2018的152MeV JUROGAM谱学是不同采集/响应。跨源同核不意味着同门、同parent normalization或相同误差协方差。

## 逐态实表核对

以下均为作者报告，不是新fit；B、Qt从同τ/branch派生，不计三份独立观测。完整26分支和10母态见 `parent-branch-clock-ledger.json`。

| Old band / later low-spin family | Iπ | Ex keV | τ ps | B(M1) μN² | B(E2) e²b² | 主带内ΔI1 γ keV |
|---|---|---|---|---|---|---|
|1 / D4|15−|5645.3|.93(9)|2.7(3)|—|229.3|
|1 / D4|16−|5954.0|.88(10)|1.7(2)|.26(3)|308.7|
|1 / D4|17−|6310.2|.71(6)|1.1(1)|.08(1)|356.2|
|1 / D4|18−|6711.4|.56(8)|.9(2)|.14(2)|401.2|
|1 / D4|19−|7147.2|.32(5)|1.7(3)|.11(2)|435.8|
|2 / D3|15−|5729.3|1.27(6)|4.4(3)|.54(8)|199.6|
|2 / D3|16−|5977.4|.87(8)|3.5(3)|.51(7)|248.1|
|2 / D3|17−|6321.8|.61(7)|1.4(2)|.44(6)|344.4|
|2 / D3|18−|6756.0|.51(7)|1.0(2)|.04(1)|434.2|
|2 / D3|19−|7221.5|.31(5)|1.6(3)|.05(1)|465.5|

例：Band1 Ex6711.4,I18−的完整打印出射分支是401.2→17−、757.4→16−、389.6→17−，branch分别.57(6)/.24(2)/.19(2)。前两条常用于M1/E2对照，但不能删除第三条再把前两条归一为1。Band2 Ex6756,I18−的434.2/778.6/445.8分支为.73(7)/.08(1)/.19(2)。这些**旧parent**不包含后来C弱带的母态。

既有局部边界核实保持：Fig2把Band2谱例写464.8，TableI相应19−→18−为465.5，Fig1约465；不指定哪个字段应改。TableII Band1 I15的E2/Qt空白，不补零。本文文字“B(E2) always differ by factors2–3”并非逐态严格界：I17中心比.44/.08=5.5，I18逆比.14/.04=3.5；用逐态表，不用该prose作全域范围。所有中心比均非新增joint显著性或普适反证门限。

## 与2018的对应限于已核级联

原Fig1/TableI与PE18 Fig1给出低spin指纹：

- **Band1→D4：**229.3/308.7/356.2/401.2/435.8对应2018图约230/309/357/402/436。
- **Band2→D3：**199.6/248.1/344.4/434.2/465.5对应约200/249/345/434/466。

这足以支持旧主带的有限区间谱系；2018能量有修订，图不列完整绝对Ex且D3高spin拓扑重排，所以不把旧Ex/τ一键搬到全域。**D3-chiral与D4-chiral是另加的弱序列**，不是给旧Band2/Band1换一个名字；旧两带之间的绝对B差异不等于各自与新C伙伴的B差异。

## 作者解释、TAC/RPA与实验的界线

**实测/派生结果：** 两负带能谱近简并且有强links；但EM不同，尤其E2随spin的差异与方向改变。作者将其作为反对旧两带互为chiral pair的直接电磁证据。寿命/branch与pure-mode假设的精度合同保留，不因输入账本未全恢复就把发表结果视为不存在。

**作者解释：** 引入两个不同配置及交叉附近的mixing；两带低位decay-out不同、links主要集中于交叉区也支持该路线（034311-1/4/5）。这不是由EM数据唯一测得每个occupation或mixing矩阵元。

**模型：** QQ TAC在N=4/5壳；κ0=.036MeV、quenching参数B=.5沿用能描述135Nd的数据选择；忽略pairing；TAC minima ε2≈.23–.25、γ≈25–30°。比较πh11/2²⊗νh11/2d3/2与πh11/2g7/2⊗νh11/2²，能量趋势尚可，但交叉位置对single-particle/deformation细节敏感。**计算没有band mixing**，作者明确说交叉区不能期待详细rate一致（034311-4/5）。模型只是解释支持，不能改称已完全重放crossing动力学。

**RPA范围：** 小振幅harmonic、well before static transition；存在noncollective solutions，πh11/2g7/2⊗νh11/2²的collective strength在hbarω=.35MeV附近碎裂。Fig5的collective模式典型100–400keV，作者据quadrupole transition matrix解释为shape相对J的reorientation/chiral vibration。最后总结明确：**两个配置各可有chiral vibration，未来在136Nd观察chirality的可能仍开放**。不能从旧mutual-pair失败推成全核永久无chirality。

2008与2018的模型配置描述也不是同一producer：PE18对D/D*按具体阻塞/Ω与新配置空间讨论，不应把2008不同occupation的最佳TAC替代解释直接充当2018的已测微观起因。

## 新Day25 comparison row：反证对象必须以pair定义

| 待检对象 | MU08能直接贡献什么 | 不能贡献什么 | 当前比较措辞 |
|---|---|---|---|
|**Old Band1 vs Band2（later D4 vs D3）**|匹配旧母态的DSAM、branch与明显不同absoluteE2；直接挑战这两条序列互为理想partner的旧解释|不唯一测得mixing参数、shape差或排除一切振动；不提供完整signedEM/actualCov|**旧互配解释受真实EM挑战，crossing/configuration路线获条件支持**|
|**2018 D3 vs D3-C**|D3旧主带在有限spin可有τ/EM anchor；可约束任何采用同主带的后续模型|没有D3-C的τ/absoluteEM，旧D4不能替D3-C|**主带有旧EM；新伙伴EM缺失，旧跨主带差异不是该pair直接反证**|
|**2018 D4 vs D4-C**|D4旧主带同上；新的成对预测须兼容旧主带数据|没有D4-Cτ/absoluteEM，旧D3不能替D4-C|**同上，按该新pair保留支持/缺项，不宣称已测不相等**|
|**2018 positive D5 vs D5-C**|方法学警示：能谱相似须加EM；为设计提供祖例|不同parity/configuration/parent；不能迁移任何MU08τ/B或负带挑战|**D5双方ratio的真实支持保持；ratio不等absoluteEM，但旧负带不是其直接反证**|
|**2018 positive D1/D2**|无旧band identity桥接；仅一般方法教训|旧被撤回positive映射不得恢复|**无对应旧τ/absoluteB，不能套2.06倍等旧错误结论**|

新的comparison row只把既有更正变成可复用的pair-level测试合同，不是新科学delta。对新pair的最小下一观测是**在已绑定同I/Jπ/parent的弱C伙伴上测τ与component-resolved完整branches**；原主带旧数据可作为约束，但需明确跨campaign响应/normalizer关系。对positiveD5，优先补双方absoluteEM及独立configuration/shape companion，不借旧负带时钟。

## 给leader的写回建议和状态

- 若只需科学claims，可标 **verified no-op**：MU08-D18-5/6/7及PE18-R146已经正确覆盖关键结果与身份。
- 新增可复用设计句（needs_review:true）：**“MU08挑战的是旧D4/D3互配；它可约束新D4/D4-C、D3/D3-C的主带，但未测新伙伴，不能直接给新pair不等强反证。positiveD5有自己ratio支持，旧negativeτ不能跨family移植。”** 类型为cross-source synthesis，不是原文直接结论。
- 保留实验真实精度与TAC/RPA域；旧普适证伪、固定2.06差、正D1/D2桥接和114相关撤回均不恢复。

`receipt.json`记录实际hash/URL/阅读范围；`parent-branch-clock-ledger.json`是当前直接原读的10母态/26分支转录，不是新fit或新独立实验。只写assigned worker与`tmp/day24-nd136-old-em-024/`。canonical/raw/PLAN/Bib/Git、session/课程信用不变；仍sameDay24 run的Day25 preview，credit0，未读Day26。
