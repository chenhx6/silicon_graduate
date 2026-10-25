---
type: concept
title: 横向摇摆
aliases: [transverse wobbling, TW, transverse wobbling motion]
created: 2026-07-01
updated: 2026-07-03
status: active
review_status: unreviewed
concept_type: wobbling-subtype
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [wobbling, triaxiality]
---

# 横向摇摆（Transverse Wobbling）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

按 [[frauendorf-2024-wobbling-review]] 的拓扑分类，准粒子角动量和总角动量进动锥轴沿短轴或长轴，垂直于具有最大转动惯量的中轴。

## Necessary Assumptions

需要确定主轴、转动惯量排序和准粒子取向；仅凭 wobbling energy 下降不是充分定义。

[[lawrie-2020-tilted-precession-wobbling]] 的 frozen-`j` 推导还要求 transverse coupling 下另外两轴分量满足 `I1²+I3²<<I²`，即 Eq.34 的 `f(n,I)<<1`。这里 1 轴是在该文 irrotational-flow convention 中具有最大 MoI 的 intermediate axis（中轴）；core rotational angular momentum projection 通常沿该轴最大，因此作者认为典型 one-quasiparticle transverse configurations 很难满足该近似。

## Discriminating Observables

集体 interband E2、进动锥拓扑以及随自旋可能接近 instability 的演化。

## Supporting Evidence

[[matta-2015-transverse-wobbling-135pr]] 是当前首篇原始支持实验：作者用 `135Pr` side-to-yrast ΔI=1 transitions 的大 E2 fractions/正偏振，以及低自旋区下降的 `E_wob`，提出 transverse-wobbling 指认。

[[frauendorf-2018-beyond-unified-model]] supplies the framework: frozen high-`j` alignment along a short axis can change the favored solution from a signature-preserving `ΔI=2` rotation to a tilted `ΔI=1` band above a critical angular momentum. This is a model mechanism, not a stand-alone experimental assignment.

[[sensharma-2019-two-phonon-wobbling-135pr]] 在该指认上增加 second side band、TW2→TW1 的 E2-dominated links 与下降的 `E_wob(TW2)`，提出 two-phonon extension。它继承 Matta 的 `n_w=0/1` 前提，不作为独立重复证据计数。

## Counter-evidence and Competing Interpretations

signature partner 可表现出相似能量系统学；mixing ratio 的实验系统误差会直接影响判断。

`135Pr` 的指认存在后续争议，当前由 [[135pr-wobbling-controversy]] 分开记录支持与反对证据；本页不据单篇来源提升结论强度。

[[lv-2022-evidence-against-wobbling-135pr]] 报告关键 links 的 `abs(δ)<1` 与 M1-dominated character，并以 tilted precession/realignment 作为替代解释。

Lawrie 2020 把 QTR 的完整 3D solutions 解释为 [[tilted-precession-bands]]，并主张 QTR agreement 本身不足以建立 transverse wobbling；后者还需要 excitation energies 与 `B(E2)/B(M1)` ratios 的 phonon-number quantization。该理论判断不替代具体核素实验复核。

## Related Nuclei and Bands

- [[135pr-yrast-band]]
- [[135pr-side-band]]
- [[135pr-second-side-band]]

## Our Current Position

保留低置信度，暂不对具体核素作确认。

## Sources

- [[nomura-2022-questioning-wobbling-ibfm]]
- [[frauendorf-2024-wobbling-review]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[lawrie-2020-tilted-precession-wobbling]]
- [[frauendorf-2018-beyond-unified-model]]

## Evolution Log

- 2026-07-01（1 review）：建立拓扑定义，等待原始实验来源。
- 2026-07-03（1 review + 1 experiment）：加入 Matta 2015 支持证据，并保留争议状态。
- 2026-07-03（1 review + 2 experiments）：加入 Sensharma 2019 two-phonon 支持链及其 assignment 依赖。
- 2026-07-03（1 review + 3 experiments）：加入 Lv 2022 counter-evidence，保持争议未裁决。
- 2026-07-04：加入 Lawrie 2020 对 transverse one-quasiparticle wobbling approximation 的理论限制。
- 2026-09-20：加入 review-level frozen-alignment/symmetry-change mechanism and preserve experiment-specific evidence boundary。

## Day 21 Checkpoint 024 证据门量化审计：IBFM 替代解释与 M1 主导证伪准则

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint024_ibfm_low_spin_wobbling_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/ibfm-low-spin-wobbling-audit-024.json），对横向摇摆运动（Transverse Wobbling）的理论审查确立核心证据门规则：

1. **粒子—转子模型能级拟合的非排他性：**
   单凭 PRM 拟合再现低自旋能级序列不能作为刚性三轴或横向摇摆的排他性证明；基于平坦 gamma-软核芯的实验室系 IBFM-2 模型在完全相同的能量尺度下同样能够自洽再现能带谱学。
2. **带间多极性判定与摇摆证伪：**
   确证横向摇摆必须通过线偏振测量排他性锁定大模解（|delta| >> 1，E2 占绝对优势且 B(E2_out) >= 20–30 W.u.）。若实验测得小模解（|delta| < 1，M1 占优如 135Pr 实测 M1 88%），则横向摇摆假说被直接证伪，体系排他性归属于准粒子与 gamma-软核芯的振动/倾斜进动耦合态。


## Day22横向几何与声子有效域校准（checkpoint092）

[[frauendorf-2014-transverse-wobbling]] F14-D22-001/003定义j垂直最大惯量轴，并明确横向粒子频率可先升后降；HFA临界软化不直接代表完整QTR带合并。旧“全区唯一”及正常形变全面证伪撤回。

### Day 22 简谐小角有效域 $f(n,I)$ 对决核芯动量与关键跃迁伴随缺口审计（Checkpoint 034）

原034的数学充要认证与跨核固定数值不再使用。指定HFA/小角公式仍需按轴号、spin、惯量及参数域检验；完整波函数拓扑、能量阶梯和电磁观测各有独立限制。163Lu的476线有两根而未测偏振，属于具体实验边界，不是全区二声子已不存在的证明。见[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-R092-1/2。
