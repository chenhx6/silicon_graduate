---
type: project
title: "131Xe 低自旋伙伴带：对象映射与混合比分支检验"
aliases: [131Xe low-spin partner crosswalk]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
project_stage: active-l3
confidentiality: private
nuclei: [131xe]
tags: [a130, l3, band-identity, signature-partner, wobbling, mixing-ratio]
---

# 131Xe 低自旋伙伴带：对象映射与混合比分支检验

## Agent active summary

2020 B5 的部分低自旋成员与2023 yrare 单链可以对应，但 B5 有其它分支，B1(a) 又是高自旋网络，两者均不能整带改名为2023新链。2023新增的 yrast 835-keV 13/2− 序列与1601-keV态的宇称修订必须单列。原作者偏好 yrare signature partner 的解释保持；当前没有全局 δ likelihood 或独立 partner-resolved 电磁矩阵，不能升级为对所有候选的排他否证。

## Research Question

在同一 INGA acquisition 的不同发表版本间，先校准核态、跃迁和观测量身份后，2023年的小 δ 分支及 B(M1)/B(E2) 能否独立区分普通 signature partner 与候选集体激发？哪些最少新增观测能改变其排序？问题承接 [[131xe]] 与 [[signature-partner-bands]]，不由相邻核标签预设答案。

## Current Hypotheses

| 假设 | 当前边界 | 改变判断所需信息 |
|---|---|---|
| H1：低自旋 yrare 链是 νh11/2 unfavored signature partner | 2023作者首选；小δ、能量与模型比较支持，但不是独立新采集 | 对两个δ解同时拟合的角分布/偏振与同母态强度 |
| H2：某一低自旋链含显著集体带间E2成分 | 未由本轮确立；不能仅凭RDCO小解标签认为全部大解已排除 | 完整 δ profile、E2 out/in 与对应波函数预测 |
| H3：yrast13/2−属另一组态或粒子—芯耦合 | 作者保持开放；不能从比值偏离直接选定某机制 | 组态敏感量、g因子/转移约束及伙伴分辨寿命 |

## Evidence Available

### 逐态与逐边对应，禁止整带同义化

| 对象 | 2020报告 | 2023报告 | 对应状态与locator |
|---|---|---|---|
| 低自旋13/2− | B5，1045.8(2) keV，704.6-keV线接约341-keV 9/2− | yrare1046.0 keV，704.6-keV线；另拆出881.8-keV连接 | 端点与级联相容；[[banik-2020-131xe-multiple-band-structures]] BNK20-D28-1；[[chakraborty-2023-131xe-wobbling-origin]] C23-D28-1 |
| 低自旋17/2−候选 | B5，1861.5(3) keV，17/2(−)，815.7-keV线 | 1861.9 keV，17/2−，815.6与1055.1-keV线 | 需保留旧暂定宇称；不是仅由能差认证，C23 Fig.2的930门同时见816/1055提供放置支持；同上两claim |
| 其它B5分支 | 1903.1-keV17/2−、2090.3-keV17/2(−)、3108.2-keV21/2(−)等 | 未全部进入Fig.1单链 | 不宣称整个B5被逐态替换；BNK20-D28-1 |
| 高自旋B1(a) | 2299-keV21/2−由682-keV线接1617-keV19/2−；另有3509-keV27/2−等 | Fig.1只保留部分高自旋参照 | 低自旋链并非该全带的重命名；BNK20-D28-1 |
| 1601-keV节点 | 1600.9(2) keV，17/2+，794.8-keV线列E1 | 1600.9 keV，17/2−；新增766.5-keV线接834.6-keV13/2− | 同能量但量子标签改变，需显式版本账本；BNK20-D28-2、C23-D28-2 |
| 约2792-keV近邻 | 2791.8(3) keV，23/2+，986.2-keV线 | 2792.1 keV，21/2−，929.7/1175.9-keV线 | 自旋/宇称/衰变端点不同，拒绝最近能量匹配；BNK20-D28-2、C23-D28-1 |

### 小δ分支、光子份额与模型输出分层

对同一M1/E2混合跃迁，`f_E2=δ²/(1+δ²)`。这定义光子辐射率份额，不是比值 `B(E2)out/B(E2)in`，也不是集体性的充分阈值。定义及同母态率公式见 [[alwaleedi-2013-band-structures-131ce]] AW13-9、[[bm1-be2-ratio]]。

| 输入层 | 中心 fE2 | 把印刷δ±数值区间映射后的份额范围 | 使用边界 |
|---|---|---|---|
| Fig.5 δ671=0.03(3) | 0.08992% | [0, 0.35871%] | 属yrast13/2−→11/2−；这里只是区间函数像，不是新置信区间 |
| Fig.5 δ882=0.09(8) | 0.80349% | [0.01000%, 2.80882%] | 属yrare13/2−→11/2−；旧“所有M1>99.2%”只是中心值叙述且越过误差边界 |
| Fig.4 δ1055=0.1(2)，正文称approximately zero | 0.99010% | [0, 8.25688%] | 区间函数像非新CI；旧0.00(2)撤回，本轮初稿漏读图内标注亦已纠正 |
| TPRM δ=-0.69 | 32.25391% | 不赋实验误差 | 模型结果，不等于测得δ≈0；不能改写成99%以上纯M1 |

来源：[[chakraborty-2023-131xe-wobbling-origin]] C23-D28-3/4，printed064318-4 Figs.4/5、printed064318-7模型比较。Fig.5曲线在负δ区与RDCO色带还有交点；这项视觉事实提示需全局分支检验，不提供另一解的精确数值或置信权重。1055-keV线还有1983年角分布比较；671/882不能自动继承这项逐线信息。

### 印刷表重算与误差合同

在同母态、已校正且选样一致的光子强度、分母纯E2、能量用MeV时，采用舍入常数κ=0.697：

\[
R=\frac{B(M1;d)}{B(E2;c)}=\kappa\frac{E_c^5}{E_d^3}\frac{I_d}{I_c}\frac{1}{1+\delta_d^2}.
\]

公式来源为 [[alwaleedi-2013-band-structures-131ce]] AW13-9、Eq.5.6/5.7；这里不重新认证其方法原始文献。共同母态寿命与总退激率相消；相对光子强度已含辐射分支，不能再随意乘ICC。绝对B仍需要寿命/分支/转换等合同。

- 由2023 Table I 的1055.1/815.6-keV线、强度6.0(2)/1.0(1)，条件δ=0得 `R=1.28496 μN²/(e²b²)`；只取印刷强度独立、一阶误差得 `σ=0.13545`。作者报告1.27(14)与此舍入表重算接近；该重算不是独立测量或完整复现作者拟合。
- 纳入Fig.4真实小解 `δ=0.1(2)` 后，`R≈1.27224`；若强度和δ独立，增加 `d lnR/dδ=-2δ/(1+δ²)` 项的一阶传播，`σ≈0.1433`，即可在所声明近似下对账作者1.27(14)。δ区间跨零且非线性，不能把该局部σ当完整profile或全局CI。精确原件入口为C23-D28-6。
- 若只固定上述边缘误差、允许两强度相关系数ρ∈[-1,1]，局部一阶σ可在 `[0.08566,0.17133]`；这是未给定相关结构的数学包络，不是额外测得系统误差。共同归一因子本可相消，实际ρ需由joint响应/统计模型给出。
- yrast 794.8/766.5-keV线用12.6(2)/≈1.8、条件δ=0得 `R≈2.57109`；分母只列近似数，没有误差，不能凭Table I重建作者2.54(4)的精确不确定度。缺误差不是零误差，不能据此声称两倍偏离具有特定显著性。
- 对十条已列边计算印刷 `Eparent−Edaughter−Eγ`，范围−0.2至+0.8 keV；1055.1线为+0.8、929.7线为+0.5。isomer164来自Fig.1的舍入值；其余来自Table I拟合/采用值。仅标记待对账的印刷闭合，不改原数、不把残差变成核态不存在的证据；无共同Σ时不报告χ²。

原始输入定位：[[chakraborty-2023-131xe-wobbling-origin]] C23-D28-2/4/5，Table I及printed064318-6/7。没有事件级重排或代理实验数据。

### 同母态两商与模型能量约定

[[131xe-same-parent-strength-identifiability]]补齐RE=B(E2;out)/B(E2;in)：在同一r=Id/Ic、u=δ²下，RE=(Ec/Ed)⁵ru/(1+u)，RM=κEc⁵/Ed³×r/(1+u)，并有RE/C+RM/A=r。1055.1/815.6-keV印刷小解给RE≈0.0163964、RM≈1.27224；这是同一输入的两个派生商，不能独立计权，也不恢复绝对B或δ符号。率公式已定向回核 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-D28-001。

Fig.11最右TPRM列的出带 `17/2−→15/2−` 为902 keV、带内 `17/2−→13/2−` 为799 keV，分别对应实验1055.1/815.6-keV线；但`RM=B(M1;out)/B(E2;in)`与出带δ之间还隔着未知`RE=B(E2;out)/B(E2;in)`，所以不能由`RM=1.27`和`δTPRM=−0.69`反推采用哪组Eγ。固定同一pair和明确`E_ref`后，8.7535、9.7933以及Fig.11端点下约5.5352/6.0614是有效的条件敏感性算术；把模型δ混入实验强度得到`RM≈0.87051`也是定义明确的hybrid sensitivity。它们都不能写成作者真实模型预测或统计裁决；当前保留模型算符、有效电荷、g因子、淬灭和δ能量约定未公开的source boundary。[[chakraborty-2023-131xe-wobbling-origin]] C23-D28-7及模型约定审计见run目录。

### 1601-keV宇称版本的反向检查

[[131xe-1601-parity-version-boundary]]记录2020在图注、表注和门分析中多次使用795-keV E1，削弱单行偶然排印的解释；2023 Table I无多极性列、766.5线无偏振，新增符合放置不自动等于新的electric/magnetic测定。直接依据为 [[banik-2020-131xe-multiple-band-structures]] BNK20-D28-3和 [[chakraborty-2023-131xe-wobbling-origin]] C23-D28-8。worker另取得DAE2018、ENSDF档案与Kaya2018的合法暂存材料；其版本线索与独立性边界已保存，但未改raw或把评估转录晋升为早期primary测量。

## Counter-evidence and Source Independence

2023 Sec.I/II明确重分析Ref22，即2020本实验。Table I注释还说已知线的部分强度、RDCO与偏振采用Ref22。两文的能级/模型解释不能作独立复测加权；1983 AD 是另一实验谱系，但本轮未取得该原件，只按2023引用报告其角色，不给予独立核验资格。

反证控制包括：2020早已建立B5局部成员；2023对yrast17/2−的比值并未与模型精确一致；RDCO曲线存在分支；更高自旋B1(a)不在低自旋证据的自动覆盖域。原作者“未发现wobbling信号”不等于所有自旋或所有带均已被排除。

## Minimal Design, Falsifier and Belief Revision

1. **先闭合身份。** 对882/880双线保存663、816、930等用于拆分的逐门谱与共享事件标识；704.6是同一1046-keV母态的竞争退激参考，不能作882的互符合门。对766门保存671与795的存在/缺失证据。若互斥级联或背景不能重现，撤回相应节点/边的固定身份，不向结构解释层推进。
2. **完整δ分支。** 逐线保存角度对/门线、alignment输入、角积分、效率、偏振asymmetry和校准参数，构造联合 `L(counts|δ,alignment,response,background)`。同时追踪正/负、大小解；没有原始计数/响应前不声称得到该likelihood。
3. **有界可证伪命题。** 针对“671/882的小解已由RDCO唯一选定”，Fig.5的第二交点已否定其单观测唯一性；这不自动否定作者整套解释。若所有与数据相容的δ/响应分支都与某个明确H1模型的逐跃迁预测不相交，则否定该指定模型；若大E2分支仍可行，则优先级改为补偏振/角分布，不直接宣告wobbling。
4. **最少新增观测与次序。** 先独立约束882的偏振或角分布，并对671/795的低统计/既有符号与量子标签作共同响应对账；随后补低自旋伙伴分辨寿命及同母态E2 out/in。只有在同一对象、同一响应与给定预测域中比较H1/H2/H3，才谈模式排序。

[[131xe-882-branch-response-contract]]将这一设计具体化：881.8/880.1双线峰形、实际角对、1046-keV条件取向、成对接受度、882偏振scatter-bin响应和联合协方差是必需输入；704.6-keV竞争退激只能作为条件性同母态取向参考，不能与882作双符合。其分支预测集合和nuisance剖面分离条件是设计合同，不是本轮实测根值或显著性。

## L4 Readiness and Failure Boundary

可执行：出版表算术、量子标签冲突识别、官方BrIcc名义αK/αTot候选集合、非线性份额映射与实验输入设计，属于L3。缺失：本次原始event/γγ矩阵、881/880逐门峰形与污染、实际角对/成对效率、完整ANGCOR输入、a2/a4联合协方差、882偏振校准及其Σ、近似1.8强度的误差、ENSDF EKC原始实验表与误差口径、794.8-keV能量误差传播、旧新版本宇称调整说明、1983原件。缺口阻止事件级L4和ICC统计裁决，不阻止继续获取直接来源。无理由生成假想detector计数、beamtime或核素级新预测。

## Risks and Blockers

目前阻塞的是事件级、共同响应下的模式裁决；来源获取与有界L3尚可继续。最主要风险是将带名/近能量当身份、将小根中心值当全局上限、把共享采集算成独立确认，或把历史脚本的通过标签当原文核验。旧source审核字段保持；新claim均needs_review。Fig.5的视觉交点不承担精确根值、权重或模型排除率。

## Next Actions

1983原件获取已有合法仓储/目录路线与访问失败记录，不再重复IOP挑战端点。下一步优先核历史转换记录的逐行来源合同及882两分支的实际响应最少输入，并寻找明确宇称修订说明；模型δ的Eγ约定同时保持未闭。当前主线仍有高信息路线，不打开Day29或第二个novelty问题。

### 1983来源身份与实际访问边界

Crossref精确端点核得：Lönnroth、Kumpulainen、Tuokko，*One- and Three-Quasiparticle States in 127,129,131,133Xe and Their Coexistence With Band Structures*，Physica Scripta 27, 228–240 (1983)，DOI `10.1088/0031-8949/27/4/002`。这只是2023 Ref20的书目对应，不认证其AD数值。Nature downloader的OA-only流程退出0但结果为`oa_not_found`、下载0项；OpenAlex同时标bronze/无repository全文。实际IOP PDF URL虽HTTP200，却为`text/html`、标题`Radware Bot Manager Captcha`，文件头不是`%PDF`，因此未获取原始全文，不声称机构无权或原文不存在。

具体访问结果：[历史来源元数据/路径回执](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/historical-source-access-001.json)、[实际响应格式](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/historical-source-format-001.json)。此处保存可复用的来源身份/访问区别；tmp中的下载manifest不作科学事实源。后续可换合法机构/作者公开仓储或其它独立原件，不重复同一受阻端点，也不绕过挑战。

## Reproducibility and Research Status

定量副本与代码：[audit_131xe.py](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/audit_131xe.py)、[table-audit-001.json](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/table-audit-001.json)。仅用Python标准库，入口验证两个原PDF哈希；0.5-keV候选比较窗只作账本筛选，不是误差判据，符合/端点核验仍需回原件。真实source解释与全部可复用数值/限制已保存在本页，outputs不是事实的唯一副本。

**Knowledge Impact and Learning Decision — revises / limits。** 修正整带同义化及旧排他性断言；暂不改变作者的有界signature-partner偏好。下一步优先取得1983角分布原文及其δ约定，并查明794.8-keV宇称修订和Fig.5两解的联合响应依据。本研究为active-L3 / candidate-L4，未进入事件级L4，不代表Day28日程收束。
