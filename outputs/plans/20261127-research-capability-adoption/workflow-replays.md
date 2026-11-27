# 三类流程回放

日期：2026-11-27。仅回读已有知识页，不构成新实验、原文复核或新计算。可复用方法见 [[evidence-driven-research-cycle]]。

```research-cycle
{
  "schema": "wiki-research-cycle-v1",
  "question": "核结构候选模式的排序能否在响应条件固定后保持？",
  "hypotheses": [
    {
      "id": "H-mode",
      "claim": "wobbling候选须与signature-partner/TiP及组态混合比较",
      "alternative": "取向、门线或响应假设可能产生表观分支偏好",
      "prediction": "冻结响应后，比较未用于选择的观测块是否仍区分候选",
      "falsifier": "只在特定响应假设下出现的排序不能支持无条件模式判断",
      "minimum_check": "先核对一条连接线的身份、门选择和偏振标定可得性",
      "null_value": "缺少输入也能界定readiness及最小数据请求",
      "novelty": {
        "status": "not-checked",
        "limits": "本轮只回放已有知识页；未新增课题查新或核物理文献检索"
      }
    }
  ],
  "cycles": [
    {
      "id": "C-replay-1",
      "hypothesis_id": "H-mode",
      "selection_reason": "核查机制是否能在已有材料中形成有边界的下一步",
      "action": {
        "state": "executed",
        "description": "回读已存在的知识页指定段落，检查工作流的证据与停止边界",
        "artifact": "knowledge/projects/a130-single-point-paper-133ce-response-aware-identifiability.md#Minimum observable bundle; Falsifiers and stop rules"
      },
      "evidence": [
        {
          "source_id": "a130-single-point-paper-133ce-response-aware-identifiability",
          "locator": "Minimum observable bundle; Falsifiers and stop rules",
          "lineage": "project-133ce-current-inputs",
          "kind": "task-inference"
        }
      ],
      "outcome": "limits",
      "verification": {
        "basis": "direct-source",
        "scope": "仅直接回读本地知识记录；不是原始实验或计算复验"
      },
      "independent_lineages_claimed": 0,
      "belief_revision": "现有project保留四类候选及条件性停止；本轮只回读决策合同，未裁决任何模式",
      "next_action": "先核对一条连接线的身份、门选择和偏振标定可得性"
    }
  ]
}
```

```research-cycle
{
  "schema": "wiki-research-cycle-v1",
  "question": "PDM内部恢复可以支持多强的验证表述？",
  "hypotheses": [
    {
      "id": "H-pdm",
      "claim": "同源生成/反演可检验内部自洽",
      "alternative": "独立代数响应可补充数值核验，但仍共享物理假设",
      "prediction": "分别登记同源恢复、独立公式比较、几何/相位与分支边界",
      "falsifier": "由同源恢复直接推出实验有效性的推理不成立",
      "minimum_check": "先对照现有合成验证的输入约定和局限段，不重跑旧计算",
      "null_value": "边界核对即使不改变结果，也能阻止验证表述越级",
      "novelty": {
        "status": "not-checked",
        "limits": "本轮只回放已有知识页；未新增课题查新或核物理文献检索"
      }
    }
  ],
  "cycles": [
    {
      "id": "C-replay-2",
      "hypothesis_id": "H-pdm",
      "selection_reason": "核查机制是否能在已有材料中形成有边界的下一步",
      "action": {
        "state": "executed",
        "description": "回读已存在的知识页指定段落，检查工作流的证据与停止边界",
        "artifact": "knowledge/sources/multipolepdm-20261120-synthetic-validation.md#Summary; Key Results PDM26-3/PDM26-5; Competing Interpretations and Limitations"
      },
      "evidence": [
        {
          "source_id": "multipolepdm-20261120-synthetic-validation",
          "locator": "Summary; Key Results PDM26-3/PDM26-5; Competing Interpretations and Limitations",
          "lineage": "pdm-seed-20261120-shared-noise",
          "kind": "task-inference"
        }
      ],
      "outcome": "limits",
      "verification": {
        "basis": "direct-source",
        "scope": "仅直接回读本地知识记录；不是原始实验或计算复验"
      },
      "independent_lineages_claimed": 0,
      "belief_revision": "现有source已分开同源与独立代数组装，并保留域和分支敏感性；本轮未重算或读回数值原件",
      "next_action": "先对照现有合成验证的输入约定和局限段，不重跑旧计算"
    }
  ]
}
```

```research-cycle
{
  "schema": "wiki-research-cycle-v1",
  "question": "下一项课题应优先补模型数量还是辨识信息？",
  "hypotheses": [
    {
      "id": "H-topic",
      "claim": "优先识别能改变竞争解释排序的伴随观测缺口",
      "alternative": "新增模型也可能有价值，但须先定义与现有路线不同的可检验预测",
      "prediction": "先记录最接近工作和输入边界，再比较一个最小观测条件的决策价值",
      "falsifier": "若所有候选在可得观测中等价，暂不提出模式确认结论",
      "minimum_check": "列最接近工作检索词及可得响应/寿命/分支字段；尚待执行外部查新",
      "null_value": "空结果可限定不可识别区域与最小实验设计",
      "novelty": {
        "status": "not-checked",
        "limits": "本轮只回放已有知识页；未新增课题查新或核物理文献检索"
      }
    }
  ],
  "cycles": [
    {
      "id": "C-replay-3",
      "hypothesis_id": "H-topic",
      "selection_reason": "核查机制是否能在已有材料中形成有边界的下一步",
      "action": {
        "state": "executed",
        "description": "回读已存在的知识页指定段落，检查工作流的证据与停止边界",
        "artifact": "knowledge/projects/a130-single-point-paper-133ce-response-aware-identifiability.md#Research Question; Current Hypotheses; Minimum observable bundle"
      },
      "evidence": [
        {
          "source_id": "a130-single-point-paper-133ce-response-aware-identifiability",
          "locator": "Research Question; Current Hypotheses; Minimum observable bundle",
          "lineage": "project-133ce-current-inputs",
          "kind": "task-inference"
        }
      ],
      "outcome": "limits",
      "verification": {
        "basis": "direct-source",
        "scope": "仅直接回读本地知识记录；不是原始实验或计算复验"
      },
      "independent_lineages_claimed": 0,
      "belief_revision": "作为选题方法回放；未进行本课题新颖性检索，不使用首创措辞",
      "next_action": "列最接近工作检索词及可得响应/寿命/分支字段；尚待执行外部查新"
    }
  ]
}
```
