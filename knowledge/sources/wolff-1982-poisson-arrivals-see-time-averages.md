---
type: source
title: "Wolff 1982 - Poisson Arrivals See Time Averages"
aliases: [Wolff 1982 PASTA, PASTA theorem, Operations Research 30 223]
created: 2026-11-13
updated: 2026-11-13
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Poisson Arrivals See Time Averages"
authors: [Ronald W. Wolff]
journal: "Operations Research"
year: 1982
volume: "30"
issue: "2"
pages: "223–231"
doi: "10.1287/opre.30.2.223"
canonical_source: "https://doi.org/10.1287/opre.30.2.223"
citation_key: "wolff-1982-poisson-arrivals-see-time-averages"
raw_file: "raw/papers/gpt/query/20261113-A130-live-time/wolff-1982-poisson-arrivals-see-time-averages.pdf"
raw_sha256: "42b994436fed08d86ddcc7dd7773dec34c0058ca505d9e0f65f92c5ec7b4e9f2"
raw_storage_status: archived-local
archive_required: true
archive_manifest: "raw/papers/gpt/query/20261113-A130-live-time/manifest.json"
actual_read_pages: [2, 3, 4, 5]
actual_read_scope: "PDF第2–5页（印刷第223–226页），重点核查Section 1模型设定、Lack of Anticipation Assumption (LAA)定义与Theorem 1及其极限定理证明。仅定向选读，不表示全文精读。"
nuclei: []
reactions: []
experiments: []
models: [poisson-process, queueing-theory, continuous-time-martingale]
observables: [time-average, arrival-average, live-time]
methods: [PASTA-theorem, stochastic-intensity, lack-of-anticipation]
tags: [PASTA, Poisson-arrivals, time-average, arrival-average, dead-time, live-time, queueing]
---

# 泊松到达观测时间平均（PASTA）定理与无预知假设

## Bibliographic Record

本地原件是完整的 10 页 PDF，来自普渡大学数学系公开教学归档（Teaching 532 PASTA.pdf）。
期刊发表身份为 *Operations Research*, Vol. 30, No. 2, pp. 223–231 (1982)。
DOI 为 `10.1287/opre.30.2.223`。
文件大小为 251,098 字节，SHA-256 为 `42b994436fed08d86ddcc7dd7773dec34c0058ca505d9e0f65f92c5ec7b4e9f2`。
已登记于 `raw/papers/gpt/query/20261113-A130-live-time/manifest.json`。
`citation_key` 为 `wolff-1982-poisson-arrivals-see-time-averages`。

## Scope and Reading Depth

- **Covered scope**:
  - PDF 第 2–3 页（印刷第 223–224 页）：引言与 PASTA 历史文献综述；
  - PDF 第 4 页（印刷第 225 页）：Section 1 模型设定、时间平均 $V(t)$ 与到达平均 $Y(t)$ 的测度定义，以及无预知假设（Lack of Anticipation Assumption, LAA）的严格数学定义；
  - PDF 第 5 页（印刷第 226 页）：Theorem 1 极限定理陈述及其基于连续时间鞅（Martingale）的证明思路。
- **Not covered**:
  - PDF 第 6–10 页中关于特定多服务台排队、一般随机网络应用以及引理的具体积分放缩细节；
  - 未重构全文涉及的所有一般拓扑测度论推广。
- **Auditing record**: G79 依据第 5 章第 5.5 节多通道联合活时间理论构建需求，对上述核心定义与极限定理进行定向选读核验。历史 `review_status: unreviewed` 记录尚未经历独立人工审核。

## Summary

Wolff (1982) 严格证明了排队论与随机服务系统中著名的 PASTA 定理（Poisson Arrivals See Time Averages）。
论文指明：到达过程所见的状态比例与系统处于该状态的时间均匀比例相等的关键充要假定是“无预知假设”（LAA）——未来到达增量独立于系统过去与当前的状态。
论文特别澄清，当前系统状态可以完全依赖过去的到达历史（即允许系统由到达驱动并产生死时间等反馈延迟），LAA 仅要求到达不可前瞻预知未来。
该定理为核电子学中将连续时间硬件占空比映射为离散粒子到达的物理活时间提供了精确的适用边界。

## Theoretical Setup

设事件到达过程为平稳泊松点过程 $\{A(t), t \ge 0\}$，到达强度为 $\lambda \in (0, \infty)$。
设被观测的随机过程为 $\{X(t), t \ge 0\}$，状态空间为可测空间；定义实值状态泛函 $U(t) = f(X(t))$（在探测器死时间语境下即为系统存活指示变量 $\mathbf{1}_{\mathrm{live}}(t)$）。
连续时间平均（Time Average）：
$$
V(t) = \frac{1}{t} \int_0^t U(s) \, \mathrm{d}s.
$$
离散到达平均（Arrival Average）：
$$
Y(t) = \frac{1}{A(t)} \int_0^t U(s) \, \mathrm{d}A(s) = \frac{1}{A(t)} \sum_{k=1}^{A(t)} U(t_k^-).
$$

## Key Results

| ID | 主张 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C-WOLFF-01 | 在无预知假设（LAA）下，泊松到达过程观测到的到达平均极限与连续时间平均极限以概率 1 存在且相等（Theorem 1）。 | formal-theorem | primary-proof | PDF第4–5页（印刷第225–226页）Theorem 1 | false |
| C-WOLFF-02 | 无预知假设（LAA）严格定义为对于任意 $t \ge 0$，未来到达增量 $\{A(t+u)-A(t), u \ge 0\}$ 独立于过去和当前状态 $\{X(s), A(s); 0 \le s \le t\}$。 | formal-definition | primary-proof | PDF第4页（印刷第225页）Section 1 LAA definition | false |
| C-WOLFF-03 | LAA 允许系统当前状态依赖过去到达历史（如探测器死时间由过去触发引起），其约束核心是未来到达不反向预知当前系统忙闲。 | physical-interpretation | primary-analysis | PDF第3–4页（印刷第224–225页） | false |
| C-WOLFF-04 | 泊松到达性质是在 LAA 下保证 PASTA 成立的充分条件，在特定非泊松系统中时间平均与到达平均亦可能局部相等，但非普遍成立。 | theoretical-limitation | primary-analysis | PDF第2–3页（印刷第223–224页） | false |

## Competing Interpretations and Limitations

1. **不可将时间平均等同于有限样本到达平均**：
   Theorem 1 是概率 1 的大数极限定理（$t \to \infty$），不保证在有限时间窗口内二者严格无差；在束流突发或短脉冲实验中必须考虑有限时间方差。
2. **级联退激与束团结构的破坏**：
   在核物理在束实验中，如果外部到达具有时间结构（如回旋加速器射频束团），或者同核发射的两光子存在能级寿命等待关联，到达过程不满足平稳独立增量泊松假设，此时时间平均死时间比例必然偏离离散级联事件的联合存活几率。

## Extracted Pages

### PDF 第 4 页（印刷第 225 页，Section 1 & LAA 定义）

> "Lack of Anticipation Assumption (LAA). For each $t \ge 0$, $\{A(t + u) - A(t), u \ge 0\}$ is independent of $\{X(s), 0 \le s \le t; A(s), 0 \le s \le t\}$."

### PDF 第 5 页（印刷第 226 页，Theorem 1）

> "Theorem 1. Under LAA, $V(t) \to V$ w.p. 1 if and only if $Y(t) \to V$ w.p. 1."
