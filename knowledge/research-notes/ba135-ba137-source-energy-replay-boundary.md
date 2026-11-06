---
type: research-note
title: "135/137Ba来源能谱重放：few-keV差别与实验态对应边界"
aliases: [135Ba137Ba来源能谱重放, Ba source energy replay boundary]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nomura-2017-odd-mass-gamma-soft-shape-transitions]
created_from: "用户授权的source-chain-replay有界能谱核查；本页仅整理已冻结结果"
promotion_target:
nuclei: [134ba, 135ba, 136ba, 137ba]
tags: [a130, ibfm, source-replay, negative-parity, state-assignment, reproducibility]
---

# 135/137Ba来源能谱重放及其边界

## Research Trigger

既有 \(^{129}\)Ba 低能理论子集的约1-keV重放，不能自动认证整条奇Ba链。母任务还存在 \(^{137}\)Ba 实验态对应的不确定性，因此独立提取 [[nomura-2017-odd-mass-gamma-soft-shape-transitions]] 的 \(^{135,137}\)Ba 负宇称理论能谱，再与既定 kernel 比较，明确“接近来源计算”与“确认实验态身份”的距离。

本页只整理已完成的有界核查，不新增计算、文献检索、参数拟合或电磁预测。结果是：**两核图示六态的排序均一致，但逐点差别最大为1.896和3.128 keV，不能声称全部点在1 keV内重放。作者实际运行身份及实验态对应仍未确认。**

## Grounded Evidence

原始文献入口为 [[nomura-2017-odd-mass-gamma-soft-shape-transitions]]，Nomura、Nikšić、Vretenar，*Phys. Rev. C* **96**, 014304 (2017)，DOI `10.1103/PhysRevC.96.014304`。本次实际读取的是该 source 登记的 **13页 arXiv:1704.07101v2**；未另行核验期刊 VoR。

- [canonical本地PDF](</workspace/wiki/raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf>)：物理页7，Fig.5(c)，负宇称理论列，\(N=79,81\)。SHA-256：`481e6a9e0f6b01e9c5db5e2b06d9b350dba0638393c7da7f532c3040e9efaea9`。
- [arXiv-v2原始源码归档](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/nomura2017-v2-source.tar.gz)：成员 `ba.level.pdf`，图件SHA-256：`b6006a11da9e56b14e31f286cedfe339fda90626bba7632fd934cc78ba861ef2`；归档SHA-256：`f7ed6dc746f50f16169d8796e4d12becd8827eaf4ac2ee4d5f1ff9cd04690faf`。
- [原始TeX804–809](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:804)：Fig.5图件与图注；[TeX851–856](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:851)：最低负宇称态自旋变化的正文说明。
- Hamiltonian与打印参数定位：PDF pp.2–4，Eqs.(1)–(6)、Tables I、III、V；[TeX200–258](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:200)、[301–302](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:301)、[392–393](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:392)、[517–518](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:517)。

以下来源列是**作者模型图示值**，kernel列是**本任务固定实现的模型结果**，差值是二者的比较；均不是新实验数据。12点全部保留，不因差别大小删点。统一定义

\[
\Delta E_J=E(J^-_{\mathrm{lowest}})-E(11/2^-_{\mathrm{lowest}}),
\qquad
\delta=\Delta E_{\rm kernel}-\Delta E_{\rm source}.
\]

两核的来源 \(11/2^-\) 点均在图中零点，当前 kernel 也以该态为负宇称空间最低态。没有拟合能量平移或比例；此零点不等于相对正宇称核基态的绝对激发能。

| 核素 | \(N\) | 图例 \(J^\pi\) | 来源图示 / keV | 当前kernel / keV | \(\delta\) / keV | 原图vector path |
|---|---:|---|---:|---:|---:|---:|
| 135Ba | 79 | \(7/2^-\) | 918 | 919.361798 | +1.361798 | 155 |
| 135Ba | 79 | \(9/2^-\) | 448 | 449.895699 | +1.895699 | 161 |
| 135Ba | 79 | \(11/2^-\) | 0 | 0.000000 | 0.000000 | 167 |
| 135Ba | 79 | \(13/2^-\) | 404 | 404.585404 | +0.585404 | 173 |
| 135Ba | 79 | \(15/2^-\) | 691 | 691.863295 | +0.863295 | 179 |
| 135Ba | 79 | \(17/2^-\) | 1180 | 1181.063643 | +1.063643 | 185 |
| 137Ba | 81 | \(7/2^-\) | 1122 | 1125.043145 | +3.043145 | 156 |
| 137Ba | 81 | \(9/2^-\) | 414 | 417.128165 | +3.128165 | 162 |
| 137Ba | 81 | \(11/2^-\) | 0 | 0.000000 | 0.000000 | 168 |
| 137Ba | 81 | \(13/2^-\) | 607 | 606.856444 | −0.143556 | 174 |
| 137Ba | 81 | \(15/2^-\) | 968 | 968.873920 | +0.873920 | 180 |
| 137Ba | 81 | \(17/2^-\) | 1880 | 1880.069173 | +0.069173 | 186 |

Vector path是上述固定图件在记录版本PyMuPDF下的绘图路径定位符，不是能级序号。图例映射为：绿色左三角 \(7/2^-\)、黄色下三角 \(9/2^-\)、黑圆 \(11/2^-\)、蓝色上三角 \(13/2^-\)、红方形 \(15/2^-\)、青色星形 \(17/2^-\)。来源取自理论(c)列，未把实验(d)列混入。

原图纵轴以 \(y=349.1919555664\) pt 为0 MeV、\(y=186.2499542236\) pt 为2 MeV，坐标原点在左上方；0.5、1.0、1.5 MeV刻度另行核对。星形取旋转中心，三角形取顶点—底边中点，不用会造成偏差的形状质心。原图与canonical PDF内嵌图是**同一来源的两种表示**，不算两份独立物理证据。

## Provisional Reasoning

去掉每核固定零点后，已有比较给出：

| 核素 | 非参考点数 | 最大绝对差 / keV | RMS差 / keV | ±0.5 keV窗口内 | ±1 keV窗口内 |
|---|---:|---:|---:|---:|---:|
| 135Ba | 5 | 1.895699 | 1.238344 | 0/5 | 2/5 |
| 137Ba | 5 | 3.128165 | 1.991747 | 2/5 | 3/5 |

窗口统计包含预先声明的0.002 keV数值提取容差。原图点接近整数keV网格，但作者绘图的具体取整规则未知；±0.5/±1 keV只是显示精度敏感性窗口，不是实验误差、参数误差或统计置信区间。

两核图示子集的能量排序均重放：135Ba为 \(11/2,13/2,9/2,15/2,7/2,17/2\)，137Ba为 \(11/2,9/2,13/2,15/2,7/2,17/2\)。这支持既定重构与该低能来源子集接近；仍有few-keV差别，不能推广为逐点精确一致或整条链认证。

| ID | 主张 | claim_kind | evidence_level | source_independence | confidence | locator | needs_review |
|---|---|---|---|---|---|---|---|
| BA-SREP-1 | 两核12个负宇称理论图点及其相对11/2零点已独立提取并冻结 | model-result | direct | single | high | arXiv v2 p.7 Fig.5(c)，N79/81；上表vector path；TeX804–809 | false |
| BA-SREP-2 | 固定kernel保留图示排序，但最大差为1.895699/3.128165 keV | model-result | direct | single | high | 上表；既有comparison.csv及run.json；原文Tables I/III/V | false |
| BA-SREP-3 | A−1芯与NB5/4有文本和计数依据，但不是作者实际运行卡身份 | our-inference | indirect | single | medium | TeX200–207、315–319、692–696、918–927；Table I无NB列 | true |
| BA-SREP-4 | 当前子集不能核验19/2态、EM生产者身份或实验同态映射 | our-inference | direct | single | high | Fig.5(c)只示7/2至17/2系列；TeX899–913为正宇称Fig.9；TeX539–545只说明PBOS求解 | false |

## Assumptions

固定实现沿用既有链合同：135Ba采用134Ba芯、\(N_B=5\)，137Ba采用136Ba芯、\(N_B=4\)，负宇称空间为单 \(h_{11/2}\)，使用Tables I、III、V的打印参数和固定 \(Q_{jj}=-\sqrt{525/(143\pi)}\)。未调整耦合、符号、正规排序、归一化或芯身份以改善差别。

[TeX918–927](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:918)明确把134Ba称为135Ba的对应芯，但上下文是正宇称E(5/4)讨论。137Ba–136Ba采用A−1链关系重构，未找到逐核执行输入。按该芯选择，\(Z=56\)对应3个质子对，134/136Ba芯分别有2/1个相对 \(N=82\) 的中子空穴对，得到 \(N_B=5/4\)。一般定义见TeX200–207，壳层见315–319，空穴表述见692–696；这些文字不能替代实际PBOS输入卡。

负宇称图例只给自旋宇称，没有显式同自旋序号或作者波函数。本次固定与最低同自旋kernel态比较，未改配到能量更接近的高态。单j费米子共同能移从相对能量中消去，不能用它解释自旋间差值。

## Competing Explanations

几keV差别可能涉及未印出的参数精度、绘图取整或实际执行约定，当前没有证据确定主因。已测得的矢量提取差不足以解释全部差别；特别是超过1 keV的点，不能一概算作1-keV网格内一致。

芯/\(N_B\)、粒子—空穴约定、\(Q_{jj}\)符号、交换及monopole映射、\(Q\cdot Q\)的一体收缩和尺度都可能改变Hamiltonian身份。这些只作为解释边界记录，没有进行替代实现扫描，也不因某个替代输入可能更贴合而选用它。没有“修正已发表代码”的结论。

## Transfer Conditions

本结果可支持限定表述：“在所声明的单j实现、原文打印参数和A−1芯重构下，135/137Ba图示负宇称理论子集的排序一致，能量相差至多约3.13 keV。”

不能把它转移为对所有同位素、所有能级、作者波函数、实验态身份或EM算符的认证。能谱接近也不证明当前有效电荷、静态矩、跃迁强度或四极不变量已复现作者运行。原图中的 \(15/2^-\) 理论系列与某个实验候选的对应关系，仍需另有证据。

## Failure Conditions

若改变原件版本、图例/理论列识别、坐标标定、能量参考或同自旋态选择，则本冻结比较不能直接沿用。若采用不同芯、\(N_B\)、符号、归一化或参数，须视为另一Hamiltonian，而非本结果的继续认证。

把来源图点当成实验观测、把0-keV负宇称参考当成绝对核基态、把几keV差别隐去，或把缺少19/2及EM检验写成已通过，均超出证据边界。

## Falsification or Reverse Tests

既有记录已完成如下技术核对，本页不重跑：

- 12个来源图点于2026-11-06 **09:33:07 UTC** 冻结；固定比较于 **09:36:57 UTC** 开始。来源JSON SHA-256为 `bc4dbed2c29f65ae8f9546cd146005efa6dbb64eb08ef23781ede6f907b91d22`。
- 原始矢量图与canonical内嵌图的最大能量提取差为 **0.000692 keV**；全部来源点距离整数keV网格小于0.000204 keV。
- 既有固定运行保留完整 \(M=1/2\) 块，维数分别为226、119；两套加载的OpenBLAS均为单线程，Hamiltonian/输入哈希前后匹配。
- 所有12点保留在表中；未剔除超出预设窗口的点，未把零参考点计入RMS和窗口通过数。

可复现工件：[冻结图点及坐标](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/source-chain-replay/source-points-frozen.json)、[冻结比较合同](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/source-chain-replay/comparison-contract.json)、[逐点比较](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/source-chain-replay/comparison.csv)、[运行记录](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/source-chain-replay/run.json)、[清单](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/source-chain-replay/artifact-inventory.json)、[完整审计说明](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/source-chain-replay/report.md)。它们是计算与提取审计工件；原文事实仍回链上列Nomura source、原始PDF/TeX和图件。

## Open Questions

- 作者实际PBOS输入卡、未圆整参数及对应波函数/EM运行卡未取得，不能确认执行身份。
- Fig.5(c)没有 \(19/2^-\) 或更高同自旋态；[Fig.9及TeX899–913](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex:899)只补充135Ba正宇称谱，不能填补该缺口。
- \(^{137}\)Ba异构态及其跃迁涉及的实验态对应，不由本能谱子集核查解决。
- 本sidecar没有EM拟合或原作者EM图件重放，也未单独比较期刊VoR；few-keV差别的具体原因仍未知。

这些是未解决边界，不是本轮继续运行的任务清单。

## Human Review

2026-11-06用户表示已读source-chain-replay报告，并明确授权新增本专属知识页。该事件不等于对本页每条主张的人工核验；新页保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-11-06：按用户授权，将已冻结的12点、残差、来源定位和适用边界整理为 `reasoning_status: provisional` 的research-note；没有新增计算或检索，没有修改共享source、index或handoff，也未将此页晋升为作者运行认证或投稿就绪结论。
