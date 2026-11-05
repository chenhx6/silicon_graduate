---
type: research-note
title: "全库残余模型状态与 A≈130 研究候选审计"
aliases: [full-library residual state audit 20261105, A130 residual claim calibration]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
scope: full-library/claim-state/a130-paper-candidates
tags: [full-library-audit, a130, wobbling, chirality, triaxiality, pado, 133ce, 135pr]
evidence_sources: [pado-alignment-response-dependence-paper, post-30-day-nuclear-structure-paper-prospectus, 135pr-common-response-evidence-contract-20261031, 135pr-hypothesis-discrimination-priority-20261101, userdata-133ce-southafrica-dataset]
created_from: "2026-11-05 full-library residual model-state and paper-candidate audit"
---

# 全库残余模型状态与 A≈130 研究候选审计

## Research Trigger

本次审计接续 P-ADO 论文收敛和此前的模型状态清理，检查
`knowledge/concepts`、`knowledge/models`、`knowledge/methods` 与
`system/scripts/analysis` 中是否仍把模型、preset、synthetic fixture 或
条件 toy 结果包装成实验确认。重点覆盖 A≈130 的 wobbling、chirality、
TiP、signature inversion、MχD、gamma-soft/gamma-rigid 和寿命/形变反演。

## Grounded Evidence

本页以当前 P-ADO project、135Pr response contract、论文 prospectus、
133Ce user-data source boundary 和本轮已通过的分析/治理检查为证据入口。
具体实验事实仍回到对应 `knowledge/sources/` 原件与 locator；本页不把
analysis regression 或 lint 当作物理验证。

## Provisional Reasoning

1. 角分布双根、偏振和共同响应问题必须分成观测层、响应层和机制层。
   `135Pr` 的旧 11.1-sigma 叙述已降为固定 toy response 下的小根偏好；
   未恢复逐角 counts、producer response、feeding 和联合协方差前，不能写成
   实验排除或 signature-partner 终局确认。
2. synthetic/model benchmark 输出统一降为 screening、conditional
   compatibility 或 declared chi-square preference。PES crossing、O(6)-like
   ratios、Mikhailov \(z_\gamma\)、DSAM/RDDS demo lifetime、MχD heuristic
   score 和 3D-TAC/CDFT angles 都不能独立成为目标核的实验事实。
3. signature inversion 是有信息量的谱学现象，但不能单独证明三轴形变或
   \(p\)-\(n\) residual interaction；M1/E2、寿命、组态、response 和竞争模型
   必须共同考虑。
4. g-factor equality、Koike selection rules 和 MχD 四类门是模型/条件筛查
   工具。相容结果不能单独建立手征性，不相容结果也只是在声明误差与模型合同
   下削弱对应解释。
5. `133Ce` 南非数据继续保持 local-only、partial-L4。当前最有信息量的动作是
   恢复 W1 producer/event lineage，修正 prompt/H/V 时间差处理，建立逐跃迁
   ledger 和 holdout；没有这些输入不写强模式结论。

## 研究候选排序

| 优先级 | 候选 | 单点创新 | 当前边界 |
|---|---|---|---|
| 1 | \(^{135}\mathrm{Pr}\) public-data EM holdout | 只用能级拟合，再预测未参与拟合的 \(\delta\)、\(f_{E2}\) 或相对 EM observable；比较 wobbling/TiP/signature 竞争模型 | 2026 Bayesian inference 的完整 likelihood、prior、energy covariance 和原始 response 尚未公开；可先写方法/不可识别性结果 |
| 2 | \(^{129}\mathrm{Ba}\) 365-keV single-line closure | 对一条历史大/小 \(\delta\) 分歧线完成 A2/A4、偏振、共同取向和寿命锚点的 response-complete closure | 需要新实验或完整公开 raw 输入，PLB/PRC 依赖结果简洁度 |
| 3 | \(^{130}\mathrm{Ba}\) gamma-soft adversarial test | 用 gamma-soft particle-core 作为 adversarial model，与两准粒子 transverse-wobbling 做共同输入比较 | 需要 transition identity、绝对/寿命锚定强度和模型共同 observable |
| 4 | \(^{135}\mathrm{Nd}\) same-nucleus chiral/TiP control | 用同核 TiP 带作为 detector/质量区控制，检验 D3/D4 partner-resolved EM observable | D3/D4 identity、寿命和绝对强度仍不闭合 |
| 5 | P-ADO \(^{67}\)Ga table-level calibration | 公开表格上的 alignment-transfer、covariance 和 family-wise coverage audit | 当前最适合 EPJ A；仍需作者、许可、永久 DOI 和 paper-level claim admission |

## 当前文章状态

P-ADO package 保持 `partial/not-ready`。其统计结论限于
independent-row Gaussian、固定边际误差、block-diagonal covariance 和有限
common-\(\rho\) grid；不能写成 event-level reanalysis、实验 p-value 或普遍
否定 P-ADO。\(133\)Ce 工作包保持 secondary，不得把私有矩阵、workbook 派生量
或 producer 不明结果放入公开 `data/`。

## 验证边界

- Wiki lint：0 errors；warnings/info 是既有治理提示，不被本笔记解释为科学确认。
- Boundary、archive gate、automation preflight：通过。
- Analysis regression：通过。
- System tests：635 passed。
- `absorb` skill tests：12 passed；`get-paper` skill tests：19 passed。

本页是 Codex self-audit 记录，不是 `human-reviewed` 结论。论文使用具体 claim
时仍需回到 `knowledge/sources/`、`raw/` 原件和 paper evidence gate。

## Assumptions

本审计假定当前 Wiki source/project 页面中的 provenance、输入身份和既有
evidence boundary 没有被未记录的外部版本替换；若原始 producer、协方差或
作者权限发生变化，相关结论必须重新审计。

## Competing Explanations

模型输出与实验模式之间的差异可能来自 response、feeding、transition identity、
configuration mixing、gamma softness、TiP、signature partner 或 source lineage
重用；本页不把任一候选自动升格为机制结论。

## Transfer Conditions

本审计方法可迁移到其它候选核素，前提是重新建立 raw/source 身份、transition
ledger、response/covariance、holdout 和公开权限；本页的数值与候选排序不直接
迁移到其它核素。

## Failure Conditions

若发现 source identity、raw hash、路径边界、作者权限或关键 locator 不闭合，
应停止论文发布；若模型筛查没有独立观测或 holdout 支持，只能保留为 L3/readiness
结果。

## Falsification or Reverse Tests

若新的独立原始数据、producer ledger 或 partner-resolved absolute EM 输入改变
候选排序，更新相应 project；若 finite-grid/P-ADO 结论对 cross-row covariance
或 feeding-aware likelihood 不稳定，则撤回其更强的 transfer-audit 解释。

## Open Questions

1. P-ADO 是否能取得永久 DOI、许可和作者 claim admission？
2. \(^{135}\mathrm{Pr}\) energy-only holdout 是否能在公开输入下完成？
3. \(^{133}\mathrm{Ce}\) W1 producer/event lineage 和修正后的 prompt/H/V 矩阵能否恢复？

## Human Review

尚未进行用户逐条 paper claim review；本页保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-11-05：建立本页，固化残余状态审计、候选创新排序和 P-ADO/133Ce readiness
边界；后续若产生独立 raw/producer/holdout 证据，再更新对应 project。
