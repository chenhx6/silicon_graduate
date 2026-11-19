---
type: source
title: "Shimada 2015 - Angular-momentum projection and high-spin rotational states"
aliases: ["Shimada doctoral thesis 2015", "Mitsuhiro Shimada projection thesis"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis-theory
reading_depth: read
title_original: "Microscopic study of various high-spin rotational states by the angular momentum projection method"
authors: ["Mitsuhiro Shimada"]
year: 2015
institution: "Kyushu University"
doi: "10.15017/1654644"
url: "https://doi.org/10.15017/1654644"
canonical_source: "Shimada, doctoral thesis, Kyushu University institutional repository, own 2015 doctoral designation"
raw_file: "raw/theses/gpt/query/20261119-international-nuclear-structure/W2916499830.pdf"
raw_sha256: "63c0784e2b1b520af9d179ea361b67a19985acb1e6ae086c55baefeace92d0bd"
raw_storage_status: "archived-local"
archive_required: true
nuclei: ["24Mg", "30Mg", "32Mg", "40Mg", "164Er", "152Dy", "163Lu", "128Cs", "104Rh"]
tags: ["HFB", "angular-momentum-projection", "GCM", "multi-cranked", "wobbling", "chirality", "thesis"]
---

# Shimada 2015 - 角动量投影方法与高自旋转动谱微观研究



## Bibliographic Record
- **题名**：Microscopic study of various high-spin rotational states by the angular momentum projection method（基于角动量投影方法的各类高自旋转动激发态微观研究）
- **著者**：Mitsuhiro Shimada（原件署名：嶋田 充宏）
- **学位授予机构**：Kyushu University（九州大学大学院理学府物理学专攻）
- **学位类别与年度**：博士学位论文，2015年（仓储自身DOI登记：10.15017/1654644，未从外部目录猜测确切授予日期）
- **原件存档与哈希**：本地归档于 `W2916499830.pdf`，SHA-256为 `63c0784e2b1b520af9d179ea361b67a19985acb1e6ae086c55baefeace92d0bd`。

## Scope and Reading Depth
本账本综合论文全文PDF 1–110及本次补核重点，覆盖全部理论框架（第2章）、低自旋同位素性质（第3章）、多推转组态混合投影与稀土高自旋（第4章）、三轴形变摆动带与手征双带（第5章）及总结（第6章）。
- **核对约定与印刷页码校正**：全书PDF 1–11为前置辅页，正文第1页始于PDF 12（即实际打印页号为 $\mathrm{printed} = \mathrm{PDF} - 11$）。此前“PDF $- 7$”标签是管理层准备错误；原请求/返回保留，不静默改provenance。本页所用定位按实际PDF核对，并补核错位造成的GCM、Mg图表、s带、负gamma/Gogny与104Rh任务缺口。
- **阅读深度定位**：七个主单元实际覆盖PDF1–110，另有七项定向补核与草稿写作；主单元中的partial不因页数齐全而自动通过。管理层核关键原页后按选定证据集成，记为read而非deep-read。
- **Not covered**：未运行作者HFB/AMP/GCM程序、未复现所有范数阈值与基组收敛测试、未数字化全部曲线、未逐篇核读引用实验原件。只做明示的非正交矩阵代数例；没有运行PDM。
- 不认证未提供的程序语言、源码开放状态或完整实现正确性，也不把范数矩阵校验当独立实验。

## Summary
本论文以微观核多体理论中的三维角动量投影技术为核心，针对平均场对称性破缺态不具备守恒自旋这一本质局限，系统发展并检验了多种超越平均场的多体方法。主要内容包括：
1. **理论与低自旋应用**：在离散生成坐标法（GCM）框架下推导三维欧拉角投影及四极形变混合投影的Hill-Wheeler广义本征方程，明确指出范数算符（重叠积分）非正交导致的度规性质，建立集体振幅规范；将Gogny-D1S自洽投影应用于中子富集Mg同位素基带结构与半径形变突变。
2. **多推转组态混合投影方法（Multi-cranked GCM）**：叠加不同推转频率$\hbar\omega_{\mathrm{rot}}$下的角动量投影态，改善所测算例的惯量自旋依赖。$^{164}\mathrm{Er}$的g带和s带分别计算后比较交叉，交叉自旋比实验高约$3\hbar$，s带惯量仍偏大；这不是完整耦合g+s空间中的反交叉复现。$^{152}\mathrm{Dy}$及稀土基带的比较也限于本文输入与算例。
3. **三轴核模式**：Woods-Saxon加可分离剩余相互作用与Gogny计算产生163Lu类声子多带；作者在其形变和轴约定下认为正gamma结果更符合所讨论的数据，但定量符合并不满意。128Cs/104Rh的形变参数经搜索选定以得到近简并双带，电磁交错支持作者的模型解释，不等于实验唯一确证或全论文无调参。

## Key Results
| ID | claim_kind | evidence_level | locator | statement |
|---|---|---|---|---|
| SH15-1 | formulation | analytical-derivation | PDF 25-27, printed 14-16 | GCM投影方程写为广义本征方程$\sum_{K'n'}\mathcal{H}^I_{Kn,K'n'}g^I_{K'n'}=E^I\sum_{K'n'}\mathcal{N}^I_{Kn,K'n'}g^I_{K'n'}$，原始权重$g$非概率振幅，归一化集体振幅由$f=\sqrt{\mathcal{N}}g$给出，范数截断为避免零模数值奇异的算法选择。 |
| SH15-2 | model-result | direct-original-pages | PDF35–39 | Mg的形变混合影响能级比和B(E2)，rms半径在所测试的弱推转设置下较不敏感；图3.8的实验半径由反应截面换算，图3.9的B(E2)为0+到2+。不是实验直接测定唯一内禀形状。 |
| SH15-3 | boundary | source-explicit-statement | PDF 54, printed 43 | $^{40}\mathrm{Mg}$计算表明其具有显著四极形变（$\beta_2=0.334$），但论文明确指出转动谱在本文当时无实验转动谱可供比对，不可宣称高自旋实验符合。 |
| SH15-4 | methodology | numerical-demonstration | PDF 73-77, printed 62-66 | 多推转投影方法成功计算了$^{164}\mathrm{Er}$的s带（选取4个频率点$\hbar\omega_{\mathrm{rot}}=0.25\sim 0.40\,\mathrm{MeV}$，截断$10^{-8}$），推转频率上限并不存在普适0.20 MeV限制。 |
| SH15-5 | model-comparison | direct-original-pages | PDF74–77、106 | 164Er模型交叉在I约18，比实验高约3hbar；作者将s带惯量偏大与该计算的中子配对消失联系，非本任务重算的因果量化。 |
| SH15-6 | author-interpretation | direct-original-pages | PDF90–94 | 作者比较所选gamma=0、30、-30、-90度参考态后，认为正gamma能量与电磁趋势更符合163Lu数据。该判断依赖轴、形变定义及参考态，不能把gamma符号当跨模型的唯一模式判据。 |
| SH15-7 | interaction | microscopic-calculation | PDF 94-96, printed 83-85 | Gogny-D1S全微观自洽投影重现了$^{163}\mathrm{Lu}$的多重声子带结构与激发能下降趋势；因形变采用核密度分布二阶矩定义，自洽平衡形变$\gamma=11.2^\circ$不同于势场形状定义的$18^\circ$。 |
| SH15-8 | prediction | numerical-demonstration | PDF 101-104, printed 90-93 | 在无推转三轴内禀态下，奇奇核$^{104}\mathrm{Rh}$（搜索选定$\beta_2=0.25, \gamma=-30^\circ$）于$I\ge 16\hbar$出现近简并$\Delta I=1$双带及剧烈的$B(M1)_{\mathrm{IN}}/B(M1)_{\mathrm{OUT}}$奇偶交错。 |
| SH15-9 | limit | parameter-search | PDF 98-104, printed 87-93 | $^{128}\mathrm{Cs}$与$^{104}\mathrm{Rh}$的手征简并带均建立在针对双带搜索的形变参数之上，理论简并自旋均高于实验，且模型涌现不等于独立实验证实。 |

## Model and Evidence Chain

完整H的旋转不变性与HFB参考态的对称性破缺不同（PDF23–26）。
投影K混合与生成坐标混合都通过非正交变分问题求解：
\[
H^I g=E_I N^I g,\qquad g^\dagger N^I g=1,\qquad f=\sqrt{N^I}g.
\]
这是投影试探空间中的动力学求解，不自动得到精确多体解或严格I(I+1)谱。
作者的规范化集体幅度不是对内禀构型的唯一、基组无关实验概率。

多推转方法取
\[
|\Psi^I_M\rangle=\sum_{nK}g^I_{nK}P^I_{MK}|\Phi(\omega_n)\rangle.
\]
它将不同频率参考态中的响应纳入所选试探空间，并不保证补全所有关联。
164Er基带例选取五个hbar*omega=0.01、0.05、0.10、0.15、0.20 MeV，
norm cut-off为10^-11（PDF43–44）；s带另用0.25、0.30、0.35、0.40 MeV，
阈值10^-8（PDF74）。两套空间分开求解，不能混同完整g-s耦合反交叉计算。
四至五个参考态足够是本文所测案例的收敛结论，不是普适保证。

163Lu的类声子谱、带间E2/M1与128Cs/104Rh的近简并、M1交错属于模型结果
与作者解释；投影本身不提供普通空间“手征宇称”量子数，也不保证双带简并。
128Cs输入beta2=0.3、gamma=-30度，104Rh为0.25、-30度，均未推转，
且是为寻找双带搜索得到（PDF98–101）。这与Mg章沿用既定Gogny-D1S、
不作逐核微调的说明必须分开。

## Competing Interpretations and Limitations
1. **多推转频率选取的非变分完备性**：多推转频率集合$\{\omega_{\mathrm{rot}}^{(n)}\}$是人为选定的离散采样点，而非完全自由变分求解的结果。虽然文中测试显示取4至5个频率后能量谱呈现数值饱和，但频率集合的选择依赖物理先验经验。
2. **s带与配对处理**：164Er s带这里用的是Gogny-D1S推转HFB，不是第五章可分离单极配对模型。该实现中中子配对消失，作者将其与惯量偏大联系（PDF74、106）；不据此把全部偏差唯一归因或推断所有实验核都发生同样塌缩。第四章采用Slater库仑交换近似与第三章的精确处理也需分别记录（PDF42），不能称精确交换算符本身“物理虚假”。
3. **带交叉的范围**：g/s能量曲线比较表明模型给出了交叉位置，但本文这项比较未量化在统一g+s空间中的非对角耦合。不能仅凭交点声称已经预测了全部混合、反交叉幅度或退相干。
4. **手征态简并的参数敏感性与起始自旋滞后**：在$^{128}\mathrm{Cs}$与$^{104}\mathrm{Rh}$中，手征双带的出现并非全自洽势能面极小化自发驱动的结果，而是作者人为固定形变参数（如$\gamma=-30^\circ$）并扫描得到。理论预测的双带近简并发生点（$I\approx 16-17\hbar$）明显滞后于实验观测自旋区间，且缺乏多推转组态混合以处理高自旋核芯转动极化。
5. **电磁量与模式推断**：不以M1比值必须为零/无穷或带间E2必须严格禁戒作为所有真实核的门槛，也不把近简并加交错当作排除全部竞争解释的充分条件。未证明左右手参考态正交时不能直接套1/sqrt(2)归一。163Lu实验仅测得某些I到I-1分支，不等于I到I+1严格为零（PDF89）；Eq.5.30的印刷声子强度关系仍有需对照之处，本任务未将其编码或静默更正。

## Extracted Pages
- **PDF 25–28 (printed 14–17)**：离散GCM生成坐标法框架，Hill-Wheeler广义本征方程推导，集体概率幅归一化定义$f=\sqrt{\mathcal{N}}g$与范数截断准则；Gogny-D1S有效相互作用形式与参数表。
- **PDF 36–39 (printed 25–28)**：Mg同位素低自旋微观计算结果，包括基带概率分布图、能级比$E(4^+)/E(2^+)$、电四极跃迁$B(E2)$以及rms核半径（图3.8实验值由反应截面换算）对四极混合与time-odd分量的依赖关系。
- **PDF 54 (printed 43)**：不稳定滴线候选核$^{40}\mathrm{Mg}$的形变内禀态性质（$\beta_2=0.334$，配对完全消失）与多推转角动量投影基态带计算，原文明确陈述其转动能谱尚无实验数据。
- **PDF 73–77 (printed 62–66)**：稀土区$^{164}\mathrm{Er}$基态带与s带计算，展示四频率多推转组态混合、g-s能带交叉位置（$I\approx 18\hbar$）、中子对隙在$\hbar\omega_{\mathrm{rot}}\ge 0.25\,\mathrm{MeV}$处的消失以及转动惯量与实验偏差分析。
- **PDF 90–97 (printed 79–86)**：奇$A$核$^{163}\mathrm{Lu}$三轴超形变摆动激发，对比分析$\gamma=0^\circ, 30^\circ, -30^\circ, -90^\circ$四类取向下的能量递减/递增特征与跃迁比；展示Gogny-D1S全微观自洽投影计算与密度定义形变对比；手征几何三维正交取向图式与$B(M1)$交错选择定则。
- **PDF 101–104 (printed 90–93)**：奇奇核$^{104}\mathrm{Rh}$无推转微观三维角动量投影计算，展示形变参数搜索选取（$\beta_2=0.25, \gamma=-30^\circ$）、双带近简并现象（$I\approx 16\hbar$）及带间/带内$M1$跃迁几率比奇偶交错震荡。
- **PDF 105–106 (printed 94–95)**：论文全文总结，系统回顾低自旋Mg同位素、多推转混合投影法、稀土高自旋及三轴奇特转动（摆动与手征）的方法成效与局限。

## Knowledge Impact and Learning Decision

- **Revises**：[[angular-momentum-projection-and-peierls-yoccoz]] 原稿把完整H与平均场混淆、把投影写成严格刚体谱并给出无依据固定30%惯量差；本轮按原页订正，旧toy不再作微观物理实证。VAP/PAV中英文顺序亦订正。
- **Supports / limits**：[[a130-rewrite-projection-selection-and-metric-truncation-20261113]] 的K/M、非正交度规和小范数截断边界得到实例支持；本文相互作用、频率与范数阈值不能跨案例替用。
- **Persistence**：本来源与AMP概念页，并在概念页对Li2016、Gu2007、Shimada三个理论来源作轻量阶段综合；区分拟合输入、检验量、对称性与动力学，不作模型排名或独立实验计票。
- **Audit boundary**：初始任务包页码错误归管理层；两个已返回JSON的格式问题由缓存修复，未重发成功阅读。逐项科学补核与来源草稿均经管理层原页核验和选择性接纳，不把worker所有说法当事实。未运行作者代码、原件实验重分析或PDM。
