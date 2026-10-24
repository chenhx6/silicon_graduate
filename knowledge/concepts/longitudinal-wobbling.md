---
type: concept
title: 纵向摇摆
aliases: [longitudinal wobbling, LW, longitudinal wobbling motion]
created: 2026-07-01
updated: 2026-07-04
status: active
review_status: unreviewed
concept_type: wobbling-subtype
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [wobbling, triaxiality]
---

# 纵向摇摆（Longitudinal Wobbling）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

进动锥围绕最大转动惯量轴的 wobbling 拓扑；准粒子角动量可沿短轴、长轴或倾斜，而总角动量围绕中轴进动。

## Necessary Assumptions

必须由完整模型或角动量几何确认；“wobbling energy 随自旋增加”只是常见特征，不是独立充分条件。

## Discriminating Observables

collective interband E2、wobbling energy、SCS/SSS 角动量几何和微观模型一致性。

## Supporting Evidence

[[frauendorf-2024-wobbling-review]] 综述若干报道案例，但指出 LW 数量少于 TW。

[[sensharma-2020-longitudinal-wobbling-187au]] 是当前首篇摄入的原始支持实验：作者以 `187Au` 的 E2-rich LW→yrast links、M1-dominated SP→yrast links、增加的 `E_wobb` 与 PRM 比较提出 LW 指认。

## Counter-evidence and Competing Interpretations

[[guo-2022-low-spin-wobbling-187au]] 是当前 `187Au` counter-source：作者用联合 `R_ac-P` 得到 Band 2 links 的小 `abs(δ)` 解，并指出 `h9/2` proton Fermi surface 靠近 intruder subshell 底部，与其概括的 LW 需准质子位于 j-shell 中部的条件冲突。QTR 进一步支持 single-particle reinterpretation；这些仍是反方解释，不是最终裁决。

## Related Nuclei and Bands

- [[187au]]
- [[187au-longitudinal-wobbling-band]]
- [[187au-signature-partner-band]]

## Our Current Position

只建立概念框架，不把综述列举或任一方模型自动转成单核素确认。`E_wobb` 随自旋增加不能脱离 connecting-transition character、mixing-ratio branch 和角动量几何独立裁决 LW。

## Sources

- [[frauendorf-2024-wobbling-review]]
- [[sensharma-2020-longitudinal-wobbling-187au]]
- [[guo-2022-low-spin-wobbling-187au]]

## Evolution Log

- 2026-07-01（1 review）：建立拓扑定义与证据缺口。
- 2026-07-03（1 review + 1 experiment）：加入 Sensharma 2020 `187Au` LW 支持链，保持争议未裁决。
- 2026-07-04：加入 Guo 2022 的 M1-dominated links、j-shell 几何批评与 single-particle counter-interpretation。

## Day 21 Checkpoint 019 证据门量化审计：纵向摇摆（LW）推断阶梯与大模解排他性证伪准则

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint019_longitudinal_wobbling_187au_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/longitudinal-wobbling-187au-audit-019.json），对纵向摇摆（LW）的推断阶梯与实验判据确立核心证据门规则：

1. **角分布混合比双解简并与偏振排他准则：**
   Delta I = 1 带间跃迁的角分布对混合比 delta 存在天然双解（|delta| > 1 与 |delta| < 1）。在未测定康普顿散射线偏振不对称度（P）或内转换系数前，严禁仅凭模型偏好挑选大模解并据此计算出虚假的集体增强 B(E2_out)。187Au 案例表明，线偏振测量排他性锁定了小模解（delta approx -0.26），带间跃迁由 M1 主导（93%–94%），使 B(E2_out) 塌缩至 ~6.5 W.u.，彻底证伪低自旋纵向摇摆假说。
2. **费米面微观动力学禁戒准则：**
   纵向摇摆物理图景要求未配对准核子角动量沿中等转动惯量轴对齐，这仅在费米面位于高 j 子壳层中部（Omega approx 5/2 - 7/2）时在动力学上可能成立。若费米面位于子壳层底部（如 187Au 的 Omega = 1/2），单粒子角动量必然沿对称轴对齐，在几何上严格禁戒纵向摇摆运动。严禁将子壳层底部的单粒子科里奥利旋称劈裂误定为纵向摇摆声子。
3. **杂质反应道排查准则：**
   确证伴随旋称伙伴带必须经过独立的衰变谱学与反应道交叉检验，严禁将伴随反应产物（如 188Pt）的杂质能带指认为多带摇摆体系的组成部分。
