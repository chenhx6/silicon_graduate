# Gizon1974：共同方法与135Ce原读（066）

已完整读取本单元分配的PDF1–4共同方法、PDF8–9和11底部135Ce正文、PDF10–11 Table2，并逐页看过这些原图和PDF7 Fig5／PDF8 Fig6。PDF9的Fig7属于135Nd，只作浮动图位置核验；另为共同归一问题定向核看PDF12 Table3左两列，未宣告该表或Nd全谱精读。064已经预暴露，开读前记录在`primed-recall.md`，非盲测、不计分。

源为Gizon等，*Deformed states of neutron-deficient cerium and neodymium nuclei*, NPA222(1974)557–578，DOI10.1016/0375-9474(74)90339-X。实际PDF22页，1,264,150bytes；SHA256 `9d09f0fca35c125cb35241bbd2f231a65ec710702889c8b0262a529af7f56dac`。原件在`tmp/day24-gizon1974-unique-parity-entry-064/attachment-object-response.pdf`；本单元自己的抽取/图像在`tmp/day24-gizon1974-methods-ce135-066/`。物理页+556=印刷页。064已按含SI范围核取完整MAIN与正式FULLXML附件清单，未见supplementary候选；小si*.gif为ALTIMG行内符号。本轮不重复下载，也不扩大SI不存在结论。

## 实验与强度/响应合同

PDF2–4／558–560为Berkeley223.5cm/88inch cyclotron的16O实验。通道为120,122Sn(16O,3n)→133,135Ce，122,124Te(16O,3n)→135,137Nd；135Ce另有124Sn(16O,5n)。共同方法列60、65、66.5、70、80、85、90MeV，而135Ce谱和Table2明确是122Sn+16O在62MeV；应保存各case实际值，不能将概述列表当完整runmanifest。靶为ORNL富集同位素约2mg/cm²，25μm Pb backing。

装置是两台8cm³ planar intrinsicGe，或一台8cm³加30cm³ coaxialGe(Li)，不是现代高重数阵列。planar分辨率在122/1330keV分别.9/1.9keV FWHM。实际布置用22Na、57Co、60Co、137Cs和177mLu标定效率/能量，另用反应产物even-even已知线校能；本页没有逐线效率修正公式、完整曲线或Cov，不能宣称重建了absoluteefficiency。

PDF3／559明写Table1–4的Iγ在**55°**测得、按最强线100归一（原生OCR的5.5°错误已看图核正）；强resolved线能误约.1%、强度约10%，弱线误差再大2–3倍。此Iγ不是角积分BR，更不是B(M1)/B(E2)。共同规范化措辞还有原表边界：PDF12／568 Table3定向原图显示135Nd198.5keV列100，而511.8keV列117。保留两值，不猜是否未放置线/不同assignment，也不推导所有真实或印刷Iγ≤100。Fig5称箭头宽按totaltransitionintensities画，不能再自动把宽度当Table2的55°光子值或绝对速率。

Fig1a/b及PDF3记录CF-trigger/TAC与RF的singlesin/outbeam和gamma-gamma方案。300ns是事件符合接收，离线还有能量/时间/背景窗；每事件存E1、E2、tγγ及一条tγRF。accidental<1%未校正；γγ通常<6ns FWHM，γRF约10ns受束团限制；后期同时采singles与coincidence，且改CF去prompttail。未给所有run ID、eventfiles或精确门界，不能声称重现原响应拟合。较低band线延迟可继承feeding，不是每个下级态自己的寿命。

90°激发函数用于归核素；另有0°、55°、90°角分布实验。PDF4原图W(θ)=1+Σ[k≥2]αk(Ii)Akmax(Ii,L1,L2,If)Pk(cosθ)，αk解释为partialalignment，α2用已知如E2线的A2exp与YamazakifullyalignedA2max比较得到。共同方法没有明确独立finitegeometryQk、openingangle或acceptancefold。δ的核别平均/忽略A4等细节应由PDF18–19单元核实，不在此假装已读；不能将135Ceα2移给133Ce。

## 135Ce：直接谱、历史输入及指认强弱

PDF8／564沿旧文献给1/2+ground、17.0h；11/2−isomer、20s、E3decay。约296keV为doublet：3/2+由135Pr27min衰变馈入，5/2+由135mCe20s馈入。这个3/2+doublet成员不是Fig5的82.6keV3/2+。先前结果谱系在正文分别列refs8,12和13–15，不能计为本实验重新测了17h/20s。

Fig5上部（PDF7／563）画1/2+0，3/2+82.6，5/2+296.1，11/2−445.7keV；149.7keVE3是isomer→5/2+。主负带13/2−1035.4、15/2−1145.3、17/2−1869.6，以及较弱/暂定19/2−2050.6。1670.6keV无明确Jπ的支态通过635.2衰变到13/2−，其能级由符合较可靠；2051keV态因181.9线很弱而明确“somewhattentative”。低态表中标b的多极性为先前已知，不能重复计作独立新判定。

Fig6／PDF8是62MeV、90°in/outbeam谱，含134Ce、135Ce decay等标记。PDF9列outbeam398、409、639、841、946、1125keV“presumably”来自134Ceisomer，不能把全部delayed峰当135Ce。作者从256、590、700、724、833keV的时间分布测8±2ns，Fig5将8ns标在2125.6keV侧馈态；这是共享feeding延迟，不是五次独立寿命。

作者用coincidence、intensity、excitationfunction和重要线multipolarity建谱，明确只有11/2−主带成员有确定Jπ。256keV(A2exp=−.26±.08)倾向stretcheddipole；类比137Nd的328keV及缺失竞争E2后，更倾向E1而非M1，故2125.6keV为(19/2+)且宇称暂定。如果E1，其hindrance为8×10^5 Weisskopf。425.6keV(A2=.28±.16)倾向stretchedE2，将2551.2keV标(23/2+)，可信度更低。Fig5括号不能抹去。预期75.0keV(19/2+)→19/2−未见，不等于测得BR=0。

Table2（PDF10–11／566–567）不是完整谱：正文说省略约30条I<2的弱线；109.5(I1.2)、181.9(I.8)因符合关系仍进图。isomer和5/2+296强度balance在计入E3后符合，因而doublet3/2+未明显激发，且in/outbeam213.4/296.1比不变。但本单元无完整conversioncoefficient与角积分输入，不再伪造独立balance重算。

|Table2线keV|I55（相对）|A2exp|多极性/边界|
|---|---|---|---|
|149.7|24.9|−.02(.06)|E3，旧指认|
|213.4|100|+.04(.01)|M1+E2，旧指认|
|256.0|30.2|−.26(.08)|(E1)，侧馈parity暂定|
|296.1|25.0|−.04(.08)|E2，旧指认|
|425.6|25.6|+.28(.16)|E2，支态Jπ较弱|
|589.7|47.2|−.71(.04)|13/2−→11/2−，M1+E2|
|635.2|17.6|−.30(.10)|1670.6→13/2−，(M1+E2)|
|699.6|73.5|+.35(.11)|15/2−→11/2−，E2|
|724.3|36.6|−.79(.03)|17/2−→15/2−，M1+E2|
|833.1|16.3|+.31(.13)|17/2−→13/2−，E2|
|906.2|21.0|+.30(.18)|(19/2−)→15/2−，E2；composite|

A2exp不是δ。空白assignment/A2也不是零或纯多极。Table2另将309.0、569.7、665.2、753.9、906.2、964.1、1012.7等标composite，尤其906.2不宜当清洁branch反演。完整原图已看，未对每条未放置弱线补指认。

## 原表最小核算与迁移边界

实际Table2两条17/2−→11/2−路径：833.1+589.7=1422.8keV；724.3+699.6=1423.9keV，相差−1.1keV。Fig5的1869.6−445.7=1423.9。原表/图不是精确自洽的现代node表；保留这一残差，不改833.1或能级、不强制closure，也不越过原文约.1%能误去宣称统计矛盾。额外一致算术：2125.6−1869.6=256.0，2551.2−2125.6=425.6，2125.6−2050.6=75.0（未见线）。

同母Table2 I55(724.3)/I55(833.1)=36.6/16.3=2.2454，只是两个不同角分布光子强度之比。724.3混合M1/E2，转为rate或B比仍需δ、响应/角积分及Eγ幂；不生成假CI或absoluteBR。机器核算见`original-table-crosscheck.json`。

135Ce的17h/20s已知ground/isomer、445.7keV基准、8ns侧馈、α2和可靠Jπ范围均不能直接移到133Ce。可迁移的是按isotope/channel/gate、历史谱系、强度定义、tentative标记逐项核对的方法。133Ce1974zero的未知ground/isomer顺序仍归064/另一单元，不能用135Ce相似谱替它裁决。本文本单元没有chirality、partnerresolved绝对率或现代133Ce构型的新测量。

`claim-ledger.json`现含35项原子记录；`receipt.json`保存实际scope。仅写自己的worker/tmp，无canonical/raw/Git/旧producer/模型fit或新网络请求。来源自审不是human-reviewed；停止因为分配单元已完成，不表示全文或Day24证据饱和。
