---
type: research-note
title: "同核异能态与六区动力学：候选判别和反方检验"
aliases: [isomer-cross-region-hypothesis-discrimination-20261107, 跨区异能态假说鉴别与反方审计]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
created_from: "Gemini candidate draft and Sol source-conditioned integration"
evidence_sources: [dracoulis-2013-192os-isomers-gamma-soft, hayes-2005-k-conservation-178hf, karmakar-2024-100ru-enhanced-e1-lifetimes, karmakar-2023-2024-100ru-alternate-parity-bands, karmakar-2025-2026-98mo-octupole-preview, liu-chen-2016-78br-chirality-reflection-symmetry-thesis, peng-2019-possible-chiral-doublets-60ni, zhang-2016-two-quasiparticle-bands-166ta, guo-2022-mo93m-isomer-beam-depletion-limit]
tags: [isomer, cross-region, hypothesis, falsification, l3, l4]
---

# 跨区候选的判别与反方检验

## Research Trigger

用户要求探索某一区已有物理能否迁移，以及现有特征能否产生其它可检验候选。
Gemini提出候选草案，总控核对来源、模型和判据后压实为四个问题。
本页是本任务推断，不是新增实验、全球新颖性认证或某个模型的排他性证明。
项目总入口为[[isomer-six-region-transfer-research]]。

## Grounded Evidence

| 原件锚点 | 实际依据 | 使用边界 |
|---|---|---|
| [[dracoulis-2013-192os-isomers-gamma-soft]] Table1，pp.331–334 | 12+的111.5与445.7-keV E2分支分别为9.7(26)与4.4(9)×10−2 W.u.；PES按组态分别最小化 | 分支不同不是形状隧穿的唯一证据；表中τ为平均寿命 |
| [[hayes-2005-k-conservation-178hf]] PDF pp.279–281 | 低K带的顺排/混合与高K带自身纯度可以不同 | 对某个态对的分析不能变成所有K异能态的定律 |
| [[karmakar-2024-100ru-enhanced-e1-lifetimes]]；[[karmakar-2023-2024-100ru-alternate-parity-bands]] | 100Ru交替宇称谱学与后续寿命原件分别提供网络和绝对率的来源 | 同一作者群、带结构与后续数据的依赖须保留；详表以两篇source为准 |
| [[karmakar-2025-2026-98mo-octupole-preview]] p.1 | 摘要报告两条E3跃迁并提出八极集体性候选 | 本轮仅有首页，未取得增强B(E3)的独立测量 |
| [[liu-chen-2016-78br-chirality-reflection-symmetry-thesis]] PDF pp.78–82、90 | 八极关联、多重手征候选与不同模型；CPQ列为未来问题 | 不能由八条E1线认证四条带的完整静态CPQ网络 |
| [[peng-2019-possible-chiral-doublets-60ni]] 模型与方位分布；[[zhang-2016-two-quasiparticle-bands-166ta]] Hamiltonian | 前者给跨壳手征候选，后者采用轴对称输入 | 不是实测静态手征，也不能由轴对称计算排除未开放的γ自由度 |
| [[guo-2022-mo93m-isomer-beam-depletion-limit]] pp.1–4、Eqs.1–3 | 隔离束条件下无显著峰，约2×10−5上限包含效率/门/ICC等输入 | 不证明所有NEEC不存在，也不唯一重建2018背景 |

## Provisional Reasoning

### C1：N≈56的八极关联是否改变取向运动

**假设。** 在一个明确的奇A/奇奇组态中，八极混合改变高j成分、惯量响应和
取向分布，使与无八极混合的共同输入模型可区分。100Ru/98Mo提供邻近核芯比较，
不是已证明具有手征—八极复合模式的两个目标。

**竞争解释。** 动态八极振动、反射对称组态混合、偶极极化与自旋相关配对
都可能改变E1和能谱；非零E1或较平滑D0不唯一识别静态形变。

**下一项判别。** 先把已有100Ru寿命、分支和误差接入同一观测表，
核对模型实际算了哪些电磁算符，再比较E3及伙伴分辨的电磁网络。
奇粒子取向计算还需指定组态与共同Hamiltonian。
若不含所提耦合的模型已解释这些联合数据，降低新增耦合的必要性。
当前为L3；没有微观输入时不从示意势能项直接生成真实核L4。

### C2：Os多分支异能态能否区分形状变化与K混合

**假设。** 同母态多分支的矩阵元及其相关误差，比一个总寿命更能限制初末态
重叠与K分布。需要比较低Eγ/高L、K混合和组态依赖形状等解释。

**竞争解释。** 同一形状下的态混合、偶然近简并、末态结构差异和相干相消，
也可产生很不均匀的分支；单个宽度比并不要求形状隧穿。

**下一项判别。** 整理Table1的支路、ICC和寿命定义，使用同一算符分别计算
保持/改变形状的模型对全部相关矩阵元的预测。
现有实验表可以支持数据整理，但没有提供完整微观Hamiltonian、投影波函数、
集体惯量和误差预算，因此尚不等于形状重叠L4-ready。
若固定形状模型已解释联合数据，则不需要新增形状机制；
一个固定形状模型失败也不自动证明另一模型唯一正确。

### C3：轻区与稀土的激发组态取向窗口

**假设。** 适合非共面取向或摆动的窗口由具体组态、恢复力、惯量、配对与
带终止共同决定，可与基态附近的形状不同。

**竞争解释。** signature、γ激发、不同组态和偶然接近可模仿部分能谱。
不能用“轻核容易终止”替代计算，也不能用166Ta的轴对称输入替代γ稳定性测量。

**下一项判别。** 先审计实际已有能级/强度范围，再用相同输入比较方位概率、
带内/带外矩阵元与组态变化。精确有限核态的有符号手征期望可为零，
不能要求实验或对称本征态必须有一个非零有符号三脚架。
若取向局域化在可布居范围内不存在，或者竞争组态更好解释联合数据，
撤回该具体候选。当前L3，不预设固定临界自旋或宣称现时文献完全缺失。

### C4：热化、受激耗散与核钟可迁移哪些机制

**问题。** 比较可迁移的选择定则、共振匹配、分支网络和时标；
分别判断天体独立物种、净耗散率和可用核钟，而不把三者合成一个效率。

**竞争解释。** 未知feeding、电子态、时间门和环境变化都可改变推断；
一套微观过程存在不意味着其速率可测或适合应用。

**下一项判别。** 电子过程需要电荷态分布、能谱/空穴及背景控制；
热化需要中间态宽度和温度轨迹；核钟需要宿主、激发/探测、锁定和不确定度。
比较共同输入下的电荷态/能量响应或耦合态布居网络。
没有这些输入时保持L3，不以任意Z幂律、能隙或增强因子生成应用率。
热交换慢于环境变化时，反而可能更需要显式独立态网络，不能据此删掉异能态。

## Assumptions

逐条核对自旋、宇称、带/支路身份、寿命定义、混合比各解及算符单位。
模型轴序与γ约定要转换；不是预先假定已对齐。
feeding、未见线、ICC和协方差按实际资料处理，不假定已经全部消除。

## Competing Explanations

候选比较使用共同数据和尽可能一致的输入/算符。
理论失败须区分参数失配、计算近似与机制失败。
不存在通用E3阈值、D0饱和值或某个强度比即可排他判定的规则。

## Transfer Conditions

迁移须检查价核芯、粒子/空穴、可及态、配对/阻塞、组态形变与观测通道。
[[seniority-mid-shell-cross-region-model-test-20261107]]给出严格的否定例：
单j的n−v须为偶数，g9/2的Ω=5不允许偶粒子v=2链达到n=5；
n=4/6的理想强度是n=2的1/9。h11/2的Ω=6则允许该链的中壳节点。
此处是代数适用域，不是对特定核寿命的预报。

## Failure Conditions

数据不足以区分模型、关键微观输入缺失、来源重复同一采集、
或预报落在没有搜索灵敏度的范围时，不将结果写成新发现。
停止某项定量计算不意味着该机制在整个质量区不存在。

## Falsification or Reverse Tests

本轮精确模型的H为−A00†A00+εΣA2M†A2M，后项是J=2对通道，不能改名为Q·Q。
在被跟踪的n=6同粒子—空穴signature态间，E2在共轭下为奇，节点仍受保护。
相反signature的v=4简并子空间则有非零总强度；该控制在此Hamiltonian中是向上激发，
不能叫异能态退激分支。解除对称性禁戒也只表示允许，不保证矩阵元非零。
以上反向检验限定了“任何非配对混合都会解除节点”的错误直觉。

## Open Questions

短期优先处理已经有可读原件的100Ru寿命/模型比较，以及192Os的分支/ICC数据表。
取向耦合和天体/电子过程的具体L4，等可靠输入后再选；不从概念相似跳过这些缺口。
全局新颖性、预测态的现时发现状态和具体装置实验可行性仍需定向检索。

## Human Review

本次为Agent草案及总控原件自审，没有新增人工审核事件。
review元数据不赋予或撤销知识资格。

## Promotion or Rejection History

2026-11-07保留Gemini草案的四候选与反方比较结构，撤回其中未经支持的
E3硬阈值、固定临界自旋、Z幂律、Os微观输入已完备、NEEC背景唯一归属，
并修正误写的Q·Q扰动、出处与转义控制字符。未把草案审核当作独立实验。
