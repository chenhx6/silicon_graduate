**Second-round editorial/scientific review — 6 November 2026**

**结论：当前阅读快照没有未解决的 must-fix 科学错误。** 固定形状控制在 Results 首项给出明确反例，IBFM 路径随后解释静态强度与带符号 E2 环的重分配，两者已围绕同一个推断问题组织。经验算符分支与异能态失败仍在正文限定适用范围，移入附录的内容没有掩盖不利结果。沿用既定 EPJA 定位，当前文本可作为一篇贡献集中的、有条件的模型研究稿进入收尾审查。

本轮结论限于四个 TeX 文件的定义、论证、数字转述及边界一致性，结合上一轮已读知识笔记与先例判断。没有检查正在构建的数据包、执行重放、运行模型、测试或编译 PDF；文中算法检验精度仍是稿件报告的结果，不是本轮重新验证的精度。

**Must-fix：无遗留项；一项公式转写问题已关闭**

最初阅读时，转子 Hamiltonian 的转动项与单粒子场之间缺少加号。主代理修正后，已重新读取[当前附录 C](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/revision-appendices.tex:6)，现为

\[
H(C)=\sum_{k=1}^{3}A_kR_k^2+C\,1\otimes Q_j(\gamma),\qquad
R_k=I_{k,\mathrm{right}}\otimes1-1\otimes j_k .
\]

加号、\(R_k\) 定义与场的分母 \(4j(j+1)\) 均已正确显示。无量纲角动量、\(A_k=\hbar^2/(2\mathcal J_k)\) 和以 MeV 表示的 \(C\) 相容；\(C=0\) 保留转动 Hamiltonian。[刚性电荷张量的拆行](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/rigid-control.tex:6)也保持了原来的 \(a_0=\cos\gamma\)、\(a_{\pm2}=\sin\gamma/\sqrt2\)。这关闭的是文字公式问题，不构成对算法或数据是否变化的独立验证。

**本轮关键核对**

| 项目 | 当前判断与定位 |
|---|---|
| 固定形状控制的证明范围 | [rigid-control.tex](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/rigid-control.tex:11)以电荷算符恒等式固定 \(q_2=1,\ q_3=0.5\)，故 \(r=0.5\)、折叠角 \(20^\circ\)；全 \(15/2\) 通道的 \(z:0.32262\to1.02625\) 因而具有清楚的反例意义。正文没有把它转移为“IBFM 几何不变”，也没有把 \(C\) 等同于 \(\Gamma_0\)。附录明确完整性只覆盖初始 \(11/2\) 所需的中间态，保留了有限采样的分支跟踪边界。 |
| 链表、耦合路径与数值方向 | [链表和解释](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:138)区分了 \(c_5>99.5\%\) 与 \(f_5=20.00\%–28.90\%\)，新增 \(q_2\) 阻止把弱变化的归一化三次矩误读成恒定集体强度。[\(\Gamma_0\) 路径](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:12)的 \(q_2\) 范围 0.67662–0.69413 确为小于 2.6%；静态份额从 **0.0091%** 升至 33.69%，不能误写成初值 0.0091 的份额。\(S_\infty\) 减小、正的 \(C_\infty\) 增大，与 \(z_\infty:0.08795\to1.02414\) 的方向一致。 |
| 三次矩符号与定标边界 | [带符号分解](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:173)中，正负扇区的抵消、共同 \(q_2^{3/2}\) 分母下的 \(-0.11467+0.06415=-0.05052\)，以及费米子项使负的完整三次矩趋近零，方向相容。以已舍入的绝对量相加出现末位约 \(10^{-5}\) 的差别不构成符号错误。[定标限制](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/controls.tex:74)仍明确：改善 \(Q_s(135)\) 的 0.923/0.915 分支给出 \(r=-1.093/-1.096\)，完整矩角也可以未定义。所有五分支与来源依赖、未知协方差均在附录保留；没有把条件定标写成独立验证。 |
| 方向因子与异能态失败 | [Discussion](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:208)把 589(20) ns 归于上部 \(19/2\) 态，保留了 \(T_{1/2}\leq\ln2/\sum\lambda_\gamma(E2)\) 的正确方向。最大上界 \(2.811\times10^{-4}\) ns 即约 0.2811 ps；结论限于不变的模型能量、振幅和被测试的态识别。附录的 \(0.46(3)\) W.u. 转换、\(19/2\leftrightarrow15/2\) 的 \(20/16\) 因子，与 \(R_{\rm stat}^{(1)}\) 所用 \(16/12\) 及偶芯 \(0\leftrightarrow2\) 的 5 分别正确。寿命及由同一衰变提取的强度没有重复算作独立证据。 |
| 静态比与谱学代价 | [静态比定义](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:235)保留 \(D_0=(5/16\pi)Q_s^2/(55/91)\)、预测值 2.2722/1.3565，以及第一态约占该模型通道 74% 的区别。没有用 \(19/2\) 寿命代替 \(15/2\to11/2\) 分母，也没有拼出“实验分子／模型分母”的实验比值。附录 B 保留中心静态匹配使能量间隔由 691.9 降至 526.6 keV、偏离暂定实验连接 682.3 keV 的代价；0.3684 与 0.4322 MeV 分别限定为中心匹配和全部四点的最大变化，未混用。 |

这张表是文本一致性核对，不是对数据文件或来源原件的新一轮审计。RME 互易关系、三次矩的 \((-1)^{2J}\) 相位与既有定义保持一致；本轮没有重推实现。

**单一贡献和经验边界：结构调整有效**

三张正文图分别承担固定形状反例、静态／带符号通道分解、固定算符 Hamiltonian 干预，分工清楚。链表新增 \(q_2\) 后已经承载全链背景，原链趋势图不再进入正文，重复明显减少。

[Discussion 的核心段](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:189)把已有先例与新增比较分开：通道依赖和不变量恒等式已有先例，本稿的贡献是把严格固定几何的控制与可解释的 IBFM 干预结合，定量显示收敛的选定通道指标仍有耦合敏感性。当前措辞没有提出新的通用形状定理、优先权主张或对原作者电磁结果的纠正。

异能态检验已压缩为约两段加一条上界式，随后自然转入可检验的 \(R_{\rm stat}^{(1)}\)。这个比重合适。失败在正文可见，其详细映射、单位和开放支路留在附录；不必把它扩展成第二项物理发现，也不宜继续压缩到只剩一句泛泛的“模型有局限”。源码显示能谱的接近没有被用于认证 \(19/2\) 态映射，高自旋失败也没有被写成对初始 \(11/2\) 三次环的直接否定。

**可选修改；均不阻断本轮科学结论**

1. **统一摘要与正文的论证顺序。** [摘要](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:13)仍先介绍 IBFM，再说独立转子控制 “then”；引言路线图也保留此顺序。可以先给固定电荷几何反例，再引出 IBFM 的具体机制，使读者按 Results 的顺序理解贡献。可采用的短桥接为：“A rigid-charge particle–rotor control establishes the coupling sensitivity at fixed intrinsic geometry. A separate fixed-operator IBFM intervention resolves the associated redistribution of static strength and signed E2 paths.” 无须扩大新颖性措辞。

2. **将一处几何表述落到算符假设。** [main.tex:138](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:138)的 “whose wavefunctions do not obey the rigid-charge identities” 建议改为 “which does not impose the rigid-charge operator identities”。恒等式是算符层面的约束，这样比对波函数作绝对判断更准确；后面的 Discussion 已有正确限定。同理，单壳附录中的 “used in all calculations” 可缩为 “used in the IBFM calculations”，避免把独立转子控制也字面包含进去。

3. **仅压缩重复的端点细节。** [main.tex:165](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/main.tex:165)与 controls 中重复出现 135Ba 静态份额，是截面描述与干预路径两种用途，保留一次简短回指即可。若还需缩短，正文可保留正负总抵消及共同分母的“选定扇区／其余扇区”结果，把个别 \(11/2\)–\(11/2\)、\(11/2\)–\(13/2\) 扇区的绝对数值交给图或附录。不要为省字删掉共同分母分解、完整矩越域分支或异能态上界条件。

**Readiness 判断**

就本轮审查的科学叙述而言，稿件已达到可信的、聚焦的 EPJA 模型论文形态；不再需要为了维持主论点补开研究方向。其可支持的结论是指定诊断量的耦合敏感性及形状解释边界，实际 Ba 核的形状、刚软性与电磁网络仍受正文列明的限制。最终数值包和重放状态由负责该范围的审查另行确认，本报告不替代那项工作，也不预判期刊接收。

**收尾定点确认 — 6 November 2026**

仅复核以下四组收尾修改，上列可选建议 1/2 已落实；没有重启全文审查，未发现这些修改引入新的 must-fix。

1. 当前摘要与引言路线图均已先述 rigid-charge 控制，再述 IBFM 干预，与 Results 顺序一致。
2. `main.tex:138` 已改为 “does not impose the rigid-charge operator identities”；单壳附录 `main.tex:283` 已限定为 “used in the IBFM calculations”。两处均准确收窄了表述对象。
3. 附录入口前的 `\clearpage` 已移除，`\appendix` 保留；本次确认限于源文件，没有重新编译或评估分页。
4. [书目条目](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/references.bib:11)已采用 1998、World Scientific、`address = {Singapore}`，并注明重刊自 1975 年 W. A. Benjamin 版。已直接读取[本地第二卷 PDF](</workspace/wiki/raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf>)第 6 页：该页载明 1975 年初版、World Scientific 1998 年版及 Singapore 出版地址，另记 1999 年重印。当前书目信息与该版权页相容；本轮没有复编检查样式输出。

此前加号修复由**主代理**完成，报告中的责任归属已统一更正。科学结论及有条件的期刊 readiness 判断不变。

**第二轮审查原始阅读快照**

下列哈希保留第二轮完整文本审查的阅读快照，不是历史数据重放证明，也不代表上述收尾修改后的全文版本。main 与 controls 在主代理修正加号前后未变；其余两文件以当时修正后版本为准。

| 文件（均位于 `raw/writing/gpt/odd-ba-quadrupole-closure/`） | 行数 | SHA-256 |
|---|---:|---|
| `main.tex` | 348 | `6854a7d52acba910c629024d5eb0f1f00b87ca1a93e58aefd093141dd53a092c` |
| `controls.tex` | 85 | `0cba43896dccc037fb41c094cf9a26494492a809e64081eb4740d44845370991` |
| `rigid-control.tex` | 62 | `4cfadbe64b5b77a52d22fada757265625d0b09b5a5c6aefd2d54c4dfea39468a` |
| `revision-appendices.tex` | 185 | `933ea5762c6b2e2b2e92764af776c09197ff290da74401e68da89e34b3c52624` |

本轮唯一写入是本报告；未修改稿件、知识页或共享文件，未提交 Git。审查在此收束。
