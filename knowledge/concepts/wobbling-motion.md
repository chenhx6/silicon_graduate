---
type: concept
title: 摇摆运动
aliases: [wobbling motion, nuclear wobbling, wobbling excitation, wobbling band]
created: 2026-07-01
updated: 2026-07-16
status: active
review_status: unreviewed
concept_type: rotational-collective-mode
confidence: medium
high_confirmed_by:
high_confirmed_date:
tags: [triaxiality, collective-motion, high-spin]
---

# 摇摆运动（Wobbling Motion）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

三轴转动体系中角动量相对本征主轴的进动型集体激发。存在准粒子时可按进动锥拓扑进一步分为 [[transverse-wobbling]]、[[longitudinal-wobbling]]，并可能经过 [[flip-mode]]。

## Necessary Assumptions

必须明确三轴形状、转动惯量排序、准粒子取向和 wobbling-phonon 带的对应关系。

[[guo-2022-low-spin-wobbling-187au]] 强调 wobbling phonon 是高自旋、小进动角下的 harmonic approximation。总角动量按 `J=j+R` 耦合；当最低态约为 `J=j+1`、即 collective angular momentum `R≈1ħ` 时，集体转动极慢，难以形成该近似所要求的高自旋小角进动。必须定量检验近似是否仍有效，不能把一般低自旋 precession 自动等同于 wobbling phonon。

[[lawrie-2020-tilted-precession-wobbling]] 进一步把一般 3D rotational/precessional bands 记为 [[tilted-precession-bands]]，并将 wobbling 限定为 `f(n,I)<<1` 时的 harmonic-phonon approximation。除小角条件外，wobbling bands 还应显示 excitation energies 和 interband transition probabilities 对 phonon number `n` 的量子化；一般 TiP bands 不要求这些特征。

## Discriminating Observables

- 相邻 n+1/n 候选带之间集体增强的 E2；
- wobbling energy 及其随自旋演化；
- 带内/带间 B(E2)、B(M1)；
- 与普通 [[signature-partner-bands]] 的比较；
- 模型中的角动量取向和进动锥。
- approximation-condition function 与 phonon-number quantization。

The 2026-07-16 experimental batch adds two important boundaries:

- `E_wob` rising or falling is model/configuration/spin-interval dependent and cannot be used alone; [[nandi-2020-multiple-transverse-wobbling-183au]] reports an increasing initial transverse branch.
- Predominant interband E2 is characteristic of many one-quasiparticle cases, but [[lv-2022-transverse-wobbling-136nd]] explicitly treats a two-quasiparticle candidate with an M1-dominated 751-keV link.

## Supporting Evidence

[[frauendorf-2024-wobbling-review]] 把集体增强 interband E2 作为核心实验标志。

[[frauendorf-2018-beyond-unified-model]] gives the rotating-mean-field distinction between simple harmonic wobbling and transverse wobbling: the former is precession about the largest-moment axis, while a high-`j` aligned quasiparticle can drive a symmetry change and tilted `ΔI=1` sequence. The review-level equations do not replace nucleus-specific lifetimes and transition data.

[[matta-2015-transverse-wobbling-135pr]] 报告 `135Pr` 候选带间 ΔI=1 transitions 的较大 E2 fractions 与正 polarization asymmetry，并由此提出 zero-/one-phonon wobbling pair。

[[odegard-2001-evidence-wobbling-163lu]] provides the high-spin benchmark with polarization-selected E2-dominated links. [[timar-2019-transverse-wobbling-105pd]], [[biswas-2019-longitudinal-wobbling-133la]] and [[mukherjee-2023-transverse-wobbling-151eu]] extend the link-character paradigm to normal-deformed cases with different model interpretations.

## Counter-evidence and Competing Interpretations

[[chakraborty-2023-131xe-wobbling-origin]] 中，新序列的 ΔI=1 连接跃迁几乎为 M1，因而支持 signature partner 而非 wobbling。

[[domscheit-1999-triaxial-superdeformation-163lu]] 曾把 `163Lu` SD2 提为 wobbling 的可能解释，但 SD1-SD2 linking transitions 及其多极性未能建立。该文因此是“相近转动惯量与模型三轴形变仍不足以识别 wobbling”的非 A≈130 限制案例。

[[guo-2022-low-spin-wobbling-187au]] 对 Sensharma 2020 的 `187Au` Band 2 links 得到 M1-dominated 小 `abs(δ)` 解，并用 QTR 提出 single-particle excitation；作者同时把 β/γ vibration 与 tilted precession 列为低自旋替代机制。该反方解释与支持方并列保留。

Lawrie 2020 的 QTR/TiP comparison 显示 TiP bands 也可有 large mixing ratios 与增强 unstretched E2 links，因此 E2-dominated connecting transitions 是必要判据之一，但不单独证明 wobbling phonon nature。

## Related Nuclei and Bands

当前已建立 `135Pr` 双方证据、`131Xe` 反例链、`187Au` LW/single-particle 争议，并加入 [[163lu]] SD2 的未决原始实验案例。

## Our Current Position

三轴形变是 wobbling 的背景条件，不是充分证据；能量系统学必须与电磁跃迁共同使用。低自旋下还必须说明 wobbling approximation 的有效区间，并排除可产生类似 E2 links 的其他集体或单粒子机制。

## Sources

- [[odegard-2001-evidence-wobbling-163lu]]
- [[jensen-2002-second-phonon-wobbling-163lu]]
- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[domscheit-1999-triaxial-superdeformation-163lu]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[lawrie-2020-tilted-precession-wobbling]]
- [[experimental-wobbling-evidence-strength-map]]
- [[frauendorf-2018-beyond-unified-model]]

## Evolution Log

- 2026-07-01（2 sources）：建立综述判据，并加入 `131Xe` 的反证案例。
- 2026-07-03（3 sources）：加入 `163Lu` SD2；缺少 linking-transition 多极性时保留 wobbling 为推测。
- 2026-07-03（4 sources）：加入 Matta 2015 的 `135Pr` 原始支持证据，不裁决后续争议。
- 2026-07-04：加入 Guo 2022 对低自旋 wobbling approximation、mixing-ratio 范式与替代机制的批评。
- 2026-07-04：加入 Lawrie 2020 的 TiP/3D rotation、`f(n,I)<<1` 与 phonon-quantization 边界。
- 2026-09-20：加入 Frauendorf 2018 的 harmonic/transverse wobbling framework、symmetry-change and semiclassical limits。

## Day 21 Checkpoint 023 证据门量化审计：多声子摆动激发判定准则与双解排他性门限

124撤回本节旧科学认证与自设阈值；旧全文保存在superseded-124，原review/flags保持。



## Day21 checkpoint124：条件证据与量词纠正

[[matta-2015-transverse-wobbling-135pr]] M15-D20-R146-1保原支持方真实INGA偏振；[[lv-2022-evidence-against-wobbling-135pr]] L22-D20-R146-1保新联合分析与TiP解释。两次采集不是同一次拟合的大小两根；偏振也不保证所有实验唯一选根，不设置20–30W.u.普适门。

## Day22：几何、声子与观测对象的分层

[[wobbling-geometry-phonon-observable-contract]]给出可复用的轴映射、HFA有效域、有限自旋模型控制和四列观测检查。[[frauendorf-2014-transverse-wobbling]] F14-D22-001/003以j相对最大惯量轴定义横纵，横向曲线可以先升后降；F14-D22-002/004保留小角近似临界失效与完整QTR重定向边界。[[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-002更正旧页对固定Ak模型复现能量趋势的过强描述。以上是本次Codex self-audit，未改原human-review/needs_review状态。

## Day22偶偶核追加裁决撤回（checkpoint092）

旧040把751 keV的M1占优当所有wobbling的排他否证，并把未匹配的寿命表映射至L1/L3，结论撤回。[[lv-2022-transverse-wobbling-136nd]] LV22-D22-R091-1/2与[[chen-2019-transverse-wobbling-even-even]] CH19-D22-R091-1/2均保留两准粒子TW支持解释及其单点/模型边界。不能据这些模型已被支持就反向称模式无争议确证。


## Day22 模式与谐近似的定义分歧（checkpoint093）

[[lawrie-2020-tilted-precession-wobbling]] LAW20-D22-R093-1以谐声子近似定义wobbling，并把一般完整转动解称TiP；[[chen-2022-study-wobbling-spin-coherent-state-maps]] CF22-D22-R093-1则用wobbling表述完整PTR进动拓扑，容许非谐性。判断需写清讨论哪一种意义，避免用前者的近似有效域直接否定后者的术语。两种叫法本身不能代替实验δ、寿命和竞争模型检验。

## Day22 checkpoint109：声子代数是局部近似，基占据不等声子标签

以通常spin约定`[J1,J2]=iJ3`作任务代数练习，定义`nK=I−m`、`b=J+/√(2I)`。精确有`[b,b†]=J3/I=1−nK/I`及`abs(⟨nK−1|b|nK⟩)²=nK[1−(nK−1)/(2I)]`。有限矩阵任意commutator的trace为0，故不能在整个有限spin空间精确等于单位阵；低占据局部仍可近似boson。这一全局事实并不否定核内有效phonon。

I=13/2时，b的2→1/1→0平方矩阵元比为1.84615；I=45/2时为1.95556。四组矩阵控制验证对易式、trace和有限ladder修正，最大误差约浮点舍入。这是单一I表示内的scaledJ矩阵元，**不是**跨I核E2跃迁或实测二声子B的修正公式。

nK不是自动等于Bogoliubov对角化后的wobblingphonon数nw；映射还受挤压/非谐项和算符影响。体固总J的对易号须按[[frauendorf-2014-transverse-wobbling]]的约定映射；本练习不直接迁移相位或电磁算符。[[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-002/004的有限I非谐性和F14-D22-R106-1/2的临界四次项说明应分别核能量阶梯、局部代数与真实跃迁强度，不设统一数值有效门。needs_review: true。
