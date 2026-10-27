---
type: project
title: "手征与形状共存：134Pr/135Nd/136Nd逐伙伴竞争解释矩阵"
aliases: [chirality shape-coexistence companion matrix]
created: 2026-10-26
updated: 2026-10-27
status: active
review_status: unreviewed
confidentiality: public
project_stage: formal-card-deliverable-active
nuclei: [134pr, 135nd, 136nd]
tags: [chirality, shape-coexistence, band-mixing, companion-observables]
---

# 不同核、不同pair的支持链不能拼成一条完整向量

## Agent active summary

本页为正式 Day 25 学习主线交付件：手征反例与形状共存竞争解释矩阵。系统阐明“近简并”为什么不是手征充分条件，明确区分 shape coexistence 与 chiral doublet，给出 134Pr / 135Nd / 136Nd 三核三行严格对照（直接观测、作者解释、替代解释），并建立最小 companion observables 组合与四级降级阶梯。所有新综合保持 `needs_review: true`；前序 Day 24 交付见 [[135nd-chiral-partner-resolved-evidence-map]]，133Ce 附属分析持续深入见 [[133ce-thesis-analysis-blueprint]]。

## Research Question

近能双带的哪些信息直接来自观测、哪些是作者/模型推断？crossing、configurationchange、γ-softness、bandmixing和多个形状极小能解释哪些部分特征，还需要什么可分辨的伴随量？形状共存与手征可以在不同层次/组态上同时讨论，不能仅凭带数或一个势面就作互斥二选一。

## 理论判据：近简并为什么不是手征充分条件及手征与形状共存的鉴别

### 1. “近简并”为什么不是手征对称性的充分条件

在转动手征性（nuclear chirality）框架中，核心图像是由三个相互正交的角动量分量（价质子/价粒子沿短轴、集体转动沿中轴、价中子/价空穴沿长轴）在核体固结坐标系中构成非共面的 aplanar 手征三脚架。在实验室坐标系中，通过量子隧穿恢复时间反演与轴转动联合对称性 $\mathcal{T}\mathcal{R}(\pi)$，产生一对自旋相同、宇称相同、$\Delta I=1$ 的能量近简并双重带。

然而，实验上观测到的“能量近简并”（near-degeneracy）仅仅是手征对称破缺恢复的必要表象，绝非充分条件：
1. **多准粒子带交叉（Band Crossings）制造表观伪简并**：在转动频率驱动下，不同准粒子构型（如两准粒子与四准粒子带）随频率演化发生交叉。在反交叉区域（level repulsion 与 band mixing），能级间隔会在有限自旋窗口内被强烈压缩（例如 134Pr 在 $I=13–19$ 之间经历若干 4-qp crossings，导致能隙压缩至仅 36–44 keV）。这种能级相近纯属交叉扰动引起的“伪简并”；
2. **形状共存（Shape Coexistence）偶发相遇**：同一核素在不同形变势阱（如不同 $\beta_2, \gamma$ 极小）中支持的转动带，因各自带头能量与转动惯量的差异，可能在特定自旋区恰好相遇；
3. **准自旋伙伴或 $\gamma$ 软度**：准自旋双重态或低激发 $\gamma$ 振动亦能产生能量相近的伴随带。

**充分性的核心要求**：手征双重带要求两带波函数在两个相反手征状态间对称，必须同时满足：
- 相近的角动量排列（alignment $\Delta i \approx 0$）与转动惯量；
- 相近的内禀四极矩（$Q_{0,1} \approx Q_{0,2}$）与带内绝对 $B(E2)$ 阶梯；
- 相同的 $B(M1)/B(E2)$ 比值和交错（staggering）趋势；
- 满足手征选择定则的特征带间 $\Delta I=1$ 的 $M1$ 和 $E2$ 跃迁连接。

如果两带的四极矩显著不等（如 134Pr 解混合得出 $Q_{0,1}/Q_{0,2} = 2.0(4)$）或 alignment 差达到 $2\hbar$，则表明两带内禀形状迥异，直接证伪了理想手征双重带假设。

---

### 2. 三轴形状共存与手征双重带的五维判据对照

| 鉴别维度 | 三轴形状共存（Triaxial Shape Coexistence） | 核手征双重带（Chiral Doublet Bands） | 鉴别判据与失败检查 |
|---|---|---|---|
| **物理机制与波函数** | 同一原子核由于壳效应存在多个不同的平衡形变极小值（不同 $\beta_2, \gamma$），两带属于不同势阱的转动激发 | 单一三轴形变势阱中，粒子-转子-空穴三维角动量非共面取向导致手征自发破缺，量子隧穿恢复形成手征伙伴态 | PES 计算是否有分离极小值；波函数在三主轴角动量投影是否有 aplanar 分量 |
| **内禀四极矩 $Q_0$ 与 $B(E2)$ 阶梯** | 两带具有显著不同的内禀四极矩 $Q_{0,1} \neq Q_{0,2}$，带内绝对 $B(E2)$ 阶梯不相称（常差 1.5–4 倍） | 理论上两带具有高度相同的内禀形状与四极矩（$Q_{0,1} \approx Q_{0,2}$），带内绝对 $B(E2)$ 在实验误差内相等 | 寿命测量 $\tau$ 结合分支比提取绝对 $B(E2)$；若比值偏离 1 则排他性挑战理想手征 |
| **电单极跃迁 $E0$** | 同自旋同宇称态之间若发生波函数混合，可观测到强 $E0$ 跃迁（$\rho^2(E0) \sim Z^2/R_0^4 a^2(1-a^2)[\Delta \langle r^2 \rangle]^2$） | 同自旋态之间不以强 $E0$ 跃迁为主导特征；手征恢复对称态之间受宇称和转动对称性约束 | 转换电子谱测量或内转换系数核查；强 $E0$ 存在高度支持形状混合 |
| **带间跃迁与选择定则** | 带间跃迁受到不同内禀形状波函数空间重叠小的阻尼；在远离交叉区带间跃迁极弱 | 存在特征的带间交错跃迁：$\Delta I=1$ 的 $M1$ 与 $E2$ 跃迁强度受手征算符选择定则约束，呈规律性奇偶交错 | 检验带间连接跃迁 $B(M1)_{\text{inter}}$ 与 $B(E2)_{\text{inter}}$ 是否满足交错特征 |
| **自旋与频率演化** | 随角动量增加，不同组态在各自势阱内独立演化或经历不同 crossings；通常某一形变逐渐占优（yrast 转换） | 随角动量增加，经历低自旋手征振动（chiral vibration）向临界频率以上静态手征（static chirality）的系统演化 | 检查能量劈裂 $\Delta E(I)$ 与 $S(I)$ 随自旋的演化规律及是否随自旋趋于简并 |

---

## Evidence Available

[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25P-001/002；[[lv-2019-chirality-135nd-reexamined]] LV19-D25P-001–004；[[petrache-2018-chiral-bands-even-even-136nd]] PE18-D25P-001–004为本次原件locator。既有MU07绝对EM为原实验的支持链，不由后文引用重复计票；旧review/撤回不更改。

|核/明确family|直接观测与实际实验支持|作者解释/模型|竞争路线与本源未闭合项|
|---|---|---|---|
|134Pr旧Band1/2在crossing段|原能谱/36、44keV gaps、alignment和E2分支资料由PE06分析引用；本文不是新寿命采集|两带解混合给Q1/Q2允许1.6–2.4及odd/even V约14/17keV；UC/TRS作shape对照|off-diagonal E2忽略、短段V固定；branch Ref11与τ Ref9不同。反对简单ideal-pair，不宣称全部动态手征残余被排除|
|135Nd正D3/D4|152MeVJUROGAM新谱学/多线角响应/偏振/修订Jπ；只有一个D3 B比|CDFT/PRM配置πh11粒子-g7空穴⊗νh11空穴，固定输入下谱与RMS几何支持|D4没有匹配绝对EM向量；589/649目标family与D2两行Ex局部歧义；RMS不是signed几何测量|
|135Nd负D5/D6，历史A/B谱系|MU07有双方τ/绝对EM支持；2019独立于MU07的另次采集有谱学扩展/relative比相近；与PE18可能共享campaign须另列|PRM能谱/比值有真实支持，γ22.2→20.2按39/2的比值增长选择|2019未重拟MU07τ/normalizer。相近数据与调参后比较不同于独立holdout；不抹去早期强EM支持|
|136Nd正D5/D5-C|五pair中仅此pair两成员都有实测派生B(M1)/B(E2)，误差内相近；有实际level/link/coincidence支持|C为六qp候选、β.26/γ23，TAC比值趋势支持|没有本篇新τ/absoluteB/g/Q；显式3D取向却是D3，不给D5代补；旧假SI不支持额外δ/B表|
|136Nd其余D1/A、D2/B正；D3/D*、D4/D负|有各自nearenergies/links/主带部分ratio，弱partner ratio缺|D3/D*唯一显式3DTAC aplanar例；D2/D3/D4 crossing作者提出8/6/6qp扩展|不是五pair equallycomplete；其它模型形状/组态支持相关，不能按模型名称计多票。MU08旧负Band1/2不映到正D1/D2|

这是一张三核表，135Nd/136Nd进一步分family以防合并；并不以行数或核数作证据强度评分。

采集独立性另限：LV19的新JUROGAM数据独立于MU07的Gammasphere寿命采集，并不因此独立于PE18。两文同152MeV 40Ar/0.5mg·cm⁻² Mo/相同装置描述、PE18同次135/136Nd产额及LV19转引共同setup说明支持同campaign谱系；未取得selected-event/producer manifest或共同Cov，不把各核的event子集当已证相同或完全统计独立。参LV19原PDF2及Ref38、PE18 PDF2–3。

[[lv-bingfeng-2019-chirality-136nd-135nd-thesis]]既有DD-20260910-136ND-01/02明确dependent campaign；本轮root/worker窄读physicalPDF66/printed65：同实验布居135/136Nd、同triggerless TDR记录5.1×10^10 fold≥3 pool。只确认此采集谱系，不认证相同selectedγ、各自response或Cov，也没有为新计票另建一次实验。

## Current Hypotheses

134Pr的简单ideal-pair受到分支/混合分析的实质限制，动态几何残余未被此分析排尽。135Nd负pair已有较强绝对EM支持，正pair仍主要为谱学/模型支持；136Nd以D5双方relative比最强，但不是同一pair已具全部3D几何/绝对EM。不同shape/组态与带混合是需预报和检验的竞争路线，本页未拟合出胜负或给概率。

## Analysis or Reasoning

以下推理把这些暂定假设接到具体可检验观测，不因一个源的失败取消其它核真实支持。

### 近简并、解混合与形状的逻辑层

PE06实际用E2分支与能隙在简化两带模型内解混合；2.0(4)是允许范围的简写，不是直接测得β比，也没有给Gaussian抽样定义。小gap只给|V|的条件上界，不能单独测混合角。UC/TRS有不同形状极小是模型计算，不能自动标定实验“两个刚性shape”。原文结论保留手征几何残余程度的问题，不能扩大成chirality在所有核失效。

LV19的两个family也不能按核名合并EM完整度。D3/D4正宇称和新谱学有坚实输入；缺匹配partner τ/absoluteB会限制其EM对称性检验，而不是抹掉Jπ/拓扑事实。负D5/D6已有MU07支持，2019新relative资料不自动成为原175MeVDSAM的absolutebranch输入；同核不同run需连assignment/normalizer谱系。

PE18中D5的实验ratio与D3的模型3D几何是两条不同pair的证据，不能拼成“D5实验三轴几何闭合”。C/D*的Ex、βγ与对齐是模型输出；作者承认crossing/混合尚未计算。配置对应多个极小可为[[triaxial-shape-coexistence]]提供模型解释路线，但实验模式归属需逐band/head/link/响应匹配。

### 旧136Nd绝对EM挑战的真实pair对象

[[mukhopadhyay-2008-136nd-transition-rates]]既有MU08-D18-5/6/7经024本轮原6页/五图/两表回核，与原科学更正相符，source无需再造delta。2008 Band1/2的负带EM不同，直接挑战的是它们互为同一pair的旧解释；有限低spin指纹对应后来D4/D3。不能把两条旧主带误作后来的新C伙伴。

|被检验pair|旧实测EM可提供|不能直接移植|
|---|---|---|
|旧Band1 vs Band2（后D4 vs D3）|旧母态DSAM/BR/不同absoluteE2，是真实有信息反证|不能唯一测得shape/组态或否定所有动态振动|
|新D3 vs D3-C|D3主带在匹配spin段可有旧EM anchor|未测D3-C τ，旧D4不能代它|
|新D4 vs D4-C|D4主带同上|未测D4-C τ，旧D3不能代它|
|正D5 vs D5-C|只有方法教训与观测设计类比|不同parity/配置/parent，旧负带τ/B不是D5直接反证|

原MU08为175MeV Gammasphere DSAM；主张新谱学/candidate的PE18为152MeV JUROGAM。原branch/clock/停止/feeding及pure-M1提取假设按母态绑定，不能删第三条outlet后将剩余两条归一为1。source已保TAC没有bandmixing、RPA限近谐振动与典型100–400keV模式，以及作者对各配置仍可能有chiral vibration的开放结论。本复核不是“全核无chirality”或D5无支持的新认证。

### 最小companion组合是问题设计，不是普适终判

先选一个pair和同一spin段，再比较预先固定输入的chiral/shape/configuration/mixed预测。下表用于本比较的可审查设计；完整组合也不保证模式数学唯一，缺某量更不自动否定实核手征。

[[heyde-wood-2011-shape-coexistence-review]] HW11-D25P-001–006的原件校准提供形状侧的量词：E0是有力的混合/半径组合约束，multistepCoulex及其它E2/radii/transfer可互补，但没有普适“两者全齐”或固定V必强mixing的门。低0+、非0与highspin结构的证据范围分别讨论，三核PES/RMS/TAC也不因引用此综述就变实测shape。旧未定位的186Pb百分比/50–100门已撤回，不迁入本矩阵。

|组合量|为何增加信息|缺一项时具体降级|
|---|---|---|
|母态/终态/family/Jπ与每线component身份、门/效率/ICC/未见branch界|不把近能线/同spin或未见线当同一个输入；实际LV19局部歧义说明其必要性|保留谱学candidate/已知部分观测，歧义行不作matchedEM比较；不连带否定全family|
|双方同I/段可逐态绑定的实测clock（允许jointfit/共享Cov）＋完整component-resolved BR/normalizer/response|把ratio/趋势接到absolute M1/E2尺度，检验同一ratio下共同尺度变化|仅有相对γ资料且没有其它absoluteEM约束时，缺clock只得relativeEM；缺branch/normalizer则新复算/精度仍条件化，既有publishedB支持保留|
|覆盖段的固定空间/shape/mixing模型与实际observable预报|防止每加一量就重新调γ/J/g，能对crossing/形状差别作可失败比较|只能说模型相容/conditional fit，不能说所有竞争解释已排除|
|可行且有分离预报的独立结构holdout，如同态g或Qs/另一E2形状量|磁/电/组态给互补约束；先证预测可区分再选技术|没有holdout时可能仍有等效配置；g不是每个模式普适必测条件，也不强迫ps态作TDPAD|

134Pr优先闭合原branch/clock并检验off-diagonal E2/固定V假设；正135Nd优先双方matchingEM；负135Nd优先normalizer恢复/新独立holdout；136Nd先选D5或另一个明确pair，不在不同pair间借几何/寿命。测量方法的clock、束流、停止/feeding/场标定属于各自响应合同，不能借131Ce/128Cs的时钟给高spin目标补数据。

### 非对角E2扩展：哪些条件能由ratio识别

[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25P-003是源Eqs1–5空间上的任务推导，非新fit。源以aI=αI、bI=√(1−aI²)定义Ry/ny；列依次(y,ny)、原基(1,2)，取

$$R_I=\begin{pmatrix}a_I&b_I\\b_I&-a_I\end{pmatrix},
\qquad Q_{fi}=\begin{pmatrix}q_1&q_{12}\\q_{12}&q_2\end{pmatrix},
\qquad M_{fi}=R_f^TQ_{fi}R_i.$$

所有q为同一E2振幅/transition-moment单位，实际B还需同spin几何因子；比例练习只设任意共同Qref，不指定eb绝对尺度。forward block的q12=q21是本扩展的一个额外real ansatz；Hermiticity联系forward与reverse block，不会自动令两个不同forward off-diagonal元素相等。

原打印a15=.894/a17=.118/a16=.427/a18=.099在原假设内提取，此处只作前向基线，不能当新模型的独立实测mixing。q1/q2=2、q12=0给Table-continuity out/in：17→15的ny/y为.333870/.703522，18→16为.170382/.062384，复得原表打印计算。17→15跨越原带身份交换，Table out/in为源Eq4/5的倒数；18→16不倒数，原Eγ/母态/终态标签须随ratio走。

加入q12的干涉后，原q1=q2或ai=0推出两rawratio相等的捷径不再普适。同parent τ消去、共同scale和一致basis重相位仍成立。改变q12而保持mix/算符其它约定固定，会改变预测；把Q与Ri/Rf同时一致重相位却不改变物理M，二者不是同一个操作。

对固定Q，orthogonal混合保

$$\|M\|_F^2=q_1^2+q_2^2+2q_{12}^2,
\qquad \det M=q_1q_2-q_{12}^2,\qquad \sigma_k(M)=\sigma_k(Q).$$

det符号还随已选statephase convention，det²与SVD不依这些符号。以上不变量是对固定Q作基变换，不是改变q12后数值仍恒定；Rf≠Ri时traceM也一般不保。完整同Ii/If的四个B才涉及共同几何下的全矩阵模平方和，不能跨spin任意求和。

仅两个parent的out/in比至多给unsigned列方向：写M=(√A u_y,√B u_ny)，列norm平方A/B未知、signed branch loop也未给，c=u_y^T u_ny。于是

$$\sigma_\pm^2=\frac{A+B\pm\sqrt{(A-B)^2+4ABc^2}}2,
\quad \|M\|_F^2=A+B,\quad (\det M)^2=AB(1-c^2).$$

所以比值本身不给绝对Frobenius/det/SVD；没有A/B也不给SVD比。四个unsigned widths加clock可提供模长/尺度，仍未必给branch-loop sign；完整signedM配已知Rf/Ri才可重建Q。反之若mixing独立已知且两ratio精确，两个scale-free symmetric-Q参数可在选定符号分支有局部离散解，不能泛称所有扩展都连续退化。

该分析只展示推断对原off-diagonalE2假设的依赖；没有重拟合V/Q、为1.6–2.4作Gaussian CI、改变能量H或证明equal-shape/alternative胜出。root已读脚本并重跑exit0，入口`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/two-band-em-022/kernel_checks.py`；结果kernel-results.json只为有限代数控制，不是actual134Pr likelihood/观测矩阵重放。

026独立审查与[[lange-kumar-hamilton-1982-multipole-admixtures]]既有LKH82-D24P-004/005及其末段完全相符：四B相同仍可有不同loop/SVD，loop也不是单γ的δ符号；该核心为verified-no-op，不包装新定理。操作scope再明确：本PE06块是ΔI2 E2，rank1 M1禁止，不能在这些边上虚设M1/E2 δ。别的ΔI1线的signedδ只给那一边两算符的相对phase，若无额外跨边关系，不能普遍补该E2 loop。任意单态overallphase与可约束的闭环相干组合分开；不从population寿命或普通分支的非相干相加推得已测loop。此note为有条件方法说明，needs_review:true，未赋实际134Pr相位。

### 真实thesis的relative出口可缩小缺口

[[lv-bingfeng-2019-chirality-136nd-135nd-thesis]] TH19-D25P-001–005不是旧假SI，而是同campaign另一真实文档的逐线表；本轮已在source固化3母态/14条出口与normalizer/方法字段。它补Ei/Jπ/Eγ/相对Iγ和部分角响应，不补δ/ICC/totalBR/τ/absoluteB；不是独立新采集。

D5-C20+、Ei7543.0的带内611.4与跨D5的1021.2两E2可作条件同parent比：

$$\frac{B(E2)_{\rm out}}{B(E2)_{\rm in}}
=\frac{0.6}{0.21}\left(\frac{611.4}{1021.2}\right)^5\simeq0.21979.$$

源Fig5.6/Table5.1支持其parent/端点与E2赋值，计算仍要求相对photonresponse可比/已正确修正。τ、commonreference和E2常数消去，完整totalBR不是此比的必要输入；gate/Cov未知则不报CI/absoluteB或phase，不用该数独断模式。其它混合行如672.5不能擅当E2crossover，未知出口也不删掉后重归一。

### 相邻母态增加一个实际输出约束

033沿同一原表补一个实际相邻母态：[[lv-bingfeng-2019-chirality-136nd-135nd-thesis]] TH19-D25P-006–008，D5-C21+/7927.1的714.1(.18(4))与1060.7(.8(4))分别到C19+/D519+，两路E2给条件R21=.61468102。与R20=.21978857的中心双比2.79669未含Cov/响应或coverage，不是显著性、确定trend或模式排他；仍是同campaign。它提供向同一冻结模型索取四条指定E2输出的理由，当前PRM未交这两个比的预测。

20+没有第三条打印E2可作冗余，330是M1。18+所选三个E2仅为子集，951.8 E2及1330.5上限等仍须保；同输入算出的第三比/cycle只是代数冗余。20与21属于不同Ji/Jf块，不能拼成同spin的完整2×2矩阵或sum rule。22+的812.1/1100.5行Ei印8355.1/8355.9不一，先隔离而不合并或推造R22。root原表视觉和Fraction复算见thesis-e2-paired-ratios-root-033.json，连续逻辑及输入已在本页/源页，不只在output。

### 四条真实线的联合响应合同

[[lv-bingfeng-2019-chirality-136nd-135nd-thesis]] TH19-D25P-009为任务推导，复用原表四线而非新实验。固定顺序(o20,i20,o21,i21)，令f_l=ε_true/ε_used，g_l为残余逐线选样/角接受，b_l为同单位的加性峰面积残差。一个明确合同为Ihat_l=100(q_l f_l g_l+b_l)/Qhat_373.7；理想同parent photon产额q_l=N_parent τ_parent C_E2 E_l^5 B_l。它只在各定义实际匹配时成立，门不同不能凭parent相同消掉g。

同一随机Qhat在Iout/Iin中逐实现消去，允许它与分子相关；若不同谱各自估normalizer再组合，须交真实变换，不能只据“都归一373.7”认为相同。加性b不是共同效率，即使两个b相等，分数偏差也一般不同。净numerator为正时，定义ρ_l=ln f_l+ln g_l+ln(1+b_l/(q_l f_l g_l))，则

$$\begin{pmatrix}\ln(\widehat R_{20}/R_{20})\\\ln(\widehat R_{21}/R_{21})\\\ln(\widehat D/D)\end{pmatrix}
=\begin{pmatrix}1&-1&0&0\\0&0&1&-1\\-1&1&1&-1\end{pmatrix}\boldsymbol\rho,
\qquad D=R_{21}/R_{20}.$$

J消去真正共有的全局及各parent内乘法mode，第三行=第二行−第一行，故不是三个独立约束。若未来Σρ实际可得，Σy=JΣρJᵀ；raw峰/背景/效率相关误差须在同一primitive模型内传播，不能重复加或把跨parent Cov默认0。这个log残差关系精确，换小背景线性化或从原始误差推Σρ另有近似；当前没有实际Cov/CI。

只在共同f(E)=(E/E*)^s、其它response固定的子模型中，两lnR斜率为.512982276/.395661338，lnD斜率为−.117320938。双比对这个单一平滑mode部分抵消，不排效率曲率、逐线门或加性背景；不由假定目标需大s排除一般系统学。root读calculate.py并重跑exit0，系数核验不是实验检验。

后续最小joint交付是四线不可变身份、归一前net/gross与背景/污染模型、实际gates/active mask/权重与event reuse、效率参数/full Cov及四能量Jacobian、gate/背景交叉项、373.7的真实共享变换、最终四线4×4 Cov与primitive模型对应、分布/coverage及producer/version。仅Cov矩阵也不自动认证弱峰比值的覆盖；可保完整likelihood。这个指定photon同E2比不强制先测τ/完整totalBR，不给absoluteB或完整decay认证。

### 同I E0与不同I E2块不能混成一个问题

[[heyde-wood-2011-shape-coexistence-review]] HW11-D25P-007进一步明确Eq14的配置基前提。设同Iπ二态radius矩阵T有对角R1/R2和offdiag t，Δ=R1−R2；H12=W exp(iφ)、δ=E2−E1、D=√(δ²+4W²)，令z=t exp(−iφ)=x+iy。取一致lower/upper本征态约定，同U变换给

$$A_{lu}=\frac{W\Delta+\delta x}{D}+iy,
\qquad d\equiv R_l-R_u=\frac{\delta\Delta-4Wx}{D},
\qquad d^2+4|A_{lu}|^2=\Delta^2+4|t|^2.$$

R、t、A单位length²，W/δ/D为energy，ρ²(E0)=Z² abs(A)²/R0⁴为无量纲。t=0才回源Eq14子模型；δ≠0时real x=−WΔ/δ可cancel，但δ=0时real t不能cancel非零Δ；不把该例写成所有小E0均由相消。封闭二态还有norm([H,T])²=2D² abs(A)²，A0说明块内commute，不独断“混合很小”。

这里T是同一个二态空间的Hermitian算符，U†TU与022不同Ii/If的Rf†Q Ri有本质不同。一个非简并energy-basis E0 offdiag的相位可用两本征态重相位移除，不是026的四边loop；configuration基里的tV*只抗那个已定义基的phase-gauge，不抗任意重新定义配置。即使energy-basis H/T信息完整，也还需物理定义unmixed基，不能把数学radius本征向量直接叫两个实验刚性shape。

029只为声明空间的连续推导/正定radius反例/极限控制，root读代码并重跑exit0；不选择实际核Z/R0、不提取百分比/βγ/置信区间。脚本`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/e0-two-state-029/e0_kernel_check.py`只核该代数，actual核输入与全空间依然缺。

### 136Nd直接PRM的支持与尚缺预测

[[chen-2018-four-j-shell-prm-136nd]] CQ18-D25P-001–006给good-I四single-j壳量子模型，不只是局部TAC率平均；D5使用πh11/2²g7/2^−2⊗νh11/2^−1f7/2¹、β.26/γ23/𝒥0=40/ξ.93，是PE18 C的宽轨道标签的具体模型选择。𝒥0/ξ按谱趋势调，能量截断误差≤.1%不是interbandEM小幅相消的同精度承诺。真实D5能谱、带内比及RMS几何支持保留，同时保D3比偏差和D4低spin失配。

关键输出边界是该v1全文实际只有Fig3带内B(M1)/B(E2)，没有20+_D5C到两个18+的E2矩阵元或out/in预测。因此上面.21979可以成为有限的未交付比较目标，不能说已经通过这篇模型。需要冻结输入/每I截断、匹配三个端点，再交两E2 B或RME及EM收敛、说明是否参与调参；τ/globalQ0可消，γ/混合/端点不能消。Fig5的g7/2 holes在I17–21重排，I20正处演化段，高spinRMS相似不补该transition。模型实验点仍来自PE18同campaign，不多计一份实验。

### MχD标签不自动证明多个不同shape

[[kuti-2014-multiple-chiral-doublets-103rh]]既有KU14-13/16和KU14-D18-7/8/9经030全文/五图复核，科学为verified-no-op。其两组负宇称候选由同effective配置、共同PRM形状输入的四本征带解释，说明MχD的带对数本身不推出不同shape/configuration共存。此为对本页三核推断量词的控制，不搬103Rh的参数/clock，也不反向证明真实态没有shape变化或混合；200keV与alignment失败仍保留。不同shape需各自直接/间接结构证据，不由多个模型或标签数量认证。

### static PES的标签与能量零点

[[leander-larsson-1975-potential-energy-surfaces-n-equals-z]] LL75-D24-006–009给一个完整历史模型控制：static intrinsic minima仍需projection/collective dynamics、ZPE和混合才能接物理态；Table2的min/saddle都以GS为零，不能把saddle值当已减well底的barrier。其40Ca失败和24Mg换surface的6/17MeV敏感性是真实源内反例，非本页三核新数据/替代fit。静态intrinsic Q、经rotational model由B推absQ和逐伙伴transition RME也必须分开，不把一个PES图与另一pair的EM拼为实测shape。

### tracked能带、yrast路径与continuum集合

[[bengtsson-ragnarsson-1985-rotational-bands-particle-hole]] BR85-D24-005/007/012/013给具体对照：粗组态标签中可有多band，globalyrast可换配置；130Ce中继续较小形变支仍符合discreteEγ，而另一模型极小成yrast。continuumJeff/Jband与resolvedband定义不同，作者的moredeformedcascade推断不能填成已解析另一band。171Ta近合曲线却有不同轨道身份，作者自己不据此确证；这提醒三核矩阵不能只按近能/近曲线或共同核名拼接shape和EM。属于真实方法/跨核控制，不是134Pr/135Nd/136Nd新增实测或替代fit。

### primary可收紧二级模型概括

[[nolan-1983-ce130-high-spin-moment-inertia]] NO83-D24-002–006将BR85 Ref63落到实际定义：valleywidth-derived J_band^(2)、不同选择的同campaign谱、污染/最高线assignment、assumed ε.25 rigidreference52。constantJ2/填谷支持转动与alignment研究，但完整离散线未得、directfeeding替代仍在，不能将BR85的52vs45或较大shape-minimum推断升为primary已精确测定另一shape。它是本页companion设计的跨核方法控制，不给三核目标补绝对EM或新模式胜负。

### Tonev2007：EM支持、模型失败与逐点表算术

[[tonev-2007-134pr-dynamic-chirality]] TO07-D24-001–008是26页实际原件；TO07-D24-007明确与Tonev2006共享实验，不重复计票。Table I含Seen、上限、模型列和空实验格；Table II跨带ΔI1未分离δ，不能把全部格都称完整实测。

TO07-D24-002/008的同spin带内E2比较可复用：

|I|Band1 B(E2), e²b²|Band2 B(E2), e²b²|中央比，无CI|
|---|---|---|---|
|14|.153(21)|.039(19)|3.9231|
|15|.148(21)|.089(20)|1.6629|
|16|.115(19)|.050(18)|2.3000|
|17|.108(22)|.047(17)|2.2979|

“约2”或“2–3倍”是趋势概括，不能要求每spin固定比值；旧.15–.25/.05–.10精确包络撤回。13₂→11₁=.0030(5)是跨带，不给13₂→11₂代填；空格不是零。共享τ/branch/归一Cov未给，未以这些打印误差制造联合CI。

原文SecVI/PDF25比较：TQPTR能谱/尖锐交叉好，但所算EM不符；IBFFM主要EM趋势好，能隙却过大、I15交叉未重现，17₂→15₁ E2和16₂→15₁ M1亦有失败（TO07-D24-004/005）。几何/形状分布是模型，不是直接β/γ测量；p11数据参与调参，不能作独立holdout成功。作者提出弱涨落主导手征并保留尚待揭示的内禀对称性（TO07-D24-006），不宣称全部竞争解释已被排尽。

PE06 Ref9与Ref11分别引寿命和branch来源；书目不同不证明事件/标定/Cov独立，不能合成两次独立绝对EM实验。134Pr的这项反证也不取消135Nd负pair与136Nd指定pair已有真实支持。

### 134Pr比较中的输入和模型空间须随spin追踪

[[tonev-2007-134pr-dynamic-chirality]] TO07-D24-009/010将当前有界比较再分开：

|对象|实际输入/选态|可支持与限制|
|---|---|---|
|TQPTR谱学|微观Js:Ji:Jl=1.52:3.55:1，尺度按邻核2+定标|能谱/尖锐交叉有支持，不等EM成功|
|TQPTR几何演示|γ30°与轴对称对照、惯量比1:4:1|为特殊几何的模型分布，不当同一谱学job或实测γ|
|IBFFM|当前数据参与H/EM参数调整，evib1.2、boson gR.15|主要EM趋势是定标后比较，不能计独立holdout；磁矩输入非Ce实测|
|高spin Band1|作者由曲率/对齐提出I>16额外qp|提示原2qp模型空间失效；配置变化不是直接探测器观测或已独立拟合完毕|
|I14/I15模型赋名|近简并混合，I15按EM系统学交换归属|同一EM不能既选family又当独立验证|

这让crossing/configuration-change反证有具体可检查边界：必须绑定比较spin段、模型空间和family选择。它不取消135Nd负pair原实验支持，也不把134Pr参数迁给133Ce低832 keV态。

## Risks and Blockers

[[tonev-2006-134pr-lifetime-chiral]] TO06-D24-006曾将分支/偏振细节留待后文；[[tonev-2007-134pr-dynamic-chirality]]现给真实详细表，但仍缺部分跨带δ、实际response/Cov与完整producer。2006/2007共享实验，PE06另引branch的统计独立性未证。IBFFM的shape分布是模型解释且存在能隙/交叉失败。LV19 D4目标/Ex歧义不静默改原件；PE18 actualSI仍未建立，旧假表认证继续撤回。这些限制不否定现有实验支持，也不允许模式排他认证。

## Learning Decision

`supports`近简并以外的EM/谱学/模型联合支持，保135Nd负pair和136Nd D5的真实链；`limits`用同核/同pair名称、多个模型或旧假SI合成不存在的完整观测向量。本文不因Pr争议否决Nd/Ce等其它真实支持，也不把物理partial当技术hardP0或用户自动待办。

## Next Actions

继续允许的Day25预习内高信息问题：134Pr真实表中的跨带上限/缺δ及共享数据依赖、two-band模型off-diagonal E2敏感性、pair-specific shape/组态预报与缺项降级。选有实际输入的一个单位，不反复撞相同失败端点，不开Day26；正式信用留到Day25自己的run。

## Sources

- [[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25P-001/002及既有PE06-D21-R45-1–4。
- [[lv-2019-chirality-135nd-reexamined]] LV19-D25P-001–004，原v1 PDF2–10；VoR仅定向核。
- [[petrache-2018-chiral-bands-even-even-136nd]] PE18-D25P-001–004，cover+六页正文及真实artifact身份。
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24-001/002，原TableI/Figs2–4；只引用本Day24已回读支持，不重新称独立测量。


## 原模型的γ软度检验也有自己的极限

[[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]] MTVII75-D24-012–015的Table6使用E2₂/E4₁和(E4₂−E2₂)/(E3₁−E2₂)，只检完全γ独立的Wilets–Jean极限，原作者同时说rigid点也未达到。两个比共享E2₂，不拿它们当独立likelihood或反演σγ。Fig10仅示意PES，摘要ΔI1/2 band coexistence不是两shape实验；effective fitγ±2°不是实测γ宽度。对本三核family的shape/配置比较仍需本核状态和EM块，不能搬邻区极限数。


- [[tonev-2007-134pr-dynamic-chirality]] TO07-D24-001–007：26页PRC长文基准，含实验/模型/上限与空格的详细表；保弱涨落主导手征的作者解释及能隙/crossing失败。
