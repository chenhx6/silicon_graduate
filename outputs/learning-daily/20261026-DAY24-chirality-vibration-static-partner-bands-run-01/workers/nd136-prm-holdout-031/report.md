# 031：四壳 PRM 支持 D5，但未发表所需的 E2 out/in holdout

**主结论：** 已取得并完整原读这篇方法论文。它采用 **good-I 的量子 PRM 波函数**，理论上可计算相干态间 EM 矩阵元；实际发表的 EM 结果却只有 **带内 B(M1)/B(E2) 比值曲线**。正文、六图、一表中**没有** D5-C20+→D5 18+（1021.2keV）与D5-C20+→D5-C18+（611.4keV）的 interbandE2/intrabandE2 预测，也没有可用于唯一恢复它的 absoluteE2 或 signedRME 表。故不能将模型摘要的“EM agreement”认证成对 thesis 条件比 **.2197885667** 的已发表检验。

这不撤销模型对 D5 能谱、带内比与几何的真实支持；它明确区分 **模型框架可算**、**论文实际给出**和**本任务尚未取得的作者输出**。

## 身份、原件与覆盖

Fresh Crossref metadata 核准：**Q.B.Chen, B.F.Lv, C.M.Petrache and J.Meng**, *Multiple chiral doublets in four-j shells particle rotor model: Five possible chiral doublets in136Nd*, **Physics Letters B782,744–749(2018)**，DOI **10.1016/j.physletb.2018.06.030**。原题名核素排版在metadata中有markup，按实际PDF可读为136Nd。

实际body：官方 `https://arxiv.org/pdf/1805.06162` 返回HTTP200 application/pdf、有效%PDF、**384518bytes、15pages**，SHA256 **cba4fa62433207c06b8673dc484d8a2d0ecdd7db51c27eafb2329726190bee91**。API exactDOI关联 **arXiv1805.06162v1**，PDF侧栏16May2018v1，titlepage另标26June2021 typesetdate。出版年与重排日期分开保存；**本轮未取得VoR**。

第二条有明确线索的Kyoto机构bitstream返回HTTP200但为3058byteHTML壳，非PDF，SHA256 **96390a027c3be423b20a21884c18fde4efb741d219248a65758aab1d00c7887c**。未继续猜URL或重试。初始Wiki/raw文件名查无该确切文献独立页/原件；既有PE18/LV19/thesis只把它列作模型引用。本轮只读这一篇新body。

实际阅读：**15页全部文字、全部6图、TableI、Eqs1–9**；PDF3–11全部关键图/表/基与输入视觉核。没有模型程序、未知code、旧114或独立数值PRM重放；没有对曲线数字化反演。

## 模型空间：比概率平均更完整，但仍不等已交付该transition

**PDF3 Eqs1–2**：H=Hcoll+Hintr，Hcoll=Σ(Ik−Jk)^2/(2Jk)，Jk=J0 sin²(γ−2kπ/3)。**PDF4 Eqs3–7**：四个single-j壳内single-particle谱，particle/hole符号与C∝β，使用intrinsicmany-particle/hole及time-reversal伙伴。

**Eqs8–9/PDF4** 将态展开在D2对称strong-coupling基；总I是好量子数，保K/内禀配置振幅。它与Wu18式的单态密度平均局部B不同：给定完整EM算符核时，`<If||T||Ii>`可在振幅层由初末态系数双线性求和。**这是由源态空间推得的能力，不是正文印出的完整EM核或本轮实际重放**。源PDF5只写“after obtaining the wave functions … B(M1),B(E2) … can be calculated”，没有列出完整transitionkernel/phase字典。

**截断：** PDF5给D1全空间示例864(2I+1)，I10/20时18144/35424；按配置能量cutoff缩到约5000–10000，作者称energyuncertainty≤.1%。该数字针对能量，**不自动等于interbandE2或小振幅消干涉的.1%误差**。每个I的实际cutoff、系数和EM收敛表未给。

## D5配置与PE18 C的对应、参数如何选

**TableI/PDF6**：

`D5, positive: pi(h11/2)^2(g7/2)^−2 ⊗ nu(h11/2)^−1(f7/2)^1, beta=.26,gamma=23°,J0=40hbar²/MeV,xi=.93`。

这是 **六个unpaired particle/hole的配置**，分布在四个shell：质子h11/2、g7/2， 中子h11/2、f7/2；不是旧被撤回的πh11²⊗νh11^−2简写。它与PE18 **C** 的六qp结构/β.26/γ23相联系，但把PE18较宽的 `(d5/2g7/2)^−2`、`(f7/2h9/2)^1` 指定为 **g7/2 holes、f7/2 particle**。这是一项实际模型空间选择，不等测得每个混合轨道occupation或完整多轨道混合。该量子PRM配置不能无说明代替PE18不同TAC-CDFT模型的全部输入。

**PDF5明确说 J0 和 Coriolisattenuation ξ adjusted to reproduce spectra trend**。β/γ来自constrainedCDFT/既有配置选择。对D5正文未说再次用这里目标out/inE2来调参，也没有显示它被用过；但完整fit输入及优化记录未给，不能据“未画该比”独立证明严格out-of-sample。

EM采用 **经验Q0=(3/√(5π))R0²Zβ、gR=Z/A、gl=1(0)、gs=.6gsfree、gp(n)=gl+(gs−gl)/(2l+1)**（PDF5）。这些不是新测Q/g或目标核绝对EM的独立校准。C的具体β标度引用Ref64；未恢复actualjob，不把文中公式视为完整可一键复算package。

## 论文实际给出的输出

| 输出 | 实际原件 | 对本次holdout意味着什么 |
|---|---|---|
|能谱/劈裂|Fig1/PDF6，数据来自PE18Ref20；D5约410keV@I18降至约150keV，PRM有相应趋势|对pair能量支持，不能唯一决定两个不同E2矩阵元 |
|S(I)|Fig2/PDF7，源按[E(I)−E(I−1)]/(2I)作比较|相同能量信息的派生诊断，不是另一份独立EM证据 |
|EM比|**Fig3/PDF8：B(M1)/B(E2)**，D5/D5-C双方点与模型曲线相近；PDF8–9承认仅此pair有双方实验ratio|这是带内M1/E2比，**不是跨带E2/带内E2**；不提供目标E2分子/分母 |
|RMS几何|Figs4/5/6，分别D2/D5/D4，PDF9–11|平方角动量分量是模型几何支持，不能恢复signedRME/相对phase或transitionkernel |
|输入表|TableI只列parity、配置、β/γ、J0、ξ|没有目标Eγ/Ei/端点索引、绝对B表或branching预测 |

**全文verified-negative：** 没有D5-C20+两条目标E2的逐线输出，没有这两endpoint间的interbandE2曲线，没有全部absoluteE2数表。这个范围只属于实际读到的v1正文；不声称作者从未计算过、别处无输出或VoR/SI一定相同。

## .21979为何不能从Fig3“比值再比值”恢复

已读thesis的条件观测量是同母态：

`R_E2 = B(E2;20+_D5C→18+_D5)/B(E2;20+_D5C→18+_D5C) ≈ .2197885667`。

Fig3给各band的带内 **M1/E2**，例如一个M1分子与带内E2分母。没有跨带E2分子；两band的带内M1也不是同一RME。多个比相近不能消去成缺失的跨带E2。图的finitepoints/lines和RMS也不包含全部波函数振幅/phase，所以不能逆造这个预测。

在good-I PRM中，若取得冻结输入和实际输出，因两路Ii=20、If=18相同，Wigner–Eckart的共同(2Ii+1)因子消去，可直接比较 `|Rout|²/|Rin|²`。共同全局Q0标尺也可在相同E2算符约定下消去，但γ/态混合/截断和端点身份不消。**这说明此项holdout有可检验价值，不说明它已经在此文通过。** 本轮没有计算未给Rout/Rin，也不给模型CI/phase。

## 真实支持、counterlimits和同数据谱系

源支持D5：能谱和带内EM趋势与PE18相容；Fig5/PDF10描述I≥21时两band角动量分量相近、rotor主沿i，h11/2protons/f7/2neutronparticles偏s，g7/2protonholes/h11/2neutronhole偏l；作者据此支持aplanarity。I≤21时两g7/2holes的l分量不同，D5-C在I17→21从约2hbar到5hbar，作者用来解释较大低spin劈裂。**这也提示I20目标就在结构演化附近，不能用高spinRMS近合无条件代填它的EM。** 几何仍是模型解释，非量子定态单手局域化测量。

源自己保留的限制：

- D2劈裂被低估（PDF5）；
- D4低于I18谱不能再现、所用配置不适低spin；后段在I≥19较好（PDF6/8/10）；
- D3的B比并不很好（PDF8）；
- PDF8–9明确仅D5双partner有实验B比，其它四组为candidates、需要进一步实验。摘要总体成功不能抹去这些局部条件。

TableI/PDF6里D3/D4的具体配置也不同于简单把PE18的D/D*原样搬入；D4额外d5/2protonholes，本文将其限制在crossing以上。不要由“consistentwithRef20”一句自动认证所有bands相同Hamiltonian/occupation。另该v1表把D6parity列为+；本单元不将其当PE18负D6的修订，更不因不相关局部字段扩大为否定D5。VoR未核，版本/assignment差别保留。

所有实验点主要复用 **PE18Ref20**，不是本模型文新采集。thesis的同campaign逐线输入是更细的实验账本，也不是第三套实验。独立模型计算可提供不同理论约束，但共享输入数据/校准不构成独立实验重复确认。

## 下一项可执行的最小model-output合同

这是本任务设计，不是作者已经交付：

1. 冻结D5配置、β/γ、J0/ξ、single-particleC与EM约定、每I的basiscutoff；交付三个态的good-I身份：20+_D5C、18+_D5C、18+_D5，并与thesisEi/branch明确对应。
2. 交付两路同E2算符的复/带符号RME或至少同规范的B(E2)，给interband与intraband端点标签，以及小矩阵元/截断收敛；不是只给M1/E2比或RMS。
3. 输出目标R_E2及独立说明它是否参与原参数选择，再与实验条件比及其未解selectedgate/Cov/响应边界同框比较。没有这些，模型的该数值预测为 **not supplied**，不以图面匹配盖章。

无需因此否认当前发表支持，也不要求先补τ才可比较同parentE2比。实验比的τ/globalnorm可消，但**模型缺的两E2输出仍不能从其它观察量推出**。

## Atomic候选草稿

均needs_review:true，actualversion=arxiv1805.06162v1，类型明确为模型/输出边界。建议source slug由leader决定。

| ID | 草稿 | Locator |
|---|---|---|
|CQ18-D25P-001|四single-j壳PRM采用D2对称strong-couplinggood-I态；原理上可在振幅层求态间EM，正文未给完整EMkernel/actualproducer|PDF3–5 Eqs1–9及计算段 |
|CQ18-D25P-002|D5为六qp πh11²g7^−2⊗νh11^−1f7^1，β.26/γ23/J0=40/ξ.93；是PE18C宽orbit配置的具体模型选择，非occupation测量|PDF6TableI；PDF5输入段；PE18C |
|CQ18-D25P-003|J0/ξ按能谱调整，Q0/g采用经验/淬灭算符；能量截断≤.1%声明不等EM小幅干涉的同精度|PDF5截断/输入段 |
|CQ18-D25P-004|实际EM图仅带内B(M1)/B(E2)，无D5-C20+两E2端点的out/in或absoluteE2表；不能认证thesis条件比.21979已被模型检验|PDF6–11全部图/表/文字，尤其Fig3PDF8 |
|CQ18-D25P-005|D5能谱/带内EM/RMS支持保留；I17–21holes重排、D3比偏差、D4低spin失配及其它四pair实验不足同时保留|PDF5–10；Figs1/3/5 |
|CQ18-D25P-006|目标同parentE2比可作有限holdout，但需冻结model/端点并交付两E2RME与收敛；不需τ/globalQ0，不由其它曲线逆造|任务design；基于Eqs8–9与实际thesis028输入 |

## 完成状态

本篇原稿范围内的完整body单元完成，目标预测仍**not published/not supplied**。两条正文路线历史保留，VoR未获；不新增网络扫描、不跑unknowncode/114。只写assignedworker/tmp；canonical/raw/PLAN/Bib/Git、session/课程信用未改。仍sameDay24run＋恰好Day25preview，worker031不是课程Day31，Day26保持关闭。
