---
type: source
title: "Ashok Kumar Jain 等 2021 - Nuclear Isomers: A Primer"
aliases: [Jain2021, Nuclear Isomers Primer, 同核异能态入门与前沿]
created: 2026-11-01
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: read
title_original: "Nuclear Isomers: A Primer"
authors: [Ashok Kumar Jain, Bhoomika Maheshwari, Alpana Goel]
publisher: "Springer Nature Switzerland"
year: 2021
citation_key: "jain_2021_130sn-isomers-primer"
pages: "151"
isbn: "978-3-030-76722-8"
canonical_source: "A. K. Jain, B. Maheshwari, and A. Goel, Nuclear Isomers: A Primer, Springer (2021)"
library_file: "raw/books/nuclear isomer - A Prime.pdf"
raw_file: "raw/books/nuclear isomer - A Prime.pdf"
raw_sha256: "20f88b84240637e10a6086eca6b9f6e80a28813ad1ecf14a795144a4d5c2ac34"
nuclei: [130sn, 134te, 210po, 94ru, 178hf]
reactions: [in-beam-gamma, delayed-gamma, isomers]
experiments: []
models: [spin-trap, seniority-isomers, k-isomers, shape-isomers]
tags: [books, nuclear-isomers, transition-hindrance, seniority-scheme, k-quantum-number, gamma-ray-half-life]
---

# Ashok Kumar Jain 等 2021 - Nuclear Isomers: A Primer

## Bibliographic Record

- **书名**：Nuclear Isomers: A Primer（SpringerBriefs in Physics）
- **著者**：Ashok Kumar Jain, Bhoomika Maheshwari, Alpana Goel (IIT Roorkee / University of Zagreb / Amity University)
- **出版信息**：Springer Nature Switzerland AG, 2021.
- **书号与定版**：ISBN 978-3-030-76722-8 / eBook ISBN 978-3-030-76723-5, DOI: 10.1007/978-3-030-76723-5.
- **全书规模**：151 物理 PDF 页；正文印刷页 1–139。
- **本地原件**：`raw/books/nuclear isomer - A Prime.pdf`
- **原件 SHA-256**：`20f88b84240637e10a6086eca6b9f6e80a28813ad1ecf14a795144a4d5c2ac34`

## Scope and Reading Depth

本来源登记状态定为 `read`，明确界定本轮针对 Seniority 异能态机制、半满壳相消、$K$-同核异能态与三轴形变诱导 $K$-混合的重点查验范围：
- **已核查章节**：
  - 封面、版权页与目录（PDF pp. 1–12）；
  - Chapter 3: Seniority Isomers and Generalized Seniority (印刷 pp. 31–52 / PDF pp. 43–64)：单 $j$ 壳层配对相互作用、Seniority 量子数 $v$、高 $j$ 轨道中子/质子占有率 $n$、带间 $B(E2)$ 跃迁几率母权系数抛物线展开与半满壳相消；
  - Chapter 5: $K$-Isomers and Hindrance Factors (印刷 pp. 71–98 / PDF pp. 83–110)：轴对称形变与 $K$ 选择定则、禁戒度 $\nu = |\Delta K| - \lambda$、折合阻碍度 $f_\nu = (F_W)^{1/\nu}$ 经验规律、以及三轴形变破坏轴对称导致 $K$-混合（$K$-mixing）使得 $f_\nu$ 异常下降的三轴指纹效应。
- **未核查内容**：Chapter 2 自旋陷阱细节、Chapter 4 形状共存与裂变同核异能态全文、Chapter 6 异能态应用与天体物理核合成。

## Summary

本书是国际权威同核异能态领域专家 A. K. Jain 教授编著的现代核异能态经典专著。全书系统解构了核能谱中长寿命激发态（$T_{1/2} \ge 1\text{ ns}$）的四类本质微观机制：自旋陷阱（Spin Traps）、Seniority 代数异能态（Seniority Isomers）、$K$-异能态（$K$-Isomers）与裂变形状异能态（Shape Isomers）。在在束核谱学与三轴集体运动研究中，本书为微观高 $j$ 壳层跃迁阻碍、半满壳粒子-空穴对称性相消、以及三轴形变诱导 $K$-破缺提供了核心物理判据。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JAIN-1 | Seniority 异能态半满壳 $B(E2)$ 相消：单 $j$ 壳层内相同 Seniority（$\Delta v = 0$）跃迁几率满足 $B(E2; j^n, v \to v) = \left(\frac{2j+1-2n}{2j+1-2v}\right)^2 B(E2; j^v, v \to v)$；在半满壳 $n = j+1/2$ 处因粒子-空穴对称性导致 $B(E2) \equiv 0$，产生极其长寿的 Seniority 异能态（如 $^{130}\text{Sn}$ 的 $10^+$ 与 $^{210}\text{Po}$ 的 $8^+$ 态）。 | model-result | direct | Ch. 3, 印刷 pp. 31–38 / PDF pp. 43–50 | false |
| JAIN-2 | $K$-同核异能态折合阻碍度幂律：对于轴对称变形核中的 $K$-禁戒跃迁（$|\Delta K| > \lambda$），定义禁戒度 $\nu = |\Delta K| - \lambda$；实验折合阻碍度遵循经验定律 $f_\nu = (F_W)^{1/\nu} \approx 100$，即每增加一级 $K$-禁戒跃迁几率约降低两个数量级。 | experimental-criterion | direct | Ch. 5, 印刷 pp. 71–78 / PDF pp. 83–90 | false |
| JAIN-3 | $K$-混合与三轴形变指纹：当原子核具备非轴对称三轴形变（如 $A \sim 130$ 区奇奇核与偶偶核）时，轴对称性被破坏导致 $K$ 量子数强烈杂化（$K$-mixing）；此时理论上高 $\nu$ 禁戒跃迁的折合阻碍度发生异常塌缩（$f_\nu < 10$），成为识别三轴非对称性的重要能谱判据。 | author-interpretation | direct | Ch. 5, 印刷 pp. 88–95 / PDF pp. 100–107 | false |

## Competing Interpretations and Limitations

- **单 $j$ 近似与组态混合**：现实原子核中半满壳 Seniority 异能态的 $B(E2)$ 并不严格为零（通常残存 $0.01 \sim 0.1\text{ W.u.}$），系邻近亚壳层组态微弱混合与核芯极化（有效电荷 $e_{\text{eff}} > e$）所致；定量计算需借助全价空间球形壳模型或拟自旋对称性展开。
- **$K$-混合的多重微观来源**：$f_\nu$ 的下降除三轴形变外，还可能来自高转速下的强 Coriolis 混合或准粒子带交叉。单独观测到小 $f_\nu$ 不能作为三轴性的孤立充分条件，须与转动带交错参数 $S(I)$ 及 $\gamma$ 谱学多极比联合验证。

## Extracted Pages

- 印刷 pp. 31–45（PDF pp. 43–57）：Seniority 代数、Racah 分数母权系数、半满壳抛物线 $B(E2)$ 分布与异能态机制。
- 印刷 pp. 71–95（PDF pp. 83–107）：$K$-异能态选择定则、经验折合阻碍度 $f_\nu$ 与三轴形变 $K$-混合指纹。
