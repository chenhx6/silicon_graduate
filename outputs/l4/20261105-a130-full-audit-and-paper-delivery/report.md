---
type: l4-report
title: "A≈130 全库审计、创新筛选与单点论文交付回执"
created: 2026-11-05
updated: 2026-11-05
status: partial
visibility: private
publication_status: local-draft
review_status: unreviewed
tags: [a130, full-library-audit, triaxiality, collective-modes, pado, 133ce, epja]
---

# A≈130 全库审计、创新筛选与单点论文交付回执

## Scope

本回执对应用户要求的三项工作：

1. 审计 Wiki 全库和历史 raw/知识材料，纠正发现的错误或过强表述；
2. 围绕 A≈130 三轴形变和集体激发模式寻找可证伪、可发表的单点创新；
3. 形成按 `raw/writing/gpt/<topic>/` 组织、可复现、适合 EPJA/PRC/PLB 路线的文章包。

审计不把旧 `raw/writing/gpt/a130-triaxial/` 当作事实源。该目录已经被记录为
素材/失败案例：它包含不一致的 `135Pr` 数值、source identity 错位、未闭合
partner evidence、不可重建的 figure cache 和 TeX/Typst/PDF 身份漂移。

## Durable audit and learning outputs

- 全库规模基线：约 `4,088` 个 raw 文件、`1,358` 个 knowledge Markdown 页面；
  South Africa `133Ce` 原始数据继续保持 local-only-unpublished。
- 代表性 proof-like 语言已在全库 claim-calibration 审计中降级为
  experimental fact、model result、author interpretation 或 conditional inference
  的对应措辞；`133Ce` 两份研究 note 的“证明/决定性证伪”边界已修正。
- 新增模型/运行时 source：
  `knowledge/sources/a130-model-runtime-and-public-code-audit-20261105.md`。
- 新增模型/运行时研究 note：
  `knowledge/research-notes/a130-model-runtime-and-code-route-audit-20261105.md`。
- 新增运行时回执：
  `outputs/l4/20261105-a130-model-runtime-audit/report.md`。
- 公开代码/文档归档 manifest：
  `raw/papers/gpt/query/20261105-model-runtime-audit/manifest.json`。
- 期刊和模板审计：
  `knowledge/research-notes/journal-route-and-template-audit-20261105.md`。

## Innovation decision

### Primary: P-ADO reaction-response calibration case study

当前最成熟的单一创新是：把“跨 projectile、beam energy 和 feeding condition
转移一个 shared `sigma/J` alignment nuisance”变成显式的 profile-likelihood、
covariance-sensitivity 和 family-wise coverage 检验。

这篇文章使用 `^{67}Ga` 公开十行表格作为 reproducible calibration case study。
它的 A≈130 价值是 downstream analysis gate：任何后来用 ADO/DCO/偏振和
mixing-ratio 分支判定 wobbling、TiP、chirality 或 signature partner 的分析，
都应先通过 alignment transfer 和 coverage 检查。文章不宣称新的 A≈130 实验
测量，也不宣称 P-ADO 普遍失效。

文章工作包：

`raw/writing/gpt/pado-alignment-response-dependence/`

核心结果在声明的 table-level Gaussian contract 下为：

- shared `r0=0.280146` at `rho=0`；
- family、energy 和 minimal global convex-mixture extension 在中心协方差
  合同下没有 AIC/BIC 支持；mixture 参数不解释为物理 feeding fraction；
- refined rho profile 的 observed minimum `Dmax^2=22.18` at `rho=0.64`；
- matched toy maximum-statistic 95% quantiles `9.60--10.59`；
- `5x7` fixed-\(\rho\) true-`r`/true-`rho` grid 的 matched acceptance 约
  `0.62--0.68`；
- 强制拟合 `rho=0` 时，部分非零相关生成格点的 coverage 约降到 `0.47`，
  发生在扫描的负相关边界。
- profile-preserving toys (1000 per true-\(\rho\)) give \(q_{0.95}=8.47--8.79\)
  for true \(\rho=-0.6,0,0.6\), compared with observed profiled
  \(D_{\max}^2=22.18\).

可支持的中心结论是：

> 在声明的表格级 Gaussian/profile 合同下，公开 `^{67}Ga` 表格与单一 shared
> alignment response 条件性不相容；family-specific、energy-dependent 或
> feeding-mixture replacement model 仍未被唯一识别，单行二维阈值也不能直接
> 当作十行 maximum statistic 的 family-wise 95% threshold。

### Secondary: `133Ce` response-aware collective-mode identifiability

`133Ce` 仍是核结构价值更高的路线，但当前保持 `partial-L4`。文章核心应是
在显式 gate、alignment、detector response、feeding、covariance 和 holdout
下比较 wobbling、signature partner/TiP、gamma-soft particle-core、
gamma-rigid rotor、crossing/configuration mixing 及 identity/null 模型。

当前停止条件仍未解除：缺 event list、完整 `polarization.xlsx`、absolute
lifetime input、producer-level response covariance 和独立 holdout。South Africa
数据也没有公开发布授权，不能把派生 workbook 数字直接写成公开实验数据。
闭合后首选 EPJA Regular Article；只有模式排序在 holdout 上稳定且数据权限和
DAS 闭合，才考虑 PRC Research Article。

## Article package state

P-ADO package 已完成：

- 正确的 Zobel Table 1 fixture 和 source locator；
- shared/family/energy/mixture profile；
- covariance profile 和 coverage grid；
- deterministic validation；
- figure producers、PDF/PNG figures 和 source claim ledger；
- Data Availability、Code Availability 和 limitation wording；
- Springer Nature EPJ A route、REVTeX fallback 和本地 source manifest；
- EPJ A `iicol` 双栏编译的六页 A4 PDF：
  `raw/writing/gpt/pado-alignment-response-dependence/main.pdf`。

最终双栏 PDF 的 SHA-256 保存在
`raw/writing/gpt/pado-alignment-response-dependence/analysis/results/compile-record.json`。
页面已重新渲染检查；表格、宽图和引用均无遮挡、截断或未解析 citation。剩余
underfull box 只是排版提示。

## Readiness boundary

当前 disposition 仍为 `partial/not-ready`。投稿前必须完成：

1. 填入作者、通讯作者、机构和合作信息；
2. 对 P0/P1 claim ledger 做作者定向确认；
3. 决定是否把 `^{67}Ga` 文章明确限定为 calibration case study，或补充第二个
   独立 reaction-conditioned benchmark；
4. 复核最终 EPJA submission page、DAS 和模板版本；
5. 若要升级为实验显著性或 event-level likelihood，必须取得原始 counts、
   row covariance、detector response 和 feeding provenance。

这些门没有关闭前，不能把文章称作已提交、已被期刊接受或已完成 event-level
重分析。

## Verification

本轮已通过：

- `wiki_boundary_check.py --root .`；
- `wiki_archive_gate.py check --root . --changed`；
- `wiki_automation_preflight.py --root .`；
- `wiki_lint.py --fail-on error`：`0 errors`；
- `system/scripts/analysis/test_analysis_suite.py`；
- P-ADO `validate_outputs.py`；
- P-ADO analysis/figure `py_compile`；
- Tectonic compilation and visual inspection of the six-page `iicol` manuscript；
- `git diff --check`。

## Resume point

下一次继续时，优先做 P-ADO P0/P1 claim-to-locator final audit 和 author/data
metadata closure；`133Ce` 继续停在 response/producer/holdout readiness。若进入
HFODD、Geant4 或 BIGSTICK 计算，先固定版本、输入、资源和独立 companion
observable，保留 benchmark/scaffold 与目标核素物理结论之间的边界。
