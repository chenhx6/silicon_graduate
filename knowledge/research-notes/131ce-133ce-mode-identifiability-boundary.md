---
type: research-note
title: "`131Ce/133Ce` 集体模式判别的可识别性边界"
aliases: [131Ce 133Ce mode identifiability boundary, A130 collective-mode decision boundary]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [alwaleedi-2013-band-structures-131ce, li-2004-lifetimes-131ce, ding-2021-131ba-133ce-signature-splitting]
created_from: "Day31 post-Day28 full-library review"
promotion_target: "131ce-collective-mode-discrimination"
scope: a130/131ce/133ce/mode-identifiability
nuclei: [131ce, 133ce, 131ba]
observables: [mixing-ratio, linear-polarization, lifetime, b-e2, b-m1, signature-splitting, alignment]
tags: [131ce, 133ce, mode-discrimination, evidence-boundary, paper-prospectus]
---

# `131Ce/133Ce` 集体模式判别的可识别性边界

## Research Trigger

全库复习显示，`131Ce/133Ce` 的现有证据已经足以构造竞争解释矩阵，但还不足以把 signature/configuration coupling、γ-soft particle-core response、wobbling、chirality 和 shape coexistence 唯一排序。本页把“什么观测量能改变排序”压缩成可复用 decision boundary，避免继续堆叠同一类能级或模型 γ 数值。

## Grounded Evidence

| Evidence layer | What is available | Exact source locator | Boundary |
|---|---|---|---|
| `131Ce` band and branch ledger | Bands 1–7、crossing/alignment、组态映射；部分 interband links 逐表闭合 | [[alwaleedi-2013-band-structures-131ce]] `AW13-8`, `AW13-14`–`AW13-22` | `δ=0` 假设，缺 measured polarization、寿命和 absolute `B` |
| `131Ce` derived strength | `B(M1)/B(E2)` 由分支强度和能量推导 | 同source `AW13-9` | 不是绝对 `B(E2)`/`B(M1)`，且依赖未测 mixing ratio |
| `131Ce` lifetime/Qt controls | 正负宇称序列存在独立寿命与 `Q_t` 量级差异 | [[li-2004-lifetimes-131ce]] `LI04-1`–`LI04-5` | 覆盖带与 AW13 Bands 1–7 不完全一致，不能直接当 partner matrix |
| `N=75` signature splitting | `131Ba/133Ce` band 2 的强耦合和 splitting，模型分别改变 γ 与 Coriolis attenuation | [[ding-2021-131ba-133ce-signature-splitting]] `D21-1`–`D21-9` | `S(I)` 不是 γ 的唯一测量；三核比较含旧实验汇编 |

### `131Ce` connection ledger

| Branch family | Transition rows | What can be used | What cannot be inferred |
|---|---|---|---|
| Band 1 → Band 4 mixed links | `504.9 keV` (`25/2−→23/2−`), `538.3 keV` (`15/2−→13/2−`), `611.1 keV` (`17/2−→15/2−`) | exact endpoint/energy and mixed M1/E2 label for a future line-level response analysis | no measured `δ`, polarization or absolute branch covariance; `611.1` must not be confused with the same-spin intraband `243.7 keV` row |
| Band 1/4 E2 links | `871.2 keV` (`19/2−→15/2−`), `994.3 keV` (`19/2−→15/2−`), `1108 keV` (`23/2−→19/2−`) | candidate same-parent comparisons after direction and band identity are frozen | a common final state or common parent does not make the three rows one independent observable |
| Intraband references | `641.2 keV` Band 1, `625.8 keV` and `755.6 keV` Band 4 | possible reference branches for a declared conditional out/in calculation | without `δ`, lifetime and shared response, a conditional intensity ratio is not absolute `B(E2)` |

Exact source anchors: [[alwaleedi-2013-band-structures-131ce]] `AW13-16`, `AW13-19`, `AW13-20`, `AW13-21`, `AW13-22`. The ledger is an identity scaffold, not a completed likelihood.

## 2026-10-31 Companion-Observable Audit

本轮对子页和 source lineage 的复核没有发现新的、独立且能关闭目标核
`δ–polarization–τ–absolute EM` 矩阵的 primary；但将当前证据分层进一步冻结：

| 对象 | 可安全使用 | 仍缺失/不得推断 |
|---|---|---|
| `131Ce` Bands 1–7 | AW13 的 crossing、alignment、相对强度、端点和原文组态标签；`504.9/538.3/611.1/871.2/994.3/1108 keV` 的候选 line ledger | AW13 的 `δ=0` 是派生假设；没有逐线 signed `δ`、偏振、partner-resolved lifetime 或绝对 `B(E2)/B(M1)` |
| `131Ce` Band-1-like / parity controls | Li 2004 与 Singh 2016 的 family-level lifetime/`Q_t` controls | 这些点覆盖不同带/实验，不能无条件接到 AW13 Band 4 或逐线 mixed links；Singh 表中的 Li 行不计为第三个独立测量 |
| `131Ce` independent HD band | Petrache 1998 的 `Q_0=7.3(4) eb` 证明同核存在另一形变尺度 | 缺 HD–ND linking、decay-out、E0/invariant 或共同配置证据，不能宣称 AW13 Bands 1–7 已证实 shape coexistence |
| `133Ce` A13/A16 candidate bands | 相对谱学指纹、同宇称 links、`S(I)`、DCO/角分布与作者模型 | A13 candidate-band lifetime 和 absolute transition probabilities缺失；A13/A16 有共享或继承 Gammasphere lineage，不能按两篇论文计独立确认 |
| `133Ce` Emediato/Joss clocks | 特定低/中自旋和高自旋态的 lifetime/`Q_t` 可作为独立控制 | 不能迁移到 A13 candidate bands 或现代低自旋 Band 4；没有共同 partner matrix |

### Minimal holdout update

若未来取得 AW13 同谱系或新测量的逐线 `δ`、偏振和寿命，可预先冻结：

> 用能级、`S(I)`、三条 mixed links 的 measured `δ`/polarization 和部分
> partner-resolved lifetime 进行模型比较；将 Band 4 `23/2−` 母态的
> `1108-keV` E2 branch 与同母态 `755.6-keV` Band-4 in-band E2 reference
> 的 absolute `B(E2)_out/B(E2)_in` 留作未参与调参的 holdout。

该 holdout 目前仍是设计项。若结果显示普通 M1/E2 signature-link 行为而不是
增强的 out-of-band E2，wobbling ranking 应下降；若显示稳定 E2-rich partner
coupling，则重新排序 signature/configuration、γ-soft、wobbling 和 chirality。
在 raw response、feeding、效率和联合 covariance 缺失时，不生成代理 L4 likelihood。

## Provisional Reasoning

### Decision boundary

| Hypothesis | Required observable bundle | Current status |
|---|---|---|
| signature/configuration coupling | 同组态 signature 序列、crossing/alignment、逐线端点和普通 mixed M1/E2 links | `131Ce` 当前最节约假设；AW13 组态/交叉链较完整 |
| γ-soft particle-core response | 多带寿命/`Q_t`、同一模型参数对多个带的联合描述、形变敏感 companion observable | 可行但主要是模型辅助；AW13 `δ=0` 和少数 `Q_t` 不足以闭合 |
| wobbling | 明确 phonon/partner identity、增强 ΔI=1 out-of-band E2、`B(E2)out/B(E2)in`、可靠 `δ`/偏振和 `E_wob` | `131Ce` 未闭合；邻核机制可行性不能替代目标核证据 |
| chirality | 同组态近简并双带、相似 intraband `B(M1)/B(E2)`、interband transitions、寿命和几何一致性 | `133Ce` 有候选链；`131Ce` 当前没有同等 partner-resolved 闭合 |
| shape coexistence | 不同带的绝对 `Q_t`/电磁不变量、HD–ND linking、配置或 decay-out 证据 | `131Ce` 同核 HD 尺度存在，但与 AW13 Bands 1–7 的共存关系未建立 |

关键可识别性结论：`AW13-9` 的 `δ=0` 只定义了一个派生强度合同；`LI04-1`–`LI04-5` 的寿命/`Q_t` 只约束相应带的 E2 集体性；`D21-4`–`D21-7` 的 γ/PES 是模型结果。三者不能互相替代，也不能合并为“已测三轴形状”。

### Minimum discriminating measurement

在现有缺口中，信息增益最高的最小测量组合是：

1. 对 AW13 已列出的 `504.9/538.3/611.1/871.2/994.3/1108 keV` 连接线逐线取得 mixing ratio 和线偏振；
2. 对同一 Bands 1–7 网络取得 partner-resolved lifetime、绝对 `B(E2)`/`B(M1)` 或等价 `Q_t`；
3. 用共同 gate、feeding、效率和联合 covariance 绑定 line identity；
4. 用未参与主模式排序的 holdout（g factor、quadrupole invariant、HD–ND linking 或独立寿命）检查竞争解释。

若只有能级、`S(I)` 或模型 γ，正式结论只能停在 L3 compatibility；不能升级到 L4 mode identification。

## Assumptions

各来源的能带和跃迁身份只在各自 source 的反应、门和版本范围内使用；不同论文和同源再分析不按论文数量重复计票。`B(M1)/B(E2)` 若由同一寿命/分支派生，不能与其输入作为独立证据重复投票。

## Competing Explanations

同一 signature splitting 可由非轴性、低-j Coriolis mixing、组态变化或模型 attenuation 共同生成；同一近简并能级也可来自 crossing、γ-softness、chirality 或 shape coexistence。没有逐线 `δ`、绝对强度和寿命时，不能把模式标签写成实验事实。

## Transfer Conditions

本 decision boundary 可迁移到 A≈130 的其它 odd-A 多带系统，但每个核素必须重新绑定反应、state identity、response、feeding 和 source lineage。不能把 `131Ce` 的模型 γ、`Q_t` 或寿命直接借给 `133Ce`、`131Ba` 或 `131Xe`。

## Failure Conditions

若连接线端点未闭合、`δ` 仅由 `δ=0` 假设产生、寿命和图点共享未知协方差、或模型使用数据调参后没有 holdout，则只能报告 compatibility/readiness boundary。缺 raw response 或 joint covariance 时不得生成代理 L4 likelihood。

## Falsification or Reverse Tests

若同一 `131Ce` link network 的 measured `δ`/偏振显示普通 M1/E2 signature links 且不存在 enhanced out-of-band E2，可削弱 wobbling；若 partner-resolved absolute strengths 与寿命在同一 state mapping 下支持另一组态或 HD–ND linking，则应重排 signature/configuration 与 shape-coexistence 的优先级。若不同模型在同一 observable bundle 上都能通过，模式仍不可识别。

## Open Questions

- `131Ce` AW13 的六条关键连接线能否取得同一实验谱系的 `δ`、偏振和寿命？
- `133Ce` 候选双带的缺失寿命是否会改变 chirality ranking？
- `131Ba/133Ce` 的 `S(I)` 与 `B(M1)/B(E2)` 是否能在共同 QTR/CSM 参数合同下区分 γ 与低-j Coriolis？
- `131Ce` HD 带与 AW13 normal-deformed Bands 1–7 是否存在可定位的 linking/decay-out 证据？

## Human Review

本页是 Codex self-audit，`review_status: unreviewed`、`reasoning_status: provisional`。它是研究设计和证据门页面，不是新的实验结果或模式裁决。

## Knowledge Impact and Learning Decision

`supports`：把 `131Ce/133Ce` 的已有谱学、寿命和模型页统一成 observable bundle 与 stop rule。

`limits`：现有 `131Ce` 证据仍不能唯一区分 signature/configuration、γ-soft、wobbling、chirality 和 shape coexistence；新增主张必须回到逐线 response/寿命/绝对强度。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | full-library post-Day28 review | none | provisional | QMD cross-links and existing source locators support a decision-boundary synthesis; target-line companion observables remain missing | [[131ce-collective-mode-discrimination]] |
