---
type: method
title: "核结构研究的证据驱动循环与科研脑暴"
aliases: [科研研究卡, evidence-driven research cycle, research brainstorming, hypothesis tree, LOOP]
method_type: research-process
created: 2026-11-27
updated: 2026-11-27
status: active
review_status: unreviewed
tags: [research-design, evidence, falsification, reproducibility, brainstorming]
sources: [book-hamilton-electromagnetic-interaction, multipolepdm-20261120-synthetic-validation]
---

# 核结构研究的证据驱动循环与科研脑暴

## Purpose

将研究建议转成有来源、可证伪、可续接的下一步。本文是本地研究方法设计，科学适用边界仍回到直接来源；规范生效不表示已实测达到博士研究员水平。
L0–L4、问题状态和授权由 `system/workflows/autonomous-research.md` 维护，不在本文建立第二套状态。

## Inputs and Assumptions

先固定当前问题、已有认识、输入身份、最强替代解释、资源和停止条件。已有 project/research-note 能保存状态时直接更新，避免另建任务数据库。
普通问答不启动写入；已授权选题/研究按任务继续，不因采用脑暴或循环方法重复索要普通调查授权。

入选研究卡按 `system/templates/research-card.md` 填写：稳定 ID、机制与前提、来源依赖、区分性预测、反驳条件、最小行动、查新范围、空结果价值、失败约束与下一步。

## Procedure

1. **恢复**：回到原件、现有证据矩阵、旧失败及未完成动作。工具退出成功、任务复述、完成标记均不能代替实际研究证据。
2. **发散**：从不同机制、测量/分析效应、模型边界和迁移条件提出候选。按问题选前提反转或从目标展开替代路径；允许反转失败，不按创意数验收。
3. **核验与收敛**：查最接近工作、反例和来源依赖；记录查询、日期、范围与未查部分。按预先说明的信息增益、可检验性、数据可得性、成本及负结果价值选下一步。
4. **执行**：一轮绑定一个可检验判断。保存选择理由、实际动作、输入版本、证据定位和核验范围；必要时多次技术重试，但不能悄悄改变所检假设来追分。
5. **修正**：区分支持、限制、反驳、无实质变化和未执行；说明结果怎样改变假设排序或下一步。拒绝路线保留原因、上层约束与复活条件。
6. **收束或续接**：达到决策目标、下一步不能改变判断、材料/权限/资源不足时有理由停止；保存证据、缺口和下一项具体动作。没有知识变化可以是 verified no-op。

只有多条持续实验路线需要比较时使用假设树。子假设有父 ID，失败结果提炼为上层条件；同源错误不能因分支数增加而变成独立支持。

## Scientific Verification Boundary

- 同次实验的论文、学位论文和综述必须保留共同谱系；不同模型或审查角色不增加实验独立性。
- “未看到信号”用于反驳时，先检查统计、效率、背景、gate、阈值、binning 和分辨率。有限灵敏度的空结果应限制结论。
- 固定输入、单位、相位、几何、代码和评测规则；修改评测器后重新建立基线。反复用于选择的数据已参与开发，不能继续称为未见确认材料。
- 开发与确认按真实问题划分。可用独立数据集/核素、独立公式或独立实现确认，但独立实现仍可能共享物理假设；必须写明独立性依据。数据稀少无法留出时声明实际边界。
- [[multipolepdm-20261120-synthetic-validation]] 的独立公式与注入恢复范围应分开阅读；同源恢复不能单独提升为实验验证。[[book-hamilton-electromagnetic-interaction]] 是响应、取向和角关联约定的原始依据入口，具体数值主张仍须回到相应 locator。
- 审查者直接读原件/代码/数据并核对旧疑点；只有 self-audit 时如实记录。分数、投票、不同模型一致意见只能作为过程信息。

## Nuclear-Structure Transfer Examples

下表是从既有知识记录提取的可复用决策方法，未运行新实验/计算，未裁决具体模式，也未新增课题查新：

| 问题 | 竞争路线与最小行动 | 可复用的停止边界 |
| --- | --- | --- |
| 候选集体模式 | 参照 [[a130-single-point-paper-133ce-response-aware-identifiability]] 保留 wobbling、signature-partner/TiP 与组态/软核解释；先核对同一连接线的门、响应与独立分支信息 | 响应/身份不能闭合时停在条件性可识别性，不增加无条件模式结论 |
| PDM分支与几何 | 参照 [[multipolepdm-20261120-synthetic-validation]] 分开同源恢复、独立代数响应、积分域和几何/相位条件 | 旧计算的内部恢复不能作为新实验验证；扩展前固定输入和评测基线 |
| 新课题形成 | 从目标观测倒推区分性信息，同时比较新增模型路线；记录最接近工作及查新未覆盖部分 | 可得观测无法区分时固化不可识别区域与最小数据需求，不写首创或确认 |

恢复应保留稳定假设/动作 ID、已完成动作及其实际证据，下一步单列为计划；仅重读检查点不增加已完成实验数。流程回放回执位于任务验收目录，具体物理结论仍回到对应来源。

## Optional Machine-Checked Record

可在原 canonical 知识页嵌入 `research-cycle` JSON 块；状态仍沿现有工作流。只在持续研究需要结构化检查时使用，不要求每次问答产生记录。
下面是**计划动作格式示例**，未执行、没有科学结果，也没有新颖性认定：

```research-cycle
{
  "schema": "wiki-research-cycle-v1",
  "question": "下一项原文核查能否区分物理机制与响应约定的影响？",
  "hypotheses": [{
    "id": "H-response",
    "claim": "候选差异可能依赖响应约定，需回原文检验",
    "alternative": "不同结构机制也可能产生相似观测",
    "prediction": "共同约定下比较必要伴随观测后，部分解释可能被限制",
    "falsifier": "约定核对一致且差异仍由独立证据支持",
    "minimum_check": "先核对一项决定性响应定义及适用条件",
    "null_value": "若定义一致，记录该路线没有解释增量",
    "novelty": {"status": "not-checked", "limits": "这是核查方向，未进行新颖性检索"}
  }],
  "cycles": [{
    "id": "C-plan",
    "hypothesis_id": "H-response",
    "selection_reason": "定义核对成本较低，可能改变后续数据比较方式",
    "action": {"state": "planned", "description": "回到直接来源核对响应定义"},
    "evidence": [],
    "outcome": "not-executed",
    "verification": {"basis": "not-performed", "scope": "仅为计划动作格式示例"},
    "belief_revision": "尚无执行结果，不改变物理判断",
    "next_action": "取得相应原页后执行核对"
  }]
}
```

检查命令：

```bash
python3 system/scripts/wiki_research_cycle.py --root . knowledge/methods/evidence-driven-research-cycle.md
```

执行记录增加 `action.artifact` 与 `evidence`：每条含 `source_id`、`locator`、`lineage`、`kind`。
`kind` 使用 `direct-report`、`author-interpretation`、`model-result` 或 `task-inference`。
`independent_lineages_claimed` 不能超过已声明的直接报告谱系数；谱系身份本身须人工阅读来源核验，由 Agent 完成，不等待用户审核。
`outcome` 为 `supports`、`limits`、`refutes`、`no-material-change` 或 `not-executed`；反驳记录包含 `failure_constraint`。
被拒候选包含 `disposition: rejected`、`rejection_reason`、`revival_condition`。

数值验证可增加 `validation`：`input_sha256`、`evaluator_sha256`、`baseline_evaluator_sha256`、`development_ids`、`confirmation_ids`、`confirmation_used_for_selection` 与 `scope`。
`scope` 为 `exploratory`、`internal-recovery` 或 `independent-check`；最后一项还须 `independence_basis` 和相容的核验依据。
相同确认集参与选择后，降为探索/内部验证范围或另取真正独立的确认材料，保留原记录。

这是结构与自洽检查：不会执行 action、读取 raw、验证填入哈希对应的实际字节、判定物理真假或保证科研水平。
输入真实存在、哈希、原件定位与模型条件仍由归档门、分析程序和直接证据核验完成。`review_status` 不参与本检查。

## Verification and Reuse

相关对抗测试：`system/tests/test_research_cycle.py`。三类材料的工作流演练与执行边界记于 `outputs/plans/20261127-research-capability-adoption/acceptance.md`，它是回执，不能代替本文或源证据。
采用机制的固定外部来源、许可、文件哈希与拒绝部分见 `system/agent-capability-adoption.md` 及其 provenance 清单。外部 Agent 方法不作为核结构事实来源。

## What It Can Establish

明确一轮研究的决策依据、执行证据、失败约束与恢复点；结构化记录能暴露若干自相矛盾的验证声明。

## What It Cannot Establish Alone

方法、格式检查和流程回放不能证明原始证据真实、物理模型正确、课题首创，或 Agent 已达到某种科研能力等级。

## Sources

- [[book-hamilton-electromagnetic-interaction]]：响应、取向与角关联定义的来源入口。
- [[multipolepdm-20261120-synthetic-validation]]：内部恢复、独立代数比较及数值域边界。
- [[a130-single-point-paper-133ce-response-aware-identifiability]]：竞争模式、共同响应和最小可识别性检查的既有研究合同。
- 外部工作流的固定来源与许可属于治理 provenance，见 `system/agent-capability-sources/research-cycle-20261127.json`，不作核物理证据。
