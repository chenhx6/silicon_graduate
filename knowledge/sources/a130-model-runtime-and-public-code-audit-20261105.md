---
type: source
title: "A≈130 模型与公开代码运行时审计：HFODD、BIGSTICK、DIRHB、ROOT 与 Geant4"
aliases: [A130 model runtime audit, public nuclear-structure code route audit]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
source_type: public-software-and-runtime-audit
reading_depth: skimmed
authors: [HFODD Collaboration, BIGSTICK contributors, DIRHB authors, ROOT Collaboration, Geant4 Collaboration]
year: 2026
citation_key: ""
title_original: "A reproducibility audit of public nuclear-structure models and the current runtime for A≈130 research"
canonical_source: "HFODD official index; BIGSTICK public repository; DIRHB arXiv:1403.4039; ROOT install page; Geant4 11.4 download page (all retained in the archive manifest)"
source_url: "See canonical_source and the archived manifest."
data_version: "runtime-audit-2026-11-05"
raw_file: "raw/papers/gpt/query/20261105-model-runtime-audit/manifest.json"
raw_sha256: "d584aaf1f51687336a0e0c299770854f4d827b5d5e4c6b312848ecc8a067260e"
raw_storage_status: archived-local
archive_required: true
nuclei: [132la, 130ba, 163lu, 208pb]
methods: [HFODD, BIGSTICK, DIRHB, ROOT, Geant4, TPSM, particle-rotor-model, TAC]
tags: [a130, model-audit, software-provenance, runtime, reproducibility, triaxiality]
---

# 代码可见性、可运行性和论文生产证据必须分开

## Bibliographic Record

本页登记的是公开软件、公开代码仓库、公开 DIRHB 论文和当前运行时审计的组合
来源，不是一篇单独的实验论文。HFODD 使用官方 v2.73y 索引与其公开 benchmark
入口；BIGSTICK 使用归档的 Git 快照；DIRHB 使用 arXiv:1403.4039；ROOT 和
Geant4 使用官方安装/下载页面快照。每个实际取得的文件、URL、大小和 SHA-256
均列在归档 manifest 中。

## Scope and Reading Depth

本单元定向审计模型/代码的版本身份、编译或 smoke test、输入输出边界和对
A≈130 论文路线的适用性。没有把所有第三方仓库读成完整代码审查，也没有把
任何 scaffold 的输出提升为目标核素实验事实。HFODD 源码文件端点在当前运行时
返回 404 JSON，DIRHB 源码没有取得；这两项均保留为访问/准备度边界。

## Research question

在 A≈130 三轴形变与集体激发研究中，哪些公开模型或工具已经在当前运行环境
通过了最小可复现实验，哪些只能作为路线候选或简化 scaffold，哪些不能替代
奇核高自旋的完整理论生产者？

## Archived material and reading boundary

本研究单元的文件清单和哈希保存在
`raw/papers/gpt/query/20261105-model-runtime-audit/manifest.json`。其中包括
BIGSTICK 的公开 Git 快照、DIRHB 的公开 arXiv 论文、HFODD 官方索引、
ROOT/Geant4 官方文档快照，以及 HFODD Mendeley 文件端点在本运行时返回的
404 JSON。最后一项是访问失败证据，不是 HFODD 源代码，不能作为已取得源码的替代。

运行时审计回执为
`outputs/l4/20261105-a130-model-runtime-audit/report.md`；它记录了命令、版本、
通过的 benchmark 和未完成的编译边界。临时下载、模型测试和 subagent 结果只有在
该回执或本页明确列出时才计入审计范围。

## Direct runtime results

### Verified in the current environment

- ROOT `6.40.04`：PyROOT 冒烟测试能够创建、填充并读取 `TH1D`。
- Geant4 `11.4.2`：`geant4-config` 可用；材料测试能够创建 `G4_AIR`；已安装的
  G4NDL、G4EMLOW、PhotonEvaporation、RadioactiveDecay 和 G4ENSDFSTATE 数据集
  通过数据集检查。
- HFODD `v2.73y`：官方 A≈130 相关 `la132-a.dat` benchmark 已编译并运行，生成
  `.rec` 与 `.rev` 输出。该结果属于公开 benchmark 的运行时审计，不能外推为
  任意奇核、任意无对称性 TAC 计算均已闭合。
- BIGSTICK：公开 Fortran 代码在当前环境串行编译并运行自带 sd-shell benchmark；
  benchmark 基底维数为 `44,133`，输出能级、波函数、密度和日志。并行构建的
  module 依赖顺序仍需单独处理。

### Available but not admitted as complete producer

- DIRHB 的公开论文描述球形、轴对称和三轴静态 RHB 计算。当前单元没有完成
  DIRHB 源码编译，也没有把它当作奇核高自旋 TAC-CDFT 生产者。
- Liverpool 页面公开的 Woods–Saxon/CSM 路线适合回弯、alignment 和 Routhian
  交叉审计；老旧 Linux 程序的稳定性和编译状态尚未在本单元闭合。
- ArbModel/IBM 的公开源码路线受当前环境缺失 Eigen 影响，未形成可运行第三方
  producer。
- KSHELL 需要 BLAS/LAPACK，当前环境未完成链接；不能把代码存在写成 A≈130
  高自旋壳模型结果。
- NPTool 的历史对象审计已经有独立 source 页，但当前运行环境没有可执行
  `nptool`，且新 GitLab successor 未在本单元取得。

## What the local scaffolds mean

仓库内 PTRM、TPSM、3D-TAC、IBM、CSM 和轴对称 RMF 脚本适合做透明的公式、
极限和参数敏感性验证。它们不能在论文中分别改称为完整 QTR、完整 TPSM、
自洽 3D-TAC-CDFT、完整 IBM producer、成熟 TRS producer 或完整 CDFT。

尤其是：

1. 简化 PTRM 可以先检验 wobbling energy 对 \(\gamma\)、惯量序和准粒子耦合
   的鲁棒性，但必须报告参数扫描和轴对称极限；
2. HFODD 可以提供自洽 Skyrme-HFB 旋转形变演化的微观约束，但不能直接给出
   奇核 partner-band 劈裂或唯一的手征双阱量子化结果；
3. Geant4+ROOT 可以量化指定几何下的探测器响应和观测量偏差，但没有真实阵列
   几何、死层、阈值、校准和响应协方差时只能作方法性模拟；
4. BIGSTICK 可以作受限壳模型交叉检查，但 A≈130 高自旋空间、有效算符、
   截断和资源约束必须单独验证。

## Summary

当前环境中最可靠、可作为后续研究基础的组合是 ROOT、Geant4、HFODD 的公开
benchmark 和 BIGSTICK 的串行 benchmark。DIRHB、KSHELL、ArbModel、NPTool
以及完整 TPSM/QTR/TAC-CDFT 生产路线仍有明确的编译、资源、数据或模型适用域
边界。第一篇单点文章不应把完整微观生产者作为硬依赖。

## Key Results

| ID | claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MRT-01 | ROOT 和 Geant4 在当前 runtime 通过最小 smoke test | runtime-result | direct-runtime | `outputs/l4/20261105-a130-model-runtime-audit/report.md` | true |
| MRT-02 | HFODD v2.73y 的公开 A≈130 benchmark 在当前环境运行 | runtime-result | delegated-runtime | same audit report; official index snapshot | true |
| MRT-03 | BIGSTICK 的公开串行 sd-shell benchmark 在当前环境运行 | runtime-result | delegated-runtime | same audit report; pinned Git snapshot | true |
| MRT-04 | DIRHB 公开且适合静态 RHB 路线，但本单元未完成运行 | access-and-readiness-boundary | direct-paper-and-access | archived arXiv PDF and report | true |
| MRT-05 | 本地 PTRM/TPSM/TAC 程序是可运行 scaffold | code-scope-audit | local-code-and-runtime | local analysis scripts and report | true |
| MRT-06 | 第一篇 A≈130 单点文章的最小可靠组合是方法层 profile/coverage；完整 TPSM 或 TAC-CDFT 暂不作为硬依赖 | research-design-inference | cross-source-synthesis | runtime audit + current P-ADO package | true |

所有 MRT claims 仍为 Codex self-audit，未标记 `human-reviewed`。软件版本、编译
器、输入文件和 benchmark 输出的身份必须在任何论文计算中重新固定；运行成功本身
不证明模型适合目标核素。

## Competing explanations and failure modes

- 一个能级曲线可以被简化转子、粒子—转子、γ-soft core、组态混合或平均场
  计算同时描述；单一模型拟合不能自动建立模式身份。
- HFODD 的 benchmark 成功可能只证明编译、输入解析和该 benchmark 的数值路径，
  不能证明目标奇核 blocking、时间反演破缺或无对称性旋转态已正确设置。
- BIGSTICK 的 sd-shell benchmark 成功不能证明 A≈130 模型空间的可行性；内存、
  BLAS/LAPACK、有效电荷和 truncation 仍是独立风险。
- Geant4 的几何响应模拟若没有 measured-vs-simulated closure，不能把名义效率
  或偏振响应当成实验修正。

## Competing Interpretations and Limitations

一个能级曲线可能同时被简化转子、粒子—转子、γ-soft core、组态混合或平均场
计算描述；代码通过 benchmark 只证明软件路径可执行。HFODD 的 benchmark 不
绑定目标奇核 blocking，BIGSTICK 的 sd-shell benchmark 不绑定 A≈130 SN100
空间，Geant4 smoke test 不提供真实阵列响应。软件版本、输入、输出和目标核素
适用域必须在任何论文计算中重新固定。

## Research route decision

当前最小研究路线按以下顺序推进：

1. 先把 P-ADO 公开表格的 covariance、family-wise coverage 和 feeding-aware
   negative control 做成可审计的单点方法文章；
2. 对 `133Ce`，只有在 event/matrix provenance、response covariance、producer
   lineage 和 holdout 闭合后，才启动 response-aware collective-mode
   identifiability 的完整核结构文章；
3. 需要独立微观约束时，优先复现 HFODD benchmark，再选择一个目标核素和少量
   旋转频率点；不同时展开多泛函、多 pairing、多 blocking 扫描；
4. 只有在完整阵列几何和校准信息可得时，才把 Geant4 响应加入 `133Ce` 文章；
5. 暂缓把完整 TPSM、3D-TAC-CDFT 或大空间 A≈130 shell-model 当作第一篇文章
   的必要条件。

## Reusable stop conditions

- 公开代码的版本、输入、输出和运行日志不能绑定；
- 代码只返回预设 benchmark，却没有目标核素的适用模型空间；
- 结果依赖未经校准的 detector response、feeding 或 effective operator；
- 不同模型均能复现能级，而没有独立 \(B(E2)\)、\(B(M1)\)、偏振、寿命或 holdout；
- 论文措辞需要把 runtime success 写成实验事实或把 scaffold 写成完整理论。

## Extracted Pages

[[a130-model-runtime-and-code-route-audit-20261105]]、[[a130-model-choice-card]]、
[[131ce-133ce-mode-identifiability-boundary]]、
[[pado-alignment-response-dependence-paper]]。

## Human review and promotion history

本页是 Codex self-audit；尚未发生用户的 paper-level claim review。2026-11-05：
将模型/运行时审计从临时 subagent 结果提升为可追踪的 source/knowledge 记录，
同时保留 HFODD 源码未取得和 DIRHB 未运行的边界。
