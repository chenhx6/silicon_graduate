---
type: output
graph-excluded: true
created: 2026-11-07
updated: 2026-11-07
---

# 同核异能态与六区机制研究：本轮交付回执

本轮是用户主动研究的有界交付，长期课题仍开放。
研究内容、公式、候选与反证以`knowledge/projects/isomer-six-region-transfer-research.md`
及其source/synthesis/research-note为准；本报告保存执行结果，不成为第二知识库。

## 模型与工作分配

Gemini Flash Tiered/high与Terra/xhigh都已通过实际subagent任务返回产物。
12个研究worker中11个Gemini、1个Terra；详细步骤、独占文件和预期结果写入派工提示。
总控负责原件/图表/单位核查与集成，Terra承担精确多体模型与复杂理论审查。
模型身份不替代证据；候选草案中的无依据阈值、模型误名和过强裁决已由总控撤回。
路由回执见`model-routing-receipt.json`。本轮未修改主会话reasoning配置或daemon。

## 验收与实际范围

1. **身份与原件**：51个输入PDF、692物理页、49种字节内容；51项均有阅读记录关联，
   0原件哈希改变。重复副本、出版/作者稿及误命名peer-review附件分别登记。
2. **重点阅读**：Jain151页分19块阅读，Ch.3–5重点代数；其它4综述75页有块级阅读账。
   刘晨2016、肖骁2019与Hayes2005学位论文关键问题回读；不宣称Hayes整本或所有实验原始数据重放。
3. **综合深化**：三篇主综合及条件化动力学综合已实质修订；相冲突的既有跨区笔记同步纠正。
   六区矩阵保留核素/组态、自旋、模型条件、竞争解释与未见/未覆盖的区别。
4. **外部补证**：新原件、源码、元数据与首页预览按各自实际范围归档。
   100Ru寿命原件已补得；98Mo与191/193Ir仍为首页范围，未升级成全文。
5. **L3/L4**：四个候选有反方模型、必要输入、可区分观测和停止条件。
   有界单j精确计算与粒子—空穴反向控制完成；真实核耦合、PES和热化/产额仍有输入缺口。
6. **验证与发布**：范围内新结构error为0；归档和边界检查通过。
   preflight已通过，QMD文字索引已更新并通过新note及L4新路径检索；Git最终发布结果见本地回执。

## 复现与检查

- `local-inventory.json`、`coverage-reconciliation.json`与`original-preservation-check.json`保存输入对账。
- `reviews/jain-primary-reading-ledger.json`、`reviews/four-review-primary-reading-ledger.json`
  保存实际块级阅读及未核验范围，不等于全部转引实验已核验。
- `final-numerical-replay.json`：20行单j强度逐值重放一致；Wigner代数的独立检查另有回执，
  不是第二套完整多体求解器。
- `coupled-coordinate-algebra-check.json`：示意耦合势3个符号恒等式通过，只验证局部代数。
- `archive-final.json`：62个source与5份规范manifest，失败数0。
- `lint-final.json`及`lint-delta.json`：全库137 errors/418 warnings，HEAD基线202/350，
  本轮新增error=0。57项source缺citation_key与17项新增孤页警告保留，
  不为通过检查制造无来源的书目key；完整metadata/DOI仍可回原件核对。
- `structure-final.json`：本轮126项文件的JSON/UTF-8、低位控制字符和冲突标记检查无异常。
- `boundary-final.json`：六类落点与QMD collection边界通过。
- `preflight-final.json`：exit0，归档及路径复查通过；数值运行回执命名已与raw归档manifest区分。
- `qmd-refresh.json`：1478篇文字索引，新增note及L4回执路径均可取回；未运行embed或独立cleanup命令，既有向量积压保留。
- Git显式范围、最终精确提交hash和push结果只写`publication-final-receipt.local.json`。

## 继续研究的入口与停止原因

当前信息增益优先项是使用已取得的100Ru寿命/模型表、补98Mo完整正文/E3，
以及恢复192Os分支、ICC与模型共同输入。具体C1–C4设计在knowledge候选笔记。
本轮不重复生成没有Hamiltonian/波函数/环境轨迹的真实核数值。
闭合的是本次文献与有限模型里程碑，不是六区所有核素、全球新颖性、
所有历史claim或所有未发现现象。没有待用户批准的普通研究步骤。

用户调用auto/go-on/brainstorm/optim/all后，继承已有授权继续执行。
原生goal查询为空；未另行推断创建目标。优化采用独占文件并行与避免重复全库扫描，
未作等价前后性能基准，因此不报告虚构加速比例。
