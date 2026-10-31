# Chen2017：good-I投影态、相干振幅与几何分布的不同信息层

本轮复用既有原件作定向深化，供leader核验后写回。不是新实验或新source身份；所有增量为`needs_review: true`，不改canonical原flags。只写指定worker/tmp，raw/PLAN/Bib/Git只读，无新agent/session/credit，未运行任何producer或旧114。

## 1. 身份、引用链与实际覆盖

核定题名为 **“Chiral geometry in symmetry-restored states: Chiral doublet bands in 128Cs”**，F. Q. Chen, Q. B. Chen, Y. A. Luo, J. Meng, S. Q. Zhang，*Physical Review C* **96**,051303(2017)，DOI **10.1103/PhysRevC.96.051303**。本轮fresh Crossref确认题名/作者/出版2017-11-20；官方`https://arxiv.org/abs/1708.07282v1`确认v1=2017-08-24、12页4图及journal ref。官方body入口为`https://arxiv.org/pdf/1708.07282v1`，本轮直接读既有raw，未重复下载body。

实际原件：`raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/chen-2017-128cs.pdf`，279433bytes，12页；重新SHA256为 **d176aed6be49e350c18d130ec388383b680da9844173f4e0b386cb34f0c676c6**，与source匹配。PDF1边栏v1/2017日期，与正文typeset “August4,2021”并存；保留两个字段，不发明2021科学修订或VoR等价。本轮locator均为**此arXiv PDF/printed1–12**，不是PRC文章页码。

实际读完整12页主线/参考文献；视觉核PDF1–8/10–12，覆盖**全部4图、Eqs1–11**、输入段与关键Ref14/40/46。没有读完全部55引用原件，没有恢复作者代码、full matrix dump或原实验response。

承接关系也实际核过：WU18现有body PDF17的**Ref55**正是本篇。不要混成“Chen2017自己的Ref55”，后者在本文PDF12是Bohr–Mottelson *Nuclear Structure*。

## 2. good-I基怎样构造，实际混合哪些自由度

源PDF2 Eq1采用spherical H0、quadrupole–quadrupole、monopole pairing及quadrupole pairing的Hamiltonian。PDF3 Eq2以N、Z、Q0、Q2约束得到intrinsic态。目标128Cs为odd–odd，先选ν/π阻塞轨道，然后intrinsic空间只列

\[
\{\Phi_\kappa\}=\{\Phi_{\nu\pi},\Phi_{\nu\bar\pi},
\Phi_{\bar\nu\pi},\Phi_{\bar\nu\bar\pi}\},
\]

bar为time-reversal conjugate，**不是四个独立shape，也不能把四个κ直接称四个手性/声子态**。

PDF3 Eqs3–4的基为

\[
|IMK;NZ\kappa\rangle=P^I_{MK}P^NP^Z|\Phi_\kappa\rangle,
\qquad
|\Psi^{I\sigma}_M\rangle=
\sum_{K\kappa} f^{I\sigma}_{K\kappa} P^I_{MK}|\Phi_{NZ\kappa}\rangle,
\]

\[
P^I_{MK}=\frac{2I+1}{8\pi^2}\int d\Omega\,D^{I*}_{MK}(\Omega)R(\Omega).
\]

这里σ是本报告加上的本征态/带指标，便于区分同I的A、B；源Eq4省略这个指标。三维Euler投影给good total I、lab M；N/Z也投影恢复。K是混合中的intrinsic投影标签，不是被强行设为好量子数。不能把它降成一个平均J−1/2，也不能把投影前的每个κ直接指定为一条实验带。

Hamiltonian/norm kernel构成Hill–Wheeler generalized EVP，源Eq5为(H−EN)f=0；基非正交。Eq6给**g=N^(1/2)f**，故在保留norm支撑上g†g=f†Nf=1。不能将raw \|fKκ\|²直接当K概率。

**实际混合与冻结：**有K混合、选定blocked orbital pair的四种time-conjugateκ混合；没有正文列出的β/γ shape generator grid，也没有不同ν/π轨道对、其它qp数目的大空间配置竞争计算。PDF5固定(β,γ)=(.20,30°)，lowest πh11/2与fourth νh11/2阻塞；Hamiltonian参数取Ref40（Gao/Chen/Sun,PLB634,195(2006)，PDF11）。所以“projection后configuration mixing”应限定这个κ/K空间，不写成已覆盖所有shape/configuration alternatives。

PDF5还比较外部CDFT(.23,23.8°)、旧PSM(.20,37°)，并不把它们混进本次波函数；CDFT信息的Ref46在PDF11只写“E.Grodner et al.,to be published(2017)”，本worker未唯一匹配该未具题名条目到后文，不冒充已读其完整原producer。

“without introducing any/free parameter”是作者摘要/总结措辞：本文有固定形变/阻塞和继承耦合参数，故应解读为其采用输入下未另引新自由拟合参数的主张，不能写成无参数模型或对任意形状唯一反演。本轮未读Ref40原件的定标谱系，不能断言继承参数从未用过同核数据，或此比较属于严格out-of-sample验证。

## 3. EM输出是否越过WU18 single-density局部率平均

**直接原文输出：**PDF5–6 Fig2给A/B能量、两带带内B(E2;I→I−2)、带内B(M1;I→I−1)，以及**单向B→A的跨带B(M1;I→I−1)**，以W.u.显示。作者明确讨论带内/跨带M1的odd-even staggering，这确实比WU18单态概率平均局部TAC率多了跨态比较。

**形式推导，不能冒作源打印公式：**将Eq4的投影态用于任意标准张量T，RME的线性性要求

\[
\mathcal R_{fi}=\langle\Psi^{I_f\sigma_f}\Vert T\Vert
\Psi^{I_i\sigma_i}\rangle
=\sum_{a,b} f^{I_f\sigma_f*}_{a}\,
\mathcal T^{I_f I_i}_{ab}\,f^{I_i\sigma_i}_{b},
\quad a=(K_f,\kappa_f),\ b=(K_i,\kappa_i).
\]

\[
B(T;I_i\sigma_i\to I_f\sigma_f)
=\frac{|\mathcal R_{fi}|^2}{2I_i+1}.
\]

这是**振幅先相干求和、后平方**；以g表示还须把核相应变成N_f^(−1/2)𝒯N_i^(−1/2)（在保留支撑内），不能只换coeff而保留未经变换的矩阵元。它与∫ρ_i(q) B_local(q)dq不是同一种输出对象。

但该12页正文Eqs1–11**没有打印EM RME核、有效电荷/g因子表、相位约定、Euler quadrature/截断或完整数值矩阵**。所以可说“此投影态框架具有相干跨态RME结构，且本文实际展示了跨带M1”，不能说“本worker已从正文独立恢复其实际coherent producer所有步骤/数值相位”。这是方法层提升与实际复现readiness的区别。

**尚未展示或恢复：**跨带E2、反向A→B的独立面板、signed RME、signedδ、g/static moments、实验branch/ICC/τ/Cov或目标135Nd/133Ce的相应核。Fig2的B是模平方；它不交付同一跃迁E2和M1振幅的相对符号。每个本征态的overall phase本来可任意选择，不影响B或同态对的δ；这里真正需要的是内部相干结构及E/M算符的一致相对phase，不是为每条band规定可观测的绝对phase。

**不利结果直接保留：**PDF5承认带头附近E2量级吻合，但高spin趋势偏离实验，作者归因frozen shape；Fig2(b)可见该偏差。摘要“reproduced well”不是完整观测向量/联合Cov下的逐量统计通过。没有本轮新拟合或替代模型排除。

## 4. K图和azimuthal图各保留多少phase/几何

### K图：metric校正之后的折叠概率

PDF3 Eq7给pI(|K|)=Σκ[\|gI(K,κ)\|²+\|gI(−K,κ)\|²]。Eq6构成g时包含norm metric与混合信息；**成图之后却折叠±K并对κ求和**，不直接保留signed K，也不能从这组模方反演各K/κ内部复幅的相对phase。更不能由总I的K分布直接恢复jπ、jν、R各矢量的全部联合矩或σ三重积算符。

源PDF4规定γ∈[0°,60°]时K为l轴分量；s/i轴分布分别用[120°,180°]/[240°,300°]表示。坐标/γ扇区必须一起带入，不能把不同文献的轴名或γ号数直接覆盖。

**zero-bin字面边界：**Eq7按完整signed-K求和若机械令K=0，±0两项会重复计数。正文未给实际zero-bin/归一producer处理；本轮未数字化Fig3总和，亦不判实际图/代码错误。后续若需逐bin概率或矩，应核K=0 convention，不能凭打印式擅加因子后声称复现原图。

### Azimuthal图：K振幅先相干组合，再取边缘分布

PDF4–5 Eqs8–11给

\[
G^I_\kappa(\Omega)=\sqrt{\frac{2I+1}{8\pi^2}}
\sum_K g^I(K,\kappa)D^{I*}_{MK}(\Omega),
\]

\[
\mathcal P(\theta,\phi)=\sum_\kappa\int_0^{2\pi}d\psi'
\left|G^I_\kappa(\psi',\theta,\pi-\phi)\right|^2.
\]

所以它**保留同κ内K、K′间的干涉**，比只画p(|K|)包含更多phase-sensitive取向信息；不能误称为另一种完全incoherent |gK|²平均。但最后对κ求和/对ψ′积分，发表的P仍是取向边缘分布，未交付完整joint state或不同初末态transition kernel。完整、归一、数值P在某给定空间可含多少tomographic信息需要另论；本轮不以“所有密度都无phase”作过强定理。

一个仅解释公式的信息例（非128Cs计算）：固定某κ，只取K=±k且同样模长、相对phase α，G的模平方含cos(2kφ′−α)干涉项；改变α可保持p(|K|)完全不变却改变P。若要再计算EM，还须另有相应算符核，P自身不能代替它。g的basis phase及核必须一致变换；不把任意basis重相位当物理差异。

**角字典：**本文θ相对l轴，φ是J在i-s面的投影相对**i轴**，θ=θ′、φ=π−φ′；lab z沿J（PDF4 Eq8/Fig1）。所以s-l平面在φ=90°；不能把该φ值照搬到从s轴起量的另一文献，或把它当TAC cranking ω角/实验γ射线发射角。

P的几何测度来自标准Euler Haar dΩ=dψ′sinθ′dθ′dφ′；这是本任务按Eq9作的条件归一推导，正文Eq11本身未再打印sinθ积分式。若ΣκK|g|²=1，按标准全Euler域有∫θ=0..π sinθdθ ∫φ=−π..π dφ P=1（或周期等价的φ区间），因为φ=π−φ′只改方位原点/方向。本文Fig4实际横轴θ=0..90°、纵轴φ=0..180°；正文未另明这个部分域的折叠归一因子，不能擅补4倍或按flat θ/φ像素等权归一。本测度是Euler/Haar测度，**不是CH16的√detB dθdφ**，不得混用。若要重放图仍需原producer；本轮没有从图估“左右概率比”或实验显著性。

## 5. 真正的逐spin几何结果与“静态”边界

源PDF6–8/Figs3–4只作I=11、14、18ℏ的模型几何展示：

| spin | 模型直接结果/作者解释 | 可说到哪里 |
|---|---|---|
|11|A在Ki=0有显著概率，B在0处消失；A峰约(θ60°,φ90°)，B约(85°,45°/135°)|作者解释为关于s-l平面的0/1声子chiral vibration；不是从一张概率图独立测得phase或实验声子数 |
|14|A的Ki峰约12ℏ；两带K分布类似；P两手方向，A约(80°,40°/140°)，B约(65°,60°/120°)|作者称static chirality，但两带峰并不完全重合，Ki/Kl=0或θ/φ平面仍有有限概率，作者据此保留隧穿与有限能差 |
|18|能差增加，K分布相似性减弱；A趋θ90°、φ30°/150°的i-s平面，B约(75°,45°/135°)|作者说static chirality消失/减弱；不能从这篇投影法外推单调“越高spin越静态” |

这给Day24的增量是：good-I并不要求两个本征态各自永久只占左/右；对称恢复的态仍能通过模型几何分布识别有限涨落/隧穿regime。有限平面概率是作者在该H/空间中的解释，P本身不是独立实验的隧穿流、时钟或有符号永久手性测量。Projection也不会自动纳入未建的shape/configuration竞争或使原模型的高spin E2偏差消失。

## 6. 数据独立性及由leader写回的具体影响

Fig2所有实验比较点明确引**Ref14=Grodner et al.,PRL97,172501(2006)**（PDF10），不是本篇新采集或对原DSAM/feeding/response的独立复测。沿用相同128Cs数据比较另一理论方法可增加解释层次，不能把实验点计为另一票；也不能因本文形变的Ref46含Grodner名字就自动视为另一独立已核实验。

本文A/B与GR06 yrast/side的逐transition标签仍需crosswalk；本worker没有仅据图例将所有母末态全面重映射，也没有移植GR18低spin g或用户旧review flags。

相对WU18，最稳妥的写回是三层：

1. WU18新EM是单态ρ对局部TAC率的平均，不能提供完整相干跨带核。
2. CH17给good-I、N/Z恢复的非正交projected state、metric变换与跨带M1输出，形式上能构造coherent跨态RME；不等同已经拿到actual核/算符/phase实现。
3. K与azimuthal图是从同一模型态构造的不同降维输出，后者保留K干涉但仍不自动成为完整EM证据，也不排尽全部替代解释。

知识影响为`refines-state-and-output-contract`。不存在本轮新实验认证、signedδ、g、全branch或新核素预测。

## 7. 产物和检查

- `source-and-reading.json`：原件URL/版本/实际raw/SHA/读取覆盖及metadata核定。
- `claim-ledger.json`：分direct与task-derived的待核增量及locator，不替换原CHEN17 flags。
- `artifact-manifest.json`：本worker及tmp文件清单/hash。
- tmp保存metadata响应、raw SHA检查、12页text/render；未写raw，也未下载其它paper。

命令：rg现有Wiki/raw发现重叠；git status只识别继承dirty；Python requests核Crossref/officialabs，hashlib/PyMuPDF检查本地raw并逐页读/渲染；view_image核全4图和Eqs1–11；WU18既有body只定向核PDF17 Ref55。无作者程序、旧114、矩阵元拟合、图像数字化或Git写操作。
