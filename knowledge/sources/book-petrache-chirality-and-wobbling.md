---
type: source
title: "Petrache (ed.) — Chirality and Wobbling in Atomic Nuclei (CRC, 2025 imprint)"
aliases: [Petrache2024, Chirality and Wobbling Book, 核手征与摆动专著]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Chirality and Wobbling in Atomic Nuclei"
authors: ["Costel Marian Petrache (editor)"]
publisher: "CRC Press / Taylor & Francis Group"
year: 2025
pages: "339 PDF pages; 320 numbered text/index pages"
isbn: "9781032691633 (ebook); 9781032691282 (hardback); 9781032691602 (paperback)"
doi: "10.1201/9781032691633"
canonical_source: "Local edition copyright page, PDF p. 5 (iv)"
library_file: "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf"
raw_file: "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf"
raw_sha256: "787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2"
raw_storage_status: archived-local
archive_required: true
nuclei: [135pr, 105pd, 133la, 187au, 130ba, 136nd, 127xe]
models: [particle-rotor-model, triaxial-projected-shell-model, ibfm, tilted-precession]
tags: [books, triaxiality, wobbling, chirality, competing-interpretations]
---

# Chirality and Wobbling in Atomic Nuclei：版本、章节与争议证据入口

## Scope and Reading Depth

本轮核验版权页、完整目录，并对若干关键段落进行了原文重读与公式复核。`reading_depth: skimmed` 表示**全书尚未完成逐章主线阅读**；局部深查不能把整部书标为 deep-read。上一版整书 deep-read、全量吸收和“争议终结”的表述撤回。正文抽取缓存放在 `tmp/`，不等于已经阅读图表或完整章节。

实际核查：PDF 43–47 的三轴转子定义及轨道分类；PDF 56–57 的 135Pr 争议；PDF 118–123 的实验判据、低自旋近似和偶偶核案例；PDF 244–246 的 IBFM 混合比公式、参数依赖与结果。PDF 244、122 还做了页面图像核对。未覆盖：其余章节正文、全部图表、参考文献的原始数据与 SI。完整阅读状态应按 [[book-corpus-coverage-ledger]] 续接。

## Bibliographic Record

本地 PDF p. 5 标注首版 2025、CRC Press、三种 ISBN 和 DOI；因此按**所持有的版本**登记 2025。部分章节叙述覆盖 2024 年文献，不以此推断版本年份。旧页面的 ISBN `9781032483863` 未由本原件支持，已撤回；Springer 归属错误。保留 `Petrache2024` alias 仅供旧链接检索，不代表书目核验结论。

本书是多人撰写的编著。各章作者的判断不能互相替代，也不因同处一书就成为独立实验复现。

## Chapter Map

页码均为 **PDF 物理页（1 起算）**，并非印刷页。正文印刷页通常为 PDF 页减 19。

| 章 | 作者/主题 | PDF 范围 | 本轮可声称的阅读状态 |
| --- | --- | --- | --- |
| 1 | Petrache，历史与展望 | 20–42 | 目录定位 |
| 2 | Frauendorf，三轴核摆动 | 43–80 | 选段核查，非全章完成 |
| 3 | Meng / Wang，核手征性 | 81–93 | 目录定位 |
| 4 | Tanabe / Sugawara-Tanabe，代数模型 | 94–109 | 目录定位 |
| 5 | Guo / Lv，实验结果与争议 | 110–126 | 选段核查，非全章完成 |
| 6 | Lawrie，倾斜进动与术语争议 | 127–155 | 目录与检索定位，正文待读 |
| 7 | Grodner，126,128Cs 与寿命/g 因子 | 156–166 | 目录定位 |
| 8 | Raduta 等，半经典模型 | 167–203 | 目录定位 |
| 9 | Zhao，含时 CDFT 手征动力学 | 204–221 | 目录定位 |
| 10 | Chen 等，CDFT+PRM | 222–238 | 目录定位 |
| 11 | Nomura，IBFM/IBFFM | 239–255 | 选段核查，非全章完成 |
| 12 | Sheikh 等，TPSM 与摆动 | 256–274 | PDF 258–259 选段阅读，公式待逐式复核 |
| 13 | Budaca，准粒子对齐的自旋动力学 | 275–291 | 目录定位 |
| 14 | Wang，TPSM 手征与摆动 | 292–301 | 目录定位 |
| 15 | Qi，A≈80 核手征 | 302–310 | 目录定位 |
| 16 | Li / Chen，Cs 同位素链 | 311–322 | 目录定位 |
| 17 | Zhang 等，过渡系统与 γ 振动模型 | 323–337 | 目录定位 |

## Key Evidence and Reasoning Chain

| ID | 原书内容与用途 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CW-1 | 三轴转子模型用三个惯量及轴约定定义；该章采用 s,m,l 为 1,2,3。不能把别章的数字轴标签直接代入。 | model-result | direct | Ch. 2, PDF 43–45 / pp. 24–26, Eqs. 2.1–2.5 | false |
| CW-2 | Frauendorf 以分离轨道的拓扑分类讨论 wobbling/flip，并明确不同意仅限谐振幅的命名建议。这是作者的分类立场。 | author-interpretation | direct | Ch. 2, PDF 45–46 / pp. 26–27, Fig. 2.3 邻文 | false |
| CW-3 | 同一章比较 135Pr 的小混合比与大混合比结果，作者仍倾向 TW，并提出需新实验确定 δ。不能说该书已一致否定 135Pr 摆动。 | author-interpretation | direct | Ch. 2, PDF 56–57 / pp. 37–38, Fig. 2.15 邻文 | false |
| CW-4 | 实验章节讨论 P 与方向角关联联合分析所给的小 δ、M1 主导，并据此反对部分低自旋摆动指认；同时要求标准化分析与公开数据。 | author-interpretation | direct | Ch. 5, PDF 120–121 / pp. 101–102 | false |
| CW-5 | 书中 130Ba/136Nd 两准粒子案例的连接跃迁可为 M1 分量更强，但 E2 相对旋称伙伴增强。因此“所有摆动必须 fE2>80%”不是通用必要条件。 | author-interpretation | direct | Ch. 5, PDF 122–123 / pp. 103–104, Fig. 5.7 后段 | false |
| CW-6 | 混合比由有符号约化 E2/M1 矩阵元及光子能量计算；E2/M1 算符有核芯、单粒子及占有振幅贡献。 | model-result | direct | Ch. 11, PDF 244–245 / pp. 225–226, Eqs. 11.10–11.12 | false |
| CW-7 | IBFM 计算对 135Pr 给出小混合比，并指出某些 127Xe 低自旋大 δ 来自过小的 M1 矩阵元，而非必然很大的 E2。 | model-result | direct | Ch. 11, PDF 245–246 / pp. 226–227, Fig. 11.3 邻文 | false |

`false` 表示本轮完成“这段原文是否如此表述”的 self-audit，不等于实验真实性、学界共识或 human-reviewed。

## Competing Interpretations and Limitations

| 问题 | 支持路线 | 反对/替代路线 | 证据依赖 |
| --- | --- | --- | --- |
| 135Pr 低自旋候选 | Ch. 2: 能量演化、拟合惯量的 QTR、TPSM、邻核类比 | Ch. 5: 新混合比分析；Ch. 11: IBFM 小 δ 与 γ 软核响应 | 章节重用既有论文，不是三次独立测量 |
| 低自旋是否称 wobbling | Ch. 2: 轨道拓扑分类可超出谐振幅 | Ch. 5/6: 强调高自旋小振幅近似与 TiP 区别 | 部分是定义/适用域之争，与数值提取争议分开 |
| E2 指纹 | 要看跨带集体 E2 与模型联合预言 | 大 δ 可来自 M1 小分母；两准粒子磁矩可使 M1 同时增强 | 需绝对或相对 B(E2)、寿命、组态和系统学 |

原文自身也须批判阅读：Ch. 11 PDF 244（p. 225）把 105Pd 列入奇质子例子，并写 127Xe 是该集合中唯一奇中子核；105Pd 的 Z=46、N=59 明确与此冲突。保留为**原书疑似笔误**，不把它转录为核素事实。Ch. 5 PDF 121 的 σ 文字描述与常用高斯宽度记号也应结合具体参数定义核对，不将一个字词强行当成方差定义。

## Analytical Reconstruction

可复用的研究顺序是：先核对轴和相位约定 → 确认能带/跃迁身份 → 保留 δ 的全部可容许解 → 在共同响应模型中联合角关联、偏振与取向不确定度 → 从混合比、分支比和寿命分别建立电磁强度 → 比较 PTR/TPSM、IBFM/γ 软核、旋称伙伴及 TiP 的区分性预言。这个流程是本任务综合，不是原书统一列出的“硬五道门”。

## Knowledge Impact and Self-audit

- 修正 [[wobbling-mixing-ratio-phase-and-transition-diagnostics]] 中未经核验的普适相位法则与自动选根。
- 连接 [[book-bohr-mottelson-nuclear-structure-vol2]] 的高自旋近似，检查用词与数学条件。
- P0 科学项：旧“理论选根即确认 TW”已撤回；旧“同宇称手征双带是正负宇称伙伴”错误也撤回。手征恢复与宇称破缺是不同对称性问题。
- P1：须继续完整重读 Ch. 2、5、6、11，再回到被引实验的实际数据/响应与后续论文；目前不据本书给 135Pr 做终局裁决。
- 无本轮 human-review 事件；原件哈希核验只确认来源身份，不证明阅读已完成。


## Summary

详见正文对应小节及核对记录。


## Key Results

详见正文对应小节及核对记录。


## Extracted Pages

详见正文对应小节及核对记录。
