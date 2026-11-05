---
type: l4-report
title: "2026-11-05 全库审计、创新候选与论文状态报告"
created: 2026-11-05
updated: 2026-11-05
status: partial
project: full-library-audit-a130-paper
---

# 2026-11-05 全库审计、创新候选与论文状态报告

本轮完成三条主线的一次收敛：

1. 对 A≈130 相关知识页、模型页、方法页和分析脚本做残余确认性措辞审计；
2. 对公开文献和 Wiki 候选做单点创新筛选；
3. 对 P-ADO 文章和 133Ce 私有路线重新检查证据门。

全库审计发现的主要问题是模型 benchmark、synthetic fixture、固定 nuisance
toy 和历史研究草稿中的语义升级。已直接更新相关知识页和分析输出，把
`confirmed/proof/definitive/excluded` 降为 `screening/conditional/model result`
并保留输入身份和证据边界。旧 A130 omnibus 草稿继续作为 withdrawn historical
failure case。

研究候选的当前排序是：

- \(^{135}\mathrm{Pr}\)：matched-input、leave-EM-out predictive test；
- \(^{129}\mathrm{Ba}\)：365-keV single-line response closure；
- \(^{130}\mathrm{Ba}\)：gamma-soft adversarial test；
- \(^{135}\mathrm{Nd}\)：same-nucleus chiral/TiP control；
- \(^{67}\mathrm{Ga}\) P-ADO：公开表格 alignment-transfer/coverage calibration。

P-ADO 仍是目前最可独立完成的文章包，适合继续按 EPJ A 方向准备；它的核心
结果仅属于公开表格级条件统计校准。文章尚缺作者/合作信息、永久公共 DOI、
许可和 paper-level claim admission，故不能宣称可投稿或已达到 publication-ready。

\(^{133}\mathrm{Ce}\) 的核结构创新潜力更高，但当前 readiness 仍为 partial-L4。
只读审计指出 W1 prompt/H/V 矩阵产品缺少可靠的 producer/run/gate lineage，
且没有事件流、partner-resolved lifetime、holdout 或联合 response covariance。
下一步应先恢复 producer/event chain，再决定是否生成核结构稿件。

## 验证

- `python3 system/scripts/analysis/test_analysis_suite.py`：通过；
- `python3 -m unittest discover -s system/tests -p 'test_*.py'`：635 tests passed；
- `python3 system/scripts/wiki_lint.py --fail-on error`：0 errors；
- `python3 system/scripts/wiki_boundary_check.py --root .`：`ok: true`；
- `python3 system/scripts/wiki_archive_gate.py check --root . --changed`：0 failures；
- `python3 system/scripts/wiki_automation_preflight.py --root .`：`ok: true`；
- `git diff --check`：通过；
- `.agents/skills/absorb`：12 tests passed；
- `.agents/skills/get-paper`：19 tests passed。

本报告是过程交代和 readiness 记录。可复用的科学边界和候选排序已同步写入
[`knowledge/research-notes/full-library-residual-state-audit-20261105.md`](../../knowledge/research-notes/full-library-residual-state-audit-20261105.md)。
