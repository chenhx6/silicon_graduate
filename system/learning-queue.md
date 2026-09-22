---
type: system-learning-queue
graph-excluded: true
updated: 2026-09-06
---

# 90 天持续学习队列

## 当前周期

- 周期：2026-09-05–2026-12-03（90 天）
- 调度：每日 22:00，`Asia/Shanghai`，Docker 内 `run_daily_learning_daemon.py`
- 主轴：核结构约 80%；相邻核科学约 20%；A≈130 不是边界
- 当前状态：`active`；第一运行从既有学位论文 corpus 的 graph closure 和跨质量区比较开始
- 入口规范：[`continuous-learning workflow`](workflows/continuous-learning.md)

## Seed corpus 状态

15 篇学位论文已完成内容摄入或复读，附加 1 篇 `103Pd` 实验报告；本队列只记录后续学习状态，不重复制品页的 claim。完整批次、raw 哈希和保护路径见 [`degree-dissertation-ingest-20260905.manifest.json`](../outputs/degree-dissertation-ingest-20260905.manifest.json)。

| 来源 | 当前入口 | 首轮学习动作 |
| --- | --- | --- |
| 丁兵 2012 | [[../knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin]] | 与 `127/128I` 能带、ADO/NPA 边界和对应期刊谱系互链 |
| Alwaleedi 2013 | [[../knowledge/sources/alwaleedi-2013-band-structures-131ce]] | 复读关键图表，连接 `131Ce`、wobbling/chirality/γ-soft 竞争解释 |
| 强赟华 2019 | [[../knowledge/sources/qiang-2019-high-spin-130-131ba-87zr]] | `130/131Ba`、`87Zr` 的高自旋结构与 signature/形变比较 |
| 车兴来 2007 | [[../knowledge/sources/che-2007-high-spin-108-112ru-134-135ba]] | `108/112Ru`、`134/135Ba` 的高自旋/fission 证据互链 |
| Smith 1998 | [[../knowledge/sources/smith-1998-rotational-bands-127-131pr]] | `127–131Pr` 多形状转动带与 A≈130 横向比较 |
| Sensharma 2021 | [[../knowledge/sources/sensharma-2021-wobbling-motion-135pr-187au]] | `135Pr/187Au` wobbling/chiral-wobbler 竞争解释和必要 observable |
| Régis 2011 | [[../knowledge/sources/regis-2011-fast-timing-labr3]] | LaBr₃(Ce)、fast timing/MSCD、寿命不确定度与 `lifetime` 页 |
| 王华磊 2006 | [[../knowledge/sources/wang-huale-2006-170re-176ir-thesis]] | `170Re/176Ir`、高自旋/超形变和质量区迁移条件 |
| Wang Enhong 2015 | [[../knowledge/sources/wang-enhong-2015-neutron-rich-fission-fragments]] | 裂变碎片布居、门条件和多核素证据独立性 |
| Hinke 2010 | [[../knowledge/sources/hinke-2010-100sn-decay-spectroscopy]] | `100Sn` 衰变/`B(GT)`、能级方案和 decay evidence |
| Lubos 2016 | [[../knowledge/sources/lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] | `100Sn` 邻近核素、同位素/同中子素比较 |
| Morgan 2008 | [[../knowledge/sources/morgan-2008-237pu-nilsson-orbitals]] | `237Pu` 第二势阱、Nilsson 轨道和模型依赖 |
| Hayes 2005 | [[../knowledge/sources/hayes-2005-k-conservation-178hf]] | `178Hf` K 守恒破缺、K-mixing 与 OCR/locator 边界 |
| Pálffy 2006 | [[../knowledge/sources/palffy-2006-neec-thesis]] | NEEC 理论 source-only，连接反应/衰变与核科学桥接 |
| 陈思泽 2014 | [[../knowledge/sources/chen-size-2014-6li-pgamma-7be]] | `6Li(p,γ)7Be` 反应谱学与直接/复合反应判据 |
| 附加报告：Dietrich 1974 | [[../knowledge/sources/dietrich-1974-excited-states-103pd]] | 标为实验报告，不与学位论文计数混淆 |

`Pálffy` 与 `陈思泽` 目前可保持 source-only，后续只有出现可复用结构/方法证据时才扩展基础页。所有 source claim 的 `needs_review` 状态按原页保留，不因进入队列自动清除。

## 运行队列与里程碑

### 下一次运行：graph closure / Phase 1

- 先补 15 篇 corpus 的 source↔source、source↔核素/能带/实验/方法/模型/project 反链。
- 建立 A≈80/100/130/160/190 与超形变/裂变同核异能态的比较坐标，明确哪些比较是同位素、同中子素或不适用。
- 从现有 `135Pr`、`187Au`、`100Sn`、`131Ba`、`127/128I` 竞争解释中选高信息增益问题；避免仅做格式维护。
- 若三篇以上直接相关来源已改变解释排序，生成第一份 thematic REFLECT 和开放问题增量。

### 后续候选池（动态，不是固定清单）

候选必须经过去重、全文/locator 核验和重要性判断后才进入运行：

- A≈80/100/160/190 的 wobbling、chirality、shape coexistence、K-isomer 和超形变独立实验；
- DCO/ADO、线偏振、mixing ratio、RDDS/DSAM/fast timing、`B(E2)`/`B(M1)`/`Q_t` 方法论文；
- 反例、null result、修订/评论文章和同一实验的独立重分析；
- 反应、衰变、质量、β/GT、裂变和探测器/数据分析资料；
- 壳模型、CSM、TRS、TAC、PRM/QTR/TPSM、IBM/IBFM、CDFT、RPA、R-matrix、NEEC 的必要桥接来源。

每批候选记录题名/作者/年份、质量区/主题、直接相关性、预计信息增益、独立性、raw/获取状态、失败原因和下一步。重要但暂不选入的问题写入当日或周报的 `Deferred important issues`，不要为凑数量强行摄入。

## 状态值

来源/问题可使用：`queued`、`active`、`checkpoint`、`deferred`、`completed-mainline`、`completed-evidence`、`blocked-needs-source`、`safe-suspended`、`candidate-L4`。`completed` 只表示本轮实际阅读覆盖，不等于人工审核或最终科学结论。
