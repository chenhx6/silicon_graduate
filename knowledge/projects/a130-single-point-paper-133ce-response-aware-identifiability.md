---
type: project
title: "133Ce 候选集体模式的响应感知可识别性"
aliases: [133Ce response-aware collective-mode identifiability, 133Ce wobbling signature-partner paper candidate]
created: 2026-11-05
updated: 2026-11-05
status: active
review_status: unreviewed
project_stage: active-L3-partial-L4
confidentiality: private
publication_status: local-draft
nuclei: [133ce, 132ce, 134ce, 131ba, 135nd]
tags: [a130, triaxiality, wobbling, signature-partner, tilted-precession, response, paper-candidate]
---

# `133Ce` 候选集体模式的响应感知可识别性

## Agent active summary

本项目是 2026-11-05 全库审计后建立的单点论文候选。研究对象是 South Africa/iThemba `133Ce` 数据中被称为 `W1` 的候选带，研究创新暂定为：把门匹配、取向宽度、DCO/ADO、偏振/不对称度、混合比和电磁分支放入同一套响应显式的可识别性分析，量化不同矩阵处理和 alignment 假设如何改变 wobbling、signature-partner/TiP、γ-soft particle-core 与 crossing/configuration-mixing 的排序。

目前没有把任何模式写成已确认实验事实。现有输入为 partial-L4-ready；论文核心 claim、期刊级别和是否公开私有数据仍待验证。

## Research Question

在保留真实 gate、prompt timing、效率、偏振灵敏度和 alignment 不确定度的条件下，`133Ce` 候选带的观测量是否足以区分单声子 wobbling 与 signature-partner/TiP 或 γ-soft particle-core 解释？如果不能，哪一个最小 companion-observable/response 条件会改变排序？

## Current Hypotheses

当前竞争假设为 one-phonon wobbling、unfavoured signature partner/TiP、
gamma-soft particle-core 和 crossing/configuration mixing。它们共享同一
transition ledger 和 response nuisance，不能按不同数据预处理分别比较。

## Evidence Available

直接输入包括 South Africa 数据合同、workbook/ROOT 内容审计、133Ce 公开谱学
source 和 132/134Ce 邻近偶偶模型先验。原始 list-mode、完整偏振输入、绝对
寿命和 producer-level covariance 仍缺失。

## Candidate innovation

**单一核心创新点：**建立并验证一个可复现的 response-aware mode-identifiability test，证明或证伪“由 workbook 派生的单一 `E_wob`/小 `delta`/分支比即可判决 wobbling”这一分析假设。

候选文章只能保留这一条主线。A≈130 其它核素只作外部控制或竞争解释背景，不能再加入独立的第二、第三个主要成果。

## Grounded evidence

| Evidence | What it supports | Boundary |
|---|---|---|
| `knowledge/sources/userdata-133ce-southafrica-dataset.md` | 本地用户数据身份、矩阵和 workbook 的 partial-L4 入口 | 数据仍为 local-only-unpublished-user-data；不能把本地留档当公开许可 |
| `outputs/l4/20261101-133ce-southafrica-data-audit/report.md` | workbook arithmetic、ROOT/m4b 内容对应和 prompt/unprompt 分支差异 | 尚未闭合 producer、event provenance、response covariance、背景和 holdout |
| `knowledge/research-notes/133ce-southafrica-l4-data-contract-20261101.md` | 最小 observable contract 与停止条件 | 只支持 readiness，不支持出版级 mode claim |
| `knowledge/research-notes/133ce-triaxial-core-collective-mode-route-20261101.md` | 132/134Ce 邻近偶偶芯背景、竞争解释和初步分析路线 | NuclearMap 是邻近偶偶模型输入，不是 133Ce 的直接形变测量 |
| `knowledge/sources/ayangeakaa-2016-133ce-in-beam.md` | 133Ce 中高自旋谱学地图和 CNS/TAC-CDFT 解释边界 | 模型形变/组态依赖，不能替代当前数据的逐线响应复核 |
| `knowledge/sources/ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce.md` | 同核历史候选带、DCO/角分布和寿命缺口 | 共享实验谱系与作者解释，不能按独立实验重复计数 |

## Competing hypotheses

1. `H_W`: one-phonon wobbling coupled to a triaxial/γ-soft core;
2. `H_SP`: unfavoured signature partner with Coriolis/signature inversion;
3. `H_TiP`: tilted precession or related planar/near-planar collective motion;
4. `H_X`: crossing/configuration mixing or quasi-γ particle-core coupling.

这些是假设集合，不是当前排序结论。每个假设必须给出同一 observable bundle 下的预测和 falsifier。

## Minimum observable bundle

- 同一 prompt gate family 下的 ADO/DCO 计数与背景窗口；
- 同一 time-selection 下的 H/V 或等价 polarization counts；
- `sigma/J` 或完整 magnetic-substate nuisance 的校准/先验；
- 有限几何和效率/偏振灵敏度的能量依赖；
- transition identity、初末自旋宇称和同母态分支；
- `delta` 的全部实根/区间及其 covariance；
- `B(E2)_out/B(E2)_in`、`B(M1)/B(E2)` 的条件结果；
- 至少一个未参与主拟合的 gate family、transition block 或 detector subset 作为 holdout。

现有全库审计进一步表明，A≈130 没有一个跨核素适用的 scalar 判据。对
`wobbling` 与 `signature/configuration`、TiP 的最小可运行组合至少需要：

1. 已确认的能带身份和同宇称关系；
2. 两个以上相邻自旋点的能量演化；
3. 一条干净连接线的 DCO/ADO 与独立偏振或内转换分支仲裁；
4. 一个寿命锚点和完整同母态分支，用于条件性 `B(E2)`/`B(M1)` 比值；
5. 冻结参数后的竞争模型比较和 holdout。

`E_wob`、`B(E2)` 和 `B(M1)` 若来自同一组能级、分支、寿命和 `delta`，
不能再次作为相互独立的证据计票。当前工作包将采用 transition-level ledger
和原始计数 forward likelihood，显式共享 acquisition、效率、偏振标定、
alignment、背景和寿命 nuisance。

## Falsifiers and stop rules

- 若门匹配和响应显式的联合模型在 holdout 上仍稳定选择 `H_W`，且 `H_SP/H_TiP/H_X` 在同一输入下无法解释 companion observables，才可考虑 wobbling-support claim；
- 若 `H_W` 的排序只在固定 `sigma/J`、固定 polarization response 或混用 prompt/unprompt 矩阵时出现，模式结论降级为 response-conditional；
- 若不同 prompt gate、背景窗口或 detector subset 给出不一致的 `delta`/模式排序，停止在 systematic/readiness boundary；
- 若 transition identity、producer history 或响应 covariance 不能闭合，停止生成 publication-grade likelihood；
- 若公开数据/权限不能覆盖文章所用输入，稿件保留 local draft，不宣称可公开复现。

## Data and provenance boundary

文章工作包位于 `raw/writing/gpt/133ce-response-aware-collective-mode-identifiability/`。私有实验原件继续保留在 `raw/data/SouthAfrica/`；文章包只复制经许可的公开派生数据或脱敏摘要。所有外部来源按 `research-archive` manifest 归档。

## Current state

- `L3`: active；motivation、反方检索和候选期刊仍在进行；
- `L4`: partial；workbook 算术和矩阵内容一致性已完成，响应/producer/holdout 尚未闭合；
- `paper evidence gate`: 未进入最终准入；关键 claim 需 source/locator 和用户定向确认；
- `human review`: 未发生；当前内容为 Codex self-audit。

## Risks and Blockers

- prompt 与 non-prompt 矩阵分支不能未经门历史重建就联合；
- private user data 尚未获得公开释放授权；
- workbook 派生的 `delta`、`B(E2)` 和 `E_wob` 不能当独立观测量；
- 没有 holdout 或 response covariance 时，模式排序只能保持 conditional/readiness。

## Reusable analysis route

现有代码可作为受限骨架：精确 `F_k`/双根计算
`system/scripts/analysis/directional_correlation_f_coefficients_calculator.py`，
双根 profile `double_root_dco_polarization_statistical_arbitrator.py`，
`sigma/I` 计算 `in_beam_spin_alignment_sigma_mixing_ratio_extractor.py`，
Poisson 峰/物理边界区间、DSAM/RDDS 和 `triaxial_wobbling_tip_chiral_analyzer.py`。
这些模块的 fixture 和硬评分只能作为 toy/回归测试；新论文必须把它们接入真实
gate、响应和协方差，不能把现有 preset 的输出当作 `133Ce` 新测量。

## Next Actions

1. 完成全库和外部文献的反方新颖性扫描；
2. 从门匹配的 prompt H/V/g45/g90 输入重建第一版观测 ledger；
3. 实现 hierarchical/profile likelihood 与 gate/response sensitivity；
4. 用公开模型/邻核 source 约束竞争解释，保留模型结果与实验事实分层；
5. 只有核心 claim 通过数据和证据门后，生成投稿版 LaTeX。
