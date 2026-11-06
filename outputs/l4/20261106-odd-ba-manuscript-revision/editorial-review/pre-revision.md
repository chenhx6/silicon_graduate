**Pre-revision editorial review — 6 November 2026**

**Recommended central claim**

> A quadrupole diagnostic that has converged within one intermediate-spin channel can remain strongly sensitive to particle–core coupling. Its evolution alone therefore does not establish a change in intrinsic charge shape.

建议围绕这一条贡献重组。固定形状粒子—转子反例负责排除“proxy 变化必然来自形状变化”的推断；IBFM 路径负责展示静态／非弹性强度和有符号环怎样随耦合重排；源码能谱复核及异能态检验分别限定实现一致性和物理适用范围。它们不是四个并列发现，也不构成两种模型对同一真实核形状的独立实验确认。

本轮按英文研究稿的论证结构审查处理，沿用 EPJA 定位；以下篇幅建议是编辑判断，不是期刊字数规定。只审查已有材料并提供改写建议，没有修改稿件或执行新分析。

**读取范围**

- 当前 `main.tex`，303 行，SHA-256 `0176dc9512ab530b1614fbef526e031a0496bffe3719832729d169af635987db`；当前 `controls.tex`，130 行，SHA-256 `ba03a6bbb8fca5292859e9b1dadc256a71db70add8cb71407b2d43de08d8c7f1`。
- [固定形状知识笔记](/workspace/wiki/knowledge/research-notes/fixed-shape-particle-rotor-quadrupole-proxy-control.md:20)、[135/137Ba 来源能谱笔记](/workspace/wiki/knowledge/research-notes/ba135-ba137-source-energy-replay-boundary.md:19)、[137Ba 异能态网络笔记](/workspace/wiki/knowledge/research-notes/ba137-isomer-e2-network-validity.md:19)。
- [四极通道先例集合](/workspace/wiki/knowledge/sources/quadrupole-invariant-spin-channel-precedents.md:56)。本轮未扩大检索，也未重新宣称读完该集合中的全部原件；新颖性措辞按其明确 locator 和适用范围限定。

**正文的最短论证链**

| 顺序与建议英文标题 | 段落任务 | 正文必须出现的证据 |
|---|---|---|
| 1. Introduction | 从 E2 形状解释进入已有通道指标，提出具体推断问题 | 先例已证明通道敏感性；本稿追问在严格固定电荷几何时能发生什么，并分析一个有界 IBFM 应用 |
| 2. Definitions and controlled comparisons | 统一两模型中的诊断定义及两类“完整” | \(q_2,q_3,r,S_n,C_n,z_n,c_n,f_n\)；完整磁多重态；全模型闭合与全 \(J+2\) 通道分开；两种 Hamiltonian/charge 约定的最简定义 |
| 3. A control at fixed intrinsic charge shape | 首先给出可独立成立的反例 | 固定电荷张量、\(\gamma=20^\circ\) 和惯量；\(q_2=1,q_3=0.5\) 的算符恒等式；\(z_{\rm all}:0.322617\to1.026250\)，末点角度未定义 |
| 4. Redistribution in the odd-Ba model | 从存在性反例进入定量机制 | 五核链压缩背景；\(^{135}\)Ba 固定算符 \(\Gamma_0\) 路径；静态／非弹性份额；\(S_\infty,C_\infty\) 及完整有符号环的补偿／抵消 |
| 5. Interpretation and empirical limits | 说明可以怎样使用结果，以及为何不是实际核形状裁决 | 算符替换／条件定标可以改变甚至使完整角度失效；静态矩比较；\(R_{\rm stat}^{(1)}\) 预测与数据缺口；正文保留异能态网络失败 |
| 6. Conclusions | 回答引言中的同一个问题 | 收敛、通道覆盖、耦合响应和形状换算须分开；固定形状控制成立，IBFM 应用仍受经验边界限制 |

固定形状结果应成为 Results 的首项实质证据，不能只在现有“Numerical controls”末尾增加几句。当前 [主稿 lines 119–130](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:119) 的轴对称 \(K=J\) 和 spectator 控制可以缩为方法校验及附录入口，让新结果承担“固定非轴形状、固定初始自旋、改变耦合”的明确任务。

正文保留两个区分即可：在刚核模型中几何是固定输入及算符恒等式；在 IBFM 中保持算符不变而改变 Hamiltonian，得到的是强度网络重排，不能据 \(q_2\) 变化较小证明几何不变。刚核控制的 \(C\) 与 IBFM 的 \(\Gamma_0\) 不是同一归一化参数，\(\mathcal Q=1\) 的控制量也不能直接与 \(eb\) 单位的 Ba 值拼接。

**可直接采用的英文新颖性段落**

> Previous work has established coupling-dependent E2 indicators in odd nuclei \cite{Nomura2016} and the sensitivity of microscopic quadrupole estimates to the retained matrix-element network \cite{Rouoof2025}. Reduced matrix-element ratios can also provide useful shape information within specified rotational regimes \cite{LawrieOrce2025}. Here we examine a specific inference: whether convergence within the selected \(J+2\) channel is sufficient to interpret its evolution as a change of intrinsic charge shape. A rigid-core particle–rotor control holds the charge geometry fixed while varying the particle coupling. A separate odd-Ba IBFM calculation resolves the static, inelastic and signed-loop contributions along a controlled coupling path. Together, these comparisons quantify how channel convergence and coupling sensitivity enter the shape interpretation.

该措辞将贡献落在具体比较及机制，不使用 “first general-spin invariant”“new universal shape measure”“correction of Nomura”或“proved unchanged Ba deformation”。先例集合中 N16 已有奇核弱／强耦合与通道指标差异；R25 已有较大网络与实验子集比较；F26 与同系列结果有依赖，不能另算独立确认；L25 则说明受限量可以在适当条件下有效。正文引用对应原论文，不引用集合页的本地 citation key 作为一篇新科学文献。

**从反例进入 IBFM 的桥接句**

> The fixed-shape control establishes that angular coupling can change the selected diagnostic without changing the intrinsic charge tensor. We next examine the same diagnostic in an odd-Ba IBFM family, where a coupling intervention resolves the redistribution of static strength and signed E2 paths. The IBFM calculation does not impose the rigid-core geometric identities, so near-constant \(q_2\) is not used as evidence of invariant intrinsic geometry.

两部分共享问题和诊断定义，贡献保持单一。正文不需要分别展开一套完整转子综述和一套 IBFM 综述。

**Isomer 限制的篇幅与位置**

建议放在 Discussion 末部一个短小节，题为 **Empirical reach of the Ba reconstruction**。保留约 **150–200 个英文词＋一条上界式**，不另起完整“异能态发现”Results 主线。其失败及对稿件解释的影响必须在正文可见；28 条强度、14 个上界、全部开放支路、单位推导和映射表放附录。

可用正文：

> A separate high-spin test limits the empirical reach of the Ba reconstruction. For each of the two tested \(19/2^-\) model parents, the sum of radiative rates over all energetically open E2 branches gives
> \[
> T_{1/2}\leq \frac{\ln 2}{\sum_f\lambda_{\gamma,f}(E2)}.
> \]
> Across the seven specified operators, the least restrictive bound is \(0.281\) ps, far below the reported \(589(20)\) ns half-life of the tentative \(^{137}\)Ba isomer \cite{Vogt2017PRC95_024316}. These unchanged model decay schemes therefore cannot represent that isomer under the tested state identifications, even when one selected strength approaches the reported \(B(E2)\). The bound uses model transition energies; omitted conversion and other decay rates can only shorten the lifetime for the same scheme. Agreement with the source's displayed energies through \(17/2\) does not establish the required \(19/2\) assignment or electromagnetic network. This failure limits the spectroscopic application of the reconstruction. It does not directly invalidate the initial-\(11/2\) scalar calculation, whose rank-two intermediate spins extend only to \(15/2\).

证据定位为[异能态知识笔记 lines 91–118](/workspace/wiki/knowledge/research-notes/ba137-isomer-e2-network-validity.md:91)及[来源能谱范围 lines 99–107](/workspace/wiki/knowledge/research-notes/ba135-ba137-source-energy-replay-boundary.md:99)。不能删去“用模型自身能量”“在预设态识别下”等条件，也不能把观测半衰期和由其提取的 \(B(E2)\) 当成两项独立似然证据。

这里的七算符是 **primary、core-only、五个经验再定标算符**；它们不是既有 35 设置扫描中的七种算符／刻度处理。两个试验族应分别命名和定位。

摘要最后用一句限定即可，例如：

> A failed high-spin isomer check limits the spectroscopic reach of the Ba application, while the fixed-shape control establishes the inference boundary within its declared model.

无需在摘要再列完整异能态能级、两种映射、\(B(E2)\)、所有寿命上界及倍率。结论同样保留一句适用性限定，避免重复讨论段。

**附录与正文取舍**

| 现有／新增材料 | 处理建议 | 正文保留什么 |
|---|---|---|
| 固定形状五点的 all-\(J+2\) 结果 | 核心结果留正文；\(n=1,5,10,\mathrm{all}\) 全部20组合放附录 | 固定几何恒等式、all 通道变化、未裁剪越域值及该初始自旋的完整覆盖范围 |
| 轴对称 \(K=J\)、spectator、D2、Euler 积分和重相位检查 | 合并进数学／数值附录，保留全部验证记录 | 方法中一个简短验证段；不反复用不同测试数量证明同一物理主张 |
| 当前 Fig.1 链趋势与 Table 2 重复数字 | 选择一处为完整主报告位置 | 可用链表 \(A,q_2,c_5,f_5,r,z_\infty\) 承载五核背景，\(z_5\) 与详细截断序列放附录；正文仍报直接检验三次量收敛的范围 |
| 当前五核自旋份额图、\(^{135}\)Ba 环分解和 \(\Gamma\) 路径 | 优先保留路径图及一个机制图／面板；其余全链分解放附录 | 静态与其它同自旋项的区别；\(S,C\) 变化；同一 \(q_2^{3/2}\) 分母下的 signed-sector 补偿 |
| 35 个算符／刻度设置 | 完整表放附录 | 改变解释的事实留正文：越域不稳健、符号／趋势可翻转；说明这是条件敏感性，不是后验 |
| 五个经验算符再定标分支、当前 Table 3 | 全分支表可移附录，禁止删掉不利分支 | 静态矩改善不保证完整 \(r\) 在实角域；明确 \(^{135}\)Ba 未参与该定标及共享来源／协方差边界 |
| \(\Gamma\)-\(Q_s\) 匹配四点 | 留在现有附录 B，正文最多一句交叉引用 | 若提及“匹配后分离仍在”，同时保留谱学代价，不能只展示静态矩改善 |
| \(^{135,137}\)Ba 源码12点、矢量提取和few-keV差异 | 全表和提取方法放实现附录 | 方法或适用范围中两句：排序一致、最大差1.896／3.128 keV；未验证 \(19/2\)、高同自旋态或作者EM运行 |
| 异能态单位与率审计 | 详细推导、所有配对与支路放专门附录 | 上述正文失败结论和条件上界式，不能整项藏入附录 |

图件以 **2–3 张核心证据图＋一张精简链表** 为编辑起点：固定形状控制、IBFM 耦合路径、必要时单列 signed-loop 分解。保留数据完整性不要求正文保留每一张分析图。精确 Hamiltonian 参数表与完整算符定义可集中于模型附录，但正文仍须给出两种控制各自改变及固定的量。

**对当前稿的具体压缩动作**

- 用新的“固定形状控制”结果段替换轴对称与 spectator 控制在正文中的扩展演示；不在现有控制段后无限追加。
- 将 [main.tex 的静态／三次环段](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:165) 与 [controls.tex 的 \(\Gamma\) 路径解释](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:34) 连续组织。端点静态份额、\(S,C\) 和完整环总和各报告一次，之后只解释它们之间的关系。
- 把目前“源码未精确复现”与新增“显示能谱近似一致”合成一个分层说明，避免读者误以为二者冲突；能量相近和 EM 未复现可同时成立。
- 保留 \(R_{\rm stat}^{(1)}\) 的定义、方向因子和预测身份，压缩实验可用性列举。Vogt 寿命归属与新的异能态失败合并交代，不先长篇说它与分母无关，再另起长篇引入同一数据。
- Discussion 负责解释两模型之间能／不能迁移的结论及物理适用范围，不再逐项重报全部能量、角度和饱和百分比。

本轮未改稿，故没有实际改写前后字数统计；上述是下一版的取舍方案，不是已完成修改的记录。

**第二轮只读 review 的核对重点**

1. 新摘要、Results 首项和结论是否围绕同一推断问题，且都保留“刚核几何固定不等于 IBFM 几何固定”。
2. 两个模型的耦合参数、charge 单位和完整性范围是否始终分开；全 \(J+2\) 通道是否未被写成全核闭合。
3. 算符依赖和异能态失败是否在正文可见，且没有把全矩角当作普遍物理真值。
4. Source replay 是否明确停在显示子集，不把few-keV一致扩展到 \(19/2\) 态映射；同源实验量和同系列先例是否没有重复计票。
5. 移入附录的全部分支与控制是否仍可定位，正文数字是否有唯一主要报告位置。

**本轮止于结构与措辞建议。** 等待用户提供修订后的 `main.tex/controls.tex` 再作第二轮只读审查；不自行改稿、开新方向或扩展模型。本次唯一写入为本文件，不修改知识页、共享文件或既有报告，不提交 Git。
