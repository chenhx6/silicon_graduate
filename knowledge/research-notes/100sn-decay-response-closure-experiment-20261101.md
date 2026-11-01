---
type: research-note
title: "`100Sn` B(GT) 联合响应闭合实验：endpoint、branching 与 isomer 的同一事件合同"
aliases: [100Sn decay response closure, 100Sn BGT joint response experiment]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hinke-2010-100sn-decay-spectroscopy, lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy, nndc-2026-logft-calculator-input-contract]
nuclei: [100sn, 100in]
observables: [half-life, endpoint-q, beta-positron-response, gamma-branching, gamma-gamma-closure, delayed-isomer-timing, b-gt]
methods: [radioactive-beam-decay-spectroscopy, implantation-decay-correlation, total-absorption-gamma-spectroscopy, positron-calorimetry, joint-likelihood]
tags: [100sn, gamow-teller, response-closure, branching, total-absorption, experiment-design, l3-readiness]
created_from: "2026-11-01 cross-mass candidate-pool rebuild and historical thesis reread"
---

# `100Sn` `B(GT)` 联合响应闭合实验

## Research Trigger

Hinke 2010 的 `HK10-5` 与 Lubos 2016 的 `LB16-2` 分别报告了依赖各自
single-state、Q/endpoint、branching 和 response 约定的 `B(GT)` 派生量。现有项目
已经把差异拆成 endpoint/Q、phase-space、branching、level scheme、detector response
和 model-space 层，但尚未把这些输入放进同一事件级响应合同。下一步最有信息量的问题
不是继续比较两个派生中心值，而是设计一次能同时约束母核半衰期、`100In`
分支、正电子响应、γ closure 和两个不同 `6+` 候选对象的实验。

## Grounded Evidence

| ID | Statement | claim_kind | locator | needs_review |
|---|---|---|---|---|
| SN100-EXP-1 | Hinke 2010 与 Lubos 2016 是不同 facility 和响应链的独立 `100Sn` 衰变实验；不能按论文版本重复计数，也不能在输入未统一前直接合并 `B(GT)`. | evidence-lineage | [[100sn-gamow-teller-independent-evidence]] Source Roles and Independence; HK10/LB16 source pages | true |
| SN100-EXP-2 | GSI 与 RIKEN 报告的 endpoint/Q、统计量、`100In` γ branching 和响应修正不同；两份 source 都把这些因素放在 `B(GT)` 提取链中。 | experimental-method-boundary | [[hinke-2010-100sn-decay-spectroscopy]] `HK10-3`–`HK10-8`; [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] `LB16-2`, `LB16-3`, `LB16-8` | true |
| SN100-EXP-3 | `100In` 的低能 γ 方案、γγ closure、约 `50 keV` link candidate 和 `100Sn` `6+` isomer timing 仍不是完全闭合的共同观测。 | evidence-boundary | HK10-4/HK10-6/HK10-7; LB16-3 | true |
| SN100-EXP-4 | 当前 LOGFT 计算器可在声明的 Q、半衰期和分支假设下重现中心量级，但这种控制计算不是新实验，也不能替代历史 raw response。 | calculator-control | [[nndc-2026-logft-calculator-input-contract]] `LOGFT26-3`–`LOGFT26-5` | true |

## Bold Hypothesis

**H1（强假设）：** 在同一套质量/endpoint 定义、`100In` branching、正电子/EC response
和共同 nuisance covariance 下，GSI 与 RIKEN 的表观 `B(GT)` 差异主要由输入与响应
链不同造成；统一后，母核 GT 约化矩阵元不需要引入额外的核结构分裂。

**H2（竞争假设）：** 即使共同响应和分支闭合，仍有不可忽略的残差，需要由 `100In`
低能级混合、未观测弱分支或 shell-model matrix-element distribution 解释。

**H3（结构性替代）：** `6+` isomer 或未识别的低能分支改变衰变链的时间/能量选择，
使“单一 `1+` 终态”近似失效。H3 只有在 delayed timing、γγ closure 和 branch-resolved
response 同时成立时才可被支持。

## Minimum Event Contract

最小事件记录应保留

$$
D=(D_{\mathrm{PID}},D_{\mathrm{implant}},D_{\beta},D_{\gamma},D_{\mathrm{time}}).
$$

- `D_PID`：入射/植入核素、TOF、能量损失、位置和污染概率；
- `D_implant`：植入像素、深度/能损代理、母核与子核空间关联、parent/daughter/
  isomer state identity 和 decay-generation 标签；
- `D_beta`：β/正电子能量、触发、pile-up、阈值、511-keV annihilation 关联和 bremsstrahlung 响应类别；
- `D_gamma`：γ 能量、晶体/分段、γγ/γγγ 关系、低能效率和 total-absorption response；
- `D_time`：母核衰变时间、γ 延迟时间、随机窗、deadtime、live-time、运行块、
  event/run/trigger ID、时钟版本和采集配置；
- `D_quality`：beam-on/off、质量门、veto、pile-up mask、channel status、energy/time
  calibration version 和每个 gate 的 live-time。

`B(GT)` 只在这个事件合同的联合似然之后作为派生量出现。不能先分别从两个端点
拟合得到 `B(GT)`，再把两个派生值当作独立原始观测。

## Experimental Design

首选架构沿用 RIKEN/BigRIPS–WAS3ABi–EURICA 的方法学链作为工程基准：束流 PID 与
植入—衰变像素关联、分段 Si 的 β/正电子响应、γ/γγ 高效率谱学和 list-mode
时间戳。若转移到 RIBLL 类平台，RIBLL 的 Br–ΔE–Br 纯化、焦平面 TOF/ΔE 和二级靶
架构只能作为 beam/PID 设计参考，不能直接当成 `100Sn` 产额或纯度保证。

申请前必须先锁定 implantation mode 或 secondary-target mode，并给出反应与束能、
charge state、磁刚度、slit/degrader、F2/F4 diagnostics、acceptance、束斑、rate、
purity、implantation geometry 和 detector compatibility；RIBLL1 的历史调束图不能
替代目标 `100Sn` 的产额/纯度验证。

首轮应同时采集：

1. 母核半衰期与母核—子核—孙核相关时间；
2. 正电子/β 能谱，包含低能阈值、511-keV、bremsstrahlung 和 conversion-electron
   响应控制；
3. `100In` 的 96、141、436、1297、2048-keV 候选 γ 线及其 γγ/γγγ closure；
4. 独立的 total-absorption 或近似总能量响应，用于搜寻未观测弱分支；
5. 分开采集两类延迟对象：`100Sn` 自身约 `3 MeV` γ 的 isomer search，以及
   `100In` 约 `50 keV` `5+→6+` link candidate；两者必须有独立 parent/daughter/state ID；
6. 一个邻近核素控制道，用已知 endpoint/branching 响应检验 β/γ 联合模拟。

### Joint Response Model

对每个运行块和 gate，期望计数可写成

$$
\mu_r=\ell_r
\sum_{b,k}
R^{\beta\gamma}_{r,b,k}(\text{PID},\text{geometry},\text{threshold},\text{pileup})
Y_{b,k}
B_r+C_r,
$$

其中 `b` 是 `100Sn→100In` 的绝对弱馈送终态，`k` 是响应类别，`R` 同时包含 β、γ、
时间和 correlation acceptance。另设 `g` 表示 `100In` 激发态的相对/绝对 γ cascade，
`d` 表示 `100In→100Cd` 的 daughter β/EC 成分。`Y_b`、`Y_{g|b}` 和 `Y_d` 使用不同
归一化分母，并以 missing-feed 约束共同连接；不能把相对 γ 强度直接当母核弱分支。
`B` 是连续背景，`C` 是随机/偶然符合。endpoint、EC/β+ 分额、branching、响应参数、
deadtime、daughter contribution 和未观测 feeding 进入共同 nuisance block；`f(Q,Z)`
和 `B(GT)` 的定义在同一 convention 下统一。

新实验的 `Cov_new` 必须拆成 response、branching、timing、daughter 和 background
blocks，声明 run 内共享项与 run 间独立项。历史 Hinke/RIKEN 若只有论文派生摘要，
只能作为外部约束；没有恢复历史 raw spectrum/response/Cov 之前，不做真正的两链
event-level joint fit。

## Controls and Falsifiers

- **Branching control：** γ singles、γγ、γγγ 和 total-absorption 的同一分支账必须
 互相一致；弱分支不能在模型中默认等于零。
- **Response control：** 用邻近核素和已知 β/γ 线检验低能阈值、511-keV、bremsstrahlung
 以及 total-absorption tail。
- **Timing control：** 分别为 `100Sn` isomer 和 `100In` link candidate 定义 parent、
  γ 能量门、`t=0`、prompt/random、寿命模型、搜索范围和 branch-specific sensitivity；
  早/晚时间窗和空植入像素只能作为控制，不能单独支持 H3。
- **Lineage control：** GSI 与 RIKEN 作为独立实验链保留；新实验的响应不能被写成
 对既有两条链的第三次独立复测，除非 acquisition identity 明确闭合。

三种结果的 belief revision：

1. **H1：** 新实验的 event-level profile 解释 endpoint、branching 和 response；
   若历史 raw/Cov 仍不可恢复，只能更新为“新测量支持输入/响应层假设”，不声称
   两条历史链已被同一 likelihood 完全解释，也不自动完成 GT quenching 裁决。
2. **H2：** 共同响应后仍有残差，且只在特定 `100In` 分支/低能级方案出现；更新为
   “level-scheme/branching 需要修订”，不把残差直接叫作内禀矩阵元变化。
3. **H3 或不可识别：** 指定 parent/daughter timing 或未观测分支改变拟合，或两模型在完整 nuisance
   profile 后仍重叠；保留结构性不可识别和 L3/readiness boundary。

## L3/L4 Stop Conditions

保持 L3/readiness 的条件包括：没有事件级 β/γ response、没有完整 `100In` branch
closure、没有共同 endpoint convention、没有 `6+` timing control、没有 deadtime/
daughter covariance，历史摘要被误当 raw response，或只能用 LOGFT 控制输出替代 raw spectrum。

只有在 response matrix、branching template、独立邻核控制、joint covariance 和
预注册 holdout 都可复核时，才可以进行 L4-level model comparison。无论结果如何，
不得生成代理事件数、合成效率、Bayes factor 或未声明的显著性。

## Provisional Reasoning

The joint response model is a design inference built from two independent source chains. It
tests whether the published `B(GT)` difference survives a shared endpoint, branching and
detector-response contract; it does not assume that H1 is true.

## Assumptions

- The new run can preserve event-level PID, implantation, beta/positron, gamma and timing
  records with run-level live-time information.
- A neighboring control channel can be selected whose endpoint and response are sufficiently
  constrained for calibration.
- Total-absorption or an equivalent closure observable can be made explicit in the proposal;
  no target efficiency or yield is assumed here.

## Competing Explanations

The active alternatives are input/response mismatch, unobserved `100In` feeding, a genuine
multi-state GT distribution, an unresolved delayed isomer, or a remaining model-space/
quenching convention difference. The same beta spectrum can be compatible with more than one
alternative until gamma closure and shared covariance are fitted.

## Transfer Conditions

The response-closure design transfers to another proton-rich decay only after redefining the
parent/daughter identity, endpoint convention, EC/β+ branches, gamma response, implantation
correlation and delayed-isomer controls for that nucleus. No `100Sn` endpoint or branching
parameter may be copied into another mass region. RIBLL/BigRIPS architecture also transfers
only after target-specific beam mode, charge state, optics, acceptance, rate, purity,
implantation geometry and detector compatibility are recalculated.

## Failure Conditions

Stop at readiness if the low-energy beta response, gamma branching, total-absorption tail,
daughter contribution, deadtime or delayed timing cannot be calibrated. A numerical LOGFT
output or a visible gamma line alone cannot promote the result to L4.

## Falsification or Reverse Tests

H1 is falsified if a common response and complete branch model cannot reproduce the two
independent chains while a resolved branch-specific residual persists. H2/H3 are weakened
if the residual disappears after gamma closure and timing controls. If H1 and H2 remain
response-folded indistinguishable, the correct result is non-identifiability and a new
companion observable is required.

## Knowledge Impact and Learning Decision

这条路线把 `100Sn` 从“两个 `B(GT)` 中心值的历史争议”改写为一个可执行的联合
response/branching 实验问题；它与 `132Sn` 两声子 doorway、`131Ba` 直接 E3 和
`131Xe` mixing-ratio 设计互不重叠。当前仍为 provisional L3 design inference，
没有新增实验数据或 L4 结果。

## Open Questions

- 哪一种 total-absorption/β-calorimetry 几何能在不牺牲植入 PID 的条件下覆盖低能
  分支和 511-keV response？
- `100In` 低能级方案中哪些 γγ 关系最能区分单终态与多分支 feeding？
- `6+` isomer 的 delayed-time search 应如何预注册 holdout，避免把早期少计数涨落当成
  timing evidence？

## Human Review

本页是 Codex self-audit，保持 `unreviewed`；所有历史 `B(GT)` 数值仍回到 source
locators，未提升为人工审阅或独立实验事实。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-01 | joint response-closure design | historical B(GT) comparison | provisional L3 research-note | endpoint, branching, beta/gamma response and isomer timing remain jointly unresolved | [[100sn-gamow-teller-independent-evidence]] |
