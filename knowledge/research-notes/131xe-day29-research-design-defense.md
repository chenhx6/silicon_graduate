---
type: research-note
title: "131Xe 794-keV宇称与882-keV双根：Day29研究设计答辩"
aliases: [131Xe Day29 research design defense]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day29 research-design-defense prompt plus Day28 131Xe response and parity contracts"
evidence_sources: [banik-2020-131xe-multiple-band-structures, chakraborty-2023-131xe-wobbling-origin, 131xe-low-spin-partner-crosswalk, 131xe-882-branch-response-contract, 131xe-1601-parity-version-boundary, rose-brink-1967-phase-defined-angular-distributions, two-point-angular-correlation-ratio]
tags: [131xe, research-design, parity, mixing-ratio, angular-distribution, polarization, internal-conversion, covariance, l3-readiness]
---

# 131Xe 794-keV宇称与882-keV双根：Day29研究设计答辩

## Research question

在同一 `130Te(α,3n)131Xe`、38-MeV INGA 数据谱系中，能否用一个可执行且可复现的联合响应分析，把 `1600.9-keV` 节点的 794-keV 宇称版本与 `881.8-keV` 混合比双根同时压缩到可辩护的候选集合？设计的目标是识别需要新增的观测和输入，不把既有相对强度、`R_DCO`、`Δ_PDCO` 或评估文件字段升级成事件级 L4 结果。

## Source lineage and object identity

| 对象 | 现有来源与定位 | 设计中如何使用 | 独立性边界 |
|---|---|---|---|
| 794.8-keV连接线 | Banik 2020 Table I：`1600.9(2) keV, 17/2+ → 15/2−`，E1，`Iγ=12.56(21)`, `R_DCO=0.55(1)`, `Δ_PDCO=+0.03(1)`；[[banik-2020-131xe-multiple-band-structures]] `BNK20-D28-2/3` | 目标线；重新做峰形、门条件和电子/γ共同归一 | 2020 的多处 E1 参照增强了标签的来源链，但不等于目标线的独立宇称测量 |
| 794.6/794.8-keV版本冲突 | Chakraborty 2023 将 `1600.9-keV` 标作 `17/2−`，并加入 766.5-keV 与 834.6-keV节点的连接；[[131xe-1601-parity-version-boundary]] | 将宇称版本作为互斥但可扩展的模型分支，保留对象身份不确定性 | 2023 明确重分析 2020 数据；不能把两篇论文计为两次采集 |
| 881.8-keV目标线 | Chakraborty 2023 Table I：`1046.0-keV 13/2− → 11/2−`，`R_DCO=0.64(11)`，偏振栏空；[[131xe-882-branch-response-contract]] `C23-D28-9` | 目标线；保留小正根与负 δ 分支的完整 profile | Fig.5 视觉交点不提供第二根的置信度、协方差或事件级计数 |
| 880.1-keV近邻/污染 | 现有 882 response contract 将其列为必须逐门建模的双线分量 | 峰形模板和污染强度同时拟合 | 不能把 880.1-keV 面积固定成常数或直接忽略 |
| 705/816/930-keV链 | Chakraborty 2023 Fig.1–2、`C23-1`；同源 2020 再分析 | 上游/下游身份与门拓扑控制；`816/930` 用于检验目标序列馈入 | 不能把同采集的再分析图表当独立验证 |
| 704.6-keV竞争退激 | Banik/Crosswalk 中的低自旋参考线 | 检查 1046 母态条件取向和门选择 | 只能作取向参考，不能强制作为 882 的互符合门 |

## Minimal observable contract

### A. 794-keV宇称块

最小目标是同一对象、同一 run 或可校准的重叠 run 中的：

1. `Nγ`：794.6/794.8-keV 峰的逐角度、逐门 γ 计数、峰窗和 sideband；
2. `Ne,K`：K 壳电子计数及电子能量窗、电子背景和时间窗；
3. `Ne,K/Nγ`：电子/γ 比的共同归一，以及 `K` 电子传输、固体角、γ 全能峰效率和死时间校正；
4. 多极性模型：E1、M1、E2，必要时 M2；统一 `Z=54`、能量、FO/NH、BrIcc 版本和内转换定义；
5. 反应/级联控制：同母态或同 acquisition 的已知 E1、E2 线，至少包含 642-keV 已知 E2 和重复作为 E1 参照的约 795-keV线；控制线只校准响应，不替代 794 目标的宇称观测。

目标量应写成共同响应下的预测：

\[
  \alpha_{K,\mathrm{obs}} =
  \frac{N_{e,K}/\epsilon_{e,K}}{N_{\gamma}/\epsilon_\gamma},
  \qquad
  \alpha_K(\delta)=
  \frac{\alpha_K(M1)+\delta^2\alpha_K(E2)}{1+\delta^2}
\]

混合式 ICC 只表示模型的条件前向关系；电子效率、γ效率、能量不确定度和理论共同协方差必须进入同一个 profile。历史 ENSDF `EKC=0.0017(7)` 仍是待核实验量，不能当作上述 `Ne,K` 的替代。

### B. 882-keV双根块

最小目标是同一 `1046.0-keV` 母态条件下的联合观测：

- 逐角度 γ 计数与真实 detector-pair acceptance；
- `R_DCO` 或 `R_ac` 的原始 numerator/denominator 计数，而不是只保留比值；
- 882 本线 Compton parallel/perpendicular scatter-bin 计数、未偏振响应 `Q_eff(E)` 或完整 Stokes 响应、轴符号和串扰；
- 881.8 与 880.1 的峰形、能量漂移、分辨函数和污染模板；
- `816/930` 上游门、随机门、sideband、663-keV或其它明确控制门的相同门逻辑；
- 1046 条件取向/feeding 的统计张量或密度矩阵、未观测馈入的参数化和退取向不确定度。

对每个观测 bin `i`，可用带污染模板的计数模型表示：

\[
 q_i(\delta,\eta)=
 \frac{a_i(\eta)+2b_i(\eta)\delta+c_i(\eta)\delta^2}{1+\delta^2},
 \qquad
 \mu_i=Y_g q_i(\delta,\eta)+B_i+\lambda_g T_{880,i}.
\]

其中 `η` 包含取向、feeding、角接受、效率、响应和门条件；`T880` 是逐门 880.1-keV 模板。`a_i,b_i,c_i` 必须由实际晶体/角对和有限几何积分得到，不能用名义 40°、90°、125° 代替。

### C. Shared calibration and joint covariance

统一建立校准参数向量 `κ`，至少包括：

- 能量增益、分辨、漂移和 794/880/882 峰分离；
- γ 全能峰效率、角接受、addback/抑制和 Compton 分析效率；
- K 电子效率、电子/γ时间窗、背景缩放和电子污染；
- 轴符号、`Q_eff`、串扰、阈值与无偏振源响应；
- deadtime/livetime、run 间归一和共同 acquisition overlap；
- 取向/feeding、sideband 和随机门的共享参数；
- BrIcc 名义系数、能量传播和理论 rank/多极性共同误差。

使用联合似然或等价的 profile likelihood 时，原始计数只能进入一次。若使用压缩后的 `R_DCO`、偏振不对称和 `EKC`，必须保留它们之间及与校准参数的联合 `Σ`；不能把原始计数和派生比值重复放入似然，也不能把同一 INGA 采集的 2020、2023、2022 理论比较当成三个独立数据集。

## Analysis sequence

1. 冻结 source manifest、run/time overlap、峰窗、sideband 和门拓扑；先以事件或互斥 bin 保存对象身份。
2. 用校准线和无偏振控制建立共同 `κ`；显式保存角对矩阵、效率矩阵、Compton response 和 K-electron response。
3. 先拟合 880.1 污染和峰形，再对 881.8 目标的角分布、DCO 和偏振联合 profile；把 feeding/alignment 作为 nuisance 参数。
4. 独立构造 794 的 E1/M1/E2/M2 响应预测，再与 882 块通过 shared `κ`、同 acquisition 和共同门条件连接。
5. 对宇称版本 `P_2020` 与 `P_2023` 分别 profile，不先用表格标签设定先验为 0 或 1；对 882 的小正根、负根和污染模型分别保留分支。
6. 只报告 profile 区间、分支相对支持和可复现的 posterior/profile 定义；没有原始计数或完整 `Σ` 时不报告 σ、Bayes factor、全局排除率或“已证实”。

## Negative controls and reverse tests

| 控制 | 目的 | 不能推出的结论 |
|---|---|---|
| 已知 642-keV E2 | 角接受、效率、取向传播 | 不能认证 794 的宇称 |
| 2020 重复使用的约 795-keV E1参照 | 电子/γ归一、E1响应 | 不能把参照线的 E1 标签转移给目标 |
| 704.6-keV同母态竞争退激 | 检查 1046 条件取向和 feeding 参数 | 不能强制其与 882 互符合 |
| 无偏振源/空门 | Compton 轴符号、随机背景、串扰 | 不能从一个总不对称量选择 δ 根 |
| 880.1 模板注入/留出 | 检查双线污染和峰形拟合 | 没有真实模板或 holdout 时不能声称双根已分离 |

## Three outcome scenarios and belief revision

| 结果情形 | belief revision | 允许的结论 |
|---|---|---|
| 794 的电子/γ比在共同响应 profile 后与 E1 预测分离，且 882 两根在留出门/角度中稳定分离 | 下调 `P_2020` 或小根简并，提升 `P_2023` 或指定 δ 分支的后验支持 | “在明确的响应、理论和门条件合同内排除候选”；可进入定向原件/复现实验核验 |
| 794 与 M1/E2 ICC 凸包重叠，或 882 两根在共同 profile 后仍交叠 | 保留宇称冲突和 δ 双根，不把低 `R_DCO` 或视觉交点升级成唯一解 | “数据对当前设计不足以裁决”；停在 L3/readiness |
| 差异由 880 污染、取向/feeding、轴符号、deadtime 或共享校准吸收 | 先修订对象/门/响应身份，再重评多极性和结构解释 | “谱学身份与响应合同优先于 wobbling/signature-partner 机制归因” |

## L3/readiness boundary

以下任一项缺失，最多保留 L3 设计和 readiness boundary：

- 没有 794 目标线的原始电子/γ计数、效率和共同归一；
- 没有 881.8/880.1 逐门峰形或双线模板；
- 没有真实 detector-pair acceptance、Compton response 或轴符号校准；
- 没有 1046 条件取向/feeding 输入，或把 704.6 参考线误当完整取向标定；
- 没有 acquisition overlap、deadtime/livetime、随机/sideband 信息；
- 只有表格比值而没有比值之间的联合协方差；
- 只有 ENSDF/评估字段、BrIcc 名义值或论文图像，没有目标线的 primary provenance；
- 只能用同一采集的 2020 与 2023 论文互相“验证”；
- 需要用代理计数、合成响应或未声明的 holdout 才能得到 L4 数字。

失败时不得生成 synthetic L4、Bayes factor、排除σ、全局 mixing-ratio CI、静态形状裁决或 wobbling 认证；应记录缺失输入、停止原因和下一条不重叠路线。

## Falsifier for the design itself

如果在真实响应矩阵、共同校准和合理 feeding nuisance 范围内，794 的候选宇称预测与 882 的两根在所有可获得的角度/偏振/转换观测上都保持重叠，那么“单次最小设计可稳健选根”的命题被否定，研究应转向新增独立 observable（例如更高统计的 K-electron measurement、明确的目标线偏振或独立 transfer/相邻级联约束）。如果能分离，结果只支持声明的实验/理论合同，不自动证明 wobbling、signature partner 或 γ-rigid 形变。

## Current status

- `131Xe` 两篇核心论文的 raw PDF 和 source pages 已入库，但 2023 是对 2020 INGA 数据的重分析；来源依赖已闭合到“同谱系、非独立实验”。
- 794-keV 原始内转换/电子响应和 Irving/Lönnroth 1979/1983 primary 全文仍未恢复；原始宇称版本保持未裁决。
- 882-keV 原始计数、880.1 峰形、Compton 响应、完整门拓扑和联合协方差仍缺；小正根与负根均保持可行候选。
- 本页是 Day29 正式研究设计资产，仍为 `provisional`、`unreviewed`；没有将设计条件写成实验事实。

### Primary source recovery boundary

`Irving 1979` 的书目身份为 A. D. Irving et al., *J. Phys. G* 5, 1595 (1979), DOI `10.1088/0305-4616/5/11/015`；`Lönnroth 1983` 为 T. Lönnroth et al., *Phys. Scr.* 27, 228–240 (1983), DOI `10.1088/0031-8949/27/4/002`。本轮核对了 NNDC 引用页和实验覆盖字段，但 IOP PDF 端点落到 Radware CAPTCHA，CORE/OA-only 检索没有取得可核原文。因此历史来源只进入书目/访问边界，不能把其目标线逐行 AD、ICC 或偏振数值写成已复核 primary。

本地 `Banik 2020` 与 `Chakraborty 2023` 原件足以支持 794.8-keV 版本冲突、881.8/880.1 双峰识别和门关系；后者明确是前者同一 INGA 数据的重分析。ENSDF adopted PDF 和 BrIcc 分别是评价资料与理论响应，不能增加独立实验权重。

## Sources and locators

- [[banik-2020-131xe-multiple-band-structures]] `BNK20-D28-2/3`, `BNK20-D28-3`, `BNK20-D28-1`
- [[chakraborty-2023-131xe-wobbling-origin]] `C23-1`–`C23-7`, `C23-D28-2`, `C23-D28-9`
- [[131xe-low-spin-partner-crosswalk]] object crosswalk and δ branch bounds
- [[131xe-882-branch-response-contract]] `C23-D28-9` and joint response equations
- [[131xe-1601-parity-version-boundary]] ICC/ENSDF boundary and BrIcc nominal envelope
- [[rose-brink-1967-phase-defined-angular-distributions]] `RB67-11`, `RB67-D23-001`, `RB67-D23-003`
- [[two-point-angular-correlation-ratio]] method inputs and geometry-transfer limits

## Human review

- Review status: `unreviewed`; this is Codex self-audit and research design, not `human-reviewed`.
- No experimental data, synthetic counts, or proxy L4 results were created.

## Research Trigger

Day29 requires an executable defense of the 794-keV parity-version conflict and the 882-keV
mixing-ratio double root while preserving source lineage and the L3/L4 evidence boundary.

## Grounded Evidence

The source lineage, object table, published observables, and primary-access boundary are recorded
above and linked to the Banik 2020 and Chakraborty 2023 source pages.

## Provisional Reasoning

The response contracts and belief-revision scenarios are design inferences conditioned on the
listed observables, detector response, feeding model, and covariance; they are not measurements.

## Assumptions

The design assumes that event-level or lossless compressed counts, calibration metadata, and
source identity can be recovered. It does not assume that any missing input exists.

## Competing Explanations

The active alternatives are a genuine parity reassignment, an inherited or misplaced label,
880-keV contamination, unresolved feeding/alignment, and an unresolved M1/E2 branch degeneracy.

## Transfer Conditions

The contract transfers to another line only when object identity, gate topology, detector response,
and shared covariance are re-established for that line; published ratios cannot be transplanted.

## Failure Conditions

Missing primary provenance, raw peak shapes, response calibration, feeding/alignment controls, or
joint covariance forces the result to remain L3/readiness and forbids synthetic L4 conclusions.

## Falsification or Reverse Tests

If the competing parity and δ branches remain overlapping after profiling the declared nuisance
space, the claim that this minimal design can select a branch is falsified.

## Open Questions

The unresolved inputs are the 1979/1983 primary full texts, 794-keV electron data, 881.8/880.1
event-level peak shapes, actual Compton response, and the complete acquisition-level covariance.

## Human Review

This page is `unreviewed`; all promotion decisions remain Codex self-audit and are not human review.

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | Day29 research-design writeback | worker/design preview | ai-draft research-note | Observable, response, covariance and readiness contract completed; primary/event inputs remain open | [[131xe-low-spin-partner-crosswalk]] |
