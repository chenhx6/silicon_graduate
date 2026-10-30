# 069：133Ce当前公开评估的ground/isomer与低能零点

**取得了真实公开评估记录。** 当前NNDC NuDat/ENSDF端点返回的133Ce adopted：**ground 0.0keV、1/2+、T1/2=97(4)min；低9/2− isomer为37.2(7)keV、T1/2=5.1(3)h**。这是直接读取L记录，不是从Wiki的207.4−170.2或592.1−554.9反造evaluated值。

版本须连结论保留：NNDC record **133058001**，`ADOPTED LEVELS, GAMMAS`，header `11NDS 201104`，Yu. Khazov / A. Rodionov / F.G. Kondev，**NDS112,855(2011)**、publication cutoff **31-Oct-2010**。这是本轮检索时公开端点实际返回的评估快照，不宣称它包含2026新实验或所有后续paper。IAEA LiveChart CSV也标相同cutoff/authors；两个接口**不是两份独立实验**。

## 先查重与有限路线

已查Wiki nucleus/source与相关raw/tmp文件入口：WK22-36已有37.2的明确**派生decimal**，但未找到本窄问题的既存133Ce adopted raw record。该派生记录保留其原证据类型，不因本轮中心值相同就改成当时独立读取评估。

只用公开HTTP入口，不碰凭据/浏览器/其它项目。IAEA `fields=levels&nuclides=133ce`及NNDC NuDat取得成功。旧式mass-file URL返回404后**没有重试**；转用仓库已有NNDC read-only quick-search POST及ENSDF text dispatcher，分别取得adopted和实际`120SN(16O,3NG)`记录；两个getrefs入口取得原引用身份。共八项请求记录在`tmp/day24-ce133-evaluated-zero-entry-069/access-complete.json`。无下载论文正文、SI、模型代码或新数据拟合。

## 原子locator与实际字段

下表line是本轮逐字抽取的ENSDF text文件行号（开头空行保留），不能只引用HTML显示顺序。

| 候选ID | 实际评估对象 | 字段 | 精确locator |
|---|---|---|---|
|N133-069-001|adopted GS|E0.0；Jπ1/2+；T1/2 97 M 4；EC+B+=100|`adopted.ensdf` L62–66|
|N133-069-002|adopted low isomer|E37.2 7，即37.2±.7keV；9/2−；5.1 H 3，即5.1±.3h；L行保M标志|同文件L67–72|
|N133-069-003|adopted precision/origin|general level energies来自least-squares fit to Eγ；同负带11/2−为207.4(7)keV、170.2(2)keV M1+E2出口到低9/2−|同文件L18、L79–84|
|N133-069-004|ground J/T lineage|J由1973In04 atomic-beam magnetic resonance；97min来自1967Ge08|同文件L64–65；`adopted-refs-text.txt`对应key|
|N133-069-005|isomer J/T lineage|J同1973In04；5.1(3)h是4.9(4)h1976Ge10与5.4(5)h1967Ge08的weighted average；另列6.3(1)h1951St03|同文件L69–71|
|N133-069-006|反应记录中的版本残留|同201104 reaction record133058014印37.3(6)keV、4.9(4)h，能量在least-squares adjustment中held fixed且E/T注“from adopted levels”|`sn120-reaction.ensdf` L82–86|
|N133-069-007|历史scheme lineage|1974Gi01以γγ、energy sums、intensity balance、excitation function建scheme，基于5.4h9/2−态；1995Ra12扩充，2011再增行/assign bands|同reaction文件L5–19|

0.7keV、0.3h和4min是**记录所给不确定度口径**，本轮不另给confidence level或Gaussian CI。这里全部T为**half-life T1/2**，不称meanτ。M及长T表明该激发态为metastable level；评估给它正激发能，所以在这个adopted快照中97min的1/2+是ground、5.1h的9/2−是isomer。

IAEA CSV有两个同名`unc_hl`列，分别对应原T单位及秒单位（位置12/15）；本轮按列位置保留，未用会覆盖重名字段的dict读法把240s或1080s误作4min/0.3h的原字面误差。NNDC定宽行与秒换算同时核这些数字。

### 能量关联与未测IT边界

Adopted 37.2(7)和207.4(7)是同评估的level参数；general comment说由Eγ least-squares求得，但**未交付level-fit covariance**。直接连接γ为170.2(2)，不能将两个.7误差假设独立后给差值误差，也不能反推一个唯一Cov。所有依赖同9/2− offset的高态，要连same-dataset fit/anchor定义再传播；本轮没有造协方差矩阵。

Adopted isomer continuation明印`%EC+%B+ LT 100$ %IT=?`。它**没有把37.2keV excitation列为一条已测37.2keV IT γ**，不可据level difference造transition/branch/ICC。IAEA CSV这行的aggregate EC+B+%显示100，与ENSDF的`LT 100/IT=?`有表示层差异；精确branch完整性按原ENSDF边界保留，不把CSV rounded/aggregate字段当已知totalBR。

## 两个真实record不完全同值，不能抹平

当前adopted37.2(7)/5.1(3)与reaction record37.3(6)/4.9(4)共用2011header，却保不同数值。reaction还直说这些来自adopted且E held fixed，说明该反应表的低态并非新独立absolute-energy或half-life measurement。**不平均、不把.1keV差给显著性、不回改原表，不因“from adopted”就假定每个值与当前adopted同步。** 本轮只能标记cross-dataset consistency boundary；不能依据这点裁原实验或evaluation有错。

这也阻止循环论证：NuDat tooltip说energy from120Sn record，但该record的37.3keV anchor又标adopted/fixed。已取得文本未唯一追清**最初确定正负宇称两基底相对激发能的独立观测路径**。公开adopted的37.2(7)本身可直接引用；若要审计其绝对anchor的首次实验依据，仍需原evaluation/早期primary完整讨论，不能把循环注释伪装成闭合独立测量链。

## 可追溯primary身份（本轮只读官方reference record）

| key | 官方ref record身份 | 此任务角色 |
|---|---|---|
|1967Ge08|C. Gerschel, G. Albouy，*Compt. Rend.*264B,183(1967)，*Isomerism in 133Ce*|ground97min及isomer旧5.4h的原引用；正文未得|
|1973In04|S. Ingelman, C. Ekström, M. Olsmats, B. Wannberg，*Phys. Scr.*7,24(1973)，*Nuclear Spins of Neutron-Deficient Lanthanum and Cerium Isotopes*|两态J的atomic-beam来源；本轮未读primary|
|1976Ge10|R.J. Gehrke, R.G. Helmer，*J. Inorg. Nucl. Chem.*38,1929(1976)，DOI10.1016/0022-1902(76)80440-X|isomer4.9(4)h参与adopted weighted average；非本轮新寿命实验|
|1974Gi01|J. Gizon, A. Gizon, M.R. Maier, R.M. Diamond, F.S. Stephens，*NPA*222,557(1974)，DOI10.1016/0375-9474(74)90339-X，*Deformed States of Neutron-Deficient Cerium and Neodymium Nuclei*|reaction scheme历史，不能由后评估倒写其当年已知ground ordering|
|1995Ra12|S. Rab，*NDS*75,491(1995)，DOI10.1006/ndsh.1995.1030|反应dataset继承/扩充层，非独立experiment|

官方refs还列1997Em01/1991Pa04等后续实验；本轮只按低态/zero任务提取相关lineage，不摄入整套高spin测量或将same nucleus当同campaign。

## 对历史zero和WK22的可消费结论

现在能用**真实evaluated record**独立于Wiki算术固定“当前adopted GS1/2+，9/2−正激发能约37keV”的表示。37.2是带.7keV uncertainty的评估能，不是本轮测得/高精度小数；它与WK22派生中心数相同，不让WK22那一行追溯性自动升级。

1974的5.4h是后来adopted isomer平均的一个输入分量，与当年scheme基于9/2−的记录相符；这并不能单靠后来的ground ordering断言Gizon当时已知或写错ground/isomer。1975图以11/2−设零和现代GS零点是另一个坐标选择，需逐态/branch确认才能整链平移，本轮不裁论文错误，也不给2022实际λ/Δ或program header。

source files/hash、原行片段、metadata和字段口径在`evaluated-records.json`；完整官方快照保tmp。可复用事实由root按evaluation/non-independent-evidence类型写回knowledge；本worker只写069/tmp，不动canonical/raw/PLAN/Bib/Git/credentials/课程/session，不开新课程日。
