# 065：MTV75 PartII写回短审

**本审范围内未发现实质P0/P1，verified no-op；无required修正。** 新PartII source与133Ce蓝本、WK22-43、135Nd页及Day25三核matrix的新增迁移段保留了源定义、定标依赖及作者限制，canonical未改。

实际读域：新`knowledge/sources/meyer-ter-vehn-1975-odd-a-unique-parity-comparison.md`全页及四个下游新增节；复用061连续原读PDF20–25与context1–2/18–19，**本轮fresh文字+整页视觉核原PDF3–4/9/13/17/19**。新增视觉对象为Table1、Table2、Tables3a/3b、Table5与Fig9；不重新宣告本worker独立全25页或独立重核前面所有应用图。原件仍为057已验SHA `fd1ba7f9280e8bafd86bbec06ec18e8a7089f93e84306829a4be897d9dd8439d`。

逐项结论：

- **取参依赖正确。** PDF3–4确以particle A−1/hole A+1邻芯确定γ大小、以odd-A谱选γ或60−γ侧；β用两邻第一2+均值，作者自己承认与γ选邻规则不完全一致。壳内λ进一步近似fit第一(j−1)目标态。因此写回将“essentially parameter-free”限制在此procedure，而非全数据独立预测，正确。
- **λ坐标正确。** particle tildeλ=(λ−ε1)/(ε2−ε1)，hole=(ε_(j+1/2)−λ)/(ε_(j+1/2)−ε_(j−1/2))；它们是单壳无量纲端点/间隔坐标，不能恢复WK22 MeV数值、共同offset或negative-parity λ。正文与下游未将tilde符号丢成实际绝对λ。
- **Table2原字面保留正确。** PDF9第一组β.141列清楚为4、25、11、40，总80；β.144列57、8、15、20，总100；实验52、3、11、34，总100。source没有擅把4修24或强制归一，第三11/2分支blank也未当0。它保原表不闭合边界，不反推缺失branch。
- **Table3字面核验正确。** PDF13的五条theory δ依次.04/.18/.19/.21/−.14，仅200和389keV行属于所印范围。2/5没有被改成p值或有coverage的CI。source还保measured Eγ用于算theory δ，因此不称它们全部独立预测。Table3a第一项1.7(+∞,−1.4)对7.07属于宽范围，不是精密符合；其它三项也在原宽/单侧范围内，写回没有误报精度。
- **La数据/定标正确。** PDF17 Table5实验129La .42(2)/.38(6)，131La .34(2)/.33(3)，e²b²；theory、轴向值和Eγ均与source一致。b6.8/6.4由邻偶核B(E2)均值给定，theory误差明来自γexp不确定度；没有把此校准量另计独立holdout或移作Ce测量。原文对weak coupling的约束保为该案例范围，不泛化模式门。
- **Ce失败和非单参数对照正确。** PDF19 Fig9 exp以11/2−为0、9/2−为−170；triaxial9/2+18、axial+37。β.22/γ23与β.19/γ0确是两套输入，非只变γ；tildeλ1与Δ1MeV原样保留。前页最低9/2失败、未施ad hoc attenuation及现代高态/branch不可整带平移的限制均保留。N75列为135Nd/133Ce/131Ba，没有误成131Ce。
- **软度论证正确。** 按061已读域，Fig10只是schematic；Table6检完全γ独立Wilets–Jean极限，同时原文说rigid点也未达到。没有把这段改成普遍排除γ软度或唯一PES。Table7 rms/fitγ与196Pt/196Hg不同列、±2°非实验CI/σγ及尚缺odd+γdynamic比较也全部保留。
- **来源独立性和迁移正确。** PartII为PartI同作者、同single-j框架应用及已有数据比较；邻核定标、引用实验、作者解释分层。135Nd新段不借历史1qp比较补现代三qp相干EM/branch/g，也不撤去本核既有真实支持；Day25matrix未用ΔI1/2共存替代两shape实验。原文积极模型支持与明确失败并存，没有以审计否定全部价值。

本审只核科学与引用量词，不改review flags；结论为source self-audit，不是human-reviewed。仅写065 worker与对应tmp，无新网络、拟合、model/toy、canonical/raw/PLAN/Bib/Git或课程/session修改。
