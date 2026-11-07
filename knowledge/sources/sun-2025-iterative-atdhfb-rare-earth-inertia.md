---
type: source
title: "Sun 等 2025：稀土核时间奇响应与迭代 ATDHFB"
aliases: [Sun 2025 rare earth inertia, exact iterative ATDHFB]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Moments of inertia of rare-earth nuclei and the nuclear time-odd mean fields within exact solutions of the adiabatic theory"
authors: [Xuwei Sun, Jacek Dobaczewski, Markus Kortelainen, Jhilam Sadhukhan, Adrián Sánchez-Fernández, Herlik Wibowo]
journal: Physics Letters B
year: 2025
volume: "868"
pages: "139685"
doi: 10.1016/j.physletb.2025.139685
arxiv: 2502.07433v3
language: en
canonical_source: https://doi.org/10.1016/j.physletb.2025.139685
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g43-new-collective-response/sun2025-atdhfb-moi-v3.pdf
raw_sha256: 7bf720ee69339743c0f9737f04147584206d0e10f7c7842a1657634fc1c8dc70
preprint_v1_file: raw/papers/gpt/query/20261108-r2-g43-new-collective-response/sun2025-atdhfb-moi.pdf
preprint_v1_sha256: 576d3b880ffc68a7820439d9b4da24fd438c76feabeedb8d11ed7b55af10c647
raw_storage_status: archived-local
archive_required: true
nuclei: [166er]
reactions: []
experiments: []
models: [atdhfb, skm-star, unedf1, gogny-d1s, hfodd]
observables: [rotational-inertia, collective-mass, effective-mass]
methods: [iterative-linear-response, self-consistent-cranking]
tags: [doctoral-foundations, time-odd-fields, pairing, functional-dependence]
---

# 形变几乎相同，惯量仍可明显不同

## Bibliographic Record

Crossref 与 arXiv 作品页核得发表身份：PLB868,139685，2025 年。
实际主底本为 **2502.07433v3，7 个物理页，2025-07-01**。
先取得的 v1 为 6 页，2025-02-11；两版均保留。
没有取得并逐字核对 PLB 最终校样，不能沿用 worker 的“与出版版完全对齐”声明。

## Scope and Reading Depth

- Completed reading_depth: skimmed，有界方法和版本深读。
- Covered scope: v1 pp. 1–5 主线；v3 方法核心及 pp. 3–5 的设置、
  166Er 三泛函数字、残差样本说明、配对限制与有效质量关联。
- Not covered: 原 HFODD 生产代码执行、每个同位素的全部输入与输出、
  有效质量回归的独立数据重拟合、所有参考文献原件和最终刊版逐字比较。

## Paper Question and Scientific Motivation

作者用自洽迭代避免显式构造/求逆完整稳定矩阵，计算给定 EDF 下的
ATDHFB 惯量，比较忽略诱导场的 IB 基准。
题名的“exact”指求解所给绝热理论方程，不是精确求解有限核完整多体 Hamiltonian。

## Method and Design Logic

Gd、Dy、Er、Yb、Hf、W、Os 偶偶同位素的系统计算，
比较 SkM*、UNEDF1、D1S。v3 使用的空间形状限制须保留；
代码原则上允许任意形状，不等于本研究已经使用全部三轴自由度。
初次不含诱导时间奇场的迭代给 IB，后续自洽更新求该理论的响应。
原有 EDF、配对及时间奇参数已有经验来源；“无额外可调参数”
不代表所有参数从未接触数据。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| S25-1 | 自洽迭代保留诱导场，首轮退化为 IB；它解的是绝热响应方程，未消除集体慢运动假设。 | model-result | direct | v3 pp. 2–3, Eqs. (2)–(15) | false |
| S25-2 | 166Er 三个泛函给出相近 β₂₀，却有不同 IB/ATDHFB 惯量；下表为正文数字，不是实验直接测定。 | model-result | direct | v3 p. 4, Fig. 1 后正文 | false |
| S25-3 | 本研究所有所算同位素的 ATDHFB 转动惯量大于 IB，但增强随核素和泛函变化，不能选一个全区常数。 | model-result | direct | v3 pp. 4–5, Figs. 1,3 及正文 | false |
| S25-4 | Hf/W/Os 约 N=100 的部分异常预测在 v3 统计中给出排除/包含两套结果；忽略三轴性是作者提出的可能原因。 | author-interpretation | direct | v3 p. 4, Fig. 2 讨论 | false |
| S25-5 | 配对形式和强度的不确定性使作者不作“IB 或 ATDHFB 更符合实验”的确定排序，D1S 结果也未形成排他结论。 | author-interpretation | direct | v3 p. 5, residuals 讨论 | false |
| S25-6 | 实验对照惯量由 \(3\hbar^2/E(2_1^+)\) 的转动模型映射取得，不是三轴张量的直接测量。 | model-result | direct | v3 p. 4, Fig. 1 的实验映射说明 | false |

166Er 的指定计算，惯量单位均为 \(\hbar^2/\mathrm{MeV}\)：

| EDF | β₂₀ | IB | ATDHFB |
|---|---:|---:|---:|
| SkM* | 0.320 | 27.584 | 34.950 |
| UNEDF1 | 0.324 | 36.401 | 41.342 |
| D1S | 0.322 | 27.865 | 41.147 |

## Summary

这里有直接的模型实例说明：相似静态四极形变并不唯一固定响应。
同时，自洽程度更高并不自动保证与全部实验更接近；配对、EDF 校准和
缺失自由度仍会改变结论。

## 版本增量与样本边界

v1 对部分 Hf/W/Os 核只报排除后的残差统计；
v3 给出包含它们的括号值，并提示忽略三轴性可能参与异常。
例如 v3 对 SkM* 的 IB 均值为 −2.55（包含后 −2.21），
ATDHFB 为 2.54（包含后 3.06）\(\hbar^2/\mathrm{MeV}\)。
不将 v1 的 −2.58/1.89 与 v3 的统计样本混用。
这不是本任务重新确定哪些实验点“应该”被删；
比较方法时必须保留作者的样本选择和两套结果。

## Competing Interpretations and Limitations

七个 Skyrme 泛函在 166Er 上的有效质量—增强比关联是作者指定集合的回归；
它不是对所有核、所有自旋或所有时间奇通道的因果定理。
保持 β 接近也没有固定配对、单粒子谱及全部残余场，不能用上表唯一归因某一项。
配对参数和时间奇调整的底层原作未在本页独立重新核验。
逐核完整数据为 on-request 状态，本任务未发送邮件索取，也未冒称公开输入已可重放。

## Knowledge Impact and Learning Decision

supports：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]] 的势—响应分层；
limits：一种形变对应唯一惯量、无经验输入、完整自洽必然全面改善拟合的过强说法。
与 [[petrik-kortelainen-2018-rotational-tv-inertia]] 存在方法和配对设置依赖。

## Agent Self-audit Triage

P0：v1/v3 独立归档，出版身份与实际读取版本分开；3×3 个 166Er 数字和
统计样本增量回原文核实。
P1：exact 的适用层、配对/时间奇校准、轴对称限制和经验惯量映射保留；
不宣称新发现或已运行原生产计算。
P2/P3：citation key 保持空值；未读取的背景题录不产生机制结论。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
