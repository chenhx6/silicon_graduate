---
type: research-note
title: "110Cd HI,XNG相对强度与Roy Table 1的证据边界"
aliases: [cd110 relative strength audit 047, 110Cd RI B(E2) boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
tags: [110Cd, antimagnetic-rotation, ENSDF, relative-intensity, B(E2), lifetime]
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, nndc-2012-cd110-adopted-lifetimes-branches, nndc-2012-cd110-hi-xng]
created_from: Day26 read-only source audit
promotion_target: antimagnetic-rotation-evidence
---

# 110Cd HI,XNG相对强度与 Roy Table 1 的证据边界

本页是只读审计，配套结构化产物为 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/cd110-relative-strength-audit-047.json`。审计目的，是把 `110Cd (HI,XNG)` 评价中的相对 γ 强度、评价文件中的结构化强度字段和 Roy 等 2011 年 Table 1 的寿命派生 `B(E2)` 分开。审计没有从相对强度反推出绝对 `B(E2)`、`B(M1)` 或 `B(M1)/B(E2)`。

## Research Trigger

Roy Table 1 与 HI,XNG 评价使用不同的观测层；本审计检查是否把 RI 误升级为绝对跃迁强度。

## Grounded Evidence

## 直接记录：HI,XNG 的 yrast B 带相对强度

`raw/papers/gpt/_incoming/day26-20261028-002/nndc/110cd-hi-xng.ensdf` 的表头说明 `Eγ, RI` 来自 1994Ju04，并说明实验测量/推导包含 `B(M1)/B(E2)`；但具体高自旋记录只给相对强度 `RI`、多极性和 DCO。18+–24+ 的带内 E2 记录为：

| 初态 | `Eγ` (keV) | RI | 多极性 | 原件定位 |
|---|---:|---:|---|---|
| 18+ → 16+ | 1224.5(2) | 11.2(2) | E2 | HI,XNG lines 443–445 |
| 20+ → 18+ | 1323.0(3) | 5.1(2) | E2 | HI,XNG lines 516–517 |
| 22+ → 20+ | 1314.1(3) | 2.7(1) | E2 | HI,XNG lines 537–538 |
| 24+ → 22+ | 1358.0(3) | 2.5(1) | E2 | HI,XNG lines 558–559 |

以 1314.1-keV RI 为分母，这四个值分别约为 4.15(8)、1.89(8)、1 和 0.93(4)。这些比值仍是同一评价归一化下的相对产额，不能直接替代寿命测量得到的约化跃迁几率。16+ → 14+ 的 1074.6-keV E2 记录为 RI=20.0(2)（HI,XNG lines 357–358），这里只作强度锚点。

## 22+ 的 1100-keV 争议

HI,XNG 在 22+（9962.4 keV）下列出 1100-keV、RI=1.0(3) 的 γ 线，但没有给出多极性或明确终态（lines 534–538）。能量差 `9962.4−1100=8862.4 keV` 接近评价中另一个 20+ 水平 8861.6 keV，而不是 yrast B 带 8648.3-keV 的 20+ 水平；因此不能把它自动当成 22+ → 20+ 的 1314-keV E2 替代线。

adopted ENSDF 对该线给出相对强度 37、`[E2]` 和 `BE2W=20(10)`，同时保留明确注释：包含 1100-keV 线时得到 `T_{1/2}=0.11(4)` ps；2011Ro01 在 γγ 门控谱中没有确认该线，采用 `T_{1/2}=0.15(5)` ps（adopted lines 2485–2499）。因此 1100-keV 的终态、归属和对 22+ 寿命的贡献必须标为有争议；它的评价 `BE2W` 不能被当作已确认的独立绝对跃迁强度。

## Roy 2011 Table 1：绝对寿命派生强度

Roy 等的 Table 1（PDF p.3）列出 110Cd 带内 E2 的寿命和 `B(E2)`：

| 跃迁 | `Eγ` (keV) | τ (ps) | `B(E2)` ((e b)²) |
|---|---:|---:|---:|
| 16+ → 14+ | 1075 | 0.36(3) | 0.14(1) |
| 18+ → 16+ | 1224 | 0.23(3) | 0.12(2) |
| 20+ → 18+ | 1323 | 0.17(3) | 0.11(2) |
| 22+ → 20+ | 1314 | 0.21(7) | 0.09(3) |
| 24+ → 22+ | 1358 | 0.27(7) | 0.06(2) |

这些是寿命到 `B(E2)` 的派生结果，物理量和误差结构不同于 HI,XNG 的 RI。Roy 文章 p.2–3 还说明 1323/1314-keV 线形存在重叠，22+ 线形在 1314-keV 门中单独提取，22+ 寿命在全局拟合中固定；停止本领系统误差可达约 20%。

## 评价文件中的 B 字段审计

HI,XNG 文件没有 `BM1W=` 或 `BE2W=` 结构化记录，只有 `RI`、多极性、DCO 和寿命相关信息。adopted ENSDF 确实包含逐 γ 的 `BE2W=` 和部分其它能带的 `BM1W=` 字段；对于 yrast B 带，18+、20+、22+、24+ E2 记录分别出现 `BE2W=41(6)`、`38(7)`、`22(8)` 和 `21(6)` W.u.，1100-keV 候选记录为 `BE2W=20(10)`、`[E2]`。但是，两个评价文件都没有一个可直接读取的、针对这组 18+–24+跃迁的 `B(M1)/B(E2)` 结构化字段。表头“Deduced: B(M1)/B(E2)”不等于每一条记录都已提供该比值。

因此，当前证据链应写成：

1. HI,XNG 提供相对 γ 产额和多极性信息；
2. adopted ENSDF 提供评价者的逐线 `BE2W` 字段，并保留 1100-keV 争议注释；
3. Roy Table 1 提供由线形寿命派生的绝对 `B(E2)`；
4. 不能用 RI 比值代替绝对 `B(E2)`，也不能仅凭 RI 和评价表头声称已获得绝对 `B(M1)/B(E2)`。

## 可复现性与证据定位

- HI,XNG SHA-256：`cd14b1104805f54023a420e6021b74fddaa149a7f7f5cd404be23a9c696b47d1`。
- adopted ENSDF SHA-256：`04975bce4e22e754b2cc556f7616a3ae9174e6a47b9f506974cc9a9b2c45ba66`。
- Roy PDF SHA-256：`2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a`。
- 机器可读审计：[cd110-relative-strength-audit-047.json](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/cd110-relative-strength-audit-047.json)。

状态：`needs_review: true` 仅用于 1100-keV 归属、评价字段与跨来源寿命差异的定向人审；本页不把评价相对量升级为绝对强度。

## Provisional Reasoning

相对 RI 只能用于同一评价对象内的条件比较；Roy 的绝对 B(E2)来自寿命与分支处理，两个层级不能静默合并。

## Assumptions

本页不重建响应、feeding、side-feeding、停止本领或联合协方差。

## Competing Explanations

Roy 中心差异可能来自分支选择、线形拟合、feeding、停止本领或舍入；现有数据不能排序这些原因。

## Transfer Conditions

只有同一门条件、响应、分支清单和初态身份完整时，RI 才能进入绝对强度重建。

## Failure Conditions

把评价 RI、表头中的 B(M1)/B(E2) 描述或 1100-keV 候选直接当作 Roy 的绝对结果会越过证据层。

## Falsification or Reverse Tests

取得 Roy 逐门 feeding 与联合协方差后，对四个高自旋跃迁逐点前向重放，并检验是否能统一解释中心差异。

## Open Questions

Roy 的原始 LINESHAPE 输入、侧馈参数和停止本领曲线是否存在公开或作者可获得版本？

## Human Review

本页为 Codex self-audit，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 修复 research-note schema并保留相对/绝对观测层边界。
