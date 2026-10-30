# 033：同母态 E2 比的冗余与更有信息的相邻自旋 holdout

**结论：D5-C20+没有第三条已列E2可作独立冗余；但邻近的D5-C21+有另一个端点明确的两E2出口比，值得加入模型holdout。** 20+、21+两个条件名义值分别为 **.21978857、.61468102**。二者是不同母态的不同输出约束，但属于同campaign，不能称两个独立实验，也不能用中心双比2.79669认证显著spin变化。另一个D5母态中**选定的三条E2子集**可给二维相对出口pattern；这不是该母态的全部E2库存，其三比乘法“closure”只是同输入代数恒等式，不是完整物理强度闭合。

## 读取与重叠检查

先读028实际ledger/report、031原模型report，以及canonical thesis source的TH19-D25P-001–005和`knowledge/projects/chirality-shape-coexistence-companion-matrix.md`。其中20+的.21979及3母态14线已固化，未重复作为新发现。**canonical未有21+条件E2比与“比值closure不独立”的设计行**；这是本单元增量。

本轮直接重新核同一真实thesis **physicalPDF94–95/printed93–94的Table5.1**（文字与新视觉），footnote **physicalPDF97/printed96**；用此前已核Fig5.6的family/端点。原件SHA256 **84e8b934fda9a97ea79527a8b1456f40e534bc67be847d61b1a1219002d85749**，`raw/papers/degree dissertation/吕冰峰.pdf`。不声称新读164页全文，不开新body或网络路线。模型仍是031已读的arXiv1805.06162v1/SHA **cba4fa62433207c06b8673dc484d8a2d0ecdd7db51c27eafb2329726190bee91**，这里不重跑producer。

## 20+本身没有额外E2冗余

同D5-C母态Ei7543.0、Iπ20+的源行只有：

| Eγ keV | Iγ | 原mode | endpoint |
|---|---|---|---|
|330.0|.42(9)|**M1**|D5-C19+，7213.0|
|611.4|.21(10)|E2|D5-C18+；daughter6931.6为原scheme/条件能差|
|1021.2|.6(1)|E2|D5 18+，6521.8|

不能将330.0换成第三E2、忽略mode或补未观测线。因此在这个已列E2二出口子集中，只有一个scale-free强度比：

`R20=(.6/.21)*(611.4/1021.2)^5=.2197885667`。

它的倒数、由这两个I计算的selected-photon share、selected-strength share，都只是同一组两输入的重表达；既不增加一条独立约束，也不是totalBR。没有完整decay inventory、absolute scale或模型T†T expectation，不能把两E2的和称物理closure。含M1行的全打印I相加仍不是每母态总decay probability。

## 真正新增：D5-C21+的另一个已观测E2比

**同母态Ei7927.1keV、21+**，四条源行必须全部保留：

| Eγ keV | Iγ | 原mode | Jf/endpoint | 处理 |
|---|---|---|---|---|
|384.1|.6(1)|M1/E2|20+，D5-C7543.0|δ未知，不当纯E2|
|672.5|.5(2)|M1/E2|20+，D5 7254.6|δ未知，不当E2crossover|
|714.1|.18(4)|E2|19+，D5-C7213.0|作为带内E2候选分母|
|1060.7|.8(4)|E2|19+，D5 6866.4|作为跨带E2分子|

在与028相同的 **源赋值正确、同parent、同XL=E2、效率修正relativeI确实对应可比无偏photonresponse** 条件下，

`R21 = (.8/.18)*(714.1/1060.7)^5 = .6146810196`。

原光子强度商是4.44444，能量因子约.13830323。τ、共同373.7keV reference、E2率常数消去，**不需τ或完整totalBR**。其余mixed出口不被删除或重归一；它们虽不进入这个指定same-XL比，仍属于母态库存与未来完整衰变检验。

描述性中心双比：`R21/R20=2.7966924248`。它把两个相邻母态的inter/intraE2分配联系起来，正好落在031原模型所讨论I17–21的g7/2hole重排区间附近，因而是有理由的扩展holdout。

**不附CI或显著性：**1060.7的Iγ=.8(4)相对误差本来很大，四I又可能通过共同reference、efficiency、gate/背景相关。原文未给jointCov、误差coverage或逐线producer。中心双比不是“2.8σ”、不是已经证明的单调trend，更不是反手征判据。每个parent内部的τ消去，不代表所有跨parentresponse/校准随之消去。

## 次一级信息：D5同一18+母态中选定三条E2子集的pattern

在D5 Ei6521.8、18+处，本段**只选取**515.6(.35(10))、764.6(1.9(2))、826.9(2.7(3))三个已观测E2、Jf16+出口作子集。该母态还有951.8(.16(2))的E2行及1330.5(<.01)的E2上限行，均保留在原ledger；所以这里的二维自由度只属于选定三项，**不是all-outlet自由度或完整库存**。以515.6→D5 16+6006.2为reference，条件值为：

| 比 | 名义值 |
|---|---|
|B764.6/B515.6|**.75696994**|
|B826.9/B515.6|**.72710194**|
|B826.9/B764.6|**.96054269**|

从这个选定子集的三条正强度只能得到**至多两个代数独立的scale-free比**，第三个严格等于前两者之商。`conditional-ratios.json`以十进制输入的exact rational算术核此恒等式。乘法cycle=1只能检查转录/计算是否一致；使用同一源记录时并非新独立实验closure。只有未来**独立提取**并带各自响应的冗余测量，才可能将非闭合用于response/背景/assignment诊断。

这个pattern的某些daughter不属于D5/D5-C pair，family绑定也未全部闭合；不能将其当同一四壳配置中的三个已确认模型本征态。它可提示其它配置/shape-band outlet值得关注，但优先级低于端点已知、family一致的R21。该parent的579.8、951.8和1330.5上限等其它行也不应被删掉以制造“完整”库存。

## 为什么这些还不是2×2 EM块或sum rule

若要检验相同Ji两条partner到相同Jf两条partner的2×2 E2矩阵，需要四个正确绑定的态间强度（进一步的相干问题还需要phase）。目前R20给**20+ D5-C这一行**的两个元素，但没有与之配齐的**20+ D5初态到相同两18+末态**完整行；R21在**不同Ji/Jf的另一个块**，不能跨spin拼成同一闭块。不得凭level能差推造那个缺失的γ。

因此当前数据不提供完整矩阵的绝对Frobenius norm、SVD、determinant或loop-sign，也不构成all-final-states的E2sum rule。几个publishedrelativeI不能补一个未测绝对尺度或完整终态集合。上述局部比仍可约束模型的对应unsignedRME大小分配；局部有效不等全局closure。

## 先隔离的22+候选，不强行多算一个点

表中D5-C的812.1-keV E2行印 **Ei8355.1keV**，1100.5-keV E2行印 **Ei8355.9keV**，两者均22+但Ei差.8keV。其它相关428/670.8行也印8355.1。当前只保这个**literal parent-identity boundary**，不指定typo、不将两行自动合母态、不反推修正能量或添加R22。“同spin+近能量”不足以达到本任务same-parent合同。故R21是更清楚的下一实际点，不为凑冗余删掉这个边界。

## 最小模型holdout升级

031证明该PRM框架good-I但未发表目标interbandE2输出；它也没有R21预测。下一个有信息的冻结输出请求是：

1. 用固定D5六qp配置、β.26/γ23/J0=40/ξ.93及同一E2算符/截断约定，分别绑定D5-C20+/21+与对应D5、D5-C18+/19+末态。
2. 交付四条**指定**E2的RME或B及截断收敛，输出(R20,R21)，而不只交一条平均B(M1)/B(E2)曲线。共同Q0/E2算符整体scale可消，但shape/态混合/端点/截断不消。
3. 明确这些量是否曾用于选参。若只在取得R20后重新拟合，再用R20验模型就是循环；可预先固定其中一项为校准、另一项为条件holdout，或将两项同时作为未用输出预测，但当前并未执行这样的fit/验证。

**不能从未给预测推模型失败。** 当前得出的是两个实际可检的输出合同、一个较清晰的扩展观测比与仍缺的response/modelproducer，而不是.21979/.61468已证伪或证实任何手征版本。原D5能谱/带内ratio支持不改变。

## 可复用草稿与scope

- **TH19-D25P-006候选：**源Table5.1 D5-C21+/7927.1的714.1(.18(4))与1060.7(.8(4))均E2且端点分别C19+/D519+，可条件得Bout/Bin=.61468102；与已核R20形成不同parent输出对，τ/reference消去但gate/Cov缺，不给CI/phase/排他。（directsource+conditionalratearithmetic，physicalPDF94–95/97）
- **TH19-D25P-007候选：**D5同18+中选定的515.6/764.6/826.9三E2子集有至多两维relativepattern；951.8E2及1330.5E2上限等其它出口保持，不把subset自由度当all-outlet。由同数据计算的第三比/乘法cycle只是代数冗余，不证明全EM或衰变closure。（taskdesign/algebra，原表PDF93–95）
- **TH19-D25P-008候选：**812.1与1100.5两22+E2行的printedEi8355.1/8355.9不一致，暂不合并为sameparent比或修表。（literalidentityboundary，physicalPDF94–95）

未取新body、未查D6版本，因为本窄问题确有新可解析输入；未造missingγ、δ/branch或模型预测。只写assignedworker与`tmp/day24-nd136-holdout-design-033/`，canonical/raw/Git及session/course状态不动；仍sameDay24run＋恰好Day25preview，无Day26。子任务033不是课程日。


## Root 指出后的措辞修订

本轮按root视觉核94/95后的建议，把D5I18三E2统一明确为**选定子集**，并在主段前置951.8E2与1330.5E2上限仍存在的说明；数值未重算、无新检索、未增加阅读范围。

另复核031实际原稿PDF8“interweaved spectra→exclude identical-configuration MχD”的句子：它是**作者针对D3/D4的解释性推断**，不是可推广的谱交织排除同配置的一般定理。031报告并未复述该排除为定理，已有输入/模型/推断边界适当，**031报告文字no-op**；本次仅在033回执中登记这项范围核查。
