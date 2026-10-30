# Larsson–Leander–Ragnarsson1978：应用、失败与133Ce输入合同

**主要方法教训：** 这些应用展示了core–quasiparticle耦合的实际解释力，也直接显示“能谱拟合→唯一shape/configuration”推断的边界。185Re需要奇核本身的参数调整；75/77Se的低能谱改善并未带来全域EM/惯量/两宇称能量的一致再现；示意高j算例中，γ、ε4、跨壳j-mixing和pairing/Fermi位置可以通过不同机制产生相似谱变化。对133Ce应迁移的是**输入、空间与未定标观测的核验合同**，不迁移本篇其它核的参数或实验结论。

## 原件与分工范围

S.E.Larsson, G.Leander and I.Ragnarsson, *Nuclear core-quasiparticle coupling*, Nuclear Physics A307(1978)189–223，DOI10.1016/0375-9474(78)90613-9。

用户提供原件 `raw/papers/1-s2.0-0375947478906139-main.pdf`：35页，SHA256 **108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb** 已重新核实。本轮不联网、不更改raw。

**本worker实际范围：PDF11–31/printed199–219**，§3Applications全部（3.1、3.2、3.3.1–3.3.3）和§4Conclusion。PDF11开头仍属§2尾，属root/032方法分工，不另声称此worker重核§2。全部 **Figs3–10、Tables2–5、Eqs18–22** 已核；figure/table与关键推导视觉页为PDF12/13/15–25/28–31。其余连续页文字全文读。本文引用的实验论文未逐篇重新取得，不增加独立实验核验次数。

这与032方法/Appendix及root scope可拼成正文阅读链，但须由leader做scope reconciliation；**本报告不声称全文数值复现、代码/作者producer恢复或所有被引实验独立核实**。

## 3.1：185Re 的支持与实际定标

对象是 **185Re positive-parity hole spectrum**，不是185Au/187Au。PDF11/printed199说明其单粒子轨道用“A=187”modified-oscillator参数；这只是参数组标签，不能把核素变成187Au。耦合空间含prolateZ=76gap以下六个positive-parityorbitals。

| 层次 | 原件信息 | Locator |
|---|---|---|
|偶芯先验|186Os core的近似 ε=.20、ε4=.06、γ16°、E(2+)=137keV 来自既有计算/实验|PDF11/199 §3.1|
|奇核调整|按185Re groundstatequadrupolemoment、groundbandinertia及[4111/2]bandhead位置，实际改用 **ε=.25、ε4=.08、γ15°、E(2+)=115keV**；ξ=1，没有Coriolisattenuation|同段；Fig4/PDF13|
|真实支持|低位positive-hole谱与decays总体较好；Table2列Qtheory2.30 vs exp2.36eb，μ2.86 vs3.17n.m.，其它E2/δ有相容实例|PDF13/201 Fig4/Table2|
|非holdout部分|Q和groundbandspacing参与选参，因此不能把它们再当完全独立无参预测。原文没有预先冻结train/test或参数联合CI|PDF11/13；本任务解释边界|
|缺失预测带|理论另有predominantK=7/2的低带未见；作者提出strongM1side-feeding可削弱cascade/population作为可能原因，不是实测证明或有效上限|PDF14/202首段；Fig4caption|

作者明确仍可细调γ/E2参数改善（PDF14举γ14.7°、E2=115.5keV）。因此该应用说明有限合理输入可以获得有用描述，**不说明偶芯参数可原样移入奇核，或一个成功谱固定了唯一shape**。把不见的理论带自动判“不存在/排除”也不受这段支持。

## 3.2：75/77Se 参数、成功与明确失败

### 定标不是独立形状测量

PDF15/printed203给出：A=70单粒子参数；BCS窗口为Fermi上下各约 **sqrt(5N)个levels**，pairingstrength依Eq18选择，使平均gap接近 **12/sqrt(A)MeV**；ε=.29（参考B(E2)、散射和势面），ε4=0。particle空间取靠近Fermi的 **五个positive、四个negativeparity轨道**。

惯量参数按奇核groundband最初几个excitedstates间隔调整。positive谱因Fermi位于g9/2中部对γ不敏感，作者改用最低三四个negative-parity态的次序/间隔选 **γ35°(75Se)、30°(77Se)**，再用于positive谱；75SepositiveHamiltonian还需 **ξ=.85** 才得到5/2+groundstate，余情形ξ=1（PDF15）。

这些γ是**在具体空间/BCS/惯量/attentuation模型内由低能谱选出的参数**；不附模型无关误差或γrigidity测量。positive/negative的独立动力学设定尤其不能只剩一个“γ测得35°/30°”摘要。

### 实际成功仍应保留

- Figs5/6（PDF16–17/204–205）：两核knownlow-spinpositive态的次序、77Se两negative bands获得非平凡总体描述。
- 77Segroundstate的p1/2component与既有spectroscopicfactor相容；μ实验.533n.m.、模型.394n.m.（PDF19Table4；PDF20讨论）。这是解释支持，不是新transfer实验。
- 75Se低位negativeyrast的部分branch/δ较好，但其它lowlyingstatesdecays较差（PDF20）。不能只保留失败而抹去成功。

### 原作者集中列出的弱点

| 问题 | 实际原件结果 | 对解释的限制 |
|---|---|---|
|远离yrast的core空间|75Se实测leveldensity约600keV起增，而理论过稀；作者指可能遗漏74Se低0+854keV等coreexcitation，低quadrupole连接的额外corefamily可产生第二oddAfamily|rigidrotorcore并不保证nonyrast完整；这只是作者可能解释，未证明具体遗漏模式|
|EM并非全面再现|Table3：75Se7/2+→5/2+ E2实验125W.u.、理论6；9/2+→5/2+则34vs37；groundQ实验约1b、理论.02b，但作者提醒该实验Q并非完全可靠|能谱/部分decay成功不等完整wavefunction/EM算符成功；单个失败也须连实验可靠性分层|
|half-life对照范围|75Se1/2−实验30nsvs理论2600ns；Table4也有明显逐态偏差|这些表不是“所有lifetimes都预测正确”|
|bandidentity可分歧|77Se按coreE2decay或按predominants.p.parentage分类，在较高态给不同bandmembership；理论预期的p1/2型R±1/2近合及强interbandM1不见|不能用一种分类直接替代另一种，预测links是独立检验对象|
|惯量不一致|negative带对应coreE2参数360keV，而邻74/76/78Se实测2+为633/560/614keV；positive带约600keV与邻核平均相当|不能简单将negative惯量增大唯一归为shape；作者自己说纯deformation解释困难|
|两parity相对位置|假设相同gap把negative谱相对实验压低 **485keV(75Se)、413keV(77Se)**|同一pairing处方未给正确relativeparityoffset；不能拿平移后各自好谱证明同零点/占据合同|
|Coriolis修正|75Sepositive ξ=.85被作者直称ad hoc、理论论证不充分，最低wavefunctions仍不满意|拟合ξ与γ/core参数不能伪装成独立微观预测|
|遗漏pairing/空间|作者建议改进blocking、高阶pairingmultipoles、particle-holecoupling、manyqpconfigurations|本篇未实际纳入/验证这些扩展，不能把建议写成已解决机制|

Locators：PDF18–21/printed206–209 Tables3/4与弱点(i)–(vi)。

**尤其重要的表格合同：Table3脚注（Table4“sameasTable3”）明确模型half-lives和branchingratios采用实验Eγ，并忽略internalconversion及非M1/E2模式。** 因而这些计算包含了实验能量的输入，不是全链从H/谱/时钟到所有decay的独立预测；缺IC/额外模式也妨碍把该理论τ直接当实验totalwidth。这里仅报告源本身的合同，不反推任何未给ICC或改作者数值。

## 3.3：高j decoupling 的实际示意机制

### 3.3.1：alignment不是永远单一adiabaticorbital

PDF21–22/209–210 Eqs19–21以rigidaxialcore、单位惯量作解释。Coriolisterm−2I·j混其它轨道，单一adiabatic近似可失效；大形变/大能间隔使spreading代价高。Ω=±1/2子空间即有semialignment，其旋转轴平均j为 **±(j+1/2)/2**；跨轨道spreading可趋更完全对齐。

作者特别指出：fullydecoupledband的所谓unfavouredstates**并非简单antialigned**，而是由较远的两个或多个轨道组成、仍几乎aligned的态（PDF22Eq21后）。这与只用favoured/unfavoured能序或一个dominant轨道给几何标签不同。

Figs7/8（PDF23–24）用γ0–180°加轴置换显示hydrodynamical惯量与h11/2轨道构成；γ0/120对应prolate、60/180对应oblate但轴身份不同。Fig8的composition图/权重不是完整复振幅phase。**Table5/PDF25**给ε=.16、γ0/30/60、coreE2=.3MeV、Fermi在最低orbital的h11/2示意权重；随spin转向shelllower/middle/upper的组合不相同。这是模型例，不是133Ce测得orbitoccupation。

### 3.3.2：ε4可模拟部分γ谱效应，且依Fermi/BCS

Fig9/PDF28与PDF27–29是示意A≈130protonMO参数κ=.0620、μ=.614、ε=.16、γ0/30/60、E2core=.3MeV；不是133Ce的输入。作者提醒三个独立intrinsichexadecapole坐标被选成特定γdependent组合，且 **正ε40对应负hexadecapolemoment**（PDF27），不能把ε4与Q4或其它β4表值直接等号。

- γ0decoupledband中增ε4使部分unfavouredstates降低，**引入γ也可能造成同方向变化，但机制不同**（PDF29）。仅看这种energytrend不能唯一识别γ。
- γ60时压缩轨道间隔增加Coriolisspreading，可提高effectiveinertia；γ30的yrast能量对ε4不敏感（PDF29）。不同观测对参数敏感度不同，不应从一个好谱泛推全空间参数已定。
- Fig9把Fermi始终放在最低orbital，gap取12/sqrt(A)。作者指出若BCSFermi略高于首orbital，qp能量对ε4变化可弱得多，所画效应会被damped（PDF29）。Fermi/Δ是解释合同的一部分，不是可无视的零点细节。

### 3.3.3：跨壳mixing与“改变core”的表面等效

Fig10/PDF30与PDF29–31比较h11/2-only和加 **f7/2、间隔5MeV** 的示意particle空间；core为βdeformed、γunstable，参数“可类似126Xe”，不是新126Xe实验。加f7/2可使spectra变化类似在corepotential加 **−cos3γ**；图中core **<cos3γ>** 趋prolate。作者给出低Ω耦合更强的机制（PDF31Eq22）。

**rigidcore不能被极化**，但在其上加入f7/2仍可得到类似oddAspectralshifts（PDF30末）。这清楚区分了“动态corepolarization”和“固定core上s.p.spacerenormalization”两个不同原因。故拟合相似能谱不能单凭趋势判coreγsoft/hard或唯一configuration。

作者最后还明确：只加一个相邻j-shell时，考虑到其它intershellcouplings，**不能在此期待numericalconvergence**（PDF31§3.3.3末）。不把这张成功解释图盖成任意空间截断的收敛证明。其§2.3方法把更多couplings放进deformeds.p.eigenstates，不等于所有oddA/manyqp态或EMkernel已无限空间精确。

## 全部关键图表的可追溯索引

| PDF / printed | 对象 | 审计用途 |
|---|---|---|
|12 /200|Fig3 “A187”protonMOlevels|Re轨道/shape路径背景，非Au实测|
|13 /201|Fig4/Table2，185Re|实际fit后谱/decay/EM支持与缺带|
|16–17 /204–205|Figs5/6，75/77Se|两parity不同惯量/ξ，谱排序与残差|
|18–19 /206–207|Tables3/4，SeEM/half-lives/branches|M1/E2/IC及实验Eγ输入合同、成功与偏差并列|
|23 /211|Fig7，Jk与<jz>vsγ|轴置换、alignment与轨道权重|
|24 /212|Fig8 compositionweights|不同γ由不同orbitals构成高j分量，非完整相位|
|25 /213|Table5，h11/2权重|spin/γ依赖与adiabatic标签边界|
|28 /216|Fig9，ε4扫描|形变高阶/间隔/惯量敏感性及Fermi合同|
|30 /218|Fig10，j-shell扩展|γunstablecorepolarization与固定core谱效应区分|
|31 /219|§4Conclusion|方法目标与aligned3qp扩展只是建议，不是本文已执行|

## 只迁移到133Ce的方法合同

以下是**本任务综合/设计**，不是1978原文对133Ce的结论；对接`133ce-thesis-analysis-blueprint`的BCS零点、γ–Coriolis辨识、空间与EMholdout问题：

1. **区分input/calibration/holdout**：偶芯E2/Q等先验、奇核用于调J0/ξ/形变的观测、未用来定标的links/EM分别列。不能把拟合过的S/能量或经验Q再当独立确认。
2. **共同单位/零点/Fermi/Δ与blocking**：133Ce实际负/正parity输入分别固定；不移植Se的360/600keV、Δ或跨parityoffset。Se失败仅提示该自由度值得验证，不证明133Ce也有同种pairing问题。
3. **空间与态身份随spin追踪**：保存完整Nilsson/qp组成、K/R信息与levelmapping；一个dominantorbital、energyordinal或banddecay标签不是全spin不变身份。未取得actualproducer不能从图权重逆得复wavefunction。
4. **γ/ε4/jmixing联合敏感性**：用源例选择需扫描的机制，而不宣称所有observable永远不可辨。133Ce须在冻结输入后看energy与未定标EM是否产生不同可检预测；固定γ的最佳fit不等γrigidity测量。
5. **rigidcore的nonyrast/多qp边界**：相似第二family不自动是同shapephonon或chirality；先核允许coreexcitation/manyqp配置及相应links。§4只提出aligned3qp未来扩展，不能引用成本篇已经求了133Ce3qp。
6. **EM以actualEγ和完整width合同检验**：理论若采用实验Eγ，标成数据辅助的matrixelement/decay检验，不叫全部预测；IC、其它mode、δphase、branch、clock与Cov不能省。1978Tables3/4的缺IC合同不能搬到现代133Ce分析。
7. **缺线/缺带不直接排他**：Re例的强M1sidefeeding只是可能可见性解释，提醒先做feeding/population/detection合同；不为133Ce虚造未见分支或上限。

这不会改变133Ce既有band用户审核、shape/config解释或actual参数。它把模型祖先的真实成功与失效转成可审查要求，不以历史参数填当前missinginput。

## Candidate atomic claims（供leader择需合并）

| ID | 草稿 | claimclass / exactlocator |
|---|---|---|
|LLR78-036-001|185Re应用用六positive-hole轨道及A187MO参数，按奇核Q/groundbandinertia/[4111/2]bandhead将186Os先验改成ε.25/ε4.08/γ15/E2=115，ξ1；总体谱/EM支持不能称完全未定标预测|author-model-input-and-result；PDF11/13–14，Figs3/4/Table2|
|LLR78-036-002|Se应用ε.29/ε4=0、BCS窗口/平均gap及activeorbitals固定；γ35/30从负parity低态次序选，惯量按oddAspacing选，75Sepositiveξ.85恢复gs|direct-calibration-contract；PDF15，Figs5/6|
|LLR78-036-003|Tables3/4的计算half-lives/branches用实验Eγ且略IC/非M1E2；能谱部分成功伴明显EM失配，不能升成完整decayprediction|direct-source-scope-and-adverse-result；PDF18–21 Tables3/4|
|LLR78-036-004|rigidcore缺额外low0+family、parity惯量与neighborcoreE2不符、同gap的485/413keVoffset和ad-hocξ均由作者保留；blocking/pairing/manyqp扩展未在本应用实际完成|author-limit-and-proposal；PDF20–21弱点(i)–(vi)|
|LLR78-036-005|fullydecoupledband的unfavouredstates可仍nearlyaligned且含远离Fermi的多轨道，不等简单antialignment；构成随spin/γ变|direct-model-mechanism；PDF22 Eqs20/21；Figs7/8/Table5PDF23–26|
|LLR78-036-006|ε4、γ、jmixing可经不同机制产生类似谱移动，效果依Fermi/Δ；这是特定模型例的辨识边界，不是energyonly普适不可识别定理|source-model-plus-labelled-inference；PDF27–31 Figs9/10|
|LLR78-036-007|γunstablecore加f7/2能改变<cos3γ>与spectra，rigidcore上也能有相似spectralshift；两者不能混成已测corepolarization；单邻壳扩展未证明数值收敛|direct-model-and-convergence-limit；PDF29–31 Fig10/Eq22|
|LLR78-036-008|133Ce迁移应冻结core/BCS/空间/轴/算符并保EMholdout和非yrast域；不移植Re/Se/Xe参数或实验结论|task-synthesis-design；以上original+133Ceexistingcontract|

所有新增候选均needs_review:true，实验列是源引用数据而非本轮新采集。root/032整合后才可描述全主线阅读覆盖；本worker的assignedscope已经完成，未模拟/复现作者谱。仅写worker/tmp，canonical/raw/PLAN/Bib/Git/session/card保持不变。


## Table3局部转录修正

root指出后，对原PDF18/printed206的Table3半衰期段作4倍局部放大。首行实际是 **1/2−**，实验30ns、理论2600ns；先前报告写1/2+是本worker转录错误，现已改正。下一两行分别7/2+与9/2+；本次未重做其它数值、未改原件或canonical。局部核验图：`tmp/day24-larsson1978-applications-036/table3-half-lives-parity-crop.png`。
