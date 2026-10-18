---
type: source
title: "γ-ray linear polarization measurement and (g9/2)−3 neutron alignment in 91Ru"
aliases: ["Zheng 2013 91Ru polarization", "91Ru EXOGAM linear polarization"]
created: 2026-09-20
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "γ-ray linear polarization measurements and (g9/2)−3 neutron alignment in 91Ru"
authors: ["Y. Zheng", "G. de France", "E. Clément", "A. Dijon", "B. Cederwall", "R. Wadsworth", "T. Bäck", "F. Ghazi Moradi", "G. Jaworski", "B. M. Nyakó", "J. Nyberg", "M. Palacz", "H. Al-Azri", "G. de Angelis", "A. Atac", "Ö. Aktaş", "S. Bhattacharyya", "T. Brock", "P. J. Davies", "A. Di Nitto", "Zs. Dombrádi", "A. Gadea", "J. Gál", "P. Joshi", "K. Juhász", "R. Julin", "A. Jungclaus", "G. Kalinka", "J. Kownacki", "G. La Rana", "S. M. Lenzi", "J. Molnár", "R. Moro", "D. R. Napoli", "B. S. Nara Singh", "A. Persson", "F. Recchia", "M. Sandzelius", "J.-N. Scheurer", "G. Sletten", "D. Sohler", "P.-A. Söderström", "M. J. Taylor", "J. Timár", "J. J. Valiente-Dobon", "E. Vardaci"]
journal: "Physical Review C"
year: 2013
volume: 87
issue: 4
pages: "044328"
doi: "10.1103/PhysRevC.87.044328"
citation_key: Zheng_2013
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Zheng, Y. et al. Gamma-ray linear polarization measurement and (g9/2)−3 neutron alignment in 91Ru. Phys. Rev. C 87, 044328 (2013)."
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2013_Zheng et al_γ -ray linear polarization measurements and ( g 9 - 2 ) − 3 neutron alignment.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2013_Zheng et al_γ -ray linear polarization measurements and ( g 9 - 2 ) − 3 neutron alignment.pdf"
raw_sha256: "0688633ba372e7f3f60b2e9fd69e556d28070b2f5bde62d13d01d1bd9a5483ef"
nuclei: ["91Ru", "91Tc", "90Mo", "88Mo"]
reactions: ["58Ni(36Ar,2p1n)91Ru"]
experiments: ["ganil-exogam-91ru-ar36-111mev"]
models: ["semiempirical-shell-model"]
observables: ["linear-polarization", "polarization-asymmetry", "dco-ratio", "angular-distribution", "gamma-ray-intensity", "alignment"]
methods: ["gamma-gamma-coincidence", "compton-polarimetry", "linear-polarization-asymmetry", "dco-ratio", "angular-distribution"]
tags: [91Ru, 91Tc, EXOGAM, clover-polarimeter, linear-polarization, neutron-alignment, g9-2]
---

# γ-ray linear polarization measurements and (g9/2)−3 neutron alignment in 91Ru

## Bibliographic Record

- 作者：Y. Zheng 等；Physical Review C 87, 044328 (2013)。DOI：`10.1103/PhysRevC.87.044328`。
- 论文电子重印包含原文前置信息和 Physical Review C 正文；正文物理页码为 044328-1 至 044328-10。
- 原始文件：`raw/papers/gpt/high-spin-20260920/纲图/2013_Zheng et al_γ -ray linear polarization measurements and ( g 9 - 2 ) − 3 neutron alignment.pdf`；SHA-256：`0688633ba372e7f3f60b2e9fd69e556d28070b2f5bde62d13d01d1bd9a5483ef`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 电子重印与正文 11 页全部阅读；反应、EXOGAM/Neutron Wall/DIAMANT 装置、DCO 公式、Compton polarimeter 定义与校准、Tables I-II、Figs.1-8、91Ru 能级图、半经验壳模型和总结均已核对。关键谱图、偏振校准图、`A-R_DCO` 图、能级图和 shell-model energy comparison 视觉核对。
- Not covered: 事件级 γγ 矩阵、EXOGAM response 文件、原始 shell-model 输入代码和引用论文全文。
- Coverage caveats: `91Ru` 基态 `Jπ=(9/2+)` 是作者采用的假设；因此除 `(31/2+)` 外的许多绝对自旋宇称赋值在该基态假设下成立。作者总结也明确保留这一边界。

## Paper Question and Scientific Motivation

- 论文用线偏振、角分布和 DCO 联合确定 `91Ru` 高自旋跃迁的电磁性质、自旋差和宇称，解决早期只靠系统学/DCO 的大不确定性（PDF pp.1-2）。
- 物理问题是 `N=47`、`g9/2` 中子空穴与质子激发之间的竞争：`ν(g9/2)−3` 可产生至 `21/2+` 的中子全顺排结构，而 `π(g9/2)2ν(g9/2)−1` 可延伸至 `25/2+`；非 yrast `(21/2+)`、`(17/2+)` 是否为 seniority-three `ν(g9/2)−3` 相关结构是主要结构问题（PDF pp.1-2, 8-10）。

## Method and Design Logic

- 反应为 `58Ni(36Ar,2p1n)91Ru`，束流 `111 MeV`、约 `10 pnA`；`EXOGAM` 使用 11 个 clover（7 个 `90°`、4 个 `135°`），Neutron Wall 50 个液闪单元，DIAMANT 80 个 CsI，触发要求至少一个中子和一个 γ；共记录约 `4×109` events（PDF p.2）。
- DCO 以 `90°/135°` 非对称 γγ 矩阵构造，定义
  \[
  R_{DCO}=\frac{I(\gamma_1\;135^\circ;\,\gamma_2\;90^\circ)}{I(\gamma_1\;90^\circ;\,\gamma_2\;135^\circ)}.
  \]
  `90°` 与 `135°` 效率行为相同，实验证得 `R_eff=1.79±0.05`，因此无需额外能量效率修正（PDF pp.2-3，式 (1)）。
- EXOGAM clover 作为 Compton polarimeter：在 `90°` clover 中选相邻晶体的水平/垂直散射，定义
  `A=([a(Eγ)N⊥]−N∥)/([a(Eγ)N⊥]+N∥)`，并用无偏振 `152Eu` 源得到 `a(Eγ)=a0+a1Eγ`，其中 `a0=1.05(3)`、`a1=3.9(9)×10−5 keV−1`（PDF pp.4-5，式 (2)-(4)）。
- 物理偏振与实验不对称满足 `A=QP`；点状 polarimeter 的 Klein-Nishina sensitivity 结合有限晶体响应给出 `Q=Qpoint(p0+p1Eγ)`。用已知纯 E2 线的角分布求 `P`，拟合得到 `p0=0.39(2)`、`p1=0.00006(3)`（PDF pp.4-5，式 (5)-(7)，Table I，Fig.5）。

## Key Evidence and Reasoning Chain

1. 已知 stretched quadrupole 的 `R_DCO≈1`、纯 stretched dipole 的 `R_DCO≈0.6`（四极门）用于初步多极性标定；DCO 对混合跃迁和非 stretched 跃迁有多解边界（PDF pp.2-3）。
2. 线偏振不对称的符号区分 stretched electric 与 magnetic character；与 DCO 联合可以区分 E1/M1/E2 和 nonstretched E1 的歧义（PDF pp.3-5，Fig.6）。
3. 在 `91Ru` 中，强正宇称序列 `974, 898, 497, 823, 959, 957 keV` 具有四极 DCO 与正偏振，支持其 stretched E2 性质；328、919 keV 连接线为 nonstretched E1，负宇称结构由偏振和 DCO 共同约束（PDF pp.6-8，Table II，Fig.7）。
4. 新观察到 436、491、1127 keV 等跃迁；491 和 436 keV 级联把第二个 `(17/2+)` 与 `(21/2+)` 状态放在 `2363`、`2799 keV`，但除 `(31/2+)` 外的绝对赋值依赖 `(9/2+)` 基态假设（PDF pp.6-8）。
5. 半经验壳模型把 yrast `(21/2+),(17/2+)` 与 `π(g9/2)2ν(g9/2)−2ν(g9/2)−1` 类多粒子-空穴结构联系起来，并把非 yrast `(21/2+),(17/2+)` 与 `π(g9/2)4ν(g9/2)−3` 的 `Jmax/Jmax−2` seniority-three 结构联系起来；计算能量与观察值接近（PDF pp.8-10，Fig.8）。

## Summary

这项 `91Ru` 熔合蒸发实验用 EXOGAM clover 的 Compton 线偏振、DCO 和角分布联合约束高自旋能级的电磁性质与宇称。论文通过已知 E2 线校准 `Q(Eγ)`，并以 `A=QP` 把探测器不对称转成物理偏振。该联合证据扩展了 `91Ru` 能级图、发现非 yrast `(17/2+)` 和 `(21/2+)` 状态，并提出其与 `g9/2` 中子空穴 seniority-three 结构的对应。由于基态宇称/自旋是假设，论文将绝对赋值保留为相应条件下的结果。

## Experimental or Theoretical Setup

- 反应：`58Ni(36Ar,2p1n)91Ru`，`111 MeV`，平均 `10 pnA`。
- 阵列：EXOGAM 11 clovers；Neutron Wall；DIAMANT；约 `4×109` triggered events。
- 分析：γγ coincidence、DCO、角分布、clover Compton polarization；Shell-model semiempirical energy estimates。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z13-1 | EXOGAM `90°` clover 的 polarization calibration 覆盖约 `0.3-1.3 MeV`；`Q(Eγ)` 用已知纯 E2 线和角分布确定。 | experimental-result | direct | PDF pp.4-5，Table I，Fig.5 | false |
| Z13-2 | `A=QP`，`a(Eγ)=1.05(3)+3.9(9)×10−5 Eγ`；拟合 `p0=0.39(2)`、`p1=0.00006(3)`。 | method-calibration | direct | PDF pp.4-5，式 (2)-(7)，Fig.4-5 | false |
| Z13-3 | 328、919 keV 为 nonstretched E1；812、721、253 keV 等负宇称带跃迁具有 stretched M1/E1 约束，具体逐线赋值见 Table II/Fig.7。 | experimental-fact/criterion | direct | PDF pp.6-8，Table II，Fig.6-7 | false |
| Z13-4 | 新的 `(17/2+_2)`、`(21/2+_2)` 状态位于约 `2363`、`2799 keV`，由 491/436 keV 级联建立。 | experimental-result | direct | PDF pp.6-8，Fig.7 | false |
| Z13-5 | 非 yrast `(21/2+_2)`、`(17/2+_2)` 可由 `π(g9/2)4ν(g9/2)−3` seniority-three `Jmax/Jmax−2` 结构解释。 | model-result/author-interpretation | direct | PDF pp.8-10，Fig.8，shell-model section | true |

## Nuclear Structure Information

- `91Ru` 采用 `(9/2+)` 基态假设；正宇称 yrast 序列由 974、898、497、823、959、957 keV 等跃迁连接。
- 新增/确认非 yrast 正宇称结构：`17/2+_2`（2363 keV）和 `21/2+_2`（2799 keV）；两者之间由 436/491 keV 级联约束。
- 负宇称结构含 `13/2−`、`17/2−`、`19/2−`、`21/2−`、`25/2−` 等候选，偏振为 parity 约束关键。

## Authors' Interpretation

- 作者把线偏振和 DCO 的联合测量视为从“系统学/间接证据”走向较强自旋宇称赋值的关键。
- 作者把非 yrast 正宇称状态解释为 `g9/2` 质子/中子空穴的 seniority-three 多粒子结构，但承认基态 `Jπ` 未被直接测量，因而绝对 assignments 仍有条件。

## Model Results

- 半经验 shell model 使用邻核已知构型能量、单粒子能量和两体相互作用估计复杂多粒子-空穴组态。
- 对 yrast `(21/2+_1,17/2+_1)` 计算约 `2399/2024 keV`，观察值约 `2369/1872 keV`；对非 yrast `(21/2+_2,17/2+_2)` 计算约 `2774/2092 keV`，观察值约 `2799/2363 keV`。这些接近支持构型解释，但不提供唯一波函数分解。

## Competing Interpretations and Limitations

- DCO 单独对混合跃迁、非 stretched 跃迁有多解；偏振联合测量减少但不自动消除所有分支歧义。
- `91Ru` 基态自旋宇称未直接测量；因此许多 level assignments 是 conditional/tentative，`31/2+` 仍特别保留不确定性。
- 论文未对左侧负宇称结构全部做线偏振测量；部分 assignments 仍依赖先前工作和局部连接关系。
- Shell-model 构型能量来自半经验邻核输入，属于模型结果而非直接观测。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-Z13-1 | Core reconstruction | 本文的主要增量是“偏振+角分布+DCO”联合证据链，而非单一偏振符号判定。 | PDF pp.2-8 | self-checking |
| AR-Z13-2 | Assumptions and dependencies | 依赖 clover `a(Eγ)`、`Q(Eγ)` 校准、已知 E2 参考线、角分布系数和 gate purity。 | PDF pp.4-5，Table I | self-checking |
| AR-Z13-3 | Transfer conditions | `A=QP` 和 Compton calibration 可迁移为方法框架；`Q(Eγ)`、符号约定、统计和阵列几何必须逐阵列重标定。 | PDF pp.4-5 | provisional |
| AR-Z13-4 | Failure conditions | 弱峰、门控污染、未知基态 `Jπ`、未测偏振的结构和混合跃迁会使绝对 assignments 不唯一。 | PDF pp.6-8，Summary | active-L3 |
| AR-Z13-5 | Reverse/falsification test | 用独立基态自旋/宇称、更多 polarization lines、branching/寿命或邻核 g-factor 数据检验 `g9/2` seniority-three assignments。 | PDF pp.1,8-10 | candidate-L3 |
| AR-Z13-6 | Research-question decision | 该来源适合作为线偏振—DCO—自旋宇称联合判据和 `g9/2` alignment 案例，不启动独立 L4。 | PDF pp.2-8 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有线偏振、Compton `P/A/Q`、DCO 和 `91Ru` 之外的高自旋 assignments 方法页；本来源补充 EXOGAM clover 的实际校准和一个 `g9/2` seniority-three 案例。
- Effect of this source: `supports` and `methodological-bridge`。
- Reason: 直接实验展示了 `A=QP`、`Q(Eγ)`、DCO 与线偏振如何联合约束 parity/multipolarity，并明确记录基态假设造成的 evidence boundary。
- Persistence decision: update [[linear-polarization-asymmetry]], [[compton-polarimetry]] and [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] as a source-level example; no independent 91Ru nucleus page yet。
- Review state: `unreviewed`; source claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[linear-polarization-asymmetry]] | EXOGAM clover `A/Q/P` calibration、符号和 DCO 联合使用案例。 |
| methodological-bridge | [[compton-polarimetry]] | 具体展示 clover 相邻晶体 Compton 散射、`Q(Eγ)` 和 figure of merit。 |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | 提供物理偏振、实验 asymmetry、响应校准和自旋宇称判据之间的完整实验链。 |

## Human Review Triage

### P0

- Z13-P0-1：`91Ru` 的绝对自旋宇称 assignments 依赖 `(9/2+)` 基态假设；论文级使用时必须保留该条件，不能把 Table II 的括号 assignments 写成无条件事实。

### P1

- Z13-P1-1：`g9/2` seniority-three 构型是半经验 shell-model 解释，需与邻核 g-factor、独立谱学或后续 shell-model 结果区分。

### P2/P3

- EXOGAM 的 `Q(Eγ)` 和 `a(Eγ)` 仅作为该装置校准记录；后续跨阵列比较需要各自 response source。

## Extracted Pages

- Nuclei: 暂不建立独立 `91Ru` 页；source 级记录核素与反应。
- Bands: `91Ru` level scheme 保留在 source，不创建未有稳定名称的 band 页。
- Concepts: 关联 `g9/2` neutron alignment、seniority-three、linear polarization。
- Methods: 更新 [[linear-polarization-asymmetry]]、[[compton-polarimetry]]。

## Non-source Notes and Follow-up

- 下一步：将 EXOGAM `A/Q/P` 校准、`F=1.51×10−5` 和基态假设边界加入方法页；后续处理 HS-005 等方法/纲图来源时比较独立性。


## DAY16延续：EXOGAM原表、门身份与校准误差边界

这是本run恰好Day17的无学分知识预习；正式课程仍只计Day16。2026-10-18本session沿原PDF全文主线重新阅读，视觉复核Figs.1–8、Tables I–II及Eqs.(1)–(9)中影响判读的内容。PDF第1页是电子重印wrapper；**正文044328-n对应PDF第n+1页**。旧字段、旧claim及其review标记原样保留；下列新增计算不由旧审阅状态背书。

### 新增原件证据与任务推断

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| Z13-6 | Fig.2三峰均用497-keV stretched E2门：616/898/974的135°/90°净面积分别2414(62)/4821(80)、6879(90)/7134(92)、6731(88)/7062(90)。Table II的898.5行改用974门，R=1.01(1)，不是Fig.2的497门R=.96(2)。 | experimental-fact | direct | 正文044328-3，Fig.2及其上方文字；044328-6，Table II的898.5行 | true |
| Z13-7 | 原Eq.(2)是aN⊥与N∥的差/和；a由无偏振152Eu定，Q由已知pure E2的A及角分布推得的P校准。Table II明列DCO门，但没有逐线Compton门、净散射计数或完整校准/背景Cov。 | method-calibration | direct | 正文044328-4，Eqs.(2)–(7)；044328-5，Table I；044328-6，Table II | true |
| Z13-8 | 328.0、919.8两条ΔJ=0的nonstretched E1都A<0；615.8 stretched M1也A<0。1280.7 stretched E1则A>0。电/磁判读须与spin path、门和geometry共同使用；绝对Jπ仍依赖(9/2+)基态假设。 | experimental-fact/author-interpretation | direct | 正文044328-6，Table II；044328-7，Fig.6及328/919/1280讨论；044328-9，Summary | true |
| Z13-9 | 条件性一阶传播中，若Table I的A、P、Q括号误差都是同一比值Q=A/P的marginal标准差，则σQ须在|σA/P−AσP/P²|到σA/P+AσP/P²之间。316、586、823、974、1054的印刷中央输入不满足；宽松允许中央值与各误差末位各±半位后，316、586、974、1054仍被保守下界排除。原误差语义/producer未得，不能由此判原实验错误。 | Codex-analysis | conditional-calculation | 正文044328-4，Eq.(4)；044328-5，Table I | true |
| Z13-10 | 以Table I十一项Q及括号误差为相互独立输入，声明的加权线性拟合得p0=.38616115、p1=7.3966836×10^-5 keV^-1，χ²=9.98029；原文p0=.39(2)、p1=.00006(3)、Fig.5标签χ²=11原样保留。没有原未舍入数据/权重/Cov，未认证原拟合复现。 | Codex-analysis | conditional-calculation | 正文044328-4，Eqs.(5)–(6)；044328-5，Table I及Fig.5 | true |
| Z13-11 | Q_i=A_i/P_i的校准点与相同A_i除回Qfit(E_i)共享输入；这种回代只检查样本内残差，不独立验证P。四个reaction-channel校准核素不自动代表四项独立Q标定；DCO/偏振/角分布及壳模型比较也不增计独立实验。 | Codex-inference | source-conditioned | 正文044328-4至5，校准程序；Table I；Fig.5 | true |
| Z13-12 | arXiv:1304.3287v1（2013-04-11）Table I的十一行A/A2/A4/P/Q印刷token与期刊一致；Table II upper435.9的A却是.17(7)，期刊为.17(5)。本次按期刊冻结输入，未把不同版本算独立实验或混用误差。 | source-version-audit | direct | arXiv v1 p.18，Table I；p.19，Table II的435.9行；期刊044328-6，同一行 | true |

### 明确门和能级身份的DCO重放

原Eq.(1)定义target在135°、gate在90°的yield为分子，互换两角为分母。若两个角组的效率曲线仅差常数c，符合效率乘积比为

\[
\frac{\epsilon_{135}(E_t)\epsilon_{90}(E_g)}
{\epsilon_{90}(E_t)\epsilon_{135}(E_g)}=1.
\]

所以原文测得R_eff=1.79(.05)后说“不需效率修正”，不能再给Fig.2的yield比额外乘1.79。由原面积直接重算三个R为.50072599、.96425568、.95312943。仅作诊断假设两拟峰面积独立时，σR为.015311、.017714、.017402；这没有补出实际背景/门共享Cov，也没有改写作者的.50(.02)、.96(.02)、.95(.02)。

898.5是1872→974、17/2+→13/2+；Table II用974门，Fig.2用497门。相同target能量不足以把这两项合成同一观测或声称数值冲突。436附近也要按parent/child区分：435.9是2799→2363的upper E2支，有R=1.02(.08)、A=.17(.05)；436.0是436→0的弱支，Table II未给R/A。538是974→436，DCO门361；不能把它的M1判据移给upper 436支。

### Table I：中央值相容与误差定义分开

全部11项的Eq.(7)中央P、及A/P中央Q在各输入与输出最后位舍入盒下相容。这个结论只涉及印刷中央值，并不认证同一误差预算。

对正A、P，令u=σA/P、v=AσP/P²，则一阶delta method给

\[
\sigma_Q^2=u^2+v^2-2\rho_{AP}uv,\qquad -1\le\rho_{AP}\le1.
\]

| Eγ / keV | 印刷A、P、Q | 名义σQ局部下界 | 印刷σQ | 宽松舍入后保守下界 / σQ上界 |
| --- | --- | --- | --- | --- |
| 316 | .17(2)、.513(2)、.331(8) | .0376944 | .008 | .0275456 / .0085 |
| 586 | .11(3)、.42(4)、.26(2) | .0464853 | .02 | .0287756 / .025 |
| 823 | .073(6)、.33(1)、.220(6) | .0114784 | .006 | .0059800 / .0065，不能稳健排除 |
| 974 | .139(4)、.71(8)、.195(6) | .0164253 | .006 | .0139359 / .0065 |
| 1054 | .114(5)、.57(6)、.201(6) | .0122807 | .006 | .0091464 / .0065 |

保守检查让每一中央值和每一括号σ都在最后位±半位内独立变化，再用u、v各自区间之间的距离作下界；它放宽了依赖约束，因此仍被排除的四项不能仅用这种printing rounding挽回。**这只否定“同一组marginal标准差经该一阶比值传播”的条件包**；原文未交代这些误差是否包含相同分量、拟合参数化/归一、其它处理或不同的σ含义，故保持未闭合，不更正原表，不设新实验显著性。对A2/A4→P的相同检查也在程序结果中保留为诊断，不据此替换源误差。

十一项Q的声明独立加权拟合参数相关为−.945826；其条件误差.0141178与1.71222×10^-5未包含未知跨点Cov。原printed参数的同一诊断χ²=13.0136，不能称原Fig.5精确重放或猜标签是reducedχ²。拟合的hat matrix trace=2，316点杠杆约.8597；同校准点回代的误差明显不应当作独立A与独立Q相加。

### 有符号偏振的真实反例及必要companion

| target / keV | Table II的parent→child / keV | ΔJ及作者性质 | RDCO（门 / keV） | A |
| --- | --- | --- | --- | --- |
| 328.0 | 2200→1872 | ΔJ=0，nonstretched E1 | 1.06(.05)，898 | −.25(.04) |
| 919.8 | 1893→974 | ΔJ=0，nonstretched E1 | .99(.04)，974 | −.07(.01) |
| 615.8 | 2985→2369 | ΔJ=1，stretched M1 | .50(.02)，497 | −.07(.01) |
| 1280.7 | 2254→974 | ΔJ=1，stretched E1 | .6(.1)，974 | +.14(.04) |

919.8与615.8连印刷A及σ都相同，电磁性质却不同。这直接限制了脱离spin/geometry的“负A必是M1”规则；由A=QP且本calibration Q>0可得偏振符号，但不能跳过ΔJ、相对宇称与branch身份。本文DCO/偏振组合支持作者的这些conditional assignments，未解除基态假设。Table II的gate栏仅是DCO门，未据它制造逐线polarization gate或假定Cov=0。

下一高信息输入是同门/同cut的Compton净面积和background ledger、校准A2/A4联合Cov、a0/a1与p0/p1及其跨点Cov/原拟合程序；不是强调某一个Q中央值或调响应来缩误差。当前结论为`supports`联合判据、`limits`单独符号与独立误差假设，未产生新Jπ、δ或独立实验。

复算材料：[冻结输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-calibration-input.json)，SHA-256 `7a540d762c971e7ade8eeb739a85a7f226a4af1d42dc30a6b0c9edfc53a0aeea`；[程序](../../system/scripts/day16_z13_calibration_audit.py)；[完整11行结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-calibration-audit.json)。actual原件hash仍为本页raw_sha256，未改raw。

同版本控制另核[arXiv:1304.3287v1](https://arxiv.org/pdf/1304.3287v1)，19页，SHA-256 `a757073de7473e2fec971d8b2f2c65b4247354e6907c326dcda6c355e8a97961`；本次只定向Table I（p.18）、Table II（p.19）、Eqs.(4)–(7)/Fig.5，不称此副本全文精读。Z13-12说明Table I所有括号误差相同，因此版本差异未消除该表误差语义缺口；upper435.9的版本差异则保留，未选取较小σ反推显著性。新PDF只在repo tmp，原raw未覆盖。


### 1368-keV文字点、外推曲线与FOM对象

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| Z13-13 | 正文另报1368 keV的Q_EXOGAM=.135(.005)、Q_EUROGAM=.121(.005)、F_EXOGAM=1.51×10^-5及F比4.4；已列pure-E2校准点只到1264 keV。以印刷p0/p1外推同能量给Q=.1600783。该差值尚无matching选样/原拟合及Cov说明，不能当已认证的实验冲突。 | direct-and-Codex-calculation | conditional | 正文044328-5，Eq.(8)–(9)后1368比较句、Fig.5、Table I；arXiv v1 p.10同句 | true |

这里的两项Q是作者在文字中分别给出的比较点，**没有证据证明它们统计独立，或证明1368点与Table I拟合拥有完全相同的selection**。原curve输入p0=.39(.02)、p1=.00006(.00003)/keV、m_ec²=511 keV给Qpoint=.33909146，因而Qcurve=.16007830；与另报.135的中央差.02507830保持，不反向调p0/p1。1368在列明的316–1264-keV校准范围外，不把外推当新calibration。

若括号σ是参数marginals，仅未知ρ_p0,p1就使一阶σ_Qcurve在.00713448–.02069814之间；比较点与曲线的cross-Cov也未给，因此没有报告差异显著性、χ²或新的误差。两个版本都保留同一1368比较句，版本不同未解释这个中央差。

在**假定同一响应对象且F=Q²epsilon_c适用**时，仅由原文字点可代数推得epsilon_EXOGAM≈8.28532×10^-4、epsilon_EUROGAM≈2.34398×10^-4；这不是两项独立效率测量。原F比4.4可分成Q²比1.244792及条件效率比3.534727，说明F改善不能只叫Q提高4.4倍。若擅用外推curve Q替换文字Q，反推epsilon_EXOGAM会变成5.89267×10^-4；这个变化来自输入对象替换，不是新测量或response修正。

重放[冻结1368输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-fom-input.json)及[逐式计算](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-fom-point-audit.json)保留精确代码式/hash和因子化检查；没有F误差或actual coincidence counts/NClo，故不造完整FOM误差或beamtime收益。
