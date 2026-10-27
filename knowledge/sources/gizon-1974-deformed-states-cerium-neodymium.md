---
type: source
title: "Gizon1974：缺中子Ce/Nd的原始谱、角分布与历史零点"
aliases: [Gizon1974 Ce Nd deformed states, Gizon1974 133Ce 135Nd]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-paper-with-model-interpretation
reading_depth: deep-read
title_original: "Deformed states of neutron-deficient cerium and neodymium nuclei"
authors: [J. Gizon, A. Gizon, M. R. Maier, R. M. Diamond, F. S. Stephens]
year: 1974
journal: Nuclear Physics A
volume: 222
issue: 3
pages: 557–578
doi: 10.1016/0375-9474(74)90339-X
canonical_source: https://doi.org/10.1016/0375-9474(74)90339-X
citation_key: ""
raw_file: raw/papers/1974_Gizon_DeformedStates_CeNd.pdf
raw_sha256: 9d09f0fca35c125cb35241bbd2f231a65ec710702889c8b0262a529af7f56dac
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-gizon1974-unique-parity-entry-064/attachment-object-response.pdf
nuclei: [133Ce, 135Ce, 135Nd, 137Nd]
reactions: [120Sn-16O-3n-133Ce, 122Sn-16O-3n-135Ce, 122Te-16O-3n-135Nd, 124Te-16O-3n-137Nd, 124Sn-16O-5n-135Ce]
models: [particle-plus-rotor, axial-prolate-core, partial-alignment]
methods: [in-beam-gamma-spectroscopy, delayed-gamma-spectroscopy, excitation-function, gamma-gamma-coincidence, angular-distribution]
observables: [level-energy, spin-parity, relative-gamma-intensity, mixing-ratio, half-life]
tags: [133Ce-analysis-blueprint, historical-energy-reference, observed-transition-ledger, response-boundary]
---

# 原实验有实际边和时间信息，也有明确的未定身份

## Bibliographic Record

J. Gizon等，NPA222(1974)557–578，DOI10.1016/0375-9474(74)90339-X；received1973-08-08、revised1974-01-22。physical页+556=印刷页。本文是[[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]] Ref26的真实原实验，不能将后者复用的数据再算一次采集。

064核Crossref exact及出版商FULL XML，按实际MAIN attachment经标准Object API取得真22页、1264150bytes和上述SHA。原生抽取首页1914/方法5.5°误字分别经原图核为1974/55°。SI默认纳入检索；所查FULL XML仅小ALTIMG行内符号，无supp候选，不扩大成全网不存在SI。原件暂在tmp，raw未归档；完整PDF/XML/OCR/页渲染不入公开manifest。

## Scope and Reading Depth

066连续原读methods1–4及135Ce正文8–9/11底、Tables2页10–11/Figs1/5/6；067读133Ce正文15/17–18、Table4页16–17/Figs8–10及δ方法18–19/Fig11；root068读137Nd4–8上、135Nd Table3页12–13/正文13/Fig7页9/Fig8页14、讨论19–21及参考21–22，另读1–4上下文。各分区text与相应figure/table视觉已核；root另核Ce Table4和历史zero相关原页。合并覆盖22页主线、Figs1–11/Tables1–4，不把任一worker说成独立全文。

本轮没有原event、校准曲线、逐线效率/有限角响应、完整Cov或原作者producer；未重新拟合δ/半衰期/核结构模型，也未全文读所有引用。历史测量与继承文献的寿命/自旋分开。

## Summary

原实验建立四核低负宇称谱和若干侧馈，提供实际γ线、角分布及时间信息。133Ce的9/2参考态在当时尚未确定为基态或异能态；单条近能光子线也未必绑定到现代能级边。prolate与粗略δ属于给定转动/取向模型下的解释，不能代替现代手征伙伴或实际程序输出。

## Experimental Setup and Intensity Contract

Berkeley氧束轰击ORNL富集Sn/Te靶，约2mg/cm²、25μm Pb backing；两8cm³ planar intrinsic Ge，或一8cm³加30cm³ coaxial Ge(Li)。共同束能列60/65/66.5/70/80/85/90MeV，但135Ce谱与Table2明确62MeV；133Ce Table4标题65MeV、Fig9/正文另66.5MeV，保case范围而非伪造单run清单。

实际布置用标准源/177mLu核能量和效率，另用已知偶核线校能；每符合事件存两E、tγγ和tγRF，接收300ns，离线能量/时间/背景窗；γγ通常<6ns FWHM、γRF约10ns受束团限制。300ns不等寿命分辨率。90°激发函数用于归核素，角分布另0/55/90°。

表中Iγ是55°相对光子强度，规范化文字称最强线100；135Nd Table3却同时印198.5keV=100、511.8keV=117，保原表/措辞边界，不猜原因或改值。强线能误约.1%、强度约10%，弱线2–3倍。I55、图示total-intensity箭头、角积分branch、绝对B是不同量；空白assignment或未列弱线不是零。

## Key Results

所有新claims needs_review:true，只有本实验实际报告的观测才列直接原实验；继承状态、作者解释和任务crosswalk另标。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GZ74-D24-001 | 120/122Sn(16O,3n)到133/135Ce、122/124Te(16O,3n)到135/137Nd，另124Sn(16O,5n)到135Ce；Ge装置/靶/束能与现代采集区分。四核同一论文也不自动是同事件集合。 | actual-experimental-channel-and-apparatus | direct-original | PDF1–4 §1–2 | true |
| GZ74-D24-002 | Tables1–4的Iγ为55°相对强度，非角积分BR；强/弱线精度与规范化文字须连原表117例外保存。actual效率/finitegeometry/Cov未给，不由Iγ直接造B。 | measurement-definition-and-readiness | direct-original | PDF3 §2; PDF12 Table3 | true |
| GZ74-D24-003 | 300ns接收、两γ时间/RF时间与离线背景窗不同；γγ<6ns、RF约10ns只是装置尺度，延迟链可继承feeding，不是每条下级线独立寿命。 | clock-and-selection-contract | direct-original | PDF2–3 Fig1 and timing paragraphs | true |
| GZ74-D24-004 | 137Nd主11/2−isomer图519.2、约1.6s；原caption允许低108.7/177.3顺序交换。87.5/176.8仅预期能差未得definite observation；581.4有小137Pr成分，563.4 composite。 | state-and-observed-line-boundary | direct-original-plus-cited-low-state-input | PDF4–8 §3.1/Table1/Fig5 | true |
| GZ74-D24-005 | 137Nd2222.4经328.2喂17/2，约1–4ns及AD/缺竞争E2使作者prefer E1，19/2+与上23/2+的parity明确tentative。不能将偏好变已测组态或完整多极性裁决。 | measured-delay-and-conditional-assignment | direct-original | PDF7–8 Fig5 and side-feeding discussion | true |
| GZ74-D24-006 | 135Nd图主序9/2零、11/2198.5、13/2560.7、15/2792.9、17/21270.0、19/21520.5；198.5/362.2/232.2 M1+E2和共门支持。作者无足够确定sidebands，不能倒填现代TiP或高spin手征带。 | original-low-family-ledger | direct-original | PDF12–14 Table3/§3.3/Fig8; PDF9 Fig7 | true |
| GZ74-D24-007 | 135Nd crossover Table3印560.3、正文560.5、Fig8节点560.7，受强122Te564线仅由coinc取得。保版本/精度差，不静默统一或作精确closure/显著性。 | source-literal-energy-versions | direct-original | PDF12 Table3; PDF13 §3.3; PDF14 Fig8 | true |
| GZ74-D24-008 | 135Ce继承旧1/2+ground17h和11/2−445.7/20s，296keV有两spin doublet。实际8±2ns为2125.6侧馈相关延迟，不是五条下级线各自τ；(19/2+)与(23/2+)宇称仍tentative，906.2 composite。 | low-state-lineage-and-new-delay-boundary | direct-original-and-explicit-cited-history | PDF7–11 Fig5/§3.2/Table2 | true |
| GZ74-D24-009 | 133Ce5.4h/I9/2与97min/I1/2来自既有decay/atomicbeam研究，作者明确谁ground/isomer未定。Fig8以9/2、5.4h为0，不是现代groundEx0认证。 | explicit-historical-reference-boundary | direct-original-citing-prior-measurements | PDF15/17 §3.4; PDF14 Fig8 | true |
| GZ74-D24-010 | Fig8 133Ce主负序11/2170.0、13/2554.9、15/2789.7、17/21306.3、19/21552.3；385–609符合与A2exp−.64(.06)支持1163.6支态到13/2的608.7边。节点/线/指认强弱分别保。 | actual-Ce-node-and-edge-ledger | direct-original | PDF14 Fig8; PDF16–18 Table4/§3.4 | true |
| GZ74-D24-011 | 133Ce2059/2260及更高侧带用符合/能和支撑，但高段线序不清；235同能峰至少半强度在上带，不能把同E当唯一边。该侧带退激报告短half-life约不超过3ns，不给每个现代低态单独τ。 | topology-and-feeding-clock-boundary | direct-original | PDF14 Fig8; PDF18 §3.4 | true |
| GZ74-D24-012 | Table4有619.7字面J标注与Fig8节点/箭头不合、159.5行2450.0与图2449.5差；保表/图/算术分层，不擅修原图或把残差当统计矛盾。 | original-table-level-consistency | direct-original-plus-arithmetic | PDF14 Fig8; PDF16 Table4 | true |
| GZ74-D24-013 | 原AD只三角，§4忽A4、由pureE2定α2并按核平均。135/137Nd α2=.43(.16)/.44(.20)，133/135Ce=.69(.19)/.76(.19)。不是可跨阵列搬的已知σ/I或完整响应。 | actual-angular-response-contract | direct-original | PDF4 angular-distribution formula; PDF18–19 §4 | true |
| GZ74-D24-014 | negativeδ与约50±25%E2是上述AD/α2反演的粗略总结；Fig11横轴absδ/(1+absδ)非E2fraction。Q0 prolate推断另依K≠1/2和(g−gR)经验sign规则、I≥7/2，非δ单独测shape/唯一γ。 | author-inference-and-sign-domain | direct-original | PDF18 Fig11; PDF19 §4 | true |
| GZ74-D24-015 | Table4实际列624.8/582.2/464.6/817.3等光子线而未绑定现代三母态或终态。old817.3被观测不等现代energy-only817.7已是582outE2reference；本篇不关闭该分母缺口。 | observed-unassigned-line-and-cross-version-boundary | direct-original-and-explicit-task-limit | PDF16–17 Table4 | true |
| GZ74-D24-016 | 轴对称prolate particle-rotor仅定性较好，作者保quantitative差、γdistortion/softness替代（Ref31 Meyer1973privatecommunication）。不是γrigid或手征测量；1975 PartII复用本实验非新独立数据。 | original-model-limits-and-source-lineage | direct-original | PDF20–22 §5.2/Ref31 | true |
| GZ74-D24-017 | Table4原70条光子线在本页完整保Eγ/I55/A2/原印assignment及空白/双峰/composite；这是原表转录而非70条现代已绑定边，不新增实验或归一。 | complete-literal-photon-ledger | direct-original-transcription | PDF16–17 Table4 | true |

## Level Ledger and Actual Arithmetic

|核/参考|主负宇称序列，按原图keV|须保边界|
|---|---|---|
|137Nd，1/2+零|11/2519.2；13/21100.6；15/21188.1；17/21894.2；19/22071；21/22819|519.2为isomer；低态顺序及side positive parity暂定|
|135Nd，9/2−零|11/2198.5；13/2560.7；15/2792.9；17/21270.0；19/21520.5|未可靠建sidebands；不与三qp MU07 A/B混合|
|135Ce，1/2+零|11/2445.7；13/21035.4；15/21145.3；17/21869.6；(19/2)2050.6|20s isomer为旧输入；侧8ns不是带内各τ|
|133Ce，历史9/2−零|11/2170.0；13/2554.9；15/2789.7；17/21306.3；19/21552.3|该零点身份当年未定，不当modernground|

root印数核算：137Nd233.4+285.8=519.2，519.2+581.4=1100.6，519.2+668.9=1188.1，1894.2+328.2=2222.4，2222.4+407.2=2629.6；135Nd198.5+362.2=560.7，560.7+232.2=792.9。均是已印数算术，不给独立实验票或无误差精确node身份。

135Ce两条17/2到11/2路径833.1+589.7=1422.8，而724.3+699.6=1423.9，差1.1keV。保原线/节点及约.1%单线误差，不强修closure或缺Cov给显著性。133Ce619.7在Table4字面写15/2→13/2，但原节点789.7−170.0=619.7对应15/2→11/2；这是一项明确表/图核对边界，不把任务算术假称原表原本就这么写。

## Historical Crosswalk to 1975 and Modern Ce

Meyer1975 Fig9改以11/2为零：170.0→0，554.9→384.9≈385，789.7→619.7≈620，1306.3→1136.3≈1136。1552.3−170=1382.3却不等其印1380，保真实差。1975顶21/2/23/2不能在本篇无同spin主支时硬找替身。

原primary现在可解前述994/1164注：1163.6−170.0=993.6≈994、旧9/2参考下1163.6≈1164。这说明数字出处，不自动给现代绝对Ex或整个Band4身份。若以现代WK22所支持的9/2派生37.2作为**任务暂定offset**，则554.9+37.2=592.1、1163.6+37.2=1200.8，差608.7与两代已列线相合；仍须保ground/isomer历史、其它边及832.0带头未绑定。主序较高态不能靠一个offset消除所有差。

Table4部分未放置光子线如下，I55仅相对值：

|old Eγ keV|I55|本表能确定的事|
|---|---:|---|
|464.6|5.2|observed photon；无现代母/终state binding|
|577.3|7.5|同上|
|582.2|4.7|同上，不自动等582.7|
|624.8|3.4|同上，不自动等624.6|
|794.7|10.8|同上，不自动补794.8 reference|
|817.3|3.4|observed old line；现代817.7仍energy-only候选|
|981.6|6.6|同上，不按近能给982.0完整身份|

接近能量只是发现线索。缺gate/母态/终态/Jπ/多极与分母归一时，不用这些列重造582 out/out或actual signedEM。

## Competing Interpretations and Limitations

原prolate结论有两条模型依赖链：perturbed ΔI1谱对比axial particle-plus-rotor、以及δsign连同g−gR/Q0规则。γdistortion或softness可改善谱是作者保留的解释，未测γrigid、未排所有混合/配置，也未计算现代高spin3qp crossing。N75两核相似不等所有同spin态一一对应，更不提供左右手或chiral vibration/static的直接证据。

全谱相对I、角分布系数、反演δ和后续理论所用这些量共享输入。不同年份的理论复用不产生新实验；原子束/β衰变旧结果只是本篇引用，未在本轮独立再测。相比现代装置，本实验反应/探测器/时间窗口确有不同，但独立观测量仍须逐state/branch核，不把核素数、论文数当独立强度计数。

本轮decision为supports：历史primary的节点、实际线、clock和失败条件不再只有转引；revises：994注数字出处与旧零点现在可追溯；limits：近线不等matchededge、historicalground非modernzero、粗δ不等实际跨带signedRME。133Ce蓝本仍持续研究，摄入本篇不表示结项。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：历史节点/线与现代分母、实际响应合同。
- [[135nd-chiral-partner-resolved-evidence-map]]：低1qp参考与高spin三qp伙伴分开。
- [[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]]：Ref26实际primary和共享数据谱系。


## Table4完整逐线ledger：55°相对光子强度

GZ74-D24-017：physicalPDF16–17/printed572–573 Table4原印70行的可复用转录。表内assignment列保字面，不把图示推断或现代标签暗填进去；表/图冲突见GZ74-D24-012。A2与强度空白不作0，多极性括号原样保。55°Iγ不是角积分BR，不能把各行合成同母态分支和。

|Eγ keV|Iγ(55°)|A2exp|原印多极性|原表assignment|备注|
|---|---:|---|---|---|---|
|134.3|7.2|—|—|—|—|
|154.7|3.4|—|—|—|—|
|159.5|23.6|-0.35±0.06|M1+E2|2609.0→2450.0|图末态2449.5|
|170.0|100.0|-0.55±0.04|M1+E2|11/2−→9/2−|—|
|183.6|4.8|—|—|—|—|
|189.5|20.9|-0.39±0.06|M1+E2|2449.5→2260.0|—|
|197.3|4.4|—|—|—|—|
|200.7|19.1|-0.38±0.07|M1+E2|2260.0→2059.0|—|
|205.4|4.6|—|—|—|—|
|208.9|1.3|—|—|—|—|
|215.4|2.2|—|—|—|—|
|223.8|7.1|—|—|—|—|
|234.8|31.9|-0.46±0.07|M1+E2|15/2−→13/2−；2844.0→2609.0|同能双边；upper至少半强度，非精确split|
|240.8|9.0|—|—|—|—|
|246.0|3.6|—|(M1+E2)|19/2−→17/2−|—|
|252.6|2.2|—|—|—|—|
|276.8|2.6|—|—|—|—|
|283.1|6.9|—|—|—|—|
|294.9|17.9|-0.42±0.06|M1+E2|3139.0→2844.0|—|
|302.9|7.3|—|—|—|—|
|357.5|13.7|-0.07±0.11|—|3496.0→3139.0|—|
|384.7|63.8|-0.61±0.05|M1+E2|13/2−→11/2−|—|
|390.6|5.5|—|—|—|—|
|400.0|5.3|—|—|—|—|
|416.2|2.8|—|—|—|—|
|423.0|6.9|—|—|—|—|
|435.9|4.6|—|—|—|—|
|444.4|8.2|—|—|—|—|
|457.6|5.0|—|—|—|—|
|464.6|5.2|—|—|—|—|
|496.8|9.5|—|—|—|—|
|507.7|7.3|—|—|—|—|
|511.0|18.6|—|—|—|—|
|516.7|21.1|-0.75±0.04|M1+E2|17/2−→15/2−|—|
|530.2|5.0|—|—|—|—|
|544.2|7.9|—|—|—|—|
|553.1|4.4|—|—|—|—|
|554.9|12.9|0.19±0.14|E2|13/2−→9/2−|—|
|562.3|5.8|—|—|—|—|
|563.7|15.5|—|—|—|—|
|570.1|9.3|—|—|—|—|
|577.3|7.5|—|—|—|—|
|582.2|4.7|—|—|—|—|
|608.7|14.5|-0.64±0.06|M1+E2|1163.6→13/2−|—|
|617.3|15.0|—|—|—|—|
|619.7|65.6|0.30±0.15|E2|15/2−→13/2−|表/图assignment冲突|
|624.8|3.4|—|—|—|—|
|630.1|4.6|—|—|—|—|
|644.4|4.4|—|—|—|—|
|691.9|7.3|—|—|—|—|
|706.3|3.9|—|—|—|—|
|751.3|21.4|0.33±0.15|E2|17/2−→13/2−|可能composite|
|762.6|28.4|0.34±0.14|E2|19/2−→15/2−|—|
|794.7|10.8|—|—|—|—|
|798.0|4.0|—|—|—|—|
|817.3|3.4|—|—|—|—|
|855.7|9.3|—|—|—|—|
|891.0|4.0|—|—|—|—|
|896.2|16.6|0.15±0.14|—|—|—|
|908.0|5.5|—|—|—|—|
|913.5|4.4|—|—|—|—|
|954.0|16.4|0.00±0.20|—|2260.0→17/2−|—|
|957.0|5.2|—|—|—|—|
|981.6|6.6|—|—|—|—|
|1023.4|8.0|—|—|—|—|
|1071.9|8.8|—|—|—|—|
|1075.8|5.6|—|—|—|—|
|1190.7|11.3|—|—|—|—|
|1269.3|29.9|—|—|2059.0→15/2−|—|
|1304.5|8.3|—|—|—|—|

脚注说I<2不列，但208.9的原行I1.3仍保；751.3可能composite。619.7表字面15/2→13/2不改，Fig8/能差对应11/2另记；159.5行2450.0不按图2449.5静默替换。原图608箭印字清晰度未解，表/正文608.7和节点差相合。全表不是现代transitionbinding，817.3仍未指认，现代817.7仍缺observedreference。


## 后续评估不覆盖当年知情边界

[[nndc-2011-133ce-low-level-reference-records]] N133CE11-D24-002–007本轮取得实际2011adopted：1/2+为0、9/2−为37.2(7)keV/5.1(3)h，后者weighted输入含原旧5.4h。这能固定服务当前采用的现代表示，不能倒写本篇1974作者已知ground/isomer排序；也不把NuDat/IAEA同源两个接口加成独立测量。reaction记录另保37.3(6)fixed/4.9(4)与fromadoptedcomments，source版本分别留。
