---
type: research-note
title: "131Xe INGA 实验谱系与 L3/L4 准备度定向审计"
aliases: [131Xe Day30 source lineage audit, 131Xe single-acquisition reconciliation]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day30 directed source lineage and prospectus prompt"
evidence_sources: [banik-2020-131xe-multiple-band-structures, chakraborty-2023-131xe-wobbling-origin, jehangir-2022-odd-neutron-tpsm-extension, irving-1979-131xe-spectroscopy-scope, lonnroth-1983-xe-quasiparticle-states, vecc-131xe-alpha-38mev]
tags: [131xe, source-lineage, inga, vecc, parity, mixing-ratio, readiness-boundary]
---

# 131Xe INGA 实验谱系与 L3/L4 准备度定向审计

## Research Trigger & Purpose

在 Day29 完成 `131Xe` 794-keV 宇称与 882-keV 双根的研究设计答辩后，Day30 对 `131Xe` 的文献谱系开展定向复核。核心目标是明确 `lineage_id`、`lineage_role`、`dependent-reanalysis` 属性、期刊与 arXiv 版本对应关系、本地原始材料哈希对账以及严格界定 L3/L4 准备度边界。**坚决杜绝把同一 INGA 数据采集的 2020、2022 与 2023 年文献误计为独立实验，杜绝无原始数据情况下臆造事件级计数值、探测器响应矩阵或联合协方差**。

## Single-Acquisition Lineage Map: `vecc-131xe-inga-38mev-130te-a3n`

本谱系由加尔各答变能量回旋加速器中心（VECC）K-130 回旋加速器上开展的单一实验采集构成：
- **束流与能量：** $^{4}\text{He}$（$\alpha$ 束流），$38\text{ MeV}$；
- **靶材与厚度：** $2\text{ mg/cm}^2$ 富集 $^{130}\text{Te}$ 靶，衬底为 $600\ \mu\text{g/cm}^2$ Mylar；
- **反应与通道：** $^{130}\text{Te}(\alpha,3n\gamma)^{131}\text{Xe}$；
- **探测器阵列：** 印度国家伽马阵列（INGA），由 7 个 Compton-suppressed clover HPGe 探测器组成，分布于束流方向的 $40^\circ$（2个）、$90^\circ$（2个）与 $125^\circ$（3个）；
- **电子学与获取：** Pixie-16 $250\text{ MHz}$、12-bit 数字采集系统（DAQ）。

三篇文献对该物理采集的依存关系如下：

| 文献标识 | 角色 (`lineage_role`) | 独立性属性 (`independence`) | 核心贡献与数据处理边界 | 独立实验计数 |
|---|---|---|---|---|
| [[banik-2020-131xe-multiple-band-structures]] (PRC 101, 044306) | `primary-analysis` | `independent-acquisition` | 首次全面建立 $38\text{ MeV}$ 反应的能级纲图（报道 72 条新跃迁），提取相对强度、DCO 比与偏振不对称度；构建 Bands 1–7 骨架。 | 1 |
| [[jehangir-2022-odd-neutron-tpsm-extension]] (PRC 105, 054310) | `dependent-theory-comparison` | `dependent-dataset` | 理论论文：奇中子 TPSM 扩展五准粒子基底。其实测 $^{131}\text{Xe}$ 能级直接引自 Banik 2020（Ref. [53]），不包含独立实验观测。 | 0 (共享 Banik 2020) |
| [[chakraborty-2023-131xe-wobbling-origin]] (PRC 107, 064318) | `dependent-reanalysis` | `dependent-reanalysis` | 实验重分析：重做相同 INGA 原始符合数据的时间门与非对称矩阵，重点分离 882-keV 双线，提取新门（如 766-keV 门），将负宇称侧带重指认为 signature partner。 | 0 (共享 Banik 2020) |

**谱系审计结论：** 全库中关于 $^{131}\text{Xe}$ 高自旋 INGA 数据的独立实验测量仅有 1 次（`independent_experiment_count: 1`）。任何综合模型拟合或似然分析，都不得把 Banik 2020、Jehangir 2022 与 Chakraborty 2023 的数据当成互相独立的观测。

## Journal vs. arXiv Version Integrity & Raw SHA-256 Reconciliation

本库对三篇文献的期刊原件与开放获取（arXiv）版本进行了逐一核查与哈希校验：

1. **Banik et al. 2020**:
   - 期刊源：*Phys. Rev. C* 101, 044306 (2020), DOI: `10.1103/PhysRevC.101.044306`.
   - 本地归档文件：`raw/papers/gpt/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection/banik-2020-131xe-reaction/PDFs/Banik_et_al_2020_131Xe_multiple_band_structures.pdf`
   - SHA-256：`21e7e1eed7a93ffc3c38f4580fcf93863d02c56e40ffc900b1634df14c7f34e6`（校验匹配）。

2. **Chakraborty et al. 2023**:
   - 期刊源：*Phys. Rev. C* 107, 064318 (2023), DOI: `10.1103/PhysRevC.107.064318`.
   - 本地期刊归档：`raw/papers/2023_Chakraborty et al_Search for the origin of wobbling motion in the A ≈ 130 region The case of Xe 131.pdf`
   - 期刊 SHA-256：`730DB39EB9A5AECD3BBCE1DCE3CB9C32829EB2F4A2062EE31C59DDC4D52BD9FF`（校验匹配）。
   - arXiv 版本：`arXiv:2311.09713v1`，归档于 `raw/papers/2023_Chakraborty et al_Search for the origin of wobbling motion in the A ≈ 130 region.pdf`
   - arXiv SHA-256：`9a871d56cd2752eed9e09f1f8fc60686cae3c23fe63efc2255846f2e38ac72a1`（校验匹配）。
   - 版本比对结论：arXiv v1 与 PRC 正文在能级、跃迁能量、Table I 数值及 Fig. 4–5 混合比结果上完全一致，无未公开修正。

3. **Jehangir et al. 2022**:
   - 期刊源：*Phys. Rev. C* 105, 054310 (2022), DOI: `10.1103/PhysRevC.105.054310`.
   - arXiv 版本：`arXiv:2203.12851v1`，归档于 `raw/papers/gpt/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection/2203-12851-tpsm-odd-neutron-xe-20260930/PDFs/Extended_triaxial_projected_shell_model_approach_for_odd-neutron_nuclei.pdf`
   - SHA-256：`2c2d428aa5d82b8951d8f927bc11ccd9d30ed791fd55d488ea9cfcfb6372dea5`（校验匹配）。

4. **历史独立实验原件访问边界（Irving 1979 / Lönnroth 1983）**:
   - Irving 1979 (*J. Phys. G* 5, 1595, DOI: `10.1088/0305-4616/5/11/015`): 元数据已归档，哈希 `7c3bfb5417828b809ae6ea027efd12f75120ef0320db2e13d751db584f879158`，当前处于 `metadata-only` 访问边界，尚未获得逐线 AD/偏振原始表格。
   - Lönnroth 1983 (*Phys. Scr.* 27, 228, DOI: `10.1088/0031-8949/27/4/002`): 元数据已归档，哈希 `0b3e378f1563b9b06c92a6b008701bca9092e0a37262ff91a742d3a96293efae`，转换电子谱线数据未逐行暴露。

## 794.8-keV Parity Version Boundary & Missing ICE Data

794.8-keV 跃迁连接 1600.9-keV 态与 806.1-keV $15/2^-$ 态：
- **Banik 2020 指认：** 将 1600.9-keV 态标为 $17/2^+$，将 794.8-keV 跃迁指认为 $E1$ 多极性（Table I, `044306-6`），依据为 $R_{DCO}=0.55(1)$（四极门下纯偶极跃迁）与 $\Delta_{PDCO}=+0.03(1)$。
- **Chakraborty 2023 指认：** 将 1600.9-keV 态重标为 $17/2^-$（Table I, `064318-3`），未给出 $E1$ 标签，通过 766.5-keV 跃迁将该态连接至 834.6-keV $13/2^-$ 态。
- **证据缺陷核验：**
  1. VECC INGA 实验仅测量 $\gamma$ 射线，未配置内转换电子（ICE）探测器，缺失内转换系数 $\alpha_K$ 的直接测量。
  2. $\Delta_{PDCO}=+0.03(1)$ 数值接近零，且存在束流不对称度系统误差，其 $3\sigma$ 区间不能有效区隔 $E1$ 与 $M1$。
  3. 1600.9-keV 节点的宇称归属属于未决的版本冲突（version boundary），在获得内转换电子数据前不能硬性闭合。

## 881.8-keV Dual-Root Mixing Ratio & Missing Polarization Response

881.8-keV 跃迁连接 1927.6-keV $17/2^-$ yrare 态与 1045.8-keV $13/2^-$ 态：
- **DCO 与多极混合比：** Chakraborty 2023 Table I 给出 $R_{DCO}=0.64(11)$（四极门）。理论方程 $R_{DCO}(\delta)$ 为关于混合比 $\delta(E2/M1)$ 的双值抛物线型函数。
- **双解并存：**
  - 解 A（小正解）：$\delta = +0.09(8)$，对应 $M1$ 主导跃迁（$B(E2)$ 成分极低），作者以此支持 signature-partner 解释；
  - 解 B（大绝对值/负解）：$\delta$ 位于高 $E2$ 区域，对应较高的 $B(E2)$ 强度。
- **数据缺失：**
  1. Chakraborty 2023 Table I 中 881.8-keV 跃迁的线偏振不对称度栏为空白；
  2. 881.8-keV 跃迁与已知的 880.1-keV 杂质/邻近跃迁构成双线重叠，在公开的标量能谱中无法完成独立的门退卷积。
  3. 缺乏联合角分布与偏振响应矩阵，不能排他性剔除解 B。

## Prohibition of Event-Level Count / Response / Covariance Synthesis

根据 Wiki 核心证据规则与路径契约：
1. **严禁凭空伪造事件：** 不得利用蒙特卡洛抽样生成虚假的事件级符合计数（event-level listmode data）来充当实验观测；
2. **严禁构造虚构响应：** 不得使用未经实验标定的纯理论响应函数冒充真实 INGA 探测器阵列响应矩阵；
3. **严禁伪造统计协方差：** 在缺乏原始逐通道计数值与符合时间窗刻度时，不得虚构实验误差协方差矩阵。所有分析必须停留在已发表标量数据及误差传递边界。

## L3/L4 Readiness Boundary and Stop Conditions

- **当前状态：** $^{131}\text{Xe}$ 低自旋结构分析严格保持为 **L3 (Research Design & Hypothesis Discrimination)** 阶段。
- **进入 L4 的硬性前提（Gate for L4 Activation）：**
  1. 获得真实的 VECC INGA 原始数据（ROOT 树、符合矩阵或逐角符合谱）；或
  2. 获得 Irving 1979 / Lönnroth 1983 的原始逐线内转换电子与角分布数据表；或
  3. 获得用户授权的其他独立实验数据集。
- **停止规则：** 在上述输入未闭合之前，停止推进数值求解，不得宣称已“证实”或“排他性证伪” $^{131}\text{Xe}$ 的 low-spin wobbling 模式。

## Knowledge Impact and Learning Decision

- `limits`: 确认 Banik 2020、Jehangir 2022 与 Chakraborty 2023 属于同一个 VECC INGA 采集谱系（`independent_experiment_count: 1`），排除了多实验独立确认的表述；
- `limits`: 确认 794.8-keV 宇称与 881.8-keV 混合比双根为现有公开数据无法决断的物理边界；
- `supports`: 建立了严格可追溯的文献谱系地图与版本哈希账本。


## Research Trigger

源于在束谱学实验数据拟合中对多极混合比、能带结构与集体激发模式的判决需求。

## Grounded Evidence

基于已归档的同行评议文献能级纲图、角分布系数与直接寿命测量数据。

## Provisional Reasoning

综合微观推转模型与唯象转子动力学进行参数反演与理论对账。

## Assumptions

假定核芯转动满足三轴水动力学惯量层级，准粒子在形变场中绝热解耦。

## Competing Explanations

能带能量靠拢与跃迁增强亦可由准粒子旋称伙伴跃迁、形状共存或伽马振动声子耦合所诱发。

## Transfer Conditions

跨质量区迁移需重新标定单粒子费米面深度、配对能隙与核芯刚性。

## Failure Conditions

若缺乏高精度康普顿线偏振排他测量或绝对寿命反演，单一混合比拟合结论失效。

## Falsification or Reverse Tests

通过两体绝对电磁矩阵元与 KSH 选择定则进行严格无公度可证伪性检验。

## Open Questions

高自旋带交叉后是否发生非绝热退耦以及偶偶核芯三轴柔软度演化规律。

## Human Review

待同行物理学家结合最新束流机时数据进行终审裁决。

## Promotion or Rejection History

2026-11-04: 完成微观证据链形式化与章节审计，维持 provisional 状态。
