---
type: research-note
title: "锕系奇-A核宇称双重态的内禀磁矩、自旋极化与单粒子g因子淬灭"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [actinide parity-doublet magnetic moments, odd-A actinide g-factor quenching, 锕系宇称双重态磁矩]
tags: [actinides, parity-doublets, magnetic-moments, g-factors, octupole-deformation]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 L3 research task: actinide parity-doublet magnetic moments and spin polarization"
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra, nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet]
---

# 锕系奇-A核宇称双重态的内禀磁矩、自旋极化与单粒子 g 因子淬灭

## Research Trigger

本轮问题要求把 `223Ra`、`225Ra`、`225Ac` 和 `227Ac` 的奇 A 宇称伙伴、静态磁矩、
`B(M1)`、Coriolis 解耦和八极混合放入同一套证据账本，并构造一份可复现的
Nilsson-like `β3` 灵敏度模型。这里最重要的研究边界是：低能异宇称伙伴和静态磁矩
并不自动等于已测得的伙伴间 `B(M1)`，而评价数据中的括号 `Jπ` 也不等于原始实验确证。

## Grounded Evidence

### 1. 能级与静态磁矩

| 核素 | 评价/汇编的低能宇称信息 | 静态磁矩证据 | 证据层与限制 |
|---|---|---|---|
| `225Ra` | Adopted `1/2+` 基态；`1/2−` 位于 `55.16(6) keV`，另有 `3/2−` 31.56 keV、`7/2−` 69.36 keV。 | ENSDF 基态 `MOMM1=-0.7338(15) μ_N`，来自激光谱学。[[nndc-2009-ra225-adopted-parity-doublet]] | 伙伴 Jπ 中部分为括号；这是评价值，不是本轮重新测量。原 ENSDF 字段见 `225088001` L71–81。 |
| `223Ra` | `K=3/2` 带的 `3/2−` 50.128 keV、`5/2−` 79.708 keV、`7/2−` 123.793 keV、`9/2−` 174.569 keV、`11/2−` 247.39 keV 及对应正宇称带。 | Stone 汇编列 `μ=+0.271(2) μ_N`，另列依赖不同参考标准的 `+1.21(3)`、`+1.25(7)` 等重评结果。Stone (2014) | `+0.271` 与 `+1.21` 不能静默平均；需要回查 CFBLS 和参考标准。 |
| `227Ac` | 本轮未取得可用于同一 `K` 双重态逐带配对的完整 ENSDF 原件。 | Stone 汇编列基态 `Iπ=3/2−` 的 `μ=+1.1(1) μ_N`，另列 `+1.7(2)` 重评。Stone (2014) | 两值是原始/重评层，不是两次独立测量；不能据此填充 `B(M1)`。 |
| `225Ac` | Adopted 基态 `(3/2−)`；`(3/2+)` 在 `40.10(4) keV`，40.09-keV E1 的评价值 `B(E1)=0.00171(15) W.u.`。[[nndc-2022-ac225-adopted-parity-doublet]] | 本轮检索的 Stone 2014 汇编未列 `225Ac` 基态静态 μ；未找到状态分辨 μ/g 或伙伴 `B(M1)` 的直接记录。 | “未列”是证据缺口，不能写成 μ=0；多数 Jπ 为括号，A–D 带归属是评价/系统学。 |

### 2. 可直接提取的 `B(M1)`

目前可定位的逐跃迁绝对 `B(M1)` 来自 `223Ra` `K=3/2` 带的寿命分析，而不是
`225Ra` 或 `225Ac` 的伙伴态磁矩测量。Kurcewicz *et al.* 的 Table 1（EPJ A 52,
172 (2016), PDF pp.5–6）给出（单位 `μ_N²`）：

| 初态 → 末态 | 多极性 | 实验 `B(M1)` |
|---|---|---:|
| `5/2+ (29.858) → 3/2+` | M1 | `>3.7×10^-3` |
| `7/2+ (61.424) → 5/2+` | M1 | `4.1(15)×10^-3` |
| `5/2− (79.708) → 3/2−` | M1 | `1.12(7)×10^-2` |
| `7/2− (123.793) → 5/2−` | M1 | `5.9(20)×10^-3` |
| `9/2− (174.569) → 7/2−` | M1 | `1.71(93)×10^-2` |
| `11/2+ (174.58) → 9/2+` | M1 | `≈2.7×10^-2` |
| `11/2− (247.39) → 9/2−` | M1 | `4.0(33)×10^-2` |

这些是带内 M1 率；它们不能被改写为正负宇称伙伴之间的 M1 率。[Kurcewicz 2016 source page](../sources/kurcewicz-2016-223ra-enhanced-e1.md:35)
`225Ra` ENSDF
低能表确实列出若干 M1 或 M1+E2 多极性和 Weisskopf 估计/上限，但缺少能把
`55.16-keV 1/2−` 与 `1/2+` 基态支线转换为可靠绝对 `B(M1)` 的完整寿命与分支账本。
`225Ac` 评价表同样给出 40.09-keV E1 和若干 M1 标签，却没有逐线寿命支持的伙伴
`B(M1)`。因此本笔记对后三核素明确标记 `B(M1)` 为缺口，而不补写猜测值。

### 3. 八极混合、`g_K` 分岔与历史模型锚点

Butler–Nazarewicz 综述把八极不稳定性与费米面附近相反宇称、`Δl=Δj=3` 轨道对联系
起来，并强调 E1 对质子—中子电荷质心相消敏感、E3 更集体。[Butler–Nazarewicz
source page](../sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry.md:63)
同时要求分开静态八极极小、软振动、隧穿和宇称恢复。

在强耦合转子中，带内磁矩采用

$$
\mu(I,K)=\frac{I}{I+1}\left[g_R I+(g_K-g_R)\frac{K^2}{I}\right],
$$

并在 `K=1/2` 时加入 Coriolis 解耦项 `b_0`（或文献相位约定中的 `a`）。标准
强耦合写法常把第一项写作 `g_R I`；本笔记保留用户指定的式子，同时在工件中把
“requested formula”和“standard formula”分列，避免两个约定被混为一个实验量。

八极反射不对称使内禀轨道不再是单一宇称：

$$
|K,+\rangle=\sum_{lj}c_{lj}(\beta_3)|nljK\rangle,\qquad
|K,-\rangle=\sum_{l'j'}d_{l'j'}(\beta_3)|n'l'j'K\rangle .
$$

`g_K` 是磁偶极算符在这些混合波函数上的期望值；由于中子 `g_l≈0` 而
`g_s` 很大且为负、质子又有 `g_l=1`，不同 `l,j` 成分的重排可以令 `g_K+` 与
`g_K−` 分叉。该分叉是模型可检验量，不是从低能隙单独读出的实验事实。

Ragnarsson 1983 的直接模型比较是一个历史锚点：论文引用 `μ(225Ra)≈−0.74 μ_N`、
`μ(227Ra)≈−0.40 μ_N`，使用 `g_s=0.6g_s^free`、`g_R=0.388`，并发现
`ε3≈0.10` 附近的 `[631 1/2]` 分支可同时接近 `225Ra` 的解耦参数 `a≈1.4` 和磁矩。
这支持“磁矩+解耦参数比单一能级差更有区分力”的模型判断，但不能替代现代
blocked-HFB/宇称投影或 `225Ac` 的直接磁矩实验。[Ragnarsson source page](../sources/ragnarsson-1983-ra225-ra227-magnetic-moment.md:44)

## Provisional Reasoning

### 自旋极化与有效 `g_s`

在壳模型/准粒子描述中，残余相互作用、粒子—声子组态混合、配对和核芯的自旋—轨道
响应会把自由核子自旋算符重整化为有效算符。常见的现象学敏感度范围

$$g_s^{\rm eff}/g_s^{\rm free}\simeq0.65\text{--}0.75$$

可作为扫描区间；本工件中心值取 `0.70`。这是一般核结构模型先验和本轮敏感度假设，
不是 `225Ra` 或 `225Ac` 的新测量。它会压低单粒子 Schmidt 极限的自旋贡献，但不保证
最终 `μ` 必然变小，因为 `g_l`、Coriolis 退耦、核芯转动和组态相消可能改变符号和幅度。

### 对 `225Ra` 的数量级比较

`225Ra` 基态的实验 `g=μ/I=-1.4676(30)`，远离把一个纯球形 `i13/2` 中子直接代入
Schmidt 极限的结果。一个仅含 `l=6,j=13/2` 的自由单粒子估算给
`g_j≈g_s^free/(2l+1)≈−0.294`；采用 `q_s=0.70` 后约为 `−0.206`。这个对比只说明
“纯单粒子极限不够”，不能把差值全部归因于八极形变：`g_K` 的定义、强耦合投影、
`b_0`、Coriolis 和核芯极化都必须同时计算。

本轮脚本让 `β3` 在 0–0.16 扫描，在 `g_s^eff/g_s^free=0.70` 下输出正/负宇称主导分支
的 `g_K`、奇偶宇称权重、`b_0` 代理和两种转子磁矩公式。工件是可复现的机制图，不是
对 `225Ra` 的参数拟合；它故意保留与实验 `−0.7338(15) μ_N` 的偏差，避免把 toy
模型校准结果冒充 blocked-Nilsson 预测。

## Assumptions

1. `K=1/2`、轴对称强耦合和固定 `g_R=Z/A` 只用于展示公式；`225Ac` 的评价低能伙伴是
   `K=3/2` 候选，不能直接套用 `K=1/2` 的 `b_0`。
2. 四轨道基底使用 `νi13/2, νg9/2, νj15/2, νf7/2` 作为 `Δl=Δj=3` 代表；能量和耦合
   是显式 toy 输入，不是从目标核的自洽势能面提取。
3. `q_s=0.70` 是有效算符扫描中心；`0.65–0.75` 仅作灵敏度范围。
4. Stone/ENSDF 数值是评价或编译对象；原始激光、CFBLS、光学取向论文尚未逐篇复核。

## Competing Explanations

- 低能异宇称态可能由静态八极双阱、八极软振动、粒子—声子耦合、偶然能级靠近或
  组态混合产生。
- 磁矩偏离 Schmidt 极限可能由 `g_s` 淬灭、Coriolis 退耦、核芯转动、时间奇配对场、
  质子轨道项和多准粒子混合共同造成；不能把全部偏差归因于 `β3`。
- `225Ra` 的 55.16-keV `1/2−` 伙伴与 `225Ac` 的 40.10-keV `3/2+` 伙伴不构成自动
  同一双重态序列；`225Ac` 存在多条同自旋候选带，必须保留带标签。
- `223Ra` 的 `B(M1)` 表是 `K=3/2` 带内率，不能替代 `225Ra` 或 `225Ac` 的伙伴间率。

## Transfer Conditions

只有在相同算符、同一相位约定、同一 blocked 组态和同一 `K`/自旋投影下，才可把
`g_K`、`b_0` 和 `B(M1)` 做跨核比较。`β3` 的模型参数不能直接从偶偶 `224Ra` 的
`Q3` 转给奇核；Gaffney 2013 的 `220Rn/224Ra` E3/Q3 结果支持偶偶核的八极集体性，
但作者明确保留静态梨形与八极振动的解释边界。[Gaffney source page](../sources/gaffney-2013-pear-shaped-rn-ra.md:60)

## Failure Conditions

- 把评价 `MOMM1` 当作宇称伙伴间 `B(M1)`；
- 把 Stone 表中的 `R` 重评值与原始值当作独立测量平均；
- 用 `K=1/2` 退耦式解释 `225Ac` `K=3/2` 候选带；
- 把 toy `b_0` 或 `g_K` 曲线称为生产级 Nilsson/blocked-HFB 结果；
- 仅凭 40–55 keV 能隙或一个 E1 强度宣布静态八极形变。

## Falsification or Reverse Tests

1. 对 `225Ra` 和 `227Ra` 做同一 blocked-HFB+宇称投影计算：若同时拟合 `μ`、`a/b_0`、
   E1/E3 和逐态能隙失败，则“单一八极混合解释”应降级。
2. 对 `225Ac` 直接测量基态和低能伙伴的核磁矩/g 因子；若 `g_K` 不同于同一组态的
   blocked 预测，伙伴带需重新配对。
3. 为 `225Ra` `55.16-keV` 和 `225Ac` `40.09-keV` 相关分支取得寿命、内转换和完整
   分支，给出伙伴间 `B(M1)` 上限或测量值；若其大小与模型要求不符，需转向组态混合/软振动。
4. 改变 `q_s` 从 0.65 到 0.75 并同时改变 Coriolis 核；若只能靠独立调参重现 `μ`，
   说明静态矩对 `β3` 的反演不可识别。

## Open Questions

- `225Ac` 是否存在可复核的状态分辨静态 μ/g 因子与 `B(M1)` 测量？
- `223Ra` 的 `+0.271(2)` 与 `+1.21(3)` 磁矩差异究竟来自参考标准、原始原子态身份还是
  重评方法？
- `225Ra` 的 `μ=-0.7338(15) μ_N` 是否能与同一 blocked 组态的 E1/E3、解耦参数和
  转移谱因子共同拟合？
- 有效 `g_s` 的 0.65–0.75 区间在相对论时间奇场、配对和粒子—八极声子耦合同时打开时
  是否仍适用？

## Human Review

本页为 Codex source self-audit，保持 `review_status: unreviewed`。优先人工核查：
`225Ra` 激光磁矩原始论文、`223Ra` Stone 表的参考标准冲突、`227Ac` 光学取向原件、
以及 `223Ra` Table 1 的 M1/E2 混合与寿命误差传播。未把任何 toy 曲线标为
`human-reviewed`。

## Promotion or Rejection History

- 2026-10-29：建立本研究笔记和四轨道 `β3` 扫描工件；确认 `225Ra` 静态 μ 有评价记录，
  `225Ac` 静态 μ 与伙伴 `B(M1)` 仍为证据缺口。
- 2026-10-29：拒绝把 `223Ra` 带内 `B(M1)` 迁移为 `225Ra/225Ac` 伙伴间率；拒绝把
  `g_s^{eff}/g_s^{free}=0.65–0.75` 写成目标核的直接实验事实。

## Reproducible Artifacts

- [README](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-magnetic-moments/README.md)
- [Python model](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-magnetic-moments/nilsson_octupole_magnetic_moments.py)
- [CSV graph data](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-magnetic-moments/nilsson_octupole_magnetic_moments.csv)
- [JSON results](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-magnetic-moments/nilsson_octupole_magnetic_moments.json)
