---
type: report
snapshot_source_type: project
graph-excluded: true
title: "手征与形状共存：134Pr/135Nd/136Nd逐伙伴竞争解释矩阵"
aliases: [chirality shape-coexistence companion matrix]
created: 2026-10-26
updated: 2026-10-26
status: active
review_status: unreviewed
confidentiality: public
project_stage: uncredited-next-card-preview
nuclei: [134pr, 135nd, 136nd]
tags: [chirality, shape-coexistence, band-mixing, companion-observables]
---

# 不同核、不同pair的支持链不能拼成一条完整向量

## Agent active summary

本页来自正式Day24 run中恰好下一卡Day25的无学分预习；不授Day25卡、不提前推进next_day_index、不打开Day26。源内真实正支持与反例保留，所有新综合`needs_review: true`。正式Day24主线见[[135nd-chiral-partner-resolved-evidence-map]]，133Ce仍见[[133ce-thesis-analysis-blueprint]]。

## Research Question

近能双带的哪些信息直接来自观测、哪些是作者/模型推断？crossing、configurationchange、γ-softness、bandmixing和多个形状极小能解释哪些部分特征，还需要什么可分辨的伴随量？形状共存与手征可以在不同层次/组态上同时讨论，不能仅凭带数或一个势面就作互斥二选一。

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

### 最小companion组合是问题设计，不是普适终判

先选一个pair和同一spin段，再比较预先固定输入的chiral/shape/configuration/mixed预测。下表用于本比较的可审查设计；完整组合也不保证模式数学唯一，缺某量更不自动否定实核手征。

|组合量|为何增加信息|缺一项时具体降级|
|---|---|---|
|母态/终态/family/Jπ与每线component身份、门/效率/ICC/未见branch界|不把近能线/同spin或未见线当同一个输入；实际LV19局部歧义说明其必要性|保留谱学candidate/已知部分观测，歧义行不作matchedEM比较；不连带否定全family|
|双方同I/段可逐态绑定的实测clock（允许jointfit/共享Cov）＋完整component-resolved BR/normalizer/response|把ratio/趋势接到absolute M1/E2尺度，检验同一ratio下共同尺度变化|仅有相对γ资料且没有其它absoluteEM约束时，缺clock只得relativeEM；缺branch/normalizer则新复算/精度仍条件化，既有publishedB支持保留|
|覆盖段的固定空间/shape/mixing模型与实际observable预报|防止每加一量就重新调γ/J/g，能对crossing/形状差别作可失败比较|只能说模型相容/conditional fit，不能说所有竞争解释已排除|
|可行且有分离预报的独立结构holdout，如同态g或Qs/另一E2形状量|磁/电/组态给互补约束；先证预测可区分再选技术|没有holdout时可能仍有等效配置；g不是每个模式普适必测条件，也不强迫ps态作TDPAD|

134Pr优先闭合原branch/clock并检验off-diagonal E2/固定V假设；正135Nd优先双方matchingEM；负135Nd优先normalizer恢复/新独立holdout；136Nd先选D5或另一个明确pair，不在不同pair间借几何/寿命。测量方法的clock、束流、停止/feeding/场标定属于各自响应合同，不能借131Ce/128Cs的时钟给高spin目标补数据。

## Risks and Blockers

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

## Remaining input boundary

Tonev2006实际body未得（已查失败入口），PE06所引Ref11当年to-be-published身份仍未唯一恢复；不能伪造其τ/BR/EM表。LV19 D4目标/Ex局部矛盾不静默改原件；PE18 actualSI未建立、旧补充表认证已撤回。数据缺口不阻止以上原件支持的知识比较，但阻止完整实际likelihood/模式排他认证。

## Learning Decision

`supports`近简并以外的EM/谱学/模型联合支持，保135Nd负pair和136Nd D5的真实链；`limits`用同核/同pair名称、多个模型或旧假SI合成不存在的完整观测向量。本文不因Pr争议否决Nd/Ce等其它真实支持，也不把物理partial当技术hardP0或用户自动待办。

## Next Actions

继续允许的Day25预习内高信息问题：134Pr实际长文/branch来源、two-band模型off-diagonal E2敏感性、pair-specific shape/组态预报与缺项降级。选有实际输入的一个单位，不反复撞相同失败端点，不开Day26；正式信用留到Day25自己的run。

## Sources

- [[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25P-001/002及既有PE06-D21-R45-1–4。
- [[lv-2019-chirality-135nd-reexamined]] LV19-D25P-001–004，原v1 PDF2–10；VoR仅定向核。
- [[petrache-2018-chiral-bands-even-even-136nd]] PE18-D25P-001–004，cover+六页正文及真实artifact身份。
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24-001/002，原TableI/Figs2–4；只引用本Day24已回读支持，不重新称独立测量。
