---
type: system-schema
graph-excluded: true
version: 0.2.0
updated: 2026-07-15
---

# 页面类型与字段规范

## 允许的核心类型

| type | 目录 | 用途 |
|---|---|---|
| source | `knowledge/sources/` | 一份原始来源的可追溯笔记 |
| nucleus | `knowledge/nuclei/` | 单个核素的汇总页 |
| band | `knowledge/bands/` | 一条能带或双重带的证据页 |
| concept | `knowledge/concepts/` | 物理现象、形变与解释框架 |
| experiment | `knowledge/experiments/` | 反应、束流、靶、装置和数据集 |
| model | `knowledge/models/` | 理论模型、哈密顿量和计算框架 |
| observable | `knowledge/observables/` | 可计算或测量的诊断观测量 |
| method | `knowledge/methods/` | 实验分析、数据处理或计算方法 |
| synthesis | `knowledge/synthesis/` | 多来源综合及反向检验 |
| project | `knowledge/projects/` | 当前研究项目状态 |
| decision | `knowledge/decisions/` | 有依据的研究决策 |
| failure | `knowledge/failures/` | 失败路线、原因与复活条件 |
| research-note | `knowledge/research-notes/` | 受控保存高价值、尚未成熟的暂定研究推理 |
| output | `outputs/` | 可复用报告、草稿或审计结果 |

## 所有正式知识页的公共字段

```yaml
---
type:
title:
aliases: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: ai-draft
review_status: unreviewed
tags: []
---
```

`status` 可取：`ai-draft`、`active`、`deprecated`、`redirect`。

`review_status` 可取：`unreviewed`、`human-reviewed`、`verified`、`needs-human-review`。

其中：

- `unreviewed`：页面尚未经过用户页面级检查；不阻止 Codex 继续进行证据核查、研究或普通发布；
- `human-reviewed`：用户已查看页面并确认无明显页面级问题，但不自动确认页面内全部 claims；
- `verified`：已按任务约定由 Codex 完成更严格核验；不等同于用户审核或论文级准入；
- `needs-human-review`：页面整体存在需要用户判断的问题。

页面级 `review_status` 与 claim-level `needs_review` 独立。页面升级为 `human-reviewed` 时，不得批量改写 claim-level 状态。

Agent 新建的 project、decision 和 failure 页面必须从 `review_status: unreviewed` 开始；只有真实完成的用户审核才能将页面标为 `human-reviewed`。`confidentiality` 只是描述性元数据，不实施访问控制；公开 Git 仓库中的 tracked 内容不会因该字段而变为保密内容。

## Source 阅读完成状态

`reading_depth` 是 source 的实际阅读完成状态，不是用户摄入模式。允许值为：

- `metadata-only`：只完成元数据整理；
- `skimmed`：完成摘要、结论或选定关键位置的初步阅读；
- `read`：完成正文主线阅读；
- `deep-read`：在完整正文主线基础上，核查关键方法、数据、图表/公式及与任务相关的补充证据。

source 还应在正文明确记录 `Covered scope` 与 `Not covered`。局部问题即使核查很深，也不能据此把未完整阅读的全文标记为 `deep-read`。三种用户摄入模式由 `system/workflows/ingest.md` 定义，不得从 `reading_depth` 反推用户模式，也不得建立一一对应关系。

## Research-note 状态与字段

`research-note` 是“暂定研究推理”的受控中间层，不是 source 或正式 synthesis。三个状态字段职责不可重叠：

- `status`：页面的一般生命周期；沿用公共枚举。
- `review_status`：页面/推理的用户审核记录；新 note 为 `unreviewed`，Codex self-audit 不写成 `human-reviewed`。
- `reasoning_status`：推理的科学成熟度与处置；允许值仅为 `provisional`、`promoted`、`rejected`、`superseded`、`withdrawn`。

新 note 必须使用 `review_status: unreviewed` 与 `reasoning_status: provisional`。`unreviewed` / `reviewed` 不得写入 `reasoning_status`。`revised` 是 `Promotion or Rejection History` 中的历史事件，不是稳定状态；修订后仍回到相应稳定枚举。

Research note 还必须包含：

- `evidence_sources`：至少一个现有 source 或可核查证据入口；
- `created_from`：产生该推理的授权任务类型，例如 ingest、reflect、project 或 synthesis；
- `promotion_target`：尚未晋升时可留空，晋升后指向正式 project/synthesis/method/concept 等 owning page。

`promoted` 表示推理已经经过相称审核并被正式页面吸收且保留回链；研究任务可先由 Codex self-audit 完成，只有后续问答或论文写作明确需要用户裁决时才记录 Human review。它不把 research note 自身变成 source evidence。`rejected`、`superseded`、`withdrawn` 均保留简短处置原因和触发证据，不静默删除历史。

## 科学主张字段

不要求每条主张单独建文件，但重要结论必须在正文或表格中记录：

- `claim_kind`: `experimental-fact`、`experimental-criterion`、`author-interpretation`、`model-result`、`our-inference`、`synthesis`；
- `evidence_level`: `direct`、`indirect`、`contextual`、`none`；
- `source_independence`: `single`、`multiple-dependent`、`multiple-independent`；
- `confidence`: `low`、`medium`、`high`；
- `locator`: 页码、图号、表号、能级或数据位置。
- `needs_review`: `true` 或 `false`；Codex 可在完成直接来源、locator、claim kind、竞争解释和适用条件的 self-audit 后更新；不得把该更新写成用户审核。论文写作或后续问答中的最终措辞仍按 paper evidence gate 触发用户确认。

source 页还使用 `citation_key` 连接只读 BibTeX 导出。无法通过 DOI、题名或文件名唯一匹配时保持空值，不得猜测；citation key 缺失影响写作链稳定性，不自动表示科学内容错误。

## 时效规则

不使用“超过两年自动过时”的通用规则。

- 已发表的实验数值和经典理论定义：默认低波动，除非出现勘误或新测量冲突。
- 物理解读、候选指认和领域综述：中等波动，出现新证据时复核。
- 项目状态、待办、计算环境和合作信息：高波动，30 天未更新即提示检查。
- 时效提示不等于内容错误，只表示需要重新确认。

## Slug

- 普通术语：英文小写连字符，例如 `chiral-doublet-bands.md`。
- 核素：质量数在前、元素符号小写，例如 `130ba.md`。
- 能带：`核素-稳定标签`，例如 `130ba-band-1.md`；不得把可能变化的物理解读直接写入文件名。
