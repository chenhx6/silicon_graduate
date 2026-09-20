---
type: source
title: "Microscopic investigation of γ vibrational band structures in odd-mass nuclei"
aliases: ["Jahangir 2026 TPSM γ bands", "Nb Tc gamma-vibrational TPSM 2026"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Microscopic investigation of γ vibrational band structures in odd-mass nuclei"
authors: ["Uzma Jahangir", "S. P. Rouoof", "S. Jehangir", "G. H. Bhat", "J. A. Sheikh", "N. A. Rather"]
journal: "arXiv preprint"
year: 2026
arxiv: "2603.07157v1"
doi: "10.48550/arXiv.2603.07157"
language: en
canonical_source: "Jahangir, U. et al. Microscopic investigation of γ vibrational band structures in odd-mass nuclei. arXiv:2603.07157v1 (2026)."
library_file: "raw/papers/gpt/high-spin-20260920/振动/2026_Jahangir et al_Microscopic investigation of γ vibrational band structures in odd-mass nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/振动/2026_Jahangir et al_Microscopic investigation of γ vibrational band structures in odd-mass nuclei.pdf"
raw_sha256: "04187f6dd9a77fcdf87b545506c17f021159a4426c6ce358277e4aeb912c49a4"
nuclei: ["103Nb", "105Nb", "107Nb", "109Nb", "103Tc", "105Tc", "107Tc", "109Tc"]
models: ["triaxial-projected-shell-model", "triaxial-Nilsson-model", "BCS-pairing"]
observables: ["band-energies", "alignment", "B(E2)", "gamma-vibrational-band-structure"]
methods: ["angular-momentum-projection", "Hill-Wheeler-diagonalization", "configuration-mixing"]
tags: [gamma-vibration, odd-mass-nuclei, Nb-isotopes, Tc-isotopes, TPSM, triaxiality, second-gamma-band]
---

# Microscopic investigation of γ vibrational band structures in odd-mass nuclei

## Bibliographic Record

- 作者：Uzma Jahangir, S. P. Rouoof, S. Jehangir, G. H. Bhat, J. A. Sheikh, N. A. Rather。
- 版本：arXiv:2603.07157v1，2026-03-07 提交；11 页、9 幅图。
- DOI：`10.48550/arXiv.2603.07157`（arXiv-issued DOI）。
- 原始文件：`raw/papers/gpt/high-spin-20260920/振动/2026_Jahangir et al_Microscopic investigation of γ vibrational band structures in odd-mass nuclei.pdf`；SHA-256：`04187f6dd9a77fcdf87b545506c17f021159a4426c6ce358277e4aeb912c49a4`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.1-11 全文；摘要、引言、TPSM 基底与投影方程 (1)-(10)、Table I 形变输入、Figs.1-9 的能带/对齐/B(E2) 结果、Table II、总结和全部参考文献均已阅读。关键图 2、4-9 视觉核对。
- Not covered: 参考文献所指原始 `103,105Nb` 能级实验全文、作者未提供的事件级数据和模型代码；这些不能由本理论预印本替代。
- Coverage caveats: 结论主要来自 TPSM 计算与既有实验能级比较；`γ2` 对 `103,105Nb` 第四条观测带的指认是模型支持的解释，不能写成新的直接实验发现。

## Paper Question and Scientific Motivation

- 论文研究 `103,105,107,109Nb` 和 `103,105,107,109Tc` 的奇质量高自旋能带，重点解释 `103,105Nb` 中已观测、但不能由跃迁强度比归为 `3γ` 的第四条带（摘要；PDF pp.1, 6, 8-10）。
- 奇质量核的父组态具有半整数 `K0`，三轴投影允许 `K=K0±2`，因此 `K0+2` 与 `K0−2` 可形成两个不同的 γ 带；作者以此提出第四条带是第二 γ 带 `γ2`，而非 `3γ`（PDF pp.1, 6, 10）。

## Method and Design Logic

- TPSM 以三轴 Nilsson Hamiltonian 为平均场、BCS 处理配对，并用三维角动量投影将多准粒子组态投影到良好 `I`；odd-proton 基底包括一质子、一质子加两中子、三质子和三质子加两中子组态（PDF pp.2-4，式 (1)-(3)）。
- 投影基底中以 `K` 量子数区分同一三轴内禀组态的 yrast、γ、2γ、γ2 和 3γ 结构；随后在含四极-四极相互作用、单极/四极配对的 Hamiltonian 中用 Hill-Wheeler 广义本征方程混合（PDF pp.3-4，式 (4)-(10)）。
- 计算采用 Table I 的轴向/三轴形变输入，`γ` 约为 `20°-28°`（Nb）和 `24°-27°`（Tc）；对比能量、对齐和跨带 `B(E2)`，而不是只用单一能级相似性判定带性质（PDF p.5，Table I；pp.5-9）。

## Key Evidence and Reasoning Chain

1. 观测的 `103,105Nb` 前三条带已标为 yrast、γ1、2γ，第四条带的实验跃迁强度比排除了简单 `3γ` 解释（摘要；PDF pp.1, 6）。
2. 对 `105Nb` 的 TPSM band diagram 显示从同一 `K0=5/2` 一质子内禀态投影出的 `K=9/2`、`13/2`、`1/2` 和 `17/2` 结构；`K=1/2=K0−2` 是第二 γ 带，`K=17/2=K0+6` 对应 3γ（PDF pp.2, 5-6）。
3. Fig.2 中，TPSM 的 `K=1/2` 第三激发带与 `103,105Nb` 第四条观测带能量相符，而预测的 3γ 带位于更高激发能；作者因此把第四条带归为 γ2（PDF pp.2, 6, 8）。
4. 对八个 Nb/Tc 核素，TPSM 重现 yrast 和已观测 γ 带的主要能量系统学；`103,105Nb` 的 γ2 为第三激发带，`107,109Tc` 的 γ 带实验数据较少，相关结论主要是预测（PDF pp.5, 8, 10）。
5. 对齐曲线和波函数显示低自旋区各带主要来自同一三轴内禀组态；高自旋偏差来自其它准粒子组态混合，Tc 的混合偏差比 Nb 更明显（PDF pp.6, 8-9，Figs.6-8）。
6. 以 `e_n=0.5e`、`e_p=1.5e` 计算的跨带 `B(E2)` 呈现 γ1→yrast、2γ→γ1、γ2→2γ 的相似系统学，但随自旋下降并受组态混合影响（PDF pp.8-9，Fig.9、Table II）。

## Summary

作者用 TPSM 系统研究八个奇质量 Nb/Tc 核素的 γ 结构，重点提出 `103,105Nb` 第四条观测带不是 `3γ`，而是由半整数父 `K0` 的 `K0−2` 投影产生的第二 γ 带 `γ2`。模型能量、对齐和 `B(E2)` 结果支持四条带来自同一三轴内禀组态的解释。对 `107,109Tc`，高自旋实验信息有限，论文主要给出预测；未来实验需要补充 γ 带和 γ2 的高自旋状态及电磁跃迁来检验模型。

## Experimental or Theoretical Setup

- 输入核素：`103,105,107,109Nb`、`103,105,107,109Tc`。
- 模型：三轴 Nilsson 平均场、BCS 配对、三维角动量投影、Hill-Wheeler 对角化；四极-四极、单极配对和四极配对相互作用。
- 参数：Table I 给出八个核素的 `ε`、`ε'`、`γ`；`B(E2)` 使用 `e_n=0.5e`、`e_p=1.5e`。
- 实验输入：既有能级和已观测能带；本文没有重新分析原始 γγ 事件或新实验谱。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| J26-1 | TPSM 对八个 Nb/Tc 核素计算 yrast、γ1、2γ、γ2 和 3γ 候选结构。 | model-result | direct | PDF pp.2-5，Figs.1,4,5 | false |
| J26-2 | `103,105Nb` 第四条观测带的能量更符合计算的 `K=K0−2` γ2 带，而不是更高能的 3γ 带。 | model-result/author-interpretation | direct | PDF pp.2,6,8；Fig.2 | true |
| J26-3 | `103,105Nb` 的 γ2 是同一三轴内禀组态的第三激发带；`107,109Tc` 的 γ2 主要是预测。 | model-result | direct | PDF pp.5,8,10；Figs.4-5 | true |
| J26-4 | 低自旋区四条带的波函数、对齐和 B(E2) 具有相似性；高自旋偏差来自准粒子组态混合，Tc 偏差更明显。 | model-result | direct | PDF pp.6,8-9；Figs.6-9 | false |
| J26-5 | 作者没有把第四条带作为新的直接实验发现，而是依据既有能量和跃迁强度约束提出 TPSM 解释，并要求未来高自旋实验验证。 | author-interpretation | direct | PDF pp.1,8-10 | false |

## Nuclear Structure Information

- 八个研究核素均为奇质量 Nb/Tc；论文重点是奇质量三轴组态的多重 γ 带结构，不建立确定的实验能带页。
- 对 `103,105Nb`，已有 yrast、γ1、2γ 和第四带实验结构；γ2/3γ 的最终性质依赖原始实验能级与跨带跃迁数据。
- `K0−2` 与 `K0+2` 在奇质量半整数父组态中不同，这一几何/投影事实是论文提出双 γ 结构的理论基础。

## Authors' Interpretation

- 作者把 `103,105Nb` 第四带解释为 γ2，理由是能量接近 `K=1/2` 投影带、3γ 预测更高，并且该带的低自旋状态尚未在实验中布居。
- 作者认为四条带主要属于同一三轴内禀组态，但承认高自旋会出现其它准粒子组态混合。

## Model Results

- TPSM 重现主要 yrast/γ 能量趋势，并给出 Nb/Tc γ2 和 3γ 的预测。
- Table I 的形变是模型输入，不是本文新测得的形变观测；`γ≈20°-28°` 不能单独作为实验三轴性证据。
- `B(E2)` 和 alignment 是模型输出；与实验部分能级/对齐的相似性支持模型解释，但不能作为独立实验数据。

## Competing Interpretations and Limitations

- 第四带也可能受未纳入或未充分约束的准粒子组态混合影响；本文用 TPSM 给出 γ2 解释，但没有新的事件级谱学或完整电磁跃迁数据。
- `3γ` 被排除的前提来自既有实验 transition-intensity ratios；应回到引用的原始 `103,105Nb` 实验来源核对，而不能只引用本预印本。
- `107,109Tc` 的 γ 数据有限，论文结论更偏向可检验预测；未来实验需要布居 γ2 的低/高自旋状态并测量 inter-band E2。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-J26-1 | Core reconstruction | 论文的核心增量是把奇质量的 `K0−2` 投影结构显式识别为第二 γ 带，并用 TPSM 能量/对齐/B(E2) 支持，而不是新增实验观测。 | PDF pp.1,6,8-10 | self-checking |
| AR-J26-2 | Assumptions and dependencies | 依赖 Table I 形变输入、既有实验带标签、TPSM 截断基底、effective charges 和引用实验的 `3γ` 排除。 | PDF pp.2-5,8-9 | self-checking |
| AR-J26-3 | Transfer conditions | `K0−2` 的奇质量 γ2 机制可迁移到其它半整数父组态，但能量排序、带混合和可见性必须逐核素计算/测量。 | PDF pp.1,6 | provisional |
| AR-J26-4 | Failure conditions | 若新实验发现第四带的 E2 branching、alignment 或高自旋能级不符合 `K0−2`，或其它组态混合能同样再现谱，γ2 指认需降级。 | PDF pp.6,8-10 | active-L3 |
| AR-J26-5 | Reverse/falsification test | 测量第四带到 2γ/γ1/yrast 的 E2 branching、低自旋未布居成员、alignment 和更高自旋延伸，并比较 `K0−2`、3γ 与组态混合计算。 | PDF pp.8-10 | candidate-L3 |
| AR-J26-6 | Research-question decision | 可作为奇质量 γ-vibration 多重带和实验设计的 L3 理论候选；当前没有本地公开原始数据可启动 L4。 | PDF pp.1,8-10 | candidate-L3 |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 TPSM 模型页及 `104,106Mo`、`135Pr` 等案例，但未记录奇质量半整数 `K0−2` γ2 结构的完整 Nb/Tc 预测。
- Effect of this source: `supports` and `revises`。
- Reason: 来源支持 TPSM 作为 γ 带/组态混合模型的用途，并把“第三/第四带简单按声子数命名”修正为必须检查半整数 `K` 投影和电磁/对齐证据。
- Persistence decision: update [[triaxial-projected-shell-model]] with a source relation; keep the γ2 conclusion in this source and a future L3 evidence map, not a universal concept claim。
- Review state: `unreviewed`; model claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[triaxial-projected-shell-model]] | 提供 8 个奇质量 Nb/Tc 核素的 TPSM γ1/2γ/γ2/3γ 能量、对齐和 B(E2) 应用案例。 |
| methodological-bridge | [[rotational-bands]] | 说明奇质量半整数 `K0` 下 `K0−2` 与 `K0+2` 可产生不同 γ-vibrational bands；当前只保留来源级结构。 |
| competing-interpretation | `103,105Nb` fourth-band assignment | γ2、3γ 与其它组态混合需要原始跃迁强度和后续实验区分。 |

## Human Review Triage

### P0

- J26-P0-1：`103,105Nb` 第四带为 γ2 而非 3γ 的结论是模型解释，必须和引用的原始 transition-intensity、能级及未来 E2 数据分开；不能升级为直接实验事实。

### P1

- J26-P1-1：Table I 形变、effective charges、TPSM 截断和准粒子混合可能改变 γ2/3γ 能量排序；跨核素迁移前需复算或回到模型输入。

### P2/P3

- arXiv v1 的元数据和版本已记录；后续若出现正式发表版，应做版本差异复核，不静默替换 v1 证据。

## Extracted Pages

- Nuclei: 暂不创建八个独立核素页；保留来源级核素列表。
- Bands: 暂不创建独立 γ2 band page；待原始实验和跨来源 evidence map。
- Concepts: 关联 γ-vibrational band、TPSM、triaxial configuration mixing。
- Models: 更新 [[triaxial-projected-shell-model]]。

## Non-source Notes and Follow-up

- 下一步：将 J26 的模型边界和奇质量 `K0−2` γ2 机制加入 TPSM model page；后续处理 HS-004 等直接实验/谱学来源时回填 cross-source evidence。
- L3 候选：为 `103,105Nb` 第四带建立 γ2/3γ/组态混合证据矩阵，优先找原始能级和 transition-intensity 数据。
